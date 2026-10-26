# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f152 import compare


def test_compare_exact_match():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]


def test_compare_mixed_differences():
    # covers x > y, x < y and x == y for abs(x - y)
    assert compare([1, 2, 3, 4], [-1, 2, 5, 4]) == [2, 0, 2, 0]


def test_compare_empty():
    # covers zero-iteration branch of the comprehension / zip
    assert compare([], []) == []
    assert compare([], [1, 2, 3]) == []
    assert compare([1, 2, 3], []) == []


def test_compare_truncates_to_shortest():
    # covers zip stopping at shortest input
    assert compare([1, 2], [1, 2, 3, 4]) == [0, 0]
    assert compare([1, 2, 3, 4], [1, 2]) == [0, 0]
