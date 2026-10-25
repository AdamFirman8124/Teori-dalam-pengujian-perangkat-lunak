

# Generated at 2026-10-24 07:48:31.906941
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Standard rounding
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Half values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-24 07:48:34.326083
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:36.734166
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:39.149405
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:41.565740
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:43.979392
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:46.393628
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:48.806380
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:51.218704
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:53.632793
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:56.046779
# Unit test for function closest_integer

# Generated at 2026-10-24 07:48:58.459873
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:00.884713
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:03.289678
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:08.765415
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-24 07:49:22.166455
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
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-24 07:49:24.584757
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:26.997883
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:29.414395
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:31.830118
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:34.244161
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:36.657400
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:39.084221
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:41.502552
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:43.918775
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:46.328944
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:48.742626
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:51.154979
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:53.571707
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:55.984574
# Unit test for function closest_integer

# Generated at 2026-10-24 07:49:58.398837
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:00.813565
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:03.229004
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:05.642823
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:08.058814
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:10.472577
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:12.894132
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:15.306818
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:17.720395
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:20.134804
# Unit test for function closest_integer

# Generated at 2026-10-24 07:50:31.506374
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
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("3.000") == 3

    # Values near zero
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0

# Generated at 2026-10-24 07:50:42.154331
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Values below and above .5
    assert module_0.closest_integer("3.4") == 3
    assert module_0.closest_integer("3.6") == 4
    assert module_0.closest_integer("-3.4") == -3
    assert module_0.closest_integer("-3.6") == -4

    # Exact halves round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-24 07:50:53.624778
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

    # Halfway values must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

# Generated at 2026-10-24 07:51:02.020219
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("8.000") == 8

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0

# Generated at 2026-10-24 07:51:04.539546
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:06.956932
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:09.371539
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:11.783761
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:14.199519
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:16.613216
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:19.026376
# Unit test for function closest_integer

# Generated at 2026-10-24 07:51:26.904294
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("4.4") == 4

# Generated at 2026-10-24 07:51:37.554444
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

# Generated at 2026-10-24 07:51:44.925844
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

# Generated at 2026-10-24 07:51:52.402776
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("4.000") == 4


test_closest_integer()

# Generated at 2026-10-24 07:52:01.158143
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
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
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("10.000") == 10

# Generated at 2026-10-24 07:52:03.675271
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:06.092104
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:08.503489
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:10.914751
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:13.333362
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:15.956164
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:18.367532
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:20.782633
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:23.199189
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:25.613962
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:28.029616
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:30.445710
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:32.859087
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:35.273239
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:37.688393
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:40.103197
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:42.521588
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:44.934889
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:47.349528
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:49.769085
# Unit test for function closest_integer

# Generated at 2026-10-24 07:52:57.118970
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10") == 10

# Generated at 2026-10-24 07:53:06.437156
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

# Generated at 2026-10-24 07:53:15.477974
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0

    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    # Trailing zeros should not affect half-value detection.
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

# Generated at 2026-10-24 07:53:31.628476
# Unit test for function closest_integer
def test_closest_integer():
    test_cases = [
        ("10", 10),
        ("15.3", 15),
        ("15.7", 16),
        ("14.5", 15),
        ("14.5000", 15),
        ("-15.3", -15),
        ("-15.7", -16),
        ("-14.5", -15),
        ("-14.5000", -15),
        ("0.5", 1),
        ("-0.5", -1),
        ("0.000", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) should return "
            f"{expected}, but returned {module_0.closest_integer(value)}"
        )

# Generated at 2026-10-24 07:53:34.045490
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:36.460565
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:38.875476
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:41.379409
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:43.791579
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:46.206036
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:48.757740
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:51.170872
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:53.585066
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:55.998322
# Unit test for function closest_integer

# Generated at 2026-10-24 07:53:58.411517
# Unit test for function closest_integer

# Generated at 2026-10-24 07:54:00.828259
# Unit test for function closest_integer

# Generated at 2026-10-24 07:54:03.240604
# Unit test for function closest_integer

# Generated at 2026-10-24 07:54:08.118834
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("3.5") == 4

# Generated at 2026-10-24 07:54:22.640218
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
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
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-24 07:54:31.330620
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("0.0") == 0

# Generated at 2026-10-24 07:54:41.440810
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

    # Boundary values
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-24 07:54:51.164720
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
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
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

# Generated at 2026-10-24 07:55:03.054189
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10") == 10

# Generated at 2026-10-24 07:55:11.405375
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("3.2") == 3
    assert module_0.closest_integer("3.8") == 4
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are ignored
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

# Generated at 2026-10-24 07:55:21.881978
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
        ("1.000", 1),
        ("0", 0),
    ]

    for value, expected in test_cases:
        assert module_0.closest_integer(value) == expected, (
            f"module_0.closest_integer({value!r}) should return {expected}"
        )

# Generated at 2026-10-24 07:55:30.411096
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

# Generated at 2026-10-24 07:55:32.927676
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:35.541724
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:37.957550
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:40.375691
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:42.793891
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:45.212133
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:47.638660
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:50.048608
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:52.463989
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:54.882797
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:57.443232
# Unit test for function closest_integer

# Generated at 2026-10-24 07:55:59.858085
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:02.276402
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:04.691303
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:07.105857
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:09.520015
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:11.939816
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:14.359245
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:20.892754
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:23.304264
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:25.719303
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:28.137002
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:30.554919
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:32.974211
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:35.397014
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:37.809398
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:40.223864
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:42.641721
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:45.058835
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:47.471103
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:49.888235
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:52.306578
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:54.723911
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:57.140941
# Unit test for function closest_integer

# Generated at 2026-10-24 07:56:59.553628
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:01.968294
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:04.383727
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:06.800025
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:09.220525
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:11.636522
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:14.052246
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:16.473690
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:18.886667
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:21.305346
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:23.718538
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:26.131659
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:28.545907
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:30.962881
# Unit test for function closest_integer

# Generated at 2026-10-24 07:57:48.336117
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3

    assert module_0.closest_integer("3.49") == 3
    assert module_0.closest_integer("3.51") == 4
    assert module_0.closest_integer("-3.49") == -3
    assert module_0.closest_integer("-3.51") == -4

# Generated at 2026-10-24 07:57:57.468296
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
    assert module_0.closest_integer("12.5000") == 13
    assert module_0.closest_integer("-12.5000") == -13
    assert module_0.closest_integer("8.000") == 8

    # Values near zero
    assert module_0.closest_integer("0.1") == 0
    assert module_0.closest_integer("-0.1") == 0


test_closest_integer()

# Generated at 2026-10-24 07:58:06.883573
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
    assert module_0.closest_integer("3.5000") == 4
    assert module_0.closest_integer("-3.5000") == -4
    assert module_0.closest_integer("7.000") == 7


test_closest_integer()

# Generated at 2026-10-24 07:58:15.499691
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
    assert module_0.closest_integer("0") == 0


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")

# Generated at 2026-10-24 07:58:25.822813
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("4.000") == 4

    # Values around zero
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.49") == 0
    assert module_0.closest_integer("-0.49") == 0