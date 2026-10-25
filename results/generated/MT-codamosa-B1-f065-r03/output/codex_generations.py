

# Generated at 2026-10-24 21:05:19.226243
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 0) == "12345"

# Generated at 2026-10-24 21:05:34.183532
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift("abcdef", 2) == "efabcd"
    assert module_0.circular_shift("abcdef", 0) == "abcdef"
    assert module_0.circular_shift("abcdef", 6) == "abcdef"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift("abc", 4) == "cba"

# Generated at 2026-10-24 21:05:45.644973
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift("12345", 2) == "45123"
    assert module_0.circular_shift("12345", 0) == "12345"
    assert module_0.circular_shift("12345", 5) == "12345"
    assert module_0.circular_shift("12345", 6) == "54321"
    assert module_0.circular_shift(12345, 2) == "45123"

# Generated at 2026-10-24 21:06:02.111097
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

# Generated at 2026-10-24 21:06:04.637791
# Unit test for function circular_shift

# Generated at 2026-10-24 21:06:07.184561
# Unit test for function circular_shift

# Generated at 2026-10-24 21:06:09.601851
# Unit test for function circular_shift