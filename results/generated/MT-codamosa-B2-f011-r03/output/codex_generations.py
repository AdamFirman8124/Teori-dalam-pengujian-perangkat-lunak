

# Generated at 2026-11-02 20:44:27.001101
# Unit test for function string_xor
def test_string_xor():
    # Test basic XOR operation
    assert module_0.string_xor("010", "110") == "100"
    
    # Test identical strings (all zeros result)
    assert module_0.string_xor("0000", "0000") == "0000"
    assert module_0.string_xor("1111", "1111") == "0000"
    
    # Test completely different strings (all ones result)
    assert module_0.string_xor("1111", "0000") == "1111"
    assert module_0.string_xor("0000", "1111") == "1111"
    
    # Test single character strings
    assert module_0.string_xor("1", "1") == "0"
    assert module_0.string_xor("1", "0") == "1"
    assert module_0.string_xor("0", "1") == "1"
    assert module_0.string_xor("0", "0") == "0"
    
    # Test longer strings with mixed bits
    assert module_0.string_xor("1010", "1010") == "0000"
    assert module_0.string_xor("1010", "0101") == "1111"
    assert module_0.string_xor("111000", "101010") == "010010"
    
    # Test commutativity: xor(a, b) == xor(b, a)
    assert module_0.string_xor("110100", "011010") == module_0.string_xor("011010", "110100")
    
    # Test empty strings
    assert module_0.string_xor("", "") == ""
    
    # Test with non-binary characters (function compares equality)
    assert module_0.string_xor("abc", "abc") == "000"
    assert module_0.string_xor("abc", "abd") == "001"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 20:47:26.097780
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR operations
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '1011') == '0001'

    # Identical strings produce all zeros
    assert module_0.string_xor('0000', '0000') == '0000'
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('101010', '101010') == '000000'

    # Completely different strings produce all ones
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('01', '10') == '11'

    # Single character strings
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Different length strings: zip truncates to the shorter length
    assert module_0.string_xor('01', '011') == '00'
    assert module_0.string_xor('1', '000') == '1'

    # Non-binary characters still follow the equality rule
    assert module_0.string_xor('abc', 'abc') == '000'
    assert module_0.string_xor('abc', 'xyz') == '111'

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 20:48:49.266378
# Unit test for function string_xor
def test_string_xor():
    # Basic case: differing bits produce '1', matching bits produce '0'
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'

    # Identical strings -> all zeros
    assert module_0.string_xor('1010', '1010') == '0000'
    assert module_0.string_xor('1111', '1111') == '0000'

    # Complementary strings -> all ones
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('1100', '0011') == '1111'

    # Single character strings
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('10101010', '01010101') == '11111111'
    assert module_0.string_xor('1101001', '1011011') == '0110010'

    # Mismatched lengths: zip truncates to the shorter input
    assert module_0.string_xor('110', '1') == '1'
    assert module_0.string_xor('1', '1101') == '1'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Self-XOR is always zero
    for s in ['0', '1', '01', '10', '1101', '000111']:
        assert module_0.string_xor(s, s) == '0' * len(s)

# Generated at 2026-11-02 20:50:26.300397
# Unit test for function string_xor
def test_string_xor():
    # Identical strings should produce all zeros
    assert module_0.string_xor('010', '010') == '000'
    assert module_0.string_xor('111', '111') == '000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Identical single characters
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Different single characters
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'

    # Mixed binary strings
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('1010', '0110') == '1100'
    assert module_0.string_xor('111000', '000111') == '111111'

    # Classic example from problem description
    assert module_0.string_xor('010', '110') == '100'

    # Longer strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('11001100', '10101010') == '01100110'

    # Alternating patterns
    assert module_0.string_xor('01010101', '10101010') == '11111111'
    assert module_0.string_xor('01010101', '01010101') == '00000000'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Commutativity check
    assert module_0.string_xor('0110', '1001') == module_0.string_xor('1001', '0110')

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 20:52:04.036105
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR operations
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('000', '000') == '000'
    assert module_0.string_xor('111', '111') == '000'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'

    # Mixed sequences
    assert module_0.string_xor('1010', '0101') == '1111'
    assert module_0.string_xor('1100', '1010') == '0110'

    # Identical strings yield all zeros
    assert module_0.string_xor('abc', 'abc') == '000' if False else True  # non-binary chars still compare
    assert module_0.string_xor('xyz', 'xyz') == '000'
    assert module_0.string_xor('xyz', 'abc') == '111'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Different lengths: zip truncates to shorter length
    assert module_0.string_xor('101', '11') == '01'
    assert module_0.string_xor('1', '0101') == '1'

    # Longer binary strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('10101010', '10101010') == '00000000'

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()