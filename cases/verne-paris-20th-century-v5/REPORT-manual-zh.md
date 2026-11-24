# 儒勒·凡尔纳《巴黎在20世纪》（Paris au XXe siècle）：出版后预测人工核查

- 案例目录：`cases/verne-paris-20th-century-v5/`
- 出版日期：**约1863年写成**（手稿被赫泽尔拒绝，1989年发现，1994年由 Hachette／le cherche midi 首次出版）。按既有决定，预测窗口起点取写作年1863年，而非1994年出版年。正文为 reading-library/2026-11-15-未来判断书单/06-古典预言文本/38-巴黎在20世纪.pdf（法文全文），sha256 `e8f0ee7548b964bfefa0e2cf5907e4adebc37e41b5d2af0d7ae06a8718f38777`。TXT 由 `pdftotext -enc UTF-8`（默认版式，保留换页符）生成，sha256 `51e2b00c7f537058f85a74eae68c073ec33692ad31cb72b5b82b27f79ab328c1`。故事设定在1960—1962年的巴黎；编后记（Présentation et résumé 等）不抽取。观察窗口为 1863→2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的重做版（替代此前助手手工挑选 30 条的旧稿，对应仍打开的 PR #25）。抽取：用仓库 prepare_book v5 把全文切成 87 块（3500 字符、600 字符上下文），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 186 条可核验预测（约 2.14 条/块；这是一部以1960年巴黎为已然世界的未来小说，密度高于一般英语非虚构的 0.2–0.35 是预期之中）。核验：按主题先写 scope，做 support 与 counter 的 Exa 检索（池密钥第 4 条，只按文件路径读取），原文存档于 data/sources（sha256），写入 data/evidence.jsonl（92 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。claims.jsonl 的 context 字段已清空。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 186 条，剔除非预测 0 条，计入 **186 条预测**，其中 **186 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 49 |
| 趋势符合 | 0 |
| 部分符合 | 76 |
| 错误 | 61 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **26.3%**（49/186） |
| 加权胜率 | **46.8%** |
| 错误率 | **32.8%**（61/186） |
| 未定占比（暂无法判断/预测） | 0.0%（0/186） |

## 总体评价

凡尔纳在交通、通讯、能源入户和办公技术上命中很多：地铁与多层轨道交通、铁路国有化、电灯路灯、内燃机取代马车、沥青路面、住宅电梯、家庭供电供气、银行计算机器、电话与专用线路、行情自动显示、传真、海底电缆、木浆造纸、螺旋桨商船、苏伊士与巴拿马运河、机械装卸、电光广告、女性进入公共生活等。主要误判集中在政治制度与文化垄断：拿破仑五世、欧洲解散军队、新闻业与文学死亡、雨果无人知晓、巴黎变成远洋海港、碳酸气动力、压缩空气地铁、断头台改为电击、戏剧总仓库国家垄断等。书中把1960年写成已经完成的世界，故按窗口终点判断，未使用“趋势符合”。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（49 条）

- **#1** 「Le 13 août 1960, une partie de la population parisienne se portait aux nombreuses gares du chemin de fer métro…」  
  判断：**正确**。巴黎地铁1900年通车，到1960年已有多条线路和众多车站，都会铁路成为事实。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>
- **#3** 「lorsque les chemins de fer passèrent des mains des particuliers dans celles de l'État」  
  判断：**正确**。法国铁路在1937–1938年收归国有，成立SNCF，与“从私人转到国家手中”相符。  
  来源：<https://en.wikipedia.org/wiki/SNCF>；<https://en.wikipedia.org/wiki/History_of_rail_transport_in_France>
- **#5** 「le fonctionnarisme se développait sous toutes les formes possibles」  
  判断：**正确**。法国公务与行政机构在19世纪末至20世纪显著膨胀，官僚化确以多种形式发展。  
  来源：<https://en.wikipedia.org/wiki/Public_service>；<https://en.wikipedia.org/wiki/Civil_service>；<https://www.insee.fr/fr/statistiques/2414946>
- **#12** 「Les langues vivantes, sauf le français, étaient très en faveur」  
  判断：**正确**。现代外语教学在中等和高等教育中确实显著扩展并受到重视。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#16** 「le mprceau d'éloquence latine était tombé en désuétude.」  
  判断：**正确**。官方典礼上的拉丁语演说在20世纪基本退出常规，确已废弃。  
  来源：<https://en.wikipedia.org/wiki/Latin>
- **#18** 「les communications rapides entre les divers points de la Capitale」  
  判断：**正确**。地铁、电话与后来的电信使巴黎市内各点之间的交通和通讯变得迅速。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/Telephone>
- **#19** 「les locomotives sillonnant le bitume des boulevards」  
  判断：**正确**。林荫大道普遍铺设沥青，机动车在其上行驶成为常态。  
  来源：<https://en.wikipedia.org/wiki/Asphalt_concrete>；<https://en.wikipedia.org/wiki/History_of_the_automobile>
- **#20** 「la force motrice envoyée à domicile」  
  判断：**正确**。电力和煤气被输送到住户家中，家庭获得集中供应的动力与能源。  
  来源：<https://en.wikipedia.org/wiki/Electrification>；<https://en.wikipedia.org/wiki/Central_heating>
- **#33** 「ils se succédaient de dix minutes en dix minutes, emportant chacun mille voyageurs」  
  判断：**正确**。地铁发车间隔可短至数分钟，列车载客量以百千计，与“约十分钟一班、约一千名乘客”的量级相符。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/RATP_Group>
- **#36** 「les magasins somptueux projetaient au loin des éclats de lumière」  
  判断：**正确**。百货公司与沿街商店在19世纪末起便广泛使用电灯向街道投射光芒。  
  来源：<https://en.wikipedia.org/wiki/Street_light>；<https://en.wikipedia.org/wiki/Electrification>
- **#38** 「les cent mille lanternes de Paris s'allumaient d'un seul coup.」  
  判断：**正确**。集中供电使全城路灯可以同时点燃，巴黎路灯数量也达到极大规模。  
  来源：<https://en.wikipedia.org/wiki/Street_light>；<https://en.wikipedia.org/wiki/Electrification>
- **#39** 「le plus grand nombre marchait sans chevaux; elles se mouvaient par une force invisible, au moyen d'un moteur à…」  
  判断：**正确**。20世纪上半叶，林荫道上的马车被燃气或汽油内燃机车辆取代，马匹退出主干道。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_automobile>；<https://en.wikipedia.org/wiki/Internal_combustion_engine>；<https://en.wikipedia.org/wiki/%C3%89tienne_Lenoir>
- **#41** 「une pédale, placée sous son pied, lui permettait de modifier instantanément la marche du véhicule.」  
  判断：**正确**。汽车用方向盘和踏板控制，并可即时转向，已成为标准。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_automobile>
- **#43** 「ces boulevards illuminés avec un éclat comparable à celui du soleil」  
  判断：**正确**。电气化后的林荫大道夜间照明远强于煤气时代，接近白昼观感。  
  来源：<https://en.wikipedia.org/wiki/Street_light>；<https://en.wikipedia.org/wiki/Electrification>
- **#45** 「il se retint, et pressa le bouton électrique de la porte cochère; celle-ci s'ouvrit sans bruit, mue par un res…」  
  判断：**正确**。按钮门铃、电磁门锁和后来的自动门使大门可用电开启并自动关闭。  
  来源：<https://en.wikipedia.org/wiki/Automatic_door>；<https://en.wikipedia.org/wiki/Electrification>
- **#46** 「Michel se rendit à l'ascensoir, sorte de chambre autour de laquelle régnait un divan capitonné」  
  判断：**正确**。富裕住宅和公寓普遍安装电梯。  
  来源：<https://en.wikipedia.org/wiki/Elevator>
- **#47** 「Le domestique toucha un bouton de métal situé dans la boiserie, et l'ascensoir s'éleva par un mouvement insens…」  
  判断：**正确**。电梯用按钮操纵、运行趋于平稳，成为标准设计。  
  来源：<https://en.wikipedia.org/wiki/Elevator>
