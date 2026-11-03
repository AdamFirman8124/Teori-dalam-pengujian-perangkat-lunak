

# Generated at 2026-11-01 22:34:55.857454
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Indices 0,1,2: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Index 3 squared, index 4 cubed (4 % 4 == 0, 4 % 3 != 0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Negative numbers: squares are positive, cubes are negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # -126

    # Index 12 is divisible by both 3 and 4 -> squared (not cubed)
    assert module_0.sum_squares(list(range(13))) == 1872

    # Floats supported
    assert module_0.sum_squares([1.5, 2, 3]) == 2.25 + 2 + 3  # 7.25

    # Single element at index 0 -> squared
    assert module_0.sum_squares([7]) == 49

    # All elements unchanged when list length < 4 elements past index 0
    assert module_0.sum_squares([2, 3, 4]) == 4 + 3 + 4  # 11

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:35:12.618442
# Unit test for function sum_squares
def test_sum_squares():
    # Basic cases
    assert module_0.sum_squares([1, 2, 3]) == 6          # 1^2 + 2 + 3
    assert module_0.sum_squares([]) == 0                 # empty list
    assert module_0.sum_squares([1, 4, 9]) == 14         # 1^2 + 4 + 9

    # Index divisible by 3
    assert module_0.sum_squares([1, 3, 5, 7]) == 58      # 1^2 + 3 + 5 + 7^2

    # Index divisible by 4 but not 3 (index 4 -> cube)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147  # 1^2 + 2 + 3 + 4^2 + 5^3

    # Multiple special indices (0, 3, 4, 6)
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 168

    # Floats and negatives
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9
    assert abs(module_0.sum_squares([-2, -5.3, -4.7]) - (-6)) < 1e-9

    # Single element (index 0 always squared)
    assert module_0.sum_squares([10]) == 100

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:35:49.367395
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 (multiple of 3) squared, index 4 (multiple of 4, not 3) cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147  # 1 + 2 + 3 + 16 + 125

    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element at index 0 is squared
    assert module_0.sum_squares([5]) == 25

    # No entries modified when no index is a multiple of 3 or 4
    assert module_0.sum_squares([1, 4, 9]) == 14

    # Negative numbers: squared/cubed values handled correctly
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 - 5 + 2 + 1 - 125

    # Basic case with only index 0 squared
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Index 12 is a multiple of both 3 and 4 -> squared (not cubed)
    assert module_0.sum_squares([1] * 12 + [2]) == 16  # twelve 1s + 2**2

    # Indices 3 and 9 squared, index 4 cubed
    assert module_0.sum_squares([2, 4, 6, 8, 10, 12]) == 1090  # 4 + 4 + 6 + 64 + 1000 + 12

    # Longer list covering indices 0-11
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1662

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:36:24.796626
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 is divisible by 3, so lst[0] is squared; others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Squares at indices 0 and 3, cube at index 4 (divisible by 4 but not 3)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 147

    # Mixed values
    assert module_0.sum_squares([1, 4, 2, 5, 7]) == 1 + 4 + 2 + 5**2 + 7**3  # 375

    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Negative numbers: squared/cubed values handle sign correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125  # -113

    # Single element (index 0 squared)
    assert module_0.sum_squares([10]) == 100

    # Longer list covering index 12 (divisible by both 3 and 4 -> squared)
    lst = list(range(13))
    expected = sum(
        x**2 if i % 3 == 0 else (x**3 if i % 4 == 0 else x)
        for i, x in enumerate(lst)
    )
    assert module_0.sum_squares(lst) == expected  # 1146

    # Floats
    assert module_0.sum_squares([0.5, 1.5]) == 0.25 + 1.5

# Generated at 2026-11-01 22:37:02.933501
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is a multiple of 3 -> squared
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([-3]) == 9

    # Indices 1 and 2 are left unchanged, index 0 squared
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14

    # Index 3 squared, index 4 cubed, index 5 unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 3 + 16 + 125 + 6

    # Negatives: squares are positive, cube at index 4 is negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Longer list covering indices 0-12:
    # index 12 is a multiple of both 3 and 4 -> squared (i % 3 takes priority)
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1231

    # Floats are handled as well
    assert module_0.sum_squares([0.5, 1.5, 2.0, 3.0, 4.0]) == 0.25 + 1.5 + 2.0 + 9.0 + 64.0

    # Every multiple of 3 gets squared even when mixed with other values
    assert module_0.sum_squares([2, 1, 1, 2, 1, 1, 2]) == 4 + 1 + 1 + 4 + 1 + 1 + 4


if __name__ == "__main__":
    test_sum_squares()
    print("All tests passed!")

# Generated at 2026-11-01 22:37:32.383363
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # Indices 0 (squared), 1, 2 (unchanged)
    assert module_0.sum_squares([1, 2, 3]) == 6          # 1^2 + 2 + 3
    assert module_0.sum_squares([1, 4, 9]) == 14         # 1^2 + 4 + 9

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 22      # 1 + 2 + 3 + 4^2

    # Index 4 divisible by 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147  # 1 + 2 + 3 + 4^2 + 5^3

    # Indices 0,3,6 squared; index 8 (8%4==0, 8%3!=0) cubed; rest unchanged
    assert module_0.sum_squares(list(range(9))) == 636   # 0 + 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512

    # Index 12 divisible by both 3 and 4 -> squared (i%3==0 takes precedence)
    assert module_0.sum_squares(list(range(13))) == 882

    # Negative numbers
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 - 5 + 2 + 1 - 125

    # Mixed values
    assert module_0.sum_squares([5, 6, 7, 8, 9, 10]) == 841  # 25 + 6 + 7 + 64 + 729 + 10

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-01 22:38:04.333118
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3, so squared
    assert module_0.sum_squares([5]) == 25

    # Simple case: indices 0 (square), 1, 2 (unchanged)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 divisible by 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Mixed: index 0 square, 3 square, 4 cube, 6 square (6%3==0 takes precedence over 6%4)
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8

    # Negative numbers: squares and cubes of negatives
    # i=0: (-1)^2 = 1, i=1: -2, i=2: -3, i=3: (-4)^2 = 16, i=4: (-5)^3 = -125
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 8: divisible by 4 but not 3 -> cubed
    # [0,0,0,0,0,0,0,0,2] -> i=8: 2^3 = 8
    assert module_0.sum_squares([0] * 8 + [2]) == 8

    # Index 12: divisible by both 3 and 4 -> square takes precedence (i%3==0 checked first)
    # [0]*11 + [3] -> i=12: 3^2 = 9
    assert module_0.sum_squares([0] * 11 + [3]) == 9

    # All zeros
    assert module_0.sum_squares([0, 0, 0, 0, 0]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:38:19.484632
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> sum is 0
    assert module_0.sum_squares([]) == 0

    # Indices 0, 3 squared; others unchanged: 1 + 2 + 9 = 12... wait, [1,2,3]:
    # i=0 -> 1**2 = 1, i=1 -> 2, i=2 -> 3 => total 6
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Mixed negatives: i=0 -> (-1)^2=1, i=1 -> -5, i=2 -> 2,
    # i=3 -> (-1)^2=1, i=4 -> (-5)^3=-125 => total -126
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Single element at index 0 gets squared
    assert module_0.sum_squares([5]) == 25

    # Index divisible by both 3 and 4 (e.g., 12) is squared, not cubed
    # [0..12] => 0+1+2+9+64+5+36+7+512+81+10+11+144 = 882
    assert module_0.sum_squares(list(range(13))) == 882

    # Cubes only when i % 4 == 0 but i % 3 != 0 (index 4 here)
    # [1, 1, 1, 1, 2] => 1 + 1 + 1 + 1 + 8 = 12
    assert module_0.sum_squares([1, 1, 1, 1, 2]) == 12

    # Works with floats: 1.5^2 + 2.0 = 2.25 + 2.0 = 4.25
    assert module_0.sum_squares([1.5, 2.0]) == 4.25

# Generated at 2026-11-01 22:38:38.436032
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Simple case: only index 0 gets squared
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Index 0 squared only
    assert module_0.sum_squares([1, 4, 9]) == 1 + 4 + 9  # 14

    # Index 3 squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 1 + 3 + 5 + 7**2  # 58

    # Indices 3 and 4 handled (squared and cubed respectively)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Cubing at index 4
    assert module_0.sum_squares([5, 1, 1, 1, 2]) == 25 + 1 + 1 + 1 + 8  # 36

    # Longer list covering indices 0..12 (index 12 is mult of 3 -> squared)
    assert module_0.sum_squares(list(range(13))) == 882

    # Float inputs
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - (1.4**2 + 4.2 + 0)) < 1e-9  # 6.16
    assert abs(module_0.sum_squares([-2.4, 1, 1]) - ((-2.4)**2 + 1 + 1)) < 1e-9  # 7.76


test_sum_squares()
print("All tests passed!")

# Generated at 2026-11-01 22:39:07.412423
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> sum is 0
    assert module_0.sum_squares([]) == 0

    # Single element at index 0 (divisible by 3) gets squared
    assert module_0.sum_squares([5]) == 25

    # No special indices beyond 0
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Index 3 is divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 4**2  # 22

    # Index 4 divisible by 4 but not 3 -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Negative numbers with mixed operations
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)  # -126

    # Indices 0, 3 squared; 4, 8 cubed; others unchanged
    lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = 2**2 + 3 + 4 + 5**2 + 6**3 + 7 + 8 + 9 + 10**3
    assert module_0.sum_squares(lst) == expected

    # Multiple of both 3 and 4 (e.g., 12) should be squared, not cubed
    lst = [1] * 13
    expected = 1 * 13
    assert module_0.sum_squares(lst) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:39:50.520109
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # Basic case: indices 0 and 3 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # Mixed squaring (i % 3 == 0), cubing (i % 4 == 0), and unchanged
    # [1, 2, 3, 4, 5]:
    # i=0 -> 1**2 = 1
    # i=1 -> 2
    # i=2 -> 3
    # i=3 -> 4**2 = 16
    # i=4 -> 5**3 = 125
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Negative numbers
    # [-1, -5, 2, -1, -5]:
    # i=0 -> (-1)**2 = 1
    # i=1 -> -5
    # i=2 -> 2
    # i=3 -> (-1)**2 = 1
    # i=4 -> (-5)**3 = -125
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Longer list verifying precedence: index divisible by both 3 and 4 (e.g. 12) is squared
    lst = list(range(13))
    expected = (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**2
    )
    assert module_0.sum_squares(lst) == expected  # 882

    # Zeros
    assert module_0.sum_squares([0, 0, 0, 0]) == 0


