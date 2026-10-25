

# Generated at 2026-10-24 15:22:43.733783
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

# Generated at 2026-10-24 15:22:46.187524
# Unit test for function circular_shift

# Generated at 2026-10-24 15:22:48.599557
# Unit test for function circular_shift

# Generated at 2026-10-24 15:22:51.013781
# Unit test for function circular_shift

# Generated at 2026-10-24 15:22:53.427339
# Unit test for function circular_shift

# Generated at 2026-10-24 15:22:55.843947
# Unit test for function circular_shift

# Generated at 2026-10-24 15:22:58.255490
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:00.668464
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:03.081006
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:05.494529
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:07.908278
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:10.320717
# Unit test for function circular_shift

# Generated at 2026-10-24 15:23:12.733749
# Unit test for function circular_shift