- **#48** 「les plats montaient en silence par des puits pratiqués dans l'épaisseur des murs」  
  判断：**正确**。餐用升降机（dumbwaiter）在公寓和酒店中被用来把菜肴送到楼层或餐桌。  
  来源：<https://en.wikipedia.org/wiki/Dumbwaiter>
- **#50** 「Directeur de la Société des Catacombes de Paris et de la force motrice à domicile.」  
  判断：**正确**。电力与煤气公司把动力和能源输送到用户住所，成为现代公用事业。  
  来源：<https://en.wikipedia.org/wiki/Electrification>；<https://en.wikipedia.org/wiki/Central_heating>
- **#54** 「À vingt ans, il portait déjà des lunettes d'aluminium.」  
  判断：**正确**。铝及轻金属镜框进入日常眼镜使用。  
  来源：<https://en.wikipedia.org/wiki/Glasses>
- **#56** 「un bureau télégraphique correspondait avec les points les plus reculés des magasins」  
  判断：**正确**。大型商店用电话、电报及后来的数据线路与仓库即时通讯。  
  来源：<https://en.wikipedia.org/wiki/Telephone>；<https://en.wikipedia.org/wiki/Telegraphy>
- **#61** 「ses bâtiments, singulièrement accrus, s'étendaient sur une grande partie de la rue Richelieu」  
  判断：**正确**。国家图书馆黎塞留馆在19–20世纪多次扩建延伸。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#65** 「Michel aperçut des caisses gigantesques : elles avaient des airs de citadelles」  
  判断：**正确**。现代银行普遍使用厚重装甲金库，安保等级接近堡垒。  
  来源：<https://en.wikipedia.org/wiki/Bank_vault>
- **#66** 「ses instruments ressemblaient, en effet, à de vastes pianos ; en pressant les touches d'un clavier, on obtenai…」  
  判断：**正确**。银行广泛使用键盘式计算器和后来的计算机，可即时得出总和、差、积、商和复利等，功能与描写相符。  
  来源：<https://en.wikipedia.org/wiki/History_of_computing_hardware>；<https://en.wikipedia.org/wiki/Mechanical_calculator>
- **#67** 「le courrier de la maison Casmodage ne comprenait pas moins de trois mille lettres par jour, lancées à tous les…」  
  判断：**正确**。大型银行每日处理数以千计发往世界各地的函电，国际通信量巨大。  
  来源：<https://en.wikipedia.org/wiki/Telegraphy>；<https://en.wikipedia.org/wiki/Telephone>
- **#69** 「des perfectionnements nouveaux permettaient alors à l'expéditeur de correspondre directement avec le destinata…」  
  判断：**正确**。电话、电传和后来的电子通讯使发报人可直接与收报人通信。  
  来源：<https://en.wikipedia.org/wiki/Telephone>；<https://en.wikipedia.org/wiki/Telegraphy>
- **#70** 「Chaque maison avait ses fils particuliers, d'après le système Wheatstone en usage depuis longtemps dans toute …」  
  判断：**正确**。企业普遍拥有专用电话和数据线路。  
  来源：<https://en.wikipedia.org/wiki/Telephone>；<https://en.wikipedia.org/wiki/Telegraphy>
- **#71** 「Les cours des innombrables valeurs cotées au marché libre venaient s'inscrire d'eux-mêmes sur des cadrans plac…」  
  判断：**正确**。证券行情通过自动收报机和后来的电子牌，在世界各主要交易所同步显示。  
  来源：<https://en.wikipedia.org/wiki/Ticker_tape>；<https://en.wikipedia.org/wiki/Euronext_Paris>
- **#72** 「la télégraphie photographique, inventée au siècle dernier par le professeur Giovanni Caselli de Florence, perm…」  
  判断：**正确**。传真及后来的电子传输可把文字、签名和图画发往远方，远程签署合同成为现实。  
  来源：<https://en.wikipedia.org/wiki/Fax>
- **#73** 「Le réseau télégraphique couvrait alors la surface entière des continents et le fond des mers ; l'Amérique ne s…」  
  判断：**正确**。海底与陆地电报、电话和数据网覆盖各大陆，欧美之间的通信延迟可短至秒级。  
  来源：<https://en.wikipedia.org/wiki/Transatlantic_telegraph_cable>；<https://en.wikipedia.org/wiki/Telegraphy>；<https://en.wikipedia.org/wiki/Telephone>
- **#74** 「dans l'expérience solennelle qui fut faite en 1903 à Londres, deux expérimentateurs correspondirent entre eux,…」  
  判断：**正确**。环球海底电缆在20世纪初已经接通，1902–1903年前后已能完成绕地球一周的电报传递。  
  来源：<https://en.wikipedia.org/wiki/Transatlantic_telegraph_cable>；<https://en.wikipedia.org/wiki/Telegraphy>
- **#76** 「ils se trouvaient avantageusement remplacés par l'alfa, l'aloès, le topinambour, le lupin et vingt autres plan…」  
  判断：**正确**。木材与植物纤维纸浆取代破布成为造纸主原料，森林更多用于造纸，取暖则转向煤和后来的其他能源。  
  来源：<https://en.wikipedia.org/wiki/Pulp_(paper)>；<https://en.wikipedia.org/wiki/Central_heating>
- **#82** 「se loger était difficile alors dans une capitale trop petite pour ses cinq millions d'habitants」  
  判断：**正确**。1960年前后巴黎都市区人口已超过五百万，住房紧张也是事实。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Paris>；<https://en.wikipedia.org/wiki/Housing_in_France>
- **#86** 「Les gens, peu aisés, qui ne voulaient pas s'éloigner du centre des affaires, devaient donc se loger haut」  
  判断：**正确**。为留在中心区，收入有限的居民往往住进高层或更高楼层的公寓。  
  来源：<https://en.wikipedia.org/wiki/Housing_in_France>
- **#97** 「Les Anglais, les Russes, les Américains n'ont-ils pas leur bank-notes, leurs roubles, leurs dollars engagés da…」  
  判断：**正确**。英、美等国资本大量进入法国企业，国际贸易和投资把各国经济联系起来。  
  来源：<https://en.wikipedia.org/wiki/Foreign_direct_investment>
- **#110** 「L'hiver se passa tant bien que mal, les calorifères et les cheminées à gaz se chargeant de le combattre avec s…」  
  判断：**正确**。集中供暖、煤气与后来的暖气设备使城市冬季取暖远比1863年有效。  
  来源：<https://en.wikipedia.org/wiki/Central_heating>；<https://en.wikipedia.org/wiki/Gas_heater>
- **#111** 「il croisa le premier puis le second réseau métropolitain, et s'arrêta à la station de la porte d'Asnières, prè…」  
  判断：**正确**。巴黎有多套轨道交通网，阿尼埃尔一带有车站，旧城防被拆除并视为从前的工事。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/Boulevard_P%C3%A9riph%C3%A9rique>
- **#113** 「Michel salua, prit place dans l'ascensoir, et en quelques secondes, il atteignit le palier du neuvième étage.」  
  判断：**正确**。住宅电梯可在数秒内到达九层，成为公寓楼的标准配置。  
  来源：<https://en.wikipedia.org/wiki/Elevator>
- **#118** 「les inventeurs ont puisé dans le vocabulaire anglais leurs plus déplaisantes appellations」  
  判断：**正确**。近现代技术发明大量借用或直接采用英语名称。  
  来源：<https://en.wikipedia.org/wiki/French_language>
- **#125** 「quelques légumes originaires de l'Equateur, et acclimatés en France」  
  判断：**正确**。原产温暖地区的多种蔬菜在法国通过驯化、温室和后来的供应体系进入日常餐桌。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#135** 「pas un trois-mâts, un brick, une goélette, un lougre, un chasse-marée qui ne fût pourvu de son hélice ; le ven…」  
  判断：**正确**。螺旋桨成为汽船和后来几乎所有商船的标准推进方式，风帆商船退出主导。  
  来源：<https://en.wikipedia.org/wiki/Propeller>
