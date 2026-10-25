

# Generated at 2026-10-24 10:57:06.759803
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:57:08.191766
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:57:09.626629
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:57:26.083472
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:57:42.597500
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:57:45.104194
# Unit test for function sum_squares

# Generated at 2026-10-24 10:57:47.519878
# Unit test for function sum_squares

# Generated at 2026-10-24 10:57:50.093372
# Unit test for function sum_squares

# Generated at 2026-10-24 10:57:52.525597
# Unit test for function sum_squares

# Generated at 2026-10-24 10:57:54.944422
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:04.107727
# Unit test for function sum_squares
def test_sum_squares():
    # i%3==0 -> square (including i=0), i%4==0 and i%3!=0 -> cube, else unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # indices 0,1,2
    assert module_0.sum_squares([2, 3, 4, 5]) == 2**2 + 3 + 4 + 5**2  # i=0 and i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # i=0,3 squared; i=4 cubed
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([7]) == 49  # only index 0 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1  # every term contributes 1
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 4 + 2 + 2 + 4 + 8  # i=4 -> cube of 2

# Generated at 2026-10-24 10:58:05.433502
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:58:21.787656
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:58:35.130303
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 10:58:37.644052
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:40.202127
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:42.621150
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:45.037740
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:47.453345
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:49.873667
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:52.291761
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:54.712810
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:57.134798
# Unit test for function sum_squares

# Generated at 2026-10-24 10:58:59.569083
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:02.175649
# Unit test for function sum_squares
def test_sum_squares():
    # i%3==0 -> square (including i=0), i%4==0 and i%3!=0 -> cube, else unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # indices 0,1,2
    assert module_0.sum_squares([2, 3, 4, 5]) == 2**2 + 3 + 4 + 5**2  # i=0 and i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # i=0,3 squared; i=4 cubed
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([7]) == 49  # only index 0 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1  # every term contributes 1
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 4 + 2 + 2 + 4 + 8  # i=4 -> cube of 2

# Generated at 2026-10-24 10:59:18.594102
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:59:34.962978
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 10:59:37.383636
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:39.801920
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:42.220010
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:44.636640
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:47.084959
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:49.470713
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:51.891405
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:54.306632
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:56.724476
# Unit test for function sum_squares

# Generated at 2026-10-24 10:59:59.140878
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:01.572935
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:03.989200
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:06.412260
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:08.836691
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:11.253083
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:13.673744
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:16.090096
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:18.513221
# Unit test for function sum_squares

# Generated at 2026-10-24 11:00:34.969488
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:00:51.355993
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:07.913777
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:10.332494
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:12.836627
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:15.253176
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:17.668080
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:20.086907
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:32.998731
# Unit test for function sum_squares
def test_sum_squares():lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Generated at 2026-10-24 11:01:34.349704
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:01:35.670074
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:36.988672
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:38.426372
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:01:40.039776
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:41.461164
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:42.789682
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:44.262641
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:01:45.681785
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:47.134464
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:01:49.642057
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:52.143357
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:54.560591
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:57.245239
# Unit test for function sum_squares

# Generated at 2026-10-24 11:01:59.663401
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:02.110889
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:04.504246
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:06.923501
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:09.340888
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:11.760557
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:14.179887
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:16.595735
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:19.013452
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:21.429807
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:23.849248
# Unit test for function sum_squares

# Generated at 2026-10-24 11:02:44.116465
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0
    # Indices: 0 (sq), 1 (same), 2 (same), 3 (sq), 4 (cube), 5 (same), 6 (sq), 7 (same), 8 (cube), 9 (sq)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3              # only index 0 squared
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16      # idx 0 sq, idx 3 sq
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # idx 4 cubed
    assert module_0.sum_squares([-1, -2, -3, -4]) == 1 + (-2) + (-3) + 16  # negatives: sq of idx3
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 4 + 2 + 2 + 4 + 8     # idx 0,3 sq; idx 4 cube
    assert module_0.sum_squares([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == (
        25 + 5 + 5 + 25 + 125 + 5 + 25 + 5 + 125 + 25 + 5 + 5 + 25
    )
    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-10-24 11:02:45.601667
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:02:47.242500
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:03:03.836188
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:03:20.313939
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:03:36.801648
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:03:53.187926
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:04:09.552951
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:04:11.978716
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:14.552290
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:16.974963
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:19.394715
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:21.974073
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:24.395218
# Unit test for function sum_squares

# Generated at 2026-10-24 11:04:41.221800
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:04:57.711010
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:05:14.185291
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:05:16.968015
# Unit test for function sum_squares

# Generated at 2026-10-24 11:05:19.389559
# Unit test for function sum_squares

# Generated at 2026-10-24 11:05:21.807634
# Unit test for function sum_squares

# Generated at 2026-10-24 11:05:24.234447
# Unit test for function sum_squares

# Generated at 2026-10-24 11:05:26.754214
# Unit test for function sum_squares
def test_sum_squares():
    # i%3==0 -> square (including i=0), i%4==0 and i%3!=0 -> cube, else unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # indices 0,1,2
    assert module_0.sum_squares([2, 3, 4, 5]) == 2**2 + 3 + 4 + 5**2  # i=0 and i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # i=0,3 squared; i=4 cubed
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([7]) == 49  # only index 0 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1  # every term contributes 1
    assert module_0.sum_squares([2, 2, 2, 2, 2]) == 4 + 2 + 2 + 4 + 8  # i=4 -> cube of 2

# Generated at 2026-10-24 11:05:43.367377
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:05:59.856000
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # index 0 is squared: 0 % 3 == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # index 3 is squared: 3 % 3 == 0
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # 22

    # index 4 is cubed: 4 % 4 == 0 and 4 % 3 != 0

# Generated at 2026-10-24 11:06:02.279847
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:04.696270
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:07.115791
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:09.533263
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:11.952498
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:14.366919
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:16.785478
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:19.201595
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:21.622119
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:24.041669
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:26.459990
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:28.878747
# Unit test for function sum_squares

# Generated at 2026-10-24 11:06:30.253833
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:06:31.676851
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 11:06:55.356080
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element, index 0 (divisible by 3 â squared)
    assert module_0.sum_squares([2]) == 4

    # Index 0 squared, index 1 unchanged
    assert module_0.sum_squares([1, 3]) == 1 + 3

    # Index 0 squared, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16

    # Index 4 is divisible by 4 (not 3) â cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 0 (sq), 3 (sq), 4 (cube), 8 (cube), 12 (sq)
    assert module_0.sum_squares(list(range(13))) == (
        0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9 + 10 + 11 + 12**2
    )

    # Negative numbers: squares/cubes preserve sign rules correctly
    assert module_0.sum_squares([-1, -2, -3, -4, -5]) == 1 - 2 - 3 + 16 - 125

    # Index 12: divisible by both 3 and 4 â squared (3 wins, not cubed)
    assert module_0.sum_squares([2] * 13) == 11 * 2 + 2**12

    print("All tests passed!")


test_sum_squares()