

# Generated at 2026-11-03 01:38:01.530861
# Unit test for function get_positive
def test_get_positive():
    # nonce:900b4839
    # Mixed positive and negative integers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # Mixed with zero and duplicates
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    # All negative numbers
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    # Empty list
    assert module_0.get_positive([]) == []
    # All positive numbers
    assert module_0.get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Zero is not positive
    assert module_0.get_positive([0, 0, 0]) == []
    # Floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]
    # Order preserved
    assert module_0.get_positive([10, -1, 20, -2, 30]) == [10, 20, 30]

# Generated at 2026-11-03 01:39:07.773521
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    
    # Test with all positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    # Test with all negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []
    
    # Test with empty list
    assert module_0.get_positive([]) == []
    
    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, -1]) == [1]
    
    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 0.1]) == [2.5, 0.1]
    
    # Test with duplicates
    assert module_0.get_positive([3, -3, 3, -3]) == [3, 3]
    
    # Test with single element
    assert module_0.get_positive([5]) == [5]
    assert module_0.get_positive([-5]) == []
    
    # Test preserves order
    assert module_0.get_positive([-10, 20, -30, 40, 50]) == [20, 40, 50]

# Generated at 2026-11-03 01:40:44.951914
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0]) == []
    assert module_0.get_positive([-5]) == []
    assert module_0.get_positive([0.5, -0.5, 1.5]) == [0.5, 1.5]

# Generated at 2026-11-03 01:42:58.994738
# Unit test for function get_positive
def test_get_positive():
    # Basic mixed list
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    
    # All positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    # All negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []
    
    # Empty list
    assert module_0.get_positive([]) == []
    
    # Zero is not positive
    assert module_0.get_positive([0, -1, 1]) == [1]
    
    # Duplicates preserved
    assert module_0.get_positive([3, -3, 3]) == [3, 3]
    
    # Floats
    assert module_0.get_positive([-1.5, 2.5, -0.1, 0.1]) == [2.5, 0.1]
    
    # Single element
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

# Generated at 2026-11-03 01:44:08.531195
# Unit test for function get_positive
def test_get_positive():
    # Mixed positive and negative integers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # Includes zero (not positive) and duplicates
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    # All negative numbers
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    # Empty list
    assert module_0.get_positive([]) == []
    # Single zero
    assert module_0.get_positive([0]) == []
    # All positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    # Floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]
    # Large numbers
    assert module_0.get_positive([-1000000, 1000000]) == [1000000]
    print("test_get_positive passed")


if __name__ == "__main__":
    test_get_positive()