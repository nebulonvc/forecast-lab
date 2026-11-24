# 拉尔夫124C 41+：2660年的传奇（Hugo Gernsback, Ralph 124C 41+）：出版后预测人工核查

- 案例目录：`cases/gernsback-ralph-124c-41-plus-v5/`
- 出版日期：1925-01-01（1911–1912 连载；1925 年 Stratford 第一版单行本。本 TXT 为 1950 年第二版 Gutenberg #60944，观察窗口按已接受的 1925 口径至 2026-11-15。1950 他人前言排除，未改代理出版年。）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 73 条，剔除非预测 0 条，计入 **73 条预测**，其中 **69 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 15 |
| 趋势符合 | 7 |
| 部分符合 | 15 |
| 错误 | 32 |
| 暂无法判断 | 4 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **21.7%**（15/69） |
| 加权胜率 | **40.2%** |
| 错误率 | **46.4%**（32/69） |
| 未定占比（暂无法判断/预测） | 5.5%（4/73） |

## 总体评价

这是一部以2660年为舞台的技术小说，多数条目把当时已写成日常的装置当作出版年之后应出现的社会技术状态来核验。在73条可核验预测中，视频通话、跨洋航线、光伏发电、语音听写、彩色传真/传图、远程剧场转播、自动包装、警察移动通报、航天执照、空间监视、航天器环控与小行星编目等主结果已在2026-11-15前实现；电动出行、无缆电梯、垂直农业、实时翻译等方向出现但未达到文中的普遍程度；行星总督、火星移民与班轮、反重力马戏团、邮票胶片报、政府所有科学家、死刑犯人体实验、催眠学习取代教育、镭合金安全热源、三日死亡后复苏等主结果则与截止日事实相反。四条因显式终点（约2600年饥荒、22世纪初120亿人口、2210年反重力发明）尚未到期，或“三年悬停实验成功”的条件未触发，记暂无法判断。34条人物转述（reported）按METHOD降为不可核验/非预测，未为计分改为author_endorsed。1950再版他人前言未作预测；代理出版年保持1925，详见案例内出版年审计。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（15 条）

- **#2** 「Stepping to the _Telephot_ on the side of the wall he pressed a group of buttons and in a few minutes the face…」  
  判断：**正确**。视频通话已成日常：Zoom、FaceTime等可在会话中实时显示对方面孔，主结果在截止日前已实现。  
  来源：<https://www.sciencenews.org/article/video-call-zoom-pandemic-popularity-phone-tech-history>；<https://en.wikipedia.org/wiki/History_of_videotelephony>
- **#8** 「The hum of the great city came faintly from below. Aeroflyers dotted the sky. From time to time, trans-oceanic…」  
  判断：**正确**。跨洋、跨大陆定期航班已是日常，纽约上空持续有洲际与国内航线飞行。  
  来源：<https://en.wikipedia.org/wiki/List_of_commercial_transatlantic_flights>
- **#13** 「Every inch of the wall, however, was covered with large-sized Telephots and loud-speaking devices.」  
  判断：**正确**。远程听众通过大屏与扩声观看、收听演讲或集会已成为常规（电视、网络视频会议、LED墙）。  
  来源：<https://www.fordav.com/projects/oracle/>；<https://www.webex.com/us/en/devices/room-series/cisco-room-kit-pro.html>
- **#17** 「The photographs had been sent by _Teleradiograph_ immediately after the occurrence in Switzerland, and the _Ne…」  
  判断：**正确**。彩色照片跨国传输并在事件后远短于二十分钟内见报或上网，自有线传真照片至互联网已实现。  
  来源：<https://time.com/3650882/associated-press-photowire-80th-anniversary/>；<https://apimagesblog.com/historical/2025/01/07/90-years-of-wirephoto>
- **#32** 「the photo-electric elements which transformed the solar heat _direct_ into electric energy.」  
  判断：**正确**。光电元件在玻璃下把日光转为电力的光伏发电已大规模应用，与Helio-Dynamophore的核心机制一致。  
  来源：<https://www.eia.gov/kids/history-of-energy/timelines/photovoltaic.php>；<https://en.wikipedia.org/wiki/Timeline_of_solar_cells>
