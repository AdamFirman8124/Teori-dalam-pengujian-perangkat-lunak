

# Generated at 2026-11-02 15:19:26.454674
# Unit test for function circular_shift
def test_circular_shift():
    # Basic right circular shift
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(123, 2) == "231"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit number
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

# Generated at 2026-11-02 15:22:11.337828
# Unit test for function circular_shift
def test_circular_shift():
    # shift = 0 returns original string
    assert module_0.circular_shift(12345, 0) == "12345"

    # shift less than length: circular right shift
    assert module_0.circular_shift(12345, 1) == "51234"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 4) == "23451"

    # shift equal to length: returns original string
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift greater than length: returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 6) == "54321"
    assert module_0.circular_shift(100, 10) == "001"

    # single digit
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 5) == "7"

    # zero
    assert module_0.circular_shift(0, 1) == "0"

    # negative number (shift within length)
    assert module_0.circular_shift(-123, 2) == "23-1"

    # negative number (shift greater than length -> reversed)
    assert module_0.circular_shift(-12, 10) == "21-"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-02 15:25:04.121997
# Unit test for function circular_shift
def test_circular_shift():
    # Normal circular shift: shift less than length
    assert module_0.circular_shift(12, 1) == "21"          # last 1 digit moved to front
    assert module_0.circular_shift(1234, 2) == "3412"      # last 2 digits moved to front
    assert module_0.circular_shift(12345, 3) == "34512"

    # Shift equal to length: returns original string
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(0, 1) == "0"

    # Shift greater than length: returns reversed string
    assert module_0.circular_shift(12, 100) == "21"
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(0, 2) == "0"            # reversed single digit

    # Shift of zero: no shift, returns original
    assert module_0.circular_shift(12345, 0) == "12345"

    # Single-digit numbers
    assert module_0.circular_shift(7, 1) == "7"

    # Negative number: sign character participates in shift
    assert module_0.circular_shift(-12, 1) == "2-1"
    assert module_0.circular_shift(-123, 2) == "23-1"

    print("All tests passed!")

# Generated at 2026-11-02 15:27:13.583945
# Unit test for function circular_shift
def test_circular_shift():
# nonce:1981a1f7
    # Result is always a string
    assert isinstance(module_0.circular_shift(12, 1), str)

    # Basic circular right shifts
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to number of digits returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift of zero returns original string
    assert module_0.circular_shift(1234, 0) == "1234"

    # Shift greater than number of digits returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 5) == "321"
    assert module_0.circular_shift(100, 4) == "001"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()