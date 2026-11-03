

# Generated at 2026-11-01 20:25:50.102867
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # nonce:e9c9fc2a
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("apple b") == True
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello Z") == True
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False

test_check_if_last_char_is_a_letter()

# Generated at 2026-11-01 20:26:21.744097
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
# nonce:04ab0b8a
    # Last token is a single lowercase letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("hello world a") == True
    assert module_0.check_if_last_char_is_a_letter("I am a i") == True

    # Single uppercase letter -> True (lowered before check)
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("foo bar Z") == True

    # Boundary alphabet characters 'a' and 'z'
    assert module_0.check_if_last_char_is_a_letter("x y z") == True
    assert module_0.check_if_last_char_is_a_letter("q w a") == True

    # Characters just outside the letter range
    assert module_0.check_if_last_char_is_a_letter("a b `") == False   # ord 96
    assert module_0.check_if_last_char_is_a_letter("a b {") == False   # ord 123

    # Digits and symbols are not letters
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hi !") == False
    assert module_0.check_if_last_char_is_a_letter("test @") == False

    # Last token longer than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("I am ai") == False
    assert module_0.check_if_last_char_is_a_letter("hello world!") == False

    # Empty string and trailing whitespace -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("z ") == False

    # Multiple consecutive spaces: last non-empty token counts
    assert module_0.check_if_last_char_is_a_letter("a  b") == True
    assert module_0.check_if_last_char_is_a_letter("a  bc") == False

    # Mixed case within words
    assert module_0.check_if_last_char_is_a_letter("Hello World") == False
    assert module_0.check_if_last_char_is_a_letter("Hello Worl d") == True

# Generated at 2026-11-01 20:27:02.711646
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single letter
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True
    assert module_0.check_if_last_char_is_a_letter("hello A") == True
    assert module_0.check_if_last_char_is_a_letter("a b c") == True

    # Last word longer than one character
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("a b cd") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e1") == False

    # Single character that is not a letter
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hello 7") == False
    assert module_0.check_if_last_char_is_a_letter("x!") == False

    # Trailing spaces and empty strings
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False

    print("All tests passed!")


test_check_if_last_char_is_a_letter()

# Generated at 2026-11-01 20:27:35.886020
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
# nonce:eb821f08
    # Single character letters
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Canonical examples
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Last token is a single letter after a space
    assert module_0.check_if_last_char_is_a_letter("apple a") == True
    assert module_0.check_if_last_char_is_a_letter("apple A") == True
    assert module_0.check_if_last_char_is_a_letter("hello world q") == True
    assert module_0.check_if_last_char_is_a_letter("hello world Q") == True

    # Last token is longer than one character
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("ab") == False
    assert module_0.check_if_last_char_is_a_letter("AB") == False
    assert module_0.check_if_last_char_is_a_letter("a1") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e1") == False

    # Single non-letter characters
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("@") == False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("hello -") == False

    # Boundary characters just outside a-z range
    assert module_0.check_if_last_char_is_a_letter("`") == False  # ord 96
    assert module_0.check_if_last_char_is_a_letter("{") == False  # ord 123

    # Empty and whitespace edge cases
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("   ") == False
    assert module_0.check_if_last_char_is_a_letter("a ") == False
    assert module_0.check_if_last_char_is_a_letter(" a") == True
    assert module_0.check_if_last_char_is_a_letter("a  b") == True
    assert module_0.check_if_last_char_is_a_letter("  a") == True
    assert module_0.check_if_last_char_is_a_letter("pumpkin pie ") == False

# Generated at 2026-11-01 20:27:52.410374
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Last word is a single lowercase letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pie b") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True

    # Last word is a single uppercase letter -> True (lower() applied)
    assert module_0.check_if_last_char_is_a_letter("apple pie B") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word has more than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie bc") == False
    assert module_0.check_if_last_char_is_a_letter("hello") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie 1") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie !") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False

    # Empty string -> False
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Trailing spaces make the last split token empty -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie ") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False