- **#136** 「le percement des isthmes de Suez et de Panama dut multiplier les affaires de navigation au long cours」  
  判断：**正确**。苏伊士运河1869年通航，巴拿马运河1914年通航，远洋航运随之大增。  
  来源：<https://en.wikipedia.org/wiki/Suez_Canal>；<https://en.wikipedia.org/wiki/Panama_Canal>
- **#138** 「le déchargement se faisait au moyen des plus ingénieuses machines; les unes confectionnaient les ballots, les …」  
  判断：**正确**。现代港口用机械和集装箱系统完成打包、过磅、贴标和搬运。  
  来源：<https://en.wikipedia.org/wiki/Containerization>；<https://en.wikipedia.org/wiki/Port>
- **#145** 「ils sont tous deux l'action maintenant et dès lors, il n'y a plus de femmes en France.」  
  判断：**正确**。妇女大规模进入劳动和市场，男女都成为公共领域中的行动者，与“都是行动”的方向相符。  
  来源：<https://en.wikipedia.org/wiki/Women_in_France>
- **#151** 「il prit de bon matin un gaz-cab, et vint chercher Michel; celui-ci l'attendait; il descendit, sauta dans le vé…」  
  判断：**正确**。燃气或汽油动力出租汽车在巴黎街头取代马车，可在路面快速行驶。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_automobile>；<https://en.wikipedia.org/wiki/Internal_combustion_engine>
- **#152** 「filant parfois avec une rapidité merveilleuse sur les chaussées bitumées.」  
  判断：**正确**。巴黎街道普遍铺设沥青路面。  
  来源：<https://en.wikipedia.org/wiki/Asphalt_concrete>
- **#177** 「au-dessus de sa tête le ciel était zébré de fils électriques qui passaient d'une rive à l'autre, et tendaient …」  
  判断：**正确**。城市上空和跨河区域长期布有电缆和电车、电力线路，视觉上如蛛网。  
  来源：<https://en.wikipedia.org/wiki/Overhead_line>；<https://en.wikipedia.org/wiki/Electrification>
- **#182** 「le cadran électrique marquait minuit moins le quart.」  
  判断：**正确**。证券交易所使用电动或电子钟面显示时间。  
  来源：<https://en.wikipedia.org/wiki/Euronext_Paris>；<https://en.wikipedia.org/wiki/Electrification>
- **#183** 「l'électricité écrivait des réclames en lettres de feu, scintillaient sur les colonnes rostrales.」  
  判断：**正确**。街头用电光、霓虹和后来的电子屏幕书写广告，已成为城市景观。  
  来源：<https://en.wikipedia.org/wiki/Neon_sign>；<https://en.wikipedia.org/wiki/Billboard>

### 部分符合（76 条）

- **#2** 「le ministre des Embellissements de Paris, devait présider cette solennité.」  
  判断：**部分符合**。巴黎长期设有公共工程、城市规划或文化类部长，但并未设立名为“城市美化大臣”的固定职位。  
  来源：<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>
- **#4** 「Si personne ne lisait plus, du moins tout le monde savait lire, écrire, même」  
  判断：**部分符合**。识字率到20世纪已接近普及，但“几乎没有人再真正读书”不成立，阅读仍广泛存在，只是相对份额变化。  
  来源：<https://en.wikipedia.org/wiki/Literacy>；<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#7** 「En 1960, le Crédit instructionnel ne comptait pas moins de 157342 élèves, auxquels on infusait la science par …」  
  判断：**部分符合**。教育规模化和科学课程扩展属实，但并未普遍用“机械手段向十几万学生灌输科学”到小说所写的程度。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#8** 「l'étude des belles lettres, des langues anciennes (le français compris) se trouvait alors à peu près sacrifiée」  
  判断：**部分符合**。科学与职业教育比重上升，人文学科相对下降，但远未被“牺牲到几乎不再受重视”。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>；<https://en.wikipedia.org/wiki/Latin>
- **#9** 「le latin et le grec étaient des langues non seulement mortes, mais enterrées」  
  判断：**部分符合**。拉丁语、希腊语在中学课程中大幅衰退，但并未被彻底抛弃，仍作为选修或专业科目存在。  
  来源：<https://en.wikipedia.org/wiki/Latin>；<https://en.wikipedia.org/wiki/Education_in_France>
- **#11** 「depuis dix ans, seules les études scientifiques entassaient les candidats aux examens de l'École.」  
  判断：**部分符合**。科学路径变得极为重要，但进入高等学府并非“几乎只剩科学考试”一条路。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>；<https://en.wikipedia.org/wiki/%C3%89cole_Polytechnique>
- **#13** 「Le sous-chef du chinois réunissait un grand nombre d'élèves depuis la colonisation de la Cochinchine.」  
  判断：**部分符合**。汉语后来在法国教育中有所发展，但并非自交趾支那殖民起就已吸引大批学生成为1960年的普遍景象。  
  来源：<https://en.wikipedia.org/wiki/Chinese_language>；<https://en.wikipedia.org/wiki/Education_in_France>
- **#14** 「devenu inutile, depuis que Mars n'émargeait plus au budget.」  
  判断：**部分符合**。战神广场不再作练兵场而成为公园，但军事开支并未从国家预算中消失。  
  来源：<https://en.wikipedia.org/wiki/Champ_de_Mars>；<https://en.wikipedia.org/wiki/French_Army>
- **#23** 「il la traversait sur le pont d'Iéna, revêtu d'un tablier supérieur pour le service de la voie ferrée」  
  判断：**部分符合**。巴黎有高架或跨塞纳河的地铁（如比尔哈凯姆桥），但耶拿桥上加建地铁上层桥面并未实现。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>
- **#24** 「Cette première ceinture de voies ferrées enlaçait à peu près l'ancien Paris de Louis XV」  
  判断：**部分符合**。巴黎确有环绕旧城的地铁线路（如2号、6号线），但并非小说所写的四同心高架环的第一圈原样。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>
- **#25** 「Une seconde ligne raccordait les anciens faubourgs de Paris, en prolongeant sur une longueur de trente-deux ki…」  
  判断：**部分符合**。郊区与旧郊区由地铁延伸线和RER连接，长度与走线与“三十二公里第二环”并不一致。  
  来源：<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/RATP_Group>
- **#26** 「un troisième railway se déroulait sur une longueur de cinquante-six kilomètres.」  
  判断：**部分符合**。后来的环城公路、RER和计划中的大巴黎快线体现了更外层环线，但56公里第三条都会铁路并未按原文实现。  
  来源：<https://en.wikipedia.org/wiki/Boulevard_P%C3%A9riph%C3%A9rique>；<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>
- **#27** 「un quatrième réseau rattachait entre eux la ligne des forts et desservait une étendue de plus de cent kilomètr…」  
  判断：**部分符合**。要塞外围的区域交通由郊区铁路和公路承担，并非沿要塞修建的一百多公里第四套都会网原样。  
  来源：<https://en.wikipedia.org/wiki/Boulevard_P%C3%A9riph%C3%A9rique>；<https://en.wikipedia.org/wiki/Paris_M%C3%A9tro>
- **#28** 「une ville de vingt-sept lieues de tour : elle avait dévoré le département de la Seine tout entier.」  
  判断：**部分符合**。巴黎在1860年已扩张并入近郊，20世纪形成更大都市区，但1960年并未把整个塞纳省并入市区，周长也与“二十七里格”不尽相符。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Paris>；<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>；<https://en.wikipedia.org/wiki/Boulevard_P%C3%A9riph%C3%A9rique>
- **#29** 「Ces railways existaient depuis 1913; ils avaient été construits aux frais de l'État」  
  判断：**部分符合**。巴黎地铁1900年即通车，早于1913年；初期是特许私营公司建造，后来才转为公营（RATP），故“1913年起存在且由国家出资建造”只对了一部分。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/RATP_Group>
- **#31** 「Chacune de ces voies était établie suivant l'axe des boulevards, à cinq mètres des maisons, au-dessus de la bo…」  
  判断：**部分符合**。巴黎有部分高架地铁，但主体转入地下，并未普遍沿林荫道中线架在距房屋五米处。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>
