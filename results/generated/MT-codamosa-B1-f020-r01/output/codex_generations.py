

# Generated at 2026-10-24 05:50:50.198813
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Two elements only
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 5.0]) == (-1.5, -1.0)

    # Duplicates â closest pair is equal values
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Ties: first closest pair found in order wins
    assert module_0.find_closest_elements([1.0, 3.0, 5.0, 7.0]) == (1.0, 3.0)

    # Floats with small gaps
    assert module_0.find_closest_elements([0.1, 0.10001, 9.9]) == (0.1, 0.10001)

    print("All tests passed!")


test_find_closest_elements()

# Generated at 2026-10-24 05:50:51.501734
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Two elements only
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 5.0]) == (-1.5, -1.0)

    # Duplicates â closest pair is equal values
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Ties: first closest pair found in order wins
    assert module_0.find_closest_elements([1.0, 3.0, 5.0, 7.0]) == (1.0, 3.0)

    # Floats with small gaps
    assert module_0.find_closest_elements([0.1, 0.10001, 9.9]) == (0.1, 0.10001)

    print("All tests passed!")


test_find_closest_elements()

# Generated at 2026-10-24 05:50:54.025327
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:50:56.442846
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:50:58.853803
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:51:01.266969
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:51:03.681686
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:51:06.096812
# Unit test for function find_closest_elements

# Generated at 2026-10-24 05:51:07.489970
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Two elements only
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 5.0]) == (-1.5, -1.0)

    # Duplicates â closest pair is equal values
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Ties: first closest pair found in order wins
    assert module_0.find_closest_elements([1.0, 3.0, 5.0, 7.0]) == (1.0, 3.0)

    # Floats with small gaps
    assert module_0.find_closest_elements([0.1, 0.10001, 9.9]) == (0.1, 0.10001)

    print("All tests passed!")


test_find_closest_elements()