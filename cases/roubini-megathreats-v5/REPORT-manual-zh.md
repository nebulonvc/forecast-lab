# 鲁比尼《大威胁》（MegaThreats, Nouriel Roubini, 2022）：出版后预测人工核查

- 案例目录：`cases/roubini-megathreats-v5/`
- 出版日期：Little, Brown and Company / Hachette Book Group 英文电子版，版权页载明 Copyright © 2022 by Nouriel Roubini，First ebook edition: October 2022，ISBN 978-0-316-28453-0。**按 2022-10 起算**至 2026-11-15。所用 PDF 为 catalog 所载 298 页英文版，sha256 79228e790812b6a6d2f642fd651a745e8c6b3cb148edfb173c2116e566c03ee0。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 pdftotext -enc UTF-8 生成全书 TXT（sha256 `cafde0d71374aeeb1a7390478a0a623cf5e23a4c3039736b092b95cfa2080830`，619,271 字符），`prepare_book.split_text(3500, 600)` 得到 179 个 chunk，逐块通读。版权页、目录、题献、致谢、作者简介和书末注释未抽预测。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 115 条可解析预测（全部 claim_type=forecast）。核验按 METHOD.md 的 PLAN/SELECT/ASSESS 口径，证据为带 sha256 的维基百科存档（data/sources + data/evidence.jsonl，54 条），并经 `pipeline.py apply assess` → `check` → `report`。引文均为 TXT 逐字片段。全文 TXT 未入库。本稿由助手逐条对照书中原文，并依据 2022-10 至 2026-11-15 窗口内可公开访问的来源人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 115 条，剔除非预测 0 条，计入 **115 条预测**，其中 **87 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 25 |
| 趋势符合 | 17 |
| 部分符合 | 44 |
| 错误 | 1 |
| 暂无法判断 | 28 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **28.7%**（25/87） |
| 加权胜率 | **68.7%** |
| 错误率 | **1.1%**（1/87） |
| 未定占比（暂无法判断/预测） | 24.3%（28/115） |

## 总体评价

这本书几乎整本都在谈出版后的超级威胁，所以可核验判断很多。约四年窗口里，方向说对的不少：中国房地产债务危机继续恶化并在2024年走到恒大清盘；美联储加息后出现2023年银行业风波，购买力因2021–2023通胀下降；友岸外包、出口管制和中美技术阵营化把全球经济往分裂里推；新冷战更冷、美国强化对台安全关系；2025年6月以色列打击伊朗军事与核设施（条件触发）；美元储备份额缓降但并未一夜崩塌；化石燃料远未被淘汰，气候极端天气已在改变美国日常生活。
说错或明显过头的，主要是把“比1970年代更糟的大滞胀”写成近期主情景：通胀在2022年见顶后于2023年明显回落，美国被广泛认为实现了软着陆。发达经济体“到2024年65%可能衰退”也只在部分欧洲经济体浅度应验。许多十年尺度的判断——债务危机之母、欧元区瓦解、护理机器人很快取代人力、中国2030年前成为最大经济体——只能记趋势或暂无法判断。
总体上看，这本书对“方向会变糟、体系会分裂、技术与地缘会重塑世界”比较敏感，对幅度、同步性和“史诗级崩溃”的节奏偏鹰。严格胜率因此不高，加权胜率仍可看，因为它把大量“方向对、终点未到”的条目计了进去。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（25 条）

- **#2** 「Welcome to the era of megathreats: they will alter the world we thought we knew」  
  判断：**正确**。生成式AI爆发、伊以开战、持续通胀与中美脱钩，确实改变了2022年时人们熟悉的政治经济图景  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>
- **#7** 「The megathreats we face will reshape our world」  
  判断：**正确**。AI扩散、地缘冲突、去全球化讨论和气候影响，均在出版后重塑了政策与市场议程  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/Climate_change>
- **#8** 「The coming tsunami will not spare China」  
  判断：**正确**。中国房地产债务危机在出版后继续深化，恒大2024年被下令清盘，多家开发商违约，未获“豁免”  
  来源：<https://en.wikipedia.org/wiki/Chinese_real_estate_crisis_(2020%E2%80%93present)>；<https://en.wikipedia.org/wiki/Evergrande_Group>
- **#14** 「our purchasing power is likely to decrease」  
  判断：**正确**。2021–2023年通胀使消费价格明显高于疫情前，实际购买力下降；即使通胀率回落，价格水平仍高  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#22** 「These financial pressures are destined to increase」  
  判断：**正确**。老龄化下社保与医疗支出压力在受托人报告中持续上修或维持高压，方向已经可观察  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#26** 「the incipient flow of potential migrants from poor countries to richer ones will swell in the next few years」  
  判断：**正确**。气候灾害、地区战争和持续的庇护/边境压力表明移民压力在出版后上升  
  来源：<https://en.wikipedia.org/wiki/Climate_migration>；<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict>
- **#33** 「By restricting global trade in goods, services, capital, technology, data, and investments, they will impose h…」  
  判断：**正确**。关税、出口管制和友岸外包持续，友岸本身被指推高制造成本；中美脱钩抑制部分贸易  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>
