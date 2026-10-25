

# Generated at 2026-10-24 22:11:22.331672
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is divisible by 3

    # Indices 0, 3, 6, 9, 12 are squared.
    # Indices 4 and 8 are cubed.
    # All remaining values are unchanged.
    assert module_0.sum_squares([2] * 13) == 48

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert module_0.sum_squares(values) == 1231

# Generated at 2026-10-24 22:11:28.677655
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it must be squared
    # because the divisibility-by-3 condition is checked first.
    assert module_0.sum_squares(list(range(1, 14))) == 1231

# Generated at 2026-10-24 22:11:34.813691
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it should be squared.
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:11:41.342809
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is squared

    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # 1Â² + 2 + 3 + 4Â² + 5Â³ = 147

    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4
    # Index 12 is divisible by both 3 and 4, so it is squared

# Generated at 2026-10-24 22:11:48.749416
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

    # Indices 0 and 3 are squared; index 4 is cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Tests several square, cube, and unchanged positions.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:11:54.278698
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is divisible by 3
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # 1Â² + 2 + 3 + 4Â² + 5Â³ = 147

    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:11:56.796421
# Unit test for function sum_squares

# Generated at 2026-10-24 22:12:11.352416
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 949

# Generated at 2026-10-24 22:12:20.187437
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([2, 3, 4, 5, 2]) == 44

    # Index 12 is divisible by both 3 and 4, so the value is squared.
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

    # A value at index 4 is cubed.
    values = [0, 0, 0, 0, -2]
    assert module_0.sum_squares(values) == -8

# Generated at 2026-10-24 22:12:28.468370
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

    # Indices 0, 3, 6, 9 are squared.
    # Indices 4 and 8 are cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Negative values verify the difference between squaring and cubing.
    assert module_0.sum_squares([0, 0, 0, -2, -3]) == -23

    # Index 12 is divisible by both 3 and 4, so it is squared.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:12:37.287147
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Indices 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # 1Â² + 2 + 3 + 4Â² + 5Â³ = 147

    # Index 12 is divisible by both 3 and 4, so it is squared
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

    # Negative number at index 4 is cubed
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8

# Generated at 2026-10-24 22:12:45.376161
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it is squared
    # because the first condition takes precedence
    assert module_0.sum_squares([2] * 13) == 48

    # Single element at index 0 is squared
    assert module_0.sum_squares([5]) == 25

# Generated at 2026-10-24 22:12:52.545236
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([2] * 13) == 48  # Index 12 uses square, not cube

# Generated at 2026-10-24 22:13:02.272606
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so the value is squared.
    values = [0] * 12 + [2]
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:13:08.722877
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it is squared
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:13:14.871126
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:13:22.179206
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3, so the value is squared
    assert module_0.sum_squares([2]) == 4

    # Covers unchanged, squared, and cubed values
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4; squaring takes priority
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:13:29.100943
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3, so the value is squared
    assert module_0.sum_squares([5]) == 25

    # Index 3 is squared, and index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4; the first condition wins
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:13:35.452054
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Tests all branches, including index 12, divisible by both 3 and 4.
    # Multiples of 3 take priority and are squared.
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:13:40.466603
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:13:50.812227
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3, so the value is squared.
    assert module_0.sum_squares([2]) == 4

    # Indices 0 and 3 are squared; index 4 is cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it is squared
    # because the first condition takes precedence.
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:13:53.337993
# Unit test for function sum_squares

# Generated at 2026-10-24 22:13:55.877830
# Unit test for function sum_squares

# Generated at 2026-10-24 22:13:58.393182
# Unit test for function sum_squares

# Generated at 2026-10-24 22:14:00.811687
# Unit test for function sum_squares

# Generated at 2026-10-24 22:14:11.497286
# Unit test for function sum_squares
def test_sum_squares():result = module_0.sum_squares([1, 2, 3, 4, 5])
assert result == 147

result = module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2])
assert result == 27

