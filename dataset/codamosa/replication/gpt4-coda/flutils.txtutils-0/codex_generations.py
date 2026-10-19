

# Generated at 2024-03-18 05:36:10.188223
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:19.027181
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:24.837656
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:31.625846
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:39.740841
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:45.162402
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:50.480794
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:36:57.298229
# Unit test for function len_without_ansi
def test_len_without_ansi():    # Test with a single ANSI escape code
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with multiple ANSI escape codes
    text_with_multiple_ansi = '\x1b[1mBold\x1b[0m and \x1b[4mUnderline\x1b[0m'
    assert len_without_ansi(text_with_multiple_ansi) == 15

    # Test with no ANSI escape codes
    text_without_ansi = 'Just plain text'
    assert len_without_ansi(text_without_ansi) == len(text_without_ansi)

    # Test with an empty string
    assert len_without_ansi('') == 0

    # Test with a list of strings with ANSI escape codes

# Generated at 2024-03-18 05:37:04.576882
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:37:10.828973
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:38:30.641179
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:38:37.717665
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:38:47.478490
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:38:53.423854
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:38:59.120808
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:39:05.181017
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:39:11.852066
# Unit test for function len_without_ansi
def test_len_without_ansi():    # Test with a string containing ANSI codes
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with a string without ANSI codes
    text_without_ansi = 'foobar'
    assert len_without_ansi(text_without_ansi) == 6

    # Test with a list of strings containing ANSI codes
    list_with_ansi = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(list_with_ansi) == 6

    # Test with a list of strings without ANSI codes
    list_without_ansi = ['foo', 'bar']
    assert len_without_ansi(list_without_ansi) == 6

    # Test with a tuple of strings containing ANSI codes

# Generated at 2024-03-18 05:39:17.194468
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:39:25.228115
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:39:30.469555
# Unit test for function len_without_ansi
def test_len_without_ansi():    # Test with a string containing ANSI codes
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with a string without ANSI codes
    text_without_ansi = 'foobar'
    assert len_without_ansi(text_without_ansi) == 6

    # Test with a list of strings containing ANSI codes
    list_with_ansi = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(list_with_ansi) == 6

    # Test with a list of strings without ANSI codes
    list_without_ansi = ['foo', 'bar']
    assert len_without_ansi(list_without_ansi) == 6

    # Test with a tuple of strings containing ANSI codes

# Generated at 2024-03-18 05:40:47.333444
# Unit test for function len_without_ansi
def test_len_without_ansi():    # Test with a single ANSI escape code
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with multiple ANSI escape codes
    text_with_multiple_ansi = '\x1b[1mBold\x1b[0m and \x1b[4mUnderline\x1b[0m'
    assert len_without_ansi(text_with_multiple_ansi) == 16

    # Test with no ANSI escape codes
    text_without_ansi = 'Just plain text'
    assert len_without_ansi(text_without_ansi) == 15

    # Test with an empty string
    empty_text = ''
    assert len_without_ansi(empty_text) == 0

    # Test with a list of strings with ANSI escape codes

# Generated at 2024-03-18 05:40:54.512607
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:00.982779
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:08.078972
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:14.460294
# Unit test for function len_without_ansi
def test_len_without_ansi():    # Test with a single ANSI escape code
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with multiple ANSI escape codes
    text_with_multiple_ansi = '\x1b[1mBold\x1b[0m and \x1b[4mUnderline\x1b[0m'
    assert len_without_ansi(text_with_multiple_ansi) == 16

    # Test with no ANSI escape codes
    text_without_ansi = 'Just plain text'
    assert len_without_ansi(text_without_ansi) == 15

    # Test with an empty string
    empty_text = ''
    assert len_without_ansi(empty_text) == 0

    # Test with a list of strings with ANSI escape codes

# Generated at 2024-03-18 05:41:22.527335
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:29.236060
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:35.780740
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:43.971728
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:41:51.447903
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:42:57.120740
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:03.050141
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:13.753257
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:22.296118
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:29.639074
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:35.625349
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:43.485664
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:50.902949
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:43:58.291106
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6

# Generated at 2024-03-18 05:44:04.280503
# Unit test for function len_without_ansi
def test_len_without_ansi():    assert len_without_ansi("\x1b[38;5;209mfoobar\x1b[0m") == 6