

# Generated at 2022-06-13 21:09:00.780565
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.txtutils import len_without_ansi
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
    text = ['\x1b[38;5;209mfoobar\x1b[0m', ': ']
    assert len_without_ansi(text) == 7



# Generated at 2022-06-13 21:09:07.104241
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoo', 'bar\x1b[0m']) == 6


# Generated at 2022-06-13 21:09:10.236421
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:16.690512
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6




# Generated at 2022-06-13 21:09:21.064839
# Unit test for function len_without_ansi
def test_len_without_ansi():
    from flutils.ansi import ansi

    assert len_without_ansi('foobar') == len('foobar')
    assert len_without_ansi(list('foobar')) == len('foobar')
    assert len_without_ansi(tuple('foobar')) == len('foobar')
    assert len_without_ansi([ansi.fg_ansi('foobar', 213)]) == len('foobar')



# Generated at 2022-06-13 21:09:26.086610
# Unit test for function len_without_ansi
def test_len_without_ansi():
    """Unit test for function len_without_ansi"""
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Generated at 2022-06-13 21:09:28.697178
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:32.760438
# Unit test for function len_without_ansi
def test_len_without_ansi():
    text = '\u001b[38;5;209mfoobar\u001b[0m'
    assert len_without_ansi(text) == 6



# Generated at 2022-06-13 21:09:42.568185
# Unit test for function len_without_ansi
def test_len_without_ansi():
    assert len_without_ansi(['\x1b[38;5;209mfoo\x1b[0m', 'bar']) == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6
    assert len_without_ansi(['\x1b[38;5;209mfoobar\x1b[0m']) == 6
    assert len_without_ansi(['foobar']) == 6
    assert len_without_ansi('foo\x1b[38;5;209mbar') == 9



# Generated at 2022-06-13 21:09:54.741771
# Unit test for function len_without_ansi
def test_len_without_ansi():  # noqa: D102; pylint: disable=unused-argument
    from pytest import raises
    from .exceptions import FlUtilsTypeError
    from .strings import ANSI_RESET
    from .txtutils import len_without_ansi

    assert len_without_ansi('') == 0
    assert len_without_ansi('foobar') == 6
    assert len_without_ansi('foo\x1bb\nar') == 6
    assert len_without_ansi(['foo', '\x1bb\n', 'ar']) == 6
    assert (
        len_without_ansi('\x1b[38;5;226mfoo\x1b[38;5;202mbar' + ANSI_RESET) ==
        6
    )