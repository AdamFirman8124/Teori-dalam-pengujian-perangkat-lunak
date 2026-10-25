# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f057 import monotonic


def test_monotonic_increasing_returns_true():
    l = [1, 2, 3, 4]
    result = monotonic(l)
    assert result is True
    assert l == [1, 2, 3, 4]


def test_monotonic_decreasing_returns_true():
    l = [4, 3, 2, 1]
    result = monotonic(l)
    assert result is True
    assert l == [4, 3, 2, 1]


def test_monotonic_non_monotonic_returns_false():
    l = [1, 3, 2, 4]
    result = monotonic(l)
    assert result is False
    assert l == [1, 3, 2, 4]


def test_monotonic_empty_and_singleton_are_monotonic():
    assert monotonic([]) is True
    assert monotonic([42]) is True


def test_monotonic_equal_elements_are_monotonic():
    assert monotonic([2, 2, 2]) is True
