# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f085 import add


def test_add_sums_even_numbers_at_odd_indices():
    assert add([100, 2, 200, 6, 300, 10]) == 18


def test_add_ignores_odd_numbers_at_odd_indices():
    assert add([100, 2, 200, 3, 300, 5]) == 2


def test_add_with_no_eligible_indices():
    assert add([]) == 0
    assert add([2]) == 0
