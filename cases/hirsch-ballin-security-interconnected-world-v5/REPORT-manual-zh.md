# 《互联世界中的安全》：出版后预测人工核查

- 案例目录：`cases/hirsch-ballin-security-interconnected-world-v5/`
- 出版日期：2020-04-07（Springer 英文版；由早期荷兰报告翻译修订）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

使用 UvA 终版 PDF，经 pdftotext -enc UTF-8 全文转换；prepare_book 原分块3500/600、156块逐块通读并手写JSON，只替代模型回答，确定性验证/归属/历史筛选/重叠去重/IDs使用 main 85e6da1。实际证据来源是 Exa 检索及 contents 抓取存档，非 WebSearch/WebFetch；48项均完成 PLAN/SELECT/ASSESS/SEMANTIC REVIEW，未定均做改变策略的第二轮。跨条复用已检索URL在SELECT记录明示；6项未定不是抓取失败。本稿以当前 v5 管线导入的55条候选中48条resolvable为计分起点；7条中性转述降为unclear，不计作者预测。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 48 条，剔除非预测 0 条，计入 **48 条预测**，其中 **42 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 22 |
| 趋势符合 | 0 |
| 部分符合 | 16 |
| 错误 | 4 |
| 暂无法判断 | 6 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **52.4%**（22/42） |
| 加权胜率 | **71.4%** |
| 错误率 | **9.5%**（4/42） |
| 未定占比（暂无法判断/预测） | 12.5%（6/48） |

## 总体评价

作者对欧洲周边安全恶化、防务任务持续以及欧洲合作制度障碍的若干方向判断得到支持，但书中包含大量独立重述，不能把条目级胜率当成独立问题的命中概率。具体国防开支稳定区间与后续结果相反；多国、多分项和因果链仅部分得到证实，迁移比较和概率基率等仍未定。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（22 条）

- **#1** 「The assignments that the armed forces must be able to perform to protect the territory and the inhabitants, to…」  
  判断：**正确**。荷兰国防白皮书记录威胁叠加、盟国要求提高与持续作战需求；审计也记录民事支援仍在执行且领土保护要求更高。整体任务负担未消退，但这不代表每一项远程任务都增加。  
  来源：<https://www.ministryofdefence.nl/latest/news/2024/09/05/defence-white-paper-2024-strong-smart-together>；<https://english.rekenkamer.nl/latest/news/2025/03/04/armed-forces-providing-effective-support-in-disasters-and-crises>；<https://www.rijksoverheid.nl/actueel/nieuws/2025/04/04/kabinet-stelt-nederlandse-belangen-centraal-bij-inzet-missies-en-operaties>
- **#2** 「The United Kingdom’s pending exit from the eu will complicate the military cooperation in Europe」  
  判断：**正确**。脱欧后英欧防务合作缺少条约基础，产业和项目准入受限，重建合作又受其他争议拖延。新的伙伴关系是补救，不能抹去已经发生的合作复杂化。  
  来源：<https://www.osw.waw.pl/en/publikacje/analyses/2025-05-23/breaking-deadlock-eu-uk-security-and-defence-partnership>；<https://www.eeas.europa.eu/eeas/eu-uk-security-and-defence-dialogue-joint-doorstep-high-representativevice-president-kaja-kallas-and_en>
- **#3** 「Although earlier austerity measures are being made up for, they will still not attain the necessary capacity.」  
  判断：**正确**。荷兰审计明确指出，增加军费和购买装备并未同步解决装备管理、人员及支援能力问题。与“补回削减仍不能达到必要能力”的主要结果相符。  
  来源：<https://www.rekenkamer.nl/actueel/nieuws/2024/05/15/betere-gereedheid-strijdkracht-vraagt-meer-dan-alleen-aanschaf-materiaal>
- **#4** 「Brexit will create a gap in the development of the European security and defence policy」  
  判断：**正确**。英欧防务政策关系一度缺乏条约性安排，英国企业被排除在有关研发和联合采购计划之外。欧盟自身防务工具后来成长，不等于这一英国参与缺口从未发生。  
  来源：<https://www.osw.waw.pl/en/publikacje/analyses/2025-05-23/breaking-deadlock-eu-uk-security-and-defence-partnership>；<https://www.cer.eu/publications/archive/policy-brief/2025/how-uk-and-eu-can-deepen-defence-co-operation>
