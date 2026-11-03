

# Generated at 2026-11-02 10:28:06.320586
# Unit test for function can_arrange
def test_can_arrange():
    # Single descending step in an otherwise sorted array
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    # Already sorted arrays return -1
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    # Fully descending arrays return the last index
    assert module_0.can_arrange([3, 2, 1]) == 2
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    # Multiple violations: largest index is returned
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([2, 1, 3, 2, 5]) == 3
    # Violation only at the beginning
    assert module_0.can_arrange([10, 1, 2, 3]) == 1
    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1
    # Equal adjacent values are not violations
    assert module_0.can_arrange([1, 1, 2, 2]) == -1

# Generated at 2026-11-02 10:29:32.911641
# Unit test for function can_arrange
def test_can_arrange():
    # Sorted array -> no index found
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 1, 2, 3]) == -1  # non-decreasing is fine

    # Single drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([2, 1]) == 1

    # Multiple drops -> returns the LAST such index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Duplicates causing a strict decrease
    assert module_0.can_arrange([1, 2, 2, 1]) == 3

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -3]) == 2
    assert module_0.can_arrange([-3, -2, -1]) == -1

# Generated at 2026-11-02 10:30:54.563058
# Unit test for function can_arrange
def test_can_arrange():
# nonce:2f75d13a
    # Last index where element is smaller than its predecessor
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 3, 2, 4, 3]) == 4

    # Sorted arrays return -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 1, 2, 3]) == -1

    # Edge cases: empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1

    # Equal adjacent values do not count (strict comparison)
    assert module_0.can_arrange([3, 3, 2, 2]) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test_can_arrange()

# Generated at 2026-11-02 10:31:50.576514
# Unit test for function can_arrange
def test_can_arrange():
    # Element at index 3 (value 3) is less than its predecessor (4)
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3

    # Sorted array -> no such element
    assert module_0.can_arrange([1, 2, 3]) == -1

    # Multiple violations -> returns the largest index
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3]) == 5

    # Strictly decreasing array -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Violation early, then another later -> later index wins
    assert module_0.can_arrange([2, 1, 4, 3]) == 3

    # Single element -> no predecessor, return -1
    assert module_0.can_arrange([1]) == -1

    # Empty array -> return -1
    assert module_0.can_arrange([]) == -1

    # Equal adjacent values are not violations
    assert module_0.can_arrange([3, 3, 3]) == -1

    # Violation only at the very end
    assert module_0.can_arrange([1, 2, 3, 4, 3]) == 4

    # Violation only at the beginning
    assert module_0.can_arrange([5, 1, 2, 3]) == 1

# Generated at 2026-11-02 10:33:01.748465
# Unit test for function can_arrange
def test_can_arrange():
    # Non-decreasing array -> no descent found
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 2, 3]) == -1

    # Single descent -> index of the drop
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([2, 1]) == 1

    # Multiple descents -> last (largest) index wins
    assert module_0.can_arrange([1, 2, 4, 3, 5, 3, 5, 4]) == 7
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4

    # Strictly decreasing -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    # Equal adjacent elements are not descents
    assert module_0.can_arrange([1, 1, 1, 1]) == -1
    assert module_0.can_arrange([3, 3, 2, 2, 1]) == 4

    # Negative numbers
    assert module_0.can_arrange([-1, -2, -1]) == 1

    # Empty and single-element arrays
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([7]) == -1


if __name__ == "__main__":
    test_can_arrange()
    print("All tests passed.")