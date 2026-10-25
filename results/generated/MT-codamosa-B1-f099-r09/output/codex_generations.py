

# Generated at 2026-10-24 04:23:46.191760
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:23:48.927349
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:23:51.540947
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:23:54.161957
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:14.630467
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:19.873083
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("3.5") == 4

# Generated at 2026-10-24 04:24:22.520595
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:25.191503
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:27.813356
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:30.422579
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:33.077508
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:35.710133
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:38.371229
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:40.985102
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:43.635539
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:24:46.130622
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:48.706435
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:51.111668
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:53.526511
# Unit test for function closest_integer

# Generated at 2026-10-24 04:24:55.942259
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:01.441537
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10.5") == 11

# Generated at 2026-10-24 04:25:04.124236
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:06.763290
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:09.385584
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:12.014983
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:14.624491
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:17.315206
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:19.947932
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:22.636351
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:25.286163
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:28.162587
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:30.775018
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:25:33.287870
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:35.706011
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:38.122360
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:40.537684
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:42.952350
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:45.367491
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:47.781377
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:50.418720
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:52.832502
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:55.255399
# Unit test for function closest_integer

# Generated at 2026-10-24 04:25:57.806133
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:00.222617
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:02.638847
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:05.054024
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:07.465257
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:09.880963
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:12.293933
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:17.013075
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10.5") == 11

# Generated at 2026-10-24 04:26:19.677688
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:22.418309
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:25.206457
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:28.665329
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:31.339165
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:34.011082
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:36.694178
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:26:39.404316
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:42.037653
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:44.665844
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:47.077976
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:49.498256
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:51.918267
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:54.334068
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:56.756473
# Unit test for function closest_integer

# Generated at 2026-10-24 04:26:59.163566
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:01.720995
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:04.163338
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:06.577829
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:08.998836
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:11.409024
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:13.832439
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:16.242812
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:18.658740
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:21.073842
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:25.468208
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:28.192362
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:30.827786
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:33.522568
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:36.146886
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:38.835511
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:41.470376
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:44.083951
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:46.706482
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:49.377488
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:27:54.679227
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:57.186491
# Unit test for function closest_integer

# Generated at 2026-10-24 04:27:59.607298
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:02.017503
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:04.433160
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:06.848310
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:09.256893
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:11.670199
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:14.082418
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:16.492699
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:18.904635
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:21.316155
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:23.727166
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:26.138641
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:28.551327
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:30.961980
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:33.385764
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:35.787767
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:38.199345
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:40.611057
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:43.022215
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:45.433633
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:47.866644
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:50.263835
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:52.676667
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:55.087522
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:57.500113
# Unit test for function closest_integer

# Generated at 2026-10-24 04:28:59.911387
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:02.324311
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:04.735558
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:13.312676
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:19.185563
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.500") == 3

# Generated at 2026-10-24 04:29:21.810224
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:24.421890
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:27.046128
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:29.683734
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:32.310712
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:34.928096
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:37.577556
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:40.226749
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:42.862216
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:29:53.259057
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:55.671162
# Unit test for function closest_integer

# Generated at 2026-10-24 04:29:58.082538
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:00.494149
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:02.914604
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:05.326945
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:07.905153
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:10.317129
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:12.729249
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:15.140520
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:17.552814
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:19.964407
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:22.375718
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:24.792404
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:27.198607
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:29.610922
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:32.020787
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:34.432041
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:36.843303
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:39.255509
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:41.666858
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:44.080017
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:46.490092
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:48.901838
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:51.314337
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:53.725749
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:56.137706
# Unit test for function closest_integer

# Generated at 2026-10-24 04:30:58.549260
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:00.960534
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:03.373335
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:16.657214
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:19.069046
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:21.479486
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:23.890913
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:26.303241
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:28.714446
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:31.126379
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:33.538240
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:35.950099
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:38.362559
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:40.775725
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:43.185592
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:45.597082
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:48.009741
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:50.420882
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:52.831458
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:55.243747
# Unit test for function closest_integer

# Generated at 2026-10-24 04:31:57.654612
# Unit test for function closest_integer

# Generated at 2026-10-24 04:32:00.066643
# Unit test for function closest_integer

# Generated at 2026-10-24 04:32:02.482200
# Unit test for function closest_integer

# Generated at 2026-10-24 04:32:05.049978
# Unit test for function closest_integer

# Generated at 2026-10-24 04:32:07.808712
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:10.452723
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:13.063326
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:51.295584
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:53.956848
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:56.582181
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:32:59.222931
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:01.943184
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:04.594596
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:07.234404
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:10.302978
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:12.960849
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-10-24 04:33:15.567493
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.7") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-14.7") == -15

    # .5 rounds away from zero
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("15.50") == 16
    assert module_0.closest_integer("-15.50") == -16
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("-2.50") == -3

    # Zero and small decimals
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()