# 雷·库兹韦尔《奇点更近》：出版后预测人工核查

- 案例目录：`cases/kurzweil-singularity-nearer-v5/`
- 出版日期：英文原版 *The Singularity Is Nearer: When We Merge with AI*，Viking，**2024-06-25**。观察窗口为 2024-06-25 至 2026-11-15，仅约两年半。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本书的大多数判断指向 2029 年（AI 通过图灵测试）、2030 年代（脑机接口、纳米机器人）和 2045 年（奇点）。按规则，写明或隐含的终点尚未到达者（202 条）一律记暂无法判断，不因方向已有苗头而提前计分；70 条为条件推演、一般机制或无时点的长期愿景，作为非预测剔除（其中第 83 条“美国拥有电脑的家庭比例将继续上升”实际可检验，改为计入预测，但出版后的官方数据尚未发布，记暂无法判断）。真正能在本窗口内检验的，主要是“到你读到本书时”“未来几年”一类近期判断。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用公开来源（WebSearch/WebFetch，必要时 Exa）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际可访问的公开页面；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 304 条，剔除非预测 69 条，计入 **235 条预测**，其中 **24 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 14 |
| 趋势符合 | 6 |
| 部分符合 | 1 |
| 错误 | 3 |
| 暂无法判断 | 211 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **58.3%**（14/24） |
| 加权胜率 | **79.2%** |
| 错误率 | **12.5%**（3/24） |
| 未定占比（暂无法判断/预测） | 89.8%（211/235） |

## 总体评价

在出版后两年多的短窗口里，库兹韦尔的近期判断准确率很高：大语言模型用户规模（ChatGPT 2026 年 2 月周活约 9 亿）、AI 投资与论文数量继续创新高、编程 AI 显著增强（SWE-bench 成绩一年内由个位数升到七成以上）并催生“氛围编程”、办公套件全面集成 AI、前沿模型训练算力每年约 4—5 倍增长、大模型推理价格下降远快于算力成本、Waymo 扩展到洛杉矶并进入更多城市、锂电池价格继续下降（2025 年 108 美元/千瓦时）、美国凶杀率 2024—2025 年大幅下降、社会保障支出继续增长、穿戴设备开始在用户察觉前提示疾病（2025 年 Apple Watch 高血压提醒获 FDA 批准）、FDA 推动以 AI 计算模型替代部分动物试验，这些都已兑现。

错误集中在他最乐观的“物质丰裕”与人机交互判断：AI 控制的垂直农业“很快”带来低成本食物——实际上 Bowery 等明星垂直农场在 2024—2025 年相继倒闭；远程办公“可能加强”——实际上大公司和美国联邦政府推行返岗，远程办公比例停滞；“到 2020 年代中期出现比键盘快数千倍的全沉浸式 VR 交互”——没有出现。需要强调：本书的核心预测（2029 年 AGI、2030 年代脑机融合、纳米医学与 2045 年奇点）全部尚未到期，记为暂无法判断；当前胜率只反映其近期、渐进性判断的质量，不能外推为对全书核心命题的检验。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（14 条）

- **#6** 「Bythetimeyoureadthis,tensofmillionsofpeoplelikelywillhaveexperiencedth…」  
  判断：**正确**。ChatGPT 2026年2月周活跃用户约9亿，远超“数千万人”；但此条在出版时已基本成立  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>
- **#22** 「Thenumberswillbeevenhigherbythetimeyoureadthis.」  
  判断：**正确**。斯坦福《AI指数2025》显示2024年全球企业AI投资、AI论文与专利数量均高于2022年  
  来源：<https://hai.stanford.edu/ai-index/2025-ai-index-report>
- **#26** 「bythetimeyoureadthis,stillmorepowerfulprogrammingAIswillbeavailable.」  
  判断：**正确**。编程AI显著增强：SWE-bench 解题率2023年约4%，2024年升至约72%  
  来源：<https://hai.stanford.edu/ai-index/2025-ai-index-report>
- **#29** 「manyastonishingnewadvanceswillsurelyhavebeenmadebythetimeyoureadthis」  
  判断：**正确**。出版后出现推理模型（OpenAI o1，2024年9月）、视频生成与智能体等多项重大进展  
  来源：<https://en.wikipedia.org/wiki/OpenAI_o1>
- **#30** 「AndAIwilllikelybewovenmuchmoretightlyintoyourdailylife.」  
  判断：**正确**。AI更深入日常生活，ChatGPT成为全球访问量前五的网站之一  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>
- **#31** 「applicationsuiteslikeGoogleWorkspaceandMicrosoftOfficeareintegratingpo…」  
  判断：**正确**。微软365 Copilot、谷歌Workspace内置Gemini已大规模推出  
  来源：<https://en.wikipedia.org/wiki/Microsoft_Copilot>；<https://en.wikipedia.org/wiki/Gemini_(chatbot)>
