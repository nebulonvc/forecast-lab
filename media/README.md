# 演示视频与动画生成套件（`media/`）

本目录收录了围绕 **132 部著作、8,130 条预测实证复盘** 制作的两部科研档案风双人配音动画视频预览、完整时间轴字幕及可复现生成代码。

> 💡 为保持 Git 仓库轻量高速克隆，两部 1080p 完整高清 MP4 原片（29 MB 与 53 MB）托管于本仓库的 **[GitHub Releases (`v1.0.0`)](https://github.com/nebulonvc/forecast-lab/releases/tag/v1.0.0)**，点击下方链接即可直接下载或播放。

---

## 视频一：《手把手学预测：向 132 部著作里最准的那批人学习》（时长 `06:08`）

![手把手学预测动图预览](previews/video1-tutorial-preview.gif)

- 📥 **[下载 / 观看 1080p 完整高清版 MP4 (29 MB)](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/01-hands-on-forecasting-tutorial.mp4)**
- 📝 **[阅读完整时间轴字幕 (`01-hands-on-forecasting-tutorial.srt`)](subtitles/01-hands-on-forecasting-tutorial.srt)**

### 章节时间轴导览
| 时间点 | 章节主题 | 核心看点 |
| :--- | :--- | :--- |
| `00:00` | 全库成绩单与两条读数底线 | 为什么全库没有全能先知？为什么国际智库（严格胜率 47.0% / 错 6.3%）远胜单线预言家？时间跨度如何决定考卷难度？ |
| `01:20` | 第一步：拆题防偷换 | 主体 + 对象 + 量词 + 指标 + 期限 + 条件；严防“出现 = 普及 = 取代”概念偷换 |
| `01:50` | 第二步：按领域选对老师 | 地缘学扎卡利亚/卡普兰/李光耀，金融学达利欧/塔勒布，产业学克里斯坦森，能源学 IEA/杰文斯，制度学伯克 |
| `02:30` | 第三步：先算硬账本 | 存量、流量、在建产能、成本与买单方（IEA 关键矿产与伯克四本账实例） |
| `02:58` | 第四步：行动者与条件分支 | 拆解 $P(A)$ 与 $P(B \mid A)$，对比 OECD 情景法与霍纳迪忽略立法反制的翻车教训 |
| `03:32` | 第五步：按跨度定承诺硬度 | 0–3 年给排期、5–15 年给情景、15 年以上只押慢结构不押精确年份 |
| `04:08` | 第六步：五大反面清单扫雷 | 遇到“无论如何都必将”“永远不会”直接降权 |
| `04:44` | 第七步 & 完整实战推演 | 事前冻结预测卡 + 事后事件/机制/时间三轴复盘；完整推演 **“2026–2030 美国数据中心用电占比”** |

---

## 视频二：《百大精彩预测 · 五十高手翻车 · 六大领域未来方向全景特辑》（时长 `07:56`）

![百大精彩与未来全景动图预览](previews/video2-panoramic-preview.gif)

- 📥 **[下载 / 观看 1080p 完整高清版 MP4 (53 MB)](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/02-panoramic-330-forecasts.mp4)**
- 📝 **[阅读完整时间轴字幕 (`02-panoramic-330-forecasts.srt`)](subtitles/02-panoramic-330-forecasts.srt)**

### 章节时间轴导览
| 时间点 | 章节主题 | 核心看点 |
| :--- | :--- | :--- |
| `00:00` | 330 条高含金量样本总览 | 从 8,130 条预测严格去重筛出：100 条封神命中 + 50 条大师翻车 + 180 条未来方向（零重叠） |
| `00:25` | Part A：百大精彩预测（`H001–H100`） | 分五组逐页展示麦金德、扎卡利亚、李光耀、杰文斯、塔勒布、克里斯坦森、博斯特罗姆、威尔斯等跨时代高光命中 |
| `02:52` | Part B：五十条大师翻车死因拆解（`M01–M50`） | 为什么超过一半的翻车源于“把方向偷换成硬年份/极端量词”？复盘 IEA、凯恩斯、克里斯坦森、凯文·凯利、彼得·蒂尔失手点 |
| `04:16` | Part C：六大领域 × 30 条未来方向罗盘（`F1–F6`） | 覆盖地缘、宏观金融、科技商业、AI奇点、人口能源、社会制度 180 条演进方向及 **2026–2035 具体领先跟踪指标** |

---

## 复现动画生成脚本（`media/generator/`）

两部视频全部由纯 Python 代码（Pillow 矢量排版渲染 + 双声部神经网络 TTS + `ffmpeg` 合成）自动生成：
- [`generator/sci_theme.py`](generator/sci_theme.py)：科研档案风配色、网格对位标、动态缓动曲线与字幕音频合成公共引擎；
- [`generator/make_video_tutorial.py`](generator/make_video_tutorial.py)：第一部《手把手学预测》生成脚本；
- [`generator/make_video_panoramic.py`](generator/make_video_panoramic.py) + [`generator/curated_330.json`](generator/curated_330.json)：第二部《330 条全景特辑》数据驱动渲染脚本。
