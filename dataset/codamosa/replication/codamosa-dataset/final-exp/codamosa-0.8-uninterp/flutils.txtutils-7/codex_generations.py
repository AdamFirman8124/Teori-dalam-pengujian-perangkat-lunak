

# Generated at 2022-06-13 21:06:28.580356
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('foöbar') == 7
    assert len_without_ansi('foo̅̊bar') == 7
    assert len_without_ansi('foo̅̊bar') == 7
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(['føø', 'bår']) == 7
    assert len_without_ansi(['fōō', 'bar']) == 7
    assert len_without_ansi(['foo', 'bār']) == 7
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi(('føø', 'bår')) == 7
    assert len

# Generated at 2022-06-13 21:06:37.129571
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from textwrap import wrap
    from itertools import chain
    from functools import reduce

    for i in range(6):
        text = ['foobar', 'blah', '\x1b[38;5;209mfoo\x1b[0m']
        new_text = []
        for c in chain.from_iterable(map(wrap, text)):
            new_text.append('\x1b[38;5;209m' + c + '\x1b[0m')
        new_text = reduce(lambda x, y: x + y, new_text)
        new_text_len = len(new_text)
        new_text_len_no_ansi = len_without_ansi(new_text)

# Generated at 2022-06-13 21:06:42.209248
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text_1 = "\x1b[38;5;209mfoobar\x1b[0m"
    assert len_without_ansi(text_1) == 6
    seq = [text_1, text_1]
    assert len_without_ansi(seq) == 12

# Generated at 2022-06-13 21:06:46.348926
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:06:57.520904
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from os import devnull
    from sys import stdout as _stdout
    from sys import stdin as _stdin
    from sys import stderr as _stderr
    from subprocess import run as _run, PIPE as _PIPE
    from unittest import TestCase as _TestCase

    __cwd__ = '.'

    class TestCase(_TestCase):
        maxDiff = None
        __slots__ = ()
        LONG_ARGS = ['-v', '-v', '-v'] + ['-vv'] * 5
        def __init__(self, *args, **kwargs) -> None:
            if not kwargs.get('verbose', None):
                out = _PIPE
            else:
                kwargs.pop('verbose')
                out = None
            self.__args

# Generated at 2022-06-13 21:06:59.578870
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D103
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:07:04.317418
# Unit test for function len_without_ansi
def test_len_without_ansi(): pass  # pragma: no cover

if __name__ == '__main__':  # pragma: no cover
    import pytest
    pytest.main([__file__])



