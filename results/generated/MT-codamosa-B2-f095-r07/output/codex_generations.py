

# Generated at 2026-11-02 20:12:49.643495
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Single key cases
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"A": 1}) == True

    # Non-string keys -> False
    assert module_0.check_dict_case({1: 1, "a": 2}) == False
    assert module_0.check_dict_case({(1, 2): "tuple"}) == False
    assert module_0.check_dict_case({None: 1}) == False

    # Keys that are neither upper nor lower -> False
    assert module_0.check_dict_case({"Hello": 1}) == False
    assert module_0.check_dict_case({"123": 1}) == False
    assert module_0.check_dict_case({"": 1}) == False

    # Lowercase with digits/underscores is still considered lowercase
    assert module_0.check_dict_case({"a1": 1, "b_2": 2}) == True

    # Uppercase with digits/underscores is still considered uppercase
    assert module_0.check_dict_case({"A1": 1, "B_2": 2}) == True

    # Mixed with non-string later in iteration -> False
    assert module_0.check_dict_case({"a": 1, "b": 2, 3: "c"}) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-11-02 20:14:36.976452
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dict returns False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Mixed case in a single key (e.g. capitalized word) -> False
    assert module_0.check_dict_case({"Name": 1, "age": 2}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Keys that are strings but neither upper nor lower (e.g. digits) -> False
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False

    # Lowercase start, then digit key breaks lower state -> False
    assert module_0.check_dict_case({"a": 1, "1": 2}) == False

    # Lowercase start, then mixed-case key -> False
    assert module_0.check_dict_case({"a": 1, "aB": 2}) == False

    # Keys with punctuation/symbols -> False
    assert module_0.check_dict_case({"!": 1, "?": 2}) == False

    # Lowercase keys with underscores/digits appended -> True
    assert module_0.check_dict_case({"a_b": 1, "c2": 3}) == True

    # Uppercase keys with underscores/digits appended -> True
    assert module_0.check_dict_case({"A_B": 1, "C2": 3}) == True

# Generated at 2026-11-02 20:16:27.015645
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Non-string keys -> False
    assert module_0.check_dict_case({"a": 1, 2: "b"}) == False
    assert module_0.check_dict_case({1: "a", "b": 2}) == False
    assert module_0.check_dict_case({(1, 2): "tuple_key"}) == False

    # Title case (neither upper nor lower) -> False
    assert module_0.check_dict_case({"Name": 1, "Age": 2}) == False

    # Single lowercase key -> True
    assert module_0.check_dict_case({"x": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"X": 1}) == True

    # Mixed string and non-string keys -> False
    assert module_0.check_dict_case({"a": 1, "b": 2, 3: 4}) == False

    # Keys with only lowercase letters and digits (digits not letters, islower False)
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Keys starting lowercase then non-lower -> False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

# Generated at 2026-11-02 20:18:38.565621
# Unit test for function check_dict_case
def test_check_dict_case():
    # nonce:ff407b49
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All lowercase string keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase string keys
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Single lowercase key
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key
    assert module_0.check_dict_case({"A": 1}) == True

    # Mixed case keys (lower then upper)
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Mixed case keys (upper then lower)
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Mixed case keys (multiple)
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Title-case keys (neither all upper nor all lower)
    assert module_0.check_dict_case({"Name": 1, "Age": 2}) == False
    assert module_0.check_dict_case({"Name": "John", "Address": "Highway 1"}) == False

    # Non-string keys
    assert module_0.check_dict_case({"a": 1, 2: "b"}) == False
    assert module_0.check_dict_case({1: "a", "b": 2}) == False
    assert module_0.check_dict_case({(1, 2): "tuple_key"}) == False

    # Keys with digits/symbols (neither upper nor lower at start state)
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False
    assert module_0.check_dict_case({"!a": 1}) == False
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == False

# Generated at 2026-11-02 20:20:56.364076
# Unit test for function check_dict_case
def test_check_dict_case():
    # nonce:fe598cde
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All lower case keys
    assert module_0.check_dict_case({"a": 1}) == True
    assert module_0.check_dict_case({"a": 1, "b": 2}) == True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All upper case keys
    assert module_0.check_dict_case({"A": 1}) == True
    assert module_0.check_dict_case({"A": 1, "B": 2}) == True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False
    assert module_0.check_dict_case({"A": 1, "B": 2, "c": 3}) == False

    # Non-string keys
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({1: 1, "a": 2}) == False
    assert module_0.check_dict_case({True: 1}) == False

    # Keys that are neither upper nor lower case
    assert module_0.check_dict_case({"aBc": 1}) == False
    assert module_0.check_dict_case({"aB": 1, "cD": 2}) == False
    assert module_0.check_dict_case({"": 1}) == False
    assert module_0.check_dict_case({"123": 1}) == False
    assert module_0.check_dict_case({"a1": 1}) == False