# Manual review (METHOD.md) of Jack London, The Scarlet Plague (1912), review_source manual-assistant-2026-11-16 (coordinator recheck #7/#18)
META={'basis': '本稿由助手逐条对照书中原文与存档证据人工复核：',
 'extra': '\n'
          '## 说明\n'
          '\n'
          '- 同一论断只计一次：“巨头委员会任命总统”（第 2 条）与“十二人统治美国”“巨头委员会主席即美国统治者”合并；“国际控制委员会七人统治世界”（第 20 条）与“王室被巨头取代”“职位趋于世袭”合并；第 4 条航空包含“跨大西洋飞艇”“富人私人飞艇”；第 7 条世界人口包含“瘟疫开始时 80 亿人”“人口越来越多”；第 17 条包含“通过电线或空中交谈”。旧金山（第 3 '
          '条）、东湾（第 6 条）、纽约（第 18 条）、芝加哥／伦敦（第 19 条）是原文中各自独立的句子和独立可判定的数字，分开计。\n'
          '- 第 3、6、18 条按原文“城市／市县”口径核对；第 10 条财富分布用 2022 年 SCF 数据代表窗口内观测。\n'
          '- 第 15、16 条为虚构的具体年份疫情，核验依赖流行病史综述（含商业科普站 worldatlas）等间接反证。\n'
          '- 第 4 条速度数字来自第三方航空资讯站；第 5 条渔获量为全加州数字。\n'
          '- 协调者复核改判（2026-11-16）：第 7 条书中为确切数字（2010 年 80 亿），实际约 69 亿，按严格口径由部分符合改为错误；第 18 条原文口径为纽约市（同段写纽约市长、市警死亡及 “New York City”），市区人口 8,175,133 对不上，由部分符合改为错误。\n',
 'method': '按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文（133,855 字符，含 Gutenberg 版权页与许可证）切成 39 块（每块 3500 字符，带 600 字符上下文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（28 条原始条目；第 34—39 '
           '块为许可证，无条目），再由仓库代码完成引文对齐、归属判定、去重和导入：共 21 条候选，其中 20 条为可核验预测，1 条（“那时的人不会走路”）因无可核验指标降为 unclear；另有 7 条（6 条瘟疫后情境内的假设推演、1 条机制性社会批判）被排除。小说人物（Granser，即 2013 年的伯克利教授 James Howard '
           'Smith）以“当年现状”口吻讲述的 2010—2013 年世界，按 Bellamy、Verne 案例的做法记为 author_endorsed（作者借人物之口）。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索（40 次，池密钥第 4 条，只按文件路径读取），未追加自适应轮次；只从检索返回的 URL 中选源。原文经 Exa '
           'contents 抓取（不足时 curl）存档于 data/sources（sha256），写入 data/evidence.jsonl（42 条）。助手阅读存档原文后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。',
 'overall': '《猩红疫》是末世小说：2013 年一场瘟疫几乎灭绝人类，2073 年幸存的老教授向野蛮化的孙辈讲述旧世界。瘟疫本身和瘟疫后的部落社会属于情节前提与假设推演，未计入；计入的 20 条全部是作者借叙述者描绘的 2010—2013 年“旧世界”：寡头巨头统治美国与世界、人口与城市规模、航空与通信、农业生产率、显微技术和疾病史。结果偏差明显：3 '
            '条正确（少数人生产全社会粮食、远距离无线通话、新传染病不断出现），4 条部分符合（航空普及但速度与飞艇设想不符、财产集中但非奴隶制、显微放大远超书中数字、部分疾病被控制而结核病未灭），13 条错误。错误集中在两类：一是伦敦作为社会主义者对“巨头委员会任命总统、七名巨头统治世界、劳动者沦为奴隶”的政治设想；二是具体数字和虚构事件（2010 '
            '年世界人口八十亿、纽约市一千七百万、旧金山四百万、东湾七百万、2000 年欧洲十五亿、芝加哥为世界第一大城、1984 年巴西瘟疫、1947 年婴儿新病、麻风不可治、螃蟹捕绝）。严格胜率 15.0%，加权胜率 25.0%，错误率 65.0%。',
 'pub': '**1912 年 6 月**首刊于 The London Magazine，1915 年 Macmillan 出单行本。正文为 Project Gutenberg #21970 英文全文（gutenberg.org/cache/epub/21970/pg21970.txt），重新下载后 sha256 为 `86391fa4…`，与书单记录逐字节一致，原样作为 '
        'TXT（133,855 字符）。观察窗口为 1912 至 2026-11-15；小说设定的“旧世界”为 2010—2013 年。',
 'title': '杰克·伦敦《猩红疫》（The Scarlet Plague）'}
