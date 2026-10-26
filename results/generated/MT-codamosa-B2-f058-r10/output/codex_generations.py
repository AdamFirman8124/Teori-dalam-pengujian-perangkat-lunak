

# Generated at 2026-10-25 11:45:02.195051
# Unit test for function common

# Generated at 2026-10-25 11:45:10.836728
# Unit test for function common
def test_common():assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]

# Generated at 2026-10-25 11:45:15.393412
# Unit test for function common
def test_common():
    # Basic overlap
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]

    # No common elements
    assert module_0.common([1, 2], [3, 4]) == []

    # Identical lists
    assert module_0.common([5, 1, 3], [5, 1, 3]) == [1, 3, 5]

    # Empty first list
    assert module_0.common([], [1, 2, 3]) == []

    # Empty second list
    assert module_0.common([1, 2, 3], []) == []

    # Both empty
    assert module_0.common([], []) == []

    # Duplicates within a list â result must not repeat
    assert module_0.common([1, 1, 2, 3], [1, 3, 3]) == [1, 3]

    # Unsorted input â output must be sorted
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]

    # String elements
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]

    # Mixed types with no overlap (int vs str never equal)
    assert module_0.common([1, 2], ["1", "2"]) == []

    print("All tests passed!")


test_common()

# Generated at 2026-10-25 11:45:44.027107
# Unit test for function common
def test_common():
    # Basic overlap
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]

    # No common elements
    assert module_0.common([1, 2], [3, 4]) == []

    # Identical lists
    assert module_0.common([5, 1, 3], [5, 1, 3]) == [1, 3, 5]

    # Empty first list
    assert module_0.common([], [1, 2, 3]) == []

    # Empty second list
    assert module_0.common([1, 2, 3], []) == []

    # Both empty
    assert module_0.common([], []) == []

    # Duplicates within a list â result must not repeat
    assert module_0.common([1, 1, 2, 3], [1, 3, 3]) == [1, 3]

    # Unsorted input â output must be sorted
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]

    # String elements
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]

    # Mixed types with no overlap (int vs str never equal)
    assert module_0.common([1, 2], ["1", "2"]) == []

    print("All tests passed!")


test_common()

# Generated at 2026-10-25 11:46:07.102552
# Unit test for function common
def test_common():
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert module_0.common([3, 2, 1], [1, 2]) == [1, 2]  # sorted result
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

# Generated at 2026-10-25 11:46:21.654090
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [1, 1, 3]) == [1, 3]
    assert module_0.common([1, 2], [3, 4]) == []
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([5, 3, 1], [1, 3, 5]) == [1, 3, 5]