- **#34** 「shifting production from low-cost emerging markets such as China to friendlier but higher-cost developed marke…」  
  判断：**正确**。友岸外包词条明确其代价包括制造更昂贵、产出下降，与预测一致  
  来源：<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>
- **#35** 「When security replaces efficiency in allocating capital, costs of productions will rise」  
  判断：**正确**。芯片补贴、实体清单和友岸政策把安全置于效率之上，并带来成本上升  
  来源：<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>；<https://en.wikipedia.org/wiki/Entity_List>
- **#41** 「Debt will continue to mount from explicit debt contracts and the implicit tab for addressing unfunded Social S…」  
  判断：**正确**。美国公共债务和社保长期缺口在窗口内继续存在并受关注，方向正确  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>；<https://en.wikipedia.org/wiki/Federal_Reserve>
- **#42** 「The draconian financial sanctions imposed on Russia to punish it for the brutal invasion of Ukraine will accel…」  
  判断：**正确**。去美元化讨论因制裁而升温，中俄贸易和金融往来加深，与“加速意愿”相符  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/China%E2%80%93Russia_relations>
- **#53** 「Expect a gradual but steady balkanization of the global economy as the current geopolitical depression becomes…」  
  判断：**正确**。友岸、出口管制、平行供应链和中美技术阵营化，显示全球经济在分裂，方向清楚  
  来源：<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#56** 「We will see reshoring and friend-shoring at the expense of full on-shoring」  
  判断：**正确**。友岸外包成为政策词汇并付诸补贴与供应链转移，与“而非完全在岸”的折中路径相符  
  来源：<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>
- **#68** 「An emerging new cold war is already becoming colder and will disrupt supply chains and rearrange alliances」  
  判断：**正确**。友岸、芯片联盟和AUKUS等表明供应链被扰乱、联盟被重组  
  来源：<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>；<https://en.wikipedia.org/wiki/AUKUS>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>
- **#70** 「I’m of the view—like many other analysts—that a cold war will get colder with more competition and confrontati…」  
  判断：**正确**。出口管制、实体清单、技术脱钩和AI军备竞赛表明竞争与对抗上升、合作空间缩小  
  来源：<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/Entity_List>；<https://en.wikipedia.org/wiki/AI_boom>
- **#72** 「A more fragmented economy will increasingly divide the world into two competing economic systems, one dominate…」  
  判断：**正确**。技术、数据和部分关键产业出现阵营化，方向清楚，但贸易并未完全一分为二  
  来源：<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#75** 「The second cold war looks so different from its predecessor at the start, and we should not expect it to end i…」  
  判断：**正确**。中国仍是世界第二大经济体和最大制造业国家，并未崩溃或“收摊认输”  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#77** 「Israel, which sees a nuclear Iran as an existential threat to its survival, is likely to strike Iran if Iran c…」  
  判断：**正确**。IAEA在开战前认定伊朗未履行核义务，以色列于2025年6月打击伊朗军事与核设施，条件触发且结果吻合  
  来源：<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/2024_Iran%E2%80%93Israel_conflict>；<https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict>
- **#79** 「the United States is likely to beef up its supply of military equipment to the island, as it belatedly did for…」  
  判断：**正确**。美台安全关系与印太安全安排在出版后继续强化，方向与“加强对岛上军备供应”一致  
  来源：<https://en.wikipedia.org/wiki/Taiwan%E2%80%93United_States_relations>；<https://en.wikipedia.org/wiki/AUKUS>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#84** 「Across the United States, global warming will upend daily life」  
  判断：**正确**。热浪、西部干旱和2024年极具破坏性的飓风季，表明气候影响已在改变美国日常生活  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Droughts_in_the_United_States>；<https://en.wikipedia.org/wiki/Effects_of_climate_change>；<https://en.wikipedia.org/wiki/2024_Atlantic_hurricane_season>
- **#90** 「the idea that we will fully phase out fossil fuels in the next few decades is totally far-fetched」  
  判断：**正确**。化石燃料仍在全球能源结构中占核心地位，能源危机也显示系统仍高度依赖化石能源，与“彻底淘汰不切实际”相符  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_the_United_States>；<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_China>
- **#100** 「America’s reserve currency status won’t collapse overnight, but we will see it coming」  
  判断：**正确**。美元仍是主导储备货币，同时份额缓降、去美元化在推进，与“不会一夜崩塌、但能看到它在走来”相符  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/Reserve_currency>
- **#102** 「The economic malaise and rising inequality that leads to populism will spur a backlash against free trade and …」  
  判断：**正确**。产业政策、关税、友岸和保护主义回潮，表明对自由贸易和全球化的政治反弹在继续  
  来源：<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/2022_United_States_elections>
