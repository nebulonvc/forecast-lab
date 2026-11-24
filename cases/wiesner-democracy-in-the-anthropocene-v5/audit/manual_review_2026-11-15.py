# Manual assistant review; Asia/Shanghai 2026-11-16
META={'basis': '实际使用Exa搜索与内容抓取，另WebFetch核实书目；搜索已于续跑前完成，续跑复用现有日志/缓存，不重复全文阅读或查询。公开证据逐条阅读，日期、对象、条件和反证复核后写完整ASSESS与SEMANTIC REVIEW，再经pipeline '
          'apply/check/report。早于首发的来源只作基线，来源中的预测不作实绩。',
 'extra': '\n'
          '## 核验边界与审计说明\n'
          '\n'
          '- 17条候选全部保留在data/claims.jsonl；13条resolvable复核后剔除1条出版前已发生事件，最终12条预测。\n'
          '- 原始抽取#6万亿富翁在写稿时或尚不确定，但公开证据显示2026年6月已经发生，早于9月首发，因此不追授“预测正确”。\n'
          '- 最初仅有2026年份，核查出版社后明确首发日2026-09-30；所有评分按真实出版后窗口重审。\n'
          '- Bloomberg实时页抓到2026-11-16，晚于截止，已从case与评分证据排除。Exeter页面正文日期与搜索索引不同，以页面9月16日为准，仅作基线。\n'
          '- 未定均逐条写明决定性缺口；不把机构未来展望、改革提案、术语普及或旧指数当成预测兑现。\n'
          '- 第3条只核对短窗中民主未整体终结，不代表民主质量上升或现代性永久存续。\n'
          '- 未调用DeepSeek；未commit/push/开PR；case不带全书、请求计划或context正文。\n',
 'method': '使用toolkit 85e6da1原始v5后处理，3500/600分块337块，所有块已完整阅读，包括参考文献、致谢、会议报告和索引；代码未划出matter_spans。逐块手写20条抽取项，仓库排除historical 1/normative 2，保留17候选（13 '
           'resolvable、4 '
           'unclear）。理论/规范性编著预测密度低，未为凑密度把建议、机制或会议转述强作预测。第一轮每条support/counter各一次；第二轮仅#2/#3/#5/#9/#12，每条两次，共36次Exa查询。未启用第三轮：余下未定主要缺少未来结果/明确指标，不是增加检索能补足。',
 'overall': '本书是民主理论、人类世与治理的多作者学术讨论集，不是预测报告。短窗口内只有“民主不会近期整体终结”能够按存续观察判正确；其余11条缺少终点事实、配对测量或完整结果链，均暂无法判断，未给宽松的趋势分。马斯克万亿身家事件发生在正式出版之前，从预测分母中剔除。单一可判条目的100%胜率没有外推意义。',
 'pub': '**2026-09-30**（Springer/Palgrave电子书首发；精装2026-10-01）。出版社书目页存档用于校准日期。观察窗口仅46天，截止2026-11-15。PDF原件sha256为6f33e2ef9af88cc3e89ccec1eddbe9b9bab9bd53358944708393649691210c88，与队列一致；pdftotext '
        '-enc UTF-8 转换TXT的sha256为83862410727693096d4efbf62b23e23699bc3c1642243eefc8de1003eb330756。',
 'title': '克劳迪娅·维斯纳、汤姆·朔伊内曼编《人类世中的民主》（Democracy in the Anthropocene）'}
