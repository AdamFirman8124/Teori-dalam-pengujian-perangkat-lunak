

# Generated at 2026-11-02 23:05:25.409676
# Unit test for function string_sequence
def test_string_sequence():
    # Basic cases
    assert module_0.string_sequence(0) == "0"
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"

    # Negative input yields empty string (range is empty)
    assert module_0.string_sequence(-1) == ""
    assert module_0.string_sequence(-100) == ""

    # Return type and structure
    assert isinstance(module_0.string_sequence(3), str)
    assert module_0.string_sequence(3).count(" ") == 3  # n spaces separating n+1 numbers

    # Larger input checks
    result = module_0.string_sequence(100)
    assert result.split()[0] == "0"
    assert result.split()[-1] == "100"
    assert len(result.split()) == 101

    # Consistency with expected construction
    for n in range(20):
        expected = " ".join(str(i) for i in range(n + 1))
        assert module_0.string_sequence(n) == expected

    print("All tests passed!")

# Generated at 2026-11-02 23:07:35.699683
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == '0'
    assert module_0.string_sequence(1) == '0 1'
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(2) == '0 1 2'
    print("All tests passed!")

# Generated at 2026-11-02 23:10:21.484310
# Unit test for function string_sequence
def test_string_sequence():
    assert module_0.string_sequence(0) == "0"
    assert module_0.string_sequence(1) == "0 1"
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
    assert module_0.string_sequence(-1) == ""
    assert module_0.string_sequence(100) == " ".join(str(x) for x in range(101))

# Generated at 2026-11-02 23:12:38.396706
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0 (single element)
    assert module_0.string_sequence(0) == '0'
    
    # Test with a small positive number
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    
    # Test with n = 1
    assert module_0.string_sequence(1) == '0 1'
    
    # Test with a larger number
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    
    # Test with negative n (empty range)
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(-5) == ''
    
    print("All tests passed!")


if __name__ == "__main__":
    test_string_sequence()

# Generated at 2026-11-02 23:13:48.239385
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0 (only one number)
    assert module_0.string_sequence(0) == "0"
    # Test with n = 1
    assert module_0.string_sequence(1) == "0 1"
    # Test with n = 5
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    # Test with a larger number
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
    # Verify space-delimited output (no commas)
    result = module_0.string_sequence(3)
    assert result == "0 1 2 3"
    assert "," not in result
    # Verify the number of elements is n + 1
    assert len(module_0.string_sequence(20).split()) == 21
# nonce:8ff9b00f