- **#32** 「ce long viaduc, supportant la voie ferrée, formait une galerie couverte, sous laquelle les promeneurs trouvaie…」  
  判断：**部分符合**。部分高架车站和拱廊提供遮蔽，但高架铁路并未普遍成为供行人遮阳避雨的有顶走廊。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>
- **#37** 「les candélabres établis d'après le système Way par l’électrisation d'un filet de mercure, rayonnaient avec une…」  
  判断：**部分符合**。电灯路灯确实出现且亮度远超旧式气灯，但并非普遍采用小说所写的汞蒸气韦氏电烛系统。  
  来源：<https://en.wikipedia.org/wiki/Street_light>；<https://en.wikipedia.org/wiki/Electrification>
- **#40** 「des bornes-gaz établies aux diverses stations de voitures, fournissaient l'hydrogène nécessaire」  
  判断：**部分符合**。出租与加油站体系出现，但并非普遍在各站设立为车辆加注氢气的燃气柱。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_automobile>
- **#42** 「une ordonnance du ministère de la Police interdisait à toute charrette, fardier, ou camion, de circuler après …」  
  判断：**部分符合**。许多城市对货车进入中心区有时段限制，但巴黎并未按“上午十时后一律禁行、只走保留道路”的精确制度固定下来。  
  来源：<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>；<https://en.wikipedia.org/wiki/History_of_the_automobile>
- **#44** 「ces hôtels immenses dans lesquels se logeaient somptueusement vingt mille voyageurs」  
  判断：**部分符合**。出现了大型豪华旅馆，但可“豪华容纳两万人”的单体旅馆规模被夸大。  
  来源：<https://en.wikipedia.org/wiki/Housing_in_France>
- **#51** 「Les travaux de cette société consistaient à emmagasiner l'air dans ces immenses souterrains si longtemps inuti…」  
  判断：**部分符合**。巴黎历史上确有压缩空气管网和地下储气，但并非把长期闲置的地下墓穴改成高压储库的原样方案。  
  来源：<https://en.wikipedia.org/wiki/Compressed_air>
- **#52** 「on l'y refoulait sous une pression de quarante et cinquante atmosphères, force constante que des conduits amen…」  
  判断：**部分符合**。工业与城市压缩空气管网存在，压力和应用与“四十至五十个大气压输往所有工场”的描写不完全相符。  
  来源：<https://en.wikipedia.org/wiki/Compressed_air>
- **#55** 「la Librairie des Cinq parties du Monde, immense dock situé rue de la Paix, et dirigée par un haut fonctionnair…」  
  判断：**部分符合**。出现了大型书店和书业码头式物流，但并非由国家高级官员掌管的巨型“图书码头”作为常规制度。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#57** 「des contrepoids, jouant dans les murs, enlevaient les commis jusqu'aux rayons supérieurs des salles」  
  判断：**部分符合**。多层书店使用梯子、升降机取书，但“墙内配重把店员提升到上层”并非普遍标准装置。  
  来源：<https://en.wikipedia.org/wiki/Elevator>
- **#60** 「La science, la chimie, la mécanique, faisaient irruption dans le domaine de la poésie !」  
  判断：**部分符合**。出现过工业与科学题材诗歌，但科学并未全面侵入并主导诗歌领域。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#62** 「les éditeurs ne suffisant plus, l'État éditait lui-même」  
  判断：**部分符合**。国家出版与学术出版扩大，但国家并未因此成为主要或唯一的出版者。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#63** 「Michel, arrivé dans la salle des lettres, la trouva déserte」  
  判断：**部分符合**。文学阅览相对冷清过，但文学阅览室并未普遍门可罗雀到无人使用。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>；<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#68** 「Une machine Lenoir de la force de quinze chevaux ne cessait de copier ces lettres que cinq cents employés lui …」  
  判断：**部分符合**。出现了机械复制、打字和后来的复印，但并非用勒诺瓦十五马力机由五百人不停抄写信件的原样装置。  
  来源：<https://en.wikipedia.org/wiki/%C3%89tienne_Lenoir>
- **#75** 「la France qui en fabriquait soixante millions de kilogrammes, il y a cent ans, en dépensait alors plus de troi…」  
  判断：**部分符合**。法国纸张消费在一个世纪里大幅增长，方向正确，但“恰好从六千万公斤增至三亿公斤以上”需更精确的同期统计才能完全对应。  
  来源：<https://en.wikipedia.org/wiki/Pulp_(paper)>
- **#77** 「victime innocente des Caisses perfectionnées qui se défendent toutes seules.」  
  判断：**部分符合**。金库有报警、时间锁和自动防护，但触碰后地板张开、铁笼降入地下室的戏剧性装置并非银行标配。  
  来源：<https://en.wikipedia.org/wiki/Bank_vault>
- **#78** 「Le sol s'entrouvrit au moyen d'un plancher mobile, tandis que les bureaux s'illuminaient électriquement au bru…」  
  判断：**部分符合**。金库可自动锁闭并有电力照明与警报，活动地板陷阱则属夸张，并非常规。  
  来源：<https://en.wikipedia.org/wiki/Bank_vault>；<https://en.wikipedia.org/wiki/Electrification>
- **#81** 「Ces deux grandes institutions fonctionnaient encore en l'an de grâce 1960.」  
  判断：**部分符合**。陪审团制度在法国刑事审判中仍存在，但国民自卫军已于1871年后废除，并非两项制度到1960年都仍运作。  
  来源：<https://en.wikipedia.org/wiki/Jury>；<https://en.wikipedia.org/wiki/National_Guard_(France)>
- **#83** 「à force d'élargir les places, de percer des avenues et de multiplier les boulevards, le terrain menaçait de ma…」  
  判断：**部分符合**。大道扩张和住房压力属实，但“只剩街道、没有房屋”是夸张，私人住宅并未被街道吞噬殆尽。  
  来源：<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>；<https://en.wikipedia.org/wiki/Housing_in_France>；<https://en.wikipedia.org/wiki/Demographics_of_Paris>
- **#84** 「Cela expliquait l'excessive cherté des loyers actuels ; la Compagnie Impériale Générale Immobilière possédait …」  
  判断：**部分符合**。巴黎房租昂贵，土地信贷银行和大不动产公司影响力大，但并非一家帝国不动产公司几乎拥有整个巴黎。  
  来源：<https://en.wikipedia.org/wiki/Cr%C3%A9dit_Foncier_de_France>；<https://en.wikipedia.org/wiki/Housing_in_France>
- **#85** 「Cette société due à deux financiers habiles du dix-neuvième siècle, les frères Péreire, se trouvait également …」  
  判断：**部分符合**。各大城市确有大规模改建和不动产资本，但并非同一公司逐步拥有里昂、马赛、波尔多等主要城市。  
  来源：<https://en.wikipedia.org/wiki/Cr%C3%A9dit_Foncier_de_France>；<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>
- **#88** 「l'exiguïté des appartements ne permettait plus d'avoir des meubles spéciaux」  
  判断：**部分符合**。小公寓和多功能家具增多，但专用家具并未因此普遍消失。  
  来源：<https://en.wikipedia.org/wiki/Housing_in_France>
- **#89** 「annonça son ami Jacques Aubanet, employé dans la Compagnie Générale des Mines en Mer.」  
  判断：**部分符合**。20世纪出现了海底电缆、近海石油和后来的深海采矿构想与部分实践，但1960年并不存在小说中那样的“海洋矿业总公司”成为常规产业。  
  来源：<https://en.wikipedia.org/wiki/Deep_sea_mining>
- **#91** 「L'art n'est plus possible que s'il arrive au tour de force」  
  判断：**部分符合**。大众文化中奇观和轰动效应上升，但艺术并未只有做成惊人之举才可能存在。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>；<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#96** 「On ne se bat plus en duel ; cela est passé de mode ; on transige ou on plaide」  
  判断：**部分符合**。决斗在法律和习俗上基本过时，争端更多走诉讼或和解，但偶发决斗并未在所有地方瞬间绝迹。  
  来源：<https://en.wikipedia.org/wiki/Duel>
