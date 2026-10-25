

# Generated at 2026-10-24 07:22:26.749978
# Unit test for function total_match

# Generated at 2026-10-24 07:22:29.166156
# Unit test for function total_match

# Generated at 2026-10-24 07:22:31.585873
# Unit test for function total_match

# Generated at 2026-10-24 07:22:33.999060
# Unit test for function total_match

# Generated at 2026-10-24 07:22:36.413357
# Unit test for function total_match

# Generated at 2026-10-24 07:22:38.827907
# Unit test for function total_match

# Generated at 2026-10-24 07:22:41.250063
# Unit test for function total_match

# Generated at 2026-10-24 07:22:43.660053
# Unit test for function total_match

# Generated at 2026-10-24 07:22:53.318544
# Unit test for function total_match
def test_total_match():
    # l1 total = 3+4 = 7, l2 total = 5 -> lst1 shorter or equal, return lst1
    assert module_0.total_match(["hi", "admin"], ["hI", "Hi"]) == ["hI", "Hi"]
    # l1 total = 4, l2 total = 4 -> tie, return lst1
    assert module_0.total_match(["four"], ["four"]) == ["four"]
    # l1 total = 1+2 = 3, l2 total = 3+4 = 7 -> return lst1
    assert module_0.total_match(["a", "bb"], ["ccc", "dddd"]) == ["a", "bb"]
    # l1 total = 1+2+3 = 6, l2 total = 2+3 = 5 -> return lst2
    assert module_0.total_match(["a", "bb", "ccc"], ["bb", "ccc"]) == ["bb", "ccc"]
    # empty list has total 0 -> returned when other is longer
    assert module_0.total_match([], ["x"]) == []
    assert module_0.total_match(["x", "y"], []) == []
    # both empty -> tie -> return lst1
    assert module_0.total_match([], []) == []

# Generated at 2026-10-24 07:22:54.624343
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

# Generated at 2026-10-24 07:22:55.931065
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