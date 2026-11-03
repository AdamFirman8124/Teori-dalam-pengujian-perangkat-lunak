

# Generated at 2026-11-02 08:46:02.728459
# Unit test for function check_dict_case
def test_check_dict_case():
    # All lowercase keys -> True
    assert module_0.check_dict_case({"a": "apple", "b": "banana"}) == True
    # All uppercase keys -> True
    assert module_0.check_dict_case({"NAME": "John", "AGE": "36", "CITY": "Houston"}) == True
    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True
    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True
    # Keys with digits still count as consistent case -> True
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Mixed case keys -> False
    assert module_0.check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
    # Title case keys -> False
    assert module_0.check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
    # Lower then upper -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    # Upper then lower -> False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False
    # Numeric string key is neither upper nor lower -> False
    assert module_0.check_dict_case({"a": "apple", "8": "banana"}) == False
    # Non-string keys -> False
    assert module_0.check_dict_case({1: "apple", 2: "banana"}) == False
    assert module_0.check_dict_case({"a": 1, 3.5: "b"}) == False
    # Empty string key is neither upper nor lower -> False
    assert module_0.check_dict_case({"": 1}) == False
    # Empty dict -> False
    assert module_0.check_dict_case({}) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-11-02 08:46:10.421138
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary
    assert module_0.check_dict_case({}) == False

    # All lowercase keys
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Single lowercase key
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key
    assert module_0.check_dict_case({"A": 1}) == True

    # Mixed case keys
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Non-string keys
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({None: 1}) == False

    # Keys with both upper and lower characters (not uniformly cased)
    assert module_0.check_dict_case({"aB": 1, "cD": 2}) == False
    assert module_0.check_dict_case({"Ab": 1, "Cd": 2}) == False

    # Empty string key (neither upper nor lower)
    assert module_0.check_dict_case({"": 1}) == False

    # Numeric string keys (neither upper nor lower)
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False

    # Three keys with one breaking the case pattern
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