- **#32** 「Theamountofcomputationusedtotrainastate-of-the-artmodelisnowincreasing…」  
  判断：**正确**。Epoch AI 统计前沿模型训练算力每年约增长4—5倍，出版后仍延续  
  来源：<https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year>
- **#34** 「algorithmicimprovementsandAI-specifichardwarespecializationmeanthatpri…」  
  判断：**正确**。Epoch AI 统计同等能力大模型的推理价格每年下降数十倍以上，远快于硬件算力成本下降  
  来源：<https://epoch.ai/data-insights/llm-inference-price-trends>
- **#65** 「Notonlywilleachindividualcapability(e.g.,writing,voice,face,conversati…」  
  判断：**正确**。2024—2025年AI在写作、语音、人脸与对话上大幅提升，并出现融合声音与画面的视频生成（Sora 2、Veo 3），逼真度大增  
  来源：<https://en.wikipedia.org/wiki/Sora_(text-to-video_model)>；<https://en.wikipedia.org/wiki/Veo_(text-to-video_model)>
- **#82** 「Fortunately,inexpensiveandefficientphotovoltaiccellswillcontinuetoexpa…」  
  判断：**正确**。光伏装机连年创纪录，离网太阳能是新增电力接入的主要来源之一，全球无电人口继续减少  
  来源：<https://www.iea.org/reports/tracking-sdg7-the-energy-progress-report-2025>；<https://en.wikipedia.org/wiki/Growth_of_photovoltaics>
- **#123** 「lithium-ionstoragecostsfellroughly80percentpermegawatt-hourandareproje…」  
  判断：**正确**。彭博新能源财经：锂电池组均价2024年降20%至115美元/千瓦时，2025年再降8%至108美元/千瓦时  
  来源：<https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/>
- **#161** 「Bythetimeyoureadthis,itspassengerservicewillhaveexpandedtoLosAngelesan…」  
  判断：**正确**。Waymo 2024年11月向洛杉矶公众开放，2025年进入奥斯汀、亚特兰大等城市  
  来源：<https://en.wikipedia.org/wiki/Waymo>
- **#199** 「WithGDPcontinuingtogrowexponentially,socialsafetynetspendingwilllikely…」  
  判断：**正确**。美国社会保障、联邦医疗保险和医疗补助支出2025财年继续增长约7—8%  
  来源：<https://www.cbo.gov/system/files/2025-06/61302-MBR.pdf>
- **#217** 「Andcrimewilllikelykeepfallingthroughacombinationofbettereducation,smar…」  
  判断：**正确**。美国凶杀率2024年大幅下降，FBI 2025年数据显示暴力犯罪再降9.3%、谋杀下降18.1%  
  来源：<https://en.wikipedia.org/wiki/Crime_in_the_United_States>

### 趋势符合（6 条）

- **#27** 「Suchcapabilitieswillunleashstaggeringamountsofhumanpotentialoverthenex…」  
  判断：**趋势符合**。2025年“氛围编程”（不写代码、用自然语言让AI生成软件）流行，非程序员开发软件门槛大降；“释放巨大潜能”尚待观察  
  来源：<https://en.wikipedia.org/wiki/Vibe_coding>
- **#85** 「costscontinuetofallandthiswilllikelyaccelerateagainassophisticatedAIpl…」  
  判断：**趋势符合**。基因组测序成本继续下降；AI是否使其“再次加速”尚无明确证据  
  来源：<https://www.genome.gov/about-genomics/fact-sheets/Sequencing-Human-Genome-cost>
- **#99** 「Thisrateofimprovementcontinuesunabated.」  
  判断：**趋势符合**。2024—2026年AI芯片性价比持续快速提升，但“速率持续不减”需更长时间检验  
  来源：<https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year>
- **#120** 「Thisprogresswillcontinueexponentiallyasfurthercostreductionsaredrivenb…」  
  判断：**趋势符合**。光伏组件价格2024年后跌至历史低位，可再生能源装机继续快速增长；AI材料发现的贡献尚不明显  
  来源：<https://en.wikipedia.org/wiki/Growth_of_photovoltaics>
- **#229** 「InthecomingyearsthiswillbeespeciallyimportantincasessimilartotheCOVID-…」  
  判断：**趋势符合**。2025年4月FDA宣布以AI计算模型等新方法逐步替代单抗等药物的动物试验，监管纳入模拟的方向明确；在疫苗审批中的应用仍有限  
  来源：<https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs>
- **#237** 「Increasingly,suchmodelswillincorporatericherformsofinformationlikedata…」  
  判断：**趋势符合**。2025年9月FDA批准Apple Watch基于机器学习的高血压提醒功能，可在用户确诊前发出提示；“建议治疗”尚未普及  
  来源：<https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250507.pdf>

### 部分符合（1 条）

