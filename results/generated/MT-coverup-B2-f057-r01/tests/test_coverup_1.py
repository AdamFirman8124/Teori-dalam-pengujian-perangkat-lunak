# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f057 import monotonic


def test_monotonic_ascending():
    values = [1, 2, 2, 3]

    assert monotonic(values) is True
    assert values == [1, 2, 2, 3]


def test_monotonic_descending():
    values = [3, 2, 2, 1]

    assert monotonic(values) is True
    assert values == [3, 2, 2, 1]


def test_non_monotonic():
    values = [1, 3, 2]

    assert monotonic(values) is False
    assert values == [1, 3, 2]
