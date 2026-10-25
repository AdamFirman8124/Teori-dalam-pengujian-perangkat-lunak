

# Generated at 2026-10-25 02:48:23.561643
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    lst1 = ["hi", "bye"]             # 5 characters
    lst2 = ["hello", "goodbye"]      # 12 characters
    assert module_0.total_match(lst1, lst2) is lst1

    # lst2 has fewer total characters
    lst1 = ["Python", "testing"]      # 13 characters
    lst2 = ["unit", "test"]           # 8 characters
    assert module_0.total_match(lst1, lst2) is lst2

    # Equal character counts should return lst1
    lst1 = ["abc"]                    # 3 characters
    lst2 = ["x", "yz"]                # 3 characters
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty-list cases
    assert module_0.total_match([], ["a"]) == []
    assert module_0.total_match(["a"], []) == []

# Generated at 2026-10-25 02:48:30.936664
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi"], ["hello"]) == ["hi"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["Python"]) == ["Python"]

    # Equal totals should return lst1
    lst1 = ["ab"]
    lst2 = ["c", "d"]
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty-list cases
    assert module_0.total_match([], ["abc"]) == []
    assert module_0.total_match(["abc"], []) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 02:48:36.771848
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "ts"], ["h", "ello"]) == ["hi", "ts"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["hi", "all"]) == ["hi", "all"]

    # Equal character counts: return lst1
    assert module_0.total_match(["abc", "de"], ["12", "345"]) == ["abc", "de"]

    # Empty-list cases
    assert module_0.total_match([], ["a"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 02:48:41.776897
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "goodbye"]) == ["hi", "bye"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "goodbye"], ["hi", "bye"]) == ["hi", "bye"]

    # Equal character counts should return lst1
    lst1 = ["abc", "de"]       # 5 characters
    lst2 = ["12", "345"]       # 5 characters
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty lists
    assert module_0.total_match([], ["a"]) == []
    assert module_0.total_match(["a"], []) == []
    assert module_0.total_match([], []) == []

    print("All tests passed!")


test_total_match()

# Generated at 2026-10-25 02:48:45.862246
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "there"], ["hello", "world"]) == ["hi", "there"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["hi", "you"]) == ["hi", "you"]

    # Equal character totals should return lst1
    assert module_0.total_match(["ab", "cd"], ["1234"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], ["hello"]) == []
    assert module_0.total_match([], []) == []

    print("All tests passed!")


test_total_match()