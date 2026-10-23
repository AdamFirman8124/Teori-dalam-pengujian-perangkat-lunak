import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("analyze", ROOT / "scripts" / "analyze.py")
analyze = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analyze)


def test_holm_is_monotonic_in_rank_order():
    adjusted = analyze.holm([0.01, 0.04, 0.03])
    assert adjusted == [0.03, 0.06, 0.06]


def test_a12_and_bootstrap():
    assert analyze.a12(np.array([2, 3]), np.array([1, 2])) == 0.875
    low, high = analyze.bootstrap_ci(np.array([1.0, 2.0, 3.0]))
    assert low <= 2.0 <= high


def test_derivatives_range():
    df = pd.DataFrame(
        {
            "n_raw_pass": [5, 10],
            "n_raw_proposals": [10, 0],
            "lines_exec": [90, 50],
            "lines_total": [100, 100],
            "branches_exec": [20, 10],
            "branches_total": [40, 40],
            "n_killed": [30, 0],
            "n_mutants": [50, 0],
        }
    )
    d = analyze.derivatives(df)
    assert d.rv.iloc[0] == 50.0
    assert np.isnan(d.rv.iloc[1])
    assert d.lc.iloc[0] == 90.0
    assert d.bc.iloc[0] == 50.0
    assert d.ms.iloc[0] == 60.0
    assert np.isnan(d.ms.iloc[1])