- **#35** 「all objects on the distant stage of the National Opera were projected full size on the composite Telephot plat…」  
  判断：**正确**。歌剧与戏剧可现场转播到影院大屏（NT Live、歌剧院直播等），远程全尺寸观看舞台已成为常规服务。  
  来源：<https://www.barbican.org.uk/whats-on/series/event-cinema>
- **#37** 「The automatic packing machine could pack anything from a small package a few inches square up to a box two fee…」  
  判断：**正确**。按货物尺寸自动成箱、带提手的包装机已在工业中使用，可在十余秒量级完成。  
  来源：<https://www.packsize.com/product/x6>
- **#51** 「Facing him on the desk was a machine of about the shape of an old-fashioned typewriter, except that there were…」  
  判断：**正确**。语音转写与听写系统（如Dragon及手机听写）已广泛使用，可把口述记录为文字。  
  来源：<https://en.wikipedia.org/wiki/Timeline_of_speech_and_voice_recognition>；<https://speechify.com/blog/history-of-dragon-dictation/>
- **#54** 「placed before a Telephot connecting with every member of the entire police force, and the picture was reproduc…」  
  判断：**正确**。警方可通过无线电、手机与计算机向全体警员分发嫌疑人照片，便携设备显示通缉影像已是常规。  
  来源：<https://legalclarity.org/what-is-an-apb-all-points-bulletin-alert/>；<https://en.wikipedia.org/wiki/BOLO>
- **#55** 「all space flyers must be licensed by law,」  
  判断：**正确**。航天发射与再入器须取得许可证，美国FAA等对商业航天器实施执照管理。  
  来源：<https://www.faa.gov/space/licenses>；<https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450>
- **#56** 「it was not until the year 2659 that Ralph 124C 41+ succeeded in accurately determining the exact location of f…」  
  判断：**正确**。地基雷达与空间监视网可定位望远镜难以直接跟踪的航天器，反射无线电波测距定向已是标准能力；能力在2659年之前早已实现。  
  来源：<https://www.nasa.gov/wp-content/uploads/2026/05/12-soa-tracking-aids-2026-final.pdf?emrc=6a08af15a012d>
- **#57** 「Towards the end of the twenty-first century, when atmospheric flying had become common,」  
  判断：**正确**。大气层飞行在20世纪中叶已成为常规客运，并早于“21世纪末”这一表述；科学家亦在20世纪中叶开始认真研制离地机械。主状态提前实现。  
  来源：<https://www.airandspace.si.edu/explore/stories/passenger-flight>；<https://airandspace.si.edu/explore/stories/evolution-commercial-flying-experience>
- **#61** 「The air supply was manufactured by chemical means on board, but very little was needed, as the original supply…」  
  判断：**正确**。航天器环控生保系统以化学与物理手段处理二氧化碳并再生氧气，重复使用携行空气，国际空间站已长期运行。  
  来源：<https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss/>；<https://www.nature.com/articles/s41526-026-00608-x>
- **#62** 「headed for the Asteroids further pursuit would be useless. There were over 4,000 of these little planets alrea…」  
  判断：**正确**。已知小行星数量远超4000，小行星中心登记的编号与未编号天体以十万计。  
  来源：<https://www.minorplanetcenter.net/mpc/summary>；<https://en.wikipedia.org/wiki/Minor_planet>
- **#71** 「Simultaneously a third assistant administered oxygen to Alice, while a fourth commenced to excite her heart rh…」  
  判断：**正确**。复苏时给氧并以电流节律性刺激心脏（除颤/起搏与高质量心肺复苏）已是国际复苏指南的标准措施。  
  来源：<https://www.ahajournals.org/doi/full/10.1161/CIR.0000000000001376>；<https://professional.heart.org/en/science-news/2026-international-liaison-committee-on-resuscitation-consensus-on-science-with-treatment-recommenda/top-things-to-know>

### 趋势符合（7 条）

