

# Generated at 2026-11-02 13:58:40.434034
# Unit test for function monotonic
def test_monotonic():
    # Increasing lists
    assert module_0.monotonic([1, 2, 4, 20]) == True
    assert module_0.monotonic([1, 20, 4, 10]) == False
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True  # decreasing
    assert module_0.monotonic([1, 1, 1, 1]) == True       # constant (both)
    assert module_0.monotonic([1, 2, 2, 3]) == True       # non-strictly increasing
    assert module_0.monotonic([5, 5, 4, 4, 1]) == True    # non-strictly decreasing
    assert module_0.monotonic([1, 3, 2, 4]) == False      # mixed
    assert module_0.monotonic([]) == True                 # empty list
    assert module_0.monotonic([42]) == True               # single element
    assert module_0.monotonic([2, 1]) == True             # decreasing pair
    assert module_0.monotonic([1, 2]) == True             # increasing pair
    assert module_0.monotonic([-5, -3, -1]) == True       # negatives increasing
    assert module_0.monotonic([-1, -3, -5]) == True       # negatives decreasing
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True    # floats
    assert module_0.monotonic([3.5, 2.5, 1.5]) == True    # floats decreasing

# Generated at 2026-11-02 14:00:13.143161
# Unit test for function monotonic
def test_monotonic():
    # Increasing sequences
    assert module_0.monotonic([1, 2, 4, 20]) == True
    assert module_0.monotonic([1, 20, 4, 10]) == False

    # Decreasing sequences
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    assert module_0.monotonic([1, 1, 1, 1]) == True  # Equal elements are both increasing and decreasing

    # Mixed (non-monotonic)
    assert module_0.monotonic([5, 3, 4, 2]) == False
    assert module_0.monotonic([1, 3, 2, 4]) == False

    # Edge cases
    assert module_0.monotonic([]) == True          # Empty list is trivially monotonic
    assert module_0.monotonic([7]) == True         # Single element is trivially monotonic
    assert module_0.monotonic([2, 2, 2, 2]) == True  # All equal values
    assert module_0.monotonic([1, 2, 2, 3]) == True  # Non-decreasing with duplicates
    assert module_0.monotonic([5, 5, 4, 3]) == True  # Non-increasing with duplicates
    assert module_0.monotonic([1, 2, 3, 2]) == False # Increase then decrease
    assert module_0.monotonic([-1, -2, -3]) == True  # Negative numbers decreasing
    assert module_0.monotonic([-3, -2, -1]) == True  # Negative numbers increasing
    assert module_0.monotonic([3.5, 2.1, 1.0]) == True  # Floats decreasing
    assert module_0.monotonic([0, 0, -1, -2]) == True   # Zero with negatives

    print("All tests passed!")


if __name__ == "__main__":
    test_monotonic()

# Generated at 2026-11-02 14:02:26.482267
# Unit test for function monotonic
def test_monotonic():
    # Strictly increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Strictly decreasing
    assert module_0.monotonic([4, 1, 0, -10]) == True
    # Not monotonic
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # All equal elements (both non-increasing and non-decreasing)
    assert module_0.monotonic([7, 7, 7]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Non-strict monotonic with duplicates
    assert module_0.monotonic([1, 2, 2, 3]) == True
    assert module_0.monotonic([5, 4, 4, 2]) == True
    # Duplicates break neither direction check incorrectly
    assert module_0.monotonic([1, 2, 2, 1]) == False
    # Two elements
    assert module_0.monotonic([1, 2]) == True
    assert module_0.monotonic([2, 1]) == True
    # Negative numbers
    assert module_0.monotonic([-3, -2, -1]) == True
    assert module_0.monotonic([-1, -2, -3]) == True
    # Floats
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([3.5, 2.5, 3.0]) == False
    # Mixed int/float
    assert module_0.monotonic([1, 1.5, 2]) == True

# Generated at 2026-11-02 14:04:55.823119
# Unit test for function monotonic
def test_monotonic():
# nonce:4786a926
    # Strictly increasing list
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # Strictly decreasing list
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # Non-monotonic list (increases then decreases)
    assert module_0.monotonic([1, 3, 2, 4, 5]) == False
    # Non-monotonic list (decreases then increases)
    assert module_0.monotonic([5, 3, 4, 2, 1]) == False
    # Non-strictly increasing (with duplicates)
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-strictly decreasing (with duplicates)
    assert module_0.monotonic([3, 2, 2, 1]) == True
    # All equal elements
    assert module_0.monotonic([7, 7, 7, 7]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element list
    assert module_0.monotonic([42]) == True
    # Two element increasing
    assert module_0.monotonic([1, 2]) == True
    # Two element decreasing
    assert module_0.monotonic([2, 1]) == True
    # Two element equal
    assert module_0.monotonic([3, 3]) == True
    # Negative numbers increasing
    assert module_0.monotonic([-5, -3, -1, 0]) == True
    # Negative numbers decreasing
    assert module_0.monotonic([0, -1, -3, -5]) == True
    # Mixed positive/negative non-monotonic
    assert module_0.monotonic([-1, 1, -2, 2]) == False
    # Floats increasing
    assert module_0.monotonic([1.1, 2.2, 3.3]) == True
    # Floats non-monotonic
    assert module_0.monotonic([1.1, 3.3, 2.2]) == False