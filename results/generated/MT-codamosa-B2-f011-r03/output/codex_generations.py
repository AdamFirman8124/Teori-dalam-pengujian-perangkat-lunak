

# Generated at 2026-10-24 07:05:12.819103
# Unit test for function string_xor

# Generated at 2026-10-24 07:05:15.244331
# Unit test for function string_xor

# Generated at 2026-10-24 07:05:20.650622
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('111', '000') == '111'
    assert module_0.string_xor('1010', '1010') == '0000'
    assert module_0.string_xor('1', '0') == '1'
    assert module_0.string_xor('', '') == ''
    assert module_0.string_xor('1101', '0110') == '1011'

# Generated at 2026-10-24 07:05:22.086124
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('1010', '1010') == '0000'   # identical -> all zeros
    assert module_0.string_xor('1', '0') == '1'

    # Single character
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('110010', '101101') == '011111'

    # Unequal lengths: zip truncates to the shorter one
    assert module_0.string_xor('1101', '10') == '01'
    assert module_0.string_xor('', '101') == ''            # empty input -> empty output

    print("All tests passed!")


test_string_xor()

# Generated at 2026-10-24 07:05:23.399418
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('1010', '1010') == '0000'   # identical -> all zeros
    assert module_0.string_xor('1', '0') == '1'

    # Single character
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('110010', '101101') == '011111'

    # Unequal lengths: zip truncates to the shorter one
    assert module_0.string_xor('1101', '10') == '01'
    assert module_0.string_xor('', '101') == ''            # empty input -> empty output

    print("All tests passed!")


test_string_xor()

# Generated at 2026-10-24 07:05:27.820110
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('1010', '1010') == '0000'   # identical -> all zeros
    assert module_0.string_xor('1', '0') == '1'

    # Single character
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('110010', '101101') == '011111'

    # Unequal lengths: zip truncates to the shorter one
    assert module_0.string_xor('1101', '10') == '01'
    assert module_0.string_xor('', '101') == ''            # empty input -> empty output

    print("All tests passed!")


test_string_xor()

# Generated at 2026-10-24 07:05:29.136587
# Unit test for function string_xor
def test_string_xor():
    # Basic cases
    assert module_0.string_xor('010', '110') == '100'
    assert module_0.string_xor('0000', '1111') == '1111'
    assert module_0.string_xor('1010', '1010') == '0000'   # identical -> all zeros
    assert module_0.string_xor('1', '0') == '1'

    # Single character
    assert module_0.string_xor('0', '0') == '0'
    assert module_0.string_xor('1', '1') == '0'

    # Longer strings
    assert module_0.string_xor('11110000', '00001111') == '11111111'
    assert module_0.string_xor('110010', '101101') == '011111'

    # Unequal lengths: zip truncates to the shorter one
    assert module_0.string_xor('1101', '10') == '01'
    assert module_0.string_xor('', '101') == ''            # empty input -> empty output

    print("All tests passed!")


test_string_xor()