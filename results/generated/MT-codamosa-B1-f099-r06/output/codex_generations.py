

# Generated at 2026-10-25 03:52:53.276386
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

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
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0
    assert module_0.closest_integer("0.51") == 1
    assert module_0.closest_integer("-0.51") == -1

# Generated at 2026-10-25 03:53:00.982609
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.4") == 14
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("14.6") == 15

    assert module_0.closest_integer("-14.4") == -14
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-14.6") == -15

    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0") == 0

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3

# Generated at 2026-10-25 03:53:09.044889
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("2.5000", 3),
        ("-2.5000", -3),
        ("2.49", 2),
        ("-2.49", -2),
        ("0.5", 1),
        ("-0.5", -1),
        ("0.0", 0),
        ("-0.0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 03:53:17.442966
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values near halfway
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 03:53:19.972832
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:22.388017
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:24.802215
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:27.217983
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:29.634431
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:32.049222
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:34.463848
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:37.290367
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:53:47.343311
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    # Values around the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:53:51.541772
# Unit test for function closest_integer

# Generated at 2026-10-25 03:53:54.408941
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:54:01.785287
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("7.49") == 7
    assert module_0.closest_integer("7.51") == 8

# Generated at 2026-10-25 03:54:08.647190
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("-2.0") == -2
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("7.5000") == 8
    assert module_0.closest_integer("-7.5000") == -8
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:54:16.115216
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

# Generated at 2026-10-25 03:54:18.760515
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:21.174986
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:23.590253
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:26.004960
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:28.419672
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:30.834418
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:33.250205
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:35.665027
# Unit test for function closest_integer

# Generated at 2026-10-25 03:54:38.248232
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:54:47.247462
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.8") == -16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros are ignored
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 03:54:54.618938
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("-15.3", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("1.5000", 2),
        ("-2.5000", -3),
        ("0.0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected

# Generated at 2026-10-25 03:55:02.909372
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
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:55:32.405715
# Unit test for function closest_integer
def test_closest_integer():
    # Integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 03:55:34.925617
# Unit test for function closest_integer

# Generated at 2026-10-25 03:55:37.339050
# Unit test for function closest_integer

# Generated at 2026-10-25 03:55:39.871854
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:55:47.157062
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
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 03:55:55.861300
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("2.49", 2),
        ("2.51", 3),
        ("-2.49", -2),
        ("-2.51", -3),
        ("0.5", 1),
        ("-0.5", -1),
        ("1.5000", 2),
        ("10.000", 10),
        ("0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 03:56:02.921306
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("10.4") == 10
    assert module_0.closest_integer("10.6") == 11

    # Values ending in .5 are rounded away from zero
    assert module_0.closest_integer("10.5") == 11
    assert module_0.closest_integer("-10.5") == -11
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    # Exact integers represented as decimals
    assert module_0.closest_integer("7.000") == 7
    assert module_0.closest_integer("-7.000") == -7

# Generated at 2026-10-25 03:56:11.523725
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
    assert module_0.closest_integer("-3.500") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:56:21.263072
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Additional edge cases
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:56:28.948830
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3

# Generated at 2026-10-25 03:56:31.555352
# Unit test for function closest_integer

# Generated at 2026-10-25 03:56:33.970959
# Unit test for function closest_integer

# Generated at 2026-10-25 03:56:36.388751
# Unit test for function closest_integer

# Generated at 2026-10-25 03:56:38.804589
# Unit test for function closest_integer

# Generated at 2026-10-25 03:56:41.606372
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 03:56:49.340370
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

    # Trailing zeros do not affect rounding
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 03:56:55.765741
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("1.500") == 2
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:57:04.666103
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

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-0.0") == 0

# Generated at 2026-10-25 03:57:12.613318
# Unit test for function closest_integer
def test_closest_integer():
    # Exact integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above .5
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
    assert module_0.closest_integer("5.000") == 5

# Generated at 2026-10-25 03:57:20.138953
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 03:57:30.566834
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

# Generated at 2026-10-25 03:57:39.673051
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

# Generated at 2026-10-25 03:57:50.442003
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
    assert module_0.closest_integer("7.000") == 7

    # Values close to zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 03:57:57.712815
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
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 03:58:06.312991
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
    assert module_0.closest_integer("7.000") == 7

    # Values around zero
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0

# Generated at 2026-10-25 03:58:15.326829
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.7") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.7") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("6.000") == 6

# Generated at 2026-10-25 03:58:23.721412
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:58:32.836920
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
    assert module_0.closest_integer("7.000") == 7

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 03:58:44.001139
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

# Generated at 2026-10-25 03:58:50.951613
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-0.5") == -1

# Generated at 2026-10-25 03:58:58.846125
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 03:59:05.091314
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 03:59:16.049032
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
    assert module_0.closest_integer("12.000") == 12

    # Other edge cases
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

# Generated at 2026-10-25 03:59:23.216109
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-14.4") == -14
    assert module_0.closest_integer("-14.6") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-25 03:59:33.472852
# Unit test for function closest_integer
def test_closest_integer():
    # Exact integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.7") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.7") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("8.000") == 8


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-25 03:59:39.293194
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
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 03:59:48.201571
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Exact halves round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4

    # Values on either side of a half
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Whole-number decimal strings
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("7.000") == 7
    assert module_0.closest_integer("-7.000") == -7

# Generated at 2026-10-25 03:59:56.188692
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 04:00:03.971505
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16

    # Values ending in .5 must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("5.000") == 5

    # Values close to zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 04:00:41.863702
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2

# Generated at 2026-10-25 04:00:44.280584
# Unit test for function closest_integer

# Generated at 2026-10-25 04:00:46.694208
# Unit test for function closest_integer

# Generated at 2026-10-25 04:00:49.111110
# Unit test for function closest_integer

# Generated at 2026-10-25 04:00:59.984949
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Zero and negative non-half values
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

# Generated at 2026-10-25 04:01:13.809950
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

# Generated at 2026-10-25 04:01:27.534575
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

    # Trailing zeros should not affect the result
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Values around rounding boundaries
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 04:01:30.066608
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:32.628162
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:35.186159
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:37.599728
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:40.015722
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:42.431953
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:44.845368
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:47.262087
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:49.678202
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:52.094692
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:54.511912
# Unit test for function closest_integer

# Generated at 2026-10-25 04:01:57.119327
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 04:02:07.573085
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Positive and negative non-tie values
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 04:02:17.246982
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 04:02:32.597918
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
    assert module_0.closest_integer("10.000") == 10

    # Values close to the halfway point
    assert module_0.closest_integer("1.4999") == 1
    assert module_0.closest_integer("-1.4999") == -1
    assert module_0.closest_integer("1.5001") == 2
    assert module_0.closest_integer("-1.5001") == -2

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 04:02:39.547186
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros should not affect rounding
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.000") == 4