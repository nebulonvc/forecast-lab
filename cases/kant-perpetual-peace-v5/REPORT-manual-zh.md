# 伊曼努尔·康德《永久和平论》（Perpetual Peace: A Philosophical Essay，1795）：出版后预测人工核查

- 案例目录：`cases/kant-perpetual-peace-v5/`
- 出版日期：康德《永久和平论》（Zum ewigen Frieden）于 **1795** 年在柯尼斯堡出版。所用 TXT 为 Project Gutenberg eBook #50922，Mary Campbell Smith 英译本（第一版 1903，1917 年第三次印行）。TXT sha256 `832e24a28acf492d90c0e13d5f3dff9f540a6aefdfc1514f7340b03451f5babb`（349,820 字节，已与队列及 Gutenberg `cache/epub/50922/pg50922.txt` 逐字节核对一致）。观察窗口按康德原著 1795 年起算，至 2026-11-15。TXT 不入库。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 101 块（3500 字符、600 字符上下文），助手逐块通读康德正文，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（前后附文块回答为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 15 条候选、其中 14 条可核验。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索，只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 14 条，剔除非预测 0 条，计入 **14 条预测**，其中 **10 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 1 |
| 趋势符合 | 3 |
| 部分符合 | 6 |
| 错误 | 0 |
| 暂无法判断 | 4 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **10.0%**（1/10） |
| 加权胜率 | **62.5%** |
| 错误率 | **0.0%**（0/10） |
| 未定占比（暂无法判断/预测） | 28.6%（4/14） |

## 总体评价

这是一部哲学论文，可核验的未来判断并不多。101 块中有 14 条可核验预测。可判定的 10 条中，1 条正确（不可指望哲学家为王），3 条趋势符合（共和制促进和平、和平联邦扩展、世界公民法秩序靠近），6 条部分符合（止战联盟、西伯利亚木材贸易、语言宗教与和平、商业精神、理性随文化增长、渐近永久和平），0 条错误。掌握恶的原则、法权取得最高地位、自然保证永久和平将会到来、恶人变少等 4 条因缺少决定性度量或证据争议，判为暂无法判断。初步条款中的“应当”条文按规范性主张未计为预测。趋势符合按严格口径使用。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（1 条）

- **#11** 「That kings should philosophise, or philosophers become kings, is not to be expected.」  
  判断：**正确**。窗口内并未形成哲学家为王或君主普遍哲思的政制模式。杰斐逊、哈维尔等偶有被称作“哲学家政治家”的人物，但连评述也承认这只是罕见例外，不能构成对“不可指望”这一否定性判断的推翻。  
  来源：<https://www.staugustine.com/story/opinion/2011/12/25/2011-12-24-2/16187289007/>；<https://plato.stanford.edu/entries/jefferson/>

### 趋势符合（3 条）

- **#1** 「has also the prospect of attaining the desired result, namely, perpetual peace.」  
  判断：**趋势符合**。共和制在出版后大幅扩展，且大量实证研究发现“联合民主”对国家间军事冲突有抑制作用。但永久和平并未到来：民主国家仍频繁参与战争（含殖民战争、对非民主国家的干涉）。方向成立，终点未到，记趋势符合。  
  来源：<https://doi.org/10.1080/03050629308434806>；<https://www.files.ethz.ch/isn/38066/democraticjihadapril2007.pdf>
- **#3** 「this idea of federation which is to extend gradually over all states and so lead to perpetual peace」  
  判断：**趋势符合**。联合国会员从1945年51国增至目前193个会员国，几乎覆盖全部主权国家，联邦式国际组织确实在扩展。但它并非康德意义上结束战争的自由国家联盟，战后战争仍持续发生。方向成立，终点未到。  
  来源：<https://www.un.org/en/about-us/growth-in-un-membership>；<https://unacov.uk/wars-since-un-was-founded/>
