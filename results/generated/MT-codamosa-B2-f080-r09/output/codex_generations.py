

# Generated at 2026-10-24 12:11:23.433046
# Unit test for function is_happy

# Generated at 2026-10-24 12:11:25.851594
# Unit test for function is_happy

# Generated at 2026-10-24 12:11:28.270211
# Unit test for function is_happy

# Generated at 2026-10-24 12:11:30.692678
# Unit test for function is_happy

# Generated at 2026-10-24 12:11:33.114308
# Unit test for function is_happy

# Generated at 2026-10-24 12:11:40.481861
# Unit test for function is_happy
def test_is_happy():
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("ab") == False
    assert module_0.is_happy("xyzt") == True

# Generated at 2026-10-24 12:11:41.794690
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

# Generated at 2026-10-24 12:11:43.116562
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

# Generated at 2026-10-24 12:11:44.517436
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