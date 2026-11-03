

# Generated at 2026-11-03 05:21:32.069209
# Unit test for function can_arrange
def test_can_arrange():
    # Already sorted (non-decreasing) array -> no descent found
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 1, 2, 2, 3]) == -1

    # Single descent
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Multiple descents -> returns the largest index where arr[i] < arr[i-1]
    assert module_0.can_arrange([3, 2, 4, 1, 5]) == 3
    assert module_0.can_arrange([1, 5, 4, 3, 6, 2]) == 5

    # Strictly decreasing array -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Two elements
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2]) == -1

    # Descent near the beginning
    assert module_0.can_arrange([9, 1, 2, 3]) == 1

    # Array with duplicates followed by a smaller value
    assert module_0.can_arrange([1, 3, 3, 2, 4]) == 3

# Generated at 2026-11-03 05:23:40.597628
# Unit test for function can_arrange
def test_can_arrange():
    # No inversion: sorted ascending array
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Single inversion in middle
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Multiple inversions: should return the largest index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5
    # Strictly descending array: inversion at every step, largest index returned
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Inversion at the very first possible position only
    assert module_0.can_arrange([2, 1, 3, 4, 5]) == 1
    # Inversion at the last position
    assert module_0.can_arrange([1, 2, 3, 5, 4]) == 4
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single-element array
    assert module_0.can_arrange([1]) == -1
    # Two-element array with inversion
    assert module_0.can_arrange([2, 1]) == 1
    # Two-element array without inversion
    assert module_0.can_arrange([1, 2]) == -1
    # Equal adjacent elements are not inversions (strict comparison)
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    # Duplicates with a real inversion
    assert module_0.can_arrange([1, 2, 2, 1]) == 3
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1
    # Later inversion overrides earlier one (largest index wins)
    assert module_0.can_arrange([10, 1, 20, 2, 30, 3]) == 5

    print("All tests passed!")


test_can_arrange()

# Generated at 2026-11-03 05:25:33.945994
# Unit test for function can_arrange
def test_can_arrange():
    # Standard case: array drops once
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Sorted array: no descent, returns -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Multiple descents: returns the largest index of a descent
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    # Strictly decreasing array: every index qualifies, last one returned
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single element
    assert module_0.can_arrange([1]) == -1
    # Equal elements are not a descent
    assert module_0.can_arrange([3, 3, 3]) == -1
    # Alternating values
    assert module_0.can_arrange([2, 1, 2, 1, 2]) == 3
    # Descent after duplicates
    assert module_0.can_arrange([1, 1, 2, 1]) == 3
    # Larger sorted values
    assert module_0.can_arrange([10, 20, 30, 40]) == -1
    # Descent in the middle of larger array
    assert module_0.can_arrange([1, 2, 3, 4, 5, 3, 7, 9, 10]) == 5

# Generated at 2026-11-03 05:27:16.429889
# Unit test for function can_arrange
def test_can_arrange():
    # No drop in ascending array
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Single element or empty array
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1
    # Strictly decreasing array - largest drop index returned
    assert module_0.can_arrange([3, 2, 1]) == 2
    # Multiple drops, should return the largest index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5
    # Drop only at the beginning
    assert module_0.can_arrange([5, 4, 6, 7, 8]) == 1
    # Drop only at the end
    assert module_0.can_arrange([1, 2, 3, 5, 4]) == 4
    # Equal adjacent elements do not count as drops
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3, -2]) == 3
    # Mixed positive/negative
    assert module_0.can_arrange([0, -1, 1, -2]) == 3

    print("All tests passed!")

test_can_arrange()

# Generated at 2026-11-03 05:29:32.958918
# Unit test for function can_arrange
def test_can_arrange():
    # nonce:dac4a06c
    # Sorted array - no inversion exists
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 4, 5]) == -1

    # Single inversion at index 3
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Multiple inversions - returns the largest such index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Inversion early in array, rest sorted
    assert module_0.can_arrange([2, 1, 3, 4, 5]) == 1

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Equal neighbors are not strict inversions
    assert module_0.can_arrange([1, 1, 1]) == -1

    # Negative numbers
    assert module_0.can_arrange([-2, -1, -3]) == 2
    assert module_0.can_arrange([-1, -3, -2]) == 1


test_can_arrange()