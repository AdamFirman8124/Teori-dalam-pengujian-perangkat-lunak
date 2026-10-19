

# Generated at 2022-06-13 21:05:35.523404
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# End unit test for function len_without_ansi



# Generated at 2022-06-13 21:05:37.721596
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:47.367079
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0mfoobarbaz'
    assert len_without_ansi(text) == 18
    text = ['\x1b[38;5;209mfoo', '\x1b[0mbar', '\x1b[38;5;209mbaz']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:55.072688
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """
    Unit test for ``len_without_ansi``.
    """
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    text_list = ['\x1b[38;5;209mfoo', '\x1b[0mbar']
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text_list) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:05:59.426856
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:08.191858
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:06:19.453788
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '\x1b[0m']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '']) == 6
    assert len_without_ansi(['']) == 0
    assert len_without_ansi(['\x1b[38;5;209mfoobar']) == 6



# Generated at 2022-06-13 21:06:22.850826
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = 6
    assert len_without_ansi(text) == ans



# Generated at 2022-06-13 21:06:25.074097
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6


# flutils.txtutils.AnsiTextWrapper

# Generated at 2022-06-13 21:06:34.763209
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test that len_without_ansi returns the right result."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', '\x1b[38;5;46mbar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoo', '\x1b[38;5;46mbar\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:12.500210
# Unit test for function len_without_ansi
def test_len_without_ansi():  # pragma: no cover
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert (
        len_without_ansi(('\x1b[36mtext', '\x1b[38;5;209mfoobar', '\x1b[0m')) ==
        9)

# Generated at 2022-06-13 21:07:15.390767
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:07:19.246963
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# -- Unit test for function len_without_ansi


# Generated at 2022-06-13 21:07:24.331202
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:27.327741
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:07:31.417372
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi(['hello', 'world', text]) == 20



# Generated at 2022-06-13 21:07:37.289825
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """
    >>> from flutils.txtutils import len_without_ansi
    >>> text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    >>> len_without_ansi(text)
    6
    """



# Generated at 2022-06-13 21:07:49.252454
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo bar') == 7
    assert len_without_ansi(['foo bar']) == 7
    assert len_without_ansi(('foo bar',)) == 7
    assert len_without_ansi(('foo bar', 'baz')) == 10
    assert len_without_ansi(('\x1b[31mfoo', 'baz')) == 8
    assert len_without_ansi(('\x1b[31mfoo', '\x1b[32mbaz')) == 7
    assert len_without_ansi(('\x1b[31mfoo', '\x1b[0mbaz')) == 7
    assert len_without_ansi('\x1b[1;32mfoobar\x1b[m') == 6
    assert len_without_

# Generated at 2022-06-13 21:07:58.463722
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi."""
    from os import linesep
    from textwrap import dedent
    from flutils.txtutils import len_without_ansi

    text = dedent('''\
        \x1b[38;5;11mfoobar\x1b[39m
        \x1b[38;5;11mbarfoo\x1b[39m''')
    text2 = dedent('''\
        foo
        bar''')
    # Test: function returns the proper character length
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text2) == len(text2)
    # Test: function works with a list of strings
    assert len_without_ansi([text, text2]) == 14
    # Test: function works

# Generated at 2022-06-13 21:08:06.460803
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;208mbar\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:25.338393
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\\x1b[38;5;209mfoobar\\x1b[0m', '\\x1b[38;5;209mbaz\\x1b[0m')
    assert len_without_ansi(text) == 9


# Generated at 2022-06-13 21:08:34.496854
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('Hello World!') == 12
    assert len_without_ansi(['Hello', 'World!']) == 12
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    text = 'foo\\x1b[38;5;209mfoobar\\x1b[0mbar'
    assert len_without_ansi(text) == 12
    text = '\\x1b[38;5;209mfoobar'
    assert len_without_ansi(text) == 0
    text = '0\\x1b[38;5;209mbar'
    assert len_without_ansi(text) == 2

# Generated at 2022-06-13 21:08:38.229489
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:46.864766
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.pyutils import TestClass

    _test_inst = TestClass()
    _test_inst.test_eq(len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m'), 6)
    _test_inst.test_eq(
        len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m',
                          '\x1b[38;5;209mhelloworld\x1b[0m']),
        len('foobarhelloworld'))

# Generated at 2022-06-13 21:08:54.198888
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # With a string
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    uut = len_without_ansi(text)
    assert uut == 6
    # With a list of strings
    text = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    uut = len_without_ansi(text)
    assert uut == 6



# Generated at 2022-06-13 21:08:58.666323
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1B[38;5;209mtest\x1B[0m'
    out = len_without_ansi(text)
    assert out == 4

# Generated at 2022-06-13 21:09:03.214968
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D103
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:07.234476
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text * 2) == 12



# Generated at 2022-06-13 21:09:15.073691
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

_WRAP_WIDTH = 80
_WRAP_INIT_KWARGS = dict(
    break_long_words=False,
    fix_sentence_endings=False,
    replace_whitespace=False,
    subsequent_indent='',
    width=_WRAP_WIDTH,
)
_WRAP_INIT_KWARGS_ENHANCED = _WRAP_INIT_KWARGS.copy()
_WRAP_INIT_KWARGS_ENHANCED.update(
    break_long_words=True,
    replace_whitespace=True,
    width=None,
)



# Generated at 2022-06-13 21:09:21.574686
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;199mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['foo', '\x1b[38;5;199mbar\x1b[0m', 'baz']
    assert len_without_ansi(text) == 9
    text = ['foo', '', '\x1b[38;5;199m', 'bar', '\x1b[0m', 'baz']
    assert len_without_ansi(text) == 9



# Generated at 2022-06-13 21:09:58.457498
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D103
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:05.162492
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoo', '\x1b[0mbar')
    assert len_without_ansi(text) == 6
test_len_without_ansi()
del test_len_without_ansi



# Generated at 2022-06-13 21:10:15.042479
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test the ``len_without_ansi`` function."""
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    # assert len_without_ansi(['foo', 'bar', '\x1b[38;5;209mfoobar\x1b[0m']) == 9
    assert len_without_ansi(['foo', 'bar', '\x1b[38;5;209mfoobar\x1b[0m']) == 10



