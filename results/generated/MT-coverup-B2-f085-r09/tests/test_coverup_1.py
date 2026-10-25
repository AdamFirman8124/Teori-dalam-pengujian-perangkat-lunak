# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f085 import add


def test_add_sums_only_even_values_at_odd_indices():
    values = [100, 2, 4, 5, 6, 8]

    result = add(values)

    assert result == 10
    assert values == [100, 2, 4, 5, 6, 8]


def test_add_returns_zero_when_no_odd_indices_exist():
    assert add([]) == 0
