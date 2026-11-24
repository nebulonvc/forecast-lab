# 尼克·博斯特罗姆《超级智能》（Superintelligence: Paths, Dangers, Strategies，2014）：出版后预测人工核查

- 案例目录：`cases/bostrom-superintelligence-v5/`
- 出版日期：**2014年7月**（牛津大学出版社第一版第一次印刷，英国发行日期 2014-07-03）。正文为 reading-library/2026-11-15-未来判断书单/03-科技和AI/15-超级智能.pdf（书内题名为 Superintelligence: Paths, Dangers, Strategies，版权页载明 © Nick Bostrom 2014、First Edition published in 2014、Impression: 1），sha256 `654b8bed510be5def0117192a56c99c53d0cb9a3b49a92f82f97834c366b7364`，已与 catalog.json / SHA256SUMS 核对。TXT 由 `pdftotext -enc UTF-8`（不加 `-layout`）生成，sha256 `24d36f2b5e065f8ee57ba20a189607d195ff2b5cd456f65571f6b1a5a85298a2`。观察窗口为 2014-07→2026-11-15。书中写明的终点（本世纪、本世纪中叶、未来十五年、十年到二十年、二十二世纪之前、本世纪下半叶、本世纪晚些时候）按各自时点判断；以“人类水平机器智能 / 起飞 / 超级智能已经出现”为前提的判断，前提未出现则记暂无法判断。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的全文通读重做版（替代此前关键词筛选、证据为空的 30 条旧稿，对应仍打开的 PR #26）。抽取：用仓库 toolkit main 85e6da1 的 prepare_book v5 把全文切成 310 块（3500 字符、600 字符上下文；txt-00001…txt-000310，覆盖第 1–15 章、注释、参考文献与索引），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码 `validate_chunk_predictions` 与 `claims_from_results` 完成引文对齐、非预测筛除、归属降级、去重和导入，得到 100 条候选、95 条可核验预测（另 5 条转述第三方观点被降为 unclear）。核验：按 METHOD.md 用 Exa 检索公开来源（池密钥第 4 条，只按文件路径读取）并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl，共 65 条），由助手阅读后按规则 10 从严对待“趋势符合”，经 pipeline.py apply assess → check → report。claims.jsonl 的 context 字段已清空。manual_report.py 使用 /workspace/forecast-line-b/tools/manual_report.py（md5 682248fa9f6c63e3492a559ccac12761）。本稿未使用 DeepSeek API。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 95 条，剔除非预测 0 条，计入 **95 条预测**，其中 **44 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 21 |
| 趋势符合 | 9 |
| 部分符合 | 14 |
| 错误 | 0 |
| 暂无法判断 | 51 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **47.7%**（21/44） |
| 加权胜率 | **79.0%** |
| 错误率 | **0.0%**（0/44） |
| 未定占比（暂无法判断/预测） | 53.7%（51/95） |

## 总体评价

本书的核心论题（机器超级智能的默认结局是存在性灾难、起飞速度、人类水平机器智能本世纪或本世纪中叶的机会）在截止日前大多仍无法判定：前提（超级智能或人类水平机器智能已被创造）尚未出现，或写明的远期终点尚未到达，故 95 条预测中有 51 条记暂无法判断。可判定的 44 条集中在较短窗口：监控与行为数据积累、软件任务范围扩大、硬件与算力继续提升、实验室竞赛、脑机接口尚未作为认知增强被广泛使用、化学路径难以带来戏剧性智商跃升、意外概念突破（Transformer，2017）等 21 条为正确；全脑仿真约 2029 年难以实现、生殖系基因改造在本世纪中叶前难有显著人口影响、控制问题现有方法在数十年尺度上仍不足等 9 条为趋势符合；围棋击败世界冠军（时点早于线性外推、路径为深度学习而非每年一段）、自然语言理解接近但仍非全面人类水平、2014 年已有原型的技术后来产生重大影响但 Transformer 当时尚未出现等 14 条为部分符合。错误 0 条。严格胜率 47.7%，与旧稿 50.0% 接近；加权胜率 79.0%，略低于旧稿 82.8%，主要因为新方法覆盖面更宽，并按规则 10 对“趋势符合”更严。这首先反映作者把大胆判断收在条件句和远期窗口里，而不是超级智能的核心故事已被证实。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（21 条）

- **#14** 「More cases like these will surely accumulate in the future.」  
  判断：**正确**。2014年以来，神经编码/解码、脑启发网络和脑成像与深度学习的交叉研究持续积累，方向成立。  
  来源：<https://arxiv.org/pdf/2307.10246>；<https://www.nature.com/articles/s41583-025-00957-8>
