

# Generated at 2026-10-25 02:36:18.772016
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.0") == 3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:36:26.957492
# Unit test for function closest_integer
def test_closest_integer():
    # Values below and above the midpoint
    assert module_0.closest_integer("10.2") == 10
    assert module_0.closest_integer("10.8") == 11
    assert module_0.closest_integer("-10.2") == -10
    assert module_0.closest_integer("-10.8") == -11

    # Exact halves round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Integers and trailing zeros
    assert module_0.closest_integer("5") == 5
    assert module_0.closest_integer("-5") == -5
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("123.000") == 123

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-0.0") == 0

# Generated at 2026-10-25 02:36:33.721958
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
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 02:36:42.601122
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-5.1") == -5

    # Halfway values round away from zero
    assert module_0.closest_integer("3.5") == 4
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Values below and above the halfway point
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Zeroes and trailing zeroes
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

# Generated at 2026-10-25 02:36:51.937863
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
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values near zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0

# Generated at 2026-10-25 02:36:58.502900
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 are rounded away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 02:37:06.081491
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("-2.0") == -2
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 02:37:13.657585
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

    # Trailing zeros
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:37:20.490953
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
    assert module_0.closest_integer("1.49") == 1
    assert module_0.closest_integer("-1.49") == -1
    assert module_0.closest_integer("1.51") == 2
    assert module_0.closest_integer("-1.51") == -2
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 02:37:29.180860
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
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
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 02:37:39.974667
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("14.5", 15),
        ("-14.5", -15),
        ("2.5", 3),
        ("-2.5", -3),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.49", 2),
        ("2.51", 3),
        ("3.5000", 4),
        ("-3.5000", -4),
        ("0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 02:37:42.534022
# Unit test for function closest_integer

# Generated at 2026-10-25 02:37:45.352838
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:37:53.389821
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

# Generated at 2026-10-25 02:38:01.990980
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
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:38:12.929278
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
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("8.0000") == 8

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 02:38:20.627439
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
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.0000") == 4

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 02:38:31.623130
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 02:38:38.548104
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
    assert module_0.closest_integer("12.5000") == 13
    assert module_0.closest_integer("-12.5000") == -13
    assert module_0.closest_integer("7.000") == 7

    # Other negative and zero values
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 02:38:46.740420
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("15.7", 16),
        ("14.5", 15),
        ("-14.5", -15),
        ("-8.4", -8),
        ("-8.6", -9),
        ("0.5", 1),
        ("-0.5", -1),
        ("0", 0),
        ("0.0", 0),
        ("23.000", 23),
        ("2.5000", 3),
        ("-2.5000", -3),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 02:38:57.124873
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
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("8.000") == 8

    # Other negative and zero values
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4
    assert module_0.closest_integer("0") == 0


test_closest_integer()

# Generated at 2026-10-25 02:39:04.249523
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

    # Values near zero
    assert module_0.closest_integer("0.2") == 0
    assert module_0.closest_integer("-0.2") == 0

# Generated at 2026-10-25 02:39:11.623213
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
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 02:39:19.406956
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

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 02:39:25.797323
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
    assert module_0.closest_integer("1.000") == 1
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:39:28.313129
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:30.728020
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:33.142917
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:35.602333
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:38.016693
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:40.433441
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:42.851838
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:45.261965
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:47.676279
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:50.091835
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:52.510363
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:54.924384
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:57.339490
# Unit test for function closest_integer

# Generated at 2026-10-25 02:39:59.754371
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:02.170186
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:04.583862
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:07.329904
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:40:47.059738
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

    # Negative values
    assert module_0.closest_integer("-14.4") == -14
    assert module_0.closest_integer("-14.6") == -15

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 02:40:49.630452
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:52.045977
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:54.460334
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:56.875966
# Unit test for function closest_integer

# Generated at 2026-10-25 02:40:59.291125
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:01.705876
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:04.120844
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:06.723842
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:41:15.934848
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Standard rounding
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.8") == -16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("2.0000") == 2

# Generated at 2026-10-25 02:41:24.851458
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
    assert module_0.closest_integer("7.49") == 7
    assert module_0.closest_integer("7.51") == 8
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:41:33.840797
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
        ("2.51", 3),
        ("-2.49", -2),
        ("-2.51", -3),
        ("3.5000", 4),
        ("-3.5000", -4),
        ("5.0", 5),
        ("0.000", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )

# Generated at 2026-10-25 02:41:42.265524
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
    assert module_0.closest_integer("10.000") == 10

    # Values close to zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 02:41:44.682383
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:47.095855
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:49.510433
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:51.924735
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:54.339781
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:56.754216
# Unit test for function closest_integer

# Generated at 2026-10-25 02:41:59.167383
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:01.581277
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:03.996578
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:06.410058
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:08.990383
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:42:18.522054
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
    assert module_0.closest_integer("0.0") == 0

    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3

# Generated at 2026-10-25 02:42:24.654664
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.4") == 14
    assert module_0.closest_integer("14.6") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("15.5000") == 16
    assert module_0.closest_integer("-15.5000") == -16
    assert module_0.closest_integer("10.000") == 10

    # Values close to zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 02:42:33.761451
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
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 02:42:43.286669
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
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-3.000") == -3

# Generated at 2026-10-25 02:42:45.925040
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:48.341635
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:50.757278
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:53.170580
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:55.585902
# Unit test for function closest_integer

# Generated at 2026-10-25 02:42:58.000629
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:00.414689
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:02.830400
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:05.245627
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:07.661299
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:10.075664
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:12.490110
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:14.907497
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:17.318713
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:19.733694
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:22.148665
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:24.563377
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:26.977781
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:29.390804
# Unit test for function closest_integer

# Generated at 2026-10-25 02:43:31.920466
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:43:42.192187
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.8") == -16

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("1.000") == 1

# Generated at 2026-10-25 02:43:50.304828
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-14.2") == -14
    assert module_0.closest_integer("-14.8") == -15

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16

    # Trailing zeros
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("2.000") == 2
    assert module_0.closest_integer("0.0") == 0


test_closest_integer()

# Generated at 2026-10-25 02:44:02.299860
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.0000") == 4
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 02:44:17.496087
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.3") == 2
    assert module_0.closest_integer("2.7") == 3
    assert module_0.closest_integer("-2.3") == -2
    assert module_0.closest_integer("-2.7") == -3

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 02:44:19.916637
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:22.330673
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:24.745548
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:27.162581
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:29.579307
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:31.996133
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:34.410125
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:36.823532
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:39.237860
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:41.652922
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:44.068218
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:46.482633
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:48.908346
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:51.334083
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:53.749214
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:56.164235
# Unit test for function closest_integer

# Generated at 2026-10-25 02:44:58.929919
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:45:07.875933
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.9") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Other negative values
    assert module_0.closest_integer("-2.1") == -2
    assert module_0.closest_integer("-2.9") == -3

# Generated at 2026-10-25 02:45:20.366495
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("3.0") == 3
    assert module_0.closest_integer("0") == 0


test_closest_integer()

# Generated at 2026-10-25 02:45:39.006512
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
    assert module_0.closest_integer("123.999") == 124

# Generated at 2026-10-25 02:45:47.912634
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.6") == -3
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 02:45:50.331678
# Unit test for function closest_integer

# Generated at 2026-10-25 02:45:52.749949
# Unit test for function closest_integer

# Generated at 2026-10-25 02:45:55.163131
# Unit test for function closest_integer

# Generated at 2026-10-25 02:45:57.688426
# Unit test for function closest_integer

# Generated at 2026-10-25 02:46:00.583894
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 02:46:10.645602
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("15.8", 16),
        ("14.5", 15),
        ("-14.5", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.5000", 3),
        ("-2.5000", -3),
        ("0.0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) should return {expected}"
        )

# Generated at 2026-10-25 02:46:21.093931
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
    assert module_0.closest_integer("0.000") == 0