

# Generated at 2026-10-25 09:22:14.016626
# Unit test for function add_elements

# Generated at 2026-10-25 09:22:18.897657
# Unit test for function add_elements
def test_add_elements():
    assert module_0.add_elements([1, -2, 93, 4, 100], 3) == -2 + 93
    assert module_0.add_elements([111, 121], 2) == 0
    assert module_0.add_elements([12, 34, 56], 3) == 102
    assert module_0.add_elements([], 5) == 0
    assert module_0.add_elements([99, 100, -7], 3) == 99
    assert module_0.add_elements([5], 0) == 0

# Generated at 2026-10-25 09:22:25.009385
# Unit test for function add_elements
def test_add_elements():
    # Typical case: first k elements, only 1-2 digit ones summed
    assert module_0.add_elements([1, -2, 18, 123, 76, 100, -1, 2, -5, 77], 5) == 94

    # k larger than array length â uses all elements
    assert module_0.add_elements([10, 20, 30], 10) == 60

    # No qualifying elements
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Single element
    assert module_0.add_elements([5], 1) == 5

    # All elements qualify
    assert module_0.add_elements([11, 22, 33], 3) == 66

    # k = 0 â empty slice, sum is 0
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # Elements beyond k are ignored even if they qualify
    assert module_0.add_elements([99, 100, 99], 2) == 99

    print("All tests passed!")


test_add_elements()

# Generated at 2026-10-25 09:22:26.511126
# Unit test for function add_elements
def test_add_elements():
    # Typical case: first k elements, only 1-2 digit ones summed
    assert module_0.add_elements([1, -2, 18, 123, 76, 100, -1, 2, -5, 77], 5) == 94

    # k larger than array length â uses all elements
    assert module_0.add_elements([10, 20, 30], 10) == 60

    # No qualifying elements
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Single element
    assert module_0.add_elements([5], 1) == 5

    # All elements qualify
    assert module_0.add_elements([11, 22, 33], 3) == 66

    # k = 0 â empty slice, sum is 0
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # Elements beyond k are ignored even if they qualify
    assert module_0.add_elements([99, 100, 99], 2) == 99

    print("All tests passed!")


test_add_elements()

# Generated at 2026-10-25 09:22:27.943304
# Unit test for function add_elements
def test_add_elements():
    # Typical case: first k elements, only 1-2 digit ones summed
    assert module_0.add_elements([1, -2, 18, 123, 76, 100, -1, 2, -5, 77], 5) == 94

    # k larger than array length â uses all elements
    assert module_0.add_elements([10, 20, 30], 10) == 60

    # No qualifying elements
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Single element
    assert module_0.add_elements([5], 1) == 5

    # All elements qualify
    assert module_0.add_elements([11, 22, 33], 3) == 66

    # k = 0 â empty slice, sum is 0
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # Elements beyond k are ignored even if they qualify
    assert module_0.add_elements([99, 100, 99], 2) == 99

    print("All tests passed!")


test_add_elements()

# Generated at 2026-10-25 09:22:29.992848
# Unit test for function add_elements
def test_add_elements():
    # Typical case: first k elements, only 1-2 digit ones summed
    assert module_0.add_elements([1, -2, 18, 123, 76, 100, -1, 2, -5, 77], 5) == 94

    # k larger than array length â uses all elements
    assert module_0.add_elements([10, 20, 30], 10) == 60

    # No qualifying elements
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Single element
    assert module_0.add_elements([5], 1) == 5

    # All elements qualify
    assert module_0.add_elements([11, 22, 33], 3) == 66

    # k = 0 â empty slice, sum is 0
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # Elements beyond k are ignored even if they qualify
    assert module_0.add_elements([99, 100, 99], 2) == 99

    print("All tests passed!")


test_add_elements()