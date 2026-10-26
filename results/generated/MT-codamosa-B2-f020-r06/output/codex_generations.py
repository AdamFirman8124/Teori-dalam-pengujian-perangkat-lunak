

# Generated at 2026-10-25 10:38:19.544883
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # output is sorted (smaller, larger) regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # duplicate values -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.0]) == (2.0, 2.0)

    # negative numbers
    assert module_0.find_closest_elements([-1.5, -1.0, 0.0, 1.0]) == (-1.5, -1.0)

    # unsorted list

# Generated at 2026-10-25 10:38:21.963848
# Unit test for function find_closest_elements

# Generated at 2026-10-25 10:38:24.376231
# Unit test for function find_closest_elements

# Generated at 2026-10-25 10:38:25.793226
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: two closest values out of order
    result = module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2), f"Expected (2.0, 2.2), got {result}"

    # Closest pair with duplicates
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2), f"Expected (2.0, 2.2), got {result}"

    # Minimal list of two elements
    result = module_0.find_closest_elements([3.5, 1.2])
    assert result == (1.2, 3.5), f"Expected (1.2, 3.5), got {result}"

    # Exact duplicates are the closest pair
    result = module_0.find_closest_elements([5.0, 5.0, 10.0])
    assert result == (5.0, 5.0), f"Expected (5.0, 5.0), got {result}"

    # Negative numbers
    result = module_0.find_closest_elements([-1.0, -1.1, 5.0])
    assert result == (-1.1, -1.0), f"Expected (-1.1, -1.0), got {result}"

    # Result must be sorted regardless of input order
    result = module_0.find_closest_elements([10.0, 8.0, 8.5])
    assert result == (8.0, 8.5), f"Expected (8.0, 8.5), got {result}"

    # Returned value is a tuple of floats
    result = module_0.find_closest_elements([1.0, 1.5])
    assert isinstance(result, tuple) and len(result) == 2
    assert result == (1.0, 1.5), f"Expected (1.0, 1.5), got {result}"

# Generated at 2026-10-25 10:38:30.433045
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # output is sorted (smaller, larger) regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # duplicate values -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.0]) == (2.0, 2.0)

    # negative numbers
    assert module_0.find_closest_elements([-1.5, -1.0, 0.0, 1.0]) == (-1.5, -1.0)

    # unsorted list

# Generated at 2026-10-25 10:38:31.799065
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # output is sorted (smaller, larger) regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # duplicate values -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.0]) == (2.0, 2.0)

    # negative numbers
    assert module_0.find_closest_elements([-1.5, -1.0, 0.0, 1.0]) == (-1.5, -1.0)

    # unsorted list

# Generated at 2026-10-25 10:38:33.172749
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # output is sorted (smaller, larger) regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # duplicate values -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.0]) == (2.0, 2.0)

    # negative numbers
    assert module_0.find_closest_elements([-1.5, -1.0, 0.0, 1.0]) == (-1.5, -1.0)

    # unsorted list