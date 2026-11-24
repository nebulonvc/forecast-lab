# 经合组织《数字经济展望2024（第二卷）：加强连接、创新与信任》（OECD Digital Economy Outlook 2024 (Volume 2): Strengthening Connectivity, Innovation and Trust）：出版后预测人工核查

- 案例目录：`cases/oecd-digital-economy-outlook-2024-vol2-v5/`
- 出版日期：经合组织 **2024 年 11 月 19 日**发布（PDF CreationDate 2024-11-15），按 2024-11 起算。正文用 `reading-library/2026-11-15-未来判断扩展100本/05-技术与科学/079-oecd-digital-economy-outlook-2024-volume-2-strengthening-connectivity-innovation-and-trust.pdf`（sha256 `896fa5f4…3114d`，与 OECD 官网 PDF 字节一致，223 页），经 `pdftotext -enc UTF-8` 生成 TXT（sha256 `589e4d45…2ace`，764,062 字符；TXT 不入库）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 222 块（3500 字符、600 字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 38 条候选、24 条可核验（resolvable；14 条转述他人的说法降为 unclear）。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（13 条做了适应性补充检索），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 24 条，剔除非预测 1 条，计入 **23 条预测**，其中 **15 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 9 |
| 趋势符合 | 6 |
| 部分符合 | 0 |
| 错误 | 0 |
| 暂无法判断 | 8 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **60.0%**（9/15） |
| 加权胜率 | **90.0%** |
| 错误率 | **0.0%**（0/15） |
| 未定占比（暂无法判断/预测） | 34.8%（8/23） |

## 总体评价

这份报告以政策盘点、统计数据和现状分析为主，明确的预测很少，222 块中只有 24 条可核验候选，其中 1 条（德国 IT 安全标签扩展到智能家居）在出版前已经发生，按出版前史实剔除，计入 23 条预测，且多为“将继续增加”“将带来影响”一类方向性判断。可判定的 15 条中，9 条正确（AI 与机器人改变技能需求、专门数字部委增多、地缘政治影响数字政策、每张 SIM 卡移动数据用量继续上升、网络需求增加、关键矿产需求大增、关键矿产竞争加剧、AI 推高 ICT 基础设施需求、MSP 仍是攻击目标），6 条趋势符合（巴西北部互联项目 12,000 公里光缆尚在推进、连通基础设施协同建设、全球升温很可能超过 1.5°C、能源系统更依赖数字技术、2050 年运输需求上升、ICT 供应链更加复杂）。没有部分符合和错误。生成式 AI 革新教学、自动化风险向低学历者转移、大模型个性化学习、电子垃圾增长、ICT 性别平等约需 90 年、量子计算颠覆密码学、AI 影响标签认证、量子纠错可能永远无法攻克等 8 条暂无法判断。出版到截止日只有约两年，趋势符合多是长期判断，窗口内只能确认方向；正确率高也部分源于这些方向性判断本身较为保守。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（9 条）

- **#1** 「Technological progress in AI and robotics will further transform skills demand.」  
  判断：**正确**。普华永道2025年全球AI就业晴雨表显示，AI暴露度最高职业中雇主所需技能的变化速度比暴露度最低职业快66%（上年为25%），技能需求转变在出版后的窗口内确实加速；斯坦福SIEPR简报提示就业冲击尚不明显，但不涉及技能需求方向。  
  来源：<https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/2025/report.pdf>；<https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality>
- **#2** 「The establishment of dedicated digital ministries, a trend likely to continue, can help in this respect.」  
  判断：**正确**。OECD《数字经济与社会展望2026》称2025年由专门数字部委主导国家数字战略的国家比例达60%（2016年24%），德国于2025年5月首次设立联邦数字部并任命首位数字部长（Euronews），设立专门数字部委的趋势在窗口内延续。  
  来源：<https://www.oecd.org/en/publications/oecd-digital-economy-and-society-outlook-2026_022ed474-en/full-report/digital-priorities-policies-and-governance_cde63c87.html>；<https://www.euronews.com/2025/05/07/merzs-government-decree-gives-german-digital-ministry-extensive-powers>
- **#3** 「geopolitics – including the Russian war of aggression in Ukraine – will affect digital policy making.」  
  判断：**正确**。欧盟2025年对外《国际数字战略》明确以地缘政治、安全与防务框定数字政策（EEAS），Intereconomics 2025年文章也指出美中科技冲突推动欧洲科技主权讨论，地缘政治确实在影响数字政策制定。  
  来源：<https://www.intereconomics.eu/contents/year/2025/number/2/article/mission-impossible-the-eu-s-search-for-an-independent-tech-policy-amid-us-china-decoupling.html>；<https://www.eeas.europa.eu/eeas/partnerships-security-global-governance-three-pillars-eu-international-digital-strategy_en>
