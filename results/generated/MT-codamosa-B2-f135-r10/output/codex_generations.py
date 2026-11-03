

# Generated at 2026-11-01 21:26:59.017237
# Unit test for function can_arrange
def test_can_arrange():
    # Strictly increasing -> no descent found
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5, 6]) == -1

    # Single descent
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Multiple descents -> return index of the last (largest) one
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    assert module_0.can_arrange([1, 3, 2, 5, 4, 6, 1]) == 6

    # Entirely decreasing -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Equal adjacent elements are not a descent (strict comparison)
    assert module_0.can_arrange([2, 2, 2]) == -1
    assert module_0.can_arrange([1, 1, 2, 2, 3]) == -1

    # Descent involving duplicates
    assert module_0.can_arrange([3, 3, 2]) == 2

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3, -4]) == 3
    assert module_0.can_arrange([-5, -3, -4, -3]) == 3


if __name__ == "__main__":
    test_can_arrange()
    print("All tests passed!")

# Generated at 2026-11-01 21:27:40.399371
# Unit test for function can_arrange
def test_can_arrange():
# nonce:b0da2459
    # Basic example: single inversion at index 3
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted arrays return -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1
    # Fully descending array: last inversion index is returned
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Two-element arrays
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2]) == -1
    # Multiple inversions: largest index wins
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([4, 3, 2, 1, 5, 4]) == 5
    # Equal adjacent values are not counted as inversions
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([1, 2, 2, 1]) == 3
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1
    # Floating point values
    assert module_0.can_arrange([1.5, 1.2]) == 1
    # Longer mixed array
    assert module_0.can_arrange([10, 20, 15, 25, 30, 18, 40]) == 5


if __name__ == "__main__":
    test_can_arrange()
    print("All tests passed!")

# Generated at 2026-11-01 21:28:10.708925
# Unit test for function can_arrange
def test_can_arrange():
    # Array with a single drop: 3 < 4 at index 3
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Already sorted array -> no drop found
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1

    # Multiple drops: should return the largest index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4

    # Strictly decreasing array: every step is a drop, largest index is last
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Empty array -> no index to check
    assert module_0.can_arrange([]) == -1

    # Single element -> no comparison possible
    assert module_0.can_arrange([7]) == -1

    # All equal elements -> no strict decrease
    assert module_0.can_arrange([2, 2, 2, 2]) == -1

    # Drop only at the very end
    assert module_0.can_arrange([1, 2, 3, 4, 3]) == 4

    # Drop only at the beginning
    assert module_0.can_arrange([5, 3, 6, 7, 8]) == 1

    # Array with duplicates followed by a decrease
    assert module_0.can_arrange([1, 1, 2, 2, 1]) == 4

    print("All tests passed!")


test_can_arrange()

# Generated at 2026-11-01 21:28:37.742555
# Unit test for function can_arrange
def test_can_arrange():
    # Array with a single drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted (non-decreasing) array
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Multiple drops: returns the largest index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    # Strictly decreasing array
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single element array
    assert module_0.can_arrange([7]) == -1
    # Two elements, out of order
    assert module_0.can_arrange([2, 1]) == 1
    # Two elements, sorted
    assert module_0.can_arrange([1, 2]) == -1
    # Drop in the middle and near the end
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    # Drop only at the very beginning
    assert module_0.can_arrange([3, 2, 4, 5, 6]) == 1
    # Duplicates are not a drop (strict comparison)
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    # Equal values followed by a drop
    assert module_0.can_arrange([2, 2, 1]) == 2

# Generated at 2026-11-01 21:29:24.643647
# Unit test for function can_arrange
def test_can_arrange():
    # Basic examples
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3   # drop occurs at index 3
    assert module_0.can_arrange([1, 2, 3]) == -1        # already sorted -> -1

    # Single decrease vs multiple decreases (should return LAST occurrence)
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([10, 9, 8, 7]) == 3     # strictly decreasing

    # Edge cases: empty and single-element lists
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Two-element list
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2]) == -1

    # Equal adjacent values are NOT a decrease (strict comparison)
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([1, 2, 2, 1]) == 3

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -1]) == 1
    assert module_0.can_arrange([-3, -2, -1]) == -1

    # Floats
    assert module_0.can_arrange([1.5, 0.5, 2.0]) == 1