- **#7** 「The strain on the security of transport routes, the strategic game surrounding logistics and connections, as w…」  
  判断：**正确**。UNCTAD记录红海和黑海航运受地缘冲突持续扰动、航线绕行以及航运网络攻击增多。运输、物流连接和流动安全承压这一主要方向已在出版后观察到。  
  来源：<https://unctad.org/system/files/official-document/rmt2025overview%5Fen.pdf>
- **#8** 「The international architecture under un auspices will also come under further pressure.」  
  判断：**正确**。安理会研究记录其处理重大危机的困难，CIVICUS明确描述有效性和合法性危机加深。未来契约仍能通过是重要限制，但不反驳国际架构承压加大的判断。  
  来源：<https://doi.org/10.1093/ia/iiaf234>；<https://lens.civicus.org/un-security-council-reform-or-irrelevance/>；<https://press.un.org/en/2024/ga12641.doc.htm>
- **#10** 「the instability and potential for conflict on the southern and eastern flanks of the eu will persist in the co…」  
  判断：**正确**。UCDP记录俄乌战争持续以及中东的国家间和其他严重冲突；欧盟对叙利亚转型也仍强调持续安全威胁。南翼和东翼不稳定持续这一结果成立，并非预测每一处都必然开战。  
  来源：<https://www.uu.se/en/news/2026/2026-06-09-ucdp-record-number-of-conflicts-between-states>；<https://www.consilium.europa.eu/en/press/press-releases/2025/03/18/brussels-ix-conference-on-standing-with-syria-meeting-the-needs-for-a-successful-transition-joint-press-statement/>
- **#11** 「The instability on the eu’s southern periphery appears set to continue for the time being.」  
  判断：**正确**。联合国记录利比亚政治与经济分裂继续加深，苏丹战争仍有外溢风险。利比亚停火大体维持只说明没有全面复战，并未使南部周边整体恢复稳定。  
  来源：<https://news.un.org/en/story/2025/04/1162376>；<https://press.un.org/en/2025/sc16104.doc.htm>
- **#12** 「The states in the east of the eu and their immediate neighbours also appear susceptible to future instability …」  
  判断：**正确**。欧盟记录俄方恶意活动在入侵乌克兰后进一步升级，并涉及成员国选举和关键设施；RAND和摩尔多瓦选举研究补充了邻国遭干预的情况。民主韧性和亲欧选举结果不等于俄罗斯破坏性介入没有增加。  
  来源：<https://www.consilium.europa.eu/en/press/press-releases/2025/07/18/hybrid-threats-russia-statement-by-the-high-representative-on-behalf-of-the-eu-condemning-russia-s-persistent-hybrid-campaigns-against-the-eu-its-member-states-and-partners/>；<https://www.rand.org/pubs/commentary/2025/07/countering-russian-influence-support-for-armenia-georgia.html>；<https://www.stimson.org/2025/moldovas-2025-elections-a-pro-european-victory-despite-russias-hybrid-threats/>
- **#19** 「With Brexit, the United Kingdom will also find itself ‘outside’ the Common Security and Defence Policy, which …」  
  判断：**正确**。英国退出欧盟决策体系后，没有立即建立英欧安全合作的条约基础，产业准入和任务参与需要新的安排，合作因此复杂化。随后建立伙伴关系并允许讨论第三国式参与，并不恢复其成员国地位或否认先前障碍。  
  来源：<https://www.osw.waw.pl/en/publikacje/analyses/2025-05-23/breaking-deadlock-eu-uk-security-and-defence-partnership>；<https://www.eeas.europa.eu/eeas/eu-and-uk-conclude-security-and-defence-partnership_en>
- **#22** 「The states on the eu’s eastern flank are high on the list of potential flashpoints of future instability and c…」  
  判断：**正确**。欧盟正式声明记录俄方干预活动在战争后进一步升级，并列出罗马尼亚选举遭混合攻击；波兰和罗马尼亚报道也记录干预增加。这里核对的是暴露于破坏性影响，而不是要求所有选举都被俄方左右。  
  来源：<https://www.consilium.europa.eu/en/press/press-releases/2025/07/18/hybrid-threats-russia-statement-by-the-high-representative-on-behalf-of-the-eu-condemning-russia-s-persistent-hybrid-campaigns-against-the-eu-its-member-states-and-partners/>；<https://therecord.media/russia-disinformation-poland-presidential-election>；<https://www.stimson.org/2025/moldovas-2025-elections-a-pro-european-victory-despite-russias-hybrid-threats/>