- **#17** 「We should expect that they will have very different cognitive architectures than biological intelligences」  
  判断：**正确**。深度网络与Transformer等现行人工智能的认知架构已明显不同于生物神经系统，这一方向在截止日前已经实现。  
  来源：<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>；<https://arxiv.org/pdf/2307.10246>
- **#22** 「it seems implausible, on both neurological and evolutionary grounds, that one could by introducing some chemic…」  
  判断：**正确**。系统综述显示莫达非尼、哌甲酯等只有中等或有限的认知增强效果，并未出现向健康人脑引入某种化学物质即引发智力戏剧性提升的情形。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/32709551/>；<https://link.springer.com/article/10.1007/s40267-023-00989-z?code=25a03bc5-a472-4477-a9f2-d97055a317af&error=cookies_not_supported>
- **#24** 「is just now starting to become feasible and will greatly increase our knowledge of the genetic architectures o…」  
  判断：**正确**。教育程度与认知相关GWAS样本量从约十万级扩至更大队列，已识别大量位点，对遗传结构的认识显著增加。  
  来源：<https://www.nature.com/articles/mp201645>；<https://pubmed.ncbi.nlm.nih.gov/27225129/>
- **#33** 「it seems unlikely that such interfaces will be widely used as enhancements any time soon.」  
  判断：**正确**。脑机接口仍主要处于医学试验阶段，用于功能恢复而非被广泛当作增强手段，与“不太可能在近期被广泛用作增强”相符。  
  来源：<https://www.nature.com/articles/s44222-024-00239-5>；<https://www.technologyreview.com/2025/04/01/1114009/brain-computer-interfaces-10-breakthrough-technologies-2025/>
- **#34** 「Voluntary and involuntary surveillance will amass vast amounts of information about human behavior.」  
  判断：**正确**。智能手机、社交媒体、闭路电视、门铃摄像头和人脸识别等，在2014年后把行为数据的规模又扩大了几个数量级。  
  来源：<https://carnegieendowment.org/files/WP-Feldstein-AISurveillance_final.pdf>；<https://www.cctv-focus.com/video-surveillance/vendor-news/ip-camera-boom>
- **#43** 「The range of specific tasks that can be better performed by software will continue to expand.」  
  判断：**正确**。2014年后软件在围棋、蛋白质折叠、图像识别、翻译和语音等许多具体任务上超过人类，可更好由软件完成的任务范围明显扩大。  
  来源：<https://ourworldindata.org/brief-history-of-ai>；<https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence>
- **#45** 「But hardware is rapidly improving, and the ultimate limits of hardware performance are vastly higher than thos…」  
  判断：**正确**。硬件持续改进：前沿模型训练算力约每年增长4–5倍，GPU性价比也在提升；生物计算衬底的物理上限仍远高于当前水平。  
  来源：<https://epoch.ai/data-insights/compute-trend-post-2010>；<https://epoch.ai/publications/trends-in-gpu-price-performance>
- **#48** 「Pharmacological enhancers might deliver some cognitive gains over the coming decades.」  
  判断：**正确**。随后十多年的综述显示，莫达非尼和兴奋剂等可带来一定认知增益，虽然幅度有限，与“可能带来一些认知增益”相符。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/31433334/>；<https://ncbi.nlm.nih.gov/pmc/articles/PMC7826302/>
- **#50** 「Genetic enhancement will get easier as technology is developed for cheap and effective genetic testing and sel…」  
  判断：**正确**。廉价基因检测和多基因评分使选择变得更容易，相关技术成本下降并进入商业胚胎筛查。  
  来源：<https://academic.oup.com/humupd/article/30/5/529/7684172>；<https://www.theatlantic.com/health/archive/2025/01/polygenic-risk-score-ivf/681323/>
- **#54** 「Although one cannot bank on this rate of improvement continuing up to the development of human-level machine i…」  
  判断：**正确**。不能再指望按美元每18个月翻一番一直持续，但在物理极限之前计算技术仍有改进空间，且已被GPU、集群和更长训练所利用。  
  来源：<https://epoch.ai/publications/trends-in-gpu-price-performance>；<https://epoch.ai/data-insights/compute-trend-post-2010>
- **#59** 「It is possible that globalization and increased surveillance will reduce typical lags between competing techno…」  
  判断：**正确**。全球化与开源使部分技术差距缩短到数月量级，但领先与跟随项目之间仍存在不可压缩的滞后期，并未降到零。  
  来源：<https://www.wired.com/story/stanford-study-global-artificial-intelligence-index/>；<https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf>
- **#73** 「it would be easier to create an AI with simple goals like these than to build one that had a human-like set of…」  
  判断：**正确**。相对而言，安装简单代理目标或优化指标远比编码人类价值体系容易，对齐文献在2014–2026年间持续记录了这一不对称。  
  来源：<https://dl.acm.org/doi/full/10.1145/3770749>；<https://theconversation.com/the-decades-old-ai-alignment-problem-has-finally-become-a-reality-solving-it-wont-be-easy-289812>
