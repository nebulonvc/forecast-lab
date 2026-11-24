# AI 2041（李开复、陈楸帆，2021）：出版后预测人工核查

- 案例目录：`cases/lee-ai-2041-v5/`
- 出版日期：2021-09（Currency / Penguin Random House，ISBN 9780593238301）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

复刻仓库 v5 流水线，仅以人工通读替代模型调用。对官方 248 个 3500 字块（含 600 字上下文）逐块抽取：陈楸帆的十篇科幻正文不视为预测，只收录李开复导言、各章 NOTE FROM KAI-FU 与分析章节中面向未来、日后可核验的判断。英文 changes / horizon / time_text 均为引文的逐字单行子串。核验使用 Exa 检索（密钥池第 4 行，仅按路径读取）并本地存档带 sha256 的公开来源，再经 pipeline apply assess → check → report。密度 109/248=0.440，高于英文基线 0.2–0.35，是因为分析章时间表明密、故事章按规定留空。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 109 条，剔除非预测 0 条，计入 **109 条预测**，其中 **67 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 16 |
| 趋势符合 | 17 |
| 部分符合 | 34 |
| 错误 | 0 |
| 暂无法判断 | 42 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **23.9%**（16/67） |
| 加权胜率 | **68.3%** |
| 错误率 | **0.0%**（0/67） |
| 未定占比（暂无法判断/预测） | 38.5%（42/109） |

## 总体评价

本书是“科幻故事＋技术分析”合集，核验窗口只有约五年（2021-09 至 2026-11-15），而大量预测指向 2030–2041，因此“趋势符合”最多（46 条），明确判错为 0：多数 2041 终点尚未到，只要主要方向仍成立就记趋势符合，不把阶段进展算终局正确。已能在窗口内看到的无期限方向记正确，例如自然语言处理在十年尺度上的迅猛崛起（ChatGPT 等大模型）、全天候对话助手、深度伪造对发达国家的冲击、自主武器军备竞赛、机器人与 RPA 持续接管任务、人机共生协作等。部分符合主要包括：2025 年量产 XR 眼镜（Apple Vision Pro 是头显而非眼镜）、无人驾驶公交三年内成为现实仅有有限部署、到 2041 放射科工作大多被接管在目前岗位仍增长的情况下进展有限、培养肉商业化停滞、情绪识别的科学基础受到质疑、GDPR 实施效果复杂等。暂无法判断 24 条多为净社会影响、种姓制度、物质丰裕、4000 逻辑比特量子计算机、XR 隐形眼镜普及、人类驾驶被禁、幸福定义演变等不可测或条件未满足的远期命题。严格胜率 18.8% 偏低，主要因为终点多在 2041；加权胜率 72.9% 更能反映“方向大体对、时点未到”的格局。错误率为 0 并不表示这些预测最终不会失败，只说明到截止日还没有足够证据把主要预测判为已经证伪。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（16 条）

- **#1** 「The applications for deep learning—and its related AI technologies—will touch nearly every aspect of our lives…」  
  判断：**正确**。自2022年末ChatGPT发布以来，生成式人工智能已进入搜索、办公、手机和消费软件等日常场景，方向与“触及生活几乎每个方面”相符。该项为无日期方向性预测，窗口内主结果已出现。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/AI_era>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#7** 「It will take over routine tasks and liberate us to do more stimulating or challenging」  
  判断：**正确**。无日期方向性预测。客服自动化、文档处理、代码补全和RPA已在多个行业接管常规任务，主方向在窗口内已经出现。  
  来源：<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>；<https://en.wikipedia.org/wiki/ChatGPT>；<https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf>
- **#8** 「Lastly, humans will work symbiotically with AI, with AI performing quantitative analysis, optimization, and ro…」  
  判断：**正确**。GitHub Copilot、办公助手和行业专用AI工具已使“AI做常规与优化、人做判断”成为常见工作方式，与人机共生的主判断相符。  
  来源：<https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf>；<https://en.wikipedia.org/wiki/ChatGPT>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#11** 「I believe that even with few or no breakthroughs, AI is still poised to make a profound impact on our society.」  
  判断：**正确**。大模型主要是规模化扩展已有深度学习，并非全新基础范式，却在2022年后带来广泛社会与产业冲击，符合“即便很少突破仍将产生深远影响”。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/AI_era>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#12** 「From the past era to the present day, the unstoppable force of AI has been revolutionizing every dimension of …」  
  判断：**正确**。2021年后生成式AI、生物计算和自动驾驶等继续扩展人工智能对经济与文化的影响，与“将继续变革人类文明各维度”的方向一致。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/AI_era>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#15** 「While the story is set in 2041, the situation described above is likely to impact the developed world earlier …」  
  判断：**正确**。深度伪造的大规模滥用、检测工具和立法讨论主要先出现在美欧等发达国家，与“更早冲击发达国家”的判断相符。  
  来源：<https://en.wikipedia.org/wiki/Deepfake>；<https://www.theverge.com/report/806359/openai-sora-deepfake-detection-c2pa-content-credentials>；<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>
