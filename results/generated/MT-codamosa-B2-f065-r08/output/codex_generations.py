

# Generated at 2026-11-03 04:40:55.941206
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift by one position
    assert module_0.circular_shift(12, 1) == "21"
    # Shift equal to length returns the original string
    assert module_0.circular_shift(12, 2) == "12"
    # Shift greater than length returns the reversed string
    assert module_0.circular_shift(12, 5) == "21"
    # Zero shift returns the original string
    assert module_0.circular_shift(12, 0) == "12"
    # Multi-digit shifts
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"
    assert module_0.circular_shift(1234, 4) == "1234"
    assert module_0.circular_shift(1234, 10) == "4321"
    # Single digit numbers
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 3) == "7"
    # Negative shift falls into else branch (shift not > len)
    assert module_0.circular_shift(12, -1) == "12"
    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-03 04:42:51.405414
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift: shift last digit to front
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 1) == "51234"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(100, 3) == "100"
    assert module_0.circular_shift(0, 1) == "0"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(100, 4) == "001"
    assert module_0.circular_shift(97, 8) == "79"

    # Zero shift returns original string
    assert module_0.circular_shift(1234, 0) == "1234"

    # Negative integer input
    assert module_0.circular_shift(-12, 1) == "2-1"

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-03 04:47:16.342040
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts (shift right by given positions)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than number of digits -> reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(100, 4) == "001"

    # Edge cases
    assert module_0.circular_shift(0, 1) == "0"       # shift == len(s), full rotation
    assert module_0.circular_shift(0, 2) == "0"       # shift > len(s), reversed
    assert module_0.circular_shift(7, 0) == "7"       # zero shift
    assert module_0.circular_shift(10, 1) == "01"     # leading zero after shift
    assert module_0.circular_shift(1000000, 2) == "001000"  # leading zeros preserved