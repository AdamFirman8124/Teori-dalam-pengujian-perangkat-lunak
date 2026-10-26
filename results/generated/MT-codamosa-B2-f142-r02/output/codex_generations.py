

# Generated at 2026-10-25 06:54:03.083206
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4                  # index 0 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 22        # index 3 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 2]) == 12     # index 4 -> cubed
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8    # negative cube
    assert module_0.sum_squares(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ) == 1231                                     # mixed branches, incl. index 12

# Generated at 2026-10-25 06:54:04.625943
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

# Generated at 2026-10-25 06:54:06.059263
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

# Generated at 2026-10-25 06:54:07.588248
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

# Generated at 2026-10-25 06:54:09.027947
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

# Generated at 2026-10-25 06:54:10.565458
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

# Generated at 2026-10-25 06:54:11.998468
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

# Generated at 2026-10-25 06:54:13.386488
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

# Generated at 2026-10-25 06:54:14.917970
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

# Generated at 2026-10-25 06:54:16.300227
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

# Generated at 2026-10-25 06:54:17.834488
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

# Generated at 2026-10-25 06:54:19.277856
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

# Generated at 2026-10-25 06:54:20.701396
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

# Generated at 2026-10-25 06:54:22.146407
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

# Generated at 2026-10-25 06:54:23.742677
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

# Generated at 2026-10-25 06:54:25.245991
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

# Generated at 2026-10-25 06:54:27.670011
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:30.083877
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:32.497889
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:34.912986
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:37.465863
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:39.912914
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:42.327777
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:44.741134
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:47.323563
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:49.740257
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:52.155921
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:54.574207
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:56.995724
# Unit test for function sum_squares

# Generated at 2026-10-25 06:54:59.405939
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:01.823817
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:04.240935
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:06.652201
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:09.068538
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:11.484428
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:13.898417
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:16.315000
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:18.732699
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:21.148298
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:23.563306
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:25.976368
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:28.390511
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:30.807183
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:33.224220
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:35.638826
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:38.055545
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:40.472405
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:43.011426
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:45.423774
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:47.839690
# Unit test for function sum_squares

# Generated at 2026-10-25 06:55:50.494170
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 06:55:51.869316
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

# Generated at 2026-10-25 06:55:53.547742
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

# Generated at 2026-10-25 06:55:54.937098
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

# Generated at 2026-10-25 06:55:56.555813
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

# Generated at 2026-10-25 06:55:58.023080
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

# Generated at 2026-10-25 06:55:59.515191
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

# Generated at 2026-10-25 06:56:00.944245
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

# Generated at 2026-10-25 06:56:02.397719
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

# Generated at 2026-10-25 06:56:03.931135
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

# Generated at 2026-10-25 06:56:05.442196
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

# Generated at 2026-10-25 06:56:06.886982
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

# Generated at 2026-10-25 06:56:08.426702
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

# Generated at 2026-10-25 06:56:09.916936
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

# Generated at 2026-10-25 06:56:11.501871
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

# Generated at 2026-10-25 06:56:14.191559
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:16.888676
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:19.310416
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:21.721309
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:24.135444
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:26.552424
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:28.972104
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:31.388433
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:33.805624
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:36.217050
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:38.633942
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:41.050480
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:43.496189
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:45.877427
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:48.294292
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:50.707384
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:53.126672
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:55.542017
# Unit test for function sum_squares

# Generated at 2026-10-25 06:56:57.954463
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:00.372431
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:03.008579
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 06:57:04.554196
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

# Generated at 2026-10-25 06:57:05.969924
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

# Generated at 2026-10-25 06:57:07.410161
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

# Generated at 2026-10-25 06:57:08.844612
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

# Generated at 2026-10-25 06:57:10.482576
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

# Generated at 2026-10-25 06:57:11.933059
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

# Generated at 2026-10-25 06:57:13.557187
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

# Generated at 2026-10-25 06:57:15.091500
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

# Generated at 2026-10-25 06:57:16.627065
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

# Generated at 2026-10-25 06:57:18.162265
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

# Generated at 2026-10-25 06:57:19.698817
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

# Generated at 2026-10-25 06:57:21.338573
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

# Generated at 2026-10-25 06:57:22.877201
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

# Generated at 2026-10-25 06:57:25.400303
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:28.082074
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:30.498148
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:32.912499
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:35.525955
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:37.941648
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:40.515650
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:42.930022
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:45.344008
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:48.899454
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:51.299614
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:53.713991
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:56.128558
# Unit test for function sum_squares

# Generated at 2026-10-25 06:57:58.542120
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:00.956481
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:03.370241
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:07.940262
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 06:58:09.780248
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

# Generated at 2026-10-25 06:58:11.307224
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