# Generated at 2022-06-13 21:10:20.581722
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi(['foo', '\x1b[38;5;209m', 'foo', 'bar\x1b[0m']) == 6



# Generated at 2022-06-13 21:10:24.949478
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # pylint: disable = invalid-name, missing-function-docstring
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    res = 6
    assert len_without_ansi(text) == res



# Generated at 2022-06-13 21:10:28.588693
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:33.473644
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6



# Generated at 2022-06-13 21:10:46.813758
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = 6
    assert len_without_ansi(text) == out
    text = ('\x1b[38;5;209mfoobar\x1b[0m',
            'foobar')
    out = 12
    assert len_without_ansi(text) == out
    text = ('foobar',
            '\x1b[38;5;209mfoobar\x1b[0m')
    out = 12
    assert len_without_ansi(text) == out
    text = [('foobar',
             '\x1b[38;5;209mfoobar\x1b[0m'),
            'foobar']
    out = 18
    assert len_without_ansi

# Generated at 2022-06-13 21:10:55.711255
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[31mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[31mfoobar\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[31mfoobar\x1b[0m', 'baz']) == 9
    assert len_without_ansi(['\x1b[31mfoobar\x1b[0m' * 5, 'baz']) == 15



# Generated at 2022-06-13 21:11:02.857296
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import ANSI_CODES as c

    text = 'foobar'
    assert len_without_ansi(text) == len(text)

    text = [c.BOLD, 'foobar', c.NORM]
    assert len_without_ansi(text) == len(text) - 2

    text = ''.join(text)
    assert len_without_ansi(text) == len(text) - 2
test_len_without_ansi()



# Generated at 2022-06-13 21:12:45.666685
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from textwrap import dedent
    from flutils.txtutils import len_without_ansi as lenwa
    text = dedent("""\
        [38;5;209mfoobar[0m
        [38;5;209mfoobar[0m
            [38;5;209mfoobar[0m
        [38;5;209mfoobar[0m""")
    assert lenwa(text) == 24


# Generated at 2022-06-13 21:12:50.595925
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['one', '\x1b[34mtwo', '\x1b[92mthree']) == 11



# Generated at 2022-06-13 21:12:56.193168
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6



# Generated at 2022-06-13 21:12:58.744095
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:07.803552
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m', 'baz']
    assert len_without_ansi(text) == 8
    text = ['\x1b[38;5;209mfoobar\x1b[0m', 'baz', 'bat']
    assert len_without_ansi(text) == 11



# Generated at 2022-06-13 21:13:10.536606
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6



# Generated at 2022-06-13 21:13:18.261172
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoo\x1b[0mbar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', 'bar\x1b[0m']) == 6


# Generated at 2022-06-13 21:13:22.077860
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:27.156285
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:34.220032
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    seq = [text] * 2
    out = len_without_ansi(seq)
    assert out == 6
    seq = [text, text]
    out = len_without_ansi(seq)
    assert out == 12

