# Manual review (METHOD.md v5) of Lawrence Lessig, The Future of Ideas (2001), review_source manual-assistant-2026-11-15
META = {
    'title': 'Lawrence Lessig《思想的未来：互联世界中公地的命运》（The Future of Ideas: The Fate of the Commons in a Connected World）',
    'pub': '**2001** 年 Random House 第一版（ISBN 0-375-50578-4，368 页，CIP 2001031968；内文排版标记 9/21/01）。官方授权 CC BY-NC 3.0 US 版。工作 PDF sha256 `ef667e1c04cde095cbaa54b9443c4b4a0681842008a8e4a4e11bfea60266b97e`，1,306,926 字节，与队列完全一致。官方列出的 https://www.the-future-of-ideas.com/download/lessig_FOI.pdf 在抓取时返回 500/404，字节级相同文件取自 https://www.dimt.it/wp-content/uploads/2015/10/www.the-future-of-ideas.com_download_lessig_FOI.pdf。pdftotext -enc UTF-8 得到 TXT，sha256 `9d98eb2d6fcb55b73b69bba28eedb7440db5e4e6914d9eaffeb9b18a0985a673`，948,762 字节，UTF-8 无 BOM、仅 LF，937,344 字符，16,181 行，368 个换页符。预测窗口按 2001→2026-11-15 计。PDF/TXT 不入库。与 lessig-code-version-2 分开分析。',
    'method': '本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1dc0f185830a6ea9037d731fd39a27411e`，prepare_book.py md5 `01fc49ad64795a345ca1cb32bb2e4366`）把全文切成 272 块（3500 字符、600 字符上下文），助手逐块通读（含前言、Notes、Index、作者简介；混合块按人工边界只抽正文），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 21 条候选，其中 16 条可核验预测、5 条 reported 被降为 unclear。英文 changes 均为 quote 的逐字单行子串；horizon/time_text 仅在引文中原文出现且不跨 pdftotext 换行时填写。跨行无法构成合规 changes 的缺口另见 audit/AUDIT_linebreak_gaps.md，未伪造子串、未改 toolkit。核验：每条可核验候选先定 scope，用 Exa 各做 support/counter 检索（密钥仅按文件路径读取 `~/.config/forecast-lab/exa-new-2.key`，未打印、未入库），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`（34 条），再经 `pipeline.py apply assess → check`。按本书流程，先清空 claims/proposals/before-assessment 中的 context，再由 canonical `/workspace/forecast-line-b/tools/manual_report.py`（md5 `682248fa9f6c63e3492a559ccac12761`）生成报告，未手改。',
    'overall': '这是莱斯格 2001 年关于互联网创新公地命运的论著。全书 272 块通读后，导入 21 条候选：16 条作者可核验预测进入评分；5 条第三方转述（Gilder 光速网络、IBM 2004 年 Linux 服务器市值、Platt 宽带将摧毁平等主义互联网、Noam 拍卖趋向寡头、Brown 教育数字平台将被法律关掉）按 v5 归属规则保持 reported 并降为 unclear，不改归属以求计分。16 条预测中，正确 3（推荐系统将更能预测个人所需、未来互联网生活将按属地再规制、当时频谱出售预期收入将超过 500 亿美元）、趋势符合 3（实体书在下一世纪仍是文化核心、电影人不久能以约百分之一成本制作数字高质量影片、偏好数据广告将以更低成本产生远高于 0.5% 的回报）、部分符合 8（控制回潮与障碍再引入、有线围墙花园、知识产权边际上保护旧势力、频谱财产化使分享更难、DRM 削弱混剪能力、AOL/微软将定义其后五年、内容与接入将被再控制等：方向或局部兑现，但未达到原断言的整体程度）、错误 0、暂无法判断 2（部族无线网以“律师解决争端之时”为条件、Macintosh 操作系统进入公有领域后将无机器可运行：两条真实条件至截止日均未触发）。可判定 14。严格胜率 21.4%，加权胜率 66.1%，错误率 0.0%。对趋势符合从严：仅方向持续且程度、时点或精确比率未完全到位时才记趋势符合，不把已完整兑现的条目降为趋势符合，也不把部分成立升为趋势符合。',
    'basis': '本稿由助手逐条对照书中原文与存档证据人工复核：',
    'extra': """

## 说明

- 抽取密度：16 条可核验 / 272 总块 ≈ 0.059。低于 METHOD §5 英文书参考区间（约 0.2–0.35）。本书大量为已发生的规制史、规范建议（“应当开放频谱/缩短保护期”）以及对 013/014 控制回潮论题的复述；未为凑密度放宽 DISCOVER_PROMPT_V5，未把规范 should、含糊 could/may、对冲的正反预测、出版前史实或跨行无法构成合规 changes 的句子收为预测。
- 前后附文人工排除记录：仓库中文 `MATTER_HEADING` 正则无法匹配本书英文封面、前言、Notes、Index 与 About the Author 标题，故 toolkit 的 `skipped_matter_chunks=[]`、`excluded_matter_spans=[]`，须人工排除并记录。

| 区段 | 字符偏移 | 内容 | 块 | 抽取 |
| --- | --- | --- | --- | --- |
| 封面/法律/题献 COVER/LEGAL/DEDICATION | 0–1953 | 封面、授权、题献等 | txt-00001 起 | 不抽 |
| 前言 PREFACE | 1953–9404 | 前言（METHOD：前言不作预测） | mid txt-00001 至 mid txt-00003 | 不抽 |
| 目录与半标题 TOC | 9404–11630 | 目录与半标题页 | mid txt-00003 至 mid txt-00004 | 不抽 |
| 正文 BODY | 11630–660350 | 第 1 章起至 Notes 之前 | mid txt-00004 至 mid txt-00192 | 按 DISCOVER_PROMPT_V5 抽 |
| 注释 NOTES | 660350–893639 | 章末注释（txt-00192 中段起） | mid txt-00192 至 mid txt-00260 | 逐块通读，不抽 |
| 索引 INDEX | 893639–936589 | Index（“I n d e x”约 893761） | mid txt-00260 至 mid txt-00272 | 逐块通读，不抽 |
| 作者简介 ABOUT THE AUTHOR | 936589–937344 | About the Author | mid/end txt-00272 | 不抽 |

- 混合块：txt-00192 仅抽取 Notes 起始（660350）之前的正文；txt-00260、txt-00272 为注释/索引与索引/作者简介混合，不抽取附文。
""",
}
NF = {}

