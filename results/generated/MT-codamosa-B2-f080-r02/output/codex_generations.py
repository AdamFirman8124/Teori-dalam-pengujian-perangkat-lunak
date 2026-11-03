

# Generated at 2026-11-03 00:22:41.573039
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Valid happy strings: every 3 consecutive chars are distinct
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("xyzabc") == True

    # Adjacent duplicates anywhere make it unhappy
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aaa") == False

    # Non-adjacent duplicates within a window make it unhappy
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abcb") == False

    # A repeat after the first window still fails
    assert module_0.is_happy("abcdabc") == True
    assert module_0.is_happy("abcabd") == False

    # Longer happy string
    assert module_0.is_happy("abcdef") == True

    # Mixed case characters are distinct
    assert module_0.is_happy("aAbB") == True

    # Single character repeated at distance 2
    assert module_0.is_happy("aba") == False

    print("All test_is_happy tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-03 00:24:56.610982
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 should return False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False
    assert module_0.is_happy("aa") == False

    # Exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False  # first and last of triple equal

    # Longer strings
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdefg") == True
    assert module_0.is_happy("xyzt") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("adbbd") == False
    assert module_0.is_happy("abcba") == False  # "bcb" window fails
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abca") == True
    assert module_0.is_happy("aabbcc") == False
    assert module_0.is_happy("aabccc") == False
    assert module_0.is_happy("abab") == False  # "aba" window: s[0]==s[2]

    # Case sensitivity
    assert module_0.is_happy("aAb") == True
    assert module_0.is_happy("aAa") == False

    # Non-letter characters
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("!@#") == True
    assert module_0.is_happy("1!1") == False

    print("All test_is_happy tests passed!")

test_is_happy()

# Generated at 2026-11-03 00:25:52.621614
# Unit test for function is_happy
def test_is_happy():
    # Test strings shorter than 3 characters
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Test strings with exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aba") == False

    # Test longer happy strings (all distinct consecutive triples)
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("adbbd") == False
    assert module_0.is_happy("xyzy") == False
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("banana") == False

    # Test strings with repeated characters at various positions
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abba") == False
    assert module_0.is_happy("abab") == False
    assert module_0.is_happy("abcabc") == True

    # Test with non-alphabetic characters
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("!@#") == True
    assert module_0.is_happy("!!@") == False

    # Test case sensitivity
    assert module_0.is_happy("aAa") == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-03 00:27:02.880168
# Unit test for function is_happy
def test_is_happy():
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("ab") == False
    assert module_0.is_happy("abcdabc") == True
    assert module_0.is_happy("aabc") == False
    assert module_0.is_happy("abca") == True
    assert module_0.is_happy("abab") == False
    assert module_0.is_happy("xyzy") == True
    assert module_0.is_happy("aabbcc") == False
    assert module_0.is_happy("abcdefg") == True

# Generated at 2026-11-03 00:28:20.591010
# Unit test for function is_happy
def test_is_happy():
# nonce:2bdc5bf4
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("aaa") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("adb") == True

    # Longer strings where every window of 3 has distinct characters
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("aabbcc") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()