

# Generated at 2026-10-25 09:49:18.007146
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:20.421224
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:22.839270
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:25.254526
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:27.667138
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:30.102987
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:32.516855
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:34.935045
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:37.352897
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:39.765380
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:42.180201
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:44.595152
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:47.011515
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:49.427515
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:51.839999
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:54.255349
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:56.670383
# Unit test for function sum_squares

# Generated at 2026-10-25 09:49:59.087365
# Unit test for function sum_squares

# Generated at 2026-10-25 09:50:01.505100
# Unit test for function sum_squares

# Generated at 2026-10-25 09:50:03.917234
# Unit test for function sum_squares

# Generated at 2026-10-25 09:50:06.350574
# Unit test for function sum_squares

# Generated at 2026-10-25 09:50:23.229528
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

# Generated at 2026-10-25 09:50:55.164758
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

# Generated at 2026-10-25 09:51:16.052777
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

# Generated at 2026-10-25 09:51:46.369997
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

# Generated at 2026-10-25 09:52:06.127322
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

# Generated at 2026-10-25 09:52:08.614153
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

# Generated at 2026-10-25 09:52:40.430549
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

# Generated at 2026-10-25 09:52:41.939703
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

# Generated at 2026-10-25 09:52:43.410985
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

# Generated at 2026-10-25 09:52:44.790812
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

# Generated at 2026-10-25 09:52:47.478769
# Unit test for function sum_squares

# Generated at 2026-10-25 09:52:50.082627
# Unit test for function sum_squares

# Generated at 2026-10-25 09:52:52.501025
# Unit test for function sum_squares

# Generated at 2026-10-25 09:52:55.032467
# Unit test for function sum_squares

# Generated at 2026-10-25 09:52:57.445260
# Unit test for function sum_squares

# Generated at 2026-10-25 09:52:59.892788
# Unit test for function sum_squares

# Generated at 2026-10-25 09:53:02.274431
# Unit test for function sum_squares

# Generated at 2026-10-25 09:53:04.692355
# Unit test for function sum_squares

# Generated at 2026-10-25 09:53:07.109225
# Unit test for function sum_squares

# Generated at 2026-10-25 09:53:09.521610
# Unit test for function sum_squares

# Generated at 2026-10-25 09:53:20.369504
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 09:54:01.840381
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

# Generated at 2026-10-25 09:54:21.944250
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

# Generated at 2026-10-25 09:54:23.427996
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

# Generated at 2026-10-25 09:54:44.950001
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

# Generated at 2026-10-25 09:55:16.183843
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

# Generated at 2026-10-25 09:55:42.398048
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

# Generated at 2026-10-25 09:56:11.787063
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

# Generated at 2026-10-25 09:56:14.203102
# Unit test for function sum_squares

# Generated at 2026-10-25 09:56:16.620191
# Unit test for function sum_squares

# Generated at 2026-10-25 09:56:18.134820
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 09:56:19.567323
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

# Generated at 2026-10-25 09:56:21.001825
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

# Generated at 2026-10-25 09:56:40.048112
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

# Generated at 2026-10-25 09:56:41.725415
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

# Generated at 2026-10-25 09:57:02.324883
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

# Generated at 2026-10-25 09:57:04.741659
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:07.155992
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:09.569697
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:11.984829
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:14.398405
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:16.811726
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:19.224862
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:21.639531
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:24.058378
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:26.471645
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:28.888988
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:31.306350
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:33.720887
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:36.136039
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:38.549111
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:40.965580
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:43.382396
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:45.796606
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:48.210971
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:50.624542
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:53.041322
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:55.457414
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:57.871111
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:00.396036
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:02.699067
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:05.115751
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:07.532169
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:09.945354
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:12.425002
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:14.807649
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:17.224417
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:19.641578
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:22.055339
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:24.501213
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:26.912328
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:29.328644
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:31.746758
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:34.161775
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:36.575940
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:38.992574
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:41.405130
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:43.820125
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:46.300889
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:48.712435
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:51.128257
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:53.543558
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:55.960771
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:58.375504
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:00.789118
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:03.203671
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:05.617334
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:08.035180
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:10.451915
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:12.865048
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:15.279047
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:17.695165
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:20.542474
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147