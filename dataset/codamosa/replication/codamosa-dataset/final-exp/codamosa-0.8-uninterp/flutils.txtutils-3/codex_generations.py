

# Generated at 2022-06-13 21:06:27.589393
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('foo\x1b[31mbar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[31m\x1b[1mbar\x1b[0;0m') == 6
    assert len_without_ansi('foo\x1b[31mbar\x1b[0;0m') == 6
    assert len_without_ansi('foo\x1b[31mb\x1b[0;0mar') == 6
    assert len_without_ansi('foo\x1b[31mb\x1b[0;0;0mar') == 6

# Generated at 2022-06-13 21:06:30.273233
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:06:33.505866
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, 'foo']) == 9



# Generated at 2022-06-13 21:06:37.904961
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar\x1b[0;39m') == 6
    assert len_without_ansi(['foo', '\x1b[38;5;208mbar\x1b[0;39m', '\x1b[38;5;153m, \x1b[0;39mbaz\x1b[0;39m']) == 9
test_len_without_ansi()
del test_len_without_ansi



# Generated at 2022-06-13 21:06:48.385973
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D103 (pycodestyle)
    from hypothesis import given, strategies as st  # type: ignore[import]
    from flutils.hypothesis import ansi_codes  # type: ignore[import]
    from flutils.py23compat import is_text_type  # type: ignore[import]

    if hexversion >= 0x03080000:
        from typing import get_args  # type: ignore[import]
        from typing import get_origin  # type: ignore[import]
        from typing_extensions import Literal  # type: ignore[import]
        from typing_extensions import TypedDict  # type: ignore[import]

        class ATD(TypedDict):
            #: Test
            test: int


# Generated at 2022-06-13 21:06:51.668652
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit tests for function ``len_without_ansi``."""
    from flutils.testing import run_tests
    return run_tests(_tests(), 'len_without_ansi')

# Generated at 2022-06-13 21:06:55.537813
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.strip()) == 6
    assert len_without_ansi(text.split()) == 6



# Generated at 2022-06-13 21:06:58.392840
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:03.737872
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6




# Generated at 2022-06-13 21:07:07.166450
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:07:52.159177
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi("Hello world") == 11
    assert len_without_ansi("Hello world\x1b") == 11
    assert len_without_ansi("Hello world\x1b[") == 11
    assert len_without_ansi("Hello world\x1b[1") == 11
    assert len_without_ansi("Hello world\x1b[38") == 11
    assert len_without_ansi("Hello world\x1b[38;") == 11
    assert len_without_ansi("Hello world\x1b[38;5") == 11
    assert len_without_ansi("Hello world\x1b[38;5;") == 11

# Generated at 2022-06-13 21:07:58.192449
# Unit test for function len_without_ansi
def test_len_without_ansi():
    str_ = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(str_) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo', '\x1b[0mbar', '\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo', 'bar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:08:09.825602
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.testing.helpers import raises
    from flutils.txtutils import len_without_ansi

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi('foo\u039A\u0391\u03A3 bar') == 13
    assert len_without_ansi('foo\U0001d5a0bar') == 9
    assert len_without_ansi([text, 'bar', '\x1b[7mfoo\x1b[0m']) == 11
    assert len_without_ansi([text, 'bar', '\x1b[7mfoo\x1b[0m', '']) == 11

    with raises(TypeError):
        len

# Generated at 2022-06-13 21:08:15.777003
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar', '\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:20.115562
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:08:30.234565
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi
    """
    from flutils.txtutils import len_without_ansi
    # no ANSI
    assert len_without_ansi('foobar') == 6
    # ANSI for entire string
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    # ANSI in middle of string
    assert len_without_ansi('foo\x1b[38;5;209mbar\x1b[0m') == 6
    # ANSI at end of string
    assert len_without_ansi('foobar\x1b[0m') == 6
    # ANSI at beginning of string

# Generated at 2022-06-13 21:08:32.503382
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:36.814231
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:08:37.773700
# Unit test for function len_without_ansi
def test_len_without_ansi():
    pass


# Generated at 2022-06-13 21:08:42.032438
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:52.442076
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:09:58.445535
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['hello', '\x1b[38;5;209mworld\x1b[0m', 'foobar']) == 14


