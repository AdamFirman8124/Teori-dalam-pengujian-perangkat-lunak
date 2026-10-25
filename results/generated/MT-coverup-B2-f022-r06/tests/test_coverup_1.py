# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_filters_non_integers():
    values = [1, "2", 3.0, None, -4, True, [], 0]

    result = filter_integers(values)

    assert result == [1, -4, True, 0]
    assert values == [1, "2", 3.0, None, -4, True, [], 0]
