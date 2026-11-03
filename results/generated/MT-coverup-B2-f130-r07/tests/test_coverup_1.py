# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

from f130 import tri


def test_tri_zero_returns_single_one():
    # Covers lines 3-4 (true branch of the n == 0 check).
    assert tri(0) == [1]


def test_tri_one_returns_base_sequence_without_loop():
    # Covers lines 5-6 and 11 with the loop body never entered
    # (false branch of the loop condition).
    assert tri(1) == [1, 3]


def test_tri_two_appends_even_branch_value():
    # Covers lines 7-8 (true branch of the i % 2 == 0 check).
    assert tri(2) == [1, 3, 2.0]


def test_tri_three_appends_odd_branch_value():
    # Covers line 10 (false branch of the i % 2 == 0 check).
    assert tri(3) == [1, 3, 2.0, 8.0]


def test_tri_five_covers_all_branches_in_one_call():
    # Exercises both loop branches (even i=2, i=4 and odd i=3, i=5)
    # and verifies the full returned sequence.
    assert tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
