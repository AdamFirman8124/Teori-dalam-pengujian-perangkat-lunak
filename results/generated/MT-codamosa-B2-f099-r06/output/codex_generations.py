

# Generated at 2026-10-25 00:38:13.404649
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
    assert module_0.closest_integer("0.0") == 0


test_closest_integer()
print("All tests passed.")

# Generated at 2026-10-25 00:38:22.182938
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

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 00:38:32.535914
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

    # Values close to zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 00:38:40.238969
# Unit test for function closest_integer
def test_closest_integer():
    # Integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above the halfway point
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("3.5") == 4
    assert module_0.closest_integer("-3.5") == -4
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 00:38:49.111345
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("1.5") == 2
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-1.5") == -2
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("7.000") == 7

    # Ordinary rounding
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

# Generated at 2026-10-25 00:38:55.614455
# Unit test for function closest_integer
def test_closest_integer():
    # Exact integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Regular rounding
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("6.000") == 6

# Generated at 2026-10-25 00:39:02.632123
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.49") == 14
    assert module_0.closest_integer("14.51") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("5.000") == 5

    # Values close to zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 00:39:10.789132
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:39:18.709895
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

    # Other negative and zero values
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4
    assert module_0.closest_integer("0") == 0


test_closest_integer()

# Generated at 2026-10-25 00:39:25.783191
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

    # Values near zero and negative values
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0
    assert module_0.closest_integer("-1.49") == -1
    assert module_0.closest_integer("-1.51") == -2

# Generated at 2026-10-25 00:39:35.397764
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros should not affect the result
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:39:44.305744
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
    assert module_0.closest_integer("0.000") == 0

    # Values close to, but not exactly, halfway
    assert module_0.closest_integer("1.49") == 1
    assert module_0.closest_integer("1.51") == 2
    assert module_0.closest_integer("-1.49") == -1
    assert module_0.closest_integer("-1.51") == -2

# Generated at 2026-10-25 00:39:52.382091
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("100") == 100

# Generated at 2026-10-25 00:40:02.534012
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("14.5", 15),
        ("14.4", 14),
        ("14.6", 15),
        ("-15.5", -16),
        ("-15.4", -15),
        ("-15.6", -16),
        ("0", 0),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.5000", 3),
        ("-2.5000", -3),
        ("3.000", 3),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected

# Generated at 2026-10-25 00:40:10.116263
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-25 00:40:19.153253
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
    assert module_0.closest_integer("-0.0") == 0

# Generated at 2026-10-25 00:40:29.454042
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
    assert module_0.closest_integer("3.0000") == 3

# Generated at 2026-10-25 00:40:36.370076
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
        ("2.49", 2),
        ("-2.49", -2),
        ("3.5000", 4),
        ("-3.5000", -4),
        ("1.000", 1),
        ("0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) returned "
            f"{module_0.closest_integer(value)}, expected {expected}"
        )


test_closest_integer()

# Generated at 2026-10-25 00:40:45.222847
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3

    # Halfway values round away from zero
    assert module_0.closest_integer("3.5") == 4
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Negative values
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2
    assert module_0.closest_integer("42.000") == 42
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 00:40:52.087621
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:41:00.491837
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

    # Values near halfway
    assert module_0.closest_integer("2.4999") == 2
    assert module_0.closest_integer("2.5001") == 3
    assert module_0.closest_integer("-2.4999") == -2
    assert module_0.closest_integer("-2.5001") == -3

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:41:08.377155
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

    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("5.000") == 5

# Generated at 2026-10-25 00:41:18.312019
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
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 00:41:26.219578
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("1.50") == 2
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("0.000") == 0
    assert module_0.closest_integer("123.000") == 123

# Generated at 2026-10-25 00:41:35.410223
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
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3

# Generated at 2026-10-25 00:41:43.296354
# Unit test for function closest_integer
def test_closest_integer():
    # Values below and above the halfway point
    assert module_0.closest_integer("10.4") == 10
    assert module_0.closest_integer("10.6") == 11
    assert module_0.closest_integer("-10.4") == -10
    assert module_0.closest_integer("-10.6") == -11

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("10.000") == 10

    # Exact integers
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("42") == 42
    assert module_0.closest_integer("-42") == -42

# Generated at 2026-10-25 00:41:54.558853
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
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 00:42:02.751416
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
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("-7.2") == -7

# Generated at 2026-10-25 00:42:12.378337
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("14.4") == 14
    assert module_0.closest_integer("-14.4") == -14
    assert module_0.closest_integer("14.6") == 15
    assert module_0.closest_integer("-14.6") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:42:20.875988
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    # Ordinary rounding
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

    # Integers and trailing zeros
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:42:29.797036
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
    assert module_0.closest_integer("3.50") == 4
    assert module_0.closest_integer("-3.500") == -4

    # Other negative values
    assert module_0.closest_integer("-2.1") == -2
    assert module_0.closest_integer("-2.9") == -3

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:42:38.581494
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15

    # Exact halves are rounded away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    # Values on either side of a half
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:42:50.162361
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.6") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:42:57.009388
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
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:43:05.317708
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.7") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.7") == -4

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 00:43:12.792911
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:43:20.677613
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

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

