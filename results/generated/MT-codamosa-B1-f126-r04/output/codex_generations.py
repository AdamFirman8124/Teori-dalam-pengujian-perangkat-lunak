

# Generated at 2026-10-24 14:13:55.276945
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists with no duplicates -> True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([]) == True
    # Sorted with at most two duplicates -> True
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 1]) == True
    # More than two duplicates of the same number -> False
    assert module_0.is_sorted([1, 1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([2, 2, 2]) == False
    # Not sorted -> False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Duplicates fine but order broken -> False
    assert module_0.is_sorted([1, 2, 2, 1]) == False
    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2, 2]) == True
    assert module_0.is_sorted([-1, -2, 0]) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()

# Generated at 2026-10-24 14:14:11.866953
# Unit test for function is_sorted
def test_is_sorted():
    # sorted cases
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert module_0.is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([1, 1]) == True

    # exactly 2 duplicates allowed if still sorted
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True

    # unsorted cases
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([2, 1]) == False

    # more than 2 duplicates -> False even if sorted
    assert module_0.is_sorted([1, 2, 2, 2, 3, 4]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3, 3]) == False

# Generated at 2026-10-24 14:14:29.835299
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists with no duplicates -> True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([]) == True
    # Sorted with at most two duplicates -> True
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 1]) == True
    # More than two duplicates of the same number -> False
    assert module_0.is_sorted([1, 1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([2, 2, 2]) == False
    # Not sorted -> False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Duplicates fine but order broken -> False
    assert module_0.is_sorted([1, 2, 2, 1]) == False
    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2, 2]) == True
    assert module_0.is_sorted([-1, -2, 0]) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()

# Generated at 2026-10-24 14:14:32.489129
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists with no duplicates -> True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([]) == True
    # Sorted with at most two duplicates -> True
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 1]) == True
    # More than two duplicates of the same number -> False
    assert module_0.is_sorted([1, 1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([2, 2, 2]) == False
    # Not sorted -> False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Duplicates fine but order broken -> False
    assert module_0.is_sorted([1, 2, 2, 1]) == False
    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2, 2]) == True
    assert module_0.is_sorted([-1, -2, 0]) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()

# Generated at 2026-10-24 14:14:35.196074
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists with no duplicates -> True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([]) == True
    # Sorted with at most two duplicates -> True
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 1]) == True
    # More than two duplicates of the same number -> False
    assert module_0.is_sorted([1, 1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([2, 2, 2]) == False
    # Not sorted -> False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Duplicates fine but order broken -> False
    assert module_0.is_sorted([1, 2, 2, 1]) == False
    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2, 2]) == True
    assert module_0.is_sorted([-1, -2, 0]) == False
    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()