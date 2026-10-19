

# Generated at 2022-06-13 21:05:13.075830
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6

#: A tuple of ANSI escape sequences to wrap a string in to determine
#: the character length.
#:
#: *New in version 0.6*
_ANSI_LEN_TUP = tuple(chain(*map(_ANSI_RE.split, ['\x1b[0m', '\x1b[38;5;123m', '\x1b[48;5;123m'])))



# Generated at 2022-06-13 21:05:19.623365
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['test', '\x1b[38;5;209mfoobar\x1b[0m', 'test2']
    assert len_without_ansi(text) == 14



# Generated at 2022-06-13 21:05:24.501657
# Unit test for function len_without_ansi
def test_len_without_ansi():
    expected = 6
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == expected



# Generated at 2022-06-13 21:05:30.498889
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text]) == 12
    assert len_without_ansi(['foo', text, 'bar']) == 10



# Generated at 2022-06-13 21:05:35.815872
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:37.976821
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:45.417131
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar', '\x1b[0m']
    assert len_without_ansi(text) == 6
    return



# Generated at 2022-06-13 21:05:52.442244
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6


# Generated at 2022-06-13 21:05:59.979499
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .unittest_types_data import text_sequences
    from .unittest_tools import get_random_str
    for txt in text_sequences:
        ansi_txt1 = get_random_str(txt, '\x1b', '\x1b')
        ansi_txt2 = get_random_str(txt, '\x1b', '\x1b')
        ansi_txt3 = get_random_str(txt, '\x1b', '\x1b')
        ansi_txt = '{}{}{}'.format(ansi_txt1, ansi_txt2, ansi_txt3)
        assert len_without_ansi(txt) == len(txt)
        assert len_without_ansi(ansi_txt) == len(txt)
        assert len

# Generated at 2022-06-13 21:06:07.183599
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foobar']) == 6



# Generated at 2022-06-13 21:06:43.347419
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m\xf0') == 7


# Generated at 2022-06-13 21:06:46.431515
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6, 'len_without_ansi must return 6'



# Generated at 2022-06-13 21:06:49.603254
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:05.852680
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from itertools import chain
    from random import randint
    from string import ascii_letters
    from timeit import Timer

    def randstr(length):
        return ''.join([
            ascii_letters[randint(0, len(ascii_letters) - 1)]
            for _ in range(length)
        ])

    def randansi(length):
        return f'\033[{length}m'

    def wrap_text(text):
        """Test case for 'len_without_ansi' function with a wrapped cycle"""
        text = list(map(lambda i: f'{i:>3}', text))
        out = '\n'.join(text)
        return out


# Generated at 2022-06-13 21:07:11.287218
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar']) == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar')) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6

# Generated at 2022-06-13 21:07:15.774504
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi((text, text)) == 12



# Generated at 2022-06-13 21:07:18.657696
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:24.156336
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:07:33.971985
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo']) == 3
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar']) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo', '\x1b[0mbar']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo']) == 3

# Generated at 2022-06-13 21:07:35.652706
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = 6
    assert len_without_ansi(text) == out



# Generated at 2022-06-13 21:08:40.352093
# Unit test for function len_without_ansi
def test_len_without_ansi():
    '''Test :func:`flutils.txtutils.len_without_ansi`.
    '''
    import flutils.txtutils.tests.test_txtutils as test_data
    assert len_without_ansi(test_data.test_string) == len(
        test_data.test_string.replace('\x1b[38;5;209m', '').replace(
            '\x1b[0m', ''))
    for key, value in test_data.ancolor_dict.items():
        assert len_without_ansi(key) == len_without_ansi(value)



# Generated at 2022-06-13 21:08:48.748706
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi as lwa
    text_in = '\x1b[38;5;209mfoobar\x1b[0m'
    exp = 6
    obs = lwa(text_in)
    assert obs == exp
    lines = (text_in, text_in)
    exp = 12
    obs = lwa(lines)
    assert obs == exp



# Generated at 2022-06-13 21:09:00.878567
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;119mbar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;119mbar\x1b[0m']) == 6
    # Also check the chars in a list
    assert len_without_ansi(list('\x1b[38;5;209mfoobar\x1b[0m')) == 6

# Generated at 2022-06-13 21:09:11.927692
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = 'foo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    text = 'foobar'
    assert len_without_ansi(text) == 6
    text = ['foo', 'bar']
    assert len_without_ansi(text) == 6
    text = ['foo\x1b[0m', 'bar']
    assert len_without_ansi(text) == 6
    text = ['foo', '\x1b[0m', 'bar']
    assert len_without_ansi(text) == 6
    text = ['foo', '\x1b[0mbar']
    assert len

# Generated at 2022-06-13 21:09:16.823901
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6



# Generated at 2022-06-13 21:09:19.974969
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text1 = 'foobar'
    text2 = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text1) == len(text1)
    assert len_without_ansi(text2) == len(text1)



# Generated at 2022-06-13 21:09:24.420804
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = 6
    assert len_without_ansi(text) == ans



