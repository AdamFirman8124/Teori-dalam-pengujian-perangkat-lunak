

# Generated at 2026-10-25 11:16:26.456416
# Unit test for function sum_squares
def test_sum_squares():
    # Indices 0, 3, and 6 are squared.
    # Index 4 is cubed.
    # All other values remain unchanged.
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7]) == 202

    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

# Generated at 2026-10-25 11:16:35.577953
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([-3]) == 9

    # Index 4 is cubed
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8

    # Index 12 is divisible by both 3 and 4, so it is squared
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

# Generated at 2026-10-25 11:16:43.048435
# Unit test for function sum_squares
def test_sum_squares():
    # Index 0 is squared
    assert module_0.sum_squares([2]) == 4

    # Indices 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125

    # Index 12 is divisible by both 3 and 4, so it is squared
    assert module_0.sum_squares(list(range(1, 14))) == 1231

    # Edge cases
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([-2, 1, 1, -3, -2]) == 4 + 1 + 1 + 9 - 8

# Generated at 2026-10-25 11:16:56.459013
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:17:13.150134
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:17:20.522207
# Unit test for function sum_squares
def test_sum_squares():
    # Indices 0, 3, 6, and 9 are squared.
    # Indices 4 and 8 are cubed.
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert module_0.sum_squares(lst) == 1039

    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4

test_sum_squares()
print("All tests passed.")

# Generated at 2026-10-25 11:17:38.381456
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:18:01.074565
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Index 0 and 3 are squared; index 4 is cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    # 1Â² + 2 + 3 + 4Â² + 5Â³ = 147

    # Index divisible by both 3 and 4 follows the square condition
    values = [0] * 13
    values[12] = 2
    assert module_0.sum_squares(values) == 4

    # Value at index 4 is cubed
    values = [0] * 5
    values[4] = 3
    assert module_0.sum_squares(values) == 27

# Generated at 2026-10-25 11:18:17.503689
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:18:34.150090
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:18:42.856176
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4  # Index 0 is squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-25 11:18:59.444191
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:19:15.928805
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:19:32.620901
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:19:39.176952
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1039

# Generated at 2026-10-25 11:19:42.654560
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:19:44.147539
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:20:00.677446
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:20:17.298827
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:20:37.849521
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:20:54.337343
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:21:10.924944
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:21:27.722581
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:23:00.595592
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:23:18.930266
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:23:36.948187
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:23:55.072879
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:24:13.097297
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:24:29.633435
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:24:32.050156
# Unit test for function sum_squares

# Generated at 2026-10-25 11:24:34.463891
# Unit test for function sum_squares

# Generated at 2026-10-25 11:24:36.880237
# Unit test for function sum_squares

# Generated at 2026-10-25 11:24:53.371204
# Unit test for function sum_squares
def test_sum_squares():
    # empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared
    assert module_0.sum_squares([5]) == 25

    # i=0 squared, i=1,2 unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # = 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 16  # = 22

    # i=4 cubed (4%4==0 and 4%3!=0)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # = 147

    # mixed
    assert module_0.sum_squares([2, 3, 4, 5, 6]) == 4 + 3 + 4 + 25 + 216  # = 252

    # i=8 cubed, i=9 squared, i=12 squared (not cubed, %3 takes precedence)
    lst = list(range(13))  # [0..12]
    # 0 +1+2 +9 +64 +5 +36 +7 +512 +81 +10+11 +144
    assert module_0.sum_squares(lst) == 882

# Generated at 2026-10-25 11:25:09.825965
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:25:12.241761
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:14.823244
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:17.229064
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:19.641371
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:22.055304
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:24.470062
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:26.883913
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:29.297709
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:31.716856
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:34.130797
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:36.542407
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:38.967571
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:41.381803
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:43.797719
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:46.214523
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:48.628851
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:51.041058
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:53.454485
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:55.868446
# Unit test for function sum_squares

# Generated at 2026-10-25 11:25:58.285111
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:00.700729
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:03.117728
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:05.528513
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:07.942745
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:10.357071
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:12.771251
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:15.187564
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:17.604284
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:20.020810
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:22.434261
# Unit test for function sum_squares