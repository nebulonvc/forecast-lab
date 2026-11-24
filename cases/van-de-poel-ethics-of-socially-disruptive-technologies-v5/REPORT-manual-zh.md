# van de Poel等《Ethics of Socially Disruptive Technologies: An Introduction》（2023）：出版后预测人工核查

- 案例目录：`cases/van-de-poel-ethics-of-socially-disruptive-technologies-v5/`
- 出版日期：2023-09-05
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

原PDF与队列SHA256完全相同，pdftotext -enc UTF-8默认布局得到391316字符TXT；113/113个3500字符body依次完整阅读（含脚注、参考文献、索引及出版广告），非关键词选句，无OCR。手写100条，原validate_chunk_predictions全部exact对齐、无拒绝；原claims_from_results自动historical排除7、重叠去重4，保留89候选（45resolvable、44unclear）。扩充SAI、化石企业、Ubuntu等短指代为原TXT连续quote，书目旧年份随扩引触发7项原historical筛选，存在误杀未来判断的已知限制，未修改分类器或人为恢复。txt-00059一条SAI连续扩引向前跨body起点213字符，仍处原600字符context范围，原代码标in_body=true；此为补主体支持的跨块引文而非拼接，所有位置均在原TXT逐字核对。44项原unclear逐项记录归属或不可核验方向的边界，未把其冒作已判预测；下文45是resolvable核验子集，非全书候选数。未进行人工语义去重，ASSESS duplicate为0。
每项先写scope及正反各1查询，首轮90次全部成功；第二轮39项各改变策略实际仅执行1条新查询（不是每项两条），包括针对条件是否满足、出版后部署及缺失结果指标的补查，共129次成功查询，无第三轮。SELECT每项最多8URL且仅来自真实返回，103个URL全部存档、SHA256记录于evidence，135条逐源注释均定位实际存档完整句子。读取返回与存档可见段落后由助手写判定、限制与六维复核；组装脚本只辅助结构和引句定位，不以脚本默认标签或自动pass代替语义判断，未用DeepSeek。Exa contents通常截至12000字符，Guardian仅1000字符开头，未抓部分不用；已选Repórter Brasil公开PDF另用curl下载并pdftotext完整转换。
不将气候模型、普通生物质能源或动物人工子宫实验当作相应人类/地球尺度技术已经部署；不把出版前实验因论文后来发表而当出版后验证。平台主权化、机器人模仿与尊重需求等虽有相关研究，因对象、时序或强度指标不对应仍记未定。5项正确、1项趋势、2项部分、0项错误、37项未定；decidable仅8，主题相关且条件句多，比例不代表独立预测技巧。未定各有具名缺口并完成第二轮。
全部context及派生context清空；113份全文plans与341项请求/响应/checkpoint等缓存仅保留worker本地，case/bundle不含全书。带认证回调查询的1个未选URL仅在交付检索记录中移除查询参数，原始缓存留worker私有；实际选源URL不变。来源用干净稳定URL，不复述先前临时签名下载地址。

抽取阶段与核验子集的分母分别列出，以下标准流程不是另一次筛选：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

原代码保留89条候选，44条原unclear不进入核验；45条resolvable全部计入 **45 条预测**，其中 **8 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 5 |
| 趋势符合 | 1 |
| 部分符合 | 2 |
| 错误 | 0 |
| 暂无法判断 | 37 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **62.5%**（5/8） |
| 加权胜率 | **84.4%** |
| 错误率 | **0.0%**（0/8） |
| 未定占比（暂无法判断/预测） | 82.2%（37/45） |

## 总体评价

近期伦理导论多讨论尚未实现技术的条件风险，因此37/45暂无法判断。已可观察的算法、单边实验、生物燃料劳动危害等仅按实际范围核对；两项部分符合保留政策阶段与私益策略的限定，技术展示仅支持一项趋向。8项可判定样本很小且相关，不据此宣称全书预测能力。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（5 条）

