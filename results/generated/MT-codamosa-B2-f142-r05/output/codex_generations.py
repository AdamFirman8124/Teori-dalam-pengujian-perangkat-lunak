

# Generated at 2026-11-02 15:33:26.118454
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3, so it is squared
    assert module_0.sum_squares([5]) == 25

    # Index 0 squared, other elements unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    # Index 3 squared (divisible by 3), index 4 cubed (divisible by 4, not 3)
    assert module_0.sum_squares([1, 4, 2, 3, 5]) == 1 + 4 + 2 + 3**2 + 5**3

    # Coverage of indices 0-8: squares at 0,3,6; cubes at 4,8; rest unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == \
        1 + 2 + 3 + 4**2 + 5**3 + 6 + 7**2 + 8 + 9**3

    # Negative numbers: squares stay positive, cubes stay negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125

    # Floating point values
    assert round(module_0.sum_squares([-7.0, 2.6, 3.4, 6.0, -8.4]), 3) == \
        round(49.0 + 2.6 + 3.4 + 36.0 + (-8.4)**3, 3)

# Generated at 2026-11-02 15:34:48.859499
# Unit test for function sum_squares
def test_sum_squares():
# nonce:35e14aaf
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Indices 0,1,2: index 0 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  #

# Generated at 2026-11-02 15:35:36.187655
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Simple case: only index 0 is squared
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14

    # Index 3 is a multiple of 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 4**2  # 22

    # Index 4 is a multiple of 4 (not 3) -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Negative values
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5) + 2 + (-1)**2 + (-5)**3  # -126

    # Single element (index 0) is squared
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([-3]) == 9

    # Index 8: multiple of 4 but not 3 -> cubed
    assert module_0.sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 3]) == 27
    assert module_0.sum_squares([0, 0, 0, 0, 0, 0, 0, 0, -2]) == -8

    # Index 12: divisible by both 3 and 4 -> squared (first branch wins)
    assert module_0.sum_squares([0] * 12 + [2]) == 4
    assert module_0.sum_squares([0] * 12 + [-2]) == 4

    # Floats supported
    assert module_0.sum_squares([1.5]) == 2.25

# Generated at 2026-11-02 15:36:14.344984
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Only squares at indices divisible by 3 (i=0)
    assert module_0.sum_squares([5]) == 25

    # Mixed: i=0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    assert module_0.sum_squares([1, 4, 9]) == 1 + 4 + 9

    # Cubes at indices divisible by 4 but not 3 (i=4), squares at i=0, i=3
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 140

    # Negative numbers: squares stay positive, cubes stay negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # -126

    # Longer list covering i=0 (square), i=3 (square), i=4 & i=8 (cube)
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10]) == \
        2**2 + 3 + 4 + 5**2 + 6**3 + 7 + 8**2 + 9 + 10**3  # 1332

    # Index 12: divisible by both 3 and 4 -> square wins (checked first)
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == \
        sum([1] * 12) + 2**2  # 16

# Generated at 2026-11-02 15:37:02.793710
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 2, 3, 4]) == 22
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 319
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == -113
    assert module_0.sum_squares([5]) == 25
    # index 12 is divisible by both 3 and 4 -> squared (not cubed)
    assert module_0.sum_squares([2] * 13) == 48
    # works with floats
    assert module_0.sum_squares([1.5, 2.5]) == 4.75

# Generated at 2026-11-02 15:37:58.740434
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # Single element at index 0 (divisible by 3) -> squared
    assert module_0.sum_squares([5]) == 25

    # [1,2,3]: idx0 squared (1), idx1 (2), idx2 (3) -> 6
    assert module_0.sum_squares([1, 2, 3]) == 6

    # [1,4,9]: 1^2 + 4 + 9 = 14
    assert module_0.sum_squares([1, 4, 9]) == 14

    # [1,3,5,7]: 1^2 + 3 + 5 + 7^2 = 62
    assert module_0.sum_squares([1, 3, 5, 7]) == 62

    # Index 4 (divisible by 4, not 3) -> cubed
    # [1,2,3,4,5]: 1^2 + 2 + 3 + 4^2 + 5^3 = 1+2+3+16+125 = 147
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 8 (divisible by 4, not 3) -> cubed
    # [2]*9: idx0->4, idx3->4, idx6->4, idx8->8, others 2 each (6 of them)
    # 4+2+2+4+8+2+4+2+8 = 36
    assert module_0.sum_squares([2] * 9) == 36

    # Index 12 (divisible by both 3 and 4) -> squared (not cubed)
    lst = [1] * 13
    lst[12] = 2
    # indices 0,3,6,9 -> 1 each; index 12 -> 4; remaining 8 indices -> 1 each
    # total = 4 + 4 + 8 = 16
    assert module_0.sum_squares(lst) == 16

    # Floats
    # [1.4, 4.2, 0]: 1.4^2 + 4.2 + 0^2 = 1.96 + 4.2 = 6.16
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9

    # [-2.4, 1, 1]: (-2.4)^2 + 1 + 1^2 = 5.76 + 2 = 7.76
    assert abs(module_0.sum_squares([-2.4, 1, 1]) - 7.76) < 1e-9

    # Negative integers: (-3)^2 = 9 at index 0
    assert module_0.sum_squares([-3]) == 9

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 15:40:07.701844
# Unit test for function sum_squares
def test_sum_squares():
    # Basic case: only index 0 is divisible by 3
    assert module_0.sum_squares([1, 2, 3]) == 6  # 1**2 + 2 + 3

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Negative numbers, index 4 gets cubed
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 + (-5) + 2 + 1 + (-125)

    # Mixed case: indices 0,3 squared; index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6]) == 153  # 1 + 2 + 3 + 16 + 125 + 6

    # Longer list exercising multiple indices
    assert module_0.sum_squares([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 1, 1, 1]) == 172

    # Zero handling
    assert module_0.sum_squares([0, 1, 2]) == 3  # 0**2 + 1 + 2

    # Index 12 divisible by both 3 and 4 -> squared (first condition wins)
    assert module_0.sum_squares([1] * 13) == 13

    print("All test cases passed!")


if __name__ == "__main__":
    test_sum_squares()