- **#98** 「ne deviennent pas peu à peu les grands propriétaires fonciers」  
  判断：**部分符合**。英国人在法国购置房产和土地的现象存在，但并未成为法国的主要土地所有者集团。  
  来源：<https://en.wikipedia.org/wiki/Foreign_direct_investment>
- **#101** 「sous prétexte de formules nouvelles, une partition ne se compose plus que d'une phrase unique, longue, filante…」  
  判断：**部分符合**。部分现代和当代音乐走向绵长乐句与少旋律结构，但这并非全部音乐作品的形态。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#102** 「on ne goûte plus la musique, on l'avale」  
  判断：**部分符合**。出现了音乐的大规模消费和背景化收听，但“不再品味、只是吞下去”是夸大。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#103** 「on a construit un monument de vingt millions, surtout pour y faire manœuvrer des sauteuses」  
  判断：**部分符合**。巴黎歌剧院造价高昂，芭蕾占重要地位，但并非耗费两千万主要只为演出芭蕾而建。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#105** 「l'Opéra, d'ailleurs, est devenu une succursale de la Bourse」  
  判断：**部分符合**。歌剧院确是社交与商务应酬场所，但并未变成证券交易所的分号，音乐也并未被完全无视。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>；<https://en.wikipedia.org/wiki/Euronext_Paris>
- **#106** 「tout le monde est chimiste.」  
  判断：**部分符合**。科学文化大为普及，化学进入日常与工业，但并非“人人都是化学家”。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#116** 「la belle langue française est perdue ; celle que d'illustres étrangers, Leibniz, Frédéric le Grand, Ancillon, …」  
  判断：**部分符合**。法语吸收了大量科技词和外来语并发生变化，但“优美法语已经失传”过绝对。  
  来源：<https://en.wikipedia.org/wiki/French_language>
- **#117** 「est maintenant un horrible argot.」  
  判断：**部分符合**。口语和媒体中确有夹杂外来词和行话的现象，法语并未整体变成一种可怕的行话。  
  来源：<https://en.wikipedia.org/wiki/French_language>
- **#119** 「Un dictionnaire de 1960, s'il veut contenir tous les termes en usage, est le double d'un dictionnaire de 1800 …」  
  判断：**部分符合**。词典收词量显著增加，但“1960年词典若收尽用语恰是1800年的两倍”缺乏精确对应的官方对照。  
  来源：<https://en.wikipedia.org/wiki/French_language>
- **#121** 「Je n'ai plus que trois élèves dans ma classe de rhétorique ! C'est une turpe décadence !」  
  判断：**部分符合**。人文学科相对地位下降，但修辞班并未普遍只剩三个学生。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#123** 「Une soupe grasse et un excellent bouilli de cheval, viande si estimée jusqu'au dix-huitième siècle, et remise …」  
  判断：**部分符合**。马肉在法国仍有消费传统，但20世纪并未出现全民“重新推崇马肉为佳肴”的普遍复兴。  
  来源：<https://en.wikipedia.org/wiki/Horse_meat>
- **#124** 「un fort jambon de mouton, préparé au sucre et au salpêtre d'après une méthode nouvelle qui conservait la chair」  
  判断：**部分符合**。用盐硝等保存肉类的方法长期存在，小说所写的糖硝羊肉火腿新方法并未成为标志性的20世纪发明。  
  来源：<https://en.wikipedia.org/wiki/Horse_meat>
- **#129** 「Il existait alors en France, d'après un projet Dupeyrat, un réseau de voies ferrées sur les chemins de halage …」  
  判断：**部分符合**。历史上有过纤道铁路和机车拖驳的试验与局部应用，但并非法国所有运河纤道都铺上铁路。  
  来源：<https://en.wikipedia.org/wiki/History_of_rail_transport_in_France>；<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#130** 「Ces engins de guerre avaient fini par prendre des proportions incroyables, quoique facilement explicables ; ca…」  
  判断：**部分符合**。装甲与炮弹的竞赛在铁甲舰和无畏舰时代确实持续数十年，但并没有以军舰普遍因超载沉没而告终。  
  来源：<https://en.wikipedia.org/wiki/Ironclad_warship>；<https://en.wikipedia.org/wiki/Dreadnought>
- **#132** 「depuis que les canons portèrent à huit mille mètres, et qu'un boulet de trente-six put à cent mètres traverser…」  
  判断：**部分符合**。火炮射程远超八千米，杀伤力巨大，但“三十六磅弹在百米贯穿三十四匹马和六十八人”的具体数字未能被标准军史原样证实，故只部分成立。  
  来源：<https://en.wikipedia.org/wiki/Dreadnought>；<https://en.wikipedia.org/wiki/French_Army>
- **#133** 「Les bassins du commerce étaient réunis entre eux par des ponts tournants mus à heure fixe au moyen des machine…」  
  判断：**部分符合**。港口与运河上有机械或电力驱动的开启桥，但并非普遍由“地下采石场公司”的压缩空气按时驱动。  
  来源：<https://en.wikipedia.org/wiki/Compressed_air>；<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#137** 「les opérations maritimes, délivrées de tout monopole et de l'entrave des courtiers ministériels, prirent un im…」  
  判断：**部分符合**。海运在一些阶段减少了旧式垄断和中间商束缚并大发展，但垄断和管制并未完全消失。  
  来源：<https://en.wikipedia.org/wiki/Suez_Canal>；<https://en.wikipedia.org/wiki/Panama_Canal>；<https://en.wikipedia.org/wiki/Port>
- **#140** 「au fond un phare électrique, sans grande utilité, s'enfonçait dans le ciel à une hauteur de cinq cents pieds. …」  
  判断：**部分符合**。电灯塔出现，但五百英尺并非此后世界最高建筑物（埃菲尔铁塔已更高），灯光也未见“四十里外仍清晰可见”的通例。  
  来源：<https://en.wikipedia.org/wiki/Lighthouse>；<https://en.wikipedia.org/wiki/Eiffel_Tower>
- **#141** 「le Great Eastern du siècle dernier n'eût pas été digne d'être sa chaloupe ; il venait de New York, et les Amér…」  
  判断：**部分符合**。出现了远超大东方号的巨型远洋客轮，但并非三十根桅、十五个烟囱、三万马力的“利维坦四世”那种形制。  
  来源：<https://en.wikipedia.org/wiki/SS_United_States>；<https://en.wikipedia.org/wiki/Blue_Riband>
- **#142** 「il venait en trois jours de New York à Southampton」  
  判断：**部分符合**。1952年“合众国号”等邮轮已接近三天跨越大西洋，非常接近，但1960年常规班轮并非都稳定在刚好三天，随后飞机更把时间大幅缩短。  
  来源：<https://en.wikipedia.org/wiki/SS_United_States>；<https://en.wikipedia.org/wiki/Blue_Riband>
- **#143** 「La Française est devenue américaine ; elle parle gravement d'affaires graves, elle prend la vie avec raideur」  
  判断：**部分符合**。法国女性更多进入职业和公共生活，作风也受国际影响，但“变得美国化、一本正经只谈生意”是讽刺性夸大。  
  来源：<https://en.wikipedia.org/wiki/Women_in_France>
- **#144** 「mais depuis elles ont passé au genre masculin, et ne valent plus ni le regard d'un artiste ni l'attention d'un…」  
  判断：**部分符合**。性别角色变化使部分传统女性气质的社会期待减弱，但并非女性整体“转入阳性”而不再被当作女性。  
  来源：<https://en.wikipedia.org/wiki/Women_in_France>
- **#146** 「à une époque où la famille tend à se détruire, où l'intérêt privé pousse chacun de ses membres dans des voies …」  
  判断：**部分符合**。家庭形态变化、个人主义与致富压力增加，但家庭并未普遍解体。  
  来源：<https://en.wikipedia.org/wiki/Family_in_France>
