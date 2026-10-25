

# Generated at 2026-10-24 07:43:50.405630
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total chars -> return lst1
    assert module_0.total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hi', 'admin']
    # lst2 has fewer total chars -> return lst2
    assert module_0.total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    # equal totals -> return lst1
    assert module_0.total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    # empty lst1 -> return lst1
    assert module_0.total_match([], ['a', 'b']) == []
    # both empty -> return lst1
    assert module_0.total_match([], []) == []
    # single chars vs longer words
    assert module_0.total_match(['a', 'b', 'c'], ['ab']) == ['ab']
    # duplicate strings count toward total
    assert module_0.total_match(['aa', 'aa'], ['bbbb']) == ['bbbb']
    # lst1 strictly shorter wins even with more elements
    assert module_0.total_match(['x'], ['yy', 'zz', 'ww']) == ['x']
    print("All tests passed!")


test_total_match()

# Generated at 2026-10-24 07:43:51.777615
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

# Generated at 2026-10-24 07:43:53.271794
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

# Generated at 2026-10-24 07:43:54.841821
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

# Generated at 2026-10-24 07:43:56.164303
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