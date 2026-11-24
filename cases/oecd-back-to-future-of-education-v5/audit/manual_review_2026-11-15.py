# Manual review of 回到教育的未来 (OECD, Back to the Future of Education, 2020), review_source manual-assistant-2026-11-15
META=dict(title='OECD《回到教育的未来：四种学校教育情景》（Back to the Future of Education: Four OECD Scenarios for Schooling）',
 pub='OECD Publishing, Paris，系列 Educational Research and Innovation，请引用为 OECD (2020)，DOI https://doi.org/10.1787/178ef527-en。ISBN 978-92-64-96753-3（pdf）。PDF 元数据 CreationDate 为 2020-09-07。**按 2020-09 起算**。主要作者为 CERI 的 Marc Fuster、Tracey Burns，Joshua Polchar 撰写第 2 章。观察窗口为 2020-09 至 2026-11-15。书中四种学校教育情景的时间范围约为 20 年，至 **2040 年**；正文多次写明情景是虚构的替代未来，“从不包含预测或建议”，因此情景叙事本身未作为预测抽取。',
 method='按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext -enc UTF-8` 生成全书 TXT（sha256 `7353280e…`，216,389 字符），`prepare_book.split_text(3500, 600)` 得到 63 个 chunk，逐块通读。前言、致谢、目录和各章参考文献未抽预测。四种情景正文按作者声明视为虚构替代未来，不作为“将会发生”的预测；只抽取趋势判断、现时信号和对出版后结果的方向性/条件性断言。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 35 条可解析预测（全部 `claim_type=forecast`）。引文均为 TXT 逐字片段，记录字符偏移与 TXT/PDF sha256。全文未入库。',
 basis='本稿由助手逐条对照书中原文，并依据 2020-09 至 2026-11-15 窗口内可公开访问的来源人工复核：',
 overall=('这本书首先是一份情景工具，不是一份“未来将会如何”的预言集。作者自己写明：情景是虚构的替代未来，不考虑将会发生或应当发生什么。因此，可核验的判断主要来自第 3 章对趋势的外推、第 4 章各情景后的“现时信号”，以及第 5 章里少数明确的方向性句子。'
 '在约六年的观察窗口里，这类判断整体方向偏对。说中的包括：大规模学校体系并未因疫情而解体；经合组织 25–34 岁高等教育完成率从书中引用的 2018 年约 44% 升至 2024 年的 48%；学前和中学后参与继续扩大；气候灾害、数字化和政治动荡确实让未来更不轻松；生成式人工智能开始冲击工作任务和学习形态；线上线下界限更模糊；终身学习目标在多数国家仍然遥远。'
 '偏离或只对了一部分的，多半是把几种技术捆在一起、或把“可能”写成了接近普遍的结果：VR/AR/机器人/区块链对学校“现状”的改造远不及人工智能；“替代性工作形式和缩短工时”里，混合办公站住了，普遍缩短工时没有出现；学历作为能力信号确有松动，但学位仍是多数专业岗位的主通道；英语在互联网上的相对份额还略有下降。学习科学“最终兑现改革意图”仍无法判断。'),
 extra='\n## 说明\n\n- 四种情景（学校教育延伸、教育外包、学校作为学习中心、随时学习）按本书自己的定义视为虚构故事，没有当作作者对 2040 年的单一预测来打分。\n- 第 6 条世界人口受教育程度推演的终点是 2100 年，只根据 2020 年后受教育程度继续上升记为趋势符合。\n- 无日期的方向性判断按 2020-09 至 2026-11-15 窗口核验：方向已经发生则记正确，不降为趋势符合。\n')
