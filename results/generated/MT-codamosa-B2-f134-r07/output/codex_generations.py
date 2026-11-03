

# Generated at 2026-11-02 22:01:31.965893
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single lowercase letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("hello worl d") == True

    # Last word is a single uppercase letter (lowercased internally) -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi E") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word has more than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False

    # Empty string -> False
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Trailing spaces: last split token is empty -> False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e  ") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False

    # Single non-letter characters -> False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("-") == False

    # Single non-ASCII character (ord outside 97..122) -> False
    assert module_0.check_if_last_char_is_a_letter("hello é") == False


if __name__ == "__main__":
    test_check_if_last_char_is_a_letter()
    print("All tests passed!")

# Generated at 2026-11-02 22:04:48.376529
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("hello world 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello world !") == False
    assert module_0.check_if_last_char_is_a_letter("hello world e1") == False
    assert module_0.check_if_last_char_is_a_letter("   ") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False

# Generated at 2026-11-02 22:08:12.365932
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single letter -> True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True
    assert module_0.check_if_last_char_is_a_letter("apple pie e") == True
    assert module_0.check_if_last_char_is_a_letter("hello world d") == True

    # Last word is longer than one character -> False
    assert module_0.check_if_last_char_is_a_letter("hello") == False
    assert module_0.check_if_last_char_is_a_letter("ab") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("a bc") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hello 3") == False
    assert module_0.check_if_last_char_is_a_letter("hello ?") == False

    # Empty string and trailing space -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("a ") == False

    # Multiple spaces between words, last word single letter -> True
    assert module_0.check_if_last_char_is_a_letter("a  b") == True