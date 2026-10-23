# Required-reading report

Both documents were read in full before implementation.

## File A — draft results chapter

`naskah_rancangan_bab_results_ai_friendly.md` is a 400-line Indonesian draft for Chapters IV–VII and appendices. It specifies manuscript structure, Tables IV–IX, Figures 3–5, metric definitions, and statistical reporting notes. It includes placeholders plus illustrative/pre-written numeric values explicitly marked dummy (`†`), including examples in Tables IV–VII and IX. None are treated as expected results.

File A predates File B's 19 October RQ3 revision: File A's RQ3 is code-characteristic correlation, while current File B changes RQ3 to cost-effectiveness. File B wins; File A remains structural guidance only.

## File B — experiment and reproduction guideline

`pedoman_eksperimen_ai_friendly.md` is a 433-line Indonesian protocol, version 1.2 dated 21 October 2026. It defines phases 0–11, hard gates, benchmark counts, timing rules, pilot design, run matrix, evaluation process, complete `results.csv` and `module_characteristics.csv` schemas, cost-effectiveness RQ3, fatal prohibitions, recovery rules, and archive contents.

## Authoritative interpretation

The full paper design includes Pynguin, CodaMOSA, CoverUp, and MuTAP with two backbones. Per user clarification, this repository executes only CodaMOSA and CoverUp because a collaborator handles Pynguin and MuTAP. Results use the complete File B schema so collaborator data can be merged later.

Within this measured subset, tool comparisons are paired separately on MT and CM. A tool's MT-vs-CM comparison is descriptive rather than paired because the units differ. Backbone comparisons and interactions remain part of File B and are retained.

## Known protocol deviation

The 425 CM modules produce eight, not nine, observed LOC × branch tertile cells; `L0B2` is empty. The user approved sampling across all eight observed cells while retaining 40 modules, three disjoint pilot modules, deterministic seed 20261022, and the 25% per-project cap.