# Generated at 2022-06-13 21:10:05.818249
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Run the tests for :func:`flutils.txtutils.len_without_ansi`."""
    from flutils.txtutils import len_without_ansi
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foobar', 'foobar']) == 12



# Generated at 2022-06-13 21:10:14.892995
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo']) == 3
    assert len_without_ansi(('foo',)) == 3
    assert len_without_ansi(('foo')) == 3
    assert len_without_ansi(['foo', 'foobar']) == 9
    assert len_without_ansi(('foo', 'foobar')) == 9



# Generated at 2022-06-13 21:10:19.737045
# Unit test for function len_without_ansi
def test_len_without_ansi():
    func_name = 'len_without_ansi'
    assert len_without_ansi(' \x1b[1mfoo\x1b[0m ') == 3, func_name
    assert len_without_ansi(('\x1b[1mfoo\x1b[0m ', '\x1b[1mfoo\x1b[0m ')) == 6, func_name



# Generated at 2022-06-13 21:10:30.194097
# Unit test for function len_without_ansi
def test_len_without_ansi():
    tests = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        '\x1b[38;5;209mfoo\x1b[0mbar',
        '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m',
        '\x1b[38;5;209mfoo\x1b[38;5;209mbar\x1b[0m',
    ]
    expected = 6
    for text in tests:
        assert len_without_ansi(text) == expected

# Generated at 2022-06-13 21:10:33.980661
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:47.062568
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:10:50.387169
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test the function :meth:`len_without_ansi`."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6




# Generated at 2022-06-13 21:11:01.845641
# Unit test for function len_without_ansi

# Generated at 2022-06-13 21:12:36.412138
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    # text = list(text)
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6



# Generated at 2022-06-13 21:12:39.480663
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    from flutils.txtutils import len_without_ansi

    text = '\x1b[38;5;209mfoobar\x1b[0m'

    with pytest.raises(TypeError):
        len_without_ansi(1)  # type: ignore[call-arg]

    assert len_without_ansi(text) == 6  # type: ignore[no-untyped-calls]

# =====



# Generated at 2022-06-13 21:12:47.513643
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = 'foobar'
    assert len_without_ansi(text) == 6

    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6

    text = [123, '\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
# enddef



# Generated at 2022-06-13 21:12:54.243691
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.testing import assert_function_output

    assert_function_output(len_without_ansi,
                           args=[''],
                           kwargs={},
                           output=0)
    assert_function_output(len_without_ansi,
                           args=['foobar'],
                           kwargs={},
                           output=6)
    assert_function_output(len_without_ansi,
                           args=['\x1b[38;5;209mfoobar\x1b[0m'],
                           kwargs={},
                           output=6)
    # You can use this function on lists, tuples, or sequences as well.
    # Not just strings.

# Generated at 2022-06-13 21:13:00.355208
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:06.504524
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    expected = 6
    out = len_without_ansi(text)
    assert out == expected



# Generated at 2022-06-13 21:13:11.363787
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:13:17.642423
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(['foo', 'bar', '\x1b[38;5;209m']) == 6



# Generated at 2022-06-13 21:13:27.497412
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """ The len_without_ansi function should return the
        character length of the given string without counting
        any ANSI codes.
    """
    import pytest
    # A string with a single ANSI code
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    # A list of strings with various ANSI codes
    seq = [text, '\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']
    assert len_without_ansi(seq) == 18
    # A tuple of strings with various ANSI codes

# Generated at 2022-06-13 21:13:33.180491
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6, 'Length without ansi codes is wrong'
# Test for error case
    text = '\x1b[38;5;209mf\x1b[0m'
    assert len_without_ansi(text) == 1, 'Length without ansi codes is wrong'

