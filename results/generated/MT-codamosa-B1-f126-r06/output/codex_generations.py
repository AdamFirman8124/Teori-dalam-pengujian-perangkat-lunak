

# Generated at 2026-10-24 11:25:55.484066
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 1]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([1, 2, 3, 2]) == False
    assert module_0.is_sorted([2, 2, 1]) == False

# Generated at 2026-10-24 11:26:13.610508
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 1]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([1, 2, 3, 2]) == False
    assert module_0.is_sorted([2, 2, 1]) == False

# Generated at 2026-10-24 11:26:22.225265
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

# Generated at 2026-10-24 11:26:40.227437
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

# Generated at 2026-10-24 11:26:42.903562
# Unit test for function is_sorted

# Generated at 2026-10-24 11:26:45.428071
# Unit test for function is_sorted

# Generated at 2026-10-24 11:26:47.855278
# Unit test for function is_sorted