- **#78** 「Benign failures are bound to occur many times between now and the eventual development of machine superintelli…」  
  判断：**正确**。在机器超级智能到来之前，已经多次出现资金中断、路线失败或未达到宣称目标的良性失败，与“必定会发生许多次”相符。  
  来源：<https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence>；<https://leap.forecastingresearch.org/reports/wave8>
- **#79** 「Richer and more complicated virtual worlds will become feasible with improvements in programming techniques an…」  
  判断：**正确**。游戏世界、虚拟现实和生成式三维场景都比2014年更丰富、更复杂，编程技术与算力的改进确实使更丰富的虚拟世界变得可行。  
  来源：<https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/>；<https://arxiv.org/html/2505.05474>
- **#84** 「Scientific progress means that more will be known.」  
  判断：**正确**。科学持续产出新知识，研究文献与可获得的实证结果在2014–2026年间明显增加。  
  来源：<https://dl.acm.org/doi/full/10.1145/3770749>；<https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence>
- **#86** 「Advances in information technology will make it easier to find, integrate, evaluate, and communicate data and …」  
  判断：**正确**。搜索、学术数据库、移动互联网和大语言模型使查找、整合、评估和交流数据与观念明显更容易。  
  来源：<https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W>；<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>
- **#89** 「With AI it is always possible that somebody will make an unexpected conceptual breakthrough.」  
  判断：**正确**。2017年Transformer论文构成一次事先难以精确预期的概念突破，说明“始终可能有人做出出乎意料的概念突破”在窗口内已经应验。  
  来源：<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>；<https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/>
- **#91** 「In the development of machine superintelligence, it seems likely that there will be at least a mild race dynam…」  
  判断：**正确**。OpenAI、Google DeepMind、Anthropic等实验室以及中美之间已形成被广泛讨论的人工智能竞赛，至少出现了轻度甚至更强的竞赛动态。  
  来源：<https://www.foreignaffairs.com/united-states/china-real-artificial-intelligence-race-innovation>；<https://www.wired.com/story/stanford-study-global-artificial-intelligence-index/>
- **#93** 「Attitudes toward human genetic engin­ eering and embryo selection vary significantly across cultures, suggesti…」  
  判断：**正确**。尽管英国等国禁止或限制多基因胚胎筛查，美国等地已有商业应用，说明即使部分国家持谨慎立场，新技术的开发与应用仍会在其他地方发生。  
  来源：<https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall>；<https://www.theatlantic.com/health/archive/2025/01/polygenic-risk-score-ivf/681323/>
- **#95** 「it is unlikely that there will be a vast number of projects that are each well enough resourced to be serious …」  
  判断：**正确**。前沿训练仍集中在少数资金充足的实验室，严肃竞争者是一小撮而非海量，与判断相符。  
  来源：<https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>

### 趋势符合（9 条）

- **#18** 「There is good reason to think that the requisite enabling technologies are attainable, though not in the near …」  
  判断：**趋势符合**。全脑仿真的前导技术仍在发展且被普遍认为可以达到，但人类全脑仿真在2014–2026年间并未到来，“近期不会实现”的方向成立，窗口尚未完全结束。  
  来源：<https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science>；<https://biologyinsights.com/mind-uploading-research-whats-the-current-progress/>
- **#20** 「the emulation path will not succeed in the near future (within the next fifteen years, say)」  
  判断：**趋势符合**。至2026年11月人类全脑仿真仍未成功，与“未来约十五年（约至2029年）内不会成功”的方向一致，但终点尚未到期。  
  来源：<https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science>；<https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/>
- **#21** 「it is conceivable—though unlikely—that somebody somewhere will get the right insight for how to do this in the…」  
  判断：**趋势符合**。在“近期”窗口内尚未出现有人在普通个人计算机上写出种子人工智能的情形，方向与“不太可能”一致，但近窗口尚未完全闭合。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#26** 「Long before then, more direct and powerful modes of genetic engineering (not to mention machine intelligence) …」  
  判断：**趋势符合**。CRISPR等更直接的基因编辑工具已出现，体细胞疗法进入临床，但安全的人类生殖系增强和相关机器智能都尚未就绪，二十二世纪之前这一终点也未到。  
  来源：<https://www.who.int/health-topics/human-genome-editing>；<https://www.cell.com/med/fulltext/S2666-6340(26)00228-X>
