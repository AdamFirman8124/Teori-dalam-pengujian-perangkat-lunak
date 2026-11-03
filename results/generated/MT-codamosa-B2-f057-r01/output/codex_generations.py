

# Generated at 2026-11-02 17:22:35.178375
# Unit test for function monotonic
def test_monotonic():
    # Increasing list
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing list
    assert module_0.monotonic([4, 1, 0, -10]) == True
    # Not monotonic
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # Non-strictly increasing (equal adjacent elements)
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-strictly decreasing (equal adjacent elements)
    assert module_0.monotonic([5, 4, 4, 2]) == True
    # Empty list is trivially monotonic
    assert module_0.monotonic([]) == True
    # Single element list
    assert module_0.monotonic([7]) == True
    # All elements equal
    assert module_0.monotonic([3, 3, 3]) == True
    # Two elements increasing
    assert module_0.monotonic([1, 2]) == True
    # Two elements decreasing
    assert module_0.monotonic([2, 1]) == True
    # Negative numbers increasing
    assert module_0.monotonic([-5, -3, -1]) == True
    # Negative numbers decreasing
    assert module_0.monotonic([-1, -3, -5]) == True
    # Floats increasing
    assert module_0.monotonic([1.1, 2.2, 3.3]) == True
    # Floats not monotonic
    assert module_0.monotonic([1.1, 3.3, 2.2]) == False
    # Mixed types (ints and floats)
    assert module_0.monotonic([1, 1.5, 2]) == True
    # Strings increasing
    assert module_0.monotonic(['a', 'b', 'c']) == True
    # Strings not monotonic
    assert module_0.monotonic(['a', 'c', 'b']) == False

# Generated at 2026-11-02 17:23:58.402510
# Unit test for function monotonic
def test_monotonic():
    # Increasing sequence
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing sequence
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Non-monotonic sequence
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Duplicates with increase
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Duplicates with decrease
    assert module_0.monotonic([3, 2, 2, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2]) == False
    assert module_0.monotonic([2, 1, 3]) == False
    # Single element
    assert module_0.monotonic([5]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Two elements
    assert module_0.monotonic([1, 2]) == True
    assert module_0.monotonic([2, 1]) == True
    # All equal elements
    assert module_0.monotonic([7, 7, 7]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, -1]) == True
    assert module_0.monotonic([-1, -3, -2]) == False
    # Floats
    assert module_0.monotonic([1.1, 2.2, 3.3]) == True
    assert module_0.monotonic([3.3, 2.2, 1.1]) == True
    assert module_0.monotonic([1.1, 3.3, 2.2]) == False

# Generated at 2026-11-02 17:26:44.782682
# Unit test for function monotonic
def test_monotonic():
    # Increasing list
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing list
    assert module_0.monotonic([20, 4, 2, 1]) == True
    # Non-monotonic list
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # List with equal adjacent elements (increasing)
    assert module_0.monotonic([4, 4, 5, 6, 7]) == True
    # List with equal adjacent elements (decreasing)
    assert module_0.monotonic([7, 6, 5, 4, 4]) == True
    # All elements equal
    assert module_0.monotonic([3, 3, 3, 3]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Two elements increasing
    assert module_0.monotonic([1, 2]) == True
    # Two elements decreasing
    assert module_0.monotonic([2, 1]) == True
    # Two elements equal
    assert module_0.monotonic([2, 2]) == True
    # Negative numbers increasing
    assert module_0.monotonic([-5, -3, 0, 2]) == True
    # Negative numbers decreasing
    assert module_0.monotonic([2, 0, -3, -5]) == True
    # Mixed positive/negative non-monotonic
    assert module_0.monotonic([-1, 3, -2, 5]) == False
    # Floats increasing
    assert module_0.monotonic([1.1, 2.2, 3.3]) == True
    # Floats non-monotonic
    assert module_0.monotonic([1.5, 0.5, 2.5]) == False
    # Duplicates break strictness but monotonic still holds
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Peak in middle
    assert module_0.monotonic([1, 2, 3, 2, 1]) == False
    # Valley in middle
    assert module_0.monotonic([3, 2, 1, 2, 3]) == False

# Generated at 2026-11-02 17:28:22.227659
# Unit test for function monotonic
def test_monotonic():
    # Increasing list
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing list
    assert module_0.monotonic([20, 4, 2, 1]) == True
    # Non-monotonic list
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # List with equal consecutive elements (still monotonic)
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Two elements
    assert module_0.monotonic([1, 2]) == True
    assert module_0.monotonic([2, 1]) == True
    assert module_0.monotonic([2, 2]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, 0, 7]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    # Floats
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([3.5, 2.5, 1.5]) == True
    assert module_0.monotonic([1.5, 3.5, 2.5]) == False
    # Strings
    assert module_0.monotonic(["a", "b", "c"]) == True
    assert module_0.monotonic(["c", "b", "a"]) == True
    assert module_0.monotonic(["a", "c", "b"]) == False

# Generated at 2026-11-02 17:29:53.882499
# Unit test for function monotonic
def test_monotonic():
    # Increasing list
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing list
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 20, 4, 10]) == False
    assert module_0.monotonic([1, 3, 2]) == False
    # Non-strict module_0.monotonic(duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) == True
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Constant list
    assert module_0.monotonic([1, 1, 1, 1]) == True
    assert module_0.monotonic([5, 5]) == True
    # Edge cases: empty and single-element lists
    assert module_0.monotonic([]) == True
    assert module_0.monotonic([7]) == True
    # Negative numbers
    assert module_0.monotonic([-1, -2, -3]) == True
    assert module_0.monotonic([-1, -3, -2]) == False
    # Floats
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([3.5, 2.5, 2.5, 1.0]) == True
    # Strings
    assert module_0.monotonic(["a", "b", "c"]) == True
    assert module_0.monotonic(["a", "c", "b"]) == False


if __name__ == "__main__":
    test_monotonic()
    print("All tests passed!")