# Generated at 2026-11-02 08:46:33.460089
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All lowercase keys should return True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # All uppercase keys should return True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # Mixed case keys should return False
    assert module_0.check_dict_case({"a": 1, "B": 2, "c": 3}) == False

    # Single lowercase key should return True
    assert module_0.check_dict_case({"hello": 1}) == True

    # Single uppercase key should return True
    assert module_0.check_dict_case({"WORLD": 1}) == True

    # Non-string keys should return False
    assert module_0.check_dict_case({1: 1, 2: 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False
    assert module_0.check_dict_case({True: 1}) == False

    # Keys with mixed case within a single key break the start state
    assert module_0.check_dict_case({"Hello": 1, "World": 2}) == False

    # Keys with digits/symbols are neither upper nor lower
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == False

    # Mixed: starts uppercase then lowercase key
    assert module_0.check_dict_case({"AB": 1, "cd": 2}) == False

    # Mixed: starts lowercase then uppercase key
    assert module_0.check_dict_case({"ab": 1, "CD": 2}) == False

    # All keys start with uppercase but contain lowercase -> not isupper
    assert module_0.check_dict_case({"Ab": 1, "Cd": 2}) == False

    # Consistent uppercase multi-char keys
    assert module_0.check_dict_case({"APPLE": 1, "BANANA": 2}) == True

    # Consistent lowercase multi-char keys
    assert module_0.check_dict_case({"apple": 1, "banana": 2}) == True

# Generated at 2026-11-02 08:46:40.935123
# Unit test for function check_dict_case
def test_check_dict_case():
# nonce:da4404a2
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All keys uppercase -> True
    assert module_0.check_dict_case({"A": 1, "B": 2, "C": 3}) == True

    # All keys lowercase -> True
    assert module_0.check_dict_case({"a": 1, "b": 2, "c": 3}) == True

    # Single lowercase key -> True
    assert module_0.check_dict_case({"a": 1}) == True

    # Single uppercase key -> True
    assert module_0.check_dict_case({"A": 1}) == True

    # Starts lower, then upper -> mixed -> False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Starts upper, then lower -> mixed -> False
    assert module_0.check_dict_case({"A": 1, "b": 2}) == False

    # Lower, lower, upper -> mixed -> False
    assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) == False

    # Non-string key -> mixed -> False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Non-string key first -> mixed -> False
    assert module_0.check_dict_case({1: "a", "b": 2}) == False

    # Key that is neither upper nor lower (digits) breaks loop -> False
    assert module_0.check_dict_case({"123": 1}) == False

    # Uppercase start, then digit key stops loop -> False
    assert module_0.check_dict_case({"A": 1, "123": 2}) == False

    # Punctuation with lowercase letters still counts as lowercase -> True
    assert module_0.check_dict_case({"a!": 1, "b?": 2}) == True

    # Punctuation with uppercase letters still counts as uppercase -> True
    assert module_0.check_dict_case({"A!": 1, "B?": 2}) == True

    # Mixed case within keys -> False
    assert module_0.check_dict_case({"aB": 1}) == False

    # Duplicate identical keys -> True
    assert module_0.check_dict_case({"A": 1, "A": 2}) == True

# Generated at 2026-11-02 08:46:47.592027
# Unit test for function check_dict_case
def test_check_dict_case():
    # Empty dictionary should return False
    assert module_0.check_dict_case({}) == False

    # All keys uppercase should return True
    assert module_0.check_dict_case({"A": 1, "B": 2}) == True

    # All keys lowercase should return True
    assert module_0.check_dict_case({"a": 1, "b": 2}) == True

    # Mixed case keys should return False
    assert module_0.check_dict_case({"a": 1, "B": 2}) == False

    # Single uppercase key should return True
    assert module_0.check_dict_case({"A": 1}) == True

    # Single lowercase key should return True
    assert module_0.check_dict_case({"a": 1}) == True

    # Non-string key should return False
    assert module_0.check_dict_case({1: 1, "a": 2}) == False
    assert module_0.check_dict_case({"a": 1, 2: 2}) == False

    # Keys starting with mixed case pattern should return False
    assert module_0.check_dict_case({"A": 1, "b": 2, "C": 3}) == False

    # Keys with digits attached still count as upper/lower
    assert module_0.check_dict_case({"A1": 1, "B2": 2}) == True
    assert module_0.check_dict_case({"a1": 1, "b2": 2}) == True

    # Keys with no cased characters (e.g. digits only) should return False
    assert module_0.check_dict_case({"1": 1, "2": 2}) == False

    # Keys with leading/trailing punctuation but consistent case
    assert module_0.check_dict_case({"_A": 1, "_B": 2}) == True

    # Switch from upper to lower mid-dict should be False
    assert module_0.check_dict_case({"ABC": 1, "def": 2}) == False

    # Switch from lower to upper mid-dict should be False
    assert module_0.check_dict_case({"abc": 1, "DEF": 2}) == False

    print("All tests passed!")


class TestCheckDictCase(unittest.TestCase):
    def test_empty_dict(self):
        self.assertFalse(module_0.check_dict_case({}))

    def test_all_upper(self):
        self.assertTrue(module_0.check_dict_case({"A": 1, "B": 2}))

    def test_all_lower(self):
        self.assertTrue(module_0.check_dict_case({"a": 1, "b": 2}))

    def test_mixed_case(self):
        self.assertFalse(module_0.check_dict_case({"a": 1, "B": 2}))

    def test_non_string_key(self):
        self.assertFalse(module_0.check_dict_case({1: 1, "a": 2}))

    def test_single_key(self):
        self.assertTrue(module_0.check_dict_case({"A": 1}))
        self.assertTrue(module_0.check_dict_case({"a": 1}))


if __name__ == "__main__":
    test_check_dict_case()
    unittest.main()