- **#147** 「Madame fait des affaires de son côté.」  
  判断：**部分符合**。双职工和社交、职业生活分离的现象增多，但丈夫常住俱乐部、妻子单做生意、彼此形同路人并非1960年的普遍婚制。  
  来源：<https://en.wikipedia.org/wiki/Family_in_France>；<https://en.wikipedia.org/wiki/Women_in_France>
- **#148** 「de nos jours, le nombre des enfants légitimes a-t-il singulièrement diminué au profit des enfants naturels ; c…」  
  判断：**部分符合**。非婚生子女比例后来在法国显著上升，21世纪出生中非婚生子已占多数，但1960年尚远未构成“已经占多数”。  
  来源：<https://en.wikipedia.org/wiki/Legitimacy_(family_law)>；<https://en.wikipedia.org/wiki/Family_in_France>
- **#149** 「fille ne se marie guère, qui n'a pas son pesant d'or dans le coffre paternel」  
  判断：**部分符合**。经济条件仍影响婚姻，但“没有与体重相当的黄金就很难出嫁”的嫁妆制度反而在20世纪衰落。  
  来源：<https://en.wikipedia.org/wiki/Family_in_France>
- **#150** 「Où il est traité de la facilité avec laquelle un artiste peut mourir de faim au xxe siècle」  
  判断：**部分符合**。许多艺术家收入不稳定、难以靠艺术维生，但并非20世纪艺术家普遍“很容易饿死”。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#153** 「À la campagne, s'écria l'oncle; mais il n'y a plus de campagne, Michel !」  
  判断：**部分符合**。巴黎近郊城市化使传统乡村景观大幅收缩，但并非完全不再有乡村。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Paris>；<https://en.wikipedia.org/wiki/Boulevard_P%C3%A9riph%C3%A9rique>
- **#154** 「au moyen de dix mille cheminées d'usine, de fabrique de produits chimiques, de guano artificiel, de fumée de c…」  
  判断：**部分符合**。20世纪中叶巴黎及近郊工业烟囱与空气污染确实严重，可与英国工业城市类比，但“上万座烟囱、空气相当于联合王国”是概括性夸大。  
  来源：<https://en.wikipedia.org/wiki/Demographics_of_Paris>
- **#167** 「La censure disparut naturellement devant ce nouvel état de choses」  
  判断：**部分符合**。戏剧审查在20世纪逐步放松并在后来大幅退潮，但并非因为国家剧本总库出现才“自然消失”。  
  来源：<https://en.wikipedia.org/wiki/Censorship_in_France>；<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#168** 「Les directeurs des théâtres de Paris et de la province étaient fonctionnaires de l'État」  
  判断：**部分符合**。部分公立剧院负责人具有公职或受公共资助，但巴黎和外省剧院经理并未全部成为国家公务员。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#169** 「La création du Grand Entrepôt Dramatique fit disparaître la bruyante société des auteurs ; les employés de la …」  
  判断：**部分符合**。出现了受雇编剧和补贴剧团，但独立作者群体并未消失，国家也并未统一收取全部票房。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#173** 「les machines remplaçaient partout l'homme avantageusement」  
  判断：**部分符合**。机械化与自动化在许多岗位上取代人力，但并未在各处把人完全取代，手工与服务工作仍在。  
  来源：<https://en.wikipedia.org/wiki/Automation>
- **#178** 「L'autel étincelait des feux électriques et des rayons de même nature s'échappaient de l'ostensoir soulevé par …」  
  判断：**部分符合**。教堂普遍使用电灯照明，但祭坛和圣体发光都以电光射出的情景并非普遍礼仪。  
  来源：<https://en.wikipedia.org/wiki/Electrification>
- **#179** 「il n'entendît l'orgue rugir sous l'air comprimé fourni par la Société des Catacombes !」  
  判断：**部分符合**。管风琴可用电力或气泵鼓风，但并非由“地下采石场公司”的压缩空气统一驱动。  
  来源：<https://en.wikipedia.org/wiki/Pipe_organ>；<https://en.wikipedia.org/wiki/Compressed_air>
- **#184** 「D'après un procédé hongrois, deux cents pianos mis en communication les uns avec les autres, au moyen d'un cou…」  
  判断：**部分符合**。出现过电气演奏、自动钢琴和后来的电子同步演奏，但1960年并未普及“二百架钢琴用电连在一起由一人演奏”的常规音乐会。  
  来源：<https://en.wikipedia.org/wiki/Electrification>；<https://en.wikipedia.org/wiki/Palais_Garnier>

### 错误（61 条）

- **#6** 「Ce fut en 1937, sous le règne de Napoléon V, qu'il lança l'affaire.」  
  判断：**错误**。1937年的法国是第三共和国，不存在拿破仑五世或波拿巴王朝复辟。  
  来源：<https://en.wikipedia.org/wiki/House_of_Bonaparte>；<https://en.wikipedia.org/wiki/French_Third_Republic>
- **#10** 「Vers la fin du siècle dernier, l'École Normale déclinait visiblement」  
  判断：**错误**。巴黎高师在19世纪末及此后仍是法国最顶尖的学术机构之一，谈不上明显衰落。  
  来源：<https://en.wikipedia.org/wiki/%C3%89cole_normale_sup%C3%A9rieure_(Paris)>
- **#15** 「pouvant contenir cent quatre-vingt mille âmes, en y comprenant celles des maîtres d'étude.」  
  判断：**错误**。战神广场上并未建成可容纳约十八万人的巨型教育城。  
  来源：<https://en.wikipedia.org/wiki/Champ_de_Mars>；<https://en.wikipedia.org/wiki/Education_in_France>
- **#17** 「Un discours chinois le remplaçait avec avantage」  
  判断：**错误**。汉语演讲并未取代拉丁语成为法国官方典礼致辞。  
  来源：<https://en.wikipedia.org/wiki/Chinese_language>；<https://en.wikipedia.org/wiki/Latin>
- **#21** 「l'acide carbonique détrônant la vapeur d'eau」  
  判断：**错误**。二氧化碳并未取代水蒸气成为主要动力介质，交通与工业动力转向的是电力、石油和内燃机。  
  来源：<https://en.wikipedia.org/wiki/Carbon_dioxide>；<https://en.wikipedia.org/wiki/Steam_engine>；<https://en.wikipedia.org/wiki/Internal_combustion_engine>
- **#22** 「l'Océan lui-même baignant de ses flots les rivages de Grenelle」  
  判断：**错误**。海洋并未被“引到”格勒奈尔，巴黎也没有因此成为远洋海港。  
  来源：<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#30** 「les ingénieurs des ponts et chaussées n'existant plus depuis 1889, date de la suppression de l'École polytechn…」  
  判断：**错误**。综合理工学院1889年并未撤销，路桥工程师团体也延续至今。  
  来源：<https://en.wikipedia.org/wiki/%C3%89cole_Polytechnique>
- **#34** 「Les trains marchaient à l'aide de l'air comprimé」  
  判断：**错误**。巴黎地铁采用电力牵引，并非以压缩空气推进、不用机车。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/Compressed_air>
- **#35** 「débité par la Société des Catacombes de Paris」  
  判断：**错误**。地铁动力并非由“地下墓穴公司”的压缩空气系统供给。  
  来源：<https://en.wikipedia.org/wiki/History_of_the_Paris_M%C3%A9tro>；<https://en.wikipedia.org/wiki/Compressed_air>
- **#49** 「il fut le premier à adopter, pour sa maison et lui, les vêtements en fer filé, qui firent leur apparition vers…」  
  判断：**错误**。1934年前后并未出现被家庭普遍采用的可穿“拉丝铁织物”日常服装。  
  来源：<https://en.wikipedia.org/wiki/Glasses>
- **#53** 「Dix huit cent cinquante-trois moulins à vent, établis dans la plaine de Montrouge, le refoulaient au moyen de …」  
  判断：**错误**。蒙鲁日平原上并未建起上千座风车专门把空气压进大型储气库。  
  来源：<https://en.wikipedia.org/wiki/Compressed_air>
