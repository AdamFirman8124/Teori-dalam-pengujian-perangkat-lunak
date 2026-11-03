# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_binary_conversion():
    """Covers lines 3-7: loop body executes (while condition True) and terminates."""
    assert change_base(8, 2) == "1000"
    assert change_base(7, 2) == "111"
    assert change_base(10, 2) == "1010"


def test_change_base_other_base():
    """Covers digit accumulation with a different base (digits prepended in order)."""
    assert change_base(8, 3) == "22"
    assert change_base(11, 3) == "102"
    assert change_base(9, 5) == "14"


def test_change_base_zero_skips_loop():
    """Covers the False branch of 'while x > 0' immediately (loop never entered)."""
    assert change_base(0, 2) == ""
    assert change_base(0, 10) == ""
