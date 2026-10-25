

# Generated at 2026-10-24 19:49:37.974027
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Identical strings -> all zeros
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Complementary strings -> all ones
    assert module_0.string_xor('1010', '0101') == '1111'

    # Single character
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Property check: xor is its own inverse
    a, b = '1101001', '0010110'
    assert module_0.string_xor(module_0.string_xor(a, b), b) == a

    print("All tests passed!")


test_string_xor()

# Generated at 2026-10-24 19:49:40.523450
# Unit test for function string_xor

# Generated at 2026-10-24 19:49:42.939541
# Unit test for function string_xor

# Generated at 2026-10-24 19:49:45.367737
# Unit test for function string_xor

# Generated at 2026-10-24 19:49:47.788596
# Unit test for function string_xor

# Generated at 2026-10-24 19:49:50.206353
# Unit test for function string_xor

# Generated at 2026-10-24 19:49:56.588521
# Unit test for function string_xor
def test_string_xor():assert module_0.string_xor("0101", "1100") == "1001"

# Generated at 2026-10-24 19:49:57.913110
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Identical strings -> all zeros
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Complementary strings -> all ones
    assert module_0.string_xor('1010', '0101') == '1111'

    # Single character
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Property check: xor is its own inverse
    a, b = '1101001', '0010110'
    assert module_0.string_xor(module_0.string_xor(a, b), b) == a

    print("All tests passed!")


test_string_xor()

# Generated at 2026-10-24 19:49:59.241244
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('1010', '0110') == '1100'

    # Identical strings -> all zeros
    assert module_0.string_xor('1111', '1111') == '0000'
    assert module_0.string_xor('0000', '0000') == '0000'

    # Complementary strings -> all ones
    assert module_0.string_xor('1010', '0101') == '1111'

    # Single character
    assert module_0.string_xor('0', '1') == '1'
    assert module_0.string_xor('1', '1') == '0'

    # Empty strings
    assert module_0.string_xor('', '') == ''

    # Property check: xor is its own inverse
    a, b = '1101001', '0010110'
    assert module_0.string_xor(module_0.string_xor(a, b), b) == a

    print("All tests passed!")


test_string_xor()