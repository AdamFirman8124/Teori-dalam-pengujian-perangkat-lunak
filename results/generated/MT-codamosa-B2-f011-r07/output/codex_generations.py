

# Generated at 2026-11-02 20:04:47.355439
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '0110') == '1100'
    assert module_0.string_xor('0101', '1010') == '1111'

    # Identical strings produce all zeros
    assert module_0.string_xor('0000', '0000') == '0000'
    assert module_0.string_xor('1111', '1111') == '0000'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('110010', '101101') == '011111'
    assert module_0.string_xor('111000', '111000') == '000000'

    # XOR with all zeros returns original string
    assert module_0.string_xor('1010101', '0000000') == '1010101'

    # XOR with all ones flips every bit
    assert module_0.string_xor('1010101', '1111111') == '0101010'

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 20:06:23.648473
# Unit test for function string_xor
def test_string_xor():import unittest


class TestStringXor(unittest.TestCase):

    def test_identical_strings(self):
        self.assertEqual(module_0.string_xor('010', '010'), '000')

    def test_opposite_strings(self):
        self.assertEqual(module_0.string_xor('010', '101'), '111')

    def test_mixed_strings(self):
        self.assertEqual(module_0.string_xor('111', '010'), '101')

    def test_single_char_same(self):
        self.assertEqual(module_0.string_xor('1', '1'), '0')

    def test_single_char_diff(self):
        self.assertEqual(module_0.string_xor('1', '0'), '1')

    def test_empty_strings(self):
        self.assertEqual(module_0.string_xor('', ''), '')

    def test_all_zeros(self):
        self.assertEqual(module_0.string_xor('0000', '0000'), '0000')

    def test_all_ones_vs_zeros(self):
        self.assertEqual(module_0.string_xor('1111', '0000'), '1111')

    def test_alternating(self):
        self.assertEqual(module_0.string_xor('1010', '0101'), '1111')

    def test_long_strings(self):
        self.assertEqual(module_0.string_xor('110010', '101101'), '011111')

    def test_result_is_string(self):
        self.assertIsInstance(module_0.string_xor('10', '01'), str)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 20:07:21.056578
# Unit test for function string_xor
def test_string_xor():
    # Identical strings -> all zeros
    assert module_0.string_xor('010', '010') == '000'
    assert module_0.string_xor('111', '111') == '000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Classic XOR examples
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('1010', '0110') == '1100'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('0', '0') == '0'

    # Complementary strings -> all ones
    assert module_0.string_xor('0101', '1010') == '1111'
    assert module_0.string_xor('1111', '0000') == '1111'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Longer strings
    assert module_0.string_xor('110100', '101010') == '011110'
    assert module_0.string_xor('10010101', '01101010') == '11111111'

# Generated at 2026-11-02 20:08:22.393738
# Unit test for function string_xor
def test_string_xor():
    # Basic XOR cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111000', '101010') == '010010'
    assert module_0.string_xor('0011', '0100') == '0111'

    # Identical strings produce all zeros
    assert module_0.string_xor('0000', '0000') == '0000'
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('101010', '101010') == '000000'

    # Completely different strings produce all ones
    assert module_0.string_xor('0101', '1010') == '1111'

    # Single character cases
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Different lengths: zip truncates to the shorter string
    assert module_0.string_xor('01', '0010001') == '01'
    assert module_0.string_xor('111', '1') == '0'
    assert module_0.string_xor('0', '1010101') == '1'

    # Empty strings
    assert module_0.string_xor('', '') == ''
    assert module_0.string_xor('abc', '') == ''

    # Non-binary characters also work (any differing chars give '1')
    assert module_0.string_xor('ab', 'ba') == '11'
    assert module_0.string_xor('aa', 'aa') == '00'

    # Result length matches the shorter input
    assert len(module_0.string_xor('1100', '10')) == 2
    assert len(module_0.string_xor('10', '1100')) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()

# Generated at 2026-11-02 20:10:00.152550
# Unit test for function string_xor
def test_string_xor():
    # Test basic XOR operations
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Test identical strings (should be all zeros)
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Test single character strings
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('1', '1') == '0'
    assert module_0.string_xor('0', '0') == '0'

    # Test longer strings
    assert module_0.string_xor('110010', '101010') == '011000'
    assert module_0.string_xor('11110000', '00001111') == '11111111'

    # Test empty strings
    assert module_0.string_xor('', '') == ''

    # Test commutativity: xor(a, b) == xor(b, a)
    assert module_0.string_xor('1101', '0110') == module_0.string_xor('0110', '1101')

    print("All tests passed!")


if __name__ == "__main__":
    test_string_xor()