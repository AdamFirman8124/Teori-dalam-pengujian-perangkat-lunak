# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f085 import add


def test_add_sums_even_values_at_odd_indices():
    assert add([8, 2, 6, 3, 4, 10]) == 12