- **#2** 「Changing the algorithm defining users’ information visualization may limit social media’s polarization effect.」  
  判断：**正确**。2025年Science报告对2024年美国大选前1256名X用户的预注册实验：降低反民主及党派敌意内容排序会使对外党感情更温和，变化超过0—100温度计上的2度。出版前2020年Facebook实验未见极化改变，但不推翻新实验对“可能减弱”这一方向的支持。  
  来源：<https://arxiv.org/html/2305.16941v5>；<https://www.science.org/doi/10.1126/science.abp9364>；<https://www.science.org/doi/10.1126/science.adu5584>；<https://theconversation.com/down-ranking-polarizing-content-lowers-emotional-temperature-on-social-media-new-research-271071>
- **#4** 「However, one challenge to this solution is that digital infrastructures cross national borders, connecting geo…」  
  判断：**正确**。2025年摩尔多瓦选举分析指出本国法律只适用于有本地法律实体的平台，而Meta、Google和TikTok均无此实体，境外审核使大量传播不受同样国内约束。这是在原跨境前提下出现监管失灵风险的具体实例；DSA合作机制不意味着每种民主监管必然无效。  
  来源：<https://theconversation.com/digital-imperialism-how-us-social-media-firms-are-using-american-law-to-challenge-global-tech-regulation-252116>；<https://www.justsecurity.org/123410/tech-platforms-russia-moldova-eu/>；<https://utrechtlawreview.org/articles/10.36633/ulr.1074>
- **#12** 「On the technical side, there is likely to be increased convergence between social robotics and other developme…」  
  判断：**正确**。2025年研究把LLM集成到人形机器人，并开展7位老年人在家探索及43位年轻人初步研究；TIAGo Head同年报告LLM对话集成。商业照护软件的幻觉案例也是实际融合的反面证据，故融合增强方向成立。  
  来源：<https://www.mdpi.com/2076-3417/15/11/6377>；<https://doi.org/10.1109/ro-man63969.2025.11217595>；<https://link.springer.com/article/10.1007/s44206-025-00161-2>
- **#22** 「An individual country or even wealthy individual actor could unilaterally decide to carry out research or even…」  
  判断：**正确**。2025年EPA向Make Sunsets发出信息要求，转述公司自称已做124次以上释放活动；2024年IEEE报道也描述其在加州自行放飞二氧化硫气球。单个私人主体在缺乏共同决定下开展SAI尝试这一风险确实发生，禁令和监管反应没有抹去已发生行为。  
  来源：<https://www.epa.gov/newsreleases/epa-demands-answers-unregulated-geoengineering-start-launching-sulfur-dioxide-air>；<https://spectrum.ieee.org/solar-geoengineering-2669008650>；<https://srm360.org/article/srm-bans-and-moratoria/>
- **#24** 「A new rush for biofuels could allow for the exploitation of biomass producers in the Global South.」  
  判断：**正确**。IFC在2024年记载全球生物燃料需求近五年年增约6%，新一轮扩张有事实背景。巴西劳动部报道2025年9月救出108名为酒精厂供应甘蔗的工人，确认缺乏安全饮水、卫生设施等严重剥削条件；这支持全球南方生物质生产者受剥削的可能结果。  
  来源：<https://reporterbrasil.org.br/wp-content/uploads/2025/10/Monitor_Biocombustiveis_EN.pdf>；<https://www.ifc.org/en/pressroom/2024/ifc-and-the-italian-climate-fund-partner-with-eni-to-support-biofuel-production-farmers-in-kenya>；<https://www.gov.br/trabalho-e-emprego/pt-br/noticias-e-conteudo/2025/outubro/forca-tarefa-resgata-108-trabalhadores-em-situacao-analoga-a-escravidao-em-goias>

### 趋势符合（1 条）

- **#5** 「social robots might become extremely impressive and lifelike within the lifetimes of many of the people who ar…」  
  判断：**趋势符合**。2026年Moya展示微表情、目光互动及模拟皮肤体温，2025年机器人头部综述也描述机械、感知与计算协同的发展，方向上趋于逼真。综述同时指出恐怖谷及口唇同步等限制；不能说许多当代人的整个有生之年终点已兑现。  
  来源：<https://newatlas.com/ai-humanoids/moya-droidup-lifelike-robot/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12650323/>

