

# Generated at 2026-10-25 00:19:30.598740
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by 1 and 2
    assert module_0.circular_shift(12345, 1) == "51234"
    assert module_0.circular_shift(12345, 2) == "45123"

    # shift by 0 returns same digits

# Generated at 2026-10-25 00:19:46.996396
# Unit test for function circular_shift
def test_circular_shift():
    # basic right rotation
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"

    # shift by full length -> unchanged
    assert module_0.circular_shift(1234, 4) == "1234"

    # shift of 0 -> unchanged
    assert module_0.circular_shift(1234, 0) == "1234"

    # shift larger than digit count -> reversed digits
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12, 100) == "21"

    # single digit
    assert module_0.circular_shift(7, 1) == "7"

    # negative number keeps the sign in place
    assert module_0.circular_shift(-123, 1) == "-312"

    print("All tests passed.")


test_circular_shift()

# Generated at 2026-10-25 00:20:09.369641
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12345, 6) == "54321"
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 2) == "7"

# Generated at 2026-10-25 00:20:25.767234
# Unit test for function circular_shift
def test_circular_shift():
    # basic right rotation
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"

    # shift by full length -> unchanged
    assert module_0.circular_shift(1234, 4) == "1234"

    # shift of 0 -> unchanged
    assert module_0.circular_shift(1234, 0) == "1234"

    # shift larger than digit count -> reversed digits
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12, 100) == "21"

    # single digit
    assert module_0.circular_shift(7, 1) == "7"

    # negative number keeps the sign in place
    assert module_0.circular_shift(-123, 1) == "-312"

    print("All tests passed.")


test_circular_shift()

# Generated at 2026-10-25 00:20:42.334571
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by 1 and 2
    assert module_0.circular_shift(12345, 1) == "51234"
    assert module_0.circular_shift(12345, 2) == "45123"

    # shift by 0 returns same digits