# Generated at 2022-06-13 21:07:12.137634
# Unit test for function len_without_ansi
def test_len_without_ansi(): # noqa: D103
    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\\x1b[1mfoobar\\x1b[0m') == 6
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi(('\\x1b[1mfoo', 'bar\\x1b[0m')) == 6
    assert len_without_ansi(('\\x1b[38;5;209mfoo', 'bar\\x1b[0m')) == 6



# Generated at 2022-06-13 21:07:15.451723
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:07:24.054683
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = len_without_ansi(text)
    assert ans == 6
    text = [
        '\x1b[38;5;209mfoo',
        'bar\x1b[0m',
    ]
    ans = len_without_ansi(text)
    assert ans == 6
    text = 'foobar'
    ans = len_without_ansi(text)
    assert ans == 6
    text = [
        'foo',
        'bar',
    ]
    ans = len_without_ansi(text)
    assert ans == 6



# Generated at 2022-06-13 21:08:16.601424
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Tests for function len_without_ansi."""
    text = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    assert len_without_ansi(text) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:08:28.361588
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo\x1b[0m', 'bar']
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    assert len_without_ans

# Generated at 2022-06-13 21:08:32.106649
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi as l
    assert l('foobar') == 6
    assert l(['foo', 'bar']) == 6



# Generated at 2022-06-13 21:08:44.259782
# Unit test for function len_without_ansi
def test_len_without_ansi():
    try:
        len_without_ansi(None)
    except (TypeError, IndexError):
        pass
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6
    assert len_without_ansi(None) == 0
    assert len_without_ansi('foo') == 3
    assert len_without_ansi([]) == 0
    assert len_without_ansi(['foo']) == 3



# Generated at 2022-06-13 21:08:52.893316
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len(text) == 18
    texts = ['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;19mbaz\x1b[0m']
    assert len_without_ansi(texts) == 9
    assert sum(map(len, texts)) == 32



# Generated at 2022-06-13 21:08:57.889529
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6



# Generated at 2022-06-13 21:09:04.716239
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    seq = list(text)
    out = len_without_ansi(seq)
    assert out == 6



# Generated at 2022-06-13 21:09:09.141166
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:16.094997
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = 'abc\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 9
    text = 'abc\x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 9
    text = 'abc\x1b[38;5;209m\x1b[0mbar'
    assert len_without_ansi(text) == 9

# Generated at 2022-06-13 21:09:22.398390
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = 'a \x1b[38;5;209mfoobar\x1b[0m b'
    assert len_without_ansi(text) == 7
    text = '\x1b[38;5;209mfoobar\x1b[0m xyz'
    assert len_without_ansi(text) == 9
    text = ('\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobaz\x1b[0m')
    assert len_without_ansi(text) == 12

# Generated at 2022-06-13 21:10:40.424024
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    tnum = len_without_ansi(text)
    assert tnum == 6



# Generated at 2022-06-13 21:10:48.181159
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209mfoobar\x1b[0m', 'baz')) == 9
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', 'baz']) == 9



# Generated at 2022-06-13 21:10:51.190145
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """
    Test the len_without_ansi() function.
    """
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 16
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:57.560016
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split('\x1b[0m')) == 6
    assert len_without_ansi([text, text]) == 12
# -- end unit tests



# Generated at 2022-06-13 21:11:03.279562
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 6


_NUM_REGEX = re.compile('[0-9]+')



# Generated at 2022-06-13 21:11:15.591838
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from pytest import mark


# Generated at 2022-06-13 21:11:21.307577
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['foo', 'bar']) == 6



# Generated at 2022-06-13 21:11:31.580266
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import flutils
    assert flutils.len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert flutils.len_without_ansi(['a', '\x1b[38;5;209mfoobar\x1b[0m', 'b']) == 6
    assert flutils.len_without_ansi('\x1b[38;5;209mfoobar') == 7
    # Test non-ascii characters
    assert flutils.len_without_ansi('\x1b[38;5;209mfööbär\x1b[0m') == 8

# Generated at 2022-06-13 21:11:34.852943
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from doctest import testmod
    testmod()



# Generated at 2022-06-13 21:11:37.716914
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:55.695383
# Unit test for function len_without_ansi
def test_len_without_ansi():
    for text in [
            '\x1b[38;5;209mfoobar\x1b[0m',
            '\x1b[38;5;209mfoobar\x1b[0m\x1b[0m',
            'foobar',
            []
    ]:
        assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:02.189827
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text]) == 12



# Generated at 2022-06-13 21:13:03.886562
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:09.459877
# Unit test for function len_without_ansi
def test_len_without_ansi():
    '''
    Test for module function len_without_ansi
    '''
    from ..txtutils import len_without_ansi
    # Function to compare if objects are equal
    def test_eq(obj1, obj2):
        return obj1 == obj2
    # Test text
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    # Test results.
    expected = 6
    actual = len_without_ansi(text)
    # Show test results
    print("Testing len_without_ansi")
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("Passed:  ", test_eq(actual, expected))



# Generated at 2022-06-13 21:13:17.095799
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    texts = ('\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;215mfoobar\x1b[0m')
    assert len_without_ansi(texts) == 12



# Generated at 2022-06-13 21:13:27.223567
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest

# Generated at 2022-06-13 21:13:32.828919
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert isinstance(out, int)
    assert out == 6
    return True



# Generated at 2022-06-13 21:13:36.289926
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:13:40.505810
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:43.120071
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[1mfoo\x1b[0m'
    assert len_without_ansi(text) == 3