### 部分符合（2 条）

- **#21** 「Many of the actors best placed to take advantage of CDR (due to existing infrastructure and ownership of appro…」  
  判断：**部分符合**。2025年对12家油气企业2024年文件的分析发现CDR披露零碎，部分企业以DAC和储存强化而非摆脱化石开采；2024年报道亦记录油气巨头游说碳移除政策。私人利益加固的策略阶段可见，但其是否压过全球严格减缓的净效果尚无法量化。  
  来源：<https://www.eenews.net/articles/energy-lobbyists-try-to-shape-carbon-removal-policies/>；<https://doi.org/10.1016/j.erss.2025.104237>
- **#28** 「Because the availability of CDR affects country mitigation policies, and has the potential to shift some decar…」  
  判断：**部分符合**。2025年欧盟2040目标谈判研究记录CDR与减排目标未被分开，政治因素使严格区分方案落空；2024—2025年文献亦提出具体减缓威慑机制。政策设计阶段的风险得到支持，但尚不能证明2040年及以后减排政策已经失败。  
  来源：<https://iopscience.iop.org/article/10.1088/1748-9326/add0c9>；<https://link.springer.com/article/10.1007/s10584-025-03984-7>；<https://doi.org/10.1016/j.envsci.2024.103884>

### 暂无法判断（37 条）

- **#1** 「With the advent of geoengineering, even the climate may be partially brought under human control (see Chapter …」  
  判断：**暂无法判断**。2026年美国文理科学院FAQ称大规模SRM尚未发生；皇家学会仍只讨论全球部署的潜在效果。缺少气候已被部分可控调节的真实观测，不能把模型或小气球释放当成全球气候控制。  
  来源：<https://www.epa.gov/geoengineering/frequent-questions>；<https://royalsociety.org/news/2025/11/solar-radiation-modification/>；<https://www.amacad.org/sites/default/files/publication/resources/2026_SRM-Primer_FAQs.pdf>
- **#3** 「the real danger of platforms becoming private sovereigns of the digital world to such a point of being accepte…」  
  判断：**暂无法判断**。2025年内容审核研究追踪至2024年的政府—平台关系，发现政府越来越依赖平台，且存在正式、非正式及协作互动。欧盟DSA同时要求平台改变系统并接受公共监督，这些研究跨度始于1995年，未单独辨识出版后新增的政治协作；不能据此认定平台主权化的方向已经兑现。  
  来源：<https://www.mediaoffice.abudhabi/en/technology/abu-dhabi-government-accelerates-digital-strategy-with-landmark-microsoft-g42-partnership/>；<https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms>；<https://doi.org/10.1016/j.telpol.2025.103024>
- **#6** 「social robots will be used in an even wider range of domains」  
  判断：**暂无法判断**。新来源记录2025年票务窗口商业试点和2026年便利店任务试验，教育及酒店综述也显示研发使用。但缺少同口径的出版前后“应用领域种类”比较，不能把新增试点或一般服务机器人销量增长直接当成领域范围已扩大。  
  来源：<https://link.springer.com/article/10.1007/s12369-024-01197-z>；<https://www.mdpi.com/2078-2489/16/1/29>；<https://dl.acm.org/doi/10.1145/3706598.3713471>；<https://www.rockingrobots.com/realbotix-humanoid-robot-works-at-tix4-kiosk-in-las-vegas/>；<https://www.globenewswire.com/news-release/2026/11/08/3398006/0/en/six-agibot-g2-robots-complete-1-730-tasks-in-24-hour-shanghai-convenience-store-trial.html>
- **#7** 「For example, creating robots with apparent social skills, and thus making robots more like humans in their beh…」  
  判断：**暂无法判断**。2025年260人实验发现机器人认知能力增强提高人的行为顺从性，2024年辅助控制实验也观察到用户改变控制策略。这些测量的是认知能力增强下的顺从或控制适应，不直接测量人模仿机器人的做事方式；原结果仍缺对应指标。  
  来源：<https://aabl.cs.tufts.edu/papers/hri2024_reuben.pdf>；<https://dl.acm.org/doi/10.1145/3682074>；<https://doi.org/10.1007/s12369-025-01293-8>