# Generated at 2026-10-24 22:14:20.918456
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0

    # Indices 0, 3, 6, 9 are squared.
    # Indices 4 and 8 are cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it is squared.
    values = [0] * 12 + [2]
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:14:28.289463
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it must be squared.
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:14:35.148888
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:14:42.010119
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

    # Index 12 is divisible by both 3 and 4, so its value is squared.
    values = [0] * 12 + [2]
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:14:48.461316
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 is divisible by 3, so its value is squared.
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # 1Â² + 2 + 3 + 4Â² + 5Â³ = 147

    assert module_0.sum_squares([]) == 0

    # Index 12 is divisible by both 3 and 4.
    # The first condition takes precedence, so the value is squared.
    values = [0] * 12 + [3]
    assert module_0.sum_squares(values) == 9

# Generated at 2026-10-24 22:14:55.578687
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it must be squared.
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:15:02.387581
# Unit test for function sum_squares
def test_sum_squares():
    # Indices 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by both 3 and 4, but is squared
    assert module_0.sum_squares([3]) == 9

    # Longer example
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:15:09.350755
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it should be squared
    # because the `if i % 3 == 0` branch is checked first.
    values = list(range(1, 14))
    assert module_0.sum_squares(values) == 1231

# Generated at 2026-10-24 22:15:15.602411
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # Indices: 0âsquare, 1âunchanged, 2âunchanged,
    #          3âsquare, 4âcube

# Generated at 2026-10-24 22:15:23.993968
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it must be squared.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:15:33.723084
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

    # Index 0, 3, 6, 9: squared
    # Index 4, 8: cubed
    # Other indices: unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it is squared
    values = [0] * 12 + [2]
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:15:42.121225
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([3]) == 9
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so the value is squared.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:15:50.408814
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 4 is divisible by 4, so its value is cubed.
    assert module_0.sum_squares([0, 0, 0, 0, 2]) == 8

    # Index 12 is divisible by both 3 and 4; squaring takes priority.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:15:57.174214
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so its value is squared.
    assert module_0.sum_squares(list(range(1, 14))) == 1231

# Generated at 2026-10-24 22:15:59.593643
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:02.008455
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:04.428148
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:19.392800
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([-1, -2, -3]) == -4
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 882
    assert module_0.sum_squares([1] * 13) == 13

# Generated at 2026-10-24 22:16:26.163442
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:16:33.309734
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4           # Index 0: squared
    assert module_0.sum_squares([2, 3, 4]) == 11    # 2Â² + 3 + 4

    # Tests square, cube, unchanged, and overlapping index 12
    values = list(range(1, 14))
    assert module_0.sum_squares(values) == 1231

# Generated at 2026-10-24 22:16:40.896126
# Unit test for function sum_squares
def test_sum_squares():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2]

    # Indices divisible by 3 are squared.
    # Other indices divisible by 4 are cubed.
    assert module_0.sum_squares(values) == 1066

    # Edge case
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 22:16:47.450197
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Covers:
    # index 0 and 3 -> squared
    # index 4       -> cubed
    # other indices -> unchanged
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it is squared
    # because the first condition takes priority.
    values = [2] * 13
    assert module_0.sum_squares(values) == 48

# Generated at 2026-10-24 22:16:50.093466
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:52.507282
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:54.927971
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:57.342072
# Unit test for function sum_squares

# Generated at 2026-10-24 22:16:59.758744
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:02.174682
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:04.590829
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:07.009528
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:09.429146
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:11.847235
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:14.263060
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:16.683729
# Unit test for function sum_squares

# Generated at 2026-10-24 22:17:19.258529
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([-1, -2, -3]) == -4
    assert module_0.sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 882
    assert module_0.sum_squares([1] * 13) == 13

# Generated at 2026-10-24 22:17:27.276523
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1]) == 1
    assert module_0.sum_squares(list(range(13))) == 882

# Generated at 2026-10-24 22:17:34.147822
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4, so it should be squared.
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:17:41.313432
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:17:47.661975
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares(list(range(1, 11))) == 1039

    # Index 12 is divisible by both 3 and 4, so it should be squared.
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:17:53.496072
# Unit test for function sum_squares
def test_sum_squares():
    # Indices 0 and 3 are squared; index 4 is cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6]) == 153

    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([3]) == 9
    assert module_0.sum_squares([1, 1, 1, 1, 1]) == 5

# Generated at 2026-10-24 22:18:02.717183
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([2] * 13) == 48

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-10-24 22:18:05.135655
# Unit test for function sum_squares

