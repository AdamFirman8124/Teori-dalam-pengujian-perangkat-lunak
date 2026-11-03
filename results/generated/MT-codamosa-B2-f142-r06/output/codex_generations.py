

# Generated at 2026-11-02 23:28:53.762892
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Basic list with small values
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3

    # Index 0 (div by 3): square; index 3 (div by 3): square
    assert module_0.sum_squares([1, 3, 5, 7]) == 1**2 + 3 + 5 + 7**2

    # Index 4 (div by 4, not 3): cube
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3

    # Negative numbers
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)

    # Floats
    assert module_0.sum_squares([-0.5, -2]) == 0.25 + (-2)

    # Index 12 (div by 3 and 4): square takes precedence
    lst = list(range(13))
    expected = sum(
        x**2 if i % 3 == 0 else (x**3 if i % 4 == 0 else x)
        for i, x in enumerate(lst)
    )
    assert module_0.sum_squares(lst) == expected

    print("All tests passed!")

# Generated at 2026-11-02 23:30:02.990009
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element at index 0 gets squared
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Index 3 squared (divisible by 3), index 0 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1**2 + 2 + 3 + 4**2  # 22

    # Index 4 cubed (divisible by 4, not by 3), indices 0 and 3 squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 147

    # Negative numbers: squared at idx 0,3; cubed at idx 4
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)  # -126

    # Mixed multipliers: idx 0,3,6 squared; idx 4,8 cubed; rest unchanged
    assert module_0.sum_squares(list(range(10))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9
    )  # 0+1+2+9+64+5+36+7+512+9 = 645

    # Larger list with floats
    assert module_0.sum_squares([1.5, 2.0, 3.0]) == 1.5**2 + 2.0 + 3.0  # 8.25

# Generated at 2026-11-02 23:31:05.347003
# Unit test for function sum_squares
def test_sum_squares():
    # Basic cases
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 6          # 1^2 + 2 + 3

    # Squares at indices divisible by 3
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147  # 1^2 + 2 + 3 + 4^2 + 5^3

    # Cubes at indices divisible by 4 but not 3
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8]) == 258  # 4 + 3 + 4 + 25 + 216 + 7 + 8

    # Index divisible by both 3 and 4 (e.g., 12) -> squared, not cubed
    lst = [1] * 13
    assert module_0.sum_squares(lst) == 12 + 1           # i=12 squared, others unchanged

    # Mixed comprehensive case
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 684

    # Negative numbers
    assert module_0.sum_squares([-1, -2]) == -1          # (-1)^2 + (-2)
    assert module_0.sum_squares([-2, -3, -4, -5, -6]) == 4 - 3 - 4 + 25 - 216

    # Zeros
    assert module_0.sum_squares([0, 0, 0, 0]) == 0

    # Repeated values
    assert module_0.sum_squares([5] * 8) == 220          # 25 + 5 + 5 + 25 + 125 + 5 + 25 + 5

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 23:32:27.371828
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 4, 9]) == 14
    assert module_0.sum_squares([1, 3, 5, 7]) == 58
    assert module_0.sum_squares([1.4, 4.2, 0]) == 0
    assert module_0.sum_squares([-2.4, 1, 1]) == 6.76
    assert module_0.sum_squares([100, 1, 15, 2, 102, 30, 40]) == 10235
    assert module_0.sum_squares([-12, -4, -6, 2, -6, -4, -8, -8]) == -172
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126
    assert module_0.sum_squares([2, 4, 6, 8, 10]) == 4 + 4 + 6 + 512 + 10

# Generated at 2026-11-02 23:33:39.769926
# Unit test for function sum_squares
def test_sum_squares():
# nonce:a13c20b5
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 % 3 == 0 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Indices 0,1,2: only index 0 squared
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    # Index 3 % 3 == 0 -> squared
    assert module_0.sum_squares([1, 4, 15, 20]) == 1 + 4 + 15 + 20**2

    # Index 4 % 4 == 0 and % 3 != 0 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 3**2 + 4**3

    # Negative values
    assert module_0.sum_squares([-1, -2, -3]) == 1 + (-2) + (-3)
    assert module_0.sum_squares([-2, -3, -4, -5]) == 4 + (-3) + (-4) + 25

    # Comprehensive check of every branch (indices 0..11)
    lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    expected = (
        2**2 + 3 + 4 + 5**2 + 6**3 + 7 + 8**2 + 9 + 10**3 + 11**2 + 12 + 13
    )
    assert module_0.sum_squares(lst) == expected

    # Floats
    assert module_0.sum_squares([2.0, 3.0]) == 4.0 + 3.0

# Generated at 2026-11-02 23:34:53.910327
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 is a multiple of 3 -> squared
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    # Indices 0, 3, 6 squared; index 4 cubed; others unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8

    # All indices covered: 0,3,6 squared; 4 cubed; rest unchanged
    assert module_0.sum_squares([1, 4, 9, 16, 25, 36, 49, 64]) == 1 + 4 + 9 + 256 + 15625 + 36 + 2401 + 64

    # Index 12 is multiple of 3 (squared, not cubed); index 8, 16 cubed
    lst = list(range(17))  # values equal to their indices
    expected = 0
    for i in range(17):
        if i % 3 == 0:
            expected += i ** 2
        elif i % 4 == 0:
            expected += i ** 3
        else:
            expected += i
    assert module_0.sum_squares(lst) == expected

    # Empty list -> sum is 0
    assert module_0.sum_squares([]) == 0

    # Negative numbers: squares are positive, cubes are negative
    assert module_0.sum_squares([-1, -2, -3]) == 1 + (-2) + (-3)
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 + (-2) + (-3) + 16 + (-125)

    # Zeros remain zero
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

    # Single element at index 0 gets squared
    assert module_0.sum_squares([5]) == 25

    # Mixed floats and ints
    assert module_0.sum_squares([2.0, 3.0, 4.0]) == 4.0 + 3.0 + 4.0

    # Verify against reference logic on random-ish data
    data = [3, 1, 7, 2, 9, 4, 8, 5, 6, 10, 11, 12, 13]
    total = 0
    for i, v in enumerate(data):
        if i % 3 == 0:
            total += v ** 2
        elif i % 4 == 0:
            total += v ** 3
        else:
            total += v
    assert module_0.sum_squares(data) == total

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()