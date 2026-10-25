# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_cycpattern_check_finds_cyclic_pattern():
    assert cycpattern_check("xxcabyy", "abc") is True


def test_cycpattern_check_rejects_missing_cyclic_pattern():
    assert cycpattern_check("zzzz", "abc") is False
