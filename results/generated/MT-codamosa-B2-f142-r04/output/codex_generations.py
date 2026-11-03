

# Generated at 2026-11-02 17:20:06.162055
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 divisible by 3 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Basic case: only index 0 is special
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1**2 + 2 + 3

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 divisible by 4 (not by 3) -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Negative numbers: squares positive, cubes negative
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Mixed case
    assert module_0.sum_squares([5, 8, 3, 4, 6, 9, 2]) == 25 + 8 + 3 + 16 + 216 + 9 + 2

    # Index 12 divisible by both 3 and 4 -> squared (elif not reached)
    assert module_0.sum_squares([0] * 12 + [2]) == 4

    # Index 8 divisible by 4 (not 3) -> cubed
    assert module_0.sum_squares([0] * 8 + [3]) == 27

    # Longer list with all branch types
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    expected = (1**2 + 2 + 3 + 4**2 + 5**3 + 6 + 7 + 8**2 + 9**2
                + 10 + 11 + 12**2 + 13)
    assert module_0.sum_squares(lst) == expected

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 17:21:42.479165
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 is divisible by 3 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Basic case: indices 0,1,2
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1**2 + 2 + 3 = 6

    # Index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # 147

    # Longer list covering indices 0..11
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = (1**2 + 2 + 3 + 4**2 + 5**3 + 6 +
                7**2 + 8 + 9**3 + 10**2 + 11**3 + 12)
    assert module_0.sum_squares(lst) == expected  # 2382

    # Index 12 is divisible by both 3 and 4 -> should be squared (not cubed)
    lst = [2] * 13
    # indices 0,3,6,9,12 squared: 5 * 4 = 20; others unchanged: 8 * 2 = 16
    assert module_0.sum_squares(lst) == 36

    # Negative numbers
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 - 3  # -4

    # Non-integer values
    assert module_0.sum_squares([1.5, 2.0, 3.0]) == 1.5**2 + 2.0 + 3.0

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 17:23:17.854112
# Unit test for function sum_squares
def test_sum_squares():
    # Basic case: index 0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # Indices divisible by 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 147

    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Single element (index 0) gets squared
    assert module_0.sum_squares([5]) == 25

    # Negative numbers: squares stay positive, others stay negative
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 - 3  # -4

    # Longer list covering all branches, including index 12 (divisible by 12 -> squared, not cubed)
    lst = [2] * 13
    expected = (2**2 + 2 + 2 + 2**2 + 2**3 + 2**2 + 2**2 + 2 + 2**3 +
                2**2 + 2 + 2**2 + 2**2)  # 52
    assert module_0.sum_squares(lst) == expected

    # Index 8 (divisible by 4, not by 3) gets cubed
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 3]) == 1*7 + 3**3  # 34

    # Index 6 (divisible by 3) gets squared, not cubed
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 4]) == 6 + 4**2  # 22

    # Mixed values
    assert module_0.sum_squares([3, -5, 7, 2, 4]) == 3**2 - 5 + 7 + 2**2 + 4**3  # 97

    print("All test cases passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-02 17:25:13.312484
# Unit test for function sum_squares
def test_sum_squares():
    # index 0 is a multiple of 3 -> squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # index 3 is a multiple of 3 -> squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 1**2 + 3 + 5 + 7**2  # 58

    # index 4 is a multiple of 4 (and not 3) -> cubed
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-5)**3  # -126

    # empty list -> 0
    assert module_0.sum_squares([]) == 0

    # single element at index 0 -> squared
    assert module_0.sum_squares([4]) == 16

    # indices 0,3,6,9,12 squared (12 is multiple of both 3 and 4 -> square wins),
    # indices 4 and 8 cubed, others unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1231

    # works with floats
    assert module_0.sum_squares([2.5, 1.5, 2.0]) == 2.5**2 + 1.5 + 2.0  # 9.75

# Generated at 2026-11-02 17:27:45.735024
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([-3]) == 9

    # All elements at indices not divisible by 3 or 4 stay unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # index 0 squared: 1

    # Index 0 squared, indices 1-3 unchanged
    assert module_0.sum_squares([2, 3, 4, 5]) == 4 + 3 + 4 + 5

    # Index 4 divisible by 4 (and not by 3) -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4 + 125  # 135

    # Index 8 cubed (8 % 4 == 0, 8 % 3 != 0)
    assert module_0.sum_squares([1] * 9) == 8 * 1 + 1**3  # 9

    # Index 8 cubed with a different value
    assert module_0.sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 2]) == 8

    # Index 12 divisible by 3 -> squared (takes priority over % 4 rule)
    assert module_0.sum_squares([1] * 13) == 12 * 1 + 144  # 156

    # Mixed case: indices 0,3,6 squared; index 4,8 cubed; rest unchanged
    lst = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # indices 0,3,6,9 -> squared: 4 each = 16
    # indices 4,8 -> cubed: 8 each = 16
    # indices 1,2,5,7 -> unchanged: 2 each = 8
    assert module_0.sum_squares(lst) == 40

    # Negative numbers: squares are positive, cubes are negative
    assert module_0.sum_squares([-1, -1, -1, -1, -2]) == 1 - 1 - 1 + 1 - 8  # -8

    # Floats
    assert module_0.sum_squares([1.5, 2.0, 3.0]) == 1.5**2 + 2.0 + 3.0

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-02 17:29:07.519673
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # No i%4 branch triggered (index 0 squared only)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # Single element: index 0 is squared
    assert module_0.sum_squares([5]) == 25

    # index 0 squared, others unchanged
    assert module_0.sum_squares([1, 4, 9]) == 14

    # index 3 squared (3 % 3 == 0)
    assert module_0.sum_squares([1, 3, 5, 7]) == 1 + 3 + 5 + 49  # 58

    # index 0 squared, index 3 squared, index 4 cubed (4 % 4 == 0, 4 % 3 != 0)
    assert module_0.sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 2 + 9 + 64  # 76

    # Negative values: (-1)^2 + (-5) + 2 + (-1)^2 + (-5)^3 = -126
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # All branches: i=0,3,6,9 squared; i=4,8 cubed; i=1,2,5,7 unchanged
    assert module_0.sum_squares(list(range(10))) == 717

    # Floats are handled: 1.5^2 + 2.0 + 3.5
    assert module_0.sum_squares([1.5, 2.0, 3.5]) == 7.75

    # Index 12: divisible by both 3 and 4 -> squared (first condition wins)
    lst = [2] * 13
    assert module_0.sum_squares(lst) == 4 + 2 + 2 + 4 + 8 + 2 + 4 + 2 + 8 + 2 + 2 + 2 + 4  # 46