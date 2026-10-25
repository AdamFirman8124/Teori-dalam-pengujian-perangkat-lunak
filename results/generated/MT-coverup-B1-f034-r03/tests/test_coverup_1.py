# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    values = [3, 1, 2, 3, 1]
    original = values.copy()

    result = unique(values)

    assert result == [1, 2, 3]
    assert values == original
