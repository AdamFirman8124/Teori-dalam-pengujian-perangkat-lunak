

# Generated at 2026-10-24 13:35:23.072822
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

# Generated at 2026-10-24 13:35:39.560774
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by 1 and 2
    assert module_0.circular_shift(12345, 1) == "51234"
    assert module_0.circular_shift(12345, 2) == "45123"

    # shift by 0 returns same digits

# Generated at 2026-10-24 13:35:41.977833
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:44.570630
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:46.984801
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:49.399197
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:51.813975
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:54.365984
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:56.784630
# Unit test for function circular_shift

# Generated at 2026-10-24 13:35:59.354540
# Unit test for function circular_shift

# Generated at 2026-10-24 13:36:01.771819
# Unit test for function circular_shift