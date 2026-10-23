# Technical checks

Status: incomplete; no paid API calls have been made.

## Completed no-cost checks

- Dataset inventory: 163 MT functions and 425 CM modules from 24 projects.
- CM path resolution and source parsing: 425/425 modules resolved.
- Deterministic CM pilot/sample: 3 disjoint pilot modules, 40 sampled modules, ≤10 modules per project, all eight observed non-empty strata represented.
- Existing CodaMOSA image `pynguin-runner:latest` imports a `model.py` whose SHA-256 matches the retained active source (`4de3e6bde3307809e176912266183874cb0a9c724030bbaced747b45fd62fcd0`).
- CodaMOSA CLI exposes model base URL, model relative URL, maximum search time, assertion generation, and seed controls.
- CoverUp checkpoint writing is atomic and its targeted checkpoint test passes.
- Local proxy unit tests verify both OpenAI/Anthropic usage shapes and credential absence from logs.
- Simulated 8,120-row CodaMOSA/CoverUp subset analysis completes, including mean/median/std, Wilcoxon signed-rank, Holm correction, A12, and bootstrap CI.

## Endpoint probe results (2026-10-22)

- **B1 passed:** request model `auto`, returned model `auto`, HTTP 200, function calling confirmed (`finish_reason=tool_calls`). The provider reported token usage. This verifies interface behavior, not the seller's GPT-5.6 Sol identity claim.
- **B2 blocked:** the configured B2 URL/key is the same SrByte endpoint and rejects `claude-sonnet-5-5` with HTTP 400: `Supported models are auto.` It cannot constitute a distinct second backbone.

Remaining blocked checks:

- CodaMOSA assertion generation through B1 and B2.
- CoverUp function-calling round-trip through the actual tool on B1 and B2.
- B2 function-calling probe using a genuine endpoint that exposes `claude-sonnet-5-5`.
- End-to-end proxy/token accounting validation.
- Pilot execution and extrapolation.

- B2 decision: user explicitly approved continuing with `auto` for B2 until a distinct second backbone can be configured. 2026-10-22 probes: B1 and B2 both HTTP 200 with `model_returned = auto` and confirmed function calling. The experiment therefore contrasts routes, not backbones; treat RQ2/backbone conclusions as invalid until a genuine B2 endpoint is verified.