- **#12** 「both stepped over into the round steel car of the electromagnetic elevator. The butler pressed one of the 28 i…」  
  判断：**趋势符合**。无缆磁浮电梯（TK Elevator MULTI）已研制并可水平/垂直运行，但常规建筑仍以钢丝绳或液压电梯为主，尚未成为通行设施。  
  来源：<https://en.wikipedia.org/wiki/TK_Elevator_MULTI>；<https://www.cnbc.com/2017/12/13/thyssenkrupp-multi-elevator-goes-up-down-sideways.html>
- **#15** 「This process was invented in 1910 by an Englishman, and improved by the American 64L 52 in 2031, who made it p…」  
  判断：**趋势符合**。八色一次走纸的胶印机在2018年后已上市，能力提前出现；但原文将改进定点在2031年的电解印刷叠印八个主题，该显式年份尚未到期，且工艺并不等同。  
  来源：<https://www.komori.com/en/global/information/news/2018/0426_16.html>；<https://www.piworld.com/article/bender-redefines-offset-with-rmgt-eight-color-long-perfector/>
- **#27** 「In reality they were _Tele-motor-coasters_. They were made of alomagnesium and each weighed only about one and…」  
  判断：**趋势符合**。电动轮滑与悬浮滑鞋已作为消费品出售，但并非城市出行的常规方式，也未达到文中作为普遍交通工具的状态。  
  来源：<https://zuumtech.com/>；<https://www.airtrick.top/post/electric-skates-vs-hoverboards-what-s-the-difference-and-which-is-better>
- **#30** 「The last Horse in Harness in the Streets of New York Died on this Spot June 19th, 2096 A.D.」  
  判断：**趋势符合**。马匹几乎退出纽约日常街道交通，市议会2026年10月通过将于2028年结束中央公园马车；但截止日仍有马车运营，且“最后一匹马死于2096-06-19”这一显式日期尚未到来。  
  来源：<https://council.nyc.gov/press/2026/10/22/3306/>；<https://apnews.com/article/nyc-mamdani-horse-carriage-ban-central-park-f7eab7520c041c4763f1913cf56e606b>
- **#40** 「The Bacillatorium, invented in 2509 by the Swede 1A 299,」  
  判断：**趋势符合**。全身紫外消毒舱已作为医疗/安检装置出现，但“2509年由瑞典人发明Bacillatorium”这一显式事件尚未到期，亦非法定人人隔日使用的装置。  
  来源：<https://www.medicalexpo.com/medical-manufacturer/whole-body-disinfection-booth-56476.html>
- **#45** 「Accelerated Plant Growing Farms and were located in every part of the world.」  
  判断：**趋势符合**。垂直农业与可控环境农场已在多国商业化，但远未“分布在世界每一处”，且行业仍在经历调整。  
  来源：<https://www.ceagworld.com/vertical-farming/around-the-world-with-vertical-farming/>
- **#46** 「Ralph's latest Accelerator made it possible to grow four, and sometimes five crops a year.」  
  判断：**趋势符合**。田间小麦通常一年一至两熟；受控环境中加速种植小麦的研究显示更高熟次可能，但四至五熟尚未成为普遍农法。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/32719119/>；<https://biologyinsights.com/how-many-times-can-you-harvest-wheat-in-a-year/>

### 部分符合（15 条）

- **#3** 「He immediately turned the small shining disc of the Language Rectifier on his instrument till the pointer rest…」  
  判断：**部分符合**。实时语音翻译耳机与通话翻译已上市，但远非“完美英语”，医学场景误差仍显著，也未成为所有视频通话的标准附件。  
  来源：<https://support.google.com/googlepixelbuds/answer/7573100?hl=en>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC13512232/>
- **#4** 「Ralph then attached the Telautograph to his Telephot while the girl did the same. When both instruments were c…」  
  判断：**部分符合**。远程手写/签名传输早已存在（传真、LongPen、电子签名），但Telautograph本身早于1925年；与视频通话一体、当场显影签名并非日常标准做法。  
  来源：<https://en.wikipedia.org/wiki/Telautograph>；<https://en.wikipedia.org/wiki/Fax>
- **#5** 「she called out sharply: "_Lux!_" The delicate detectophone mechanism of the Luminor responded instantly to her…」  
  判断：**部分符合**。冷光源（荧光/LED）已成为房间照明主流，语音控灯在智能家居中可用且增长，但并非普遍以口语检测器作为标准开关方式。  
  来源：<https://www.statista.com/topics/2430/smart-homes/>；<https://www.theverge.com/news/772038/lepro-smart-light-built-in-microphone-ifa>
