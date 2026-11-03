

# Generated at 2026-11-03 05:47:48.336672
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # i=0 is divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # i=3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 1 + 3 + 5 + 7**2  # 58

    # i=4 divisible by 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 145

    # Repeated indices: 0,3,6 squared; 4,8 cubed; others unchanged
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10]) == (
        2**2 + 3 + 4 + 5**2 + 6**3 + 7 + 8**2 + 9 + 10**3
    )  # 1332

    # Negative numbers: squares positive, cubes negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == (
        (-1)**2 + (-5) + 2 + (-1)**2 + (-5)**3
    )  # -126

    assert module_0.sum_squares([-7, -3, -2, -9, -11]) == (
        (-7)**2 + (-3) + (-2) + (-9)**2 + (-11)**3
    )  # -1206

    # Index 12 divisible by both 3 and 4 -> squared (3-check wins)
    assert module_0.sum_squares(list(range(13))) == 882

    # All ones
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9

# Generated at 2026-11-03 05:50:02.172391
# Unit test for function sum_squares
def test_sum_squares():
    # Squared entries: indices divisible by 3 (including index 0)
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14
    assert module_0.sum_squares([1, 3, 5, 7]) == 58          # 1^2 + 3 + 5 + 7^2

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 always squared
    assert module_0.sum_squares([5]) == 25

    # Cubed entries: indices divisible by 4 but not by 3
    assert module_0.sum_squares([0, 0, 0, 0, 2]) == 8        # index 4: 2^3
    assert module_0.sum_squares([0] * 8 + [2]) == 8          # index 8: 2^3
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8      # index 4: (-2)^3

    # Index divisible by both 3 and 4 -> squared branch wins
    assert module_0.sum_squares([0] * 12 + [2]) == 4         # index 12: 2^2

    # All ones: every branch contributes 1
    assert module_0.sum_squares([1] * 10) == 10

    # Mixed entries covering all branches
    # i=0:1^2, i=1:2, i=2:3, i=3:4^2, i=4:5^3, i=5:6, i=6:7^2, i=7:8, i=8:9^3
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

    # Negative numbers
    assert module_0.sum_squares([-2, -5, 3, -1]) == 3        # 4 + (-5) + 3 + 1

    # Floats
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9

# Generated at 2026-11-03 05:51:16.182879
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Simple case: index 0 is squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    # Index 3 is divisible by 3, so element is squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # All indices not divisible by 3 or 4 remain unchanged
    assert module_0.sum_squares([1, 4, 1]) == 6

    # Squaring applies at indices 0 and 3
    assert module_0.sum_squares([1, 3, 5, 7]) == 1 + 3 + 5 + 49

    # Cubing applies at index 4 (divisible by 4 but not 3), works with negatives
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)

    # Index divisible by both 3 and 4 (e.g. 12) is squared, not cubed
    assert module_0.sum_squares([2] * 13) == 48

    # Squaring negative numbers yields positive results
    assert module_0.sum_squares([-1, 2, 3, -4, 5]) == 1 + 2 + 3 + 16 + 5

test_sum_squares()
print("All tests passed!")

# Generated at 2026-11-03 05:52:04.649359
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # All elements unchanged (indices 1, 2)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # index 0 squared: 1

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1**2 + 2 + 3 + 4**2  # 1+2+3+16 = 22

    # Index 4 divisible by 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 147

    # Mixed case with all branches
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (
        1**2 + 2 + 3 + 4**2 + 5**3 + 6 + 7**2 + 8 + 9**3
    )  # 1+2+3+16+125+6+49+8+729 = 939

    # Index divisible by 12 -> i % 3 == 0 takes priority (squared, not cubed)
    lst = [10] * 13
    assert module_0.sum_squares(lst) == 10**2 * 4 + 10**3 * 2 + 10 * 7

    # Negative numbers
    assert module_0.sum_squares([-1, -2, -3, -4]) == (-1)**2 + (-2) + (-3) + (-4)**2  # 1-2-3+16 = 12

    # Single element at index 0 -> squared
    assert module_0.sum_squares([5]) == 25

    # Zero values
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

    print("All tests passed!")

# Generated at 2026-11-03 05:52:56.458987
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is a multiple of 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # Basic example: 1^2 + 2 + 3
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Indices 0,3,6 squared; index 4 (mult of 4, not 3) cubed
    # 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 9 = 219
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 219

    # Negative values: (-1)^2 + (-2) + (-3) = -4
    assert module_0.sum_squares([-1, -2, -3]) == -4

    # Mixed signs: 1 + 4 + 1 + 4 + (-27) + 5 = -12
    assert module_0.sum_squares([-1, 4, 1, 2, -3, 5]) == -12

    # Cubing branch at index 4: 4 + 3 + 4 + 25 + 216 = 252
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 252

    # All zeros
    assert module_0.sum_squares([0, 0, 0, 0]) == 0

    # Index 12 is a multiple of both 3 and 4 -> squared (i % 3 branch wins)
    # sum: 0 + 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144 = 882
    assert module_0.sum_squares(list(range(13))) == 882

    # Floats: 1.5^2 + 2 + 3 + 4^2 = 23.25
    assert module_0.sum_squares([1.5, 2, 3, 4]) == 23.25


