

# Generated at 2026-11-03 04:55:10.765692
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
    assert module_0.get_positive([3, -3, 3, 3]) == [3, 3, 3]

    # Test preserving order
    assert module_0.get_positive([5, -2, 1, -8, 9]) == [5, 1, 9]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_positive()

# Generated at 2026-11-03 04:57:06.081838
# Unit test for function get_positive
def test_get_positive():import pytest


def test_get_positive_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]


def test_get_positive_all_positive():
    """Test with all positive numbers."""
    assert module_0.get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_get_positive_all_negative():
    """Test with all negative numbers."""
    assert module_0.get_positive([-1, -2, -3, -4, -5]) == []


def test_get_positive_empty_list():
    """Test with an empty list."""
    assert module_0.get_positive([]) == []


def test_get_positive_with_zero():
    """Test that zero is excluded (not strictly positive)."""
    assert module_0.get_positive([0, 1, -1, 0, 2]) == [1, 2]


def test_get_positive_with_floats():
    """Test with float values."""
    assert module_0.get_positive([-1.5, 2.5, 0.1, -0.3]) == [2.5, 0.1]


def test_get_positive_duplicates():
    """Test that duplicates are preserved."""
    assert module_0.get_positive([3, -3, 3, 3, -7]) == [3, 3, 3]


def test_get_positive_large_numbers():
    """Test with very large numbers."""
    assert module_0.get_positive([-10**18, 10**18]) == [10**18]


def test_get_positive_returns_list():
    """Test that the return type is a list."""
    result = module_0.get_positive([1, -2])
    assert isinstance(result, list)

# Generated at 2026-11-03 04:59:47.667478
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, -1, 0.5]) == [0.5]
    assert module_0.get_positive([-1.5, 2.5, -3.5, 4.5]) == [2.5, 4.5]

# Generated at 2026-11-03 05:02:00.586457
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

    # Test with all positive numbers
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # Test with all negative numbers
    assert module_0.get_positive([-1, -2, -3, -4]) == []

    # Test with empty list
    assert module_0.get_positive([]) == []

    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, 0, -1]) == [1]

    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]

    # Test with single element
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

    # Test preserves order
    assert module_0.get_positive([3, -1, 2, -5, 1]) == [3, 2, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_positive()

# Generated at 2026-11-03 05:03:39.412878
# Unit test for function get_positive
def test_get_positive():
    # Mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    
    # Empty list
    assert module_0.get_positive([]) == []
    
    # All negative numbers
    assert module_0.get_positive([-1, -2, -3, -4]) == []
    
    # All positive numbers
    assert module_0.get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Zero is not positive
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([-1, 0, 1]) == [1]
    
    # Floating point numbers
    assert module_0.get_positive([-1.5, 2.5, -3.7, 0.1]) == [2.5, 0.1]
    
    # Single element
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []
    
    # Duplicates preserved
    assert module_0.get_positive([3, 3, -3, 3]) == [3, 3, 3]