- **#104** 「Those adversaries will increasingly counter American strength with asymmetric warfare that deploys cyber espio…」  
  判断：**正确**。深度伪造、网络攻击和信息战在AI时代被广泛视为不对称工具，地缘冲突中的代理与网络对抗也在升级  
  来源：<https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict>；<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#106** 「Earth’s rising temperature will unleash storms and heat waves more frequent and more severe than humans can en…」  
  判断：**正确**。热浪、干旱和2024年高损失飓风季支持“更严重的极端天气”；“超出人类承受”是程度上的夸张  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Effects_of_climate_change>；<https://en.wikipedia.org/wiki/2024_Atlantic_hurricane_season>；<https://en.wikipedia.org/wiki/Droughts_in_the_United_States>

### 趋势符合（17 条）

- **#15** 「Current projections anticipate insolvency—the fund running out of assets—in 2033」  
  判断：**趋势符合**。2026年受托人报告将OASI耗尽时点前移至2032年第四季度，方向与时点都接近原预测，但终点尚未到来  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>；<https://en.wikipedia.org/wiki/Social_Security_Trust_Fund>
- **#16** 「Anyone who expects to retire after that date may see only about 76 percent of the benefits that they are owed」  
  判断：**趋势符合**。2026年报告：OASI耗尽后可支付预定给付的78%，合并口径约83%，与书中约76%同方向、幅度接近，终点未到  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#25** 「Employers worldwide are likely to go the same route, putting algorithms to work instead of humans」  
  判断：**趋势符合**。生成式AI和企业自动化加速，方向明确，但远未成为全球雇主的统一做法  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#28** 「promises of pensions and health care to older workers will become untenable in the foreseeable future」  
  判断：**趋势符合**。信托基金耗尽路径表明现行承诺在2030年代将无法全额兑现，方向符合，全面“难以为继”尚未发生  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#37** 「Vast tracts of the earth will face severe drought and become desert, lacking water」  
  判断：**趋势符合**。美国西部长期干旱、全球干旱和荒漠化风险有记录且被指将随变暖加剧，方向符合，全球“大片变成荒漠”尚未完成  
  来源：<https://en.wikipedia.org/wiki/Droughts_in_the_United_States>；<https://en.wikipedia.org/wiki/Effects_of_climate_change>；<https://en.wikipedia.org/wiki/Climate_change>
- **#40** 「over the next few decades, the dollar is likely to become tarnished」  
  判断：**趋势符合**。官方储备中的美元份额二十年来缓慢下降，去美元化在推进，但美元仍居主导，更像“开始失光”而非已经失色  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/Reserve_currency>
- **#44** 「Gradually, the role of the US dollar as the major global reserve currency could start to slip and fade」  
  判断：**趋势符合**。储备份额缓慢下降，符合“开始下滑”；“褪色”远未完成  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>
- **#45** 「The Chinese, seeing most of the Russian foreign reserves in dollars, euros, pounds, yen, and so forth frozen d…」  
  判断：**趋势符合**。在制裁示范和美方技术管制下，中国推动本币结算与备用支付渠道，脱钩在推进但远未完成  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93Russia_relations>；<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/Entity_List>
- **#46** 「Even if the US dollar retains global reserve currency status in the short run, over the next two decades its r…」  
  判断：**趋势符合**。窗口只覆盖预测时域的一小段，已出现份额缓降，方向符合，终点未到  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/Reserve_currency>
- **#65** 「Indeed who controls AI may become the dominant world super-power」  
  判断：**趋势符合**。美中被广泛描述为处于AI竞赛/AI冷战，算力与模型成为国力变量，方向符合，尚未出现单一主导者  
  来源：<https://en.wikipedia.org/wiki/AI_boom>
- **#82** 「Global warming of 1.5 degrees C and 2 degrees C will be exceeded during the 21st century unless deep reduction…」  
  判断：**趋势符合**。全球持续升温、影响增强，1.5℃的长期超标风险仍然很高；21世纪终点未到，且取决于后续减排  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Effects_of_climate_change>
- **#83** 「the world was increasingly at risk of experiencing global warming of 1.5 degrees C within the next five years」  
  判断：**趋势符合**。全球气温纪录在窗口内被多次刷新，接近或短暂触及1.5℃的讨论增多，方向符合，五年窗口在2027年才结束  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Effects_of_climate_change>
- **#87** 「Lofty pledges promise to reduce emissions by 50 percent for the United States and 55 percent for Europe by 203…」  
  判断：**趋势符合**。美国排放有所下降但仍是全球第二，2025年仍约70亿吨，距离十年末减半目标仍远，方向符合，2030终点未到  
  来源：<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_the_United_States>
- **#89** 「the melting of the permafrost will release massive amounts of methane」  
  判断：**趋势符合**。气候影响综述确认永久冻土正在融化，甲烷释放是已知反馈，方向符合，释放规模的观测仍在推进  
  来源：<https://en.wikipedia.org/wiki/Effects_of_climate_change>；<https://en.wikipedia.org/wiki/Climate_change>
- **#92** 「the goal of cutting GHG emissions in the US in half by the end of the decade looks dead on arrival」  
  判断：**趋势符合**。《通胀削减法案》提供了政策工具，排放有下降，但以2025年仍高居全球第二、降幅有限来看，减半目标仍然非常勉强，终点未到  
  来源：<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_the_United_States>；<https://en.wikipedia.org/wiki/Inflation_Reduction_Act>