NF={6: ('historical', '出版社书目页确认2026-09-30首发；福布斯确认2026-06-12即已发生万亿富翁事件，属于出版前已兑现的写作期判断，保留候选但不计预测。')}
V={1: ('U',
     'PIK 的生态边界越界主要是出版前基线；出版后的 UNEP 报告确认气候风险并保留减排后回到目标的路径。它们未给出 9 月30日后人类生存资源净缩减或“人类生命本身受危及”的独立终局观测，不能把风险预测当成兑现。',
     ['https://www.pik-potsdam.de/en/news/latest-news/planetary-health-check-2026-finds-mounting-pressures-across-earth2019s-life-support-systems',
      'https://www.unep.org/en/news-and-stories/story/temperatures-spike-new-report-outlines-humanitys-options-containing-climate',
      'https://news.exeter.ac.uk/exeter-in-the-conversation/earthshot-and-the-science-of-positive-tipping-points-how-environmental-progress-can-become-unstoppable/']),
 2: ('U',
     'Frontiers 的研究强调去政治化既可能抑制异议也可能恢复集体行动；RETOOL 对专家咨询机构的观察反而发现问责与效能贡献。两者均早于出版，不能证明此后技术官僚治理已进一步削弱民主，亦不足反证作者对未来的概括。',
     ['https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1726794/full',
      'https://www.retoolproject.eu/sites/default/files/2026-08/Deliverable%204.2%20final.pdf']),
 3: ('C',
     '出版后的 AP 报道仍记载美国选民投票并且法院阻止总统干预；11月8日《卫报》也报道多国选举对威权领导人的反制。故在截至11月15日的短观察窗内，民主并未整体终结；几内亚比绍推迟选举说明严重挑战仍在，而非全球民主已经消失。',
     ['https://apnews.com/article/midterms-election-day-voting-polls-trump-ba3037eed7bd816cc084bb1c4a2e6ccf',
      'https://www.dw.com/en/will-guinea-bissau-remain-trapped-in-political-chaos/a-79734069']),
 4: ('U',
     'V-Dem 的民主倒退资料观察的是2025年，属于出版前基线。出版后的 Reuters/AP 摘录同时表明特朗普施压选举官员及法院加以限制，尚无法证实“越不受阻→依次损害话语、制度、公共物品和文化”的完整条件后果链。',
     ['https://www.v-dem.net/news/press-release-democratic-backsliding-reaches-western-democracies-with-us-decline-unprecedented/',
      'https://www.reuters.com/3fec1b0a85a0/legal/government/with-us-midterms-underway-courts-rebuff-trumps-pressure-state-election-officials-2026-11-03/']),
 5: ('U',
     '哈萨克斯坦政府10月材料确认 Network School 迁入阿斯塔纳并扩展教育和技术合作，但这仍是受东道国管辖的校园/公司。10月综述明确称尚无网络国家获外交承认；项目扩展与此前马来西亚撤照并存，不足证实书中有主权领土和外交承认的“网络国家”已成为现实。',
     ['https://www.gov.kz/org/maidd/press/news/details/1309072?lang=en',
      'https://www.abc.net.au/news/2026-07-29/why-malaysia-shut-down-network-school-digital-nomad-hub/106953874',
      'https://www.nomadlayer.com/articles/network-states-explained']),
 7: ('U',
     'WFP 10月7日访谈警告厄尔尼诺与投入成本将带来2027年粮食安全后果，但关键数字和后果仍是预测。FAO 的改善数据反映2025年，不能作为出版后反证；原文“in the coming years”尚未走完，缺乏相同口径的实际生存斗争加剧结果。',
     ['https://www.wfp.org/stories/how-record-breaking-el-nino-could-deepen-global-hunger',
      'https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en']),
 8: ('U',
     '11月的国际安全论文讨论自由秩序危机同时保留制度自我纠错的解释，11月选举报道又显示对威权的反制。六周的危机和反制都不能证实或推翻“永不回到自由主义原状”的不可逆断言。',
     ['https://www.theguardian.com/world/2026/nov/08/election-brazil-serbia-israel-and-us-resilience-democracy-grassroots-activism-authoritarianism',
      'https://direct.mit.edu/isec/article/51/2/39/139772/The-Liberal-Balance-of-Power-and-the-Four-Horsemen']),
 9: ('U',
     '10月6日欧委会提出扩员所需的制度改革，同时报道成员国分歧和一致同意门槛；此前欧洲议会决议亦承认统一选举程序仍不完整。提出方案、预期阻力并不等于制度转移已经失败，现有材料也不能宣告其成功。',
     ['https://www.euronews.com/2026/10/06/eu-commission-throws-down-the-gauntlet-to-member-states-on-reforming-the-bloc',
      'https://eur-lex.europa.eu/eli/C/2026/3685/oj/eng']),
 10: ('U',
      '剑桥所列研究使用1990—2019年资料说明市场势力与民主退化相关，不能证明出版后“民主—资本主义—现代化”的组合将结束。10月 IMF 材料仍描述经济韧性；经济增长既不是民主长存的证据，也不能凭旧资料推出该组合很快瓦解。',
      ['https://www.imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026',
       'https://www.econ.cam.ac.uk/publications/journals/market-power-political-power-pressure-declining-competition-democracy']),
 11: ('U',
      '11月 Autocar 报道欧议会环境委员会支持降低汽车减排目标，显示汽车业诉求仍有政策影响；欧委会页面同时区分现行100%目标与修订提案。但委员会表决并非完整立法落地，更不等同恢复旧的城市交通制度，民族国家与家庭价值两个分项也未获得对应结果证据。',
      ['https://www.autocar.co.uk/car-news/new-cars/car-makers-win-reprieve-eu-eases-2035-emissions-rules',
       'https://climate.ec.europa.eu/areas-action/transport-decarbonisation/road-transport/cars-and-vans_en']),
 12: ('U',
      'ICS 存档确认原人类世提案被拒；出版后10月2日 ABC 报道仍非正式地质年代，同时研究者要求重审程序。原文说“eventually”，因此2024年否决及当前仍未通过不能证明最终必不接受，也没有新的正式批准支持趋势符合。',
      ['https://www.abc.net.au/news/science/2026-10-02/anthropocene-working-group-epoch-rejection/107215280', 'https://stratigraphy.org/news/152']),
 13: ('U',
      'OECD 的出版前观测显示2026年上半年增长放缓但仍为正，IMF 10月材料仍称经济有韧性，其全年数字则是预测。没有出版后同口径财富、资源和可分配剩余全面减少的实测，不能把增长放缓或机构展望当作“各方面都更少”已成立。',
      ['https://www.oecd.org/en/publications/2026/09/oecd-economic-outlook-interim-report-september-2026_8312492f/full-report.html',
       'https://www.imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026'])}
