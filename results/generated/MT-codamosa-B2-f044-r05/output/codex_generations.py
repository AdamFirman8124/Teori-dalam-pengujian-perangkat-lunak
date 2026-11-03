

# Generated at 2026-11-03 02:00:37.716116
# Unit test for function change_base
def test_change_base():
    # Basic binary conversions
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(1, 2) == "1"

    # Base 3 conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(9, 3) == "100"

    # Base 10 (identity for positive ints)
    assert module_0.change_base(123, 10) == "123"

    # Base 16: digits >= 10 are rendered as decimal strings
    assert module_0.change_base(255, 16) == "1515"

    # Single digit result
    assert module_0.change_base(5, 8) == "5"

    # Edge case: zero yields empty string (loop never runs)
    assert module_0.change_base(0, 2) == ""

    print("All tests passed!")


if __name__ == "__main__":
    test_change_base()

# Generated at 2026-11-03 02:01:58.096624
# Unit test for function change_base
def test_change_base():
    # Basic conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"

    # Base 10 round trips
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(123, 10) == "123"
    assert module_0.change_base(5, 10) == "5"

    # Single digit results
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(2, 2) == "10"

    # Edge case: zero yields empty string (loop never runs)
    assert module_0.change_base(0, 2) == ""

    # Larger numbers
    assert module_0.change_base(100, 2) == "1100100"
    assert module_0.change_base(16, 2) == "10000"

    # Exact power of the base
    assert module_0.change_base(27, 3) == "1000"
    assert module_0.change_base(9, 3) == "100"

    # Base larger than digit values (digits rendered in decimal)
    assert module_0.change_base(255, 16) == "1515"

    print("All tests passed!")


test_change_base()

# Generated at 2026-11-03 02:04:09.888691
# Unit test for function change_base
def test_change_base():
    # Basic binary conversions
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(15, 2) == "1111"
    assert module_0.change_base(31, 2) == "11111"
    assert module_0.change_base(32, 2) == "100000"

    # Other bases
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(9, 8) == "11"
    assert module_0.change_base(100, 10) == "100"
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(255, 8) == "377"

    # Base larger than 10: digit values are concatenated as decimal strings
    assert module_0.change_base(255, 16) == "1515"
    assert module_0.change_base(10, 16) == "10"

    # Edge case: zero input returns empty string (loop never executes)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Property: round-trip conversion for many values and valid bases
    for n in range(1, 200):
        for b in range(2, 11):
            assert int(module_0.change_base(n, b), b) == n, f"round-trip failed for n={n}, base={b}"
# nonce:033f7611

# Generated at 2026-11-03 02:05:13.900395
# Unit test for function change_base
def test_change_base():
    # nonce:de04e085
    # Basic conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"

    # Single digit results
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 10) == "5"

    # Base larger than x (single digit)
    assert module_0.change_base(5, 7) == "5"
    assert module_0.change_base(9, 16) == "9"

    # Larger numbers
    assert module_0.change_base(100, 5) == "400"      # 4*25 = 100
    assert module_0.change_base(255, 16) == "1515"    # digit 15 twice (str, not hex letters)
    assert module_0.change_base(1024, 2) == "10000000000"

    # Edge case: x = 0 returns empty string (loop never executes)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Verify round-trip consistency with int()
    for x, base in [(13, 2), (45, 8), (999, 10), (77, 3)]:
        result = module_0.change_base(x, base)
        assert int(result, base) == x

    print("All tests passed!")


test_change_base()

# Generated at 2026-11-03 02:06:54.755483
# Unit test for function change_base
def test_change_base():
    # Standard conversions
    assert module_0.change_base(10, 2) == '1010'
    assert module_0.change_base(8, 3) == '22'
    assert module_0.change_base(7, 2) == '111'
    assert module_0.change_base(8, 2) == '1000'
    assert module_0.change_base(5, 10) == '5'

    # Larger numbers
    assert module_0.change_base(1024, 2) == '10000000000'
    assert module_0.change_base(100, 3) == '10201'
    assert module_0.change_base(255, 16) == '1515'

    # Base larger than x (single digit result)
    assert module_0.change_base(3, 4) == '3'
    assert module_0.change_base(9, 10) == '9'

    # Powers of the base
    assert module_0.change_base(81, 3) == '10000'
    assert module_0.change_base(32, 2) == '100000'

    # Edge case: zero yields empty string
    assert module_0.change_base(0, 2) == ''

# nonce:c89ffac5