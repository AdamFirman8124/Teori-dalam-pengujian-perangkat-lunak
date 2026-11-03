

# Generated at 2026-11-02 14:40:59.419225
# Unit test for function can_arrange
def test_can_arrange():
# nonce:1a213e1b
    # Single out-of-order element in the middle
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Already sorted array -> -1
    assert module_0.can_arrange([1, 2, 3]) == -1

    # Out-of-order element at the end
    assert module_0.can_arrange([1, 2, 4, 5, 3]) == 4

    # Strictly decreasing array -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Two-element violation
    assert module_0.can_arrange([2, 1]) == 1

    # Multiple violations -> largest index is returned
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 4]) == 5

    # Empty array
    assert module_0.can_arrange([]) == -1

    # Single-element array
    assert module_0.can_arrange([7]) == -1

    # Equal adjacent elements are not violations
    assert module_0.can_arrange([1, 1, 1]) == -1

    # Violation right at the start
    assert module_0.can_arrange([4, 3, 5]) == 1

    # Duplicates mixed with drops
    assert module_0.can_arrange([3, 3, 2, 2, 1]) == 4

# Generated at 2026-11-02 14:42:23.081997
# Unit test for function can_arrange
def test_can_arrange():
    # nonce:105b9c22
    # Sorted (non-decreasing) arrays -> -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1
    assert module_0.can_arrange([1, 1, 1]) == -1  # equal elements are not violations

    # Single violation -> index of the drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([3, 1]) == 1

    # Multiple violations -> largest index wins
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7, 9, 10]) == 5
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([1, 2, 2, 1]) == 3

    # Violation at the last position
    assert module_0.can_arrange([1, 2, 3, 1]) == 3

    # Negative numbers
    assert module_0.can_arrange([-1, -2, 0]) == 1
    assert module_0.can_arrange([-3, -2, -1]) == -1

    print("test_can_arrange passed")

# Generated at 2026-11-02 14:44:57.652198
# Unit test for function can_arrange
def test_can_arrange():
    # Array with a single drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted array
    assert module_0.can_arrange([1, 2, 3]) == -1
    # Multiple drops, returns last drop index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 7]) == 5
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single element array
    assert module_0.can_arrange([5]) == -1
    # Strictly decreasing array
    assert module_0.can_arrange([3, 2, 1]) == 2
    # All equal elements
    assert module_0.can_arrange([1, 1, 1]) == -1
    # Multiple drops scattered
    assert module_0.can_arrange([2, 1, 3, 2, 5, 4]) == 5

# Generated at 2026-11-02 14:47:25.285837
# Unit test for function can_arrange
def test_can_arrange():
    # Array with a single drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Sorted array returns -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    # Last index of a drop is preferred (largest index wins)
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    # Strictly decreasing array: last index returned
    assert module_0.can_arrange([3, 2, 1]) == 2
    # Empty array
    assert module_0.can_arrange([]) == -1
    # Single element array
    assert module_0.can_arrange([5]) == -1
    # Equal adjacent elements are not a drop
    assert module_0.can_arrange([2, 2, 2]) == -1
    # Two elements, descending
    assert module_0.can_arrange([5, 4]) == 1
    # Two elements, ascending
    assert module_0.can_arrange([4, 5]) == -1
    # Drop early, sorted afterwards
    assert module_0.can_arrange([10, 1, 2, 3, 4]) == 1
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -1, -3]) == 3
    print("All tests passed!")

test_can_arrange()

# Generated at 2026-11-02 14:48:23.034252
# Unit test for function can_arrange
def test_can_arrange():
    # Single violation in otherwise sorted array -> index 3 (3 < 4)
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Sorted array -> no violation
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Fully descending array -> last index is the largest violation
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Multiple violations -> latest one is returned
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    # Two elements
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 2]) == -1
    # Single element and empty array
    assert module_0.can_arrange([7]) == -1
    assert module_0.can_arrange([]) == -1
    # Equal neighbors are not a descent
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([1, 2, 2, 1]) == 3
    # Duplicates mixed with descents
    assert module_0.can_arrange([1, 5, 4, 4, 3]) == 4
    assert module_0.can_arrange([3, 3, 2]) == 2
    # Negative numbers
    assert module_0.can_arrange([-1, -2, -1]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1
    assert module_0.can_arrange([0, -5, -6, 10, 9]) == 4