# Generated at 2026-10-24 22:18:07.554014
# Unit test for function sum_squares

# Generated at 2026-10-24 22:18:09.972308
# Unit test for function sum_squares

# Generated at 2026-10-24 22:18:12.389164
# Unit test for function sum_squares

# Generated at 2026-10-24 22:18:14.806140
# Unit test for function sum_squares

# Generated at 2026-10-24 22:18:16.168388
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 949

# Generated at 2026-10-24 22:18:24.527501
# Unit test for function sum_squares
def test_sum_squares():
    # Covers normal, square, cube, and overlapping indices.
    # Index 12 is divisible by both 3 and 4, so it is squared.
    assert module_0.sum_squares(list(range(1, 14))) == 1231

    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

# Generated at 2026-10-24 22:18:33.233419
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4                 # Index 0: squared
    assert module_0.sum_squares([0, 2]) == 2              # Index 1: unchanged
    assert module_0.sum_squares([0, 0, 0, 2]) == 4        # Index 3: squared
    assert module_0.sum_squares([0, 0, 0, 0, 2]) == 8     # Index 4: cubed

    # Index 12 is divisible by both 3 and 4, so the first condition wins.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-24 22:18:39.988886
# Unit test for function sum_squares
def test_sum_squares():
    # Indices 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 12 is divisible by both 3 and 4, so it is squared
    values = [0] * 12 + [2]
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:18:47.879006
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Covers indices divisible by 3, divisible by 4, and index 12,
    # which is divisible by both (the square rule takes precedence).
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:18:55.349149
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Exercises square, cube, and unchanged branches
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4; the square branch takes priority
    assert module_0.sum_squares([2] * 13) == 48

# Generated at 2026-10-24 22:18:57.774439
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:00.195002
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:02.614351
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:05.031484
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:07.452464
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:09.866115
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:12.403697
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:14.822527
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:17.242629
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:19.656331
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:31.008519
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-24 22:19:37.947657
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0: squared
    assert module_0.sum_squares([0, 0, 0, 3]) == 9  # Index 3: squared
    assert module_0.sum_squares([0, 0, 0, 0, 2]) == 8  # Index 4: cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-24 22:19:45.114843
# Unit test for function sum_squares
def test_sum_squares():
    lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Transformed values:
    # [2Â², 3, 4, 5Â², 6Â³, 7, 8Â², 9, 10Â³]
    expected = 1332

    assert module_0.sum_squares(lst) == expected
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 22:19:52.963977
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

    # Indices 0, 3, 6, 9 are squared.
    # Indices 4 and 8 are cubed.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

    # Index 12 is divisible by both 3 and 4, so it is squared.
    assert module_0.sum_squares([0] * 12 + [2]) == 4

# Generated at 2026-10-24 22:19:55.482450
# Unit test for function sum_squares

# Generated at 2026-10-24 22:19:57.900610
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:00.316819
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:02.733105
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:05.149799
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:07.570712
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:09.989406
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:12.407921
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:14.825802
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:17.249514
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:19.663312
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:22.082583
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:24.500074
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:26.920088
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:29.336893
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:31.755752
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:34.171765
# Unit test for function sum_squares

# Generated at 2026-10-24 22:20:47.477817
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 22:20:54.549858
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is squared

    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

    # Index 12 is divisible by both 3 and 4, so it is squared
    # because the first condition takes precedence.
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-24 22:21:02.439418
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3, so the value is squared
    assert module_0.sum_squares([2]) == 4

    # Indices 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

    # Index 12 is divisible by both 3 and 4; squaring takes priority
    values = [0] * 12 + [3]
    assert module_0.sum_squares(values) == 9

# Generated at 2026-10-24 22:21:07.205359
# Unit test for function sum_squares

# Generated at 2026-10-24 22:21:09.727479
# Unit test for function sum_squares

# Generated at 2026-10-24 22:21:12.148151
# Unit test for function sum_squares

# Generated at 2026-10-24 22:21:14.565843
# Unit test for function sum_squares

# Generated at 2026-10-24 22:21:16.984746
# Unit test for function sum_squares

# Generated at 2026-10-24 22:21:19.403880
# Unit test for function sum_squares