- **#23** 「NLP), which is poised for a meteoric rise in the coming decade, including the capacity for AI to teach itself」  
  判断：**正确**。自监督语言模型在2022年后迅速成为主流平台技术，ChatGPT等产品证明自然语言处理在“未来十年”前半段已迅猛崛起。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>；<https://en.wikipedia.org/wiki/AI_era>
- **#26** 「They will be capable of offering help 24/7, which humans often cannot.」  
  判断：**正确**。ChatGPT等对话系统已能全天候回答问题并提供客服与辅导，主结果在出版后数年内已经出现。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/List_of_chatbots>
- **#27** 「I believe the kind of romantic-adjacent relationship depicted in the movie Her would be rare.」  
  判断：**正确**。虽有个别把聊天机器人当作伴侣的报道，这类近乎《Her》的浪漫关系仍属少数，与“将会很少见”相符。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Artificial_intelligence_controversies>
- **#31** 「In twenty years, deep learning and its extensions will beat humans on an ever-increasing number of tasks, but …」  
  判断：**正确**。生成式模型已在翻译、编程、图像识别等越来越多任务上达到或超过常人水平，同时在常识、责任和精细操作上人类仍有优势，两项都已可观察。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#34** 「what has become clear now is that AI will reshape healthcare, from speeding the discovery of vaccines and drug…」  
  判断：**正确**。AlphaFold、医学影像模型和早期AI药物管线已改变科研与部分临床流程，无日期的“将重塑医疗保健”方向已经出现。  
  来源：<https://en.wikipedia.org/wiki/AlphaFold>；<https://med.stanford.edu/radiology/news/2026-news/award-winning-study-puts-ai-s-impact-on-radiology-into-perspecti.html>；<https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really>
- **#36** 「This, in turn, will accelerate digitization and the speed of data collection. More data means better AI, which…」  
  判断：**正确**。新冠期间远程办公、在线教育和数字化流程被强制推广，并成为后续自动化的基础，与加速数字化和岗位替代条件的判断相符。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#67** 「Governments will approve pervasive AV only when it is “safer than people.”」  
  判断：**正确**。监管机构普遍以证明不低于人类安全作为扩大自动驾驶运营的前提，与“只有更安全才会批准普及”的原则相符。  
  来源：<https://en.wikipedia.org/wiki/Self-driving_car>；<https://en.wikipedia.org/wiki/Waymo>
- **#75** 「In the near future, robots will be able to perform the same function, when costs come down.」  
  判断：**正确**。开源组件和低成本无人机已使《Slaughterbots》式场景在技术上可被爱好者或武装组织接近实现，与“近未来成本下降后即可执行相同功能”相符。  
  来源：<https://www.theguardian.com/world/2026/nov/06/autonomous-weapons-ai-russia-us-binding-rules>；<https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/>
- **#76** 「This will surely be exacerbated with autonomous weapons, because there are many more ways to “win”」  
  判断：**正确**。主要军事大国继续研发自主武器，美国和俄罗斯等在2026年仍阻挠有约束力的国际规则，军备竞赛被加剧的判断成立。  
  来源：<https://www.theguardian.com/world/2026/nov/06/autonomous-weapons-ai-russia-us-binding-rules>；<https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/>
- **#80** 「robotics and robotic process automation will continue to evolve to take over tasks for both white-collar and」  
  判断：**正确**。机器人流程自动化和仓库、工厂机器人在2021年后继续扩大对白领常规任务和蓝领搬运分拣的替代，主方向已经出现。  
  来源：<https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>；<https://en.wikipedia.org/wiki/Technological_unemployment>

### 趋势符合（17 条）

- **#14** 「I am confident there will be technology and policy solutions to address the challenges of AI’s influence, bias…」  
  判断：**趋势符合**。欧盟《人工智能法》已通过并按时间表实施透明与禁止性规定，说明政策方案在推进，但到2028年才全面落地，偏见与不透明问题也未解决。  
  来源：<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>；<https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline>
- **#16** 「By 2041, fully photo-realistic 3D models should be possible, as we will see in “Twin Sparrows” and “My Hauntin…」  
  判断：**趋势符合**。视频生成和三维高斯溅射已能做出接近照片级的画面，但动态三维一致性仍是开放问题。朝2041年终点的方向明显，终点未到。  
  来源：<https://www.theverge.com/report/806359/openai-sora-deepfake-detection-c2pa-content-credentials>；<https://arxiv.org/html/2503.13272>
- **#20** 「By 2041, AI will take over this “routine” task of recognizing and verifying people.」  
  判断：**趋势符合**。消费级面容与指纹解锁、机场和边境生物识别已大量接管日常核验，但公共部门与高风险场景仍并行使用人工核验。朝2041年终点推进，尚未完全接管。  
  来源：<https://en.wikipedia.org/wiki/Deepfake>；<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>
- **#24** 「What’s the chance of humans being able to form relationships with sophisticated AI companions like Atoman with…」  
  判断：**趋势符合**。儿童和青少年已广泛使用对话机器人和陪伴应用，关系化使用已经出现，但尚未普遍达到故事中那种高保真长期陪伴。二十年窗口未结束。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/List_of_chatbots>
