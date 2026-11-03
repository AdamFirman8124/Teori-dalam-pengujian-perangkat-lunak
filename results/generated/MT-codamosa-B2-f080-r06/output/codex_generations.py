

# Generated at 2026-11-02 15:02:04.542277
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 distinct characters is happy
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("xyz") == True
    assert module_0.is_happy("a b") == True

    # Longer strings where every window of 3 has distinct chars
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("abcbab") == True

    # Strings with repeated characters within any window of 3
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("xxz") == False
    assert module_0.is_happy("xyx") == False
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aaabcd") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False

    # Repeats later in the string should fail
    assert module_0.is_happy("abcabcd") == False
    assert module_0.is_happy("abcabc") == True  # each window abc, bca, cab, abc all distinct

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.is_happy("aAa") == True
    assert module_0.is_happy("AaA") == True

# Generated at 2026-11-02 15:02:55.128513
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aaa") == False

    # Every window of 3 consecutive chars must be distinct
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("adbbd") == False
    assert module_0.is_happy("xyzy") == False

    # Longer strings
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abcab") == True
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("abcc") == False
    assert module_0.is_happy("abcdefg") == True
    assert module_0.is_happy("abcdeefg") == False

    # Case sensitivity: 'a' and 'A' are distinct characters
    assert module_0.is_happy("aAbB") == True
    assert module_0.is_happy("aAa") == False

    # Digits and mixed characters
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("1a2b3c") == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-02 15:05:55.051501
# Unit test for function is_happy

# Generated at 2026-11-02 15:09:11.476816
# Unit test for function is_happy
def test_is_happy():
    assert module_0.is_happy("a") is False
    assert module_0.is_happy("aa") is False
    assert module_0.is_happy("") is False
    assert module_0.is_happy("ab") is False
    assert module_0.is_happy("abc") is True
    assert module_0.is_happy("xyz") is True
    assert module_0.is_happy("xyy") is False
    assert module_0.is_happy("aab") is False
    assert module_0.is_happy("aba") is False
    assert module_0.is_happy("abcd") is True
    assert module_0.is_happy("aabb") is False
    assert module_0.is_happy("adb") is True
    assert module_0.is_happy("abcabc") is True
    assert module_0.is_happy("abca") is True
    assert module_0.is_happy("xyzz") is False
    assert module_0.is_happy("aaa") is False
    assert module_0.is_happy("aabbcc") is False
    assert module_0.is_happy("abcdef") is True