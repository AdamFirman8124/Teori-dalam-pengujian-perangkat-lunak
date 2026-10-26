

# Generated at 2026-10-25 06:20:55.213436
# Unit test for function x_or_y

# Generated at 2026-10-25 06:20:57.631129
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:00.231354
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:02.671411
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:05.084439
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:07.497340
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:09.935089
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:12.350952
# Unit test for function x_or_y

# Generated at 2026-10-25 06:21:19.155411
# Unit test for function x_or_y
def test_x_or_y():assert module_0.x_or_y(1, "x", "y") == "y"

# Generated at 2026-10-25 06:21:25.707912
# Unit test for function x_or_y
def test_x_or_y():
    # n is prime -> returns x
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(13, 1, 0) == 1

    # n is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(100, 1, 0) == 0

    # edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    assert module_0.x_or_y(0, "prime", "not") == "prime"  # loop skipped, falls to else
    assert module_0.x_or_y(-5, "prime", "not") == "prime"  # negative: loop skipped

    print("All tests passed.")

test_x_or_y()

# Generated at 2026-10-25 06:21:27.147397
# Unit test for function x_or_y
def test_x_or_y():
    # n is prime -> returns x
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(13, 1, 0) == 1

    # n is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(100, 1, 0) == 0

    # edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    assert module_0.x_or_y(0, "prime", "not") == "prime"  # loop skipped, falls to else
    assert module_0.x_or_y(-5, "prime", "not") == "prime"  # negative: loop skipped

    print("All tests passed.")

test_x_or_y()