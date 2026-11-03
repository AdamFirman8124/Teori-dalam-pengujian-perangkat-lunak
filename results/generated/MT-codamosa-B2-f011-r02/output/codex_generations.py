

# Generated at 2026-11-03 03:26:45.996974
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '1011') == '0001'

    # Same strings result in all zeros
    assert module_0.string_xor('1010', '1010') == '0000'
    assert module_0.string_xor('000', '000') == '000'

    # Complementary strings result in all ones
    assert module_0.string_xor('1010', '0101') == '1111'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Different lengths: zip truncates to the shorter length
    assert module_0.string_xor('1101', '10') == '01'

    # Longer strings
    assert module_0.string_xor('11110000', '10101010') == '01011010'

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-03 03:27:57.981778
# Unit test for function string_xor
def test_string_xor():
    # Basic case: differing bits produce '1', matching bits produce '0'
    assert module_0.string_xor('010', '110') == '100'
    # Example from classic spec
    assert module_0.string_xor('111', '101') == '010'
    # Identical strings should produce all zeros
    assert module_0.string_xor('1010', '1010') == '0000'
    # All differing bits produce all ones
    assert module_0.string_xor('0000', '1111') == '1111'
    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'
    # Empty strings produce empty result
    assert module_0.string_xor('', '') == ''
    # Zip truncates to the shorter string
    assert module_0.string_xor('101', '10') == '01'
    assert module_0.string_xor('1', '1010') == '1'
    # Longer binary strings
    assert module_0.string_xor('110010', '011000') == '101010'
    # XOR is commutative
    assert module_0.string_xor('1101', '0110') == module_0.string_xor('0110', '1101')
    # XOR with itself yields all zeros
    s = '1101001'
    assert module_0.string_xor(s, s) == '0' * len(s)

# Generated at 2026-11-03 03:29:51.959316
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '1010') == '0000'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('1101', '0110') == '1011'
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('10101010', '01010101') == '11111111'

# Generated at 2026-11-03 03:31:29.851449
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '1010') == '0000'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('0', '0') == '0'

    # Identical strings yield all zeros
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('0101', '0101') == '0000'

    # Complementary strings yield all ones
    assert module_0.string_xor('0101', '1010') == '1111'

    # Longer strings
    assert module_0.string_xor('110011', '101010') == '011001'
    assert module_0.string_xor('00000000', '11111111') == '11111111'

    # Unequal lengths: zip truncates to shorter length
    assert module_0.string_xor('110', '1') == '0'
    assert module_0.string_xor('10', '101') == '01'

    # Empty strings
    assert module_0.string_xor('', '') == ''
    assert module_0.string_xor('abc', '') == ''

    # Non-binary characters also work (any differing chars -> '1')
    assert module_0.string_xor('ab', 'ab') == '00'
    assert module_0.string_xor('ab', 'ba') == '11'

    # Result is always composed of '0' and '1'
    result = module_0.string_xor('0123456789', '9876543210')
    assert all(c in '01' for c in result)
    assert len(result) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-03 03:33:16.657422
# Unit test for function string_xor
def test_string_xor():
    # Identical strings produce all zeros
    assert module_0.string_xor('010', '010') == '000'
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('', '') == ''

    # Completely different strings produce all ones
    assert module_0.string_xor('010', '101') == '111'
    assert module_0.string_xor('0000', '1111') == '1111'

    # Mixed cases
    assert module_0.string_xor('1010', '0110') == '1100'
    assert module_0.string_xor('111000', '101010') == '010010'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # zip truncates to the shorter string
    assert module_0.string_xor('1010', '101') == '000'
    assert module_0.string_xor('1', '101010') == '0'

    # Single characters
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'

    # XOR is symmetric
    assert module_0.string_xor('1101', '0110') == module_0.string_xor('0110', '1101')

    # XOR with itself yields all zeros
    s = '1101001'
    assert module_0.string_xor(s, s) == '0' * len(s)

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()