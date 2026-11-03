

# Generated at 2026-11-02 23:49:56.059912
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift right by 1
    assert module_0.circular_shift(12, 1) == "21"
    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    # Multi-digit shifts
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"
    assert module_0.circular_shift(1234, 4) == "1234"
    # Zero shift returns original
    assert module_0.circular_shift(123, 0) == "123"
    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"
    # Zero value
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(0, 10) == "0"
    # Negative number edge cases (sign treated as a character)
    assert module_0.circular_shift(-12, 1) == "2-1"
    assert module_0.circular_shift(-12, 5) == "21-"
    # Large numbers
    assert module_0.circular_shift(1000000, 3) == "0001000"
    print("All tests passed!")

test_circular_shift()

# Generated at 2026-11-02 23:50:53.617500
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift (shift < length of digits)
    assert module_0.circular_shift(12, 1) == "21"        # "12" shifted right by 1 -> "21"
    assert module_0.circular_shift(123, 2) == "231"      # "123" shifted right by 2 -> "231"
    assert module_0.circular_shift(1234, 2) == "3412"    # "1234" shifted right by 2 -> "3412"
    assert module_0.circular_shift(12345, 3) == "34512"  # "12345" shifted right by 3 -> "34512"

    # Shift equal to length -> original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift of zero -> original string
    assert module_0.circular_shift(123, 0) == "123"

    # Shift greater than length -> reversed string
    assert module_0.circular_shift(12, 5) == "21"
    assert module_0.circular_shift(123, 4) == "321"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 10) == "5"

    # Zero input
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(0, 3) == "0"

# Generated at 2026-11-02 23:51:49.093502
# Unit test for function circular_shift
def test_circular_shift():
    # Basic right circular shift
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(1234, 4) == "1234"  # shift equal to length -> unchanged

    # Shift by zero returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(100, 4) == "001"
    assert module_0.circular_shift(12345, 10) == "54321"

    # Single digit
    assert module_0.circular_shift(7, 1) == "7"

    # Shift of 1 on typical number
    assert module_0.circular_shift(9876, 1) == "6987"

    # Larger shift within length
    assert module_0.circular_shift(123456, 3) == "456123"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-02 23:52:30.479220
# Unit test for function circular_shift
def test_circular_shift():
    # Basic right circular shifts
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(100, 10) == "001"

    # Zero shift returns original string
    assert module_0.circular_shift(1234, 0) == "1234"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(7, 10) == "7"

    # Result is always a string
    assert isinstance(module_0.circular_shift(1234, 2), str)

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-02 23:53:46.224161
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift by 1
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(1234, 1) == "4123"

    # Shift by more than one position
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(1234, 2) == "3412"

    # Shift equal to length returns original string
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(12, 2) == "12"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(12, 5) == "21"
    assert module_0.circular_shift(1234, 10) == "4321"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Zero as input
    assert module_0.circular_shift(0, 1) == "0"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)
    assert isinstance(module_0.circular_shift(123, 10), str)

    print("All tests passed!")


test_circular_shift()