- **#16** 「With this method it was possible to "print" a "newspaper," fully ten times as large in volume as any newspaper…」  
  判断：**部分符合**。数字设备与微型电子纸可在远小于大幅报纸的载体上容纳远超“十倍篇幅”的内容，但并非把整份报纸印在邮票大小的胶片上作为标准报纸形态。  
  来源：<https://epaperdaily.com/articles/boox-picco-evaluating-the-pocket/>；<https://en.wikipedia.org/wiki/Newspaper_format>
- **#28** 「The trolley car had long since become obsolete as well as the gasoline-driven automobile. Only electromobiles …」  
  判断：**部分符合**。有轨电车在许多城市已退出，电动汽车份额上升；但汽油车在2026年仍广泛使用，并未“早已过时、只剩电动载具”。  
  来源：<https://www.forbes.com/sites/jonmarkman/2026/10/15/evs-and-hybrids-push-gas-only-cars-below-half-of-global-sales/>；<https://theicct.org/publication/global-ev-market-monitor-for-light-duty-vehicles-in-key-markets-h1-2026/>
- **#38** 「a package could be delivered in the average space of forty minutes from the time of purchase.」  
  判断：**部分符合**。部分城市可对部分商品提供一至三小时甚至更快配送，但平均包裹时效仍以日计，并非地下邮管实现的普遍四十分钟送达。  
  来源：<https://www.aboutamazon.com/news/retail/amazon-fast-delivery-orders>
- **#39** 「the flag of the United States in immense proportions was seen. It was composed of 6,000 flyers, all together i…」  
  判断：**部分符合**。数千架无人机可在空中组成国旗图像，但并非6000架载人飞行器在同一水平面组成巨旗。  
  来源：<https://www.guinnessworldrecords.com/world-records/742000-largest-aerial-image-of-a-flag-formed-by-multirotors-drones>；<https://english.news.cn/20261110/30a8c0ddcf0748638a6b51c7099b6b86/c.html>
- **#41** 「were called _Arcturium Rays_ and would instantly destroy any bacilli exposed to them for a few seconds.」  
  判断：**部分符合**。紫外线尤其是222纳米远UVC可在短时间杀灭多种微生物并号称对哺乳动物组织较安全，但并非“数秒内消灭任何杆菌、经氦过滤即对人体完全无灼伤”的通用射线。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC6122858/>；<https://www.sciencedirect.com/science/article/pii/S0195670120301298>
- **#47** 「There was, the _appear_, a cross between an apple and a pear, which had all the good qualities of the apple an…」  
  判断：**部分符合**。苹果与梨的属间杂交或“papple”类报道存在，但并非日常餐桌上兼具二者优点的常规品种。  
  来源：<https://www.gardendesign.com/edible/hybrid-papple.html>
- **#48** 「chemical laboratories which manufactured sugar, milk, cooking fats, butter and cheese.」  
  判断：**部分符合**。食糖的化学制取早已存在，精密发酵乳蛋白与合成脂肪已有工业尝试，但尚未全面取代牛乳与天然油脂的生产。  
  来源：<https://www.foodanddrinkbusiness.com.au/news/nourish-ingredients-scales-creamilux-in-europe>
- **#49** 「Of particular interest was the new kind of cloth, which was much fighter than wool or cotton, and, at the same…」  
  判断：**部分符合**。软木织物已用于服装与配件，但“化学消化软木线、比羊毛更轻且冬暖夏凉并取代棉毛”并未成为主要衣料。  
  来源：<https://www.cork-a-tex.com/products-technical-information/>
- **#63** 「These little Asteroids, revolving in an orbit between Mars and Jupiter were practically uninhabited, although …」  
  判断：**部分符合**。小行星确实基本无人居住，但较大的小行星并没有良好大气与宜人气候，也无巨型植被。  
  来源：<https://en.wikipedia.org/wiki/Asteroid>