- **#99** 「Debasement and weaponization of the dollar for geopolitical goals will lead to a gradual decline of central ba…」  
  判断：**趋势符合**。制裁强化了武器化印象，官方储备中的美元份额呈长期缓降，方向符合  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>
- **#111** 「They will materialize over the next decade or two」  
  判断：**趋势符合**。多种威胁已在窗口内显现，方向符合，完整时域（至约2040年）尚未结束  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Deglobalization>

### 部分符合（44 条）

- **#1** 「this long stretch of relative prosperity is not likely to continue much longer」  
  判断：**部分符合**。窗口内出现高通胀、乌克兰战争、2023年银行风波和中国房地产危机，稳定性下降；但美国实现软着陆、未陷入萧条式崩溃，繁荣并未整体中断  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Chinese_real_estate_crisis_(2020%E2%80%93present)>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#3** 「are at serious risk of giving way to economic and financial crises unlike anything we’ve seen since the Great …」  
  判断：**部分符合**。出现了严重通胀和2023年银行业风波，但深度和持续度远不及大萧条，美国还避免了衰退  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#6** 「We cannot assume that automating certain jobs will lead to new and better jobs elsewhere, as it often has in t…」  
  判断：**部分符合**。生成式AI在部分认知任务上形成替代，同时也在模型和芯片等环节创造新岗位；“不能再假定别处必然出现更好工作”只得到部分支持，并非已确认的单方向结果。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#9** 「Debt that was manageable when interest rates were zero or negative will become unsustainable as central banks …」  
  判断：**部分符合**。加息确实导致2023年银行债券巨亏和挤兑，说明债务/久期风险显现；但多数主权和家庭债务仍可维持，未出现全球性不可持续崩溃  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Silicon_Valley_Bank>；<https://en.wikipedia.org/wiki/Federal_Reserve>
- **#11** 「some sort of event will eventually lance the worldwide debt bubble」  
  判断：**部分符合**。部分经济体增长放缓，冲击刺破了局部泡沫（中资地产、部分银行），但全球债务泡沫并未被整体刺破  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Chinese_real_estate_crisis_(2020%E2%80%93present)>
- **#12** 「The next shock is likely to push us over」  
  判断：**部分符合**。2023年银行冲击一度接近临界，但监管紧急出手，系统未被整体推倒  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>
- **#13** 「It could come in the form of a great crash, bursting the bubble and triggering default, or inflation, or even …」  
  判断：**部分符合**。通胀确实在2022年前后大幅上升，并伴随局部金融压力；但随后通胀回落，美国软着陆，并未出现大崩盘或持久滞胀  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#18** 「Lower rates of spending and savings by younger generations will pump the brakes on economic growth」  
  判断：**部分符合**。老龄化对增长构成逆风，但美国在窗口内仍实现软着陆，增长未被明显“踩刹车”  
  来源：<https://en.wikipedia.org/wiki/Soft_landing_(economics)>；<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#24** 「Also, productivity growth may fall with aging」  
  判断：**部分符合**。老龄化是逆风，但生成式AI带来新的生产率讨论，窗口内并非简单下降  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#27** 「Alas, the gates and borders will be closed to them, not just in Japan but increasingly in the United States an…」  
  判断：**部分符合**。政策确有收紧，但美欧仍经历大规模抵达，边境并未真正“关闭”  
  来源：<https://en.wikipedia.org/wiki/Climate_migration>；<https://en.wikipedia.org/wiki/2022_United_States_elections>
- **#29** 「Thus I see the probability of a recession in advanced economies at 65 percent by 2024」  
  判断：**部分符合**。美国被广泛认为实现软着陆、避免了衰退；部分欧洲经济体出现浅度或技术性收缩，结果是分化而非全面衰退  
  来源：<https://en.wikipedia.org/wiki/Soft_landing_(economics)>；<https://en.wikipedia.org/wiki/Recession>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#32** 「The shrinking pool of young workers will force employers to boost wages to fill jobs」  
  判断：**部分符合**。2022–2023年劳工市场紧张、工资加快上升，与预测同向；随后劳动力市场降温，涨薪放缓，且移民也补充了供给  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#36** 「Global climate change will trigger stagflationary pressures in at least three ways」  
  判断：**部分符合**。2020年代能源危机、干旱和极端天气带来供给冲击，曾推高通胀；但未形成持续滞胀机制  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#38** 「Energy prices are apt to rise so long as this imbalance persists」  
  判断：**部分符合**。2022年能源价格大涨，之后回落，说明失衡期价格确会上升，但失衡并未在整个窗口持续  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/Price_of_oil>
- **#43** 「They will start trading goods, services, commodities, and financial assets using the ruble and the renminbi (R…」  
  判断：**部分符合**。2022年后中俄贸易显著扩大，人民币原油合约和本币结算也在推进，但归档摘要并未证明商品、服务、大宗商品和金融资产已开始以卢布和人民币而非美元交易。  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93Russia_relations>；<https://en.wikipedia.org/wiki/Petroyuan>；<https://en.wikipedia.org/wiki/Renminbi>