- **#37** 「With a data-centric and pragmatic approach, AI healthcare will surely blossom in the next twenty years.」  
  判断：**趋势符合**。AI在影像、蛋白质结构和早期药物研发中已明显展开，医疗AI仍处扩张期，二十年窗口未结束。  
  来源：<https://en.wikipedia.org/wiki/AlphaFold>；<https://med.stanford.edu/radiology/news/2026-news/award-winning-study-puts-ai-s-impact-on-radiology-into-perspecti.html>；<https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really>
- **#41** 「we can expect all surgeries will have some robotic participation in twenty years, with fully autonomous roboti…」  
  判断：**趋势符合**。机器人辅助手术比例较2010年代上升，但远未覆盖“所有手术”，全自主手术更未占多数。朝窗口方向前进，终点未到。  
  来源：<https://med.stanford.edu/radiology/news/2026-news/award-winning-study-puts-ai-s-impact-on-radiology-into-perspecti.html>
- **#45** 「But by 2041, warehouses should be virtually automated, while factories will be mostly automated.」  
  判断：**趋势符合**。亚马逊已部署超过一百万台仓库机器人，并接近机器人与员工数量持平，工厂自动化也在推进，但离“仓库几乎全部、工厂大部分自动化”仍有距离。  
  来源：<https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/>；<https://www.cnbc.com/2025/10/22/amazon-switch-to-robots-will-save-it-up-to-4-billion-a-year-morgan-stanley-says.html>
- **#47** 「All of these technology components exist now—and will be fine-tuned and integrated in the decade to come.」  
  判断：**趋势符合**。商用与家用机器人组件在2021年后继续集成，自动配送和清扫等产品已更常见，十年窗口尚未结束。  
  来源：<https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/>；<https://en.wikipedia.org/wiki/Robotaxi>
- **#49** 「By 2041, I predict that computer vision technologies will be able to unpack a scene into its」  
  判断：**趋势符合**。分割、深度和场景理解模型已能拆解图像中的主要物体，但“理解几乎所有成分的作用”仍未达到，2041年终点未到。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>；<https://arxiv.org/html/2503.13272>
- **#50** 「I predict that MR will develop the capability to add new virtual objects to environments, presenting them in w…」  
  判断：**趋势符合**。Apple Vision Pro等混合现实设备已能把虚拟物体放入真实房间，物理交互仍有限，方向正确但能力未完成。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#55** 「The technologies are already in early commercial products and should mature well before 2041 for many」  
  判断：**趋势符合**。消费级触觉背心和体感配件已有早期商品，距离“对许多应用足够成熟”仍有差距，但方向与“2041年前成熟”一致。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#66** 「So, over the long term, we can certainly expect much greater safety from AV.」  
  判断：**趋势符合**。Waymo等公布的里程和事故数据支持在运营设计域内比人类司机更安全，但“长期、高得多的总体安全性”仍有待更广域部署。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#69** 「These jobs will be gradually replaced by AI.」  
  判断：**趋势符合**。无人出租开始替代部分网约车行程，但出租车、卡车和公交司机岗位在总体上仍主要由人类承担，替代是渐进的。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Robotaxi>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#78** 「I hope I’ve established that autonomous weapons are already a clear and present danger, and will become more i…」  
  判断：**趋势符合**。自主武器在感知、协同和可得性上持续升级，国际谈判却滞后，与“更快变得更智能、更致命、更易获取”的方向一致。  
  来源：<https://www.theguardian.com/world/2026/nov/06/autonomous-weapons-ai-russia-us-binding-rules>；<https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/>
- **#102** 「We are approaching a confluence of improved solar, wind, and battery technologies with the capacity to rebuild…」  
  判断：**趋势符合**。国际能源署预计可再生能源发电占比将由2025年约33%升至2031年近45%，风光发电量将翻倍以上，具备继续改写电力结构的能力，但“到2041年重建全球能源基础设施”尚未完成。  
  来源：<https://www.iea.org/reports/global-energy-review-2026/electricity-supply>；<https://en.wikipedia.org/wiki/Renewable_energy>
- **#103** 「By 2041, much of the developed world and some developing countries will be primarily powered by solar and wind…」  
  判断：**趋势符合**。全球电力中可再生能源份额2025年约34%，部分国家风光占比很高，但多数发达国家仍未“主要由太阳能和风能供电”。  
  来源：<https://www.iea.org/reports/global-energy-review-2026/electricity-supply>；<https://en.wikipedia.org/wiki/Renewable_energy>；<https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production>
- **#104** 「By 2041, it should be even lower, as the prices of these three components continue to descend.」  
  判断：**趋势符合**。风光度电成本已大幅下降并在许多市场成为最便宜的新电源，但加上储能后的系统成本是否在2041年低于每千瓦时3美分仍未到期。  
  来源：<https://www.iea.org/reports/global-energy-review-2026/electricity-supply>；<https://en.wikipedia.org/wiki/Renewable_energy>

### 部分符合（34 条）

- **#2** 「AI is an omni-use technology that will penetrate virtually all industries.」  
  判断：**部分符合**。欧盟联合研究中心显示，战略部门企业使用AI的比例从2021年的7%升至2025年的18%，几乎每个战略部门都在增长，但渗透率仍远未达到“几乎所有行业的全面渗透”。主方向出现，但程度明显不足。  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/ai-adoption-more-doubles-almost-every-eu-strategic-sector-2026-10-14_en>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>；<https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf>