- **#30** 「germline enhancements are unlikely to have a significant impact on society before the middle of this century.」  
  判断：**趋势符合**。截至2026年，生殖系增强几乎没有对社会产生显著影响（仅有一例违规事件并随后被禁），与“本世纪中叶前不太可能有显著影响”的方向一致，但中叶终点未到。  
  来源：<https://en.wikipedia.org/wiki/He_Jiankui_affair>；<https://www.scmp.com/news/china/politics/article/3270285/china-bans-clinical-research-germline-genome-editing-irresponsible>
- **#39** 「Brain–computer interfaces look unlikely as a source of superintelligence.」  
  判断：**趋势符合**。脑机接口仍远离超级智能来源，方向与“看起来不太可能”一致，但超级智能本身尚未出现，不能视为终点已验证。  
  来源：<https://www.nature.com/articles/s44222-024-00239-5>；<https://leap.forecastingresearch.org/reports/wave8>
- **#81** 「There are several quite strong reasons to believe that the riskiness of an intelligence explosion will decline…」  
  判断：**趋势符合**。控制问题与对齐研究在出版后十余年明显推进，为“风险会在数十年尺度上下降”提供了方向性支持，但数十年窗口未结束，实际起飞风险也无法直接测量。  
  来源：<https://dl.acm.org/doi/full/10.1145/3770749>；<https://theconversation.com/the-decades-old-ai-alignment-problem-has-finally-become-a-reality-solving-it-wont-be-easy-289812>
- **#82** 「It is plausible that the state of the art will advance greatly over the next several decades; and if the probl…」  
  判断：**趋势符合**。对齐、强化学习人类反馈和可解释性等使控制问题的技术水平在2014年后明显前进，与“未来数十年将大幅前进”的方向一致，但数十年终点未到，问题也仍未解决。  
  来源：<https://dl.acm.org/doi/full/10.1145/3770749>；<https://www.transformernews.ai/p/no-ai-alignment-isnt-solved>
- **#90** 「We can therefore be confident that WBE is not imminent (not less than, say, fifteen or twenty years away).」  
  判断：**趋势符合**。人类全脑仿真在2026年仍未被认为迫在眉睫，与“至少还要十五到二十年（约至2029–2034年）”的方向一致，但窗口尚未完全结束。  
  来源：<https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science>；<https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/>

### 部分符合（14 条）

- **#2** 「most technologies that will have a big impact on the world in five or ten years from now are already in limite…」  
  判断：**部分符合**。智能手机、深度学习、CRISPR等2014年已在有限使用或实验室中，其后确实产生重大影响；但Transformer（2017）和ChatGPT所代表的生成式跃迁在出版时并无相应原型。  
  来源：<https://en.wikipedia.org/wiki/2010s_in_science_and_technology>；<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>
- **#3** 「technologies that will reshape the world in less than fifteen years probably exist as laboratory prototypes.」  
  判断：**部分符合**。多数在十五年窗口内产生重大影响的技术在2014年已有实验室或早期形态，但支撑后来最大变革的Transformer架构直到2017年才出现。  
  来源：<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>；<https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/>
- **#5** 「If this rate of improvement continues, they might beat the human world champion in about a decade.」  
  判断：**部分符合**。围棋程序确实击败了人类世界冠军，但时点早于线性外推的约2022年（2016–2017），路径是深度学习跃迁而非每年一段的匀速提升。  
  来源：<https://en.wikipedia.org/wiki/AlphaGo>；<https://en.wikipedia.org/wiki/AlphaGo_versus_Ke_Jie>
- **#6** 「an AI that could understand natural language as well as a human adult, they would in all likelihood also eithe…」  
  判断：**部分符合**。大语言模型在多项语言理解任务上已接近或达到人类成人水平，但通用能力、推理与主体性仍有明显缺口，并非“只差很短一步就具备全面人类水平能力”。  
  来源：<https://arxiv.org/html/2303.08774v4>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC11840437/>；<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>
- **#23** 「The range of traits that can be selected for or against will expand greatly over the next decade or two.」  
  判断：**部分符合**。可选择性状已从单基因检测扩展到多基因风险评分等商业服务，范围确实扩大；但专业学会仍认为其未准备好进入临床，谈不上“大大扩展”并被广泛采用。  
  来源：<https://academic.oup.com/humupd/article/30/5/529/7684172>；<https://www.asrm.org/news-and-events/asrm-news/press-releasesbulletins/asrm-ethics-and-practice-committees-release-new-report-concluding-polygenic-embryo-screening-is-not-ready-for-clinical-use/>
- **#25** 「Any trait with a non-negligible heritability—including cognitive capacity—could then become susceptible to sel…」  
  判断：**部分符合**。认知等具有遗传力的性状在技术上已可用多基因评分做胚胎筛选，但临床证据不足、多地不支持常规使用，远未成为稳定可及的选择手段。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11981603/>；<https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall>
