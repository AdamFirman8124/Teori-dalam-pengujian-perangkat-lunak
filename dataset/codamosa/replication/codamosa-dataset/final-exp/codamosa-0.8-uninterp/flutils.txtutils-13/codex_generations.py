

# Generated at 2022-06-13 21:05:44.135233
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """ Unit test for function :func:`len_without_ansi`. """
    from .helpers import get_results_str
    from .test_decorators import test_cached_property
    from .test_helpers import test_print_results
    from .type_vars import SequenceOfStr
    from .unittest_classes import (
        BaseTestCase,
        TestAttributes,
        TestCall,
        TestReturned,
    )


# Generated at 2022-06-13 21:05:49.604305
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar', '\x1b[0m']) == 6
    assert len_without_ansi(['xyzzy', '\x1b[38;5;209mfoobar', '\x1b[0m']) == 8

# Generated at 2022-06-13 21:05:52.476761
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 20
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:59.998215
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoo\x1b[38;5;39m\x1b[m\x1b[1mbar\x1b[0m'
    assert 'foobar' == text.replace('\x1b[m', '\x1b[0m')
    assert len('foobar') == len(text)
    assert 6 == len_without_ansi(text)
    assert 6 == len_without_ansi(text.split('\x1b[38;5;209m')[1])
    assert 6 == len_without_ansi(text.split('\x1b[0m')[0])

# Generated at 2022-06-13 21:06:09.298477
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['foo', '\x1b[38;5;209m', 'bar', '\x1b[0m']) == 3
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar') == 6
    assert len_without_ansi('foobar\x1b[0m') == 6



# Generated at 2022-06-13 21:06:17.291933
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', '\x1b[0m']) == 0

# Generated at 2022-06-13 21:06:22.811034
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi('test') == 4
    text = ['\x1b[38;5;209mfoobar', '\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:25.233242
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    if len_without_ansi(text) != 6:
        raise TypeError('Unit test for function len_without_ansi failed.')



# Generated at 2022-06-13 21:06:33.305699
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    color = ('\x1b[38;5;209m', '\x1b[0m')
    assert len_without_ansi([color[0], 'foobar', color[1]]) == 6
    assert len_without_ansi(['a', 'b', 'c', 'foo', 'bar']) == 6

# Generated at 2022-06-13 21:06:35.399288
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:08.163803
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text, text]) == 12



# Generated at 2022-06-13 21:07:13.189809
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['foo', '\x1b[38;5;209mbar\x1b[0m']
    assert len_without_ansi(text) == 3
# Allow indirect execution
del test_len_without_ansi



# Generated at 2022-06-13 21:07:20.419955
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert 0 == len_without_ansi('')
    assert 0 == len_without_ansi([''])
    assert 0 == len_without_ansi(['', ''])
    assert len(text) == len_without_ansi(text)
    assert 0 == len_without_ansi(textwrap.dedent('''
        \x1b[38;5;209mfoobar\x1b[0m
    '''))



# Generated at 2022-06-13 21:07:25.796167
# Unit test for function len_without_ansi
def test_len_without_ansi():
    out = len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m')
    assert out == 6
    out = len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m',
                            '\x1b[38;5;209mfoobar\x1b[0m'])
    assert out == 12


# Generated at 2022-06-13 21:07:31.270615
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', '12']) == 8
    assert len_without_ansi('foobar') == 6



# Generated at 2022-06-13 21:07:35.480532
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:47.396895
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from sys import version_info
    from flutils.txtutils import len_without_ansi
    from flutils.dotdict import DotDict

    class TestDotDict(DotDict):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.expected = kwargs['expected']


# Generated at 2022-06-13 21:07:57.508738
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert  len_without_ansi(text) == 6

    text = 'foo\x1b[0mbar'
    assert len_without_ansi(text) == 6

    text = ('\x1b[38;5;209mfoo\x1b[0m', 'bar')
    assert len_without_ansi(text) == 6

    text = '\x1b[38;5;209mfoo\x1b[0mbar\x1b[38;5;207mbaz'

# Generated at 2022-06-13 21:08:01.194577
# Unit test for function len_without_ansi
def test_len_without_ansi():
    _text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(_text) == 6



# Generated at 2022-06-13 21:08:04.926610
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:08:35.993371
# Unit test for function len_without_ansi
def test_len_without_ansi():
    seq_1 = 'foobar'
    seq_2 = '\x1b[38;5;209mfoobar\x1b[0m'
    out_1 = len_without_ansi(seq_1)
    out_2 = len_without_ansi(seq_2)
    assert out_1 == 6
    assert out_2 == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:08:46.159531
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    expected = 'foobar'
    actual = len_without_ansi(text)
    assert actual == len(expected)
    text = '\x1b[38;5;209m' + text + '\x1b[0m'
    expected = ['\x1b[38;5;209m', 'foobar', '\x1b[0m']
    actual = len_without_ansi(text)
    assert actual == len_without_ansi(expected)
    text = '\x1b[38;5;209m' + text + '\x1b[0m'
    expected = '\x1b[38;5;209mfoobar\x1b[0m'
    actual

# Generated at 2022-06-13 21:08:56.046349
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    seq = ['\\x1b[38;5;209mfoobar', '\\x1b[0m']
    assert len_without_ansi(seq) == 6
    seq = ['\\x1b[38;5;209mfoobar\\x1b[0m', '\\x1b[38;5;209mfoobar\\x1b[0m']
    assert len_without_ansi(seq) == 12


# Generated at 2022-06-13 21:09:09.364567
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(['foo', 'bar']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo', 'bar', '\x1b[0m']) == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foo', 'bar']) == 6
    assert len_without_ansi(['foo', 'bar', '\x1b[0m']) == 6
    assert len_without_ansi([]) == 0
    return
# Tests for function len_without_ansi



# Generated at 2022-06-13 21:09:16.214160
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for len_without_ansi"""
    from flutils.txtutils import len_without_ansi
    # Function len_without_ansi handles string
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    # Function len_without_ansi handles a tuple of strings
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi([text]) == 6
    # Function len_without_ansi handles a list of strings
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi([text]) == 6
test_len_without_ansi()

# Generated at 2022-06-13 21:09:18.056573
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa
    from .testing import run_doctest
    run_doctest(len_without_ansi, globals())



# Generated at 2022-06-13 21:09:23.644720
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    ans = len(text)
    out = len_without_ansi(text)
    assert ans == 9
    assert out == 6



# Generated at 2022-06-13 21:09:27.356642
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi."""
    seq = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(seq) == 6



# Generated at 2022-06-13 21:09:30.542526
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text + text) == 12
    assert len_without_ansi([text, text]) == 12



# Generated at 2022-06-13 21:09:40.333568
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    text = [c for c in '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m']
    out = len_without_ansi(text)
    assert out == 6
