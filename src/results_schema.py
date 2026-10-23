from __future__ import annotations

FIELDS = [
    "run_id", "suite", "unit_id", "project", "tool", "tool_version", "backbone",
    "model_requested", "model_returned", "run_idx", "seed", "start_time", "end_time",
    "budget_s", "gen_time_s", "ratelimit_wait_s", "hit_budget", "wait_flag", "attempt",
    "status", "error_category", "n_api_calls", "tokens_in", "tokens_out", "cost_usd",
    "n_raw_proposals", "n_raw_pass", "n_tests_final", "n_pass_first", "n_fail", "n_error",
    "n_timeout", "k_reruns", "n_flaky", "n_valid", "lines_total", "lines_exec",
    "branches_total", "branches_exec", "mutation_tool", "n_mutants", "n_killed",
    "n_survived", "n_mutant_timeout", "sim_max_median",
]