- **#23** 「The instability and potential for conflict along the southern and eastern flanks of the eu will persist in the…」  
  判断：**正确**。UCDP记录欧洲东侧的俄乌战争持续，中东亦存在严重武装冲突，欧盟对南部转型仍有重大安全担忧。区域不稳定持续得到支持；局部对话与停火不等于两翼整体稳定。  
  来源：<https://www.uu.se/en/news/2026/2026-06-09-ucdp-record-number-of-conflicts-between-states>；<https://www.consilium.europa.eu/en/press/press-releases/2025/03/18/brussels-ix-conference-on-standing-with-syria-meeting-the-needs-for-a-successful-transition-joint-press-statement/>
- **#24** 「The instability on the southern border seems set to continue for the time being.」  
  判断：**正确**。联合国仍描述利比亚的脆弱转型、政治分裂和经济压力，以及苏丹战事向周边外溢。停火大体维持并未消除南部周边的不稳定。  
  来源：<https://news.un.org/en/story/2025/04/1162376>；<https://press.un.org/en/2025/sc16104.doc.htm>
- **#25** 「The death toll in the civil war in Syria has climbed into the hundreds of thousands and the war will probably …」  
  判断：**正确**。UNDP的事后评估明确称冲突已摧毁近四十年的经济、社会和人力资本进步，世界银行亦记录经济严重萎缩。这里采用的是已经发生的倒退评估，不把未来恢复年限的模型展望当成实际结果。  
  来源：<https://www.undp.org/syria/press-releases/accelerating-economic-recovery-critical-reversing-syrias-decline-and-restoring-stability>；<https://www.worldbank.org/en/news/press-release/2025/07/07/new-world-bank-report-highlights-syria-s-economic-challenges-and-recovery-prospects-for-2025>
- **#27** 「Pressure will also increase on the international architecture constructed under the auspices of the un.」  
  判断：**正确**。安理会研究确认重大危机应对困难，CIVICUS明确指出有效性与合法性危机加深。未来契约表明合作并未消失，但与架构承压增加并不矛盾。  
  来源：<https://doi.org/10.1093/ia/iiaf234>；<https://lens.civicus.org/un-security-council-reform-or-irrelevance/>；<https://press.un.org/en/2024/ga12641.doc.htm>
- **#32** 「Another dominant trend concerns the expectation that armed forces will be called on more frequently to tackle …」  
  判断：**正确**。北约明确将协助民政当局救灾需求增加称为延续中的趋势，MiRCH记录多国国内及跨国气候灾害军事应对。主要方向得到支持，不将灾害增多简单等同于每国每年军队出动都增加。  
  来源：<https://www.nato.int/content/dam/nato/legacy-wcm/media_pdf/2024/7/pdf/240709-Climate-Security-Impact.pdf>；<https://climateandsecurity.org/2025/11/mirch-updates-june-october-2025-militaries-intervene-worldwide-during-wildfire-and-tropical-cyclone-season/>
- **#36** 「Especially in Africa there will be a great need for stabilisation and peacekeeping missions」  
  判断：**正确**。SIPRI记录非洲冲突管理面对大量激烈冲突，多边维和资源削减同时留下新旧冲突应对缺口。原句预测的是稳定与维和的需要，而不是实际派遣人数，不能因部署下降就判需求下降。  
  来源：<https://www.sipri.org/news/2025/sipri-co-hosts-workshop-future-conflict-management-africa>；<https://www.sipri.org/publications/2026/sipri-fact-sheets/developments-and-trends-multilateral-peace-operations-2025>；<https://press.un.org/en/2025/sc16104.doc.htm>
- **#37** 「The eu has been a frontrunner in this type of operation in the last decade and is also expected to develop sec…」  
  判断：**正确**。欧盟年度报告记录推出内部安全战略、内部安全基金项目、共同边境数字系统及与第三国边境合作。这些是传统共同外交与安全政策以外的安全活动发展，不只是成员国军费上升。  
  来源：<https://op.europa.eu/webpub/com/general-report-2025/en/chapter3.html>
