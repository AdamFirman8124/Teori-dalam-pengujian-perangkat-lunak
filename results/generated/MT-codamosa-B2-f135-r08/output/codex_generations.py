

# Generated at 2026-11-03 01:15:33.818559
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array - returns -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 2, 3]) == -1

    # Single drop - returns index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Multiple drops - returns the largest index
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([1, 5, 4, 3, 2, 6]) == 4

    # Strictly decreasing array
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Duplicates (non-strict comparisons) - no drop
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    assert module_0.can_arrange([3, 3, 3]) == -1

    # Empty array - loop never runs
    assert module_0.can_arrange([]) == -1

    # Single element - loop never runs
    assert module_0.can_arrange([7]) == -1

    # Alternating pattern
    assert module_0.can_arrange([10, 20, 15, 30, 25, 40]) == 4

    # Negative numbers
    assert module_0.can_arrange([-1, -3, -2, 0]) == 2

    # Floats
    assert module_0.can_arrange([1.5, 2.5, 2.0]) == 2

    # Drop only at the very end
    assert module_0.can_arrange([1, 2, 3, 0]) == 3

# Generated at 2026-11-03 01:16:22.152119
# Unit test for function can_arrange
def test_can_arrange():
    # nonce:7f8bbd39
    # Sorted (ascending) arrays -> -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 2]) == -1
    assert module_0.can_arrange([7]) == -1
    assert module_0.can_arrange([]) == -1

    # Arrays with a disorder point -> index of last drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5

    # Fully descending array -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Duplicates use strict '<' comparison
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    assert module_0.can_arrange([1, 3, 3, 2]) == 3

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1

    # Floats
    assert module_0.can_arrange([1.5, 2.5, 2.0]) == 2


if __name__ == "__main__":
    test_can_arrange()
    print("All tests passed!")

# Generated at 2026-11-03 01:17:26.665531
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array -> no index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 2, 3]) == -1

    # Single inversion
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Largest (rightmost) inversion index should be returned
    assert module_0.can_arrange([1, 3, 5, 6, 7, 4]) == 5
    assert module_0.can_arrange([5, 3, 2, 1]) == 3
    assert module_0.can_arrange([10, 9, 8, 7, 6]) == 4

    # Multiple inversions -> last one wins
    assert module_0.can_arrange([3, 2, 4, 1, 5]) == 3

    # Duplicates with strict inequality: equal neighbors don't count
    assert module_0.can_arrange([1, 2, 3, 4, 5, 6, 6, 6, 6, 7]) == -1
    assert module_0.can_arrange([1, 2, 2, 1]) == 3

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([42]) == -1

    # Two elements
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2]) == -1

    # Negative numbers
    assert module_0.can_arrange([-1, -3, -2]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1

    # Increasing then dropping at the very end
    assert module_0.can_arrange([1, 2, 3, 4, 0]) == 4

# Generated at 2026-11-03 01:18:50.111669
# Unit test for function can_arrange
def test_can_arrange():
    # Case where a decrease occurs at index 3 (4 > 3)
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Strictly increasing array -> no valid index
    assert module_0.can_arrange([1, 2, 3, 4, 5, 6, 7]) == -1
    # Multiple decreases; largest index should be returned (5 > 3 at index 5)
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 4]) == 5
    # Strictly decreasing array -> last index is the answer
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Empty array -> -1
    assert module_0.can_arrange([]) == -1
    # Single element -> -1
    assert module_0.can_arrange([1]) == -1
    # Simple two-element decrease
    assert module_0.can_arrange([2, 1]) == 1
    # Two-element array with no decrease
    assert module_0.can_arrange([1, 2]) == -1
    # Multiple scattered decreases; last one at index 4 (4 > 3)
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    # Decrease only at the very end
    assert module_0.can_arrange([1, 2, 3, 4, 0]) == 4
    # Decrease only at the beginning
    assert module_0.can_arrange([10, 1, 2, 3, 4]) == 1
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -1]) == 2

# Generated at 2026-11-03 01:19:35.486004
# Unit test for function can_arrange
def test_can_arrange():
    # Basic case: single drop in the middle
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted array returns -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5, 6, 7]) == -1
    # Drop near the end
    assert module_0.can_arrange([3, 4, 5, 1, 2]) == 3
    # Multiple drops: returns the largest index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 4]) == 5
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1
    # Simple pair out of order
    assert module_0.can_arrange([2, 1]) == 1
    # Descending array: last index qualifies
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4