- **#5** 「the human race may be brought nearer the realisation of a cosmopolitan constitution.」  
  判断：**趋势符合**。1945年后国际人权法、国际刑事法院和多边贸易法律体系使陌生人往来更多地处于公法之下，人类确实更接近某种世界公民法秩序。但执行力弱，许多国家拒绝接受国际刑事法院管辖，完整的世界公民宪法并未实现。方向成立，终点未到。  
  来源：<https://www.un.org/en/chronicle/article/international-human-rights-law-short-history>；<https://www.otago.ac.nz/__data/assets/pdf_file/0020/331454/a-force-to-be-reckoned-with-the-international-criminal-court-and-the-problem-of-enforcement-734259.pdf>

### 部分符合（6 条）

- **#4** 「a federation averting war, maintaining its ground and ever extending over the world may stop the current of th…」  
  判断：**部分符合**。欧洲一体化后成员国之间出现了持久的“长和平”，与“止战联盟自我维持并扩展”部分相符。但联合国未能阻止包括2022年俄罗斯入侵乌克兰在内的多场战争，战争倾向并未被整体止住。故为部分符合。  
  来源：<https://www.cambridge.org/core/journals/european-review/article/abs/has-europe-solved-the-problem-of-war-explaining-the-long-peace-of-the-post1945-era/552BB1FA801DE63C4E2B40DE888115D0>；<https://news.un.org/en/story/2022/04/1115592>
- **#6** 「the inhabitants of the shores of the River Obi, the Yenisei, the Lena will supply them with it through trade」  
  判断：**部分符合**。叶尼塞河畔伊加尔卡自1929年起成为西伯利亚木材经北冰洋航线出口的港口，鄂毕—叶尼塞流域的木材确曾北运。但这主要是国家主导的出口与流放式运输，并非康德所说北极沿岸居民以畜产交换木材的常规贸易；部分木材还以漂流木形式出现在北极海岸。故只部分成立。  
  来源：<https://en.wikipedia.org/wiki/Igarka>；<https://www.science.org/content/article/soviet-era-timber-litters-arctic-shores>
- **#8** 「with the growth of culture and the gradual advance of men to greater unanimity of principle, they lead to conc…」  
  判断：**部分符合**。1795年后没有出现持久的世界君主国或普遍帝国，这一面成立。但语言与宗教差异并未随着文化增长而普遍导向和平：南斯拉夫解体、卢旺达、阿以冲突等显示仇恨与战争借口仍然存在。故为部分符合。  
  来源：<https://ehne.fr/en/encyclopedia/themes/humanism-enlightenment/europe-wars-religion/europe-between-religious-war-and-peace>；<https://www.polsoz.fu-berlin.de/polwiss/forschung/international/frieden/publikationen1/warlist-1_3-2008.pdf>
- **#9** 「The commercial spirit cannot co-exist with war, and sooner or later it takes possession of every nation.」  
  判断：**部分符合**。几乎所有国家都已进入国际贸易，商业精神“占据每个民族”这一面大致成立。但商业与战争并非不能共存：第一次世界大战前贸易高度相互依赖仍爆发大战，2022年俄乌战争也打破了经济联系必然止战的假设。故为部分符合。  
  来源：<https://ourworldindata.org/trade-and-globalization>；<https://www.nytimes.com/2022/03/04/business/economy/ukraine-russia-global-economy.html>
- **#13** 「human reason, fitted for the practical realisation of ideas of right according to that principle, grows contin…」  
  判断：**部分符合**。全球识字率从1820年约十分之一升至当代大部分人口识字，教育与科学研究亦大幅扩张，“文化前进、理性能力增长”这一面成立。但20世纪极权与以现代理性组织起来的大屠杀表明，实现“法权理念”的适切性并非持续单向上升。故为部分符合。  
  来源：<https://ourworldindata.org/literacy>；<https://isi.org/what-went-wrong-in-europebr-a-reflection-on-western-modernity/>
