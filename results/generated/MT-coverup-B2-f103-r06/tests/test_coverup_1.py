# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import f103


def test_rounded_avg_returns_minus_one_when_m_is_less_than_n():
    assert f103.rounded_avg(5, 4) == -1


def test_rounded_avg_sums_inclusive_range_and_returns_binary_average():
    assert f103.rounded_avg(1, 5) == "0b11"