- **#4** 「This trend will continue upwards with the increased adoption of 5G across OECD countries.」  
  判断：**正确**。Tefficient 2025年11月对40国的分析显示移动数据用量在多数市场同比继续增长（仅土耳其、卡塔尔下降），方向成立；麦肯锡指出增速放缓，但未出现下降。  
  来源：<https://tefficient.com/arpu-growth-softens-further-as-mobile-data-usage-growth-slows-in-half-of-the-countries/>；<https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/slowing-data-growth-a-new-telecommunications-paradigm>
- **#5** 「the demand on networks is only expected to increase」  
  判断：**正确**。ITU 2025年统计估计固定宽带流量由上年6.2 ZB增至2025年7.3 ZB，移动宽带约1.5 ZB，网络需求在窗口内继续增加。  
  来源：<https://www.itu.int/itu-d/reports/statistics/2025/10/15/ff25-internet-traffic/>
- **#12** 「the sector is a primary user of some critical minerals, for which the demand is expected to sharply increase i…」  
  判断：**正确**。IEA《2025年全球关键矿产展望》显示2024年锂需求增长近30%，远高于2010年代约10%的年增速，镍、钴、石墨和稀土需求增长6—8%，关键矿产需求在窗口内强劲上升。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>
- **#13** 「Market pressure and competition for critical minerals are expected to intensify as these minerals are essentia…」  
  判断：**正确**。IEA 2025年10月评论指出中国于2025年4月和10月对稀土等关键矿产实施新出口管制，供应集中风险“成为现实”；CNBC报道2025年11月中方暂停部分管制一年，但竞争与市场压力加剧的主结果已出现。  
  来源：<https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality>；<https://www.cnbc.com/2025/11/10/china-suspends-some-critical-mineral-export-curbs-to-the-us-as-trade-truce-takes-hold.html>
- **#14** 「Technologies like AI could further increase the demand for ICT infrastructure」  
  判断：**正确**。Dell'Oro数据显示2025年二季度全球数据中心资本开支同比增长43%、创纪录，预计全年增长30%以上，主要由AI部署驱动；IEEFA提示存在过度建设风险，但不否定需求上升。  
  来源：<https://www.delloro.com/news/hyperscaler-ai-deployments-lift-data-center-capex-to-record-highs-in-2q-2025/>；<https://ieefa.org/resources/risk-ai-driven-overbuilt-infrastructure-real>
- **#23** 「may indicate that MSPs will remain an attractive target for malicious actors」  
  判断：**正确**。Sophos 2025年5月披露DragonForce勒索团伙利用某MSP的SimpleHelp远程管理工具攻击其多家客户，CISA于2025年6月发布AA25-163A公告专门警示针对MSP及其客户的攻击，MSP在窗口内仍是攻击者的重要目标。  
  来源：<https://www.sophos.com/en-us/blog/dragonforce-actors-target-simplehelp-vulnerabilities-to-attack-msp-customers>；<https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

### 趋势符合（6 条）

- **#6** 「will extend 12 000 km of sub-fluvial fibre to connect broadband to 59 municipalities (10 million people) in th…」  
  判断：**趋势符合**。截至2026年6月，Norte Conectado已完成9条水下光纤干线中的5条（Teletime），巴西通信部2026年10月称已覆盖40个市镇、可惠及约580万人，Infovia 05预计2027年上半年完工；方向持续推进但书中“59个市镇、1000万人”的终点尚未达到。  
  来源：<https://www.gov.br/mcom/pt-br/noticias/2026/setembro/norte-conectado-ja-leva-internet-de-alta-capacidade-a-40-municipios-da-amazonia-e-pode-beneficiar-5-8-milhoes-de-pessoas>；<https://teletime.com.br/25/06/2026/norte-conectado-soma-5-infovias/>
- **#7** 「the co-integration of connectivity solutions will become increasingly important.」  
  判断：**趋势符合**。T-Mobile于2025年推出基于Starlink直连手机卫星的T-Satellite并在10月扩展到应用数据业务，地面与卫星网络的协同整合在窗口内实际落地；SpaceNews指出两行业融合仍有障碍，故仅记趋势符合。  
  来源：<https://www.t-mobile.com/news/network/t-satellite-data-ready-app-expansion>；<https://spacenews.com/the-merger-between-satellite-and-cellular-industries-not-yet-a-marriage-made-in-heaven/>
