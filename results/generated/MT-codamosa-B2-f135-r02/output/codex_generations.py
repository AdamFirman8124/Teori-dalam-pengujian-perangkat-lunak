

# Generated at 2026-11-03 06:06:56.456384
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array: no element smaller than its predecessor
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1

    # Single violation at index 3 (3 < 4)
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Strictly decreasing: last violation is the final index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Multiple violations: largest index wins
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([3, 1, 2, 4, 0]) == 4

    # Empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1

    # Equal adjacent elements are not violations
    assert module_0.can_arrange([1, 1, 2, 2]) == -1

    # Duplicate followed by a descent
    assert module_0.can_arrange([2, 2, 1]) == 2

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1

    # Descents with mixed positives/negatives
    assert module_0.can_arrange([0, -1, 1, -2]) == 3

# Generated at 2026-11-03 06:08:25.849611
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array returns -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 4, 5, 6]) == -1
    assert module_0.can_arrange([1, 1, 1, 1]) == -1

    # Single drop found at last occurrence
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 4]) == 5

    # Strictly decreasing array: last index is the answer
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([2, 1]) == 1

    # Equal elements are not considered a drop
    assert module_0.can_arrange([3, 3, 2, 2, 1]) == 4
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1

# Generated at 2026-11-03 06:10:13.063090
# Unit test for function can_arrange
def test_can_arrange():
    # index where arr[i] < arr[i-1] exists
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 4, -1]) == 4
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([3, 3, 2, 2]) == 2
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5, 4]) == 6

    # no index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 2, 2, 3, 3, 4]) == -1

    # edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1

# Generated at 2026-11-03 06:11:56.189141
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array - no drop found
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Array with a single drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Array with multiple drops - returns last drop index
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    # Completely reversed array
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single element array
    assert module_0.can_arrange([1]) == -1
    # Two elements out of order
    assert module_0.can_arrange([2, 1]) == 1
    # Equal adjacent elements are not drops
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    # Drop after equal elements
    assert module_0.can_arrange([1, 2, 2, 1]) == 3
    # Negative numbers
    assert module_0.can_arrange([-1, -3, -2, 0]) == 2
    assert module_0.can_arrange([-5, -4, -3, -2]) == -1
    # Drop at the very end
    assert module_0.can_arrange([1, 2, 3, 0]) == 3

# Generated at 2026-11-03 06:13:33.158116
# Unit test for function can_arrange
def test_can_arrange():
    # Descending pair in middle
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted array returns -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    # Largest index of a drop is returned
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5
    # Equal adjacent elements do not count as a drop
    assert module_0.can_arrange([1, 1]) == -1
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    # Simple swap at the start
    assert module_0.can_arrange([2, 1]) == 1
    # Fully descending array returns last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Multiple drops, last one wins
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    # Duplicates before drops
    assert module_0.can_arrange([3, 3, 2, 2, 1]) == 4
    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1