if __name__ == "__main__":
    test_sum_squares()
    print("All tests passed.")

# Generated at 2026-11-01 22:40:37.838097
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # Basic case: only index 0 gets special treatment
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Negative numbers: squared/cubed values can be negative
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Indices 3 (sq), 4 (cube), 6 (sq) exercised
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 127

    # Index 8 cubed, index 9 squared, index 12 squared (multiple of both 3 and 4 -> square wins)
    assert module_0.sum_squares(list(range(1, 14))) == 885

    # Zeros remain zero regardless of transformation
    assert module_0.sum_squares([0, 0, 0, 0]) == 0

    # Longer mixed case: verify manual computation
    # [2,3,4,5,6,7,8,9,10]:
    # i0:4, i1:3, i2:4, i3:25, i4:512, i5:7, i6:36, i7:9, i8:1000
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1600

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-01 22:41:15.923940
# Unit test for function sum_squares
def test_sum_squares():
# nonce:d0b20bf2
    # index 0 is squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([]) == 0

    # index 3 is squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 58  # 1**2 + 3 + 5 + 7**2
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9

    # index 4 is cubed (divisible by 4 but not 3)
    assert module_0.sum_squares([-2, -3, -4, -5, -6]) == -194  # 4 - 3 - 4 + 25 + (-6)**3
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 319
    # 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 9 + 100

    # floats
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9  # 1.4**2 + 4.2

    # negatives with mixed operations
    assert module_0.sum_squares([-1, -3, 5, -6, -4, 2]) == -23  # 1 - 3 + 5 + 36 - 64 + 2
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8]) == 132
    # 0 + 1 + 2 + 9 + 64 + 5 + 36 + 7 + 8

