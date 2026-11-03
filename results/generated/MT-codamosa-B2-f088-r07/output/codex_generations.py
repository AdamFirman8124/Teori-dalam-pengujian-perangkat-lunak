

# Generated at 2026-11-02 11:43:17.089721
# Unit test for function sort_array
def test_sort_array():
# nonce:1ba0d681
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]

    # First + last is odd (2 + 5 = 7) -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # First + last is even (2 + 6 = 8) -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # First + last is odd (2 + 1 = 3) -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # First + last is odd (15 + 0 = 15) -> ascending
    assert module_0.sort_array([15, 42, 87, 32, 11, 0]) == [0, 11, 15, 32, 42, 87]

    # First + last is even (21 + 11 = 32) -> descending
    assert module_0.sort_array([21, 14, 23, 11]) == [23, 21, 14, 11]


if __name__ == "__main__":
    test_sort_array()
    print("All tests passed!")

# Generated at 2026-11-02 11:44:36.526262
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([7]) == [7]

    # Sum of first and last element is odd -> sort ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]                            # 2+1=3 (odd)
    assert module_0.sort_array([5, 2, 8, 1, 4]) == [1, 2, 4, 5, 8]          # 5+4=9 (odd)

    # Sum of first and last element is even -> sort descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 (even)
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                          # 1+3=4 (even)
    assert module_0.sort_array([2, 4, 1, 3, 8]) == [8, 4, 3, 2, 1]              # 2+8=10 (even)

    # Arrays with duplicates
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]                          # 1+1=2 (even)
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]                    # 3+2=5 (odd)

    # Arrays with negative numbers
    assert module_0.sort_array([-1, -5, -3]) == [-1, -3, -5]                    # -1+-5=-6 (even)
    assert module_0.sort_array([-3, 4, 1]) == [4, 1, -3]                        # -3+1=-2 (even)


if __name__ == "__main__":
    test_sort_array()
    print("All tests passed!")

# Generated at 2026-11-02 11:45:45.086377
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single-element arrays
    assert module_0.sort_array([5]) == [5]   # 5+5=10 (even) -> descending
    assert module_0.sort_array([0]) == [0]   # 0+0=0 (even) -> descending

    # First + last is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7
    assert module_0.sort_array([2, 1]) == [1, 2]                            # 2+1=3
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]                # 1+4=5
    assert module_0.sort_array([-1, -3, -5, 2]) == [-5, -3, -1, 2]          # -1+2=1

    # First + last is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]                          # 1+3=4
    assert module_0.sort_array([5, 3, 1]) == [5, 3, 1]                          # 5+1=6
    assert module_0.sort_array([3, 1, 2, 3]) == [3, 3, 2, 1]                    # 3+3=6
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]                    # -2+-4=-6

    # Original array must not be modified (uses sorted(), not sort())
    original = [3, 1, 2]
    module_0.sort_array(original)  # 3+2=5 (odd) -> ascending
    assert original == [3, 1, 2]


if __name__ == "__main__":
    test_sort_array()
    print("All tests passed!")

# Generated at 2026-11-02 11:48:14.223185
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single-element arrays return as-is
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Sum of first and last element is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 (odd)
    assert module_0.sort_array([5, 3, 2, 8]) == [2, 3, 5, 8]                  # 5+8=13 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]                              # 2+1=3 (odd)
    assert module_0.sort_array([2, 2, 3, 3]) == [2, 2, 3, 3]                  # 2+3=5 (odd)

    # Sum of first and last element is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 (even)
    assert module_0.sort_array([3, 6, 5]) == [6, 5, 3]                        # 3+5=8 (even)
    assert module_0.sort_array([1, 1]) == [1, 1]                              # 1+1=2 (even)
    assert module_0.sort_array([4, 2, 9, 6]) == [9, 6, 4, 2]                  # 4+6=10 (even)

    # Negative numbers
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]                  # -2+-4=-6 (even)
    assert module_0.sort_array([-1, -5, 2]) == [-5, -1, 2]                    # -1+2=1 (odd)

    # Original array is not mutated
    original = [3, 1, 2]
    result = module_0.sort_array(original)
    assert original == [3, 1, 2]
    assert result == [1, 2, 3]

    print("All sort_array tests passed!")


test_sort_array()

# Generated at 2026-11-02 11:49:57.088468
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns an empty list
    assert module_0.sort_array([]) == []

    # Sum of first and last element is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 1]) == [1, 2, 3, 4]      # 2+1=3 (odd)
    assert module_0.sort_array([1, 2]) == [1, 2]                  # 1+2=3 (odd)
    assert module_0.sort_array([5, 2, 1, 4]) == [1, 2, 4, 5]      # 5+4=9 (odd)
    assert module_0.sort_array([3, 1, 1, 2]) == [1, 1, 2, 3]      # 3+2=5 (odd)
    assert module_0.sort_array([0, 1]) == [0, 1]                  # 0+1=1 (odd)

    # Sum of first and last element is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0]) == [4, 3, 2, 0]      # 2+0=2 (even)
    assert module_0.sort_array([5, 2, 1, 3]) == [5, 3, 2, 1]      # 5+3=8 (even)
    assert module_0.sort_array([1, 3]) == [3, 1]                  # 1+3=4 (even)
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]            # 1+3=4 (even)