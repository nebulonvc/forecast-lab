# Manual review (METHOD.md redo) of Kaplan, The Revenge of Geography
# review_source manual-assistant-2026-11-15
# V is defined in audit/V.py (same directory)
import runpy
from pathlib import Path
V = runpy.run_path(str(Path(__file__).resolve().parent / "V.py"))["V"]
NF = {}
META = {
    "title": "罗伯特·D·卡普兰《地理的复仇》（The Revenge of Geography）",
    "pub": "**2012 年 9 月 11 日**（Random House 初版；电子版 ISBN 978-0-679-60483-9）。正文为 reading-library 书单中的 PDF（sha256 `64e13003…`）经 pdftotext 得到的全书 TXT（sha256 `ff5b7f15…`）。观察窗口为 2012-09-11 至 2026-11-15（Asia/Shanghai）。书中写明的终点（如 2018—2020 年、1995—2025 年、2050 年）按各自时点判断。",
    "method": "本稿是按 METHOD.md 的重做版（替代此前助手用关键词筛句后只保留 33 条预测的旧稿）。抽取：用仓库 prepare_book v5 流水线把全文切成 221 块（3500 字符、600 字符上下文），助手通读正文各块、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 137 条可核验预测。前言与致谢不录入预测。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，只从检索返回的 URL 中选源，原文存档于 data/sources（sha256），写入 data/evidence.jsonl（210 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。",
    "overall": "卡普兰对2012年后大国竞争回归、印太海权和边缘地带制衡、欧洲因俄乌战争再次被对俄关系决定、南海成为亚洲政治地理核心、伊朗在伊拉克遭反感、叙利亚成为阿拉伯动荡中心等判断，多数已经应验。人口、互联互通和海军投射等方向性预测也大体同向。主要失准集中在定量或时机过满的句子：全球城市人口并未在2025年达到三分之二，俄罗斯穆斯林人口没有在约十年内升至20%，朝鲜半岛政治边界并未移动，两岸经济联系没有降低军事统一压力，阿萨德政权也没有在本书出版前倒下。条件未出现或终点仍在“最终”的条目（朝鲜统一、美国放弃台湾、伊朗政权更迭、阿富汗被稳定等）记为暂无法判断。与旧稿 33 条相比，通读后预测数量明显增加，严格胜率有所下降，但加权胜率仍高，说明书的大方向比若干具体时点和数字更经得起检验。",
    "basis": "本稿由助手逐条对照书中原文与存档证据人工复核：",
    "extra": "\n## 说明\n\n- 本稿取代此前关键词筛选的人工稿（32 条可判定，严格胜率 60%）。新稿按原 DeepSeek 管线通读全书，每条预测都有存档证据。\n- 第 9 条（超音速运输缩短美亚航程）书中未写明年份，按出版日至截止日的隐含窗口判断为错误；相关项目仍在研制，但不把未到期的远期能力记为暂无法判断。\n- 第 56 条（俄罗斯不会出兵重新占领东欧）按上下文理解为已加入北约的东欧国家；俄罗斯入侵了乌克兰，但并未占领波兰、波罗的海等北约东翼。\n- 第 115 条是复合判断：阿萨德“可能撑不到本书出版”与约旦绝对君主制的前景均不成立，整体记为错误。\n- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。\n",
}
