# Manual review of 奇点更近 (Kurzweil, The Singularity Is Nearer 2024), review_source manual-assistant-2026-11-15
import json as _j
_pre=_j.load(open(__file__.rsplit('/',1)[0]+'/prescreen.json'))
AIX='https://hai.stanford.edu/ai-index/2025-ai-index-report'
EPC='https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year'
EPP='https://epoch.ai/data-insights/llm-inference-price-trends'
NHGRI='https://www.genome.gov/about-genomics/fact-sheets/Sequencing-Human-Genome-cost'
WFH='https://wfhresearch.com/'
FDA='https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs'
IEA='https://www.iea.org/reports/tracking-sdg7-the-energy-progress-report-2025'
BNEF='https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/'
CBO='https://www.cbo.gov/system/files/2025-06/61302-MBR.pdf'
APPLE='https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250507.pdf'
META=dict(title='雷·库兹韦尔《奇点更近》',
 pub='英文原版 *The Singularity Is Nearer: When We Merge with AI*，Viking，**2024-06-25**。观察窗口为 2024-06-25 至 2026-11-15，仅约两年半。',
 method='本书的大多数判断指向 2029 年（AI 通过图灵测试）、2030 年代（脑机接口、纳米机器人）和 2045 年（奇点）。按规则，写明或隐含的终点尚未到达者（202 条）一律记暂无法判断，不因方向已有苗头而提前计分；70 条为条件推演、一般机制或无时点的长期愿景，作为非预测剔除（其中第 83 条“美国拥有电脑的家庭比例将继续上升”实际可检验，改为计入预测，但出版后的官方数据尚未发布，记暂无法判断）。真正能在本窗口内检验的，主要是“到你读到本书时”“未来几年”一类近期判断。',
 overall=('在出版后两年多的短窗口里，库兹韦尔的近期判断准确率很高：大语言模型用户规模（ChatGPT 2026 年 2 月周活约 9 亿）、AI 投资与论文数量继续创新高、编程 AI 显著增强（SWE-bench 成绩一年内由个位数升到七成以上）并催生“氛围编程”、办公套件全面集成 AI、前沿模型训练算力每年约 4—5 倍增长、大模型推理价格下降远快于算力成本、Waymo 扩展到洛杉矶并进入更多城市、锂电池价格继续下降（2025 年 108 美元/千瓦时）、美国凶杀率 2024—2025 年大幅下降、社会保障支出继续增长、穿戴设备开始在用户察觉前提示疾病（2025 年 Apple Watch 高血压提醒获 FDA 批准）、FDA 推动以 AI 计算模型替代部分动物试验，这些都已兑现。\n\n'
 '错误集中在他最乐观的“物质丰裕”与人机交互判断：AI 控制的垂直农业“很快”带来低成本食物——实际上 Bowery 等明星垂直农场在 2024—2025 年相继倒闭；远程办公“可能加强”——实际上大公司和美国联邦政府推行返岗，远程办公比例停滞；“到 2020 年代中期出现比键盘快数千倍的全沉浸式 VR 交互”——没有出现。需要强调：本书的核心预测（2029 年 AGI、2030 年代脑机融合、纳米医学与 2045 年奇点）全部尚未到期，记为暂无法判断；当前胜率只反映其近期、渐进性判断的质量，不能外推为对全书核心命题的检验。'))
