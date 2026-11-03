

# Generated at 2026-11-02 13:14:35.627440
# Unit test for function change_base
def test_change_base():
    # Basic conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(100, 2) == "1100100"
    assert module_0.change_base(6, 2) == "110"
    assert module_0.change_base(27, 4) == "123"

    # Single digit
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 10) == "5"

    # Edge case: zero returns empty string (loop never runs)
    assert module_0.change_base(0, 2) == ""

    # Base larger than 10 produces multi-character "digits"
    assert module_0.change_base(255, 16) == "1515"

    # Large number
    assert module_0.change_base(1024, 2) == "10000000000"

    # Cross-check: converting back gives original value
    for x, base in [(12345, 7), (999, 5), (314159, 6)]:
        assert int(module_0.change_base(x, base), base) == x

# Generated at 2026-11-02 13:16:47.986192
# Unit test for function change_base
def test_change_base():
    # Basic base conversions
    assert module_0.change_base(8, 3) == "22"        # 8 = 2*3 + 2
    assert module_0.change_base(8, 2) == "1000"      # binary
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"      # base 10 unchanged
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 5) == "10"
    assert module_0.change_base(100, 2) == "1100100"
    assert module_0.change_base(123, 7) == "234"     # 123 = 2*49 + 3*7 + 4

    # Base larger than 10 uses decimal digit strings, not letters
    assert module_0.change_base(255, 16) == "1515"

    # Edge case: zero returns empty string (loop never runs)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Property check: converting back matches original number
    for x in range(1, 200):
        for base in range(2, 11):
            reconstructed = 0
            for ch in module_0.change_base(x, base):
                reconstructed = reconstructed * base + int(ch)
            assert reconstructed == x, (x, base)


if __name__ == "__main__":
    test_change_base()
    print("All tests passed!")

# Generated at 2026-11-02 13:20:14.685982
# Unit test for function change_base
def test_change_base():
    # Standard conversions
    assert module_0.change_base(8, 3) == "22"
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(255, 16) == "ff" if False else module_0.change_base(255, 15) == "1170"

    # Base larger than x (single digit results)
    assert module_0.change_base(5, 10) == "5"
    assert module_0.change_base(9, 10) == "9"

    # Powers of base
    assert module_0.change_base(16, 2) == "10000"
    assert module_0.change_base(27, 3) == "1000"

    # Single unit values
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(1, 5) == "1"

    # Edge case: zero returns empty string (loop never executes)
    assert module_0.change_base(0, 2) == ""
    assert module_0.change_base(0, 10) == ""

    # Larger numbers
    assert module_0.change_base(1024, 2) == "10000000000"
    assert module_0.change_base(100, 4) == "1210"

    # Verify round-trip: converting back yields original number
    for x, base in [(123, 5), (456, 7), (789, 12), (3141, 8)]:
        back = int(module_0.change_base(x, base), base)
        assert back == x, f"Round-trip failed for x={x}, base={base}"

    print("All tests passed!")


test_change_base()

# Generated at 2026-11-02 13:22:29.017213
# Unit test for function change_base
def test_change_base():
    # Standard base conversions
    assert module_0.change_base(8, 2) == "1000"
    assert module_0.change_base(7, 2) == "111"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(255, 2) == "11111111"

    # Base 10 (identity)
    assert module_0.change_base(123, 10) == "123"
    assert module_0.change_base(9, 10) == "9"

    # Base 3
    assert module_0.change_base(10, 3) == "101"
    assert module_0.change_base(27, 3) == "1000"

    # Base 8
    assert module_0.change_base(64, 8) == "100"
    assert module_0.change_base(7, 8) == "7"

    # Base 16 (digits may exceed 9, represented numerically)
    assert module_0.change_base(255, 16) == "1515"

    # Edge case: x = 0 returns empty string (loop never executes)
    assert module_0.change_base(0, 2) == ""

    # Single digit results
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 10) == "5"

    # Larger numbers
    assert module_0.change_base(1024, 2) == "10000000000"
    assert module_0.change_base(100, 5) == "400"

    print("All tests passed!")


if __name__ == "__main__":
    test_change_base()