- **#35** 「ThistrendwilllikelyaccelerateasAIisuseddirectlyinoptimizingchipdesign,…」  
  判断：**部分符合**。AI已用于芯片设计（谷歌AlphaChip用于TPU布局），但尚无证据表明芯片性价比提升因此“加速”  
  来源：<https://en.wikipedia.org/wiki/AlphaChip>

### 错误（3 条）

- **#91** 「Astechnologicalchangeenablesmoreandmorejobstobedoneremotely,thistrendw…」  
  判断：**错误**。出版后远程办公并未加强：亚马逊等大公司和美国联邦政府推行全面返岗，远程办公占比基本停滞  
  来源：<https://wfhresearch.com/>；<https://en.wikipedia.org/wiki/Remote_work>
- **#106** 「wewillsoonproducehigh-quality,low-costfoodusingverticalagriculturewith…」  
  判断：**错误**。“很快”实现AI垂直农业低成本食物未见端倪：Bowery Farming 2024年11月停业，多家垂直农场倒闭，产品仍比传统农业贵  
  来源：<https://en.wikipedia.org/wiki/Bowery_Farming>；<https://en.wikipedia.org/wiki/Vertical_farming>
- **#300** 「Bythemiddleofthe2020swewillhaveameansofinteractingwithacomputerthatist…」  
  判断：**错误**。到2020年代中期并未出现比键盘快数千倍的全沉浸式VR交互，头显仍是小众产品  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>

### 暂无法判断（211 条）

- **#1** 「Eventuallynanotechnologywillenablethesetrendstoculminateindirectlyexpa…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#2** 「InthiswaywewillmergewithAIandaugmentourselveswithmillionsoftimesthecom…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#3** 「Thiswillexpandourintelligenceandconsciousnesssoprofoundlythatit'sdiffi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#4** 「asthetransitionhappens,wewillenhanceourcognitionquicklyenoughtoadapt」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#5** 「long-termtrendssuggestthattheSingularitywillhappenaround2045」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#7** 「Duringthecomingdecade,peoplewillinteractwithAIthatcanseemconvincinglyh…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#8** 「Adigitalrevolutioninbiotechwillcurediseasesandmeaningfullyextendpeople…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#9** 「manyworkerswillfeelthestingofeconomicdisruption,andallofuswillfacerisk…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#10** 「Duringthe2030s,self-improvingAIandmaturingnanotechnologywillunitehuman…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#11** 「Ifwecanmeetthescientific,ethical,social,andpoliticalchallengesposedbyt…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#13** 「Asthesetechnologiesunlockenormousmaterialabundanceforourcivilization,o…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#14** 「Sonext,we'lllookaheadtothetoolswe'lluseoverthecomingdecadestogainincre…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#15** 「IntheFifthEpoch,wewilldirectlymergebiologicalhumancognitionwiththespee…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#18** 「PassingtheTuringtest,whichIhavebeenanticipatingfor2029,willbringustoth…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#19** 「Akeycapabilityinthe2030swillbetoconnecttheupperrangesofourneocorticest…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#20** 「Bythetimethishappens,thenonbiologicalportionsofourmindswillprovidethou…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#21** 「Asthisprogressesexponentially,wewillextendourmindsmanymillions-foldby2…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#23** 「Andafterintegratedcircuitshavereachedtheirlimits,newparadigmsusingnano…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#24** 「anactualself-drivingcarwillultimatelybeabletoperformmuch,muchbettertha…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#25** 「Thiscreativitywilltransformcreativefieldsthatrecentlyseemedstrictlyint…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#28** 「SuchabilitieswillrapidlyexpandAI'sreachintotherealworld.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#33** 「exponentialprice-performanceimprovementsmeanthatthecostofcomputationwi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#37** 「Itmightturnout,forexample,thatin2034AIcancomposeGrammy-winningsongsbut…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#40** 「Evenifitturnsouttorequire1016operationspersecond,$1,000ofhardwarewillp…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#41** 「computerswillbeabletosimulatehumanbrainsinallthewayswemightcareaboutwi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#42** 「childrenborntodaywilllikelyseetheTuringtestpassedwhiletheyareinelement…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#43** 「Between2023and2029,theyearIexpectthefirstrobustTuringtesttobepassed,co…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#45** 「eventhoughwemayseemarginalimprovementsfromAIandimprovedsensortechnolog…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#46** 「Ultimately,brain-computerinterfaceswillbeessentiallynoninvasivewhichwi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#47** 「Atsomepointinthe2030swewillreachthisgoalusingmicroscopicdevicescalledn…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#48** 「Thesetinyelectronicswillconnectthetoplayersofourneocortextothecloud,al…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#51** 「Theresultwillbetheinventionofmeansofexpressionvastlyricherthantheartan…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#53** 「ourmindswillbeempoweredtogrowexponentially,ultimatelyexpandingourintel…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#54** 「Yetthecausebehindsubjectiveconsciousnesswillsoonbemorethanjustasubject…」  
  判断：**暂无法判断**。“很快”无终点；意识扩展到生物大脑之外的技术尚未出现  
  来源：—