if __name__ == "__main__":
    test_sum_squares()
    print("All tests passed!")

# Generated at 2026-11-03 05:53:28.509743
# Unit test for function sum_squares
def test_sum_squares():import pytest

def test_sum_squares_empty_list():
    assert module_0.sum_squares([]) == 0

def test_sum_squares_single_element():
    # Index 0 satisfies i % 3 == 0, so it is squared
    assert module_0.sum_squares([5]) == 25

def test_sum_squares_basic():
    # indices: 0 squared, 1 kept, 2 kept
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

def test_sum_squares_index_multiple_of_3():
    # index 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

def test_sum_squares_index_multiple_of_4_not_3():
    # index 4 -> cubed (4 % 4 == 0, 4 % 3 != 0)
    assert module_0.sum_squares([1, 4, 1, 4, 1]) == 1 + 4 + 1 + 16 + 1

def test_sum_squares_mixed():
    # index 0 -> 1^2 = 1, index 3 -> 7^2 = 49
    assert module_0.sum_squares([1, 3, 5, 7]) == 58

def test_sum_squares_all_same():
    # indices 0,3,6 squared: 3*4=12; index 8 cubed: 8; remaining 5 kept: 10
    assert module_0.sum_squares([2] * 9) == 30

def test_sum_squares_negative_numbers():
    # index 0 -> 1, index 3 -> 16, others kept
    assert module_0.sum_squares([-1, -2, -3, -4]) == 1 - 2 - 3 + 16

def test_sum_squares_floats():
    # index 0 -> 0.25, index 3 -> 0.25, index 4 -> 0.125
    assert module_0.sum_squares([0.5, 0.5, 0.5, 0.5, 0.5]) == pytest.approx(1.625)

def test_sum_squares_longer_list():
    # indices 0,3,6,9,12 squared; indices 4,8,16 cubed; rest kept
    lst = list(range(1, 18))
    expected = sum(lst)
    for i in (0, 3, 6, 9, 12):
        expected += lst[i]**2 - lst[i]
    for i in (4, 8, 16):
        expected += lst[i]**3 - lst[i]
    assert module_0.sum_squares(lst) == expected

def test_sum_squares_zeros():
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

# Generated at 2026-11-03 05:53:58.615200
# Unit test for function sum_squares
def test_sum_squares():
    # nonce:f486c852

    # Basic case: index 0 is squared (i % 3 == 0)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1^2 + 2 + 3 = 6

    # Indices 3 (squared) and 4 (cubed, since 4 % 3 != 0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # 147

    # Empty list should return 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 squared
    assert module_0.sum_squares([5]) == 25

    # Negative numbers: squares preserve sign loss, plain values keep sign
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 - 3  # -4

    # Longer list covering indices 0..6
    # i=0: 2^2=4, i=1: 3, i=2: 4, i=3: 5^2=25, i=4: 6^3=216, i=5: 7, i=6: 8^2=64
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8]) == 323

    # Index 12 is divisible by both 3 and 4 -> squared (first condition wins)
    lst = [1] * 13
    lst[12] = 3
    # sum = 12 * 1 + 3^2 = 15
    assert module_0.sum_squares(lst) == 15

    # Works with floats
    assert module_0.sum_squares([1.5, 2, 3]) == 2.25 + 2 + 3  # 7.25

    # Zero elements
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-03 05:55:02.923566
# Unit test for function sum_squares
def test_sum_squares():
    # i % 3 == 0 -> squared, i % 4 == 0 (and not % 3) -> cubed, otherwise unchanged
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1**2 + 2 + 3
    assert module_0.sum_squares([]) == 0                    # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147     # 1**2 + 2 + 3 + 4**2 + 5**3
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # (-1)**2 - 5 + 2 + (-1)**2 + (-5)**3
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1734
    # squares at i=0,3,6,9; cubes at i=4,10; i=12 is squared (12 % 3 == 0)
    assert module_0.sum_squares([-7.5, -6.5, -1, -1.5]) == 51.0  # (-7.5)**2 - 6.5 - 1 + (-1.5)**2
    assert module_0.sum_squares([0]) == 0                    # 0**2 == 0
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 8 + 2 + 2 + 4 + 8  # 4+2+2+16+125? no: 2**2+2+2+2**2+2**3 = 4+2+2+4+8 = 20
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 20
    assert module_0.sum_squares([5, 1, 1, 5]) == 25 + 1 + 1 + 25  # i=3 squared
    assert module_0.sum_squares([1.5, 2.5]) == 1.5**2 + 2.5       # i=0 squared, i=1 unchanged