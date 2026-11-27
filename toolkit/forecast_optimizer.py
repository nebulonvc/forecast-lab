#!/usr/bin/env python3
"""Data-driven Forecast Method Optimization & Calibration Engine for Forecast Lab.

Academic foundations implemented (pure Python 3.11+ standard library, zero external deps):
1. Reference Class Forecasting & Hierarchical Empirical Bayes (Kahneman & Tversky 1979;
   Efron & Morris 1975; Gelman & Hill 2007 Dirichlet-Multinomial partial pooling).
2. Right-Censoring & Competing-Horizon Decomposition (Kalbfleisch & Prentice 2002):
   P(Y_5 | X, M, H_t0) = P(Decidable | X, M, H_t0) * P(Y_4 | Decidable, X, M, H_t0).
3. Feature-based Forecast Model Averaging & Method Meta-Learning (Montero-Manso,
   Athanasopoulos, Hyndman & Talagala 2020, FFORMA) via 2nd-order Newton Histogram
   Gradient-Boosted Decision Trees (Friedman 2001; Chen & Guestrin 2016; Ke et al. 2017).
4. Stratified Cochran-Mantel-Haenszel (CMH) & L2-Regularized GLMM deconfounded estimation
   of the 6 Signal Method Archetypes and 5 Noise Failure Traps, anchored on 146 works
   (10,745 forecasts, 7,522 decided outcomes, 2,942 excluded non-forecasts, and t_0
   macro-historical structural regimes from 1531 to 2026).
5. Log-Linear Opinion Pooling & Temperature Scaling Calibration (Genest & Zidek 1986;
   Bates & Granger 1969; Satopaa, Baron, Foster, Mellers, Tetlock & Ungar 2014;
   Gneiting & Raftery 2007 strictly proper scoring rules; Halawi et al. 2024).
"""
from __future__ import annotations

import argparse
import collections
import csv
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import random
import re
import sys
import time
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODEL_PATH = REPO_ROOT / "datasets" / "forecast_optimizer_model.json"
DEFAULT_BENCHMARK_PATH = REPO_ROOT / "datasets" / "optimization_benchmark.json"
DEFAULT_ATLAS_PATH = REPO_ROOT / "datasets" / "historical_tech_diffusion_atlas.json"

VERDICTS_5 = ["正确", "趋势符合", "部分符合", "错误", "暂无法判断"]
VERDICTS_4 = ["正确", "趋势符合", "部分符合", "错误"]

CANONICAL_DOMAINS = [
    "地缘政治与国际秩序",
    "宏观经济、金融与市场",
    "科技、商业与产业颠覆",
    "AI与奇点前沿",
    "人口、能源、资源与生态",
    "社会结构、制度、文化与教育",
    "科幻推演与乌托邦/反乌托邦",
]

DOMAIN_ALIASES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"AI|人工智能|大模型|算力|奇点|具身|机器人|自动驾驶|agent|llm|compute", re.I), "AI与奇点前沿"),
    (re.compile(r"能源|电力|电网|矿产|储能|锂|铜|石油|煤炭|气候|碳|人口|老龄|生育|农业|粮食|生态|energy|power|climate|demograph", re.I), "人口、能源、资源与生态"),
    (re.compile(r"地缘|国际|战争|军事|海权|大国|外交|制裁|关税|供应链安全|北约|台海|欧亚|geopolit|war|alliance|hegemon", re.I), "地缘政治与国际秩序"),
    (re.compile(r"宏观|经济|金融|利率|通胀|债务|汇率|央行|财政|货币|股市|房价|危机|macro|inflation|debt|bank|market", re.I), "宏观经济、金融与市场"),
    (re.compile(r"科技|商业|产业|企业|互联网|软件|硬件|芯片|半导体|平台|车企|制造|商业化|tech|industry|business|disrupt", re.I), "科技、商业与产业颠覆"),
    (re.compile(r"科幻|乌托邦|反乌托邦|永生|星际|utopia|sci-fi", re.I), "科幻推演与乌托邦/反乌托邦"),
    (re.compile(r"社会|制度|文化|教育|治理|宪政|法律|媒介|政治学|语言|social|institution|education|culture", re.I), "社会结构、制度、文化与教育"),
]

CANONICAL_ARCHETYPES = [
    "国际机构与政府智库",
    "政治家与战略实务者",
    "地缘与社科政治学者",
    "经济学家与金融投资人",
    "科技商业思想家与产业实践者",
    "古典思想家与科幻/乌托邦作家",
]

ARCHETYPE_ALIASES = {
    "institutional": "国际机构与政府智库",
    "think_tank": "国际机构与政府智库",
    "智库": "国际机构与政府智库",
    "机构": "国际机构与政府智库",
    "practitioner": "政治家与战略实务者",
    "strategist": "政治家与战略实务者",
    "战略实务": "政治家与战略实务者",
    "scholar": "地缘与社科政治学者",
    "academic": "地缘与社科政治学者",
    "学者": "地缘与社科政治学者",
    "economist": "经济学家与金融投资人",
    "investor": "经济学家与金融投资人",
    "投资人": "经济学家与金融投资人",
    "tech_builder": "科技商业思想家与产业实践者",
    "operator": "科技商业思想家与产业实践者",
    "产业实践": "科技商业思想家与产业实践者",
    "visionary": "古典思想家与科幻/乌托邦作家",
}

PUB_YEAR_FALLBACK = {
    "hamilton-madison-jay-federalist-papers-v5": 1788,
    "mill-considerations-on-representative-government-v5": 1861,
}

SIGNAL_METHODS: dict[str, dict[str, Any]] = {
    "constraint_ledger": {
        "name": "约束账本法",
        "en_name": "Physical & Fiscal Constraint Ledger",
        "summary": "把系统拆成现有存量、年度新增流量、在建产能周期、热力学/电网/财政硬边界，算清瓶颈与买单方。",
        "best_horizon_years": [1, 30],
        "default_counter_lens": "高价倒逼的替代技术路线跃迁（如钠电替代锂钴、页岩油替代传统油气）与杰文斯效率反弹效应",
        "exemplars": ["IEA《全球关键矿产展望2024》(66.7%严格/3.2%错)", "杰文斯《煤炭问题》(52.8%严格)", "UK GO-Science《智能基础设施2055》(74.1%严格)"],
        "leading_indicator_hint": "在建项目CapEx与投产排期、关键设备交付周期（如变压器/光刻机）、瓶颈环节库存与价差",
        "derivation_steps": [
            "① 盘点当前基期存量与统计分母基线",
            "② 核算已锁定在建产能/CapEx排期与物理交付时滞",
            "③ 标定热力学/电网/财政偿付硬瓶颈上限及买单方",
            "④ 扣除高价诱发的替代供给或效率反弹后锁定区间",
        ],
    },
    "institutional_incentive": {
        "name": "制度与激励结构法",
        "en_name": "Institutional & Incentive Veto Analysis",
        "summary": "不看口头宣示，拆解谁掌握否决权、谁承担改革代价、在位者受何种现行毛利结构与考核指标捆绑。",
        "best_horizon_years": [3, 35],
        "default_counter_lens": "新进入者绕开现行价值网的双轨破局（高端性能奇袭 vs 低端低成本渗透）及代际领导层更替",
        "exemplars": ["伯克《法国革命论》(48.4%严格/0%错)", "克里斯坦森《创新者的窘境》(41.2%严格)", "亨廷顿《第三波》文官控军"],
        "leading_indicator_hint": "在位者高毛利业务占比、预算与人事否决权归属、受损利益集团游说或合规壁垒强度",
        "derivation_steps": [
            "① 识别拥有实质预算/监管/人事否决权的关键行动者",
            "② 拆解在位者受捆绑的现行毛利结构、选票或KPI考核约束",
            "③ 推演受损利益方的合规阻挠或第三路径绕行反应",
            "④ 给出现行激励兼容条件下可落地的真实变化边界",
        ],
    },
    "geopolitical_chassis": {
        "name": "地缘底盘与权力均衡法",
        "en_name": "Geopolitical Chassis & Balance of Power",
        "summary": "锚定地理海道、缓冲带、人口经济体量与大国长期安全困境，分层评估军事、科技、金融底盘。",
        "best_horizon_years": [5, 50],
        "default_counter_lens": "内部财政透支承压 + 第三国转口贸易/供应链绕行对冲正面封锁",
        "exemplars": ["扎卡利亚《后美国世界》(59.0%严格/6.0%错)", "麦金德《民主的理想与现实》(57.9%严格)", "卡普兰《地理的复仇》(69.5%方向)"],
        "leading_indicator_hint": "军费与付息占财政收入比、关键海道航运保费、第三国转口贸易与FDI流向份额",
        "derivation_steps": [
            "① 锚定地理海道、陆海缓冲带与人口队列等慢变量底盘",
            "② 分层对比各方军事投送、产业制造与货币金融实力份额",
            "③ 评估同盟安全困境触发条件及第三国转口绕行弹性",
            "④ 区分长期实力均势演进方向与短期外交战术波动",
        ],
    },
    "functional_diffusion": {
        "name": "技术功能扩散链法",
        "en_name": "Functional Diffusion & Cost-Threshold Chain",
        "summary": "沿‘已有工程雏形 → 单位成本跨门槛 → 配套基础设施就位 → 组织工作流重塑’推演，押核心功能不押单一产品形态。",
        "best_horizon_years": [3, 40],
        "default_counter_lens": "能力参差（Jaggedness）、企业组织采用摩擦、监管合规时滞，严禁跳向‘消灭战争/政治大同’",
        "exemplars": ["戴维《航空器》(52.4%严格)", "威尔斯《预言》(52.2%严格)", "博斯特罗姆《超级智能》(47.7%严格/0%错)"],
        "leading_indicator_hint": "单位功能综合成本跨过盈亏平衡线比例、真实企业付费留存率（非试点POC）、配套基建就绪度",
        "derivation_steps": [
            "① 确认底层工程功能雏形在真实环境中已获验证（非纯概念）",
            "② 测算单位功能综合BOM/推理成本跨过商业替代门槛的时点",
            "③ 核查电力、通信、标准与合规责任等配套基础设施就绪周期",
            "④ 计入企业组织流程改造摩擦（押任务功能渗透，不押彻底消灭岗位或政治终局）",
        ],
    },
    "risk_fragility": {
        "name": "风险边界与反脆弱法",
        "en_name": "Tail Fragility & Asymmetric Payoff Audit",
        "summary": "不赌危机爆发的精确日期或点位，识别‘收益私有化、尾部爆雷公有化’的激励不对称与高杠杆脆弱结构。",
        "best_horizon_years": [2, 25],
        "default_counter_lens": "央行流动性兜底/债务展期拉长脆弱结构存续期（防止把结构脆弱误判为下季度必崩盘）",
        "exemplars": ["塔勒布《黑天鹅》(40.9%严格/0%错)", "达利欧《债务危机》(42.9%严格/0%错)", "基辛格三书(错1.2%)"],
        "leading_indicator_hint": "部门杠杆率与短债滚续覆盖比、隐性担保利差、集中度与单一节点断供敞口",
        "derivation_steps": [
            "① 定位杠杆堆积、期限错配或单一供应链节点集中度敞口",
            "② 拆解‘顺周期收益私有化、尾部损失外部化’的道德风险机制",
            "③ 评估央行扩表、财政展期或监管宽容能够延缓出清的时间缓冲",
            "④ 以脆弱性阈值与重定价方向替代拍脑袋崩盘精确日期",
        ],
    },
    "conditional_scenario": {
        "name": "多情景条件分支法",
        "en_name": "Explicit Conditional Scenario Branching",
        "summary": "拒绝单线宿命论，显式拆分独立可观测前提 A 的发生概率 P(A) 与条件结果 P(B|A)，为每条分支挂载触发阈值。",
        "best_horizon_years": [2, 30],
        "default_counter_lens": "严防循环论证（禁止把结果B未发生解释为前提A不够大），必须绑定事前可测的触发指标",
        "exemplars": ["OECD四份展望报告(51.8%严格/0%错)", "世界银行WDR系列(83.9%方向/2.3%错)", "荷兰WRR智库报告(52.4%严格)"],
        "leading_indicator_hint": "分支切换的显式政策/价格/技术里程碑触发器及各情景实时先验权重",
        "derivation_steps": [
            "① 分离独立于结果B之外的关键外生分岔前提 A 并评估先验权重 P(A)",
            "② 分别推演基准分支 P(B|A) 与受阻替代分支 P(B|¬A) 的定量区间",
            "③ 为每条情景分支绑定公开可查的领先切换触发器（Trigger）",
            "④ 事前冻结各分支证伪标准，杜绝事后挑有利分支自证正确",
        ],
    },
}

NOISE_TRAPS: dict[str, dict[str, Any]] = {
    "unanchored_hard_number": {
        "name": "无账本硬年份/极端数字外推",
        "cmh_effect_note": "同时间档控制下严格胜率平均下降 9.1pp，错误率上升 3.6pp",
        "remediation": "删除拍脑袋精确年份或每年固定增长率（如‘每年减半’‘超50%’）；改用由在建周期/存量周转率推导的区间阈值。",
    },
    "surpass_explicit_no_ledger": {
        "name": "无存量账本的‘超越/取代’定时断言",
        "cmh_effect_note": "同时间档控制下错误率飙升 +7.9pp，严格胜率下降 5.2pp",
        "remediation": "区分‘增量占比提升’与‘存量彻底取代/总量超越’，补齐双方存量基数、折旧周期与汇率/价格平减口径。",
    },
    "linear_rate_extrapolation": {
        "name": "把阶段性顺风外推为永久指数/单调直线",
        "cmh_effect_note": "同时间档控制下严格胜率下降 8.6pp，错误率上升 5.1pp",
        "remediation": "引入饱和S型曲线瓶颈（物理能耗、人口上限、回报递减、基数效应），明确写出斜率放缓的变轨条件。",
    },
    "cross_layer_utopian_jump": {
        "name": "跨层跳跃（从技术/经济可行直接跳到政治终局或消灭冲突）",
        "cmh_effect_note": "同时间档控制下严格胜率骤降 17.9pp（全库翻车最重灾区）",
        "remediation": "将预测降维锚定在‘技术功能渗透率、商业成本或具体制度安排’层，剥离关于终极政治大同或战争消失的断言。",
    },
    "compound_claim_bundling": {
        "name": "多目标复合捆绑承诺（A且B同时成立）",
        "cmh_effect_note": "同时间档控制下严格胜率下降 6.7pp（任一分项偏差即降级为部分符合）",
        "remediation": "将复合命题拆分为独立的原子预测卡：把‘方向演进’‘具体技术路线’与‘次生社会后果’分立记账。",
    },
}

METHOD_PATTERNS: dict[str, re.Pattern[str]] = {
    "constraint_ledger": re.compile(
        r"存量|流量|产能|装机|储量|产量|能耗|电力|电网|赤字|债务|付息|财政|预算|人口结构|老龄化|队列|生育率|建设周期|排期|供应链|矿产|精炼|成本曲线|边际成本|热力学|物理边界|账本|"
        r"capacity|supply|reserves|stock|flow|fiscal|debt|deficit|demographic|cohort|fertility|grid|electricity|mineral|capex|bottleneck|constraint|cost curve",
        re.I,
    ),
    "institutional_incentive": re.compile(
        r"激励|否决权|利益集团|毛利|价值网|在位者|官僚|政体|宪政|产权|税收|军纪|议会|选举|游说|监管|委托代理|制度|"
        r"incentive|incumbent|margin|value network|veto|bureaucrac|institution|property right|parliament|coalition|regulator|constituenc|christensen",
        re.I,
    ),
    "geopolitical_chassis": re.compile(
        r"海道|海峡|陆权|海权|缓冲|地缘|均势|霸权|同盟|核威慑|大国|安全困境|欧亚|腹地|边界|战略|版图|"
        r"geopolit|maritime|heartland|eurasia|buffer|balance of power|hegemon|alliance|deterrence|great power|strait|geography",
        re.I,
    ),
    "functional_diffusion": re.compile(
        r"扩散|普及|渗透率|商业化|基础设施|网络效应|平台|自动化|数字化|替代传统|工作流|应用|终端|通信|算力|协议|"
        r"diffusion|adoption|penetration|infrastructure|commercial|network effect|automation|digital|workflow|protocol|appliance|computing",
        re.I,
    ),
    "risk_fragility": re.compile(
        r"脆弱|尾部|黑天鹅|不对称|危机|泡沫|违约|挤兑|杠杆|风险|失衡|崩溃|冲击|道德风险|兜底|反脆弱|"
        r"fragil|tail risk|asymmetric|bubble|default|leverage|contagion|bailout|moral hazard|shock|crisis|imbalance",
        re.I,
    ),
    "conditional_scenario": re.compile(
        r"如果|若|倘若|只要|除非|前提|情景|取决于|一旦|倘使|条件下|分支|"
        r"\bif\b|\bunless\b|\bprovided\b|\bscenario\b|\bdepend|\bcontingent|\bin the event",
        re.I,
    ),
}

