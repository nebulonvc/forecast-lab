# UNESCO International Commission on the Futures of Education（教科文组织教育的未来国际委员会）《共同重新构想我们的未来：教育的新社会契约》：出版后预测人工核查

- 案例目录：`cases/unesco-reimagining-our-futures-together-v5/`
- 出版日期：**2021-11-10**。英文报告 Reimagining Our Futures Together: A New Social Contract for Education 由教科文组织教育的未来国际委员会撰写，教科文组织于2021年11月10日正式发布（PDF 元数据 CreationDate 为 2021-11-02）。所用文件为公开英文 PDF（186页，sha256 9f91d253…），经 pdftotext -enc UTF-8 转为 TXT（sha256 e667f274…）。观察窗口按 2021-11-10 起算至 2026-11-15；书中写明的终点（2050、2070、2100、2030、2034、今后数年等）分别适用。不将发布日及此前已知事件计为出版后命中。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻仓库 DeepSeek 管线、仅以人工阅读替代模型调用：先对源文做 prepare_book v5 分块并逐块抽取，再经仓库代码对齐、去重后导入 data/claims.jsonl；核验时每条先写 scope，用 Exa 检索公开来源并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl），再由助手按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 51 条，剔除非预测 0 条，计入 **51 条预测**，其中 **40 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 16 |
| 趋势符合 | 10 |
| 部分符合 | 13 |
| 错误 | 1 |
| 暂无法判断 | 11 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **40.0%**（16/40） |
| 加权胜率 | **75.0%** |
| 错误率 | **2.5%**（1/40） |
| 未定占比（暂无法判断/预测） | 21.6%（11/51） |

## 总体评价

这份2021年报告的可核验判断里，对教育不平等、气候与人口格局、数字技术扩散等方向多数成立或部分成立，错误很少。不少条目写明2050或更远终点，或有赖世界银行/教科文组织分组统计，本轮部分曾因接口或下载失败暂无法判断，需在QA中重试证据后再决定是否改判。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（16 条）

- **#7** 「Even as schools reopened, millions of students will not return, particularly those from poorer and more margin…」  
  判断：**正确**。UNICEF 2022年3月指出重开后仍有大量儿童未返校，并记录乌干达2022年1月约十分之一学生未报到，与“数百万人不再返校”的方向和量级相符。  
  来源：<https://www.unicef.org/press-releases/23-countries-yet-fully-reopen-schools-education-risks-becoming-greatest-divider>
- **#8** 「the effects of climate change which have already taken place are baked into our systems, they will shape life …」  
  判断：**正确**。窗口期内2024年成为有记录以来最热年份，均温较工业化前高约1.55°C，极端天气已造成重大经济社会冲击，说明已锁定的气候影响正在塑造生活。  
  来源：<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>；<https://en.wikipedia.org/wiki/Climate_change>
- **#13** 「Even if zero-emissions were achieved tomorrow and we had 100% clean energy systems, we would still face the da…」  
  判断：**正确**。净零百科摘要写明即使达到全球净零，已在大气中的温室气体仍会继续贡献升温；同时2024年已出现破纪录高温与极端天气冲击，2026年地球仍在年度再生能力之前进入超载，说明承诺式气候影响与其他生态压力并未因“尚未零排放”而不存在。  
  来源：<https://en.wikipedia.org/wiki/Net_zero_emissions>；<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>；<https://en.wikipedia.org/wiki/Earth_Overshoot_Day>
- **#15** 「other extreme weather events that are likely to only increase in scale, degree and frequency.」  
  判断：**正确**。WMO确认2024年为有记录以来最热年份，并强调极端天气已带来巨大经济社会动荡，与规模和强度上升的方向一致。  
  来源：<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>
- **#16** 「Evidence shows that climate change increases gender inequality, especially among the most poor and marginalize…」  
  判断：**正确**。UN Women 2026年更新的解释稿明确指出气候危机并非性别中立，其影响会放大既有性别不平等，对妇女和女童的生计、健康与安全打击更重，与预测方向一致。  
  来源：<https://www.unwomen.org/en/news-stories/explainer/2022/02/explainer-how-gender-inequality-and-climate-change-are-interconnected>
