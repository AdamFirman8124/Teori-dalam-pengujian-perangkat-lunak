

# Generated at 2026-11-02 18:00:41.172047
# Unit test for function check_dict_case
def test_check_dict_case():
    # Test empty dictionary
    assert module_0.check_dict_case({}) == False

    # Test all lower case keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # Test all upper case keys
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Test mixed case keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Test single key dictionaries
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"A": 1}) == True

    # Test non-string keys
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Test keys with mixed characters (not purely upper/lower)
    assert module_0.check_dict_case({"aB": 1, "cd": 2}) == False
    assert module_0.check_dict_case({"Ab": 1}) == False

    # Test keys with digits/symbols (isupper/islower are False)
    assert module_0.check_dict_case({"a1": 1}) == False
    assert module_0.check_dict_case({"1": 1}) == False

    # Test longer dictionaries
    assert module_0.check_dict_case({"name": 1, "age": 2, "city": 3}) == True
    assert module_0.check_dict_case({"NAME": 1, "AGE": 2, "CITY": 3}) == True
    assert module_0.check_dict_case({"name": 1, "AGE": 2}) == False

# nonce:1d166d1f

# Generated at 2026-11-02 18:03:14.567345
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary -> False
    assert module_0.check_dict_case({}) == False

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # All lowercase keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({1: 1, 2: 2, 3: 3}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({1: "a", "b": 2}) == False

    # Keys with no letter case (digits/symbols) -> False
    assert module_0.check_dict_case({"1": 1}) == False
    assert module_0.check_dict_case({"a": 1, "1": 2}) == False
    assert module_0.check_dict_case({"!": 1, "?": 2}) == False

    # Values should not affect the result
    assert module_0.check_dict_case({"x": "UPPER", "y": [1, 2]}) == True
    assert module_0.check_dict_case({"X": None, "Y": {"k": 1}}) == True

    print("All tests passed!")


test_check_dict_case()

# Generated at 2026-11-02 18:05:11.733437
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary returns False
    assert module_0.check_dict_case({}) == False

    # All uppercase string keys returns True
    assert module_0.check_dict_case({"A": 1, "B": 2}) == True
    assert module_0.check_dict_case({"AAA": 1, "BBB": 2, "CCC": 3}) == True

    # All lowercase string keys returns True
    assert module_0.check_dict_case({"a": 1, "b": 2}) == True
    assert module_0.check_dict_case({"aaa": 1, "bbb": 2, "ccc": 3}) == True

    # Mixed case keys returns False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Single key cases
    assert module_0.check_dict_case({"A": 1}) == True
    assert module_0.check_dict_case({"a": 1}) == True

    # Non-string key causes mixed state
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({(1, 2): "tuple", "a": 1}) == False

    # Keys with digits attached to letters keep case classification
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Keys with mixed-case letters (neither isupper nor islower) fail at start
    assert module_0.check_dict_case({"aB": 1, "Ab": 2}) == False
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    # Keys with no cased characters at all fail at start
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False
    assert module_0.check_dict_case({"!@#": 1}) == False

    # Uppercase start then non-uppercase key becomes mixed
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    # Lowercase start then non-lowercase key becomes mixed
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

# Generated at 2026-11-02 18:07:14.984799
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary returns False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": "apple", "b": "banana"}) == True
    assert module_0.check_dict_case({"name": "John", "age": "36", "city": "Houston"}) == True

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": "apple", "B": "banana"}) == True

# Generated at 2026-11-02 18:08:40.076289
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All keys uppercase
    assert module_0.check_dict_case({"A": 1, "B": 2}) == True
    assert module_0.check_dict_case({"A": 1, "BC": 2, "DEF": 3}) == True

    # All keys lowercase
    assert module_0.check_dict_case({"a": 1, "b": 2}) == True
    assert module_0.check_dict_case({"abc": 1, "def": 2}) == True

    # Single key cases
    assert module_0.check_dict_case({"A": 1}) == True
    assert module_0.check_dict_case({"a": 1}) == True

    # Mixed case keys
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    assert module_0.check_dict_case({"Ab": 1}) == False
    assert module_0.check_dict_case({"aB": 1, "cd": 2}) == False

    # Non-string keys
    assert module_0.check_dict_case({1: 1, "a": 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({1.5: 1}) == False

    # Keys with no letter case
    assert module_0.check_dict_case({"1": 1}) == False
    assert module_0.check_dict_case({"": 1}) == False
    assert module_0.check_dict_case({"A": 1, "1": 2}) == False

    # Uppercase/lowercase keys containing digits
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    print("All tests passed!")