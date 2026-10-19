

# Generated at 2022-06-13 21:05:13.069908
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 21:05:18.050558
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:23.006075
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ret = len_without_ansi(text)
    assert ret == 6



# Generated at 2022-06-13 21:05:33.848515
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m  baz'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar  baz\x1b[0m'
    assert len_without_ansi(text) == 9
    text = '  \x1b[38;5;209mfoobar  \x1b[0m  baz'
    assert len_without_ansi(text) == 9

# Generated at 2022-06-13 21:05:43.046322
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi(
        ['\x1b[38;5;209m', 'foo', '\x1b[38;5;215m', 'bar', '\x1b[0m']
    ) == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6

# Generated at 2022-06-13 21:05:46.268068
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'  # noqa: E501
    assert len(text) == 19
    assert len_without_ansi(text) == 6


_ANSI_FORMAT_RE = re.compile(r'(\x1b\[(?:[0-9;:]+)?(?:[ABCDEFGHJKSTfhilmns]))')



# Generated at 2022-06-13 21:05:54.643948
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m\x1b[38;5;213mbarfoo\x1b[0m'
    assert len_without_ansi(text) == 12
    assert len_without_ansi(text.split()) == 12
    text = '\x1b[38;5;209mfoobar\x1b[0mfoobar'
    assert len_without_ansi(text) == 12


# Generated at 2022-06-13 21:05:57.849206
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, 'baz']) == 9


# Used in the type comment at the top of the class

# Generated at 2022-06-13 21:06:12.800681
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils import txtutils
    from hypothesis import strategies as st
    from hypothesis import given

    @given(st.text())
    def test_len_without_ansi(text):
        # Verify len_without_ansi with no ANSI codes.
        test_text = text
        assert len(test_text) == txtutils.len_without_ansi(test_text)
        # Verify len_without_ansi with ANSI codes.
        # (Can't use a strategy here because of the use of \x1b)
        test_text = '\x1b[38;5;209m{}\x1b[0m'.format(text)
        assert len(text) == txtutils.len_without_ansi(test_text)

    test_len_without_ansi()



# Generated at 2022-06-13 21:06:23.721137
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['foo', 'bar', 'baz']) == 9
    assert len_without_ansi('') == 0
    assert len_without_ansi('\x1b[38;5;209m\x1b[0m') == 0
    assert len_without_ansi(
        '\x1b[38;5;209mThe quick brown fox jumps over the lazy dog\x1b[0m'
    ) == 43
    assert len_without_ansi(['foo\x1b[0m', 'bar\x1b[38m']) == 6
    assert len_without

# Generated at 2022-06-13 21:07:27.642742
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:33.437398
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # fmt: off
    tests = [
        [
            ['\x1b[38;5;209mfoo',
             '\x1b[38;5;209mbar',
             '\x1b[38;5;209m'],
            0
        ],
        ['\x1b[38;5;209mfoobar\x1b[0m',
         6]
    ]
    # fmt: on
    for data, expected in tests:
        assert len_without_ansi(data) == expected



# Generated at 2022-06-13 21:07:44.376525
# Unit test for function len_without_ansi
def test_len_without_ansi():

    text = '\x1b[38;5;209mfoobar\x1b[0m'

    assert len_without_ansi(text) == 6

    text = '\x1b[38;5;209mtext1\x1b[0m \x1b[38;5;209mtext2\x1b[0m'

    assert len_without_ansi(text) == 10

    parts = ('\x1b[38;5;209mtext1\x1b[0m', '\x1b[38;5;209mtext2\x1b[0m')

    assert len_without_ansi(parts) == 10


# Generated at 2022-06-13 21:07:48.296922
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# vim: set sts=4 sw=4 ts=8 expandtab ft=python:

# Generated at 2022-06-13 21:07:52.428878
# Unit test for function len_without_ansi
def test_len_without_ansi():
    _text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(_text) == 6
    assert len_without_ansi([_text]) == 6
# Systest for function len_without_ansi

# Generated at 2022-06-13 21:08:00.382437
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # no ansi
    text = 'foobar'
    assert len_without_ansi(text) == 6

    # single ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    # multiple ansi
    text = '\x1b[38;5;209m\x1b[1;30mbold\x1b[0m\x1b[0m'
    assert len_without_ansi(text) == 4

    # list of strings without ansi
    text = ['foobar']
    assert len_without_ansi(text) == 6

    # list of strings with ansi

