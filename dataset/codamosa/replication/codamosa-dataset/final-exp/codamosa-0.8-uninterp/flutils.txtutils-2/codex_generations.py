

# Generated at 2022-06-13 21:06:05.106018
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:16.688868
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '\x1b[0m']) == 6


# The AnsiTextWrapper() class is patterned off of textwrap.TextWrapper.
# Its purpose is to provide an easy and automated way to handle ANSI
# codes in the text being wrapped.  The major difference between this
# and textwrap.TextWrapper() is that the returned value from wrap()
# is always a list of strings, instead of a single string.

# Generated at 2022-06-13 21:06:28.281918
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .test_helpers import HashableTestCase
    from .txtutils_tests import (
        TESTCASES as _TESTCASES,
    )
    class TestCase(HashableTestCase):
        pass
    for text, ansi_text in _TESTCASES:
        kw = {'ansi_text': ansi_text}
        if not text:
            kw['expected'] = 0
            testname = 'len_without_ansi_empty'
        elif text[0] == _ANSI_RE.split(ansi_text)[0]:
            kw['expected'] = len(text)
            testname = 'len_without_ansi_start'
        elif text[-1] == _ANSI_RE.split(ansi_text)[-1]:
            kw

# Generated at 2022-06-13 21:06:33.424302
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6


# Generated at 2022-06-13 21:06:40.214454
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('\x1b[38;5;209m') == 0
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar']) == 6
    assert len_without_ansi(['foo\x1b[38;5;209m', 'bar', '\x1b[0m']) == 6
    assert len_without_ansi(['foo\x1b[38;5;209m', 'bar\x1b[0m']) == 6
    assert len_without

# Generated at 2022-06-13 21:06:41.787008
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6



