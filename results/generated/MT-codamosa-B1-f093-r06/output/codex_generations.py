

# Generated at 2026-10-25 06:14:55.300785
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Swapcase + vowel shift: lowercase vowels became uppercase, then shift +2
    assert module_0.encode("I DO") == "k dq"
    #   "I DO" -> swapcase "i do" -> 'i'->'k', 'o'->'q'

    assert module_0.encode("YES") == "ygs"
    #   "YES" -> "yes" -> 'e'->'g'

    # Uppercase vowels after swapcase are lowercase originals, shifted +2
    assert module_0.encode("aeiou") == "CGKQW"
    #   "aeiou" -> "AEIOU" -> 'A'->'C', 'E'->'G', 'I'->'K', 'O'->'Q', 'U'->'W'

    assert module_0.encode("AEIOU") == "cgkqw"
    #   "AEIOU" -> "aeiou" -> +2 each

    # Consonants only swap case
    assert module_0.encode("goodbye") == "GQQDBYG"
    #   "goodbye" -> "GOODBYE" -> 'O'->'Q', 'E'->'G'

    # Non-letters untouched
    assert module_0.encode("123!@# a") == "123!@# C"

    # Mixed content
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    #   "Hello World" -> "hELLO wORLD" -> 'E'->'G', 'O'->'Q'

    print("All encode tests passed.")


if __name__ == "__main__":
    test_encode()

# Generated at 2026-10-25 06:14:56.633683
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Swapcase + vowel shift: lowercase vowels became uppercase, then shift +2
    assert module_0.encode("I DO") == "k dq"
    #   "I DO" -> swapcase "i do" -> 'i'->'k', 'o'->'q'

    assert module_0.encode("YES") == "ygs"
    #   "YES" -> "yes" -> 'e'->'g'

    # Uppercase vowels after swapcase are lowercase originals, shifted +2
    assert module_0.encode("aeiou") == "CGKQW"
    #   "aeiou" -> "AEIOU" -> 'A'->'C', 'E'->'G', 'I'->'K', 'O'->'Q', 'U'->'W'

    assert module_0.encode("AEIOU") == "cgkqw"
    #   "AEIOU" -> "aeiou" -> +2 each

    # Consonants only swap case
    assert module_0.encode("goodbye") == "GQQDBYG"
    #   "goodbye" -> "GOODBYE" -> 'O'->'Q', 'E'->'G'

    # Non-letters untouched
    assert module_0.encode("123!@# a") == "123!@# C"

    # Mixed content
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    #   "Hello World" -> "hELLO wORLD" -> 'E'->'G', 'O'->'Q'

    print("All encode tests passed.")


if __name__ == "__main__":
    test_encode()

# Generated at 2026-10-25 06:14:58.128956
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Swapcase + vowel shift: lowercase vowels became uppercase, then shift +2
    assert module_0.encode("I DO") == "k dq"
    #   "I DO" -> swapcase "i do" -> 'i'->'k', 'o'->'q'

    assert module_0.encode("YES") == "ygs"
    #   "YES" -> "yes" -> 'e'->'g'

    # Uppercase vowels after swapcase are lowercase originals, shifted +2
    assert module_0.encode("aeiou") == "CGKQW"
    #   "aeiou" -> "AEIOU" -> 'A'->'C', 'E'->'G', 'I'->'K', 'O'->'Q', 'U'->'W'

    assert module_0.encode("AEIOU") == "cgkqw"
    #   "AEIOU" -> "aeiou" -> +2 each

    # Consonants only swap case
    assert module_0.encode("goodbye") == "GQQDBYG"
    #   "goodbye" -> "GOODBYE" -> 'O'->'Q', 'E'->'G'

    # Non-letters untouched
    assert module_0.encode("123!@# a") == "123!@# C"

    # Mixed content
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    #   "Hello World" -> "hELLO wORLD" -> 'E'->'G', 'O'->'Q'

    print("All encode tests passed.")


if __name__ == "__main__":
    test_encode()

# Generated at 2026-10-25 06:14:59.465351
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Swapcase + vowel shift: lowercase vowels became uppercase, then shift +2
    assert module_0.encode("I DO") == "k dq"
    #   "I DO" -> swapcase "i do" -> 'i'->'k', 'o'->'q'

    assert module_0.encode("YES") == "ygs"
    #   "YES" -> "yes" -> 'e'->'g'

    # Uppercase vowels after swapcase are lowercase originals, shifted +2
    assert module_0.encode("aeiou") == "CGKQW"
    #   "aeiou" -> "AEIOU" -> 'A'->'C', 'E'->'G', 'I'->'K', 'O'->'Q', 'U'->'W'

    assert module_0.encode("AEIOU") == "cgkqw"
    #   "AEIOU" -> "aeiou" -> +2 each

    # Consonants only swap case
    assert module_0.encode("goodbye") == "GQQDBYG"
    #   "goodbye" -> "GOODBYE" -> 'O'->'Q', 'E'->'G'

    # Non-letters untouched
    assert module_0.encode("123!@# a") == "123!@# C"

    # Mixed content
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    #   "Hello World" -> "hELLO wORLD" -> 'E'->'G', 'O'->'Q'

    print("All encode tests passed.")


if __name__ == "__main__":
    test_encode()

# Generated at 2026-10-25 06:15:02.224474
# Unit test for function encode

# Generated at 2026-10-25 06:15:04.733775
# Unit test for function encode

# Generated at 2026-10-25 06:15:07.061100
# Unit test for function encode