- **#47** 「elevating crypto to the status of legitimate currencies endorses a dangerous precedent that is most likely to …」  
  判断：**部分符合**。FTX在出版后不久破产，加密货币仍未成为普遍法偿货币，这条判断部分成立；但作为资产类别后来显著反弹，并非全面“惨败”  
  来源：<https://en.wikipedia.org/wiki/FTX>；<https://en.wikipedia.org/wiki/Terra_(blockchain)>；<https://en.wikipedia.org/wiki/Cryptocurrency>
- **#49** 「Instead of promoting stability, they will elevate systemic risk and disruptions to levels we have never seen b…」  
  判断：**部分符合**。加密崩溃和2023年银行风波显示风险上升，但幅度仍低于2008年，难言“前所未见”  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/FTX>
- **#50** 「Expect chaos and financial instability as fiat currencies get debased, the EMU may eventually implode, the rol…」  
  判断：**部分符合**。美元地位受到更多挑战、去美元化在讨论中升温；但欧元区并未瓦解，也没有出现全面货币体系混乱  
  来源：<https://en.wikipedia.org/wiki/Dedollarisation>；<https://en.wikipedia.org/wiki/Reserve_currency>
- **#51** 「Deglobalization will stymie economic growth, disable the means to cope with massive debts, and grease the rail…」  
  判断：**部分符合**。友岸、管制和贸易分裂在推进，也曾叠加通胀；但美国软着陆，未出现“史诗级”通胀滞胀和偿债能力普遍丧失  
  来源：<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#52** 「China will certainly retaliate, in part by penalizing Chinese firms that launch initial public offerings on US…」  
  判断：**部分符合**。中概股监管和上市/退市压力在中美博弈中确实存在，但“肯定会报复、且以惩罚赴美IPO为手段”在窗口内并非清晰的新的、全面报复行动  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/Entity_List>
- **#54** 「Opponents of globalization have found one, and in the foreseeable climate they will have the upper hand」  
  判断：**部分符合**。关税、产业政策和贸易冲突在窗口内延续，保护主义回潮是事实；但去全球化词条是概念说明，全球贸易并未被反全球化力量压倒，“占上风”并未被清楚确立。  
  来源：<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/2022_United_States_elections>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>
- **#57** 「To be sure, slowbalization would curb competition and productivity, adding stagflationary pressures」  
  判断：**部分符合**。友岸外包被指提高成本和降低产出，与抑制竞争、抬升成本的方向部分相符；窗口内并未出现全面滞胀。  
  来源：<https://en.wikipedia.org/wiki/Friendshoring>；<https://en.wikipedia.org/wiki/Deglobalization>
- **#61** 「a large number of white-collar jobs using advanced levels of cognition will become obsolete」  
  判断：**部分符合**。生成式AI已冲击写作、编程和客服等认知任务，但“白领工作将变得过时”尚未普遍发生，也未被就业数据坐实。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#62** 「All signs indicate that AI alternatives will drive down wages and salaries」  
  判断：**部分符合**。部分可自动化职业出现议价压力的讨论，但归档材料没有工资被AI压低的序列，且2022–2023年宏观工资还在上升，不能记为已经确认的降薪方向。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#67** 「The United States may lose leadership in the technologies of the future that increasingly link everything from…」  
  判断：**部分符合**。美国在生成式AI和芯片设计上仍处领先，同时中国开源模型追赶；是竞争加剧而非已经失去领导权  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/CHIPS_and_Science_Act>
- **#69** 「if the host countries cannot repay China’s generous loans, China will gain direct control of the ports and oth…」  
  判断：**部分符合**。汉班托塔港99年租约是标志性案例，但交接发生在出版前；出版后没有同等清晰的新“收港”高潮  
  来源：<https://en.wikipedia.org/wiki/Hambantota_International_Port>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>
- **#71** 「It might remain a cold war without a hot war」  
  判断：**部分符合**。中美之间没有直接热战，符合“可能仍是冷战”；但伊以在2025–2026年爆发热战，全球并不平静  
  来源：<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#73** 「China will advise clients to replace dollars with renminbi as their reserve currency」  
  判断：**部分符合**。人民币结算和原油合约在推广，符合制度准备；但人民币仍是第五大交易货币，归档证据不能说明客户已把美元储备替换为人民币。  
  来源：<https://en.wikipedia.org/wiki/Petroyuan>；<https://en.wikipedia.org/wiki/Renminbi>；<https://en.wikipedia.org/wiki/Dedollarisation>
- **#74** 「New cooperation and development agreements between China and its clients will forge partnerships that increasi…」  
  判断：**部分符合**。一带一路和对俄贸易等平行网络在延续，但发达工业经济体仍深度参与对华贸易，谈不上已在打造“日益孤立”它们的伙伴关系。  
  来源：<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/China%E2%80%93Russia_relations>；<https://en.wikipedia.org/wiki/Huawei>