- **#3** 「By the time you read this new book in late 2021 or beyond, the predictions I made in AI Superpowers will have …」  
  判断：**部分符合**。作者前作关于互联网与金融应用、感知和自主系统的判断，在2021年末至2026年间部分落地（大模型与自动驾驶试点），但并非“大体都已成为现实”。只能记部分符合。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#6** 「AI will also create efficient services that will give us back our most valuable resource—time.」  
  判断：**部分符合**。企业普遍部署对话和辅助工具，部分研究显示开发效率提升，但也有调查称使用AI的员工工作时间更长、省时证据矛盾。节省时间只在部分场景成立。  
  来源：<https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf>；<https://www.cio.com/article/4243615/does-ai-actually-save-employees-time-data-is-contradictory.html>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#9** 「Each human’s productivity will be amplified, allowing us to realize our potential.」  
  判断：**部分符合**。随机对照和行业研究显示生成式AI可提高部分高技能工作的产出，但也有文献指出整体生产率效果不稳定。生产力被放大只在部分职业和指标上成立。  
  来源：<https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf>；<https://www.cio.com/article/4243615/does-ai-actually-save-employees-time-data-is-contradictory.html>；<https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf>
- **#13** 「These AI-based fintech companies are poised to overtake brickand-mortar financial corporations because they de…」  
  判断：**部分符合**。金融科技在部分可测的人工智能应用上快于传统银行，但信贷和保险等核心市场仍由银行主导，谈不上已经或清楚走向“超越传统实体金融机构”。  
  来源：<https://www.mckinsey.com/industries/financial-services/our-insights/banking-matters/banking-trends-snapshot-how-banks-can-catch-up-to-fintechs-on-ai>；<https://en.wikipedia.org/wiki/Financial_technology>
- **#17** 「By 2041, anti-deepfake software will be similar to anti-virus software.」  
  判断：**部分符合**。C2PA等内容凭证和检测工具已经出现，但报道指出像Sora这样的系统仍使检测严重失效，远未达到“像杀毒软件一样广泛有效”。  
  来源：<https://www.theverge.com/report/806359/openai-sora-deepfake-detection-c2pa-content-credentials>；<https://en.wikipedia.org/wiki/Deepfake>
- **#21** 「I also anticipate that in the next twenty years, the use of smart biometrics for criminal investigations and f…」  
  判断：**部分符合**。执法部门已使用面部等生物识别辅助破案，但把犯罪率下降主要归因于智能生物识别缺少可靠证据，只部分符合。  
  来源：<https://en.wikipedia.org/wiki/Deepfake>；<https://en.wikipedia.org/wiki/Artificial_intelligence_controversies>
- **#25** 「how AI will become a great complement to human teachers and significantly enhance the future of education.」  
  判断：**部分符合**。人工智能辅导已进入部分课堂，作为教师补充的方向存在；但系统评价显示学习效果不稳定，不能确认已经或正在“显著提升未来教育”。  
  来源：<https://scale.stanford.edu/ai/evidence-base-review/evidence-base-ai-k12-november-review>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#28** 「This progress will only grow exponentially.」  
  判断：**部分符合**。模型规模和能力在2021–2024年继续快速上升，但2026年研究报告已强调规模定律的限度和收益递减，不能再写成无约束的指数增长。  
  来源：<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>；<https://arxiv.org/abs/2511.12869>
- **#32** 「With ever-more data, AI will make learning much more effective, engaging, and fun.」  
  判断：**部分符合**。斯坦福2026年K-12综述显示，AI在用于理解材料时可能有帮助，用于代写作业则效果不稳，不能概括为已经使学习“更加有效、有趣”。  
  来源：<https://scale.stanford.edu/ai/evidence-base-review/evidence-base-ai-k12-november-review>
- **#33** 「I believe this symbiotic and flexible new education model can dramatically improve accessibility of education,…」  
  判断：**部分符合**。低成本辅导工具扩大了部分学习者的获取途径，但优质教育可及性并未被大幅拉平，幅度与“大幅提高并帮助每个学生发挥潜力”不符。  
  来源：<https://scale.stanford.edu/ai/evidence-base-review/evidence-base-ai-k12-november-review>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#38** 「I believe that AI will significantly accelerate drug discovery and reduce its cost, making available」  
  判断：**部分符合**。已有AI发现的候选药物进入临床，成本在发现阶段被宣传为下降，但科学评论指出真实临床影响证据仍然很薄，尚未普遍“更多有效药物更低价格”。  
  来源：<https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really>；<https://en.wikipedia.org/wiki/AlphaFold>
- **#39** 「I anticipate diagnostic AI will exceed all but the best doctors in the next twenty years.」  
  判断：**部分符合**。在部分放射和病理任务上算法已可匹敌专科医生，但面向全科、超越除最顶尖医生以外所有医生的方向尚未被清楚确立。  
  来源：<https://med.stanford.edu/radiology/news/2026-news/award-winning-study-puts-ai-s-impact-on-radiology-into-perspecti.html>；<https://en.wikipedia.org/wiki/AlphaFold>
