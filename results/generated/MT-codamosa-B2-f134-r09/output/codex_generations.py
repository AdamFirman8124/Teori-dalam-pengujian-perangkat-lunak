

# Generated at 2026-10-24 20:41:35.148276
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello a!") is False
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False

# Generated at 2026-10-24 20:41:51.270901
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:42:15.592046
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello A") is True
    assert module_0.check_if_last_char_is_a_letter("Hello z") is True

    assert module_0.check_if_last_char_is_a_letter("Hello") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:42:32.020245
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

# Generated at 2026-10-24 20:42:53.581941
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:43:19.291503
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("The last character is a") is True
    assert module_0.check_if_last_char_is_a_letter("The last character is Z") is True

    assert module_0.check_if_last_char_is_a_letter("The last word is no") is False
    assert module_0.check_if_last_char_is_a_letter("The last character is 7") is False
    assert module_0.check_if_last_char_is_a_letter("Ends with punctuation !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a ") is False

# Generated at 2026-10-24 20:43:32.082643
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Z") is True

    assert module_0.check_if_last_char_is_a_letter("ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("hello 12") is False

# Generated at 2026-10-24 20:43:48.467576
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

# Generated at 2026-10-24 20:43:51.079149
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:43:53.496252
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:43:55.912930
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:44:12.532184
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

# Generated at 2026-10-24 20:44:28.448210
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:44:29.775081
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("apple pi e") == True

# Generated at 2026-10-24 20:44:43.252463
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:44:59.738915
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

# Generated at 2026-10-24 20:45:17.152751
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # True: last token is single letter
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi E") == True
    assert module_0.check_if_last_char_is_a_letter("apple a") == True
    assert module_0.check_if_last_char_is_a_letter("A") == True
    assert module_0.check_if_last_char_is_a_letter("z") == True

    # False: last token is a word, not a single letter
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("apple 1") == False
    assert module_0.check_if_last_char_is_a_letter("apple !") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi 1") == False

# Generated at 2026-10-24 20:45:32.403823
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


def module_0.check_if_last_char_is_a_letter(txt):
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("hello a", True),
        ("hello Z", True),
        ("a", True),
        ("hello 1", False),
        ("hello ab", False),
        ("hello !", False),
        ("hello a!", False),
        ("hello ", False),
        ("", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-24 20:45:56.676404
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("hello z") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:46:11.840638
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False

# Generated at 2026-10-24 20:46:28.331139
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

# Generated at 2026-10-24 20:46:50.950193
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Z") is True
    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:47:01.750127
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello a!") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:47:17.876774
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 20:47:41.326668
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello world a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello world Z") is True

    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("Hello world 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello world !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a ") is False

# Generated at 2026-10-24 20:47:55.156746
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest

@pytest.mark.parametrize(
    "txt, expected",
    [
        ("a", True),
        ("hello A", True),
        ("hello z", True),
        ("hello 1", False),
        ("hello !", False),
        ("hello ab", False),
        ("hello", False),
        ("", False),
        ("hello a ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-24 20:47:57.691496
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("hello world") is False
    assert module_0.check_if_last_char_is_a_letter("hello world 3") is False
    assert module_0.check_if_last_char_is_a_letter("hello world z") is True
    assert module_0.check_if_last_char_is_a_letter("hello world Z") is True
    assert module_0.check_if_last_char_is_a_letter("abc de1") is False

# Generated at 2026-10-24 20:48:14.300044
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

# Generated at 2026-10-24 20:48:30.893097
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

# Generated at 2026-10-24 20:48:44.922800
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
        ("hello A", True),
        ("hello ab", False),
        ("hello 1", False),
        ("hello!", False),
        ("", False),
        ("hello ", False),
        ("hello a ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) == expected

# Generated at 2026-10-24 20:49:11.950606
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello!") is False
    assert module_0.check_if_last_char_is_a_letter("123a") is True
    assert module_0.check_if_last_char_is_a_letter("1234") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ") is False

# Generated at 2026-10-24 20:49:27.246747
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("hello A") is True
    assert module_0.check_if_last_char_is_a_letter("hello z") is True

    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False

# Generated at 2026-10-24 20:49:43.695276
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

# Generated at 2026-10-24 20:49:46.217617
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:49:48.733063
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:49:51.150364
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:49:53.567629
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:49:55.985090
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:49:58.402386
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:00.820017
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:03.236137
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:05.656877
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:08.073135
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:10.493118
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:12.906282
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:15.321397
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:17.739423
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:20.154819
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:22.570762
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:24.986215
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:27.403635
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:29.820908
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:32.236384
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:34.653144
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:37.069622
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:39.486855
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:41.902902
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:44.320425
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:46.738559
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:49.155073
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:51.571815
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:53.988866
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 20:50:56.578293
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("hello world") is False
    assert module_0.check_if_last_char_is_a_letter("hello world 3") is False
    assert module_0.check_if_last_char_is_a_letter("hello world z") is True
    assert module_0.check_if_last_char_is_a_letter("hello world Z") is True
    assert module_0.check_if_last_char_is_a_letter("abc de1") is False

# Generated at 2026-10-24 20:51:11.862223
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


def module_0.check_if_last_char_is_a_letter(txt):
    check = txt.split(" ")[-1]
    return True if len(check) == 1 and 97 <= ord(check.lower()) <= 122 else False


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("hello a", True),
        ("hello Z", True),
        ("a", True),
        ("hello ab", False),
        ("hello 1", False),
        ("hello !", False),
        ("hello", False),
        ("hello ", False),
        ("", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) == expected

# Generated at 2026-10-24 20:51:26.608641
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


def module_0.check_if_last_char_is_a_letter(txt):
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("hello a", True),
        ("hello Z", True),
        ("a", True),
        ("hello ab", False),
        ("hello 1", False),
        ("hello !", False),
        ("hello a!", False),
        ("hello", False),
        ("hello ", False),
        ("", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) == expected