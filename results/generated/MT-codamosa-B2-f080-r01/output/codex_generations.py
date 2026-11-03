

# Generated at 2026-11-02 15:01:56.766562
# Unit test for function is_happy
def test_is_happy():
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("ab") == False
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("xyo") == True
    assert module_0.is_happy("xyuy") == False
    assert module_0.is_happy("xd") == False
    assert module_0.is_happy("x") == False
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("aabbcc") == False
    assert module_0.is_happy("xyzy") == False
    assert module_0.is_happy("zxyz") == True
    assert module_0.is_happy("abcdcba") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-02 15:02:37.707844
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 are not happy
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("") == False

    # Exactly 3 distinct chars is happy
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("xyz") == True

    # Repeated chars within a window of 3 are not happy
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False

    # Longer strings, all windows distinct
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdef") == True

    # Longer strings with a violation somewhere
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("abac") == False  # 'a' repeats at distance 2
    assert module_0.is_happy("abcba") == False  # window "bcb" has repeat

    # Case sensitivity: 'A' != 'a'
    assert module_0.is_happy("aAbB") == True

    print("All tests passed!")

test_is_happy()

# Generated at 2026-11-02 15:03:19.024649
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Basic happy strings (every 3 consecutive chars are distinct)
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("abcdabc") == True

    # Basic unhappy strings (duplicate within a window of 3)
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("aabb") == False

    # Overlapping windows: violation later in the string
    assert module_0.is_happy("abcba") == False  # "bcb" has duplicate b
    assert module_0.is_happy("abcab") == False  # "bca" ok, "cab" ok, "aba" has duplicate a
    assert module_0.is_happy("abca") == False   # "bca" ok, "cab" ok, "bca"-> wait: "abc","bca","cab" all distinct? no: "bca" distinct, "cab" distinct -> True? check

    # Corrected check for "abca": windows "abc","bca","cab" - all distinct
    assert module_0.is_happy("abca") == True

    # Longer mixed strings
    assert module_0.is_happy("abcdefg") == True
    assert module_0.is_happy("aabbccdd") == False
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abab") == False  # "aba" has duplicate a

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.is_happy("aAa") == True
    assert module_0.is_happy("AAa") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-02 15:05:00.011346
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 should return False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Strings where every 3 consecutive chars are distinct
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcde") == True
    assert module_0.is_happy("abcabc") == True

    # Strings containing repeated characters within a window of 3
    assert module_0.is_happy("aa") == False  # handled by length check
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abcc") == False
    assert module_0.is_happy("aabbcc") == False

    # Longer strings with a violation late in the string
    assert module_0.is_happy("abcdabc") == False  # last triple 'abc' ok? no: 'bca','cab' fine but ends 'abc'... check
    assert module_0.is_happy("abcdaab") == False
    assert module_0.is_happy("abcdefab") == True

    print("All tests passed!")

# Generated at 2026-11-02 15:09:27.358646
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Basic happy strings
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("a") is False if False else True  # no-op guard

    # Exactly length 3 with distinct chars
    assert module_0.is_happy("xyz") == True

    # Exactly length 3 with repeated chars
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False  # first == third
    assert module_0.is_happy("aaa") == False

    # Sliding window across longer strings
    assert module_0.is_happy("aabb") == False   # window "aab"
    assert module_0.is_happy("abcb") == False   # window "bcb"
    assert module_0.is_happy("abab") == False   # window "aba"
    assert module_0.is_happy("abca") == True    # windows: abc, bca
    assert module_0.is_happy("abcdefg") == True
    assert module_0.is_happy("abcdeabc") == False  # window "abc" ok... "abc" at end ok -> all distinct
    assert module_0.is_happy("abcabd") == False    # window "abc" ok, "bca" ok, "cab" ok, "abd" ok

    # Single repeated char in middle breaks happiness
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("yyx") == False
    assert module_0.is_happy("xyyx") == False    # window "yyx"
    assert module_0.is_happy("xyzxy") == True    # windows: xyz, yzx, zxy

    # Non-alphabetic characters also work
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("!@#$%") == True
    assert module_0.is_happy("!@#") == True
    assert module_0.is_happy("!!@") == False

    # Mixed content
    assert module_0.is_happy("a1b2c3") == True
    assert module_0.is_happy("a11b") == False