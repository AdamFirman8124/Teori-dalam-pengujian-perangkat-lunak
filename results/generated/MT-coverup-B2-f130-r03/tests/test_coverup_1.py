# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

"""Tests for f130.tri covering all previously unexecuted lines (3-11)."""

from f130 import tri


def test_tri_zero_hits_base_case():
    # Covers lines 3-4: the `n == 0` early return branch.
    assert tri(0) == [1]


def test_tri_one_skips_loop_body():
    # Covers line 5 (my_tri = [1, 3]) and line 11 (return) with an
    # empty loop (range(2, 2) yields nothing).
    assert tri(1) == [1, 3]


def test_tri_two_hits_even_branch():
    # Covers lines 6-8: loop entry and the `i % 2 == 0` branch.
    # i = 2 -> append(2 / 2 + 1) == 2.0
    assert tri(2) == [1, 3, 2.0]


def test_tri_three_hits_odd_branch():
    # Covers lines 9-10: the else branch.
    # i = 3 -> append(my_tri[2] + my_tri[1] + (3 + 3) / 2) == 2.0 + 3 + 3.0 == 8.0
    assert tri(3) == [1, 3, 2.0, 8.0]


def test_tri_four_hits_both_branches():
    # Exercises both loop branches across multiple iterations:
    # i = 2 (even) -> 2.0
    # i = 3 (odd)  -> 2.0 + 3 + 3.0 == 8.0
    # i = 4 (even) -> 4 / 2 + 1 == 3.0
    result = tri(4)
    assert result == [1, 3, 2.0, 8.0, 3.0]
    # Postcondition: length is n + 1 for n >= 1.
    assert len(result) == 5


def test_tri_result_length_postcondition():
    # Postcondition check: for n >= 1 the result always has n + 1 elements
    # and starts with the fixed seed values [1, 3].
    for n in (1, 2, 3, 4, 5):
        result = tri(n)
        assert len(result) == n + 1
        assert result[0] == 1
        assert result[1] == 3