NF={i:('长期愿景/条件推演/一般机制','无可检验时点的长期设想、条件推演或一般规律，不针对窗口内的具体事件') for i in _pre['NF'] if i!=83}
HFR='原文终点（2029年、2030年代、2045年或“未来数十年”等）尚未到达，按规则记暂无法判断'
V={i:('U',HFR,[]) for i in _pre['HF']}
V.update({
83:('U','可检验，但出版后的美国人口普查/ACS家庭电脑拥有率数据尚未覆盖足够年份，暂无法判断',[]),
6:('C','ChatGPT 2026年2月周活跃用户约9亿，远超“数千万人”；但此条在出版时已基本成立',['w:ChatGPT']),
22:('C','斯坦福《AI指数2025》显示2024年全球企业AI投资、AI论文与专利数量均高于2022年',[AIX]),
26:('C','编程AI显著增强：SWE-bench 解题率2023年约4%，2024年升至约72%',[AIX]),
27:('T','2025年“氛围编程”（不写代码、用自然语言让AI生成软件）流行，非程序员开发软件门槛大降；“释放巨大潜能”尚待观察',['w:Vibe coding']),
29:('C','出版后出现推理模型（OpenAI o1，2024年9月）、视频生成与智能体等多项重大进展',['w:OpenAI o1']),
30:('C','AI更深入日常生活，ChatGPT成为全球访问量前五的网站之一',['w:ChatGPT']),
31:('C','微软365 Copilot、谷歌Workspace内置Gemini已大规模推出',['w:Microsoft Copilot','w:Gemini (chatbot)']),
32:('C','Epoch AI 统计前沿模型训练算力每年约增长4—5倍，出版后仍延续',[EPC]),
34:('C','Epoch AI 统计同等能力大模型的推理价格每年下降数十倍以上，远快于硬件算力成本下降',[EPP]),
35:('P','AI已用于芯片设计（谷歌AlphaChip用于TPU布局），但尚无证据表明芯片性价比提升因此“加速”',['w:AlphaChip']),
54:('U','“很快”无终点；意识扩展到生物大脑之外的技术尚未出现',[]),
65:('C','2024—2025年AI在写作、语音、人脸与对话上大幅提升，并出现融合声音与画面的视频生成（Sora 2、Veo 3），逼真度大增',['w:Sora (text-to-video model)','w:Veo (text-to-video model)']),
82:('C','光伏装机连年创纪录，离网太阳能是新增电力接入的主要来源之一，全球无电人口继续减少',[IEA,'w:Growth of photovoltaics']),
85:('T','基因组测序成本继续下降；AI是否使其“再次加速”尚无明确证据',[NHGRI]),
91:('W','出版后远程办公并未加强：亚马逊等大公司和美国联邦政府推行全面返岗，远程办公占比基本停滞',[WFH,'w:Remote work']),
99:('T','2024—2026年AI芯片性价比持续快速提升，但“速率持续不减”需更长时间检验',[EPC]),
100:('U','终点“未来十年”（约2034年）未到',[]),
106:('W','“很快”实现AI垂直农业低成本食物未见端倪：Bowery Farming 2024年11月停业，多家垂直农场倒闭，产品仍比传统农业贵',['w:Bowery Farming','w:Vertical farming']),
109:('U','终点“本十年”（2029年）未到；目前垂直农场倒闭、多地立法禁售培养肉，方向不利',['w:Cultured meat']),
118:('U','“未来几年”未满，3D打印光伏尚未产业化',[]),
120:('T','光伏组件价格2024年后跌至历史低位，可再生能源装机继续快速增长；AI材料发现的贡献尚不明显',['w:Growth of photovoltaics']),
123:('C','彭博新能源财经：锂电池组均价2024年降20%至115美元/千瓦时，2025年再降8%至108美元/千瓦时',[BNEF]),
124:('U','“未来几年”未满，尚无可检验结果',[]),
127:('U','“未来几年”未满；目前垂直农业成本仍远高于传统农业',['w:Vertical farming']),
161:('C','Waymo 2024年11月向洛杉矶公众开放，2025年进入奥斯汀、亚特兰大等城市',['w:Waymo']),
199:('C','美国社会保障、联邦医疗保险和医疗补助支出2025财年继续增长约7—8%',[CBO]),
217:('C','美国凶杀率2024年大幅下降，FBI 2025年数据显示暴力犯罪再降9.3%、谋杀下降18.1%',['w:Crime in the United States']),
220:('U','缺乏与2021年USC工具可直接比较的公开评估，暂无法判断',[]),
221:('U','“很快”无终点；AlphaFold数据库约2亿条结构，宏基因组预测库数亿条，尚未达到“数十亿”',['w:AlphaFold']),
229:('T','2025年4月FDA宣布以AI计算模型等新方法逐步替代单抗等药物的动物试验，监管纳入模拟的方向明确；在疫苗审批中的应用仍有限',[FDA]),
237:('T','2025年9月FDA批准Apple Watch基于机器学习的高血压提醒功能，可在用户确诊前发出提示；“建议治疗”尚未普及',[APPLE]),
300:('W','到2020年代中期并未出现比键盘快数千倍的全沉浸式VR交互，头显仍是小众产品',['w:Apple Vision Pro']),
})
