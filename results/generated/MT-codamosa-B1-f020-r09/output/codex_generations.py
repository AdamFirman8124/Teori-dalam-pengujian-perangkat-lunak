

# Generated at 2026-10-24 21:34:11.978821
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.5, 4.0]) == (3.5, 4.0)
    assert module_0.find_closest_elements([-10.0, -4.0, -3.0, 7.0]) == (-4.0, -3.0)
    assert module_0.find_closest_elements([5.0, 5.0, 10.0]) == (5.0, 5.0)
    assert module_0.find_closest_elements([9.0, 1.0]) == (1.0, 9.0)
    assert module_0.find_closest_elements([0.1, 0.15, 1.0]) == (0.1, 0.15)

# Generated at 2026-10-24 21:34:20.681285
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([4.0, 1.0, 7.0, 3.5]) == (3.5, 4.0)
    assert module_0.find_closest_elements([-10.0, -3.0, -4.0, 8.0]) == (-4.0, -3.0)
    assert module_0.find_closest_elements([1.5, 1.1, 4.8, 1.2]) == (1.1, 1.2)
    assert module_0.find_closest_elements([5.0, 2.0, 5.0]) == (5.0, 5.0)
    assert module_0.find_closest_elements([-1.0, 1.0]) == (-1.0, 1.0)

# Generated at 2026-10-24 21:34:27.084056
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([-10.0, -3.0, -4.0, 7.0]) == (-4.0, -3.0)
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)
    assert module_0.find_closest_elements([4.5, 2.0, 4.5]) == (4.5, 4.5)

# Generated at 2026-10-24 21:34:34.688942
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([10.0, -5.0, 3.0, 3.1]) == (3.0, 3.1)
    assert module_0.find_closest_elements([5.0, 1.0, 5.0]) == (5.0, 5.0)
    assert module_0.find_closest_elements([-10.0, -3.0, -3.5, 8.0]) == (-3.5, -3.0)
    assert module_0.find_closest_elements([0.1, 100.0]) == (0.1, 100.0)

# Generated at 2026-10-24 21:34:42.458707
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 2.2, 5.0]) == (2.0, 2.2)
    assert module_0.find_closest_elements([-10.0, -3.0, -4.0, 8.0]) == (-4.0, -3.0)
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)
    assert module_0.find_closest_elements([3.5, 1.2, 3.5, 9.0]) == (3.5, 3.5)
    assert module_0.find_closest_elements([0.01, 0.03, 0.02]) == (0.01, 0.02)