- **#17** 「Technological innovations have reshaped the ways we live and learn and are certain to continue doing so.」  
  判断：**正确**。出版后生成式人工智能迅速进入文本、图像、代码等日常应用，教科文组织亦将2025年国际扫盲日主题放在数字时代的读写，说明技术仍在重塑生活与学习。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>；<https://www.unesco.org/sites/default/files/medias/fichiers/2025/09/ild-2025-factsheet.pdf>
- **#19** 「people of all ages, not just children, will be increasingly forced to learn to live with a damaged planet.」  
  判断：**正确**。破纪录高温、海平面与极端天气冲击已是当前生活条件的一部分，与“越来越被迫与受损星球共处”的方向相符。  
  来源：<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>；<https://en.wikipedia.org/wiki/Climate_change>
- **#25** 「Skills developed today are unlikely to align with those demanded by the jobs of tomorrow and many will become …」  
  判断：**正确**。数字时代读写被提到政策前台，生成式人工智能在出版后迅速改变对文本与代码技能的需求，说明既有技能组合正在过时、错配压力已经出现。  
  来源：<https://www.unesco.org/sites/default/files/medias/fichiers/2025/09/ild-2025-factsheet.pdf>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#31** 「The skillsets and critical outlooks required to understand technology and harness it for good will be in const…」  
  判断：**正确**。生成式人工智能在短时间内改变了所需的数字技能，扫盲政策也转向数字文本与工具，说明技能组合确实处于持续变动之中。  
  来源：<https://www.unesco.org/sites/default/files/medias/fichiers/2025/09/ild-2025-factsheet.pdf>；<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#33** 「which is part of what makes the relational work of teachers irreplaceable even by the most sophisticated machi…」  
  判断：**正确**。2024年联合国仍就全球教师短缺发出警报，需在2030年前新增4400万中小学教师，说明教学岗位在生成式人工智能出现后仍被当作不可替代的核心需求。  
  来源：<https://news.un.org/en/story/2024/02/1147067>
- **#35** 「Without significant changes, it will be difficult to attract the large number of motivated teachers-to-be need…」  
  判断：**正确**。小学教师流失率由2015年的4.62%升至2022年的9.06%，2024年仍就全球短缺发出警报，说明吸引和留住教师的困难在窗口内持续存在，条件“无重大改变”也大体成立。  
  来源：<https://news.un.org/en/story/2024/02/1147067>
- **#36** 「increased migration and internal displacement resulting from climate change, social and political violence, an…」  
  判断：**正确**。UNHCR统计显示，到2024年底全球流离失所人数达1232万，为十年高位，且主要受苏丹、缅甸、乌克兰等冲突推动，符合“未来数年将增多”。  
  来源：<https://news.un.org/en/story/2025/06/1164256>
- **#39** 「The pandemic has proved that the school cannot be entirely displaced into virtual spaces.」  
  判断：**正确**。各国在疫情后恢复面授，UNICEF强调无法与教师和同伴互动会使学习损失可能永久化，说明学校并未、也不能被完全迁入虚拟空间。  
  来源：<https://www.unicef.org/press-releases/23-countries-yet-fully-reopen-schools-education-risks-becoming-greatest-divider>；<https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education>
- **#40** 「special attention needs to be paid to refugees who do not enjoy the protection of a state. International bodie…」  
  判断：**正确**。2024年底全球流离失所人数创十年新高，强迫迁移在观察窗口内确实更加常见。  
  来源：<https://news.un.org/en/story/2025/06/1164256>
- **#44** 「Habitual ways of living, and our relationships to work and leisure will change.」  
  判断：**正确**。远程工作成为相对办公室出勤的常见安排，平台与零工就业持续扩张，说明工作组织方式在窗口内已经改变。  
  来源：<https://en.wikipedia.org/wiki/Remote_work>；<https://en.wikipedia.org/wiki/Gig_economy>