- **#14** 「the periods in which a given advance takes place towards the realisation of the ideal of perpetual peace will,…」  
  判断：**部分符合**。海牙和会（1899、1907）、国际联盟与联合国等和平制度确有推进，人类在制度上比1795年更接近和平理想。但主要战争间隔并未单调缩短（拿破仑战争后的相对长和平之后是两次世界大战），近年冲突死亡亦有回升，不能说已稳定地“越来越接近”且间隔越来越短。故为部分符合。  
  来源：<https://www.ungeneva.org/en/about/league-of-nations/background>；<https://ourworldindata.org/war-and-peace-long-run>

### 暂无法判断（4 条）

- **#2** 「he will in time gain the mastery over the evil principle in his nature」  
  判断：**暂无法判断**。人际暴力在部分长期序列中下降，但20世纪两次世界大战与大规模种族灭绝造成数千万平民死亡。所谓“掌握恶的原则”缺少可检验的决定性度量，无法据此确认或否定。  
  来源：<https://ourworldindata.org/data-insights/homicide-rates-have-declined-dramatically-over-the-centuries>；<https://blogs.lse.ac.uk/europpblog/2025/01/30/dark-figures-innocent-bystanders-the-civilian-victims-of-the-two-world-wars/>
- **#7** 「the irresistible will of nature that right shall at last get the supremacy.」  
  判断：**暂无法判断**。战后各国宪法权利条款与法治指数显示“法权”制度有过扩散，但2010年代以来威权回潮、强权政治冲击国际法，“法权终于取得最高地位”既无清晰终点，也无决定性事实可确认或否定。  
  来源：<https://worldjusticeproject.org/sites/default/files/documents/WJPIndex2025.pdf>；<https://freedomhouse.org/article/new-report-authoritarian-rule-challenging-democracy-dominant-global-model>
- **#10** 「nature guarantees the coming of perpetual peace, through the natural course of human propensities」  
  判断：**暂无法判断**。永久和平并未到来。战后大国间战争减少的说法与近年乌克兰、加沙、苏丹等冲突并存，文献对“战争下降”亦有统计争议。自然“保证永久和平将会到来”既未兑现为已实现的结果，也缺少足够清晰、无争议的趋证据，不宜判为趋势符合。  
  来源：<https://stevenpinker.com/files/pinker/files/the_decline_of_war_and_conceptions_of_human_nature_by_s_pinker.pdf>；<https://www.scielo.org.za/pdf/phronimon/v25n1/06.pdf>
- **#12** 「The world will certainly not perish by any means, because the number of wicked people in it is becoming fewer.」  
  判断：**暂无法判断**。部分地区长期杀人率下降、酷刑与公开残暴习俗减少，但“恶人数量变少”没有可操作的计数标准；20世纪大规模杀戮也使简单的道德进步叙事难以成立。缺少决定性事实。  
  来源：<https://ourworldindata.org/data-insights/homicide-rates-have-declined-dramatically-over-the-centuries>；<https://www.sciencefocus.com/science/less-violent-world-peace>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/kant-perpetual-peace-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/kant-perpetual-peace-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/kant-perpetual-peace-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（14 条可核验 / 101 块 ≈ 0.14）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。本书以法权哲学和规范性条款为主，初步条款中的“不得/应当”视为规范而非预测；译者导论与拉塔序言按前后附文排除。未为提高数量而放宽标准。
- 第 6 条候选（北极漂流木将随文明进步而中断）因引文落在脚注的引号问句内，被仓库规则降为 unclear，不计入可核验，也不进入计分。
- 趋势符合只在存档证据明确证实方向、且明确终点尚未到达时使用。无明确期限、又缺少决定性度量的长期判断判为暂无法判断。
- 证据以独立第三方为主（Our World in Data、联合国、ETH Zurich、Cambridge、IMF/贸易数据、科学期刊等）。
- `data/claims.jsonl`、`output/txt_import/claims_proposals.jsonl` 及评估快照中的 `context` 字段已清空。