- **#67** 「once in twenty-four he looked at the blood vessels. This was made possible by means of his _Platinum-Barium-Ar…」  
  判断：**部分符合**。手术用头戴荧光透视显示器可使术者看到影像，但并不存在依靠镭溶液激发、像X光屏一样观察全身血管的普通眼镜。  
  来源：<https://www.jvscit.org/article/S2468-4287(26)00269-8/pdf>
- **#68** 「Space-sickness is one of the most unpleasant sensations that a human being can experience. Not all are subject…」  
  判断：**部分符合**。空间运动病是公认现象，并非人人发生，初期常在约两日内缓解；但“不超过48小时且永不复发”过强，再入适应病等可再次出现。  
  来源：<https://www.nasa.gov/wp-content/uploads/2025/09/ochmo-mtb-004-space-adaptation-sickness-sas.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10311550/>
- **#69** 「the optical nerves usually become affected and everything appears upside down, as if the sufferer were looking…」  
  判断：**部分符合**。空间运动病使用异丙嗪、东莨菪碱等药物，但并非必须大剂量“Siltagol”，也不存在不加药就会脑炎的既定病程。  
  来源：<https://doi.org/10.1002/bcp.70056>；<https://www.nasa.gov/wp-content/uploads/2025/09/ochmo-mtb-004-space-adaptation-sickness-sas.pdf>

### 错误（32 条）

- **#1** 「He was _Ralph 124C 41+_, one of the greatest living scientists and _one of the ten men on the whole planet ear…」  
  判断：**错误**。若干国家设有国家级科学家勋衔，但不存在全球仅十人、以Plus标记独占的科学家等级制度。  
  来源：<https://www.members.nast.dost.gov.ph/index.php>；<https://www.dost.gov.ph/knowiedge-resources/news/78-2023-news/3309-paiace-confers-the-order-of-nationai-scientist-to-dr-carmencita-d-padiiia.html>
- **#6** 「the building, which was built of steelonium (the new substitute for steel).」  
  判断：**错误**。钢仍是建筑不可或缺的结构材料，石墨烯等仍处探索，并不存在已替代钢的“steelonium”。  
  来源：<https://globalabc.org/buildingmaterialsandclimate/chapter-5-improve/5-3-steel.html>；<https://www.thefabricator.com/thefabricator/blog/metalsmaterials/the-industries-shaping-steel-demand-in-2026>
- **#7** 「Ralph 124C 41+, in New York, four thousand miles distant, had turned off the power of his ultra-generator.」  
  判断：**错误**。微波无线传能实验约在1公里、千瓦级，远未达到纽约向瑞士四千英里定向输电或融化雪崩的功率与距离。  
  来源：<https://www.nrl.navy.mil/Media/News/Article/3004608/nrl-conducts-successful-terrestrial-microwave-power-beaming-demonstration/>；<https://www.irishtimes.com/business/innovation/2023/10/19/energy-beams-market-for-long-distance-wireless-transmission-of-power-not-yet-viable/>
- **#9** 「He belonged, not to himself, but to the Government--the Government, who fed and clothed him, and whose doctors…」  
  判断：**错误**。顶尖科学家并不“属于政府、由政府供养并严格监护”；大量科研仍在大学与私营部门，学术自主仍是原则。  
  来源：<https://www.nature.com/articles/d41586-026-02932-4>；<https://www.science.org/doi/full/10.1126/science.aei6193>
- **#10** 「That institution would supply him with some criminal under sentence of death who would be compelled to undergo…」  
  判断：**错误**。美联邦常识规则Subpart C禁止对囚犯进行超最小风险的生物医学实验，与“政府提供死刑犯做危险实验、死了也无损失”相反。  
  来源：<https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-C/section-46.306>；<https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/common-rule-subpart-c/index.html>
- **#11** 「He would call up the Planet Governor, the ruler of 15 billion human beings,」  
  判断：**错误**。不存在统治全人类的行星总督；2026年世界人口约82亿，并非150亿。联合国也不是世界政府。  
  来源：<https://en.wikipedia.org/wiki/World_population>；<https://en.wikipedia.org/wiki/Demographics_of_the_world>
