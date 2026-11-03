

# Generated at 2026-11-02 10:23:28.299900
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular right shift
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

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Zero
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(0, 10) == "0"

    # Negative numbers (minus sign is part of the string)
    assert module_0.circular_shift(-12, 1) == "2-1"
    assert module_0.circular_shift(-12, 4) == "21-"

    print("All tests passed!")

# Generated at 2026-11-02 10:25:52.993317
# Unit test for function circular_shift
def test_circular_shift():
    # Shift smaller than number of digits: rotate right by shift
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to number of digits: returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than number of digits: returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(125, 4) == "521"
    assert module_0.circular_shift(1234, 10) == "4321"

    # Zero shift: returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(7, 2) == "7"

    # Negative numbers (string includes minus sign)
    assert module_0.circular_shift(-12, 1) == "21"
    assert module_0.circular_shift(-12, 3) == "21-"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-02 10:27:12.562843
# Unit test for function circular_shift
def test_circular_shift():
    # shift smaller than length: circular right rotation
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(100, 2) == "001"
    assert module_0.circular_shift(100, 3) == "100"
    assert module_0.circular_shift(0, 1) == "0"

    # shift greater than length: returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(123, 100) == "321"
    assert module_0.circular_shift(0, 2) == "0"

    print("All circular_shift tests passed!")


test_circular_shift()

# Generated at 2026-11-02 10:28:12.671045
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(12345, 2) == "45123"

    # Shift by 0 leaves number unchanged (as string)
    assert module_0.circular_shift(123, 0) == "123"

    # Shift equal to length leaves number unchanged
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 6) == "54321"
    assert module_0.circular_shift(12345, 100) == "54321"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 10) == "5"

    # Numbers containing zeros
    assert module_0.circular_shift(100, 1) == "010"
    assert module_0.circular_shift(100, 2) == "001"

    # Negative numbers (sign is treated as part of the string)
    assert module_0.circular_shift(-12, 1) == "2-1"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)

# Generated at 2026-11-02 10:29:38.028932
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 3) == "34512"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(987654, 6) == "987654"

    # Shift of zero returns original string
    assert module_0.circular_shift(123, 0) == "123"
    assert module_0.circular_shift(0, 0) == "0"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 5) == "21"
    assert module_0.circular_shift(123, 10) == "321"
    assert module_0.circular_shift(0, 1) == "0"

    # Single digit numbers
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 3) == "7"