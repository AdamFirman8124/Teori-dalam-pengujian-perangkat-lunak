

# Generated at 2026-10-25 14:15:06.096980
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:08.510261
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:10.927716
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:13.342421
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:15.757609
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:18.376370
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:20.792068
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:23.205165
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:25.619971
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:28.037427
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:30.451807
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:32.862679
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:35.311824
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:37.714850
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:40.127674
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:42.546018
# Unit test for function circular_shift

# Generated at 2026-10-25 14:15:49.055975
# Unit test for function circular_shift
def test_circular_shift():assert module_0.circular_shift(12345, 2) == "45123"

# Generated at 2026-10-25 14:16:05.540484
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 14:16:30.846492
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 4) == "1234"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 2) == "7"

# Generated at 2026-10-25 14:16:52.147285
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(100, 2) == "001"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(97, 8) == "79"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 3) == "34512"
    assert module_0.circular_shift(11, 101) == "11"

# Generated at 2026-10-25 14:17:11.660114
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 14:17:12.998194
# Unit test for function circular_shift
def test_circular_shift():import pytest

def module_0.circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


@pytest.mark.parametrize("x, shift, expected", [
    (12345, 2,   "45123"),   # normal right rotation
    (12345, 5,   "12345"),   # shift == len(s) -> else branch, unchanged
    (12345, 6,   "54321"),   # shift > len(s) -> reversed
    (12345, 0,   "12345"),   # zero shift -> unchanged
    ("abc", 1,   "cab"),     # str input
    ("abc", 100, "cba"),     # huge shift -> reversed
    (7,     1,   "7"),       # single char, shift == len(s)
])
def test_circular_shift(x, shift, expected):
    assert module_0.circular_shift(x, shift) == expected

# Generated at 2026-10-25 14:17:21.432901
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 6) == "54321"

# Generated at 2026-10-25 14:17:22.772806
# Unit test for function circular_shift
def test_circular_shift():import pytest

def module_0.circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


@pytest.mark.parametrize("x, shift, expected", [
    (12345, 2,   "45123"),   # normal right rotation
    (12345, 5,   "12345"),   # shift == len(s) -> else branch, unchanged
    (12345, 6,   "54321"),   # shift > len(s) -> reversed
    (12345, 0,   "12345"),   # zero shift -> unchanged
    ("abc", 1,   "cab"),     # str input
    ("abc", 100, "cba"),     # huge shift -> reversed
    (7,     1,   "7"),       # single char, shift == len(s)
])
def test_circular_shift(x, shift, expected):
    assert module_0.circular_shift(x, shift) == expected

# Generated at 2026-10-25 14:17:30.239101
# Unit test for function circular_shift
def test_circular_shift():
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12345, 6) == "54321"
    assert module_0.circular_shift(7, 1) == "7"

# Generated at 2026-10-25 14:17:31.672267
# Unit test for function circular_shift
def test_circular_shift():import pytest

def module_0.circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


@pytest.mark.parametrize("x, shift, expected", [
    (12345, 2,   "45123"),   # normal right rotation
    (12345, 5,   "12345"),   # shift == len(s) -> else branch, unchanged
    (12345, 6,   "54321"),   # shift > len(s) -> reversed
    (12345, 0,   "12345"),   # zero shift -> unchanged
    ("abc", 1,   "cab"),     # str input
    ("abc", 100, "cba"),     # huge shift -> reversed
    (7,     1,   "7"),       # single char, shift == len(s)
])
def test_circular_shift(x, shift, expected):
    assert module_0.circular_shift(x, shift) == expected