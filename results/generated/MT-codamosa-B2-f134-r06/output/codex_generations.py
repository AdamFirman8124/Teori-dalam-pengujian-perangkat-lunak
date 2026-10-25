

# Generated at 2026-10-25 02:33:08.109618
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("This is a") is True
    assert module_0.check_if_last_char_is_a_letter("This is Z") is True

    assert module_0.check_if_last_char_is_a_letter("This is 7") is False
    assert module_0.check_if_last_char_is_a_letter("This is !") is False
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Ends with a ") is False

# Generated at 2026-10-25 02:33:23.829195
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("hello") is True
    assert module_0.check_if_last_char_is_a_letter("Ends with Z") is True

    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("number 1") is False
    assert module_0.check_if_last_char_is_a_letter("trailing space ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:33:32.478976
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:33:38.136614
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    assert module_0.check_if_last_char_is_a_letter("Hello") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:33:47.426728
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("Apple P", True),
        ("Apple p", True),
        ("Apple pie", False),
        ("Apple 1", False),
        ("Apple ?", False),
        ("A", True),
        ("", False),
        ("Apple ", False),
        ("Apple Ã©", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:33:52.594156
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("apple a") is True

# Generated at 2026-10-25 02:34:00.006259
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pi E") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi 3") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi !") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False

# Generated at 2026-10-25 02:34:07.904831
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest

@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("hello a", True),
        ("hello Z", True),
        ("a", True),
        ("Z", True),
        ("hello", False),
        ("hello ab", False),
        ("hello 1", False),
        ("hello !", False),
        ("hello a ", False),
        ("", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:34:12.444754
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("This is a test a") is True

# Generated at 2026-10-25 02:34:27.052381
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Valid single-letter final tokens
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("hello b") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True

    # Invalid final tokens
    assert module_0.check_if_last_char_is_a_letter("hello word") is False
    assert module_0.check_if_last_char_is_a_letter("hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello Ã©") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("hello A ") is False

# Generated at 2026-10-25 02:34:36.269753
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:34:43.163971
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("A", True),
        ("z", True),
        ("Hello a", True),
        ("Hello Z", True),
        ("Hello world", False),
        ("Hello 1", False),
        ("Hello !", False),
        ("Hello", False),
        ("", False),
        ("Hello a ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:34:47.109797
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("Hello World a") is True

# Generated at 2026-10-25 02:34:59.513295
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello!") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ") is False
    assert module_0.check_if_last_char_is_a_letter("Ã©") is False

# Generated at 2026-10-25 02:35:09.241817
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("A") is True

    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:35:14.976263
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True

    assert module_0.check_if_last_char_is_a_letter("Hello") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:35:25.422960
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("Hello", True),
        ("ABC", True),
        ("ends with z", True),
        ("Hello!", False),
        ("abc1", False),
        ("", False),
        (" ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:35:30.642814
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("hello a") is True

# Generated at 2026-10-25 02:35:40.370906
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("a", True),
        ("Z", True),
        ("Hello a", True),
        ("Hello Z", True),
        ("Hello ab", False),
        ("Hello 7", False),
        ("Hello !", False),
        ("Hello a ", False),
        ("Hello", False),
        ("", False),
        ("Hello Ã©", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:35:45.708826
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("hello a") is True

# Generated at 2026-10-25 02:35:56.038769
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("x") is True

# Generated at 2026-10-25 02:36:05.793266
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pi Z") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi 3") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi !") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True

# Generated at 2026-10-25 02:36:26.953438
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False

# Generated at 2026-10-25 02:36:37.193904
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pie") is True
    assert module_0.check_if_last_char_is_a_letter("apple pi3") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pi %") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("9") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:36:44.871947
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("Hello world a", True),
        ("Hello world Z", True),
        ("Hello world", False),
        ("Hello world 7", False),
        ("Hello world !", False),
        ("a", True),
        ("", False),
        ("Hello world ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:36:49.583960
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("Hello a") is True

# Generated at 2026-10-25 02:36:55.624596
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pie m") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie Z") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie 1") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie !") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True

# Generated at 2026-10-25 02:37:05.019680
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    # Valid isolated letters
    assert module_0.check_if_last_char_is_a_letter("hello a") is True
    assert module_0.check_if_last_char_is_a_letter("hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    # Invalid endings
    assert module_0.check_if_last_char_is_a_letter("hello") is False
    assert module_0.check_if_last_char_is_a_letter("hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("hello !") is False
    assert module_0.check_if_last_char_is_a_letter("hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:37:15.604549
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest


@pytest.mark.parametrize(
    ("txt", "expected"),
    [
        ("A", True),
        ("z", True),
        ("This ends with a", True),
        ("This ends with Z", True),
        ("Hello", False),
        ("This ends with 7", False),
        ("This ends with !", False),
        ("", False),
        ("Ends with a space ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:37:22.259660
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("Hello z") is True

# Generated at 2026-10-25 02:37:29.429315
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pi e") is True
    assert module_0.check_if_last_char_is_a_letter("apple pi E") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi 3") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi !") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("apple pi e ") is False

# Generated at 2026-10-25 02:37:39.597160
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello") is True
    assert module_0.check_if_last_char_is_a_letter("123Z") is True
    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:37:42.017656
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-25 02:37:49.523515
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("Hello world a") is True

# Generated at 2026-10-25 02:37:57.898082
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello 1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello word") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False

# Generated at 2026-10-25 02:38:06.393630
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello!") is False
    assert module_0.check_if_last_char_is_a_letter("Hello1") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:38:12.780043
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("apple pie d") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie D") is True
    assert module_0.check_if_last_char_is_a_letter("apple pie") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie 5") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("ab") is False
    assert module_0.check_if_last_char_is_a_letter("apple pie a ") is False

# Generated at 2026-10-25 02:38:18.681666
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("This ends in y") is True
    assert module_0.check_if_last_char_is_a_letter("This ends in Z") is True
    assert module_0.check_if_last_char_is_a_letter("This ends in ay") is False
    assert module_0.check_if_last_char_is_a_letter("This ends in 1") is False
    assert module_0.check_if_last_char_is_a_letter("This ends in !") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("a") is True
    assert module_0.check_if_last_char_is_a_letter("word") is False

# Generated at 2026-10-25 02:38:30.626612
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("a") is True

    assert module_0.check_if_last_char_is_a_letter("Hello world") is False
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello !") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False
    assert module_0.check_if_last_char_is_a_letter("") is False

# Generated at 2026-10-25 02:38:36.342593
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():import pytest

@pytest.mark.parametrize(
    "txt, expected",
    [
        ("a", True),
        ("Z", True),
        ("This ends with a", True),
        ("This ends with X", True),
        ("This ends with ab", False),
        ("This ends with 1", False),
        ("This ends with a.", False),
        ("This ends with Ã©", False),
        ("", False),
        ("This ends with a ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    assert module_0.check_if_last_char_is_a_letter(txt) is expected

# Generated at 2026-10-25 02:38:40.706437
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("Hello z") is True

# Generated at 2026-10-25 02:38:43.341813
# Unit test for function check_if_last_char_is_a_letter

# Generated at 2026-10-25 02:38:49.196535
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():assert module_0.check_if_last_char_is_a_letter("apple pie a") is True

# Generated at 2026-10-25 02:38:58.388614
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("Hello a") is True
    assert module_0.check_if_last_char_is_a_letter("Hello Z") is True
    assert module_0.check_if_last_char_is_a_letter("Hello 7") is False
    assert module_0.check_if_last_char_is_a_letter("Hello ab") is False
    assert module_0.check_if_last_char_is_a_letter("") is False
    assert module_0.check_if_last_char_is_a_letter("Hello a ") is False

# Generated at 2026-10-25 02:39:07.936648
# Unit test for function check_if_last_char_is_a_letter
def test_check_if_last_char_is_a_letter():
    assert module_0.check_if_last_char_is_a_letter("hello") is True
    assert module_0.check_if_last_char_is_a_letter("Hello World") is True
    assert module_0.check_if_last_char_is_a_letter("A") is True
    assert module_0.check_if_last_char_is_a_letter("hello!") is False
    assert module_0.check_if_last_char_is_a_letter("hello ") is False
    assert module_0.check_if_last_char_is_a_letter("123") is False
    assert module_0.check_if_last_char_is_a_letter("") is False