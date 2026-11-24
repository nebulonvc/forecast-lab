# Manual review (METHOD.md v5) of Bertrand Russell, Icarus; or, The Future of Science (1924)
# review_source = manual-assistant-2026-11-15
META = {'title': '伯特兰·罗素《伊卡洛斯，或科学的未来》（Icarus; or, The Future of Science，1924）',
 'pub': '伯特兰·罗素（Bertrand Russell）**1924** 年由伦敦 Kegan Paul, Trench, Trubner & Co. 出版，To-Day and To-Morrow '
        '丛书短篇科学前瞻；所用美国 Dutton 印本版权页记有 1924 年 6 月第二次印刷。正文用 '
        '`reading-library/2026-11-15-未来判断扩展100本/05-技术与科学/096-icarus-or-the-future-of-science.txt`，与 Project '
        'Gutenberg #66225（pg66225.txt）逐字节一致（64,256 字节，sha256 '
        '`eff5586291d05c0be8a56c095ec7720252478252a3a140d09118d9b5df53f362`），CRLF 原样使用，未转换。TXT 不入库。预测窗口按 '
        '1924→2026-11-15 计；写明“此后约五十年”的条目以约 1974 年为终点。',
 'method': '本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main '
           '`85e6da1`，prepare_book.py md5 `01fc49ad64795a345ca1cb32bb2e4366`）把全文切成 19 块（3500 字符、600 '
           '字符上下文）。英文封面、目录、版权页等未被中文前后附文正则识别（`excluded_matter_spans=[]`），由助手按块人工排除前后附文后，对正文逐块按 DISCOVER_PROMPT_V5 '
           '写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 44 条候选，全部为可核验预测（resolvable）。核验：对全部 44 条先定 scope，用 '
           'Exa（池密钥第 4 条，只按文件路径读取）各做一次 support/counter 检索，必要时补一轮适应性检索；只从检索返回的 URL 中选源，优先独立第三方（联合国、Our World in '
           'Data、OECD、NIH/NHGRI、学术期刊与官方机构），存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`。再经 `pipeline.py '
           'apply assess → check`，报告由 canonical `manual_report.py`（md5 `682248fa9f6c63e3492a559ccac12761`）生成，不手改。',
 'basis': '本稿由助手逐条对照书中原文与存档证据人工复核：',
 'overall': '这是 1924 年的短篇科学前瞻，核心论点是科学将增强主导群体的权力，并可能威胁文明。44 条预测全部进入核验，其中 6 条因世界政府或官方育种等条件未触发、或缺少可核验指标而暂无法判断；可判定 38 '
            '条。13 条正确：孟德尔式遗传使农业发生革命、生物武器能力出现、技术上可选择子女性别、广播获得巨大效力、1924–1974 '
            '年政府权力显著增强、世界经济更趋一体、世界作为产消单位的技术条件已经具备、部分发达国家随后出现人口减少、多国在出版后获得强制绝育权且起初用于所谓“低能”、心理宣传技术被用于塑造对政府的信任、生理学找到控制情绪的方法、科学（尤其核武器）构成文明级毁灭威胁。2 '
            '条趋势符合：宪政对军备的控制持续削弱但未过时；药物和激素已能部分调节情绪与性欲，但远未达到“随心所欲”。16 '
            '条部分符合，多为方向成立、程度或伴随后果过强（例如性别选择造成男性过剩但家庭制度并未彻底改变；欧洲裔占世界人口份额下降，但并未在雇佣军哗变中被灭绝）。7 '
            '条错误：优生学并未成为精密科学、两集团争霸的胜者并未建立世界政府、1974 '
            '年前大多数白人国家人口并未静止、政府并未为保兵源而阻止在非洲推广节育、反叛者并未被普遍作为低能加以绝育、绝育并未提高平均智力、初等教育也并未改以注射或饮食造就性情。对 1924 '
            '年的书采用出版日至截止日的长窗口，趋势符合从严，不以密度为目标放宽标准。',
 'extra': '\n'
          '## 说明\n'
          '\n'
          '- 前后附文人工排除：`prepare_book` 没有识别出 matter 区段（`excluded_matter_spans=[]`）。txt-00001 中 Gutenberg 版权头、书名页、“BY '
          'THE SAME AUTHOR”广告、印刷记录和目录（字符 0–2443，至 “I. INTRODUCTORY” 之前）按前后附文排除，只抽取正文起始段。txt-00013 中结论之后的 '
          "Transcriber's Notes（自字符 44943 起）以及 txt-00014–00019 的 Gutenberg 完整许可证全部排除，回答为空。结论一章本身是正文，已抽取。\n"
          '- 英文 `changes` 均为 quote 对齐后原文的逐字单行子串，不跨行。44 条候选全部通过 `validate_chunk_predictions` 与 '
          '`claims_from_results`，无重叠去重、无归属降级。\n'
          '- 抽取密度：44 条可核验 / 19 块 ≈ 0.23 条/块，处于 METHOD 英文书参考区间（约 0.2–0.35）内。按正文块（txt-00001–00013，后 6 块为许可证）计约为 '
          '3.4，偏高是因为这是几乎通篇在做前瞻的短册，而非为凑密度放宽标准。\n'
          '- 第 23 条“五十年内大多数白人国家人口趋于静止”按明确窗口判至约 1974 年：当时欧洲和北美人口仍在增长，判错误，不把此后出现的人口下降前移到该窗口。第 24 '
          '条（可能继续减至人口减少）按出版日至截止日判断，为正确。\n'
          '- 第 21、22、29 条涉及世界政府：至截止日尚未建立，未给出时限的路径判断或未触发条件一律记暂无法判断，不把“百年未出现”直接判错。\n'
          '- 证据均为第三方公开来源（Our World in Data、联合国人口司、OECD、NHGRI、《科学》、NobelPrize.org 等）。第 42 条的 Exa 检索曾返回本书 '
          'Gutenberg/马克思主义者互联网档案馆全文，以及罗素 1951 年《科学对社会的影响》中的相近表述，这些与原书大段重合或只是作者后来复述预测，已不作为结果证据，并在该条 limitation '
          '中注明。\n'
          '- 案例的 `context` 字段按协调者口径清空（`claims.jsonl` 与 `claims_proposals.jsonl`）。\n'
          '- 弗吉尼亚 1924 年绝育法通过时间与本书印次接近，第 30 条不以该州单部法律为唯一依据，而以出版后多国扩展（Buck v. Bell 1927、瑞典等）为观测。\n'}