- **#39** 「With the emergence of border security as a new priority, the third main task will only become more explicitly …」  
  判断：**正确**。荷兰宪兵实际新增临时内部边境检查，并将检查延伸到机场，第三任务向边境安全倾斜得到体现。审计对政策效果和人员短缺的批评不否认这一职责调整本身。  
  来源：<https://www.marechaussee.nl/onderwerpen/t/tijdelijke-herinvoering-van-grenscontroles/resultaten-binnengrenscontroles>；<https://english.rekenkamer.nl/latest/news/2025/06/03/internal-border-controls-not-achieving-policy-goals-more-quickly>
- **#40** 「With border security increasingly justifying European cooperation, defence policy will become an intrinsic com…」  
  判断：**正确**。欧盟已经提出共同防务白皮书、跨欧洲能力建设和共同融资工具，防务成为欧洲合作的核心政策议题。采购碎片化和治理障碍仍在，但原句并未预测立即建立统一军队。  
  来源：<https://defence-industry-space.ec.europa.eu/eu-defence-industry/white-paper-european-defence-readiness-2030_en>；<https://www.bruegel.org/policy-brief/governance-and-funding-european-rearmament>
- **#42** 「The Netherlands is confronted with direct threats – ‘old’ and ‘new’, around Europe and global – and constant d…」  
  判断：**正确**。荷兰国防白皮书记录累积的新旧威胁和持续作战能力要求，政府也重申继续参加国际任务。减少长期远程大规模部署属于任务组合调整，不等于原句所说的持续任务需求消失。  
  来源：<https://www.ministryofdefence.nl/latest/news/2024/09/05/defence-white-paper-2024-strong-smart-together>；<https://www.rijksoverheid.nl/actueel/nieuws/2025/04/04/kabinet-stelt-nederlandse-belangen-centraal-bij-inzet-missies-en-operaties>
- **#47** 「Furthermore, the turbulence is unlikely to abate in the foreseeable future.」  
  判断：**正确**。UCDP记录俄乌、中东与苏丹仍有严重武装暴力，欧洲周边动荡没有整体消退。叙以局部停火是缓和证据，但欧盟同一声明仍要求停止暴力并推进安全重建，不等于周边全面稳定。  
  来源：<https://www.uu.se/en/news/2026/2026-06-09-ucdp-record-number-of-conflicts-between-states>；<https://www.eeas.europa.eu/eeas/syria-statement-spokesman-ceasefire-agreement_en>

### 部分符合（16 条）

- **#5** 「the likelihood that American involvement in nato will diminish under President Trump」  
  判断：**部分符合**。国会研究处记录欧洲威慑倡议经费在特朗普首任末期下降，投入减少这一财政分项成立；但驻军重置方案同时强调加强轮驻和欧洲承诺，不能据削减德国驻军的计划就判美国整体退出或全面减少北约参与。  
  来源：<https://www.congress.gov/crs_external_products/IF/PDF/IF10946/IF10946.8.pdf>；<https://www.jcs.mil/Media/News/News-Display/Article/2292956/dod-proposes-removing-more-than-11000-troops-from-germany/>
- **#6** 「The growing economic and political influence of countries like Russia, China, Indonesia, India, Brazil and Mex…」  
  判断：**部分符合**。SIPRI记录中国、印度等的军费增长及大国资源供应链竞争，支持军力和资源竞争分项；巴西的多向结盟及与中美同时合作说明并非所有列举国家都走向同一种对抗。对整个国家组、全部通道和由地位上升造成紧张的完整链条，证据不足。  
  来源：<https://www.sipri.org/sites/default/files/2026-04/2604_milex_2025.pdf>；<https://www.sipri.org/sites/default/files/2024-10/critical_minerals.pdf>；<https://www.belfercenter.org/research-analysis/multi-alignment-strategy-how-brazil-navigates-between-washington-beijing-and>
- **#14** 「Furthermore, raw materials extraction and the trade routes in the Arctic region will grow in importance becaus…」  
  判断：**部分符合**。北极理事会确认船舶活动和航行距离增加，并将海冰变化和资源项目列为推动因素；另一方面，北方航道货运及油气项目受到制裁和运力瓶颈限制。航运重要性上升得到支持，但不能把它扩大成所有资源开采及航线均持续增强。  
  来源：<https://arctic-council.org/news/increase-in-arctic-shipping/>；<https://gcaptain.com/northern-sea-route-traffic-slips-in-2025-as-sanctions-constrain-russias-arctic-ambitions/>
