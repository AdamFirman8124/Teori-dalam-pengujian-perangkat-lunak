

# Generated at 2026-11-02 16:31:19.783779
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single-letter last word returns True (case insensitive)
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("apple pie b") == True
    assert module_0.check_if_last_char_is_a_letter("hello Z") == True
    assert module_0.check_if_last_char_is_a_letter("a b c") == True
    assert module_0.check_if_last_char_is_a_letter(" b") == True

    # Multi-character last word returns False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi") == False
    assert module_0.check_if_last_char_is_a_letter("APPLE") == False
    assert module_0.check_if_last_char_is_a_letter("apple B2") == False

    # Single non-letter last word returns False
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("apple !") == False
    assert module_0.check_if_last_char_is_a_letter("apple ?") == False
    assert module_0.check_if_last_char_is_a_letter("apple _") == False
    assert module_0.check_if_last_char_is_a_letter("apple {") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False

    # Empty string and trailing-space edge cases
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("a ") == False
    assert module_0.check_if_last_char_is_a_letter("apple b ") == False

    # Multiple spaces still find the last token
    assert module_0.check_if_last_char_is_a_letter("a  b") == True
    assert module_0.check_if_last_char_is_a_letter("a   ") == False

# Generated at 2026-11-02 16:32:12.641224
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single lowercase letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pie a") is True
    assert module_0.check_if_last_char_is_a_letter("hello b") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("x y z") is True

    # Uppercase single letter (lowered internally) -> True
    assert module_0.check_if_last_char_is_a_letter("apple B") is True
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("test Z") is True

    # Last word has more than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("hello world") is False

    # Single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("apple 1") is False
    assert module_0.check_if_last_char_is_a_letter("apple !") is False
    assert module_0.check_if_last_char_is_a_letter("apple ?") is False
    assert module_0.check_if_last_char_is_a_letter("apple -") is False

    # Empty string and trailing whitespace -> False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter(" ") is False
    assert module_0.check_if_last_char_is_a_letter("apple ") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie  ") is False

    # Boundary letters of the alphabet
    assert module_0.check_if_last_char_is_a_letter("end z") is True
    assert module_0.check_if_last_char_is_a_letter("start a") is True

# nonce:bba4cacc

# Generated at 2026-11-02 16:33:23.362250
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single letter words -> True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word is a single letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple b") == True
    assert module_0.check_if_last_char_is_a_letter("hello world a") == True
    assert module_0.check_if_last_char_is_a_letter("a  b") == True  # multiple spaces

    # Last word has multiple characters -> False
    assert module_0.check_if_last_char_is_a_letter("ab") == False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False

    # Empty string and trailing spaces -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("a ") == False
    assert module_0.check_if_last_char_is_a_letter("apple ") == False

    # Non-ASCII single characters -> False
    assert module_0.check_if_last_char_is_a_letter("é") == False
    assert module_0.check_if_last_char_is_a_letter("apple é") == False

    print("All tests passed!")

# Generated at 2026-11-02 16:34:30.720919
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # nonce:a801b758
    # Last token is a single letter
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("hello world d") == True
    assert module_0.check_if_last_char_is_a_letter("a b") == True

    # Uppercase single letter is still a letter
    assert module_0.check_if_last_char_is_a_letter("Z") == True
    assert module_0.check_if_last_char_is_a_letter("a B") == True

    # Last token is a word longer than one char
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("ab") == False

    # Last token is a digit or symbol
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("a 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello!") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie!") == False

    # Empty / trailing space cases
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("hello! ") == False

# Generated at 2026-11-02 16:35:46.885803
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # nonce:3bcf1f25
    # Single alphabetic character as last token -> True
    assert module_0.check_if_last_char_is_a_letter("apple b") == True
    assert module_0.check_if_last_char_is_a_letter("apple B") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True
    assert module_0.check_if_last_char_is_a_letter("hello worl d") == True

    # Multi-character last token -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("b apple") == False

    # Single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("apple !") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("@") == False
    assert module_0.check_if_last_char_is_a_letter("apple {") == False

    # Punctuation attached to last word -> False
    assert module_0.check_if_last_char_is_a_letter("hello world!") == False

    # Empty string and whitespace edge cases -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("apple b ") == False  # trailing space -> last token is ""

    # Multiple spaces between words -> True (last token is still single letter)
    assert module_0.check_if_last_char_is_a_letter("apple  b") == True

    # Non-ASCII single character -> False (ord outside a-z range)
    assert module_0.check_if_last_char_is_a_letter("apple é") == False

    # Tab-separated (not split by space) -> False
    assert module_0.check_if_last_char_is_a_letter("apple\tb") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_check_if_last_char_is_a_letter()