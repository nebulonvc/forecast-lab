# 《公众舆论》（Public Opinion）：出版后预测人工核查

- 案例目录：`cases/lippmann-public-opinion-v5/`
- 出版日期：1922（英文原著；Gutenberg文本）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

逐块通读原始Gutenberg TXT；按3500/600分块并手写模型回答，确定性对齐、归属、历史筛选、重叠去重、ID均用/workspace/forecast-batch-a/repo的toolkit 85e6da1。实际联网来源是Exa search及contents存档抓取，不是WebSearch/WebFetch，不使用DeepSeek；PLAN/SELECT/ASSESS/SEMANTIC REVIEW由助手逐条完成，末轮未定均改变策略补查。40候选中38条resolvable进入核验；另2条中性转述为unclear不评分。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 38 条，剔除非预测 16 条，计入 **22 条预测**，其中 **15 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 4 |
| 趋势符合 | 0 |
| 部分符合 | 11 |
| 错误 | 0 |
| 暂无法判断 | 7 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **26.7%**（4/15） |
| 加权胜率 | **63.3%** |
| 错误率 | **0.0%**（0/15） |
| 未定占比（暂无法判断/预测） | 31.8%（7/22） |

## 总体评价

有声电影发展、专家权力增长、政策统计常规化及研究教学数据积累得到出版后材料支持；信息改善与公共判断之间仅有局部、条件性的经验支持。全知式自治、报纸的终局能力、终身记忆与审计独立等更强判断仍未定。大量制度思想实验不宜用后世相近制度计算胜负；零错误不代表全部论断正确。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（4 条）

- **#2** 「In the western world, however, during the last few centuries there has been an enormous increase in the volume…」  
  判断：**正确**。电影史研究明确记载英国、德国和法国转向有声长片制作，多语种长片也进入生产。有声电影确实成为出版后扩展叙事表达的媒介，早期技术试验不等于这种后来形成的产业媒介。  
  来源：<https://www.liverpooluniversitypress.co.uk/doi/10.3828/msmi.2018.7>；<https://publish.iupress.indiana.edu/read/the-birth-of-the-talkies/section/b6d8461d-7342-4352-8411-d7e0ca90db49>
- **#24** 「The idea that the expert is an ineffectual person because he lets others make the decisions is quite contrary …」  
  判断：**正确**。专业史明确描述经济学在整个世纪逐步取得设计、改造社会的合法权威，规划史也记录专家知识在新的治理结构中的赋权。对专家未来掌握更多权力这一未定期方向，出版后材料确认了主要结果。  
  来源：<https://sociology.berkeley.edu/sites/default/files/faculty/fourcade/AJSII.pdf>；<https://discovery.ucl.ac.uk/id/eprint/10087411/3/Hebbert_Planning%20Knowledge%20and%20Technocracy%202019%20final%20ms.pdf>；<https://www.annualreviews.org/content/journals/10.1146/annurev-polisci-033123-020420>
- **#36** 「Therefore, though here, as in most other matters, "education" is the supreme remedy, the value of this educati…」  
  判断：**正确**。政府统计史明确记载，出版后继续围绕具体实践问题设立统计单位，统计还被制度化用于宏观政策和公共资源分配。信息搜集成为决策的常规需要并再供社会科学使用，符合原句关于直接动因与后续用途的主要判断。  
  来源：<https://gwipp.gwu.edu/sites/g/files/zaxdzs6111/files/downloads/Reamer%20Testimony%20to%20Commission%20on%20Evidence-based%20Policymaking%2003-13-17.pdf>；<https://www.princeton.edu/~starr/articles/articles80-89/Starr_Sociology-of-Official-Statistics.pdf>
- **#37** 「there will accumulate a body of data which political science can turn into generalization, and build up for th…」  
  判断：**正确**。数据机构的历史和教学资料确认，出版后形成了持续积累、共享的社会政治数据资源，并实际用于研究和学生训练。独立的数据使用研究也发现学生是主要下载群体，原句所说可供政治科学概括和教学使用的数据已形成。  
  来源：<https://www.icpsr.umich.edu/sites/icpsr/about/history>；<https://wpvip.icpsr.umich.edu/icpsr/wp-content/uploads/sites/11/ICPSRbrochure-2025-FINAL-wcag.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC11086874/>

### 部分符合（11 条）