- **#15** 「These trends will also further increase the migration potential in the world」  
  判断：**部分符合**。IOM明确记录气候影响正在增加迁移压力，环境与生计受损这一分项支持迁移潜力上升；同一报告也指出资源不足会把人困在原地。尚不能由这一压力分项推断所有所述趋势共同造成的全球总体潜力，更不能以实际移民存量替代潜力。  
  来源：<https://worldmigrationreport.iom.int/what-we-do/world-migration-report-2026/chapter-6/climate-change-and-migration-understanding-context>；<https://migrantprotection.iom.int/system/files/resources/2b1229a6-52a6-40cf-bc75-0d979ee186ff/document/IOM%202024%2C%20Key%20Messages%20Environmental%20Migration%20and%20Protection%2C%20WGEMP.pdf?id=6116&lang=en&type=node>
- **#16** 「There is also increasing evidence that future inter-state conflicts will be played out in the free, still open…」  
  判断：**部分符合**。USNI记录中菲海上对峙升级，公海及争议海域成为国家间冲突场域这一分项成立。但该材料没有同时证实海底矿藏、各类渔场及跨国饮用水源均成为同类冲突场域，故不判整体正确。  
  来源：<https://news.usni.org/2025/01/10/top-stories-2024-south-china-sea-flashpoints>
- **#17** 「The intensification of cross-border flows, the sharp increase in the number of non-­ state actors and the disa…」  
  判断：**部分符合**。荷兰威胁评估记录跨境国家行为与非国家行为结合、破坏活动增加及威胁更难预测，支持数字和破坏活动这一分项。证据并非所有政府全部跨国安全问题的发生频率，不能据此判整体方向完全兑现。  
  来源：<https://english.nctv.nl/documents/2025/09/25/threat-assessment-of-state-actors-2025>；<https://english.nctv.nl/latest/news/2025/12/02/cybersecurity-assessment-netherlands-2025>
- **#26** 「The further growth of the economic and political importance of countries like China, Indonesia, India, Brazil …」  
  判断：**部分符合**。SIPRI资料支持军力扩张及资源供应链安全竞争，但印尼与巴西的官方联合合作安排说明国家间也在深化贸易和防务合作。不能由中国等国的表现推出原列举国家在贸易、资源、通道和军力各分项上全面兑现。  
  来源：<https://www.sipri.org/sites/default/files/2026-04/2604_milex_2025.pdf>；<https://www.sipri.org/sites/default/files/2024-10/critical_minerals.pdf>；<https://www.setneg.go.id/baca/index/indonesia_dan_brasil_sepakat_menuju_kemitraan_ekonomi_komprehensif_untuk_perkuat_perdagangan_dan_investasi>
- **#28** 「It is reasonable to expect that these power shifts and the fragmentation of power towards non-state actors wil…」  
  判断：**部分符合**。SIPRI明确记录核武器依赖增强和升级风险上升，核威胁增大的分项成立。既有国家扩充或改良武库并不自动证明向更多行为者扩散，叙利亚新发现也属于旧政权遗产，因此“核及其他大规模杀伤性武器扩散与威胁”不能整体判对。  
  来源：<https://www.sipri.org/media/press-release/2026/increasing-focus-nuclear-weapons-amid-heightened-escalation-risks-new-sipri-yearbook-out-now>；<https://press.un.org/en/2026/sc16377.doc.htm>
- **#29** 「The stability of the relationships within the alli- 5 Defence Policy in a Changed Security Environment 105 anc…」  
  判断：**部分符合**。脱欧后英欧安全联系确实需要重新谈判，特朗普首任末期也出现经费下降和驻军重置争议，支持同盟关系受扰动的部分。现有证据不足以给整个同盟稳定性的可预测性建立可比尺度，后来另一届任期的言论不拿来单独证明首任期预测。  
  来源：<https://www.osw.waw.pl/en/publikacje/analyses/2025-05-23/breaking-deadlock-eu-uk-security-and-defence-partnership>；<https://www.congress.gov/crs_external_products/IF/PDF/IF10946/IF10946.8.pdf>；<https://www.jcs.mil/Media/News/News-Display/Article/2292956/dod-proposes-removing-more-than-11000-troops-from-germany/>