# Generated at 2026-11-01 22:41:48.282672
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3, so squared
    assert module_0.sum_squares([2]) == 4

    # Only index 0 is special here
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1**2 + 2 + 3 = 6

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 4**2  # 22

    # Index 4 divisible by 4 (and not 3) -> cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Mixed case covering squared, cubed, and unchanged entries
    # i=0:1^2, i=3:4^2, i=4:5^3, i=6:7^2, i=8:9^3, others unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 971

    # Negative numbers: squares are positive, cubes stay negative
    assert module_0.sum_squares([-1, -2, -3, -4]) == 1 - 2 - 3 + 16  # 12

    # Index 12 divisible by both 3 and 4 -> squared rule (first branch) wins
    lst = [1] * 13
    # indices 0,3,6,9,12 squared (5), indices 4,8 cubed (2), rest unchanged (6)
    assert module_0.sum_squares(lst) == 13

    # Works with floats
    assert module_0.sum_squares([1.5, 2.0, 3.0, 4.0]) == 1.5**2 + 2.0 + 3.0 + 4.0**2

# Generated at 2026-11-01 22:42:11.427257
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 divisible by 3 -> squared
    assert module_0.sum_squares([5]) == 25

    # Two elements
    assert module_0.sum_squares([3, 4]) == 13  # 3**2 + 4

    # Basic case, no cubing needed
    assert module_0.sum_squares([1, 2, 3]) == 6  # 1**2 + 2 + 3

    # Index 3 divisible by 3 -> squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 58  # 1 + 3 + 5 + 7**2

    # Negative numbers: squared at idx 0 and 3, cubed at idx 4
    assert module_0.sum_squares([-2, -5, 3, -1, 2, 7]) == 18  # 4 - 5 + 3 + 1 + 8 + 7

    # Cubing a negative value at index 4 (div by 4, not by 3)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 - 5 + 2 + 1 + (-5)**3

    # Floats with exact binary representation
    assert module_0.sum_squares([1.5, 2.5, 3.5]) == 8.25  # 1.5**2 + 2.5 + 3.5

    # Squaring at idx 0,3,6; cubing at idx 4,8
    assert module_0.sum_squares([2] * 9) == 36  # 4+2+2+4+8+2+4+2+8

    # Mixed values covering indices 0-9 with cubing at 4 and 8
    assert module_0.sum_squares([2, 3, 10, 15, 15, 15, 15, 15, 15, 10]) == 7137

    # Index 12 divisible by both 3 and 4 -> squared (3-check takes precedence)
    assert module_0.sum_squares([2] * 13) == 48

    # Larger mixed list
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6]) == 117  # 0+1+2+9+64+5+36