- **#35** 「soon, these people might begin uploading continuous life recordings from microphones and video cameras embedde…」  
  判断：**部分符合**。出现了可拍照录音的智能眼镜（如Ray-Ban Meta）和部分连续记录设备，但社交网络用户并未普遍开始上传连续生活记录。  
  来源：<https://www.eff.org/deeplinks/2026/03/think-twice-buying-or-using-metas-ray-bans>；<https://www.reuters.com/business/media-telecom/smart-glasses-ai-pins-privacy-fears-challenge-techs-next-big-bet-2026-09-22/>
- **#36** 「Automated analysis of such data streams will enable many new applications」  
  判断：**部分符合**。人脸识别、门铃摄像头和智能眼镜的自动分析已经带来新应用，但针对连续生活记录数据流的全面自动分析远未普及。  
  来源：<https://carnegieendowment.org/files/WP-Feldstein-AISurveillance_final.pdf>；<https://www.eff.org/deeplinks/2026/03/think-twice-buying-or-using-metas-ray-bans>
- **#52** 「It is entirely possible that the quest for artificial intelligence will appear to be lost in dense jungle unti…」  
  判断：**部分符合**。2017年Transformer和此后的大规模语言模型带有“看似胶着后突然出现突破”的色彩，但并未证明人类水平人工智能的终点已近在咫尺。  
  来源：<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>；<https://leap.forecastingresearch.org/reports/wave8>
- **#66** 「If and when it becomes a common belief among prestigious scientists that there is a substantial chance that su…」  
  判断：**部分符合**。2023年后辛顿、本吉奥等著名科学家公开警告，英美等国建立了安全研究所并加强对前沿实验室的评估与报告要求，但并非古典意义上情报机构对研究人员的全面监控。  
  来源：<https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute>；<https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence?%3F%3F%3Futm_source=adzuna>
- **#67** 「If political elites were persuaded by the seriousness of the risk, civilian efforts in sensitive areas might b…」  
  判断：**部分符合**。政治精英在一定程度上接受了风险讨论，欧盟人工智能法、出口管制和行政令等已对民用前沿活动加以监管，但并未禁止或取缔民用通用人工智能研究。  
  来源：<https://www.bbc.com/future/article/20231107-why-global-regulation-of-artificial-intelligence-is-still-a-long-way-off>；<https://www.insidedeeptech.com/global-agi-regulations-2026-september-update/>
- **#68** 「a total intelligence failure cannot be ruled out. Such a failure is especially likely if breakthroughs should …」  
  判断：**部分符合**。议题在起飞发生前已进入公众视野，降低了“在声名远扬前突然突破导致完全情报失败”的特定情形；但“不能排除完全失败”本身仍无法被证伪。  
  来源：<https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute>；<https://pubmed.ncbi.nlm.nih.gov/38768279/>
- **#74** 「a meaningless reductionistic goal is easier for humans to code and easier for an AI to learn, it is just the k…」  
  判断：**部分符合**。能力优先、先让系统“能用”的激励确实存在，但前沿实验室同时也投入了对齐与安全，并未普遍把无意义的还原论目标装进种子系统。  
  来源：<https://dl.acm.org/doi/full/10.1145/3770749>；<https://openai.com/index/frontier-model-forum/>
- **#85** 「Economic growth may give a greater portion of the world’s population adequate nutrition (particularly during t…」  
  判断：**部分符合**。互联网普及和教育完成率等有所提高，但新冠疫情使中低收入国家的学习贫困显著恶化，营养与优质教育的覆盖并非单纯扩大。  
  来源：<https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W>；<https://www.worldbank.org/en/news/press-release/2022/06/23/70-of-10-year-olds-now-in-learning-poverty-unable-to-read-and-understand-a-simple-text>

### 暂无法判断（51 条）

- **#1** 「the world will be some 4.8 times richer by 2050 and about 34 times richer by 2100 than it is today.」  
  判断：**暂无法判断**。按过去五十年增速外推到2050/2100的条件尚未完结；2014年后全球增速已低于长期均值，前提是否成立也不清楚。  
  来源：<https://tradingeconomics.com/world/full-year-gdp-growth>；<https://www.worldbank.org/en/research/publication/long-term-growth-prospects>
- **#4** 「The train might not pause or even decelerate at Humanville Station. It is likely to swoosh right by.」  
  判断：**暂无法判断**。人类水平机器智能尚未出现，无法核验达到该水平后是否会迅速越过。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>；<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>
