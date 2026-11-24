# -*- coding: utf-8 -*-
"""Manual decisions for suleyman-coming-wave-v5, 2026-11-15 (Asia/Shanghai)."""
AU = 'manual-audit-2026-11-15'
MA = 'manual-assistant-2026-11-15'
IH = 'manual-audit-2026-11-15-implicit-horizon'

NF = {
    218: ('hedge', '“国家等大型实体的规模优势可能加强，也可能被削弱”两头都说，任何结果都不能证伪。'),
    257: ('normative', '“我们没有足够时间让机构慢慢摸索”是对紧迫性的呼吁，不是对可观察结果的预测。'),
    258: ('descriptive', '说欧盟《人工智能法案》等举动“在争取一个可能实现遏制的未来”，是对现有努力的定性描述，没有可判定的结果。'),
}

def ev(*pairs):
    return list(pairs)

_UND = lambda why: ('暂无法判断', False, why, MA, ev())

V = {
    # ---- stuck (manual-assistant) ----
    3: _UND('“尾部风险可能威胁民族国家生存、颠覆地缘格局”是可能性判断。窗口内尚未发生由人工智能或合成生物学引发、足以威胁国家生存的事件，后果未出现，也不能据此证伪，暂无法判断。'),
    69: _UND('原文期限是“未来几十年”，截止日距出版仅三年多，人工智能已成主导性技术之一，但量子计算、先进生物技术尚处早期，整体期限未到，暂无法判断。'),
    87: _UND('前提是“一旦出现超级智能”。截止日尚无公认的超级智能，前提未触发。'),
    102: _UND('“永久性提升经济增长率”需要长期数据。窗口内 IMF 等机构只给出情景预测，全要素生产率尚无可归因于人工智能的持续上升，时间不足以判断。'),
    168: _UND('没写期限的“这场变革对数亿人来说都将极为动荡”。窗口内多国失业率总体仍低，大规模就业冲击尚未出现；但作者所指是整个技术浪潮的长期后果，尚不足以判错，暂无法判断。'),
    179: ('部分符合', True,
          '原文说大型商业实体的规模、影响力和能力会进一步扩大。窗口内英伟达市值在2024年增加约2万亿美元，大型科技公司合计市值到2025年9月约21万亿美元，反垄断拆分诉求也未能实质削弱头部平台，方向一致；但“能力和影响力”不止市值，且2025年后增速放缓，判趋势符合。',
          MA, ev(('https://www.reuters.com/technology/artificial-intelligence/global-markets-marketcap-pix-2025-01-02/', "Reuters (2 Jan 2025): Nvidia's market value gets $2 trillion boost in 2024 on AI rally."),
                 ('https://www.cnbc.com/2025/09/05/tech-megacaps-worth-market-cap.html', "CNBC (5 Sep 2025): Tech's megacaps are now worth $21 trillion as market caps swell."))),
    197: _UND('条件句：如果技术优势出现在通用人工智能或量子霸权领域，新进入者和政府都难以挑战。截止日既无公认的通用人工智能，也无具实用意义的量子霸权，前提未触发。'),
    206: _UND('条件句：如果尖端技术同时集中在某一专制国家手中，就会产生前所未有的权力实体。窗口内尚无一国同时垄断上述各项技术，前提未触发。'),
    215: ('部分符合', False,
          '原文说开放会成为常态、模仿随处可见、成本持续下降、获取壁垒消失。Hugging Face 上的公开模型在2024年9月突破100万个，开放权重模型持续增长，“开放、模仿、降本”这几项成立；但前沿模型仍以闭源为主，训练前沿模型所需的算力和资金门槛反而上升，“壁垒消失”不成立，判部分符合。',
          MA, ev(('https://arstechnica.com/information-technology/2024/09/ai-hosting-platform-surpasses-1-million-models-for-the-first-time/', 'Ars Technica (26 Sep 2024): Hugging Face surpasses 1 million AI models.'),
                 ('https://epoch.ai/publications/open-models-report', 'Epoch AI (Nov 2024): open models lag closed frontier models by roughly a year.'),
                 ('https://doi.org/10.3386/w33139', 'NBER w33139 (Nov 2024): Concentrating Intelligence: Scaling and Market Structure in AI.'))),
    219: _UND('“不平等将最早出现在生物学领域”。窗口内基因编辑、增强等生物技术带来的不平等尚未形成可观察的规模，也无法比较与其他领域的先后，暂无法判断。'),
    225: _UND('“权力和服务主要由国家集中掌握的格局可能逐步瓦解”是长期可能性。窗口内 OECD 财政数据并未显示中央政府职能明显外移，也不足以否定长期判断，暂无法判断。'),
    229: _UND('V-Dem 等报告显示窗口内民主倒退持续，但难以把它归因于作者所说的技术压力和新能力中心，因果链缺少可核实证据，暂无法判断。'),
    240: _UND('条件句：如果未能遏制技术浪潮，灾难迟早降临。“迟早”没有期限，窗口内也未出现作者所指的灾难，暂无法判断。'),
    241: _UND('说潜在危机规模将远超博帕尔和切尔诺贝利，属可能性描述。窗口内没有此类全球性灾难，但不能据此证伪，暂无法判断。'),
    246: _UND('条件句：当国家集中权力受威胁、遏制越来越难时，收紧控制是必然结果。前提没有清楚触发，各国人工智能政策在窗口内松紧不一，暂无法判断。'),
    247: ('部分符合', True,
          '原文说技术浪潮为“人工智能专政”提供了动机和手段。窗口内有多份独立报告记录专制政府把人工智能、大数据和生物识别用于监控和压制（如中国的新人工智能系统、缅甸军方使用人工智能），手段在增强，方向一致；但“自我强化的人工智能专政”作为一种新的统治形态尚未成形，判趋势符合。',
          MA, ev(('https://www.aspi.org.au/report/the-partys-ai-how-chinas-new-ai-systems-are-reshaping-human-rights/', 'ASPI (1 Dec 2025): The party’s AI: How China’s new AI systems are reshaping human rights.'),
                 ('https://www.ned.org/wp-content/uploads/2025/02/NED_FORUM-China-Emerging-Technologies-Report.pdf', 'NED (Feb 2025): Data-Centric Authoritarianism.'),
                 ('https://www.ohchr.org/sites/default/files/documents/cfi-subm/sr-terrorism-ai/subm-position-paper-hr-cso-10-myanmar.pdf', 'Submission to UN Special Rapporteur (Aug 2025): Myanmar’s repressive use of AI.'))),
    250: _UND('“技术浪潮可能自相矛盾地创造出遏制自身的工具”是低确定性的可能性。窗口内有人工智能用于安全评估等零星例子，但遏制工具尚未成形，暂无法判断。'),
    # ---- audit of completed items ----
    63: ('暂无法判断', False,
         '原文说我们即将迎来“关键节点”，随后人工智能将使机器人能复制人类所有物理行为。机器以“截止日机器人远未覆盖人类全部动作”判错，但那是作者设想的终点，不是“即将”所指的节点；终点没有期限，不在窗口内判错。',
         AU, ev()),
    191: ('暂无法判断', False,
          '“几乎所有东西就近生产并由人工智能管理”是作者对未来数十年的设想，原文没给期限，不宜用三年的窗口判错；目前 3D 打印药品和食品仍是小规模应用，暂无法判断。',
          AU, ev()),
    274: ('暂无法判断', False,
          '“我们将进入一个新纪元，大多数日常互动是与人工智能交流”是长期设想。窗口内多数日常交流仍发生在人与人之间，但作者所说的新纪元没有期限，不提前判错。',
          AU, ev()),
    283: ('暂无法判断', False,
          '“许多人可能会完全沉浸在虚拟世界中”是没有期限的低确定性判断。窗口内 VR 仍属小众，但不足以否定长期判断，暂无法判断。',
          AU, ev()),
    268: ('部分符合', True,
          '原文说未来可能采取类似全民基本收入的举措。窗口内美国多地出现保障收入项目，部分已转为常设（如库克县），方向一致；但这些项目针对特定人群、规模有限，不是全民基本收入，由正确改为趋势符合。',
          AU, ev()),
}

RR = {}