- **#55** 「Yetwhenwecanaugmenttheneocortexitself,duringthe2030sand2040s,wewon'tju…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#57** 「Soinitiallyitwillfalltothepeopledevelopingthemtoformulateethicalframew…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#64** 「duringthisdecadeourtechnologiesforrecording,storing,andorganizingthisi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#66** 「Peoplewillhavemixedreactionstothisforcultural,ethical,orpersonalreason…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#67** 「Replicantbodieswillexistmostlyinvirtualandaugmentedreality,butrealisti…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#68** 「thereisalreadysignificantresearchgoingonthatwilllaythegroundworkformuc…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#69** 「Eventuallyreplicantsmayevenbehousedincyberneticallyaugmentedbiological…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#70** 「Bythatpointreanimatedpeoplewilllikelytranscendtheuncannyvalley,atleast…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#72** 「Intheearly2040s,nanobotswillbeabletogointoalivingperson'sbrainandmakea…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#74** 「Oneofthemajorresearchprojectsofthenexttwodecadeswillbefiguringoutwhatl…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#75** 「Theseareawesomechallenges,butthesuperhumanAItoolsofthe2030swillenableu…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#76** 「FuturereplicantAIwillalsohaveaccesstoallkindsofmetadataaboutaperson'sl…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#78** 「howtheresultwillbeadramaticimprovementofmostaspectsoflifeintheverynear…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#79** 「Andasartificialintelligencegainsapplicabilitytomoreandmorefields,theex…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#80** 「That,inshort,iswhymostaspectsoflifewillbegettingexponentiallybetterint…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#81** 「overthenextcoupleofdecadesthisprogresswillgointoveryhighgear」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#83** 「thepercentagecontinuestoriseastheGreatestGenerationdeclinesandmillenni…」  
  判断：**暂无法判断**。可检验，但出版后的美国人口普查/ACS家庭电脑拥有率数据尚未覆盖足够年份，暂无法判断  
  来源：—
- **#84** 「bytheendofthisdecadewewillbeabletostarttheprocessofaugmentingandultima…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#86** 「Wewillthenbeabletostartdirectlyaddressingthebiologicalfactorsthatnowli…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#87** 「Inthe2030swewillreachthethirdbridgeofradicallifeextension:medicalnanor…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#88** 「Likewise,smartnanobotswillenabletargetedrepairorupgradingofindividualc…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#89** 「Thefourthbridgebeingabletobackupourmindfilesdigitallywillbea2040stechn…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#90** 「Thematurationof3Dprintingandeventuallynanotechnologywillexponentiallya…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#93** 「Oncehumanityhasextremelycheapenergy(largelyfromsolarand,eventually,fus…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#94** 「Inthiswaythemillions-foldimprovementininformationtechnologiesbetweenno…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#95** 「Cheaprenewableenergywillunlockgreatmaterialabundance,butpeoplesharingi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#96** 「Acrucialchallengeoverthecomingdecadeswillbehelpingcountriesthatfallint…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#97** 「Imaginehowtheexponentialprogressofthenexttwodecadeswillallowustorealiz…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#98** 「Asinformationtechnologymakesvastlymoreprogressinthenexttwentyyearsthan…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#100** 「Myresponse:thiswillallchangeoverthenextdecade.」  
  判断：**暂无法判断**。终点“未来十年”（约2034年）未到  
  来源：—
- **#102** 「Probablysometimeinthe2030sthiswillcrossintonanotechnology,whereobjects…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#103** 「thecostreductionwillsurelybeenormous.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#104** 「therewillbemanyfreedesignsavailablealongsideproprietaryones.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#105** 「thecoexistenceofanopen-sourcemarketwhichisandwillbeagreatlevelerwithth…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#107** 「Andmeatgrowncleanlyandethicallyfromcellcultureswilldisplaceenvironment…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#108** 「Whenculturedmeatcanconvincinglyimitateallitsanimal-basedcounterparts,h…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#109** 「Allthesetechnologieshavealreadybeensuccessfullydemonstratedandwillbeco…」  
  判断：**暂无法判断**。终点“本十年”（2029年）未到；目前垂直农场倒闭、多地立法禁售培养肉，方向不利  
  来源：<https://en.wikipedia.org/wiki/Cultured_meat>