# Generated at 2026-10-25 00:43:30.469964
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

    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:43:36.935210
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-7") == -7
    assert module_0.closest_integer("0") == 0

    # Values below and above .5
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("6.000") == 6

# Generated at 2026-10-25 00:43:45.752960
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.51") == -4
    assert module_0.closest_integer("5.5000") == 6
    assert module_0.closest_integer("-5.5000") == -6
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:43:53.724270
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

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-25 00:44:01.228495
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
    assert module_0.closest_integer("0.8") == 1
    assert module_0.closest_integer("-0.8") == -1


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-25 00:44:08.601212
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("5.2") == 5
    assert module_0.closest_integer("5.8") == 6
    assert module_0.closest_integer("-5.2") == -5
    assert module_0.closest_integer("-5.8") == -6

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:44:16.793799
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
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.51") == -3
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 00:44:25.293001
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.8") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.8") == -16

    # Halfway values must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 00:44:35.124792
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.2") == 14
    assert module_0.closest_integer("14.8") == 15
    assert module_0.closest_integer("-14.2") == -14
    assert module_0.closest_integer("-14.8") == -15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.000") == 3
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:44:42.496382
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
    assert module_0.closest_integer("8.000") == 8

    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:44:51.201345
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("1.5000") == 2
    assert module_0.closest_integer("-1.5000") == -2

    # Values on either side of the halfway point
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Zero and trailing zeros
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("5.000") == 5

# Generated at 2026-10-25 00:44:59.800766
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:45:07.466888
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

    # Other negative values
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("8.000") == 8

    # Zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:45:09.996017
# Unit test for function closest_integer

# Generated at 2026-10-25 00:45:12.408388
# Unit test for function closest_integer

# Generated at 2026-10-25 00:45:44.387927
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 00:45:55.294163
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("14.5", 15),
        ("-15.5", -16),
        ("0.5", 1),
        ("-0.5", -1),
        ("2.49", 2),
        ("2.51", 3),
        ("-2.49", -2),
        ("-2.51", -3),
        ("3.000", 3),
        ("1.5000", 2),
        ("-1.5000", -2),
        ("0.000", 0),
    ]

    for value, expected in test_cases:
        actual = module_0.closest_integer(value)
        assert actual == expected, (
            f"module_0.closest_integer({value!r}) returned {actual}; "
            f"expected {expected}"
        )

# Generated at 2026-10-25 00:46:03.586532
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("14.49") == 14
    assert module_0.closest_integer("14.51") == 15
    assert module_0.closest_integer("-14.49") == -14
    assert module_0.closest_integer("-14.51") == -15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 00:46:11.568857
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("123.49") == 123
    assert module_0.closest_integer("123.51") == 124

# Generated at 2026-10-25 00:46:13.986128
# Unit test for function closest_integer

# Generated at 2026-10-25 00:46:16.523003
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 00:46:25.830305
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Values ending in .5 are rounded away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-25 00:46:31.346596
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values near zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0


test_closest_integer()

# Generated at 2026-10-25 00:46:38.313323
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

# Generated at 2026-10-25 00:46:46.913498
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Halfway values round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    # Non-halfway values round to the nearest integer
    assert module_0.closest_integer("1.4") == 1
    assert module_0.closest_integer("1.6") == 2
    assert module_0.closest_integer("-1.4") == -1
    assert module_0.closest_integer("-1.6") == -2

    # Whole numbers with decimal notation
    assert module_0.closest_integer("3.0") == 3
    assert module_0.closest_integer("-7.000") == -7

# Generated at 2026-10-25 00:46:54.695789
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
    assert module_0.closest_integer("8.000") == 8

# Generated at 2026-10-25 00:46:57.113291
# Unit test for function closest_integer

# Generated at 2026-10-25 00:46:59.528085
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:01.943948
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:04.357482
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:06.772289
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:09.186546
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:11.612071
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:14.026598
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:16.440723
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:18.855804
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:21.283925
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:23.709880
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:26.137332
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:28.552182
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:30.966352
# Unit test for function closest_integer

# Generated at 2026-10-25 00:47:45.298888
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
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("2.000") == 2

    # Other negative and zero values
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-25 00:47:53.067006
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.0000") == 3

# Generated at 2026-10-25 00:48:00.592356
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5") == 4
    assert module_0.closest_integer("-3.5") == -4

    # Trailing zeros
    assert module_0.closest_integer("4.5000") == 5
    assert module_0.closest_integer("-4.5000") == -5
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-25 00:48:03.139274
# Unit test for function closest_integer

# Generated at 2026-10-25 00:48:05.557866
# Unit test for function closest_integer

# Generated at 2026-10-25 00:48:07.972604
# Unit test for function closest_integer