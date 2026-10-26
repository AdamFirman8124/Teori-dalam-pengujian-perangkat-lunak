# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f083 import starts_one_ends


def test_starts_one_ends_n_equals_one():
    assert starts_one_ends(1) == 1


def test_starts_one_ends_n_equals_two():
    assert starts_one_ends(2) == 18 * (10 ** 0)
    assert starts_one_ends(2) == 18


def test_starts_one_ends_n_greater_than_two():
    assert starts_one_ends(3) == 18 * (10 ** 1) == 180
    assert starts_one_ends(4) == 18 * (10 ** 2) == 1800
    assert starts_one_ends(5) == 18 * (10 ** 3) == 18000
