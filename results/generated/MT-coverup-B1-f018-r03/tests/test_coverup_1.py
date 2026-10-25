# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

def test_how_many_times_counts_overlaps_and_nonmatches():
    from f018 import how_many_times

    assert how_many_times("banana", "ana") == 2
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abc", "z") == 0
    assert how_many_times("ab", "abcd") == 0
    assert how_many_times("abc", "") == 4
