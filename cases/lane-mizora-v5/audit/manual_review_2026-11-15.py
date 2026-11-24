# Manual review (METHOD.md) of Mary E. Bradley Lane, Mizora: A Prophecy (1890), review_source manual-assistant-2026-11-16
META={'basis': '本稿由助手逐条对照书中原文与存档证据人工复核：',
 'extra': '\n'
          '## 说明\n'
          '\n'
          '- 去重只按 claims_from_results 的重叠规则（无重叠条目被丢弃），未按主题合并。第 7 条（宗教将被完全放弃）与 unclear 候选“灵魂观念终将消退”主题相近，后者不计分，不影响胜率。\n'
          '- 第 1 条以 1917 年俄国革命为主要观测，预测本身无日期、措辞宽泛，判为正确可能偏宽；第 2 条“穷人才智转向化学”的机制部分不核验。\n'
          '- 第 8 条“叙述者有生之年”按约至 1940 年理解；第 7 条以欧洲宗教归属比例近似“智识普及”的社会。\n'
          '- 9 条 unclear 隐含技术预言（人造肉、无线电话、视频通话、电动车等）若改按预测计分，多数会判正确，胜率会明显上升；本稿按原文未明确指向外部世界而不计入。\n',
 'method': '按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文（339,078 字符，含 Gutenberg 版权页、序言与许可证）切成 98 块（每块 3500 字符，带 600 字符上下文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（18 条原始条目；第 '
           '93—98 块为许可证，无条目），再由仓库代码完成引文对齐、归属判定、去重和导入：共 18 条候选，其中 8 条为可核验预测，10 条为 unclear（9 条是以米佐拉“现状”呈现的隐含技术预言——人造肉、人工降雨、扫地机、电动车、电解水制氢燃料、远距离通话、远程影像演讲、可视通话、化学纺丝；1 条“灵魂观念终将消退”对象不明），不计分。核验：每条先写 '
           'scope，各做一次 support 与 counter 的 Exa 检索（第 2、6 条另加一轮，共 20 次，池密钥第 4 条，只按文件路径读取）；只从检索返回的 URL 中选源。原文经 Exa contents 抓取存档于 data/sources（sha256），写入 data/evidence.jsonl（20 '
           '条）。助手阅读存档原文后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。',
 'overall': '《米佐拉》是女性乌托邦小说：俄国流亡贵妇在北极地下发现一个只有金发女性的国度，那里以化学合成食物、电力与压缩空气驱动交通、远距离影像通话，并通过普及免费教育消灭了贫困、疾病、犯罪与宗教。书中大部分“未来技术”以米佐拉的现状写出，原文并未断言外部世界将会实现，按 DISCOVER_PROMPT_V5 记为 unclear、不计分。计入的 8 条都是米佐拉人（院长 '
            'Preceptress 与其女 Wauna）明确针对叙述者世界的判断，按 Bellamy、Verne 案例做法记为 author_endorsed。结果：3 条正确（未受教育的劳工暴力反抗资本——1917 年俄国革命；机器承担繁重家务；以机器替代役畜带来显著农业经济变化）；3 '
            '条部分符合（化学使照明和食物变廉价但化石燃料没有结构性降价；教育普及后宗教世俗化但远未“完全放弃”；美国领先普及公共教育但到 1940 年仍只有约一半青年中学毕业）；1 条错误（人类永远无法改变花香——转基因玫瑰的香气化合物可提高到 6.5 倍）；1 条（贫困与疾病消失）因“以石头为食”的前提从未实现记为暂无法判断。',
 'pub': '1880—1881 年连载于《Cincinnati Commercial》，**1890 年**由 G. W. Dillingham 出单行本（书单 orig_pub_date=1890，以此为出版年代理）。正文为 Project Gutenberg #24750 英文全文（gutenberg.org/cache/epub/24750/pg24750.txt），重新下载后 '
        'sha256 为 `d291f7a4…`，与书单记录逐字节一致，原样作为 TXT（339,078 字符，CRLF 换行）。观察窗口为 1890 至 2026-11-15。',
 'title': '玛丽·E·布拉德利·莱恩《米佐拉：一个预言》（Mizora: A Prophecy）'}