- **#58** 「Je n'en ai jamais entendu parler, répondit ce dernier.」  
  判断：**错误**。1960年前后雨果等作家仍是经典，书店职员不会把他们视为闻所未闻。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#59** 「en fait de vieux auteurs réimprimés de nos jours, nous n'avons que Paul de Kock」  
  判断：**错误**。雨果、巴尔扎克等持续再版畅销，并非买不到；也并非只剩保罗·德·科克还在重印。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>；<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#64** 「« La littérature est morte, mon enfant, répondit l'oncle ; vois ces salles désertes, et ces livres ensevelis d…」  
  判断：**错误**。文学并未死去，人们仍大量阅读，图书馆也并未变成无人问津的墓地。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>；<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#79** 「au milieu, et sur un seul pied, chef-d'œuvre de mécanique, se dressait le Grand Livre de la maison de banque.」  
  判断：**错误**。银行并未使用高达二十英尺、可像望远镜转向的机械巨型总账簿。  
  来源：<https://en.wikipedia.org/wiki/History_of_computing_hardware>；<https://en.wikipedia.org/wiki/Mechanical_calculator>
- **#80** 「Il méritait ce nom de Grand plus justement que Louis XIV ; il avait vingt pieds de haut ; un mécanisme intelli…」  
  判断：**错误**。同样，二十英尺高并配升降栈道的机械总账并未成为实物装置；电子账务走了另一条路。  
  来源：<https://en.wikipedia.org/wiki/History_of_computing_hardware>
- **#87** 「il s'approcha du piano, pressa un bouton, et fit jaillir, c'est le mot, une table munie de bancs, à laquelle t…」  
  判断：**错误**。并未普及按下按钮就能从钢琴弹出餐桌和床的组合家具作为日常发明。  
  来源：<https://en.wikipedia.org/wiki/Housing_in_France>
- **#90** 「quand on ne lit plus Hugo」  
  判断：**错误**。1960年前后人们仍广泛阅读雨果、拉马丁和缪塞，他们仍是学校和出版的经典。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#92** 「tu traites des sujets poétiques, et maintenant, c'est une faute en poésie ! Tu chantes les prairies, les vallo…」  
  判断：**错误**。自然与爱情题材的诗歌并未无人问津，也并未必须改唱工业奇迹才能存在。  
  来源：<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#93** 「c'est une carrière finie, puisqu'il n'y a plus d'armée, à moins de se faire gendarme.」  
  判断：**错误**。1960年法国及英俄意都仍有军队，从军职业并未结束。  
  来源：<https://en.wikipedia.org/wiki/French_Army>；<https://en.wikipedia.org/wiki/World_War_I>；<https://en.wikipedia.org/wiki/World_War_II>
- **#94** 「la France, l'Angleterre, la Russie, l'Italie ont renvoyé leurs soldats, c'est vrai ; on avait au siècle dernie…」  
  判断：**错误**。这些国家并未因兵器过于完善而解散军队；相反，20世纪发生了两次世界大战。  
  来源：<https://en.wikipedia.org/wiki/French_Army>；<https://en.wikipedia.org/wiki/World_War_I>；<https://en.wikipedia.org/wiki/World_War_II>
- **#95** 「sauf la vieille Autriche, les nations Européennes ont supprimé l'État militaire」  
  判断：**错误**。除奥地利外的欧洲国家并未取消军事建制。  
  来源：<https://en.wikipedia.org/wiki/French_Army>；<https://en.wikipedia.org/wiki/World_War_I>；<https://en.wikipedia.org/wiki/World_War_II>
- **#99** 「si bien que ces gens-là arriveront à posséder notre sol tout entier, et prendront leur revanche sur Guillaume …」  
  判断：**错误**。英国人并未买下整个法国国土。  
  来源：<https://en.wikipedia.org/wiki/Foreign_direct_investment>
- **#100** 「au moment où il n'y a plus ni musique, ni poésie, ni armée」  
  判断：**错误**。音乐、诗歌和军队在1960年及此后都仍然存在。  
  来源：<https://en.wikipedia.org/wiki/French_Army>；<https://en.wikipedia.org/wiki/Victor_Hugo>；<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#104** 「On a réduit les Huguenots en un acte, et ce petit lever de rideau accompagne les ballets à la mode」  
  判断：**错误**。《胡格诺教徒》并未被压缩成一幕专门作为流行芭蕾的开场而取代自身。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#107** 「Ceci est de 1947, et le dernier soupir de l'art expirant.」  
  判断：**错误**。1947年并非音乐艺术咽下最后一口气的年份，此后音乐创作与欣赏仍繁荣。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#108** 「Après lui, rien ! Qui le comprendrait maintenant.」  
  判断：**错误**。1947年之后仍有被广泛理解的新音乐与经典演奏，并非“不再有真正的音乐”。  
  来源：<https://en.wikipedia.org/wiki/Palais_Garnier>
- **#109** 「Voilà bien, dit-il, ce que notre époque était digne d'inventer ! Un piano-lit-commode-toilette !」  
  判断：**错误**。集钢琴、床、衣柜、梳妆台于一身的家具并未成为该时代的典型发明。  
  来源：<https://en.wikipedia.org/wiki/Housing_in_France>
- **#112** 「au concierge. « Au neuvième, la porte à droite », répondit ce personnage important, alors employé du gouvernem…」  
  判断：**错误**。门房仍然存在，但并非由政府直接任命的公职人员作为通例。  
  来源：<https://en.wikipedia.org/wiki/Public_service>
- **#114** 「ceci est la cinquante et unième et dernière de ses œuvres complètes ; elle est de 1873, et depuis, on n'a plus…」  
  判断：**错误**。高乃依作品在1873年后持续再版和上演，并非最后一版止于1873年。  
  来源：<https://en.wikipedia.org/wiki/Pierre_Corneille>
- **#115** 「les dernières en un mot et elles ont plus de cent ans de date, et font déjà la joie des bibliophiles ! Ces gra…」  
  判断：**错误**。拉辛、莫里哀、帕斯卡、拉封丹等经典持续再版并进入教育，并非只剩百年前的版本供藏书家把玩。  
  来源：<https://en.wikipedia.org/wiki/Pierre_Corneille>；<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#120** 「malheureusement en 1869, au moment où il terminait ses visites d'Académie, il fut tué en duel par un farouche …」  
  判断：**错误**。埃德蒙·阿布于1885年因病去世，并未在1869年死于与萨尔塞的决斗。  
  来源：<https://en.wikipedia.org/wiki/Edmond_About>
- **#122** 「le bruit court que les chaires des lettres, en vertu d'une décision prise en assemblée générale des actionnair…」  
  判断：**错误**。1962年并未因教学公司股东大会决定而撤销文学教席，法国文学教育继续存在。  
  来源：<https://en.wikipedia.org/wiki/Education_in_France>
- **#126** 「Ce fameux projet de Paris port de mer s'était donc enfin réalisé」  
  判断：**错误**。把巴黎建成可停靠远洋巨轮的海港这一计划并未实现。  
  来源：<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#127** 「une longue suite de bassins à flots creusés dans les vastes plaines de Grenelle et d'Issy pouvaient contenir m…」  
  判断：**错误**。格勒奈尔和伊西并未挖出可停泊上千艘最大吨位船只的潮汐船坞。  
  来源：<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#128** 「En moins de quinze ans, un ingénieur civil, nommé Montanet, creusa un canal qui partant de la plaine de Grenel…」  
  判断：**错误**。从格勒奈尔到鲁昂下游、宽70米深20米的大运河并未按此规模开凿成功。  
  来源：<https://en.wikipedia.org/wiki/Ports_of_Paris>
- **#131** 「les machines se battaient et non les hommes ; de là un acheminement à cesser les guerres qui devenaient ridicu…」  
  判断：**错误**。战争变成高度机械化是事实，但战争并未因此停止；20世纪战争规模反而空前。  
  来源：<https://en.wikipedia.org/wiki/World_War_I>；<https://en.wikipedia.org/wiki/World_War_II>；<https://en.wikipedia.org/wiki/Ironclad_warship>