- **#11** 「These trends sound the alarm for a world that will likely exceed the 1.5°C temperature target of the Paris Agr…」  
  判断：**趋势符合**。WMO确认2024年全球均温约高出工业化前1.55°C，哥白尼2026年11月称2026年几乎必然第二次超过1.5°C、2023—2026四年平均也将超过；但《巴黎协定》按长期平均衡量的1.5°C尚未被正式突破，故记趋势符合。  
  来源：<https://wmo.int/news/media-centre/wmo-confirms-2024-warmest-year-record-about-155degc-above-pre-industrial-level>；<https://climate.copernicus.eu/2026-and-4-year-global-temperature-average-track-exceed-15degc-above-pre-industrial-levels>
- **#16** 「global energy systems will increasingly rely on digital technologies」  
  判断：**趋势符合**。IEA《能源与AI》（2025）称能源系统正变得“日益电气化、数字化、互联和分散化”并大量部署AI应用；ABB调查显示亚太仅不足15%企业充分利用数字工具，进展不均，记趋势符合。  
  来源：<https://www.iea.org/reports/energy-and-ai/ai-for-energy-optimisation-and-innovation>；<https://esgbusiness.com/exclusive/digital-tools-underused-in-asia-pacific-energy-transition-abb>
- **#17** 「Moreover, demand for transport is expected to increase by 2050.」  
  判断：**趋势符合**。终点为2050年；ICAO统计2024年定期航班旅客增至47亿人次、同比增7.9%，ITF统计2025年航空货运吨公里增3.4%，运输需求方向与预测一致但终点未到。  
  来源：<https://www.icao.int/about-icao/AnnualReport2024/world-air-transport-2024>；<https://www.itf-oecd.org/sites/default/files/docs/itf-key-transport-statistics-2026.pdf>
- **#22** 「Because the supply chain will keep increasing in complexity」  
  判断：**趋势符合**。Sonatype《2026年软件供应链状况报告》称2025年软件供应链进入“机器规模”、依赖图更大、复用更频繁，ICT供应链复杂性上升的方向得到支持；个别项目（如Eleventy）削减依赖属于反例但不改变总体方向。  
  来源：<https://www.sonatype.com/state-of-the-software-supply-chain/introduction>；<https://www.11ty.dev/blog/review-2025/>

### 暂无法判断（8 条）

- **#8** 「The use of generative artificial intelligence (AI) might revolutionise teaching and learning」  
  判断：**暂无法判断**。书中仅称生成式AI“可能”彻底改变教学；RAND显示2025年师生AI使用率上升约15个百分点，但斯坦福SCALE 2026年11月综述认为对学习结果的因果证据仍然混杂，“彻底改变”这一关键事实无法认定。  
  来源：<https://scale.stanford.edu/ai/evidence-base-review/evidence-base-ai-k12-november-review>；<https://www.rand.org/pubs/research_reports/RRA4180-1.html>
- **#9** 「Looking ahead, the risk of automation will increasingly fall on low-educated workers.」  
  判断：**暂无法判断**。缺少按受教育程度分组、跨期比较的自动化风险数据；ILO 2025年指出文书类职业暴露最高且专业技术岗位暴露上升，美联储笔记关注大学专业暴露，均不能确认风险“越来越多”落在低学历者身上。  
  来源：<https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure>；<https://www.federalreserve.gov/econres/notes/feds-notes/educational-exposure-to-generative-artificial-intelligence-20250226.html>
- **#10** 「Advances in large language models could unlock a future of increasingly personalised learning for students in …」  
  判断：**暂无法判断**。书中用“could”表述；2025年已有RCT显示AI辅导优于课堂主动学习（Scientific Reports），但另有研究指出现有聊天机器人个性化能力有限，“日益个性化的学习”是否普遍实现尚无决定性证据。  
  来源：<https://www.nature.com/articles/s41598-025-97652-6>；<https://doi.org/10.1007/s10639-025-13369-z>
- **#15** 「The ICT sector generates large amounts of electronic waste, which is expected to grow as demand for digital pr…」  
  判断：**暂无法判断**。出版后检索到的全球电子垃圾数据仍引用2022年6200万吨（UNEP 2025年转述2024年报告），没有2023年以后的全球实测值，无法确认ICT电子垃圾在窗口内是否继续增长。  
  来源：<https://www.unep.org/en/news-and-stories/story/electronic-waste-surges-countries-look-answers>