# Generated at 2022-06-13 21:08:03.946629
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:09.511821
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[0m\x1b[38;5;209m{0}\x1b[0m'
            .format('foo'))
    assert len_without_ansi(text) == 3



# Generated at 2022-06-13 21:08:16.328171
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m', 'quux']
    out = len_without_ansi(text)
    assert out == 9



# Generated at 2022-06-13 21:08:26.985599
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Flutils: Testing function flutils.txtils.len_without_ansi."""
    from flutils.txtutils import len_without_ansi
    _text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(_text) == 6
    _text = '\\x1b[38;5;209mfoo\\x1b[0mbar\\x1b[38;5;209m\\x1b[0m'
    assert len_without_ansi(_text) == 6
    assert len_without_ansi([_text]) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:09:49.190479
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:09:52.143387
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:59.300135
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
# end function test_len_without_ansi



# Generated at 2022-06-13 21:10:01.738494
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:06.196676
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    _len = len_without_ansi(text)
    assert _len == 6, f"len_without_ansi returned {_len} instead of 6."



# Generated at 2022-06-13 21:10:18.697267
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from sys import hexversion

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar\x1b[0m']) == 6
    if hexversion < 0x03080000:
        assert (
            len_without_ansi(
                [
                    '\x1b[38;5;209m',
                    'foobar',
                    '\x1b[0m',
                    '\x1b[38;5;209m',
                    'foobar\x1b[0m',
                ],
            )
            == 12
        )

# Generated at 2022-06-13 21:10:21.534532
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:24.814754
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:34.268820
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    text_seq = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    good = 6
    assert len_without_ansi(text) == good
    assert len_without_ansi(text_seq) == good
    with pytest.raises(TypeError):
        len_without_ansi(None)



# Generated at 2022-06-13 21:10:37.560529
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:11:32.215057
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.testutils import (
        AssertCallableReturns,
        AssertCallableRaises,
    )

# Generated at 2022-06-13 21:11:38.350012
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:46.169650
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .txtfmt import ansi, fg256

    text = 'foobar'
    textlen = len(text)

    # Test a string with ANSI colors
    _text = ansi(fg256(209)('foobar'))
    assert len_without_ansi(_text) == textlen

    # Test a string with ANSI colors between quotes
    _text = ansi(fg256(209)("'" + text + "'"))
    assert len_without_ansi(_text) == textlen

    # Test a string with ANSI colors at the beginning
    _text = ansi(fg256(209)(text))
    assert len_without_ansi(_text) == textlen

    # Test a string with ANSI colors at the end
    _text = ansi(fg256(209)(text))
    assert len_without_ans

# Generated at 2022-06-13 21:11:52.201504
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:59.307321
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['foo\n', 'ba', '\x1b[38;5;209mr\x1b[0m']) == 6
    assert len_without_ansi(['one', 'two', 'three']) == 11
    assert len_without_ansi(['one', 'tw\x1b[38;5;209mo\x1b[0m', 'three']) == 11



# Generated at 2022-06-13 21:12:08.199804
# Unit test for function len_without_ansi
def test_len_without_ansi():

    def _test(
            text: str,
            expected: int = None
    ):
        if expected is None:
            expected = len(text)
        assert len_without_ansi(text) == expected

    _test('foobar')
    _test('foo bar')
    _test('foo\x1bbaz')
    _test('foo\x1b[38;5;209mbar')
    _test('foo\x1b[38;5;209mbar\x1b[0m', 6)
    _test('\x1b[38;5;209mfoob\x1b[0mar')
    _test(['foo', 'bar'])
    _test(['foo', '\x1b[38;5;209mbar\x1b[0m'], 6)



# Generated at 2022-06-13 21:12:13.766868
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:20.085998
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:26.507746
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test for :func:`len_without_ansi`."""
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split(' ')) == 6
    text = '1\\x1b[38;5;209m2\\x1b[0m3'
    assert len_without_ansi(text) == 3
    assert len_without_ansi(text.split(' ')) == 3



# Generated at 2022-06-13 21:12:30.819633
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert isinstance(out, int)
    assert out == 6