NF = {}
V = {1: ('P',
     '20世纪后半叶国家显著把科学技术用于监控与社会控制（MIT/Marx）；同时预期寿命、公共卫生和福利国家也把科学转化为普遍福利（Deaton/EH.net，PMC）。科学既增强了主导群体的权力，也增进了幸福，“而非让人幸福”这一对照不能成立。',
     ['https://web.mit.edu/gtmarx/www/techandsocial.html',
      'https://eh.net/book_reviews/the-great-escape-health-wealth-and-the-origins-of-inequality/',
      'https://pmc.ncbi.nlm.nih.gov/articles/PMC1449802/']),
 2: ('C',
     '孟德尔遗传学成为现代育种基础，绿色革命使主要谷物单产大幅提高（俄勒冈州立大学教材；Borlaug '
     '1970年诺贝尔演讲中的美国玉米单产：1940年1.8吨/公顷至1999年约7.7吨/公顷）。遗传理论确实使农业发生了革命。',
     ['https://open.oregonstate.education/cultivatedplants/chapter/geneticimprovements/',
      'https://www.nobelprize.org/uploads/2018/06/borlaug-lecture.pdf']),
 3: ('C',
     '微生物学使生物武器成为可能：日本731部队等已研发并使用鼠疫等病原体（Clinical Microbiology and '
     'Infection；PBS时间线）。后来《禁止生物武器公约》限制了使用，但不否定“得以用疾病消灭敌人”这一能力已经出现。',
     ['https://www.clinicalmicrobiologyandinfection.org/article/S1198-743X(14)64174-4/fulltext',
      'https://www.pbs.org/wgbh/americanexperience/features/weapon-timeline/',
      'https://www.cfr.org/articles/governance-or-arms-control-the-future-of-the-biological-and-toxin-weapons-convention']),
 4: ('W',
     '美国国家人类基因组研究所将优生学定性为不道德的伪科学，其遗传理解是错误且带偏见的；《科学》杂志回顾亦强调其政治意识形态性质。遗传研究并未使优生学成为精密科学。',
     ['https://www.genome.gov/about-genomics/educational-resources/timelines/eugenics',
      'https://www.science.org/doi/10.1126/science.abm4415']),
 5: ('C',
     '胚胎植入前基因检测（PGT）等技术已能在体外受精中选择胚胎性别（PMC综述；ASRM 2022伦理意见）。许多国家限制非医学目的使用，但“能够按意愿决定子女性别”的技术能力已经实现。',
     ['https://pmc.ncbi.nlm.nih.gov/articles/PMC10504547/',
      'https://www.asrm.org/practice-guidance/ethics-opinions/use-of-reproductive-technology-for-sex-selection-for-nonmedical-reasons-an-ethics-committee-opinion-2022/']),
 6: ('P',
     '条件已部分满足：性别选择技术被用于群体层面。中国、印度等地因产前性别选择出现严重出生性别比失衡、男性过剩（PMC；UNFPA《出生性别失衡》）。家庭与婚姻市场因此紧张，但并非“家庭制度的彻底变化”。',
     ['https://pmc.ncbi.nlm.nih.gov/articles/PMC3168620/',
      'https://unfpa.org/sites/default/files/pub-pdf/Sex%20Imbalances%20at%20Birth.%20PDF%20UNFPA%20APRO%20publication%202012.pdf',
      'https://pmc.ncbi.nlm.nih.gov/articles/PMC10504547/']),
 7: ('C',
     '广播在20世纪迅速成为大众媒介，既能影响舆论，也成为娱乐与新闻的主力（LibreTexts大众传播教材）。公众将其接受为日常媒介而非仅仅宣传工具后，其效力已经非常巨大。',
     ['https://socialsci.libretexts.org/Bookshelves/Communication/Journalism_and_Mass_Communication/Book%3A_Media_Society_Culture_and_You_(Poepsel)/01%3A_Chapters/1.07%3A_Radio_Broadcasting_Podcasting_and_Superbug_Media']),
 8: ('P',
     '形式民主在全球显著扩大（Our World in '
     'Data：20世纪下半叶选举成为主导的领导人产生方式）。与此同时存在精英理论和民主回潮，但1924–2026年整体上实际政治参与和权利也随普选、民权而扩大，并非“真正民主控制一味趋于下降”。',
     ['https://ourworldindata.org/the-rise-of-electoral-democracy']),
 9: ('P',
     '20世纪极权体制中，大众传媒与宣传使领袖个人崇拜和权力集中极为显著（人格崇拜研究；独裁体制权力个人化）。但网络社会中传播技术也产生了去中心化与反权力（Castells）。方向在部分历史阶段成立，并非单向到底。',
     ['https://pressto.amu.edu.pl/index.php/pp/article/download/19209/18950',
      'https://eprints.gla.ac.uk/396904/1/396904.pdf',
      'https://ijoc.org/index.php/ijoc/article/download/46/35']),
 10: ('P',
      '国际联盟未能阻止第二次世界大战（二战博物馆）。此后联合国及WTO等体现了部分政治与经济国际主义，并取得有限成功，但并未达到作者所说的以国际协议划分原料与市场的完整经济国际主义，政治国际主义也远未完全成功。',
      ['https://www.nationalww2museum.org/war/articles/world-war-ii-and-founding-united-nations',
       'https://www.nottingham.ac.uk/gep/documents/seminars/2013/nelson-17-05-13.pdf']),
 11: ('P',
      '在经济权力仍大量私有的社会里，超级富豪对选举与政策的影响力被充分记载（Winters/LSE，Inequality.org）。但自由主义民主同时以宪政、法治和公民权利保障多数人的自由（Rodrik等），“自由只属于少数人”这一绝对表述不能成立。',
      ['https://blogs.lse.ac.uk/usappblog/2026/05/14/how-oligarchs-dominate-our-democracies-and-preserve-inequality/',
       'https://inequality.org/article/an-oligarchy-expert-answers-our-questions/',
       'https://drodrik.scholar.harvard.edu/files/dani-rodrik/files/the_political_economy_of_liberal_democracy_feb2019.pdf']),
 12: ('P',
      '“很快”的窗口内，1930年斯穆特—霍利关税标志自由贸易严重倒退，1930年代多国出现新闻审查与舆论控制（Princeton；Atlantic '
      '1938）。但这些理想并未永久成为过去：战后关税与贸易总协定、新闻自由与教育体系在许多国家得到重建和扩大。',
      ['https://press.princeton.edu/books/ebook/9781400888429/peddling-protectionism-pdf',
       'https://www.theatlantic.com/magazine/archive/1938/03/government-by-mimeograph/654938/']),
 13: ('T',
      '美国等国行政战争权扩张、国会权威边缘化（Georgetown战争权综述；Miller '
      'Center论杜鲁门单边主义）显示宪政控制军备的方向是削弱。欧洲议会战争权研究也表明多数立法机构的防务监督并不强。该控制并未完全过时，终点未到，方向持续。',
      ['https://nationalsecurity.law.georgetown.edu/wp-content/uploads/2026/07/Presidential-War-Powers-Executive-Expansion-and-Congressional-Retreat-Johnson-and-Klaris-16.2.pdf',
       'https://millercenter.org/the-living-presidency/first-general-declarer-wars',
       'https://www.dcaf.ch/sites/default/files/publications/documents/PP27.pdf']),
 14: ('C',
      '在约1924–1974的五十年窗口内，工业国政府支出占GDP的份额大幅上升：Maddison表显示法国由1913年的8.9%升至1973年的38.8%；Tanzi/Schuknecht与IMF综述记载一战后至1960–1980年代公共支出份额持续扩大。政府权力显著增强。',
      ['https://www.theworldeconomy.org/publications/worldeconomy/Maddisontable3-9.pdf',
       'http://assets.cambridge.org/052166/2915/sample/0521662915wsn01.pdf',
       'https://www.imf.org/external/pubs/ft/fandd/1996/09/pdf/tanzi.pdf',
       'https://ourworldindata.org/government-spending']),
 15: ('P',
      '军备与石油利益确实深刻影响部分国家的政策（武器—石油美元循环等研究）。但把政府形态归结为“符合控制军备与原料者所希望的那种”，忽略了选举政治、劳工运动与福利国家等其他决定因素，只部分符合。',
      ['https://doi.org/10.1080/09692299508434329']),
 16: ('P',
      '西方国家的民主形式在1924年后总体存续，并在二战后巩固。权势集团与媒体影响被广泛讨论（NED等），公众也并非因此普遍变成恭顺的“服从式民主”，抗议、政党轮替与新闻抗争仍在发生。',
      ['https://ourworldindata.org/the-rise-of-electoral-democracy',
       'https://www.ned.org/wp-content/uploads/2020/02/Firming-Up-Democracys-Soft-Underbelly-Authoritarian-Influence-and-Media-Vulnerability-Lucas.pdf']),
 17: ('P',
      '金融危机后“企业国籍不再重要”的信心下降，经济民族主义与国家冠军企业仍然存在（International Business史综述）。但公司也大规模全球化、部分脱离单一民族国家（Yale '
      'Insights）。民族绑定与跨国化并存。',
      ['https://www.tandfonline.com/doi/full/10.1080/00076791.2022.2118718',
       'https://insights.som.yale.edu/insights/how-did-the-corporation-become-global']),
 18: ('C',
      '按世界银行/Our World in Data，2022年各国进出口之和相当于全球GDP的63%，远高于20世纪前期的一体化水平。两次大战与大萧条曾打断全球化，但1924–2026年窗口的净方向是世界经济更趋一体。',
      ['https://ourworldindata.org/data-insights/in-2022-the-sum-of-imports-and-exports-across-countries-amounted-to-63-of-global-gdp',
       'https://www.chicagofed.org/publications/chicago-fed-letter/2001/april-164']),
 19: ('C',
      '集装箱运输使全球分散生产链成为可能（集装箱化与全球化综述），并在各国迅速扩散（美联储研究）。加上通信与互联网，把世界组织成一个生产与消费单位的技术条件已经具备。',
      ['https://doi.org/10.1002/9781119372080.ch9',
       'https://www.federalreserve.gov/econresdata/feds/2014/files/201488pap.pdf']),
 20: ('W',
      '冷战中美苏两个集团争夺主宰，条件已经出现（斯坦福哲学百科）。但胜利者并未建立防止文明相互灭绝的单一世界性组织；联合国也不是世界政府（Weiss）。条件触发后，所预言的后果没有发生。',
      ['https://plato.stanford.edu/entries/world-government/',
       'https://cooperative-individualism.org/weiss-thomas_what-happened-to-the-idea-of-world-government-2009-jun.pdf']),
 21: ('U',
      '“世界政府”作为对全人类拥有管辖权的单一政治权威至2026年11月仍未建立（斯坦福哲学百科；LegalClarity）。作者未给出实现时限，无法判定“只能靠武力建立且起初专制”这一路径是否会兑现。',
      ['https://plato.stanford.edu/entries/world-government/',
       'https://legalclarity.org/what-is-one-world-government-history-models-and-debate/',
       'https://en.wikipedia.org/wiki/World_government']),
 22: ('U',
      '世界政府尚未实现，条件未触发，对“一旦实现将逐渐产生可忍受生活的其他条件”既不能判对也不能判错。',
      ['https://legalclarity.org/what-is-one-world-government-history-models-and-debate/',
       'https://en.wikipedia.org/wiki/World_government']),
 23: ('W',
      '“大多数白人国家在五十年内（至约1974年）人口趋于静止”没有发生。欧洲人口由1900年约4.08亿增至1950年约5.50亿并继续增长（RAO）；联合国1970年报告显示较发达地区1960–1970年自然增长率仍为正；1976年报道的是增速放缓而非人口静止。',
      ['https://raoglobal.org/insights/europes-populationdeclining-ageing-and-diversifying',
       'https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/files/documents/2020/Jan/un_1970_the_world_population_situation_in_1970_0.pdf',
       'https://www.nytimes.com/1976/11/21/archives/demography-the-growth-of-population-is-slowing-down.html',
       'https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-55.pdf']),
 24: ('C',
      '节育和低生育率并未停在静止状态，许多欧洲和东亚国家已出现人口下降或自然减少（OECD关于人口停滞与下降；Our World in '
      'Data：已过人口峰值的国家几乎都在欧洲和东亚）。作者所提示的“可能减至人口减少”已经实现。',
      ['https://www.oecd.org/en/publications/shrinking-smartly-and-sustainably_f91693e3-en/full-report/demographic-trends-in-oecd-countries-towards-a-definition-of-depopulating-places_4f092035.html',
       'https://ourworldindata.org/which-countries-have-already-passed-peak-population-and-when-will-the-rest-do-so',
       'https://www.pewresearch.org/short-reads/2024/07/08/in-some-countries-immigration-accounted-for-all-population-growth-between-2000-and-2020/']),
 25: ('P',
      '20世纪中叶起现代避孕在西方国家迅速普及（Journal of Biosocial '
      'Science综述），当时发展中地区生育率仍明显更高、同时死亡率因现代医学下降。此后发展中地区也经历生育转变，“未开化种族仍将旺盛生育”并未长期保持；所谓“不降低素质”无法作为可核验的科学命题。',
      ['https://www.cambridge.org/core/journals/journal-of-biosocial-science/article/abs/dynamics-of-contraceptive-use-an-overview/DAEFF67D3418950C955248F544B5B5F1',
       'https://pmc.ncbi.nlm.nih.gov/articles/PMC1116808/']),
 26: ('P',
      '法国外籍兵团和部分殖民/外籍募兵确实存在（非公民士兵研究）。但18–19世纪以来的主导规范是转向公民军队、停止大规模雇用外国雇佣军（OUP专章）。“雇用高生育种族为雇佣军”并未成为普遍倾向。',
      ['http://eriklg.com/wp-content/uploads/2018/09/Hanson_Lin-Greenberg_NonCitizenSoldiers_16June18.pdf',
       'https://academic.oup.com/book/4622/chapter/146765429']),
 27: ('W',
      '检索未发现政府为保留兵源而系统反对在非洲传授节育的证据。相反，战后多国在非洲推广计划生育：南非自1970年起在城镇等地直接提供免费计划生育服务；非洲地区虽起步较晚，但已有政府支持家庭计划的政策（PMC；NCBI）。',
      ['https://pmc.ncbi.nlm.nih.gov/articles/PMC6947935/', 'https://www.ncbi.nlm.nih.gov/books/NBK236398/']),
 28: ('P',
      '欧洲及北美占世界人口的份额由1950年约29%降至2020年约14.5%（CPS依据UN '
      'WPP），数量相对劣势的方向成立。但“在雇佣军哗变中被灭绝”并未发生，白色人种人口本身在20世纪仍先增后部分下降，主结果不成立。',
      ['https://blog.cpsindia.org/2025/07/demography-of-world-i.html',
       'https://raoglobal.org/insights/europes-populationdeclining-ageing-and-diversifying',
       'https://www.cso.ie/en/releasesandpublications/ep/p-eii/environmentalindicatorsireland2021/globalcontext/']),
 29: ('U',
      '世界政府并未建立（Full Fact澄清联合国并非世界政府；Stanford/LegalClarity）。条件未触发，无法判定其是否会降低“被统治种族”生育率并解决人口问题。',
      ['https://fullfact.org/online/fake-UN-agenda-2030-mission-goals-repeat/',
       'https://legalclarity.org/what-is-one-world-government-history-models-and-debate/']),
 30: ('C',
      '1924年出版后，强制绝育权在多国被确立或扩大：美国弗吉尼亚1924年法及1927年Buck v. Bell；瑞典等国随后长期实施强制绝育，至1976年才废止（Embryo Project；Indiana '
      'McKinney综述）。政府确实获得了对被认为不宜生育者实行绝育的权力。部分州法律早于1924年，但不否定出版后的广泛扩展。',
      ['https://embryo.asu.edu/pages/sterilization-act-1924',
       'https://mckinneylaw.iu.edu/practice/law-reviews/iiclr/pdf/vol8p475.pdf',
       'https://pmc.ncbi.nlm.nih.gov/articles/PMC4202623/']),
 31: ('C',
      '获得该权力后，早期实施对象主要是所谓“低能/智障”（feebleminded、mentally '
      'retarded）：印第安纳1907年法等及随后美国实践均以此为首要目标（PMC综述）。出版后新获权力的地方，起初用法与作者所说一致。',
      ['https://pmc.ncbi.nlm.nih.gov/articles/PMC4202623/']),
 32: ('W',
      '强制绝育的对象主要是残疾、疾病或种族分类，而非把“反对政府”普遍当作低能证据并对各类反叛者绝育。极权政权对异见者更多使用关押、流放或杀害；苏联占领区还废止了纳粹绝育法（强制绝育综览；ZZF）。政治化滥用存在，但并非作者所预言的普遍结果。',
      ['https://en.wikipedia.org/wiki/Compulsory_sterilization',
       'https://www.zzf-potsdam.de/en/research/projects/socialist-eugenics']),
 33: ('P',
      '癫痫、精神疾病等确实被写入多部绝育法（Kindregan综述；1936年对德国法律的当代介绍也包括相关疾病类别）。但“最终把未能通过常规学校考试的人统统包括进去”并未成为制度性标准。',
      ['https://scholarship.kentlaw.iit.edu/cgi/viewcontent.cgi?article=1994&context=cklawreview',
       'http://chwe.net/michael/kopp_1936.pdf']),
 34: ('W',
      '没有证据表明优生绝育提高了平均智力。智商的长期上升（弗林效应）主要被归于环境与社会因素，而非淘汰“不宜生育者”的遗传效果。',
      ['https://doi.org/10.1017/cbo9780511605253.006']),
 35: ('P',
      '精子捐献使一名男子在事实上成为数百名不同母亲所生子女的父亲已成为可能（荷兰捐精者据报超过550名子女；The Conversation）。但这并未成为被广泛接受的道德标准，相反许多国家正限制捐精子女人数。',
      ['https://theconversation.com/why-we-need-to-set-limits-on-sperm-donation-211854',
       'https://plato.stanford.edu/entries/gametes-donation-sale/']),
 36: ('U',
      '国家官员仍无法在可操作意义上“决定人口类型”（基因组研究仍受人群结构与样本限制，NHGRI）。条件未满足，无法判定是否会培育出恭顺而缺乏主动性的人口。',
      ['https://www.genome.gov/about-genomics/policy-issues/population-descriptors-in-genomics']),
 37: ('C',
      '公共关系与政治心理学被系统用于塑造公众对政府与制度的态度：伯奈斯把宣传定义为持续影响公众关系的努力，并成为民主国家中的专业实践（MIT Press '
      'Reader）。这一技术确实被用来让民主政体更相信现有权力“明智而善良”。',
      ['https://thereader.mitpress.mit.edu/masters-of-crowds-the-rise-of-mass-social-engineering/']),
 38: ('P',
      '智力测验确被广泛采用。Wellcome指出测验偏重正式应试能力，可能低估建筑师、音乐家、舞者等才能，与作者担心的方向一致。但没有证据表明“许多极具艺术才能的人被归为低能（moron）”这一强烈结果普遍发生。',
      ['https://wellcomecollection.org/stories/exceptional-talent-and-the-trouble-with-iq-tests']),
 39: ('T',
      '激素、抗雄激素和精神药物已能在临床上调节攻击性、情绪和性欲（PMC；法医神经科学手册）。这是朝“按需调节性情”的持续进展，但远未达到可随意、精确地使人“易怒或胆怯、性欲强弱随心所欲”的终点。',
      ['https://pmc.ncbi.nlm.nih.gov/articles/PMC7465123/',
       'https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118650868.ch27']),
 40: ('U', '检索未发现任何国家以注射或其他生理手段，按阶级系统赋予权势者子女“指挥性情”、无产者子女“服从性情”的计划。情绪的生理控制也尚未达到可如此施用的程度，条件未满足。', []),
 41: ('C',
      '精神药理学、电休克和深部脑刺激等躯体治疗已被用于控制情绪障碍（PMC综述）。生理学已经找到了控制情绪的方法，尽管并非对所有情绪的完全、任意控制。',
      ['https://pmc.ncbi.nlm.nih.gov/articles/PMC3238088/']),
 42: ('W',
      '即便已有药物等控制情绪的途径，初等教育的主要事务仍是教学、课堂管理与训导，而非以注射或饮食造就性情（Education '
      'Week等）。人口也并未普遍具有“统治者所希望的情绪”。检索中出现的本书或罗素1951年著作摘录只是预测本身的复述，不作为结果证据。',
      ['https://www.edweek.org/teaching-learning/opinion-the-classroom-management-field-cant-stop-chasing-the-wrong-goal/2021/09']),
 43: ('U', '“管理者是否不比1924年更少愚蠢、更少偏见”缺少可公开核验的决定性指标，现有关于功绩制或移民政策的文献不能承担这一判断，暂无法判断。', []),
 44: ('C',
      '原文是科学“威胁要造成我们文明的毁灭”，而非断言文明已被毁灭。核武器及其全球后果（核冬天模型，Science '
      '1983）以及罗特布拉特等对科学威胁人类存续的论述表明，这一文明级毁灭威胁已经真实出现。文明尚未毁灭，并不否定威胁本身成立。',
      ['https://www.nobelprize.org/prizes/peace/1995/rotblat/article/',
       'https://doi.org/10.1126/science.222.4630.1283',
       'https://aeon.co/essays/none-of-our-technologies-has-managed-to-destroy-humanity-yet'])}
