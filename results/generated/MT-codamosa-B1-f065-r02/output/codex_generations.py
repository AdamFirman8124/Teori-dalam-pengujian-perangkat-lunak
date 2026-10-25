

# Generated at 2026-10-24 19:38:42.202053
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

# Generated at 2026-10-24 19:38:56.562048
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift("12345", 2) == "45123"
    assert module_0.circular_shift("12345", 0) == "12345"
    assert module_0.circular_shift("12345", 5) == "12345"
    assert module_0.circular_shift("12345", 6) == "54321"
    assert module_0.circular_shift(12345, 2) == "45123"

# Generated at 2026-10-24 19:38:59.079522
# Unit test for function circular_shift

# Generated at 2026-10-24 19:39:01.496168
# Unit test for function circular_shift

# Generated at 2026-10-24 19:39:03.916433
# Unit test for function circular_shift

# Generated at 2026-10-24 19:39:06.436316
# Unit test for function circular_shift

# Generated at 2026-10-24 19:39:08.853494
# Unit test for function circular_shift

# Generated at 2026-10-24 19:39:13.739201
# Unit test for function circular_shift
def test_circular_shift():assert module_0.circular_shift(12345, 2) == "45123"

# Generated at 2026-10-24 19:39:30.125793
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