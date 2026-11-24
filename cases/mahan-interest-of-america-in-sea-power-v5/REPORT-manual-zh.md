# 马汉《美国海权的利益：现在与未来》：出版后预测人工核查

- 案例目录：`cases/mahan-interest-of-america-in-sea-power-v5/`
- 出版日期：1897（论文集统一出版年）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

TXT逐块审读并经85e6da1版工具确定性导入；全部context清空。实际证据取得方式为Exa检索与Exa contents公开页存档，不是WebSearch/WebFetch。79个导入候选中67条可核验预测进入本次人工核验，12条unclear保留但不评分。没有按主题语义去重；重叠去重仅由claims_from_results执行。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 67 条，剔除非预测 0 条，计入 **67 条预测**，其中 **58 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 29 |
| 趋势符合 | 0 |
| 部分符合 | 19 |
| 错误 | 10 |
| 暂无法判断 | 9 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **50.0%**（29/58） |
| 加权胜率 | **66.4%** |
| 错误率 | **17.2%**（10/58） |
| 未定占比（暂无法判断/预测） | 13.4%（9/67） |

## 总体评价

对美国走向海外、英美合作、运河成为航运枢纽等方向预见较好；尼加拉瓜选址、海程比例、长期小海军和若干绝对安全保证失准。条件未保持、道德文明定义含混与结果证据不足均保留未定。相同主题反复出现可能放大表观胜率，敏感性见PR_BODY。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（29 条）

- **#1** 「Independently of all bias for or against protection, it is safe to predict that, when the opportunities for ga…」  
  判断：**正确**。美国后来成为制成品净出口国，存档研究将这一转变置于约1910年，并确认钢铁出口的显著增长；开拓海外销路的方向已经实现。  
  来源：<https://doi.org/10.3386/w7638>
- **#2** 「But the great seaboard powers there do not stand on guard against their continental rivals only; they cherish …」  
  判断：**正确**。美德在马尼拉和委内瑞拉等海外利益问题上发生实际对抗。预测是利益冲突可能继续，并非所有冲突必然开战；部分事件和平解决不构成反证。  
  来源：<https://digitalcommons.iwu.edu/cgi/viewcontent.cgi?article=1025&context=history_honproj>；<https://en.wikipedia.org/wiki/Germany%E2%80%93United_States_relations>
- **#3** 「In a general way, it is evident enough that this canal, by modifying the direction of trade routes, will induc…」  
  判断：**正确**。运河通航后船舶流量大幅增加，巴拿马形成连接两洋的港口与交通网络，符合加勒比交通量增加和航运通道繁忙化；不把运河流量说成整个加勒比地区的经济增长率。  
  来源：<https://www.acs-aec.org/en/article/caribbean-and-widening-panama-canal-panacea-or-problems>；<https://pancanal.com/en/connectivity/>
- **#5** 「When the Isthmus is pierced, this isolation will pass away, and with it the indifference of foreign nations.」  
  判断：**正确**。增长的跨洋通航和两洋港口连接结束了地峡作为航运障碍的状态。这里核验交通与国际联系，不把区域内每座岛屿都已繁荣作为附加结论。  
  来源：<https://www.acs-aec.org/en/article/caribbean-and-widening-panama-canal-panacea-or-problems>；<https://pancanal.com/en/connectivity/>
- **#7** 「Whether they will or no, Americans must now begin to look outward. The growing production of the country deman…」  
  判断：**正确**。美国随后取得海外岛屿和属地并展开帝国扩张，反帝国主义运动未阻止这一发展。只确认向外行动增强，不宣称原文列出的每个推动因素均被独立证实。  
  来源：<https://history.house.gov/Exhibitions-and-Publications/APA/Historical-Essays/Exclusion-and-Empire/1898/>；<https://www.jstor.org/stable/j.ctv4rft41>
- **#9** 「The military needs of the Pacific States, as well as their supreme importance to the whole country, are yet a …」  
  判断：**正确**。圣迭戈基地建立后维修、训练与舰队设施迅速扩张，直接显示美国本土太平洋沿岸的军事需求和全国海军价值；未用当时并非太平洋各州的夏威夷替代。  
  来源：<https://cnrsw.cnic.navy.mil/Installations/NAVBASE-San-Diego/About/History/>
- **#14** 「Whichever it be, the convergence there of so many ships from the Atlantic and the Pacific will constitute a ce…」  
  判断：**正确**。运河成为连接两洋的全球运输要道，围绕控制权的条约谈判以及入口两端设防也有记录，符合商业中心形成及入口受重视的主干判断。  
  来源：<https://www.trade.gov/market-intelligence/panama-panama-canal>；<https://warhistory.org/article/panama-canal-zone-defences-i>；<https://history.state.gov/milestones/1899-1913/panama-canal>
- **#15** 「So the Isthmian Canal is an inevitable part in the future of the United States; yet one that cannot be separat…」  
  判断：**正确**。跨地峡运河后来建成，并伴随巴拿马独立、通行与控制权条约及美国安全保证等政策行动，符合这一未设终点的结果预测。  
  来源：<https://history.state.gov/milestones/1899-1913/panama-canal>