- **#1** 「Travel and trade, the mails, the wires, and radio, railroads, highways, ships, motor cars, and in the coming g…」  
  判断：**部分符合**。航空史记载，长途航线使殖民地居民更快读到伦敦报纸并维持政治文化联系，支持思想传播加速这一部分。航空客运仍相当有限，不能据这些局部网络确认其对整体思想传播已具有原句所称的极大影响。  
  来源：<https://www.ghi-dc.org/fileadmin/publications/Bulletin/bu69/GHI69fall_07FEA-Greiner_Fpp.pdf>；<https://www.tandfonline.com/doi/full/10.1080/17551820902742772>
- **#4** 「The Covenant of the League of Nations says, [Footnote: Article XIX.] for example, that "the character of the m…」  
  判断：**部分符合**。外交档案明确记载，阿拉伯方面因英国没有给出独立的确定日期而反对方案，并担心另一方能无限推迟建国。自治时间认识确实影响了这部分托管关系；现有材料不足以覆盖原句概括的全部托管双方关系及影响程度。  
  来源：<https://history.state.gov/historicaldocuments/frus1939v04/d794>；<https://history.state.gov/historicaldocuments/frus1939v04/d811>
- **#9** 「it is no daring prophecy to say that the knowledge of how to create consent will alter every political calcula…」  
  判断：**部分符合**。政治顾问史记载，科学民调、广播及经过测试的信息深刻改变了政治运作和行政权力关系，支持原句的一部分。说服实验也显示平均影响很小，不能据此证明一切政治计算和一切政治前提都已改变。  
  来源：<https://ebrary.net/96319/business_finance/emergent_profession_political_advice>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7467695/>
- **#10** 「But surely there is a still more momentous question, the question of how to validate our private versions of t…」  
  判断：**部分符合**。实验表明，将识别情绪操纵的训练与准确性提示相结合，可以改善对真假消息的辨别；单独识别操纵却未改善真实性判断。基于意见形成知识的自我监控有局部成效，但不能据此确认政治意见有效性已普遍而大幅提高。  
  来源：<https://www.nature.com/articles/s41562-024-02023-2>；<https://econtent.hogrefe.com/doi/full/10.1027/1016-9040/a000492>
- **#21** 「The only prospect which is not visionary is that each of us in his own sphere will act more and more on a real…」  
  判断：**部分符合**。专业史记录了经济学专家组织在战后向更多地区扩展，数据机构也扩大了研究与教育服务，支持更多专业人员这一分项。公众知识调查没有显示信息媒介革命带来相应的全面知识改善，故不能确认每个人都越来越依据现实图景行动。  
  来源：<https://sociology.berkeley.edu/sites/default/files/faculty/fourcade/AJSII.pdf>；<https://www.icpsr.umich.edu/sites/icpsr/about/history>；<https://www.pewresearch.org/politics/2007/04/15/public-knowledge-of-current-affairs-little-changed-by-news-and-information-revolutions/>
- **#23** 「The social scientist will acquire his dignity and his strength when he has worked out his method. He will do t…」  
  判断：**部分符合**。专业史记载经济学逐步取得塑造政策与社会的专业权威，技术工具也改变了决策所能使用的信息。这支持部分社会科学专业地位上升，但不同制度中影响强弱不一，不能由经济学这一门学科推成全部社会科学都靠方法发展获得同等尊严与力量。  
  来源：<https://sociology.berkeley.edu/sites/default/files/faculty/fourcade/AJSII.pdf>；<https://epberman.net/wp-content/uploads/2018/09/hirschman-and-berman-do-economists-make-policies.pdf>
- **#25** 「All governing agencies will tend to organize bodies of research and information, which will throw out tentacle…」  
  判断：**部分符合**。政府统计史记载出版后继续增设政策统计单位，经合组织也记录多国已形成长期及临时政策咨询机构。这支持设立与扩展的一部分，但部门之间的证据文化差异显著，不能据样本断言所有治理机构都会如此。  
  来源：<https://gwipp.gwu.edu/sites/g/files/zaxdzs6111/files/downloads/Reamer%20Testimony%20to%20Commission%20on%20Evidence-based%20Policymaking%2003-13-17.pdf>；<https://www.oecd.org/content/dam/oecd/en/publications/reports/2017/11/policy-advisory-systems_g1g8362d/9789264283664-en.pdf>；<http://ideas.repec.org/a/oup/polsoc/v43y2024i4p494-520..html>
