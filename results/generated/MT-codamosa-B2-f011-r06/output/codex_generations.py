

# Generated at 2026-11-02 13:58:54.052717
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR operations
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '0101') == '1111'

    # Identical strings produce all zeros
    assert module_0.string_xor('0000', '0000') == '0000'
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('101010', '101010') == '000000'

    # Single character cases
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Commutativity: xor(a, b) == xor(b, a)
    assert module_0.string_xor('0110', '1010') == module_0.string_xor('1010', '0110')

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Different lengths: zip truncates to the shorter string
    assert module_0.string_xor('10', '1') == '0'
    assert module_0.string_xor('1', '10') == '0'
    assert module_0.string_xor('110', '1') == '0'

    # Self-inverse property: xor(a, a) is all zeros
    assert module_0.string_xor('1101001', '1101001') == '0000000'

    # XOR with zeros returns the original string
    assert module_0.string_xor('101101', '000000') == '101101'

# Generated at 2026-11-02 14:00:30.756553
# Unit test for function string_xor
def test_string_xor():
    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'

    # Multi-character strings
    assert module_0.string_xor('0101', '0101') == '0000'
    assert module_0.string_xor('1111', '0000') == '1111'
    assert module_0.string_xor('1010', '0110') == '1100'
    assert module_0.string_xor('1010', '1011') == '0001'

    # Classic example
    assert module_0.string_xor('010', '110') == '100'

    # Different lengths (zip truncates to shorter string)
    assert module_0.string_xor('0101', '01') == '00'
    assert module_0.string_xor('1', '1101') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Longer binary strings
    assert module_0.string_xor('111000', '000111') == '111111'
    assert module_0.string_xor('1100110011', '0011001100') == '1111111111'

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 14:02:48.297005
# Unit test for function string_xor
def test_string_xor():
    # Basic example from the function's intended behavior
    assert module_0.string_xor('010', '110') == '100'

    # XOR with all zeros returns the other string
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('000', '111') == '111'

    # XOR with itself returns all zeros
    assert module_0.string_xor('111', '111') == '000'
    assert module_0.string_xor('1010', '1010') == '0000'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings with alternating patterns
    assert module_0.string_xor('10101010', '01010101') == '11111111'
    assert module_0.string_xor('1100', '1010') == '0110'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Mixed longer binary strings
    assert module_0.string_xor('110110', '101101') == '011011'
    assert module_0.string_xor('1001001', '0110110') == '1111111'

# Generated at 2026-11-02 14:04:59.680241
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('000', '000') == '000'
    assert module_0.string_xor('111', '111') == '000'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Different lengths: zip truncates to shorter length
    assert module_0.string_xor('0101', '11') == '01'
    assert module_0.string_xor('1', '1010') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Longer strings
    assert module_0.string_xor('1100101', '1011010') == '0111111'
    assert module_0.string_xor('1000001', '0000001') == '1000000'

    # Property checks: XOR with self yields zeros, XOR with zeros yields self
    assert module_0.string_xor('110101', '110101') == '000000'
    assert module_0.string_xor('110101', '000000') == '110101'

    # Symmetry: xor(a, b) == xor(b, a)
    assert module_0.string_xor('0110', '1010') == module_0.string_xor('1010', '0110')


test_string_xor()
print("All tests passed!")

# Generated at 2026-11-02 14:06:34.233948
# Unit test for function string_xor
def test_string_xor():
    # Test with equal length binary strings
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('000', '000') == '000'
    assert module_0.string_xor('111', '111') == '000'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Test with single characters
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Test with empty strings
    assert module_0.string_xor('', '') == ''

    # Test with different lengths (zip truncates to shorter string)
    assert module_0.string_xor('10', '1') == '0'
    assert module_0.string_xor('1', '10') == '0'

    # Test longer strings
    assert module_0.string_xor('1101001', '1010101') == '0111100'

    # Test XOR properties
    a, b = '0110', '1010'
    # XOR is its own inverse
    assert module_0.string_xor(module_0.string_xor(a, b), b) == a
    # XOR with all zeros gives identity
    assert module_0.string_xor(a, '0000') == a
    # XOR is commutative
    assert module_0.string_xor(a, b) == module_0.string_xor(b, a)

    print("All string_xor tests passed!")


if __name__ == "__main__":
    test_string_xor()