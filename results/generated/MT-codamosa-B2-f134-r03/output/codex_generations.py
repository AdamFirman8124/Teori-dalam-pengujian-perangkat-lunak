

# Generated at 2026-10-24 22:21:25.195036
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:21:27.614523
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:21:30.037213
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:21:53.973676
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("I love u") is True
    assert module_0.check_if_last_char_is_a_letter("I love you") is False
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 22:22:19.130791
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-24 22:22:21.552597
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:22:23.970026
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:22:26.388857
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:22:28.804194
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:22:31.223594
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:22:32.600939
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("apple pi e") == True

# Generated at 2026-10-24 22:22:59.411130
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello.") is False
    assert module_0.check_if_last_char_is_a_letter("Hello1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("z") is True

# Generated at 2026-10-24 22:23:15.855937
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

# Generated at 2026-10-24 22:23:18.370293
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:20.790535
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:23.338899
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:25.967874
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:28.388499
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:30.809549
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:33.225137
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:35.642904
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:38.062953
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:40.480954
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:42.899782
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:45.317400
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:47.733172
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:50.149700
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:52.566996
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:54.986413
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:57.406243
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:23:59.825673
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:24:02.242209
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-24 22:24:03.611518
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("apple pi e") == True

# Generated at 2026-10-24 22:24:26.628567
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("I love u") is True
    assert module_0.check_if_last_char_is_a_letter("I love you") is False
    assert module_0.check_if_last_char_is_a_letter("The letter is A") is True
    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("z") is True
    assert module_0.check_if_last_char_is_a_letter("7") is False
    assert module_0.check_if_last_char_is_a_letter("!") is False
    assert module_0.check_if_last_char_is_a_letter("") is False