- **#40** 「we see that by 2041 radiologists’ jobs will be mostly taken over by AI.」  
  判断：**部分符合**。研究认为AI可减少约三分之一放射工作负荷，但放射科医生需求仍在增长，与“到2041年工作大多被接管”的岗位含义并不一致。  
  来源：<https://med.stanford.edu/radiology/news/2026-news/award-winning-study-puts-ai-s-impact-on-radiology-into-perspecti.html>
- **#46** 「By 2041, end-to-end delivery should be pervasive, with autonomous forklifts moving items in the warehouse, dro…」  
  判断：**部分符合**。自动配送和部分无人机试点已经出现，但端到端配送远未普及，现有试点不足以清楚确认到2041年将会普及。  
  来源：<https://en.wikipedia.org/wiki/Robotaxi>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#48** 「In the next twenty years, XR will revolutionize entertainment, training, retail, healthcare, sports, and trave…」  
  判断：**部分符合**。消费级头显首先改变了游戏和部分娱乐，对培训、零售、医疗、体育和旅游的“彻底改变”在窗口内并未出现，只是局部改变。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#51** 「These developments suggest that a mass-produced set of XR glasses should be on the market by 2025, perhaps wit…」  
  判断：**部分符合**。苹果于2024年上市Vision Pro，时间早于2025，但产品是头戴式头显而非轻量眼镜，也未形成大众级“眼镜”品类，形态与普及度只部分符合。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#58** 「The bottom line is that by 2041, much of our work and play will involve the use of virtual technologies.」  
  判断：**部分符合**。娱乐和部分远程协作已使用虚拟或混合现实，但“许多工作和娱乐都将涉及虚拟技术”在2026年尚未成为普遍事实，也未被就业或时间分配数据坐实。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#59** 「There will be giant XR breakthroughs, probably starting in entertainment.」  
  判断：**部分符合**。消费级VR的突破确实主要从游戏和娱乐开始，但把既有头显迭代称为“重大突破”并已改写各行业，依据不足，故只记部分符合。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#63** 「but robo-buses should become a reality within three years.」  
  判断：**部分符合**。中国等地在2022–2024年已有自动驾驶巴士或固定线路试点，但到约2024年并未成为广泛商业现实，只部分兑现“三年内成为现实”。  
  来源：<https://en.wikipedia.org/wiki/Robotaxi>；<https://en.wikipedia.org/wiki/Apolong>
- **#64** 「As shared-ride cars become autonomously driven, shared-ride services will be able to reduce costs dramatically…」  
  判断：**部分符合**。无人出租已在部分城市运营，票价有时低于有人驾驶网约车，但并没有稳定出现作者所说因去掉75%司机分成而“大幅”降本的普遍结果。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Robotaxi>
- **#70** 「Gas stations, car dealerships, and parking garages will be dramatically reduced, as will their employees.」  
  判断：**部分符合**。电动化已使部分加油站需求承压，但经销商和停车场的显著萎缩主要还不是自动驾驶造成的，只在部分对象上出现方向。  
  来源：<https://en.wikipedia.org/wiki/Self-driving_car>；<https://en.wikipedia.org/wiki/Renewable_energy>
- **#79** 「The deployment of autonomous weapons will be accelerated by an inevitable arms race that will lack the natural…」  
  判断：**部分符合**。大国竞争在加快自主武器讨论，但全面部署尚未发生，也缺少“缺乏核威慑式相互确保摧毁的军备竞赛正在加速部署”的直接度量。  
  来源：<https://www.theguardian.com/world/2026/nov/06/autonomous-weapons-ai-russia-us-binding-rules>；<https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/>
- **#81** 「This simple fact is poised to generate tremendous economic value but also to cause unprecedented job displacem…」  
  判断：**部分符合**。人工智能带来了巨大投资和可观的潜在经济价值，但高盛等评估认为近期就业冲击有限，并不支持已经出现“空前规模”的普遍失业。  
  来源：<https://www.goldmansachs.com/insights/articles/is-ai-impacting-global-labor-markets>；<https://www.goldmansachs.com/insights/articles/how-will-ai-affect-the-global-workforce>；<https://www.pwc.com/gx/en/news-room/press-releases/2025/ai-adoption-could-boost-global-gdp-by-an-additional-15-percentage.html>；<https://www.cnbc.com/2026/11/09/october-jobs-report-hiring-by-sector.html>
- **#82** 「by 2041, warehouse pickers—who perform routine tasks—will have long been displaced; many construction workers …」  
  判断：**部分符合**。领先物流企业的仓库拣货自动化在加深，但建筑工人被大规模替代尚未出现，2041年的两项替代只有前一项方向较清楚。  
  来源：<https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/>；<https://www.cnbc.com/2025/10/22/amazon-switch-to-robots-will-save-it-up-to-4-billion-a-year-morgan-stanley-says.html>