- **#8** 「Moreover, some have raised concerns that the implementation and use of social robots may negatively impact us …」  
  判断：**暂无法判断**。2025年伴聊实验整体上未显著改变21天内社会健康，老年实体机器人综述反而发现孤独感减少；2026年丹麦研究仍强调日常长期互动知识有限。尚未证实原条件中实体机器人实际排挤人际关系并导致损害。  
  来源：<https://arxiv.org/abs/2509.19515>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12598933/>；<https://vbn.aau.dk/en/publications/resident-and-social-robot-interactions-in-danish-nursing-homes-a-/>
- **#9** 「The stronger the need for seamless integration of robots into the interpersonal sphere, the stronger the deman…」  
  判断：**暂无法判断**。2024年335人电梯冲突实验发现机器人下命令或抢先违反预期时接受度较低，礼貌请求可改善互动。礼貌偏好已可观察，但没有直接测量无缝融入的需要随时间增强及需求同步增强；2025年31人Pepper研究记录预期与互动策略适应，仍未测两种强度的共同上升。  
  来源：<https://arxiv.org/abs/2406.17641>；<https://dl.acm.org/doi/abs/10.1145/3613904.3642082>
- **#10** 「In a similar way, robots can potentially contribute to a broader, more inclusive understanding of the body」  
  判断：**暂无法判断**。2024年身体与残障研究仍批评白人、健全身体的工程想象，2026年残障学生实验测的是对机器人或语音代理的理解、隐私等感受。没有直接观测社会对人类身体概念变得更包容的前后变化。  
  来源：<https://www.degruyterbrill.com/document/doi/10.1515/9783110792270-023/html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC11877043/>；<https://arxiv.org/html/2601.15293>
- **#11** 「Notably, in the future, it is to be expected that social robots will be used in an even wider range of domains…」  
  判断：**暂无法判断**。IFR报告2024年专业服务机器人销量增9%，但包含物流而非仅社交机器人；2026年消费者评论研究显示使用体验，未提供领域范围扩张的基线。与#6引文不重叠，原规则要求保留并独立记录同样的证据缺口。  
  来源：<https://link.springer.com/article/10.1007/s12369-024-01197-z>；<https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom/>；<https://dl.acm.org/doi/abs/10.1145/3695772>；<https://doi.org/10.1080/0144929x.2026.2744317>
- **#13** 「This is concerning because should robot relations crowd out human relations, we would be interacting with huma…」  
  判断：**暂无法判断**。2025年伴侣AI关系论文明确称对人际关系影响的研究不足，相关道德地位讨论仍是哲学论证。未获得实体机器人排挤关系后，人际交往及通过交往形成道德品格机会同步下降的直接研究。  
  来源：<https://link.springer.com/article/10.1007/s00146-025-02318-6>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12598933/>；<https://link.springer.com/article/10.1007/s00146-025-02638-7>
- **#14** 「As such, we want to make sure that the benefits of developing social robots that we have obligations to outwei…」  
  判断：**暂无法判断**。2024—2026年资料讨论责任缺口、信任无可信性及假想照护机器人情景。尚没有能确认“对机器人有义务且收益未超过风险成本”这一前提、并进一步失去控制的实际个案。  
  来源：<https://www.annualreviews.org/content/journals/10.1146/annurev-control-062023-082238>；<https://link.springer.com/article/10.1007/s13347-025-00850-3>；<https://link.springer.com/article/10.1007/s44163-026-01025-5>
- **#15** 「SAI could give rise to large risks (i.e. droughts, effect on agriculture, etc.) in different places from where…」  
  判断：**暂无法判断**。2025年SAI干旱研究用GeoMIP6和GLENS模型估算，2026年EDF仍以历史烟霾和卫星数据推断潜在农业影响。联合国说明大尺度户外测试未开展，缺少真实SAI部署造成异地或延迟损害的观察。  
  来源：<https://acp.copernicus.org/articles/25/13103/2025/>；<https://www.un.org/scientific-advisory-board/sites/default/files/2025-05/250403-SRM-Rev-8.pdf>；<https://www.edf.org/edf-grantees-study-past-data-understand-potential-srm-impacts>
