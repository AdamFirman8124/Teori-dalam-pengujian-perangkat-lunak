

# Generated at 2026-10-24 10:37:05.266574
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #

# Generated at 2026-10-24 10:37:12.253956
# Unit test for function double_the_difference
def test_double_the_difference():
    # Basic positive odd numbers
    assert module_0.double_the_difference([1, 3, 5]) == 1 + 9 + 25  # 35

    # Empty list
    assert module_0.double_the_difference([]) == 0

    # Negative numbers are ignored (even negative odds)
    assert module_0.double_the_difference([-1, -3, 5]) == 25
    assert module_0.double_the_difference([-2, -4]) == 0

    # Even numbers are ignored
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Floats are ignored
    assert module_0.double_the_difference([1.5, 3.2, 5]) == 25
    assert module_0.double_the_difference([0.5, 1.5]) == 0

    # Zero is ignored
    assert module_0.double_the_difference([0, 1]) == 1

    # Mixed case
    assert module_0.double_the_difference([1, -2, 3, 4.5, 0, -5, 7]) == 1 + 9 + 49  # 59

    # Large odd numbers
    assert module_0.double_the_difference([9, 11]) == 81 + 121  # 202

    print("All tests passed!")


test_double_the_difference()

# Generated at 2026-10-24 10:37:13.560927
# Unit test for function double_the_difference
def test_double_the_difference():
    # Basic positive odd numbers
    assert module_0.double_the_difference([1, 3, 5]) == 1 + 9 + 25  # 35

    # Empty list
    assert module_0.double_the_difference([]) == 0

    # Negative numbers are ignored (even negative odds)
    assert module_0.double_the_difference([-1, -3, 5]) == 25
    assert module_0.double_the_difference([-2, -4]) == 0

    # Even numbers are ignored
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Floats are ignored
    assert module_0.double_the_difference([1.5, 3.2, 5]) == 25
    assert module_0.double_the_difference([0.5, 1.5]) == 0

    # Zero is ignored
    assert module_0.double_the_difference([0, 1]) == 1

    # Mixed case
    assert module_0.double_the_difference([1, -2, 3, 4.5, 0, -5, 7]) == 1 + 9 + 49  # 59

    # Large odd numbers
    assert module_0.double_the_difference([9, 11]) == 81 + 121  # 202

    print("All tests passed!")


test_double_the_difference()

# Generated at 2026-10-24 10:37:14.869129
# Unit test for function double_the_difference
def test_double_the_difference():
    # Basic positive odd numbers
    assert module_0.double_the_difference([1, 3, 5]) == 1 + 9 + 25  # 35

    # Empty list
    assert module_0.double_the_difference([]) == 0

    # Negative numbers are ignored (even negative odds)
    assert module_0.double_the_difference([-1, -3, 5]) == 25
    assert module_0.double_the_difference([-2, -4]) == 0

    # Even numbers are ignored
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Floats are ignored
    assert module_0.double_the_difference([1.5, 3.2, 5]) == 25
    assert module_0.double_the_difference([0.5, 1.5]) == 0

    # Zero is ignored
    assert module_0.double_the_difference([0, 1]) == 1

    # Mixed case
    assert module_0.double_the_difference([1, -2, 3, 4.5, 0, -5, 7]) == 1 + 9 + 49  # 59

    # Large odd numbers
    assert module_0.double_the_difference([9, 11]) == 81 + 121  # 202

    print("All tests passed!")


test_double_the_difference()

# Generated at 2026-10-24 10:37:16.185195
# Unit test for function double_the_difference
def test_double_the_difference():
    # Basic positive odd numbers
    assert module_0.double_the_difference([1, 3, 5]) == 1 + 9 + 25  # 35

    # Empty list
    assert module_0.double_the_difference([]) == 0

    # Negative numbers are ignored (even negative odds)
    assert module_0.double_the_difference([-1, -3, 5]) == 25
    assert module_0.double_the_difference([-2, -4]) == 0

    # Even numbers are ignored
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Floats are ignored
    assert module_0.double_the_difference([1.5, 3.2, 5]) == 25
    assert module_0.double_the_difference([0.5, 1.5]) == 0

    # Zero is ignored
    assert module_0.double_the_difference([0, 1]) == 1

    # Mixed case
    assert module_0.double_the_difference([1, -2, 3, 4.5, 0, -5, 7]) == 1 + 9 + 49  # 59

    # Large odd numbers
    assert module_0.double_the_difference([9, 11]) == 81 + 121  # 202

    print("All tests passed!")


test_double_the_difference()