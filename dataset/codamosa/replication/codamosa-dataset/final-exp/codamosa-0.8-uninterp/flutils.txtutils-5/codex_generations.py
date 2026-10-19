

# Generated at 2022-06-13 21:06:17.399670
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:20.397014
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
test_len_without_ansi()



# Generated at 2022-06-13 21:06:32.336403
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Test :func:`len_without_ansi`.
    """
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoobar\x1b[0m \x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 12
    text = '\x1b[38;5;209mfoobar\x1b[0m \x1b[38;5;209mbar\x1b[0m'
    assert len_without_ansi(text) == 11

# Generated at 2022-06-13 21:06:34.508164
# Unit test for function len_without_ansi
def test_len_without_ansi():
    s = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(s) == 6



# Generated at 2022-06-13 21:06:45.038152
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    text2 = 'foo\x1b[38;5;209mbar'
    text3 = '\x1b[38;5;209mbaz\x1b[0m'
    line = ['foo\x1b[38;5;209mbar', 'baz\x1b[0m']
    assert len_without_ansi(text) == cast(int, 6)
    assert len_without_ansi(text2) == cast(int, 6)
    assert len_without_ansi(text3) == cast(int, 3)
    assert len_without_ansi(line) == cast(int, 9)



# Generated at 2022-06-13 21:06:49.785100
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = '\x1b[38;5;209mfoo\x1b[0mbar'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoo\x1b[0m', 'bar']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:06:58.413771
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi(['foo', 'bar']) == 6


# Generated at 2022-06-13 21:07:03.187692
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:07:10.010921
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m', 'baz']
    assert len_without_ansi(text) == 9
    text = ('\x1b[38;5;209mfoobar\x1b[0m', 'baz')
    assert len_without_ansi(text) == 9



# Generated at 2022-06-13 21:07:22.435245
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


if hexversion >= 0x03080000:
    class AnsiTextWrapper(TextWrapper):
        """This class is used to wrap text so that it fits within the
        specified width, taking ANSI code length into consideration.
        It has the same API as :obj:`textwrap.TextWrapper`.

        *New in version 0.6*
        """

        @cached_property
        def ansi_code_to_len(self) -> dict:
            """Create a dictionary to keep track of the ANSI code length.

            :rtype:
                :obj:`dict`
            """

# Generated at 2022-06-13 21:10:36.300281
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = "\x1b[38;5;209mfoobar\x1b[0m"
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:10:48.049901
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from random import choice
    from string import ascii_lowercase
    from ._compat import range

    for i in range(500):
        length = choice(range(20, 100))
        text = ''.join(choice(ascii_lowercase) for _ in range(length))
        if i % 2 == 0:
            ansi = '\x1b[38;5;209m'
            ansi2 = '\x1b[0m'
            s = 0
            e = len(ansi) + len(ansi2)
            text = ''.join((ansi, text[s:e], ansi2, text[e:]))
            assert len_without_ansi(text) == len(text) - len(ansi) - len(ansi2)
        else:
            assert len_without_

# Generated at 2022-06-13 21:10:56.034908
# Unit test for function len_without_ansi
def test_len_without_ansi():  # pylint: disable=too-many-statements
    """Unit test for function len_without_ansi."""
    from flutils.txtutils import len_without_ansi
    from flutils.pyutils import is_string
    from flutils.txtutils import validate_text
    from .testutils import rand_str

    assert len_without_ansi(validate_text('')) == 0
    assert len_without_ansi(validate_text('a')) == 1
    assert len_without_ansi(validate_text(rand_str(10))) == 10

    assert len_without_ansi(('\x1b[38;5;209m', 'foobar', '\x1b[0m')) == 6

# Generated at 2022-06-13 21:11:02.222023
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\\x1b[38;5;209mfoo', 'baz\\x1b[0m']
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:11:11.574475
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # type: () -> None
    """Create a test to run with pytest."""
    from flutils.txtutils import len_without_ansi
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(('\x1b[38;5;209mfoo\x1b[0m',
                             '\x1b[38;5;209mbar\x1b[0m')) == 6



# Generated at 2022-06-13 21:11:18.518216
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for len_without_ansi."""
    text = '\\x1b[38;5;209mfoobar\\x1b[0m'
    assert len_without_ansi(text) == 6
    assert len_without_ansi(text.splitlines()) == 6



# Generated at 2022-06-13 21:11:23.808507
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6



# Generated at 2022-06-13 21:11:27.724020
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6


# noinspection PyShadowingBuiltins

# Generated at 2022-06-13 21:11:36.686814
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209m', 'foobar', '\x1b[0m']) == 6



# Generated at 2022-06-13 21:11:43.533457
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""

    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6



# Generated at 2022-06-13 21:13:52.092120
# Unit test for function len_without_ansi
def test_len_without_ansi():
    # Single string tests
    assert len_without_ansi('\\x1b[38;5;209mfoobar\\x1b[0m') == 6
    assert len_without_ansi('\\x1b[38;5;209mfoo') == 3
    assert len_without_ansi('bar\\x1b[0m') == 3
    assert len_without_ansi('\\x1b[38;5;209mf') == 1
    assert len_without_ansi('o\\x1b[0mbar') == 3
    # Multiple string tests
    assert len_without_ansi(('\\x1b[38;5;209mfoobar\\x1b[0m',
                             '\\x1b[38;5;209mbazquux\\x1b[0m')) == 12


# Generated at 2022-06-13 21:13:59.098031
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi(('\x1b[38;5;209mfoobar\x1b[0m',)) == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', 'bar']) == 6



# Generated at 2022-06-13 21:14:03.447617
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