# Generated at 2026-10-25 06:58:12.843707
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

# Generated at 2026-10-25 06:58:14.276466
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

# Generated at 2026-10-25 06:58:15.812873
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

# Generated at 2026-10-25 06:58:18.236584
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

# Generated at 2026-10-25 06:58:20.186642
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

# Generated at 2026-10-25 06:58:26.576812
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

# Generated at 2026-10-25 06:58:28.100769
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

# Generated at 2026-10-25 06:58:29.541966
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

# Generated at 2026-10-25 06:58:31.071768
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4                  # index 0 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 22        # index 3 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 2]) == 12     # index 4 -> cubed
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8    # negative cube
    assert module_0.sum_squares(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ) == 1231                                     # mixed branches, incl. index 12

# Generated at 2026-10-25 06:58:32.505210
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

# Generated at 2026-10-25 06:58:33.941548
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

# Generated at 2026-10-25 06:58:35.373249
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

# Generated at 2026-10-25 06:58:36.806200
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

# Generated at 2026-10-25 06:58:38.341174
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

# Generated at 2026-10-25 06:58:39.774589
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

# Generated at 2026-10-25 06:58:50.864811
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:53.278753
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:55.692320
# Unit test for function sum_squares

# Generated at 2026-10-25 06:58:58.107022
# Unit test for function sum_squares

# Generated at 2026-10-25 06:59:00.519326
# Unit test for function sum_squares

# Generated at 2026-10-25 06:59:02.933130
# Unit test for function sum_squares

# Generated at 2026-10-25 06:59:05.589477
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 6
    assert module_0.sum_squares([1, 2, 3, 4]) == 22
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 147

# Generated at 2026-10-25 06:59:07.054202
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

# Generated at 2026-10-25 06:59:08.426617
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

# Generated at 2026-10-25 06:59:09.882040
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

# Generated at 2026-10-25 06:59:11.314252
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

# Generated at 2026-10-25 06:59:12.749383
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

# Generated at 2026-10-25 06:59:14.386999
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

# Generated at 2026-10-25 06:59:16.025712
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

# Generated at 2026-10-25 06:59:34.761572
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

# Generated at 2026-10-25 06:59:36.300688
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([2]) == 4                  # index 0 -> squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 22        # index 3 -> squared
    assert module_0.sum_squares([1, 1, 1, 1, 2]) == 12     # index 4 -> cubed
    assert module_0.sum_squares([0, 0, 0, 0, -2]) == -8    # negative cube
    assert module_0.sum_squares(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ) == 1231                                     # mixed branches, incl. index 12

# Generated at 2026-10-25 06:59:38.040863
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

# Generated at 2026-10-25 06:59:39.576741
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

# Generated at 2026-10-25 06:59:41.112997
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

# Generated at 2026-10-25 06:59:42.648698
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

# Generated at 2026-10-25 06:59:44.390677
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

# Generated at 2026-10-25 06:59:46.232380
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

# Generated at 2026-10-25 06:59:47.665755
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

# Generated at 2026-10-25 06:59:49.202498
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

# Generated at 2026-10-25 07:00:28.406275
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

# Generated at 2026-10-25 07:00:29.851732
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

# Generated at 2026-10-25 07:00:31.262930
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

# Generated at 2026-10-25 07:00:32.691577
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

# Generated at 2026-10-25 07:00:34.144343
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

# Generated at 2026-10-25 07:00:35.596736
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

# Generated at 2026-10-25 07:00:38.238669
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:41.027373
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:43.446513
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:46.054458
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:48.641785
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:51.059618
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:53.471970
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:55.886151
# Unit test for function sum_squares

# Generated at 2026-10-25 07:00:58.301902
# Unit test for function sum_squares

# Generated at 2026-10-25 07:01:00.715890
# Unit test for function sum_squares

# Generated at 2026-10-25 07:01:03.133027
# Unit test for function sum_squares

# Generated at 2026-10-25 07:01:05.552658
# Unit test for function sum_squares

# Generated at 2026-10-25 07:02:25.498375
# Unit test for function sum_squares

# Generated at 2026-10-25 07:02:27.913654
# Unit test for function sum_squares

# Generated at 2026-10-25 07:02:30.316836
# Unit test for function sum_squares

# Generated at 2026-10-25 07:02:31.685513
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

# Generated at 2026-10-25 07:02:33.136269
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

# Generated at 2026-10-25 07:02:34.576234
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

# Generated at 2026-10-25 07:02:36.004106
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

# Generated at 2026-10-25 07:02:37.436871
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

# Generated at 2026-10-25 07:02:38.870244
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

# Generated at 2026-10-25 07:02:40.303144
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

# Generated at 2026-10-25 07:02:41.839370
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

# Generated at 2026-10-25 07:02:43.275835
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