# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_cycpattern_check_finds_rotated_pattern():
    assert cycpattern_check("xxbcayy", "abc") is True


def test_cycpattern_check_returns_false_when_no_rotation_matches():
    assert cycpattern_check("abdabd", "abc") is False
