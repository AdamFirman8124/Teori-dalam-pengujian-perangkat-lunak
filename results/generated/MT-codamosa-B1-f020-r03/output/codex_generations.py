

# Generated at 2026-10-24 12:00:14.763239
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic case from spec: 3.9 and 4.0 are closest (distance 0.1)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # order of input should not matter, output is sorted (smaller, larger)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 4.5, 1.0]) == (4.5, 5.0)

    # equally spaced -> first encountered pair wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # duplicates -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # negative numbers
    assert module_0.find_closest_elements([-5.0, -4.9, 10.0, 0.0]) == (-5.0, -4.9)
    assert module_0.find_closest_elements([-1.5, -0.5, 0.0]) == (-0.5, 0.0)

    # unsorted list
    assert module_0.find_closest_elements([10.5, 8.2, 8.0, 12.0]) == (8.0, 8.2)

    # result properties: tuple of 2, sorted
    result = module_0.find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (4.0, 5.0)

# Generated at 2026-10-24 12:00:16.196180
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic case from spec: 3.9 and 4.0 are closest (distance 0.1)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # order of input should not matter, output is sorted (smaller, larger)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 4.5, 1.0]) == (4.5, 5.0)

    # equally spaced -> first encountered pair wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # duplicates -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # negative numbers
    assert module_0.find_closest_elements([-5.0, -4.9, 10.0, 0.0]) == (-5.0, -4.9)
    assert module_0.find_closest_elements([-1.5, -0.5, 0.0]) == (-0.5, 0.0)

    # unsorted list
    assert module_0.find_closest_elements([10.5, 8.2, 8.0, 12.0]) == (8.0, 8.2)

    # result properties: tuple of 2, sorted
    result = module_0.find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (4.0, 5.0)

# Generated at 2026-10-24 12:00:17.566196
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic case from spec: 3.9 and 4.0 are closest (distance 0.1)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # order of input should not matter, output is sorted (smaller, larger)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 4.5, 1.0]) == (4.5, 5.0)

    # equally spaced -> first encountered pair wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # duplicates -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # negative numbers
    assert module_0.find_closest_elements([-5.0, -4.9, 10.0, 0.0]) == (-5.0, -4.9)
    assert module_0.find_closest_elements([-1.5, -0.5, 0.0]) == (-0.5, 0.0)

    # unsorted list
    assert module_0.find_closest_elements([10.5, 8.2, 8.0, 12.0]) == (8.0, 8.2)

    # result properties: tuple of 2, sorted
    result = module_0.find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (4.0, 5.0)

# Generated at 2026-10-24 12:00:18.970191
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic case from spec: 3.9 and 4.0 are closest (distance 0.1)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # order of input should not matter, output is sorted (smaller, larger)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 4.5, 1.0]) == (4.5, 5.0)

    # equally spaced -> first encountered pair wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # duplicates -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # negative numbers
    assert module_0.find_closest_elements([-5.0, -4.9, 10.0, 0.0]) == (-5.0, -4.9)
    assert module_0.find_closest_elements([-1.5, -0.5, 0.0]) == (-0.5, 0.0)

    # unsorted list
    assert module_0.find_closest_elements([10.5, 8.2, 8.0, 12.0]) == (8.0, 8.2)

    # result properties: tuple of 2, sorted
    result = module_0.find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (4.0, 5.0)

# Generated at 2026-10-24 12:00:21.661760
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # basic case from spec: 3.9 and 4.0 are closest (distance 0.1)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # only two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # order of input should not matter, output is sorted (smaller, larger)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 4.5, 1.0]) == (4.5, 5.0)

    # equally spaced -> first encountered pair wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # duplicates -> distance 0
    assert module_0.find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # negative numbers
    assert module_0.find_closest_elements([-5.0, -4.9, 10.0, 0.0]) == (-5.0, -4.9)
    assert module_0.find_closest_elements([-1.5, -0.5, 0.0]) == (-0.5, 0.0)

    # unsorted list
    assert module_0.find_closest_elements([10.5, 8.2, 8.0, 12.0]) == (8.0, 8.2)

    # result properties: tuple of 2, sorted
    result = module_0.find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (4.0, 5.0)