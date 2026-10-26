

# Generated at 2026-10-25 09:54:14.334803
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

# Generated at 2026-10-25 09:54:55.293625
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

# Generated at 2026-10-25 09:54:57.708783
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:00.312926
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:02.730200
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:05.142664
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:07.643737
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:09.999646
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:12.414063
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:14.830488
# Unit test for function sum_squares

# Generated at 2026-10-25 09:55:20.073351
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 09:55:21.612915
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

# Generated at 2026-10-25 09:55:23.054197
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

# Generated at 2026-10-25 09:55:27.753627
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

# Generated at 2026-10-25 09:55:29.289673
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

# Generated at 2026-10-25 09:55:30.826566
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

# Generated at 2026-10-25 09:55:32.355045
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

# Generated at 2026-10-25 09:55:33.795260
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

# Generated at 2026-10-25 09:55:35.948182
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

# Generated at 2026-10-25 09:55:55.309926
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

# Generated at 2026-10-25 09:56:32.062483
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

# Generated at 2026-10-25 09:56:33.581346
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

# Generated at 2026-10-25 09:56:36.491218
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

# Generated at 2026-10-25 09:56:55.613154
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

# Generated at 2026-10-25 09:56:58.196023
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:00.611753
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:03.196431
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:05.610838
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:08.025452
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:10.450779
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:12.855298
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:15.268619
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:17.682842
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:20.096754
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:22.510890
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:24.925554
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:27.340003
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:29.758647
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:32.175721
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:34.587906
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:37.005927
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:39.417098
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:41.834135
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:44.250589
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:46.662770
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:49.077524
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:51.493123
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:53.910433
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:56.326797
# Unit test for function sum_squares

# Generated at 2026-10-25 09:57:58.739843
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:01.153161
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:03.568381
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:05.986275
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:08.403070
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:10.815647
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:13.230075
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:15.644002
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:18.061336
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:20.479057
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:22.891239
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:25.305376
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:27.720056
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:30.138413
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:32.555438
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:34.968442
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:37.385022
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:39.797652
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:42.211202
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:44.626675
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:47.041909
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:49.457267
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:51.871789
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:54.289839
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:56.706561
# Unit test for function sum_squares

# Generated at 2026-10-25 09:58:59.120916
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:01.535439
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:03.954627
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:06.366504
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:08.783597
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:11.197126
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:13.612922
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:16.026204
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:18.442512
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:21.329223
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 09:59:22.866594
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

# Generated at 2026-10-25 09:59:24.518294
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

# Generated at 2026-10-25 09:59:26.245786
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

# Generated at 2026-10-25 09:59:27.991174
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

# Generated at 2026-10-25 09:59:29.934092
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

# Generated at 2026-10-25 09:59:46.623338
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

# Generated at 2026-10-25 09:59:49.041253
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:51.454111
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:53.868395
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:56.452459
# Unit test for function sum_squares

# Generated at 2026-10-25 09:59:58.870747
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:01.298490
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:03.712181
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:06.126591
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:08.544388
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:10.960657
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:13.373946
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:15.788252
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:18.202670
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:20.617594
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:23.030752
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:25.443875
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:27.860493
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:30.276192
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:32.690673
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:35.105518
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:37.522330
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:39.935247
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:42.351479
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:44.768262
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:47.184337
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:49.600558
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:52.017057
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:54.427220
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:56.843911
# Unit test for function sum_squares

# Generated at 2026-10-25 10:00:59.259959
# Unit test for function sum_squares

# Generated at 2026-10-25 10:01:01.674042
# Unit test for function sum_squares

# Generated at 2026-10-25 10:01:04.087554
# Unit test for function sum_squares

# Generated at 2026-10-25 10:01:06.502727
# Unit test for function sum_squares

# Generated at 2026-10-25 10:01:30.361972
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

# Generated at 2026-10-25 10:01:50.155358
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

# Generated at 2026-10-25 10:01:51.546727
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

# Generated at 2026-10-25 10:02:08.222747
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

# Generated at 2026-10-25 10:02:09.676252
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

# Generated at 2026-10-25 10:02:27.802456
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

# Generated at 2026-10-25 10:02:57.393476
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

# Generated at 2026-10-25 10:02:58.818646
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

# Generated at 2026-10-25 10:03:04.461230
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

# Generated at 2026-10-25 10:03:06.099562
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

# Generated at 2026-10-25 10:03:10.554757
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

# Generated at 2026-10-25 10:03:12.087784
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

# Generated at 2026-10-25 10:03:13.589740
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

# Generated at 2026-10-25 10:03:15.114742
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

# Generated at 2026-10-25 10:03:16.546238
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

# Generated at 2026-10-25 10:03:33.347194
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

# Generated at 2026-10-25 10:03:50.148650
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

# Generated at 2026-10-25 10:04:06.710559
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

# Generated at 2026-10-25 10:04:09.121044
# Unit test for function sum_squares

# Generated at 2026-10-25 10:04:11.535168
# Unit test for function sum_squares

# Generated at 2026-10-25 10:04:13.949060
# Unit test for function sum_squares

# Generated at 2026-10-25 10:04:16.364907
# Unit test for function sum_squares

# Generated at 2026-10-25 10:04:19.916561
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939