STRUCTURAL_PATTERNS: dict[str, re.Pattern[str]] = {
    "absolutist_hedgehog": re.compile(
        r"必然|必将|绝不可能|永远不会|彻底取代|完全消灭|彻底消亡|无论.*都|注定|不可逆转|"
        r"\binevitabl|\bno matter what\b|\bcompletely replace|\beradicate\b|\bdoomed to\b|\bforever\b|\bnever again\b",
        re.I,
    ),
    "unanchored_hard_number": re.compile(
        r"每年.*%|翻一番|翻倍|减半|\d+(?:\.\d+)?\s*%|到\s*20\d\d\s*年.*超|\d+倍|"
        r"\b\d+(?:\.\d+)?\s*%|\bdouble\b|\bhalve\b|\bsurpass\b.*\bby (?:19|20)\d\d",
        re.I,
    ),
    "cross_layer_utopian_jump": re.compile(
        r"世界政府|消灭战争|人类大同|乌托邦|永生|不死|不再有战争|政治终局|永久和平|阶级消亡|货币消亡|国家消亡|"
        r"world government|abolish war|end of war|immortal|utopia|perpetual peace|abolish money|withering away",
        re.I,
    ),
    "linear_rate_extrapolation": re.compile(
        r"每年.*%|每年减半|每年翻|指数增长|几何级数|延续目前的速度|照此速度|一直增长|"
        r"\bexponential|\bevery year\b.*\d+%|\bgeometric\b|\bdouble every\b",
        re.I,
    ),
    "fox_hedging": re.compile(
        r"可能|很可能|或许|倾向|往往|大约|区间|比重|份额|部分|有望|未必|至少|不超过|"
        r"\blikely\b|\bmay\b|\bmight\b|\btend to\b|\bshare\b|\bproportion\b|\bprobable\b|\bat least\b|\bno more than\b",
        re.I,
    ),
    "compound_claim": re.compile(
        r"同时|并且|不仅.*而且|既.*又|以及.*并|"
        r"\bboth\b.*\band\b|;\s*\w+",
        re.I,
    ),
    "comparative_surpass": re.compile(
        r"超过|超越|取代|跃居第一|最大|霸主|主导|淘汰|消亡|"
        r"\bsurpass\b|\bovertake\b|\breplace\b|\bdisplace\b|\blargest\b|\bdominate\b|\bobsolete\b",
        re.I,
    ),
    "measurable_metric": re.compile(
        r"GDP|人口|比重|占比|份额|增长率|通胀|利率|失业率|产量|发电|装机|销量|渗透率|贸易额|顺差|逆差|军费|预算|赤字|寿命|生育率|能耗|成本|价格|百分点|台数|留存率|"
        r"\bgdp\b|\bshare\b|\bpercent|\brate\b|\binflation\b|\boutput\b|\bsales\b|\btrade\b|\bprice\b|\bcost\b|\bpopulation\b|\bemployment\b",
        re.I,
    ),
    "authoritative_source_named": re.compile(
        r"统计局|央行|美联储|世行|世界银行|IMF|OECD|IEA|EIA|LBNL|BLS|WTO|联合国|FAO|年报|财报|海关|人口普查|"
        r"world bank|census|bureau of labor|central bank|federal reserve|annual report|official statistics",
        re.I,
    ),
    "abstract_normative_or_utopian": re.compile(
        r"美德|灵魂|幸福|正义|自由的真谛|人性|天命|道德复兴|精神危机|乌托邦|大同|永恒|救赎|"
        r"\bvirtue\b|\bsoul\b|\bhappiness\b|\bhuman nature\b|\bdestiny\b|\bmoral\b|\bsalvation\b|\butopia\b|\bliberty\b",
        re.I,
    ),
    "normative_should": re.compile(
        r"应当|应该|必须采取|亟需|呼吁|建议政府|唯有如此才能|"
        r"\bshould\b|\bmust adopt\b|\bought to\b|\bwe need to\b|\bimperative that\b",
        re.I,
    ),
    "causal_mechanism_connector": re.compile(
        r"因为|由于|得益于|受制于|源于|导致|迫使|倒逼|激励|瓶颈|"
        r"\bbecause\b|\bdue to\b|\bdriven by\b|\bconstrained by\b|\bforce[sd]?\b|\bbottleneck\b",
        re.I,
    ),
    "counter_caveat": re.compile(
        r"除非|但若|然而|前提是|例外|受限于|不排除|倘若没有|反校验|不包括|"
        r"\bunless\b|\bhowever\b|\bprovided that\b|\bexcept\b|\bcaveat\b|\bsubject to\b|\bexclud",
        re.I,
    ),
    "heavy_atom_or_regulated": re.compile(
        r"机器人|自动驾驶|无人驾驶|汽车|电网|电力|变压器|核电|储能|矿产|晶圆|工厂|量产线|航空|飞机|火箭|临床|新药|基因|纳米|脑机|"
        r"\brobot|\bautonomous|\bvehicle|\bgrid\b|\belectricity|\bnuclear|\bfactory|\bmanufactur|\baircraft|\baviation|\bclinical|\bdrug|\bnanotech|\bbiotech",
        re.I,
    ),
    "stock_replacement_scope": re.compile(
        r"彻底取代|完全取代|取代.*工作|取代.*岗位|淘汰|保有量|存量|总发电量|全部.*替换为|不再有|"
        r"\breplace\b.*\bjobs?\b|\bfleet\b|\binstalled base\b|\bobsolete\b|\beliminate\b",
        re.I,
    ),
}


def bass_time_between_shares(p: float, q: float, s0: float, s1: float, stock_inertia: float = 1.0) -> float:
    """Analytical inverse of Bass (1969) S-curve F(t) = (1 - exp(-(p+q)t)) / (1 + (q/p)exp(-(p+q)t))
    giving exact years required to diffuse from baseline share s0 to target share s1.
    """
    s0_c = min(max(float(s0), 0.005), 0.95)
    s1_c = min(max(float(s1), s0_c + 0.01), 0.98)
    qp = q / max(p, 1e-6)
    t0 = math.log((1.0 + qp * s0_c) / (1.0 - s0_c)) / (p + q)
    t1 = math.log((1.0 + qp * s1_c) / (1.0 - s1_c)) / (p + q)
    return max(0.2, (t1 - t0) * max(stock_inertia, 1.0))


def bass_share_after_years(p: float, q: float, s0: float, delta_years: float, speedup: float = 1.0, stock_inertia: float = 1.0) -> float:
    """Analytical Bass (1969) forward projection from current share s0 over delta_years under speedup factor."""
    s0_c = min(max(float(s0), 0.005), 0.95)
    qp = q / max(p, 1e-6)
    t0 = math.log((1.0 + qp * s0_c) / (1.0 - s0_c)) / (p + q)
    t_eff = t0 + max(0.0, float(delta_years)) * max(speedup, 0.1) / max(stock_inertia, 1.0)
    eb_term = math.exp(-(p + q) * t_eff)
    return min(max((1.0 - eb_term) / (1.0 + qp * eb_term), s0_c), 0.99)


def parse_target_share(text: str, s0: float = 0.04) -> float | None:
    """Extract target penetration/replacement fraction in (0, 1) if stated in text."""
    # Check percentage-point delta first (e.g. '提高至少2.0个百分点' -> s0 + 0.02, NOT 35%!)
    m_pp = re.search(r"(\d+(?:\.\d+)?)\s*个?百分点", text)
    if m_pp:
        delta_pp = float(m_pp.group(1)) / 100.0
        if 0.005 <= delta_pp <= 0.80:
            return min(s0 + delta_pp, 0.95)
    m_pct = re.findall(r"(\d+(?:\.\d+)?)\s*%", text)
    for raw in m_pct:
        val = float(raw)
        if 5.0 <= val <= 100.0 and not re.search(r"每年.*%|增长\s*" + re.escape(raw), text):
            return min(val / 100.0, 0.95)
    if re.search(r"一半|半数|过半|\bhalf\b|\bmajority\b", text, re.I):
        return 0.50
    if re.search(r"彻底取代|完全取代|全面普及|普遍采用|主导|\bcompletely replace|\bdominate\b|\bubiquitous\b", text, re.I):
        return 0.60
    return None


def normalize_domain(domain: str) -> str:
    d = (domain or "").strip()
    if d in CANONICAL_DOMAINS:
        return d
    for pat, target in DOMAIN_ALIASES:
        if pat.search(d):
            return target
    return "科技、商业与产业颠覆"


def normalize_archetype(archetype: str) -> str:
    a = (archetype or "").strip()
    if a in CANONICAL_ARCHETYPES:
        return a
    low = a.lower()
    for k, target in ARCHETYPE_ALIASES.items():
        if k in low:
            return target
    return "国际机构与政府智库"


def window_to_horizon_bucket(window_years: float) -> str:
    w = max(0.5, float(window_years))
    if w <= 3.5:
        return "0–3年(超短窗)"
    if w <= 9.5:
        return "4–9年(中短窗)"
    if w <= 19.5:
        return "10–19年(中长窗)"
    if w <= 39.5:
        return "20–39年(长周期)"
    if w <= 99.5:
        return "40–99年(跨代)"
    return "≥100年(跨世纪)"


def historical_regime_features(year: int) -> dict[str, float]:
    """Point-in-time macro-historical regime strictly known on or before forecast year t_0.

    Grounded in Maddison Project global growth chronology, Reinhart-Rogoff inflation/debt
    crisis regimes, Perez (2002) techno-economic irruption waves, and systemic polarity eras.
    """
    if year < 1850:
        data_infra = 0.05
    elif year < 1930:
        data_infra = 0.20
    elif year < 1970:
        data_infra = 0.45
    elif year < 2000:
        data_infra = 0.75
    else:
        data_infra = 1.00

    if 1914 <= year <= 1945:
        geo_stress = 0.95
    elif 1789 <= year <= 1815:
        geo_stress = 0.85
    elif 1989 <= year <= 1993:
        geo_stress = 0.75
    elif year >= 2016:
        geo_stress = 0.80
    elif 2001 <= year <= 2015:
        geo_stress = 0.55
    elif 1946 <= year <= 1988:
        geo_stress = 0.65
    else:
        geo_stress = 0.45

    if (1793 <= year <= 1815) or (1918 <= year <= 1923) or (1968 <= year <= 1982) or (2020 <= year <= 2024):
        scarcity_shock = 0.90
    elif (2008 <= year <= 2012) or (1929 <= year <= 1939):
        scarcity_shock = 0.75
    else:
        scarcity_shock = 0.25

    if (1895 <= year <= 1912) or (1994 <= year <= 2000) or (2022 <= year <= 2028):
        tech_frenzy = 0.90
    elif (1960 <= year <= 1970) or (2013 <= year <= 2021):
        tech_frenzy = 0.65
    else:
        tech_frenzy = 0.25

    if year < 1820:
        trailing_gdp_pc_growth = 0.15
    elif year < 1870:
        trailing_gdp_pc_growth = 0.55
    elif year < 1914:
        trailing_gdp_pc_growth = 1.30
    elif year < 1946:
        trailing_gdp_pc_growth = 0.85
    elif year < 1973:
        trailing_gdp_pc_growth = 2.90
    elif year < 1995:
        trailing_gdp_pc_growth = 1.45
    elif year < 2008:
        trailing_gdp_pc_growth = 2.35
    elif year < 2020:
        trailing_gdp_pc_growth = 1.85
    else:
        trailing_gdp_pc_growth = 1.70

    return {
        "data_infra": data_infra,
        "geo_stress": geo_stress,
        "scarcity_shock": scarcity_shock,
        "tech_frenzy": tech_frenzy,
        "trailing_growth": round(trailing_gdp_pc_growth / 3.0, 4),
        "is_pre_modern": 1.0 if year < 1900 else 0.0,
        "is_modern_post2000": 1.0 if year >= 2000 else 0.0,
    }