- **#7** 「the median numbers reported in the expert survey do not have enough probability mass on later arrival dates. A…」  
  判断：**暂无法判断**。这是关于2075/2100年概率质量应如何分配的判断，终点仍在未来，无法用2026年的观察判定对错。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#8** 「I assign a higher probability to superintelligence being created relatively soon after human-level machine int…」  
  判断：**暂无法判断**。超级智能是否会在人类水平机器智能之后很快到来，前提（人类水平机器智能已经出现）尚未满足。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#9** 「thinking an extremely good or an extremely bad outcome to be somewhat more likely than a more balanced outcome…」  
  判断：**暂无法判断**。关于人类水平机器智能之长期结局极端好坏更可能的判断，结局尚未展开。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#10** 「human-level machine intelligence has a fairly sizeable chance of being developed by mid-century」  
  判断：**暂无法判断**。本世纪中叶（约2050年）尚未到达，人类水平机器智能也尚未被公认实现，无法判定“相当可观的机会”是否成立。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>；<https://santageai.com/agi/agi-timelines>
- **#11** 「it might perhaps fairly soon thereafter result in superintelligence」  
  判断：**暂无法判断**。取决于人类水平机器智能先出现，该前提尚未满足。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#12** 「a wide range of outcomes may have a significant chance of occurring, including extremely good outcomes and out…」  
  判断：**暂无法判断**。关于长期结局（含灭绝）具有显著概率的判断，无法在截止日前用已实现结果核验。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#13** 「Even a century of continued Moore’s law would not be enough to close this gap.」  
  判断：**暂无法判断**。“即使再持续一个世纪的摩尔定律也不足以填平与神经系统进化算力的差距”是跨世纪的计算判断，十二年观察不足以判定。  
  来源：<https://epoch.ai/data-insights/compute-trend-post-2010>；<https://www.fhi.ox.ac.uk/wp-content/uploads/ai-evolution-and-selection-effects.pdf>
- **#15** 「continuing incremental progress in brain science should eventually discover them all.」  
  判断：**暂无法判断**。“最终发现大脑全部基本机制”的终点尚未到来；果蝇等连接组有进展，但人类大脑机制远未穷尽。  
  来源：<https://www.nature.com/articles/s41583-025-00957-8>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC13659455/>
- **#16** 「it is likely that most will be—extremely alien.」  
  判断：**暂无法判断**。这句话针对未来大多数人工智能的心智形态；当前系统既有异于人类的一面，也深度依赖人类语料，尚不能代表“大多数”。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>
- **#19** 「it seems quite likely that the first whole brain emulation that we would achieve if we went down this path wou…」  
  判断：**暂无法判断**。全脑仿真路径尚未走到第一例人类仿真，无法核验其保真度是否会偏低。  
  来源：<https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/>
- **#27** 「even after the technology has been perfected, adoption rates will probably start out low. Some countries might…」  
  判断：**暂无法判断**。迭代胚胎选择技术尚未完善，关于完善之后初期采用率和部分国家禁止的判断前提未满足。  
  来源：<https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall>
- **#28** 「might not only permit but actively promote the use of genetic selection and genetic engineering to enhance the…」  
  判断：**暂无法判断**。用于增强群体智力的成熟技术并未被认定已经可用；中国在贺建奎事件后禁止生殖系临床研究，新加坡也未见此类促进计划。  
  来源：<https://www.scmp.com/news/china/politics/article/3270285/china-bans-clinical-research-germline-genome-editing-irresponsible>；<https://en.wikipedia.org/wiki/He_Jiankui_affair>
- **#29** 「There is some chance that a large attitudinal shift could take place over a relatively short time, perhaps in …」  
  判断：**暂无法判断**。“技术被证明有效并带来显著好处”这一前提尚未成立，无法核验态度是否会在约十年内大幅转变。  
  来源：<https://www.asrm.org/news-and-events/asrm-news/press-releasesbulletins/asrm-ethics-and-practice-committees-release-new-report-concluding-polygenic-embryo-screening-is-not-ready-for-clinical-use/>
- **#31** 「the intelligence of significant segments of the adult population may begin to be boosted by genetic enhancemen…」  
  判断：**暂无法判断**。“本世纪中叶起”的窗口尚未开始。  
  来源：<https://en.wikipedia.org/wiki/He_Jiankui_affair>
- **#32** 「the probable emergence of a generation of genetically enhanced populations—voters, inventors, scientists—with …」  
  判断：**暂无法判断**。本世纪下半叶及以后的增强世代尚未出现。  
  来源：<https://en.wikipedia.org/wiki/He_Jiankui_affair>
- **#37** 「might plausibly first be attained via the AI path.」  
  判断：**暂无法判断**。超级智能尚未被创造，无法核验它是否会首先经由人工智能路径达到。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#38** 「It seems fairly likely, however, that even if progress along the whole brain emulation path is swift, artifici…」  
  判断：**暂无法判断**。全脑仿真路径并未迅速推进到终点，比较哪一条路先达到超级智能尚无法判定。  
  来源：<https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/>