# Generated at 2026-11-01 22:42:24.841135
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list should return 0
    assert module_0.sum_squares([]) == 0

    # Indices divisible by 3 are squared (index 0)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1**2 + 2 + 3 = 6
    assert module_0.sum_squares([1, 4, 9]) == 1 + 4 + 9  # 1**2 + 4 + 9 = 14
    assert module_0.sum_squares([1, 3, 5, 7]) == 1 + 3 + 5 + 49  # index 3 squared: 7**2 = 49

    # Floats are squared at index 0
    assert module_0.sum_squares([1.4, 4.2, 0]) == 1.96 + 4.2 + 0
    assert module_0.sum_squares([-2.4, 1, 1]) == 5.76 + 1 + 1

    # Mixed: index 0 squared, index 3 squared, index 4 cubed (4 % 4 == 0, 4 % 3 != 0)
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 16 + 125 + 6 + 7 + 8  # 168

    # Longer list: indices 0,3,6 squared (but 6 is skipped since 6%3==0 takes priority),
    # indices 4,8 handled: 8%3!=0 and 8%4==0? No, 8%4==0 -> cubed, wait check:
    # i=0: 0**2=0, i=3: 9, i=4: 64, i=8: 8%3!=0, 8%4==0 -> cubed 512? No: 8%3==2, 8%4==0 -> 8**3=512?
    # Actually i=8: 8 % 3 != 0 and 8 % 4 == 0 -> cubed. Recompute:
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8]) == (
        0      # i=0: 0**2
        + 1    # i=1
        + 2    # i=2
        + 9    # i=3: 3**2
        + 64   # i=4: 4**3
        + 5    # i=5
        + 6    # i=6
        + 7    # i=7
        + 512  # i=8: 8**3
    )  # 666

    # Index 8 and 10 cubed (divisible by 4 but not 3)
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

    # Negative numbers: index 3 squared -> 36
    assert module_0.sum_squares([-1, -1, -1, -6]) == 1 + (-1) + (-1) + 36  # 35

    # Index 4 cubed with negative value
    assert module_0.sum_squares([2, 2, 2, 2, -3]) == 4 + 2 + 2 + 4 + (-27)  # -15

    # Index 6: 6 % 3 == 0 -> squared (takes priority over 6 % ... )
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 5]) == 1 + 1 + 1 + 1 + 1 + 1 + 25  # 31

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-01 22:42:38.047268
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 (divisible by 3) -> squared: 1**2 = 1
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Index 4 (divisible by 4, not by 3) -> cubed: 5**3 = 125
    # Index 3 (divisible by 3) -> squared: 4**2 = 16
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # 147

    # Mixed case covering all branches
    # i=0:1, i=1:2, i=2:3, i=3:16, i=4:125, i=5:6,
    # i=6:49, i=7:8, i=8:9, i=9:100, i=10:11, i=11:12
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 342

    # Index 12 divisible by both 3 and 4 -> squared (not cubed)
    assert module_0.sum_squares([2] * 13) == 42

    # Negative numbers: (-1)**2 = 1, -2 unchanged, 3 unchanged
    assert module_0.sum_squares([-1, -2, 3]) == 2

    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element gets squared
    assert module_0.sum_squares([5]) == 25

