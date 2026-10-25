

# Generated at 2026-10-25 04:12:02.620645
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Max at start / middle / end
    assert module_0.max_element([9, 4, 2]) == 9
    assert module_0.max_element([1, 9, 2]) == 9
    assert module_0.max_element([1, 2, 9]) == 9

    # Single element and duplicates
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([4, 4, 4]) == 4

    # Negatives only
    assert module_0.max_element([-3, -1, -7]) == -1

    # Floats mixed with ints
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # Empty list raises IndexError
    try:
        module_0.max_element([])
        assert False, "expected IndexError"
    except IndexError:
        pass

    print("All tests passed.")

# Generated at 2026-10-25 04:12:03.959281
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Max at start / middle / end
    assert module_0.max_element([9, 4, 2]) == 9
    assert module_0.max_element([1, 9, 2]) == 9
    assert module_0.max_element([1, 2, 9]) == 9

    # Single element and duplicates
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([4, 4, 4]) == 4

    # Negatives only
    assert module_0.max_element([-3, -1, -7]) == -1

    # Floats mixed with ints
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # Empty list raises IndexError
    try:
        module_0.max_element([])
        assert False, "expected IndexError"
    except IndexError:
        pass

    print("All tests passed.")

# Generated at 2026-10-25 04:12:06.377921
# Unit test for function max_element

# Generated at 2026-10-25 04:12:08.911559
# Unit test for function max_element

# Generated at 2026-10-25 04:12:11.500345
# Unit test for function max_element

# Generated at 2026-10-25 04:12:14.031693
# Unit test for function max_element

# Generated at 2026-10-25 04:12:16.446561
# Unit test for function max_element

# Generated at 2026-10-25 04:12:18.863601
# Unit test for function max_element

# Generated at 2026-10-25 04:12:21.291559
# Unit test for function max_element

# Generated at 2026-10-25 04:12:23.706353
# Unit test for function max_element

# Generated at 2026-10-25 04:12:26.122396
# Unit test for function max_element