- **#31** 「But enough has been done to demonstrate, I think, that unseen environments can be reported effectively, that t…」  
  判断：**部分符合**。有组织的公共审议实验记录了不同立场参与者态度去极化；综述也确认，合适的信息和讨论程序能改善议题理解与判断。这只支持应对不可见现实的部分能力，不足以证明偏见中立的报道前提普遍实现，更未证明自治的核心困难已整体克服。  
  来源：<https://www.cambridge.org/core/journals/american-political-science-review/article/is-deliberation-an-antidote-to-extreme-partisan-polarization-reflections-on-america-in-one-room/5DEFB6F8D944ECDE77A5E80C3346D4DE>；<https://www.annualreviews.org/content/journals/10.1146/annurev-lawsocsci-110316-113639>
- **#32** 「It is possible to-day, it will become more possible when more labor has gone into it, to reduce the discrepanc…」  
  判断：**部分符合**。研究把识别操纵的训练与准确性提示结合后，改善了对真实与虚假消息的辨别，证实缩小部分认知与现实差距的能力已有进展。但训练或提示单独使用并无相同结果，且不能把有限消息实验推广为对所有不可见环境的认识都改善。  
  来源：<https://www.nature.com/articles/s41562-024-02023-2>；<https://econtent.hogrefe.com/doi/full/10.1027/1016-9040/a000492>
- **#33** 「But as one party to a dispute, as a committeeman in a legislature, as an officer in government, business, or a…」  
  判断：**部分符合**。政策分析史明确指出，政治人物的专业需要和政府事务复杂化推动了对信息的需求，支持越来越欢迎议题报告的一部分。综述仍发现研究难以找到政策受众，且没有同口径覆盖企业、工会及各类争端当事方的欢迎程度变化。  
  来源：<https://www.scielo.org.mx/scielo.php?pid=S0185-013X2015000200540&script=sci_abstract&tlng=en>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC3909454/>
- **#35** 「The effect of naming, the effect, that is, of saying that the labor groups C and M, but not X, are underpaid, …」  
  判断：**部分符合**。包含识别自身偏见和运用减少偏见策略的训练曾降低特定种族隐性偏见，支持重新教育的一部分作用。综合研究指出持久效果和发表偏差仍有疑问，且识别操纵本身未必提高真实性判断，不能据此确认公共意见整体贴近环境或庞大的刻板化机制已被消解。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC3603687/>；<https://www.annualreviews.org/content/journals/10.1146/annurev-psych-071620-030619>；<https://www.nature.com/articles/s41562-024-02023-2>

### 暂无法判断（7 条）

- **#3** 「The shadowy idea becomes vivid; your hazy notion, let us say, of the Ku Klux Klan, thanks to Mr. Griffiths, ta…」  
  判断：**暂无法判断**。研究记录了影片对地方仇恨行为及三K党支持的持久影响，也讨论观众接受的差异。这些不是对原先特定观众终身听名就浮现白衣骑手的个体记忆追踪，关键事实仍缺失。  
  来源：<https://scholar.harvard.edu/files/ang/files/ang_birthofanation_july2022.pdf>；<https://researchnow.flinders.edu.au/en/publications/blackface-disguise-and-invisibility-in-the-reception-of-the-birth/>
- **#11** 「Therefore, unless there is in the community at large a growing conviction that prejudice and intuition are not…」  
  判断：**暂无法判断**。政策研究和事实核查研究显示，证据信任、机构可信度与支持或使用之间有关联。材料没有检验整个社会越来越承认偏见和直觉不足，是否是建立现实政治意见获得支持的必要条件。  
  来源：<https://www.oecd.org/en/publications/building-capacity-for-evidence-informed-policy-making_86331250-en/full-report/component-4.html>；<https://econtent.hogrefe.com/doi/full/10.1027/1864-1105/a000484>
- **#20** 「There is no prospect, in any time which we can conceive, that the whole invisible environment will be so clear…」  
  判断：**暂无法判断**。现有政治知识研究确认现实中的知识限制，也指出知识测验与实际决策能力不能简单等同。这既不能证明任何可设想未来都不可能达到原句的状态，也没有出现覆盖全体人和全部政府事务的反例。  
  来源：<https://ciaotest.cc.columbia.edu/olj/cr/cr_v15_12_wem01.pdf>；<https://www.arthurlupia.com/_files/ugd/fa8393_7310894868464aa0a63d20c6213e5fc3.pdf>