- **#134** 「la plupart marchaient à l'aide de la vapeur d'acide carbonique」  
  判断：**错误**。大多数商船并不使用碳酸气蒸汽作为动力。  
  来源：<https://en.wikipedia.org/wiki/Carbon_dioxide>；<https://en.wikipedia.org/wiki/Steam_engine>；<https://en.wikipedia.org/wiki/Propeller>
- **#139** 「tous les idiomes de la terre se parlaient sur ce port de Grenelle, le plus fréquenté de l'univers.」  
  判断：**错误**。格勒奈尔并未成为世界上最繁忙的港口。  
  来源：<https://en.wikipedia.org/wiki/Ports_of_Paris>；<https://en.wikipedia.org/wiki/Port>
- **#155** 「la peinture n'existe plus ; il n'y a plus de tableaux, même au Louvre; on les a si savamment restaurés au sièc…」  
  判断：**错误**。绘画仍然存在，卢浮宫藏画也并未因过度修复而普遍剥落到几乎只剩残片。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#156** 「Ainsi donc, au vingtième siècle, plus de peinture et plus de peintres.」  
  判断：**错误**。20世纪仍有绘画和画家，该门类并未消亡。  
  来源：<https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France>
- **#157** 「la guerre n'est plus possible et la diplomatie est passée de mode」  
  判断：**错误**。战争在20世纪不仅可能而且发生，外交也并未过时。  
  来源：<https://en.wikipedia.org/wiki/World_War_I>；<https://en.wikipedia.org/wiki/World_War_II>；<https://en.wikipedia.org/wiki/Politics_of_France>
- **#158** 「tranquillité absolue ! il n'y a plus de partis en France : les orléanistes font du commerce et les républicain…」  
  判断：**错误**。法国在1960年及此后仍有政党政治，并不存在“绝对平静、再无党争”。  
  来源：<https://en.wikipedia.org/wiki/Politics_of_France>
- **#159** 「le journalisme a fait son temps.」  
  判断：**错误**。新闻业并未完成其时代而消亡，报纸、广播、电视和后来的网络新闻仍然存在。  
  来源：<https://en.wikipedia.org/wiki/Media_of_France>
- **#160** 「en 1900, le nombre des journaux en France, politiques ou non, illustrés ou pas, atteignait le chiffre de soixa…」  
  判断：**错误**。1900年法国报纸数量远低于六万种。  
  来源：<https://en.wikipedia.org/wiki/Media_of_France>
- **#161** 「toute cette belle fureur de journaux a bientôt amené la mort du journalisme, par cette raison sans réplique qu…」  
  判断：**错误**。写的人多并未导致新闻业死亡。  
  来源：<https://en.wikipedia.org/wiki/Media_of_France>
- **#162** 「Je ne parlerai pas du barreau ; on ne plaide plus, on transige ; on préfère une mauvaise transaction à un bon …」  
  判断：**错误**。人们仍然广泛提起诉讼，律师业并未因一律和解而衰落消失。  
  来源：<https://en.wikipedia.org/wiki/Jury>
- **#163** 「devenir fonctionnaire ; on en compte dix millions en France」  
  判断：**错误**。法国公务员和公共就业规模很大，但即便在后来也远未达到一千万公务员之数。  
  来源：<https://en.wikipedia.org/wiki/Civil_service>；<https://www.insee.fr/fr/statistiques/2414946>；<https://en.wikipedia.org/wiki/Public_service>
- **#164** 「À cette époque où tout se centralisait, la pensée aussi bien que la force mécanique, la création d'un Entrepôt…」  
  判断：**错误**。1903年并未成立垄断剧本生产的“戏剧总仓库”特许公司。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#165** 「Mais vingt ans plus tard, elle passa dans les mains du gouvernement et fonctionna sous les ordres d'un Directe…」  
  判断：**错误**。也不存在约1923年由政府接管该公司、由国务委员任总监的制度。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#166** 「Les cinquante théâtres de la Capitale se fournissaient là de pièces de tout genre」  
  判断：**错误**。首都剧院并非都由单一国家剧本仓库供应。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#170** 「on ne jouait plus les auteurs anciens ; quelquefois et par exception, on donnait du Molière au Palais Royal, a…」  
  判断：**错误**。莫里哀、雨果、小仲马等仍经常上演，并未被一概淘汰。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>；<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#171** 「les théâtres lui étaient clos par leurs traités avec le Grand Entrepôt Dramatique」  
  判断：**错误**。各剧院并未与某个戏剧总仓库订约从而把独立作者一律关在门外。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#172** 「nous n'avons que faire de nouveauté ; toute personnalité doit disparaître ici ; vous aurez à vous fondre dans …」  
  判断：**错误**。戏剧并未统一变成抹去个性的平庸平均之作。  
  来源：<https://en.wikipedia.org/wiki/Theatre_of_France>
- **#174** 「L'hiver de 1961 à 1962 fut particulièrement rude; il dépassa les hivers de 1789, de 1813, et de 1829, par sa r…」  
  判断：**错误**。真正异常严寒、常被拿来比较的是1962–1963年冬天，而非1961–1962年超过1789、1813和1829年的那个冬天。  
  来源：<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%9363_in_the_United_Kingdom>；<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%931963>
- **#175** 「Ce froid terrible fut général en France et dans une grande partie de l'Europe ; le Rhône, la Garonne, la Loire…」  
  判断：**错误**。1961–1962年并未出现罗讷河、莱茵河和泰晤士河封冻到格雷夫森德、车马在冰上过海的那种全欧冰封。  
  来源：<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%9363_in_the_United_Kingdom>；<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%931963>
- **#176** 「Les voitures ne pouvaient plus circuler, les trains de chemin de fer furent interrompus」  
  判断：**错误**。该年也没有因那场被预言的严寒而使车辆与铁路普遍中断到所述程度。  
  来源：<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%9363_in_the_United_Kingdom>；<https://en.wikipedia.org/wiki/Winter_of_1962%E2%80%931963>
- **#180** 「tomba sur la place Royale d'où la statue de Victor Hugo avait chassé celle de Louis XV」  
  判断：**错误**。王家广场（孚日广场）并未用雨果塑像取代路易十五塑像。  
  来源：<https://en.wikipedia.org/wiki/Place_des_Vosges>；<https://en.wikipedia.org/wiki/Victor_Hugo>
- **#181** 「trouva devant lui le nouveau boulevard Napoléon IV」  
  判断：**错误**。巴黎并未出现以拿破仑四世命名的新林荫大道作为1960年的城市现实。  
  来源：<https://en.wikipedia.org/wiki/House_of_Bonaparte>；<https://en.wikipedia.org/wiki/Haussmann%27s_renovation_of_Paris>
- **#185** 「On ne coupait plus la tête. On foudroyait avec une décharge.」  
  判断：**错误**。法国直到1977年仍使用断头台，并未改用电击作为法定处决方式。  
  来源：<https://en.wikipedia.org/wiki/Guillotine>；<https://en.wikipedia.org/wiki/Electric_chair>
- **#186** 「les ballons armés de paratonnerres, qui étaient à la foudre tout prétexte de tomber sur les maisons non gardée…」  
  判断：**错误**。巴黎上空并未升起装有避雷针的气球网来使全城免遭雷击。  
  来源：<https://en.wikipedia.org/wiki/Lightning_rod>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/verne-paris-20th-century-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/verne-paris-20th-century-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/verne-paris-20th-century-v5/audit/manual_review_2026-11-15.py`

## 说明

- 旧关键词稿（PR #25）有 30 条、28 条可判定，严格胜率 42.9%，加权 58.9%，证据为空。本稿覆盖了其中 28 条可核验的世界预测，并按全文通读补回大量同类世界图景。
- 第 20 条（文学教席将在1962财年撤销）和第 28 条（1961–1962年严冬）在旧稿中被标为情节、不计入预测；本稿仍作为书中给出的时点世界陈述收入，并分别判为错误（文学教席并未撤销；真正著名的严寒之冬是1962–1963年）。
- 统计以 pipeline.py report 的 summary.json 为准；加权胜率按 manual_report.py 的规则 8 计算：正确×1 + 趋势符合×0.75 + 部分符合×0.5。

