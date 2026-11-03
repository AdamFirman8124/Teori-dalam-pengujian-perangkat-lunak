

# Generated at 2026-11-02 12:20:46.886955
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single letter
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("hello worl d") == True
    assert module_0.check_if_last_char_is_a_letter("hi there Q") == True

    # Last word is a single non-letter character
    assert module_0.check_if_last_char_is_a_letter("apple pi e 1") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hi there 5") == False

    # Last word has more than one character
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e!") == False
    assert module_0.check_if_last_char_is_a_letter("ab") == False
    assert module_0.check_if_last_char_is_a_letter("!!!") == False

    # Empty string / trailing space cases
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("hello ") == False

    # Single letter preceded by spaces
    assert module_0.check_if_last_char_is_a_letter("  e") == True
    assert module_0.check_if_last_char_is_a_letter("   7") == False

# Generated at 2026-11-02 12:21:31.623440
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single lowercase letter as the last word
    assert module_0.check_if_last_char_is_a_letter("apple b") == True
    assert module_0.check_if_last_char_is_a_letter("hello a") == True

    # Single uppercase letter as the last word (lowered internally)
    assert module_0.check_if_last_char_is_a_letter("apple Z") == True
    assert module_0.check_if_last_char_is_a_letter("apple Q") == True

    # Multi-character last word
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple ba") == False

    # Last word is a digit
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False

    # Last word is a special character
    assert module_0.check_if_last_char_is_a_letter("apple !") == False
    assert module_0.check_if_last_char_is_a_letter("apple @") == False

    # Trailing space -> last split token is empty string
    assert module_0.check_if_last_char_is_a_letter("apple b ") == False

    # Empty string
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Only a single letter in the string
    assert module_0.check_if_last_char_is_a_letter("a") == True

    # Multiple spaces between words
    assert module_0.check_if_last_char_is_a_letter("apple  z") == True

    # Multiple words ending with a single letter
    assert module_0.check_if_last_char_is_a_letter("a b c") == True

# Generated at 2026-11-02 12:22:18.594848
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single letter at end
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("hello worl d") == True

    # Multi-character last word
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e1") == False

    # Non-letter single character
    assert module_0.check_if_last_char_is_a_letter("hello world !") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("hello 2") == False

    # Trailing space / empty cases
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Leading spaces still isolate last word
    assert module_0.check_if_last_char_is_a_letter("   a") == True

    # Punctuation attached to last word
    assert module_0.check_if_last_char_is_a_letter("hello!") == False

    print("All tests passed!")


test_check_if_last_char_is_a_letter()

# Generated at 2026-11-02 12:23:18.535567
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single letter -> True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("hello worl d") == True
    assert module_0.check_if_last_char_is_a_letter("x y") == True

    # Uppercase single letter -> True
    assert module_0.check_if_last_char_is_a_letter("hello Z") == True
    assert module_0.check_if_last_char_is_a_letter("Q") == True

    # Last word has more than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("e apple") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("number 5") == False
    assert module_0.check_if_last_char_is_a_letter("hello ?") == False

    # Trailing space makes last token empty -> False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("a ") == False

    # Empty string -> False
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Multi-character non-alphabetic token -> False
    assert module_0.check_if_last_char_is_a_letter("hello !!") == False
    assert module_0.check_if_last_char_is_a_letter("hello 42") == False

# Generated at 2026-11-02 12:24:29.382751
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single letter as the only word -> True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word is a single letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("hello A") == True
    assert module_0.check_if_last_char_is_a_letter("unit z") == True

    # Last word is longer than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello ab") == False
    assert module_0.check_if_last_char_is_a_letter("pumpkin pie") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e1") == False
    assert module_0.check_if_last_char_is_a_letter("chart ?") == False

    # Empty string and trailing whitespace -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie ") == False

    # Non-ASCII letter is not in the a-z range -> False
    assert module_0.check_if_last_char_is_a_letter("hello é") == False


if __name__ == "__main__":
    test_check_if_last_char_is_a_letter()
    print("All tests passed!")