

# Generated at 2026-10-24 11:26:31.890875
# Unit test for function is_happy
def test_is_happy():
    # too short -> False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # happy: every length-3 window has 3 distinct chars
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abca") == True
    assert module_0.is_happy("abcab") == True
    assert module_0.is_happy("abcdefgh") == True

    # unhappy: duplicate in window
    assert module_0.is_happy("aaa") == False  # s[i] == s[i+1]
    assert module_0.is_happy("aab") == False  # first two equal
    assert module_0.is_happy("abb") == False  # last two equal
    assert module_0.is_happy("aba") == False  # s[i] == s[i+2]
    assert module_0.is_happy("abcc") == False
    assert module_0.is_happy("aabc") == False
    assert module_0.is_happy("ababa") == False

# Generated at 2026-10-24 11:26:49.863987
# Unit test for function is_happy
def test_is_happy():
    # length < 3 always False
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # length 3
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("aba") is False   # first == third
    assert module_0.is_happy("abb") is False
    assert module_0.is_happy("aaa") is False

    # longer, happy
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcabc") is True
    assert module_0.is_happy("abcdefg") is True

    # longer, one window fails
    assert module_0.is_happy("abcc") is False    # "bcc"
    assert module_0.is_happy("aabc") is False    # "aab"
    assert module_0.is_happy("abcaa") is False   # "caa"
    assert module_0.is_happy("xyzyy") is False   # "zyy"
    assert module_0.is_happy("abac") is False    # "aba"


if __name__ == "__main__":
    test_is_happy()
    print("all tests passed")

# Generated at 2026-10-24 11:26:51.190654
# Unit test for function is_happy
def test_is_happy():
    # length < 3 always False
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # length 3
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("aba") is False   # first == third
    assert module_0.is_happy("abb") is False
    assert module_0.is_happy("aaa") is False

    # longer, happy
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcabc") is True
    assert module_0.is_happy("abcdefg") is True

    # longer, one window fails
    assert module_0.is_happy("abcc") is False    # "bcc"
    assert module_0.is_happy("aabc") is False    # "aab"
    assert module_0.is_happy("abcaa") is False   # "caa"
    assert module_0.is_happy("xyzyy") is False   # "zyy"
    assert module_0.is_happy("abac") is False    # "aba"


if __name__ == "__main__":
    test_is_happy()
    print("all tests passed")

# Generated at 2026-10-24 11:26:52.510088
# Unit test for function is_happy
def test_is_happy():
    # length < 3 always False
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # length 3
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("aba") is False   # first == third
    assert module_0.is_happy("abb") is False
    assert module_0.is_happy("aaa") is False

    # longer, happy
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcabc") is True
    assert module_0.is_happy("abcdefg") is True

    # longer, one window fails
    assert module_0.is_happy("abcc") is False    # "bcc"
    assert module_0.is_happy("aabc") is False    # "aab"
    assert module_0.is_happy("abcaa") is False   # "caa"
    assert module_0.is_happy("xyzyy") is False   # "zyy"
    assert module_0.is_happy("abac") is False    # "aba"


if __name__ == "__main__":
    test_is_happy()
    print("all tests passed")

# Generated at 2026-10-24 11:26:53.841244
# Unit test for function is_happy
def test_is_happy():
    # length < 3 always False
    assert module_0.is_happy("") is False
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("ab") is False

    # length 3
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("aba") is False   # first == third
    assert module_0.is_happy("abb") is False
    assert module_0.is_happy("aaa") is False

    # longer, happy
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("abcabc") is True
    assert module_0.is_happy("abcdefg") is True

    # longer, one window fails
    assert module_0.is_happy("abcc") is False    # "bcc"
    assert module_0.is_happy("aabc") is False    # "aab"
    assert module_0.is_happy("abcaa") is False   # "caa"
    assert module_0.is_happy("xyzyy") is False   # "zyy"
    assert module_0.is_happy("abac") is False    # "aba"


if __name__ == "__main__":
    test_is_happy()
    print("all tests passed")