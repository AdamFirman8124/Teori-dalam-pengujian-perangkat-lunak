

# Generated at 2026-11-02 20:37:06.827025
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase keys should return True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys should return True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys should return False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Mixed case within a single key should return False
    assert module_0.check_dict_case({"aB": 1, "Av": 2}) == False

    # Non-string keys should return False
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Keys with no case (digits/symbols) should return False
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False
    assert module_0.check_dict_case({"a": 1, "1": 2}) == False

    # Single lowercase key should return True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key should return True
    assert module_0.check_dict_case({"A": 1}) == True

    # Keys with leading/trailing uppercase should return False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-11-02 20:38:34.315418
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dict should return False
    assert module_0.check_dict_case({}) == False

    # All uppercase keys should return True
    assert module_0.check_dict_case({"a": 1, "b": 2}) == True

    # All lowercase keys should return True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # Mixed case keys should return False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Keys that are neither upper nor lower (e.g., mixed case word) should return False
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    # Non-string keys should return False
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Single uppercase key should return True
    assert module_0.check_dict_case({"A": 1}) == True

    # Single lowercase key should return True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single mixed-case key should return False
    assert module_0.check_dict_case({"Ab": 1}) == False

    # Keys with punctuation/digits (neither upper nor lower) should return False
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False

    # Start with uppercase then lowercase should return False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Start with lowercase then uppercase should return False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # All uppercase keys with values should return True
    assert module_0.check_dict_case({"KEY1": 1, "KEY2": 2}) == True

    # All lowercase keys with underscores should return True
    assert module_0.check_dict_case({"key_one": 1, "key_two": 2}) == True


# nonce:13ac7646

# Generated at 2026-11-02 20:40:17.608596
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary returns False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys returns True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys returns True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed upper and lower case keys returns False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

    # Single lowercase key returns True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key returns True
    assert module_0.check_dict_case({"A": 1}) == True

    # Non-string key returns False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Keys with mixed casing within string (e.g. title case) returns False
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    # Keys with digits/symbols (not upper or lower) returns False
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == False

    # Mixed lowercase keys still True with multiple entries
    assert module_0.check_dict_case({"apple": 1, "banana": 2}) == True

    # Mixed uppercase keys still True with multiple entries
    assert module_0.check_dict_case({"APPLE": 1, "BANANA": 2}) == True

    print("All tests passed!")

if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-11-02 20:41:26.501727
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Single key cases
    assert module_0.check_dict_case({"A": 1}) == True
    assert module_0.check_dict_case({"a": 1}) == True

    # Keys with non-alpha characters (isupper/islower return False) -> False
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == False
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == False
    assert module_0.check_dict_case({"!": 1, "@": 2}) == False

    # Mixed upper and lower starting with upper -> False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Mixed upper and lower starting with lower -> False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

    # Multi-character keys
    assert module_0.check_dict_case({"HELLO": 1, "WORLD": 2}) == True
    assert module_0.check_dict_case({"hello": 1, "world": 2}) == True
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    print("All tests passed!")


test_check_dict_case()

# Generated at 2026-11-02 20:43:12.072765
# Unit test for function check_dict_case
def test_check_dict_case():
    # nonce:d3fbb84a
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All lower case keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All upper case keys
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Non-string keys
    assert module_0.check_dict_case({1: "one", 2: "two"}) == False
    assert module_0.check_dict_case({"a": 1, 2: "two"}) == False

    # Single key dictionaries
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"A": 1}) == True

    # Alphanumeric keys that are consistently lower/upper
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True

    # Keys that are neither upper nor lower (digits only)
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False

    # Title case keys (neither all upper nor all lower)
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    # Empty string key
    assert module_0.check_dict_case({"": 1}) == False

    # Lower case start but later key not lower
    assert module_0.check_dict_case({"a": 1, "b": 2, "1C": 3}) == False

    print("All tests passed!")