

# Generated at 2026-11-03 02:51:41.350132
# Unit test for function decimal_to_binary
def test_decimal_to_binary():
    # nonce:babe1518
    assert module_0.decimal_to_binary(0) == "db0db"
    assert module_0.decimal_to_binary(1) == "db1db"
    assert module_0.decimal_to_binary(2) == "db10db"
    assert module_0.decimal_to_binary(3) == "db11db"
    assert module_0.decimal_to_binary(5) == "db101db"
    assert module_0.decimal_to_binary(15) == "db1111db"
    assert module_0.decimal_to_binary(32) == "db100000db"
    assert module_0.decimal_to_binary(255) == "db11111111db"
    assert module_0.decimal_to_binary(1024) == "db10000000000db"

    # Verify structure and round-trip conversion
    for n in [0, 1, 7, 42, 100, 999, 4096]:
        result = module_0.decimal_to_binary(n)
        assert result.startswith("db") and result.endswith("db")
        assert int(result[2:-2], 2) == n

# Generated at 2026-11-03 02:52:28.145670
# Unit test for function decimal_to_binary
def test_decimal_to_binary():
    # nonce:7620fe0d
    assert module_0.decimal_to_binary(0) == "db0db"
    assert module_0.decimal_to_binary(1) == "db1db"
    assert module_0.decimal_to_binary(2) == "db10db"
    assert module_0.decimal_to_binary(5) == "db101db"
    assert module_0.decimal_to_binary(15) == "db1111db"
    assert module_0.decimal_to_binary(32) == "db100000db"
    assert module_0.decimal_to_binary(103) == "db1100111db"
    assert module_0.decimal_to_binary(255) == "db11111111db"
    assert module_0.decimal_to_binary(1024) == "db10000000000db"
    # Verify format: wrapped with 'db' markers on both sides
    result = module_0.decimal_to_binary(42)
    assert result.startswith("db") and result.endswith("db")
    assert result[2:-2] == bin(42)[2:]
    print("test_decimal_to_binary passed")


if __name__ == "__main__":
    test_decimal_to_binary()

# Generated at 2026-11-03 02:54:10.750167
# Unit test for function decimal_to_binary
def test_decimal_to_binary():
    # Basic cases
    assert module_0.decimal_to_binary(0) == "db0db"
    assert module_0.decimal_to_binary(1) == "db1db"
    assert module_0.decimal_to_binary(2) == "db10db"
    assert module_0.decimal_to_binary(15) == "db1111db"
    assert module_0.decimal_to_binary(32) == "db100000db"
    assert module_0.decimal_to_binary(103) == "db1100111db"

    # Larger number
    assert module_0.decimal_to_binary(255) == "db11111111db"
    assert module_0.decimal_to_binary(1024) == "db10000000000db"

    # Output should always start and end with "db"
    for n in range(0, 65):
        result = module_0.decimal_to_binary(n)
        assert result.startswith("db")
        assert result.endswith("db")

        # Inner content must match Python's binary representation
        assert result[2:-2] == bin(n)[2:]

        # Round-trip check
        assert int(result[2:-2], 2) == n

    print("All tests passed!")


if __name__ == "__main__":
    test_decimal_to_binary()

# Generated at 2026-11-03 02:56:52.851761
# Unit test for function decimal_to_binary
def test_decimal_to_binary():
    # Basic cases
    assert module_0.decimal_to_binary(15) == "db1111db"
    assert module_0.decimal_to_binary(32) == "db100000db"

    # Edge cases
    assert module_0.decimal_to_binary(0) == "db0db"
    assert module_0.decimal_to_binary(1) == "db1db"
    assert module_0.decimal_to_binary(2) == "db10db"
    assert module_0.decimal_to_binary(3) == "db11db"

    # Powers of two
    assert module_0.decimal_to_binary(4) == "db100db"
    assert module_0.decimal_to_binary(8) == "db1000db"
    assert module_0.decimal_to_binary(16) == "db10000db"
    assert module_0.decimal_to_binary(64) == "db1000000db"
    assert module_0.decimal_to_binary(128) == "db10000000db"

    # Larger numbers
    assert module_0.decimal_to_binary(255) == "db11111111db"
    assert module_0.decimal_to_binary(256) == "db100000000db"
    assert module_0.decimal_to_binary(1023) == "db1111111111db"
    assert module_0.decimal_to_binary(1024) == "db10000000000db"

    # Property checks: prefix/suffix and round-trip conversion
    for n in range(0, 100):
        result = module_0.decimal_to_binary(n)
        assert result.startswith("db") and result.endswith("db")
        assert int(result[2:-2], 2) == n

    print("All tests passed!")


if __name__ == "__main__":
    test_decimal_to_binary()

# Generated at 2026-11-03 02:59:26.760582
# Unit test for function decimal_to_binary
def test_decimal_to_binary():
    # Basic conversions
    assert module_0.decimal_to_binary(0) == "db0db"
    assert module_0.decimal_to_binary(1) == "db1db"
    assert module_0.decimal_to_binary(2) == "db10db"
    assert module_0.decimal_to_binary(3) == "db11db"
    assert module_0.decimal_to_binary(15) == "db1111db"
    assert module_0.decimal_to_binary(32) == "db100000db"
    assert module_0.decimal_to_binary(103) == "db1100111db"

    # Larger numbers
    assert module_0.decimal_to_binary(255) == "db11111111db"
    assert module_0.decimal_to_binary(256) == "db100000000db"
    assert module_0.decimal_to_binary(1023) == "db1111111111db"

    # Verify framing characters
    result = module_0.decimal_to_binary(42)
    assert result.startswith("db")
    assert result.endswith("db")
    assert result[2:-2] == bin(42)[2:]

    # Verify internal content matches Python's bin() output
    for n in range(0, 100):
        assert module_0.decimal_to_binary(n) == "db" + bin(n)[2:] + "db"