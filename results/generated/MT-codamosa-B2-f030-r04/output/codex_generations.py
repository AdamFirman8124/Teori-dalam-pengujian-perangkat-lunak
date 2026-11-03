

# Generated at 2026-11-01 20:02:39.640945
# Unit test for function get_positive
def test_get_positive():
    # nonce:d3829bec
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

# Generated at 2026-11-01 20:03:07.761619
# Unit test for function get_positive
def test_get_positive():
    # Basic mixed positive/negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # All positive numbers remain unchanged (order preserved)
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]

    # All negative numbers -> empty list
    assert module_0.get_positive([-1, -2, -3]) == []

    # Empty input list
    assert module_0.get_positive([]) == []

    # Zero is not positive
    assert module_0.get_positive([0, -0]) == []

    # Floats are handled correctly
    assert module_0.get_positive([-2.5, 3.7, -0.1, 0.5]) == [3.7, 0.5]

    # Duplicates are preserved
    assert module_0.get_positive([1, 1, -1, 2, 2]) == [1, 1, 2, 2]

    # Result type is a list
    result = module_0.get_positive([1, -2, 3])
    assert isinstance(result, list)


if __name__ == "__main__":
    test_get_positive()
    print("All tests passed!")

# Generated at 2026-11-01 20:03:44.726015
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([0]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([-1.5, 2.5, -3.5, 4.5]) == [2.5, 4.5]
    assert module_0.get_positive([-1, -2, 3, -4, 5, 6, -7, 8]) == [3, 5, 6, 8]

# Generated at 2026-11-01 20:04:35.009451
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    
    # Test with all positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    # Test with all negative numbers
    assert module_0.get_positive([-1, -2, -3, -4]) == []
    
    # Test with empty list
    assert module_0.get_positive([]) == []
    
    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, -1, 0, 3]) == [1, 3]
    
    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.3, 4.7]) == [2.5, 4.7]
    
    # Test with single element
    assert module_0.get_positive([5]) == [5]
    assert module_0.get_positive([-5]) == []

# Generated at 2026-11-01 20:04:52.623924
# Unit test for function get_positive
def test_get_positive():
    # nonce:242e97de
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -3]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([0]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]