- **#33** 「Achieving military superiority will be more challenging and more expensive because of the accelerating pace at…」  
  判断：**部分符合**。RUSI比较出版前后能力，明确指出中俄对西方空中优势的挑战加大，CNAS也记录技术迅速模仿和进攻更难。获得优势更难这一分项成立，但同一研究指出廉价无人系统可替代部分昂贵能力，整体“更昂贵”并未得到同口径成本证实。  
  来源：<https://www.rusi.org/explore-our-research/publications/insights-papers/evolution-russian-and-chinese-air-power-threats>；<https://www.cnas.org/publications/reports/evolution-not-revolution>
- **#34** 「Under the Readiness Action Plan, the mutual assistance clause, laid down in Article 5 of the nato treaty, will…」  
  判断：**部分符合**。北约资料确认东翼轮驻和战斗编队扩展、战后最大规模演习及空中警戒持续加强。空中警戒不完全等于原句的空中侦察，且原计划名下各组成部分与后续措施的逐一对应没有充分落实，故只判部分符合。  
  来源：<https://www.nato.int/en/what-we-do/deterrence-and-defence/strengthening-natos-eastern-flank>
- **#35** 「These measures will be supplemented with more and heavier firepower」  
  判断：**部分符合**。北约东翼已扩展编队并建立装甲旅，增加火力的方向有实际组织和部署依据；但部分旅仍在形成，现有材料不足以证明所有相关部署已配齐更重火力。不能把最终成军计划当作全部交付。  
  来源：<https://www.nato.int/en/what-we-do/deterrence-and-defence/strengthening-natos-eastern-flank>；<https://www.defenceiq.com/indirect-fires/articles/how-nato-allies-are-closing-land-warfare-capability-gaps-on-the-eastern-flank>
- **#43** 「A look at the planning overview for the armed forces, assembled in the so-called ‘template’ in the defence bud…」  
  判断：**部分符合**。审计确认大额潜艇替换项目，主战装备现代化这一分项成立；但新的工业创新议程已经启动基金和专门预算，不符合几乎不投入创新的全面判断。已拨预算不等同于全部花完，这一限制保留。  
  来源：<https://english.rekenkamer.nl/latest/news/2024/05/23/provisional-award-decision-for-new-submarines-careful-and-transparent>；<https://www.tweedekamer.nl/downloads/document?id=2025D15101>
- **#45** 「At the same time, however, the strength of the only recently adopted Common Foreign and Security Policy, as la…」  
  判断：**部分符合**。匈牙利多次阻延援乌与制裁体现共同外交行动受掣肘，支持共同价值分歧影响政策这一分项。英欧后来建立新伙伴关系且合作延续，材料不足以证明脱欧和价值分歧已使共同外交与安全政策整体净实力下降。  
  来源：<https://www.dw.com/en/eu-sidesteps-hungary-veto-but-more-ukraine-showdowns-loom/a-71991130>；<https://www.consilium.europa.eu/en/meetings/international-summit/2025/05/19/>
- **#46** 「There are many fragile states in Africa and the Middle East, where unrest and conflict will have serious impli…」  
  判断：**部分符合**。EUAA记录叙利亚局势改变与欧洲庇护申请及审理政策直接联动，支持中东动荡通过迁移影响欧洲。申请近期下降也必须保留；现有材料没有完整隔离非洲与中东冲突各自造成的严重影响，不能把所有庇护申请都归于这些冲突。  
  来源：<https://www.euaa.europa.eu/latest-asylum-trends-annual-analysis/applications>；<https://www.euaa.europa.eu/news-events/eu-asylum-applications-down-one-fifth-2025-amid-shifting-geopolitical-dynamics>
- **#48** 「Governments will be confronted more frequently with transnational (security) issues whose origin, course and c…」  
  判断：**部分符合**。荷兰官方评估记录跨国破坏风险增加、数字威胁更多样且难预测，支持安全问题复杂化这一分项。该国数字领域的材料不能直接代表所有政府全部跨国问题的频率，故不判整体正确。  
  来源：<https://english.nctv.nl/documents/2025/09/25/threat-assessment-of-state-actors-2025>；<https://english.nctv.nl/latest/news/2025/12/02/cybersecurity-assessment-netherlands-2025>

### 错误（4 条）

- **#18** 「in time the diminishing American dependence on oil from the Middle East will translate into lower oil prices a…」  
  判断：**错误**。EIA的年均布伦特价格序列在出版后高于出版年，未呈现原句预期的更低油价。美国中东进口占比较低不等于所预测的后果已经成立，且不足以证明安全政策已因此持续从欧洲和中东转向亚太。  
  来源：<https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=a&n=pet&s=rbrte>；<https://www.eia.gov/todayinEnergy/detail.php?id=67407>
