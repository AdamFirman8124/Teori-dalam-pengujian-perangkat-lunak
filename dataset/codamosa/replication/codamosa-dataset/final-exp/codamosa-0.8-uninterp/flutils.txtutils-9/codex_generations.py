

# Generated at 2022-06-13 21:05:46.089165
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:05:57.486680
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m \x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 12
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m \x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ans

# Generated at 2022-06-13 21:06:01.331748
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:14.107236
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    # Type check
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(('foo', 'bar')) == 6
    # Strip ANSI codes
    assert len_without_ansi(
        '\x1b[38;5;209mfoobar\x1b[0m'
    ) == 6
    # Preserve non-ASCII characters
    assert len_without_ansi('bâr') == 3
    # Works with join
    assert len_without_ansi(['foo', 'bâr']) == 6
    # Works with list comprehension
    assert len_without_ansi([text for text in ['foo', 'bâr']]) == 6
    # Works with generator expression
    assert len_without_ans

# Generated at 2022-06-13 21:06:18.576468
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:06:30.449118
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('') == 0
    assert len_without_ansi('a') == 1
    assert len_without_ansi('abc') == 3
    assert len_without_ansi(('a', 'b', 'c')) == 3
    assert len_without_ansi(['a', 'b', 'c']) == 3
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6

# If the python version is >= 3.8

# Generated at 2022-06-13 21:06:33.983233
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """
    >>> from flutils.txtutils import len_without_ansi
    >>> text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    >>> len_without_ansi(text)
    6
    """



# Generated at 2022-06-13 21:06:40.618309
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = [
        '\x1b[38;5;209mfoo\x1b[0m',
        '\x1b[38;5;209mbar\x1b[0m',
        '\x1b[38;5;207mfoobar\x1b[0m',
    ]
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:06:43.925270
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6



# Generated at 2022-06-13 21:06:46.547727
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:21.269609
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    text = [
        '\x1b[38;5;209m',
        'hello',
        ' ',
        'world',
        '\x1b[0m',
    ]
    out = len_without_ansi(text)
    assert out == 11



# Generated at 2022-06-13 21:07:31.197852
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test for flutils.txtutils.len_without_ansi"""
    from flutils.txtutils import len_without_ansi

# Generated at 2022-06-13 21:07:35.068541
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['one', 'two', '\x1b[38;5;209m', 'three', '\x1b[0m']) == 3



# Generated at 2022-06-13 21:07:39.776731
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test function len_without_ansi."""
    from random import randrange
    from string import printable
    from flutils.txtutils import (
        ansi_text,
        ansi_style,
    )
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(str(ansi_text('foobar'))) == 6
    assert len_without_ansi(str(ansi_style('foobar', fg='red'))) == 6
    assert len_without_ansi(str(ansi_style('foobar', bg='red'))) == 6

# Generated at 2022-06-13 21:07:42.329033
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len(text) == 16
    assert len_without_ansi(text) == 6
    
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']) == 12

# class AnsiTextWrapper(object):

# Generated at 2022-06-13 21:07:47.264454
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Without ANSI codes
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi(' foo ') == 5
    # With ANSI codes
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:07:53.620544
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foo') == 3
    assert len_without_ansi(('foo', 'bar')) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', 'baz']) == 9



# Generated at 2022-06-13 21:07:58.730968
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6



# Generated at 2022-06-13 21:08:09.835142
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from .testing import flutils_eq
    from .testing import text
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    flutils_eq(
        len_without_ansi(text),
        6,
        test_name='len_without_ansi_str',
        docstring=len_without_ansi.__doc__,
    )
    text = [
        '\\x1b[38;5;209m',
        'foobar',
    ]
    flutils_eq(
        len_without_ansi(text),
        6,
        test_name='len_without_ansi_list',
        docstring=len_without_ansi.__doc__,
    )