- **#22** 「If the newspapers, then, are to be charged with the duty of translating the whole public life of mankind, so t…」  
  判断：**暂无法判断**。报纸研究既有未发现政治知识改善的实验，也有优质报纸与真实知识相关的结果。它们都不检验报纸在任何未来能否让每个成人对每个议题形成意见，缺少原句全称终局的决定性证据。  
  来源：<https://doi.org/10.1257/app.1.2.35>；<https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1251379/full>
- **#26** 「But the experts will remain human beings. They will enjoy power, and their temptation will be to appoint thems…」  
  判断：**暂无法判断**。官方调查确认情报表达不充分、分析与政策之间需要恰当分离，也明确没有证据证明有关材料被不当植入或受到不当政治改写。尚不能由这些事实认定职能界定不清的专家自己筛选事实并吸收实质决策权、成为所预言的官僚体系。  
  来源：<https://www.globalsecurity.org/intell/library/congress/2004_rpt/iraq-wmd_intell_09jul2004_conclusions.htm>；<https://www.gov.uk/government/speeches/pm-statement-on-the-iraq-inquiry-6-july-2016>；<https://www.oecd.org/content/dam/oecd/en/publications/reports/2017/11/policy-advisory-systems_g1g8362d/9789264283664-en.pdf>
- **#27** 「In industry, the auditors, accountants, and inspectors should be independent of the manager, the superintenden…」  
  判断：**暂无法判断**。监管资料强调公共看门人职责和独立性，但同一制度仍把审计人最终责任置于股东，改革文献还有把控制权交给股东的建议。缺少足够证据表明社会已经认可原句更强的独立于董事会和股东这一必要条件，不能用独立于管理层替代。  
  来源：<https://pcaobus.org/news-events/speeches/speech-detail/auditor-independence-and-the-role-of-the-pcaob-in-investor-protection_616>；<https://www.osc.ca/en/securities-law/instruments-rules-policies/5/52-110/unofficial-consolidation-companion-policy-52-110cp-audit-committees>；<https://digitalcommons.law.uw.edu/wlr/vol81/iss3/3/>
- **#34** 「The private citizen, beset by partisan appeals for the loan of his Public Opinion, will soon see, perhaps, tha…」  
  判断：**暂无法判断**。政治广告研究发现客观说服知识仍然低，犬儒和广告怀疑也不等于公民认识到党派动员侮辱自己的证据意识。原句的不久没有明确长度，现有材料不能还原早期公民是否发生了所说的普遍认识转变。  
  来源：<https://politicaladvertisingliteracy.web.illinois.edu/wp-content/uploads/2022/07/Nelson-Ham-Haley-2021.pdf>；<https://academic.oup.com/joc/article-abstract/63/2/287/4085984>；<https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0295329>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 5 | And so collapses the Marxian remedy for … | mechanism | 这是为反驳公有制自动产生共同利益而设置的认识论论证，解释群体如何仍可能分层，不是对特定出版后阶级形成事件的预测。 |
