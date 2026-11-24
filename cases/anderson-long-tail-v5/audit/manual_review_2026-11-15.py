# Manual review of 长尾理论 (Chris Anderson, The Long Tail, 2006), review_source manual-assistant-2026-11-15
HBR='https://hbr.org/2008/07/should-you-invest-in-the-long-tail'
ADELE='https://www.billboard.com/pro/adele-25-historic-chart-numbers/'
LUM='https://www.billboard.com/pro/music-streaming-2023-statistic-songs-played-zero-times/'
RS='https://www.rollingstone.com/pro/news/top-1-percent-streaming-1055005/'
RIAA='https://www.billboard.com/pro/riaa-2024-year-end-music-report-streaming-vinyl-revenue/'
NFLX='https://www.reuters.com/article/lifestyle/netflix-launches-1000-title-online-movie-feature-idUSN11457284/'
PW='https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/96468-self-publishing-s-output-and-infuence-continue-to-grow.html'
PEW14='https://www.pewresearch.org/politics/2014/06/12/political-polarization-in-the-american-public/'
PEW20='https://www.pewresearch.org/journalism/2020/01/24/u-s-media-polarization-and-the-2020-election-a-nation-divided/'
ITU='https://www.itu.int/itu-d/reports/statistics/2024/11/10/ff24-internet-use/'
META=dict(title='克里斯·安德森《长尾理论》（The Long Tail）',
 pub='Hyperion **2006 年 7 月 11 日**初版，按 **2006-07** 起算。正文用 `reading-library/2026-11-15-未来判断书单/03-科技和AI/20-长尾理论.pdf`（Hyperion 2008 年增订电子版，Adobe Acrobat eBook Reader October 2008，ISBN 978-1-4013-8725-9，282 页，sha256 `f327e116…`，已与 catalog.json / SHA256SUMS 核对）。版权页列 2006、2008；Open Library 等书目载明，2008 年 7 月 8 日的 Revised and Updated 增订本新加入第 15 章 “The Long Tail of Marketing” 与 Epilogue。这两部分可明确识别为修订新增，其中的预测（如麦肯锡关于 2010 年电视广告效力、Epilogue 里对 Type 1/2/3 热门的分类判断等）**未纳入本次计分**。正文里偶有 2007 年事实性括注（如亚马逊推出 MP3 下载），视为修订插入，不单独当作新预测。观察窗口为 2006-07 至 2026-11-15；书中写明的“soon”“someday”“此后数十年”“21 世纪”按各自的表述判断。',
 method='本书没有现成的 v5 抽取结果（不使用 DeepSeek，也不用 LLM 抽取）。候选句由助手通读 PDF 文字层、并对 will／going to／soon／someday／future／decades 等做检索后，手工挑选作者本人可核验的判断，共 35 条。第 15 章与 Epilogue 中仅见于 2008 年修订的内容一律排除，不进入 `claims.jsonl`。引文逐字取自 pdftotext 25.03.0 按页抽取的文字层（保留连字 ﬁ／ﬂ 等原文字形），`data/claims.jsonl` 里记录了 PDF 页码、页内字符位置和 PDF 的 sha256；为避免版权问题，未把全文文本放进仓库。',
 basis='本稿由助手逐条对照扫描本原文人工复核：',
 overall=('《长尾理论》把 2004 年那篇 Wired 文章扩成一本书，核心命题是：当货架和渠道不再稀缺，文化与商业会从少数热门转向海量利基，过滤和推荐会成为新的稀缺资源。**方向性的判断大体应验了。** 流媒体、用户生成内容和自出版把“无限货架”做成了默认基础设施：Netflix 在 2007 年推出在线播放，后来自己带头把海量片目变成即时可得；任天堂 Wii 的 Virtual Console 把回溯游戏做成可下载的长尾；美国录音产业收入在 2024 年已有约 84% 来自流媒体订阅等新模式；YouTube、TikTok、Kindle Direct Publishing 让业余创作者以前所未见的速度填满长尾；半小时电视之外，碎片化短视频成为主流移动形态。安德森说大众文化“不会消亡，只是不那么大众”，也比“热门将死”更经得起时间检验。'
 '\n\n**定量的“需求曲线会变平、利基将与热门平起平坐”则明显说满了。** 哈佛商学院 Anita Elberse 2008 年就在《哈佛商业评论》里指出，Rhapsody 前 1% 曲目仍占 32% 的播放、前 10% 占 78%。流媒体时代这一集中度往往更高：Alpha Data 统计，2019—2020 年间约 1% 的艺人拿走了 90% 的播放。Luminate 2023 年数据更直接打脸“几乎每一首歌都会卖掉”：在 1.84 亿首有 ISRC 的录音中，约 4560 万首（25%）全年零播放。Adele《25》2015 年首周售出 338 万张，打破了安德森以为“很可能再也无法打破”的 *NSYNC 242 万张纪录。篇末关于家用 3D 打印会像喷墨打印机一样普及、实物长尾会经光纤送到家里再物化的想象，到 2026 年也没有成为日常生活。他押注“近乎无限的信息会让人更开放”，结果被随后二十年的政治极化打脸。'
 '\n\n总体看，这本书对**渠道和供给端**（无限货架、过滤为王、业余生产爆发、视听全面宽带化）看得很准，对**需求端的平等化**过于乐观：长尾变长了、变厚了一点，但头部往往更集中，而不是被削平。'),
)
NF={}
V={
1:('T','“一刀切”的大众市场确实不再是唯一形态：流媒体、电商和用户生成内容把选择权交给了个人，SKU 和频道数量远超 2006 年。但超级碗、漫威电影、泰勒·斯威夫特式的超级热门仍然存在，大众市场是变小了，并没有结束',['w:Cord-cutting','w:Streaming_media']),
2:('C','数字娱乐经济与 2006 年的大众市场已截然不同：唱片店和音像租赁店基本消失，付费下载之后是订阅流媒体，视频从院线和电视档期转向 Netflix、YouTube 等按需平台。美国录音产业 2024 年收入中流媒体约占 84%',[RIAA,'w:Streaming_media','w:Music_download']),
3:('P','利基确实成为二十一世纪娱乐的重要一半：独立音乐、网剧、播客、游戏模组和同人作品都有了可持续的分发渠道。但“同样关于利基”说得过满——播放和收入仍然高度集中在头部，流媒体时代约 1% 的艺人拿走约 90% 的播放，热门并未与利基平起平坐',[RS,HBR,'w:The_Long_Tail_(book)']),
4:('W','“几乎每一首都会卖掉”在目录规模扩大后并不成立。Luminate 统计，2023 年 1.84 亿首有 ISRC 的录音中，约 4560 万首（25%）全年零播放，约 82.7% 的曲目播放不足 1000 次。安德森所依据的是当时 Rhapsody 相对较小的曲库；放到今天的海量目录上，这条判断失败了',[LUM]),
5:('T','条件成立：书店货架之外的图书市场远比 2006 年所见更大。Bowker 统计，2023 年仅自出版、带 ISBN 的新书就约 260 万种，比 2022 年再增 7.2%；Kindle Direct Publishing 等平台让长尾书成为常规供给。实际扩张幅度已超过“再大一半”的估计，故记趋势符合而非逐字“正确”',[PW,'w:Self-publishing','w:Kindle_Direct_Publishing']),
6:('C','此后二十年，音乐、影视、出版和零售都被无限货架和推荐系统改造：Netflix、Spotify、Amazon、YouTube 成为各自行业的默认基础设施，文化消费方式也从同步大众档期转向按需和兴趣社群。正反馈在渠道端确实运转了数十年',['w:Streaming_media','w:Netflix','w:Amazon_(company)']),
7:('W','*NSYNC《No Strings Attached》2000 年首周约 241.6 万张的纪录被打破：Adele《25》在 2015 年 11 月 26 日当周售出 338 万张（Nielsen），是 SoundScan 有记录以来最大的单周专辑销量',[ADELE,'w:25_(Adele_album)']),
8:('P','实体专辑时代的“工厂式”少年偶像机器和超白金首周销量整体走弱，这一点应验了。但爆款并没有结束，只是换了形态：Adele、泰勒·斯威夫特、Drake 等在流媒体和巡演中仍是文化级大热门，头部集中度甚至更高。说“爆款时代终结”只说对了介质，没说对结构',[ADELE,RS,'w:Music_industry']),
9:('T','兴趣社群和跨地域的网络部落成为日常组织方式，地理和同步广播的约束明显下降。不过国家、语言和线下生活仍在定义认同，并不是完全由兴趣取代地理',['w:Internet_culture','w:Social_media']),
10:('P','长尾被拉长了：远比实体店更多的书、歌、片能找到至少一个听众。但“需求曲线变平、热门相对不那么热”并未系统性出现。Elberse 2008 年对 Rhapsody 的统计显示前 10% 曲目仍占 78% 播放；Alpha Data 2019—2020 年数据显示约 1% 的艺人占 90% 的流媒体播放，头部往往更集中而不是更扁',[HBR,RS]),
11:('P','在部分市场，利基加总确实是一股可观力量：早期亚马逊图书、Google AdSense、eBay 都靠长尾客户做成了大生意。但在音乐流媒体这一本书最核心的例子里，利基加总并不能与头部匹敌——约 1% 的艺人拿走约 90% 的播放',[HBR,RS]),
12:('C','业余和半职业生产的速度远超 2006 年的想象：YouTube、TikTok、Bandcamp、自出版和应用程序商店让个人可以持续上传作品；流媒体平台一度达到每天数万甚至更高的新曲上传量。长尾被填满的速度前所未见',['w:YouTube','w:TikTok','w:User-generated_content']),
13:('C','维基百科词条从成书时的约百万量级扩展到数百万条，快速修订和反破坏机制覆盖了绝大部分条目，多数恶意篡改会在短时间内被回退。自我修复随规模扩展，这一点应验了',['w:Wikipedia','w:Reliability_of_Wikipedia']),
14:('T','“正式出版”的边界确实模糊了：Kindle Direct Publishing 自 2007/2009 年起把网络发表变成常规的第一阶段，Bowker 统计 2023 年自出版 ISBN 约 260 万种。不过传统出版社的品牌和渠道仍有分量，“正式出版的书”并未失去全部含义；“未来几年”内趋势已经展开，只是没有把旧定义彻底取消',[PW,'w:Kindle_Direct_Publishing']),
15:('T','从 YouTube、TikTok 走出来的艺人和创作者成为娱乐业的常规人才管道（如贾斯汀·比伯等）。“拯救好莱坞于刻板公式”则说得过满：漫威式公式大片同期更加兴盛。方向对，程度和结果只对了一半，故记趋势符合',['w:YouTuber','w:Justin_Bieber','w:TikTok']),
16:('T','CD 之前的大量录音已经出现在 Spotify、Apple Music 等目录中，包括重新灌录的老唱片和现场录音。但版权空隙仍在，尤其是更早的录音、地方和古典曲目，并不是“大部分”都已完整数字化',['w:Spotify','w:Music_streaming_service']),
17:('P','数字音乐服务最终把曲库做到了数千万量级，版权清算也出现了集体管理的工业化安排，方向对。但文中的“他们”以亚马逊等传统零售商为主，亚马逊并未成为把音乐长尾铺到尽头的主场，赢家是 Spotify、Apple Music 等专门的流媒体。句中“2007 年推出 MP3 下载”的括注是 2008 年修订插入的事后说明，判断窗口仍按 2006-07 起算',['w:Amazon_Music','w:Spotify']),
18:('C','按需印刷成为自出版和回溯书目的常规技术：Amazon Kindle Direct Publishing Print、Ingram Lightning Source 等把零库存出书做成了产业标配，采用速度明显加快',['w:Print_on_demand','w:Kindle_Direct_Publishing']),
19:('C','Netflix 于 2007 年 1 月 16 日推出当时名为 Watch Now 的在线播放，随后把公司重心转到流媒体，并在权利允许的范围内把大量片目做成即时可得。它确实自己带头完成了作者所设想的那一步；完整 DVD 目录并未全部上线，但判断的主干成立',[NFLX,'w:Netflix']),
20:('C','代号 Revolution 的主机即 2006 年 11 月发售的 Wii。Virtual Console 从 2006 年底起提供 NES、SNES、N64、世嘉 Genesis 等回溯游戏的付费下载，把过往目录做成了可检索的长尾内容',['w:Virtual_Console','w:Wii']),
21:('T','用户生成平台和应用商店几乎让“先上网、再看有没有人要”成为默认；推荐、搜索和排行成了真正的稀缺能力。说“所有东西”都会进市场是修辞上的夸大，但分拣取代前置把关这一转向已经发生',['w:Recommender_system','w:YouTube','w:App_store']),
22:('P','“不必再只经营头部”这一层应验了：数字库存成本接近于零，卖长尾在商业上变得合理。但“销售会在热门与利基之间更均匀”并未普遍出现，流媒体的集中度往往更高。80/20 作为经营教条是松了，作为需求形态并没有失去锋芒',[HBR,RS]),
23:('C','唱片业随后确实转向了新模式：从单曲 0.99 美元下载，到 Spotify 等免费增值和付费订阅，再到与视频平台、通信和电商的捆绑。美国录音产业 2024 年收入中流媒体约占 84%，付费订阅是其中的主体',[RIAA,'w:Music_streaming_service']),
24:('T','网络电视份额持续下降，同步“全村人看同一档节目”的场景变少，利基文化也比以前容易被找到。与此同时，超级碗、现象级流媒体剧和巡演仍然能制造大众时刻。大众文化变“薄”了，但没有消失，与原文的分寸大体一致',['w:Cord-cutting','w:Streaming_television']),
25:('C','兴趣部落、粉丝圈、政治自媒体和垂直社区成为社会组织的常见单元，联系更多靠共同兴趣而不是办公室饮水机或地理邻近。社交媒体把这一转变做成了基础设施',['w:Social_media','w:Internet_culture']),
26:('W','作者承认回音室风险，却押注好奇心会让大多数人更开放。此后美国等国的政党情感极化明显上升：皮尤 2014 年报告显示两党对对方的强烈负面评价较 1990 年代翻倍以上，2020 年的媒体使用和信任也按意识形态明显分裂。信息总量增加了，开放程度并没有随之提高',[PEW14,PEW20]),
27:('C','文化消费在很大程度上变成按兴趣并行的许多条线：人们仍与他人共享文化，但不再与“所有人”共享同一套节目单。大众文化淡化、共同文化以圈层形式保留，与这条判断相符',['w:Internet_culture','w:Social_media']),
28:('C','手机短视频成为日常消费形态：从 Vine 到 TikTok、Instagram Reels、YouTube Shorts，专门用于通勤和间隙观看的短内容已经规模化，时机和形态都与预测一致',['w:TikTok','w:Vine_(service)','w:YouTube']),
29:('P','短内容确实爆发，长内容也在流媒体上走强（剧集往往比半小时更长的“优质电视”）。但半小时情景喜剧并未消亡，仍是流媒体和广播的常规长度。“任意的中间长度将无法站稳”只说对了一半',['w:TikTok','w:Streaming_television','w:Sitcom']),
30:('C','互联网把可看的电影和视频扩大了几个数量级：YouTube、Netflix、Prime Video、Disney+ 以及各种免费和盗版渠道，选择远不止“千倍”，用“无数倍”来形容并不夸张',['w:Streaming_service','w:YouTube','w:Netflix']),
31:('T','谷歌后来的广告增长确实大量来自搜索和 AdSense 所覆盖的长尾查询、长尾网站和中小广告主；YouTube 也把大量小创作者纳入广告网络。与此同时，品牌广告、移动端和云服务同样是增长来源，不能说增长“主要”只来自长尾，故记趋势符合',['w:Google_Ads','w:AdSense']),
32:('T','版权和授权至今仍是限制回溯电影、音乐采样和完整曲库上线的主要摩擦之一。与此同时，内容过载和推荐算法也成了新的瓶颈，法律限制不再是唯一的“首要”障碍，但作为约束条件依然成立',['w:Copyright','w:Music_licensing']),
33:('C','宽带对电影、游戏和电视的冲击在随后几年内就到来：Netflix 2007 年起流媒体化，电视转向订阅点播，游戏则出现数字下载和云游戏。与音乐经历过的“去原子化”十分相似，而且来得很快',['w:Streaming_media','w:Netflix','w:Cloud_gaming']),
34:('W','消费级 3D 打印机价格已降到数百美元，但仍是创客、教育和爱好者工具，远未达到喷墨打印机的家庭普及程度。美国等市场的家用打印机仍是常见办公设备，消费级 3D 打印的家庭渗透率仍很低，谈不上“像喷墨一样常见”',['w:3D_printing','w:Inkjet_printing']),
35:('W','“物的长尾以比特存储、经光纤到家、在消费端物化”没有成为日常消费方式。人们主要仍通过电商把现成的原子商品运上门；面向消费者的在线 3D 打印平台（如 Shapeways 的消费市场）未能普及，家用自制也只覆盖少数玩具和配件',['w:3D_printing','w:Shapeways']),
}
