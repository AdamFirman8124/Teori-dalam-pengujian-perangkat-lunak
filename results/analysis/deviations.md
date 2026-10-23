# Deviasi dari File B (dilog otomatis)

| # | File | Requirement | What was done | Rationale / decision |
|---|---|---|---|---|
| 1 | File B | CM stratum is 3x3 LOC x n_branches (9 strata) | Only 8 non-empty strata exist; L0B2 is empty | Approved deviation, 2026-10-22; all eight observed strata sampled, CM sample >= 40 modules, per-project cap 25% |
| 2 | File B | Pynguin and MuTAP included as tool rows | Only CodaMOSA and CoverUp are implemented here; collaborator owns Pynguin/MuTAP results | User clarification; File B schema retained so collaborator rows can merge later |
| 3 | File A (obsolete) | Code-characteristics RQ3 (Table VIII Spearman) | File B revisi 19 Oktober 2026 mengubah RQ3 menjadi cost-effectiveness (cost_usd, delta E, CE, Pareto) | File B mengalahkan File A; tabel karakteristik kode File A dianggap arsip struktur saja |
| 4 | File B | 13 Wilcoxon cost tests | Number 13 interpreted as all paired tool/backbone/suite cost comparisons available from measured data | If a fixed exact 13-test matrix exists, add it when specified |
| 5 | File B | model_returned must be recorded for every API call | llm_proxy records model_requested and model_returned per call | Required Gate 3 checks are still pending until credentials are present |
| 6 | File B | Dry-run generates Figures 3-5 | Analysis script generates CSV tables; figures are generated only after real data is available | Figure scripts are a remaining deliverable, not synthetic-plotted data |
