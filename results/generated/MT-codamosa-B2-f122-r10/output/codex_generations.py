

# Generated at 2026-10-25 10:37:24.253915
# Unit test for function add_elements

# Generated at 2026-10-25 10:37:26.764384
# Unit test for function add_elements
def test_add_elements():assert module_0.add_elements([1, 2, 3, 100, 5], 3) == 6

# Generated at 2026-10-25 10:37:48.519292
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

# Generated at 2026-10-25 10:38:08.280049
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

# Generated at 2026-10-25 10:38:10.699911
# Unit test for function add_elements

# Generated at 2026-10-25 10:38:13.382203
# Unit test for function add_elements

# Generated at 2026-10-25 10:38:15.795635
# Unit test for function add_elements

# Generated at 2026-10-25 10:38:18.211932
# Unit test for function add_elements

# Generated at 2026-10-25 10:38:20.627864
# Unit test for function add_elements

# Generated at 2026-10-25 10:38:23.044502
# Unit test for function add_elements