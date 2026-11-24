#!/usr/bin/env python3
"""Generate the ten analytical figures used in docs/00-key-insights.md.

Data source: datasets/all_cases_summary.csv (132 works). Method-cluster and
failure-mode tallies are taken from docs/reports/panoramic-report.md and
docs/reports/curated-330-compendium.md respectively.

Usage: python3 docs/figures/make_figures.py
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CSV = ROOT / "datasets/all_cases_summary.csv"

# ---------------------------------------------------------------- style
for cand in ["/System/Library/Fonts/Hiragino Sans GB.ttc",
             "/System/Library/Fonts/STHeiti Medium.ttc",
             "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"]:
    if Path(cand).exists():
        font_manager.fontManager.addfont(cand)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=cand).get_name()
        break
plt.rcParams["axes.unicode_minus"] = False

BG = "#F6F4EE"
INK = "#141413"
BODY = "#383733"
MUTED = "#78746C"
GRID = "#E3DED3"
GREY = "#C9C3B6"
TERRA = "#C85A3A"
COBALT = "#2B5B84"
FOREST = "#3D6B52"
AMBER = "#A66E28"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "axes.edgecolor": GREY, "axes.labelcolor": BODY, "xtick.color": BODY,
    "ytick.color": BODY, "text.color": INK, "font.size": 12,
    "axes.spines.top": False, "axes.spines.right": False,
})

SRC = "数据来源：Forecast Lab · 132 部著作 · 8,130 条预测 · 证据截止 2026-11"


def frame(title: str, subtitle: str, figsize=(12, 6.75)):
    fig = plt.figure(figsize=figsize)
    fig.text(0.045, 0.94, title, fontsize=20, fontweight="bold", color=INK, ha="left", va="top")
    fig.text(0.045, 0.875, subtitle, fontsize=12.5, color=MUTED, ha="left", va="top")
    fig.text(0.045, 0.025, SRC, fontsize=9, color=MUTED, ha="left")
    return fig


def save(fig, name: str):
    fig.savefig(OUT / name, dpi=160)
    plt.close(fig)
    print("saved", name)


def pct(s: str) -> float | None:
    s = (s or "").replace("%", "").replace("pp", "").replace("+", "").strip()
    return float(s) if s else None


rows = list(csv.DictReader(CSV.open(encoding="utf-8-sig")))
for r in rows:
    for k in ("可判定数", "正确", "趋势符合", "部分符合", "错误", "暂无法判断", "预测数",
              "写明时间可判定数", "隐含窗口可判定数"):
        r[k] = int(r[k] or 0)

DOMAIN_SHORT = {
    "地缘政治与国际秩序": "地缘政治",
    "宏观经济、金融与市场": "宏观金融",
    "科技、商业与产业颠覆": "科技商业",
    "AI与奇点前沿": "AI 与奇点",
    "人口、能源、资源与生态": "人口能源资源",
    "社会结构、制度、文化与教育": "社会制度教育",
    "科幻推演与乌托邦/反乌托邦": "科幻乌托邦",
}
TYPE_SHORT = {
    "国际机构与政府智库": "国际机构与智库",
    "政治家与战略实务者": "政治家与实务者",
    "地缘与社科政治学者": "地缘与社科学者",
    "经济学家与金融投资人": "经济学家与投资人",
    "科技商业思想家与产业实践者": "科技商业思想家",
    "古典思想家与科幻/乌托邦作家": "古典与科幻作家",
}


def agg(rs):
    n = sum(r["可判定数"] for r in rs)
    c = sum(r["正确"] for r in rs)
    t = sum(r["趋势符合"] for r in rs)
    w = sum(r["错误"] for r in rs)
    f = sum(r["预测数"] for r in rs)
    u = sum(r["暂无法判断"] for r in rs)
    return dict(n=n, strict=c / n * 100 if n else 0, direction=(c + t) / n * 100 if n else 0,
                error=w / n * 100 if n else 0, undecided=u / f * 100 if f else 0, works=len(rs))


# =================================================================== F1
def fig1():
    fig = frame("三分之一的可判定预测完全应验，13.6% 明确错误",
                "从 10,683 条候选语句到 5,060 条可判定预测：先剔除非预测，再如实保留无法判断的部分")
    ax = fig.add_axes([0.045, 0.50, 0.91, 0.30])
    ax.set_xlim(0, 10683); ax.set_ylim(-0.5, 2.6); ax.axis("off")
    stages = [(10683, "候选语句", GREY, "10,683"),
              (8130, "可评分预测", COBALT, "8,130"),
              (5060, "可判定预测", FOREST, "5,060")]
    for i, (v, lab, col, txt) in enumerate(stages):
        y = 2 - i
        ax.barh(y, v, height=0.62, color=col, alpha=0.9 if i else 0.55)
        ax.text(120, y, f"{lab}  {txt}", va="center", ha="left", fontsize=13,
                color="white" if i else INK, fontweight="bold")
    ax.text(8130 + 120, 1, "剔除 2,553 条非预测语句", va="center", fontsize=11, color=MUTED)
    ax.text(5060 + 120, 0, "另有 3,070 条（37.8%）因期限未到或证据不足，记为“暂无法判断”",
            va="center", fontsize=11, color=MUTED)

    ax2 = fig.add_axes([0.045, 0.14, 0.91, 0.26])
    cats = [("正确", 1686, FOREST), ("趋势符合", 971, "#7FA48C"),
            ("部分符合", 1714, AMBER), ("错误", 689, TERRA)]
    total = sum(v for _, v, _ in cats)
    left = 0
    for lab, v, col in cats:
        ax2.barh(0, v, left=left, color=col, height=0.55)
        ax2.text(left + v / 2, 0.02, f"{lab}\n{v:,} · {v / total:.1%}", ha="center", va="center",
                 color="white", fontsize=12.5, fontweight="bold")
        left += v
    ax2.set_xlim(0, total); ax2.set_ylim(-0.6, 0.75); ax2.axis("off")
    ax2.text(0, 0.55, "5,060 条可判定预测的结果构成", fontsize=13, color=INK, fontweight="bold")
    ax2.text(total, 0.55, "方向命中率 = 正确 + 趋势符合 = 52.5%", fontsize=11.5, color=FOREST, ha="right")
    save(fig, "fig01-overview.png")


# =================================================================== F2
TIERS = [("0–3年", "0–3年"), ("4–9年", "4–9年"), ("10–19年", "10–19年"),
         ("20–39年", "20–39年"), ("40–99年", "40–99年"), (">=100年", "100 年以上")]


def fig2():
    fig = frame("观察窗口越长，错误率越高；短窗口的低错误率主要源于“尚未到期”",
                "按出版年至证据截止日的跨度分档。折线：错误率与方向命中率（占可判定）；灰柱：未定率（占全部预测）")
    ax = fig.add_axes([0.08, 0.15, 0.86, 0.66])
    labels, err, und, dirn = [], [], [], []
    for key, lab in TIERS:
        a = agg([r for r in rows if r["时间跨度分档"].startswith(key)])
        labels.append(f"{lab}\n{a['works']} 部 · 未定 {a['undecided']:.0f}%")
        err.append(a["error"]); und.append(a["undecided"]); dirn.append(a["direction"])
    x = list(range(len(labels)))
    ax.axvspan(1.5, 3.5, color=COBALT, alpha=0.06, zorder=0)
    ax.text(2.5, 90, "最适合检验预测能力的区间", ha="center", color=COBALT, fontsize=11.5, fontweight="bold")
    ax.text(2.5, 85, "已揭晓结果充足，又未被技术代际淘汰", ha="center", color=COBALT, fontsize=10)
    ax.bar(x, und, color=GREY, width=0.5, alpha=0.55, label="未定率")
    ax.plot(x, dirn, color=FOREST, lw=2, marker="s", ms=7, ls="--", label="方向命中率", zorder=3)
    ax.plot(x, err, color=TERRA, lw=3, marker="o", ms=9, label="错误率", zorder=4)
    for i in x:
        if i == 4:
            ax.text(i - 0.15, err[i] + 1.5, f"{err[i]:.1f}%", ha="right", va="bottom", color=TERRA,
                    fontweight="bold", fontsize=12.5)
        else:
            ax.text(i + 0.12, err[i] - 0.5, f"{err[i]:.1f}%", ha="left", va="top", color=TERRA,
                    fontweight="bold", fontsize=12.5)
        ax.text(i, dirn[i] + 2.5, f"{dirn[i]:.0f}%", ha="center", color=FOREST, fontsize=10.5)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylim(0, 96); ax.set_ylabel("%")
    ax.yaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    ax.legend(loc="upper right", frameon=False, fontsize=11, ncol=3, bbox_to_anchor=(1, 1.08))
    save(fig, "fig02-time-horizon.png")


# =================================================================== F3
def fig3():
    fig = frame("宏观金融最难押准，人口能源两极分化，科幻乌托邦错误率最高",
                "各领域的严格胜率与错误率——这是判断单部作品是否“超越基准”的参照线")
    ax = fig.add_axes([0.17, 0.13, 0.78, 0.68])
    data = []
    for d, short in DOMAIN_SHORT.items():
        a = agg([r for r in rows if r["领域"] == d])
        data.append((short, a))
    data.sort(key=lambda t: t[1]["error"])
    for i, (lab, a) in enumerate(data):
        ax.plot([a["error"], a["strict"]], [i, i], color=GREY, lw=2, zorder=1)
        ax.scatter(a["strict"], i, s=170, color=FOREST, zorder=3)
        ax.scatter(a["error"], i, s=170, color=TERRA, zorder=3)
        ax.text(a["strict"] + 1.2, i, f"{a['strict']:.1f}%", va="center", color=FOREST, fontsize=11)
        ax.text(a["error"] - 1.2, i, f"{a['error']:.1f}%", va="center", ha="right", color=TERRA, fontsize=11)
        ax.text(52, i, f"可判定 {a['n']:,}", va="center", color=MUTED, fontsize=10)
    ax.set_yticks(range(len(data))); ax.set_yticklabels([d[0] for d in data], fontsize=12.5)
    ax.set_xlim(0, 58); ax.set_xlabel("%")
    ax.xaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    ax.scatter([], [], s=120, color=FOREST, label="严格胜率")
    ax.scatter([], [], s=120, color=TERRA, label="错误率")
    ax.legend(loc="lower right", frameon=False, fontsize=11, ncol=2, bbox_to_anchor=(1, 1.0))
    save(fig, "fig03-domain-baselines.png")


# =================================================================== F4
def fig4():
    fig = frame("锁定同一时间跨度后，国际机构与智库在可比的两档中均居首位",
                "六类作者在三个时间跨度档内的严格胜率；“—”表示该档样本不足（可判定 < 50 条）")
    groups = [("0–9 年", ("0–3年", "4–9年")), ("10–39 年", ("10–19年", "20–39年")),
              ("40 年以上", ("40–99年", ">=100年"))]
    types = list(TYPE_SHORT)
    ax = fig.add_axes([0.06, 0.22, 0.90, 0.58])
    width = 0.13
    for gi, (glab, keys) in enumerate(groups):
        for ti, t in enumerate(types):
            rs = [r for r in rows if r["作者类型"] == t and r["时间跨度分档"].startswith(keys)]
            a = agg(rs)
            xpos = gi + (ti - 2.5) * width
            if a["n"] < 50:
                ax.text(xpos, 1.5, "—", ha="center", color=MUTED, fontsize=11)
                continue
            col = TERRA if t == "国际机构与政府智库" else GREY
            ax.bar(xpos, a["strict"], width=width * 0.92, color=col)
            ax.text(xpos, a["strict"] + 0.8, f"{a['strict']:.0f}", ha="center", fontsize=10,
                    color=TERRA if col == TERRA else BODY, fontweight="bold" if col == TERRA else None)
    ax.set_xticks(range(3)); ax.set_xticklabels([g[0] for g in groups], fontsize=13)
    ax.set_ylabel("严格胜率 %"); ax.set_ylim(0, 56)
    ax.yaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    # legend as ordered labels
    for ti, t in enumerate(types):
        fig.text(0.06 + ti * 0.152, 0.085, f"{ti + 1}. {TYPE_SHORT[t]}", fontsize=10.5,
                 color=TERRA if ti == 0 else BODY, fontweight="bold" if ti == 0 else None)
    fig.text(0.06, 0.12, "每组柱子从左到右依次为：", fontsize=10, color=MUTED)
    save(fig, "fig04-author-types-by-horizon.png")


# =================================================================== F5
LABELS5 = {  # title: (label, text_x, text_y, ha)
    "智能基础设施的未来：通向2055的情景": ("UK GO-Science\n《智能基础设施2055》", 45.5, 14.5, "right"),
    "回到教育的未来：经合组织的四种学校教育情景": ("OECD《回到教育的未来》", 33, -6, "left"),
    "全球关键矿产展望2024（Global Critical Minerals Outlook 2024）": ("IEA《关键矿产2024》", 33, -10, "left"),
    "后美国世界": ("扎卡利亚《后美国世界》", 27, -13.5, "left"),
    "战略远见": ("布热津斯基《战略远见》", 26.5, -18.5, "left"),
    "世界是平的": ("弗里德曼《世界是平的》", 13, -8, "center"),
    "煤炭问题：关于国家进步与煤矿可能耗尽的探究": ("杰文斯《煤炭问题》", 27, 10, "left"),
    "预言": ("威尔斯《预言》", 23, 13.5, "left"),
    "超级智能": ("博斯特罗姆《超级智能》", 1, 15.5, "center"),
    "增长的极限": ("梅多斯《增长的极限》", 7, 28.1, "right"),
    "法国革命论": ("伯克《法国革命论》", 17.5, 25.6, "left"),
    "奇点临近": ("库兹韦尔《奇点临近》", -30, -20.5, "center"),
    "注定一战": ("艾利森《注定一战》", -17.7, -15.4, "left"),
    "回顾": ("贝拉米《回顾》", -24.8, -34.4, "left"),
    "人口原理": ("马尔萨斯《人口原理》", -3.5, -33.5, "left"),
    "人口爆炸": ("埃利希《人口爆炸》", -4.5, -11.2, "left"),
    "必然": ("凯文·凯利《必然》", -27, -4.5, "center"),
    "原则：应对变化中的世界秩序": ("达利欧《世界秩序》", -14.5, -9, "center"),
    "金融炼金术": ("索罗斯《金融炼金术》", 12, -21.3, "left"),
}


def fig5():
    fig = frame("超越同档基准且错误更少的作品，集中在右上象限",
                "每个点代表一部作品（可判定 ≥ 15 条）；点越大样本越多。横轴：胜率超出同档多少；纵轴：错误比同档少多少",
                figsize=(12, 8))
    ax = fig.add_axes([0.08, 0.10, 0.88, 0.72])
    pts = []
    for r in rows:
        x, y = pct(r["同档超额严格胜率_pp"]), pct(r["同档低错优势_pp"])
        if x is None or y is None or r["可判定数"] < 15:
            continue
        pts.append((x, y, r))
    ax.axhline(0, color=MUTED, lw=1); ax.axvline(0, color=MUTED, lw=1)
    for x, y, r in pts:
        if x > 0 and y > 0:
            col, a = FOREST, 0.75
        elif x < 0 and y < 0:
            col, a = TERRA, 0.75
        else:
            col, a = GREY, 0.7
        ax.scatter(x, y, s=r["可判定数"] * 2.2 + 20, color=col, alpha=a, edgecolor="white", lw=0.8)
        if r["书名"] in LABELS5:
            lab, tx, ty, ha = LABELS5[r["书名"]]
            far = abs(tx - x) > 3 or abs(ty - y) > 2
            ax.annotate(lab, (x, y), xytext=(tx, ty), textcoords="data", fontsize=9.5, color=INK,
                        ha=ha, va="center",
                        arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7) if far else None)
    ax.set_xlim(-36, 46); ax.set_ylim(-42, 34)
    ax.set_xlabel("同档超额严格胜率（百分点）"); ax.set_ylabel("同档低错优势（百分点）")
    kw = dict(fontsize=13, fontweight="bold", alpha=0.85)
    ax.text(44, 31, "又准又稳", color=FOREST, ha="right", **kw)
    ax.text(-35, -27, "胜率低且错误多", color=TERRA, ha="left", **kw)
    ax.text(44, -38, "命中多，但错误也多", color=MUTED, ha="right", fontsize=11)
    ax.text(-34, 31, "谨慎少错，但少有完全命中", color=MUTED, ha="left", fontsize=11)
    ax.grid(True, color=GRID); ax.set_axisbelow(True)
    save(fig, "fig05-beat-the-baseline.png")


# =================================================================== F6
SHORTNAME = {
    "后美国世界": "扎卡利亚《后美国世界》", "民主的理想与现实": "麦金德《民主的理想与现实》",
    "注定一战": "艾利森《注定一战》", "贫困、繁荣与地球报告2024：走出多重危机的路径": "世界银行《贫困、繁荣与地球》",
    "世界秩序": "基辛格《世界秩序》",
    "Essentials of Economic Theory: As Applied to Modern Problems of Industry and Public Policy": "J. B. 克拉克《经济理论要义》",
    "金融炼金术": "索罗斯《金融炼金术》", "原则：应对变化中的世界秩序": "达利欧《世界秩序》",
    "智能基础设施的未来：通向2055的情景": "UK GO-Science《智能基础设施2055》",
    "经合组织数字经济展望2024（第二卷）：加强连接、创新与信任": "OECD《数字经济展望2024》",
    "免费": "安德森《免费》", "奇点更近": "库兹韦尔《奇点更近》*",
    "为人工智能的未来做准备": "美国 NSTC《为AI的未来做准备》", "奇点临近": "库兹韦尔《奇点临近》",
    "全球关键矿产展望2024（Global Critical Minerals Outlook 2024）": "IEA《关键矿产2024》",
    "煤炭问题：关于国家进步与煤矿可能耗尽的探究": "杰文斯《煤炭问题》",
    "正在消失的野生生物": "霍纳迪《正在消失的野生生物》",
    "回到教育的未来：经合组织的四种学校教育情景": "OECD《回到教育的未来》",
    "共同重新构想我们的未来：教育的新社会契约": "UNESCO《共同重新构想我们的未来》",
    "政党：现代民主中寡头化倾向的社会学研究": "米歇尔斯《政党》",
    "航空器：战争与和平中的发展及其商业未来": "戴维《航空器》", "预言": "威尔斯《预言》",
    "回顾": "贝拉米《回顾》", "战略远见": "布热津斯基《战略远见》",
}


def fig6():
    fig = frame("每个领域都有显著跑赢与跑输同档基准的作品",
                "同档超额严格胜率（百分点）：各领域领先的前两部与落后的一部（可判定 ≥ 15 条）",
                figsize=(12, 9))
    ax = fig.add_axes([0.34, 0.10, 0.62, 0.74])
    items, ylabels, domain_marks = [], [], []
    y = 0
    for d, short in DOMAIN_SHORT.items():
        rs = [r for r in rows if r["领域"] == d and r["可判定数"] >= 15 and pct(r["同档超额严格胜率_pp"]) is not None]
        rs.sort(key=lambda r: pct(r["同档超额严格胜率_pp"]), reverse=True)
        pick = rs[:2] + rs[-1:]
        domain_marks.append((y, short))
        for r in pick:
            items.append((y, pct(r["同档超额严格胜率_pp"]), r))
            ylabels.append((y, SHORTNAME.get(r["书名"], r["书名"][:14])))
            y += 1
        y += 0.8
    for yy, v, r in items:
        col = FOREST if v > 0 else TERRA
        ax.barh(yy, v, color=col, height=0.7)
        ax.text(v + (0.8 if v > 0 else -0.8), yy, f"{v:+.1f}", va="center",
                ha="left" if v > 0 else "right", fontsize=10, color=col)
    ax.set_yticks([p for p, _ in ylabels]); ax.set_yticklabels([l for _, l in ylabels], fontsize=10.5)
    ax.invert_yaxis(); ax.axvline(0, color=MUTED, lw=1)
    ax.set_xlim(-38, 46); ax.xaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    for yy, short in domain_marks:
        fig.text(0.02, 0, "")
        ax.text(-37.5, yy - 0.75, short, fontsize=11.5, fontweight="bold", color=COBALT, va="center")
    fig.text(0.60, 0.025, "* 《奇点更近》仅 24 条可判定且近九成未到期，暂不具参考价值", fontsize=9.5, color=MUTED)
    save(fig, "fig06-domain-leaders.png")


# =================================================================== F7
PAIRS7 = [
    ("H. G. 威尔斯", "预言", "公开的阴谋", "技术功能推演 → 世界政府构想"),
    ("凯文·凯利", "失控", "必然", "系统规律 → 具体公司与年份"),
    ("瑞·达利欧", "债务危机", "原则：应对变化中的世界秩序", "债务机制 → 历史周期套用指标"),
    ("雷·库兹韦尔", "奇点更近", "奇点临近", "2 年窗口 vs 21 年窗口"),
    ("英国政府科学办公室", "智能基础设施的未来：通向2055的情景", "制造业的未来：英国的新机遇与挑战", "情景与趋势 → 含大量定时断言"),
    ("克里斯·安德森", "长尾理论", "免费", "方向判断 → 固定速率与全称量词"),
    ("纳西姆·塔勒布", "黑天鹅", "反脆弱", "风险结构 → 医学创新铁律"),
    ("塞缪尔·亨廷顿", "第三波", "文明的冲突与世界秩序的重建", "民主化趋势 → 文明取代国家"),
]


SHORT7 = {"原则：应对变化中的世界秩序": "世界秩序", "智能基础设施的未来：通向2055的情景": "智能基础设施2055",
          "制造业的未来：英国的新机遇与挑战": "制造业的未来", "文明的冲突与世界秩序的重建": "文明的冲突"}


def fig7():
    fig = frame("同一作者在不同题材上的差距，往往大于不同作者之间的差距",
                "拥有多部作品的作者：表现较好与较差的作品严格胜率对比", figsize=(12, 7.5))
    ax = fig.add_axes([0.20, 0.13, 0.46, 0.69])
    idx = {r["书名"]: r for r in rows}
    for i, (author, good, bad, why) in enumerate(PAIRS7):
        g, b = idx[good], idx[bad]
        gv, bv = pct(g["严格胜率"]), pct(b["严格胜率"])
        ax.plot([bv, gv], [i, i], color=GREY, lw=3, zorder=1)
        ax.scatter(gv, i, s=200, color=FOREST, zorder=3)
        ax.scatter(bv, i, s=200, color=TERRA, zorder=3)
        ax.text(gv + 2, i - 0.25, f"《{SHORT7.get(good, good)}》{gv:.0f}%", fontsize=9.5, color=FOREST, va="center")
        ax.text(bv - 2, i + 0.25, f"《{SHORT7.get(bad, bad)}》{bv:.0f}%", fontsize=9.5, color=TERRA, va="center", ha="right")
        fig.text(0.73, 0.82 - (i + 0.5) * (0.69 / len(PAIRS7)), why, fontsize=10.5, color=BODY, va="center")
    ax.set_yticks(range(len(PAIRS7))); ax.set_yticklabels([p[0] for p in PAIRS7], fontsize=12)
    ax.set_ylim(len(PAIRS7) - 0.5, -0.5)
    ax.set_xlim(-14, 88); ax.set_xlabel("严格胜率 %")
    ax.xaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    fig.text(0.73, 0.845, "差异来源", fontsize=12, fontweight="bold", color=COBALT)
    fig.text(0.45, 0.025, "注：达利欧《债务危机》仅 7 条可判定；库兹韦尔《奇点更近》近九成未到期。", fontsize=9.5, color=MUTED)
    save(fig, "fig07-same-author.png")


# =================================================================== F8
def fig8():
    fig = frame("写明期限的预测错误率更高，这一规律在七个领域均成立",
                "各领域中“原文写明期限”与“只给方向未写期限”两类预测的错误率对比")
    ax = fig.add_axes([0.17, 0.17, 0.55, 0.64])
    data = []
    for d, short in DOMAIN_SHORT.items():
        rs = [r for r in rows if r["领域"] == d]
        ne = sum(r["写明时间可判定数"] for r in rs)
        ni = sum(r["隐含窗口可判定数"] for r in rs)
        we = sum(r["写明时间可判定数"] * (pct(r["写明时间错误率"]) or 0) / 100 for r in rs)
        wi = sum(r["隐含窗口可判定数"] * (pct(r["隐含窗口错误率"]) or 0) / 100 for r in rs)
        data.append((short, we / ne * 100, wi / ni * 100, ne, ni))
    data.sort(key=lambda t: t[1] - t[2], reverse=True)
    for i, (lab, e, m, ne, ni) in enumerate(data):
        ax.plot([m, e], [i, i], color=GREY, lw=2.5, zorder=1)
        ax.scatter(m, i, s=160, color=COBALT, zorder=3)
        ax.scatter(e, i, s=160, color=TERRA, zorder=3)
        ax.text(e + 1.3, i, f"{e:.1f}%", va="center", color=TERRA, fontsize=10.5)
        ax.text(m - 1.3, i, f"{m:.1f}%", va="center", ha="right", color=COBALT, fontsize=10.5)
    ax.set_yticks(range(len(data))); ax.set_yticklabels([d[0] for d in data], fontsize=12)
    ax.invert_yaxis(); ax.set_xlim(-2, 56); ax.set_xlabel("错误率 %")
    ax.xaxis.grid(True, color=GRID); ax.set_axisbelow(True)
    ax.scatter([], [], s=110, color=TERRA, label="写明期限")
    ax.scatter([], [], s=110, color=COBALT, label="只给方向")
    ax.legend(loc="lower right", frameon=False, fontsize=11)
    # side panel: case
    box = fig.add_axes([0.75, 0.20, 0.22, 0.55]); box.axis("off")
    box.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.02", fc="#FCFBF8", ec=GREY))
    box.text(0.08, 0.90, "典型案例", fontsize=12, fontweight="bold", color=COBALT, transform=box.transAxes)
    box.text(0.08, 0.80, "UK GO-Science\n《制造业的未来》(2013)", fontsize=11, color=INK, va="top", transform=box.transAxes)
    box.text(0.08, 0.56, "只给方向", fontsize=10.5, color=COBALT, transform=box.transAxes)
    box.text(0.08, 0.44, "3.7%", fontsize=24, fontweight="bold", color=COBALT, transform=box.transAxes)
    box.text(0.08, 0.30, "写死年份", fontsize=10.5, color=TERRA, transform=box.transAxes)
    box.text(0.08, 0.18, "56.0%", fontsize=24, fontweight="bold", color=TERRA, transform=box.transAxes)
    box.text(0.08, 0.05, "如“金砖四国 2015 年超美国”", fontsize=9.5, color=MUTED, transform=box.transAxes)
    fig.text(0.045, 0.06, "全库：写明期限错误率 17.9%，只给方向 12.3%。但有产能、建设周期核算支撑时，"
             "写明期限照样准（IEA 53.3%、米尔斯海默 62.5%）。", fontsize=10, color=BODY)
    save(fig, "fig08-explicit-vs-implicit.png")


# =================================================================== F9
METHODS = [  # name, decided, strict, direction, error  (panoramic-report §4)
    ("地缘格局 / 权力平衡", 419, 40.3, 47.5, 13.1),
    ("人口 / 资源 / 生态约束账本", 87, 34.5, 56.3, 8.1),
    ("趋势外推 / 定量预测", 3063, 34.8, 51.5, 16.6),
    ("其他综合定性", 1169, 29.9, 55.1, 8.7),
    ("制度结构 / 激励", 42, 28.6, 59.5, 16.7),
    ("社会心理 / 观念变迁", 62, 27.4, 51.6, 4.8),
    ("经济周期 / 金融结构", 138, 26.8, 45.6, 15.2),
    ("技术曲线 / 成本扩散", 127, 26.0, 66.9, 10.2),
    ("历史类比 / 长周期归纳", 254, 23.6, 58.7, 7.9),
    ("条件情景 / 风险推演", 194, 22.2, 51.0, 9.3),
]


def fig9():
    fig = frame("约束账本兼顾较高胜率与低错误；单纯趋势外推样本最多，错误率也最高",
                "按推理方法聚类的表现（同一预测可归入多类）：横轴错误率，纵轴严格胜率，气泡大小为可判定条数")
    ax = fig.add_axes([0.08, 0.16, 0.88, 0.66])
    for name, n, s, d, e in METHODS:
        col = FOREST if (s >= 34 and e <= 14) else (TERRA if e >= 15 else COBALT)
        ax.scatter(e, s, s=max(n, 40) * 1.1, color=col, alpha=0.55, edgecolor="white", lw=1)
        off = (10, -12) if name.startswith("条件情景") else ((10, 6) if name.startswith("历史类比") else (10, 0))
        ax.annotate(f"{name}\n胜率 {s}% · 错误 {e}% · n={n:,}", (e, s), xytext=off,
                    textcoords="offset points", fontsize=9.5, va="center", color=INK)
    ax.set_xlim(3, 21); ax.set_ylim(19, 44)
    ax.set_xlabel("错误率 %（越靠左越少出错）"); ax.set_ylabel("严格胜率 %（越靠上越常完全命中）")
    ax.grid(True, color=GRID); ax.set_axisbelow(True)
    ax.text(3.4, 43, "↖ 理想区域：命中多、错误少", fontsize=12, color=FOREST, fontweight="bold")
    fig.text(0.045, 0.06, "注：方法标签 69.2% 为研究者归纳、24.1% 为作者明示；反映相关性而非因果。",
             fontsize=9.5, color=MUTED)
    save(fig, "fig09-methods.png")


# =================================================================== F10
FAILS = [  # curated-330 compendium Part B tallies
    ("方向正确，但年份或量词过硬", 26, "“边际成本每年减半”“2015 年金砖超美国”\n“2026 年谷歌主营不再是搜索”"),
    ("忽略行动者绕行与政策反制", 9, "镍禁令被中国与印尼产能对冲；美洲鹤因保护立法恢复"),
    ("忽略替代供给与技术跃迁", 7, "杰文斯：煤用完前不会有更强替代能源；凯恩斯漏算美洲小麦"),
    ("把阶段性顺风外推为直线", 5, "费雪：战后通胀将持续；达利欧：缺勤问题“只会恶化”"),
    ("跨层跳跃", 3, "戴维：航空将消灭战争；蒂尔：计算机不与人类争夺电力"),
]


def fig10():
    fig = frame("大师失误中占比最高的，是方向正确、但数字或年份写得过硬",
                "50 条代表性错误按失误模式归类：第一类属于“精度失准”，其余四类才是方向或机制层面的误判")
    ax = fig.add_axes([0.28, 0.17, 0.30, 0.60])
    for i, (lab, v, ex) in enumerate(FAILS):
        col = AMBER if i == 0 else TERRA
        ax.barh(i, v, color=col, height=0.62)
        ax.text(v + 0.6, i, f"{v} 条 · {v / 50:.0%}", va="center", fontsize=12,
                color=AMBER if i == 0 else TERRA, fontweight="bold" if i == 0 else None)
        fig.text(0.62, 0.77 - (i + 0.5) * 0.60 / len(FAILS), ex, fontsize=10.5, color=BODY,
                 va="center", wrap=True)
    ax.set_yticks(range(len(FAILS))); ax.set_yticklabels([f[0] for f in FAILS], fontsize=12)
    ax.invert_yaxis(); ax.set_xlim(0, 34); ax.xaxis.set_visible(False)
    ax.spines["bottom"].set_visible(False)
    fig.text(0.62, 0.795, "典型案例", fontsize=12, fontweight="bold", color=COBALT)
    fig.text(0.045, 0.095, "第一类的典型情形：中美竞争加剧、数字产品成本下降、AI 重塑搜索等方向判断成立，失误在于具体年份、速率或“几乎全部”等量词。",
             fontsize=10.5, color=BODY)
    fig.text(0.045, 0.06, "自检信号：凡出现“无论如何都必将”“永远不会”“几乎全部”“到某年彻底取代”，应先确认是否有核算支撑。",
             fontsize=10.5, color=TERRA)
    save(fig, "fig10-failure-modes.png")


# =================================================================== F11
LABELS11 = {  # title: (label, tx, ty, ha)
    "法国革命论": ("伯克《法国革命论》", 17.5, 26.5, "left"),
    "智能基础设施的未来：通向2055的情景": ("UK GO-Science《智能基础设施2055》", 45, 25, "right"),
    "大国政治的悲剧": ("米尔斯海默《大国政治的悲剧》", -1, 24, "right"),
    "英语的未来？（The Future of English? A guide to forecasting the popularity of the English language in the 21st century）": ("Graddol《英语的未来？》", 4, 20.5, "right"),
    "必然": ("凯文·凯利《必然》", -19, 21, "center"),
    "历史的终结与最后的人": ("福山《历史的终结》", -11, 18.5, "center"),
    "人工智能时代与人类未来": ("基辛格等《人工智能时代》", -6, 13, "right"),
    "生命3.0": ("泰格马克《生命3.0》", -3, 17, "right"),
    "亚洲的21世纪": ("马凯硕《亚洲的21世纪》", -26, 9, "center"),
    "大棋局": ("布热津斯基《大棋局》", 9, 9.5, "left"),
    "煤炭问题：关于国家进步与煤矿可能耗尽的探究": ("杰文斯《煤炭问题》", 26, 20, "left"),
    "后美国世界": ("扎卡利亚《后美国世界》", 27, 3, "left"),
    "奇点临近": ("库兹韦尔《奇点临近》", -30, -22.5, "center"),
    "注定一战": ("艾利森《注定一战》", -17, -12.5, "left"),
}


def fig11():
    fig = frame("方向判断与完全命中是两种能力：左上象限的作者方向极准，只是终点尚未兑现",
                "每个点为一部作品（可判定 ≥ 15 条）。横轴：严格胜率超出同档多少；纵轴：方向命中率（正确 + 趋势符合）超出同档多少",
                figsize=(12, 8))
    ax = fig.add_axes([0.08, 0.10, 0.88, 0.72])
    ax.axhline(0, color=MUTED, lw=1); ax.axvline(0, color=MUTED, lw=1)
    ax.axhspan(0, 30, xmin=0, xmax=36 / 82, color=COBALT, alpha=0.05, zorder=0)
    for r in rows:
        x, y = pct(r["同档超额严格胜率_pp"]), pct(r["同档超额方向命中率_pp"])
        if x is None or y is None or r["可判定数"] < 15:
            continue
        if y > 0 and x < 0:
            col = COBALT
        elif y > 0:
            col = FOREST
        elif x < 0:
            col = TERRA
        else:
            col = GREY
        ax.scatter(x, y, s=r["可判定数"] * 2.2 + 20, color=col, alpha=0.7, edgecolor="white", lw=0.8)
        if r["书名"] in LABELS11:
            lab, tx, ty, ha = LABELS11[r["书名"]]
            far = abs(tx - x) > 3 or abs(ty - y) > 2
            ax.annotate(lab, (x, y), xytext=(tx, ty), fontsize=9.5, color=INK, ha=ha, va="center",
                        arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7) if far else None)
    ax.set_xlim(-36, 46); ax.set_ylim(-36, 30)
    ax.set_xlabel("同档超额严格胜率（百分点）"); ax.set_ylabel("同档超额方向命中率（百分点）")
    ax.grid(True, color=GRID); ax.set_axisbelow(True)
    ax.text(-35, 28, "方向判断强，但少有完全兑现", color=COBALT, fontsize=13, fontweight="bold")
    ax.text(45, 28, "方向与终点都准", color=FOREST, fontsize=13, fontweight="bold", ha="right")
    ax.text(-35, -34, "方向与终点都弱于同档", color=TERRA, fontsize=12, fontweight="bold")
    save(fig, "fig11-direction-vs-strict.png")


# =================================================================== F12
SHORT12 = {
    "法国革命论": "伯克《法国革命论》", "煤炭问题：关于国家进步与煤矿可能耗尽的探究": "杰文斯《煤炭问题》",
    "航空器：战争与和平中的发展及其商业未来": "戴维《航空器》",
    "智能基础设施的未来：通向2055的情景": "UK GO-Science《智能基础设施2055》",
    "大国政治的悲剧": "米尔斯海默《大国政治的悲剧》", "民主的理想与现实": "麦金德《民主的理想与现实》",
    "增长的极限": "梅多斯《增长的极限》",
    "英语的未来？（The Future of English? A guide to forecasting the popularity of the English language in the 21st century）": "Graddol《英语的未来？》",
    "经合组织数字经济展望2024（第二卷）：加强连接、创新与信任": "OECD《数字经济展望2024》",
    "世界发展报告2023：移民、难民与社会（World Development Report 2023: Migrants, Refugees, and Societies）": "世界银行《WDR 2023：移民》",
    "黑人的灵魂": "杜波依斯《黑人的灵魂》", "生命3.0": "泰格马克《生命3.0》", "预言": "威尔斯《预言》",
    "即将到来的事物：对战后的预测": "威尔斯《即将到来的事物》",
    "回到教育的未来：经合组织的四种学校教育情景": "OECD《回到教育的未来》",
    "必然": "凯文·凯利《必然》", "历史的终结与最后的人": "福山《历史的终结》",
    "下一步：经济世界联邦计划": "Nearing《下一步》",
    "人工智能时代与人类未来": "基辛格等《人工智能时代》", "大棋局": "布热津斯基《大棋局》",
}


def fig12():
    fig = frame("方向判断最强的 20 部作品：不少作者的优势主要来自“趋势符合”",
                "按同档超额方向命中率排序（可判定 ≥ 15 条）。条形长度为方向命中率，深色为完全命中，浅色为趋势符合",
                figsize=(12, 9))
    ax = fig.add_axes([0.30, 0.08, 0.60, 0.76])
    rs = [r for r in rows if r["可判定数"] >= 15 and pct(r["同档超额方向命中率_pp"]) is not None]
    rs.sort(key=lambda r: pct(r["同档超额方向命中率_pp"]), reverse=True)
    rs = rs[:20]
    for i, r in enumerate(rs):
        n = r["可判定数"]
        st, tr = r["正确"] / n * 100, r["趋势符合"] / n * 100
        ax.barh(i, st, color=FOREST, height=0.68)
        ax.barh(i, tr, left=st, color="#9DBBA7", height=0.68)
        ax.text(st + tr + 1, i, f"{st + tr:.0f}%  （超同档 {pct(r['同档超额方向命中率_pp']):+.0f}）  错误 {r['错误率']}",
                va="center", fontsize=9.5, color=BODY)
    ax.set_yticks(range(len(rs)))
    ax.set_yticklabels([f"{SHORT12.get(r['书名'], r['书名'][:14])}（{r['出版年']}）" for r in rs], fontsize=10.5)
    ax.invert_yaxis(); ax.set_xlim(0, 135); ax.xaxis.set_visible(False)
    ax.spines["bottom"].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=FOREST, label="完全命中（正确）"), Patch(color="#9DBBA7", label="趋势符合")],
              loc="upper right", frameon=False, fontsize=11, bbox_to_anchor=(1.08, 1.06))
    save(fig, "fig12-direction-leaders.png")


# =================================================================== F13
def fig13():
    fig = frame("政治家与科技思想家的严格胜率不高，但方向命中率仅次于智库",
                "六类作者全部可判定预测的结果构成，按方向命中率（正确 + 趋势符合）从高到低排列")
    ax = fig.add_axes([0.20, 0.13, 0.76, 0.62])
    data = []
    for t, short in TYPE_SHORT.items():
        rs = [r for r in rows if r["作者类型"] == t]
        n = sum(r["可判定数"] for r in rs)
        parts = [sum(r[k] for r in rs) / n * 100 for k in ("正确", "趋势符合", "部分符合", "错误")]
        data.append((short, parts))
    data.sort(key=lambda d: d[1][0] + d[1][1], reverse=True)
    cols = [FOREST, "#9DBBA7", "#D8C3A0", TERRA]
    names = ["正确", "趋势符合", "部分符合", "错误"]
    for i, (lab, parts) in enumerate(data):
        left = 0
        for j, v in enumerate(parts):
            ax.barh(i, v, left=left, color=cols[j], height=0.62)
            if v > 4:
                ax.text(left + v / 2, i, f"{v:.0f}", ha="center", va="center", fontsize=10.5,
                        color="white" if j in (0, 3) else INK)
            left += v
        ax.text(-1.5, i + 0.38, f"方向命中 {parts[0] + parts[1]:.1f}%", ha="right", fontsize=9.5,
                color=FOREST, va="center")
    ax.axvline(52.5, color=INK, lw=1, ls=":")
    ax.text(52.5, -0.65, "全库方向命中率 52.5%", fontsize=9.5, ha="center", color=INK)
    ax.set_yticks(range(len(data))); ax.set_yticklabels([d[0] for d in data], fontsize=12)
    ax.invert_yaxis(); ax.set_xlim(0, 100); ax.set_xlabel("占可判定预测 %")
    for j, nm in enumerate(names):
        fig.text(0.20 + j * 0.12, 0.81, "■", color=cols[j], fontsize=14, va="center")
        fig.text(0.215 + j * 0.12, 0.81, nm, fontsize=11, va="center", color=BODY)
    save(fig, "fig13-author-type-composition.png")


# =================================================================== F14
def fig14():
    fig = frame("写明期限并不降低方向判断的准确度，变化的是结果的结算方式",
                "原文写明期限与只给方向两类预测的结果构成：方向命中率几乎相同（53.0% vs 52.2%）")
    ax = fig.add_axes([0.20, 0.30, 0.76, 0.45])
    groups = [("写明期限\n可判定 1,199", [292, 343, 349, 215]),
              ("只给方向\n可判定 3,833", [1383, 619, 1360, 471])]
    cols = [FOREST, "#9DBBA7", "#D8C3A0", TERRA]
    names = ["正确", "趋势符合", "部分符合", "错误"]
    for i, (lab, vals) in enumerate(groups):
        n = sum(vals); left = 0
        for j, v in enumerate(vals):
            w = v / n * 100
            ax.barh(i, w, left=left, color=cols[j], height=0.55)
            ax.text(left + w / 2, i, f"{names[j]}\n{w:.1f}%", ha="center", va="center", fontsize=11,
                    color="white" if j in (0, 3) else INK)
            left += w
        d = (vals[0] + vals[1]) / n * 100
        ax.annotate("", xy=(d, i - 0.36), xytext=(0, i - 0.36),
                    arrowprops=dict(arrowstyle="<->", color=FOREST, lw=1.4))
        ax.text(d / 2, i - 0.45, f"方向命中 {d:.1f}%", ha="center", va="bottom", fontsize=10.5,
                color=FOREST, fontweight="bold")
    ax.set_yticks([0, 1]); ax.set_yticklabels([g[0] for g in groups], fontsize=12)
    ax.invert_yaxis(); ax.set_xlim(0, 100); ax.set_ylim(1.5, -0.75); ax.xaxis.set_visible(False)
    ax.spines["bottom"].set_visible(False)
    fig.text(0.20, 0.20, "解读：写明期限的预测中，“完全命中”更少、“趋势符合”更多——方向已在兑现，但尚未在原定时间内达到终点；",
             fontsize=11, color=BODY)
    fig.text(0.20, 0.16, "到期未达终点的部分则被记为错误。因此，期限写得过硬是精度问题，不等于方向判断失误。",
             fontsize=11, color=BODY)
    save(fig, "fig14-explicit-composition.png")


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13, fig14):
        f()
