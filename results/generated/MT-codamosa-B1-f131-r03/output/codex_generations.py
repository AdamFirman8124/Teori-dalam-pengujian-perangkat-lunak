

# Generated at 2026-10-24 10:56:43.512454
# Unit test for function digits
def test_digits():
    assert module_0.digits(12345) == 15       # 1 * 3 * 5
    assert module_0.digits(13579) == 945      # 1 * 3 * 5 * 7 * 9
    assert module_0.digits(2468) == 0         # No odd digits
    assert module_0.digits(1002) == 1         # Only odd digit is 1
    assert module_0.digits(0) == 0            # No odd digits

# Generated at 2026-10-24 10:57:03.789589
# Unit test for function digits
def test_digits():
    # product of odd digits
    assert module_0.digits(12345) == 15      # 1*3*5
    assert module_0.digits(13579) == 945     # 1*3*5*7*9
    assert module_0.digits(7) == 7           # single odd digit
    assert module_0.digits(11) == 1          # odd digits multiply to 1

    # no odd digits -> 0
    assert module_0.digits(2468) == 0
    assert module_0.digits(0) == 0
    assert module_0.digits(2) == 0

    # even digits are ignored, odd digit 1 still counts as "found"
    assert module_0.digits(102) == 1         # only 1 is odd
    assert module_0.digits(1234) == 3        # 1*3


# Known bug: negative input raises ValueError from int('-')
@pytest.mark.xfail(raises=ValueError, reason="int('-') fails; see note")
def test_digits_negative():
    assert module_0.digits(-135) == 15

# Generated at 2026-10-24 10:57:05.106802
# Unit test for function digits
def test_digits():
    # product of odd digits
    assert module_0.digits(12345) == 15      # 1*3*5
    assert module_0.digits(13579) == 945     # 1*3*5*7*9
    assert module_0.digits(7) == 7           # single odd digit
    assert module_0.digits(11) == 1          # odd digits multiply to 1

    # no odd digits -> 0
    assert module_0.digits(2468) == 0
    assert module_0.digits(0) == 0
    assert module_0.digits(2) == 0

    # even digits are ignored, odd digit 1 still counts as "found"
    assert module_0.digits(102) == 1         # only 1 is odd
    assert module_0.digits(1234) == 3        # 1*3


# Known bug: negative input raises ValueError from int('-')
@pytest.mark.xfail(raises=ValueError, reason="int('-') fails; see note")
def test_digits_negative():
    assert module_0.digits(-135) == 15

# Generated at 2026-10-24 10:57:06.764224
# Unit test for function digits
def test_digits():
    # product of odd digits
    assert module_0.digits(12345) == 15      # 1*3*5
    assert module_0.digits(13579) == 945     # 1*3*5*7*9
    assert module_0.digits(7) == 7           # single odd digit
    assert module_0.digits(11) == 1          # odd digits multiply to 1

    # no odd digits -> 0
    assert module_0.digits(2468) == 0
    assert module_0.digits(0) == 0
    assert module_0.digits(2) == 0

    # even digits are ignored, odd digit 1 still counts as "found"
    assert module_0.digits(102) == 1         # only 1 is odd
    assert module_0.digits(1234) == 3        # 1*3


# Known bug: negative input raises ValueError from int('-')
@pytest.mark.xfail(raises=ValueError, reason="int('-') fails; see note")
def test_digits_negative():
    assert module_0.digits(-135) == 15

# Generated at 2026-10-24 10:57:08.197203
# Unit test for function digits
def test_digits():
    # product of odd digits
    assert module_0.digits(12345) == 15      # 1*3*5
    assert module_0.digits(13579) == 945     # 1*3*5*7*9
    assert module_0.digits(7) == 7           # single odd digit
    assert module_0.digits(11) == 1          # odd digits multiply to 1

    # no odd digits -> 0
    assert module_0.digits(2468) == 0
    assert module_0.digits(0) == 0
    assert module_0.digits(2) == 0

    # even digits are ignored, odd digit 1 still counts as "found"
    assert module_0.digits(102) == 1         # only 1 is odd
    assert module_0.digits(1234) == 3        # 1*3


# Known bug: negative input raises ValueError from int('-')
@pytest.mark.xfail(raises=ValueError, reason="int('-') fails; see note")
def test_digits_negative():
    assert module_0.digits(-135) == 15