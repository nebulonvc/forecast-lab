# 迈克斯·泰格马克（Max Tegmark）《生命3.0》：出版后预测人工核查

- 案例目录：`cases/tegmark-life-3-0-v5/`
- 出版日期：**2017-08**。阿尔弗雷德·A·克诺夫出版社（Alfred A. Knopf，Borzoi）2017年第一版，ISBN 9781101946596。美国发行日期为2017年8月29日，publication_year_proxy=2017。正文为对 reading-library/2026-11-15-未来判断书单/03-科技和AI/16-生命3.0.pdf 运行 pdftotext -enc UTF-8 得到的 TXT（不使用 -layout），sha256 见 source_txt_sha256；PDF sha256 36095deb8ea2a6429c9ce7de8d64239ad129f894c6a27c00c1ba69d68a39d357，已与 catalog.json / SHA256SUMS 核对。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻仓库 DeepSeek 管线、仅以人工阅读替代模型调用：先对源文做 prepare_book v5 分块并逐块抽取，再经仓库代码对齐、去重后导入 data/claims.jsonl；核验时每条先写 scope，用 Exa 检索公开来源并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl），再由助手按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 65 条，剔除非预测 0 条，计入 **65 条预测**，其中 **36 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 12 |
| 趋势符合 | 15 |
| 部分符合 | 9 |
| 错误 | 0 |
| 暂无法判断 | 29 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **33.3%**（12/36） |
| 加权胜率 | **77.1%** |
| 错误率 | **0.0%**（0/36） |
| 未定占比（暂无法判断/预测） | 44.6%（29/65） |

## 总体评价

泰格马克2017年的判断大量指向通用人工智能及其社会后果，终点多在未来，因此暂无法判断偏多。已可判定的条目里，对算力、机器学习应用扩散和AI安全讨论升温的方向大体成立，严格胜率受终局未到的限制，加权更高；到截止日尚无足够证据将主要预测判为错误。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（12 条）

- **#14** 「Assuming that the water will keep rising for at least a while longer, AI’s impact on society will keep growing…」  
  判断：**正确**。2017年后深度学习与基础模型能力持续扩展，2022年ChatGPT触发新一轮热潮，投资、公众关注与社会影响明显增大，前提与方向均成立。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Foundation_model>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#15** 「Long before AI reaches human level across all tasks, it will give us fascinating opportunities and challenges …」  
  判断：**正确**。窗口内已出现自动驾驶安全与监管、2024年欧盟人工智能法、致命自主武器与巡飞弹讨论及部署、以及自动化冲击就业的广泛辩论，且AGI尚未实现，与判断一致。  
  来源：<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>；<https://en.wikipedia.org/wiki/Lethal_autonomous_weapon>；<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#16** 「I therefore consider it likely that brisk AI progress will continue for many years」  
  判断：**正确**。2017年至2026年出现基础模型、生成式AI与ChatGPT热潮，进展在“许多年”尺度上确实持续。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Foundation_model>
- **#18** 「long before any AGI can match us at all tasks, AI might have a dramatic impact on how we view ourselves, on wh…」  
  判断：**正确**。ChatGPT等生成式系统已改变工作与学习方式并引发广泛自我理解与职业焦虑，而AGI仍未实现，与判断一致。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#22** 「Progress in AI is likely to offer great future profit」  
  判断：**正确**。出版后算法交易继续主导外汇等市场（2019年研究显示约92%由算法执行），AI量化交易构成重要盈利途径，与判断一致。  
  来源：<https://en.wikipedia.org/wiki/Algorithmic_trading>
- **#32** 「the deployment of such systems is practically if not legally feasible within years, not decades」  
  判断：**正确**。出版后数年内，可按程序约束搜索并打击目标的无人机/巡飞弹等系统已实际存在并被广泛讨论和部署，实践可行性在“数年而非数十年”内得到印证。  
  来源：<https://en.wikipedia.org/wiki/Lethal_autonomous_weapon>；<https://en.wikipedia.org/wiki/Loitering_munition>
- **#36** 「China and Russia are likely to take note」  
  判断：**正确**。中国将AI列为国家战略并与美国并列为领先者，俄罗斯领导人公开强调AI领先者将统治世界，且文献将此置于大国竞赛语境，与“会注意到”一致。  
  来源：<https://en.wikipedia.org/wiki/Artificial_intelligence_industry_in_China>；<https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race>
- **#38** 「as long as automation continues, we should expect those who own the machines to take a growing fraction of the…」  
  判断：**正确**。自动化在零售等部门继续推进，美国非农劳动份额在2026年第二季降至1947年以来最低，方向与“资本/机器所有者份额上升”一致。  
  来源：<https://en.wikipedia.org/wiki/Labor_share>；<https://en.wikipedia.org/wiki/Labor_share>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#42** 「there are many jobs that won’t get entirely eliminated, but which will see many of their tasks automated」  
  判断：**正确**。技术性失业文献与当代例子表明岗位任务被自动化（如收银），同时职业或行业往往并未整体消失，与判断一致。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#59** 「We certainly can’t last a billion years, after which the gradually warming Sun will have cranked up Earth’s te…」  
  判断：**正确**。《地球的未来》综述指出，约10亿年后太阳光度升高约10%，地球进入湿温室并将导致海洋失控蒸发，与“撑不过十亿年、液态水被煮干”的物理判断一致。  
  来源：<https://en.wikipedia.org/wiki/Future_of_Earth>
- **#62** 「even if we could travel at the speed of light, all galaxies beyond about 17 billion light-years remain forever…」  
  判断：**正确**。宇宙学事件视界的当前距离约为50亿秒差距（160亿光年），该视界之外发出的光永远无法到达观察者，与原文“约170亿光年以外永远无法触及”属同一物理结论（数值随参数在约16–17之间更新）。  
  来源：<https://en.wikipedia.org/wiki/Cosmological_horizon>
- **#65** 「AI is likely to give us both grand opportunities and tough challenges」  
  判断：**正确**。窗口内同时出现基础模型与科学应用等重大机遇，以及安全、法律、就业与存在性风险方面的严峻挑战，与判断一致。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>；<https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence>；<https://en.wikipedia.org/wiki/Technological_unemployment>

### 趋势符合（15 条）

- **#3** 「many of the safety problems are so hard that they may take decades to solve」  
  判断：**趋势符合**。至2026年对齐与存在性风险问题仍在研究与争论中，尚未解决，方向符合“很困难、可能需数十年”；但“数十年”终点未到，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/AI_alignment>；<https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence>
- **#7** 「climate change, which might wreak havoc in fifty to two hundred years」  
  判断：**趋势符合**。出版后全球平均气温持续上升、气候系统影响扩大，方向朝向更严重后果；但原文终点为五十年至两百年，截止日尚未到达，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Climate_change>
- **#9** 「As the sea level keeps rising, it may one day reach a tipping point, triggering dramatic change」  
  判断：**趋势符合**。至2026年AI公司已越来越多把编码与研究委派给模型，出现走向自我改进的项目，但人类工作仍必要，戏剧性智能爆炸尚未发生，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>；<https://en.wikipedia.org/wiki/Foundation_model>
- **#10** 「Yes, Moore’s law will of course end, meaning that there’s a physical limit to how small transistors can be mad…」  
  判断：**趋势符合**。约2010年起半导体进步已低于两年倍增节奏，微缩逼近物理极限，摩尔本人亦称不能永远持续；但产业对“何时停止适用”尚无共识，先进制程仍在推进，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Moore%27s_law>；<https://en.wikipedia.org/wiki/Moore%27s_law>
- **#12** 「What will future historians put next on that list of enabling inventions? My guess is artificial intelligence.」  
  判断：**趋势符合**。ChatGPT等产品已使AI成为当代技术史的中心事件之一，方向支持该猜测；但“未来历史学家”的清单尚未写出，不能作终局正确，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Foundation_model>
- **#21** 「verification will itself get more difficult as software moves into robots and new environments」  
  判断：**趋势符合**。自动驾驶在有限域商业化的同时仍未在全域达到L5，对齐与不可预测行为使验证成为突出难题，方向符合；难以用单一指标证明“更困难”的程度，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Self-driving_car>；<https://en.wikipedia.org/wiki/AI_alignment>
- **#23** 「Future AI progress is likely to make the “smart grid” even smarter」  
  判断：**趋势符合**。智能电网在窗口内继续以双向通信与智能设备增强管理，方向符合；公开摘要难以证明由AI进展导致的增量，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Smart_grid>
- **#25** 「it could revolutionize personalized medicine」  
  判断：**趋势符合**。个性化/精准医疗与AI在诊断、药物和治疗规划中的应用都在扩展，方向符合；“彻底改变”尚未完成，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Personalized_medicine>；<https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare>；<https://en.wikipedia.org/wiki/AlphaFold>
- **#33** 「autonomous weapons will become the Kalashnikovs of tomorrow」  
  判断：**趋势符合**。巡飞弹与自杀无人机已在冲突中扩散，方向朝向廉价普及；但尚未达到与卡拉什尼科夫步枪相当的全球普遍装备程度，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Loitering_munition>；<https://en.wikipedia.org/wiki/Lethal_autonomous_weapon>
- **#34** 「they’ll become ubiquitous and cheap」  
  判断：**趋势符合**。军备竞赛与巡飞弹药的扩散显示廉价化与扩散方向；尚未证明所有重要军事强国都已大规模、普遍装备，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Loitering_munition>；<https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race>
- **#35** 「we may soon be spending more money on the latter—especially if a military AI arms race takes off」  
  判断：**趋势符合**。来源指出自2010年代中期已出现大国军事AI竞赛，前提可视为满足；支出上升有定性支持，但缺少民用与军用AI投资的直接对比，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race>；<https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race>
- **#39** 「aren’t likely to last long before getting automated away」  
  判断：**趋势符合**。收银等重复性岗位已部分被自助收银和无人店取代，方向成立；但此类工作并未在窗口内整体消失，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#45** 「they may increasingly replace us on the job market」  
  判断：**趋势符合**。收银自动化、部分驾驶自动化和生成式AI对任务的替代表明替代在增加，方向符合；全面取代尚未发生，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>；<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#49** 「even if we one day manage to replicate or upload brains, we’ll end up discovering one of those simpler solutio…」  
  判断：**趋势符合**。意识上传仍是假想，条件未实现；但工程化的基础模型已在无需上传的情况下取得广泛能力，与“更简单方案会先出现”的方向一致，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Mind_uploading>；<https://en.wikipedia.org/wiki/Foundation_model>；<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#50** 「Before any human-level AGI is created, we may start getting strong indications about whether this milestone is…」  
  判断：**趋势符合**。当前主导路径明显是计算机工程/基础模型而非心智上传，已提供方向性迹象；但AGI尚未出现，迹象是否“有力”到可锁定路径仍可争辩，记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Foundation_model>；<https://en.wikipedia.org/wiki/Mind_uploading>；<https://en.wikipedia.org/wiki/Recursive_self-improvement>

### 部分符合（9 条）

- **#8** 「the rise of AI will have greater overall impact」  
  判断：**部分符合**。2017–2026年AI热潮、立法与产业影响显著上升，但同期仍有大规模战争等问题，无法证明AI总体影响已经更大，结果混合。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Artificial_Intelligence_Act>
- **#19** 「Even modest progress in AI might translate into major improvements in science and technology and corresponding…」  
  判断：**部分符合**。AlphaFold等带来显著科学进展，医疗AI用于诊断与药物研发，部分方向成立；战争、贫困与不公正并未因此明显下降，结果混合。  
  来源：<https://en.wikipedia.org/wiki/AlphaFold>；<https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare>；<https://en.wikipedia.org/wiki/Climate_change>
- **#24** 「the best experts for performing such diagnosis may soon be AI systems」  
  判断：**部分符合**。AI已广泛用于疾病诊断并被用于提高准确性，但权威综述仍将其定位为协助临床医生，而非已全面成为“最佳专家”，部分成立。  
  来源：<https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare>
- **#26** 「robots have the potential to become more accurate and reliable surgeons」  
  判断：**部分符合**。机器人辅助手术已用于增强外科医生能力并克服微创限制，显示潜力；但证据是“增强人类”而非已普遍比人类更可靠，部分成立。  
  来源：<https://en.wikipedia.org/wiki/Robot-assisted_surgery>
- **#31** 「AI may help reduce famine and disease」  
  判断：**部分符合**。AI在蛋白质结构、诊断与药物研发上的进展有助于疾病应对，方向部分成立；存档未显示全球饥荒因此减少，结果混合。  
  来源：<https://en.wikipedia.org/wiki/AlphaFold>；<https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare>
- **#40** 「Drivers of trucks, buses, taxis and Uber/Lyft cars are likely to follow soon」  
  判断：**部分符合**。至2026年6月Waymo已在10个美国都市区商业运营无人出租车，方向部分实现；但截至2025年底尚无全域L5，卡车仍以带安全员测试和有限试点为主，“很快全面取代司机”未成立，结果混合。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>；<https://en.wikipedia.org/wiki/Self-driving_truck>
- **#41** 「these professions won’t get serious competition from machines」  
  判断：**部分符合**。生成式AI已能生成文本、图像与设计相关内容，对写作和设计构成不可忽视的竞争，与“不会很快有严重机器竞争”不完全吻合；但这些职业并未被取代，运动员一侧尤然，结果混合。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#44** 「If AI progress continues unabated, then both sides might be right」  
  判断：**部分符合**。2017–2026年AI进展持续，新任务/职业与技术性失业讨论并存，短期“两边都有道理”的混合图景部分成立；长期“无人可雇”尚未到来。  
  来源：<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#57** 「Cyborgs and uploads are plausible, but arguably not the fastest route」  
  判断：**部分符合**。脑机接口已存在，意识上传仍为假想；领先能力来自工程化基础模型而非上传，与“不是最快路径”一致。上传是否终将可行仍未证实，故记部分符合。  
  来源：<https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface>；<https://en.wikipedia.org/wiki/Mind_uploading>；<https://en.wikipedia.org/wiki/Foundation_model>

### 暂无法判断（29 条）

- **#1** 「Perhaps life will spread throughout our cosmos and flourish for billions or trillions of years—and perhaps thi…」  
  判断：**暂无法判断**。时间尺度为数十亿年，截止日前无法观察该结果是否发生，也尚无生命已开始星际扩散的决定性证据。  
  来源：—
- **#2** 「my guess is that if superintelligent digital life engulfs our Universe in my lifetime, it will be because of L…」  
  判断：**暂无法判断**。前提（超级智能数字生命在其有生之年吞没宇宙）尚未发生，条件未触发，不能按正误计分。  
  来源：—
- **#4** 「Even if building robots were physically impossible, a superintelligent and super-wealthy AI could easily pay o…」  
  判断：**暂无法判断**。尚无被确认的超级智能、超级富有AI处于可观察状态，能力命题无法在窗口内判定。  
  来源：—
- **#5** 「if we cede our position as smartest on our planet, it’s possible that we might also cede control.」  
  判断：**暂无法判断**。通用人工智能仍被权威综述视为假设性系统，人类整体上尚未让出“最聪明”地位，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#6** 「Artificial intelligence may enable us to launch Life 3.0 this century」  
  判断：**暂无法判断**。本世纪尚未结束，能够全面设计自身硬件与软件的生命3.0亦未出现，无法给出终局判断。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#11** 「even if we keep doubling the power of our computers every couple of years, it will take over two centuries unt…」  
  判断：**暂无法判断**。倍增节奏自约2010年起已经放缓，前提是否成立存在争议，且两个多世纪的终点远在窗口之外。  
  来源：<https://en.wikipedia.org/wiki/Moore%27s_law>
- **#13** 「we also need to consider the possibility that it will happen, perhaps even in our lifetime」  
  判断：**暂无法判断**。通用人工智能仍被描述为假设，全面超越尚未发生，有生之年窗口也未关闭，只能记录可能性仍被讨论，不能判定结果。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#17** 「there’s no fundamental reason why this progress can’t continue until AI matches human abilities on most tasks」  
  判断：**暂无法判断**。这是关于有无根本障碍的判断，窗口内既有快速进展也有对齐与能力上限争论，无法证实或证伪“不存在根本理由”。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>；<https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence>
- **#20** 「future AI may help us explore other solar systems and galaxies—if it’s bug-free」  
  判断：**暂无法判断**。星际探索性AI探测器尚未实现该结果，条件与结果都无法在窗口内判定。  
  来源：—
- **#27** 「One day, such robojudges may therefore be both more efficient and fairer」  
  判断：**暂无法判断**。窗口内未见可与人类法官全面替代比较的机器人法官制度落地，“有朝一日”终点未到。  
  来源：—
- **#28** 「they could make it dramatically cheaper to get justice」  
  判断：**暂无法判断**。该制度尚未规模化实施，成本效应无法观察。  
  来源：—
- **#29** 「models with a sterling safety record will qualify for premiums that are very」  
  判断：**暂无法判断**。Waymo等已商业运营，但存档来源未给出按安全记录定价、使优等车型保费极低的保险制度已经确立的证据。  
  来源：<https://en.wikipedia.org/wiki/Waymo>；<https://en.wikipedia.org/wiki/Self-driving_car>
