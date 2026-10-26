

# Generated at 2026-10-25 12:42:59.225414
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

# Generated at 2026-10-25 12:43:00.666667
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

# Generated at 2026-10-25 12:43:03.192180
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

# Generated at 2026-10-25 12:43:04.830708
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

# Generated at 2026-10-25 12:43:12.943857
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