- **#40** 「Improvements in networks and organizations might result in weakly superintelligent forms of collective intelli…」  
  判断：**暂无法判断**。“长期来看”的弱超级智能集体智能尚未成为可核验的既成事实。  
  来源：<https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence>
- **#41** 「Machines have a number of fundamental advantages which will give them overwhelming superiority.」  
  判断：**暂无法判断**。机器对生物心智的压倒性优势以机器超级智能为前提，该前提未出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#42** 「Biological humans, even if enhanced, will be outclassed.」  
  判断：**暂无法判断**。增强后的生物人是否会被机器智能全面超越，取决于后者已经出现，目前无法判定。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#44** 「The far greater changes in computing resources and architecture that machine intelligence will enable will pro…」  
  判断：**暂无法判断**。机器智能将带来比人猿脑差异更深远的后果，取决于相关机器智能已经出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#46** 「Given that machines will eventually vastly exceed biology in general intelligence,」  
  判断：**暂无法判断**。“最终将在通用智能上大幅超越生物学”的终点尚未到来。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#47** 「this chapter will present some reasons for thinking that the slow transition scenario is improbable. If and wh…」  
  判断：**暂无法判断**。智能起飞尚未发生，无法核验它是否会是爆炸性的。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#49** 「subsequent gains will be increasingly hard to come by.」  
  判断：**暂无法判断**。难以确认“最容易的改进”是否已经完成，以及此后增益是否确实越来越难获得。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/32709551/>
- **#51** 「collective intelligence, with a recalcitrance that seems at the moment to be in the moderate range—progress is…」  
  判断：**暂无法判断**。互联网集体智能的改进难度是否因低垂果实耗尽而上升，并没有单一可核验的指标；随后又出现了大语言模型等新工具。  
  来源：<https://en.wikipedia.org/wiki/Transformer_(deep_learning)>
- **#53** 「It will almost certainly prove harder and take longer to build a machine intelligence that has a general level…」  
  判断：**暂无法判断**。尚无公认的、达到“乡村白痴”级通用机器智能的系统，因此无法核验从这一水平再提升到远超人类是否会更容易、更快。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#55** 「In summary, we can talk about the likelihood of a hardware overhang: when human-level software is created, eno…」  
  判断：**暂无法判断**。人类水平软件尚未被创造，硬件过剩是否会出现无法核验。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#56** 「likely that the applied optimization power will increase during the transition: initially because humans try h…」  
  判断：**暂无法判断**。判断针对起飞过渡期，该阶段尚未开始。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#57** 「This would create a real possibility of a fast or medium takeoff even if recalcitrance were constant or slight…」  
  判断：**暂无法判断**。关于起飞速度的可能性判断，起飞尚未发生。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#58** 「For these reasons, although a fast or medium takeoff looks more likely, the possibility of a slow takeoff cann…」  
  判断：**暂无法判断**。快速或中速起飞看起来更可能、慢速不能排除，属于对尚未发生之起飞的事先判断。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#60** 「it is highly unlikely that two projects would be close enough to undergo a fast takeoff concurrently; for a me…」  
  判断：**暂无法判断**。关于不同起飞速度下有多少项目会并行进入起飞的判断，起飞尚未发生。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#61** 「a scenario of this kind is a serious possibility, and it increases the chances that the leading project will a…」  
  判断：**暂无法判断**。以起飞发生并出现交叉点后的爆炸性增长为前提，前提未出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#62** 「A lone hacker scen­ ario cannot be excluded either.」  
  判断：**暂无法判断**。“不能排除孤独黑客场景”是可能性判断，无法用已实现结果判定对错。  
  来源：<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#63** 「it is possible that the last critical breakthrough idea might come from a single individual or a small group t…」  
  判断：**暂无法判断**。最后关键突破是否会来自个人或小团体，取决于该突破已经发生。  
  来源：<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#64** 「The likelihood of the final breakthrough being made by a small project increases if most previous progress in …」  
  判断：**暂无法判断**。开放文献与开源软件是否提高小项目做出最后突破的可能性，在最后突破尚未出现时无法核验。  
  来源：<https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025>；<https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era>
- **#65** 「governments would likely seek to nationalize any project on their territory that they thought close to achievi…」  
  判断：**暂无法判断**。尚未有被当局认定“接近起飞”的具体项目被国有化，触发条件并不清楚是否已经满足。  
  来源：<https://www.thecairoreview.com/essays/will-washington-and-beijing-nationalize-ai-labs/>；<https://www.insidedeeptech.com/global-agi-regulations-2026-september-update/>
