

# Generated at 2026-11-02 12:20:51.661603
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == '0'
    assert module_0.string_sequence(1) == '0 1'
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert module_0.string_sequence(50) == ' '.join(str(x) for x in range(51))
    # Edge case: negative input yields empty string
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(-100) == ''

# Generated at 2026-11-02 12:21:34.941473
# Unit test for function string_sequence
def test_string_sequence():
    # Edge case: n = 0 should return just "0"
    assert module_0.string_sequence(0) == "0"

    # Small positive value
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"

    # Includes the endpoint n
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"

    # Correct number of elements and boundaries for a larger input
    result = module_0.string_sequence(100)
    parts = result.split()
    assert len(parts) == 101
    assert parts[0] == "0"
    assert parts[-1] == "100"

    # Separator is a single space (no double spaces)
    assert "  " not in module_0.string_sequence(50)

    # Every element is a valid non-negative integer string
    assert all(p.isdigit() for p in module_0.string_sequence(20).split())

    print("All tests passed!")


test_string_sequence()

# Generated at 2026-11-02 12:22:23.622971
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0: should return just "0"
    assert module_0.string_sequence(0) == '0'

    # Test with n = 5: numbers 0 through 5 joined by spaces
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'

    # Test with a larger value
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

    # Test that the result is a string
    result = module_0.string_sequence(3)
    assert isinstance(result, str)

    # Test that numbers are separated by single spaces
    assert module_0.string_sequence(3) == '0 1 2 3'
    assert '  ' not in module_0.string_sequence(100)

    # Test element count: n + 1 numbers should be present
    assert len(module_0.string_sequence(7).split()) == 8

    print("All tests passed!")


if __name__ == "__main__":
    test_string_sequence()

# Generated at 2026-11-02 12:23:23.026470
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == "0"
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"

# Generated at 2026-11-02 12:24:31.308778
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0
    assert module_0.string_sequence(0) == '0'
    
    # Test with n = 5
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    
    # Test with a larger value
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    
    # Test with negative number (empty range)
    assert module_0.string_sequence(-1) == ''
    
    # Test return type
    assert isinstance(module_0.string_sequence(3), str)
    
    # Test correct number of elements
    assert len(module_0.string_sequence(7).split()) == 8
    
    print("All tests passed!")


if __name__ == "__main__":
    test_string_sequence()