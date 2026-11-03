

# Generated at 2026-11-03 06:12:20.136986
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == '0'
    assert module_0.string_sequence(1) == '0 1'
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(100) == ' '.join(str(i) for i in range(101))

# Generated at 2026-11-03 06:13:47.363581
# Unit test for function string_sequence
def test_string_sequence():
    # Basic case: single element
    assert module_0.string_sequence(0) == "0"
    
    # Small values
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    
    # Larger value
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
    
    # Negative input yields empty string
    assert module_0.string_sequence(-1) == ""
    
    # Structural checks
    assert module_0.string_sequence(3).split() == ["0", "1", "2", "3"]
    assert module_0.string_sequence(100).startswith("0 1 2")
    assert module_0.string_sequence(100).endswith("98 99 100")
    assert len(module_0.string_sequence(50).split()) == 51
    
    print("All string_sequence tests passed!")


if __name__ == "__main__":
    test_string_sequence()

# Generated at 2026-11-03 06:14:58.761731
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == '0'
    assert module_0.string_sequence(1) == '0 1'
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert module_0.string_sequence(3) == '0 1 2 3'

    # Verify structure for a larger input
    result = module_0.string_sequence(100)
    parts = result.split(' ')
    assert len(parts) == 101
    assert parts[0] == '0'
    assert parts[-1] == '100'
    assert ' ' not in ''.join(parts)  # each token is a pure number
    assert [int(x) for x in parts] == list(range(101))

    # Ensure single-space separation, no leading/trailing spaces
    assert not result.startswith(' ')
    assert not result.endswith(' ')
    assert '  ' not in result

    print("All tests passed!")

test_string_sequence()

# Generated at 2026-11-03 06:15:59.692532
# Unit test for function string_sequence
def test_string_sequence():
    # Single element
    assert module_0.string_sequence(0) == "0"
    
    # Small values
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(2) == "0 1 2"
    
    # Typical case
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    
    # Larger value
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
    
    # Negative input yields empty string
    assert module_0.string_sequence(-1) == ""
    assert module_0.string_sequence(-10) == ""
    
    # Verify spaces between numbers but not at ends
    result = module_0.string_sequence(3)
    assert result.startswith("0") and result.endswith("3")
    assert "  " not in result
    
    print("All tests passed!")


if __name__ == "__main__":
    test_string_sequence()

# Generated at 2026-11-03 06:17:57.554640
# Unit test for function string_sequence
def test_string_sequence():
    # Test basic case with n = 0
    assert module_0.string_sequence(0) == '0'
    
    # Test small positive number
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    
    # Test another small number
    assert module_0.string_sequence(3) == '0 1 2 3'
    
    # Test larger number
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    
    # Test negative input returns empty string
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(-10) == ''
    
    # Verify the result is a string type
    assert isinstance(module_0.string_sequence(5), str)
    
    # Verify correct number of elements (n + 1 items)
    assert len(module_0.string_sequence(7).split()) == 8
    
    # Verify first and last elements
    seq = module_0.string_sequence(4).split()
    assert seq[0] == '0'
    assert seq[-1] == '4'
    
    print("All tests passed!")


test_string_sequence()