| 6 | And under socialism, though you removed … | hypothetical | 句子先设定社会主义已经消除全部绝对利益冲突，再说明信息不完全仍有冲突，是理论假设的机制推演；没有断言该前提将在现实发生。 |
| 7 | A socialist state will not be able to di… | mechanism | 这里论证教育、道德和自由学术不会因财产制度改变而失去必要性，并非预言社会主义国家实际允许或保留何种具体制度。 |
| 8 | That is why you can breakup a particular… | mechanism | 上下文以特权的相对性及无法完全均一解释任何有凝聚力群体都会产生组织机器，是一般组织机制，不是特指某城市党机器改革后的出版后事件。 |
| 12 | They do expect, and of course quite righ… | hypothetical | 收入完全平等是想象工团社会中的理论前提，这句话认可条件下关系改变的机制，并未预测实际将实现收入平等或随后某一现实事件。 |
| 13 | Representatives will aim to carry out th… | hypothetical | 作者明确让读者想象工团社会已经存在，以此检验代表机制，永久交易或车间混乱是这一制度思想实验的结果，非现实未来事件预言。 |
| 14 | For while the worker in the shop can hav… | mechanism | 这是从车间的有限经验推论外部世界容易出错的认识机制，置于同一工团制度思想实验；不是对现实工人判断正确率的出版后统计预测。 |
| 15 | As a matter of experience, the represent… | hypothetical | 句子继续同一未断言会成立的工团社会思想实验，用代表可能遇不到明确意愿来反驳理论，不能把既有工会经验计成后来兑现实绩。 |
| 16 | And since the communes of the guild soci… | hypothetical | 激烈选举是设想赋予公社广泛经济权力后的理论反驳，作者没有预测现实将建立该完整工团制度。 |
| 17 | It is not at all unlikely that certain f… | hypothetical | 此处仍在设想社会主义如何界定工团职能的路径，工会成为中心是其中一种可能机制，非对某个现实工会取得政权的未来判断。 |
| 18 | fairly soon one would find, I think, tha… | hypothetical | 激进派要求强公社的判断依赖正在设想的工团社会和前述过渡斗争，属于该制度思想实验的内部推演，不是断言实际将发生的运动进程。 |
| 19 | If there is no settled scheme of functio… | mechanism | 各工团会从不同角度看同一方案，是反驳理论预设和谐的意见形成机制，未提出独立的现实未来变化。 |
| 28 | since operation of the Department would … | normative | 这是各部门设置独立情报局的改革方案中可能有利的制度效果，作者随后明确说具体建议只是例示，未作实际采用或过细立法减少的未来预言。 |
| 29 | It would be idle to deny that such a net… | normative | 本句为所设计的情报局网络辩护，说明方案为何应当简化生活；属于作者明确限定为例示的改革设计，不是实际将建立该网络并简化生活的预测。 |
| 30 | The employment of an intelligence system… | normative | 单位结果人员下降是上述知识组织改革设计的预期效率理由，而非对一个已实施或即将实施制度的现实绩效预测；不能拿计算机生产率替代方案兑现。 |
| 38 | Until reason is subtle and particular, t… | mechanism | 结尾阐释理性成熟速度与即时政治行动的结构张力，机智、力量和信念的必要性属于一般政治认识机制，没有可独立识别的出版后变化。 |

## 文件

- 本文：`cases/lippmann-public-opinion-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/lippmann-public-opinion-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/lippmann-public-opinion-v5/audit/manual_review_2026-11-15.py`
## 质量风险与敏感性

- Gutenberg TXT与队列sha256一致，CRLF原样保留；早期续跑曾按通用read_text换行归一化生成草稿，已废止。最终重新按原字节解码生成186块，逐块通读并精确校验47个原始引句；只打包哈希/条目覆盖证据，不打包全文、分块正文和请求。
- 原代码排除1条historical、去除6个重叠项，40 candidates/38 resolvable；2个reported/unclear不评分。历史屏幕排除项涉及科学与行动互惠的未来句，但引文包含旧脚注而触发历史筛选；原提案和原因保留，未改过滤或暗加分母。38项中16项经体裁复核为机制、规范方案或工团制度思想实验，因此最终仅22项预测；本书主要是认识论、历史分析和制度设计，密度低于典型预测书，仍有体裁边界与漏收风险，不为密度凑数。
- 正式只按claims_from_results重叠规则去重，未加主题或语义duplicate。同类独立句的相关性会放大条目级胜率：相关近义组各留最早句为20预测/13可判，正3/趋0/部10/错0/未7，strict23.08%、weighted61.54%；更宽主题组各留最早句为13预测/6可判，正1/趋0/部5/错0/未7，strict16.67%、weighted58.33%。两组错误率均0，但不是独立抽样的准确率；分组见audit/sensitivity.json。
- 全称终局否定#20/#22一律未定，不把当前不足当作永远不可能；#3的地区长期仇恨效应不替代个体终身视觉记忆；#34的soon不被拉长至今天补命中；#27的管理层独立不替代董事会和股东独立。
- #10/#32/#35采用实际真假辨别或偏见分项的实验材料，仅判部分，不把分享意向直接改成信念准确性；#31的去极化不等于真理或整体自治成功。#24/#36虽主结果符合，专业权力的定性范围和资料搜集的多种动机仍有解释空间。
- 研究实际为Exa search/contents，共94个正反查询；9项改变策略再查，7个最终未定都完成二轮。每项最多3个选择来源，跨条复用在SELECT明示；51个公开来源存档与51条evidence逐一sha256核验。部分正文截断、发布元数据缺失，非阻断警告保留；不声称HTTP逐站独立验证，也不用截断的LA Times来源评分。
- 语义复核由同一助手完成，不声称独立人类或另一模型验收。原文引用均逐字连续；context一律空。toolkit来自85e6da1，manual_report实际使用canonical版，md5 682248fa9f6c63e3492a559ccac12761。