- **#14** 「Many made that city their permanent home, although the law on the planet Earth, as well as on Mars, which forb…」  
  判断：**错误**。SETI尚未证实地外文明到访；没有火星人定居纽约，也没有地火通婚禁令。  
  来源：<https://www.space.com/space-exploration/search-for-life/where-are-all-the-aliens-maybe-they-just-dont-want-to-talk-to-us>；<https://www.albany.edu/news-center/news/2026-ask-expert-what-are-odds-aliens-exist>
- **#18** 「The Menograph was one of Ralph 124C 41+'s earliest inventions, and entirely superseded the pen and pencil.」  
  判断：**错误**。脑机接口可让部分瘫痪患者以意念打字，仍属实验；笔、键盘与屏幕输入并未被思维记录仪完全取代。  
  来源：<https://www.scientificamerican.com/article/brain-implant-allows-people-who-are-paralyzed-to-type-using-their-thoughts/>；<https://apnews.com/article/typewriter-ai-cheating-chatgpt-cornell-ce10e1ca0f10c96f79b7d988bb56448b>
- **#19** 「to perfect the Hypnobioscope, which transmitted words direct to the sleeping brain, in such a manner that ever…」  
  判断：**错误**。睡眠中巩固已学材料有证据，但不能把新词句在睡眠中完整灌入并于次日详细记住；经典催眠教学法大体被否定。  
  来源：<https://en.wikipedia.org/wiki/Sleep-learning>；<https://www.sleepfoundation.org/how-sleep-works/can-you-learn-a-language-while-sleeping>
- **#20** 「All books were read while one slept. _Most of the studying was done while one slept._ Some people mastered ten…」  
  判断：**错误**。书籍与功课仍主要在清醒时完成，不能在睡梦中掌握十种语言。  
  来源：<https://www.sleepfoundation.org/how-sleep-works/can-you-learn-a-language-while-sleeping>；<https://blog.duolingo.com/can-you-learn-a-language-while-sleeping/>
- **#21** 「In 2009, Anatole M610 B9, the great French physicist, found that Radium obtained all its energy from the ether…」  
  判断：**错误**。以太说早被放弃；2009年并不存在Anatole M610 B9发现镭能来自以太的事件，镭衰变能量来自原子核。  
  来源：<https://en.wikipedia.org/wiki/Luminiferous_aether>；<https://ojs.ehu.eus/index.php/THEORIA/article/view/457>
- **#22** 「Radium-K, as used by Ralph, was not pure Radium, but an alloy composed of Radium and Argonium. This alloy exhi…」  
  判断：**错误**。不存在可随意用手触摸、不灼伤组织的镭合金热源；镭仍是危险放射性物质。  
  来源：<https://www.epa.gov/radiation/radionuclide-basics-radium>；<https://link.springer.com/article/10.1007/s10238-026-02292-3>
- **#23** 「The latter was filled with _Permagatol_, a green gas having the property of preserving animal tissue permanent…」  
  判断：**错误**。器官与组织保存仍受时限约束，没有可永久无限期保存动物组织的实用气体。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11772108/>；<https://arpa-h.gov/explore-funding/initiatives-and-sprints/tigar>
- **#25** 「its cathode shot the powerful F-9-Rays into the animal's brain. No sooner had these rays, which are among the …」  
  判断：**错误**。没有从真空管阴极射出、可把长期保存的动物复苏的F-9射线类脑刺激器。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13194118/>；<https://www.newscientist.com/article/2435695-light-activated-drugs-could-keep-sleep-deprived-military-pilots-alert/>
- **#26** 「animal opened its eyes as if awakening from a long sleep.」  
  判断：**错误**。没有在“死亡”保存三年后把狗复苏如从长眠醒来的成功记录；宠物冷冻与克隆不能等同于该复苏。  
  来源：<https://www.technologyreview.com/2026/10/16/1146766/pet-biotech-longevity-cloning-cryonics/>
- **#29** 「Meats, vegetables, and other eatables, were all liquefied and were prepared with utmost skill to make them pal…」  
  判断：**错误**。代餐袋与液体营养是小众或医疗用途，餐馆仍以固体餐食为主，并非用管子进食的标准科学餐厅。  
  来源：<https://www.nytimes.com/2026/02/02/dining/food-pouches-soylent.html?searchResultPosition=2>
