# Running CoverUp on the two MuTAP datasets (RQ1 / RQ2)

## Datasets found in this folder

| Dataset | Location | Tasks | Program-under-test | Provided mutants |
|---|---|---|---|---|
| **HumanEval** | `MuTAP/HumanEval/Testing_HumanEval/<id>/` | 164 (dirs `0`..`163`) | `script_<id>.py` | `Mutants/mutant_<id>_<k>.py` |
| **Refactory** | `MuTAP/Refactory/Reference_Scripts/` | 5 (`q1`..`q5`) | `Tests/<q>/script_<q>.py` | `Wrong_st/<q>/wrong/wrong_<q>_<n>.py` (108-575 each) |

These are exactly the two datasets MuTAP's README describes and the "MT suite" the CoverUp
FSE'25 paper compares against, so results are directly comparable.

## Metric definitions (identical for every method)

| Metric | How it is computed |
|---|---|
| **Coverage** | Line coverage of the PUT, measured with **SlipCover** (CoverUp's own instrumenter), restricted to the PUT file. |
| **Pass Rate** | Passing test units / total test units, **each unit executed in isolation** so one broken test cannot mask the others. |
| **Mutation Score** | MuTAP's protocol: `killed / (all - problematic)`. Killed = suite raises `AssertionError`; survived = clean run; problematic (excluded) = timeout or non-assertion error. |
| **Wall time** | Generation time of the suite (CoverUp run). Left empty for pre-existing baseline suites rather than conflated with evaluation time. |
| **Cost** | USD as accounted by CoverUp itself (`litellm.completion_cost`, persisted in CoverUp's checkpoint). |

Two suite styles occur in the datasets and are handled transparently:

* **inline** (MuTAP/Codex, Copilot): the file embeds the PUT and defines `def test():`
  without calling it - MuTAP's own protocol, reproduced exactly;
* **import** (CoverUp, Pynguin): the file imports the module under test - the mutant
  shadows the PUT through `PYTHONPATH`.

## Harness validation

The mutation-score implementation reproduces MuTAP's published numbers exactly:

| Task | Harness | MuTAP's shipped `st_fewshot_mut_all_mutant_score.csv` |
|---|---|---|
| Refactory q1 | 0.9566326530612245, killed 375, all 575, problematic 183 | 0.956632653061224, 375, 575 |

## Commands

```bash
# 1) Baselines that need no LLM (MuTAP-Codex, Copilot-FS, Pynguin), both datasets
.venv/bin/python run_experiment.py --dataset both --methods baselines --outdir results

# 2) CoverUp (RQ1 + RQ2). Requires working LLM access.
.venv/bin/python run_experiment.py --dataset both --methods all --model gpt-4o --outdir results
```

Output: `results/rows.csv` (one row per dataset/task/method) plus the aggregated
`results/rq1.md` and `results/rq2.md` tables.

Set `OPENAI_API_KEY` in the environment before running CoverUp. Keep API keys out of
the project tree and shell history.

## Reference numbers from the CoverUp FSE'25 paper (MT suite = these two datasets)

**RQ1 / Table 2** - overall coverage:

| Test generator | Line | Branch | Line+Branch |
|---|---|---|---|
| CoverUp (gpt-4o) | 89.2 % | 88.7 % | 89.0 % |
| MuTAP (codex few-shot) | 80.8 % | 71.7 % | 77.7 % |
| MuTAP (codex zero-shot) | 79.2 % | 72.7 % | 77.0 % |
| MuTAP (gpt4o zero-shot) | 78.0 % | 74.5 % | 76.8 % |
| MuTAP (gpt4o few-shot) | 15.9 % | 0.0 % | 10.4 % |

**RQ4 / Table 3** - backbone cost (CM suite): CoverUp 28,690 prompts, 58.1M prompt +
7.3M completion tokens, **4.0 h, US$399**; CodaMosa (gpt4o) 71.0 h, US$265.

**Pass rate**: the paper reports MuTAP baselines at 100 % on the MT suite (Table 2 right side).

## Current blocker

The provided OpenAI key authenticated but had **no credits**
(`429 insufficient_quota / credit_balance_exhausted`), so CoverUp cannot generate tests.
`run_experiment.py` now performs a one-call LLM preflight and fails immediately with that
diagnosis instead of spending the run in litellm's exponential backoff. Baseline rows are
unaffected and can be produced without any API access. The exposed key file was removed;
revoke/rotate that key in the OpenAI dashboard before using another key.