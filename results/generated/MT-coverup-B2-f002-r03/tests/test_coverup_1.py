# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f002 import truncate_number


def test_truncate_number_returns_fractional_part():
    assert truncate_number(3.75) == 0.75
    assert truncate_number(5.0) == 0.0
    assert truncate_number(-2.25) == 0.75
