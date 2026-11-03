

# Generated at 2026-11-03 04:41:14.222983
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(100, 2) == "1100100"
    assert module_0.change_base(255, 16) == "1515"
    assert module_0.change_base(31, 2) == "11111"
    assert module_0.change_base(5, 5) == "10"
    assert module_0.change_base(9, 9) == "10"
    assert module_0.change_base(123, 5) == "443"
    print("All test cases passed!")


if __name__ == "__main__":
    test_change_base()

# Generated at 2026-11-03 04:43:17.155990
# Unit test for function change_base
def test_change_base():
    # nonce:cec43b70
    # Standard conversion cases
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    # Single-digit / small values
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(3, 10) == "3"
    # Larger numbers
    assert module_0.change_base(100, 2) == "1100100"
    assert module_0.change_base(255, 2) == "11111111"
    # Base 16 yields decimal digit strings (not hex letters)
    assert module_0.change_base(255, 16) == "1515"
    # Zero never enters the loop -> empty string
    assert module_0.change_base(0, 2) == ""
    # Round-trip consistency checks
    for x, b in [(123, 5), (999, 7), (64, 4), (17, 8)]:
        assert int(module_0.change_base(x, b), b) == x

# Generated at 2026-11-03 04:47:27.585935
# Unit test for function change_base
def test_change_base():
    # Basic conversions
    assert module_0.change_base(8, 3) == "22"        # 8 = 2*3 + 2
    assert module_0.change_base(8, 2) == "1000"      # 8 in binary
    assert module_0.change_base(7, 2) == "111"       # 7 in binary
    assert module_0.change_base(10, 10) == "10"      # same base as decimal
    assert module_0.change_base(5, 2) == "101"       # 5 in binary
    assert module_0.change_base(100, 16) == "64"     # 100 = 6*16 + 4
    assert module_0.change_base(255, 16) == "1515"   # digits beyond 9 are numeric values

    # Single digit results
    assert module_0.change_base(1, 10) == "1"
    assert module_0.change_base(9, 10) == "9"
    assert module_0.change_base(15, 16) == "15"

    # Edge cases
    assert module_0.change_base(0, 2) == ""          # loop never runs for x = 0
    assert module_0.change_base(0, 10) == ""         # loop never runs for x = 0
    assert module_0.change_base(-5, 2) == ""         # negative input returns empty string

    # Larger numbers
    assert module_0.change_base(1024, 2) == "10000000000"
    assert module_0.change_base(1023, 2) == "1111111111"
    assert module_0.change_base(1000, 8) == "1750"   # 1000 = 1*512 + 7*64 + 5*8 + 0

    # Base 3 checks
    assert module_0.change_base(9, 3) == "100"
    assert module_0.change_base(26, 3) == "222"      # 26 = 2*9 + 2*3 + 2

    print("All tests passed!")


if __name__ == "__main__":
    test_change_base()