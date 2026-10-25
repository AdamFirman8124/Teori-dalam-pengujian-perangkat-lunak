

# Generated at 2026-10-25 01:27:31.382585
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor("10101", "00101") == "10000"
    assert module_0.string_xor("1111", "0000") == "1111"
    assert module_0.string_xor("1100", "1010") == "0110"
    assert module_0.string_xor("", "") == ""

# Generated at 2026-10-25 01:27:37.564143
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor("10101", "00101") == "10000"
    assert module_0.string_xor("1111", "0000") == "1111"
    assert module_0.string_xor("1100", "1010") == "0110"
    assert module_0.string_xor("0000", "0000") == "0000"
    assert module_0.string_xor("", "") == ""

# Generated at 2026-10-25 01:27:42.577378
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor("10101", "00101") == "10000"
    assert module_0.string_xor("0000", "0000") == "0000"
    assert module_0.string_xor("1111", "0000") == "1111"
    assert module_0.string_xor("1010", "0101") == "1111"
    assert module_0.string_xor("", "") == ""

# Generated at 2026-10-25 01:27:47.914659
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor("10101", "00101") == "10000"
    assert module_0.string_xor("0000", "0000") == "0000"
    assert module_0.string_xor("1111", "0000") == "1111"
    assert module_0.string_xor("1111", "1111") == "0000"
    assert module_0.string_xor("", "") == ""

# Generated at 2026-10-25 01:27:52.766909
# Unit test for function string_xor
def test_string_xor():
    assert module_0.string_xor("1010", "0101") == "1111"
    assert module_0.string_xor("1100", "1010") == "0110"
    assert module_0.string_xor("1111", "1111") == "0000"
    assert module_0.string_xor("", "") == ""