

# Generated at 2026-11-02 22:04:09.943508
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dict should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

    # Non-string key -> False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({3: 1, "b": 2}) == False

    # Keys with no alphabetic characters -> False (isupper/islower both False)
    assert module_0.check_dict_case({"1": 1}) == False
    assert module_0.check_dict_case({"aB": 1}) == False
    assert module_0.check_dict_case({"Ab": 1, "cD": 2}) == False

    # Mixed case transition after valid start -> False
    assert module_0.check_dict_case({"A": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

# Generated at 2026-11-02 22:07:56.824908
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary -> False
    assert module_0.check_dict_case({}) == False

    # Single-key dictionaries
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"A": 1}) == True

    # All lowercase keys -> True
    assert module_0.check_dict_case({"p": "pineapple", "b": "banana"}) == True
    assert module_0.check_dict_case({"apple": 1, "banana": 2, "cherry": 3}) == True

    # All uppercase keys -> True
    assert module_0.check_dict_case({"NAME": "JOHN", "AGE": "36", "CITY": "HOUSTON"}) == True
    assert module_0.check_dict_case({"APPLE": 1, "BANANA": 2}) == True

    # Mixed-case keys -> False
    assert module_0.check_dict_case({"p": "pineapple", "A": "banana", "B": "banana"}) == False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({1: "one", 2: "two"}) == False
    assert module_0.check_dict_case({"p": "pineapple", 5: "banana", "z": "banana"}) == False
    assert module_0.check_dict_case({"a": 1, 2: "b"}) == False

    # Keys that are neither all-upper nor all-lower (title case) -> False
    assert module_0.check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
    assert module_0.check_dict_case({"aB": 1}) == False

# Generated at 2026-11-02 22:10:10.117439
# Unit test for function check_dict_case
def test_check_dict_case():
# nonce:44fb1134
    # Empty dictionary returns False
    assert module_0.check_dict_case({}) == False

    # All lowercase keys return True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True
    assert module_0.check_dict_case({"a": 1}) == True

    # All uppercase keys return True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True
    assert module_0.check_dict_case({"A": 1}) == True
    assert module_0.check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True

    # Mixed case keys return False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    assert module_0.check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False

    # Title case keys (neither upper nor lower) return False
    assert module_0.check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False

    # Non-string keys return False
    assert module_0.check_dict_case({1: "a", 2: "b"}) == False
    assert module_0.check_dict_case({"a": 1, 2: "b"}) == False

    # Keys with digits/punctuation still count by their cased letters
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True


if __name__ == "__main__":
    test_check_dict_case()
    print("All tests passed!")