# Generated at 2026-11-01 22:42:50.237283
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is divisible by 3, so squared
    assert module_0.sum_squares([5]) == 25

    # Simple case
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # only index 0 squared: 1

    # Mixed indices: squares at multiples of 3, cubes at multiples of 4 (not 3)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 147

    # Longer list covering all branches
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (
        1**2 + 2 + 3 + 4**2 + 5**3 + 6 + 7**2 + 8 + 9**3 + 10**2  # 1039
    )

    # Negative values
    assert module_0.sum_squares([-1, -2, -3, -4]) == (-1)**2 + (-2) + (-3) + (-4)**2  # 12

    # Index 12 is divisible by both 3 and 4 -> squared (first branch wins)
    assert module_0.sum_squares([1] * 13) == 13

    # All elements unchanged when no special indices beyond 0
    assert module_0.sum_squares([2, 2, 2]) == 4 + 2 + 2  # 8

# Generated at 2026-11-01 22:43:03.958410
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list sums to 0
    assert module_0.sum_squares([]) == 0

    # Single element at index 0 (divisible by 3) -> squared
    assert module_0.sum_squares([5]) == 25

    # Basic example: index 0 squared, rest unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # == 6

    # Indices: 0 -> square, 3 -> square, 4 -> cube (4 % 4 == 0, 4 % 3 != 0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # == 147

    # Longer list covering indices 0..11
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = (
        1**2 + 2 + 3 + 4**2 + 5**3 + 6
        + 7**2 + 8 + 9**3 + 10**2 + 11 + 12**2
    )
    assert module_0.sum_squares(lst) == expected  # == 1194

    # Negative numbers
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # == -126

    # All elements equal: [2,2,2,2,2] -> 4 + 2 + 2 + 4 + 8 = 20
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 20

    # Index divisible by both 3 and 4 (e.g., 12) -> squared (i % 3 == 0 takes priority)
    lst2 = [0] * 13 + [5]
    # index 12: 12 % 3 == 0 -> squared
    assert module_0.sum_squares(lst2) == 5**2  # == 25

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-01 22:43:39.236839
# Unit test for function sum_squares

# Generated at 2026-11-01 22:43:45.939445
# Unit test for function sum_squares
def test_sum_squares():
    # Branches: i%3==0 -> square, i%4==0 (and i%3!=0) -> cube, else unchanged
    lst = [1, 2, 3, 4, 5]
    # i=0: 1**2 = 1 ; i=1: 2 ; i=2: 3 ; i=3: 4**2 = 16 ; i=4: 5**3 = 125
    assert module_0.sum_squares(lst) == 1 + 2 + 3 + 16 + 125 == 147

    assert module_0.sum_squares([]) == 0

    # Negative values: i=0 squares (-2)**2 = 4
    assert module_0.sum_squares([-2]) == 4

    # Mixed signs across indices 0..7:
    # i=0:(-1)^2=1; i=1:-2; i=2:3; i=3:4^2=16; i=4:5^3=125; i=6:7^2=49
    assert module_0.sum_squares([-1, -2, 3, 4, 5, 6, 7]) == 1 - 2 + 3 + 16 + 125 + 6 + 49 == 199

