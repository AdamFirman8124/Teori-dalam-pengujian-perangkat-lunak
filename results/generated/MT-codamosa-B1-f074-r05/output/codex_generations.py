

# Generated at 2026-10-24 10:45:52.151599
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars -> return lst1
    assert module_0.total_match(["hi", "there"], ["a", "b", "c"]) == ["hi", "there"]

    # lst2 has fewer total chars -> return lst2
    assert module_0.total_match(["aaaa", "bbbb"], ["a"]) == ["a"]

    # tie -> return lst1 (<=)
    assert module_0.total_match(["ab"], ["cd"]) == ["ab"]

    # empty vs empty -> tie -> lst1
    assert module_0.total_match([], []) == []

    # empty lst1 -> lst1 wins (0 <= anything)
    assert module_0.total_match([], ["x"]) == []

    # empty lst2 -> lst2 wins only if lst1 is longer
    assert module_0.total_match(["x"], []) == []

    # same object identity preserved, not a copy
    a, b = ["a"], ["bb"]
    assert module_0.total_match(a, b) is a

# Generated at 2026-10-24 10:45:54.603846
# Unit test for function total_match

# Generated at 2026-10-24 10:45:57.020729
# Unit test for function total_match

# Generated at 2026-10-24 10:45:59.437779
# Unit test for function total_match

# Generated at 2026-10-24 10:46:02.065481
# Unit test for function total_match

# Generated at 2026-10-24 10:46:04.620765
# Unit test for function total_match

# Generated at 2026-10-24 10:46:07.039395
# Unit test for function total_match

# Generated at 2026-10-24 10:46:09.457553
# Unit test for function total_match

# Generated at 2026-10-24 10:46:11.874847
# Unit test for function total_match

# Generated at 2026-10-24 10:46:14.293852
# Unit test for function total_match

# Generated at 2026-10-24 10:46:15.663082
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars -> return lst1
    assert module_0.total_match(["hi", "there"], ["a", "b", "c"]) == ["hi", "there"]

    # lst2 has fewer total chars -> return lst2
    assert module_0.total_match(["aaaa", "bbbb"], ["a"]) == ["a"]

    # tie -> return lst1 (<=)
    assert module_0.total_match(["ab"], ["cd"]) == ["ab"]

    # empty vs empty -> tie -> lst1
    assert module_0.total_match([], []) == []

    # empty lst1 -> lst1 wins (0 <= anything)
    assert module_0.total_match([], ["x"]) == []

    # empty lst2 -> lst2 wins only if lst1 is longer
    assert module_0.total_match(["x"], []) == []

    # same object identity preserved, not a copy
    a, b = ["a"], ["bb"]
    assert module_0.total_match(a, b) is a