- **#16** 「Ethical concerns with BECCS arise due to the very large scales of envisaged implementation seen in climate mit…」  
  判断：**暂无法判断**。2025年BECCS研究计算土地、水及生物圈约束，工作坊报告仍讨论扩大规模的未来争议。未取得足以显著改变大气CO2的实际BECCS规模及其粮食竞争观测；模型关系不能直接验证此条件结果。  
  来源：<https://www.naturebasedsolutionsinitiative.org/wp-content/uploads/2025/12/BECCS-Workshop-Report_2025_Royal-Society-and-Nature-based-Solutions-Initiative.pdf>；<https://www.nature.com/articles/s43247-025-02033-6>；<https://www.stateofcdr.org/asset/State-of-Carbon-Dioxide-Removal-Edition-3_June-2026.pdf>
- **#17** 「Clearing land in order to grow BECCS crops could also negatively impact regional biodiversity」  
  判断：**暂无法判断**。2024年印尼材料确有能源林清地，但其燃料用于与煤混烧，没有证明同时配套碳捕集储存。2025及2026年BECCS生物多样性论文使用情景模型，缺少专门为BECCS作物清地后的区域多样性实测。  
  来源：<https://news.mongabay.com/2024/10/indonesia-biomass-zone-for-japan-and-s-korea-energy-razes-rainforest-in-sulawesi/>；<https://www.nature.com/articles/s43247-025-02033-6>；<https://www.nature.com/articles/s41558-026-02557-5>
- **#18** 「Thus, although a single BECCS facility may not have any noteworthy impacts, large-scale implementation would r…」  
  判断：**暂无法判断**。2026年北欧投资银行报道丹麦生物气碳捕集设施，显示项目存在，不能笼统说BECCS不存在。但所选资料未提供大规模实施中脆弱社区与其他群体的实际受损比较，故“最受影响”仍缺证。  
  来源：<https://assets.publishing.service.gov.uk/media/68bec3ee626205fb47f01d8c/Review_of_potential_social_implications_of_bioenergy_with_carbon_capture_and_storage.pdf>；<https://www.stateofcdr.org/asset/State-of-Carbon-Dioxide-Removal-Edition-3_June-2026.pdf>；<https://www.nib.int/articles/inside-the-worlds-largest-biogas-carbon-capture-facility>
- **#19** 「the most commonly discussed approach is through Stratospheric Aerosol Injection, or SAI. This entails spraying…」  
  判断：**暂无法判断**。2026年MIT技术评论仍讨论尚未建成的太阳地球工程基础设施，皇家学会给的是全球协调部署的潜在降温。没有真实SAI造成全球均温下降的观测，火山自然类比不算技术部署兑现。  
  来源：<https://www.epa.gov/geoengineering/frequent-questions>；<https://royalsociety.org/news/2025/11/solar-radiation-modification/>；<https://www.technologyreview.com/2026/06/17/1138743/hacking-atmosphere-geoengineering-reality-check/>
- **#20** 「First, SRM, and particularly SAI, may be insufficiently disruptive, preventing the much-needed sustainability …」  
  判断：**暂无法判断**。2024年在线实验及2026年策略实验讨论的是信息或博弈条件下的减缓选择，后者总体增加合作、但效果更强且更确定时减缓下降。尚未证实真实采用SAI已阻止必要可持续转型，不能据实验方向直接判对或错。  
  来源：<https://link.springer.com/article/10.1007/s10584-025-04026-y>；<https://www.sciencedirect.com/science/article/pii/S0272494424000616>；<https://link.springer.com/article/10.1007/s10640-026-01072-7>
- **#23** 「The sourcing of sustainable biomass will be a particular challenge for BECCS. A pure market approach based upo…」  
  判断：**暂无法判断**。BCG及南美木料生命周期研究涉及北美原料和具体项目，2026年CDR市场白皮书讨论融资与承购。未找到纯最低成本市场下全球BECCS生物质产地的已实现份额，不能由局部北美项目断言全球南方将非主要来源。  
  来源：<https://www.bcg.com/publications/2024/big-opportunities-in-biogenic-emissions>；<https://sig-gis.com/wp-content/uploads/2024/10/SIG-BECCS-LCA-report-2024.pdf>；<https://reports.weforum.org/docs/WEF_Carbon_Dioxide_Removal_Technologies_2026.pdf>