# Generated at 2022-06-13 21:06:44.538528
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:06:50.920562
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[36mfoobar\x1b[0m') == 6
    assert len_without_ansi(['foobar', '\x1b[36mfoobar\x1b[0m']) == 12
    assert len_without_ansi(['foobar', '\x1b[36mfoobar\x1b[0m', 'foobar']) == 18

# Generated at 2022-06-13 21:06:54.984665
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text: str = 'foo\x1b[43;30mbar\x1b[0m'
    assert len_without_ansi(text) == 3



# Generated at 2022-06-13 21:06:57.102246
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0



# Generated at 2022-06-13 21:07:34.456495
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Return the results of the unit tests for len_without_ansi.
    """
    seq = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(seq) == 6
    seq = '\\x1b[31m\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(seq) == 6
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi(['foobar', 'baz']) == 9



# Generated at 2022-06-13 21:07:46.939841
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # pylint: disable=unused-variable
    from flutils.txtutils import len_without_ansi
    log = []
    text = 'hello'
    assert len_without_ansi(text) == 5
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:07:53.290593
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6



# Generated at 2022-06-13 21:07:56.100095
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi
    """
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:08:07.444793
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from random import randint

    text = '\x1b[38;5;{}mfoobar\x1b[0m'
    for i in range(0, 256):
        assert len_without_ansi(text.format(i)) == 6
    assert len_without_ansi('\x1b[1mfizz\x1b[0mbuzz') == 8
    assert len_without_ansi(list('\x1b[0mfoobar')) == 6
    assert len_without_ansi(tuple('\x1b[38;5;9mfoobar')) == 6
    assert len_without_ansi(['\x1b[38;5;9m', 'f', 'oob', 'ar']) == 6

# Generated at 2022-06-13 21:08:12.796946
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:17.673607
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 16
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:08:23.135714
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209mfoobar\x1b[0m', 'foobar')) == 12



# Generated at 2022-06-13 21:08:31.247195
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test return value when given a string
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    # Test return value when given a list of strings
    text = ['\x1b[38;5;209mfoobar', '\x1b[0m']
    assert len_without_ansi(text) == 6

    # Test return value when given a tuple of strings
    text = ('\x1b[38;5;209mfoobar', '\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:33.251110
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:09:30.633589
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from . import tst

    _in = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        ['\x1b[38;5;209m', 'foobar', '\x1b[0m'],
    ]
    _out = [
        6, 6
    ]
    _tst = [
        (i, o) for i, o in zip(_in, _out) if len_without_ansi(i) != o
    ]
    if _tst:
        _failing_in = [i for i, _ in _tst]
        _failing_out = [o for _, o in _tst]

# Generated at 2022-06-13 21:09:40.650842
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('yes') == 3
    assert len_without_ansi('no') == 2
    assert len_without_ansi('can') == 3
    assert len_without_ansi('do') == 2
    assert len_without_ansi('') == 0
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(
        [
            '\x1b[38;5;209mfoobar\x1b[0m',
            '\x1b[38;5;209mfoobar\x1b[0m',
        ]
    ) == 12



# Generated at 2022-06-13 21:09:51.298391
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['\x1b[0m']) == 0
    assert len_without_ansi('\x1b[0m') == 0
    assert len_without_ansi(['\x1b[0m', 'foobar']) == 6
    assert len_without_ansi('\x1b[0mfoobar') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:09:57.254206
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = 'foo bar\x1b[38;5;209m\x1b[48;5;234mfoobar\x1b[0m'
    assert len_without_ansi(text) == 9



# Generated at 2022-06-13 21:09:59.825692
# Unit test for function len_without_ansi
def test_len_without_ansi():
    txt = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(txt) == 6



# Generated at 2022-06-13 21:10:05.579401
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # This helper function will be used as a fixture in a unit test
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6
    assert len_without_ansi([text, text]) == 12



# Generated at 2022-06-13 21:10:10.226804
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# end unit test



# Generated at 2022-06-13 21:10:20.376859
# Unit test for function len_without_ansi
def test_len_without_ansi():  # pragma: no cover
    from .itertools import color
    from .types import Color
    from .utils import get_random_string
    from .flutils import equals_to_precision

    func = len_without_ansi

    str_ = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = 6
    out = func(str_)
    assert out == ans, (out, ans)

    str_ = get_random_string(size=20)
    str_ = color(str_[:10], foreground=Color.blue) + str_[10:]
    ans = 20
    out = func(str_)
    assert out == ans, (out, ans)

    str_ = get_random_string(size=20)

# Generated at 2022-06-13 21:10:23.529145
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:35.129579
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test ``len_without_ansi`` function."""
    assert len_without_ansi('abc') == 3
    assert len_without_ansi('\x1b[1mabc') == 3
    assert len_without_ansi('abc\x1b[0m') == 3
    assert len_without_ansi('\x1b[1mabc\x1b[0m') == 3
    assert len_without_ansi('\x1b[1mab') == 2
    assert len_without_ansi('ab\x1b[0m') == 2
    assert len_without_ansi('abc\x1b[0mdef') == 3
    assert len_without_ansi('\x1b[1mabc\x1b[0mdef') == 3
    assert len_without_ans

# Generated at 2022-06-13 21:11:07.760828
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
test_len_without_ansi()
del test_len_without_ansi



# Generated at 2022-06-13 21:11:11.446696
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:20.635147
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = len_without_ansi(text)
    assert ans == 6

# Generated at 2022-06-13 21:11:23.177446
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:11:36.921152
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from shutil import get_terminal_size

    cols, *_ = get_terminal_size()
    text_with_ansi = '\x1b[31mfoo\x1b[0m'
    assert isinstance(text_with_ansi, str)
    assert len_without_ansi(text_with_ansi) == len(text_with_ansi) - 8
    assert len_without_ansi([text_with_ansi]) == len(text_with_ansi) - 8
    assert len_without_ansi([text_with_ansi, text_with_ansi]) == \
        len(text_with_ansi) - 8



# Generated at 2022-06-13 21:11:46.107622
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test for function len_without_ansi."""
    from flutils.txtutils import len_without_ansi
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    text = ['\\x1b[38;5;209m0\\x1b[0m', '\\x1b[38;5;209m1\\x1b[0m', '2 3']
    assert len_without_ansi(text) == 6
    assert len_without_ansi('foo bar') == 7



# Generated at 2022-06-13 21:11:49.908820
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:55.724414
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['one', 'two']
    assert len_without_ansi(text) == 7
test_len_without_ansi()



# Generated at 2022-06-13 21:11:57.937712
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6


# Generated at 2022-06-13 21:12:06.863673
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function :func:`len_without_ansi`."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        '\x1b[38;5;208mbaz\x1b[0m',
    ]
    assert len_without_ansi(text) == 10
test_len_without_ansi()



# Generated at 2022-06-13 21:12:58.387157
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6



# Generated at 2022-06-13 21:13:02.513977
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import doctest
    doctest.testmod(
        name='len_without_ansi',
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
    )



# Generated at 2022-06-13 21:13:13.974588
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi(('\\x1b[38;5;209mfoo', 'bar\\x1b[0m')) == 6
    assert len_without_ansi(('\\x1b[38;5;209mfoo', 'bar\\x1b[0m')) == 6
    text = '\\x1b[38;5;209mfoobar\\x1b[0m\\x1b[38;5;209mfoobar\\x1b[0m'
   

# Generated at 2022-06-13 21:13:19.839332
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 15
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text]) == 6
    assert len_without_ansi((text, text)) == 6
    assert len_without_ansi([text, text]) == len_without_ansi((text, text))
    assert len_without_ansi(text + text) == len_without_ansi([text, text])
    assert len_without_ansi(text + text) == len_without_ansi((text, text))
    assert len_without_ansi([text + text, text + text]) == len_without_ansi(
        (text, text)
    )
    assert len_

# Generated at 2022-06-13 21:13:25.859987
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:32.479778
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 19
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:36.289811
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:43.719518
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test function for len_without_ansi."""
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:13:47.144276
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# Original method by Lennart Regebro: http://stackoverflow.com/a/3006636

# Generated at 2022-06-13 21:13:52.612946
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoo', '\x1b[0mbar')
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text * 1000) == 6 * 1000
# Test for function len_without_ansi
test_len_without_ansi()


_ANSI_RE_WITH_CODE = re.compile(
    '(\\x1b\\[([0-9;:]+)[ABCDEFGHJKSTfhilmns])'
)