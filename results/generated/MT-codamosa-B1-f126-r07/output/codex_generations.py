

# Generated at 2026-10-24 14:19:18.890152
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:21.307043
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:23.725358
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:26.140169
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:28.553256
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:30.967032
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:33.379378
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:35.794086
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:38.206446
# Unit test for function is_sorted

# Generated at 2026-10-24 14:19:40.938237
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

# Generated at 2026-10-24 14:19:43.622519
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