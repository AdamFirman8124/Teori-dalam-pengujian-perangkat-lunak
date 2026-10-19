

# Generated at 2022-06-13 21:12:33.775830
# Unit test for function len_without_ansi
def test_len_without_ansi():
    _text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(_text) == 6
    _text = '\x1b[38;5;209mfoobar\x1b[0m\x1b[44m'
    assert len_without_ansi(_text) == 6
    _text = 'hello'
    assert len_without_ansi(_text) == 5
    _text = ['\x1b[38;5;209mfoo', '\x1b[38;5;208mbar\x1b[0m', '\n', 'hello']
    assert len_without_ansi(_text) == 11



# Generated at 2022-06-13 21:12:37.148073
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


del hexversion



# Generated at 2022-06-13 21:12:47.703134
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo']) == 3
    assert len_without_ansi(['foo', '\x1b[38;5;209m', 'bar', '\x1b[0m']) == 3
    assert len_without_ansi(['', 'foo', '\x1b[38;5;209m', 'bar', '\x1b[0m', '']) == 3



# Generated at 2022-06-13 21:12:55.691068
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Functional test for the :func:`len_without_ansi` function.
    """
    assert len_without_ansi('\x1b[1;5;31mfoo\x1b[0mbar\x1b[1;5;31mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:13:01.732574
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:04.398090
# Unit test for function len_without_ansi
def test_len_without_ansi():
    out = len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m')
    assert out == 6



# Generated at 2022-06-13 21:13:13.640391
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """
    Test the functionality of the function len_without_ansi.

    :return:
    :rtype: None
    """
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m is a test'
    assert len_without_ansi(text) == 13
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6



# Generated at 2022-06-13 21:13:25.708912
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.splitlines()) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi([text.splitlines()]) == 6
    assert len_without_ansi([text, text.splitlines()]) == 12



# Generated at 2022-06-13 21:13:29.837652
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:13:37.944360
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # type: () -> None
    """Test that len_without_ansi() works"""
    text = 'foo\x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['foo', '\x1b[38;5;209m', 'bar', '\x1b[0m']) == 6
    assert len_without_ansi(['foo\x1b[38;5;209m', 'bar\x1b[0m']) == 6

