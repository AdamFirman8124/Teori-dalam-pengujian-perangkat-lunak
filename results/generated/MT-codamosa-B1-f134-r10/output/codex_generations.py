

# Generated at 2026-10-24 14:00:25.393202
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

# Generated at 2026-10-24 14:00:27.807953
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:30.223022
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:32.635680
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:35.048621
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:37.461206
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:39.873847
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:42.287312
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:44.701056
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:47.112498
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:49.526108
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:52.083264
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:54.496704
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:56.909286
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:00:59.322280
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:01.736872
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:04.149602
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:06.561993
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:20.350527
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

# Generated at 2026-10-24 14:01:39.737193
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

# Generated at 2026-10-24 14:01:42.153437
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:44.570065
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:46.989375
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:49.404666
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:51.819594
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:54.232173
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:56.645276
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:01:59.060595
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:01.471830
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:03.887228
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:06.300465
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:08.714686
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:11.128790
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:13.539640
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:15.952844
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:18.365993
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:20.778797
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:23.191860
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:25.604083
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:28.017628
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:30.436634
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:32.843640
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:35.256749
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:37.672048
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:40.082708
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:42.495806
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:44.909714
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:47.325709
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:49.758002
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:52.182500
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:54.597962
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:57.017541
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:02:59.432869
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:13.021096
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") == True
    assert module_0.check_if_last_char_is_a_letter("apple pi E") == True
    assert module_0.check_if_last_char_is_a_letter("a") == True
    assert module_0.check_if_last_char_is_a_letter("Z") == True
    assert module_0.check_if_last_char_is_a_letter("apple b c d") == True
    assert module_0.check_if_last_char_is_a_letter("apple pie") == False
    assert module_0.check_if_last_char_is_a_letter("apple") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi 1") == False
    assert module_0.check_if_last_char_is_a_letter("1") == False
    assert module_0.check_if_last_char_is_a_letter("apple pi !") == False
    assert module_0.check_if_last_char_is_a_letter("apple pie!") == False
    assert module_0.check_if_last_char_is_a_letter("") == False
    assert module_0.check_if_last_char_is_a_letter("apple ") == False
    assert module_0.check_if_last_char_is_a_letter(" ") == False

# Generated at 2026-10-24 14:03:14.362222
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

# Generated at 2026-10-24 14:03:15.729798
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

# Generated at 2026-10-24 14:03:17.135200
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

# Generated at 2026-10-24 14:03:18.662780
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

# Generated at 2026-10-24 14:03:20.014662
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

# Generated at 2026-10-24 14:03:21.494250
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

# Generated at 2026-10-24 14:03:22.817893
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

# Generated at 2026-10-24 14:03:24.177746
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

# Generated at 2026-10-24 14:03:25.518130
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

# Generated at 2026-10-24 14:03:26.831156
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

# Generated at 2026-10-24 14:03:28.155043
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

# Generated at 2026-10-24 14:03:29.486509
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

# Generated at 2026-10-24 14:03:30.846174
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

# Generated at 2026-10-24 14:03:33.363347
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:35.894780
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:38.407226
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:40.821821
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:43.237177
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 14:03:45.655847
# Unit test for function check_if_last_char_is_a_letter