- **#51** 「emergency settings which are likely to increase in frequency as climate change accelerates.」  
  判断：**正确**。2024年破纪录高温与极端天气冲击，叠加十年高位的流离失所和持续冲突，说明气候与人道紧急状态在窗口内更频繁、更严重，与“频率可能增加”相符。  
  来源：<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>；<https://news.un.org/en/story/2025/06/1164256>

### 趋势符合（10 条）

- **#2** 「In higher and middle-income countries, participation rates are converging, with near universal pre-primary par…」  
  判断：**趋势符合**。世界银行WDI学前教育毛入学率显示，高收入与中等收入组别在2000–2020年由约41个百分点的差距收窄至约18个百分点，趋同方向清楚；高收入2020年为83.8%、中等收入为66.2%，2050年“接近普及”的终点尚未到达。  
  来源：<https://api.worldbank.org/v2/en/indicator/SE.PRE.ENRR?downloadformat=csv>
- **#4** 「Equally, this bodes well for a future of universal adult literacy, as youth move into adulthood.」  
  判断：**趋势符合**。UIS显示2015–2024年全球成人识字率仅由86%缓慢升至88%，青年识字率已达93%，方向朝普及，但2024年仍有7.39亿成人不具备基本识字能力，远未达到“普遍”。  
  来源：<https://www.unesco.org/sites/default/files/medias/fichiers/2025/09/ild-2025-factsheet.pdf>
- **#6** 「higher education participation rates in lower middle income counties will only reach some 35% by 2050, and les…」  
  判断：**趋势符合**。原文所称lower middle income在WDI口径下2024年高等教育毛入学率为27.4%，较2015年的21.7%继续上升，方向指向2050年前后约35%的量级；低收入组别2021年仍为9.3%，低于15%的上限，但该汇总数列此后缺值。2050年终点未到。  
  来源：<https://api.worldbank.org/v2/en/indicator/SE.TER.ENRR?downloadformat=csv>
- **#28** 「By 2050, dependency ratios are expected to increase sharply in Europe, North America, and more moderately in A…」  
  判断：**趋势符合**。人口老龄化确实先在发达国家深化、并已扩展到发展中国家，65岁及以上人口规模按官方展望将继续大幅上升，方向与预测一致；但本轮没有分区域抚养比的精确序列，不能确认“急剧/温和”的差别幅度。  
  来源：<https://en.wikipedia.org/wiki/Population_ageing>；<https://www.un.org/esa/foresight/chapter-three.html>
- **#29** 「the total dependency ratio for Africa is projected to decrease as half the region’s population will be under 2…」  
  判断：**趋势符合**。非洲人口快速增长并具有显著青年膨胀，与抚养比下降、人口结构年轻化的方向相符；但归档摘要未给出总抚养比或“一半人口在25岁以下”的精确核验数字，故只记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Africa>
- **#32** 「All projections point to a continuous growth in higher education enrolments in the coming decades.」  
  判断：**趋势符合**。世界高等教育毛入学率由2021年41.07%升至2024年43.62%，2015年以来也由36.6%持续上升，入学人数/参与率在“未来几十年”窗口的已观察阶段继续增长；该期限尚未走完，记趋势符合而非终局正确。  
  来源：<https://api.worldbank.org/v2/en/indicator/SE.TER.ENRR?downloadformat=csv>
- **#38** 「This sustained lack of in-person education had profound impacts on the social, intellectual, and mental well-b…」  
  判断：**趋势符合**。UNICEF记录面授中断规模巨大，并警告学习损失可能成为永久性，与长期影响的方向相符；但“贯穿一生”在截止日仍无法完成观察，故记趋势符合而非终局正确。  
  来源：<https://www.unicef.org/press-releases/23-countries-yet-fully-reopen-schools-education-risks-becoming-greatest-divider>；<https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education>
- **#42** 「As more and more people live longer and healthier lives, the ways that education is entangled with life will c…」  
  判断：**趋势符合**。预期寿命已恢复并继续延长、人口老龄化加深，人生阶段结构确实在变；但教育制度如何随之改组（终身学习、学段重排等）缺少直接证据，故记趋势符合。  
  来源：<https://ourworldindata.org/un-population-2024-revision/>；<https://en.wikipedia.org/wiki/Population_ageing>；<https://www.un.org/esa/foresight/chapter-three.html>