- **#84** 「which will make RPA and other technologies even easier to apply, thereby accelerating job displacements.」  
  判断：**部分符合**。疫情确使工作流数字化，从而更便于部署RPA，但随后几年的宏观失业并没有因此而显著加速，只部分符合。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://www.goldmansachs.com/insights/articles/is-ai-impacting-global-labor-markets>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#88** 「Jobs that are asocial and routine, such as telemarketers or insurance adjusters, are likely to be taken over i…」  
  判断：**部分符合**。电话推销、理算和数据录入已大量自动化，但这些岗位并未在整体上被完全接管，程度未到原预测的终局。  
  来源：<https://www.goldmansachs.com/insights/articles/is-ai-impacting-global-labor-markets>；<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#95** 「With so many features, AI will be able to detect human emotions (happy, sad, disgusted, surprised, angered, or…」  
  判断：**部分符合**。商业情感计算被广泛推销，部分实验室任务可识别基本表情，但权威心理科学评论认为读取内在情绪缺乏可靠科学基础。  
  来源：<https://www.psychologicalscience.org/news/experts-say-emotion-recognition-lacks-scientific-foundation.html>
- **#97** 「But by that time, AI’s ability to read human emotions should be quite advanced, well beyond human capabilities…」  
  判断：**部分符合**。情绪识别和数字心理健康应用可视为早期原型，但并未达到“远超人类、相当先进”的读取能力。  
  来源：<https://www.psychologicalscience.org/news/experts-say-emotion-recognition-lacks-scientific-foundation.html>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#98** 「However, the current implementation described above is unlikely to achieve these goals and may even be counter…」  
  判断：**部分符合**。GDPR提高了透明和罚款约束，但也常被批评为同意弹窗形式化、并与AI训练需求冲突，与“难以实现目标甚至可能适得其反”部分相符，并非全面失效。  
  来源：<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>；<https://www.edps.europa.eu/system/files/2025-06/techdispatch_federated-learning_en.pdf>
- **#100** 「privacy computing will likely not be totally pervasive by 2041, but these technologies will be mature enough t…」  
  判断：**部分符合**。联邦学习等隐私计算已有部分生产应用，与“可用于特定场景”部分相符；但“到2041年很可能不会完全普及”仍属尚未到期、也未被证伪的判断。  
  来源：<https://www.edps.europa.eu/system/files/2025-06/techdispatch_federated-learning_en.pdf>
- **#101** 「AI and other technologies will drive down the cost of almost all goods, most of which will be produced for」  
  判断：**部分符合**。数字内容的边际成本已接近为零，但食品、住房和多数实物商品并未被压到“几乎免费”，只在部分门类符合。  
  来源：<https://www.theguardian.com/news/ng-interactive/2026/nov/05/lab-grown-meat-save-the-world-food-revolution-climate-crisis-food-system>；<https://en.wikipedia.org/wiki/Renewable_energy>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#105** 「Switching to this form of energy can eliminate more than 50 percent of all greenhouse gas emissions, which is …」  
  判断：**部分符合**。电力和能源相关排放是温室气体的最大来源之一，转向清洁电力可大幅减排，但“消除全部温室气体的50%以上”还取决于交通、工业和农业，幅度只部分成立。  
  来源：<https://www.iea.org/reports/global-energy-review-2026/electricity-supply>；<https://en.wikipedia.org/wiki/Renewable_energy>
- **#106** 「Synthetic biology will revolutionize the food industry.」  
  判断：**部分符合**。培养肉已在个别司法管辖区获得批准，但2026年的报道指出商业化大规模未实现、产业受挫，谈不上已经“彻底改变食品产业”。  
  来源：<https://en.wikipedia.org/wiki/Cultured_meat>；<https://www.theguardian.com/news/ng-interactive/2026/nov/05/lab-grown-meat-save-the-world-food-revolution-climate-crisis-food-system>

### 暂无法判断（42 条）

- **#4** 「And like most technologies, AI will eventually produce more positive than negative impacts on our society.」  
  判断：**暂无法判断**。“最终净影响为正”的终点是eventually，截至2026-11-15既无法用单一指标证明净正面，也无法证伪。缺少可判定的决性事实。  
  来源：—
- **#5** 「Firstly, AI will create tremendous value to our society—PricewaterhouseCoopers estimates $15.7 trillion by 203…」  
  判断：**暂无法判断**。所谓“巨大价值”的依据是另一份仍在更新的咨询估计，不是窗口内已经实现的15.7万亿美元结果；2030年终点未到，也没有可绑定的实现路径数据。  
  来源：<https://www.pwc.com/gx/en/news-room/press-releases/2025/ai-adoption-could-boost-global-gdp-by-an-additional-15-percentage.html>；<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025>
- **#10** 「These stories offer a portrait of our world in 2041, based on technologies with a greater than 80-percent like…」  
  判断：**暂无法判断**。该书十条故事涉及数十项技术，其在2041年“总体超过80%可能实现”无法在2026年用统一口径核验，缺少决性的逐项盘点。  
  来源：—
- **#18** 「This process will eliminate deepfakes. However, this “upgrade” will not arrive by 2041, as it requires all dev…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://www.theverge.com/report/806359/openai-sora-deepfake-detection-c2pa-content-credentials>；<https://en.wikipedia.org/wiki/Deepfake>
- **#19** 「its positive applications will surely outnumber its negative applications, just as with most new breakthrough …」  
  判断：**暂无法判断**。GAN及生成模型的“正面应用是否必定多于负面”缺乏可统一计量的清单，窗口内无法判定。  
  来源：—