- **#31** 「The machine, which was very light and operated entirely by electricity, was built of metal throughout; it shot…」  
  判断：**错误**。电动空中出租车仍在试飞、商业载客多指向2027年以后，巡航速度远低于每小时600英里。  
  来源：<https://www.ainonline.com/aviation-news/futureflight/2026-11-10/joby-and-archer-push-evtol-passenger-flights-2027>
- **#33** 「this plant supplied all the power, light, and heat for entire New York.」  
  判断：**错误**。纽约电力并非全部由太阳能供给；太阳能约占全市用电的1%–1.5%，其余为化石、核电与水电等。  
  来源：<https://comptroller.nyc.gov/reports/meeting-new-york-citys-energy-demand-challenge/>
- **#34** 「it was not until the year 2469 that the Italian 63A 1243 invented the photo-electric cell, which revolutionize…」  
  判断：**错误**。光电效应与光电管在19世纪末至20世纪初即已出现，远早于出版年；把它说成2469年才发明，与已发生的历史相反。  
  来源：<https://www.encyclopedia.com/science-and-technology/computers-and-electrical-engineering/electrical-engineering/photoelectric-cell>
- **#36** 「it was made of _Alohydrolium_, which is the lightest of all metals, being one-eighth the weight of aluminum.」  
  判断：**错误**。最轻实用金属锂的密度仍高于铝的八分之一；不存在密度仅为铝八分之一的包装用金属。  
  来源：<https://sciencenotes.org/what-is-the-lightest-metal/>
- **#42** 「The Bacillatorium was prescribed by law and each citizen ordered to use it at least every other day, thus maki…」  
  判断：**错误**。不存在命令每位公民至少隔日进入全身灭菌舱、从而使人体无法携带杆菌的法律。  
  来源：<https://en.wikipedia.org/wiki/Compulsory_sterilization>
- **#43** 「extended the span of human life to between one hundred and twenty and one hundred and forty years,」  
  判断：**错误**。人群预期寿命远低于120–140岁；有记录的人类寿命上限约122岁，并非因强制灭菌使寿命普遍达到120–140岁。  
  来源：<https://my.clevelandclinic.org/health/articles/lifespan>；<https://en.wikipedia.org/wiki/Maximum_life_span>
- **#50** 「Once away from the influence of the apparatus she became visible again.」  
  判断：**错误**。超材料隐身仍为实验室尺度，不存在可使人完全隐形、离开装置后又恢复可见的实用装备。  
  来源：<https://www.nationalgeographic.com/science/article/invisibility-science-fiction-reality-technology>
- **#52** 「gravitation was cut off, and the horse rose, beating the air with his hoofs,」  
  判断：**错误**。不能在马戏团场地切断引力使人马失重；不存在可开关的场地重力屏蔽。  
  来源：<https://hsarpa.org/archive/field-phenomena/gravity-control-gravitational-field-manipulation>
- **#53** 「the next inter-planetary liner, which left Earth for Mars,」  
  判断：**错误**。截至截止日尚无载人火星航班，更无地球—火星定期客运班轮。  
  来源：<https://en.wikipedia.org/wiki/Human_mission_to_Mars>；<https://www.spacex.com/humanspaceflight/mars/>
- **#60** 「lift a weight of 1,000 kilograms with an anti-gravitator weighing but 12 kilograms.」  
  判断：**错误**。在出版年至截止日窗口内，不存在重12公斤、可举起1000公斤而无需反作用工质的反重力装置。  
  来源：<https://www.popularmechanics.com/science/a74399234/nasa-veteran-says-drive-needs-no-propellant-survived-independent-test/>
- **#64** 「This was the spectacle that at times greatly increased the transport space flyer travel between Earth and Mars…」  
  判断：**错误**。不存在地球与火星居民往返观光的客运飞行。  
  来源：<https://en.wikipedia.org/wiki/Human_mission_to_Mars>；<https://www.spacex.com/humanspaceflight/mars/>
