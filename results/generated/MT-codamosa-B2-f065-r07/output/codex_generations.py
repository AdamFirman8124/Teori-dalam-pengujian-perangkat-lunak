

# Generated at 2026-11-02 00:44:14.226842
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift by 1
    assert module_0.circular_shift(12, 1) == "21"
    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    # Multi-digit shift
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 3) == "34512"
    # Shift equal to length (no change)
    assert module_0.circular_shift(12345, 5) == "12345"
    # Shift exceeding length (reversed)
    assert module_0.circular_shift(12345, 6) == "54321"
    # Zero shift returns original
    assert module_0.circular_shift(12345, 0) == "12345"
    # Single digit
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 5) == "7"
    # Digits with zeros
    assert module_0.circular_shift(100, 2) == "001"
    assert module_0.circular_shift(100, 1) == "010"
    # Shift by 0 on single digit
    assert module_0.circular_shift(0, 1) == "0"
    # Large shift far beyond length
    assert module_0.circular_shift(12, 100) == "21"
    print("All tests passed!")

if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-02 00:45:38.952282
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift (shift < length)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(97, 8) == "79"
    assert module_0.circular_shift(11, 101) == "11"
    assert module_0.circular_shift(12345, 6) == "54321"

    # Leading zeros preserved as string
    assert module_0.circular_shift(100, 2) == "001"

    # Zero shift returns original string
    assert module_0.circular_shift(1234, 0) == "1234"

    # Single digit cases
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 5) == "7"

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-02 00:47:11.648431
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift: last `shift` characters move to the front
    assert module_0.circular_shift(12345, 1) == "51234"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 3) == "34512"
    assert module_0.circular_shift(12345, 4) == "23451"

    # Shift equal to the number of digits returns the original string
    assert module_0.circular_shift(12345, 5) == "12345"

    # Shift of zero returns the original string
    assert module_0.circular_shift(12345, 0) == "12345"

    # Shift greater than number of digits returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(1000, 5) == "0001"

    # Single digit inputs
    assert module_0.circular_shift(7, 0) == "7"
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 2) == "7"  # reversed single digit is itself

    # Two digit inputs
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"

    # Inputs containing zeros
    assert module_0.circular_shift(105, 1) == "510"
    assert module_0.circular_shift(100, 1) == "010"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)
    assert isinstance(module_0.circular_shift(123, 10), str)

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-02 00:48:16.710804
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift (shift < length)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(100, 3) == "100"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 4) == "321"
    assert module_0.circular_shift(100, 5) == "001"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(7, 2) == "7"

    # Result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)
    assert isinstance(module_0.circular_shift(123, 10), str)

    print("All tests passed!")


if __name__ == "__main__":
    test_circular_shift()

# Generated at 2026-11-02 00:49:42.439757
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift by 1
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"

    # Shift by more than one position
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to length returns original string
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length reverses the string
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(100, 4) == "001"

    # Zero shift returns original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 10) == "7"
    assert module_0.circular_shift(0, 1) == "0"

    # Larger numbers
    assert module_0.circular_shift(987654, 2) == "549876"
    assert module_0.circular_shift(987654, 7) == "456789"

    print("All tests passed!")


test_circular_shift()