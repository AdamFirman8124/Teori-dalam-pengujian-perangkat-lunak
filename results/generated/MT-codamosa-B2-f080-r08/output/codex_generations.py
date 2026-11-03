

# Generated at 2026-11-03 04:55:07.823676
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 characters are not happy
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 characters
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aaa") == False

    # Longer strings where all consecutive triples are distinct
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("xyza") == True

    # Longer strings with a violation somewhere
    assert module_0.is_happy("aabc") == False   # 'a' repeated in first triple
    assert module_0.is_happy("abba") == False   # 'b' repeated in middle triple
    assert module_0.is_happy("abab") == False   # 'a' repeats at positions 0 and 2
    assert module_0.is_happy("aabbcc") == False
    assert module_0.is_happy("xyy") == False

    # Violation late in the string
    assert module_0.is_happy("abcdeff") == False

    # Case sensitivity
    assert module_0.is_happy("aAa") == True
    assert module_0.is_happy("AaAa") == True

    # Non-alphabetic characters
    assert module_0.is_happy("123") == True
    assert module_0.is_happy("112") == False
    assert module_0.is_happy("!@#") == True
    assert module_0.is_happy("1!1") == False

# Generated at 2026-11-03 04:57:02.598131
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 should return False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Simple happy strings
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("aabbccdd") == False  # adjacent duplicates

    # Non-happy due to adjacent duplicates
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aaa") == False

    # Non-happy due to s[i] == s[i+2]
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("xyxy") == False

    # Longer happy strings
    assert module_0.is_happy("abcdef") == True
    assert module_0.is_happy("abcde") == True

    # Longer non-happy strings
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("abcdabc") == False  # "abc","bcd","cda","dab","abc" - check

    # Edge case: exactly 3 chars
    assert module_0.is_happy("xyz") == True
    assert module_0.is_happy("xxa") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_happy()

# Generated at 2026-11-03 04:59:42.996945
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 should return False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("aa") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 distinct characters -> happy
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyz") == True

    # Exactly 3 with a repeat -> not happy
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("xyy") == False

    # Longer strings where every window of 3 has distinct chars -> happy
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("xyzw") == True

    # Longer strings with a repeat somewhere in a window -> not happy
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abab") == False
    assert module_0.is_happy("abca") == False  # window "bca" ok, but "abc","bca"... check "aca"? no—'a' repeats at start/end
    assert module_0.is_happy("aabbcc") == False
    assert module_0.is_happy("abcdd") == False

    # Case sensitivity: different cases are distinct characters
    assert module_0.is_happy("aAbB") == True
    assert module_0.is_happy("aAa") == False

    print("All tests passed!")

# Generated at 2026-11-03 05:01:55.987073
# Unit test for function is_happy
def test_is_happy():
    # Strings shorter than 3 should return False
    assert module_0.is_happy("") == False
    assert module_0.is_happy("a") == False
    assert module_0.is_happy("ab") == False

    # Exactly 3 distinct characters -> happy
    assert module_0.is_happy("abc") == True
    assert module_0.is_happy("adb") == True
    assert module_0.is_happy("xyz") == True

    # Exactly 3 characters with a repeat -> not happy
    assert module_0.is_happy("aab") == False
    assert module_0.is_happy("aba") == False
    assert module_0.is_happy("abb") == False
    assert module_0.is_happy("aaa") == False

    # Longer strings where every window of 3 is distinct
    assert module_0.is_happy("abcd") == True
    assert module_0.is_happy("abcabc") == True
    assert module_0.is_happy("abcdef") == True

    # Longer strings with a repeat somewhere
    assert module_0.is_happy("aabb") == False
    assert module_0.is_happy("abab") == False
    assert module_0.is_happy("xyy") == False
    assert module_0.is_happy("abcba") == False
    assert module_0.is_happy("abcda") == False  # "cda" ok but "bcd" ok... check: b,c,d / c,d,a all distinct -> True
    # Correcting expectation for "abcda": windows abc, bcd, cda all distinct
    assert module_0.is_happy("abcda") == True

    # Case sensitivity: 'A' and 'a' are different characters
    assert module_0.is_happy("aAb") == True
    assert module_0.is_happy("aAa") == False