- **#21** 「it is still true that the canal will present an element of much weakness from the military point of view.」  
  判断：**正确**。军事评析明确列出运河易受多类威胁、大型航母不能使用等重大局限，符合安全体系中存在明显薄弱环节；另一来源说明其转场收益，未把有弱点扩大成毫无战略益处。  
  来源：<https://www.usni.org/magazines/proceedings/1980/january/military-aspects-panama-canal-issue>；<https://www.usni.org/magazines/proceedings/1914/may/german-view-strategic-importance-panama-canal>
- **#24** 「In these conditions, not in European necessities, is to be found the assurance that the canal will be made.」  
  判断：**正确**。美国两岸交通需求和海军绕行困难确曾推动其主导修建，运河最终建成；欧洲方面的先行工程失败没有使这一美国自身需求所指向的结果落空。  
  来源：<https://history.state.gov/milestones/1899-1913/panama-canal>；<https://pancanal.com/en/american-canal-construction/>；<https://www.history.navy.mil/research/histories/ship-histories/danfs/o/oregon-ii.html>
- **#25** 「Many causes will combine to retain in the line of the Suez Canal the commerce of Europe with the East; but to …」  
  判断：**正确**。交通地理研究分别确认苏伊士服务欧洲至亚洲通路、巴拿马大幅改善美洲太平洋沿岸可达性，运河局也记录贸易格局改变。原预测不是说所有欧洲至亚洲船舶永远只走苏伊士，替代航线的存在不作过度反证。  
  来源：<https://transportgeography.org/contents/chapter1/emergence-of-mechanized-transportation-systems/suez-panama-canal-geography-impacts/>；<https://pancanal.com/en/maritime-services/trade-routes/>
- **#26** 「With the changes consequent upon the canal, this indifference will diminish. We also shall be entangled in the…」  
  判断：**正确**。美国以门罗主义承担区域警察角色并实际介入加勒比事务，国际义务与负担增加已出现；后来转向不干涉并不抹去此前已经发生的卷入。  
  来源：<https://www.archives.gov/milestone-documents/roosevelt-corollary>；<https://www.degruyterbrill.com/document/doi/10.1515/9781400870462/html>
- **#27** 「when, besides the powerful sentimental impulse, it is remembered that beneath considerable differences of poli…」  
  判断：**正确**。英美在世界大战中形成高度整合的联合行动，协调成为现实；早期封锁与海军竞争是反向阶段，但未阻止这项无明确终点的趋近判断在观测窗内实现。  
  来源：<https://kansaspress.ku.edu/9780700633180/>；<https://www.cambridge.org/core/books/british-naval-supremacy-and-angloamerican-antagonisms-19141930/A090D59DA6245C6B9085CAFD17712A34>
- **#29** 「experience cannot be had before that further development of the facts which will follow the not far distant da…」  
  判断：**正确**。美国因海外战争结束原有近乎隔离的国际地位，走向海洋及海外行动；反帝联盟虽形成，但未阻止这一转向。  
  来源：<https://history.state.gov/departmenthistory/short-history/superpower>；<https://guides.loc.gov/world-of-1898/anti-imperialist-league>
- **#30** 「in that process of adjusting the parts to be played by each nation, upon which alone a satisfactory cooperatio…」  
  判断：**正确**。英美合作深化期间的政治军事分歧及苏伊士危机严重破裂，直接证实调整合作角色时会有摩擦；没有引用误检的同名矿业公司。  
  来源：<https://link.springer.com/chapter/10.1007/978-1-349-17579-6_3?code=802042cf-a1ae-473b-aea1-597c9da94556&error=cookies_not_supported>；<https://link.springer.com/article/10.1007/s42533-024-00162-9>
- **#31** 「there is no immediate danger of the leading peoples turning their swords into ploughshares」  
  判断：**正确**。海牙会议的成果远低于制止陆军军备增长的目标，后来虽有条约式军备控制，也不是强国近期全面解除武装。全面裁军未发生与有限军控同时存在并不矛盾。  
  来源：<https://researchrepository.murdoch.edu.au/id/eprint/55185>；<http://etheses.lse.ac.uk/319/1/Keefer_Great%20Britain%20and%20Naval%20Arms%20Control.pdf>
- **#32** 「In this same pregnant strife the United States doubtless will be led, by undeniable interests and aroused nati…」  
  判断：**正确**。美国实际参加欧洲大战并提出战后和平安排，已越过不参加欧洲纷争的界线；参议院拒绝凡尔赛安排说明承诺有反复，不否定已经实现的参与。  
  来源：<https://history.state.gov/departmenthistory/short-history/war>；<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>
- **#37** 「If such coincidence there be, however, it is indicative not of a deliberate purpose, but of a commencing chang…」  
  判断：**正确**。海军胜利带来海外领地与海上优势，海权成为美国对外活动要素；裁军与预算不足的阶段反复不等于美国活动重新永久局限国内。  
  来源：<https://www.usni.org/magazines/naval-history-magazine/2013/january/new-navy-new-power>；<https://digital-commons.usnwc.edu/cgi/viewcontent.cgi?article=7974&context=nwc-review>
- **#38** 「nations have international duties as well as international rights, and that international complications will a…」  
  判断：**正确**。美国卷入欧洲战争及其战后国际责任已有明确记录。战间期孤立与中立政策是阶段性反复，不推翻观测窗内已发生的国际卷入。  
  来源：<https://history.state.gov/departmenthistory/short-history/war>；<https://www.archives.gov/files/legislative/resources/education/foreign-policy-1920-2020/timeline-small.pdf>；<https://doi.org/10.1093/acrefore/9780199329175.013.49>
- **#39** 「her probable dependence in the near future upon an Isthmian canal for the freest and most copious intercourse …」  
  判断：**正确**。经济回顾明确记载运河为美国两岸间贸易带来巨大成本节约并承担大量货运，支持其成为两岸交通要道；不将其夸成所有交通方式都被完全替代。  
  来源：<https://www.library.hbs.edu/working-knowledge/panama-canal-troubled-history-astounding-turnaround>；<https://www.hbs.edu/faculty/Pages/item.aspx?research=7357>
- **#41** 「however diverse the modes of operation, all have a common characteristic, in that they bear the stamp of the n…」  
  判断：**正确**。欧洲对外扩张继续发展到战前及战后的高峰，随后转为撤退与非殖民化。原句有达到调整为止的界限，不能擅自解释成殖民扩张必须永久持续。  
  来源：<https://doi.org/10.4324/9780203930182-42>；<https://assets.press.princeton.edu/chapters/s10963.pdf>
- **#43** 「Do we ourselves realize that, happy as the issue of our intervention has been, it may entail upon us greater r…」  
  判断：**正确**。后续委内瑞拉危机及其仲裁促成罗斯福推论，扩展美国区域警察责任，符合责任与行动加重；没有把出版前那次边界争端本身算作预测应验。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/09592290903293738>；<https://history.state.gov/milestones/1899-1913/roosevelt-and-monroe-doctrine>
- **#49** 「That the impress of Christianity will remain throughout the coming century is reasonably as certain as that it…」  
  判断：**正确**。欧洲及美国在二十世纪以后仍保有广泛基督教归属，世俗化研究也不支持信仰影响会迅速一概消失。原句容许信仰减弱，因而不以基督徒比例下降否定文化印记持续。  
  来源：<https://academic.oup.com/edited-volume/37088/chapter/323198004>；<https://doi.org/10.1093/oxfordhb/9780198834267.013.14>；<https://www.pewresearch.org/religion/2025/02/26/decline-of-christianity-in-the-us-has-slowed-may-have-leveled-off/>；<https://www.pewresearch.org/religion/2024/03/15/8-in-10-americans-say-religion-is-losing-influence-in-public-life/>
- **#52** 「Nor, with the recent resuscitation of the Turkish army before men's eyes, can it be thought unlikely that the …」  
  判断：**正确**。中国后来形成经过组织重建与现代化的强大区域军事力量，符合将人口和国家潜力组织成有效军力的结果。军阀割据是中间阶段；原句没有要求从出版日起始终统一，也未要求打败所有其他国家。  
  来源：<https://www.congress.gov/crs-product/R46808>；<https://doi.org/10.1353/tcc.2022.0008>
- **#53** 「Comparative slowness of evolution may be predicated, but that which for so long has kept China one, amid many …」  
  判断：**正确**。中国后来的国家整合及巨大经济规模和全球影响有存档记载，实质凝聚并放大整体行动影响的主要结果已经出现。与军事组织预测采用相同无终点口径，不因中间军阀分裂就把最终实现自动降为部分符合，也不把实质统一夸成所有旧疆域均完整保留。  
  来源：<https://press-files.anu.edu.au/downloads/press/n11724/pdf/ch13.pdf>；<https://referenceworks.brill.com/display/entries/BECO/SIM-00160.xml>；<https://bristoluniversitypressdigital.com/view/journals/gd/14/2-3/article-p316.xml>
- **#57** 「When we begin really to look abroad, and to busy ourselves with our duties to the world at large in our genera…」  
  判断：**正确**。英美和解形成稳定合作，后来共同组织联合战争行动，符合美国参与世界事务时向英国合作的结果。海军竞争说明合作并非无摩擦，不否定实际伸手合作。  
  来源：<https://www.degruyterbrill.com/document/doi/10.1515/9781400834419-005/html>；<https://doi.org/10.5287/ora-qmwydvkv2>；<https://kansaspress.ku.edu/9780700633180/>
- **#61** 「the gradual broadening and tightening hold upon the sentiment of American democracy of that conviction loosely…」  
  判断：**正确**。美国加强门罗主义下的区域角色，同时建成强大海军并与英国开展实质合作和集体防御。这里只核验强海权及英美联系出现，不把单一思想必然导致建军的因果解释另算成功。  
  来源：<https://www.usni.org/magazines/proceedings/1914/july/half-century-naval-administration-america-1861-1911>；<https://history.state.gov/milestones/1937-1945/atlantic-conf>；<https://history.state.gov/milestones/1945-1952/nato>；<https://history.state.gov/milestones/1899-1913/roosevelt-and-monroe-doctrine>
- **#62** 「in the Mediterranean at present the Sea Powers, Great Britain, France, and Italy, are opposed to the Land Powe…」  
  判断：**正确**。德国虽介入委内瑞拉封锁，却不足以夺取并维持领地，英国才是该行动主要力量，美国随后主导区域。有限介入并不等于大陆诸强像在地中海那样主导加勒比。  
  来源：<http://hdl.handle.net/11244/11968>；<https://www.historytoday.com/archive/feature/1902-blockade-venezuela>；<https://www.gilderlehrman.org/history-resources/essays/united-states-and-caribbean-1877-1920>
- **#63** 「when it shall be pierced by a canal, it will present a maritime centre analogous to the mouth of the Mississip…」  
  判断：**正确**。运河局记载其连接广泛国际航线与港口，联合国贸发会议亦把该运河中断视为全球运输冲击；地峡成为航运枢纽已经实现。干旱等运营风险不是尚未成为枢纽的证据。  
  来源：<https://pancanal.com/en/celebrates-110-years-of-trust-and-progress/>；<https://unctad.org/system/files/official-document/osginf2024d2_en.pdf>

### 部分符合（19 条）

- **#4** 「Every position in that sea will have enhanced commercial and military value, and the canal itself will become …」  
  判断：**部分符合**。运河防御确实成为重要军事议题，证明运河自身战略地位这一部分；但证据未逐一覆盖加勒比各据点的商业与军事价值上升，不能将运河价值外推到每一处据点。后来评析又记载新式战争削弱其原有军事重要性，作为边界保留。  
  来源：<https://www.usni.org/magazines/proceedings/1980/january/military-aspects-panama-canal-issue>；<https://www.foreignaffairs.com/articles/panama/1959-04-01/control-panama-canal-obsolete-shibboleth>
- **#6** 「To protect and develop its own, each nation will seek points of support and means of influence in a quarter wh…」  
  判断：**部分符合**。德国寻找加勒比基地、美国购买并预占据点以阻止德国的竞争都有记录，证实多国争夺这一部分；证据不足以把各国逐一都寻求据点的宽泛表述整体判对。  
  来源：<https://www.usni.org/magazines/proceedings/1917/july/international-notes-naval-war-notes>；<https://www.usni.org/magazines/naval-history-magazine/2006/august/roosevelts-pursuit-temperate-caribbean-policy>
- **#11** 「Formal alliance between the two is out of the question, but a cordial recognition of the similarity of charact…」  
  判断：**部分符合**。大西洋宪章确认两国合作，但两国随后同为北约集体防御条约成员，否定不会正式结盟这一子项；合作成真不能抵消正式联盟预测失准。  
  来源：<https://history.state.gov/milestones/1945-1952/nato>；<https://history.state.gov/milestones/1937-1945/atlantic-conf>
- **#12** 「China, however, may burst her barriers eastward as well as westward, toward the Pacific as well as toward the …」  
  判断：**部分符合**。中国向太平洋方向扩大海洋领土主张有存档记录，向欧洲大陆方向突破旧疆界的另一半未获证实，陆地边界研究反而记载多次妥协让步；不以西藏整合冒充向欧洲扩张。  
  来源：<https://www.geostrategy.org.uk/all-research/the-south-china-sea-historical-and-legal-background/>；<https://chinaindiaborderdispute.wordpress.com/wp-content/uploads/2010/07/fravelchinaborders.pdf>
- **#17** 「The radical identity of spirit which underlies our superficial differences of polity surely will draw us close…」  
  判断：**部分符合**。英美关系趋近及合作确有成果，但两国间也存在海军竞争；美国战后单独拥有无人可挑战的海上优势，不等于英美共同主导的全部命题得到证明。  
  来源：<https://history.state.gov/milestones/1937-1945/atlantic-conf>；<https://www.cambridge.org/core/books/british-naval-supremacy-and-angloamerican-antagonisms-19141930/A090D59DA6245C6B9085CAFD17712A34>；<https://digital-commons.usnwc.edu/nwc-review/vol48/iss3/6/>
- **#18** 「control will abide still with those whose ships, whose capital, whose traders support the industrial system of…」  
  判断：**部分符合**。美国资本、工业利益与海军协同扩张并取得部分岛屿及运河控制得到记录。但全区控制并不等同同一主体、同一层次的控制，运河法律主权后来移交巴拿马；仅确认部分地区与阶段，不以美国海上影响替代整个西印度群岛和地峡的政治经济控制。  
  来源：<https://www.gilderlehrman.org/history-resources/essays/united-states-and-caribbean-1877-1920>；<https://www.cfr.org/articles/who-controls-panama-canal>
- **#20** 「The chief political result of the Isthmian Canal will be to bring our Pacific coast nearer, not only to our At…」  
  判断：**部分符合**。运河确实缩短两洋航程，但存档明确指出现代大型航母不能通行，因而不能把商船距离收益无条件推及所有强大海军的机动能力；仅部分军舰与时期符合。  
  来源：<https://pancanal.com/en/maritime-services/trade-routes/>；<https://www.usni.org/magazines/proceedings/1954/may/panama-canal-auxiliary-fleet>
- **#28** 「There is yet another noteworthy condition common to the two states, which must tend to incline them towards a …」  
  判断：**部分符合**。两国实际形成联合行动和海上反潜合作，但美国也为欧洲战场扩建大规模陆军；共同免于庞大陆军负担的前提描述不成立，不能将合作结果当作整个地理解释均正确。  
  来源：<https://kansaspress.ku.edu/9780700633180/>；<https://scholarcommons.scu.edu/historical-perspectives/vol18/iss1/11>；<https://www.army.mil/article/185229/world_war_i_building_the_american_military>
- **#33** 「Whate'er betide, Sea Power will play in those days the leading part which it has in all history, and the Unite…」  
  判断：**部分符合**。美国长期从本土与海外前沿投送海军力量，海上基地与前沿行动这一部分得到确认；空中、核与太空力量改变军力结构，不能仅用海军仍然重要来证明海权始终居全面主导地位。  
  来源：<https://www.cna.org/reports/2021/08/Sea-Changes-Transforming-US-Navy-Deployment-Strategy-1775-2002.pdf>；<https://seer.ufrgs.br/index.php/austral/article/download/113269/66027/501284>
- **#36** 「In the same way it may be asserted quite confidently that the concession of immunity to what is unthinkingly c…」  
  判断：**部分符合**。英国作为领先海权确曾反对普遍海上私产豁免，但美国在扩大海军、马汉自称国力已强时仍坚持推动该原则。拒绝全面豁免并非所有自信海权国家永不接受的普遍定律；美国倡议也不冒充已缔结普遍豁免条约。  
  来源：<https://www.usni.org/magazines/naval-history-magazine/2017/december/mahans-interference-us-policy>；<https://avalon.law.yale.edu/20th_century/hague11.asp>
- **#42** 「That we shall seek to secure the peaceable solution of each difficulty as it arises is attested by our whole h…」  
  判断：**部分符合**。美国曾成功调停外国战争，同时也在海外持续介入并产生新冲突；但部分调停事例不证明每项争端都寻求和平，因此仅确认和平斡旋与新纠葛并存的部分。  
  来源：<https://millercenter.org/president/roosevelt/foreign-affairs>；<https://www.usni.org/magazines/naval-history-magazine/2021/august/never-known-day-peace>
- **#51** 「in India, though there be no probability of the old mutinies reviving, there are signs enough of the awaking o…」  
  判断：**部分符合**。印度政治觉醒及独立运动符合重大政治变化的方向，但皇家印度海军后来也出现与独立运动相联系的兵变。只确认政治觉醒这一部分，不把未再发生旧式兵变的附属判断整体确认；也不宣称后一次兵变与旧兵变的动机完全相同。  
  来源：<https://countrystudies.us/india/19.htm>；<https://snr.org.uk/the-mutiny-of-the-royal-indian-navy-at-bombay-in-february-1946/>
- **#54** 「Our material advantages, once noted, will be recognized readily and appropriated with avidity; while the spiri…」  
  判断：**部分符合**。中国吸收技术并推进军力现代化是已观察的物质转变，但基督教在中韩社会的活力及其参与经济政治变化，反驳东方整体长期拒绝西方精神观念的概括。只确认技术采用等部分，不把宗教人数代替全部伦理。  
  来源：<https://www.congress.gov/crs-product/R46808>；<https://brill.com/view/journals/ijac/4/1/article-p5_5.xml?language=en>；<https://www.journals.uchicago.edu/doi/pdf/10.1086/599246>
- **#55** 「The peoples of European civilization, after a period of comparative repose, are again advancing all along the …」  
  判断：**部分符合**。欧洲力量在中国沿海取得租借地并直接接触东方古国，但缓冲地带并未全部成为直接统治领地，阿富汗等仍保留特定政治地位。接触增强成立，普遍吞并缓冲地带的宽断言只部分成立。  
  来源：<https://thechinaproject.com/2022/05/25/frances-hong-kong-the-leased-territory-of-guangzhouwan/>；<https://www.iranicaonline.org/articles/anglo-russian-convention-of-1907-an-agreement-relating-to-persia-afghanistan-and-tibet/>；<https://www.cambridge.org/core/books/abs/cambridge-history-of-china/foreign-presence-in-china/31F0E7708B288E2DCFDBC5EFC42973AC>
- **#56** 「Mr. Balfour has used an expression, "race patriotism,"--a phrase which finds its first approximation, doubtles…」  
  判断：**部分符合**。北约条约确实把英语国家与其他西方国家置于共同文明和集体防御框架，相关研究也讨论其种族化边界。但正式联盟并非可无条件等同所有同源文明国家的族群爱国主义，只确认跨英语国家的部分扩展。  
  来源：<https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/1949/04/04/the-north-atlantic-treaty>；<https://academic.oup.com/ia/article-abstract/100/2/491/7617203>
- **#58** 「Wherever situated, whether at Panama or at Nicaragua, the fundamental meaning of the canal will be that it adv…」  
  判断：**部分符合**。运河和配套交通确实把两洋及美洲多地贸易网络连接起来，但贸易通达不等于整个美洲国家体系在政治文明层面得到无可替代的统一，只能确认交通商业联系加强这一部分。  
  来源：<https://pancanal.com/en/connectivity/>；<https://www.trade.gov/market-intelligence/panama-panama-canal>
- **#60** 「The Isthmus, with all that depends upon it,--its canal and its approaches on either hand,--will link the easte…」  
  判断：**部分符合**。运河早期为美国两岸货运带来巨大成本收益，但经济史也明确记载铁路技术及公路网降低其比较优势，陆水联运仍是竞争路线。运河贡献成立，任何陆路网络永不能匹敌的无条件上限不能整体确认。  
  来源：<https://www.library.hbs.edu/working-knowledge/panama-canal-troubled-history-astounding-turnaround>；<https://www.ams.usda.gov/sites/default/files/media/Impact%20of%20Panama%20Canal%20Expansion%20on%20the%20U.S.%20Intermodal%20System.pdf>
- **#64** 「It can never be the ultimate base of operations, as Pensacola or New Orleans can, because it is an island, a s…」  
  判断：**部分符合**。基韦斯特后来成为有效的海军与航空活动基地，且引水管道改变了原文缺水的限制；但普通作战或训练基地不自动等于原文的最终作战基地。仅确认前沿实用性，不贸然将这个未定义的上限判为已完全推翻或完全证明。  
  来源：<https://cnrse.cnic.navy.mil/Installations/NAS-Key-West/About/History/>；<https://keysweekly.com/42/keys-history-arrival-of-fresh-water-brought-relief-to-the-island-chain/>
- **#66** 「The same probable neutrality must be admitted for the remaining positions that have been distinguished: Mujere…」  
  判断：**部分符合**。圣托马斯后来归美国并有海军设施，不能继续整体视为政治中立的三地组合。但关于圣托马斯的反例不能代替对穆赫雷斯和萨马纳两地分别下结论，因此不把全组一概判错。  
  来源：<https://www.ibiblio.org/hyperwar/NHC/bases/bases-18.htm>；<https://www.usni.org/magazines/proceedings/1931/april/american-interests-west-indies>

### 错误（10 条）

- **#13** 「Whether the canal of the Central American isthmus be eventually at Panama or at Nicaragua matters little to th…」  
  判断：**错误**。最终决策选择巴拿马而非尼加拉瓜，路线与原预测相反；没有因运河终究建成而给该路线预测加分。  
  来源：<https://www.sil.si.edu/Exhibitions/Make-the-Dirt-Fly/chooseroute.html>
- **#23** 「Under such conditions, perhaps not yet come, but plainly coming, the consequence of an artificial waterway tha…」  
  判断：**错误**。芝加哥大学所藏运河资料列纽约至旧金山由13,135海里减至5,262海里，节省7,873海里，明确称三分之五，而非预测的三分之二。具体缩短比例失准，不能因航程都缩短就按数量级给部分符合；另一书的英里粗数不用于替代注明海里的对照表。  
  来源：<https://www.lib.uchicago.edu/ead/pdf/century0463.pdf>；<https://www.czbrats.com/AmPan/chap20.htm>
- **#34** 「It is improbable that control ever again will be exercised, as once it was, by a single nation. Like the petti…」  
  判断：**错误**。海军战争学院研究明确记载战后没有任何国家能够在公海挑战美国海军。单一国家再度取得海上压倒性优势，否定不会再由一国掌控的主干断言，后来竞争恢复不能消除反例。  
  来源：<https://digital-commons.usnwc.edu/nwc-review/vol48/iss3/6/>；<https://www.cambridge.org/core/books/british-naval-supremacy-and-angloamerican-antagonisms-19141930/A090D59DA6245C6B9085CAFD17712A34>
- **#35** 「I have on another occasion said that the principle that the flag covers the goods is forever secured--meaning …」  
  判断：**错误**。巴黎宣言规定中立旗保护非禁运敌货，但美国外交存档明确记载英国在法律上并未宣布封锁的情况下扣留非禁运货物。原句不仅预言法律文本存在，还断言海权不足以武力违背它；实际强制扣货否定这种永久安全保证，并非将合法禁运品例外误作违规。  
  来源：<https://ihl-databases.icrc.org/en/ihl-treaties/paris-decl-1856/declaration>；<https://history.state.gov/historicaldocuments/frus1915Supp/d195>；<https://history.state.gov/historicaldocuments/frus1916Supp/d602>
