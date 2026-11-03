

# Generated at 2026-11-02 17:41:01.074260
# Unit test for function change_base
def test_change_base():
    # Standard base conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(100, 10) == "100"
    assert module_0.change_base(5, 2) == "101"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(9, 5) == "14"
    assert module_0.change_base(123, 5) == "443"
    assert module_0.change_base(1024, 2) == "10000000000"

    # Bases larger than 10: digits >= 10 are emitted as decimal numbers
    assert module_0.change_base(255, 16) == "1515"
    assert module_0.change_base(31, 16) == "115"

    # Edge cases: zero and negative inputs return an empty string
    assert module_0.change_base(0, 10) == ""
    assert module_0.change_base(-7, 2) == ""

# Generated at 2026-11-02 17:42:20.608206
# Unit test for function change_base
def test_change_base():
    # Basic conversions
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(5, 2) == "101"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(255, 16) == "1515"  # digit-wise: 15*16 + 15

    # Base 3
    assert module_0.change_base(100, 3) == "10201"
    assert module_0.change_base(9, 3) == "100"

    # Powers of base
    assert module_0.change_base(16, 2) == "10000"
    assert module_0.change_base(64, 8) == "100"

    # Edge cases
    assert module_0.change_base(0, 2) == ""      # loop never runs for x = 0
    assert module_0.change_base(0, 10) == ""
    assert module_0.change_base(-5, 2) == ""     # loop never runs for x < 0

    # Cross-check against Python's int parsing (digit-wise, so reconstruct)
    for x in [1, 2, 13, 42, 99, 1234]:
        for base in [2, 3, 8, 10]:
            result = module_0.change_base(x, base)
            # Reconstruct the value digit by digit
            reconstructed = 0
            for digit in result:
                reconstructed = reconstructed * base + int(digit)
            assert reconstructed == x

# nonce:26ae223e

# Generated at 2026-11-02 17:44:46.918536
# Unit test for function change_base
def test_change_base():# Test basic conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(5, 2) == "101"

    # Test base equal to 10
    assert module_0.change_base(100, 10) == "100"
    assert module_0.change_base(42, 10) == "42"

    # Test single digit results
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(3, 2) == "11"
    assert module_0.change_base(9, 9) == "10"

    # Test edge case: x = 0 returns empty string
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Test larger numbers
    assert module_0.change_base(255, 16) == "1515"  # note: digits beyond 9 are raw numbers concatenated
    assert module_0.change_base(1023, 2) == "1111111111"
    assert module_0.change_base(31, 2) == "11111"

    # Test base larger than x
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(4, 8) == "4"

# Generated at 2026-11-02 17:47:13.926933
# Unit test for function change_base
def test_change_base():
    # Basic conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"

    # Base 10 should return the number as string
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(123, 10) == "123"

    # Powers of the base
    assert module_0.change_base(16, 2) == "10000"
    assert module_0.change_base(27, 3) == "1000"

    # Single digit results
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(1, 2) == "1"

    # Large number
    assert module_0.change_base(1023, 2) == "1111111111"
    assert module_0.change_base(100, 5) == "400"

    # Edge case: zero returns empty string (loop never runs)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Note: for bases > 10, digits are represented in decimal (e.g., 15 -> "15")
    assert module_0.change_base(255, 16) == "1515"

# nonce:7b547888

# Generated at 2026-11-02 17:49:01.183627
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(100, 5) == "400"
    assert module_0.change_base(255, 16) == "1515"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(0, 2) == ""  # zero yields empty string
    assert module_0.change_base(-5, 2) == ""  # negative input yields empty string
    assert module_0.change_base(31, 2) == "11111"
    assert module_0.change_base(64, 4) == "1000"