NF={}
V={1: ('W',
     '湾区实际修建的是常规轨道而非单轨：BART 为双轨（dual-rail）高速电气化捷运网，1972 年开通；BART 规划时虽曾考虑高架单轨方案，最终未采用',
     ['https://onlinepubs.trb.org/Onlinepubs/sr/sr111/111-002.pdf', 'https://www.bart.gov/news/articles/2022/news20220504']),
 2: ('W',
     '2012 年美国总统由选举产生：奥巴马获 332 张选举人票、65,915,795 张普选票（51.06%），并非由“巨头委员会”任命；经济精英对政策影响较大的研究（Gilens 与 Page）只说明影响力不均，不构成总统任命制',
     ['https://www.archives.gov/electoral-college/2012', 'https://www.fec.gov/resources/cms-content/documents/2012pres.pdf', 'https://www.bbc.com/news/blogs-echochambers-27074746']),
 3: ('W',
     '2010 年普查旧金山市县人口为 805,235，远低于四百万；即使整个九县湾区 2014 年也只有约 7,500,000 人',
     ['https://census.bayareametro.gov/population?location=san_francisco&year=2010', 'https://www.sfpublicpress.org/census-estimates-show-bay-area-growing-faster-than-expected/']),
 4: ('P',
     '航空成为常规交通这一点成立，但具体设想不符：主力客机波音 737 巡航速度约 515 到 540 英里/小时，远超书中“200 英里为最低、300 英里已属冒险”；客运飞艇在 1937 年兴登堡号事故后即告终结，并未与飞机并行普及',
     ['https://www.blackjet.com/post/cruise-speed-of-737', 'https://www.livescience.com/58959-hindenburg-crash.html']),
 5: ('W',
     '旧金山一带的珍宝蟹并未被捕捞殆尽：加州 2010 年捕获 27.5 million 磅，次年创纪录达 31.6 million 磅，为 100 年来最大渔获；商业捕捞季按法规为数月（旧金山所在的“其他各区”为 November 15 至 June 30），并非只有一个月',
     ['https://perishablenews.com/seafood/central-ca-crabbers-gear-up-for-commercial-dungeness-season/',
      'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FGC&sectionNum=8276.']),
 6: ('W',
     '东湾两县 2010 年普查人口：阿拉米达县 1,510,271，康特拉科斯塔县 1,049,025，合计远不到书中的七百万',
     ['https://census.bayareametro.gov/population?location=alameda_county&year=2010', 'https://www.contracosta.ca.gov/5342/Demographics']),
 7: ('W',
     '书中给的是确切数字（2010 年人口普查 80 亿），实际不符：2010 年全球人口为 6.9 billion，联合国估计到 2022 年 11 月 15 日才达到 8 billion；按确切数字的严格口径，2010 年的数字偏高约一成半，判错误（人口增至数十亿的方向虽成立，不足以支撑部分符合）',
     ['https://www.prb.org/resource/2010-world-population-data-sheet/', 'https://www.un.org/en/desa/world-population-reach-8-billion-15-november-2022']),
 8: ('W',
     '2000 年欧洲人口约 728,164,209，不到书中十五亿的一半',
     ['https://www.populationpyramid.net/europe/2000/',
      'https://www.oerproject.com/OER-Materials/OER-Media/HTML-Articles/Origins/Unit9/Population-and-Environmental-Trends-1800-to-the-Present/870L?share=embed']),
 9: ('C',
     '少数人生产全社会粮食成立：2012 年美国农业就业占比仅 1.5%；美国农场产出在 1948 至 2017 年间增至近三倍，而农业使用的土地与劳动力下降',
     ['https://fred.stlouisfed.org/series/USAPEMANA', 'https://www.ers.usda.gov/amber-waves/2020/july/productivity-is-the-major-driver-of-u-s-farm-sector-s-economic-growth']),
 10: ('P',
      '财产高度集中这一面部分成立，但“劳动者沦为奴隶”不成立：圣路易斯联储据消费者财务调查指出，2022 年顶层 10% 家庭拥有近四分之三的财富，底层 50% 家庭只拥有约 2%；而20世纪美国劳动者工时缩短、工资上升、劳动条件改善，并享有最低工资等法定保障',
      ['https://fraser.stlouisfed.org/files/docs/publications/frbsl_ov/frbstl_openvault_20240207.pdf', 'https://www.bls.gov/opub/mlr/cwc/american-labor-in-the-20th-century.pdf']),
 11: ('P',
      '显微技术大幅超越光学极限的方向成立，但数字严重偏低：1931 年 Ruska 与 Knoll 造出第一台透射电子显微镜，现代电子显微镜可放大到 ten million 倍，远超书中“最好的超显微镜四万倍”',
      ['https://ethz.ch/content/dam/ethz/special-interest/dual/scopem/PDFs/TEM.pdf',
       'https://documents.thermofisher.com/TFS-Assets/MSD/Handbooks/Exploring-uncharted-realms-with-electron-microscopy.pdf']),
 12: ('C',
      '新的传染病持续出现成立：Jones 等人统计 1940 年以来出现 335 种新发传染病，数量逐步上升并在 1980 年代达到高峰；学界估计大约每年出现一种新病',
      ['https://www.npr.org/2008/02/21/19226040/study-finds-emerging-diseases-on-rise', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7390567/']),
 13: ('P',
      '对部分疾病成立、对结核病不成立：昏睡病病例 2009 年降至 9878 例，为 50 年来首次低于 10 000；但结核病 2013 年仍有 9.0 million 人发病、1.5 million 人死亡，远未被消灭（原文下句亦自限为“有时”）',
      ['https://www.who.int/news/item/02-06-2010-human-african-trypanosomiasis-number-of-new-cases-drops-to-historically-low-level-in-50-years',
       'https://www.who.int/publications/i/item/9789241564809']),
 14: ('W',
      '麻风已可治愈：世卫组织指出麻风可用联合化疗（MDT）治愈，联合化疗自 1980 年代推广，已有近 16 million 患者接受治疗',
      ['https://www.who.int/teams/control-of-neglected-tropical-diseases/leprosy/treatment', 'https://www.pasteur.fr/en/your-health/understanding-diseases/diseases-z/leprosy']),
 15: ('W',
      '没有 1984 年在巴西爆发、致数百万人死亡的新瘟疫：20 世纪最致命的新发流行病是 1981 年发现的艾滋病；巴西 1980 年代以来的主要新发疫情是登革热，以报告病例计（如 2002 年超过 794,000 例），并非致数百万人死亡的瘟疫',
      ['https://www.worldatlas.com/articles/the-deadliest-epidemics-of-the-20th-century.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3294356/']),
 16: ('W',
      '1947 年并未出现前所未见、使婴儿瘫痪的新病：最接近的脊髓灰质炎早在 1789 年就有临床描述、1840 年被确认为独立疾病，20 世纪上半叶流行加剧；疫苗于 1955 年问世',
      ['https://www.who.int/news-room/spotlight/history-of-vaccination/history-of-polio-vaccination',
       'https://www.cdc.gov/pinkbook/hcp/table-of-contents/chapter-18-poliomyelitis.html?CDC_AAref_Val=https%3A%2F%2Fwww.cdc.gov%2Fvaccines%2Fpubs%2Fpinkbook%2Fpolio.html']),
 17: ('C',
      '跨越数千英里的无线通话成立：跨大西洋无线电话于 1927 年 1 月 7 日开通；到 2013 年全球移动电话用户达 6.8 billion',
      ['https://www.comsoc.org/node/18956', 'https://www.itu.int/en/itu-d/statistics/documents/facts/ictfactsfigures2013-e.pdf']),
 18: ('W',
      '原文口径为纽约市：“that noblest city of America”，下文同一叙事写“New York City and Chicago were in chaos”，并说纽约警察三分之一死亡、警察局长与市长也死了，指的是有市长和市警的纽约市。2010 年普查纽约市人口为 8,175,133，不到书中一千七百万的一半；纽约都市区 2013 年约 19,950,000 '
      '人，但那不是原文口径，不能用来支撑',
      ['https://www.nyc.gov/assets/planning/download/pdf/planning-level/nyc-population/census2010/dcp-2010-census-population-adjustment.pdf',
       'https://www.newgeography.com/content/004240-special-report-2013-metropolitan-area-population-estimates']),
 19: ('W',
      '芝加哥并非世界最大城市、伦敦也非第二：2014 年联合国数据中东京以 38 million 居首、德里约 25 million 居次；2010 年芝加哥市人口 2,695,598，伦敦 2011 年 8.17 million',
      ['https://www.thehindubusinessline.com/news/delhi-most-populous-city-after-tokyo/article23123036.ece',
       'https://web.archive.org/web/20220719224850/https:/en.wikipedia.org/wiki/Chicagoan',
       'https://data.london.gov.uk/download/2zjjy/f20094c9-e527-4f9e-8e41-59744862f8b4/2011-census-first-results.pdf']),
 20: ('W',
      '世界并未由七名巨头组成的“国际控制委员会”统治：2011 年南苏丹成为联合国第 193 个会员国，主权国家体系仍是世界治理基础；跨国公司股权网络研究发现控制权流向少数金融机构组成的紧密核心，这只说明经济控制集中，不构成政治统治',
      ['https://news.un.org/en/story/2011/07/381552', 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0025995'])}