- **#18** 「if average growth rates persist, it will take a lifetime (almost 90 years) to reach parity.」  
  判断：**暂无法判断**。“近90年”是基于现有增速的长期外推；Eurostat显示2025年欧盟ICT专业人员中女性占19.5%，较2015年仅升3个百分点，无法在两年窗口内检验90年的终点。  
  来源：<https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260527-2>
- **#19** 「Consequently, they are expected to have a disruptive effect on cryptography, and thus on digital security.」  
  判断：**暂无法判断**。截至2026年仍无量子计算机破解实际部署的RSA（RSA公司2026年博客），英国NCSC等正在推进后量子迁移；“颠覆性影响”取决于未来出现的密码学相关量子计算机，决定性事实尚未发生。  
  来源：<https://www.rsa.com/resources/blog/zero-trust/setting-the-record-straight-on-quantum-computing-and-rsa-encryption/>；<https://www.ncsc.gov.uk/guidance/pqc-migration-timelines>
- **#21** 「Technical advancements, such as artificial intelligence, will also surely have an impact on labelling and cert…」  
  判断：**暂无法判断**。检索到的仅有欧盟资助的CertifAI研究项目和Attestra等AI辅助CRA合规工具，尚无证据表明AI已实际改变官方安全标签与认证项目，“必将产生影响”无法在窗口内认定。  
  来源：<https://www.cybercertlabs.com/cra-ai/>；<https://www.dnv.com/research/future-of-digital-assurance/certifai/>
- **#24** 「Error correction in quantum computers is a challenge that may never be overcome」  
  判断：**暂无法判断**。谷歌2024年12月在Nature发表低于表面码阈值的纠错实验，但Eisert与Preskill 2025年指出距容错应用级量子计算仍有重大工程与概念鸿沟；“可能永远无法攻克”无法在窗口内证实或证伪。  
  来源：<https://www.nature.com/articles/s41586-024-08449-y>；<https://thequantuminsider.com/2025/11/01/nisq-to-fasq-quantum-computing-still-faces-a-climb-from-promise-to-practicality/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 20 | It is envisioned that Germany will make … | 出版前史实 | 书中写“设想德国把IT安全标签扩展到智能家居等其他产品组”，但BSI早在2022年9月（出版前）就已为IT安全标签开放“智能消费设备”类别，覆盖智能家居类联网设备（BSI 2022-09-28新闻稿）。所述扩展在出版前已经发生，按“出版前已发生的事件不算预测”剔除，不计入可判定。出版后BSI于2025年8月又新增“智能安防技术”类别，仅作背景，不据此判正确。 |

## 文件

- 本文：`cases/oecd-digital-economy-outlook-2024-vol2-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/oecd-digital-economy-outlook-2024-vol2-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/oecd-digital-economy-outlook-2024-vol2-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（24 条可核验 / 222 块 ≈ 0.11）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。原因是本报告以政策盘点、国别案例和统计描述为主，并含大量参考文献、注释和统计附录；进行时态的趋势陈述不计为预测；序言（Foreword）、读者指南、目录、各章参考文献与注释、统计附录、图表清单和封底按“前后附文不算预测”的规则人工排除（明细见 PR_BODY）。本稿没有为提高数量而放宽标准。
- 14 条 unclear 均为报告转述他人的预测（如 Statista 预计 2026 年托管服务市场超 4000 亿美元、日本经产省 2025 年 3 月前推出标签制度、各机构对流量和市场规模的预测等），按 v5 归属规则不进入核验。
- 第 20 条“德国将把 IT 安全标签扩展到智能家居等其他产品组”：BSI 在 2022 年 9 月（出版前）已为该标签开放“智能消费设备”类别，所述扩展在出版前已经发生，按出版前史实剔除，不计入可判定；2025 年 8 月新增的“智能安防技术”类别只作背景。
- 趋势符合按严格口径使用：只有存档证据明确证实方向时才给出；“AI 影响标签与认证”只找到研究项目层面的证据，未见制度层面的变化，因此判为暂无法判断，而不是趋势符合。
- 证据以独立第三方来源为主（普华永道、Euronews、欧盟对外行动署、Tefficient、ITU、Teletime、RAND、斯坦福、ILO、WMO、哥白尼、IEA、CNBC、Dell'Oro、ICAO、Eurostat、BSI、Sophos、CISA、Nature 等），不只引用 OECD 自身出版物。
- `data/claims.jsonl`、`output/txt_import/claims_proposals.jsonl` 及评估快照中的 `context` 字段已清空，案例不含整段书中原文。

