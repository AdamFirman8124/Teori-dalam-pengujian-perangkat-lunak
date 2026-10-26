# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_empty_list():
    assert unique_digits([]) == []


def test_unique_digits_mixed_single_digits():
    # 1 and 3 have only odd digits (included), 2 and 4 do not (excluded)
    # exercises both True and False outcomes of the `if all(...)` branch
    assert unique_digits([1, 2, 3, 4]) == [1, 3]


def test_unique_digits_multi_digit_and_sorted():
    # 11, 5, 33, 135, 15 contain only odd digits; 22 and 246 contain an even digit
    # also verifies the result is sorted
    assert unique_digits([33, 22, 11, 246, 135, 5]) == [5, 11, 33, 135]
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([2, 4, 6, 8]) == []
