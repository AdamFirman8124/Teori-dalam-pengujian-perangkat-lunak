# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

from f106 import f


def test_f_even_and_odd_branches():
    # f(2) executes the loop body for i=1 (odd branch, lines 10-12)
    # and i=2 (even branch, lines 6-8), plus init (line 3) and return (line 13).
    # i=1: x = 0+1 = 1 ; i=2: x = 1*1*2 = 2
    assert f(2) == [1, 2]


def test_f_edge_cases_and_values():
    # n=0: loop never runs, returns empty list (lines 3 and 13 only)
    assert f(0) == []
    # n=1: only odd branch
    assert f(1) == [1]
    # n=5: interleaves both branches; odd i -> sum 1..i, even i -> factorial i
    assert f(5) == [1, 2, 6, 24, 15]
