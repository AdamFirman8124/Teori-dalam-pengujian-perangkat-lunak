

# Generated at 2026-10-25 01:59:41.361432
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hello", "hi"], ["Python", "coding"]) == ["hello", "hi"]

    # lst2 has fewer total characters
    assert module_0.total_match(["apple", "banana"], ["cat", "dog"]) == ["cat", "dog"]

    # Equal character counts: lst1 should be returned
    assert module_0.total_match(["ab", "cd"], ["test"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], ["abc"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 01:59:47.755499
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "a"], ["hello"]) == ["hi", "a"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["cat"]) == ["cat"]

    # Equal totals should return lst1
    lst1 = ["ab"]
    lst2 = ["c", "d"]
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty-list cases
    assert module_0.total_match([], ["abc"]) == []
    assert module_0.total_match(["abc"], []) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 01:59:53.138424
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "world"]) == ["hi", "bye"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["a", "bc"]) == ["a", "bc"]

    # Equal totals: the function should return lst1
    assert module_0.total_match(["ab", "c"], ["x", "yz"]) == ["ab", "c"]

    # Empty-list cases
    assert module_0.total_match([], ["test"]) == []
    assert module_0.total_match(["test"], []) == []
    assert module_0.total_match([], []) == []


test_total_match()
print("All tests passed!")

# Generated at 2026-10-25 01:59:57.333686
# Unit test for function total_match
def test_total_match():
    assert module_0.total_match(["hi", "bye"], ["hello", "goodbye"]) == ["hi", "bye"]
    assert module_0.total_match(["hello", "world"], ["a", "bc"]) == ["a", "bc"]
    assert module_0.total_match(["ab", "cd"], ["1234"]) == ["ab", "cd"]  # Tie returns lst1
    assert module_0.total_match([], ["test"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 02:00:01.632261
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hello", "hi"], ["hello", "world"]) == ["hello", "hi"]

    # lst2 has fewer total characters
    assert module_0.total_match(["Python", "testing"], ["unit", "test"]) == ["unit", "test"]

    # Equal character counts return lst1
    assert module_0.total_match(["ab", "cd"], ["abcd"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], ["a"]) == []
    assert module_0.total_match([], []) == []