- **#76** 「NATO may become a tool to contain the rising power of China」  
  判断：**部分符合**。美英澳AUKUS和美国对华竞争政策在出版后延续，但已归档的北约摘要几乎没有对华议程，不能把北约本身写成已经变成遏制中国的工具。  
  来源：<https://en.wikipedia.org/wiki/NATO>；<https://en.wikipedia.org/wiki/AUKUS>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#78** 「It is likely to continue missile launches and other provocations that will at some point precipitate an outrig…」  
  判断：**部分符合**。朝鲜继续发展核导能力，试射与挑衅的方向有支持；“在某个时点引发直接军事对抗”在窗口内并未发生，复合判断只部分成立。  
  来源：<https://en.wikipedia.org/wiki/North_Korea_and_weapons_of_mass_destruction>
- **#88** 「Emerging markets including China and India, the world’s two most populous countries, expect to increase emissi…」  
  判断：**部分符合**。印度等新兴市场排放仍与增长相关；但中国排放可能已在2024或2025年达峰，与“中国也将再升十年”不完全一致  
  来源：<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_China>；<https://en.wikipedia.org/wiki/Climate_change_in_India>
- **#91** 「If current policies raise the price for fossil fuels we may end up with “greenflation.”」  
  判断：**部分符合**。2022年能源价格大涨曾带有转型和供给冲击色彩；此后价格回落，绿色通胀并非持续主线  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#94** 「Hurricanes will increase in number and frequency」  
  判断：**部分符合**。2024年大西洋季异常活跃且损失极高，2025年出现多个五级飓风但命名风暴接近常年、登陆美国飓风为零，频率并非单边上升  
  来源：<https://en.wikipedia.org/wiki/2024_Atlantic_hurricane_season>；<https://en.wikipedia.org/wiki/2025_Atlantic_hurricane_season>；<https://en.wikipedia.org/wiki/Climate_change>
- **#95** 「the inevitable result will be another asset bubble that is building up dangerously」  
  判断：**部分符合**。AI相关资产和风险资产在2023–2026年大幅上涨并伴随泡沫讨论，同时也经历了2022年熊市和2023年银行调整，并非单一、尚未破裂的泡沫  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>
- **#97** 「Everything points toward a coming Great Stagflationary Debt Crisis」  
  判断：**部分符合**。债务压力和一次通胀冲击确实出现，但滞胀债务危机作为全局事件并未在窗口内落地，美国还实现了软着陆  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#98** 「High inflation, close to double digits, could eventually undermine a weakened dollar」  
  判断：**部分符合**。美国通胀一度接近或达到很高水平，随后回落；美元并未因这段通胀而崩溃，储备地位仍在  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/Dedollarisation>
- **#101** 「Unfolding megathreats and the rising tide of populism will partly decide the 2022 midterm elections in the Uni…」  
  判断：**部分符合**。通胀确实拖累执政党，共和党拿下众议院，说明经济不满起了作用；但“红潮”落空，堕胎议题等同样关键，并非主要由超级威胁/民粹决定  
  来源：<https://en.wikipedia.org/wiki/2022_United_States_elections>；<https://en.wikipedia.org/wiki/2022_United_States_House_of_Representatives_elections>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>
- **#105** 「Similar tensions will mount in the Baltics, Central and Eastern Europe, the Caucasus, and parts of Central Asi…」  
  判断：**部分符合**。俄乌战争使欧洲东部安全紧张上升，但已归档材料并未表明波罗的海、高加索和中亚（如哈萨克斯坦）同等加剧，区域预测只部分相符。  
  来源：<https://en.wikipedia.org/wiki/NATO>；<https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict>
- **#108** 「Energy prices will skyrocket as supplies dwindle, leaving large populations literally powerless」  
  判断：**部分符合**。2022年价格飙升符合机制，之后供应紧张缓解、价格回落，并未留下“大量人口陷入缺电”的全球常态  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/Price_of_oil>
- **#109** 「Even the cost of commodities necessary for renewable energy—like lithium and copper—will sharply rise as the p…」  
  判断：**部分符合**。能源危机阶段部分关键矿产价格曾大涨，但锂价随后大幅回落，并非随化石燃料同步持续飙升  
  来源：<https://en.wikipedia.org/wiki/2020s_energy_crisis>
- **#110** 「Paired with slowing productivity, the coming supply shocks will trigger stagflation」  
  判断：**部分符合**。2022年出现过供给冲击型通胀，但随后通胀回落、美国避免衰退，滞胀没有成为新的常态  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/2020s_energy_crisis>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#114** 「Over the next couple of decades, they will lead to a titanic collision of economic, financial, technological, …」  
  判断：**部分符合**。人工智能、冲突、气候和货币政治在窗口内确有交织，但“巨大碰撞/titanic collision”难以用已归档事实度量，只能记部分符合。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Dedollarisation>
- **#115** 「Their impact will shake our lives and upend the global order in ways no one today has ever experienced」  
  判断：**部分符合**。生成式人工智能和大规模直接地区战争带来了一些新的冲击，但“颠覆全球秩序”尚未被观察结果支持。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/Climate_change>

### 错误（1 条）

