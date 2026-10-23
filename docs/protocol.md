# Frozen-candidate experiment protocol

Status: **not frozen**. Main execution is prohibited until every gate in `pedoman_eksperimen_ai_friendly.md` passes and the user approves the pilot.

## Interpretation

File B is authoritative. The complete study combines this repository's CodaMOSA and CoverUp measurements with Pynguin and MuTAP measurements produced by the collaborator. This pipeline runs only CodaMOSA and CoverUp, but preserves File B's two-suite, two-backbone, R=10 design and schema so collaborator rows can be merged without changing the analysis.

The measured factorial subset is:

- Tool: CodaMOSA, CoverUp
- Suite: MT, CM
- Backbone: B1, B2
- Repetitions: 10 per tool × suite × backbone × unit

Tool comparisons are paired within each suite, backbone, unit, and repetition. Dataset comparisons within one tool are descriptive only because MT functions and CM modules are not paired experimental units.

## Inputs and unit definition

- MT: 163 directories `dataset/coverup-eval/MuTAP-benchmarks/f001` … `f163`. One task is one benchmark function packaged as a Python module.
- CM: 425 rows in `dataset/codamosa/replication/test-apps/cm_modules.csv` from 24 projects. One task is the Python module named by one manifest row. The main run uses a deterministic stratified sample of at least 40 modules; the three pilot modules are excluded from it.
- Total available units: 588, confirming the colleague's approximate total of 580.

## Fixed decisions

- Budget: 600 seconds wall-clock per run; evaluation is outside the generation budget.
- Rate-limit wait counts toward the 600-second deadline but is subtracted from `gen_time_s`; waits above 60 seconds set `wait_flag=1` and receive one same-seed retry at the end of the block.
- Parallelism P=5, fixed within a block and no greater than six physical cores.
- Each run uses an isolated container with 2 CPUs, 2200 MB RAM, SIGINT at 600 seconds, and SIGKILL 30 seconds later.
- Seeds derive deterministically from protocol seed 20261022, configuration, unit, and repetition.
- Flaky check k=5.
- Shared mutation evaluator: Cosmic Ray 8.7.0. The same precomputed mutant manifest must be reused across tools and repetitions for a unit. Mutation timeout counts as killed and is reported separately.
- Temperature: CodaMOSA 0.8. CoverUp sampling parameters must be explicit after its installed interface is verified.
- CM project cap: at most 25% of the 40-module sample from one project.
- Documented Gate 4 deviation approved 2026-10-22: the empirical LOC × branch tertiles contain no `L0B2` modules, so the CM sample covers all eight observed non-empty strata rather than inventing a ninth populated stratum.
- API cost cap: USD 900 paid-equivalent across both backbones, both tools, suites, pilot, and reruns.
- Elapsed cap: 14 days from pilot start.
- Stop launching new runs at 80% of either cap; hard stop at 100%.

## Models and pricing

### B1

- Requested model: `auto`
- Report label: `gpt-5.6-sol (seller-claimed; endpoint reports "auto")`
- Base URL: environment variable `LLM_BASE_URL`; approved endpoint is `https://stream.srbyte.id/v1`
- Credential: environment variable `LLM_API_KEY`
- Paid-equivalent reference: OpenAI GPT-5.6 Sol, USD 4.00 / 1M input and USD 20.00 / 1M output tokens
- Source: <https://developers.openai.com/api/docs/models/gpt-5.6-sol.md>, accessed 2026-10-22
- Promotional price stated available at least through 2026-11-21
- Identity limitation: the endpoint returns `auto`; the seller's claim that it is GPT-5.6 Sol is unverified

### B2

- Requested model: `auto`
- Report label: `auto (B2 route; shared endpoint configuration; File B deviation)`
- Base URL: environment variable `LLM_BASE_URL_B2`
- Credential: environment variable `LLM_API_KEY_B2`
- Paid-equivalent reference: same seller-endpoint estimate as B1; to be re-priced when a distinct B2 route is configured.
- Required Gate 0 deviation approved 2026-10-22: B2 is temporarily using the same seller endpoint/configuration as B1 because the configured B2 route only exposes `auto`. This duplicates B1 and does not satisfy File B's two-backbone design. Configure `LLM_BASE_URL_B2` and `LLM_API_KEY_B2` to a genuine second endpoint before interpreting results as two-backbone.

Every raw response must retain its returned `model` field. Any change in `model_returned` stops the block.


## Metrics and analysis

Primary per run: raw validity, flaky count, line coverage, branch coverage, and mutation score. Secondary: wall-clock generation time, rate-limit wait, API calls, input/output tokens, paid-equivalent cost, failure category, and budget hit.

Aggregation follows File A/B: median over repetitions per unit, then median over units for effectiveness tables. Mean, median, and standard deviation over repetitions are also reported as explicitly requested. Paired CodaMOSA-vs-CoverUp comparisons use Wilcoxon signed-rank on per-unit repetition medians, Vargha–Delaney A12, and Holm correction. Bootstrap 95% confidence intervals are reported for mean differences. MT emphasizes mutation score; CM reports branch coverage and mutation score.

## Required gates before API use

1. Pin source provenance and build reproducible images.
2. Verify CodaMOSA assertions, CoverUp interruption/checkpointing, B1/B2 function calling, custom endpoints, and the independent evaluation pipeline.
3. Verify proxy request/response/token logging without credentials.
4. Build module characteristics and a valid CM pilot/sample split.
5. Generate all expected tables and plots from simulated data.
6. Ensure all four credential/base-URL environment variables are present.

No API request has been made under this protocol yet.
