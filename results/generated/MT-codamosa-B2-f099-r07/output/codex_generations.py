

# Generated at 2026-10-25 03:20:57.987941
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above .5
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Exact .5 values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.0000") == 4

# Generated at 2026-10-25 03:21:00.404929
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:02.819822
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:05.234423
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:07.825970
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:10.241633
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:12.656881
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:15.073401
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:17.488366
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:19.905114
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:22.323247
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:24.735238
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:27.149913
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:29.563703
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:31.978095
# Unit test for function closest_integer

# Generated at 2026-10-25 03:21:34.836185
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:21:44.261296
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Halfway values must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("5.000") == 5

    # Values close to, but not exactly, halfway
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

# Generated at 2026-10-25 03:21:51.634319
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:22:00.748471
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("1.49") == 1
    assert module_0.closest_integer("-1.49") == -1
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:22:09.042526
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4


test_closest_integer()

# Generated at 2026-10-25 03:22:11.463357
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:13.879399
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:16.295592
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:18.711149
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:21.256010
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:23.668495
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:26.082138
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:28.662865
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:31.079266
# Unit test for function closest_integer

# Generated at 2026-10-25 03:22:38.536519
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:22:46.114507
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:22:53.984282
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:23:01.359711
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:23:10.892875
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("3.50") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:23:13.313117
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:15.729944
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:18.147036
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:20.560711
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:22.977762
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:25.389308
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:27.804472
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:30.218121
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:32.632550
# Unit test for function closest_integer

# Generated at 2026-10-25 03:23:41.612529
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:23:50.395292
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:23:59.595061
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Exact halves must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("-2.0") == -2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    # Values around half
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:24:07.525477
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0

# Generated at 2026-10-25 03:24:13.872368
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:24:21.654504
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:24:30.663655
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("123.000") == 123

    # Values close to, but not exactly, .5
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

# Generated at 2026-10-25 03:24:40.912032
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:24:48.992183
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:24:57.254550
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.00") == 3


test_closest_integer()

# Generated at 2026-10-25 03:25:05.479334
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

# Generated at 2026-10-25 03:25:12.449653
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.2") == 14
    assert module_0.closest_integer("14.8") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.2") == -14
    assert module_0.closest_integer("-14.8") == -15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3


test_closest_integer()

# Generated at 2026-10-25 03:25:21.555963
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10

    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Values exactly halfway are rounded away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.0000") == 4

# Generated at 2026-10-25 03:25:30.157427
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Values ending in .5 must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("4.000") == 4

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:25:37.641231
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Other negative and zero values
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4
    assert module_0.closest_integer("0") == 0


test_closest_integer()

# Generated at 2026-10-25 03:25:45.210804
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values around zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 03:25:52.174256
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.000") == 0
    assert module_0.closest_integer("-2.0") == -2

# Generated at 2026-10-25 03:25:54.591471
# Unit test for function closest_integer

# Generated at 2026-10-25 03:25:57.395260
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:26:05.792760
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 03:26:13.882282
# Unit test for function closest_integer
def test_closest_integer():
    # Values below and above the halfway point
    assert module_0.closest_integer("10.4") == 10
    assert module_0.closest_integer("10.6") == 11
    assert module_0.closest_integer("-10.4") == -10
    assert module_0.closest_integer("-10.6") == -11

    # Halfway values round away from zero
    assert module_0.closest_integer("10.5") == 11
    assert module_0.closest_integer("-10.5") == -11
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Integers and trailing zeros
    assert module_0.closest_integer("7") == 7
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("2.000") == 2

# Generated at 2026-10-25 03:26:22.453322
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 03:26:31.379941
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("2.000") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 03:26:39.790634
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:26:48.082341
# Unit test for function closest_integer
def test_closest_integer():
    # Exact integers
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10

    # Normal rounding
    assert module_0.closest_integer("2.3") == 2
    assert module_0.closest_integer("2.7") == 3
    assert module_0.closest_integer("-2.3") == -2
    assert module_0.closest_integer("-2.7") == -3

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 03:26:56.277037
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values exactly halfway are rounded away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("7.000") == 7

    # Values around the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 03:27:03.239540
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.2") == 14
    assert module_0.closest_integer("14.8") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.500") == 4
    assert module_0.closest_integer("-3.500") == -4
    assert module_0.closest_integer("7.000") == 7

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 03:27:09.358443
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:27:15.527747
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.2") == 14
    assert module_0.closest_integer("14.8") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.000") == 4

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0


test_closest_integer()

# Generated at 2026-10-25 03:27:22.272962
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.2") == 14
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("15.8") == 16

    assert module_0.closest_integer("-14.2") == -14
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("-15.8") == -16

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0

# Generated at 2026-10-25 03:27:31.169225
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:27:39.149335
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:27:41.700525
# Unit test for function closest_integer

# Generated at 2026-10-25 03:27:44.511664
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:27:51.636533
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:27:58.655229
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 03:28:08.877757
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 03:28:16.250975
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("14.4") == 14
    assert module_0.closest_integer("-14.4") == -14
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("123.999") == 124

# Generated at 2026-10-25 03:28:18.781302
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:21.196201
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:23.801401
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:26.215129
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:28.642131
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:31.056656
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:33.472102
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:35.884963
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:38.297547
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:40.713047
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:43.127900
# Unit test for function closest_integer

# Generated at 2026-10-25 03:28:45.732696
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:28:55.150916
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 03:29:03.842692
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:29:13.083575
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.8") == -16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-25 03:29:15.502219
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:17.917932
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:21.695606
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:30.131591
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:32.546686
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:34.961163
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:37.376111
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:39.791315
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:42.209937
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:44.624747
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:47.040274
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:49.455386
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:51.869505
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:54.286634
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:56.702333
# Unit test for function closest_integer

# Generated at 2026-10-25 03:29:59.120281
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:01.537339
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:03.950474
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:06.366371
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:08.783175
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:11.199253
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:13.614086
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:16.028595
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:18.444820
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:20.859404
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:23.275983
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:25.689557
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:28.104388
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:30.522951
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:32.935721
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:35.352056
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:37.766455
# Unit test for function closest_integer

# Generated at 2026-10-25 03:30:40.182834
# Unit test for function closest_integer