- **#20** 「Britain’s departure from the eu would seem to increase the chances of a more European, but less military Commo…」  
  判断：**错误**。欧盟共同安全与防务政策的快速部署能力已进入运作阶段，形成新的共同军事工具；欧盟还设立支持军事行动的和平基金。军事政策方向并未变得更弱，不能只凭英国离开就判这一复合预测部分成功。  
  来源：<https://www.eeas.europa.eu/eeas/common-security-and-defence-policy-eu-rapid-deployment-capacity-becomes-operational_en>；<https://www.consilium.europa.eu/en/policies/european-defence-readiness/>
- **#21** 「The Caribbean parts of the Kingdom of the Netherlands currently fall into the latter category, although there …」  
  判断：**错误**。欧盟委员会仍将这些岛屿列为海外国家和领地；近期研究也明确它们保持现有地位，外缘地区地位仍只是可选方案。按出版至截止日的近期窗口，地位改变没有发生，不能把“仍可能讨论”无限顺延为未定。  
  来源：<https://international-partnerships.ec.europa.eu/countries/overseas-countries-and-territories_en>；<https://www.bes-reporter.com/news/general/91924/upg-status-for-bes-islands-requires-continued-support-from-the-hague>
- **#41** 「In the Netherlands, the increase in the defence budget will stabilise defence spending at around 1.1% and, dep…」  
  判断：**错误**。北约同口径序列显示荷兰支出占GDP在2023年为1.60%，随后估计继续提高，已明显脱离书中低位稳定区间。具体比例与实际方向均不符，不能按数量级给部分符合。  
  来源：<https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2025-en.pdf>；<https://www.sipri.org/sites/default/files/2026-04/2604_milex_2025.pdf>

### 暂无法判断（6 条）

- **#9** 「These power shifts and the fragmentation of power among state and non-state actors will probably also be refle…」  
  判断：**暂无法判断**。SIPRI证实既有拥核国家现代化和风险上升，但这不能直接等同于核武器及其他大规模杀伤性武器向更多行为者扩散。补检索取得的叙利亚材料主要是发现旧政权未申报的化武遗产，仍缺出版后新增扩散的同口径事实。  
  来源：<https://www.sipri.org/media/press-release/2026/increasing-focus-nuclear-weapons-amid-heightened-escalation-risks-new-sipri-yearbook-out-now>；<https://press.un.org/en/2026/sc16377.doc.htm>
- **#13** 「The Atlantic Basin is likely to become increasingly important because roughly 60% of the increase in oil produ…」  
  判断：**暂无法判断**。大西洋盆地研究明确记录其产油量及全球份额上升，但全球总产量份额并非原句所说的增产份额。原句写明的终点尚未到，且基期和地理口径不能从现有产量表严密重建，不能把另一份机构展望当作兑现。  
  来源：<https://www.transatlantic.org/wp-content/uploads/2024/10/Atlantic-Energy-Forum-Isbell-paper-final-oct-6-2024.pdf>；<https://publications.opec.org/asb/chapter/show/154/2827/2831>；<https://www.iea.org/reports/oil-2025/executive-summary>
- **#30** 「Concurrent conflicts with countries with which we have trade relations are likely to become more rather than l…」  
  判断：**暂无法判断**。欧俄仍有贸易且同时存在严重对抗，但单个国家对或全球冲突总数不能证明“有贸易关系的国家间冲突”更频繁。补检索的贸易与战争研究以出版前的争端样本为主，仍缺出版后同口径国家对频率的直接结论。  
  来源：<https://ec.europa.eu/eurostat/statistics-explained/index.php?title=EU_trade_with_Russia_-_latest_developments&utm=>；<https://www.rieti.go.jp/jp/publications/dp/25e065.pdf>；<https://svmiller.com/peacesciencer/reference/cow_trade_ndy.html>
- **#31** 「Although large-scale military conflicts cannot be ruled out, hybrid forms of conflict and warfare appear more …」  
  判断：**暂无法判断**。IISS和CSIS记录混合攻击上升，UCDP同时记录常规国家间战争增加；两类资料的事件定义和分母不同。补检索仍没有取得可比的概率或基率，不能将许多破坏事件与少数战争直接相除，也不能仅因发生大战就反判原句错误。  
  来源：<https://www.iiss.org/globalassets/media-library---content--migration/files/research-papers/2025/08/pub25-095-the-scale-of-russian-sabotage-operations.pdf>；<https://www.csis.org/analysis/russias-shadow-war-against-west>；<https://www.uu.se/en/news/2026/2026-06-09-ucdp-record-number-of-conflicts-between-states>；<https://icds.ee/static/icds_policy_paper_russias_hybrid_attacks_in_europe_henrik_praks_april_2025-2.pdf>