- **#69** 「A project that controls the first superintelligence in the world would probably have a decisive strategic adva…」  
  判断：**暂无法判断**。世界上第一个超级智能尚未出现，其控制者是否会获得决定性战略优势无法核验。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#70** 「a superintelligence—at least in the absence of intellectual peers and in the absence of effective safety measu…」  
  判断：**暂无法判断**。以无智力同侪且事先缺乏有效安全措施的超级智能为前提，前提未出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#71** 「With a fast or medium takeoff, it is likely that one project will get a decisive strategic advantage.」  
  判断：**暂无法判断**。以快速或中速起飞为前提，起飞尚未发生。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#72** 「a superintelligence with a decisive strategic advantage would have immense powers, enough that it could form a…」  
  判断：**暂无法判断**。拥有决定性战略优势的超级智能尚未出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#75** 「a plausible default outcome of the creation of machine superintelligence is existential catastrophe.」  
  判断：**暂无法判断**。机器超级智能尚未被创造，其“说得通的默认结果是存在性灾难”无法用已实现结果判定。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#76** 「This suggests that—absent a special effort—the first superintelligence may have some such random or reductioni…」  
  判断：**暂无法判断**。第一个超级智能尚未出现，是否会在缺乏专门努力时带有任意或还原论的最终目标，尚无法核验。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#77** 「the outcome could easily be one in which humanity quickly becomes extinct.」  
  判断：**暂无法判断**。未对齐的第一个超级智能是否会轻易导致人类灭绝，取决于该系统已经出现。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>
- **#80** 「Yet there are reasons, if we take a longer view and assume a state of unchanging technology and continued pros…」  
  判断：**暂无法判断**。前提要求“技术不变且持续繁荣”；2014年后技术并未冻结，全球生育率也未见回到栖息地极限的趋势。  
  来源：<https://www.worldbank.org/en/research/publication/long-term-growth-prospects>
- **#83** 「an optimist could expect that the “sanity level” of humanity will rise over the course of this century—that pr…」  
  判断：**暂无法判断**。这是对乐观主义者可以期待的本世纪趋势的表述，世纪尚未结束，偏见、洞见与抽象风险思维的净变化也缺乏单一可判定的指标。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/38768279/>
- **#87** 「by the century’s end, humanity will have made an additional hundred years’ worth of mistakes, from which somet…」  
  判断：**暂无法判断**。终点是本世纪末，目前无法判定是否会从额外一百年的错误中学到东西。  
  来源：—
- **#88** 「it is possible that progress toward whole brain emulation will not yield whole brain emulation. It may instead…」  
  判断：**暂无法判断**。全脑仿真路径尚未走到岔口，是否会先得到神经形态人工智能只是一种可能性，无法判定。  
  来源：<https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/>
- **#92** 「The required level of security might be nearly unattainable at present, but advances in lie detection and surv…」  
  判断：**暂无法判断**。“本世纪晚些时候”尚未到来；测谎技术仍不可靠，尚不足以支撑高度隔离的国际协作安全水平。  
  来源：<https://doi.org/10.3390/forensicsci6040094>；<https://www.pnas.org/doi/10.1073/pnas.2412881121>
- **#94** 「It is of course also possible that there will be no takeoff at all. But since, as argued earlier, superintelli…」  
  判断：**暂无法判断**。尚未发生起飞并不等于最终不会有起飞，因此无法用当前状态核验“可能完全没有起飞、若无则很可能是因为存在性灾难等挫败因素”。  
  来源：<https://leap.forecastingresearch.org/reports/wave8>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/bostrom-superintelligence-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/bostrom-superintelligence-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/bostrom-superintelligence-v5/audit/manual_review_2026-11-15.py`

## 说明

- 旧关键词稿（PR #26）抽出 30 条候选、26 条预测（可判定 16 条：正确 8、趋势符合 5、部分符合 3、错误 0、暂无法判断 10；严格胜率 50.0%，加权 82.8%），且 data/evidence.jsonl 为空。本稿覆盖了旧稿全部 30 条判断所对应的命题（含 4 条当时被标为非预测、现按全文规则重新归类的条目），并补入全书其余可核验预测。
- 密度为 95 条可核验预测 / 310 块 ≈ 0.31 条/块；若只计正文块，略高于 METHOD.md 英语书 0.2–0.35 条/块的参考区间。这是体裁决定的：本书是关于超级智能路径、风险与策略的预测专著，显式、对冲、条件与定量判断密集。助手通读了全部 310 块（含注释中两条正文未重复的作者预测；参考文献与索引未抽新预测），未用机制句或未触发的玩具情景凑密度。
- 5 条 resolvable=false 的候选是流水线将“转述第三方、作者未背书”的观点降为 unclear（专家调查中位数、Chalmers/Moravec 时点、全脑仿真路线图、干细胞专家、人口学家），不进入预测分母。
- 统计以 pipeline.py report 的 summary.json 与本稿 summary.json 为准；二者对 正确 / 趋势符合 / 部分符合 / 错误 / 暂无法判断 的计数一致。