V = {
1: ("P",
    "控制一侧有较多兑现：DMCA 反规避、DRM 与平台门禁确实加强了对网络使用的约束；但 2001 年后 Web 2.0、开源、维基与智能手机等持续爆发，不能认定创新在互联网与社会中被整体削弱。合取命题只部分成立。",
    ["https://www.eff.org/issues/dmca",
     "https://www.computerhistory.org/revolution/the-web/20/403"]),
2: ("P",
    "应用商店、DRM 与围墙花园等确实重新引入了部分被早期互联网消解的门槛；但 YouTube、独立发布与开源工具同时大幅降低了创作与分发门槛。障碍被部分而不是原样整体“重新引入”。",
    ["https://techcrunch.com/2008/07/24/apples-app-store-the-new-walled-garden/",
     "https://www.nytimes.com/2006/12/10/arts/music/10pare.html"]),
3: ("U",
    "预测以“律师解决主权/频谱之争之时”为时间条件。部族频谱主权与接入差距在 2020 年代仍在立法与政策过程中，Hendricks 方案所涉那场法律战并未形成可据以检验速度对比的明确完结，条件未触发。",
    ["https://www.wired.com/2002/01/hendricks/",
     "https://www.minneapolisfed.org/-/media/assets/papers/cicdwp/2021/cicd-wp-2021-03.pdf"]),
4: ("T",
    "“下一世纪至少”尚未走完，不能判完全正确；但至截止日印刷书仍占销售与阅读的主体（约三四倍于电子书，调查显示更多人仍读纸书），与“实体书仍是文化核心”的方向高度一致。",
    ["https://www.pewresearch.org/short-reads/2026/04/09/americans-still-opt-for-print-books-over-digital-or-audio-versions-few-are-in-book-clubs/",
     "https://wordsrated.com/print-book-vs-e-book-sales-statistics/"]),
5: ("T",
    "“不久后能以传统工具约 1% 的成本为数字设备制作高质量影片”在能力意义上方向正确（数字摄影、低成本独立制作、以至 iPhone 剧情长片如 Tangerine）；精确的 1% 比率缺乏系统对照，故作趋势符合而非完全正确。",
    ["https://www.indiewire.com/features/craft/how-to-be-unstoppable-sean-baker-and-the-digital-filmmaking-revolution-247890/",
     "https://www.wipo.int/edocs/mdocs/mdocs/en/wipo_ip_econ_ge_2_15/wipo_ip_econ_ge_2_15_ref_waldfogel.pdf"]),
6: ("C",
    "“除非被阻止”的条件未实现为普遍叫停：推荐系统在亚马逊、Netflix、YouTube、TikTok 等成为核心，并持续提高对个人偏好的预测与投放，与原断言一致。",
    ["https://research.netflix.com/research-area/recommendations",
     "https://dl.acm.org/doi/10.1145/3673426"]),
7: ("T",
    "基于偏好数据的定向与程序化广告成长为远大于传统 0.5% 反馈率渠道的产业，单位成本与定向效率总体更高；但广告欺诈与展示无效使“高得多的回报”并非一律成立，故趋势符合。",
    ["https://www.invespcro.com/blog/the-average-direct-mail-conversion-rate-and-the-best-tips-to-improve-it/",
     "https://www.bcg.com/publications/2018/guaranteed-opportunity-programmatic-advertising"]),
8: ("P",
    "条件部分成立：Cisco 类策略路由/管控产品确被部署，有线商如 Comcast 也曾干扰 P2P。但网络中立规则、OTT 视频崛起限制了“由网络决定用途与内容”的全面围墙花园，控制被部分而非完整兑现。",
    ["https://docs.fcc.gov/public/attachments/FCC-08-183A1.pdf",
     "https://www.eff.org/deeplinks/2008/08/fcc-rules-against-comcast-bit-torrent-blocking",
     "https://www.brookings.edu/articles/the-open-internet-rule-expands-online-streaming-video-options/"]),
9: ("C",
    "地理屏蔽、数据本地化、GDPR 及各国内容规制等表明，未来互联网上的生活确实在相当程度上按属地再规制，与 Goldsmith/Sykes 所描述、Lessig 所断言的方向一致。",
    ["https://hls.harvard.edu/today/controls-internet/",
     "https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/12/data-localisation-trends-and-challenges_d775fe8a/7fbaed62-en.pdf"]),
10: ("P",
    "Eldred 维持版权延期、DMCA 与专利主张实体等确实在边际上护卫了在位者；同时 eBay v. MercExchange、合理使用与部分专利改革又给新进入者留下空间。旧对新的保护是部分而非单向的。",
    ["https://copyright.gov/pr/eldred.html",
     "https://www.theguardian.com/film/2003/jan/16/news1",
     "https://www.eff.org/deeplinks/2016/01/fair-use-economics-how-fair-use-makes-innovation-possible-and-profitable"]),
11: ("P",
    "许可频谱仍大量按排他权利拍卖，分享技术面对在位权利的摩擦真实存在；但 TV 白空间、CBRS、Wi-Fi 6E 等分享制度也在 2001 年后建成。财产化使分享更难，却并未杜绝分享。",
    ["https://www.dynamicspectrumalliance.org/solving-the-spectrum-crunch.pdf",
     "https://dl.acm.org/doi/10.1109/MCOM.001.2400325"]),
12: ("C",
    "美国频谱拍卖收入在 1994–2009 年已达约 526 亿美元，其后继续累积（含 700MHz、AWS-3 等大拍），远超书中“这些出售的预期收入将超过 500 亿美元”的阈值。",
    ["https://www.accc.gov.au/system/files/Hazlett%2C%20Thomas%20%28Auctions%20Paper%29.pdf",
     "https://www.fcc.gov/auctions-summary"]),
13: ("P",
    "CSS/DRM、DMCA 反规避与 Content ID 确实削弱了合法抽取与混剪影片的能力；但 YouTube 混剪文化、合理使用实践与后来的规避例外又表明“完全剥夺这一能力”并未发生。",
    ["https://www.eff.org/pages/unintended-consequences-fifteen-years-under-dmca",
     "https://www.everythingisaremix.info/everything-is-a-remix-fair-use"]),
14: ("U",
    "条件是“当苹果 Macintosh 操作系统进入公有领域之时”。公司作品保护期一般为发表后 95 年，经典 Mac OS（1984 年起）至截止日 2026-11-15 仍未进入公有领域，条件未触发，不评价其后件。",
    ["https://www.copyright.gov/circs/circ15a.pdf"]),
15: ("P",
    "2001–2006 年间微软在操作系统与浏览器上仍有支配力，互联网也确实与前十年不同；但 AOL–Time Warner 迅速失势，Google 等成为更关键的定义者，创新并不只按这两家平台许可展开。",
    ["https://knowledge.wharton.upenn.edu/article/aol-in-search-of-a-new-strategy/",
     "http://news.bbc.co.uk/1/hi/technology/8403308.stm",
     "https://www.abc.net.au/news/2005-06-07/google-becomes-wall-streets-top-media-dog/1587672"]),
16: ("P",
    "应用商店与平台化确实使内容与接入更多地受控；但开放网络、开源与反复拉锯的网络中立说明创新公地并未被完整切割出售、也未简单重构成旧 AT&T 网。",
    ["https://en.wikipedia.org/wiki/Net_neutrality_in_the_United_States",
     "https://www.theverge.com/report/851629/net-neutrality-fcc-retrospective-2025"]),
}
NF = {}