- **#38** 「the third main task of the armed forces, providing support for civil authorities in upholding the law and prov…」  
  判断：**暂无法判断**。审计确认民事支援有效且重要，但同时记录领土保护挤压有限能力，并没有给出第三任务重要性上升的同口径历史比较。补检索仍未解决其绝对需求和相对资源权重的区别，不能把“重要”本身当成“比过去更重要”。  
  来源：<https://english.rekenkamer.nl/latest/news/2025/03/04/armed-forces-providing-effective-support-in-disasters-and-crises>；<https://english.rekenkamer.nl/documents/2025/03/04/the-third-main-task-of-the-dutch-armed-forces>
- **#44** 「The consequences of climate change could cause far greater migration streams, for example from the Nile Delta …」  
  判断：**暂无法判断**。IOM与实地研究说明孟加拉气候迁移主要是国内和近距离流动，不能与叙利亚跨境难民潮混作同一分母。补检索仍缺尼罗河三角洲及孟加拉实际气候归因迁移量与叙利亚的可比观察；远期模型人数也不是截至截止日的兑现。  
  来源：<https://crisisresponse.iom.int/index.php/response/bangladesh-crisis-response-plan-2025>；<https://www.swissinfo.ch/eng/swiss-diplomacy/bangladesh-sheds-light-on-climate-change-migration-patterns/88942372>；<https://documents1.worldbank.org/curated/en/099050825085041392/pdf/P500493-ed598674-9483-4417-a8fa-9852c3caa057.pdf>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/hirsch-ballin-security-interconnected-world-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/hirsch-ballin-security-interconnected-world-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/hirsch-ballin-security-interconnected-world-v5/audit/manual_review_2026-11-15.py`
## 质量风险与敏感性

- 使用 UvA-DARE 所存出版社终版公开 PDF，而非队列字节版本；正文版本是否完全一致没有独立逐字比对。2020 版沿用早期荷兰报告，统一以 2020-04-07 之后的事实计分，不把较早已发生结果直接计为命中。
- 156 块全部通读，61 个原始抽取项；85e6da1 确定性处理得到 55 candidates / 48 resolvable，7 个 reported/unclear 保留候选不计分。管线历史屏幕排除 5 项、重叠去重 1 项，不作主题去重。历史屏幕对含旧年份的未来句可能误排；其中涉及战略概念回顾、轮驻延续、跨页技术风险图注、北约协议后续经费的 4 项仍含未来成分，全部保留在 policy_report/proposals 供协调者复审，未绕过代码筛选或暗加分母。
- 无明确终点的“近期地位改变”按同一隐含窗口评错；气候迁移“远大于叙利亚”因具体地理与归因人口不可比而未定，不是无限等待。大西洋增产份额不拿总产量份额或新机构预测冒充兑现。核扩散与既有武库/威胁严格区分。
- 同主题独立句可能提高胜率。正式只执行 claims_from_results 的重叠规则。近似重述组每组仅留最早句的敏感性：39 预测、33 可判，正15/趋0/部14/错4/未6；strict 45.45%、weighted 66.67%、错误率12.12%。更宽主题组敏感性：36 预测、30 可判，正13/趋0/部13/错4/未6；strict43.33%、weighted65.00%、错误率13.33%。分组与取舍见 audit/sensitivity.json，不替代正式评分。
- 77 个证据记录对应 77 个实际存档 URL，部分动态网页日期元数据是初始日期，部分 PDF/网页文本经 Exa 截断；只使用实际存档出现的段落，发布元数据不当作观测期。日期缺失的警告保留在 audit/validation_warnings.json。
- 语义复核由同一助手手工完成，不声称独立人类或独立模型验收；因果归属、定性“重要性/实力”和多分项范围仍有解释风险。#32 以北约明确承认救灾需求延续上升为方向依据，MiRCH累计个案数不是频率增长证据。#18 的油价判断对出版年基期敏感。#29 书中跨页连字符及页眉保留在连续原文引文中。