NF={}
V={1: ('C',
     '条件（穷人未受教育）成立且结果出现：1897 年俄国人口普查中 10 岁以上识字者仅 26.5%；1917 年俄国革命由罢工工人和要面包的示威群众发动，彼得格勒的抗议者与警察冲突，数日后沙皇尼古拉退位，受压迫的劳动者确实以暴力起来反抗有产阶级',
     ['https://www.history.com/articles/russian-revolution', 'https://nottingham-repository.worktribe.com/OutputFile/16503447']),
 2: ('P',
     '照明和食物两项成立，燃料一项不成立：从木柴、蜡烛、煤气灯到电灯，照明成本下降了近 100%（Human Progress 引 Nordhaus 的测算）；哈伯—博施合成氮肥如今支撑约一半的世界人口；电价在 1890—1920 年间实际每年平均下降 6%，但化石燃料价格因资源耗竭和卡特尔并未出现结构性下降',
     ['https://humanprogress.org/trends/lighting-costs-near-nothing-now/',
      'https://ourworldindata.org/how-many-people-does-synthetic-fertilizer-feed',
      'https://www.powermag.com/a-look-back-at-electricity-rates/',
      'https://www.construction-physics.com/p/on-technologies-vs-commodities']),
 3: ('U',
     '前提只部分出现：木浆制成的人造丝（rayon）1910 年在美国商业化生产，但“以石头为食”从未实现，条件不成立，按规则不判对错；作为背景，按世界银行 2025 年口径，2022 年仍有约 838 million 人生活在极端贫困中，贫困并未消失',
     ['https://www.fibersource.com/f-tutor/rayon/', 'https://www.worldbank.org/en/news/factsheet/2025/06/05/june-2025-update-to-global-poverty-lines']),
 4: ('C',
     '机器承担繁重家务已成惯例：1900 年没有家用电器的美国家庭每周在做饭、洗衣和清洁上花 58 小时，此后洗衣机、冰箱等家用设备迅速普及；到 2005 年 18 至 64 岁女性每周家务时间比 1900 年少 18 小时',
     ['https://www.nber.org/system/files/working_papers/w32253/w32253.pdf', 'https://www.nber.org/digest/oct08/hours-spent-homemaking-have-changed-little-century']),
 5: ('W',
     '人类已能改变花香：转入 PAP1 转录因子的玫瑰释放的萜类香气化合物最多达对照的 6.5 倍，嗅觉测试显示蜜蜂和人都能分辨其花香差异；2015 年研究又找到决定玫瑰香气的关键基因 RhNUDX1，可望用于把香气重新育回玫瑰；花香调控与基因工程已成为专门的研究领域',
     ['https://nph.onlinelibrary.wiley.com/doi/10.1111/j.1469-8137.2012.04161.x',
      'https://pmc.ncbi.nlm.nih.gov/articles/PMC11500596/',
      'https://www.sciencedaily.com/releases/2015/07/150702152526.htm']),
 6: ('C',
     '以机器替代役畜确实带来显著的农业经济变化：1930 年美国仍有 65 million 英亩耕地用于饲养马和骡，到 1960 年只剩 5 million 英亩；每头役畜每年约需 6 英亩饲料地，腾出的土地可改种出售的作物',
     ['https://www.nber.org/system/files/working_papers/w7947/w7947.pdf', 'https://www.si.edu/stories/five-ways-tractor-changed-american-farming']),
 7: ('P',
     '宗教形式与信仰随教育普及而变化、世俗化方向在欧洲成立，但“完全放弃”远未出现：到 2020 年欧洲约三分之二居民仍是基督徒，无宗教者约占四分之一；2020 年全球仍有 75.8% 的人自认属于某一宗教',
     ['https://www.pewresearch.org/religion/2025/06/09/religion-in-europe/', 'https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/']),
 8: ('P',
     '美国确实领先世界普及公共教育：1918 年密西西比州成为最后一个通过义务教育法的州；1910 至 1940 年中学在学比例由 18% 升至 71%，毕业比例由 9% 升至 51%，美国在普及公费中学教育方面领先其他国家。但到 1940 年仍只有约一半青年中学毕业，并未让“每个孩子”都得到当时最高水平的教育',
     ['https://openhistory.education/pages/compulsion_schooling', 'https://doi.org/10.3386/w10075', 'https://www.nber.org/papers/w6439'])}