- **#110** 「overthenextcoupleofdecades,brain-computerinterfacetechnologywillbecome…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#111** 「Culturedmeatandverticalfarmingwillenabletheseneedstobemetwithonlyasmal…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#112** 「Thiswillmakepossibleagreaterabundanceofhealthyfoodandaccommodateanincr…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#113** 「Autonomousvehicleswillfacilitateless-crowdedlandusebymakinglongercommu…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#114** 「Thisexperiencewilllikelyhavealong-termimpactonhowbothemployeesandemplo…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#115** 「AstheLOARtakesinformationtechnologiesintothesteeppartsoftheseexponenti…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#116** 「AI-assistedbreakthroughsinnanotechnologywillincreasecellefficiencybyen…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#117** 「Suchtechnologieswillallowphotovoltaicsofthefuturetobethinner,lighter,a…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#118** 「Intheyearsahead,nano-basedtechnologywillalsoreducemanufacturingcostsby…」  
  判断：**暂无法判断**。“未来几年”未满，3D打印光伏尚未产业化  
  来源：—
- **#119** 「Thiswillreduceinstallationcostsandgivemorecommunitiesaroundtheworldacc…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#121** 「From3.6percentin2021,itwouldtakeonlyabout4.8doublingstoreach100percent…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#122** 「Theimplicationisthatsolarwilldominatesometimeduringthe2030s.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#124** 「Inthecomingyears,nanoengineeredmaterialswillenablefilterstoworkfastera…」  
  判断：**暂无法判断**。“未来几年”未满，尚无可检验结果  
  来源：—
- **#126** 「Asverticalagriculturebecomeslessexpensiveandmorewidespread,itwillleadt…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#127** 「Inthecomingyears,converginginnovationsinphotovoltaicelectricity,materi…」  
  判断：**暂无法判断**。“未来几年”未满；目前垂直农业成本仍远高于传统农业  
  来源：<https://en.wikipedia.org/wiki/Vertical_farming>
