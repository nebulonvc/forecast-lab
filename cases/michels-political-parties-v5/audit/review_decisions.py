# Manual judgments after reading archived passages. Each tuple fixes: code, basis, condition,
# reason, limitation, named remaining gap (U only), and hand-selected verbatim evidence sentences.
R={}
def add(i,code,basis,cs,reason,lm,gap,notes):
 R[i]=dict(code=code,basis=basis,cs=cs,reason=reason,limitation=lm,gap=gap,notes=notes)
add(1,'P','observed_window','unconditional','竞争政党通过候选人、纲领和选举争取代表权，群众选举渠道确实成为政治竞争的重要方式；但卡特尔党研究同时指出群众党模式衰退及公众联系减弱，不能认定精英逻辑已被完全取代。','资料主要讨论民主政党的制度形态，不是全球统治原则的统一时间序列；群众党组织与争取群众选票并非同一概念。','',[
('d8f66a509f95','support','In systems with responsible government, universal suffrage, and open, competitive elections, parties put up candidates and programs in a competitive struggle for representation and office.'),
('a91bb8b0acae','counter','This evolution helps to explain the decline in popular connection to political parties.')])
add(2,'U','conditional','unknown','研究说明了Rittinghausen直接立法方案的地方议会设计，德国后来也引入直接民主程序；尚未找到按其整套制度实施后自治失败的直接记录。','现代公投并不等于Rittinghausen的分区起草及表决制度，不能用别的直接民主制度代判。','需确定该整套制度在出版后是否实际实施，以及实施后的自治结果。',[
('a2b4801f81bf','background','Instead, they claimed that real democracy would require a sharp distinction between legislation and administration and the consequent direct involvement of the people in lawmaking through their participation in local assemblies, tasked with both drafting and approving legislative proposals of general import.')])
add(3,'U','evidence','unknown','Your Party允许全体党员网上投票，Podemos也以网上程序处理多次党务选举；这些材料不能证明或推翻上万人按日常党务频率在同一地点开会的可行性。','线上参与、年度大会与同地高频实体会议须严格区分；不能因没搜到实例就判“不可能”正确。','缺少同地万人会议在明确日常党务频率下的实际运行或不可行性证据。',[
('837227b88c2b','boundary','All members will be able to vote online, whether they are in the conference hall or not – unlike Labour, we’re not scared of democracy.'),
('a9ea0db8e2e9','boundary','Podemos hosts multiple electoral processes yearly.')])
add(4,'U','conditional','unknown','马尔堡研究指出Michels的地方经验不代表整个德国劳工运动；现有资料未同时记录党员警惕程度和支薪书记是否垄断地方倡议。','全国党主席人事冲突不是地方书记权力的直接指标，不能借全国案例补足条件。','需要出版后地方支部的党员控制措施与书记独占倡议权的配对材料。',[
('48d080eed74e','boundary',"The unusual nature of Marburg's social and political profile meant that Michels's experience of Social Democratic politics at the local grass-roots level was anything but representative of the German labour movement as a whole.")])
add(5,'W','observed_window','unconditional','国际印刷工会被研究者明确列为成熟组织中真实民主的例外；西欧政党代表研究也发现，在基层与全国领导冲突时，一些代表更重视基层立场。这与永久代表制“始终”等于代表支配被代表者的绝对断言不符。','工会例外不等于所有政党均民主；政党代表的态度也不等于每次实际决策，但足以反对无例外的表述。','',[
('5c444a232ba0','counter','They chose the International Typographical Union (ITU) because almost alone among established unions (one might easily add, almost alone among voluntary associations of any kind or size) the ITU is genuinely democratic.'),
('45400448025c','counter',"We find that New Politics supporters, especially within socialist parties, are predisposed to emphasize the representation of their local party constituency, in case the views of local party branches and a party's national leadership clash.")])
add(6,'P','observed_window','unconditional','SNP研究确实记载多数新增党员不活跃、领导层集中权力，但同一材料又记载约五万党员参加领导选举，不能将所有党务都概括为少数人参与。','单次领导选举与持续日常党务不同，不能把参与人数直接等同于决策权。','',[
('d4826277bd34','support','However, research has shown that the average post-surge SNP member was not very active.'),
('d4826277bd34','counter','50,000 members of the SNP participated in a process which ultimately elected Humza Yousaf as the party’s new leader and Scotland’s next First Minister.')])
add(7,'U','evidence','unknown','比较研究发现上海与圣彼得堡工人对知识分子的从属程度不同，并将差异追溯到历史文化情境；它没有检验知识分子人数增加是否使每人的影响按比例下降。','知识分子整体地位、个人影响力及人数占比是不同变量，不能互相替代。','缺少人数变化与单个知识分子群众影响力相联的出版后数据。',[
('cfea30b3f428','boundary','The investigation demonstrates that workers acquiesced in their subordination to a greater degree in Shanghai than in St Petersburg, and this and other differences are traced back to historical and cultural context.')])
add(8,'P','observed_window','unconditional','前议员访谈显示，党鞭约束有时使工人出身者无法按阶级立场投票，向上流动顾虑也影响行为；但这些人仍保有工人阶级认同，并非一律丧失团结感。','访谈不能证明政治复杂化必然造成统一的新阶级，也不是领导人与基层距离的纵向测量。','',[
('816458d1c09a','support','Class origins may be decisive in shaping ideological outlook but not necessarily behaviour once elected, when the party line becomes a factor.'),
('816458d1c09a','counter','The MP’s working-class identity stretched beyond his parents, back to his grandparents and beyond into how he saw the rest of the world.')])
add(9,'U','conditional','unknown','CPGB材料记载1920年对议会参与的争论，联邦档案馆也记载KAPD拒绝议会道路；但未证明某个已放弃议会策略的党因旧领导的议会技能而继续依赖他们。','新成立的反议会政党与同一政党放弃既有议会策略并不相同。','缺少同一政党策略转向前后、旧议会领导影响及其技能原因的记录。',[
('ad089d2383d7','boundary','Eine vermittelte Form demokratischer Teilhabe durch ein Parlament lehnten sie ab.')])
add(10,'P','conditional','unknown','澳大利亚选举研究报告说，转离工党的选民普遍不满Rudd被撤换；罢免带来政治代价这一部分得到支持。但BBC同时记载其支持率已在被撤换前下滑，不能确认“普遍受尊重”前提及灾难程度。','事后不满与撤换造成的净因果损失不同，也不能从一次案例推出任何受尊重领袖被免都会遭全国性灾难。','',[
('a32edc130407','support','The survey found that 79 per cent of these voters switching support away from Labor disapproved of the way the ALP handled its leadership change when Julia Gillard replaced Mr Rudd last June.'),
('a39ee779f4f8','boundary','But after picking a fight with the resources sector over his plans for a super tax on their super profits, the polls slumped again - especially in the mining states of Western Australia and Queensland.')])
add(11,'P','observed_window','unconditional','战间期英国独立工党确实同时容纳激进知识分子、工人派别及素食生活改革，并以全面社会主义改造为目标，符合激进党成为多种革新试验场的一部分。','这只支持特定党及特定改革，不能证明每个颠覆性政党都容纳所有类型革新者；NPA开除派别的声明也显示容纳有边界。','',[
('c083401d1f22','support','The ILP in the twenties did retain some of the earlier sense of socialism as something that transformed all aspects of life, and Fenner Brockway wrote of their summer schools, where there were always vegetarian tables: \'At the schools we enjoyed a comradeship which we rarely know now.'),
('c313b405d65a','boundary','This declaration addresses the de facto expulsion from the organization of its 296 signers, militants of the New Anticapitalist Party in France from 34 of the party’s committees.')])
add(12,'U','conditional','unknown','客户主义研究发现党内选拔竞争较弱且领导更占优势，但它检验的是客户主义，不是官员自行决定继任圈子后新思想逐年被拒绝。','不能把所有领导支配或客户主义直接当成自我吸纳规则及思想僵化。','需要明确的官员自选继任制度，以及随后新人和新思想准入的变化。',[
('540530419c1d','background','Longitudinal analyses corroborate the hypothesized negative relationship for a sample of CEE parties and for a larger sample of parties outside the region.')])
add(13,'P','conditional','unknown','1918年10月SPD参与包含自由派的议会政府，并继续寻求宪法改革；但同一材料也记载此前的运动分裂以及随后超越改革的十一月革命，不能判定改良主义全面无阻力地扩散。','Max von Baden内阁仅作为温和议会化内阁的近似案例；不能把在此前已存在的改良主义算作该内阁造成的新变化。','',[
('b3606bd90f64','support','Prince Max von Baden is appointed the Chancellor of a parliamentary government formed with the majority parties (the SPD, the Center Party, the Liberals).'),
('823428a4ecd5','counter','Yet the constitutional reforms it was working for were surpassed by the November Revolution.')])
add(14,'W','observed_window','unconditional','1912年确有工会合作保险公司成立，但SPD在1921年仍有政治纲领，2025年仍是拥有联邦议员的政治党，并未在观察窗内变成工人保险社。','判断的是所预警的组织转化结果，而不是否认SPD福利取向；保险企业与政党本体必须区分。','',[
('4a5ac1896a60','boundary','Die gewerkschaftlich-genossenschaftliche »Volksfürsorge«-Versicherungsgesellschaft wird gegründet.'),
('3956ab90ad58','counter','Further, the SPD appealed for the transformation of capitalism into socialism.'),
('d43e17421be3','counter','Initially a socialist workers’ party, the SPD evolved in the Federal Republic of Germany to become a “left-wing catch-all party” with close union ties.')])
add(15,'U','conditional','unknown','FES记录1914年党员总数为1,085,905，其他资料也记载组织及服务扩展；但总存量不能直接证明出版后因互助保险路线新增数十万人。','不把1904—1914整个区间的增长全部算作1911年后的预测命中，也不把保险投保人数当作党员新增数。','缺少1911后净增党员数及其与特定互助保险路线相联系的直接资料。',[
('c5bc5192ad02','background','Die Zahl der Parteimitglieder beträgt 1 085 905, davon 174754 weibliche.')])
add(16,'P','conditional','unknown','资料记载SPD以支薪职员替代早期志愿者，并在1913年雇用约4,000名全职官员；官僚扩张结果与预测相符，但尚不能将其全部归于特定互助福利路线。','较长历史区间含出版前发展，不能把已在1911年前形成的机构全部列作新增；福利条件与结果因果联系有限。','',[
('6403152f5279','support','By 1913 the SPD employed 4,000 full-time officials, with 750 of these assigned to Berlin (Mitchell and Stearns 1971: 97).'),
('6403152f5279','support','With a membership of one million by 1914, organizational needs required the recruitment of a cadre of salaried officers and functionaries to replace the volunteers and part-time activists of an earlier era.')])
add(17,'U','conditional','unknown','资料明确记载意大利1912年开始议员津贴，并有工人代表靠同伴筹款任职的先例；不能用其后有薪制度下的议员构成来判无薪且党贫穷的条件预测。','先例起于1900年，作为边界而非出版后预测反例；1911至津贴改革前的实际人员构成仍缺乏资料。','需要1911—1912无薪期间社会主义党财力及议员私人财产的配对记录。',[
('01680d71a0b7','boundary','Quando, nel 1912, fu introdotta l’indennità parlamentare, Abbo poté dormire a Roma e Pietro Chiesa poté fare a meno della colletta dei compagni.')])
add(18,'U','evidence','unconditional','1919年SPD大会既批评政府内的党员又向其表示信任；当代评论也承认专业干部支配倾向。但这些材料不能确定寡头权力在“可预见时期”内是否作为制度被推翻。','领导人更替不等于寡头制被推翻；原文没有可直接采用的“相当时期”终点或制度阈值。','需固定可预见时期及寡头权力的可操作指标，并有相应组织权力证据。',[
('e01760939934','boundary','Den Parteimitgliedern in der Regierung wird das Vertrauen ausgesprochen, wenn auch der Parteitag an ihnen Kritik übt.')])
add(19,'P','observed_window','unconditional','德国社会运动实证研究发现组织趋于官僚化且行动更温和，支持组织发展伴随保守化的方向；同一研究明确发现正式组织也可能激进，否定不褪色、无例外的保守印记。','社会运动组织不是所有革命党，研究也不支持把相关关系全当成组织自然发展导致的永久结果。','',[
('228402b92200','support','Movements tend to become more centralized-bureaucratic and more moderate in their actions over time.'),
('228402b92200','counter','Informal groups can be moderate in their activities and formal groups can tend towards radical action.')])
add(20,'U','conditional','unknown','Corbyn在2016年挑战后保住领导并于2017年改善地位，但该挑战主要来自议会同僚，基层反而支持他；矿工民主运动案例又是旧领导被替换，均不满足原文“基层反抗但旧领袖留任”的完整条件。','恢复支持与恢复支配不同，更无法从这些材料证明服从是伪装。','缺少基层反抗、领袖留任和其后恢复支配三者连续对应的案例。',[
('91bad33c37f9','boundary','He ultimately won a second leadership election in September 2016 thanks to a strong grassroots movement, and without gaining much credit or support among his colleagues.'),
('7286deec3526','boundary','In national balloting supervised by the U.S. Department of Labor (DOL), Arnold Miller, Mike Trbovich and Harry Patrick ousted an old guard slate headed by W.A. (“Tony”) Boyle, the benighted successor to John L. Lewis, who ran the UMWA in autocratic fashion for 40 years.')])
add(21,'P','conditional','satisfied','USPD分裂后领导层初期几乎由传统中间派构成，显示领导精英延续；但学术研究发现地方组织能违背全国领导意愿决定党政策，两个新组织都重现寡头支配的结论不完整。','地方分权并不自动等于所有层面民主，领导派别构成也不是独占全部权力的充分证明。','',[
('26fd03d7706c','support',"In spite of the varied ideological makeup of the party, the USPD's leadership initially consisted almost exclusively of members of its traditionalist-centrist faction."),
('a2e39d74ec27','counter','An analysis of some sixty extant Independent Social Democratic publications, combined with the examination of more traditional archival sources, particularly the records of the political police, not only suggests a fairly widespread concern with international questions among supporters of the USPD, but also that this local involvement came to be an important and even determining factor in shaping party policy, often against the will of the national leader ship.')])
add(22,'W','conditional','satisfied','Manchin在2018年违背民主党同僚立场支持Kavanaugh，却在随后的参议院选举连任，直接否定异议议员下次选举“必丢席”的绝对结果。','材料证明违背党团共同立场及连任，不声称当代美国党团有与欧洲政党相同的法律性投票命令，也不否认违纪可能有其他代价。','',[
('6ef8b2893a97','counter','When U.S. Sen. Joe Manchin, D-W.Va., was running for reelection, he broke with fellow Democrats by voting to confirm President Donald Trump’s Supreme Court nominee, Brett Kavanaugh.'),
('080fd5d5791f','counter','Democratic Sen. Joe Manchin won reelection in West Virginia on Tuesday, beating Republican state Attorney General Patrick Morrisey and denying the GOP a Senate pickup in a state President Donald Trump carried by a huge margin in 2016.')])
add(23,'P','observed_window','unconditional','1977年的研究记载德国工会候选名单常由地方领导机构组成，重要地区职位受上级影响，说明权力集中未随民主化完全消失；IG Metall同时公开强调自下而上的民主结构。','以组织程序中的领导控制作有限指标，不把任何代表制或工会集中谈判一概称为权威主义，也不能证明未来永不消失。','',[
('43261e32f795','support','Auch hier existiert kein der Kandidatenaufstellung der Parteien vergleichbares Prinzip der Nominierung durch Delegiertenversammlungen, sondern die Kandidatenlisten werden meist durch die örtlichen Führungsgremien zusammengestellt.'),
('ee963f9ad34d','counter','IG Metall has a democratic structure and is organized from the bottom up.')])
add(24,'W','observed_window','unconditional','魏玛时期普鲁士转为有民主议会法律基础的国家，宪制包括男女普选，方向与只有官员享有完整公民权的官员共和国相反。','并不以纸面宪法单独证明所有实际权利平等；史学研究也明确将魏玛普鲁士描述为民主议会国家，纳粹时期破坏另当别论。','',[
('90ac36d01150','counter',"The Constitution provided for a Landtag (parliament) elected by proportional representation under universal suffrage for both men and women, and a State Council (Staatsrat) elected by local parliaments to represent the interests of Prussia's provinces."),
('e5e69423646f','counter','The new Prussia in Weimar Germany, as Otto Braun attempted to make it a reality, was a democratic parliamentary state based on strict legal foundations, destined to unite permanentiy the democratic middle classes and the social democratic working classes, political Catholicism and the left.')])
add(25,'C','observed_window','satisfied','波兰的民族意识和抵抗在斯大林时代仍保存了民族自治与真实生活空间；二战资料也记载民众反对去民族化并保护文化，民族未被强权消灭的结果在观察窗内成立。','不等于主权从未中断、民众未遭大规模杀害，也不把此后所有可能强权的结果一并判定。','',[
('d63bfdbab9e5','support','The enduring strength of the national sentiment enabled Poland to preserve some important islands of national autonomy and authenticity throughout the Stalinist era.'),
('6c3f35a5af7d','boundary','The local peasantry supported Polish independence and stood against the occupier, especially with regard to the policy of denationalising Poles, destroying their culture and the physical ruination of the Polish people.')])
add(26,'U','evidence','unknown','Nan Hardie在1933年仍以工党候选人当选，说明后代并不必然政治倒向敌方；但政治立场延续本身不能证明家庭经济阶级没有改变，尚不能完整判定原文的阶级转化断言。','Liebknecht家族材料也不是工人出身并受工人运动提升的家庭样本；不以政治标签直接替代经济阶级。','需要符合原始工人出身和运动提升条件的家庭，及其本人和子女后续经济地位、政治转向证据。',[
('42f44f8f1023','counter','In 1933 she was elected as a Labour candidate to Cumnock town council, and she became convenor of Cumnock public health committee in the following year.')])
add(27,'U','evidence','unknown','富裕工人研究没有发现物质改善必然带来转投保守党，并拒绝将工人一律理解为日益去激进或必然反体制；这些结果不足以直接测量原文所说革命愿望的逐渐减弱。','政党投票、家庭生活取向和彻底制度变革愿望不可等同；不把拒绝资产阶级化理论直接当成相反的革命化。','缺少同一批工人物质处境改善与革命愿望变化的直接、出版后纵向指标。',[
('ef2ed7b0ca9f','boundary','The notion that there was a necessary connection, among manual workers, between growing material prosperity and increased support for the Conservative Party was therefore decisively rejected.')])
add(28,'P','conditional','unknown','Fimi Media案报道记载同一非法资金同时使HDZ和Sanader本人获益，并称党内将腐败视为常态，支持党用资金与个人侵吞并存的风险。','报道明确是当时非终审判决，并有部分指控证据不足；“高尚动机”起点和将腐败正式视为合法方式未证实，不能全判正确。','',[
('f44b56da9a5c','support',"Sanader received about HRK 250,000 from the company's profits, while the HDZ received more than HRK 14 million, and Nevenka Jurak and others also benefited, she added."),
('f44b56da9a5c','boundary','She said that the charge was dropped that the HDZ had derived undue financial benefits from donations, adding that donations were a legal way of financing political parties.')])
add(29,'U','conditional','unknown','1912年Hildebrand被开除引发自由讨论和科学权利争论；这不等于德国社会主义整体排除知识分子，资料也未给出整体排除后的声望变化。','个别党员开除与排除整个社会类别不是同一条件；争论存在不能自动等同声望大幅下降。','缺少整体排除知识分子的条件实际成立及其后声望变化的证据。',[
('fb3004dcb007','boundary','The facts that Göhre and Schippel gave up their parliamentary seats, that Calwer renounced his party membership in 1909 and that Gerhard Hildebrand, a former member of the National-Social Association, was excluded from the party in 1912, were part of the important ideological disputes within the SPD in Imperial Germany.')])
add(30,'U','evidence','unknown','南约克郡工人教育研究说明工人可成长为有机知识分子，但同时仍有公共知识分子任教师和组织者；英国议会资料又显示工党议员毕业生比例上升。两者都不直接测量运动对外来知识分子帮助的必要性。','“遥远未来”没有明确年限，不能以毕业生增加机械否定帮助必要性减弱，也不能把有机知识分子与资产阶级知识分子等同。','需要相同工人运动在劳动、民主条件改善前后对特定知识分子功能依赖的测量。',[
('9940ac2ab764','background',"Workers involved in the process of popular workers' education become organic intellectuals having key roles in local and national politics, in the steel and miners' strikes of the 1980s, and in the formation of Northern College."),
('3b7e8dc43421','boundary','Before 1945, less than 20% of Labour MPs were graduates.')])
add(31,'P','conditional','unknown','瑞士公投在20世纪后半叶出现参与率下降，且较多直接民主程序与较低选举参与有关，支持参与负荷问题的一部分；研究却把关系解释为长期适应而非即时投票疲劳。','瑞士平均每年四次联邦公投，不是每周堆满重要问题；选举投票率也不同于公投热情，条件频率与原因均不完全匹配。','',[
('f0a6f4478cca','support','Over the second part of the twentieth century, turnout at federal referendums fell from around 50-70% to an average of around 40%; this mirrored a similar decline in turnout at federal elections from 80% to around 45%.'),
('90c8c1cdb48a','counter','Furthermore, by distinguishing between short and long-term effects of direct democracy, we show that the relationship observed is of a long-term nature and can therefore be seen as a result of adaptive learning processes rather than of instantaneous voter fatigue.')])
add(32,'W','observed_window','unconditional','瓦文萨领导罢工并成为团结工会领袖的案例支持常见领导形成；但1977年西班牙鞋业罢工记述明确称代表是可撤回的临时传达人、受大会控制，构成“任何罢工都无法避免独立领袖阶层”的反例。','西班牙材料是带政治立场的运动记述，短期罢工不等于所有组织长期无领导；这里反驳的是无例外、任何形式的绝对说法。','',[
('52b823dea7c3','counter','They had to accept the wishes of the assemblies because in the end they were no more than emissaries.'),
('da751cd66ae6','support','Wałęsa became the leader of the popular new labour union, Solidarity.')])
add(33,'U','conditional','unknown','德国1918—1919年扩大投票权，葡萄牙激进左翼支持政府后也兑现不少政策承诺；但资料不能确认这些案例就是旧统治阶级成功吸纳全部极左反对派的条件，更未直接检验公共权利民主化停止。','革命更换统治结构、议会支持协议和被旧统治阶级收编不宜混用；社会经济政策兑现也不是公民权利扩张本身。','需要可识别的极左收编完成事件和其前后公共权利变化的直接指标。',[
('cacd90909d14','boundary','The government programme changed the law on elections so that people aged 20-25 and soldiers on active service could vote for the first time.'),
('782b0f267d82','boundary','In exchange, the majority of policy pledges agreed with the socialists were implemented by the beginning of the legislature.')])
add(34,'U','conditional','unknown','1919年德国起义流血失败，而1917年布尔什维克成功夺权；关于俄国的研究明确指出国家机构瓦解使成功成为可能，不能把这个非常态反例直接套进“通常情况下”的条件。','原文未给“通常”可操作边界，现有成功与失败案例又都位于战争和革命危机，不能任意挑一个判对错。','缺少预先界定的一般国家条件及其下社会主义党正面对抗结果的匹配资料。',[
('9286847b8829','boundary','The Bolshevik Revolution, also referred to as the "Great October Socialist Revolution," was the first successful Marxist coup in history.'),
('28df92716f61','boundary','This structural demobilization both made it possible for relatively modest numbers of revolutionary forces to succeed in October 1917 and made the emergence of widespread apathy and disillusionment in 1918 much more likely.')])
add(35,'W','conditional','satisfied','1920年右翼政变攻击共和国时，SPD领导人Wels参与组织总罢工并促使政变崩溃，说明受攻击不必然导致放弃既得阵地；他在1933年也公开反对授权法。','罢工并非武装内战，不能据此声称SPD总会诉诸武力；反例针对一遭攻击就放弃权利的结果，而非否认1933年遭镇压。','',[
('7b79e23d4eb0','counter','In 1920, he helped to organize the general strike in Berlin, which led to the collapse of a right-wing coup, the so-called Kapp Putsch.'),
('7b79e23d4eb0','counter',"He was the only German parliamentary leader to openly oppose passage of the Enabling Act, legislation proposed by the Nazis that turned over authority to pass laws to Hitler's ruling coalition for a period of 4 years.")])
add(36,'P','conditional','unknown','苏联的社会财富管理确实依赖庞大行政层级及中央计划，支持集体管理仍需广泛官僚机构的观察结果；但不能把实际苏联直接等同原文的无阶级、严格可撤回任职社会。','南斯拉夫自我管理提供不同制度边界，证明某个历史体制依赖官僚并不证明所有可撤回自治制度都技术上必须如此。','',[
('c6d12807ff56','support','This authority was realized through a vast administrative hierarchy responsible for turning the general objectives and wishes of the Party and its leadership into operational plans and detailed implementing instructions, and then overseeing and enforcing their implementation to the extent possible.')])
add(37,'C','conditional','satisfied','美国国会图书馆据档案记载，布尔什维克夺权后由小型精英集团以法令和恐怖统治，重大决策集中于党内高层，符合革命过渡成为领导人专政的主结果。','早期工人曾尝试工厂自治，不能将群众参与全部抹去；判定仅指已发生的苏联过渡，不证明所有可能的社会主义过渡都相同。','',[
('6b5d71c70a62','support','The small, elite group of Bolshevik revolutionaries which formed the core of the newly established Communist Party dictatorship ruled by decree, enforced with terror.'),
('0c50e5dae8b8','boundary','It traces the attempts of workers to take control of their working lives from the February Revolution through to June 1918, when the Bolsheviks nationalised industry.')])
add(38,'P','observed_window','unconditional','共产主义社会研究记载苏联和东欧形成明显分层、精英子女通过关系及教育延续地位，支持革命后新特权的问题；但中国研究又显示旧精英后代优势回归，不能将一切都说成全新隐蔽寡头的替换。','社会经济分层不是对“秘密煽动寡头”全部政治机制的证明，平等外衣、秘密操作及旧阶级完全替换并未全部得到核实。','',[
('76a7bde0111f','support','By the 1960s the rapid upward mobility of worker and peasant children in the intelligentsia and Party hierarchy had noticeably slowed, and an inherited class structure emerged.'),
('08efd8b394c7','counter','However, the pattern of inequality that characterized the pre-revolution generation re-emerges today.')])
add(39,'U','evidence','satisfied','人权观察确认苏联长期系统性侵犯人权并于1991年瓦解，但这不能单独证明忽略自由就是社会主义失败的决定机制；其他存档同时强调经济停滞、民族诉求及思想异议。','制度侵犯自由与其后崩溃并存不等于充分的因果检验，也没有“经济组织即使出色”条件下的可比证据。','缺少区分经济、民族及自由因素，并直接检验自由被忽视导致失败的证据。',[
('639b94af03ba','background','The Soviet system of rule had for many years been notorious for systematic violations of human rights.'),
('5363d5031f66','boundary','Among these, three stand out: economic stagnation, the aspirations of the national minorities, and intellectual dissent.')])
add(40,'P','observed_window','unconditional','New Labour在集体劳工权利方面拒绝逆转若干限制，符合工人党领导可能偏离工会利益的担忧；但同一材料记载最低工资和个体劳动权利改善，并非所有政策都服务于完全相反的利益。','工会利益不是全部无产阶级利益，不能把劳工党内部复杂的政策组合一概判为背叛工人。','',[
('e859e1d0b4b8','support','However, largely out of fear of being portrayed as restoring trade-union power, it has refused to address the bigger issue of collective rights and resisted European Union initiatives in this direction.'),
('e859e1d0b4b8','counter','Since coming to office in 1997, New Labour has honoured many of its pledges to improve the individual rights of British workers, including the minimum wage and protection against unfair dismissal.')])
add(41,'C','observed_window','satisfied','苏联在1922—1991年间仍有明确的最高领导序列，领导人多通过掌握共产党领导权取得权力，社会主义者胜利后并未消除领导与被领导的政治区分。','只判已经观察到的社会主义政权，不将“始终”理解为已经验证了无限未来；委员会民主的制度理想也仍涉及代表。','',[
('86555fbc9a4b','support','The Soviet Union had eight leaders during its existence from 1922 to 1991.'),
('86555fbc9a4b','support','Unlike countries in which a president or prime minister is the designated head of state, the leaders of the USSR mostly assumed power by becoming the head of the Soviet Union’s Communist Party, in addition to any other roles they may have taken on along the way.')])
add(42,'P','observed_window','unconditional','莫斯科1922—1923年研究发现新的统治集团与工人之间已形成剥削和对抗关系，支持革命胜利仍可能延续统治区分；但早期妇女和教育改革说明不能说社会主义的一切实际理想都同时落空。','局部统治阶级形成与群众内部结构完全不变、理想全部消亡不是同一强度命题。','',[
('05529f2c4f1f','support','The article aims to show that, while the process of the formation of the Soviet ruling class was still at a very early stage, exploitative and antagonistic relationships with the working class were already developing.'),
('2250a3f4c463','counter','Initiated by figures like Alexandra Kollontai, they aimed to liberate women by removing traditional restrictions on marriage, divorce, abortion and contraception.')])
add(43,'W','observed_window','unconditional','Porto Alegre参与式预算把投资和支出的真实决定交给开放地方大会，让数千公民作实际决定并监督结果，不只是抽象称其为统治者，与群众永不实际治理的绝对断言冲突。','地方部分预算治理不是全国全部国家权力；反例只否定“永不、只有抽象”的无限断言，不能推出所有群众统治都成功。','',[
('52fbc9434bf0','counter','By turning over government decisions on investment and spending to local assemblies open to all, participatory budgeting has enabled several thousand Brazilian citizens to make real decisions, to demand accountability, and to monitor the results.')])
add(44,'U','definition','unknown','100项研究的元分析发现参与小型公共议事可提高知识和推理技能，这反对将群众能力视为完全不可改善；但能力改善仍不能证明原文所谓整体治理“不成熟”已经消失。','小规模议事者、全体群众以及社会主义实现是不同范围，不能将可学习性或知识分数直接当成完全治理成熟。','需预先界定治理成熟标准，并有民主化或社会主义后整体群众达到或未达到该标准的证据。',[
('6e122ce968fa','counter','We also find that participation in mini-publics changes citizens’ policy attitudes and positively affects citizens’ political attitudes, knowledge, internal efficacy and reasoning skills.')])
add(45,'P','conditional','unknown','跨社会WVS研究发现生活机会扩大伴随更强的解放价值倾向，支持经济和文明条件改善的一部分；但东亚比较发现高教育不必然带来相同自我表达变化，灌输教育也可增强威权动员。','解放价值、自我表达和自由探究并非同一测量；不以民主支持或一般教育程度冒充直接的批判探究能力。','',[
('468152760008','support','Empirically, we demonstrate evidence for the following sequence: (1) in response to widening opportunities of life, people place stronger emphasis on emancipative values, (2) in response to a stronger emphasis on emancipative values, feelings of agency gain greater weight in shaping people’s life satisfaction, (3) in response to a greater impact of agency feelings on life satisfaction, the level of life satisfaction itself rises.'),
('9c0b303a5901','counter','Specifically, in Japan, where education levels are as high as in Germany, the support for liberal notions of democracy was comparatively low, what can be called the `second paradox\'.')])
add(46,'U','conditional','unknown','全球民意研究显示对民主有较强偏好，也同时出现对不受约束领导更为宽容；这些资料没有把“认识民主优于贵族制”与“因看见民主缺陷而回归贵族制”的概率变化直接联系起来。','世袭君主作为礼仪国家元首不等于贵族统治，故不把欧洲君主制存续机械当作反例。','缺少对贵族统治而非君主象征的偏好，以及民主优势认知与回归概率的直接联动证据。',[
('a180e0b23950','boundary','Our analysis shows that, over the past quarter century, humanity consistently has had a strong preference for democratic government.'),
('3f5ec9c8e8c2','boundary','In practice, the countries studied are de facto republics, but with hereditary heads of state who occupy social roles beyond the reach of quotidian politics.')])
add(47,'P','observed_window','unconditional','Podemos和五星运动研究发现线上协商仍由领导层控制议题和时机，符合民主运动重新集中权力的一阶段；德国绿党及工会民主研究又表明领导支配并非不可避免。','存档并未验证不断与旧统治阶级融合、再由新反对派取代的完整无限循环；这是实质环节缺证，不是单纯因尚未到终点而降为趋势。','',[
('934fdb6e6cce','support','The conclusion is that the impact of the participation platforms on the quality of IPD is modest insofar as the leadership of both parties controls the subject, framing, and timing of the consultations to strengthen its own position.'),
('3d1de8fec2a5','counter','The organization of the West German Green Party, while not completely successful in avoiding oligarchic tendencies, does inhibit leadership domination of the membership and party activists.')])
