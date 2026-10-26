

# Generated at 2026-10-25 11:35:19.212883
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

# Generated at 2026-10-25 11:35:21.759600
# Unit test for function common

# Generated at 2026-10-25 11:35:24.265192
# Unit test for function common

# Generated at 2026-10-25 11:35:26.679736
# Unit test for function common

# Generated at 2026-10-25 11:35:29.091605
# Unit test for function common

# Generated at 2026-10-25 11:35:31.505212
# Unit test for function common

# Generated at 2026-10-25 11:35:33.920588
# Unit test for function common

# Generated at 2026-10-25 11:35:36.333923
# Unit test for function common

# Generated at 2026-10-25 11:35:38.749273
# Unit test for function common

# Generated at 2026-10-25 11:35:41.163605
# Unit test for function common

# Generated at 2026-10-25 11:35:43.579095
# Unit test for function common

# Generated at 2026-10-25 11:35:45.991665
# Unit test for function common

# Generated at 2026-10-25 11:35:48.409006
# Unit test for function common