- **#128** 「Manyfacilitieswillbepoweredbyefficientsolarcells,producenewfertilizers…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#129** 「Withveryfewworkersrequiredandasmalllandfootprint,futureverticalfarmswi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#130** 「As3D-printingtechnologyadvances,itwillbeabletohandleevenmoreexoticmate…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#131** 「Decentralizedmanufacturingwillalsohavesignificantenvironmentalbenefits…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#132** 「Asresolutionimproves(thatis,thesizeofthesmallestattainabledesignfeatur…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#134** 「Becauseprintingspeedisalsoincreasing,high-volumemanufacturingwillbecom…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#135** 「Scientistsarecurrentlytestingtechniquesthatwillmakepossibletheprinting…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#136** 「Thismethodwillultimatelybefarsuperiortotransplantingorgansfromoneperso…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#137** 「as3D-printedstructuresbecomelessexpensivetoproduce,theywillbecomeacomm…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#138** 「Ultimately,3Dprintingofbothbuildingmodulesandthesmallerobjectsthatgoin…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#139** 「Bythelate2020sitwillbepossibleforthisassemblyofmodulestobedonelargelyb…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#140** 「Chinaisalreadyahubof3D-printedbuildingsandwillhavemuchneedformorematur…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#141** 「Inthefuture,3Dprintingmaybeusedtomakeskyscraperseasierandcheapertobuil…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#142** 「A3D-printingsystem,togetherwithautonomousrobotsthatcanusebuildingmater…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#144** 「ultimatelytheeffectivenessofthetechnologywillwinout.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#145** 「AIsimulationswillhelpbreakthislogjam.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#146** 「animportantlineofresearchgoingforwardwillbefindingwaystominimizetheris…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#149** 「the2030swillbringanotherhealthrevolution,whichmybookonhealth(coauthore…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#150** 「Nanorobotsnotonlywillbeprogrammedtodestroyalltypesofpathogensbutwillbe…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#151** 「Medicalnanorobotswillmonitorthebloodsupplyandincreaseordecreasevarious…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#152** 「Usingthesetechnologies,bytheendofthe2030swewilllargelybeabletoovercome…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#153** 「byaround2030,themostdiligentandinformedpeoplewillreach“longevityescape…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#154** 「ThisscenariowillbecomerealisticasweapproachtheSingularityinthemid-2040…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#155** 「Whileadvancesinmedicineandneurosciencecannotpreventallofthosecases,the…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#156** 「afeaturethatwillbegreatlyenhancedbythe2040s.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#157** 「Thisforceiswhatwillmakelifeitselfexponentiallybetterinthetimeahead.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#158** 「Ouracceleratingprogress,withsubstantialgainsoverthepastfewdecadesandpr…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#159** 「Theconvergenttechnologiesofthenexttwodecadeswillcreateenormousprosperi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#160** 「Butthesesameforceswillalsounsettletheglobaleconomy,forcingsocietytoada…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#162** 「Whilethereisroomfordisagreementoverexactlyhowquicklyautonomousvehicles…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#163** 「Astruckdriverslosetheirjobstoautomation,therewillbelessneedforpeopleto…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#164** 「weknowAIisgoingtocontinuetoprogressexponentiallyuntilwehavesuperhuman-…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#165** 「Lookingtothefuture,theemergenceofautomatedverticalfarmingwilllikelyfos…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#166** 「AsAIandroboticsadvanceandrenewableenergybecomescheaper,therewilleventu…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#167** 「Asfoodpricesbecomelessdependentonhumanlaborandscarcenaturalresources,p…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#170** 「Driverless-vehicleAI,forexample,willreplacehumandriversaltogether.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#171** 「AsmoreandmoretasksfallwithinthecapabilitiesofAIandrobotics,therewillbe…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#172** 「Self-drivingcarswillbemuchsaferthanthoseoperatedbyhumandrivers,andtheA…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#173** 「Asthistechnologyadvances,humangraphicdesignersmayspendlesstimephysical…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#174** 「Inthelongterm,theeconomicincentivesforautomationwillpushAItotakeoveran…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#175** 「AsAIapproacheshumanand,shortlythereafter,superhumanlevelsofcompetence,…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#176** 「artificialintelligenceandtechnologicalconvergencewillturnmoreandmoreki…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#177** 「AdvancedAItutorswillmakepossibleindividuallytailoredlearningonanysubje…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#178** 「AI-enhancedmedicineanddrugdiscoveryarestillintheirinfancyasofthiswriti…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#179** 「AI-drivenadvancesinmaterialssciencewillmakesolarphotovoltaicelectricit…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#180** 「Withcheapenergyandmaterials,andautomationincreasinglyreplacinghumanlab…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#181** 「inthe2030sitwillberelativelyinexpensivetoliveatalevelthatisconsideredl…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#185** 「AsAIunlocksunprecedentedmaterialabundanceacrosscountlessareas,thestrug…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#187** 「Overthenexttwodecadesthistransformationwillacceleratedramatically.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#188** 「Thesecapabilitieswillbecomemoresophisticatedandwillexpandtomusic,video…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#189** 「PeoplewillbeabletodescribetheirideastoAIandtweaktheresultswithnaturall…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#190** 「Insteadofneedingthousandsofpeopleandhundredsofmillionsofdollarstoprodu…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#191** 「Automationanditsindirecteffectshavealreadyeradicatedmanyjobsnearthebot…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#192** 「Asawhole,oursocietyhasmoveduptheskillladder,andthiswillcontinue.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#193** 「Searchwilltransformfromthefamiliarparadigmoftextstringsandlinkpagesint…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#194** 「Real-timetranslationbetweenanypairoflanguageswillbecomesmoothandaccura…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#195** 「Augmentedrealitywillbeprojectedconstantlyontoourretinasfromourglassesa…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#196** 「Mostofitsfunctionsandinformationwillnotbeexplicitlyrequested,butoureve…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#197** 「Inthe2030s,medicalnanorobotswillbegintointegratethesebrainextensionsdi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#198** 「Thiswillbeavailabletoeveryoneandultimatelywillbeinexpensive,justasmobi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#200** 「asAI-drivenadvancesmakeitpossibleformedicine,food,andhousingtobemuchch…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#202** 「Thankstoacceleratingtechnologicalchange,overallwealthwillbefargreater,…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#205** 「asweenteraneraofabundance,andtheavailabilityofmaterialnecessitiesevent…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#206** 「whenwedigitallyaugmentourneocortexstartingsometimeinthe2030s,wewillbea…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#207** 「informationtechnologyhasbeengrowingandwillcontinuetogrowexponentiallyi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#208** 「weareheadedtowardaneraofabundancethatwillmeetourphysicalneedsandthatth…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#209** 「autonomousvehicleswillbringmassivebenefitstosocietyfromsavedlivestolow…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#211** 「theharmsfromautonomousvehicleswillbemainlyconfinedtotheseveralmillionp…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#213** 「thesepositivechangeswillcomeasquicklyasthedisruptiveones」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#214** 「Inasimilarway,wewillharnesstheadvancesof2030and2040toseamlesslyaugment…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#215** 「Butmyexpectationisthataviolenttransitionisunlikely,giventhepowerfullon…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#216** 「Butthesametechnologiesthatwillcausethesesocialdisruptionswillalsobemak…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#219** 「asAIplaysanevergreaterroleinmedicine,healthcarewillreaptheexponentialb…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#220** 「Bythetimeyoureadthis,evenmoreadvancedmethodswilllikelybeavailable.」  
  判断：**暂无法判断**。缺乏与2021年USC工具可直接比较的公开评估，暂无法判断  
  来源：—
- **#221** 「itwillsoonreachthebillions.」  
  判断：**暂无法判断**。“很快”无终点；AlphaFold数据库约2亿条结构，宏基因组预测库数亿条，尚未达到“数十亿”  
  来源：<https://en.wikipedia.org/wiki/AlphaFold>