- **#30** 「Together with loose monetary and fiscal policies and staggering levels of debt, they will precipitate stagflat…」  
  判断：**错误**。通胀在2022年见顶后于2023年明显回落，美国避免衰退，并未出现比1970年代更糟的滞胀  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>

### 暂无法判断（28 条）

- **#4** 「a technological revolution that will displace more jobs in less time than any that has come before」  
  判断：**暂无法判断**。归档证据只说明生成式AI迅速扩散并重新点燃失业辩论，同时写明就业净影响仍有争议、大规模岗位消失尚未成为事实，不足以确认“将在更短时间内取代比以往更多岗位”这一方向。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/ChatGPT>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#5** 「without amazing luck, almost unprecedented economic growth, and unlikely global cooperation, this won’t end we…」  
  判断：**暂无法判断**。“结局不会好”过于笼统；窗口内虽有战争与通胀，归档材料既未显示全面灾变，也不能把通胀冲高后回落写成持续恶化的既定方向。  
  来源：<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/Deglobalization>
- **#10** 「The Mother of All Debt Crises may take place sometime during the current or next decade」  
  判断：**暂无法判断**。2023年银行风波和中国地产危机是严重压力，但还不能认定为全球“债务危机之母”；预测窗口延续至约2032年，终点未到  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Chinese_real_estate_crisis_(2020%E2%80%93present)>
- **#17** 「the paychecks of active workers will be more and more devoted to maintaining safety nets for the elderly」  
  判断：**暂无法判断**。归档的社保词条只给出信托基金耗尽时点，没有工薪税或在职工人负担份额的数据，无法确认“薪水将越来越多地用于养老保障”。  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#19** 「If young workers do not yet resent surrendering their futures in order to bankroll retirees, they eventually w…」  
  判断：**暂无法判断**。“最终会怨恨”缺乏可观察度量；已归档材料只有受托人报告，没有代际政治或态度证据。  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#20** 「The ratio slipped below 3 to 1 in 2009 and is headed toward 2 to 1 by 2030」  
  判断：**暂无法判断**。已归档摘要没有给出参保职工与受益人之比或其官方轨迹，不能仅凭耗尽时点认定正在走向2030年的2比1。  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#21** 「more retirees in the United States will swell Social Security rolls to 73 million beneficiaries」  
  判断：**暂无法判断**。已归档摘要没有7300万或最新受益人规模，无法确认该数量预测的方向是否成立。  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#23** 「Unfunded liabilities will balloon as more workers qualify for the safety net and political will falters」  
  判断：**暂无法判断**。已归档材料确认精算缺口仍在，但没有无资金准备负债规模上升的可绑定数字，不能把耗尽时点临近直接写成负债已经膨胀。  
  来源：<https://en.wikipedia.org/wiki/Social_Security_(United_States)>；<https://en.wikipedia.org/wiki/Social_Security_Trust_Fund>
- **#31** 「Rapid aging of populations will disrupt developed and emerging markets」  
  判断：**暂无法判断**。已归档的中国经济与美国社保摘要没有给出发达和新兴市场因快速老龄化而受冲击的直接证据。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Social_Security_(United_States)>
- **#39** 「In the worst case, crippling cyberattacks will increasingly damage growth」  
  判断：**暂无法判断**。原判定已承认公开证据不足以证明破坏性网络攻击正在日益损害增长；AI扩散词条也不能补上这一因果。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>
- **#48** 「Central bank digital currencies may cut banks out of the payment system that sustains them」  
  判断：**暂无法判断**。主要经济体的CBDC仍多处于试验或讨论，商业银行支付中介地位未被取代，预测尚未可判定  
  来源：<https://en.wikipedia.org/wiki/Federal_Reserve>
- **#55** 「A similar fate will increasingly hurt low- and semiskilled white collar service workers where virtual access c…」  
  判断：**暂无法判断**。归档证据只是生成式AI扩散和失业辩论，没有中低技能白领服务岗位已被远程或模型替代的职业数据，方向未被清楚确认。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#58** 「even nursing jobs for the elderly—previously thought as being available only to humans—may be soon replaced by…」  
  判断：**暂无法判断**。护理机器人仍属试点，“很快取代”在窗口内没有成为现实，也还看不到完成替代的清晰时点  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#59** 「Tomorrow, robots and drones will deliver goods to their destinations」  
  判断：**暂无法判断**。本条只绑定了人工智能热潮词条，该摘要并不涉及机器人或无人机配送，无法确认“货物将被机器人和无人机送达”。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>
- **#60** 「All this is why the AI revolution may be the first one that destroys overall jobs and wages」  
  判断：**暂无法判断**。归档材料写明就业净影响仍有争议；窗口内总体就业和工资也并未被摧毁，不能把“可能是第一场摧毁总体就业和工资的革命”记为已确认的方向。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#63** 「As people earn less, inequality will grow」  
  判断：**暂无法判断**。“收入下降因而不平等加剧”的完整链条没有被已归档宏观或分配数据坐实。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>
