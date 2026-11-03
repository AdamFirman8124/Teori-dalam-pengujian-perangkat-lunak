

# Generated at 2026-11-03 00:48:08.962588
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Indices 0 and 3 squared (multiples of 3), others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14
    assert module_0.sum_squares([1, 3, 5, 7]) == 58  # 1^2 + 3 + 5 + 7^2

    # Index 4 is a multiple of 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147  # 1^2 + 2 + 3 + 4^2 + 5^3
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 16 + 125 + 6 + 7 + 512

    # Negative numbers
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)

    # Floats
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9
    assert abs(module_0.sum_squares([-2.4, 1, 1]) - 7.76) < 1e-9

    # Large values
    assert module_0.sum_squares([100, 1, 1, 100]) == 20002

# Generated at 2026-11-03 00:49:08.978504
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 4, 15]) == 20
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126
    assert module_0.sum_squares([-1, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 498

# Generated at 2026-11-03 00:50:30.236117
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # i=0 squared, i=3 squared, i=4 cubed (divisible by 4 but not 3)
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 3 + 16 + 125 + 6  # 153

    # Negative numbers: squares are positive, cubes keep sign
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # -126

    # Index divisible by both 3 and 4 (i=12) is squared, not cubed
    assert module_0.sum_squares([1] * 12 + [2]) == 12 + 4  # 16

    # Works with floats
    assert module_0.sum_squares([1.5, 2, 3]) == 2.25 + 2 + 3  # 7.25


test_sum_squares()

# Generated at 2026-11-03 00:51:28.780185
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is a multiple of 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # All zeros
    assert module_0.sum_squares([0, 0, 0, 0]) == 0

    # Indices: 0 (sq), 1 (same), 2 (same), 3 (sq), 4 (cube)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Longer list covering indices 0-9:
    # i=0 sq, i=3 sq, i=4 cube, i=6 sq, i=8 cube, i=9 sq
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Negative numbers: squares stay positive, untouched values stay negative
    assert module_0.sum_squares([-1, -2, -3, -4]) == 1 - 2 - 3 + 16  # 12

    # Uniform list of length 9:
    # i=0,3,6 squared (3 * 4), i=4,8 cubed (2 * 8), i=1,2,5,7 unchanged (4 * 2)
    assert module_0.sum_squares([2] * 9) == 3 * 4 + 2 * 8 + 4 * 2  # 36

    # Length 17 list: multiples of 3 (0,3,6,9,12,15) squared,
    # multiples of 4 but not 3 (4,8,16) cubed, rest unchanged
    assert module_0.sum_squares([3] * 17) == 6 * 9 + 3 * 27 + 8 * 3  # 159

    # Index 12 (multiple of 3) is squared, not cubed, despite 12 % 4 == 0
    lst = [0] * 13 + [7]
    assert module_0.sum_squares(lst) == 7**2  # 49

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-03 00:52:44.822389
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 2, 3, 4]) == 22
    assert module_0.sum_squares([1, 4, 9]) == 98
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 252
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12
    assert module_0.sum_squares([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 375
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8]) == 187

# Generated at 2026-11-03 00:54:10.075815
# Unit test for function sum_squares
def test_sum_squares():
    # All indices < 3 except 0 stay unchanged; index 0 squared, index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 1 + 2 + 9 + 64  # == 77

    # Negative numbers: squares stay positive, cubes keep sign
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # == -126

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 is divisible by 3)
    assert module_0.sum_squares([5]) == 25

    # Longer list covering indices 0..11
    # i=0:1^2, i=1:2, i=2:3, i=3:3^2, i=4:4^3, i=5:6, i=6:6^2, i=7:8,
    # i=8:9^2, i=9:10^2, i=10:11, i=11:12
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 333

    # Index 12 is divisible by both 3 and 4 -> square takes priority
    assert module_0.sum_squares([0] * 12 + [7]) == 49

    # Zero values
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

    # Fractional values
    assert module_0.sum_squares([0.5, 1.5, 2.5]) == 0.25 + 1.5 + 2.5  # == 4.25

# Generated at 2026-11-03 00:56:07.986221
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0
    # Basic case
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14
    # Negative numbers: index 0 squared, index 3 squared, index 4 cubed
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126
    # Single element at index 0 is squared
    assert module_0.sum_squares([5]) == 25
    # Index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # Index 12 is a multiple of both 3 and 4 -> squared (3-check takes priority)
    assert module_0.sum_squares([2] * 13) == 48
    # Longer mixed case covering all branches
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 899
# nonce:37209fd8

# Generated at 2026-11-03 00:57:15.533002
# Unit test for function sum_squares
def test_sum_squares():
# nonce:e7cf19eb
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 4, 9]) == 14
    assert module_0.sum_squares([1, 3, 5, 7]) == 58
    assert module_0.sum_squares([1.4, 4.2, 0]) == 6.16
    assert module_0.sum_squares([-2, -3, -4, -1, -2, -5]) == -15
    assert module_0.sum_squares([-2, 4, -4, 9]) == 85
    assert module_0.sum_squares([5]) == 25
    # index 4 is divisible by 4 (and not 3) -> cubed
    assert module_0.sum_squares([0, 0, 0, 0, 2]) == 8
    # mixed: i=3 squared, i=4 cubed, i=6 squared, i=8 cubed