- **#65** 「his comet had been "discovered" simultaneously on Earth, on Venus, and on Mars the same day he had made it.」  
  判断：**错误**。彗星可在地球上由多台望远镜同日发现，但金星与火星上没有可与地球并列的发现网络，不能做到三行星同日独立发现并命名。  
  来源：<https://people.ast.cam.ac.uk/~jds/coms26.htm>
- **#66** 「He had to pump an antiseptic solution through the veins of Alice, and after that the blood vessels must be fil…」  
  判断：**错误**。血液代用品与器官保存液不能在抽干血液后永久阻止遗体的物理化学变化，不存在实用的镭-K溴化物血液替代保存剂。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13678070/>；<https://pubmed.ncbi.nlm.nih.gov/32012441/>
- **#70** 「the surgeon had opened the large arteries of both Ralph and Cléose, and had introduced a flexible glass tube i…」  
  判断：**错误**。直接动脉对动脉输血是20世纪初的历史做法，后被血库取代；并不能作为把长期保存、已抽干血液的人体复苏的现行术式。  
  来源：<https://www.aabb.org/blood-biotherapies/blood/transfusion-medicine/transfusion-medicine-resources/transfusion-medicine-history>；<https://en.wikipedia.org/wiki/Blood_transfusion>
- **#72** 「Ralph had sent for a Hypnobioscope, the head pieces of which they fastened to Alice's temples.」  
  判断：**错误**。对无反应患者可用脑刺激或EEG探测残留意识，但没有把催眠学习仪绑在太阳穴上以唤醒明显死者的医疗程序。  
  来源：<https://academic.oup.com/brain/advance-article/doi/10.1093/brain/awag210/8931697>；<https://en.wikipedia.org/wiki/Sleep-learning>
- **#73** 「A moment later her breast rose gently and fell again, and from the white lips came the suggestion of a sigh.」  
  判断：**错误**。临床死亡后数日、血液已抽干的人体不能按该程序在一周后清醒康复；罕见的“拉撒路现象”发生在宣布死亡后的短时间内，不能作为该复苏术成功的证据。  
  来源：<https://my.clevelandclinic.org/health/articles/24876-lazarus-effect>；<https://www.wma.net/policies-post/wma-declaration-of-sydney-on-the-determination-of-death-and-the-recovery-of-organs/>

### 暂无法判断（4 条）

- **#24** 「If the experiment succeeded it meant the prolongation of human life over greater periods of the earth's histor…」  
  判断：**暂无法判断**。条件“若为期三年的狗悬停实验成功”在现实中并未触发；紧急保存复苏与冷冻人仍属研究或未验证，不能据此把“过早死亡将结束”判对或判错。  
  来源：<https://tsaco.bmj.com/content/11/2/e002165>；<https://www.bbc.com/future/article/20250115-cryonics-the-start-up-that-wants-to-freeze-you-in-suspended-animation>
- **#44** 「When, about the year 2600, the population of the planet had increased tremendously and famines due to lack of …」  
  判断：**暂无法判断**。显式时间约为2600年，观察窗口尚未关闭；虽然1925年以来世界人口大增，且2026年仍有粮食危机，但不能把尚未到来的2600年饥荒爆发判对或判错。  
  来源：<https://www.fao.org/hunger/en>；<https://www.wfp.org/publications/global-report-food-crises-grfc>
- **#58** 「the enormous population of Earth, which had passed the twelve billion mark,」  
  判断：**暂无法判断**。显式时间是22世纪初，窗口未关闭；2026年人口约82亿，联合国2024年展望预计本世纪见顶且可能不到120亿，但结果尚未实现，不作对错。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>；<https://ourworldindata.org/un-population-2024-revision/>
- **#59** 「the _Anti-Gravitator_ was invented by the American 969L 9 in the year 2210.」  
  判断：**暂无法判断**。反重力装置发明被定点在2210年，窗口未关闭；至今没有经确认的工作用反重力陀螺升力机，但不能因日期未到判错。  
  来源：<https://skepticalinquirer.org/2017/01/project-greenglow-how-horizon-lost-the-message-in-the-medium/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/gernsback-ralph-124c-41-plus-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/gernsback-ralph-124c-41-plus-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/gernsback-ralph-124c-41-plus-v5/audit/manual_review_2026-11-15.py`
