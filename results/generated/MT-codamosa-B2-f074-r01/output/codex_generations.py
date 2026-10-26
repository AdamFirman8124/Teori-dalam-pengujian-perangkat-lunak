

# Generated at 2026-10-25 11:18:13.878858
# Unit test for function total_match
def test_total_match():
    # lst1 has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "world"]) == ["hi", "bye"]

    # lst2 has fewer total characters
    assert module_0.total_match(["apple", "banana"], ["a", "bc"]) == ["a", "bc"]

    # Equal character counts return lst1
    assert module_0.total_match(["ab", "cd"], ["abcd"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], []) == []
    assert module_0.total_match([], ["hello"]) == []

# Generated at 2026-10-25 11:18:18.776155
# Unit test for function total_match
def test_total_match():
    assert module_0.total_match(["hi", "bye"], ["hello", "goodbye"]) == ["hi", "bye"]
    assert module_0.total_match(["hello", "world"], ["hi", "bye"]) == ["hi", "bye"]
    assert module_0.total_match(["abc", "de"], ["12", "345"]) == ["abc", "de"]  # Tie: return lst1
    assert module_0.total_match([], ["hello"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 11:18:23.438282
# Unit test for function total_match
def test_total_match():
    assert module_0.total_match(["hello", "world"], ["hi", "bye"]) == ["hi", "bye"]
    assert module_0.total_match(["hi", "bye"], ["hello", "world"]) == ["hi", "bye"]

    # If both totals are equal, return the first list
    assert module_0.total_match(["abc", "de"], ["12", "345"]) == ["abc", "de"]

    # Empty-list cases
    assert module_0.total_match([], ["hello"]) == []
    assert module_0.total_match(["hello"], []) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 11:18:29.491345
# Unit test for function total_match
def test_total_match():
    # First list has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "world"]) == ["hi", "bye"]

    # Second list has fewer total characters
    assert module_0.total_match(["hello", "world"], ["hi", "bye"]) == ["hi", "bye"]

    # Equal character counts should return the first list
    first = ["a", "bb"]
    second = ["ccc"]
    assert module_0.total_match(first, second) is first

    # Empty-list cases
    assert module_0.total_match([], ["test"]) == []
    assert module_0.total_match([], []) == []

# Generated at 2026-10-25 11:18:33.684051
# Unit test for function total_match
def test_total_match():
    # First list has fewer total characters
    assert module_0.total_match(["hi", "bye"], ["hello", "world"]) == ["hi", "bye"]

    # Second list has fewer total characters
    assert module_0.total_match(["Python", "coding"], ["cat", "dog"]) == ["cat", "dog"]

    # Equal totals should return the first list
    assert module_0.total_match(["ab", "cd"], ["abcd"]) == ["ab", "cd"]

    # Empty lists
    assert module_0.total_match([], []) == []
    assert module_0.total_match([], ["text"]) == []