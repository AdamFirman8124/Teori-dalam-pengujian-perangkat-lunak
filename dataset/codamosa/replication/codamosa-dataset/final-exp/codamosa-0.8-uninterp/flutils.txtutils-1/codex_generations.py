

# Generated at 2022-06-13 21:05:01.546327
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:05:07.663784
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:05:12.278514
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:16.024906
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:19.920764
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[0mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\\x1b[0mfoobar\\x1b[0m', 'test']) == 10
# /test_len_without_ansi



# Generated at 2022-06-13 21:05:24.389599
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:34.523602
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(('foobar',)) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0m'
    assert len_without_ansi(text) == 3
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:05:37.164020
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('x\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:05:49.446786
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    # This is important; it should have the same effect as doing
    # len(['foobar'])
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;196mbar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;196mbar\x1b[0m']) == 6
    assert len_without

# Generated at 2022-06-13 21:05:53.101032
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:06:39.704377
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test functionality for the :func:`len_without_ansi` function."""
    tests = [
        (['be', '\x1b[38;5;209mfoobar', 'm'], 3),
        ('\x1b[38;5;209mfoobar\x1b[0m', 6),
        '\x1b[38;5;209mfoobar\x1b[0m',
        (['be', '', 'm'], 2),
    ]
    for test in tests:
        assert len_without_ansi(test[0]) == test[1]



# Generated at 2022-06-13 21:06:48.961402
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(['foo\x1b[31m', 'bar\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '\x1b[0m']) == 6


# Generated at 2022-06-13 21:06:53.033895
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:57.102720
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:08.954525
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('') == 0
    assert len_without_ansi('\x1b[0mfoobar\x1b[38;5;209m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[0mfoobar', '\x1b[38;5;209m']) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '\x1b[0m']) == 6

# Generated at 2022-06-13 21:07:12.484901
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text1 = '\x1b[38;5;209mfoobar'
    assert len_without_ansi(text1) == 6

# Generated at 2022-06-13 21:07:16.475835
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test 1
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:26.670388
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest

    text = ('\x1b[38;5;209mfoobar\x1b[0m',
            ['\x1b[38;5;209mfoob', 'a', '\x1b[38;5;209m', 'r', '\x1b[0m'])

    for seq in text:
        assert len_without_ansi(seq) == 6

    with pytest.raises(TypeError) as exc:  # pragma: no cover
        len_without_ansi(1)
    assert exc.match('must be a string or sequence of strings')

    with pytest.raises(TypeError) as exc:  # pragma: no cover
        len_without_ansi(1.0)
    assert exc.match('must be a string or sequence of strings')

   

# Generated at 2022-06-13 21:07:33.619102
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('\\x1b[38;5;209mfoo') == 3
    assert len_without_ansi('\\x1b[38;5;209mfoo\\x1b[0m') == 3
    assert len_without_ansi('\\x1b[38;5;209mfoo\\x1b[0mbar') == 6
    words = ['\\x1b[38;5;209mfoo', '\\x1b[0mbar']
    assert len_without_ansi(words) == 6



# Generated at 2022-06-13 21:07:46.427466
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .txtutils import len_without_ansi
    from .txtutils import _ANSI_RE
    from functools import reduce
    from operator import mul
    from random import choice
    from string import ascii_letters
    from typing import List, Optional
    from .types_ import RGBType


# Generated at 2022-06-13 21:08:03.124456
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:06.456983
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:11.148527
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6



# Generated at 2022-06-13 21:08:27.539038
# Unit test for function len_without_ansi

# Generated at 2022-06-13 21:08:31.376839
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:08:36.644390
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""
    test_seqs = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        ['\x1b[38;5;209m', 'foobar', '\x1b[0m'],
        ('\x1b[38;5;209m', 'foobar', '\x1b[0m')
    ]
    expected = 6
    for seq in test_seqs:
        assert len_without_ansi(seq) == expected



# Generated at 2022-06-13 21:08:42.877171
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6



# Generated at 2022-06-13 21:08:55.815396
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text_list = ['\\x1b[1msome text\\x1b[0m', ['\\x1b[0msome', 'other text\\x1b[0m']]
    assert(len_without_ansi(text_list) == 12)
    text_tuple = ('\\x1b[1msome text\\x1b[0m', ('\\x1b[0msome', 'other text\\x1b[0m'))
    assert(len_without_ansi(text_tuple) == 12)
    text_tuple = ('\\x1b[1msome text\\x1b[0m', ('\\x1b[0msome', 'other text\\x1b[0m'))
    assert(len_without_ansi(text_tuple) == 12)
    text_

# Generated at 2022-06-13 21:09:00.813448
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for :func:`len_without_ansi`."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:05.174860
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:28.758719
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    seq = ['\x1b[38;5;209mfoo\x1b[0m', 'bar']
    assert len_without_ansi(text) == 6
    assert len_without_ansi(seq) == 6

# Generated at 2022-06-13 21:09:34.593152
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:38.065223
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == len('foobar')



# Generated at 2022-06-13 21:09:44.024632
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('foobar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[0;32mbar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[0;32;42mbar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[0;32;42mbar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[0;32;42mbar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[0;32;42mbar\x1b[0m') == 6

# Generated at 2022-06-13 21:09:49.307927
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi((1, 2, 3)) == 3
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('12\x1b[42m3\x1b[0m') == 2
test_len_without_ansi()



# Generated at 2022-06-13 21:09:58.030882
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['foo', '\x1b[38;5;209mfoobar\x1b[0m', 'bar']
    assert len_without_ansi(text) == 9
    assert len_without_ansi(text[0]) == 3
    assert len_without_ansi(text[1]) == 3
    assert len_without_ansi(text[2]) == 3

test_len_without_ansi()  # type: ignore[no-unused-variable]
del test_len_without_ansi



# Generated at 2022-06-13 21:10:07.577892
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Without
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    # With multiline
    text = ['\x1b[38;5;209mfoo', '\x1b[0m', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
    # Without count
    text = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    assert len_without_ansi(text) == 6
    # Without count multiline

# Generated at 2022-06-13 21:10:11.371363
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .testutils import _check_constants_docstrs
    _check_constants_docstrs(len_without_ansi)



# Generated at 2022-06-13 21:10:15.469724
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('fo\x1b[3moo') == 3
    assert len_without_ansi(['foo bar', 'fo\x1b[3moo\x1b[0m']) == 7
    assert len_without_ansi('fo\x1b[3moo\x1b[0m') == 3



# Generated at 2022-06-13 21:10:21.070828
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert callable(len_without_ansi)

    # noinspection PyTypeChecker
    seq = '\x1b[38;5;209mfoobar\x1b[0m'
    assert isinstance(seq, str)
    assert len_without_ansi(seq) == 6

    seq = ['\x1b[38;5;209mfoobar\x1b[0m', 'baz']
    assert isinstance(seq, (tuple, list))
    assert len_without_ansi(seq) == 9



# Generated at 2022-06-13 21:12:54.116059
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test."""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:13:00.878177
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('foobar') == 6


# flutils.txtutils.AnsiTextWrapper

# Generated at 2022-06-13 21:13:06.601479
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[39m'
    ans = len_without_ansi(text)
    assert ans == 6



# Generated at 2022-06-13 21:13:14.224011
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    assert len_without_ansi(text) == 6
# end unit test for function len_without_ansi



# Generated at 2022-06-13 21:13:25.550497
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoo\x1b[0mbar') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6

# pylint: disable=too-many-ancestors



# Generated at 2022-06-13 21:13:32.205287
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\033[38;5;209mfoobar\033[0m') == 6



# Generated at 2022-06-13 21:13:39.830756
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from random import choice
    from string import ascii_lowercase
    from unittest import TestCase
    from unittest.mock import patch

    class TestLenWithoutAnsi(TestCase):
        @patch('flutils.txtutils.len')
        def test_with_string(self, mock_len):
            from flutils.txtutils import len_without_ansi
            mock_len.side_effect = len
            ansi_text = ''.join(choice(ascii_lowercase) for i in range(10))
            self.assertNotEqual(len(ansi_text), len_without_ansi(ansi_text))
            mock_len.assert_called_with(ansi_text)


# Generated at 2022-06-13 21:13:50.077255
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from hypothesis import given
    from .strategies import non_empty_str_lists
    @given(non_empty_str_lists)
    def test_pos(strl: List[str]):
        assert len_without_ansi(strl) >= 0
    test_pos()

    @given(non_empty_str_lists)
    def test_nonzero(strl: List[str]):
        assert len_without_ansi(strl) > 0
    test_nonzero()

    text = 'foobar'
    assert len_without_ansi(text) == len(text)
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == len('foobar')

# Generated at 2022-06-13 21:13:58.175947
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ['foo\x1b[38;5;209', 'bar']
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar']
    assert len_without_ansi(text) == 3


# Generated at 2022-06-13 21:14:04.948402
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert(len_without_ansi(text) == 6)
    text = ('\x1b[38;5;209mfoobar', 'bazqux\x1b[0m')
    assert(len_without_ansi(text) == 10)

