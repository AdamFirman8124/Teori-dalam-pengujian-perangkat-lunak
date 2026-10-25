

# Generated at 2026-10-24 06:27:08.131897
# Unit test for function string_xor
def test_string_xor():assert module_0.string_xor("10101", "00101") == "10000"

# Generated at 2026-10-24 06:27:15.175740
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

# Generated at 2026-10-24 06:27:16.487247
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

# Generated at 2026-10-24 06:27:17.813321
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

# Generated at 2026-10-24 06:27:19.129064
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