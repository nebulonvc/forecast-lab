#!/usr/bin/env python3
"""Zero-dependency Model Context Protocol (MCP) Server for Forecast Lab Method Optimization.

Implements the official MCP stdio JSON-RPC 2.0 specification using only Python 3.11+
standard library modules, so any Agent terminal (Claude Code, Antigravity, Cursor,
Codex CLI, Windsurf, Cline, Gemini CLI, Zed) can connect out-of-the-box without
creating virtual environments or installing third-party packages.

Run directly via MCP host configuration:
    python3 toolkit/forecast_mcp.py
Or self-test from terminal:
    python3 toolkit/forecast_mcp.py --self-test
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import forecast_optimizer as fo  # noqa: E402
import periodic_tracker as pt  # noqa: E402
import pipeline as pl  # noqa: E402

SERVER_NAME = "forecast-lab-optimizer"
SERVER_VERSION = "1.0.0"
SUPPORTED_PROTOCOLS = ("2025-06-18", "2025-03-26", "2024-11-05")


TOOLS_SPEC: list[dict[str, Any]] = [
    {
        "name": "optimize_forecast",
        "description": (
            "Audit a draft prediction and optimize its forecasting method, counter-lens, and commitment "
            "hardness using Forecast Lab's Super-Learner trained on 146 works (10,745 predictions, "
            "7,522 decided verdicts, 2,942 non-forecasts, and t_0 macro-historical regimes)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "statement": {
                    "type": "string",
                    "description": "The draft prediction or intuition to audit and optimize.",
                },
                "domain": {
                    "type": "string",
                    "description": "Domain (e.g., AI与奇点前沿, 地缘政治与国际秩序, 宏观经济、金融与市场, 科技、商业与产业颠覆, 人口、能源、资源与生态, 社会结构、制度、文化与教育).",
                },
                "horizon": {
                    "type": "string",
                    "description": "Target time horizon text, e.g. '到2030年底' or '2026-2029'.",
                },
                "target_years": {
                    "type": "number",
                    "description": "Explicit numeric horizon in years from current_year.",
                },
                "scope": {
                    "type": "string",
                    "description": "Statistical denominator, measurement scope, and authoritative data source.",
                },
                "condition_text": {
                    "type": "string",
                    "description": "Triggering premise or conditional scenario A.",
                },
                "method": {
                    "type": "string",
                    "description": "Current reasoning method if already chosen.",
                },
                "counter_lens": {
                    "type": "string",
                    "description": "Current counter-lens or falsification check if already chosen.",
                },
                "leading_indicators": {
                    "type": "string",
                    "description": "Observable quarterly/semi-annual leading indicators.",
                },
                "falsification": {
                    "type": "string",
                    "description": "Explicit quantitative threshold or condition that falsifies the forecast.",
                },
                "forecaster_stance": {
                    "type": "string",
                    "description": "Baseline stance of the raw draft (default: 科技商业思想家与产业实践者).",
                },
                "output_format": {
                    "type": "string",
                    "enum": ["both", "json", "markdown"],
                    "description": "Output representation format (default: both).",
                },
            },
            "required": ["statement"],
        },
    },
    {
        "name": "query_reference_class",
        "description": (
            "Query Hierarchical Empirical Bayes base rates, stratum sample sizes, top benchmark books, "
            "and matched curated exemplars/failures (H001-H100, M01-M50, F1-F6) for a domain and horizon."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Target forecast domain."},
                "horizon_years": {"type": "number", "description": "Evaluation horizon in years (default: 10)."},
                "is_explicit": {"type": "boolean", "description": "Whether the forecast specifies an explicit date/year (default: true)."},
                "forecaster_stance": {"type": "string", "description": "Forecaster archetype (default: 国际机构与政府智库)."},
                "keyword": {"type": "string", "description": "Optional topic keyword to match historical precedents."},
            },
            "required": ["domain"],
        },
    },
    {
        "name": "bayesian_update_forecast",
        "description": (
            "Perform a three-axis (event / mechanism / time) damped Log-Odds Bayesian posterior update "
            "on a forecast given newly observed support, counter, or boundary evidence items."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "statement": {"type": "string", "description": "Forecast statement (used to derive prior if prior_decided_probs is omitted)."},
                "domain": {"type": "string", "description": "Forecast domain."},
                "horizon_years": {"type": "number", "description": "Forecast horizon in years."},
                "prior_decided_probs": {
                    "type": "object",
                    "description": "Optional 4-class prior dict with keys 正确, 趋势符合, 部分符合, 错误.",
                },
                "evidence_items": {
                    "type": "array",
                    "description": "List of evidence items with relation, source_tier, axis, and summary.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "relation": {"type": "string", "enum": ["support", "counter", "boundary"]},
                            "source_tier": {
                                "type": "string",
                                "enum": ["official_stats", "institutional", "filing", "academic", "media"],
                            },
                            "axis": {"type": "string", "enum": ["event", "mechanism", "time"]},
                            "summary": {"type": "string"},
                        },
                        "required": ["relation", "summary"],
                    },
                },
            },
            "required": ["evidence_items"],
        },
    },
    {
        "name": "audit_forecast_ledger",
        "description": (
            "Batch-audit all forecasts in a personal ledger directory (default: my-forecasts), "
            "reporting operationalizability scores, active noise traps, and optimal method upgrades."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "ledger_path": {
                    "type": "string",
                    "description": "Relative or absolute path to ledger directory (default: my-forecasts).",
                }
            },
        },
    },
    {
        "name": "register_optimized_forecast",
        "description": (
            "Freeze and register a validated, optimized forecast card into my-forecasts (or custom ledger) "
            "and run deterministic SHA-256 & schema verification via pipeline.py."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "claim_id": {"type": "string", "description": "Unique forecast slug ID, e.g. '2026-us-grid-storage'."},
                "domain": {"type": "string", "description": "Forecast domain."},
                "statement": {"type": "string", "description": "Frozen operationalized forecast statement."},
                "horizon": {"type": "string", "description": "Explicit target window, e.g. '2026-2030'."},
                "scope": {"type": "string", "description": "Denominator, exclusions, and authoritative data source."},
                "method": {"type": "string", "description": "Primary Signal Method lens name (e.g., 约束账本法)."},
                "method_derivation": {
                    "type": "string",
                    "description": "Explicit step-by-step derivation explaining HOW the chosen prediction method derives this forecast (stock/flow ledger, veto incentives, cost threshold, etc.).",
                },
                "counter_lens": {"type": "string", "description": "Paired Counter-Lens check and neutralized blind spots."},
                "leading_indicators": {"type": "string", "description": "2-3 observable leading indicators."},
                "falsification": {"type": "string", "description": "Explicit falsification threshold."},
                "condition_text": {"type": "string", "description": "Optional triggering premise."},
                "ledger_path": {"type": "string", "description": "Target ledger directory (default: my-forecasts)."},
            },
            "required": [
                "claim_id",
                "domain",
                "statement",
                "horizon",
                "scope",
                "method",
                "counter_lens",
                "leading_indicators",
                "falsification",
            ],
        },
    },
    {
        "name": "evaluate_tech_differentiation",
        "description": (
            "Test 'Is This New Technology Really Different This Time?' against 150 years of historical "
            "technology diffusion S-curves (Comin-Hobijn NBER CHAT, Bass 1969, Paul David Dynamo Paradox), "
            "identifying the physical/institutional friction layer (1 to 4), stock-vs-flow inertia, "
            "calibrated penetration range, and exact real-time bottleneck parameters to fetch."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "statement": {"type": "string", "description": "Technology adoption or disruption forecast statement."},
                "domain": {"type": "string", "description": "Optional domain hint."},
                "scope": {"type": "string", "description": "Denominator scope (new sales flow vs installed fleet/headcount stock)."},
                "horizon_years": {"type": "number", "description": "Target horizon in years."},
                "current_penetration": {"type": "number", "description": "Current baseline penetration fraction in (0, 1), e.g. 0.04."},
                "target_penetration": {"type": "number", "description": "Target penetration fraction in (0, 1), e.g. 0.50."},
                "is_stock_scope": {"type": "boolean", "description": "True if claiming installed-stock or total headcount replacement."},
            },
            "required": ["statement"],
        },
    },
    {
        "name": "get_optimizer_benchmark",
        "description": (
            "Return the 5-fold Out-of-Book Grouped Cross-Validation benchmark across 7 academic models, "
            "Super-Learner ensemble weights, and Cochran-Mantel-Haenszel stratified causal method effects."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
]

RESOURCES_SPEC: list[dict[str, Any]] = [
    {
        "uri": "forecast-lab://benchmark/out-of-book-cv",
        "name": "Out-of-Book 5-Fold Cross-Validation Benchmark (10,745 Forecasts)",
        "description": "Empirical proper scoring rule comparison (Brier, LogLoss, RPS, ECE) across 7 academic models.",
        "mimeType": "application/json",
    },
    {
        "uri": "forecast-lab://methodology/signal-lenses-and-traps",
        "name": "6 Signal Method Archetypes & 5 Noise Failure Traps Catalog",
        "description": "Structured taxonomy with empirical CMH controlled percentage-point effects and exemplars.",
        "mimeType": "application/json",
    },
    {
        "uri": "forecast-lab://atlas/historical-tech-diffusion",
        "name": "Historical Technology Diffusion & 4-Layer Bottleneck Atlas (1882-2025)",
        "description": "Bass (p, q) diffusion S-curves, 5%->50% flow/stock durations, and bottleneck checklists across 12 tech waves.",
        "mimeType": "application/json",
    },
    {
        "uri": "forecast-lab://ledger/my-forecasts",
        "name": "Active Personal Forecast Ledger Audit (my-forecasts)",
        "description": "Live optimization audit of forecasts registered in my-forecasts/.",
        "mimeType": "application/json",
    },
]

PROMPTS_SPEC: list[dict[str, Any]] = [
    {
        "name": "optimize-my-prediction",
        "description": "Turn a rough intuition or thesis into a data-calibrated, trap-free Forecast Lab prediction card.",
        "arguments": [
            {"name": "draft_idea", "description": "User's raw prediction idea or thesis", "required": True},
            {"name": "domain", "description": "Optional domain hint", "required": False},
        ],
    },
    {
        "name": "quarterly-bayesian-review",
        "description": "Run bidirectional support/counter evidence collection and three-axis Bayesian posterior updating.",
        "arguments": [
            {"name": "ledger_path", "description": "Path to forecast ledger (default: my-forecasts)", "required": False},
        ],
    },
]


class ForecastMCPServer:
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        self._engine: fo.ForecastOptimizerEngine | None = None

    @property
    def engine(self) -> fo.ForecastOptimizerEngine:
        if self._engine is None:
            self._engine = fo.ForecastOptimizerEngine.load(repo_root=self.repo_root)
        return self._engine

    def _resolve_ledger(self, raw_path: str | None) -> Path:
        if not raw_path:
            return (self.repo_root / "my-forecasts").resolve()
        p = Path(raw_path)
        if not p.is_absolute():
            p = (self.repo_root / p).resolve()
        # Prevent path traversal outside repo_root unless explicitly inside repo_root
        return p

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name == "optimize_forecast":
            res = self.engine.optimize_forecast(
                statement=arguments["statement"],
                domain=arguments.get("domain", ""),
                horizon=arguments.get("horizon", ""),
                target_years=arguments.get("target_years"),
                scope=arguments.get("scope", ""),
                condition_text=arguments.get("condition_text", ""),
                method=arguments.get("method", ""),
                counter_lens=arguments.get("counter_lens", ""),
                leading_indicators=arguments.get("leading_indicators", ""),
                falsification=arguments.get("falsification", ""),
                forecaster_stance=arguments.get("forecaster_stance", "科技商业思想家与产业实践者"),
            )
            fmt = arguments.get("output_format", "both")
            contents = []
            if fmt in ("both", "markdown"):
                contents.append({"type": "text", "text": fo.format_optimization_markdown(res)})
            if fmt in ("both", "json"):
                contents.append({"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=2)})
            return {"content": contents, "isError": False}

        if name == "query_reference_class":
            res = self.engine.query_reference_class(
                domain=arguments["domain"],
                horizon_years=float(arguments.get("horizon_years", 10.0)),
                is_explicit=bool(arguments.get("is_explicit", True)),
                forecaster_stance=arguments.get("forecaster_stance", "国际机构与政府智库"),
                keyword=arguments.get("keyword", ""),
            )
            return {"content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=2)}], "isError": False}

        if name == "bayesian_update_forecast":
            res = self.engine.bayesian_update(
                prior_decided_probs=arguments.get("prior_decided_probs"),
                statement=arguments.get("statement", ""),
                domain=arguments.get("domain", ""),
                horizon_years=float(arguments.get("horizon_years", 5.0)),
                evidence_items=arguments["evidence_items"],
            )
            return {"content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=2)}], "isError": False}

        if name == "audit_forecast_ledger":
            ledger_dir = self._resolve_ledger(arguments.get("ledger_path"))
            res = self.engine.audit_ledger(ledger_dir)
            return {"content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=2)}], "isError": False}

        if name == "register_optimized_forecast":
            ledger_dir = self._resolve_ledger(arguments.get("ledger_path"))
            opt_check = self.engine.optimize_forecast(
                statement=arguments["statement"],
                domain=arguments["domain"],
                horizon=arguments["horizon"],
                scope=arguments["scope"],
                condition_text=arguments.get("condition_text", ""),
                method=arguments["method"],
                counter_lens=arguments["counter_lens"],
                leading_indicators=arguments["leading_indicators"],
                falsification=arguments["falsification"],
                forecaster_stance="国际机构与政府智库",
            )
            b4 = opt_check["baseline_evaluation"]["probs_decided_4class"]
            base_rate_str = (
                f"SuperLearner校准先验: 严格胜率 {b4['正确']:.1%}, "
                f"方向命中 {(b4['正确'] + b4['趋势符合']):.1%}, 错误风险 {b4['错误']:.1%}"
            )
            deriv = (arguments.get("method_derivation") or "").strip()
            full_method_text = f"{arguments['method'].strip()}｜推导链：{deriv}" if deriv else arguments["method"].strip()
            rec = pt.add_forecast(
                ledger_dir,
                claim_id=arguments["claim_id"],
                domain=arguments["domain"],
                statement=arguments["statement"],
                horizon=arguments["horizon"],
                scope=arguments["scope"],
                method=full_method_text,
                counter_lens=arguments["counter_lens"],
                leading_indicators=arguments["leading_indicators"],
                falsification=arguments["falsification"],
                condition_text=arguments.get("condition_text", ""),
                base_rate=base_rate_str,
            )
            pl.ROOT = ledger_dir
            pl.check()
            pl.assessment_report()
            payload = {
                "status": "registered_and_verified",
                "claim_id": rec["id"],
                "card_path": str(ledger_dir / rec["review_metadata"]["card_path"]),
                "calibrated_prior": b4,
            }
            return {"content": [{"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=2)}], "isError": False}

        if name == "evaluate_tech_differentiation":
            res = self.engine.evaluate_tech_differentiation(
                statement=arguments["statement"],
                domain=arguments.get("domain", ""),
                scope=arguments.get("scope", ""),
                horizon_years=arguments.get("horizon_years"),
                current_penetration=arguments.get("current_penetration"),
                target_penetration=arguments.get("target_penetration"),
                is_stock_scope=arguments.get("is_stock_scope"),
            )
            return {"content": [{"type": "text", "text": json.dumps(res, ensure_ascii=False, indent=2)}], "isError": False}

        if name == "get_optimizer_benchmark":
            bpath = self.repo_root / "datasets" / "optimization_benchmark.json"
            if bpath.is_file():
                data = json.loads(bpath.read_text(encoding="utf-8"))
            else:
                _, data = fo.train_and_benchmark(repo_root=self.repo_root, save=True)
            return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=2)}], "isError": False}

        raise ValueError(f"Unknown tool: {name}")

    def read_resource(self, uri: str) -> dict[str, Any]:
        if uri == "forecast-lab://benchmark/out-of-book-cv":
            bpath = self.repo_root / "datasets" / "optimization_benchmark.json"
            text = bpath.read_text(encoding="utf-8") if bpath.is_file() else "{}"
            return {"contents": [{"uri": uri, "mimeType": "application/json", "text": text}]}

        if uri == "forecast-lab://methodology/signal-lenses-and-traps":
            payload = {
                "signal_methods": fo.SIGNAL_METHODS,
                "noise_traps": fo.NOISE_TRAPS,
                "cmh_empirical_effects": self.engine.cmh_effects,
            }
            return {
                "contents": [
                    {"uri": uri, "mimeType": "application/json", "text": json.dumps(payload, ensure_ascii=False, indent=2)}
                ]
            }

        if uri == "forecast-lab://atlas/historical-tech-diffusion":
            apath = self.repo_root / "datasets" / "historical_tech_diffusion_atlas.json"
            return {"contents": [{"uri": uri, "mimeType": "application/json", "text": apath.read_text(encoding="utf-8")}]}

        if uri == "forecast-lab://ledger/my-forecasts":
            res = self.engine.audit_ledger(self.repo_root / "my-forecasts")
            return {"contents": [{"uri": uri, "mimeType": "application/json", "text": json.dumps(res, ensure_ascii=False, indent=2)}]}

        raise ValueError(f"Unknown resource URI: {uri}")

    def get_prompt(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name == "optimize-my-prediction":
            idea = arguments.get("draft_idea", "")
            dom = arguments.get("domain", "")
            prompt_text = (
                f"用户提出了以下预测想法：\n「{idea}」（领域提示：{dom or '自动识别'}）。\n\n"
                "请严格执行 Forecast Lab 数据驱动优化闭环（铁律：最终交付的预测必须把【预测方法与推导链】完整写出来，绝不只给裸结论或单一概率）：\n"
                "1. 先调用 `optimize_forecast` 工具，获取该草案的样本外校准概率分布、可操作化缺口、命中的高赔率噪音陷阱，以及基于 10,745 条历史预测优选出的最佳「主方法 + 四步推导链 + 反校验透镜 + 承诺硬度」与边际改善幅度。\n"
                "2. 结合返回的成功先例（H编号）与大师翻车反例（M编号），帮用户把原想法收敛为完整的《终局预测卡》，必须显式包含：\n"
                "   - **可核验预测承诺**（主体、对象、量词、含分母可测指标、唯一权威数据源、明确期限）；\n"
                "   - **显式预测方法与四步推导链**（写明采用哪套主方法、基期存量/流量/激励约束怎么算出该结论、配了什么反校验透镜对冲盲区、为何匹配当前承诺硬度）；\n"
                "   - **10,745 库校准先验概率**与**定期领先指标 + 明确证伪阈值**。\n"
                "3. 再次调用 `optimize_forecast` 验证改写后版本的校准严格胜率提升与错误率下降，展示前后对比表；确认后调用 `register_optimized_forecast`（传入 `method_derivation`）冻结入库。"
            )
            return {
                "description": "Data-driven forecast optimization workflow",
                "messages": [{"role": "user", "content": {"type": "text", "text": prompt_text}}],
            }

        if name == "quarterly-bayesian-review":
            ledger = arguments.get("ledger_path", "my-forecasts")
            prompt_text = (
                f"请对 `{ledger}` 账本执行本周期的三轴贝叶斯复盘：\n"
                "1. 先调用 `audit_forecast_ledger` 读取全部在册预测及其领先观测指标。\n"
                "2. 针对每条预测，同时检索公开权威的【支持证据（Support）】与【反面/摩擦证据（Counter）】。\n"
                "3. 调用 `bayesian_update_forecast` 按事件轴（event）、机制轴（mechanism）、时间轴（time）计算阻尼对数赔率后验分布，汇报信号跃迁。"
            )
            return {
                "description": "Quarterly three-axis Bayesian forecast review",
                "messages": [{"role": "user", "content": {"type": "text", "text": prompt_text}}],
            }

        raise ValueError(f"Unknown prompt: {name}")

    def handle_request(self, msg: dict[str, Any]) -> dict[str, Any] | None:
        """Process a single JSON-RPC 2.0 message. Returns None for notifications."""
        method = msg.get("method", "")
        msg_id = msg.get("id")
        params = msg.get("params") or {}

        # Notifications have no 'id' field -> must not emit a response
        if "id" not in msg:
            return None

        try:
            if method == "initialize":
                client_proto = params.get("protocolVersion", "2025-03-26")
                proto = client_proto if client_proto in SUPPORTED_PROTOCOLS else "2025-03-26"
                result = {
                    "protocolVersion": proto,
                    "capabilities": {
                        "tools": {"listChanged": False},
                        "resources": {"subscribe": False, "listChanged": False},
                        "prompts": {"listChanged": False},
                    },
                    "serverInfo": {
                        "name": SERVER_NAME,
                        "version": SERVER_VERSION,
                    },
                    "instructions": (
                        "Use optimize_forecast before drafting or registering any prediction to calibrate "
                        "probabilities against 10,745 historical forecasts and select the optimal reasoning method."
                    ),
                }
                return {"jsonrpc": "2.0", "id": msg_id, "result": result}

            if method == "ping":
                return {"jsonrpc": "2.0", "id": msg_id, "result": {}}

            if method == "tools/list":
                return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SPEC}}

            if method == "tools/call":
                tool_name = params.get("name", "")
                tool_args = params.get("arguments") or {}
                try:
                    out = self.call_tool(tool_name, tool_args)
                    return {"jsonrpc": "2.0", "id": msg_id, "result": out}
                except Exception as exc:
                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": f"Tool execution error: {exc}"}],
                            "isError": True,
                        },
                    }

            if method == "resources/list":
                return {"jsonrpc": "2.0", "id": msg_id, "result": {"resources": RESOURCES_SPEC}}

            if method == "resources/read":
                uri = params.get("uri", "")
                return {"jsonrpc": "2.0", "id": msg_id, "result": self.read_resource(uri)}

            if method == "prompts/list":
                return {"jsonrpc": "2.0", "id": msg_id, "result": {"prompts": PROMPTS_SPEC}}

            if method == "prompts/get":
                pname = params.get("name", "")
                pargs = params.get("arguments") or {}
                return {"jsonrpc": "2.0", "id": msg_id, "result": self.get_prompt(pname, pargs)}

            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }
        except Exception as exc:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32603, "message": str(exc)},
            }

    def serve_stdio(self) -> None:
        """Serve MCP over stdin/stdout supporting both newline-delimited JSON-RPC (official MCP spec)
        and Content-Length framed JSON-RPC (legacy clients).
        """
        stdin = sys.stdin.buffer
        stdout = sys.stdout.buffer

        while True:
            line = stdin.readline()
            if not line:
                break
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.lower().startswith(b"content-length:"):
                length = int(stripped.split(b":", 1)[1].strip())
                # Consume remaining headers until blank line
                while True:
                    hdr = stdin.readline()
                    if not hdr or hdr in (b"\r\n", b"\n"):
                        break
                body = stdin.read(length)
                if not body:
                    break
                msg = json.loads(body.decode("utf-8"))
                resp = self.handle_request(msg)
                if resp is not None:
                    payload = json.dumps(resp, ensure_ascii=False).encode("utf-8")
                    header = f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii")
                    stdout.write(header + payload)
                    stdout.flush()
            else:
                msg = json.loads(stripped.decode("utf-8"))
                resp = self.handle_request(msg)
                if resp is not None:
                    payload = (json.dumps(resp, ensure_ascii=False) + "\n").encode("utf-8")
                    stdout.write(payload)
                    stdout.flush()


def run_self_test() -> int:
    srv = ForecastMCPServer()
    init_resp = srv.handle_request({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "self-test", "version": "1.0"}},
    })
    assert init_resp and init_resp["result"]["serverInfo"]["name"] == SERVER_NAME
    tools_resp = srv.handle_request({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    assert tools_resp and len(tools_resp["result"]["tools"]) == 7
    call_resp = srv.handle_request({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "optimize_forecast",
            "arguments": {
                "statement": "到2029年全球人形机器人将完全取代汽车工厂工人。",
                "domain": "AI与奇点前沿",
                "output_format": "json",
            },
        },
    })
    assert call_resp and not call_resp["result"]["isError"]
    parsed = json.loads(call_resp["result"]["content"][0]["text"])
    assert "recommended_optimization" in parsed
    assert parsed["tech_differentiation_audit"]["differentiation_verdict_code"] == "extreme_overreach"
    print(json.dumps({"self_test": "passed", "tools_registered": len(tools_resp["result"]["tools"])}, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Forecast Lab MCP Server (stdio JSON-RPC 2.0)")
    parser.add_argument("--self-test", action="store_true", help="Run offline protocol & tool smoke check and exit")
    args = parser.parse_args(argv)
    if args.self_test:
        return run_self_test()
    ForecastMCPServer().serve_stdio()
    return 0


if __name__ == "__main__":
    sys.exit(main())
