# Manual review (METHOD.md v5) of World Development Report 2019: The Changing Nature of Work, review_source manual-assistant-2026-11-15
META={
 "title": "世界银行《2019年世界发展报告：工作性质的变化》（World Development Report 2019: The Changing Nature of Work）",
 "pub": "世界银行 **2018 年 10 月**发布（PDF CreationDate 2018-10-10），按 2018-10 起算。正文用 `reading-library/2026-11-15-未来判断扩展100本/04-经济与资源/058-world-development-report-2019-the-changing-nature-of-work.pdf`（sha256 `9d437a98…a7e3f2`，与世界银行官网 PDF 一致，CC BY 3.0 IGO），经 `pdftotext -enc UTF-8` 生成 TXT（sha256 `c0d1da0e…70e8`，379,189 字符；TXT 不入库）。",
 "method": "本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 110 块（3500 字符、600 字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 19 条候选、16 条可核验（resolvable；3 条转述他人的说法降为 unclear）。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（5 条做了适应性补充检索），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。",
 "overall": "这份报告以描述现状和政策建议为主，明确的预测很少，110 块中只有 16 条可核验预测。可判定的 12 条中，3 条正确（IFR 关于 2019 年全球机器人存量达 260 万台的引用预测、全球公式分配未被采纳、法国义务教育起始年龄降到 3 岁），6 条趋势符合（非洲和南亚没有出现带来正规就业的工业化、非洲没有大规模工业化、非洲就业仍以非正规为主、叙利亚失学儿童难以弥补、复合技能需求上升、中韩等国劳动年龄人口开始下降）。另有 2 条部分符合（人际互动岗位总体增长，但客服被 AI 部分替代；实际工资确实下降，但低薪群体相对受益），1 条错误（“职业极化可能推高发达经济体不平等”：窗口内美国等发达经济体的不平等总体下降或持平）。Sberbank 后台 2021 年降到 1000 人、2050 年人口增长和 2018 年入学儿童将从事尚不存在的职业等 4 条暂无法判断。趋势符合的多是“永远不会”“将持续”一类开放式判断，窗口内只能确认方向。",
 "basis": "本稿由助手逐条对照书中原文与存档证据人工复核：",
 "extra": "\n## 说明\n\n- 抽取密度（16 条可核验 / 110 块 ≈ 0.15）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。原因是 WDR 以现状描述、数据回顾和政策建议为主，进行时态的趋势陈述不计为预测；Jim Yong Kim 的序言（Foreword）按“序言不算预测”的规则排除。本稿没有为提高数量而放宽标准。\n- 3 条 unclear 均为转述他人观点（OECD 承诺 2020 年前达成方案、新加坡 2020 年起对进口服务征 GST、Subramanian 预计印度一两个邦两年内实行全民基本收入），按 v5 归属规则不进入核验。\n- 第 3 条“到 2019 年新增 140 万台、总数 260 万台”是报告转引 IFR 2016 年的预测，按书中原文计入。\n- 第 5 条原文为“may translate into rising inequality”，虽有保留语气，但属于无终点的方向性判断，按出版日到截止日的窗口判断；窗口内方向相反，记错误。\n- 第 16 条为“除非人人有公平机会获得技能，否则不平等加剧”的条件句，前提无法度量，记暂无法判断。\n- 案例的 `context` 字段按协调者口径（brzezinski/kaplan）清空。\n"
}
NF={}
# Verdicts for world-bank-wdr-2019-changing-nature-of-work-v5 resolvable claims 1-16 (idx = order of resolvable claims in data/claims.jsonl)
BLS='https://www.bls.gov/ooh/most-new-jobs.htm'
SF='https://fortune.com/2025/09/02/salesforce-ceo-billionaire-marc-benioff-ai-agents-jobs-layoffs-customer-service-sales/'
RT='https://www.reuters.com/world/india/meet-ai-chatbots-replacing-indias-call-center-workers-2025-10-15/'
ILOAF='https://www.ilo.org/sites/default/files/2025-02/Africa_Informality%20Regional%20statistical%20profile.pdf'
SAS='https://www.griffith.edu.au/__data/assets/pdf_file/0020/1935110/GAPSO2024-Policy-brief-Confronting-labour-market-challenges-in-South-Asia-An-SDG-perspective.pdf'
WBIND='https://blogs.worldbank.org/en/africacan/industrialization-in-africa-must-compete-connect-and-create-value'
IFR20='https://ifr.org/ifr-press-releases/news/record-2.7-million-robots-work-in-factories-around-the-globe'
KUKA='https://www.kuka.com/-/media/kuka-corporate/countries/united-kingdom/documents/kuka-weareorange.pdf'
IFR16='https://ifr.org/ifr-press-releases/news/world-robotics-report-2016'
IFR17='https://ifr.org/news/industrial-robot-sales-increase-worldwide-by-29-percent/'
SSC='https://sscclub.ru/article/transformacija-operacionnoj-funkcii-sbera/'
FTF='https://www.fintechfutures.com/bankingtech/case-study-sberbank-tech-them-on'
DP='https://www.dp.ru/a/2017/06/29/German_Gref_k_2021_godu'
EPI23='https://www.epi.org/blog/wage-inequality-fell-in-2023-amid-a-strong-labor-market-bucking-long-term-trends-but-top-1-wages-have-skyrocketed-182-since-1979-while-bottom-90-wages-have-seen-just-44-growth/'
CEPR='https://cepr.org/voxeu/columns/inequality-within-countries-falling'
WBDEC='https://blogs.worldbank.org/en/opendata/declining-trends-in-national-inequality'
SDG='https://datatopics.worldbank.org/sdgatlas/goal-10-reduced-inequalities/'
OECDW='https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/real-wages-regaining-some-of-the-lost-ground_90aab4e8/2f798dfe-en.pdf'
OECD23='https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/oecd-employment-outlook-2023_904bcef3/08785bba-en.pdf'
EPIW='https://www.epi.org/publication/swa-wages-2023/'
ISS='https://futures.issafrica.org/thematic/guide.pdf?thematic=07-manufacturing&topic=04-manufacturing-sector'
WB21='https://www.worldbank.org/en/region/afr/publication/industrialization-in-subsaharan-africa-seizing-opportunities-in-global-value-chains'
IMF='https://www.imf.org/-/media/files/publications/reo/afr/2024/october/english/jobsnote.pdf'
OECDT='https://www.oecd.org/content/dam/oecd/en/topics/policy-issues/beps/statement-on-a-two-pillar-solution-to-address-the-tax-challenges-arising-from-the-digitalisation-of-the-economy-october-2021.pdf'
TF='https://taxfoundation.org/blog/formulary-apportionment-oecd-tax-deal/'
UNI25='https://www.unicef.org/syria/press-releases/new-chapter-education-syria-back-learning-campaign-presents-new-opportunities'
GPE='https://www.globalpartnership.org/results/country-journeys/syria-back-school-moment-no-other'
SCU='https://www.scu.edu/business/blog/careers/new-ai-job-titles/'
PLU='https://pluralist.com/future-of-work-statistic-closer-look/'
WEF='https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/3-skills-outlook/'
JB='https://blog.jetbrains.com/datalore/2024/07/11/5-emerging-data-job-trends-in-2024/'
LEGI='https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006166564'
EUA='https://www.european-agency.org/country-information/france/legislation-and-policy'
VP='https://www.vie-publique.fr/loi/269264-loi-ecole-de-la-confiance-du-26-juillet-2019-loi-blanquer'
WPP='https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf'
NW='https://www.newsweek.com/map-global-population-increase-sub-saharan-africa-population-birth-rate-fertility-rate-2103515'
CN='https://www.cnbc.com/2024/01/19/chinas-working-age-population-is-shrinking.html'
KR='https://www.allkpop.com/buzz/2025/07/why-south-koreas-population-increased-in-2024-despite-the-low-birth-rate'
TH='https://www.nationthailand.com/in-focus/30380560'
V={
1:('P','照护类人际互动岗位没有被机器取代、仍在增长：美国劳工统计局预测2025—2035年新增岗位最多的职业是居家护理和个人护理助理。但同为人际互动工作的客服岗位已被AI部分替代：Salesforce称AI代理让它削减了约4000个客服岗位，路透社报道印度呼叫中心岗位正被AI聊天机器人取代。主体方向成立，客服这一子类与预测明显不符',[BLS,SF,RT]),
2:('T','截至窗口内，非洲和南亚都没有出现“把劳动力转入正规部门”的工业化：国际劳工组织2025年非洲非正规经济统计概览显示非正规就业仍占主体；孟加拉国、印度、巴基斯坦和尼泊尔的非正规就业约占85%。世界银行指出撒哈拉以南非洲制造业就业有所增长，但正规化没有跟上。方向与预测一致；“技术是原因”这一因果部分无法核验',[ILOAF,SAS,WBIND]),
3:('C','国际机器人联合会（IFR）《2020年世界机器人报告》称，2019年全球工厂中运行的工业机器人创纪录地达到270万台，略高于预测的260万台。按IFR数据，2016—2019年的年装机量分别约为29.4万、40万、42.2万和37.3万台，合计约149万台，与“新增140万台”相符',[IFR20,KUKA,IFR17,IFR16]),
4:('U','缺少决定性事实：没有找到 Sberbank 2021年后台（运营中心）员工实际人数的公开数据。已知的是，2016年降至1万人，2017—2018年降至约6000人（Sberbank 2021年2月的行业访谈）。窗口内无法确认是否降到1000人',[SSC,FTF,DP]),
5:('W','窗口内发达经济体的不平等总体没有上升，反而下降或持平：EPI显示美国工资不平等在2019—2023年收窄，2023年继续下降；世界银行称多数国家疫情后基尼系数下降，富裕国家不平等下降；CEPR/VoxEU称国内不平等已停止上升并在下降。主要结果与“不平等上升”相反',[EPI23,WBDEC,SDG,CEPR]),
6:('P','实际工资确实下降了：OECD称2022—2023年多数成员国实际工资下降，2023年第三季度在多数国家仍低于2019年水平。但这是通胀所致，而且低薪行业的实际工资表现好于中等收入行业；美国第10百分位实际时薪在2019—2023年上涨13.2%。“低技能工资因竞争而下降”这一子项与事实明显不符',[OECDW,OECD23,EPIW]),
7:('T','截至窗口内，非洲没有出现大规模工业化：ISS African Futures称撒哈拉以南非洲制造业占GDP比重自1990年代中期以来一直在12%左右或更低。世界银行2021年称该地区制造业就业有实质增长，但制造业增加值占比没有改善。方向与“未经历大规模工业化”一致，但“永远不会”无法在窗口内证实，自动化的因果作用也未核验',[ISS,WB21]),
8:('T','国际劳工组织2025年非洲非正规经济统计概览和IMF 2024年10月《撒哈拉以南非洲区域经济展望》就业专题都显示，非洲就业仍以高度非正规、低生产率的工作为主，与“就业仍停留在低工资非正规服务部门”一致。前提“城市维持现有模式”无法度量，记为条件未知',[ILOAF,IMF]),
9:('C','全球公式分配没有被采纳。2021年10月OECD/G20包容性框架达成的是“双支柱方案”，没有采用全球公式分配；Tax Foundation指出，支柱一的金额A只是部分借鉴了公式分配思路，基础仍是现有体系的修补',[OECDT,TF]),
10:('T','联合国儿童基金会2025年9月称，叙利亚仍有240多万儿童失学、100多万面临辍学风险，三分之一学校不能使用。GPE称有1.5万多名儿童通过补习回到正规教育，规模远小于失学人数。方向与“许多人难以弥补失学年份”一致，“永远无法弥补”不能在窗口内证实',[UNI25,GPE]),
11:('U','“2018年入学儿童中很大比例将从事尚不存在的职业”要到这批人2030年代就业时才能检验。窗口内确实出现了提示工程师等新职业，但也有来源指出常被引用的“65%”说法缺乏研究依据。终点未到，无法判断',[SCU,PLU]),
12:('T','世界经济论坛《2025年未来就业报告》称，与2023年版相比，“AI与大数据”等技能作为核心技能的重要性明显上升，并列为增长最快的技能。但2023—2024年纯数据岗位招聘一度收缩（JetBrains称竞争加剧但总体稳定）。复合技能需求旺盛的方向一致，但证据多为雇主调查和预期',[WEF,JB]),
13:('C','法国2019年7月26日颁布第2019-791号《为了信任学校法》，把义务教育起始年龄从6岁降到3岁；法国《教育法典》L131-1条修改后自2019年9月2日起生效。报告出版不到一年即实现，与“很快”相符',[LEGI,EUA,VP]),
14:('U','“到2050年全球人口增长一半以上发生在撒哈拉以南非洲”的终点在2050年。联合国《世界人口展望2024》等最新预测仍维持这一判断，但预测本身不是观测结果，截至核验日无法判断',[WPP,NW]),
15:('T','2040年终点未到，但三国劳动年龄人口已在下降。CNBC称中国劳动年龄人口在萎缩；韩国统计厅2024年普查显示15—64岁人口为3626.3万，比上年减少28.3万（0.8%）；泰国国家经济社会发展委员会预测劳动年龄人口将由4320万降到3650万。泰国的实际下降缺少直接观测数据',[CN,KR,TH]),
16:('U','这是条件句：“除非人人有公平机会获得这些技能，否则不平等会加剧”。前提（技能获取机会是否公平）无法度量。窗口内世界银行数据显示多数国家国内不平等下降，与结论方向相反，但前提状态未知，按规则不判对错',[WBDEC,CEPR]),
}
