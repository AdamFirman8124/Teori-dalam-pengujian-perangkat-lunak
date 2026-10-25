

# Generated at 2026-10-24 04:15:00.762309
# Unit test for function total_match
def test_total_match():
    # lst1 has the smaller total length -> return lst1
    assert module_0.total_match(["a", "b"], ["abc"]) == ["a", "b"]

    # lst2 has the smaller total length -> return lst2
    assert module_0.total_match(["abc"], ["a", "b"]) == ["a", "b"]

    # tie on total length -> lst1 wins
    assert module_0.total_match(["ab"], ["cd"]) == ["ab"]

    # both empty -> lst1
    assert module_0.total_match([], []) == []

    # lst1 empty, lst2 not -> lst1 (0 <= n)
    assert module_0.total_match([], ["x"]) == []

    # lst2 empty, lst1 not -> lst2
    assert module_0.total_match(["x"], []) == []

    # empty strings contribute 0 length -> tie -> lst1
    assert module_0.total_match(["", ""], []) == ["", ""]

    # single-element equal lengths -> lst1
    assert module_0.total_match(["abc"], ["xyz"]) == ["abc"]

    # longer lists where only totals matter, not element count
    assert module_0.total_match(["aaa", "b"], ["cc", "d", "e"]) == ["cc", "d", "e"]  # 4 vs 4 -> lst1

# Generated at 2026-10-24 04:15:03.179603
# Unit test for function total_match

# Generated at 2026-10-24 04:15:05.597770
# Unit test for function total_match

# Generated at 2026-10-24 04:15:08.012028
# Unit test for function total_match

# Generated at 2026-10-24 04:15:10.505045
# Unit test for function total_match

# Generated at 2026-10-24 04:15:13.005949
# Unit test for function total_match

# Generated at 2026-10-24 04:15:15.423265
# Unit test for function total_match

# Generated at 2026-10-24 04:15:17.843669
# Unit test for function total_match

# Generated at 2026-10-24 04:15:20.255881
# Unit test for function total_match

# Generated at 2026-10-24 04:15:22.671283
# Unit test for function total_match

# Generated at 2026-10-24 04:15:25.085255
# Unit test for function total_match

# Generated at 2026-10-24 04:15:27.498273
# Unit test for function total_match

# Generated at 2026-10-24 04:15:29.912746
# Unit test for function total_match