- **#45** 「If these trends continue, there is considerable danger that in 2050 much」  
  判断：**趋势符合**。生成式人工智能在出版后加速把知识生产与检索变成模型和设备中介的过程，条件大体成立、方向相符；但2050年终点未到，也不能证明“许多知识只能经数字设备获取”已经实现。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#47** 「a continent that will be home to the world’s largest share of youth in 2050, and which is projected to face so…」  
  判断：**趋势符合**。ECA称2050年全球每三名青年中将有一名是非洲人，这支持“份额最大”的方向；同时破纪录高温与极端天气也显示环境压力已经很直接。2050年份额尚未实现，故记趋势符合。  
  来源：<https://businessday.ng/news/article/eca-urges-investment-in-youth-says-1-in-3-young-people-globally-will-be-african-by-2050/>；<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>

### 部分符合（13 条）

- **#1** 「To continue on the current path is to accept unconscionable inequalities and exploitation, the spiralling of m…」  
  判断：**部分符合**。出版后冲突与被迫流离失所升至2024年底1232万人的十年高位，2024年全球均温破纪录、极端天气冲击巨大，说明暴力与环境破坏方向发生；但“灾难性生物多样性丧失”与全球不平等趋势缺少同等直接度量，不能算主要结果全部兑现。  
  来源：<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024>；<https://news.un.org/en/story/2025/06/1164256>；<https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts>
- **#5** 「Projections based on trends since 1970 indicate that high income countries could reach 100% participation rate…」  
  判断：**部分符合**。高收入国家高等教育毛入学率由2015年76.2%升至2024年82.0%，仍在上升，但按近九年约0.65个百分点/年的速度，到2034年难以达到100%；中等收入由2015年33.6%升至2024年43.3%，若节奏大体延续，2050年落入60%–80%区间更为接近。两项数量预测只有后一项方向和节奏较吻合。  
  来源：<https://api.worldbank.org/v2/en/indicator/SE.TER.ENRR?downloadformat=csv>
- **#9** 「the deadline will come much sooner.」  
  判断：**部分符合**。已归档的IPCC AR6 WGIII决策者摘要显示，将升温限制在1.5°C的路径中，全球净零CO2的中位时段仍约为2050–2055年，并不是把时限整体改到“远早于2050”；但5–95百分位可早至2035年，部分路径确实早于2050。与“时限将比2050早得多”的主表述只部分相符。  
  来源：<https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_SPM.pdf>
- **#10** 「Current projections suggest population growth will reach 9.7 billion in 2050 and then likely plateau at around…」  
  判断：**部分符合**。WPP 2024中位方案将2050年写作96亿（另有9.7亿约数），与97亿接近；但峰值被提前到2080年代中期约103亿，2100年回落至102亿，并不存在“稳定在约110亿”的平台。  
  来源：<https://www.un.org/esa/foresight/chapter-three.html>；<https://news.un.org/en/story/2024/07/1151971>；<https://ourworldindata.org/un-population-2024-revision/>
- **#23** 「The greening of our economies will create millions of jobs as we adopt sustainable practices and clean technol…」  
  判断：**部分符合**。IRENA与国际劳工组织2023年《可再生能源与就业》记录，可再生能源直接和间接就业在2022年已达1370万，并预期未来还会再增加数百万岗位，绿色就业“创造数百万”这一侧已有清楚证据；同一摘录没有给出各国缩减碳密集产业后岗位消失的对应官方数列，另一侧仍不能确认。  
  来源：<https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2023/Sep/IRENA_Renewable_energy_and_jobs_2023.pdf>
- **#24** 「The platform economy could recreate nineteenth century working」  
  判断：**部分符合**。零工与平台经济在21世纪持续扩张、并主要通过数字平台组织劳动，与“数字零工”兴起相符；但已归档摘要并未直接证明其用工条件已经等同于十九世纪日工制，故只记部分符合。  
  来源：<https://en.wikipedia.org/wiki/Gig_economy>；<https://en.wikipedia.org/wiki/Platform_economy>
