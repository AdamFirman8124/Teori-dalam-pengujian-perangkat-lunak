

# Generated at 2022-06-13 21:05:40.382401
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi

    assert len_without_ansi('\x1b[38;5;209mfoobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:05:44.879422
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foo', 'bar', 'baz']) == 9
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text, text]) == 18

# Custom TextWrapper class to selectively ignore
# ANSI codes when determining the length of given
# strings

# Generated at 2022-06-13 21:05:46.881429
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:05:57.840550
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test flutils.txtutils.len_without_ansi
    """
    from flutils.txtutils import len_without_ansi

    seq = 'foobar'
    assert len_without_ansi(seq) == 6

    seq = 'foo\x1bbbar'
    assert len_without_ansi(seq) == 6

    seq = 'foo\x1bbbarbaz'
    assert len_without_ansi(seq) == 9

    seq = '\x1b[0mfoo'
    assert len_without_ansi(seq) == 3

    seq = '\x1b[0mfoo\x1b[1mbar'
    assert len_without_ansi(seq) == 6

    seq = '\x1b[1mbazfoo\x1b[0mbar'

# Generated at 2022-06-13 21:06:01.814793
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:05.378785
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:10.401417
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    print('test_len_without_ansi: PASS')



# Generated at 2022-06-13 21:06:22.239820
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.generalutils import get_called_function_name
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(
        '\x1b[38;5;209mfoobar\x1b[0m',
    ) == 6
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi(('foobar',)) == 6
    assert len_without_ansi(('\x1b[38;5;209mfoo\x1b[0m', 'bar')) == 6

# Generated at 2022-06-13 21:06:33.678334
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from pytest import raises
    from .exceptions import FlutilsTypeError

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6

    with raises(FlutilsTypeError):
        len_without_ansi(None)  # type: ignore[arg-type]
    with raises(FlutilsTypeError):
        len_without_ansi(['foo', 1])  # type: ignore[arg-type]
    with raises(FlutilsTypeError):
        len_without_ansi(['foo', ['bar']])  # type: ignore[arg-

# Generated at 2022-06-13 21:06:38.059073
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi(['\\x1b[38;5;209m', 'foobar', '\\x1b[0m']) == 6
    assert len_without_ansi(['\\x1b[38;5;209m' 'foobar', '\\x1b[0m']) == 6



# Generated at 2022-06-13 21:07:09.133195
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi((text,)) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:07:15.140810
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    len_without_ansi(text)

    text = 'foobar'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:21.070248
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi([
        '\x1b[38;5;209m',
        'foo',
        '\x1b[38;5;46mbar',
        '\x1b[0mbaz',
    ]) == 10



# Generated at 2022-06-13 21:07:32.312312
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209m\x1b[0m\x1b[38;5;209mbar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;209m\x1b[0m', '\x1b[38;5;209mbar\x1b[0m']) == 6



# Generated at 2022-06-13 21:07:45.151777
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from pytest import raises
    from flutils.txtutils import len_without_ansi

    # Test 1
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    # Test 2
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    text = list(text)
    assert len_without_ansi(text) == 6

    # Test 3
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6

    # Test 4
    text = '\x1b[38;5;209mfoo\x1b[0mbar'

# Generated at 2022-06-13 21:07:55.984374
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .basetest import BaseTest
    from .decorators import b
    from .objectutils import BaseObject
    from .txtutils import len_without_ansi

    class Test(BaseTest):
        def test_len_without_ansi(self):
            oo = BaseObject()
            text = '\x1b[38;5;209mfoobar\x1b[0m'
            self.assertEqual(
                len(text),
                len_without_ansi(text),
            )
            text = oo.join(
                '\x1b[38;5;209mfoobar\x1b[0m',
                '\x1b[38;5;209mbaz\x1b[0m',
            )

# Generated at 2022-06-13 21:07:58.486470
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[45;7mfoo\x1b[0m') == 3
    assert len_without_ansi(['\x1b[45;7mfoo\x1b[0m']) == 3



# Generated at 2022-06-13 21:08:08.356315
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .testutils import AssertRaisesJunk

    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(
        '\x1b[38;5;209mfoo\x1b[0mbar\x1b[38;5;209mbaz\x1b[0m'
    ) == 9

    with AssertRaisesJunk('`seq` must be a sequence of strings'):
        len_without_ansi(None)



# Generated at 2022-06-13 21:08:20.249542
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for :func:`len_without_ansi`"""
    arg = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(arg) == 6
    arg = [
        '\\x1b[38;5;209mfoo',
        'bar',
        '\\x1b[0m',
    ]
    assert len_without_ansi(arg) == 6
    arg = ['\\x1b[38;5;209mfoo', 'bar', '\\x1b[0m']
    assert len_without_ansi(arg) == 6
    arg = [
        '\\x1b[38;5;209mfoo',
        'bar',
        '\\x1b[0m',
    ]
    assert len

# Generated at 2022-06-13 21:08:28.183024
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    #
    text = [
        '\x1b[38;5;209mfoobar\x1b[0m',
        '\x1b[7;1mbaz\x1b[0m',
        'bal',
    ]
    assert len_without_ansi(text) == 11



