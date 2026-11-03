

# Generated at 2026-11-01 20:28:12.035707
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift within length
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"  # full shift returns original
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length -> reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12345, 10) == "54321"

    # Single digit
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(7, 2) == "7"

    # Zero shift returns original
    assert module_0.circular_shift(100, 0) == "100"

    # Leading zero appears after shift
    assert module_0.circular_shift(100, 1) == "010"

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-01 20:28:27.293373
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift right by 1
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(1234, 1) == "4123"

    # Shift by 2
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(1234, 2) == "3412"

    # Shift equal to length returns original string
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(12, 2) == "12"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(12, 5) == "21"
    assert module_0.circular_shift(1000, 10) == "0001"

    # Shift of zero returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"  # shift > len -> reversed (same)

    # Zero input
    assert module_0.circular_shift(0, 1) == "0"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-01 20:28:51.767738
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts
    assert module_0.circular_shift(12, 1) == "21"        # shift right by 1
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(1234, 2) == "3412"    # shift right by 2
    assert module_0.circular_shift(123456, 3) == "456123"

    # Shift equal to length returns original string
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(12, 2) == "12"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(12, 100) == "21"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 10) == "5"         # reversed single digit

    # Zero as input
    assert module_0.circular_shift(0, 1) == "0"

    # Result type is string
    assert isinstance(module_0.circular_shift(123, 1), str)

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-01 20:29:14.802039
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift within bounds
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(100, 1) == "010"

    # Shift equal to length -> unchanged
    assert module_0.circular_shift(123, 3) == "123"

    # Zero shift -> unchanged
    assert module_0.circular_shift(456, 0) == "456"

    # Shift larger than length -> reversed string
    assert module_0.circular_shift(12345, 6) == "54321"
    assert module_0.circular_shift(120, 10) == "021"

    # Single-digit inputs
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 5) == "7"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)

    # String representation handles negative sign as part of digits
    assert module_0.circular_shift(-12, 1) == "2-1"

# Generated at 2026-11-01 20:29:46.491022
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts (right rotation)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(7, 10) == "7"

    # Edge cases
    assert module_0.circular_shift(0, 1) == "0"          # single digit, shift == len
    assert module_0.circular_shift(123, 0) == "123"      # zero shift
    assert module_0.circular_shift(100, 1) == "010"      # preserves leading zeros in rotation

    print("All tests passed!")


test_circular_shift()