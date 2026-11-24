import json
_c=[json.loads(l) for l in open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','data','claims.jsonl'))]
CFA='https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment'
IEADC='https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions'
NWW='https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html'
AX='https://www.axios.com/2026/02/24/ai-data-center-boom-projects-numbers'
IFR='https://ifr.org/news/five-million-robots-now-operate-in-factories-globally/'
WSTS='https://www.wsts.org/76/103/Global-Semiconductor-Market-grows-26-in-2025-to-796B'
DEL='https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html'
BNP='https://cib.bnpparibas/semiconductor-market-2026-it-is-not-solely-about-ai/'
EP='https://epoch.ai/publications/the-plunging-price-of-thought'
BB='https://www.bloomberg.com/news/articles/2025-12-04/the-rise-of-ai-reasoning-models-comes-with-a-big-energy-tradeoff'
TOK='https://finance.yahoo.com/technology/ai/articles/tokens-getting-cheaper-companies-spending-185229986.html'
DO25='https://www.prnewswire.com/news-releases/data-center-capex-surges-57-percent-in-2025-as-ai-deployments-accelerate-according-to-delloro-group-302715242.html'
RCR='https://rcrtech.com/semiconductor-news/ai-is-shifting-to-the-edge/'
FUT='https://futurumgroup.com/press-release/ai-capable-devices-slow-to-deliver-on-cloudless-agentic-ai-experiences/'
DD='https://ddnews.gov.in/en/indias-data-centre-capacity-more-than-doubled-in-2025/'
SAV='https://www.savills.in/research_articles/165611/237969-0'
SRG='https://www.srgresearch.com/articles/synergy-updates-its-ranking-of-the-worlds-top-20-hyperscale-data-center-locations'
VC='https://www.visualcapitalist.com/data-center-capacity-around-the-world/'
CON='https://www.constellationr.com/insights/news/ai-pc-upgrade-cycle-crawling-amid-murky-value'
GAR='https://www.gartner.com/en/newsroom/press-releases/2025-10-16-gartner-says-worldwide-pc-shipments-grew-8-percent-in-third-quarter-of-2025'
KAD='https://kadence.com/en-us/knowledge/why-tech-buyers-are-saying-not-yet/'
TM='https://www.turbomachinerymag.com/view/steam-turbines-gas-turbine-bottleneck-siemens-energy'
ED='https://eastdaley.com/daley-note/get-in-line-turbine-delays-stall-demand-growth-in-gas-market'
AXG='https://www.axios.com/2026/02/04/ai-natural-gas-power-data-centers'
EMUS='https://ember-energy.org/latest-updates/solar-met-61-of-us-electricity-demand-growth-in-2025/'
CB='https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025'
IER='https://www.instituteforenergyresearch.org/fossil-fuels/fossil-fuels-dominate-global-energy-supply-in-2025/'
EMEI='https://ember-energy.org/latest-insights/energy-institute-statistical-review-of-world-energy/'
AP='https://asian-power.com/news/global-electricity-demand-hits-record-31779-twh-in-2025-growth-pace-eases'
IOT='https://iot-analytics.com/number-connected-iot-devices/'
CIOT='https://iot-analytics.com/cellular-iot-market-update-spring-2026/'
JPT='https://jpt.spe.org/industry-executives-offer-practical-advice-on-how-to-use-modern-ai-models-wisely'
JPT25='https://jpt.spe.org/curiosity-meets-comprehension-how-energy-llm-is-bridging-knowledge-gaps'
EC1='https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational'
EC0='https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational'
COL='https://www.datacenterdynamics.com/en/news/colliers-data-center-investment-tops-580-billion-beating-oil-investment-for-the-first-time/'
DO26='https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/'
DOQ2='https://www.prnewswire.com/news-releases/data-center-capex-grew-92-percent-in-2q-2026-driven-by-surging-ai-demand-and-memory-costs-according-to-delloro-group-302879910.html'
ABC='https://www.reuters.com/technology/alphabet-buy-data-center-infrastructure-firm-intersect-475-billion-deal-2025-12-22/'
META='https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/'
D={
1:('T','第三方（CFA Institute 2026-08）引用的估计显示全球数据中心用电从2024年约415TWh升至2025年约485TWh（约+17%），快于到2030年翻倍所需的约12%年增速；终点2030年未到，方向持续符合。',[CFA,IEADC]),
10:('P','Sightline Climate/Currence等第三方估计2026年计划投运的大型数据中心容量有30%-50%可能延误，延误风险确实兑现且风险未被消除；但比例明显高于书中“约20%”，量级不符。',[NWW,AX]),
12:('C','IFR统计2025年全球工业机器人安装量首次超过60万台、运行存量增长9%至创纪录的500万台，工业自动化在窗口内继续加深。',[IFR]),
15:('C','WSTS统计2025年全球半导体销售增长26%至7956亿美元，德勤等指出增长主要由AI基础设施/数据中心推动；BNP提醒2026年增长部分来自涨价和工业补库，但AI/数据中心仍是关键驱动。',[WSTS,DEL,BNP]),
16:('C','Epoch AI（2026-09）测算过去三年同等性能AI的成本每季度下降约47%，模型效率在窗口内持续快速提升；反证（彭博2025-12）显示推理模型单次耗电更高，但不否定同等性能效率提升。',[EP,BB]),
17:('C','Silicon Data指数显示单个token价格自2023年降逾90%而LLM支出仍翻倍；Dell’Oro统计2025年数据中心资本开支增长57%，更便宜的模型带来更多使用与更多算力投入。',[TOK,DO25]),
18:('T','与第1条同一预测（正文重复）：2025年全球数据中心用电约485TWh、较2024年增约17%，增速快于2030年翻倍路径；终点未到。',[CFA,IEADC]),
21:('P','端侧推理在窗口内确有增长（NPU手机/AI PC），但Futurum指出多数助手与智能体体验仍依赖云端，推理负载并未明显从数据中心转出，仅部分符合。',[RCR,FUT]),
22:('C','印度2025年新增数据中心容量387MW IT，较2024年的191MW翻倍；2026年上半年再新增约258MW、同比增59%，行业在窗口内快速增长。',[DD,SAV]),
31:('C','Synergy（2025-07）显示北弗吉尼亚和北京地区占全球超大规模容量约20%、美国占比最高；Visual Capitalist汇总显示美国、欧洲、中国为装机最大的地区，窗口内仍为三大地区。',[SRG,VC]),
35:('W','窗口内PC换机主要由Windows 10停服驱动（Gartner），Constellation称AI PC换机周期“爬行”；手机持有周期反而延长（Kadence），未见AI加速设备更换。',[CON,GAR,KAD]),
37:('T','大型燃气轮机交货期已排至2029-2030年（Turbomachinery），GE Vernova积压约116GW、相当于数年产能（East Daley）；新燃气电厂投运推迟的方向已明确，是否推迟到2030年后尚待观察。',[TM,ED]),
46:('P','Axios（2026-02）称燃气是数据中心自建电源的明显赢家；但Ember显示2025年美国新增用电需求的61%由太阳能满足，电网层面增量并非燃气主导，只部分符合。',[AXG,EMUS]),
54:('C','能源研究所《世界能源统计年鉴2026》显示2025年化石燃料占一次能源86%，为历史最低（Carbon Brief）；IER强调仍为86%，但份额下降方向成立。',[CB,IER]),
55:('P','2025年全球电力需求增长约3.0%，快于能源总供应的1.7%，电力份额继续上升；但电力需求增速从2024年的4.4%放缓至约2.8%-3%，“加速”未出现。',[EMEI,AP]),
56:('T','IoT Analytics统计2025年联网IoT设备增长14%至211亿台，高于2024-2030年翻倍所需的约12%年增速；蜂窝IoT增速放缓至13%，终点未到，方向符合。',[IOT,CIOT]),
57:('C','JPT（SPE，2026-09）称EnRG-LLM在2025年进入会员测试后不久即开放给油气公司授权使用，预测的商业可用已实现（但需求不及预期）。',[JPT,JPT25]),
59:('C','ECMWF在2025年2月和7月先后让AIFS单一与集合AI预报投入业务运行，均与传统物理模式IFS并行，AI补充而非取代数值预报。',[EC1,EC0]),
65:('T','2025年全球数据中心投资超过5800亿美元（Colliers），Dell’Oro预计2026年资本开支超过1万亿美元；按此路径2025-2030年累计4.2万亿美元的方向成立，终点未到。',[COL,DO26]),
68:('C','Alphabet于2025-12以47.5亿美元收购清洁能源开发商Intersect；Meta在一年内出资建设至少十几座燃气电厂，数字/科技部门在能源部门的角色在窗口内明显加大。',[ABC,META]),
69:('T','Dell’Oro称2026年全球数据中心资本开支有望超过1万亿美元，2026年二季度同比增长92%；超过每年8000亿美元已接近实现，但全年数据尚未出，暂记趋势符合。',[DO26,DOQ2]),
}
UR={
23:'书中“两年内上线逾2GW（最大设计容量）”终点约为2027年4月；窗口内实际新增IT容量约650MW（2025年387MW+2026年上半年258MW），步伐明显偏慢，但口径（设计容量与IT负载）不同且终点未到，暂无法判断。',
71:'十年期相对增速预测；2025年印度能源需求增速仅约1%、美国电力需求增约3.1%，与预测方向相反，但仅一年且受季风天气影响，不足以判断十年结果。',
}
V={}
for i,c in enumerate(_c,1):
    if i in D: V[i]=D[i]; continue
    import re as _re
    ex=c.get('extraction_v2') or {}
    h=ex.get('horizon') or ''
    yrs=sorted(set(_re.findall(r'20[3-9]\d', (ex.get('claim') or '')+' '+h)))
    if i in UR: r=UR[i]
    elif yrs or '十年' in (ex.get('claim') or '') or h:
        tag=h or ('、'.join(yrs) if yrs else '未来十年')
        r=f'预测终点（{tag}）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。'
    else:
        r='表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。'
    V[i]=('U',r,[])