- **#222** 「Thiswillgreatlyacceleratethepaceofbiomedicaldiscoveries.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#223** 「Overthecomingdecades,though,AIwillgainthecapacitytosearchmorecreativel…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#225** 「Meanwhile,AIwillscaleuptomodelingeverlargersystemsinsimulationfromprot…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#226** 「Doingsowillenableustocurediseaseswhosecomplexityputsthemoutofthereacho…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#227** 「WithAIsimulationswe'llbeabletounderstandtheirrootcausesandtreatpatient…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#228** 「Thosesamebrain-simulationtoolswillalsoletusachievebreakthroughsforment…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#230** 「Simulationswillbeabletofindnumeroussuchcorrelations,yieldinghighlyspec…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#234** 「Thisisalong-termgoal,butitisoneofthemostprofoundlyimportantlifesavingo…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#235** 「Therewilllikelybesubstantialresistanceinthemedicalcommunitytoincreasin…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#238** 「Forthesamereason,itwillberelativelyeasytogeneralizesystemslikeCheXNeta…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#239** 「UltimatelyAIwilllikelybeabletounlockvastuntappedpotentialinmedicalimag…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#240** 「Thiswillmakesurgerymuchsaferandmoreeffectivethanitistoday.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#241** 「asnanotechnologyadvances,thedigitalrealmwillbeabletopullevenfurtherahe…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#242** 「theywillleaveunaugmentedbiologicalbrainsinthedust.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#244** 「eventhoughitwillbeatleastadecadebeforethefieldstartsmaturing,likelyaid…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#245** 「Overthenextdecade,though,AIwillallowdetailedchemistrysimulationsthatun…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#246** 「allofwhichwillseeahugevarietyofpracticalapplicationsoverthenexttwodeca…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#247** 「consideringthatsuperhumanengineeringAIwillbeavailablebytheendofthe2020…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#248** 「Butconvergentinnovationswillbedramaticallyreducingmostofthosecostsinth…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#249** 「Rawmaterialswillbecheapertoextractorsynthesizewithautomation,roboticsw…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#251** 「the“informationcontent”ofmostproductsisrapidlyincreasingandwillultimat…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#252** 「Inmanycases,thiswillmakeproductscheapenoughthattheycanbefreetoconsumer…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#253** 「Thisdramaticreductionofphysicalscarcitywillfinallyallowustoeasilyprovi…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#254** 「withthesetechniqueswewillbeabletodiscoververypowerfulnewtherapiesinday…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#255** 「The2030swillusherinthethirdphaseoflifeextension,whichwillbetousenanote…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#256** 「eventhoughitwillcertainlytakedecadestofullyaccomplish」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#259** 「WithAIplayingakeyroleinresearchbythen,progressduringthattimewillbeexpo…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#262** 「AsIseeit,thelong-termgoalismedicalnanorobots.Thesewillbemadefromdiamon…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#265** 「akeyroleofthesenanobotswillbetorepairandaugmentthem.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#266** 「Ultimately,nanobotswillbeabletoreplacebiologicalorgansaltogether,ifnee…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#267** 「Althoughcancermedicinehasmadeamazingstridesoverthepastdecadeandwillmak…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#271** 「AsAIgainsgreaterabilitytounderstandhumanbiology,itwillbepossibletosend…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#272** 「evenourbloodsupplymaybereplacedbynanobots」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#273** 「Ultimately,evenheartsmadefromnanomaterialswillmakepeopleimmunetohearta…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#274** 「Yetthemostimportantroleofnanotechinourbodieswillbeaugmentingthebrainwh…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#275** 「Adeepervirtualneocortexwillgiveustheabilitytothinkthoughtsmorecomplexa…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#277** 「Basedonthe2000-2023trend,by2053about$1,000ofcomputingpower(in2023dolla…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#278** 「Inthe2040sand2050s,wewillrebuildourbodiesandbrainstogovastlybeyondwhat…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#279** 「Asnanotechnologytakesoff,wewillbeabletoproduceanoptimizedbodyatwill:we…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#280** 「Wewillthinkmillionsoftimesfaster,butmostimportantly,wewillnotbedepende…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#284** 「Nanotechnologywillmakepossibleawiderangeofoffensiveweapons,manyofwhich…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#288** 「asAImodelsaregivenincreasinglycomplextasks,itwillbecomemorechallenging…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#294** 「Thisoppositionwillultimatelyfail,however,becausethedemandfortherapiest…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#295** 「Butinthe2020swewillhavevirtualandaugmentedrealitydeliveredinverycompac…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#296** 「Wewillinhabitvastvirtualandaugmentedrealitieslimitedonlybyourimaginati…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#298** 「Inoneareaafteranother,theywillbebetterthanallhumansby2029.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#299** 「Butitwillstillhappen,partlydrivenbythegoaloffixingthesignificantbraind…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#301** 「Thiswillultimatelyreplaceinteractionbykeyboards.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#302** 「externalbrainextenderswithadvancedAIwillletusperformdifficulttasksands…」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—
- **#303** 「Idothinkwewillachieveanextensionoftheneocortexbytheearly2030s.」  
  判断：**暂无法判断**。原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 12 | AsIwillshow,thelawofacceleratingreturnsi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 16 | Ultimately,whenaprogrampassestheTuringte… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 17 | Thus,attheTuringtestlevel,AIswillhavecap… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 36 | ThiscapabilitywillaffordAIcrucialflexibi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 38 | Sotheremaywellbeasignificanttransitional… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 39 | oncewetriggeranintelligenceexplosion,any… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 44 | WhenAIlanguageunderstandingcatchesuptoth… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 49 | oncewehavethefirstlayerofvirtualneocorte… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 50 | Whenwecanaccessadditionalneocortexinthec… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 52 | Butwemighteventuallyhaveartthatputsachar… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 56 | Idoubtthatourpoliticalsystemwilladaptfas… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 58 | Perhapsafuture“theoryofeverything”willun… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 59 | Althoughitwilleventuallybecomepossibleto… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 60 | AkeyissueIexploredinHowtoCreateaMindisth… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 61 | Asweplacenonbiologicalsystemsintoourbodi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 62 | Copyingourmindfilestoaremotebackupstorag… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 63 | ourlegalandethicalsystemswouldlikelyhave… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 71 | Asthistechnologybecomesmoreprevalent,soc… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 73 | Thiswouldbethemosttheoreticallycompletes… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 77 | Onceourbrainsarebackeduponamoreadvancedd… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 92 | Idon'tthinkthiswillbepermanent. | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 101 | Suchgoodswill,therefore,besubjecttothesa… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 125 | Itispossiblethatfuturearchaeologicaldisc… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 133 | Oncethetechnologycanachievefabric-likedi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 143 | Thetransitionfromhumantrialstosimulatedi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 147 | OncewecananalyzethemechanismsofiPSaction… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 148 | Asaresultofthesetechnologies,theoldlinea… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 168 | IfIamcorrectthatsignificantlife-extensio… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 169 | Trendslikethistendtoreplacelow-payingjob… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 182 | technology-drivendeflationinallthesearea… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 183 | evenastechnologicalchangeisrenderingmany… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 184 | Maximizingthequalityoftheseopportunities… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 186 | Theupcomingrevolutionwillempowerhumansfo… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 201 | Ifthispercentagecontinuestogrow,itcanfun… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 203 | Althoughinnovationwillunlocktransformati… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 204 | peoplemightspreadsimilarrumorsaboutdecis… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 210 | eventhoughweknowstatisticallythattensoft… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 212 | thedifferencethistimewillbethebreadth,de… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 218 | Turningmedicineintoanexactsciencewillreq… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 224 | itmightidentifyaproblemthathumanclinicia… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 231 | Drugsconsistingmainlyofasinglemoleculear… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 232 | AIsimulationswillneedtomodelnotjustthedi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 233 | Buttovalidatethesetoolsassafe,we'lllikel… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 236 | simulationswillneedaverysolidtrackrecord… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 243 | Thiswillallowformoreefficientcomputation… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 250 | Asallthesecomponentsofvaluebecomelessexp… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 257 | theannualriskofdeathwouldnolongerincreas… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 258 | Ifthenanotechnologyof2050solvesenoughiss… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 260 | Soeventhoughtheseprojectionsareadmittedl… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 261 | Forbabiesbornin2024,thetechnologicaladva… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 263 | Sonanobotswillneedtoharnessdifferentprin… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 264 | Likewise,nanobotsprobablywon'tbeabletost… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 268 | Oncenanobotscanselectivelyrepairordestro… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 269 | AIwillallowustosimulateitinenoughdetailb… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 270 | Atfirstsuchtreatmentswouldbeinitiatedbyh… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 276 | Evenifonlyaminusculefractionofthesevalue… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 281 | Thereisgoodreasontobelievethatourciviliz… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 282 | Aslongashigh-alertarsenalsaremaintainedi… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 283 | AI-drivencountermeasureswillbecriticalto… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 285 | SincenanotechwillbetakingadvantageofAI-o… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 286 | theactualrateofdestructionwouldbemuchslo… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 287 | Idobelieveitwillproveaworkableapproach. | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 289 | Further,whatwill“human”evenultimatelymea… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 290 | regardlessofanyexplanationtheyprovide,we… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 291 | whichwillbeagrowingriskasmachine-learnin… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 292 | militarypowerswillhavestrongincentivesto… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 293 | italsoincreasesthechancesthatsafetypreca… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 297 | WhileAIiscreatingnewtechnicalthreats,itw… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |
| 304 | Sothein-betweenperiodprobablywon'tbevery… | 长期愿景/条件推演/一般机制 | 无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件 |

## 文件

- 本文：`cases/kurzweil-singularity-nearer-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/kurzweil-singularity-nearer-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/kurzweil-singularity-nearer-v5/audit/manual_review_2026-11-15.py`