- **#40** 「Yet the interests exist, and the navy is growing; and in the latter fact is the best surety that no breach of …」  
  判断：**错误**。海军增长并未保证维护海外利益不致破坏和平：美国实际通过美西战争取得海外权益。威慑是政策目的而非无战争的已实现结果。  
  来源：<https://history.state.gov/milestones/1866-1898/spanish-american-war>；<https://www.usni.org/magazines/naval-history-magazine/2022/april/theodore-roosevelts-great-power-navy>
- **#44** 「the chief military power of which must lie ever in navies, never an aggressive factor such as armies have been…」  
  判断：**错误**。英美后来都依靠大规模陆军动员，而苏伊士入侵包含海上登陆与海军陆战队行动。海军永为主要力量且从不成为侵略因素的绝对组合断言不成立；并非用平时与战时口径混算军种人数。  
  来源：<https://www.army.mil/article/185229/world_war_i_building_the_american_military>；<https://nzhistory.govt.nz/war/united-kingdom-facts>；<https://www.nam.ac.uk/explore/suez-crisis>
- **#46** 「Of invasion, in any real sense of the word, we run no risk, and if we did, it must be by sea;」  
  判断：**错误**。日本对阿留申群岛的实际入侵和占领反驳美国本土无真正入侵风险的主干否定句。这不是把边境小股袭扰当作全面占领；入侵来自海上只吻合其后附带的路线判断，不能挽救无风险断言。  
  来源：<https://www.nationalww2museum.org/visit/exhibits/special-exhibits/american-shores-aleutian-islands-campaign>；<https://history.army.mil/Research/Reference-Topics/Army-Campaigns/Brief-Summaries/Mexican-Expedition/>
- **#47** 「in a small navy, as ours, relatively, long will be, this is doubly imperative;」  
  判断：**错误**。同期海军史明确记载美国造舰在出版后大幅加速，舰队增长快于除英国外的海军；后来的回顾又记载美国达到世界第二海军地位，与长期相对较小相反。  
  来源：<https://www.usni.org/magazines/proceedings/1914/july/half-century-naval-administration-america-1861-1911>；<https://www.usni.org/magazines/naval-history-magazine/2022/april/theodore-roosevelts-great-power-navy>
- **#65** 「Holland is a small state, unlikely to join again in a general war.」  
  判断：**错误**。荷兰在世界大战中遭德国实际入侵并作战，已构成参加全面战争的反例；另一次大战保持中立不能证明以后都不大可能参战，原句也未限定必须主动开战。  
  来源：<https://www.annefrank.org/en/anne-frank/go-in-depth/german-invasion-netherlands/>；<https://en.wikipedia.org/wiki/Netherlands_in_World_War_I>
- **#67** 「Samana Bay, because, although the island on which it is is large and productive, it has not now, and gives no …」  
  判断：**错误**。萨马纳所在多米尼加的经济扩张与商业增长得到世行和国际货币基金组织回顾确认，与看不到商业繁荣希望的主要悲观判断相反。未用海地情况代替多米尼加，也未声称整座岛屿已经同样实现政治稳定。  
  来源：<https://documents1.worldbank.org/curated/en/099072523145018880/pdf/P176709-452d1173-eea1-43a4-8ae7-6718fe03a5af.pdf>；<https://www.elibrary.imf.org/view/journals/024/2009/002/article-A004-en.xml>

### 暂无法判断（9 条）

- **#8** 「It has been said that, in our present state of unpreparedness, a trans-isthmian canal will be a military disas…」  
  判断：**暂无法判断**。实际开通前美国经历海军扩建，运河两端也修筑炮台与陆上防御，保持原有无准备状态的前提没有原样持续。不能把后来没有发生所述灾难当作无条件反证。  
  来源：<https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-023/h-023-1.html>；<https://warhistory.org/article/panama-canal-zone-defences-i>
- **#10** 「Whatever temporary aberration may occur, a return to mutual standards of right will certainly follow.」  
  判断：**暂无法判断**。苏伊士争执及此后修复关系有明确记录，但恢复合作不等于回到共同正义标准。原文未界定该标准与判定阈值，第二轮仍无法把道德判断转成同口径事实。  
  来源：<https://theconversation.com/suez-crisis-shows-what-happens-when-friends-dont-share-65844>；<https://api.parliament.uk/historic-hansard/commons/1957/apr/01/bermuda-talks-1>
