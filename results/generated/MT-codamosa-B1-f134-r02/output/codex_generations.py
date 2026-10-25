

# Generated at 2026-10-24 22:12:11.279845
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello A") is True
    assert module_0.check_if_last_char_is_a_letter("Hello z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("Hello A ") is False

# Generated at 2026-10-24 22:12:25.522331
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


def module_0.check_if_last_char_is_a_letter(txt):
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("a", True),
        ("A", True),
        ("hello z", True),
        ("hello Z", True),
        ("hello", False),       # More than one character
        ("hello 1", False),     # Digit
        ("hello !", False),     # Punctuation
        ("hello ab", False),    # More than one character
        ("", False),            # Empty string
        ("hello ", False),      # Trailing space
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-24 22:12:47.938732
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("Hello") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False

# Generated at 2026-10-24 22:13:14.049485
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello World") is True

    assert module_0.check_if_last_char_is_a_letter("Hello!") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 22:13:30.534172
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Core behavior: last char is a letter AND forms its own word
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True    # 'e' alone
    assert module_0.check_if_last_char_is_a_letter("apple pi") == True      # 'i' alone
    assert module_0.check_if_last_char_is_a_letter("a") == True             # single letter
    assert module_0.check_if_last_char_is_a_letter("A") == True             # uppercase works

    # Last char is a letter but part of a longer word -> False
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie e!") == False # 'e!' isn't a lone letter

    # Last char is not a letter -> False
    assert module_0.check_if_last_char_is_a_letter("hello world!") == False
    assert module_0.check_if_last_char_is_a_letter("hello 1") == False

    # Edge cases
    assert module_0.check_if_last_char_is_a_letter("") == False             # empty string
    assert module_0.check_if_last_char_is_a_letter("   ") == False          # spaces only
    assert module_0.check_if_last_char_is_a_letter("hello ") == False       # trailing space
    assert module_0.check_if_last_char_is_a_letter("a  b") == True          # multiple spaces

    print("All tests passed.")


test_check_if_last_char_is_a_letter()