- **#22** 「AI security will be largely achieved with only occasional perpetration (just like we still occasionally get at…」  
  判断：**暂无法判断**。“人工智能安全将大体实现、仅偶发侵害”没有明确时点；2026年攻击面仍在扩大，既不能说已经大体实现，也不能就此判错。  
  来源：—
- **#29** 「So, will deep learning eventually become “artificial general intelligence” (AGI), matching human intelligence …」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#30** 「I believe we are unlikely to see a dozen in twenty years.」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>；<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>
- **#35** 「When we look back in 2041, we will likely see healthcare as the industry most transformed by AI.」  
  判断：**暂无法判断**。“2041年回看时医疗是否是被AI改造最深的行业”取决于尚未结束的比较，2026年更显著的改造发生在软件与互联网，无法提前判定。  
  来源：—
- **#42** 「COVID-19 will likely accelerate this growth rate.」  
  判断：**暂无法判断**。原判定已承认缺乏与该书市场增速预测相对应的统一数据，疫情加速医疗人工智能市场的具体增长率不能从现有归档材料确认。  
  来源：<https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really>；<https://en.wikipedia.org/wiki/AlphaFold>
- **#43** 「I anticipate that AI will contribute to longevity—not just helping us to live longer but also to do so with a …」  
  判断：**暂无法判断**。“人工智能将贡献于延长寿命并保持生活质量”缺少到2026年可归因的人群预期寿命证据。  
  来源：—
- **#44** 「General human-level sight, touch, manipulation, movement, and coordination are too difficult to perfect in twe…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#52** 「I believe XR contact lenses may be the first XR technology to achieve the milestone of mass acceptance.」  
  判断：**暂无法判断**。“隐形眼镜可能是第一种大规模普及的XR”是或然判断，2026年尚未出现大众级XR隐形眼镜，也无法排除未来，暂无法判定。  
  来源：—
- **#53** 「By 2041, we anticipate the “invisibility” of contact lenses will truly cause the market to accept the」  
  判断：**暂无法判断**。2041年市场是否接受XR隐形眼镜取决于尚未发生的成本、隐私和监管结果，2026年没有决性事实。  
  来源：—
- **#54** 「By 2030, good ear sets should be almost invisible, through boneconducting, omni-binaural immersive sound and o…」  
  判断：**暂无法判断**。已归档材料没有“几乎隐形”耳戴设备的可绑定规格或份额，不能把一般性的小型化讨论写成通往2030年该终点的清楚方向。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#56** 「it is unlikely that naked-eye holography will become anywhere as good as XR assisted by glasses or contact len…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Apple_Vision_Pro>
- **#57** 「Neuralink engineered an interesting prototype, but by 2041 it will not likely achieve Musk’s human-amplificati…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Neuralink>
- **#60** 「That’s why in “The Holy Driver” we predict that AV tech will not reach maturity until 2041, thirtytwo years af…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#61** 「The transmission of high-fidelity video with minimal latency will take a lot of bandwidth, but 6G is set to pr…」  
  判断：**暂无法判断**。证据只是频谱路线图仍把6G放在2030年前后，这是“尚未被证伪”的时间表，不是窗口内已经确认的带宽实现方向。  
  来源：<https://radio-spectrum-policy-group.ec.europa.eu/document/download/469641a9-dec2-4c74-8415-b1ec44258a82_en?filename=RSPG26-013final-RSPG_Opinion-6G_Spectrum_Roadmap.pdf>
- **#62** 「With iterations of improvements, we predict that L5 can be broadly and safely deployable around 2040 (assuming…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>；<https://en.wikipedia.org/wiki/Robotaxi>
- **#65** 「This cost reduction will lead to dramatically cheaper rides and encourage people to forgo owning their own car…」  
  判断：**暂无法判断**。因自动驾驶而大规模放弃私家车的现象在2026年尚无清晰统计，无法判定。  
  来源：—
- **#68** 「Human driving may follow in the footsteps of driving under the influence. It will eventually be outlawed on pu…」  
  判断：**暂无法判断**。“人类驾驶最终在公路上被禁止”属于长期eventually情景，2026年没有任何司法管辖区走向全面禁驶。  
  来源：—
- **#71** 「In the long term, I believe that, just as Chamal discovered in “The Holy Driver,” L5 AV will be hugely benefic…」  
  判断：**暂无法判断**。L5对人类“在许多方面巨大有益”是长期总评，广泛L5尚未到来，无法在2026年判定净效益。  
  来源：—
- **#72** 「First, I’ll describe quantum computing, which I believe has an 80-percent chance of working by 2041.」  
  判断：**暂无法判断**。量子硬件在进步，但“到2041年有80%机会能够运行”是未到期的概率判断，不能把硬件迭代直接写成该概率预测已经得到趋势确认。  
  来源：<https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027>；<https://www.ibm.com/roadmaps/quantum/>；<https://en.wikipedia.org/wiki/Quantum_computing>