- **#30** 「designed models from sloppy manufacturers will only qualify for insurance policies that make them prohibitivel…」  
  判断：**暂无法判断**。缺少窗口内按制造商安全记录使劣质车型保险贵到无法拥有的直接证据。  
  来源：<https://en.wikipedia.org/wiki/Self-driving_car>
- **#37** 「Once mass-produced, small AI-powered killer drones are likely to cost little more than a smartphone」  
  判断：**暂无法判断**。巡飞弹已出现并扩散，但本地存档未给出与智能手机价格直接比较的量产成本数据，无法判定该定量判断。  
  来源：<https://en.wikipedia.org/wiki/Loitering_munition>
- **#43** 「the whole archipelago will get submerged, and there will be no jobs left」  
  判断：**暂无法判断**。这是长期终点判断：窗口内仍有大量人类工作，全面“淹没”尚未发生，也不足以把它判为已经证伪。  
  来源：<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#46** 「There’s a non-negligible possibility that AGI progress will proceed to human levels and beyond」  
  判断：**暂无法判断**。该判断是对可能性的陈述，窗口内AGI仍属假说且争论继续，既不能证实也不能否定“不可忽视的可能”本身作为已实现结果。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>；<https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence>
- **#47** 「we can’t completely dismiss the possibility that we’ll eventually build human-level AGI」  
  判断：**暂无法判断**。同样是认知/可能性判断：至2026年仍无人能将该可能排除，但也不是一个已完成的事件结果。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#48** 「it’s likely that if it breaks out, we’ll have no idea how it happened」  
  判断：**暂无法判断**。递归自我改进仍属假说，被确认的超级智能逃逸事件并未发生，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#51** 「If we one day succeed in building human-level AGI, this may trigger an intelligence explosion, leaving us far …」  
  判断：**暂无法判断**。人类水平AGI尚未建成，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>；<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#52** 「If a group of humans manage to control an intelligence explosion, they may be able to take over the world in a…」  
  判断：**暂无法判断**。智能爆炸尚未发生，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#53** 「If humans fail to control an intelligence explosion, the AI itself may take over the world even faster」  
  判断：**暂无法判断**。智能爆炸尚未发生，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#54** 「a rapid intelligence explosion is likely to lead to a single world power」  
  判断：**暂无法判断**。迅速智能爆炸尚未发生，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#55** 「a slow one dragging on for years or decades may be more likely to lead to a multipolar scenario」  
  判断：**暂无法判断**。持续数年或数十年的智能爆炸尚未发生，条件未触发。  
  来源：<https://en.wikipedia.org/wiki/Recursive_self-improvement>
- **#56** 「Superintelligence is likely to enable coordination on ever-larger cosmic scales」  
  判断：**暂无法判断**。超级智能尚未出现，宇宙尺度协调无法观察。  
  来源：<https://en.wikipedia.org/wiki/Artificial_general_intelligence>
- **#58** 「The climax of our current race toward AI may be either the best or the worst」  
  判断：**暂无法判断**。竞赛仍在进行，高潮尚未到来，无法判定其为最好或最坏。  
  来源：<https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence>；<https://en.wikipedia.org/wiki/ChatGPT>
- **#60** 「I think it’s highly unlikely that the annual probability of accidental nuclear war is as low as one in a thous…」  
  判断：**暂无法判断**。一万年终点远未到来，窗口内9年未发生核战争既不能证实也不能证伪所设的年概率下限，条件性定量判断无法结算。  
  来源：—
- **#61** 「We’ll get there in a couple of centuries if computational power keeps doubling every couple of years」  
  判断：**暂无法判断**。倍增节奏已经放缓，前提存疑，两个世纪终点也未到。  
  来源：<https://en.wikipedia.org/wiki/Moore%27s_law>
- **#63** 「The main commodity shared or traded across cosmic distances is likely to be information」  
  判断：**暂无法判断**。尚无跨星系文明交易可观察，该判断无法核验。  
  来源：—
- **#64** 「the latter is arguably less likely than it is between today’s civilizations」  
  判断：**暂无法判断**。没有观察到的星际文明碰撞样本，无法比较可能性。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/tegmark-life-3-0-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/tegmark-life-3-0-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/tegmark-life-3-0-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本 audit 文件由批量 QA 于 2026-11-16 根据已有判定（来源：accepted_assessment）重建，供 canonical manual_report.py 生成报告；判定本身未在重建时改写。

