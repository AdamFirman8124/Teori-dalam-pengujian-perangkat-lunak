

# Generated at 2026-11-03 01:27:33.082701
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({1: 1, 2: 2, 3: 3}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2, "c": 3}) == False

    # Keys with neither upper nor lower (e.g., digits/punctuation) -> False
    assert module_0.check_dict_case({"123": 1, "456": 2}) == False
    assert module_0.check_dict_case({"!@#": 1, "$%^": 2}) == False

    # Mixed string and non-lower/upper -> False
    assert module_0.check_dict_case({"a": 1, "123": 2}) == False

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # Uppercase followed by non-uppercase -> False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Lowercase followed by non-lowercase -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Keys with mixed content in string -> False
    assert module_0.check_dict_case({"Hello": 1}) == False
    assert module_0.check_dict_case({"aBc": 1}) == False

    # Multiple lowercase keys -> True
    assert module_0.check_dict_case({"apple": 1, "banana": 2}) == True

    # Multiple uppercase keys -> True
    assert module_0.check_dict_case({"APPLE": 1, "BANANA": 2}) == True

# Generated at 2026-11-03 01:30:08.354810
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

    # Mixed case keys (reverse order) should return False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Non-string key should return False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({1: 1, "b": 2}) == False

    # Single lowercase key should return True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key should return True
    assert module_0.check_dict_case({"A": 1}) == True

    # Title-case key (neither all upper nor all lower) should return False
    assert module_0.check_dict_case({"Name": 1, "Bob": 2}) == False

    # Keys with digits attached to lowercase letters are still lowercase
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Keys that are neither upper nor lower (e.g., digits only) should return False
    assert module_0.check_dict_case({"123": 1, "456": 2}) == False

    # Lowercase followed by non-string key should return False
    assert module_0.check_dict_case({"apple": 1, "banana": 2, (1, 2): 3}) == False

    # Values don't matter, only keys
    assert module_0.check_dict_case({"x": None, "y": [1, 2]}) == True

    print("All tests passed!")


test_check_dict_case()

# Generated at 2026-11-03 01:31:39.149171
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True
    assert module_0.check_dict_case({"p": "pineapple", "b": "banana"}) == True

    # All uppercase string keys
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True
    assert module_0.check_dict_case({"KEY": "value"}) == True

    # Mixed lower/upper keys across the dict
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"p": "pineapple", "A": "banana", "B": "banana"}) == False

    # Mixed case within keys
    assert module_0.check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False

    # Non-string keys
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2, "c": 3}) == False
    assert module_0.check_dict_case({"A": 1, 2: 2}) == False

    # Single-key dictionaries
    assert module_0.check_dict_case({"key": 1}) == True
    assert module_0.check_dict_case({"KEY": 1}) == True

    # Keys with no cased characters (neither upper nor lower)
    assert module_0.check_dict_case({"123": 1, "456": 2}) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-11-03 01:33:07.834394
# Unit test for function check_dict_case
def test_check_dict_case():
    assert module_0.check_dict_case({}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, 3: "c"}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, "cc": 3}) == True
    assert module_0.check_dict_case({"A": 1, "B": 2, "CC": 3}) == True
    assert module_0.check_dict_case({"Name": 1, "Address": 2}) == False
    assert module_0.check_dict_case({"123": 1, "456": 2}) == False

test_check_dict_case()

# Generated at 2026-11-03 01:34:43.276029
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary -> False
    assert module_0.check_dict_case({}) == False

    # Single lowercase / uppercase keys -> True
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"A": 1}) == True

    # All lowercase keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case violation on second key -> False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({"a": 1, 2: 3}) == False
    assert module_0.check_dict_case({1: "a"}) == False
    assert module_0.check_dict_case({None: 1}) == False

    # Keys with no letter case (digits, symbols, empty string) -> False
    assert module_0.check_dict_case({"a1": 1}) == False
    assert module_0.check_dict_case({"1a": 1}) == False
    assert module_0.check_dict_case({"": 1}) == False
    assert module_0.check_dict_case({"Name": "John"}) == False

    # Uppercase keys containing digits still count as upper -> True
    assert module_0.check_dict_case({"STATE": "NC", "OID": "32"}) == True

    # Lowercase keys mixed with uppercase -> False
    assert module_0.check_dict_case({"p": "pineapple", "B": "banana"}) == False

    print("All tests passed!")