

# Generated at 2026-10-25 00:26:21.933022
# Unit test for function total_match

# Generated at 2026-10-25 00:26:27.095822
# Unit test for function total_match
def test_total_match():assert module_0.total_match(["hi", "cat"], ["hello", "world"]) == ["hi", "cat"]

# Generated at 2026-10-25 00:26:33.262378
# Unit test for function total_match
def test_total_match():
    short = ["hi", "bye"]             # Total length: 5
    long = ["hello", "goodbye"]       # Total length: 12

    assert module_0.total_match(short, long) is short
    assert module_0.total_match(long, short) is short

    # If lengths are equal, the first list should be returned
    lst1 = ["ab", "c"]                # Total length: 3
    lst2 = ["xyz"]                    # Total length: 3
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty-list cases
    empty = []
    assert module_0.total_match(empty, ["a"]) is empty
    assert module_0.total_match(empty, []) is empty

# Generated at 2026-10-25 00:26:41.361469
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["a", "bc"], ["hello", "world"]) == ["a", "bc"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["a", "bc"]) == ["a", "bc"]

    # Equal lengths should return lst1
    lst1 = ["ab", "c"]       # 3 characters
    lst2 = ["x", "yz"]       # 3 characters
    assert module_0.total_match(lst1, lst2) is lst1

    # Empty-list cases
    assert module_0.total_match([], ["a"]) == []
    assert module_0.total_match(["a"], []) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 00:26:45.518351
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "goodbye"]) == ["hi", "bye"]

    # lst2 has fewer total characters
    assert module_0.total_match(["hello", "world"], ["hi", "bye"]) == ["hi", "bye"]

    # Equal character counts should return lst1
    assert module_0.total_match(["ab", "cd"], ["abc", "d"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], ["test"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 00:26:51.283526
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "cat"], ["hello", "world"]) == ["hi", "cat"]

    # lst2 has fewer total characters
    assert module_0.total_match(["Python", "coding"], ["hi", "cat"]) == ["hi", "cat"]

    # Equal totals should return lst1
    assert module_0.total_match(["ab", "cd"], ["1234"]) == ["ab", "cd"]

    # Empty-list cases
    assert module_0.total_match([], ["hello"]) == []
    assert module_0.total_match(["hello"], []) == []
    assert module_0.total_match([], []) == []