- **#25** 「Particularly because SRM would immediately have a global effect on the climate, as well as regional (weather) …」  
  判断：**暂无法判断**。皇家学会及2026年实验分类研究讨论潜在全球协调部署，UKRI研究明确只用电脑模型。没有达到足以识别全球及区域天气效应的SRM部署，故即时全球效应不能用模型即真值来判定。  
  来源：<https://royalsociety.org/news/2025/11/solar-radiation-modification/>；<https://www.ukri.org/news/modelling-the-impact-of-solar-radiation-modification/>；<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EF007303>
- **#26** 「As noted in Section 4.1, because too little mitigation has happened, it is very likely that limiting warming t…」  
  判断：**暂无法判断**。2024年CDR状态摘要及2026年章节都在低升温情景中配置碳移除，并指出排放延迟使未来所需移除增加。然而“远低于2°C”这一长期结果尚未最终实现，情景一致性不是必要条件已获事后证明。  
  来源：<https://www.stateofcdr.org/asset/SoCDR-2nd-Edition-Executive-Summary.pdf>；<https://climateactiontracker.org/global/emissions-pathways/>；<https://www.stateofcdr.org/asset/SoCDR-Ed3_Chapter-9_Final.pdf>
- **#27** 「As noted in Section 4.2, the example of BECCS shows this clearly: an ungoverned expansion in the global demand…」  
  判断：**暂无法判断**。2025年英国议会称英国尚无运营BECCS厂，并讨论生物质与粮食、造林的土地竞争；2026年人权简报多为大规模前景。尚缺未经治理的BECCS生物质需求扩张与食品、缺水、多样性及圈地组合结果的同期观测。  
  来源：<https://publications.parliament.uk/pa/cm5901/cmselect/cmpubacc/715/report.html>；<https://assets.publishing.service.gov.uk/media/68bec3c2de0987fe84e0dd1e/Bioenergy_with_carbon_capture_and_storage_-_evidence_on_potential_environmental_impacts.pdf>；<https://environmentalpaper.org/wp-content/uploads/2026/06/HumanRightsBiomass.pdf>
- **#29** 「By potentially exacerbating severe weather impact, SAI has the potential to impose severe injustice upon peopl…」  
  判断：**暂无法判断**。2025年社会经济干旱暴露研究使用气候情景，2026年方法论论文仍讨论以模型和小尺度试验了解SAI。未有实际实施并加重极端天气、继而伤害适应能力最低者的实测链条。  
  来源：<https://doi.org/10.5194/acp-25-13103-2025>；<https://www.un.org/scientific-advisory-board/sites/default/files/2025-05/250403-SRM-Rev-8.pdf>；<https://link.springer.com/article/10.1007/s13194-026-00762-9>
- **#30** 「Relatedly, questions of how to compensate for damage caused by climate change internationally will be increasi…」  
  判断：**暂无法判断**。2026年赔偿责任论文仍争论部署者与排放者应由谁付费，EPA亦否认已发生大规模太阳地球工程。没有大规模部署后跨国气候赔偿案件的前后困难比较；法理争议不能替代条件已触发。  
  来源：<https://carnegieendowment.org/research/2025/07/geoengineering-assessing-risks-in-the-era-of-planetary-security>；<https://www.epa.gov/geoengineering/frequent-questions>；<https://doi.org/10.1080/21550085.2026.2631362>
- **#31** 「Climate engineering makes the already extremely complex climate systems even more complicated, which will furt…」  
  判断：**暂无法判断**。2026年环境法研究所列出未来地球工程损害归因挑战，联合国亦指出模型和部署评估困难。缺少实际大尺度气候工程使责任归属比原先更困难的可比案件或测量，暂不能判正误。  
  来源：<https://www.nature.com/articles/s44168-025-00273-y>；<https://www.un.org/scientific-advisory-board/sites/default/files/2025-05/250403-SRM-Rev-8.pdf>；<https://www.eli.org/vibrant-environment-blog/lack-legal-framework-geoengineering>