# Generated at 2022-06-13 21:09:05.091780
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test function len_without_ansi.

    *New in version 0.6*

    """
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
# !Unit test for function len_without_ansi



# Generated at 2022-06-13 21:09:13.687854
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""
    _GENS = [
        (_[0], len_without_ansi(_[0]), _[1]) for _ in [
            ('\x1b[31mfoo\x1b[0m bar', 7),
            (['foo', 'bar'], 6),
            (('foo', 'bar'), 6),
            (['\x1b[31mfoo\x1b[0m', 'bar'], 6),
            (('\x1b[31mfoo\x1b[0m', 'bar'), 6),
        ]
    ]

# Generated at 2022-06-13 21:09:22.034235
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi('\\x1b[38mfoo\\x1b[0m') == 3
    assert len_without_ansi(['\\x1b[38m', 'foo', '\\x1b[0m']) == 3
    assert len_without_ansi(['\\x1b[38mfoo']) == 3
    assert len_without_ansi(['\\x1b[38m', 'foo']) == 3
    assert len_without_ansi(['\\x1b[38;5;209mfoobar']) == 6

# Generated at 2022-06-13 21:09:24.951782
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:30.351613
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi(['\\x1b[38;5;209m', 'foobar', '\\x1b[0m']) == 6
    assert len_without_ansi(('\\x1b[38;5;209m', 'foobar', '\\x1b[0m')) == 6



# Generated at 2022-06-13 21:09:40.821423
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from pytest import raises
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(iter(text)) == 6
    assert len_without_ansi([text, text]) == 12
    assert len_without_ansi(iter([text, text])) == 12
    raises(ValueError, len_without_ansi, [None])
    assert len_without_ansi('\x1b[31mmfoobar\x1b[0m') == 1
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['']) == 0
    assert isinstance(len_without_ansi(''), int)

# Generated at 2022-06-13 21:09:51.704496
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209', 'mfoobar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209', 'mfoobar\x1b[0m')
    assert len_without_ansi(text) == 6
# Unit tests for class AnsiTextWrapper

# Generated at 2022-06-13 21:10:04.836134
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:10:09.483522
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:13.172139
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:41.391745
# Unit test for function len_without_ansi
def test_len_without_ansi():
    exp = 6
    act = len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m')
    assert exp == act

    text = ['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']
    exp = 12
    act = len_without_ansi(text)
    assert exp == act

    text = ['foo\x1b[38;5;209mbar\x1b[0m', 'baz']
    exp = 8
    act = len_without_ansi(text)
    assert exp == act



# Generated at 2022-06-13 21:10:45.221139
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:48.257161
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(list(text)) == 6



# Generated at 2022-06-13 21:10:51.267833
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils.len_without_ansi import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:55.408827
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6



# Generated at 2022-06-13 21:11:07.054236
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test the function len_without_ansi."""
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[31mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[31m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi('\x1b[31mfoobar') == 6
    assert len_without_ansi('foobar\x1b[0m') == 6
    assert len_without_ansi('foo\x1b[31mbar') == 6
    assert len_without_ansi('foobar\x1b[0mfoo') == 9

# Generated at 2022-06-13 21:11:10.900116
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:20.616545
# Unit test for function len_without_ansi

# Generated at 2022-06-13 21:11:24.567384
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:37.648569
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import TextWrapper
    from .ansi import ansi
    from .random_ import random_sample
    from .utils import make_random_bytes
    from .utils import make_random_string

    wrapper = TextWrapper(
        width=10,
        fix_sentence_endings=True,
        expand_tabs=False,
        replace_whitespace=True,
        break_long_words=True,
        drop_whitespace=True,
        break_on_hyphens=True,
        max_lines=None,
        placeholder=None,
        tabsize=None,
    )
    # -------------------------------------------------------------------------
    # Test case: text
    # -------------------------------------------------------------------------
    text = wrapper.fill(random_sample('abcdefghijklmnopqrstuvwxyz'))
   

# Generated at 2022-06-13 21:12:23.937985
# Unit test for function len_without_ansi
def test_len_without_ansi():
    test_value1 = '\x1b[38;5;209mfoobar\x1b[0m'
    test_value2 = ['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']
    test_value3 = ('\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m')
    assert len_without_ansi(test_value1) == 6
    assert len_without_ansi(test_value2) == 6
    assert len_without_ansi(test_value3) == 6



# Generated at 2022-06-13 21:12:33.460692
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('\x1b[30mblah blah\x1b[0m') == len('blah blah') == 9
    assert len_without_ansi('\x1b[30mbla\x1b[0mh \x1b[30mbla\x1b[0mh') == 9
    assert len_without_ansi('\x1b[30mblah \x1b[1mblah\x1b[0m') == 9
    assert len_without_ansi('\x1b[1m\x1b[30mblah \x1b[1mblah\x1b[0m') == 9

# Generated at 2022-06-13 21:12:37.458915
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi([]) == 0
    assert len_without_ansi(['a', 'b', 'c']) == 3
    assert len_without_ansi(['\x1b[1;37mfoobar\x1b[0m']) == 6
    assert len_without_ansi('\x1b[1;37mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:12:44.000057
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:12:51.049813
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('abc', '\x1b[38;5;209m', 'def')) == 6
    assert len_without_ansi(['abc', '\x1b[38;5;209m', 'def']) == 6



# Generated at 2022-06-13 21:12:56.278400
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['foo', 'bar']) == 3
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6



# Generated at 2022-06-13 21:13:04.449463
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar', '\x1b[0m']
    assert len_without_ansi(text) == 6
    text = '\n'.join(text)
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:13:10.582171
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[1mbaz', '\x1b[38;5;209mfoobar\x1b[2;0m']
    assert len_without_ansi(text) == 9

# Generated at 2022-06-13 21:13:18.268438
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = 'X\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 0
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:20.696245
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:13:58.894631
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test len_without_ansi()"""
    assert len_without_ansi('\x1b[4;3mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[4;3mfoobar\x1b[0m',)) == 6
    assert len_without_ansi(['\x1b[4;3mfoobar\x1b[0m']) == 6
    assert len_without_ansi(('\x1b[4;3mfoobar\x1b[0m', '\x1b[2mbaz\x1b[0m')) == 9

# Generated at 2022-06-13 21:14:02.488459
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:14:09.174308
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test function len_without_ansi."""
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
test_len_without_ansi()

