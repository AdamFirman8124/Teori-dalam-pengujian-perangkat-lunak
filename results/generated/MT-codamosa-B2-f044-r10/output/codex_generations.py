

# Generated at 2026-11-01 20:25:15.904074
# Unit test for function change_base
def test_change_base():
    # Standard conversions
    assert module_0.change_base(8, 2) == '1000'
    assert module_0.change_base(8, 3) == '22'
    assert module_0.change_base(7, 2) == '111'
    assert module_0.change_base(10, 10) == '10'
    assert module_0.change_base(100, 10) == '100'

    # Base larger than digits present
    assert module_0.change_base(5, 10) == '5'

    # Digits above 9 are rendered as decimal numbers
    assert module_0.change_base(255, 16) == '1515'
    assert module_0.change_base(16, 16) == '10'

    # Zero and negative inputs yield empty string
    assert module_0.change_base(0, 2) == ''
    assert module_0.change_base(-5, 2) == ''

    # Large number
    assert module_0.change_base(1024, 2) == '10000000000'

    print("All tests passed!")


if __name__ == "__main__":
    test_change_base()

# Generated at 2026-11-01 20:25:38.596193
# Unit test for function change_base
def test_change_base():
    # Standard multi-digit conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(123, 5) == "443"
    assert module_0.change_base(1024, 2) == "10000000000"
    assert module_0.change_base(255, 16) == "1515"

    # Single-digit / trivial results
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(9, 10) == "9"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(3, 10) == "3"
    assert module_0.change_base(6, 8) == "6"

    # Zero input yields an empty string (loop never executes)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Round-trip property check (bases where every digit is a single char)
    for value in range(1, 300):
        for base in range(2, 11):
            repr_str = module_0.change_base(value, base)
            assert repr_str != ""
            assert int(repr_str, base) == value


test_change_base()
print("All tests passed!")

# Generated at 2026-11-01 20:26:08.329762
# Unit test for function change_base
def test_change_base():
    # Standard conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(100, 10) == "100"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(123, 5) == "443"

    # Base larger than 10: digits stay numeric (no letters)
    assert module_0.change_base(255, 16) == "1515"
    assert module_0.change_base(10, 16) == "10"

    # Power-of-two boundaries
    assert module_0.change_base(16, 2) == "10000"
    assert module_0.change_base(32, 2) == "100000"

    # Edge cases: zero and negative input return empty string
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(-5, 2) == ""

    # Large number
    assert module_0.change_base(1023, 2) == "1111111111"
    assert module_0.change_base(1024, 2) == "10000000000"

# Generated at 2026-11-01 20:26:48.778918
# Unit test for function change_base
def test_change_base():
    # nonce:ac8cb286

    # Standard conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(100, 16) == "64"

    # Multi-digit result with base 16 (digits remain numeric strings)
    assert module_0.change_base(255, 16) == "1515"

    # Single digit results
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(3, 10) == "3"

    # Base larger than input value yields single digit
    assert module_0.change_base(4, 8) == "4"

    # Zero input returns empty string
    assert module_0.change_base(0, 2) == ""

    # Negative input never enters loop, returns empty string
    assert module_0.change_base(-5, 2) == ""

    print("All tests passed!")


test_change_base()

# Generated at 2026-11-01 20:27:11.920765
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(8, 3) == '22'
    assert module_0.change_base(8, 2) == '1000'
    assert module_0.change_base(7, 2) == '111'
    assert module_0.change_base(10, 10) == '10'
    assert module_0.change_base(1, 2) == '1'
    assert module_0.change_base(100, 16) == '64'
    assert module_0.change_base(255, 16) == '1515'
    assert module_0.change_base(5, 5) == '10'
    assert module_0.change_base(0, 2) == ''  # loop never runs for x=0
    assert module_0.change_base(123456, 7) == '1021566'