- **#32** 「Considering the many ways in which the choices of pregnant women and new mothers/parents are moralized, it see…」  
  判断：**暂无法判断**。2026年围产期综述仍称人工子宫临近临床转化，开普敦大学10月也描述正在研究人体可行性。缺少技术真实可选后对孕产妇选择的新增道德评判记录。  
  来源：<https://www.nature.com/articles/s41372-026-02657-2>；<https://www.cambridge.org/core/elements/artificial-womb-on-trial/F74D45F1B5AE2C2ACD8A51FDEDE482EA>；<https://www.news.uct.ac.za/article/-2026-10-26-the-ethics-of-artificial-womb-technology>
- **#33** 「The possibility of using ectogestative technology for fetuses that would otherwise be born prematurely and fac…」  
  判断：**暂无法判断**。2026年综述及Baker研究所仍讨论首次人体试验的准备；所抓Guardian正文只有1000字符开头，不支持检索摘要更远处的断言。尚无已使用设备的早产儿准父母选择及其道德负担实测。  
  来源：<https://www.nature.com/articles/s41372-026-02657-2>；<https://www.theguardian.com/world/2025/nov/05/baby-alive-outside-womb>；<https://www.bakerinstitute.org/research/building-framework-artificial-womb-technology-clinical-trials>
- **#34** 「Ectogestative technology can be expected to accelerate the process of medicalization of pregnancy and giving b…」  
  判断：**暂无法判断**。2025年22位医护的访谈显示未来部分体外孕育的谨慎态度仍带有医疗化回声，2026年资料则仍在探讨人体可行性。此为预期和既有框架，未观察技术引入后妊娠分娩医疗化加速。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12560763/>；<https://www.nature.com/articles/s41372-026-02657-2>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#35** 「The development of partial-ectogestation is likely to contribute to further medicalization of pregnancy and bi…」  
  判断：**暂无法判断**。2025年医护访谈及2026年临床前综述研究的是预期与动物平台，Lancaster说明当前研究用羊胎或模拟而非人胎。部分体外孕育实际应用后的进一步医疗化尚无观测。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12560763/>；<https://www.cureus.com/articles/428509>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#36** 「Full-ectogestation could potentially open opportunities for fathers to have stronger bonds with their babies, …」  
  判断：**暂无法判断**。2026年综述将完整体外发生归为未来情景，Lancaster也区分当前部分孕育研究与完整体外孕育。尚未出现完整技术下父亲与婴儿的实际依恋比较，故不因理论上的平等机会判对。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC10897319/>；<https://www.nature.com/articles/s41372-026-02657-2>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#37** 「On the other hand, the possibility of full-ectogestation could create the opposite kind of social and moral pr…」  
  判断：**暂无法判断**。2025年社会强制论文章明确讨论“若成为标准孕育选项”的未来压力，Cambridge著作称完整体外发生尚未实现；2026年开普敦资料仍研究可行性。没有技术真实可选后自然妊娠更有德行或使用者被污名的观察。  
  来源：<https://link.springer.com/article/10.1007/s40592-025-00253-2>；<https://www.cambridge.org/core/elements/artificial-womb-on-trial/F74D45F1B5AE2C2ACD8A51FDEDE482EA>；<https://www.news.uct.ac.za/article/-2026-10-26-the-ethics-of-artificial-womb-technology>
- **#38** 「Within the workplace, opting for a ‘natural’ pregnancy over ectogestation may be viewed negatively from the pe…」  
  判断：**暂无法判断**。2025及2026年综述讨论未来人工子宫的伦理法律争议，尚非完整体外孕育的真实工作场所。没有因雇员拒绝此技术而受到生产率或进取心负评的实证个案。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12535042/>；<https://www.nature.com/articles/s41372-026-02657-2>
