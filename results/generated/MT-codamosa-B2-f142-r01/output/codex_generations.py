

# Generated at 2026-10-25 12:38:29.986069
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

# Generated at 2026-10-25 12:38:31.521728
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

# Generated at 2026-10-25 12:38:33.104551
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

# Generated at 2026-10-25 12:38:35.640281
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:38.286835
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:40.821574
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:43.239020
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:45.650645
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:48.063601
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:50.575263
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:52.983727
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:55.399298
# Unit test for function sum_squares

# Generated at 2026-10-25 12:38:57.813732
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:00.227103
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:02.641961
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:05.057936
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:07.471218
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:09.883792
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:12.297893
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:19.035097
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 79  # 1**2 + 2 + 3 + 3**2 + 4**3 = 1+2+3+9+64
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([5]) == 25  # index 0 divisible by 3 -> squared
    assert module_0.sum_squares([2, 2, 2, 2, 2, 2, 2, 2]) == 2 + 2 + 2 + 4 + 8 + 4 + 2 + 8  # i=3 ->4, i=4 ->8, i=7 ->8
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 + 9  # i=0 ->1, i=1 ->-2, i=2 ->9

# Generated at 2026-10-25 12:39:20.469003
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

# Generated at 2026-10-25 12:39:21.844626
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

# Generated at 2026-10-25 12:39:23.345472
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

# Generated at 2026-10-25 12:39:24.877485
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

# Generated at 2026-10-25 12:39:26.460788
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

# Generated at 2026-10-25 12:39:30.392535
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

# Generated at 2026-10-25 12:39:31.881373
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

# Generated at 2026-10-25 12:39:34.412387
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:37.041046
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:39.451193
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:42.179357
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:44.593070
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:47.187299
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:49.596137
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:52.011842
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:54.426152
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:56.839298
# Unit test for function sum_squares

# Generated at 2026-10-25 12:39:59.252438
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:01.670272
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:04.080125
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:06.494464
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:08.909738
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:11.323107
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:13.736093
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:16.149208
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:18.562842
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:24.467989
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 12:40:27.645884
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

# Generated at 2026-10-25 12:40:29.381908
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

# Generated at 2026-10-25 12:40:30.837782
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

# Generated at 2026-10-25 12:40:32.662166
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

# Generated at 2026-10-25 12:40:49.320156
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

# Generated at 2026-10-25 12:40:51.737544
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:54.680001
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:57.097738
# Unit test for function sum_squares

# Generated at 2026-10-25 12:40:59.509253
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:01.922470
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:04.335827
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:06.749186
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:09.329208
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:11.759065
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:14.173669
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:16.588160
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:19.001424
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:21.414662
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:23.828537
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:26.242584
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:28.657220
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:31.071459
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:33.486280
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:35.900704
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:38.313160
# Unit test for function sum_squares

# Generated at 2026-10-25 12:41:40.943616
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 79  # 1**2 + 2 + 3 + 3**2 + 4**3 = 1+2+3+9+64
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([5]) == 25  # index 0 divisible by 3 -> squared
    assert module_0.sum_squares([2, 2, 2, 2, 2, 2, 2, 2]) == 2 + 2 + 2 + 4 + 8 + 4 + 2 + 8  # i=3 ->4, i=4 ->8, i=7 ->8
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 + 9  # i=0 ->1, i=1 ->-2, i=2 ->9

# Generated at 2026-10-25 12:41:57.453274
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

# Generated at 2026-10-25 12:42:14.038989
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

# Generated at 2026-10-25 12:42:16.452315
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:18.866771
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:21.280659
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:23.694780
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:26.107985
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:28.522244
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:32.116296
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:34.533641
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:36.949682
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:39.384575
# Unit test for function sum_squares

# Generated at 2026-10-25 12:42:41.942726
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 79  # 1**2 + 2 + 3 + 3**2 + 4**3 = 1+2+3+9+64
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([5]) == 25  # index 0 divisible by 3 -> squared
    assert module_0.sum_squares([2, 2, 2, 2, 2, 2, 2, 2]) == 2 + 2 + 2 + 4 + 8 + 4 + 2 + 8  # i=3 ->4, i=4 ->8, i=7 ->8
    assert module_0.sum_squares([-1, -2, -3]) == 1 - 2 + 9  # i=0 ->1, i=1 ->-2, i=2 ->9

# Generated at 2026-10-25 12:43:03.191984
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

# Generated at 2026-10-25 12:43:19.934393
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

# Generated at 2026-10-25 12:43:22.527396
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:24.941405
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:27.355096
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:30.103683
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:32.517906
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:34.934018
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:37.349173
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:39.762875
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:42.179161
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:44.596546
# Unit test for function sum_squares

# Generated at 2026-10-25 12:43:46.050390
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 12:43:47.427278
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

# Generated at 2026-10-25 12:43:48.782302
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

# Generated at 2026-10-25 12:44:03.615370
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

# Generated at 2026-10-25 12:44:05.248355
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

# Generated at 2026-10-25 12:44:06.681422
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

# Generated at 2026-10-25 12:44:08.113580
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

# Generated at 2026-10-25 12:44:31.254708
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

# Generated at 2026-10-25 12:44:33.669629
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:36.081206
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:38.495624
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:40.909075
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:43.322982
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:45.739359
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:48.155991
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:50.569848
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:52.982625
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:55.469110
# Unit test for function sum_squares

# Generated at 2026-10-25 12:44:57.883328
# Unit test for function sum_squares

# Generated at 2026-10-25 12:45:00.296293
# Unit test for function sum_squares

# Generated at 2026-10-25 12:45:02.713677
# Unit test for function sum_squares

# Generated at 2026-10-25 12:45:04.251183
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 12:45:23.992960
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

# Generated at 2026-10-25 12:45:46.759739
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

# Generated at 2026-10-25 12:46:06.384980
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

# Generated at 2026-10-25 12:46:07.846403
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

# Generated at 2026-10-25 12:46:09.307332
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

# Generated at 2026-10-25 12:46:14.818265
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

# Generated at 2026-10-25 12:46:16.215486
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

# Generated at 2026-10-25 12:46:17.649964
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

# Generated at 2026-10-25 12:46:19.068664
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

# Generated at 2026-10-25 12:46:35.568372
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

# Generated at 2026-10-25 12:46:38.225808
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:40.639839
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:43.057567
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:45.471313
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:47.887496
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:50.299980
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:52.714120
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:55.129390
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:57.543735
# Unit test for function sum_squares

# Generated at 2026-10-25 12:46:59.960470
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:02.810757
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:05.230274
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:07.645004
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:10.058703
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:11.510073
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 12:47:13.011992
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

# Generated at 2026-10-25 12:47:19.096938
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

# Generated at 2026-10-25 12:47:20.521829
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

# Generated at 2026-10-25 12:47:22.275646
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

# Generated at 2026-10-25 12:47:40.387876
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

# Generated at 2026-10-25 12:47:42.942308
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:45.356170
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:47.769934
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:50.389680
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:52.804962
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:55.216519
# Unit test for function sum_squares

# Generated at 2026-10-25 12:47:57.629280
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:00.289379
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:02.703643
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:05.117905
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:07.533111
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:09.950793
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:12.360754
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:14.774346
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:17.189378
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:19.602838
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:22.018871
# Unit test for function sum_squares

# Generated at 2026-10-25 12:48:24.432744
# Unit test for function sum_squares