#!/usr/bin/env python3
"""Build the full same-tier ranking of all works.

Reads datasets/all_cases_summary.csv and writes:
  - docs/05-same-tier-ranking.md   (full ranking table, all works)
  - datasets/same_tier_ranking.csv (machine-readable)

Composite score = mean of three same-tier excesses (percentage points):
  strict-rate excess, direction-rate excess, and low-error advantage.

Usage: python3 docs/make_ranking.py
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "datasets/all_cases_summary.csv"
OUT_MD = ROOT / "docs/05-same-tier-ranking.md"
OUT_CSV = ROOT / "datasets/same_tier_ranking.csv"

DOMAIN = {
    "地缘政治与国际秩序": "地缘政治", "宏观经济、金融与市场": "宏观金融",
    "科技、商业与产业颠覆": "科技商业", "AI与奇点前沿": "AI 与奇点",
    "人口、能源、资源与生态": "人口能源资源", "社会结构、制度、文化与教育": "社会制度教育",
    "科幻推演与乌托邦/反乌托邦": "科幻乌托邦",
}


def num(s):
    s = (s or "").replace("%", "").replace("pp", "").replace("+", "").strip()
    return float(s) if s else None


def tier(s):
    t = s.split("(")[0] if s else "—"
    return "100 年以上" if t.startswith(">=") else t


def short_title(t, n=26):
    t = t.split("（")[0].split("(")[0].strip() or t
    return t if len(t) <= n else t[: n - 1] + "…"


def short_author(a, n=22):
    a = a.strip()
    return a if len(a) <= n else a[: n - 1] + "…"


def signed(v):
    return "—" if v is None else f"{v:+.1f}"


rows = list(csv.DictReader(SRC.open(encoding="utf-8-sig")))
for r in rows:
    r["n"] = int(r["可判定数"] or 0)
    r["xs"] = num(r["同档超额严格胜率_pp"])
    r["xd"] = num(r["同档超额方向命中率_pp"])
    r["xe"] = num(r["同档低错优势_pp"])
    vals = [r["xs"], r["xd"], r["xe"]]
    r["score"] = sum(vals) / 3 if all(v is not None for v in vals) else None


TOL = 1.5  # |excess| <= 1.5pp is treated as on par with the tier baseline


def sgn(v):
    return 1 if v > TOL else (-1 if v < -TOL else 0)


def grade(r):
    a, b, c = sgn(r["xs"]), sgn(r["xd"]), sgn(r["xe"])
    if min(a, b, c) >= 0 and (a + b + c) >= 2:
        return "全面领先"
    if a > 0 and c < 0:
        return "高命中·高波动"
    if a > 0:
        return "准且稳"
    if b > 0 and a <= 0:
        return "方向型"
    if max(a, b, c) <= 0 and (a + b + c) <= -2:
        return "全面落后"
    if c > 0:
        return "谨慎少错"
    return "偏弱"


main = sorted([r for r in rows if r["score"] is not None and r["n"] >= 15], key=lambda r: r["score"], reverse=True)
small = sorted([r for r in rows if r["score"] is not None and 5 <= r["n"] < 15], key=lambda r: r["score"], reverse=True)
rest = sorted([r for r in rows if r not in main and r not in small], key=lambda r: (-r["n"], r["书名"]))
assert len(main) + len(small) + len(rest) == len(rows)


def flag(r):
    u = num(r["未定率"])
    return " ⚠️" if u is not None and u >= 60 else ""


def line(rank, r):
    return (f"| {rank} | {short_author(r['作者'])} | 《{short_title(r['书名'])}》{flag(r)} | {r['出版年'] or '—'} | "
            f"{DOMAIN.get(r['领域'], r['领域'])} | {tier(r['时间跨度分档'])} | {r['n']} | "
            f"{r['严格胜率'] or '—'}（{signed(r['xs'])}） | {r['方向命中率'] or '—'}（{signed(r['xd'])}） | "
            f"{r['错误率'] or '—'}（{signed(r['xe'])}） | **{signed(r['score'])}** | {grade(r)} |")


HEAD = ("| 排名 | 作者 | 作品 | 出版 | 领域 | 跨度档 | 可判定 | 严格胜率（超额） | 方向命中率（超额） | "
        "错误率（低错优势） | 综合超额 | 类型 |\n"
        "| ---: | :--- | :--- | ---: | :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |")

counts = {}
for r in main:
    counts[grade(r)] = counts.get(grade(r), 0) + 1
beat = sum(r["score"] > 0 for r in main)

md = [
    f"# 同档基准排行榜：全部 {len(rows)} 部作品",
    "",
    "> 本表将全部作品与**同一时间跨度档**的平均水平比较，按综合超额从高到低排列。由 [`make_ranking.py`](make_ranking.py) 依据 "
    "[`datasets/all_cases_summary.csv`](../datasets/all_cases_summary.csv) 自动生成，机器可读版本见 "
    "[`datasets/same_tier_ranking.csv`](../datasets/same_tier_ranking.csv)。",
    "",
    "## 指标说明",
    "",
    "| 指标 | 计算方式 | 含义 |",
    "| :--- | :--- | :--- |",
    "| 严格胜率超额 | 本书严格胜率 − 同档平均严格胜率 | 完全兑现的比例比同龄作品高多少 |",
    "| 方向命中率超额 | 本书方向命中率 − 同档平均方向命中率 | 方向判断（正确 + 趋势符合）比同龄作品准多少 |",
    "| 低错优势 | 同档平均错误率 − 本书错误率 | 出错比例比同龄作品低多少 |",
    "| **综合超额** | 上述三项的算术平均（百分点） | 排序依据；正值表示总体跑赢同档基准 |",
    "",
    "同档基准按六个时间跨度档分别计算：0–3 年、4–9 年、10–19 年、20–39 年、40–99 年、100 年以上。"
    "三项指标单独排序的结果可能不同，表中三列均已列出，便于按需重排。",
    "",
    "**类型标签**（与同档相差在 ±1.5 个百分点内视为持平）：全面领先（三项均不低于同档，且至少两项领先）· "
    "准且稳（严格胜率领先，错误率不高于同档）· 高命中·高波动（严格胜率领先，但错误率高于同档）· "
    "方向型（方向命中率领先，严格胜率不高于同档）· 谨慎少错（仅错误率低于同档）· 全面落后（三项均不高于同档，且至少两项落后）· 偏弱（其他）。",
    "",
    "## 概览",
    "",
    f"- 可判定 ≥ 15 条的作品共 **{len(main)}** 部，其中 **{beat}** 部综合超额为正，跑赢同档基准。",
    "- 类型分布：" + "，".join(f"{k} {v} 部" for k, v in sorted(counts.items(), key=lambda kv: -kv[1])) + "。",
    f"- 可判定 5–14 条的作品 {len(small)} 部单独排序；可判定不足 5 条或缺少同档基准的作品 {len(rest)} 部列于文末。",
    "",
    "⚠️ 表示该作品未定率 ≥ 60%（多为近年出版、大量预测尚未到期），排名稳定性较低。",
    "",
    "> [!NOTE]",
    "> 本表为回顾性统计，同一作品内的预测可能共享事件簇，选书亦有偏好。排名反映的是本库口径下相对同龄作品的表现，"
    "不应视为对作者整体能力的定论。样本量越小，排名越不稳定。",
    "",
    f"## 一、主榜：可判定 ≥ 15 条（{len(main)} 部）",
    "",
    HEAD,
    *[line(i + 1, r) for i, r in enumerate(main)],
    "",
    f"## 二、参考榜：可判定 5–14 条（{len(small)} 部，样本较少，仅供参考）",
    "",
    HEAD,
    *[line(i + 1, r) for i, r in enumerate(small)],
    "",
    f"## 三、未参与排名：可判定不足 5 条或缺少同档基准（{len(rest)} 部）",
    "",
    "这些作品多为古典政治哲学或经济理论著作，主要阐述抽象条件下的制度规律，可直接结算的预测较少；"
    "或出版时间过近、预测尚未到期。它们的价值在于提供制度与激励分析的思想资源，而非计分样本。",
    "",
    "| 作者 | 作品 | 出版 | 领域 | 预测数 | 可判定 | 未定率 |",
    "| :--- | :--- | ---: | :--- | ---: | ---: | ---: |",
    *[f"| {short_author(r['作者'])} | 《{short_title(r['书名'])}》 | {r['出版年'] or '—'} | "
      f"{DOMAIN.get(r['领域'], r['领域'])} | {r['预测数']} | {r['n']} | {r['未定率'] or '—'} |" for r in rest],
    "",
]
OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["榜单", "排名", "slug", "作者", "书名", "出版年", "领域", "时间跨度分档", "可判定数",
                "严格胜率", "同档超额严格胜率_pp", "方向命中率", "同档超额方向命中率_pp",
                "错误率", "同档低错优势_pp", "综合超额_pp", "类型"])
    for label, group in (("主榜", main), ("参考榜", small)):
        for i, r in enumerate(group, 1):
            w.writerow([label, i, r["slug"], r["作者"], r["书名"], r["出版年"], r["领域"], r["时间跨度分档"],
                        r["n"], r["严格胜率"], signed(r["xs"]), r["方向命中率"], signed(r["xd"]),
                        r["错误率"], signed(r["xe"]), f"{r['score']:+.1f}", grade(r)])
    for r in rest:
        w.writerow(["未排名", "", r["slug"], r["作者"], r["书名"], r["出版年"], r["领域"], r["时间跨度分档"],
                    r["n"], r["严格胜率"], "", r["方向命中率"], "", r["错误率"], "", "", "样本不足"])

print(f"main={len(main)} small={len(small)} rest={len(rest)} beat={beat}")
print("top10:", [(short_title(r["书名"], 12), round(r["score"], 1)) for r in main[:10]])
