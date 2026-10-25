

# Generated at 2026-10-24 19:23:11.678895
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 19:23:12.998747
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 19:23:14.316207
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 19:23:15.690034
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails

# Generated at 2026-10-24 19:23:17.005036
# Unit test for function is_happy
def test_is_happy():
    # Too short
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # Happy: every 3-char window has distinct characters
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcab") is True
    assert module_0.is_happy("abca") is True  # repeat at distance 3 is allowed

    # Not happy: repeat within a 3-char window
    assert module_0.is_happy("aab") is False   # s[0] == s[1]
    assert module_0.is_happy("abb") is False   # s[1] == s[2]
    assert module_0.is_happy("aba") is False   # s[0] == s[2]
    assert module_0.is_happy("abcc") is False  # later window fails
    assert module_0.is_happy("abcb") is False  # later window fails