# Generated at 2022-06-13 21:08:20.506912
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test the len_without_ansi function"""
    from flutils.pycompat import IS_PYTHON_2

    assert len_without_ansi('\x1b[31mfoo\x1b[0m') == 3
    assert len_without_ansi(('\x1b[31mfoo\x1b[0m',)) == 3
    assert len_without_ansi(['\x1b[31mfoo\x1b[0m']) == 3
    assert len_without_ansi(['\x1b[31mfoo\x1b[0m', 'bar']) == 6
    assert len_without_ansi(('\x1b[31mfoo\x1b[0m', 'bar')) == 6

# Generated at 2022-06-13 21:08:55.651616
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m']
    assert len_without_ansi(text) == 6
    text = ('\x1b[38;5;209mfoobar\x1b[0m',)
    assert len_without_ansi(text) == 6
    text = 'foobar'
    assert len_without_ansi(text) == 6
    text = ['foobar']
    assert len_without_ansi(text) == 6
    text = ('foobar',)
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:05.934276
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\\x1b[1mfoo\\x1b[0m bar\\x1b[1m\\x1b[38;5;209mbaz\\x1b[0m'
    assert len_without_ansi(text) == 8
# end function test_len_without_ansi



# Generated at 2022-06-13 21:09:08.546974
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# Generated at 2022-06-13 21:09:10.687195
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:14.936602
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:20.123415
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Single line
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    # Multiple lines
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m', '\x1b[38;5;209mfoobar\x1b[0m']) == 12

# Generated at 2022-06-13 21:09:25.214008
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    assert len_without_ansi(['foo', 'bar', 'baz']) == 9



# Generated at 2022-06-13 21:09:32.749570
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = '\x1b[38;5;173mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

    text = ('\x1b[38;5;173mfoo\x1b[38;5;4mbar\x1b[0m')
    assert len_without_ansi(text) == 6

    text = [
        '\x1b[38;5;173mfoo\x1b[38;5;4mbar\x1b[0m',
        'baz'
    ]
    assert len_without_ansi(text) == 9


# Generated at 2022-06-13 21:09:42.163520
# Unit test for function len_without_ansi
def test_len_without_ansi():  # pylint: disable=missing-docstring
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    out = len_without_ansi(text)
    assert out == 6
    seq = ['\x1b[38;5;209mfoobar\x1b[0m']
    out = len_without_ansi(seq)
    assert out == 6
    seq = ('\x1b[38;5;209mfoobar\x1b[0m', 'foo')
    out = len_without_ansi(seq)
    assert out == 9
test_len_without_ansi()


# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes

# Generated at 2022-06-13 21:09:50.347032
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Test string with ANSI codes
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    # Test list/tuple of strings
    text = ('\x1b[38;5;209mfoobar\x1b[0m', 'foobar')
    assert len_without_ansi(text) == 12
# end def test_len_without_ansi()



# Generated at 2022-06-13 21:10:13.885204
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = 'foo\x1b[3;5mbar\x1b[0mbaz'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:18.082297
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
# Test: test_len_without_ansi
test_len_without_ansi()



# Generated at 2022-06-13 21:10:30.277604
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m',) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m',
                            '\x1b[38;5;209mfoobar\x1b[0m') == 12

# Generated at 2022-06-13 21:10:45.060165
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[1m\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == len_without_ansi(('\x1b[1m', '\x1b[38;5;209m', 'foobar', '\x1b[0m'))
    assert not len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m')

# Generated at 2022-06-13 21:10:50.642785
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m\x1b[38;5;209mfoobar\x1b[0m') == 12
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m\x1b[38;5;209m\x1b[38;5;209mfoobar\x1b[0m\x1b[38;5;209m\x1b[0m') == 12



# Generated at 2022-06-13 21:10:55.288366
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = 'foobar'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:00.208856
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi([text]) == 6
    assert len_without_ansi([text, text]) == 12

# Generated at 2022-06-13 21:11:02.607099
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:11.035790
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test len_without_ansi() with a string."""
    assert len_without_ansi('\x1b[1;32mfoobar\x1b[0m') == 6
    # Ensure that len_without_ansi() can handle both sequences and string-like
    # objects.
    assert len_without_ansi(['\x1b[1;32m', 'foobar', '\x1b[0m', '\\']) == 7



# Generated at 2022-06-13 21:11:20.428173
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = ('\x1b[38;5;209mfoobar\x1b[0m'
            '\x1b[38;5;125m\x1b[48;5;235mhelloworld\x1b[0mworld\x1b[0m')
    assert len_without_ansi(text) == 22
    assert len_without_ansi(text.split()) == 5
    assert len_without_ansi(text.split()[0]) == 7
    assert len_without_ansi(text.split()[-1]) == 5
    text = 'foobarhelloworld'
    assert len_without_ansi(text) == 15
    assert len_without_ansi(text.split()) == 3
    assert len_without_ansi(text.split()[0]) == 6