# Generated at 2026-11-01 22:43:54.029220
# Unit test for function sum_squares
def test_sum_squares():
    # Squared at indices divisible by 3
    assert module_0.sum_squares([1, 2, 3]) == 6          # 1^2 + 2 + 3
    assert module_0.sum_squares([1, 2, 3, 4]) == 22      # 1^2 + 2 + 3 + 4^2
    assert module_0.sum_squares([1, 4, 1]) == 18         # 1^2 + 4 + 1^2

    # Cubed at indices divisible by 4 (but not 3)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 - 5 + 2 + 1 + (-5)^3

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Index 0, 3, 6, 9, 12 squared; index 4, 8 cubed; rest unchanged
    assert module_0.sum_squares([2] * 13) == 48          # 5*4 + 2*8 + 6*2

    # Negative values with mixed operations
    assert module_0.sum_squares([-2] * 9) == -12         # 3*4 - 2*8 - 4*2

    # Mixed list
    assert module_0.sum_squares([-7, 1, 1, 1, 1, 1, 1, 5]) == 60  # 49 + 1*5 + 5

    # All entries unchanged when no index qualifies
    assert module_0.sum_squares([1, 1, 1]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-01 22:43:59.765232
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element (index 0 is multiple of 3 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Indices 0,1,2: 1^2 + 2 + 3
    assert module_0.sum_squares([1, 2, 3]) == 6

    # Index 3 is multiple of 3 -> squared: 1 + 2 + 3 + 16
    assert module_0.sum_squares([1, 2, 3, 4]) == 22

    # Index 4 is multiple of 4 but not 3 -> cubed: 22 + 125
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Negative numbers: 1 + (-5) + 2 + 1 + (-125)
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126

    # Index 6 (multiple of 3) takes priority over multiple of 4
    assert module_0.sum_squares([2, 2, 2, 2, 2, 2, 2]) == 4 + 2 + 2 + 4 + 2 + 2 + 4

    # Longer list mixing all branches
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # i=0: 1, i=1: 2, i=2: 3, i=3: 16, i=4: 125, i=5: 6,
    # i=6: 49, i=7: 8, i=8: 512
    assert module_0.sum_squares(lst) == 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 512

    # Floats work too
    assert module_0.sum_squares([2.0, 3.0, 4.0]) == 4.0 + 3.0 + 4.0


if __name__ == "__main__":
    test_sum_squares()
    print("All tests passed!")

# Generated at 2026-11-01 22:44:11.335571
# Unit test for function sum_squares
def test_sum_squares():import unittest


class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(module_0.sum_squares([]), 0)

    def test_single_element_squared(self):
        # index 0 is divisible by 3 -> squared
        self.assertEqual(module_0.sum_squares([5]), 25)

    def test_basic_values(self):
        # [1, 2, 3] -> 1**2 + 2 + 3 = 6
        self.assertEqual(module_0.sum_squares([1, 2, 3]), 6)

    def test_mixed_operations(self):
        # indices: 0 sq, 1 same, 2 same, 3 sq, 4 cube
        # 1 + 2 + 3 + 9 + 64 = 79
        self.assertEqual(module_0.sum_squares([1, 2, 3, 4, 5]), 79)

    def test_negative_numbers(self):
        # [-1,-2,-3,-4,-5,-6,-7,-8]
        # 1 + (-2) + (-3) + 9 + (-64) + (-5) + 36 + (-7) + (-512) = -547
        self.assertEqual(module_0.sum_squares([-1, -2, -3, -4, -5, -6, -7, -8]), -547)

    def test_index_divisible_by_both_3_and_4_uses_square(self):
        # [2]*13: indices 0,3,6,9,12 squared (4 each = 20),
        # indices 4,8 cubed (8 each = 16), rest unchanged (2 each x6 = 12)
        self.assertEqual(module_0.sum_squares([2] * 13), 48)

    def test_floats(self):
        # [1.5, 2.0, 3.0] -> 1.5**2 + 2.0 + 3.0 = 7.25
        self.assertAlmostEqual(module_0.sum_squares([1.5, 2.0, 3.0]), 7.25)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 22:44:20.859461
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0
    # basic case, index 0 gets squared
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 4, 9]) == 14
    # index 3 is a multiple of 3 -> squared
    assert module_0.sum_squares([1, 3, 5, 7]) == 58  # 1^2 + 3 + 5 + 7^2
    # indices 4 and 8 are multiples of 4 (but not 3) -> cubed
    assert module_0.sum_squares([1, 1, 1, 1, 2, 1, 1, 1, 3]) == 41  # 1^2+1+1+1^2+2^3+1+1^2+1+3^3
    # negative numbers
    assert module_0.sum_squares([-2, -5, 3, -1, 5, 7]) == 135  # 4 - 5 + 3 + 1 + 125 + 7
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == -126  # 1 - 5 + 2 + 1 - 125
    # index 12 is a multiple of both 3 and 4 -> squared (condition 1 wins)
    assert module_0.sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 4
    # floating point values
    assert abs(module_0.sum_squares([1.4, 4.2, 0]) - 6.16) < 1e-9  # 1.4^2 + 4.2 + 0