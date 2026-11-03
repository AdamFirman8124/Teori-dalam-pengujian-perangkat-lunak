

# Generated at 2026-11-02 22:08:42.768257
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift by one position
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"

    # Shift by multiple positions
    assert module_0.circular_shift(123, 2) == "231"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(4567, 4) == "4567"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 4) == "321"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Numbers containing zeros
    assert module_0.circular_shift(100, 2) == "001"
    assert module_0.circular_shift(1000, 1) == "0100"

# Generated at 2026-11-02 22:11:21.795863
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts
    assert module_0.circular_shift(12, 1) == "21"       # shift right by 1
    assert module_0.circular_shift(12, 2) == "12"       # shift equals length -> unchanged
    assert module_0.circular_shift(12345, 2) == "45123" # last 2 digits move to front
    assert module_0.circular_shift(12345, 3) == "34512"

    # Shift of 0 returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Shift greater than length -> reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(100, 4) == "001"

    # Single digit
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 2) == "7"         # reversed single digit is same

    # Zero
    assert module_0.circular_shift(0, 1) == "0"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)

    print("All circular_shift tests passed!")


def test_circular_shift_edge_cases():
    # Negative shift falls into else branch: s[len-shift:] is empty,
    # s[:len-shift] covers whole string -> original returned
    assert module_0.circular_shift(123, -1) == "123"

    # Large numbers
    assert module_0.circular_shift(987654321, 4) == "432198765"
    assert module_0.circular_shift(987654321, 9) == "987654321"
    assert module_0.circular_shift(987654321, 10) == "123456789"

    # Leading zeros after reversal
    assert module_0.circular_shift(1200, 5) == "0021"

    print("All edge case tests passed!")


if __name__ == "__main__":
    test_circular_shift()
    test_circular_shift_edge_cases()

# Generated at 2026-11-02 22:13:36.555117
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular right shift
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 2) == "001"

    # Shift equal to string length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than string length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 10) == "54321"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit number
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Negative number (minus sign is part of the string)
    assert module_0.circular_shift(-12, 1) == "2-1"
    assert module_0.circular_shift(-12, 4) == "21-"

    # Leading zeros after shift are preserved in string result
    assert module_0.circular_shift(1050, 1) == "0105"