- **#64** 「If you are a low- or even medium-skilled blue- or white-collar worker, AI will eventually reduce your wages an…」  
  判断：**暂无法判断**。“最终将降低中低技能者工资并使其工作过时”仍属未兑现的终局判断，归档证据只是一般性辩论。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>
- **#66** 「Once China wields the world’s biggest economic club, as most experts predict it will before 2030」  
  判断：**暂无法判断**。至2026年中国仍为名义GDP第二；增长放缓使2030年前超越更不确定，但终点未到，不宜提前判错  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)>
- **#80** 「If China continues to grow and the United States stumbles, the United States will see its strategic advantages…」  
  判断：**暂无法判断**。前提并不完整：美国避免了衰退，中国增长放缓但仍增长，美国战略优势并未消失  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)>；<https://en.wikipedia.org/wiki/Soft_landing_(economics)>
- **#81** 「Even if weaker, China may become more aggressive toward Taiwan」  
  判断：**暂无法判断**。“即便变弱”的前提在窗口内并不成立；已归档的美台关系和对华政策摘要也没有给出对台姿态更强硬的直接证据。  
  来源：<https://en.wikipedia.org/wiki/Taiwan%E2%80%93United_States_relations>；<https://en.wikipedia.org/wiki/United_States_foreign_policy_toward_the_People%27s_Republic_of_China>
- **#85** 「Fifty years from now, coasts may be flooded, much of the south may be too hot for people to want to live there」  
  判断：**暂无法判断**。海平面上升和极端高温风险被广泛记录，但“五十年后”远超截止日，窗口内不能判定终点  
  来源：<https://en.wikipedia.org/wiki/Effects_of_climate_change>；<https://en.wikipedia.org/wiki/Climate_change>
- **#86** 「We should expect to see conflict and grinding poverty push migration to a scale never seen before」  
  判断：**暂无法判断**。气候移民词条是定义说明，没有全球总量或“前所未见”的比较，不能确认冲突与贫困已把移民规模推向历史新高。  
  来源：<https://en.wikipedia.org/wiki/Climate_migration>；<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict>
- **#93** 「Given current policies and actions the world is headed instead toward an average increase in temperature of 2.…」  
  判断：**暂无法判断**。已归档的气候变化与中美排放摘要没有给出“现行政策通向平均升温2.7℃”的路径评估，该数字不能从现有摘录中确认。  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_China>；<https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_the_United_States>
- **#96** 「This tsunami will hit the global economy in the next decade」  
  判断：**暂无法判断**。已有局部危机，但“下一个十年”的全局海啸尚未到来，窗口只覆盖时域的前半  
  来源：<https://en.wikipedia.org/wiki/2023_United_States_banking_crisis>；<https://en.wikipedia.org/wiki/Chinese_real_estate_crisis_(2020%E2%80%93present)>
- **#103** 「Technology will become autocracy’s handmaiden」  
  判断：**暂无法判断**。已归档的人工智能热潮和华为词条没有说明技术正在成为威权主义的帮手，方向缺乏直接证据。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Huawei>
- **#107** 「Zoonotic diseases will spawn pandemics and tax health care networks more than ever」  
  判断：**暂无法判断**。窗口内没有出现与新冠同等规模的新全球大流行病；已归档的气候和移民词条也不能支持“人畜共患病将更沉重地消耗卫生体系”。  
  来源：<https://en.wikipedia.org/wiki/Climate_change>；<https://en.wikipedia.org/wiki/Climate_migration>
- **#112** 「Between these two, unfortunately, the dystopian scenario looks much more likely」  
  判断：**暂无法判断**。“反乌托邦情景更可能”是相对而且笼统的判断；窗口内既有战争和气候压力，也有通胀回落，不能把相对可能性写成已确认的方向。  
  来源：<https://en.wikipedia.org/wiki/Twelve-Day_War>；<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://en.wikipedia.org/wiki/Deglobalization>；<https://en.wikipedia.org/wiki/AI_boom>
- **#113** 「In all likelihood, artificial intelligence will steal jobs for good」  
  判断：**暂无法判断**。归档材料写明宏观就业上“永久夺走岗位”尚未兑现，且净影响仍有争议，不能记趋势符合。  
  来源：<https://en.wikipedia.org/wiki/AI_boom>；<https://en.wikipedia.org/wiki/Technological_unemployment>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/roubini-megathreats-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/roubini-megathreats-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/roubini-megathreats-v5/audit/manual_review_2026-11-15.py`

## 说明

- 无日期的方向性判断按 2022-10 至 2026-11-15 窗口核验：方向已经发生则记正确，不降为趋势符合。
- 写明十年或更长终点、且窗口内只有持续方向证据的，记趋势符合。
- 条件未触发的（如“若美国踉跄而中国继续高速增长”）不计正误。
- 证据均为维基百科公开存档，附 sha256；data/evidence.jsonl 非空。

- 2026-11-16 QA 按 WORKER_BRIEF 第10条复核全部趋势符合：仅保留归档证据已清楚确认方向的条目；方向未被证据坐实、或原判定已承认“尚未兑现/证据不足”的，改为暂无法判断或部分符合。改判清单见 notes/roubini_qa_changes.json。