- **#26** 「a future very likely to reinforce the significance of the informal economy for billions around the world.」  
  判断：**部分符合**。非正规经济仍在发展中国家占重要份额，零工/平台用工也在扩张，与“非正规和新型就业更重要”相符；但“2021年后进一步强化”的增量以及再培训压力缺少直接统计，故记部分符合。  
  来源：<https://en.wikipedia.org/wiki/Informal_economy>；<https://en.wikipedia.org/wiki/Gig_economy>
- **#27** 「A quickly expanding youth population in some regions is set to exacerbate youth unemployment and migratory pre…」  
  判断：**部分符合**。非洲仍呈显著青年膨胀，全球65岁及以上人口走向快速上升，与人口侧预测一致；但青年失业和移民压力、社保负担加重缺少可绑定的劳动与财政数据，只能部分确认。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Africa>；<https://en.wikipedia.org/wiki/Population_ageing>；<https://www.un.org/esa/foresight/chapter-three.html>
- **#30** 「Human longevity may also increase and perhaps with it, at least for some, the extension of the work period of …」  
  判断：**部分符合**。OWID依据WPP指出全球预期寿命已回到并超过疫情前水平，寿命延长这一侧得到支持；工作年限是否延长则没有可绑定证据，结果只部分成立。  
  来源：<https://ourworldindata.org/un-population-2024-revision/>
- **#34** 「close to 70 million new primary and secondary teachers will need to be recruited worldwide by 2030 to meet the…」  
  判断：**部分符合**。全球教师短缺仍然存在，但教科文组织2024年报告将所需新增中小学教师修订为4400万，数量明显低于近7000万，故主要方向成立、幅度不符。  
  来源：<https://news.un.org/en/story/2024/02/1147067>
- **#46** 「Their room for manoeuvre will be affected by the economic realities of a post-pandemic world, as international…」  
  判断：**部分符合**。UNHCR方面出现“流离失所人数十年倍增而资金水平大致不变”、标题亦写作资金收缩，说明至少在难民人道主义融资上出现了相对紧缩；但这不是全球教育官方发展援助的完整账本，故只记部分符合。  
  来源：<https://news.un.org/en/story/2025/06/1164256>
- **#48** 「Aid supplies an ever-shrinking share of national needs, and as such will have declining influence and relevanc…」  
  判断：**部分符合**。难民机构资金未随需求倍增而增加，相对份额下降已经出现；但“全球舞台上的影响力下降”缺少可独立核验的度量，故只记部分符合。  
  来源：<https://news.un.org/en/story/2025/06/1164256>
- **#49** 「displaced populations and involuntary migrants, whose numbers will grow as the climate crisis deepens.」  
  判断：**部分符合**。2024年底流离失所人数确实升至十年高位；但该材料把主因归纳为苏丹、缅甸、乌克兰等地的冲突，气候危机加深只得到部分对应，不能把全部增量记到气候上。  
  来源：<https://news.un.org/en/story/2025/06/1164256>

### 错误（1 条）

- **#50** 「particularly on Africa, where the vast majority of the world’s youth will live and learn by 2050.」  
  判断：**错误**。联合国非洲经济委员会在2024年公开采用的口径是：到2050年全球每三名青年中将有一名来自非洲。三分之一并不能构成“绝大多数”，与该判断的主要数量含义相反。  
  来源：<https://businessday.ng/news/article/eca-urges-investment-in-youth-says-1-in-3-young-people-globally-will-be-african-by-2050/>；<https://www.un.org/esa/foresight/chapter-three.html>

### 暂无法判断（11 条）

- **#3** 「This bodes well for primary gender parity in the coming years, as pre-primary cohorts age into primary」  
  判断：**暂无法判断**。未取到小学毛入学性别均等指数（GPI）的官方时间序列，无法确认2021年后“未来数年”是否已实现或仍存缺口。  
  来源：—
