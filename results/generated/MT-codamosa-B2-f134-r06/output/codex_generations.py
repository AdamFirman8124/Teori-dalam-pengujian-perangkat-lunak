

# Generated at 2026-11-02 21:21:42.451186
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single-letter last word (lowercase)
    assert module_0.check_if_last_char_is_a_letter("apple a") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True

    # Single-letter last word (uppercase, lowered before check)
    assert module_0.check_if_last_char_is_a_letter("apple A") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True

    # Multi-character last word -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("ab") == False

    # Single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("?") == False

    # Empty string and trailing space -> last token is empty -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("apple ") == False

    # Multiple spaces: last non-empty token is still isolated
    assert module_0.check_if_last_char_is_a_letter("a  b") == True

    # Tab is not a split delimiter, so last token length > 1
    assert module_0.check_if_last_char_is_a_letter("a\tb") == False

    # Non-ASCII single character outside a-z range
    assert module_0.check_if_last_char_is_a_letter("apple é") == False


if __name__ == "__main__":
    test_check_if_last_char_is_a_letter()
    print("All tests passed!")

# Generated at 2026-11-02 21:23:14.555735
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # nonce:f86d1f56
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("p") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("apple e") == True
    assert module_0.check_if_last_char_is_a_letter("apple  e") == True
    assert module_0.check_if_last_char_is_a_letter("apple E") == True
    assert module_0.check_if_last_char_is_a_letter("apple Z") == True
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("apple !") == False
    assert module_0.check_if_last_char_is_a_letter("apple .") == False
    assert module_0.check_if_last_char_is_a_letter("apple @") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("apple banana") == False

# Generated at 2026-11-02 21:25:14.412169
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # nonce:6221bbde

    # Last word is a single lowercase letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True

    # Last word is a single uppercase letter (case-insensitive) -> True
    assert module_0.check_if_last_char_is_a_letter("hello A") == True
    assert module_0.check_if_last_char_is_a_letter("hello Z") == True

    # Last word has more than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi ee") == False

    # Last word is a single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False
    assert module_0.check_if_last_char_is_a_letter("hello 5") == False

    # Empty string and trailing spaces -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False

    # Characters just outside the a-z range -> False
    assert module_0.check_if_last_char_is_a_letter("x `") == False   # ord('`') == 96
    assert module_0.check_if_last_char_is_a_letter("x {") == False   # ord('{') == 123

    # Multiple consecutive spaces still find the single-letter last word
    assert module_0.check_if_last_char_is_a_letter("hello  a") == True

# Generated at 2026-11-02 21:27:31.100374
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single standalone letters (case-insensitive)
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word longer than one character
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False

    # Last space-separated token is a single letter
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("I am A") == True
    assert module_0.check_if_last_char_is_a_letter("a b c") == True

    # Trailing space -> empty last token
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("   ") == False

    # Empty string
    assert module_0.check_if_last_char_is_a_letter("") == False

    # Non-alphabetic last tokens
    assert module_0.check_if_last_char_is_a_letter("!!") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("hello world 7") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e1") == False
    assert module_0.check_if_last_char_is_a_letter("x y ?") == False

    # Non-space separators count as part of the word
    assert module_0.check_if_last_char_is_a_letter("a\tb") == False

# Generated at 2026-11-02 21:29:01.045143
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Single letter alone -> True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True

    # Single uppercase letter (lowered before check) -> True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True

    # Last word is a single letter -> True
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("hello world x") == True
    assert module_0.check_if_last_char_is_a_letter("ab c") == True

    # Last word longer than one character -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("hello world") == False
    assert module_0.check_if_last_char_is_a_letter("a bc") == False

    # Single non-letter character -> False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("!") == False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False
    assert module_0.check_if_last_char_is_a_letter("hello !") == False

    # Boundary characters around a-z (96, 97, 122, 123)
    assert module_0.check_if_last_char_is_a_letter("`") == False   # ord 96
    assert module_0.check_if_last_char_is_a_letter("ab `") == False
    assert module_0.check_if_last_char_is_a_letter("hello {") == False  # ord 123

    # Empty and whitespace-only inputs -> False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("   ") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False

    # Multiple spaces: last split token still evaluated
    assert module_0.check_if_last_char_is_a_letter("a  b") == True
    assert module_0.check_if_last_char_is_a_letter("b  ") == False