def parse_explicit_span(text: str, pub_year: int) -> float | None:
    """Extract target horizon distance (in years from pub_year) from explicit horizon expressions."""
    range_m = re.findall(r"(?:18|19|20|21)\d{2}", text)
    years = [int(y) for y in range_m]
    future_years = [y for y in years if pub_year < y <= pub_year + 300]
    if future_years:
        # Use max endpoint for ranges like '2026-2030', min endpoint if multiple distinct mentions
        if len(future_years) == 2 and future_years[1] - future_years[0] <= 30:
            return float(future_years[1] - pub_year)
        return float(min(future_years) - pub_year)
    m_num = re.search(r"(\d+)\s*(?:年|years?)", text, re.I)
    if m_num:
        val = int(m_num.group(1))
        if 1 <= val <= 200:
            return float(val)
    zh_nums = {"三": 3.0, "五": 5.0, "十": 10.0, "十五": 15.0, "二十": 20.0, "三十": 30.0, "五十": 50.0, "百": 100.0}
    for zk, zv in sorted(zh_nums.items(), key=lambda x: -len(x[0])):
        if f"{zk}年" in text:
            return zv
    if re.search(r"\bdecade\b", text, re.I):
        return 10.0
    if re.search(r"two decades|twenty years", text, re.I):
        return 20.0
    if re.search(r"半个世纪|half a century", text, re.I):
        return 50.0
    if re.search(r"本世纪末|end of the century", text, re.I):
        century_end = ((pub_year // 100) + 1) * 100
        return float(max(5, century_end - pub_year))
    if re.search(r"近期|不久的将来|near future|short term|soon", text, re.I):
        return 3.0
    return None


def compute_pit_priors_fast(train_forecasts: list[dict[str, Any]], target_recs: list[dict[str, Any]]) -> list[dict[str, float]]:
    """O(N + M) strictly causal expanding-window historical base rates (only books with pub_year <= t_0 - 10)."""
    by_year_global: dict[int, list[float]] = collections.defaultdict(lambda: [0.0] * 5)
    by_year_domain: dict[tuple[str, int], list[float]] = collections.defaultdict(lambda: [0.0] * 5)
    years_set = set()
    for tr in train_forecasts:
        y = int(tr["pub_year"])
        yi = VERDICTS_5.index(tr["verdict"])
        by_year_global[y][yi] += 1.0
        by_year_domain[(tr["domain"], y)][yi] += 1.0
        years_set.add(y)

    sorted_years = sorted(years_set)
    # Build prefix sums over sorted_years
    g_prefix: dict[int, list[float]] = {}
    d_prefix: dict[tuple[str, int], list[float]] = {}
    running_g = [1.0] * 5  # Weak symmetric Dirichlet(1,...,1) prior before 1531
    running_d: dict[str, list[float]] = {dom: [0.0] * 5 for dom in CANONICAL_DOMAINS}

    for y in sorted_years:
        add_g = by_year_global[y]
        running_g = [running_g[c] + add_g[c] for c in range(5)]
        g_prefix[y] = list(running_g)
        for dom in CANONICAL_DOMAINS:
            add_d = by_year_domain.get((dom, y))
            if add_d:
                running_d[dom] = [running_d[dom][c] + add_d[c] for c in range(5)]
            d_prefix[(dom, y)] = list(running_d[dom])

    import bisect

    out: list[dict[str, float]] = []
    kappa = 30.0
    for r in target_recs:
        cutoff_y = int(r["pub_year"]) - 10
        pos = bisect.bisect_right(sorted_years, cutoff_y) - 1
        if pos < 0:
            g_cnt = [1.0] * 5
            d_cnt = [0.0] * 5
        else:
            y_key = sorted_years[pos]
            g_cnt = g_prefix[y_key]
            d_cnt = d_prefix.get((r["domain"], y_key), [0.0] * 5)
        gs = sum(g_cnt)
        gp = [c / gs for c in g_cnt]
        ds = sum(d_cnt)
        post = [(d_cnt[c] + kappa * gp[c]) / (ds + kappa) for c in range(5)]
        dec = max(1.0 - post[4], 1e-6)
        out.append({
            "strict": round(post[0] / dec, 5),
            "dir": round((post[0] + post[1]) / dec, 5),
            "err": round(post[3] / dec, 5),
            "unres": round(post[4], 5),
        })
    return out


def extract_features(
    rec: dict[str, Any],
    pit_prior: dict[str, float] | None = None,
    method_override: dict[str, float] | None = None,
    trap_override: dict[str, float] | None = None,
) -> dict[str, float]:
    """Extract strictly ex-ante features observable at forecast creation time t_0."""
    full_txt = f"{rec.get('quote', '')} {rec.get('claim', '')} {rec.get('time_text', '')} {rec.get('condition_text', '')} {rec.get('ex_method', '')} {rec.get('scope_text', '')}"
    claim_only = f"{rec.get('quote', '')} {rec.get('claim', '')} {rec.get('condition_text', '')}"
    pub_year = int(rec.get("pub_year", 2026))
    win = max(1.0, float(rec.get("window_years", 5.0)))
    is_exp = 1.0 if rec.get("horizon_source") == "explicit" else 0.0
    span = rec.get("explicit_span_years")
    if span is None and is_exp > 0.5:
        span = parse_explicit_span(f"{rec.get('time_text', '')} {rec.get('quote', '')} {rec.get('claim', '')}", pub_year)
    eff_span = float(span) if span is not None else win

    hist = historical_regime_features(pub_year)
    m_scores = {k: (1.0 if pat.search(full_txt) else 0.0) for k, pat in METHOD_PATTERNS.items()}
    cond_txt = (rec.get("condition_text") or "").strip()
    if cond_txt and "无明确条件" not in cond_txt and "无附加" not in cond_txt:
        m_scores["conditional_scenario"] = 1.0
    if method_override:
        m_scores.update(method_override)

    s_scores = {k: (1.0 if pat.search(claim_only) else 0.0) for k, pat in STRUCTURAL_PATTERNS.items()}
    if rec.get("scope_text") and STRUCTURAL_PATTERNS["authoritative_source_named"].search(rec["scope_text"]):
        s_scores["authoritative_source_named"] = 1.0
    if trap_override:
        s_scores.update(trap_override)

    has_structural_anchor = max(
        m_scores["constraint_ledger"],
        m_scores["institutional_incentive"],
        m_scores["geopolitical_chassis"],
    )
    unanchored_explicit = is_exp * (1.0 - has_structural_anchor)
    anchored_explicit = is_exp * has_structural_anchor
    unanchored_number = s_scores["unanchored_hard_number"] * (1.0 - m_scores["constraint_ledger"])
    anchored_number = s_scores["unanchored_hard_number"] * m_scores["constraint_ledger"]

    log_win = math.log1p(win) / 5.0
    log_span = math.log1p(eff_span) / 5.0
    span_exceeds_window = 1.0 if (span is not None and float(span) > win) else 0.0
    short_window = 1.0 if win <= 3.5 else 0.0
    med_short_window = 1.0 if 3.5 < win <= 9.5 else 0.0
    mid_long_window = 1.0 if 9.5 < win <= 39.5 else 0.0
    ultra_long_window = 1.0 if win > 39.5 else 0.0

    feats: dict[str, float] = {
        "bias": 1.0,
        "log_win": log_win,
        "log_span": log_span,
        "is_explicit": is_exp,
        "has_parsed_span": 1.0 if span is not None else 0.0,
        "span_exceeds_window": span_exceeds_window,
        "short_window": short_window,
        "med_short_window": med_short_window,
        "mid_long_window": mid_long_window,
        "ultra_long_window": ultra_long_window,
        "is_classical": float(rec.get("is_classical_philosophy", 0.0)),
        "text_len": min(len(rec.get("claim", "") or rec.get("quote", "")), 300) / 300.0,
        **{f"hist_{k}": v for k, v in hist.items()},
        **{f"m_{k}": v for k, v in m_scores.items()},
        **{f"s_{k}": v for k, v in s_scores.items()},
        # Theory-driven non-linear interactions
        "ix_unanchored_explicit": unanchored_explicit,
        "ix_anchored_explicit": anchored_explicit,
        "ix_unanchored_number": unanchored_number,
        "ix_anchored_number": anchored_number,
        "ix_surpass_explicit_no_ledger": s_scores["comparative_surpass"] * is_exp * (1.0 - m_scores["constraint_ledger"]),
        "ix_frenzy_hedgehog": hist["tech_frenzy"] * s_scores["absolutist_hedgehog"],
        "ix_scarcity_hedgehog": hist["scarcity_shock"] * s_scores["absolutist_hedgehog"],
        "ix_short_tech": short_window * hist["tech_frenzy"],
        "ix_long_explicit": ultra_long_window * is_exp,
        "ix_measurable_x_infra": s_scores["measurable_metric"] * hist["data_infra"],
        "ix_abstract_x_long": s_scores["abstract_normative_or_utopian"] * ultra_long_window,
        "ix_heavy_short_explicit_no_ledger": (
            s_scores["heavy_atom_or_regulated"] * (short_window + med_short_window) * is_exp * (1.0 - m_scores["constraint_ledger"])
        ),
        "ix_stock_replace_short": s_scores["stock_replacement_scope"] * short_window,
    }
    if pit_prior is not None:
        feats["pit_strict_rate"] = pit_prior["strict"]
        feats["pit_dir_rate"] = pit_prior["dir"]
        feats["pit_err_rate"] = pit_prior["err"]
        feats["pit_unres_rate"] = pit_prior["unres"]

    dom = normalize_domain(rec.get("domain", ""))
    aut = normalize_archetype(rec.get("author_type", ""))
    feats[f"dom_{dom}"] = 1.0
    feats[f"aut_{aut}"] = 1.0
    return feats


def load_training_corpus(repo_root: Path = REPO_ROOT) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Load all 10,745 forecasts + 2,942 non-forecasts across 146 works + 330 curated gold cases."""
    summary_csv = repo_root / "datasets" / "all_cases_summary.csv"
    with open(summary_csv, encoding="utf-8-sig") as f:
        summary_rows = list(csv.DictReader(f))

    forecasts: list[dict[str, Any]] = []
    nonforecasts: list[dict[str, Any]] = []

    for r in summary_rows:
        slug = r["slug"]
        cdir = repo_root / "cases" / slug
        batch = r["批次口径"]
        if r["出版年"].isdigit():
            pub_year = int(r["出版年"])
        elif slug in PUB_YEAR_FALLBACK:
            pub_year = PUB_YEAR_FALLBACK[slug]
        else:
            pub_year = int(json.loads((cdir / "config.json").read_text(encoding="utf-8"))["publication_year_proxy"])
        cutoff_year = int(r["截止日"][:4])
        window_years = max(1, cutoff_year - pub_year)

        claims_map: dict[str, dict[str, Any]] = {}
        with open(cdir / "data" / "claims.jsonl", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    obj = json.loads(line)
                    claims_map[obj["id"]] = obj

        s = json.loads((cdir / "output" / "summary.json").read_text(encoding="utf-8"))
        raw_items: list[tuple[str, str, str | None, dict[str, Any], dict[str, Any]]] = []
        if s["forecast_n"] == int(r["预测数"]) and s["decided_n"] == int(r["可判定数"]):
            for cid, obj in claims_map.items():
                a = obj.get("assessment")
                if not a:
                    continue
                if a.get("inclusion") == "forecast":
                    dv = "趋势符合" if (a.get("verdict") == "部分符合" and a.get("trend_aligned")) else a.get("verdict")
                    raw_items.append((cid, "forecast", dv, obj, a))
                elif a.get("inclusion") == "nonforecast":
                    raw_items.append((cid, "nonforecast", None, obj, a))
        elif batch in ("v4_early", "v5_early_verify"):
            p = (
                cdir / "output" / "verify-manual-audit-2026-11-14-v2" / "results.slim.jsonl"
                if batch == "v4_early"
                else cdir / "output" / "verify-final" / "results.slim.jsonl"
            )
            with open(p, encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line)
                    cid = obj.get("claim_id") or obj.get("id")
                    base_obj = claims_map.get(cid, obj)
                    a = obj.get("assessment") or {}
                    if obj.get("nonforecast") or a.get("nonforecast") or a.get("inclusion") == "nonforecast":
                        raw_items.append((cid, "nonforecast", None, base_obj, obj))
                        continue
                    dv = obj.get("display_verdict")
                    if not dv:
                        dv = "趋势符合" if (a.get("verdict") == "部分符合" and a.get("trend_aligned")) else a.get("verdict")
                    if dv in VERDICTS_5:
                        raw_items.append((cid, "forecast", dv, base_obj, obj))
        elif batch == "v5_pr18_pr24_manual":
            p = cdir / "output" / "manual-final" / "results.manual.jsonl"
            with open(p, encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line)
                    cid = obj.get("claim_id") or obj.get("id")
                    base_obj = claims_map.get(cid, obj)
                    if obj.get("nonforecast"):
                        raw_items.append((cid, "nonforecast", None, base_obj, obj))
                        continue
                    dv = obj.get("display_verdict") or obj.get("verdict")
                    if dv in VERDICTS_5:
                        raw_items.append((cid, "forecast", dv, base_obj, obj))

        for cid, kind, dv, base_obj, eval_obj in raw_items:
            ext = base_obj.get("extraction_v2") or {}
            quote = base_obj.get("quote") or eval_obj.get("quote") or ""
            claim_txt = ext.get("expanded_claim") or ext.get("claim") or base_obj.get("claim") or eval_obj.get("claim") or ""
            time_txt = ext.get("horizon") or ext.get("time_text") or base_obj.get("time_text") or ""
            cond_txt = ext.get("condition_text") or base_obj.get("condition_text") or ""
            ex_method = ext.get("method") or base_obj.get("method") or ""
            h_src = eval_obj.get("horizon_source") or ext.get("horizon_source") or ""
            if not h_src:
                h_src = "explicit" if time_txt.strip() else "implicit_publication_to_cutoff"

            rec = {
                "case_slug": slug,
                "book": r["书名"],
                "author": r["作者"],
                "domain": r["领域"],
                "author_type": r["作者类型"],
                "batch": batch,
                "pub_year": pub_year,
                "window_years": window_years,
                "horizon_bucket": r["时间跨度分档"],
                "is_classical_philosophy": 1.0 if batch == "v5_acceptance_zip" else 0.0,
                "claim_id": cid,
                "kind": kind,
                "verdict": dv,
                "quote": quote,
                "claim": claim_txt,
                "time_text": time_txt,
                "condition_text": cond_txt,
                "ex_method": ex_method,
                "horizon_source": h_src,
            }
            if kind == "forecast":
                forecasts.append(rec)
            else:
                nonforecasts.append(rec)

    curated_csv = repo_root / "datasets" / "curated_330_forecasts.csv"
    with open(curated_csv, encoding="utf-8-sig") as f:
        curated_330 = list(csv.DictReader(f))

    return forecasts, nonforecasts, curated_330


# ---------------------------------------------------------------------------
# Proper Scoring Rules & Calibration Metrics
# ---------------------------------------------------------------------------

def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def brier_multiclass(probs_list: list[list[float]], y_indices: list[int], k: int) -> float:
    total = 0.0
    for p, y in zip(probs_list, y_indices):
        for c in range(k):
            target = 1.0 if c == y else 0.0
            total += (p[c] - target) ** 2
    return total / max(len(y_indices), 1)


def logloss_multiclass(probs_list: list[list[float]], y_indices: list[int]) -> float:
    total = 0.0
    for p, y in zip(probs_list, y_indices):
        prob = max(min(p[y], 1.0 - 1e-12), 1e-12)
        total -= math.log(prob)
    return total / max(len(y_indices), 1)


def rps_ordinal(probs_list: list[list[float]], y_indices: list[int], k: int) -> float:
    total = 0.0
    for p, y in zip(probs_list, y_indices):
        cum_p = 0.0
        s = 0.0
        for c in range(k - 1):
            cum_p += p[c]
            cum_y = 1.0 if y <= c else 0.0
            s += (cum_p - cum_y) ** 2
        total += s / (k - 1)
    return total / max(len(y_indices), 1)


def expected_calibration_error(probs_pos: list[float], y_bin: list[int], bins: int = 10) -> float:
    buckets: list[list[tuple[float, int]]] = [[] for _ in range(bins)]
    for p, y in zip(probs_pos, y_bin):
        idx = min(max(int(p * bins), 0), bins - 1)
        buckets[idx].append((p, y))
    ece = 0.0
    n = max(len(y_bin), 1)
    for b in buckets:
        if not b:
            continue
        avg_p = sum(x[0] for x in b) / len(b)
        avg_y = sum(x[1] for x in b) / len(b)
        ece += (len(b) / n) * abs(avg_p - avg_y)
    return ece


def log_linear_pool(
    probs_list_of_models: list[list[list[float]]],
    weights: tuple[float, ...] | list[float],
    temperature: float = 1.0,
) -> list[list[float]]:
    """Log-Linear Opinion Pool with Temperature Calibration."""
    n = len(probs_list_of_models[0])
    k = len(probs_list_of_models[0][0])
    out: list[list[float]] = []
    for i in range(n):
        logits = [0.0] * k
        for m_idx, w in enumerate(weights):
            if w == 0.0:
                continue
            p_vec = probs_list_of_models[m_idx][i]
            for c in range(k):
                logits[c] += w * math.log(max(p_vec[c], 1e-12))
        logits = [z / temperature for z in logits]
        out.append(softmax(logits))
    return out


# ---------------------------------------------------------------------------
# Statistical & Machine Learning Estimators (Zero-Dependency Stdlib)
# ---------------------------------------------------------------------------

class HierarchicalEmpiricalBayes:
    """Multi-level Dirichlet-Multinomial Partial Pooling across Reference Classes."""

    def __init__(self, n_classes: int = 5, kappas: tuple[float, float, float] = (15.0, 25.0, 35.0)):
        self.k = n_classes
        self.kappas = list(kappas)
        self.p0: list[float] = [1.0 / n_classes] * n_classes
        self.l1: dict[str, list[int]] = {}
        self.l2: dict[str, list[int]] = {}
        self.l3: dict[str, list[int]] = {}

    @staticmethod
    def _k1(r: dict[str, Any]) -> str:
        return f"{r['horizon_bucket']}|{int(r.get('is_classical_philosophy', 0))}"

    @staticmethod
    def _k2(r: dict[str, Any]) -> str:
        return f"{r['horizon_bucket']}|{normalize_domain(r['domain'])}|{normalize_archetype(r['author_type'])}"

    @staticmethod
    def _k3(r: dict[str, Any]) -> str:
        return f"{r['horizon_bucket']}|{normalize_domain(r['domain'])}|{normalize_archetype(r['author_type'])}|{r['horizon_source']}"

    def fit(self, recs: list[dict[str, Any]], y_list: list[int]) -> "HierarchicalEmpiricalBayes":
        k = self.k
        g = [0] * k
        l1: dict[str, list[int]] = collections.defaultdict(lambda: [0] * k)
        l2: dict[str, list[int]] = collections.defaultdict(lambda: [0] * k)
        l3: dict[str, list[int]] = collections.defaultdict(lambda: [0] * k)
        for r, y in zip(recs, y_list):
            g[y] += 1
            l1[self._k1(r)][y] += 1
            l2[self._k2(r)][y] += 1
            l3[self._k3(r)][y] += 1
        tot = max(sum(g), 1)
        self.p0 = [c / tot for c in g]
        self.l1 = dict(l1)
        self.l2 = dict(l2)
        self.l3 = dict(l3)
        return self

    def predict_one(self, r: dict[str, Any]) -> tuple[list[float], dict[str, Any]]:
        k1, k2, k3 = self.kappas
        c1 = self.l1.get(self._k1(r), [0] * self.k)
        n1 = sum(c1)
        p1 = [(c1[c] + k1 * self.p0[c]) / (n1 + k1) for c in range(self.k)]

        c2 = self.l2.get(self._k2(r), [0] * self.k)
        n2 = sum(c2)
        p2 = [(c2[c] + k2 * p1[c]) / (n2 + k2) for c in range(self.k)]

        c3 = self.l3.get(self._k3(r), [0] * self.k)
        n3 = sum(c3)
        p3 = [(c3[c] + k3 * p2[c]) / (n3 + k3) for c in range(self.k)]
        meta = {
            "horizon_bucket": r["horizon_bucket"],
            "stratum_n_horizon": n1,
            "stratum_n_domain_archetype": n2,
            "stratum_n_exact_cell": n3,
            "raw_exact_cell_counts": dict(zip(VERDICTS_5[: self.k], c3)),
        }
        return p3, meta

    def predict_proba(self, recs: list[dict[str, Any]]) -> list[list[float]]:
        return [self.predict_one(r)[0] for r in recs]

    def to_dict(self) -> dict[str, Any]:
        return {"k": self.k, "kappas": self.kappas, "p0": self.p0, "l1": self.l1, "l2": self.l2, "l3": self.l3}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "HierarchicalEmpiricalBayes":
        obj = cls(n_classes=d["k"], kappas=tuple(d["kappas"]))
        obj.p0 = d["p0"]
        obj.l1 = d["l1"]
        obj.l2 = d["l2"]
        obj.l3 = d["l3"]
        return obj


class MultinomialLogReg:
    """L2-Regularized Multinomial Logistic Regression (GLMM / MaxEnt)."""

    def __init__(self, n_classes: int, l2: float = 3.0, lr: float = 0.05, epochs: int = 45, seed: int = 42):
        self.k = n_classes
        self.l2 = l2
        self.lr = lr
        self.epochs = epochs
        self.seed = seed
        self.feat_names: list[str] = []
        self.w: list[list[float]] = []

    def fit(self, X_dicts: list[dict[str, float]], y_list: list[int]) -> "MultinomialLogReg":
        fset = sorted({k for d in X_dicts for k in d.keys()})
        self.feat_names = fset
        fmap = {k: i for i, k in enumerate(fset)}
        d = len(fset)
        k = self.k
        self.w = [[0.0] * d for _ in range(k)]

        X_sparse = [[(fmap[fk], fv) for fk, fv in row.items() if fv != 0.0] for row in X_dicts]
        n = len(X_sparse)
        m_adam = [[0.0] * d for _ in range(k)]
        v_adam = [[0.0] * d for _ in range(k)]
        rng = random.Random(self.seed)
        indices = list(range(n))
        batch_size = 128
        step = 0
        lam = self.l2 / max(n, 1)
        bias_idx = fmap.get("bias", -1)

        for ep in range(self.epochs):
            rng.shuffle(indices)
            lr_t = self.lr / (1.0 + 0.04 * ep)
            for start in range(0, n, batch_size):
                batch = indices[start : start + batch_size]
                bsz = len(batch)
                step += 1
                grads = [[0.0] * d for _ in range(k)]
                for idx in batch:
                    x_row = X_sparse[idx]
                    y = y_list[idx]
                    logits = [sum(self.w[c][fi] * fv for fi, fv in x_row) for c in range(k)]
                    probs = softmax(logits)
                    for c in range(k):
                        diff = (probs[c] - (1.0 if c == y else 0.0)) / bsz
                        g_c = grads[c]
                        for fi, fv in x_row:
                            g_c[fi] += diff * fv
                b1_corr = 1.0 - 0.9 ** step
                b2_corr = 1.0 - 0.999 ** step
                for c in range(k):
                    for fi in range(d):
                        g = grads[c][fi]
                        if fi != bias_idx:
                            g += lam * self.w[c][fi]
                        if g == 0.0 and m_adam[c][fi] == 0.0:
                            continue
                        m_adam[c][fi] = 0.9 * m_adam[c][fi] + 0.1 * g
                        v_adam[c][fi] = 0.999 * v_adam[c][fi] + 0.001 * (g * g)
                        m_hat = m_adam[c][fi] / b1_corr
                        v_hat = v_adam[c][fi] / b2_corr
                        self.w[c][fi] -= lr_t * m_hat / (math.sqrt(v_hat) + 1e-8)
        return self

    def predict_proba(self, X_dicts: list[dict[str, float]]) -> list[list[float]]:
        fmap = {k: i for i, k in enumerate(self.feat_names)}
        out: list[list[float]] = []
        for row in X_dicts:
            logits = [0.0] * self.k
            for fk, fv in row.items():
                fi = fmap.get(fk)
                if fi is not None and fv != 0.0:
                    for c in range(self.k):
                        logits[c] += self.w[c][fi] * fv
            out.append(softmax(logits))
        return out

    def to_dict(self) -> dict[str, Any]:
        return {
            "k": self.k,
            "feat_names": self.feat_names,
            "w": [[round(v, 6) for v in row] for row in self.w],
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "MultinomialLogReg":
        obj = cls(n_classes=d["k"])
        obj.feat_names = d["feat_names"]
        obj.w = d["w"]
        return obj


class HistXGBoostMulticlass:
    """Histogram-based 2nd-Order Newton Gradient Boosted Trees (XGBoost / LightGBM math)."""

    def __init__(
        self,
        n_classes: int,
        n_estimators: int = 85,
        lr: float = 0.08,
        max_depth: int = 3,
        min_child_hess: float = 5.0,
        reg_lambda: float = 10.0,
        gamma: float = 0.15,
        colsample: float = 0.8,
        subsample: float = 0.85,
        seed: int = 42,
    ):
        self.k = n_classes
        self.n_estimators = n_estimators
        self.lr = lr
        self.max_depth = max_depth
        self.min_child_hess = min_child_hess
        self.reg_lambda = reg_lambda
        self.gamma = gamma
        self.colsample = colsample
        self.subsample = subsample
        self.seed = seed
        self.feat_names: list[str] = []
        self.bin_edges: list[list[float]] = []
        self.init_logits: list[float] = []
        self.trees: list[list[dict[str, Any]]] = []
        self.feature_gain: dict[str, float] = {}

    def _build_tree(self, X_binned, sample_idxs, grad, hess, feat_subset, depth) -> dict[str, Any]:
        g_tot = sum(grad[i] for i in sample_idxs)
        h_tot = sum(hess[i] for i in sample_idxs)
        leaf_val = round(g_tot / (h_tot + self.reg_lambda), 6)
        if depth >= self.max_depth or h_tot < 2.0 * self.min_child_hess or len(sample_idxs) < 20:
            return {"leaf": leaf_val}

        parent_score = (g_tot * g_tot) / (h_tot + self.reg_lambda)
        best_gain = self.gamma
        best_split = None

        for fi in feat_subset:
            n_bins = len(self.bin_edges[fi]) + 1
            if n_bins <= 1:
                continue
            g_bin = [0.0] * n_bins
            h_bin = [0.0] * n_bins
            col = X_binned[fi]
            for i in sample_idxs:
                b = col[i]
                g_bin[b] += grad[i]
                h_bin[b] += hess[i]

            g_l, h_l = 0.0, 0.0
            for b in range(n_bins - 1):
                g_l += g_bin[b]
                h_l += h_bin[b]
                h_r = h_tot - h_l
                if h_l < self.min_child_hess or h_r < self.min_child_hess:
                    continue
                g_r = g_tot - g_l
                gain = 0.5 * ((g_l * g_l) / (h_l + self.reg_lambda) + (g_r * g_r) / (h_r + self.reg_lambda) - parent_score)
                if gain > best_gain:
                    best_gain = gain
                    best_split = (fi, b)

        if best_split is None:
            return {"leaf": leaf_val}

        fi_best, b_best = best_split
        fname = self.feat_names[fi_best]
        self.feature_gain[fname] = self.feature_gain.get(fname, 0.0) + best_gain
        col_best = X_binned[fi_best]
        left_idxs = [i for i in sample_idxs if col_best[i] <= b_best]
        right_idxs = [i for i in sample_idxs if col_best[i] > b_best]
        return {
            "fi": fi_best,
            "bin_thr": b_best,
            "thr": round(self.bin_edges[fi_best][b_best], 6),
            "left": self._build_tree(X_binned, left_idxs, grad, hess, feat_subset, depth + 1),
            "right": self._build_tree(X_binned, right_idxs, grad, hess, feat_subset, depth + 1),
        }

    @staticmethod
    def _eval_raw(node: dict[str, Any], x_dict: dict[str, float], feat_names: list[str]) -> float:
        while "leaf" not in node:
            val = x_dict.get(feat_names[node["fi"]], 0.0)
            node = node["left"] if val <= node["thr"] else node["right"]
        return node["leaf"]

    @staticmethod
    def _eval_binned(node: dict[str, Any], X_binned: list[list[int]], i: int) -> float:
        while "leaf" not in node:
            node = node["left"] if X_binned[node["fi"]][i] <= node["bin_thr"] else node["right"]
        return node["leaf"]

    def fit(self, X_dicts: list[dict[str, float]], y_list: list[int]) -> "HistXGBoostMulticlass":
        fset = sorted({k for d in X_dicts for k in d.keys() if k != "bias"})
        self.feat_names = fset
        d = len(fset)
        n = len(X_dicts)
        self.feature_gain = {}

        self.bin_edges = []
        X_binned: list[list[int]] = []
        for fk in fset:
            col_raw = [row.get(fk, 0.0) for row in X_dicts]
            uniq = sorted(set(col_raw))
            if len(uniq) <= 1:
                edges: list[float] = []
            elif len(uniq) <= 12:
                edges = [(uniq[j] + uniq[j + 1]) / 2.0 for j in range(len(uniq) - 1)]
            else:
                qs = [int(len(col_raw) * q / 12) for q in range(1, 12)]
                s_vals = sorted(col_raw)
                edges = sorted({s_vals[idx] for idx in qs})[:11]
            self.bin_edges.append(edges)
            if not edges:
                X_binned.append([0] * n)
            elif len(edges) == 1:
                e0 = edges[0]
                X_binned.append([1 if v > e0 else 0 for v in col_raw])
            else:
                col_b = []
                for v in col_raw:
                    b = 0
                    for e in edges:
                        if v > e:
                            b += 1
                        else:
                            break
                    col_b.append(b)
                X_binned.append(col_b)

        counts = [sum(1 for y in y_list if y == c) for c in range(self.k)]
        self.init_logits = [round(math.log((cnt + 1.0) / (n + self.k)), 6) for cnt in counts]
        logits = [list(self.init_logits) for _ in range(n)]
        self.trees = []

        rng = random.Random(self.seed)
        all_feats = [fi for fi in range(d) if len(self.bin_edges[fi]) > 0]
        all_rows = list(range(n))
        n_sub = max(32, int(n * self.subsample))
        m_feat = max(4, int(len(all_feats) * self.colsample))

        for _ in range(self.n_estimators):
            probs = [softmax(l) for l in logits]
            sub_rows = rng.sample(all_rows, n_sub) if n_sub < n else all_rows
            round_trees = []
            for c in range(self.k):
                feat_sub = rng.sample(all_feats, m_feat) if m_feat < len(all_feats) else all_feats
                grad = [(1.0 if y_list[i] == c else 0.0) - probs[i][c] for i in range(n)]
                hess = [max(2.0 * probs[i][c] * (1.0 - probs[i][c]), 0.02) for i in range(n)]
                tree = self._build_tree(X_binned, sub_rows, grad, hess, feat_sub, 0)
                round_trees.append(tree)
                for i in range(n):
                    logits[i][c] += self.lr * self._eval_binned(tree, X_binned, i)
            self.trees.append(round_trees)
        return self

    def predict_proba(self, X_dicts: list[dict[str, float]]) -> list[list[float]]:
        out: list[list[float]] = []
        for row in X_dicts:
            l = list(self.init_logits)
            for round_trees in self.trees:
                for c in range(self.k):
                    l[c] += self.lr * self._eval_raw(round_trees[c], row, self.feat_names)
            out.append(softmax(l))
        return out

    def to_dict(self) -> dict[str, Any]:
        return {
            "k": self.k,
            "lr": self.lr,
            "feat_names": self.feat_names,
            "init_logits": self.init_logits,
            "trees": self.trees,
            "feature_gain": {k: round(v, 3) for k, v in sorted(self.feature_gain.items(), key=lambda x: -x[1])[:40]},
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "HistXGBoostMulticlass":
        obj = cls(n_classes=d["k"], lr=d["lr"])
        obj.feat_names = d["feat_names"]
        obj.init_logits = d["init_logits"]
        obj.trees = d["trees"]
        obj.feature_gain = d.get("feature_gain", {})
        return obj


def compute_cmh_stratified_effects(forecasts: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """Cochran-Mantel-Haenszel (CMH) stratified log-odds & percentage-point effects
    controlling for (domain, horizon_bucket, horizon_source) with inverse-sqrt book-cluster
    weights across the 7,522 decided forecasts (eliminating Simpson's paradox & single-book dominance).
    """
    decided = [r for r in forecasts if r["verdict"] != "暂无法判断"]
    book_n = collections.Counter(r["case_slug"] for r in decided)
    strata: dict[tuple[str, str, str], list[tuple[dict[str, Any], dict[str, float], float]]] = collections.defaultdict(list)
    for r in decided:
        cw = 1.0 / math.sqrt(max(book_n[r["case_slug"]], 15))
        strata[(r["domain"], r["horizon_bucket"], r["horizon_source"])].append((r, extract_features(r), cw))

    keys = [
        "m_constraint_ledger",
        "m_institutional_incentive",
        "m_geopolitical_chassis",
        "m_functional_diffusion",
        "m_risk_fragility",
        "m_conditional_scenario",
        "s_unanchored_hard_number",
        "s_cross_layer_utopian_jump",
        "s_linear_rate_extrapolation",
        "s_compound_claim",
        "s_comparative_surpass",
        "ix_anchored_explicit",
        "ix_unanchored_explicit",
        "ix_surpass_explicit_no_ledger",
        "ix_heavy_short_explicit_no_ledger",
    ]
    effects: dict[str, dict[str, float]] = {}
    for key in keys:
        w_sum = 0.0
        d_vec = [0.0, 0.0, 0.0, 0.0]
        n_pos = 0
        for items in strata.values():
            pos = [(r, cw) for r, f, cw in items if f.get(key, 0.0) > 0.5]
            neg = [(r, cw) for r, f, cw in items if f.get(key, 0.0) <= 0.5]
            if len(pos) < 2 or len(neg) < 3:
                continue
            w1 = sum(cw for _, cw in pos)
            w0 = sum(cw for _, cw in neg)
            w = (w1 * w0) / (w1 + w0)
            w_sum += w
            n_pos += len(pos)
            for c, vname in enumerate(VERDICTS_4):
                p1 = sum(cw for r, cw in pos if r["verdict"] == vname) / w1
                p0 = sum(cw for r, cw in neg if r["verdict"] == vname) / w0
                d_vec[c] += w * (p1 - p0)
        if w_sum > 0:
            deltas = [d / w_sum for d in d_vec]
            effects[key] = {
                "n_positive": n_pos,
                "delta_strict_pp": round(deltas[0] * 100.0, 2),
                "delta_trend_pp": round(deltas[1] * 100.0, 2),
                "delta_partial_pp": round(deltas[2] * 100.0, 2),
                "delta_error_pp": round(deltas[3] * 100.0, 2),
                "delta_directional_pp": round((deltas[0] + deltas[1]) * 100.0, 2),
            }
    return effects


# ---------------------------------------------------------------------------
# Unified Super-Learner Model Container, Training, & Out-of-Book CV Benchmark
# ---------------------------------------------------------------------------

class ForecastOptimizerEngine:
    """End-to-end calibrated forecast evaluation, counterfactual method optimization, and Bayesian updater."""

    def __init__(self, model_bundle: dict[str, Any], repo_root: Path = REPO_ROOT):
        self.bundle = model_bundle
        self.repo_root = repo_root
        self.heb = HierarchicalEmpiricalBayes.from_dict(model_bundle["heb"])
        self.maxent = MultinomialLogReg.from_dict(model_bundle["maxent"])
        self.xgb_direct = HistXGBoostMulticlass.from_dict(model_bundle["xgb_direct"])
        self.xgb_stage1 = HistXGBoostMulticlass.from_dict(model_bundle["xgb_stage1_hazard"])
        self.xgb_stage2 = HistXGBoostMulticlass.from_dict(model_bundle["xgb_stage2_decided"])
        self.denoiser = HistXGBoostMulticlass.from_dict(model_bundle["stage0_denoiser"])
        self.pool_weights: list[float] = model_bundle["pool_weights"]
        self.temperature: float = model_bundle["temperature"]
        self.modern_pit_priors: dict[str, dict[str, float]] = model_bundle["modern_pit_priors"]
        self.cmh_effects: dict[str, dict[str, float]] = model_bundle["cmh_effects"]
        self._curated_cache: list[dict[str, str]] | None = None
        self._summary_cache: list[dict[str, str]] | None = None
        self._atlas_cache: dict[str, Any] | None = None

    @classmethod
    def load(cls, model_path: Path = DEFAULT_MODEL_PATH, repo_root: Path = REPO_ROOT) -> "ForecastOptimizerEngine":
        if not model_path.is_file():
            bundle, _ = train_and_benchmark(repo_root=repo_root, save=True)
            return cls(bundle, repo_root=repo_root)
        bundle = json.loads(model_path.read_text(encoding="utf-8"))
        return cls(bundle, repo_root=repo_root)

    def _curated_rows(self) -> list[dict[str, str]]:
        if self._curated_cache is None:
            p = self.repo_root / "datasets" / "curated_330_forecasts.csv"
            with open(p, encoding="utf-8-sig") as f:
                self._curated_cache = list(csv.DictReader(f))
        return self._curated_cache

    def _summary_rows(self) -> list[dict[str, str]]:
        if self._summary_cache is None:
            p = self.repo_root / "datasets" / "all_cases_summary.csv"
            with open(p, encoding="utf-8-sig") as f:
                self._summary_cache = list(csv.DictReader(f))
        return self._summary_cache

    def _atlas_data(self) -> dict[str, Any]:
        if self._atlas_cache is None:
            p = self.repo_root / "datasets" / "historical_tech_diffusion_atlas.json"
            self._atlas_cache = json.loads(p.read_text(encoding="utf-8"))
        return self._atlas_cache

    def evaluate_tech_differentiation(
        self,
        *,
        statement: str,
        domain: str = "",
        scope: str = "",
        horizon_years: float | None = None,
        current_penetration: float | None = None,
        target_penetration: float | None = None,
        is_stock_scope: bool | None = None,
    ) -> dict[str, Any]:
        """Test 'Is This New Technology Really Different This Time?' against 150 years of
        historical technology diffusion S-curves (Comin-Hobijn CHAT, Bass 1969, Paul David 1990)
        and output both the historical structural skeleton and the real-time bottleneck parameters to check.
        """
        atlas = self._atlas_data()
        layers = atlas["four_layer_speed_laws"]
        waves = atlas["waves"]
        combined_low = f"{statement} {domain} {scope}".lower()
        year_now = date.today().year
        eff_years = horizon_years or parse_explicit_span(statement, year_now) or 5.0

        # 1. Match structural historical analogs from the 12-wave Atlas
        scored_waves: list[tuple[float, dict[str, Any]]] = []
        for w in waves:
            sc = 0.0
            for kw in w["keywords"]:
                if kw.lower() in combined_low:
                    sc += 3.0 if len(kw) >= 3 else 1.5
            # Domain fallback affinity
            canon_dom = normalize_domain(domain or statement)
            if canon_dom == "人口、能源、资源与生态" and w["wave_id"] == "utility_grid_power_and_storage":
                sc += 2.0
            elif canon_dom == "AI与奇点前沿" and w["wave_id"] == "enterprise_public_cloud":
                sc += 1.5
            elif canon_dom == "科技、商业与产业颠覆" and w["wave_id"] in ("smartphone_mobile_terminal", "enterprise_public_cloud"):
                sc += 1.0
            scored_waves.append((sc, w))

        scored_waves.sort(key=lambda x: x[0], reverse=True)
        primary_wave = scored_waves[0][1]
        top_analogs = [w for _, w in scored_waves[:3]]
        layer_info = layers[primary_wave["layer_id"]]

        # 2. Disambiguate Incremental Flow Share vs Installed Stock Replacement
        detected_stock = (
            is_stock_scope
            if is_stock_scope is not None
            else bool(STRUCTURAL_PATTERNS["stock_replacement_scope"].search(f"{statement} {scope}"))
        )
        s0 = current_penetration if current_penetration is not None else 0.04
        s1_parsed = target_penetration if target_penetration is not None else parse_target_share(statement, s0=s0)
        s1 = s1_parsed if s1_parsed is not None else 0.35
        if s1 <= s0 + 0.004:
            s1 = min(0.90, s0 + 0.15)

        stock_inertia = (
            primary_wave["stock_5_to_50_years"] / max(primary_wave["flow_5_to_50_years"], 0.5)
            if detected_stock
            else 1.0
        )
        hist_req_years = bass_time_between_shares(
            primary_wave["bass_p"],
            primary_wave["bass_q"],
            s0,
            s1,
            stock_inertia=stock_inertia,
        )
        turnover_floor = primary_wave["asset_turnover_cycle_years"] * (s1 - s0) * (1.25 if detected_stock else 0.45)
        effective_hist_years = max(hist_req_years, turnover_floor)
        speedup_multiple = round(effective_hist_years / max(eff_years, 0.25), 2)

        # Calibrated realistic penetration range at user's horizon (1.0x historical baseline vs 1.5x catalyzed wave)
        proj_1x = bass_share_after_years(primary_wave["bass_p"], primary_wave["bass_q"], s0, eff_years, speedup=1.0, stock_inertia=stock_inertia)
        proj_1_5x = bass_share_after_years(primary_wave["bass_p"], primary_wave["bass_q"], s0, eff_years, speedup=1.5, stock_inertia=stock_inertia)

        if speedup_multiple > 2.2 or (detected_stock and eff_years < turnover_floor * 0.85):
            verdict_code = "extreme_overreach"
            verdict_label = f"高危‘这次不一样’跨层透支（要求速度为历史同构前辈的 {speedup_multiple:.1f} 倍）"
            diagnosis = (
                f"当前命题落在【{layer_info['name']}】，按{'存量替代/保有量' if detected_stock else '增量渗透'}口径从 {s0:.0%} 到 {s1:.0%}，"
                f"同构前辈「{primary_wave['name']}」需约 {effective_hist_years:.1f} 年（受制于资产/组织周转底线 {primary_wave['asset_turnover_cycle_years']:.1f} 年），"
                f"而当前仅给 {eff_years:.1f} 年窗口！即便给予 1.5 倍技术催化加速，{eff_years:.1f} 年内合理校准区间约为 {proj_1x:.1%}–{proj_1_5x:.1%}。"
            )
        elif speedup_multiple > 1.35:
            verdict_code = "catalyst_dependent"
            verdict_label = f"温和超速（为历史同构基准的 {speedup_multiple:.1f} 倍，需实时瓶颈指标验证催化强度）"
            diagnosis = (
                f"当前命题落在【{layer_info['name']}】，要求扩散速度快于「{primary_wave['name']}」历史均值（{effective_hist_years:.1f} 年 vs 给定 {eff_years:.1f} 年）。"
                f"必须核验下方实时参数，确认单位成本已跨过平价点且未卡在物理/审批队列。"
            )
        else:
            verdict_code = "historically_grounded"
            verdict_label = f"符合历史扩散斜率（要求速度为历史同构基准的 {speedup_multiple:.2f} 倍）"
            diagnosis = (
                f"当前时间窗口（{eff_years:.1f} 年）与【{layer_info['name']}】历史同构前辈「{primary_wave['name']}」的 S 曲线斜率（约 {effective_hist_years:.1f} 年）匹配稳健。"
            )

        jevons_notes = {
            "high_expansion": "强杰文斯反弹：历史表明该层技术降本 90% 后，前 5–10 年主效应是引爆长尾新需求总量（如煤耗/算力/金融分析量暴增），而非净归零存量。",
            "task_shift_and_expansion": "任务重塑而非岗位净消失：如 Excel 与云计算历史所示，先替代单一重复任务(Task)并扩大总产出，净编制缩减远慢于任务渗透。",
            "substitution_dominant": "存量折旧替代主导：终局替代明确，但斜率严格受存量设备/车队物理报废周期封顶，严禁混同‘新车/新增占比’与‘全社会保有量占比’。",
            "regulated_gradual": "零容错立法配速：实验室指标突破不等于商业普及，实际斜率由事故归责立法、三期临床/适航牌照与保险准入速度决定。",
        }

        return {
            "assigned_friction_layer": layer_info,
            "scope_mode": "installed_stock_replacement（存量保有量/存量岗位替代口径）" if detected_stock else "incremental_flow_adoption（新增流量/增量渗透口径）",
            "assumed_baseline_share": round(s0, 4),
            "target_share_evaluated": round(s1, 4),
            "target_horizon_years": round(eff_years, 2),
            "historical_analog_required_years": round(effective_hist_years, 2),
            "physical_turnover_floor_years": round(turnover_floor, 2),
            "required_speedup_multiple": speedup_multiple,
            "differentiation_verdict_code": verdict_code,
            "differentiation_verdict": verdict_label,
            "diagnosis": diagnosis,
            "calibrated_share_range_in_horizon": {
                "historical_1x_baseline": round(proj_1x, 4),
                "accelerated_1_5x_catalyst": round(proj_1_5x, 4),
            },
            "jevons_elasticity_effect": jevons_notes[primary_wave["jevons_elasticity"]],
            "primary_structural_analog": {
                "wave_id": primary_wave["wave_id"],
                "name": primary_wave["name"],
                "flow_5_to_50_years": primary_wave["flow_5_to_50_years"],
                "stock_5_to_50_years": primary_wave["stock_5_to_50_years"],
                "primary_bottlenecks": primary_wave["primary_bottlenecks"],
                "archive_anchor": primary_wave["archive_anchor"],
            },
            "secondary_analogs": [
                {"name": w["name"], "flow_5_to_50_years": w["flow_5_to_50_years"], "stock_5_to_50_years": w["stock_5_to_50_years"]}
                for w in top_analogs[1:]
            ],
            "realtime_parameters_to_fetch_now": primary_wave["realtime_parameters_to_check"],
        }

    def predict_record(
        self,
        rec: dict[str, Any],
        method_override: dict[str, float] | None = None,
        trap_override: dict[str, float] | None = None,
    ) -> dict[str, Any]:
        dom = normalize_domain(rec.get("domain", ""))
        pit = self.modern_pit_priors.get(dom) or next(iter(self.modern_pit_priors.values()))
        X = extract_features(rec, pit_prior=pit, method_override=method_override, trap_override=trap_override)

        p_valid = self.denoiser.predict_proba([X])[0][1]
        p_heb, ref_meta = self.heb.predict_one(rec)
        p_me = self.maxent.predict_proba([X])[0]
        p_xgb5 = self.xgb_direct.predict_proba([X])[0]
        ps1 = self.xgb_stage1.predict_proba([X])[0]
        ps2 = self.xgb_stage2.predict_proba([X])[0]
        p_2stage = [ps1[1] * ps2[0], ps1[1] * ps2[1], ps1[1] * ps2[2], ps1[1] * ps2[3], ps1[0]]

        p5 = log_linear_pool([[p_heb], [p_me], [p_xgb5], [p_2stage]], self.pool_weights, self.temperature)[0]

        # Apply subtle CMH deconfounded micro-calibration on the 4 decided classes for rare traps & counterfactual overrides
        dec_mass = max(1.0 - p5[4], 1e-8)
        p4 = [p5[c] / dec_mass for c in range(4)]
        cmh_shift = [0.0, 0.0, 0.0, 0.0]
        for t_key in ("s_unanchored_hard_number", "s_linear_rate_extrapolation", "s_comparative_surpass", "s_compound_claim"):
            v = X.get(t_key, 0.0)
            if v > 0.5 and t_key in self.cmh_effects:
                eff = self.cmh_effects[t_key]
                cmh_shift[0] += 0.35 * (eff["delta_strict_pp"] / 100.0)
                cmh_shift[1] += 0.35 * (eff["delta_trend_pp"] / 100.0)
                cmh_shift[2] += 0.35 * (eff["delta_partial_pp"] / 100.0)
                cmh_shift[3] += 0.45 * (eff["delta_error_pp"] / 100.0)
        if any(s != 0.0 for s in cmh_shift):
            p4 = [max(0.005, p4[c] + cmh_shift[c]) for c in range(4)]
            s4 = sum(p4)
            p4 = [v / s4 for v in p4]
            p5 = [p4[0] * dec_mass, p4[1] * dec_mass, p4[2] * dec_mass, p4[3] * dec_mass, p5[4]]

        # Proper utility score: rewards strict & directional accuracy, penalizes outright errors & unresolvable vagueness
        # Strictly transparent decision rule; raw 5-class probabilities are always returned separately!
        utility = (
            1.00 * p5[0]
            + 0.70 * p5[1]
            + 0.30 * p5[2]
            - 1.25 * p5[3]
            - 0.35 * p5[4]
        )
        decided_utility = 1.00 * p4[0] + 0.72 * p4[1] + 0.30 * p4[2] - 1.35 * p4[3]

        return {
            "is_valid_forecast_prob": round(p_valid, 4),
            "probs_5class": {VERDICTS_5[c]: round(p5[c], 4) for c in range(5)},
            "probs_decided_4class": {VERDICTS_4[c]: round(p4[c], 4) for c in range(4)},
            "strict_win_prob_given_decided": round(p4[0], 4),
            "directional_hit_prob_given_decided": round(p4[0] + p4[1], 4),
            "error_prob_given_decided": round(p4[3], 4),
            "unresolved_prob": round(p5[4], 4),
            "composite_utility": round(utility, 4),
            "decided_utility": round(decided_utility, 4),
            "reference_class": ref_meta,
            "active_features": {k: v for k, v in X.items() if v != 0.0 and (k.startswith("m_") or k.startswith("s_") or k.startswith("ix_"))},
        }

    def audit_operationalizability(
        self,
        *,
        statement: str,
        horizon: str,
        scope: str,
        condition_text: str,
        falsification: str,
        leading_indicators: str,
        method: str = "",
        counter_lens: str = "",
    ) -> dict[str, Any]:
        combined = f"{statement} {scope} {horizon}"
        slots = {
            "actor_and_object": len(statement.strip()) >= 12,
            "measurable_metric_and_denominator": bool(
                STRUCTURAL_PATTERNS["measurable_metric"].search(combined)
                or re.search(r"分母|口径|比例|占比|总数|台数|亿美元|GW|TWh|万吨|百分点", combined, re.I)
            ),
            "authoritative_data_source": bool(STRUCTURAL_PATTERNS["authoritative_source_named"].search(combined)),
            "explicit_horizon": bool(horizon.strip()) or bool(parse_explicit_span(statement, date.today().year)),
            "falsification_threshold": bool(falsification.strip()) or bool(re.search(r"至少|不超过|高于|低于|超过|下降|突破|\d+", statement)),
            "leading_indicators": bool(leading_indicators.strip()),
        }
        explicit_method_disclosed = bool(method.strip()) and bool(counter_lens.strip())
        passed = sum(1 for v in slots.values() if v)
        missing = [k for k, v in slots.items() if not v]
        if not explicit_method_disclosed:
            missing.append("explicit_method_and_counter_lens")

        # Detect active noise traps
        traps_found = []
        s_feats = {k: bool(pat.search(statement)) for k, pat in STRUCTURAL_PATTERNS.items()}
        m_feats = {k: bool(pat.search(f"{statement} {scope}")) for k, pat in METHOD_PATTERNS.items()}
        has_ledger = m_feats["constraint_ledger"]

        if s_feats["unanchored_hard_number"] and not has_ledger:
            traps_found.append({"trap_id": "unanchored_hard_number", **NOISE_TRAPS["unanchored_hard_number"]})
        if s_feats["comparative_surpass"] and slots["explicit_horizon"] and not has_ledger:
            traps_found.append({"trap_id": "surpass_explicit_no_ledger", **NOISE_TRAPS["surpass_explicit_no_ledger"]})
        if s_feats["linear_rate_extrapolation"]:
            traps_found.append({"trap_id": "linear_rate_extrapolation", **NOISE_TRAPS["linear_rate_extrapolation"]})
        if s_feats["cross_layer_utopian_jump"]:
            traps_found.append({"trap_id": "cross_layer_utopian_jump", **NOISE_TRAPS["cross_layer_utopian_jump"]})
        if s_feats["compound_claim"]:
            traps_found.append({"trap_id": "compound_claim_bundling", **NOISE_TRAPS["compound_claim_bundling"]})
        if s_feats["normative_should"]:
            traps_found.append({
                "trap_id": "normative_advocacy",
                "name": "把政策倡议/价值呼吁（应当如何）混作实证预测（将会如何）",
                "cmh_effect_note": "抽取管线 v5 中此类命题属于非预测噪音（normative），禁止直接计分",
                "remediation": "改为客观行为主体在现行激励约束下‘实际会出台何种政策或达成何种指标’，剥离‘应该’语态。",
            })

        return {
            "score_out_of_6": passed,
            "explicit_method_disclosed": explicit_method_disclosed,
            "slots": {**slots, "explicit_method_and_counter_lens": explicit_method_disclosed},
            "missing_slots": missing,
            "traps_detected": traps_found,
        }

    def retrieve_precedents(self, domain: str, statement: str, top_k: int = 3) -> dict[str, list[dict[str, str]]]:
        canon_dom = normalize_domain(domain)
        tokens = set(re.findall(r"[\u4e00-\u9fff]{2,4}|[a-zA-Z]{3,}", f"{statement} {domain}".lower()))

        def score_row(r: dict[str, str]) -> float:
            s = 3.0 if r["领域"] == canon_dom else 0.0
            txt = f"{r['预测命题']} {r['核心标签']} {r['核验或前瞻摘要']}".lower()
            for tok in tokens:
                if tok in txt:
                    s += 1.0
            return s

        rows = self._curated_rows()
        hits = sorted([r for r in rows if r["板块"].startswith("A_")], key=score_row, reverse=True)[:top_k]
        misses = sorted([r for r in rows if r["板块"].startswith("B_")], key=score_row, reverse=True)[:top_k]
        compass = sorted([r for r in rows if r["板块"].startswith("C")], key=score_row, reverse=True)[:top_k]

        fmt = lambda lst: [
            {
                "id": r["编号"],
                "book": f"{r['作者']}《{r['书名']}》({r['出版年']})",
                "domain": r["领域"],
                "claim": r["预测命题"],
                "tag": r["核心标签"],
                "lesson_or_indicator": r["复盘启示或2026-2035跟踪指标"] or r["核验或前瞻摘要"][:120],
            }
            for r in lst
        ]
        return {
            "best_signal_exemplars": fmt(hits),
            "failure_anti_precedents": fmt(misses),
            "forward_compass_peers": fmt(compass),
        }

    def optimize_forecast(
        self,
        *,
        statement: str,
        domain: str = "",
        horizon: str = "",
        target_years: float | None = None,
        scope: str = "",
        condition_text: str = "",
        method: str = "",
        counter_lens: str = "",
        leading_indicators: str = "",
        falsification: str = "",
        forecaster_stance: str = "科技商业思想家与产业实践者",
        current_year: int | None = None,
    ) -> dict[str, Any]:
        """Run full data-driven audit & counterfactual forecast method optimization."""
        year_now = current_year or date.today().year
        canon_dom = normalize_domain(domain or statement)
        parsed_span = target_years or parse_explicit_span(f"{horizon} {statement}", year_now)
        eff_years = parsed_span if parsed_span is not None else 5.0
        has_explicit = bool(horizon.strip()) or (parsed_span is not None)

        # 1. Baseline evaluation of the user's draft AS-IS
        draft_rec = {
            "domain": canon_dom,
            "author_type": normalize_archetype(forecaster_stance),
            "pub_year": year_now,
            "window_years": eff_years,
            "horizon_bucket": window_to_horizon_bucket(eff_years),
            "is_classical_philosophy": 0.0,
            "quote": statement,
            "claim": statement,
            "time_text": horizon,
            "condition_text": condition_text,
            "ex_method": f"{method} {counter_lens}".strip(),
            "scope_text": scope,
            "horizon_source": "explicit" if has_explicit else "implicit_publication_to_cutoff",
            "explicit_span_years": parsed_span,
        }
        baseline = self.predict_record(draft_rec)
        audit = self.audit_operationalizability(
            statement=statement,
            horizon=horizon,
            scope=scope,
            condition_text=condition_text,
            falsification=falsification,
            leading_indicators=leading_indicators,
            method=method,
            counter_lens=counter_lens,
        )

        # 2. Counterfactual Method & Commitment Policy Search (FFORMA + CMH + Empirical Domain-Method Prior)
        # Compute empirical Domain x Method log-odds affinity from curated gold exemplars (Laplace smoothed)
        tag_to_mkey = {
            "约束账本": "constraint_ledger",
            "制度激励": "institutional_incentive",
            "地缘底盘": "geopolitical_chassis",
            "功能扩散": "functional_diffusion",
            "风险边界": "risk_fragility",
            "情景分支": "conditional_scenario",
        }
        dom_m_counts = {k: 1.0 for k in SIGNAL_METHODS}
        for r in self._curated_rows():
            if r["板块"].startswith("A_") and r["领域"] == canon_dom:
                mk = tag_to_mkey.get(r["核心标签"].strip())
                if mk:
                    dom_m_counts[mk] += 2.0
        dom_m_total = sum(dom_m_counts.values())
        dom_m_prior = {k: v / dom_m_total for k, v in dom_m_counts.items()}

        # Enforce falsifiability discipline: <=15y forecasts must keep explicit deadlines; >15y allow structural directional windows
        commitment_regimes = [
            ("explicit_interval_with_ledger", "explicit", "显式期限 + 存量产能账本区间门槛（推荐短中期）"),
            ("conditional_scenario_branch", "explicit", "显式前提分支 P(A) × P(B|A) + 领先指标触发阈值（推荐中长期）"),
        ]
        if eff_years > 15.0:
            commitment_regimes.append(
                ("directional_structural_window", "implicit_publication_to_cutoff", "结构方向承诺 + 排除拍脑袋年份（推荐15年以上超长周期）")
            )

        candidates: list[dict[str, Any]] = []
        clean_trap_override = {
            "absolutist_hedgehog": 0.0,
            "cross_layer_utopian_jump": 0.0,
            "linear_rate_extrapolation": 0.0,
            "compound_claim": 0.0,
            "normative_should": 0.0,
            "fox_hedging": 1.0,
            "measurable_metric": 1.0,
            "authoritative_source_named": 1.0,
            "causal_mechanism_connector": 1.0,
            "counter_caveat": 1.0,
        }

        for m_key, m_info in SIGNAL_METHODS.items():
            min_y, max_y = m_info["best_horizon_years"]
            horizon_fit_bonus = 0.025 if (min_y <= eff_years <= max_y) else -0.02

            for reg_id, h_src, reg_desc in commitment_regimes:
                cf_rec = dict(draft_rec)
                cf_rec["author_type"] = "国际机构与政府智库"
                cf_rec["horizon_source"] = h_src
                cf_rec["explicit_span_years"] = eff_years if h_src == "explicit" else None

                m_ovr = {k: 0.0 for k in SIGNAL_METHODS}
                m_ovr[m_key] = 1.0
                if reg_id == "conditional_scenario_branch":
                    m_ovr["conditional_scenario"] = 1.0
                if reg_id == "explicit_interval_with_ledger":
                    m_ovr["constraint_ledger"] = max(m_ovr["constraint_ledger"], 1.0 if m_key == "constraint_ledger" else 0.5)

                t_ovr = dict(clean_trap_override)
                if h_src == "implicit_publication_to_cutoff":
                    t_ovr["unanchored_hard_number"] = 0.0

                pred = self.predict_record(cf_rec, method_override=m_ovr, trap_override=t_ovr)

                # Incorporate controlled CMH empirical method effect + Domain x Method Empirical Bayes affinity
                cmh_m = self.cmh_effects.get(f"m_{m_key}", {})
                cmh_bonus = 0.0025 * cmh_m.get("delta_strict_pp", 0.0) - 0.004 * cmh_m.get("delta_error_pp", 0.0)
                dom_affinity_bonus = 0.045 * math.log(max(dom_m_prior[m_key] * len(SIGNAL_METHODS), 0.25))
                long_exp_pen = -0.06 if (eff_years > 15 and h_src == "explicit" and reg_id != "conditional_scenario_branch") else 0.0
                cond_mid_bonus = 0.025 if (6 <= eff_years <= 20 and reg_id == "conditional_scenario_branch") else 0.0

                adj_score = pred["composite_utility"] + horizon_fit_bonus + cmh_bonus + dom_affinity_bonus + long_exp_pen + cond_mid_bonus
                candidates.append({
                    "method_key": m_key,
                    "method_name": m_info["name"],
                    "method_summary": m_info["summary"],
                    "derivation_steps": m_info["derivation_steps"],
                    "commitment_regime": reg_id,
                    "commitment_label": reg_desc,
                    "recommended_counter_lens": m_info["default_counter_lens"],
                    "leading_indicator_template": m_info["leading_indicator_hint"],
                    "exemplars": m_info["exemplars"],
                    "calibrated_probs_5class": pred["probs_5class"],
                    "calibrated_probs_decided_4class": pred["probs_decided_4class"],
                    "strict_win_prob_given_decided": pred["strict_win_prob_given_decided"],
                    "directional_hit_prob_given_decided": pred["directional_hit_prob_given_decided"],
                    "error_prob_given_decided": pred["error_prob_given_decided"],
                    "unresolved_prob": pred["unresolved_prob"],
                    "optimization_score": round(adj_score, 4),
                    "cmh_empirical_evidence": cmh_m,
                })

        candidates.sort(key=lambda c: c["optimization_score"], reverse=True)
        best = candidates[0]
        # Deduplicate top 3 distinct primary methods for diverse comparison
        seen_m = set()
        top_diverse = []
        for c in candidates:
            if c["method_key"] not in seen_m:
                seen_m.add(c["method_key"])
                top_diverse.append(c)
            if len(top_diverse) >= 3:
                break

        precedents = self.retrieve_precedents(canon_dom, statement, top_k=3)

        # 3. Historical Tech-Diffusion & "Is This Time Different?" 4-Layer Stress Test
        is_tech_relevant = canon_dom in (
            "AI与奇点前沿",
            "科技、商业与产业颠覆",
            "人口、能源、资源与生态",
            "科幻推演与乌托邦/反乌托邦",
        ) or bool(re.search(r"技术|AI|智能|自动|电动|芯片|算力|互联网|机器人|基因|核电|光伏|储能|数字化|tech|ai|digital|automat", f"{statement} {domain}", re.I))

        tech_diff_audit = (
            self.evaluate_tech_differentiation(
                statement=statement,
                domain=canon_dom,
                scope=scope,
                horizon_years=eff_years,
            )
            if is_tech_relevant
            else None
        )
        if tech_diff_audit and tech_diff_audit["differentiation_verdict_code"] == "extreme_overreach":
            audit["traps_detected"].append({
                "trap_id": "this_time_is_different_speed_overreach",
                "name": "‘这次不一样’跨层速度透支（无视物理周转墙与组织重构周期）",
                "cmh_effect_note": tech_diff_audit["differentiation_verdict"],
                "remediation": (
                    f"{tech_diff_audit['diagnosis']} 请将分母明确限定为增量/任务级口径，或将目标阈值下调至历史校准区间 "
                    f"{tech_diff_audit['calibrated_share_range_in_horizon']['historical_1x_baseline']:.0%}–"
                    f"{tech_diff_audit['calibrated_share_range_in_horizon']['accelerated_1_5x_catalyst']:.0%}，并核查实时瓶颈参数。"
                ),
            })

        uplift = {
            "delta_strict_win_prob_pp": round(
                (best["strict_win_prob_given_decided"] - baseline["strict_win_prob_given_decided"]) * 100.0, 2
            ),
            "delta_directional_hit_prob_pp": round(
                (best["directional_hit_prob_given_decided"] - baseline["directional_hit_prob_given_decided"]) * 100.0, 2
            ),
            "delta_error_prob_pp": round(
                (best["error_prob_given_decided"] - baseline["error_prob_given_decided"]) * 100.0, 2
            ),
            "delta_unresolved_prob_pp": round(
                (best["unresolved_prob"] - baseline["unresolved_prob"]) * 100.0, 2
            ),
            "delta_utility": round(best["optimization_score"] - baseline["composite_utility"], 4),
        }

        # Concrete step-by-step optimization actions for any calling Agent
        prescriptions = []
        if baseline["is_valid_forecast_prob"] < 0.60:
            prescriptions.append("【去伪存真】当前表述疑似夹杂规范倡议（应该如何）或静态机制格言，请改写为对未来可观测指标变化的实证承诺。")
        if audit["missing_slots"]:
            slot_zh = {
                "actor_and_object": "明确行为主体与受影响对象边界",
                "measurable_metric_and_denominator": "补齐可测指标与统计分母（严查‘出现≠普及≠主导≠取代’）",
                "authoritative_data_source": "绑定唯一结算权威数据源（如 EIA / BLS / 国家统计局 / IEA / 上市公司年报）",
                "explicit_horizon": "明确观察窗口起止时间（如‘截至2029年12月31日’）",
                "falsification_threshold": "写出可证伪的定量阈值或反向推翻条件",
                "leading_indicators": "配置2–3个每季度/半年可观测的先行指标",
                "explicit_method_and_counter_lens": "在终局预测中显式写出【预测方法及四步推导链】与【反校验透镜】（严禁只给结论不写方法）",
            }
            prescriptions.append("【补齐规范要素缺口】需补充：" + "；".join(slot_zh[s] for s in audit["missing_slots"]) + "。")
        for tr in audit["traps_detected"]:
            prescriptions.append(f"【拆除翻车陷阱：{tr['name']}】{tr['remediation']}")
        prescriptions.append(
            f"【切换并显式写出最优预测方法】主透镜采用「{best['method_name']}」，按四步链写出推导过程（{' → '.join(best['derivation_steps'])}），搭配反校验透镜「{best['recommended_counter_lens']}」，承诺硬度采用「{best['commitment_label']}」。"
        )

        horizon_label = horizon.strip() or f"{year_now}–{int(year_now + eff_years)}"
        b_o4 = best["calibrated_probs_decided_4class"]
        tech_card_lines = []
        if tech_diff_audit:
            pa = tech_diff_audit["primary_structural_analog"]
            rng = tech_diff_audit["calibrated_share_range_in_horizon"]
            tech_card_lines = [
                f"- **历史同构扩散校准（‘这次是否不一样’四层检验）**：",
                f"  - **所属摩擦层级**：{tech_diff_audit['assigned_friction_layer']['name']}（`{tech_diff_audit['scope_mode']}`）",
                f"  - **历史同构前辈**：{pa['name']}（增量 5%→50% 耗时 `{pa['flow_5_to_50_years']}年` / 存量耗时 `{pa['stock_5_to_50_years']}年`）",
                f"  - **速度压力测试**：{tech_diff_audit['differentiation_verdict']}；本窗口内历史校准区间 `{rng['historical_1x_baseline']:.1%}–{rng['accelerated_1_5x_catalyst']:.1%}`",
                f"  - **必查当下实时瓶颈参数**：{' ； '.join(tech_diff_audit['realtime_parameters_to_fetch_now'])}",
            ]
        final_card_md = "\n".join([
            f"### 终局预测卡（含显式预测方法与历史同构校准披露）",
            f"- **可核验预测承诺**：{statement.strip() if audit['score_out_of_6'] == 6 and not audit['traps_detected'] else '<请基于上方处方收敛后的六要素定量承诺>'}",
            f"- **统计口径与权威结算源**：{scope.strip() or '<唯一官方统计/财报口径与分母定义>'}（窗口：`{horizon_label}`）",
            f"- **显式预测方法（为什么这么判）**：",
            f"  - **主推理方法**：**{best['method_name']}** —— {best['method_summary']}",
            f"  - **方法四步推导链**：{' ； '.join(best['derivation_steps'])}",
            f"  - **反校验透镜（防盲区对冲）**：{counter_lens.strip() or best['recommended_counter_lens']}",
            f"  - **承诺硬度选择依据**：{best['commitment_label']}",
            *tech_card_lines,
            f"- **全库 {self.bundle.get('trained_on_forecasts', 10745):,} 条预测校准先验**：严格胜率 `{b_o4['正确']:.1%}` ｜ 方向命中率 `{(b_o4['正确'] + b_o4['趋势符合']):.1%}` ｜ 部分符合 `{b_o4['部分符合']:.1%}` ｜ 错误风险 `{b_o4['错误']:.1%}`",
            f"- **定期追踪领先指标**：{leading_indicators.strip() or best['leading_indicator_template']}",
            f"- **明确证伪条件（三轴结算红线）**：{falsification.strip() or '<明确推翻本预测的定量反证阈值>'}",
        ])

        return {
            "input_summary": {
                "statement": statement,
                "canonical_domain": canon_dom,
                "evaluation_horizon_years": eff_years,
                "horizon_bucket": window_to_horizon_bucket(eff_years),
                "current_year_t0": year_now,
                "historical_regime_at_t0": historical_regime_features(year_now),
            },
            "operationalizability_audit": audit,
            "tech_differentiation_audit": tech_diff_audit,
            "baseline_evaluation": baseline,
            "recommended_optimization": best,
            "explicit_method_specification": {
                "primary_method": best["method_name"],
                "method_principle": best["method_summary"],
                "four_step_derivation_chain": best["derivation_steps"],
                "paired_counter_lens": counter_lens.strip() or best["recommended_counter_lens"],
                "commitment_hardness": best["commitment_label"],
                "mandatory_rule": "最终输出的预测必须完整写出上述主方法四步推导链与反校验对冲逻辑，不得仅输出裸结论或单一概率数字。",
            },
            "final_forecast_card_markdown": final_card_md,
            "alternative_method_rankings": top_diverse,
            "expected_uplift": uplift,
            "actionable_prescriptions": prescriptions,
            "historical_precedents": precedents,
            "periodic_tracker_cli_template": (
                f'python3 toolkit/periodic_tracker.py --case my-forecasts add '
                f'--id "opt-{year_now}-001" --domain "{canon_dom}" '
                f'--statement "<按处方收敛后的冻结承诺>" --horizon "{horizon_label}" '
                f'--scope "<权威数据源与分母口径>" '
                f'--method "{best["method_name"]}（推导链：{" -> ".join(best["derivation_steps"])}）" '
                f'--counter-lens "{best["recommended_counter_lens"]}" '
                f'--indicators "{leading_indicators or best["leading_indicator_template"]}" '
                f'--falsification "<明确证伪阈值>"'
            ),
        }

    def query_reference_class(
        self,
        *,
        domain: str,
        horizon_years: float = 10.0,
        is_explicit: bool = True,
        forecaster_stance: str = "国际机构与政府智库",
        keyword: str = "",
    ) -> dict[str, Any]:
        canon_dom = normalize_domain(domain)
        bucket = window_to_horizon_bucket(horizon_years)
        rec = {
            "domain": canon_dom,
            "author_type": normalize_archetype(forecaster_stance),
            "horizon_bucket": bucket,
            "horizon_source": "explicit" if is_explicit else "implicit_publication_to_cutoff",
            "is_classical_philosophy": 0.0,
        }
        p_heb, meta = self.heb.predict_one(rec)
        dec = max(1.0 - p_heb[4], 1e-8)

        # Top benchmark books in same domain from all_cases_summary.csv
        books = [
            r for r in self._summary_rows()
            if r["领域"] == canon_dom and int(r["可判定数"]) >= 15
        ]
        books.sort(key=lambda r: float(r["同档超额严格胜率_pp"].replace("pp", "") or 0.0), reverse=True)
        top_books = [
            {
                "slug": b["slug"],
                "title": f"{b['作者']}《{b['书名']}》({b['出版年']})",
                "window_bucket": b["时间跨度分档"],
                "decided_n": int(b["可判定数"]),
                "strict_win_rate": b["严格胜率"],
                "directional_rate": b["方向命中率"],
                "error_rate": b["错误率"],
                "excess_strict_vs_peers": b["同档超额严格胜率_pp"],
            }
            for b in books[:5]
        ]
        precedents = self.retrieve_precedents(canon_dom, keyword or canon_dom, top_k=3)
        return {
            "canonical_domain": canon_dom,
            "horizon_bucket": bucket,
            "empirical_bayes_5class": {VERDICTS_5[c]: round(p_heb[c], 4) for c in range(5)},
            "empirical_bayes_decided_rates": {
                "strict_win_rate": round(p_heb[0] / dec, 4),
                "directional_hit_rate": round((p_heb[0] + p_heb[1]) / dec, 4),
                "partial_rate": round(p_heb[2] / dec, 4),
                "error_rate": round(p_heb[3] / dec, 4),
                "unresolved_rate": round(p_heb[4], 4),
            },
            "stratum_sample_sizes": meta,
            "top_domain_benchmark_works": top_books,
            "matched_precedents": precedents,
        }

    def backtest_historical_tech(self, max_pub_year: int = 2021) -> dict[str, Any]:
        """Run blind ex-ante backtest of the 4-layer Bass S-curve differentiation test across
        all decided technology & AI predictions published on or before max_pub_year.
        """
        forecasts, _, _ = load_training_corpus(self.repo_root)
        tech_decided = [
            r for r in forecasts
            if r["verdict"] != "暂无法判断"
            and int(r["pub_year"]) <= max_pub_year
            and r["domain"] in ("科技、商业与产业颠覆", "AI与奇点前沿")
        ]
        by_speed: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
        by_layer: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)

        for r in tech_decided:
            txt_all = f"{r['time_text']} {r['quote']} {r['claim']}"
            sp = parse_explicit_span(txt_all, int(r["pub_year"]))
            eff_span = sp if sp is not None else float(r["window_years"])
            td = self.evaluate_tech_differentiation(
                statement=f"{r['quote']} {r['claim']}",
                domain=r["domain"],
                horizon_years=eff_span,
            )
            by_speed[td["differentiation_verdict_code"]][r["verdict"]] += 1
            by_layer[td["assigned_friction_layer"]["layer_id"]][r["verdict"]] += 1

        def summarize(grp: dict[str, collections.Counter[str]]) -> dict[str, dict[str, Any]]:
            out = {}
            for k, cnt in sorted(grp.items()):
                n = sum(cnt.values())
                if n == 0:
                    continue
                out[k] = {
                    "decided_n": n,
                    "strict_win_rate": round(cnt["正确"] / n, 4),
                    "directional_hit_rate": round((cnt["正确"] + cnt["趋势符合"]) / n, 4),
                    "partial_rate": round(cnt["部分符合"] / n, 4),
                    "error_rate": round(cnt["错误"] / n, 4),
                }
            return out

        return {
            "max_publication_year": max_pub_year,
            "total_decided_tech_forecasts": len(tech_decided),
            "by_ex_ante_speed_verdict": summarize(by_speed),
            "by_friction_layer": summarize(by_layer),
        }

    def bayesian_update(
        self,
        *,
        prior_decided_probs: dict[str, float] | None = None,
        statement: str = "",
        domain: str = "",
        horizon_years: float = 5.0,
        evidence_items: list[dict[str, str]],
    ) -> dict[str, Any]:
        """Three-axis (Event / Mechanism / Time) damped Log-Odds Bayesian Updater.

        Prevents confirmation bias and premature convergence:
        - Event-axis official statistics move outcome log-odds directly;
        - Mechanism-only evidence shifts '趋势符合' / '部分符合' without falsely certifying endpoint '正确';
        - Time-axis lag shifts mass from '正确' toward '趋势符合' / '部分符合'.
        """
        if prior_decided_probs:
            p = [float(prior_decided_probs.get(v, 0.25)) for v in VERDICTS_4]
            s = sum(p)
            prior = [v / s for v in p]
        else:
            opt = self.optimize_forecast(statement=statement or "待更新预测", domain=domain, target_years=horizon_years)
            d4 = opt["baseline_evaluation"]["probs_decided_4class"]
            prior = [d4[v] for v in VERDICTS_4]

        tier_weights = {
            "official_stats": 1.0,
            "institutional": 0.80,
            "filing": 0.75,
            "academic": 0.65,
            "media": 0.30,
        }
        logits = [math.log(max(v, 1e-6)) for v in prior]
        trace = []

        for item in evidence_items:
            rel = (item.get("relation") or "support").lower()
            tier = (item.get("source_tier") or "institutional").lower()
            axis = (item.get("axis") or "event").lower()
            w = tier_weights.get(tier, 0.50)

            delta = [0.0, 0.0, 0.0, 0.0]  # [正确, 趋势符合, 部分符合, 错误]
            if axis == "event":
                if rel == "support":
                    delta = [0.42 * w, 0.35 * w, -0.05 * w, -0.45 * w]
                elif rel == "counter":
                    delta = [-0.45 * w, -0.30 * w, 0.10 * w, 0.50 * w]
                else:  # boundary / mixed
                    delta = [-0.15 * w, 0.05 * w, 0.35 * w, -0.05 * w]
            elif axis == "mechanism":
                # Mechanism validation never alone proves endpoint '正确' (Signal & Noise Rule §3.3!)
                if rel == "support":
                    delta = [0.12 * w, 0.32 * w, 0.05 * w, -0.25 * w]
                elif rel == "counter":
                    delta = [-0.20 * w, -0.15 * w, 0.25 * w, 0.22 * w]
                else:
                    delta = [-0.05 * w, 0.05 * w, 0.25 * w, 0.0]
            elif axis == "time":
                if rel == "support":  # on-schedule or ahead
                    delta = [0.30 * w, 0.15 * w, -0.10 * w, -0.25 * w]
                elif rel == "counter":  # delayed / bottleneck lag
                    delta = [-0.38 * w, 0.22 * w, 0.20 * w, 0.18 * w]
                else:
                    delta = [-0.15 * w, 0.20 * w, 0.15 * w, 0.0]

            logits = [logits[c] + delta[c] for c in range(4)]
            cur_p = softmax(logits)
            trace.append({
                "summary": item.get("summary", ""),
                "axis": axis,
                "relation": rel,
                "source_tier": tier,
                "posterior_after_step": {VERDICTS_4[c]: round(cur_p[c], 4) for c in range(4)},
            })

        post = softmax(logits)
        has_support = any((e.get("relation") or "").lower() == "support" for e in evidence_items)
        has_counter = any((e.get("relation") or "").lower() == "counter" for e in evidence_items)
        bias_warning = None
        if evidence_items and not (has_support and has_counter):
            bias_warning = "确认偏误告警：当前仅输入了单向证据，按《信号与噪音》双向搜证铁律，正式改判前必须补充反面/摩擦证据检索！"

        return {
            "prior_decided_4class": {VERDICTS_4[c]: round(prior[c], 4) for c in range(4)},
            "posterior_decided_4class": {VERDICTS_4[c]: round(post[c], 4) for c in range(4)},
            "prior_directional_prob": round(prior[0] + prior[1], 4),
            "posterior_directional_prob": round(post[0] + post[1], 4),
            "net_shift_pp": {VERDICTS_4[c]: round((post[c] - prior[c]) * 100.0, 2) for c in range(4)},
            "confirmation_bias_warning": bias_warning,
            "step_trace": trace,
        }

    def audit_ledger(self, case_dir: Path) -> dict[str, Any]:
        claims_path = case_dir / "data" / "claims.jsonl"
        if not claims_path.is_file():
            raise FileNotFoundError(f"Missing claims.jsonl in {case_dir}")
        rows = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        results = []
        for r in rows:
            a = r.get("assessment") or {}
            if a.get("inclusion", "forecast") != "forecast":
                continue
            meta = r.get("review_metadata") or {}
            opt = self.optimize_forecast(
                statement=r.get("claim") or r.get("quote") or "",
                domain=meta.get("domain") or r.get("family") or "",
                horizon=r.get("time_text") or a.get("future_time_text") or "",
                scope=a.get("scope") or "",
                condition_text=r.get("condition_text") or "",
                method=r.get("method") or "",
                leading_indicators=meta.get("leading_indicators") or "",
                falsification=meta.get("falsification") or "",
                forecaster_stance="国际机构与政府智库",
            )
            results.append({
                "id": r["id"],
                "current_verdict": a.get("verdict", "暂无法判断"),
                "operationalizability_score": opt["operationalizability_audit"]["score_out_of_6"],
                "traps_count": len(opt["operationalizability_audit"]["traps_detected"]),
                "baseline_probs_decided": opt["baseline_evaluation"]["probs_decided_4class"],
                "recommended_method": opt["recommended_optimization"]["method_name"],
                "expected_uplift": opt["expected_uplift"],
                "prescriptions": opt["actionable_prescriptions"],
            })
        return {
            "ledger_dir": str(case_dir),
            "forecast_count": len(results),
            "items": results,
        }


def train_and_benchmark(
    repo_root: Path = REPO_ROOT,
    model_out: Path = DEFAULT_MODEL_PATH,
    benchmark_out: Path = DEFAULT_BENCHMARK_PATH,
    save: bool = True,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Run 5-fold Out-of-Book Grouped CV tournament across 7 academic models + fit full Super-Learner."""
    t_start = time.time()
    summary_csv = repo_root / "datasets" / "all_cases_summary.csv"
    with open(summary_csv, encoding="utf-8-sig") as f:
        summary_rows = list(csv.DictReader(f))
    expected_forecasts = sum(int(r["预测数"]) for r in summary_rows)
    n_works = len(summary_rows)
    forecasts, nonforecasts, _ = load_training_corpus(repo_root)
    if len(forecasts) != expected_forecasts:
        raise RuntimeError(f"Expected {expected_forecasts:,} forecasts across {n_works} works, got {len(forecasts):,}")

    slugs = sorted({r["case_slug"] for r in forecasts})
    rng = random.Random(20261124)
    rng.shuffle(slugs)
    slug_to_fold = {s: idx % 5 for idx, s in enumerate(slugs)}
    y5_all = [VERDICTS_5.index(r["verdict"]) for r in forecasts]

    oof: dict[str, list[list[float]]] = {
        name: [[] for _ in range(len(forecasts))]
        for name in [
            "M0_Uniform_Marginal_Prior",
            "M1_Static_Horizon_Explicit_Table",
            "M2_Hierarchical_Empirical_Bayes",
            "M3_Regularized_GLMM_NoHist_Ablation",
            "M4_Regularized_GLMM_Full_Hist_Lenses",
            "M5_HistXGBoost_Direct_5Class",
            "M6_TwoStage_Censored_HistXGBoost",
            "M7_Calibrated_LogLinear_SuperLearner",
        ]
    }

    for fold in range(5):
        tr_idx = [i for i, r in enumerate(forecasts) if slug_to_fold[r["case_slug"]] != fold]
        va_idx = [i for i, r in enumerate(forecasts) if slug_to_fold[r["case_slug"]] == fold]
        tr_recs = [forecasts[i] for i in tr_idx]
        va_recs = [forecasts[i] for i in va_idx]
        y_tr = [y5_all[i] for i in tr_idx]

        pit_tr = compute_pit_priors_fast(tr_recs, tr_recs)
        pit_va = compute_pit_priors_fast(tr_recs, va_recs)
        X_tr = [extract_features(r, p) for r, p in zip(tr_recs, pit_tr)]
        X_va = [extract_features(r, p) for r, p in zip(va_recs, pit_va)]

        # M0: Marginal
        cnt0 = [sum(1 for y in y_tr if y == c) for c in range(5)]
        p0 = [c / len(y_tr) for c in cnt0]
        for idx in va_idx:
            oof["M0_Uniform_Marginal_Prior"][idx] = p0

        # M1: Static Horizon x Explicitness table
        tab1: dict[tuple[str, str], list[float]] = collections.defaultdict(lambda: [1.0] * 5)
        for r, y in zip(tr_recs, y_tr):
            tab1[(r["horizon_bucket"], r["horizon_source"])][y] += 1.0
        for idx, r in zip(va_idx, va_recs):
            cvec = tab1[(r["horizon_bucket"], r["horizon_source"])]
            s = sum(cvec)
            oof["M1_Static_Horizon_Explicit_Table"][idx] = [v / s for v in cvec]

        # M2: Hierarchical Empirical Bayes
        heb = HierarchicalEmpiricalBayes(5).fit(tr_recs, y_tr)
        for idx, p in zip(va_idx, heb.predict_proba(va_recs)):
            oof["M2_Hierarchical_Empirical_Bayes"][idx] = p

        # M3: Ablation GLMM without historical regime, PIT priors, or method lenses
        def strip_ablation(d: dict[str, float]) -> dict[str, float]:
            return {
                k: v for k, v in d.items()
                if not k.startswith(("hist_", "pit_", "m_", "s_", "ix_"))
            }

        m3 = MultinomialLogReg(5, l2=3.0, lr=0.05, epochs=45).fit([strip_ablation(x) for x in X_tr], y_tr)
        for idx, p in zip(va_idx, m3.predict_proba([strip_ablation(x) for x in X_va])):
            oof["M3_Regularized_GLMM_NoHist_Ablation"][idx] = p

        # M4: Full GLMM
        m4 = MultinomialLogReg(5, l2=3.0, lr=0.05, epochs=45).fit(X_tr, y_tr)
        for idx, p in zip(va_idx, m4.predict_proba(X_va)):
            oof["M4_Regularized_GLMM_Full_Hist_Lenses"][idx] = p

        # M5: Direct 5-class HistXGBoost
        m5 = HistXGBoostMulticlass(5, n_estimators=85, lr=0.08, max_depth=3, min_child_hess=5.0, reg_lambda=10.0).fit(X_tr, y_tr)
        for idx, p in zip(va_idx, m5.predict_proba(X_va)):
            oof["M5_HistXGBoost_Direct_5Class"][idx] = p

        # M6: Two-Stage Censored Hazard x Conditional 4-Class HistXGBoost
        y_dec_tr = [0 if y == 4 else 1 for y in y_tr]
        s1 = HistXGBoostMulticlass(2, n_estimators=75, lr=0.08, max_depth=3, min_child_hess=5.0, reg_lambda=10.0).fit(X_tr, y_dec_tr)
        dec_X = [x for x, y in zip(X_tr, y_tr) if y < 4]
        dec_y = [y for y in y_tr if y < 4]
        s2 = HistXGBoostMulticlass(4, n_estimators=80, lr=0.08, max_depth=3, min_child_hess=4.0, reg_lambda=10.0).fit(dec_X, dec_y)
        for idx, a, b in zip(va_idx, s1.predict_proba(X_va), s2.predict_proba(X_va)):
            oof["M6_TwoStage_Censored_HistXGBoost"][idx] = [a[1] * b[0], a[1] * b[1], a[1] * b[2], a[1] * b[3], a[0]]

    # Nested OOF optimization of Log-Linear Opinion Pool weights + Temperature
    fold_weights = []
    for fold in range(5):
        tr_idx = [i for i, r in enumerate(forecasts) if slug_to_fold[r["case_slug"]] != fold]
        va_idx = [i for i, r in enumerate(forecasts) if slug_to_fold[r["case_slug"]] == fold]
        y_tr = [y5_all[i] for i in tr_idx]
        cands_tr = [
            [oof["M2_Hierarchical_Empirical_Bayes"][i] for i in tr_idx],
            [oof["M4_Regularized_GLMM_Full_Hist_Lenses"][i] for i in tr_idx],
            [oof["M5_HistXGBoost_Direct_5Class"][i] for i in tr_idx],
            [oof["M6_TwoStage_Censored_HistXGBoost"][i] for i in tr_idx],
        ]
        best_obj = 1e9
        best_cfg = (0.05, 0.20, 0.35, 0.40, 1.05)
        for w0 in (0.05, 0.10):
            for w1 in (0.15, 0.25):
                for w2 in (0.25, 0.35, 0.45):
                    w3 = round(1.0 - w0 - w1 - w2, 4)
                    if w3 < 0.15:
                        continue
                    for temp in (0.95, 1.0, 1.05, 1.10):
                        p_tr = log_linear_pool(cands_tr, (w0, w1, w2, w3), temp)
                        obj = logloss_multiclass(p_tr, y_tr) + 0.5 * brier_multiclass(p_tr, y_tr, 5)
                        if obj < best_obj:
                            best_obj = obj
                            best_cfg = (w0, w1, w2, w3, temp)
        fold_weights.append(best_cfg)
        cands_va = [
            [oof["M2_Hierarchical_Empirical_Bayes"][i] for i in va_idx],
            [oof["M4_Regularized_GLMM_Full_Hist_Lenses"][i] for i in va_idx],
            [oof["M5_HistXGBoost_Direct_5Class"][i] for i in va_idx],
            [oof["M6_TwoStage_Censored_HistXGBoost"][i] for i in va_idx],
        ]
        for idx, p in zip(va_idx, log_linear_pool(cands_va, best_cfg[:4], best_cfg[4])):
            oof["M7_Calibrated_LogLinear_SuperLearner"][idx] = p

    dec_idx = [i for i, y in enumerate(y5_all) if y < 4]
    y4_dec = [y5_all[i] for i in dec_idx]
    model_metrics = {}
    for name, preds in oof.items():
        b5 = brier_multiclass(preds, y5_all, 5)
        ll5 = logloss_multiclass(preds, y5_all)
        ece_u = expected_calibration_error([p[4] for p in preds], [1 if y == 4 else 0 for y in y5_all])
        preds4 = [[v / max(sum(preds[i][:4]), 1e-12) for v in preds[i][:4]] for i in dec_idx]
        b4 = brier_multiclass(preds4, y4_dec, 4)
        ll4 = logloss_multiclass(preds4, y4_dec)
        rps4 = rps_ordinal(preds4, y4_dec, 4)
        ece_d = expected_calibration_error([p[0] + p[1] for p in preds4], [1 if y in (0, 1) else 0 for y in y4_dec])
        ece_e = expected_calibration_error([p[3] for p in preds4], [1 if y == 3 else 0 for y in y4_dec])
        model_metrics[name] = {
            "brier_5class": round(b5, 4),
            "logloss_5class": round(ll5, 4),
            "ece_unresolved": round(ece_u, 4),
            "decided_brier_4class": round(b4, 4),
            "decided_logloss_4class": round(ll4, 4),
            "decided_ordinal_rps": round(rps4, 4),
            "decided_ece_directional": round(ece_d, 4),
            "decided_ece_error": round(ece_e, 4),
        }

    # Fit final production models on 100% of the corpus
    pit_full = compute_pit_priors_fast(forecasts, forecasts)
    X_full = [extract_features(r, p) for r, p in zip(forecasts, pit_full)]

    heb_full = HierarchicalEmpiricalBayes(5).fit(forecasts, y5_all)
    maxent_full = MultinomialLogReg(5, l2=3.0, lr=0.05, epochs=45).fit(X_full, y5_all)
    xgb_direct_full = HistXGBoostMulticlass(5, n_estimators=85, lr=0.08, max_depth=3, min_child_hess=5.0, reg_lambda=10.0).fit(X_full, y5_all)
    y_dec_full = [0 if y == 4 else 1 for y in y5_all]
    xgb_s1_full = HistXGBoostMulticlass(2, n_estimators=75, lr=0.08, max_depth=3, min_child_hess=5.0, reg_lambda=10.0).fit(X_full, y_dec_full)
    dec_X_full = [x for x, y in zip(X_full, y5_all) if y < 4]
    dec_y_full = [y for y in y5_all if y < 4]
    xgb_s2_full = HistXGBoostMulticlass(4, n_estimators=80, lr=0.08, max_depth=3, min_child_hess=4.0, reg_lambda=10.0).fit(dec_X_full, dec_y_full)

    all_cands = forecasts + nonforecasts
    y_s0 = [1] * len(forecasts) + [0] * len(nonforecasts)
    X_s0 = [extract_features(r) for r in all_cands]
    denoiser_full = HistXGBoostMulticlass(2, n_estimators=65, lr=0.08, max_depth=3, min_child_hess=5.0, reg_lambda=10.0).fit(X_s0, y_s0)

    avg_w = [round(sum(fw[i] for fw in fold_weights) / 5.0, 4) for i in range(4)]
    w_sum = sum(avg_w)
    avg_w = [round(v / w_sum, 4) for v in avg_w]
    avg_temp = round(sum(fw[4] for fw in fold_weights) / 5.0, 4)

    modern_dummy = [{"domain": dom, "pub_year": 2026} for dom in CANONICAL_DOMAINS]
    modern_pits = dict(zip(CANONICAL_DOMAINS, compute_pit_priors_fast(forecasts, modern_dummy)))
    cmh_effects = compute_cmh_stratified_effects(forecasts)
    elapsed = round(time.time() - t_start, 2)

    benchmark_report = {
        "schema_version": "forecast-optimizer-benchmark-v1",
        "evaluation_protocol": "5-Fold Out-of-Book Grouped Cross-Validation by case_slug (zero book/author leakage)",
        "corpus_counts": {
            "independent_works": n_works,
            "total_candidates": len(all_cands),
            "scored_forecasts": len(forecasts),
            "decided_forecasts": len(dec_idx),
            "excluded_nonforecasts": len(nonforecasts),
            "publication_year_span": "1531-2026",
        },
        "models": model_metrics,
        "selected_production_architecture": "M7_Calibrated_LogLinear_SuperLearner",
        "ensemble_weights": {
            "Hierarchical_Empirical_Bayes": avg_w[0],
            "Regularized_GLMM_Hist_Lenses": avg_w[1],
            "HistXGBoost_Direct_5Class": avg_w[2],
            "TwoStage_Censored_HistXGBoost": avg_w[3],
            "temperature_T": avg_temp,
        },
        "cmh_stratified_method_and_trap_effects": cmh_effects,
        "top_xgboost_feature_gains": xgb_direct_full.to_dict()["feature_gain"],
        "training_wall_seconds": elapsed,
    }

    model_bundle = {
        "schema_version": "forecast-optimizer-model-v1",
        "trained_on_works": n_works,
        "trained_on_forecasts": len(forecasts),
        "trained_on_nonforecasts": len(nonforecasts),
        "pool_weights": avg_w,
        "temperature": avg_temp,
        "modern_pit_priors": modern_pits,
        "cmh_effects": cmh_effects,
        "benchmark_summary": model_metrics["M7_Calibrated_LogLinear_SuperLearner"],
        "heb": heb_full.to_dict(),
        "maxent": maxent_full.to_dict(),
        "xgb_direct": xgb_direct_full.to_dict(),
        "xgb_stage1_hazard": xgb_s1_full.to_dict(),
        "xgb_stage2_decided": xgb_s2_full.to_dict(),
        "stage0_denoiser": denoiser_full.to_dict(),
    }
    raw_bytes = json.dumps(model_bundle, ensure_ascii=False, sort_keys=True).encode("utf-8")
    model_bundle["artifact_sha256"] = hashlib.sha256(raw_bytes).hexdigest()

    if save:
        model_out.parent.mkdir(parents=True, exist_ok=True)
        model_out.write_text(json.dumps(model_bundle, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        benchmark_out.write_text(json.dumps(benchmark_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return model_bundle, benchmark_report


# ---------------------------------------------------------------------------
# Markdown Report Formatter & CLI Entrypoint
# ---------------------------------------------------------------------------

def format_optimization_markdown(res: dict[str, Any]) -> str:
    inp = res["input_summary"]
    aud = res["operationalizability_audit"]
    base = res["baseline_evaluation"]
    opt = res["recommended_optimization"]
    up = res["expected_uplift"]
    b4 = base["probs_decided_4class"]
    o4 = opt["calibrated_probs_decided_4class"]

    lines = [
        "# Forecast Lab 数据驱动预测方法优化报告",
        "",
        f"- **原始命题**：{inp['statement']}",
        f"- **归属领域**：`{inp['canonical_domain']}` ｜ **评估跨度**：`{inp['evaluation_horizon_years']:.1f} 年`（`{inp['horizon_bucket']}`）",
        f"- **可操作化体检得分**：`{aud['score_out_of_6']}/6` ｜ **有效预测置信度**：`{base['is_valid_forecast_prob']:.1%}`",
        "",
        "## 1. 样本外校准概率对比（优化前基线 vs 最优方法干预）",
        "",
        "| 指标（基于已判定条件分布） | 原始草案基线 | 优化后预期 | 边际改善 (Δ) |",
        "| :--- | ---: | ---: | ---: |",
        f"| **严格胜率 P(正确)** | {base['strict_win_prob_given_decided']:.1%} | **{opt['strict_win_prob_given_decided']:.1%}** | `{up['delta_strict_win_prob_pp']:+.2f}pp` |",
        f"| **方向命中率 P(正确+趋势)** | {base['directional_hit_prob_given_decided']:.1%} | **{opt['directional_hit_prob_given_decided']:.1%}** | `{up['delta_directional_hit_prob_pp']:+.2f}pp` |",
        f"| **部分符合率 P(部分符合)** | {b4['部分符合']:.1%} | {o4['部分符合']:.1%} | `{(o4['部分符合'] - b4['部分符合']) * 100:+.2f}pp` |",
        f"| **明确翻车率 P(错误)** | {base['error_prob_given_decided']:.1%} | **{opt['error_prob_given_decided']:.1%}** | `{up['delta_error_prob_pp']:+.2f}pp` |",
        f"| **不可判定风险 P(暂无法判断)** | {base['unresolved_prob']:.1%} | **{opt['unresolved_prob']:.1%}** | `{up['delta_unresolved_prob_pp']:+.2f}pp` |",
        "",
        "## 2. 最优预测方法与四步推导链（最终预测必写项）",
        "",
        f"- **首选主方法**：**{opt['method_name']}**（标杆参照：{'、'.join(opt['exemplars'])}）",
        f"- **方法四步推导链**：",
        *[f"  - {step}" for step in opt["derivation_steps"]],
        f"- **必配反校验透镜**：{opt['recommended_counter_lens']}",
        f"- **承诺硬度策略**：{opt['commitment_label']}",
        f"- **推荐领先观测指标**：{opt['leading_indicator_template']}",
        "",
    ]
    td = res.get("tech_differentiation_audit")
    if td:
        pa = td["primary_structural_analog"]
        rng = td["calibrated_share_range_in_horizon"]
        lines += [
            "## 2.5 新技术“这次是否不一样？”历史同构扩散曲线 × 实时瓶颈校准",
            "",
            f"- **摩擦层级定位**：**{td['assigned_friction_layer']['name']}** —— *{td['assigned_friction_layer']['is_different_verdict']}*",
            f"- **统计分母性质**：`{td['scope_mode']}`（基线 `{td['assumed_baseline_share']:.1%}` → 目标 `{td['target_share_evaluated']:.1%}`，窗口 `{td['target_horizon_years']:.1f} 年`）",
            f"- **最接近的历史同构前辈**：**{pa['name']}**（增量 5%→50% 历时 `{pa['flow_5_to_50_years']} 年`，存量更替历时 `{pa['stock_5_to_50_years']} 年`；书库锚点：{pa['archive_anchor']}）",
            f"- **Bass 扩散斜率压力测试**：**{td['differentiation_verdict']}**（历史同构需 `{td['historical_analog_required_years']} 年`；`{td['target_horizon_years']:.1f} 年`内 1.0x–1.5x 校准合理渗透区间为 **`{rng['historical_1x_baseline']:.1%} – {rng['accelerated_1_5x_catalyst']:.1%}`**）",
            f"- **杰文斯需求弹性提示**：{td['jevons_elasticity_effect']}",
            f"- **必须联网核查的当下实时瓶颈参数（用今天的新事实修正历史斜率）**：",
            *[f"  - 🔍 {param}" for param in td["realtime_parameters_to_fetch_now"]],
            "",
        ]
    lines += [
        "## 3. 逐条可执行优化处方",
        "",
    ]
    for idx, p in enumerate(res["actionable_prescriptions"], 1):
        lines.append(f"{idx}. {p}")

    lines += ["", "## 4. 全库同领域正反历史先例锚点", ""]
    for item in res["historical_precedents"]["best_signal_exemplars"][:2]:
        lines.append(f"- ✅ **成功范式 [{item['id']}]** {item['book']}（`{item['tag']}`）：{item['claim']}")
    for item in res["historical_precedents"]["failure_anti_precedents"][:2]:
        lines.append(f"- ⚠️ **翻车警示 [{item['id']}]** {item['book']}（`{item['tag']}`）：{item['claim']} → *{item['lesson_or_indicator']}*")

    lines += [
        "",
        "## 5. 标准终局输出模板（预测结论 + 显式预测方法一体交付）",
        "",
        res["final_forecast_card_markdown"],
        "",
        "## 6. 一键登记入库命令模板",
        "",
        "```bash",
        res["periodic_tracker_cli_template"],
        "```",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Forecast Lab data-driven forecast method optimizer")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_train = sub.add_parser("train", help="Run 5-fold out-of-book CV tournament and save fitted Super-Learner artifact")
    p_train.add_argument("--model-out", type=Path, default=DEFAULT_MODEL_PATH)
    p_train.add_argument("--benchmark-out", type=Path, default=DEFAULT_BENCHMARK_PATH)

    p_bench = sub.add_parser("benchmark", help="Display saved out-of-book cross-validation benchmark metrics")
    p_bench.add_argument("--benchmark-path", type=Path, default=DEFAULT_BENCHMARK_PATH)

    p_opt = sub.add_parser("optimize", help="Audit and optimize a draft forecast proposition and reasoning method")
    p_opt.add_argument("--statement", required=True, help="Draft forecast statement")
    p_opt.add_argument("--domain", default="", help="Forecast domain")
    p_opt.add_argument("--horizon", default="", help="Target horizon text, e.g. '2026-2030' or '到2029年底'")
    p_opt.add_argument("--target-years", type=float, default=None, help="Explicit numeric horizon in years")
    p_opt.add_argument("--scope", default="", help="Measurement scope and authoritative data source")
    p_opt.add_argument("--condition", default="", help="Triggering condition")
    p_opt.add_argument("--method", default="", help="Current reasoning method")
    p_opt.add_argument("--counter-lens", default="", help="Current counter-lens")
    p_opt.add_argument("--indicators", default="", help="Leading indicators")
    p_opt.add_argument("--falsification", default="", help="Falsification threshold")
    p_opt.add_argument("--stance", default="科技商业思想家与产业实践者", help="Baseline forecaster stance")
    p_opt.add_argument("--format", choices=["markdown", "json"], default="markdown")

    p_ref = sub.add_parser("reference-class", help="Query Empirical Bayes base rates and historical precedents")
    p_ref.add_argument("--domain", required=True)
    p_ref.add_argument("--horizon-years", type=float, default=10.0)
    p_ref.add_argument("--implicit", action="store_true")
    p_ref.add_argument("--keyword", default="")

    p_upd = sub.add_parser("update", help="Run three-axis Bayesian posterior update with new evidence")
    p_upd.add_argument("--statement", default="")
    p_upd.add_argument("--domain", default="")
    p_upd.add_argument("--horizon-years", type=float, default=5.0)
    p_upd.add_argument("--prior-json", default="", help="Optional JSON dict of 4-class prior probabilities")
    p_upd.add_argument("--evidence-json", required=True, help="JSON list of evidence objects")

    p_led = sub.add_parser("audit-ledger", help="Batch-audit and optimize all forecasts in a ledger directory")
    p_led.add_argument("--case", type=Path, default=REPO_ROOT / "my-forecasts")

    p_tech = sub.add_parser("tech-analog", help="Test 'Is This New Technology Different?' against 150-year historical S-curve analogs")
    p_tech.add_argument("--statement", required=True, help="Technology adoption/disruption claim")
    p_tech.add_argument("--domain", default="", help="Forecast domain")
    p_tech.add_argument("--scope", default="", help="Denominator scope")
    p_tech.add_argument("--horizon-years", type=float, default=None, help="Target horizon in years")
    p_tech.add_argument("--current-share", type=float, default=None, help="Current baseline penetration in (0, 1)")
    p_tech.add_argument("--target-share", type=float, default=None, help="Target penetration in (0, 1)")
    p_tech.add_argument("--stock", action="store_true", help="Force installed-stock / headcount replacement mode")

    p_bt = sub.add_parser("backtest-tech", help="Run blind ex-ante backtest on resolved historical tech/AI forecasts")
    p_bt.add_argument("--max-pub-year", type=int, default=2021)

    args = parser.parse_args(argv)

    if args.cmd == "train":
        _, bench = train_and_benchmark(model_out=args.model_out, benchmark_out=args.benchmark_out, save=True)
        print(json.dumps(bench, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "benchmark":
        if not args.benchmark_path.is_file():
            _, bench = train_and_benchmark(save=True)
        else:
            bench = json.loads(args.benchmark_path.read_text(encoding="utf-8"))
        print(json.dumps(bench, ensure_ascii=False, indent=2))
        return 0

    engine = ForecastOptimizerEngine.load()

    if args.cmd == "optimize":
        res = engine.optimize_forecast(
            statement=args.statement,
            domain=args.domain,
            horizon=args.horizon,
            target_years=args.target_years,
            scope=args.scope,
            condition_text=args.condition,
            method=args.method,
            counter_lens=args.counter_lens,
            leading_indicators=args.indicators,
            falsification=args.falsification,
            forecaster_stance=args.stance,
        )
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
        else:
            print(format_optimization_markdown(res))
        return 0

    if args.cmd == "reference-class":
        res = engine.query_reference_class(
            domain=args.domain,
            horizon_years=args.horizon_years,
            is_explicit=not args.implicit,
            keyword=args.keyword,
        )
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "update":
        prior = json.loads(args.prior_json) if args.prior_json else None
        ev_items = json.loads(args.evidence_json)
        res = engine.bayesian_update(
            prior_decided_probs=prior,
            statement=args.statement,
            domain=args.domain,
            horizon_years=args.horizon_years,
            evidence_items=ev_items,
        )
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "audit-ledger":
        res = engine.audit_ledger(args.case)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "tech-analog":
        res = engine.evaluate_tech_differentiation(
            statement=args.statement,
            domain=args.domain,
            scope=args.scope,
            horizon_years=args.horizon_years,
            current_penetration=args.current_share,
            target_penetration=args.target_share,
            is_stock_scope=True if args.stock else None,
        )
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "backtest-tech":
        res = engine.backtest_historical_tech(max_pub_year=args.max_pub_year)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
