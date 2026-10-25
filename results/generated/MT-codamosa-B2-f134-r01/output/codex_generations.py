

# Generated at 2026-10-24 16:04:14.812691
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

# Generated at 2026-10-24 16:04:16.150359
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

# Generated at 2026-10-24 16:04:17.529624
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

# Generated at 2026-10-24 16:04:19.017489
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

# Generated at 2026-10-24 16:04:20.451179
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

# Generated at 2026-10-24 16:04:21.869240
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

# Generated at 2026-10-24 16:04:23.524599
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

# Generated at 2026-10-24 16:04:25.302837
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

# Generated at 2026-10-24 16:04:26.607694
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

# Generated at 2026-10-24 16:04:27.930920
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

# Generated at 2026-10-24 16:04:30.448312
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:32.955143
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:35.366513
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:37.779832
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:40.194229
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:42.611567
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:45.023786
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:47.477522
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:49.890695
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:52.301496
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:54.712947
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:57.125213
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:04:59.536869
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:05:01.949161
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 16:05:04.359600
# Unit test for function check_if_last_char_is_a_letter