NF={}
EAG="https://www.oecd.org/en/publications/education-at-a-glance-2025_1c0d9c79-en.html"
EAG_ECE="https://www.oecd.org/en/publications/education-at-a-glance-2025_1c0d9c79-en/full-report/how-does-the-provision-of-and-participation-in-early-childhood-education-and-care-vary-across-countries_86b8275d.html"
EAG_TEACH="https://www.oecd.org/en/publications/education-at-a-glance-2025_1c0d9c79-en/full-report/how-severe-are-teacher-shortages-across-countries_781f4a97.html"
EPO="https://www.oecd.org/en/publications/education-policy-outlook-2024_dd5140e4-en/full-report/component-5.html"
SKILLS="https://www.oecd.org/en/publications/empowering-the-workforce-in-the-context-of-a-skills-first-approach_345b6528-en/full-report/skills-first-in-oecd-countries-concepts-trends-and-implications-for-the-labour-market_0d6ba66f.html"
SKILLS2="https://www.oecd.org/en/publications/bridging-talent-shortages-in-tech_f35da44f-en/full-report/component-4.html"
ILO="https://www.ilo.org/publications/generative-ai-and-jobs-2025-update"
OECD_AI="https://www.oecd.org/en/publications/job-creation-and-local-economic-development-2024_83325127-en/full-report/component-7.html"
ADULT="https://www.oecd.org/en/publications/trends-in-adult-learning_ec0624a6-en.html"
EAG_ADULT="https://www.oecd.org/en/publications/education-at-a-glance-2024_c00cad36-en/full-report/to-what-extent-do-adults-participate-in-education-and-training_c2f90a06.html"
PEW="https://www.pewresearch.org/short-reads/2025/02/20/a-look-at-homeschooling-in-the-us/"
W3="https://w3techs.com/technologies/history_overview/content_language/ms/y"
REMOTE="https://www.oecd.org/en/publications/oecd-regions-and-cities-at-a-glance-2024_f42db3bf-en/full-report/the-new-geography-of-remote-jobs_6fe0d665.html"
PNAS="https://doi.org/10.1073/pnas.2509892122"
V={
1:('C','终身学习已成为教育政策的常规议题：微观证书、技能战略和成人学习项目把重组学习环境的讨论扩展到基础教育之外，尽管落实仍不均衡',[ADULT,EAG]),
2:('C','窗口内三方面都出现了：多地极端气候与高温纪录、生成式人工智能带来的数字化跃迁，以及乌克兰战争、中东冲突和主要民主国家的政治动荡',[ 'w:Climate change','w:Generative artificial intelligence','w:Russian invasion of Ukraine']),
3:('C','新冠疫情迫使学校在数周内改远程，2022 年底后生成式人工智能又迅速进入课堂与职场，都快于常规教育立法和课程修订周期',['w:COVID-19 pandemic','w:ChatGPT']),
4:('C','OECD《教育概览 2025》显示，25–34 岁高等教育完成率 2024 年为 48%，为有记录以来最高，高于书中引用的 2008–2018 年从 35% 升至 44% 的轨迹；增速自 2021 年起放缓，但方向仍是扩张',[EAG]),
5:('C','学前与高等教育等非强制阶段参与继续上升：3 岁以下入学率在过去十年提高 9 个百分点至 2023 年的 29%，3–5 岁达 85%；青年高等教育完成率亦升至 48%',[EAG_ECE,EAG]),
6:('T','投影终点为 2100 年，尚未到达。2020 年后全球及经合组织人口的受教育程度继续提高，青年高等教育完成率和较低学历人口下降的方向与 SSP2“受教育的未来”一致',[EAG]),
7:('P','生成式人工智能已对大量认知任务产生实质影响：ILO 2025 年估计全球约四分之一劳动者所处职业有一定暴露，高收入国家约 34%；OECD 称当前约四分之一劳动者暴露，若与软件深度整合，部分地区可能超过 70%。影响是强的，但“现行大多数工作中的任务”这一全称尚未被全球数据坐实',[ILO,OECD_AI]),
8:('C','大规模在线课程、编程训练营、企业学院、微观证书和各类数字学习项目在 2020 年后继续扩张，传统学校和学院之外的学习供给明显增多',[SKILLS,ADULT]),
9:('C','到 2026 年，学习分析、自适应平台和生成式人工智能辅导（如 Khanmigo 等）已在许多系统中实际支持学生与教师；使用深度仍不均衡，但“可能很快会支持”这一近预期已经发生',['w:Educational technology','w:Learning analytics']),
10:('P','教师队伍确在老化：OECD 中学教师 50 岁及以上比例 2013–2023 年从 36% 升至 38%，部分国家升幅超过 8 个百分点，同时普遍面临教师短缺、需要招募新教师。张力存在，但公共讨论的主轴是短缺与退休潮，而不总是“保障资深教师工作权对优待年轻人”这一对子',[EAG_TEACH,EPO]),
11:('C','早期学习、校外项目和中学后教育的可及性在窗口内继续提高，与第 4、5 条所依据的同一组《教育概览》趋势一致',[EAG,EAG_ECE]),
12:('U','“最终兑现教育改革意图”没有给出可核验的近终点。学习科学成果有所扩散，但还不能判断改革意图是否已被兑现，也看不出清晰、持续的实现轨迹',[]),
13:('C','学校被要求承担的职责继续变多，包括心理健康、数字与人工智能素养、气候教育和全纳，公众与问责压力上升',['w:21st century skills',EPO]),
14:('C','新冠疫情造成的大规模停课是暂时的，到 2022 年后“叫学校的那个地方”仍是经合组织国家教育青少年的主导模式，大规模学校体系没有解体',['w:Impact of the COVID-19 pandemic on education']),
15:('P','学位仍是多数专业岗位的重要信号，OECD 也写明雇主并未抛弃学历；但技能优先招聘明显推进：美国 LinkedIn 2022 年四分之一职位不再要求学位（2020 年为 15%），IBM 称其美国职位一半以上已不再要求大学学历。依赖在继续，同时也在松动',[SKILLS,SKILLS2]),
16:('T','微观证书、可叠加学分和国家终身学习策略使终身学习开始被纳入正规体系的边缘，但成人学习参与在许多国家停滞或下降，距离“成为体系的一部分”仍远',[ADULT,EAG_ADULT]),
17:('P','国际组织、教育科技公司和政府之间的伙伴关系并未消失，但作为前提的全球化与多边主义在窗口内明显承压（大国竞争、战争、部分援助与合作退坡），条件只部分成立',[ 'w:International relations of the European Union']),
18:('P','生成式人工智能已开始改变教学、评估和部分管理环节；虚拟/增强现实、机器人和区块链在学校中的应用仍属试点，远未改写构成“现状”的多数系统性要素',['w:Artificial intelligence in education','w:Educational technology']),
19:('P','替代性工作形式确实延续：混合办公在疫情后成为许多岗位的稳定安排。但普遍缩短工时并未出现，四天工作制多是压缩工时试点，总工时往往并不减少',[REMOTE,PNAS,'https://www.eurofound.europa.eu/en/publications/all/four-days-a-week-europe-debates-shorter-working-times']),
20:('C','课外辅导、私立与国际学校、微型学校以及多样化在线课程，显示教育程度较高的家长继续推动公共与私人方案的多样化',[PEW,'https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3600/RRA3698-1/RAND_RRA3698-1.pdf']),
21:('P','美国在家上学比例高于疫情前（Pew：2022–23 学年约 3.4%，疫情前约 2.8%），微型学校也有增长；但这是边缘扩张，不是经合组织范围内传统学校体系的普遍退出',[PEW]),
22:('T','正式学历作为能力信号正在松动（技能优先招聘、微观证书、部分政府职位取消学历门槛），但学位在多数专业领域仍是主通道，侵蚀尚未完成',[SKILLS,SKILLS2]),
23:('C','IBM、Google 等公司继续并扩大了不将高等学历作为硬性条件的招聘；IBM 称其美国职位一半以上不再要求大学学历，美国二十多个州的公共部门也取消了部分学历门槛',[SKILLS2]),
24:('P','对人工智能和数字化的投资与兴趣在 2022 年后显著增强，作为“情景 4 有可能实现”的信号变强了；但学校体系并未走向解体，随时随地学习也没有取代学校教育。信号在，情景本身没有展开',[ILO,'w:ChatGPT']),
25:('C','智能手表、无线耳机、健康手环和手机上的生成式人工智能助手进一步把技术嵌进日常生活；脑机接口仍处早期，但“嵌入生活（乃至身体）”的方向已经发生',['w:Wearable technology','w:Virtual assistant']),
26:('C','窗口内没有出现教育治理普遍回摆到彻底中央集权或彻底社群主义的局面。绩效问责、网络治理和地方自主仍然并存，个别体系有再集中迹象，但不是书中所否定的那种必然钟摆',[EPO]),
27:('T','疫情期间家庭深度介入子女学习，美国等地的学校选择、在家上学和微型学校讨论升温，高学历家长的选择权更常被当作内在价值；证据偏于部分国家，强度是“也许越来越”',[PEW]),
28:('T','学习分析和教育数据在增长，国际测评仍在进行；同时也出现减少高利害考试的讨论。总体看，“衡量结果”没有缩小，数字化指标还在扩大，但并非所有系统都把测量做得更大',[EAG]),
29:('C','学校网络、国际组织、研究—实践伙伴以及公私合作在疫情应对和教育科技扩散中继续被当作动员专长的常规手段',[EPO]),
30:('C','Google、Microsoft、Apple 等数字平台与学校系统的合作因远程教学而扩大，校园健康、检测和远程医疗等教育—卫生联盟在疫情期间也明显增多',['w:Educational technology','w:School health services']),
31:('C','生成式人工智能和快速变化的技能需求使“学校所学迅速过时、需要持续再技能化”成为 2023 年后劳动与教育政策的主流判断，风险已经可观察',[ILO,ADULT]),
32:('C','OECD《成人学习趋势》显示，尽管终身学习的重要性已有共识，成人学习参与在许多国家停滞甚至下降，平均约 40%，正规项目仅约 8%。目标仍相当遥远',[ADULT,EAG_ADULT]),
33:('C','在个人仍看重学业、看护、社会化和认证的条件下，今日意义上的学校教育继续存在，疫情后入学恢复，学校仍是主导制度',[EAG,'w:Impact of the COVID-19 pandemic on education']),
34:('P','英语仍是互联网和科学交流中最大的单一语言，作为通用语的地位还在。但 W3Techs 显示网站英语份额从 2024 年 1 月约 52.2% 降至 2025 年 1 月约 49.3%，其他语言内容在增长。绝对使用广泛，相对份额并未“更加”占优',[W3,'w:Languages used on the Internet']),
35:('C','混合办公、混合教学和始终在线的通讯使线上与线下的界限在窗口内明显变模糊，远程工作在许多国家稳定在每周约 1–3 天',[REMOTE,PNAS]),
}