# Generated at 2022-06-13 21:09:32.281779
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test 1: single string with one ANSI code
    a = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(a) == 6
    # Test 2: list of strings with different ANSI codes
    b = ['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[1m\x1b[2m\x1b[38;2;0;150;150mbaz\x1b[0m']
    assert len_without_ansi(b) == 9
    # Test 3: single string of ANSI codes

# Generated at 2022-06-13 21:09:35.827140
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:47.502678
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m')
    assert len_without_ansi(text) == 12
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:10:18.959102
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6



# Generated at 2022-06-13 21:10:31.128592
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test the ANSI code remover."""
    import pytest
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    list_of_text = ['\x1b[38;5;209mfoobar', '\x1b[0m']
    assert len_without_ansi(list_of_text) == 6

    list_of_text = [
        '\x1b[38;5;208mfoobar', '\x1b[38;5;209mfoobar', '\x1b[0m'
    ]
    assert len_without_ansi(list_of_text) == 6


# Generated at 2022-06-13 21:10:40.240138
# Unit test for function len_without_ansi
def test_len_without_ansi():  # pragma: no cover
    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[0mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']) == 12

# Generated at 2022-06-13 21:10:48.374868
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo', 'bar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:10:57.460614
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;208mbar\x1b[0m\x1b[38;5;207mbaz\x1b[0m'
    assert len_without_ansi(text) == 9
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;208mbar\x1b[0m']) == 6



# Generated at 2022-06-13 21:11:00.166566
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:12.080436
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(['foo']) == 3
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(['foo' * 5, 'bar' * 5]) == 30
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m' * 5]) == 30

# Generated at 2022-06-13 21:11:16.025263
# Unit test for function len_without_ansi
def test_len_without_ansi():
    pass



# Generated at 2022-06-13 21:11:27.331215
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = [
        '\x1b[38;5;209mfoo\x1b[0m',
        '\x1b[38;5;209mbar\x1b[0m',
        '\x1b[38;5;209mbaz\x1b[0m',
    ]
    assert len_without_ansi(text) == 9
    pass



# Generated at 2022-06-13 21:11:32.777425
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test case 1
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:39.418984
# Unit test for function len_without_ansi
def test_len_without_ansi():
    import pytest
    from itertools import product
    from textwrap import dedent

    from flutils.txtutils import AnsiTextWrapper, len_without_ansi


# Generated at 2022-06-13 21:12:47.654281
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('foo\x1b[0mbar') == 6
    assert len_without_ansi('\x1b[0mfoo\x1b[0mbar\x1b[0m') == 6
    assert len_without_ansi('\x1b[0mfoo\x1b[0mb\x1b[0mr\x1b[0m') == 6
    assert len_without_ansi('fo\x1b[0mo\x1b[0mb\x1b[0mar\x1b[0m') == 6
    assert len_without_ansi('') == 0

# Generated at 2022-06-13 21:12:50.802820
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text]) == 12



# Generated at 2022-06-13 21:12:55.678591
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:03.794699
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6
    text = '\x1b[31mfoo\x1b[0m\x1b[32mbar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.split()) == 6
    text = '\x1b[31mfoo\x1b[0m \x1b[32mbar\x1b[0m'
    assert len_without_ansi(text) == 7
    assert len_without_ansi(text.split()) == 7



# Generated at 2022-06-13 21:13:08.577599
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoo', 'bar\x1b[0m')
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:16.750792
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text2 = [text, '\x1b[38;5;209mothers\x1b[0m']
    assert len_without_ansi(text2) == 13
# ----



# Generated at 2022-06-13 21:13:27.207338
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D103
    from pytest import raises
    from sys import intern
    from random import choice  # noqa: S404
    from string import ascii_letters, digits  # noqa: S404
    def all_letters() -> str:  # noqa: D103
        return ''.join(choice(ascii_letters + digits) for _ in range(40))

    assert len_without_ansi('') == 0
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(all_letters()) == len(all_letters())
    assert len_without_ansi('🤯') == 1
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi(['foo', '🤯']) == 4

   

# Generated at 2022-06-13 21:13:37.982604
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi('foobar\\x1b[0m') == 6
    assert len_without_ansi('\\x1b[38;5;209mfoobar') == 6
    assert len_without_ansi('\\x1b[38;5;209mf') == 1
    assert len_without_ansi('foob') == 4
    assert len_without_ansi('\\x1b[38;5;209\\x1b[0m') == 0
    assert len_without_ansi('\\x1b[38;5;209') == 0

# Generated at 2022-06-13 21:13:49.435200
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    out = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        '\x1b[0mfoo\x1b[38;5;209mbar\x1b[0m',
        '\x1b[38;5;209mfoo\x1b[0mbar',
    ]
    assert len_without_ansi(out[0]) == 6
    assert len_without_ansi(out[1]) == 12
    assert len_without_ansi(out[2]) == 6
    assert len_without_ansi(out) == 24

