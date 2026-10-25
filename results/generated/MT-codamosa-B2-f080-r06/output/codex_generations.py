

# Generated at 2026-10-24 12:18:53.390179
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

# Generated at 2026-10-24 12:18:54.717535
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

# Generated at 2026-10-24 12:18:56.031378
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

# Generated at 2026-10-24 12:18:57.346914
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

# Generated at 2026-10-24 12:18:58.683453
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