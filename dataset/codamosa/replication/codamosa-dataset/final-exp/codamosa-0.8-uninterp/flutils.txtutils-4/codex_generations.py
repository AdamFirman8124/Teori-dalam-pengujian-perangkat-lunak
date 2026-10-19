

# Generated at 2022-06-13 21:05:44.121101
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    text = ('\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;209mbar\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:49.319560
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = ('\x1b[38;5;209mfoo\x1b[0mbar', '\x1b[38;5;209mbaz', 'qux\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:54.338063
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('\\x1b[0mfoo\\x1b[0m') == 3
    assert len_without_ansi(('\\x1b[0mfoo\\x1b[0m', 'bar')) == 6



# Generated at 2022-06-13 21:05:59.563739
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test a single string
    s = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(s) == 6

    # Test a list of strings
    sq = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(sq) == 6

    # Test a tuple of strings
    tq = ('\x1b[38;5;209mfoo', 'bar\x1b[0m')
    assert len_without_ansi(tq) == 6



# Generated at 2022-06-13 21:06:14.360260
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi as _len_without_ansi

    # A string
    assert _len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert _len_without_ansi('hello world') == 11

    # A list/tuple
    assert _len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert _len_without_ansi(('hello world', '\x1b[38;5;209mfoobar\x1b[0m')) == 17

# Generated at 2022-06-13 21:06:21.173262
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert not len_without_ansi('')
    assert 5 == len_without_ansi('foobar')
    assert 6 == len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m')
    assert 5 == len_without_ansi(('foobar', 'foobar'))
    assert 11 == len_without_ansi(['foo', 'bar'])
    assert 5 == len_without_ansi(('foobar', 'foobar'))



# Generated at 2022-06-13 21:06:24.926755
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for ``len_without_ansi``."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# end function test_len_without_ansi



# Generated at 2022-06-13 21:06:31.702913
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        'foobar',
    ]
    assert len_without_ansi(text) == 12



# Generated at 2022-06-13 21:06:34.875207
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[1m' + 'foobar' + '\x1b[0m'
    out = {'expected': 6}
    out['actual'] = len_without_ansi(text)
    assert out['actual'] == out['expected']



# Generated at 2022-06-13 21:06:36.806527
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:20.336256
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', '\x1b[38;5;222mbar\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:24.461607
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# Test end



# Generated at 2022-06-13 21:07:31.341963
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', '\x1b[0mbar']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:36.462239
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    expected = 6
    assert len_without_ansi(text) == expected



# Generated at 2022-06-13 21:07:40.888182
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 20
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:43.912875
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:07:46.801482
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:53.155257
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar\x1b[38;5;209m') == 6
    assert len_without_ansi('foobar\x1b[38;5;209m ') == 6
    assert len_without_ansi('foobar ') == 6
    assert len_without_ansi(['foobar\x1b[38;5;209m', 'foobar ']) == 12


# Generated at 2022-06-13 21:07:55.645060
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:57.646202
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:08:30.039759
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m \x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 12
    text = '\x1b[38;5;209mfoobar\x1b[0m\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 12



# Generated at 2022-06-13 21:08:33.361693
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6

# Generated at 2022-06-13 21:08:37.138821
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:08:46.495599
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from pytest import raises
    from doctest import testmod
    from typing import Type
    from typing_extensions import Protocol
    class _StrOrListOfStr(Protocol):
        def __iter__(self):
            ...
        def __len__(self):
            ...
        def __getitem__(self, i):
            ...
    t1: str = '\x1b[38;5;209mfoobar\x1b[0m'
    t2: List[str] = ['\x1b[38;5;209mfoobar\x1b[0m']
    assert len_without_ansi(t1) == 6
    assert len_without_ansi(t2) == 6
    with raises(TypeError):
        len_without_ansi(1)

# Generated at 2022-06-13 21:08:52.777075
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('abc', '\x1b[1mbc\x1b[0m', 'def', '\x1b[32mdef\x1b[0m')
    assert len_without_ansi(text) == 9



# Generated at 2022-06-13 21:08:56.153677
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:59.365230
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:02.781613
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:12.949570
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('abcdefg') == 7
    assert len_without_ansi('abc\x1b[38;5;209;mdef') == 7
    assert len_without_ansi('abc\x1b[38;5;209;mdef\x1b[0m') == 7
    assert len_without_ansi('abc\x1b[38;5;209;mdef\x1b[0;m') == 7
    assert len_without_ansi('\x1b[38;5;209;mabc\x1b[0;mdef\x1b[0;m') == 5
    assert len_without_ansi(['abcdefg', '\x1b[38;5;209;mhijkl']) == 12



# Generated at 2022-06-13 21:09:21.983917
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo']) == 3
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi([]) == 0
    assert len_without_ansi(b"foo") == 3
    assert len_without_ansi([b"foo"]) == 3
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi([]) == 0
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo']) == 3
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi([]) == 0

# Generated at 2022-06-13 21:09:56.543636
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:09:59.868969
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:10:05.621139
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi(('foo', text, 'bar')) == 9
test_len_without_ansi()



# Generated at 2022-06-13 21:10:17.217240
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest

    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    len_text = len(text)
    assert len(text) > len_without_ansi(text)
    assert len_text == len(_ANSI_RE.sub('', text))
    assert (len_without_ansi([
        '\\x1b[38;5;209mfoobar\\x1b[0m',
        '\\x1b[38;5;209mfoobar\\x1b[0m',
    ]) ==
        len_without_ansi(text) * 2)
# end function test_len_without_ansi


# Generated at 2022-06-13 21:10:20.677127
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert isinstance(text, str)
    assert text == '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:24.676233
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:10:34.702255
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mf\x1b[0moobar'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mf', 'o', 'obar\x1b[0m']
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:10:47.335195
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[1mfoobar') == 6
    assert len_without_ansi('\x1b[1mfoo\x1b[0mbar') == 6
    assert len_without_ansi('\x1b[1;7mfoo\x1b[0mbar') == 6
    # ANSI codes split the string into multiple substrings
    assert len_without_ansi('\x1b[1mfoo\x1b[0mbar\x1b[1mfoo\x1b[0m') == 12
    assert len_without_ansi(['foo', 'bar']) == 6

# Generated at 2022-06-13 21:10:50.818987
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:53.909924
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:01.379304
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Set up
    text = '\x1b[1m\x1b[38;5;238mfoobar\x1b[0m'
    expected = 6
    # Test
    assert len_without_ansi(text) == expected



# Generated at 2022-06-13 21:12:08.174644
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from nose.tools import assert_equal
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert_equal(len_without_ansi(text), 6)
    assert_equal(len_without_ansi([text, text]), 12)



# Generated at 2022-06-13 21:12:10.750753
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import doctest; doctest.testmod(optionflags=doctest.ELLIPSIS)



# Generated at 2022-06-13 21:12:15.351540
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:12:22.683884
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m')
    assert len_without_ansi(text) == 12
    return

# Generated at 2022-06-13 21:12:30.987585
# Unit test for function len_without_ansi

# Generated at 2022-06-13 21:12:37.745178
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test function :func:`flutils.txtutils.len_without_ansi`."""
    # 1
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    # 2
    text = '\x1b[38;5;209mfoo\x1b[0m'
    assert len_without_ansi(text) == 3



# Generated at 2022-06-13 21:12:44.042875
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[1mfoo\x1b[0m \x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 7



# Generated at 2022-06-13 21:12:49.448190
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:55.115712
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

