

# Generated at 2026-10-25 12:41:50.485775
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

# Generated at 2026-10-25 12:41:52.124362
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

# Generated at 2026-10-25 12:41:53.681182
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

# Generated at 2026-10-25 12:41:57.141677
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

# Generated at 2026-10-25 12:41:58.664566
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