- **#73** 「I believe there is an 80-percent chance that by 2041 there will be a functional 4,000 logical qubit (and over …」  
  判断：**暂无法判断**。公开路线图仍远未达到4000个逻辑比特，也没有破解现行比特币加密的实例；2041年终点未到，2026年不能把80%概率判对或判错。  
  来源：—
- **#74** 「Perhaps only after the inevitable quantum bitcoin heist happens will people wake up to revamp the algorithms.」  
  判断：**暂无法判断**。量子比特币盗窃并未发生，抗量子算法也只是在准备中，无法验证“只有失窃后才会升级”这一机制。  
  来源：—
- **#77** 「This multilateral arms race, if allowed to run its course, will eventually become a race toward oblivion.」  
  判断：**暂无法判断**。“若听任军备竞赛发展则最终走向毁灭”是未触发的长期条件句，无法在2026年判定。  
  来源：—
- **#83** 「In AI Superpowers I estimated that about 40 percent of our jobs could be accomplished mostly by AI and automat…」  
  判断：**暂无法判断**。“到2033年约40%的工作可主要由AI和自动化完成”的终点尚未到来，2026年的就业数据既不能证实也不能否定该比例。  
  来源：—
- **#85** 「While AI displacement is gradual, eventually it will also be total.」  
  判断：**暂无法判断**。“替代最终将是彻底的”属于长期eventually判断，窗口内无法判定。  
  来源：—
- **#86** 「Left unchecked, AI in the twenty-first century may bring about a new caste system, with a plutocratic AI elite…」  
  判断：**暂无法判断**。“若放任不管则出现新种姓制度”是有条件的世纪尺度情景，缺少已实现的决性社会分层证据。  
  来源：—
- **#87** 「These are the three capabilities where I see AI falling short, and that AI will likely still struggle to maste…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#89** 「we can expect an AIled renaissance that will enable and celebrate creativity, compassion, and humanity.」  
  判断：**暂无法判断**。“人工智能引领的文艺复兴”是文化总评，2026年虽有AI艺术和创作工具，还不能据此判定一场新的文艺复兴已经或将会到来。  
  来源：—
- **#90** 「The AI job-displacement tidal wave will eventually take away virtually all routine jobs, which tend to be entr…」  
  判断：**暂无法判断**。“最终夺走几乎所有常规工作”的终点未到，且目前就业数据并未显示常规岗位整体消失。  
  来源：—
- **#91** 「The ambiguous outcome in this story suggests that AI’s efforts to improve our happiness will still be a work i…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://www.psychologicalscience.org/news/experts-say-emotion-recognition-lacks-scientific-foundation.html>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#92** 「Defining happiness will be even more complex by 2041, when society will have progressed, through AI technology…」  
  判断：**暂无法判断**。“到2041年因生活普遍舒适而更难定义幸福”依赖于尚未出现的普遍丰裕，2026年无法判定。  
  来源：—
- **#93** 「If society is governed by good leaders, government will take care of all the people, assuring them material su…」  
  判断：**暂无法判断**。该判断以“良治”为条件，且“保障所有人物质充足”并未作为可观察的普遍结果出现。  
  来源：—
- **#94** 「By 2041, in wealthier societies, people will find that their definition of happiness is evolving, as people ad…」  
  判断：**暂无法判断**。富裕社会幸福定义是否在2041年从享乐转向实现意义，缺少可操作的测量和决性事实。  
  来源：—
- **#96** 「By 2041, we will not gain a full understanding of what determines our state of mind, nor will we know how long…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://www.psychologicalscience.org/news/experts-say-emotion-recognition-lacks-scientific-foundation.html>
- **#99** 「I also predict that in the next twenty years, small countries governed by strong leaders with the support of t…」  
  判断：**暂无法判断**。“未来二十年技术采纳突破最可能来自有强势领导的小国”缺少可检验的对照样本和已完成的窗口，无法判定。  
  来源：—
- **#107** 「I expect that plenitude would start with these necessities and gradually expand to provide a comfortable」  
  判断：**暂无法判断**。“丰裕从必需品开始逐步扩展到所有人的舒适生活”在2026年没有对应的制度或分配事实可以核验。  
  来源：—
- **#108** 「Which singularity vision—cyborgs or machine overlords—might arrive by 2041? I’d say neither.」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#109** 「We will need at least a dozen more breakthroughs to reach superintelligence, which is unlikely to happen in ju…」  
  判断：**暂无法判断**。本书2021年出版，到截止日只有约五年窗口。归档证据仅表明该否定或远期判断“尚未被证伪”，并不能清楚确认正在走向原预测的终局；按规则10记暂无法判断，不因尚未发生就记趋势符合。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/lee-ai-2041-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/lee-ai-2041-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/lee-ai-2041-v5/audit/manual_review_2026-11-15.py`

- 2026-11-16 QA 按 WORKER_BRIEF 第10条复核全部趋势符合。对指向2041/二十年终点的否定性或“尚未发生”判断，短窗口内仅“尚未被证伪”的改为暂无法判断；只有归档证据已清楚显示方向的才保留趋势符合。改判见 notes/ai2041_qa_changes.json。

