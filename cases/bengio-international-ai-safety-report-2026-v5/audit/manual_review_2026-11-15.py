# Manual review (METHOD.md) of International AI Safety Report 2026 (zh), review_source manual-assistant-2026-11-15
META={
 "title": "《2026年国际人工智能安全报告》（International AI Safety Report 2026，官方中文版，Yoshua Bengio 主持）",
 "pub": "**2026 年 2 月**，国际人工智能安全报告官方中文译本（internationalaisafetyreport.org，190 页）。重新下载的 PDF sha256 为 `9e50aeda…`，与书单记录逐字节一致；pdftotext 抽出 TXT 的 sha256 为 `16e1e136…`（525,717 字符）。2025 年及以前的数据视为已知历史。观察窗口为 2026-02 至 2026-11-15，只有约 9 个月。",
 "method": "按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线把全文（525,717 字符）切成 152 块（每块 3500 字符，带 600 字符上下文），跳过前言（第 1-5 块）和参考文献（第 54-152 块），正文 48 块。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共 46 条候选，其中 37 条为可核验预测；9 条降为 unclear（多为书中转述的专家调查数字），另有 1 条假设推演被排除。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索（74 次），其中 3 条追加一轮检索（6 次）；只从检索返回的 URL 中选源。原文存档于 data/sources（sha256），写入 data/evidence.jsonl（60 条）。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。",
 "basis": "本稿由助手逐条对照书中原文与存档证据人工复核：",
 "overall": "这是一份 2026 年 2 月出版的综述报告，主体是描述现状，预测多以 2027、2028、2030 年为终点，而观察窗口只有约 9 个月，所以未定占比很高（27/37）。可判定的 10 条中没有错误：通用型 AI 能力继续提升、带自然语言接口的生物设计工具陆续发布、主要 AI 公司短期内靠大量采购芯片维持算力增长、欧盟通用型 AI 模型规则 2026 年 8 月起执行，四条按时成立；AI 投资大幅增长、AI 用电持续增长、模型在多个科学领域接近研究级三条方向一致但期限未走完，记“趋势符合”；劳动力需求结构变化、自动化竞争压力、高低收入国家差距三条只部分成立。可判定样本太小，胜率不宜外推。",
 "extra": "\n## 说明\n\n- 观察窗口只有约 9 个月（2026-02 至 2026-11-15），终点在 2027 年及以后的预测一律记“暂无法判断”。\n- 第 11 条与第 8 条语义相关，但原文区间不重叠；按 prepare_book.py:424–432、619–642 的原重叠去重规则全部保留。第 11 条恢复为预测，终点未到，记暂无法判断。本轮只撤销人工添加的语义去重，其他判断不变。\n- 第 15 条是条件句，前提“投资未能产生收入”没有出现，记“暂无法判断”。\n- 第 18 条（2026 年 AI 计算用电≈奥地利或芬兰）：2026 年尚未结束，Gartner 的 AI 优化服务器口径估计已高于芬兰全国用电，但口径不同，暂不判定。\n- 第 33 条美国劳动收入份额降至纪录低点，但未能归因于 AI 且只覆盖美国，不判定。\n- 第 34 条以使用率差距代替“益处”，口径不同，只记“部分符合”。\n",
}
NF={}
EPT='https://epoch.ai/trends'
EP30='https://epoch.ai/publications/can-ai-scaling-continue-through-2030'
METR='https://metr.org/blog/2026-01-29-time-horizon-1-1/'
MIRROR='https://metr.org/blog/2026-04-10-mirrorcode-preliminary-results/'
TF8='https://www.trendforce.com/presscenter/news/20260803-13161.html'
GART='https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026'
IEA26='https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions'
SIGHT='https://www.forbes.com/sites/robertszczerba/2026/06/25/whoever-wins-ai-will-count-transformers-not-nvidia-chips/'
CNAS='https://www.cnas.org/publications/reports/american-ai-companies-cant-get-enough-chips'
EPDC='https://epoch.ai/graphs/largest-ai-data-centers-by-power-capacity'
YALE='https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market'
V={
11:('U', '按原重叠去重规则保留：与第8条的原文区间不重叠，不另作语义去重。该条以趋势持续为前提，2027-2028年及本十年末（2030年）的节点均晚于截止日2026-11-15；沿用已存档METR材料作背景，不把出版前的时间跨度估计或演示外推成未来节点命中，记暂无法判断。', ['https://metr.org/blog/2026-01-29-time-horizon-1-1/']),
1:('U','终点为2030年。截至截止日能力仍在提升（见第6条），但“2030年前持续进步”需到2030年才能检验',[EPT]),
2:('T','“未来几年”尚未走完，已观察到的2026年方向一致：TrendForce估计全球九大云厂商2026年资本开支同比增长约90%，摩根大通预计2026年AI资本开支接近1万亿美元；但10月微软、谷歌下调或维持资本开支预期，增长能否持续数年尚待观察',[TF8,'https://www.jpmorgan.com/insights/global-research/artificial-intelligence/ai-capex','https://www.cnbc.com/2026/10/29/microsoft-google-ai-capex-estimates.html']),
3:('U','终点为2030年。Epoch AI显示前沿训练算力仍按约每年5倍增长，但125倍和“不触及硬上限”须到2030年检验',[EPT]),
4:('U','“每年提高2-6倍”是速率判断，出版后的估计分歧很大：Epoch AI认为算法进步测量本身很不确定，另有研究估计固定数据和规模下算法进步仅约每年1.6倍；没有可与书中口径直接对照的新测量，无法判断',['https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress','https://hansgundlach.substack.com/p/measuring-the-dark-energy-of-ai-progress']),
5:('U','终点为2030年。METR 2026年4月报告AI已能完成部分耗时数周的编码任务（可验证的重写类任务），但书中预测的2030年节点未到',[MIRROR]),
6:('C','未写时间，按出版至截止日窗口检验。窗口内能力继续提升：2026年3月GPT-5.4在USAMO 2026题目上得分95%；4月METR报告AI已能完成部分耗时数周的编码任务；10月谷歌Gemini 4 Carbon在Artificial Analysis智能指数上排名第一。也有评论认为推理类基准增长放缓，但主要方向成立',['https://www.sri.inf.ethz.ch/blog/usamo',MIRROR,'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/','https://algorithmine.com/research/reasoning-model-benchmark-plateau-2026']),
7:('U','条件句，终点为2030年。截至截止日Epoch AI仍显示训练算力约每年5倍增长，但3000倍须到2030年检验',[EPT]),
8:('U','条件外推，节点为2027年和2030年，截止日前均未到。METR 2026年1月更新的时间跨度估计仍在增长，但不能提前判定',[METR]),
9:('U','原文指向2030年左右。窗口内算力仍在增长，但已出现电力与设备瓶颈信号：据Bloomberg引用Sightline数据，约一半原定2026年投运的美国数据中心推迟或取消；是否“不触及根本性瓶颈”要到2030年左右才能判断',[SIGHT,'https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/navigating-a-system-of-ai-bottlenecks']),
10:('U','终点为2027-2028年，截止日前未到',['https://www.sri.inf.ethz.ch/blog/usamo']),
12:('U','终点为2028-2030年，截止日前未到',['https://www.businessinsider.com/ai-agents-failed-consulting-tasks-mercor-ceo-improving-replace-consultants-2026-2']),
13:('T','“未来几年内”尚未走完，已出现方向一致的证据：2026年10月OpenAI公布数学、计算机科学和物理三项新发现，其中量子色动力学相关证明经OpenAI指定的专家组核验（《科学美国人》报道）；但这些结果多由公司发布，独立评测也发现AI研究智能体在原创机器学习研究上没有做出发现，“多个专业科学领域达到研究级”尚未完全成立',['https://openai.com/index/building-scientific-understanding-with-academic-communities/','https://www.scientificamerican.com/article/openais-shepherds-affirm-blockbuster-physics-result/','https://danielsamfdo.github.io/blog/2026-10-15-the-21-lie-why-ai-research-agents-can-t-be-trusted-with-their-own-resu.html']),
14:('U','缺少可靠的训练成本数据。对2026年发布的GPT-6 Astra只有媒体按GPU时价推算的5.4亿至10亿美元，以及按Epoch单价折算的约9.2亿美元，恰在书中10亿美元下限附近，且“下一代”所指不明，无法判断',['https://wccftech.com/openais-1-billion-gpt-6-astra-heralds-the-age-of-agi-according-to-nvidias-jensen-huang-yet-anthropics-fable-5-1-still-beats-it-on-swe-bench-pro-and-coding-benchmarks/','https://businessmodelanalyst.com/gpt-6-astra-training-shelf-life-markdown/']),
15:('U','条件句。“投资未能产生收入”这一前提没有出现：Anthropic 2026年三季度收入约170亿美元，OpenAI季度收入首次超过100亿美元，不判正确或错误',['https://officechai.com/ai/anthropics-quarterly-revenue-is-now-17-billion-far-ahead-of-openais-10-billion/','https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/']),
16:('U','条件句，终点为2030年。Epoch AI估计同等性能的推理成本每年下降约13倍，但这是推理价格口径，不是训练算力需求，且终点未到',['https://epoch.ai/publications/the-plunging-price-of-thought']),
17:('T','“数年”尚未走完，方向一致：IEA称2025年数据中心用电大幅增长；Gartner估计2026年全球数据中心用电增长26%至565 TWh，其中AI优化服务器用电增长约84%。也有反向信号，美国得州暂停新建数据中心后用电增长预测被下调',[IEA26,GART,'https://www.bloomberg.com/news/articles/2026-09-09/us-power-demand-forecast-cut-after-texas-pause-on-data-centers']),
18:('U','2026年尚未结束，全年数据未出。现有估计口径不一：Gartner估计AI优化服务器用电2025年约95 TWh，2026年预计175 TWh，而芬兰2025年全国用电约85 TWh。若口径可比，书中估计偏低，但“AI计算用电”与“AI优化服务器用电”口径不同，暂不判定',[GART,'https://energia.fi/wp-content/uploads/2026/01/Electricity-Year-2025-1.pdf']),
19:('U','终点为2030年。截至2026年11月最大的AI数据中心约1 GW（Epoch AI），2030年4-16 GW需届时检验',[EPDC]),
20:('U','终点为本十年末，截止日前未到。窗口内出现电网瓶颈信号（美国并网排队、挪威冻结数据中心新增电网容量预留），也有多GW园区开工，无法提前判断',['https://www.axios.com/2026/10/20/goldman-ai-energy-infrastructure-bottleneck','https://www.techtarget.com/news/norway-slams-brakes-on-ai-data-center-boom-over-grid-fears/874652/']),
21:('U','未写时间。截至截止日芯片挑战仍未解决：CNAS称2026年AI芯片产量已成为算力建设的约束，TrendForce称HBM短缺持续到2027年；台积电在扩产CoWoS。“很可能被克服”没有终点，窗口内也未见克服，暂无法判断',[CNAS,'https://www.trendforce.com/presscenter/news/20260929-13255.html']),
22:('C','“短期内”与观察窗口一致。主要AI公司继续大量采购芯片维持算力增长：英伟达截至2026年7月的季度营收约962亿美元，同比翻倍以上，数据中心收入890亿美元中超大规模云厂商占约490亿美元；AWS计划在2027-2028年再部署200万块英伟达GPU',['https://www.datacenterdynamics.com/en/news/nvidia-revenue-doubles-over-last-year-as-company-forecasts-record-growth/','https://www.datacenterknowledge.com/data-center-chips/-out-of-hyperbole-nvidia-s-ai-boom-tests-data-center-infrastructure-limits']),
23:('U','终点为2030年，截止日前未到',[EPT]),
24:('U','终点为2030年。窗口内芯片供给仍偏紧（CNAS），但是否在2030年前阻碍扩展须届时检验',[CNAS]),
25:('U','“在未来”没有终点。2026年的研究发现AI在文字对话中比专家级人类说服者更有说服力，论文也提到早期AI并不比人类更有说服力，但这是不同研究、不同对照之间的比较，不能直接证明同一指标随时间上升，暂不判定',['https://arxiv.org/html/2606.16475','https://www.science.org/content/article/ai-chatbots-are-becoming-experts-changing-people-s-minds-what-s-their-secret']),
26:('U','窗口内有多项操纵行为评测（如多环境操纵评测），但没有可比的时间序列说明操纵能力增强，综述也认为有害操纵的证据仍有限，无法判断',['https://arxiv.org/html/2606.25899','https://doi.org/10.1016/j.copsyc.2026.102478']),
27:('U','窗口内出现新的篡改/后门研究（微软2026年11月发布后训练供应链攻击与“沉睡智能体”研究），但“随能力提升而变得尤其重要”缺乏可度量的对照，无法判断',['https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/']),
28:('C','未写时间，按出版至截止日窗口检验。窗口内陆续发布带自然语言/对话接口的生物设计工具：2026年3月Dyno Therapeutics推出智能体式蛋白结合物设计套件Psi-Phi；4月Matwings推出对话式蛋白研发智能体；9月Geodesic推出带对话智能体的NovaDDE；11月微软Discovery接入NVIDIA BioNeMo智能体工具设计蛋白结合物',['https://www.dynotx.com/news/dyno-therapeutics-launches-dyno-psi-phi-an-agentic-ai-suite-for-protein-binder-design-at-nvidia-gtc-2026','https://www.matwings.com/en/site/news-detail/MatwingsVenus%E2%84%A2%3A%20A%20Conversational%20Protein%20R%26D%20Agent%2C%20Officially%20Launched%20Globally','https://www.geodesiclab.com/news/novadde-ai-workbench','https://techcommunity.microsoft.com/blog/microsoft-discovery-blog/nvidia-bionemo-agent-toolkit-bringing-nvidia-models-in-biology-to-every-scientis/4572674']),
29:('U','窗口内有多起多智能体安全事件报道，但多智能体系统的规模化部署仍很少（Forrester），缺少风险随普及而上升的量化证据，无法判断',['https://www.cooperativeai.com/post/lessons-from-multi-agent-safety-incidents','https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/']),
30:('P','部分成立：德国ifo指标显示，AI暴露度最高职业中20-24岁全职就业自2022年三季度以来下降14%；美国人口普查局工作论文发现引入AI后早期职业招聘下降。但耶鲁预算实验室10月称职业结构尚未出现与AI明确对应的变化，“影响众多职业”还没有在总量层面出现',['https://www.ifo.de/en/press-release/2026-11-09/early-indicator-shows-strong-effect-ai-job-prospects-entry-level-workers','https://www2.census.gov/ces/wp/2026/CES-WP-26-27.pdf',YALE]),
31:('P','部分成立：2026年微软、Kroger等公司宣布的裁员与AI投入转移挂钩（路透社汇总）；但麦肯锡调查称AI导致的岗位流失低于预期，斯坦福SIEPR认为AI对总体就业影响可能较小',['https://www.investing.com/news/stock-market-news/factboxcompanies-cutting-jobs-as-investments-shift-toward-ai-4945243','https://www.mckinsey.com/featured-insights/charts/ai-job-losses-fall-short-of-forecasts','https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality']),
32:('U','窗口内没有把收入与财富差距变化归因于AI的观测数据，现有文献多为模型推演（IMF工作论文），无法判断',['https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026166-source-pdf.pdf']),
33:('U','美国劳动收入份额2026年降至有记录以来最低（Haver、Axios），但纽约联储把下降归于疫情后因素，现有资料不能把这一变化归因于AI应用；且只覆盖美国，不判定',['https://www.haver.com/articles/labor-s-share-of-income-falls-to-all-time-low-in-third-quarter','https://libertystreeteconomics.newyorkfed.org/2026/06/the-post-covid-decline-in-the-labor-share/']),
34:('P','只部分成立：微软报告显示2026年一季度发达国家15-64岁人口生成式AI使用率27.5%，发展中国家15.4%，差距比2025年下半年扩大1.5个百分点。但这衡量的是使用率，不是“益处”，世界银行也称生成式AI在各国扩散快于以往技术',['https://www.straitstimes.com/world/united-states/ai-use-surges-globally-but-rich-poor-divide-widens-microsoft-says','https://thedocs.worldbank.org/en/doc/ec0b4de6941eb645d2ef5d99a6e43799-0050062026/original/Adopting-Fast-and-Slow.pdf']),
35:('U','窗口内主要是专家调查和评论（IPIE调查76%专家预期信息环境恶化），缺少信息质量下降的实测数据，无法判断',['https://www.ipie.info/research/sr2026-3-trends-information-environment-2026-expert-survey-results']),
36:('U','条件外推，终点为2027年。2026年GPT-6 Astra训练成本只有媒体估算（约5.4亿至10亿美元），截止日前不能判定',['https://wccftech.com/openais-1-billion-gpt-6-astra-heralds-the-age-of-agi-according-to-nvidias-jensen-huang-yet-anthropics-fable-5-1-still-beats-it-on-swe-bench-pro-and-coding-benchmarks/']),
37:('C','按时发生：2026年8月2日起欧盟AI办公室开始对通用型AI模型规则行使调查和处罚权，《通用型人工智能行为准则》的过渡宽限期结束；2026年7月生效的AI综合简化条例推迟的是高风险系统义务，没有推迟通用型AI模型规则',['https://futurium.ec.europa.eu/en/apply-ai-alliance/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august','https://techinsights.linklaters.com/post/102o605/the-eu-ai-act-the-enforcement-era-begins','https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/when-does-enforcement-start','https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act']),
}
