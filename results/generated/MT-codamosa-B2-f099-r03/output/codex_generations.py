

# Generated at 2026-10-25 01:43:52.414863
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Exact halves round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("12.5000") == 13
    assert module_0.closest_integer("-12.5000") == -13
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 01:43:54.831658
# Unit test for function closest_integer

# Generated at 2026-10-25 01:43:57.250073
# Unit test for function closest_integer

# Generated at 2026-10-25 01:43:59.662438
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:02.079127
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:04.493128
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:06.907251
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:09.438553
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:11.854326
# Unit test for function closest_integer

# Generated at 2026-10-25 01:44:14.736751
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:44:23.646332
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.6") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:44:32.353787
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("4.49") == 4
    assert module_0.closest_integer("4.51") == 5
    assert module_0.closest_integer("-4.49") == -4
    assert module_0.closest_integer("-4.51") == -5

    # Halfway values round away from zero
    assert module_0.closest_integer("4.5") == 5
    assert module_0.closest_integer("-4.5") == -5
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 01:44:39.732868
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("-14.50") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2

# Generated at 2026-10-25 01:44:45.559115
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.8") == 15

    # Exact halves round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("3.000") == 3

    # Values close to half
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-0.0") == 0

# Generated at 2026-10-25 01:44:56.721870
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Normal rounding
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
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 01:44:59.138921
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:01.553797
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:03.970586
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:06.385078
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:08.802690
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:11.220881
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:13.634313
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:16.049580
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:18.465331
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:20.879597
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:23.297169
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:25.709608
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:28.124897
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:30.542283
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:32.954964
# Unit test for function closest_integer

# Generated at 2026-10-25 01:45:42.289135
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
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 01:45:49.248812
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0


test_closest_integer()

# Generated at 2026-10-25 01:45:57.449503
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4


test_closest_integer()

# Generated at 2026-10-25 01:46:06.394997
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Standard rounding
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Half values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:46:08.931965
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:11.454302
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:13.873024
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:16.285906
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:18.701114
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:21.280641
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:23.696011
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:26.114619
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:28.530908
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:30.946101
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:33.361146
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:35.776466
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:38.194453
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:40.605019
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:43.020034
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:45.435290
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:47.851639
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:50.264682
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:52.700221
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:55.114780
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:57.530510
# Unit test for function closest_integer

# Generated at 2026-10-25 01:46:59.944412
# Unit test for function closest_integer

# Generated at 2026-10-25 01:47:02.359458
# Unit test for function closest_integer

# Generated at 2026-10-25 01:47:04.947150
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:47:13.222595
# Unit test for function closest_integer
def test_closest_integer():
    # Exact integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 01:47:20.807527
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
    assert module_0.closest_integer("3.0000") == 3

    # Values around the .5 boundary
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 01:47:29.292612
# Unit test for function closest_integer
def test_closest_integer():
    # Values exactly halfway between integers round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros should not affect halfway detection
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15

    # Regular rounding
    assert module_0.closest_integer("14.49") == 14
    assert module_0.closest_integer("14.51") == 15
    assert module_0.closest_integer("-14.49") == -14
    assert module_0.closest_integer("-14.51") == -15

    # Whole numbers and zero
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.000") == 0


test_closest_integer()

# Generated at 2026-10-25 01:47:36.916735
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("3.5") == 4
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 01:47:45.179114
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
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 01:47:52.452276
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


test_closest_integer()

# Generated at 2026-10-25 01:47:54.866408
# Unit test for function closest_integer

# Generated at 2026-10-25 01:47:57.283698
# Unit test for function closest_integer

# Generated at 2026-10-25 01:47:59.697109
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:02.293850
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:04.711749
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:07.125782
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:09.719787
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:12.722183
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:48:21.524078
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
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 01:48:28.896372
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
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:48:45.612431
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the midpoint
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Exact midpoint: round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 01:48:54.073557
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
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:48:56.633434
# Unit test for function closest_integer

# Generated at 2026-10-25 01:48:59.145260
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:01.663252
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:04.077075
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:06.491746
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:09.072142
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:11.486560
# Unit test for function closest_integer

# Generated at 2026-10-25 01:49:14.215167
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:49:24.499134
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4

# Generated at 2026-10-25 01:49:31.871642
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
    assert module_0.closest_integer("3.000") == 3

    print("All tests passed.")


test_closest_integer()

# Generated at 2026-10-25 01:49:38.399820
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
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("10.000") == 10
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:49:46.002705
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.49", 2),
        ("-2.49", -2),
        ("2.51", 3),
        ("-2.51", -3),
        ("3.5000", 4),
        ("-3.5000", -4),
        ("7.000", 7),
        ("0.0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 01:49:56.857016
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

# Generated at 2026-10-25 01:50:09.338896
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15

    # Halfway values must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0.0") == 0

    # Values immediately around a halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 01:50:11.755646
# Unit test for function closest_integer

# Generated at 2026-10-25 01:50:14.550602
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:50:28.498855
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

    # Values close to, but not equal to, .5
    assert module_0.closest_integer("1.4999") == 1
    assert module_0.closest_integer("1.5001") == 2

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:50:38.124577
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("14.5000") == 15

    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-14.5000") == -15

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("1.49") == 1
    assert module_0.closest_integer("1.51") == 2
    assert module_0.closest_integer("-1.49") == -1
    assert module_0.closest_integer("-1.51") == -2

# Generated at 2026-10-25 01:50:46.168183
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 01:50:53.503508
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
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("12.000") == 12

    # Values close to zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 01:51:01.164917
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:51:09.971448
# Unit test for function closest_integer
def test_closest_integer():
    # Integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Normal rounding
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.500") == 5
    assert module_0.closest_integer("-4.500") == -5
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 01:51:12.673127
# Unit test for function closest_integer

# Generated at 2026-10-25 01:51:15.089334
# Unit test for function closest_integer

# Generated at 2026-10-25 01:51:17.678787
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:51:27.393653
# Unit test for function closest_integer
def test_closest_integer():
    # Integers
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
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 01:51:36.475966
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 01:51:45.505093
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-14.2") == -14
    assert module_0.closest_integer("-14.8") == -15

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 01:51:57.792220
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above .5
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
    assert module_0.closest_integer("12.5000") == 13
    assert module_0.closest_integer("-12.5000") == -13
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 01:52:06.189168
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
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3

    # Other negative and boundary values
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 01:52:08.717841
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:11.285334
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:13.699475
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:16.112490
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:18.677626
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:21.092432
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:23.508493
# Unit test for function closest_integer

# Generated at 2026-10-25 01:52:26.094810
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 01:52:36.396506
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.49", 2),
        ("-2.49", -2),
        ("1.5000", 2),
        ("-1.5000", -2),
        ("0", 0),
        ("0.000", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) should return {expected}"
        )

# Generated at 2026-10-25 01:52:46.227396
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2

# Generated at 2026-10-25 01:52:55.341669
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 01:53:02.834820
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 01:53:11.210168
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.0") == 2

# Generated at 2026-10-25 01:53:13.627268
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:16.041742
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:18.456676
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:20.872329
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:23.285796
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:25.700981
# Unit test for function closest_integer

# Generated at 2026-10-25 01:53:34.253481
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("-7.4") == -7
    assert module_0.closest_integer("-7.6") == -8

# Generated at 2026-10-25 01:53:42.547511
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Exact halves round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    # Values near zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 01:53:51.252757
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("15.7", 16),
        ("14.5", 15),
        ("-14.5", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.5000", 3),
        ("-2.5000", -3),
        ("0.0", 0),
        ("3.49", 3),
        ("3.51", 4),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )