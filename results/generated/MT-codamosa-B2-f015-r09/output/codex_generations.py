

# Generated at 2026-11-02 17:59:06.946163
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0: sequence contains just "0"
    assert module_0.string_sequence(0) == '0'

    # Test with n = 5: numbers 0 through 5 separated by spaces
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'

    # Test with n = 1: smallest multi-element sequence
    assert module_0.string_sequence(1) == '0 1'

    # Test with a larger value
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

    # Test with negative n: empty range produces empty string
    assert module_0.string_sequence(-1) == ''

    # Test result type is a string
    assert isinstance(module_0.string_sequence(3), str)

    # Test number of elements matches n + 1
    assert len(module_0.string_sequence(7).split(' ')) == 8

    print("All tests passed!")


test_string_sequence()

# Generated at 2026-11-02 18:00:34.599323
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0 (single element)
    assert module_0.string_sequence(0) == '0'
    
    # Test with a small positive number
    assert module_0.string_sequence(3) == '0 1 2 3'
    
    # Test with a larger number
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    
    # Test with n = 1
    assert module_0.string_sequence(1) == '0 1'
    
    # Test with negative input (empty range)
    assert module_0.string_sequence(-1) == ''
    assert module_0.string_sequence(-5) == ''

# Generated at 2026-11-02 18:02:46.239202
# Unit test for function string_sequence
def test_string_sequence():
    # Test with n = 0
    assert module_0.string_sequence(0) == '0'
    
    # Test with n = 5
    assert module_0.string_sequence(5) == '0 1 2 3 4 5'
    
    # Test with n = 10
    assert module_0.string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    
    # Test type of result
    assert isinstance(module_0.string_sequence(3), str)
    
    # Test that elements are space-separated
    result = module_0.string_sequence(4)
    assert result.split(' ') == ['0', '1', '2', '3', '4']
    
    # Verify length matches expected count (n + 1 elements)
    assert len(module_0.string_sequence(7).split(' ')) == 8

# Generated at 2026-11-02 18:04:59.033720
# Unit test for function string_sequence
def test_string_sequence():
    # Test with a typical positive integer
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"

    # Test edge case: n = 0 (single number)
    assert module_0.string_sequence(0) == "0"

    # Test edge case: n = 1
    assert module_0.string_sequence(1) == "0 1"

    # Test with a larger number
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"

    # Test that the return type is a string
    assert isinstance(module_0.string_sequence(3), str)

    # Test correct number of elements and space separation
    result = module_0.string_sequence(4)
    assert result.split(' ') == ["0", "1", "2", "3", "4"]
    assert len(result.split(' ')) == 5  # should contain n + 1 numbers

    # Test edge case: negative input yields an empty string
    assert module_0.string_sequence(-1) == ""


test_string_sequence()
print("All tests passed!")

# Generated at 2026-11-02 18:06:47.156014
# Unit test for function string_sequence
def test_string_sequence():
    # nonce:4343335f
    # Test with n = 0 (single element)
    assert module_0.string_sequence(0) == "0"
    
    # Test with n = 1
    assert module_0.string_sequence(1) == "0 1"
    
    # Test with a typical case
    assert module_0.string_sequence(5) == "0 1 2 3 4 5"
    
    # Test with a larger number
    assert module_0.string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
    
    # Test with a large value
    assert module_0.string_sequence(100) == " ".join(str(x) for x in range(101))
    
    # Test with negative input (edge case: empty range)
    assert module_0.string_sequence(-1) == ""
    assert module_0.string_sequence(-5) == ""
    
    # Verify return type is always a string
    assert isinstance(module_0.string_sequence(3), str)
    
    # Verify correct number of elements (split on spaces)
    assert len(module_0.string_sequence(7).split()) == 8
    
    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_string_sequence()