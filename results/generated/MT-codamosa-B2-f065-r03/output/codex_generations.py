

# Generated at 2026-11-02 07:09:22.038185
# Unit test for function circular_shift
def test_circular_shift():
    # Shift by 1 moves last digit to front
    assert module_0.circular_shift(12, 1) == "21"
    # Shift equal to number of digits returns original
    assert module_0.circular_shift(12, 2) == "12"
    # Shift greater than number of digits reverses the digits
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 10) == "321"
    # Zero shift returns original
    assert module_0.circular_shift(1234, 0) == "1234"
    # Multi-digit shifts
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 4) == "23451"
    # Single digit number
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 100) == "5"

# Generated at 2026-11-02 07:10:55.630221
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shifts
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(125, 1) == "512"
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(12345, 2) == "45123"

    # Shift equal to string length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 5) == "21"
    assert module_0.circular_shift(123, 100) == "321"

    # Shift of zero returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 10) == "5"

    # Large numbers
    assert module_0.circular_shift(1000000, 3) == "000100"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-02 07:12:47.776131
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift (right shift by 1)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 1) == "51234"

    # Shift by more than one position
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 3) == "34512"

    # Shift equal to length returns the original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(12345, 5) == "12345"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 10) == "54321"
    assert module_0.circular_shift(100, 4) == "001"

    # Single digit numbers
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 5) == "7"

    # Shift by length - 1 moves first digit to the end
    assert module_0.circular_shift(1234, 3) == "2341"

# Generated at 2026-11-02 07:13:59.440974
# Unit test for function circular_shift
def test_circular_shift():
    # Shift smaller than number of digits: last `shift` digits rotate to front
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(12345, 3) == "34512"

    # Shift equal to number of digits: string unchanged
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than number of digits: digits reversed
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(125, 4) == "521"

    # Shift of zero: unchanged
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit cases
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"
    assert module_0.circular_shift(0, 1) == "0"

# Generated at 2026-11-02 07:14:37.226861
# Unit test for function circular_shift
def test_circular_shift():
    # Basic right circular shift within string length
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(123, 2) == "231"

    # Shift equal to length results in unchanged string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"
    assert module_0.circular_shift(12345, 5) == "12345"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(12345, 10) == "54321"

    # Zero shift leaves the string unchanged
    assert module_0.circular_shift(1234, 0) == "1234"

    # Single digit number
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Numbers containing zeros
    assert module_0.circular_shift(100, 1) == "010"
    assert module_0.circular_shift(100, 2) == "001"

    # Larger number
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(987654, 3) == "654987"