- **#39** 「If full-ectogestation were to become a reality and the mother’s behaviour ceased to have a direct effect on th…」  
  判断：**暂无法判断**。2025年利益相关者研究为将来首次人体试验征求意见，Lancaster研究状态和2026年开普敦讨论尚限可行性。完整体外孕育、母体行为不再直接影响胎儿这一前提尚未出现，因此行为去道德化不能判定。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12411662>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>；<https://www.news.uct.ac.za/article/-2026-10-26-the-ethics-of-artificial-womb-technology>
- **#40** 「Full-ectogestation would allow for more and earlier medical interventions on the developing fetus.」  
  判断：**暂无法判断**。2026年Baker研究所与临床前系统综述仍聚焦早产支持和首次人体试验转化，没有完整体外孕育中的早期胎儿医疗干预实例。更多更早的人类干预结果仍待技术及比较数据。  
  来源：<https://www.bakerinstitute.org/research/building-framework-artificial-womb-technology-clinical-trials>；<https://www.cureus.com/articles/428509-artificial-womb-technology-a-systematic-review-of-preclinical-evidence-and-implications-for-neonatal-viability-and-intensive-care>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#41** 「Ectogestation might also create opportunities for simple forms of human enhancement, for example, by allowing …」  
  判断：**暂无法判断**。2025年底神经发育综述与2026年Baker报告讨论早产支持、长期结果和人体试验准备。未有安全延长人类孕育时间后带来认知增强的临床比较。  
  来源：<https://www.bakerinstitute.org/research/building-framework-artificial-womb-technology-clinical-trials>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12839978/>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#42** 「However, partialectogestation will turn a coetaneous physical and physiological process into a fragmented one,…」  
  判断：**暂无法判断**。2026年叙述综述说明动物平台旨在保留胎儿生理，2025年医护研究仍争论如何定义将来接受体外孕育的实体。尚缺人类临床中位置出生和生理出生实际分离的病例。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13084614/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12453669/>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>
- **#43** 「If the possibility of full-ectogestation were to become reality, there could be children who had only genetic …」  
  判断：**暂无法判断**。2026年Baker报告区分部分体外支持与完整孕育，系统综述称其证据库尚无人体试验，Lancaster也只描述羊胎及模拟。没有从受精到出生完全体外孕育、因而无妊娠母亲的儿童。  
  来源：<https://www.bakerinstitute.org/research/building-framework-artificial-womb-technology-clinical-trials>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12883048/>
- **#44** 「In addition, regarding fullectogestation, it has to be kept in mind that the technology would use a lot of ene…」  
  判断：**暂无法判断**。2026年Baker报告及临床前综述说明研究仍在动物和人体试验转化阶段，2025年围产医学综述亦列出未解决的工程限制。没有完整体外孕育设备实际运行的能耗记录，不能由保温等设备想当然推出“大量”。  
  来源：<https://www.bakerinstitute.org/research/building-framework-artificial-womb-technology-clinical-trials>；<https://www.degruyterbrill.com/document/doi/10.1515/jpm-2025-0290/html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12883048/>
- **#45** 「As many cultural and religious traditions and rituals are associated with birth, it is likely that with ectoge…」  
  判断：**暂无法判断**。2026年伦理综述及开普敦讨论聚焦未来可行性，2025年医护访谈也非实际人类设备用户。没有体外孕育临床实施后新生的文化宗教出生仪式记录。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12560763/>；<https://www.nature.com/articles/s41372-026-02657-2>；<https://www.news.uct.ac.za/article/-2026-10-26-the-ethics-of-artificial-womb-technology>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 本表只列45条resolvable；44条原unclear保留于data/claims.jsonl及audit/original-unclear-assessments.jsonl，未人工挑选最终候选 |

## 文件

- 本文：`cases/van-de-poel-ethics-of-socially-disruptive-technologies-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/van-de-poel-ethics-of-socially-disruptive-technologies-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/van-de-poel-ethics-of-socially-disruptive-technologies-v5/audit/manual_review_2026-11-15.py`
已知限制：原屏幕对含旧年份扩引会误排；SOURCE_COMMIT标85e6da1但无.git，仅核对toolkit逐文件hash与w1快照一致。首轮65候选/33resolvable曾只是前缀，本报告已全书113块。