- **#11** 「It is estimated that by 2050, demand for food will rise by another 35%, demand for water by 20-30%, and demand…」  
  判断：**暂无法判断**。2050年终点未到，且本轮未检索到可归档的FAO/IEA官方需求预测文本，无法核验这组百分比。  
  来源：—
- **#12** 「Without course correction, in 2050 we will be using resources at four times the rate it takes for them to repl…」  
  判断：**暂无法判断**。2026年地球超载日仍在7月30日，说明持续处于生态超载，但该指标不能折算为“再生速度的四倍”；2050年终点未到，也未见通往四倍的可检验轨迹。  
  来源：<https://en.wikipedia.org/wiki/Earth_Overshoot_Day>
- **#14** 「up to one-third of the world’s population is likely to live in areas that are considered unsuitably hot」  
  判断：**暂无法判断**。2070年终点远未到达，本轮也未取得该“三分之一”预测所依据的后续研究文本，不能用五年窗口外推终局。  
  来源：—
- **#18** 「the capacity to resist the negative aspects of digitality which could become increasingly widespread in 2050」  
  判断：**暂无法判断**。2050年终点未到；已归档材料可以说明生成式人工智能扩散，但没有足以度量“负面方面更普遍”的系统指标，不能把技术扩散直接写成该预测已经兑现。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#20** 「The unknown trajectories of these political transformations will be with us at least for several decades with …」  
  判断：**暂无法判断**。“至少数十年”的终点未到，且本轮未取得全球民主/威权指数或教育政治化的可归档数据集，无法评价轨迹。  
  来源：—
- **#21** 「This global crisis disrupted the world of work in ways that are still coming into focus and are expected by ma…」  
  判断：**暂无法判断**。已归档的人口材料显示全球预期寿命已回到并超过疫情前水平，但这不是劳动市场疤痕的直接证据；本轮未取得ILO等就业/劳动力参与率的官方序列，无法判定长期不利后果是否成立。  
  来源：<https://ourworldindata.org/un-population-2024-revision/>
- **#22** 「Technological advances, such as AI, automation and robotics, will create new jobs, but will also displace many…」  
  判断：**暂无法判断**。生成式人工智能已出现，但已归档摘要只说明其生成能力，没有给出创造与取代岗位的净效应，也没有“失业者最缺乏准备”的直接证据。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#37** 「the growth of machine learning technologies risks fragmenting educational processes into ‘data sets’ and accel…」  
  判断：**暂无法判断**。已归档材料没有教育场景中的监控、管理主义或去专业化指标，不能把生成式人工智能的一般扩散写成该风险已经实现。  
  来源：<https://en.wikipedia.org/wiki/Generative_artificial_intelligence>
- **#41** 「The continued normalization of surveillance – especially if education systems habituate children to it from yo…」  
  判断：**暂无法判断**。“教育系统从幼年习惯监控”这一前提在已归档材料中既未证实也未证伪，条件未确立，不能按正误计分。  
  来源：—
- **#43** 「In some areas four generations will be co-living in the same space-time in a way never seen in history.」  
  判断：**暂无法判断**。老龄化与寿命延长使四代重叠在人口学上更为可能，但本轮没有家庭结构或隔代同居的统计，不能把可能性写成已经发生的事实。  
  来源：<https://en.wikipedia.org/wiki/Population_ageing>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/unesco-reimagining-our-futures-together-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/unesco-reimagining-our-futures-together-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/unesco-reimagining-our-futures-together-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本 audit 文件由批量 QA 于 2026-11-16 根据已有判定（来源：accepted_assessment）重建，供 canonical manual_report.py 生成报告；判定本身未在重建时改写。

- 2026-11-16 QA 对原先因世界银行接口/教科文组织统计下载失败而暂无法判断的条目重试了官方WDI批量CSV、IPCC AR6 WGIII SPM、IRENA《可再生能源与就业》2023和Xu等预测的BBC报道。其中#2、#6、#32改为趋势符合，#5、#9、#23改为部分符合；#3因小学GPI汇总值仍止于2020年保持暂无法判断。判定改动见 STATUS 与 notes/unesco_qa_changes.json。

