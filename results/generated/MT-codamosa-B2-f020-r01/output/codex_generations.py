

# Generated at 2026-10-25 01:49:49.428123
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-10-25 01:49:50.753447
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-10-25 01:49:52.145600
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-10-25 01:49:53.522479
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-10-25 01:49:54.848723
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()