- **#16** 「If to these safeguards be added, on our part, a sober recognition of what our reasonable sphere of influence i…」  
  判断：**暂无法判断**。美国区域优势及拉美反干涉行动都可观察，但合理势力范围、公正对待外方利益没有共同可操作定义。后来的不干涉协议也不足以证明整段复合前提已满足，不能把一般霸权直接判作条件预测正确。  
  来源：<https://history.state.gov/milestones/1899-1913/roosevelt-and-monroe-doctrine>；<https://doi.org/10.1590/s0102-85292013000200006>；<https://www.encyclopedia.com/history/dictionaries-thesauruses-pictures-and-press-releases/buenos-aires-peace-conference>
- **#19** 「So far as these changes are purely commercial, they will operate to some extent to the disadvantage of Great B…」  
  判断：**暂无法判断**。美国商业运输获得便利及英方对通行待遇的抗议均有资料，但这些并非英国商业净受损的同口径结果。第二轮找到的竞争研究含开通前推测，经济回溯主要计量美国收益，仍缺英国相对损失的决定性事实。  
  来源：<https://history.state.gov/historicaldocuments/frus1912/d665>；<https://doi.org/10.1163/9789004274273_007>；<http://bdigital.binal.ac.pa/bdp/The%20Panama%20canal%20and%20Inter1.pdf>；<https://www.library.hbs.edu/working-knowledge/panama-canal-troubled-history-astounding-turnaround>
- **#22** 「So long as the United States jealously resents all foreign interference in the Isthmus, and at the same time t…」  
  判断：**暂无法判断**。美国实际重新谈判运河条约、制定控制政策并显著加速造舰，原句不制定政策或发展实力的前提并未持续。英方后来让出权利不能用来直接判定这个未保持前提的条件预测错误。  
  来源：<https://www.theodorerooseveltcenter.org/encyclopedia/foreign-affairs/hay-pauncefote-treaty/>；<https://history.state.gov/historicaldocuments/frus1901/d233>；<https://www.usni.org/magazines/proceedings/1914/july/half-century-naval-administration-america-1861-1911>
- **#45** 「As regards Canada, Great Britain maintains a standing army; but, like our own, its numbers indicate clearly th…」  
  判断：**暂无法判断**。英国确有欧洲大陆派兵与海外入侵，但派遣陆军不自动等于侵略，苏伊士又可能落在原句明列的遥远海区例外中。第二轮仍缺既明确属侵略又明确排除该地理例外的同口径事实，不能拿布尔战争或一般参战直接判错。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/09592296.2023.2188794>；<https://www.nam.ac.uk/explore/suez-crisis>；<https://www.degruyterbrill.com/document/doi/10.1515/9781685858643-004/html>
- **#48** 「The firmness with which the position of the former statesman has been maintained ever since by the great body …」  
  判断：**暂无法判断**。两轮共四条自适应查询找到门罗主义的反再殖民政策、美国区域霸权和欧洲继续保持文化经济联系的记载，但这些均不能代替对独立西属美洲国家后来是否被欧洲重新政治殖民的明确结果核查。仍缺直接覆盖该结果的历史综述；不以政策目标、欧洲影响或检索未见反例充当预测正确的证据。  
  来源：<https://routledgelearning.com/internationalhistory20c/students/chapter-5-good-neighbors-the-united-states-and-the-americas-1900-45/>；<https://www.cambridge.org/core/journals/americas/article/latin-america-and-europe-in-the-twentieth-century-looking-to-the-americas-archives/29E73B033285C69621AB6586BAB01925>；<https://www.foreignaffairs.com/articles/central-america-caribbean/1929-01-01/latin-america-europe-and-united-states>
- **#50** 「gradual likewise, granting the utmost possible spread of Christian beliefs among them, will be the approximati…」  
  判断：**暂无法判断**。亚洲基督徒人数与传播有资料，但人数不是国家整体接近基督教伦理原则的指标。最大限度传播在句中是让步而非可直接宣布未触发的事件前提；第二轮仍未得到同口径伦理变化速度的界定与实测。  
  来源：<https://www.gordonconwell.edu/blog/christianity-in-asia/>；<https://www.pewresearch.org/religion/2006/10/05/overview-pentecostalism-in-asia/>
- **#59** 「On the side of the land, these great armies, and the blind outward impulse of the European peoples, are the as…」  
  判断：**暂无法判断**。欧洲战争和苏联向东欧扩展有记录，但原文的基督教文明防线与外部力量未给出清楚边界；俄罗斯在相关文明分类中本就有争议。不能把欧洲内部战争或苏联占领不加定义地当作外部攻破文明堡垒。  
  来源：<https://www.thebritishacademy.ac.uk/documents/1562/06_Kershaw_1817.pdf>；<https://encyclopedia.ushmm.org/content/en/article/the-soviet-union-and-europe-after-1945>；<https://doi.org/10.14712/23363525.2014.35>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/mahan-interest-of-america-in-sea-power-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/mahan-interest-of-america-in-sea-power-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/mahan-interest-of-america-in-sea-power-v5/audit/manual_review_2026-11-15.py`
注意：canonical报告统计中的“候选67”指可核验层；实际导入候选79（含12条unclear）。TXT章节THE ISTHMUS日期与目录及总出版年冲突，原文未改。
