

# Generated at 2026-11-02 00:17:19.676070
# Unit test for function hex_key
def test_hex_key():
    # Basic cases with known prime hex digits
    assert module_0.hex_key("AB") == 1          # B is prime
    assert module_0.hex_key("1077E") == 2       # 7 and 7 are prime
    assert module_0.hex_key("ABED1A33") == 4    # B, D, 3, 3 are prime
    assert module_0.hex_key("1232024") == 5     # 2, 3, 2, 2, 2 are prime
    assert module_0.hex_key("2020") == 3        # 2, 2, 2 are prime

    # No prime digits present
    assert module_0.hex_key("111") == 0
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("E") == 0
    assert module_0.hex_key("8") == 0

    # Empty string
    assert module_0.hex_key("") == 0

    # All prime digits
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("2222") == 4

    # Mixed case with repeated digits
    assert module_0.hex_key("FFFF") == 0
    assert module_0.hex_key("DDDD") == 4
    assert module_0.hex_key("BBBB") == 4

    # Long mixed string
    assert module_0.hex_key("2020ABED1077E") == 3 + 4 + 2

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 00:17:53.769383
# Unit test for function hex_key
def test_hex_key():
    # Test with a string containing multiple prime hex digits
    assert module_0.hex_key("AB") == 1, "Expected 1 prime digit in 'AB'"
    assert module_0.hex_key("1077E") == 2, "Expected 2 prime digits in '1077E'"
    assert module_0.hex_key("ABED1A33") == 4, "Expected 4 prime digits in 'ABED1A33'"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Expected 6 prime digits in '123456789ABCDEF0'"
    assert module_0.hex_key("2020") == 2, "Expected 2 prime digits in '2020'"
    
    # Test with no prime digits
    assert module_0.hex_key("111") == 0, "Expected 0 prime digits in '111'"
    assert module_0.hex_key("9A0146") == 0, "Expected 0 prime digits in '9A0146'"
    
    # Test with empty string
    assert module_0.hex_key("") == 0, "Expected 0 prime digits in empty string"
    
    # Test with all prime digits
    assert module_0.hex_key("2357BD") == 6, "Expected 6 prime digits in '2357BD'"
    
    # Test with lowercase (should not count, since primes are uppercase)
    assert module_0.hex_key("bd") == 0, "Expected 0 prime digits in lowercase 'bd'"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 00:18:40.171773
# Unit test for function hex_key
def test_hex_key():
    # Basic cases with known prime digit counts
    assert module_0.hex_key("AB") == 1          # only B is prime
    assert module_0.hex_key("1077E") == 2       # two 7s
    assert module_0.hex_key("ABED1A33") == 4    # B, D, 3, 3
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D
    assert module_0.hex_key("2020") == 2        # two 2s

    # Edge cases
    assert module_0.hex_key("") == 0            # empty string
    assert module_0.hex_key("01469EF") == 0     # no prime digits at all
    assert module_0.hex_key("2357BD") == 6      # all prime digits
    assert module_0.hex_key("2") == 1           # single prime digit
    assert module_0.hex_key("1") == 0           # single non-prime digit

    print("All tests passed!")

# Generated at 2026-11-02 00:20:55.321130
# Unit test for function hex_key
def test_hex_key():
    # Basic examples
    assert module_0.hex_key("AB") == 1, "Expected 1 prime digit ('B') in 'AB'"
    assert module_0.hex_key("1077E") == 2, "Expected 2 prime digits ('7','7') in '1077E'"
    assert module_0.hex_key("ABED1A33") == 4, "Expected 4 prime digits in 'ABED1A33'"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Expected 6 prime digits in '123456789ABCDEF0'"
    assert module_0.hex_key("2020") == 2, "Expected 2 prime digits ('2','2') in '2020'"

    # Edge cases
    assert module_0.hex_key("") == 0, "Empty string should return 0"
    assert module_0.hex_key("0") == 0, "'0' is not prime"
    assert module_0.hex_key("1") == 0, "'1' is not prime"
    assert module_0.hex_key("2") == 1, "'2' is prime"
    assert module_0.hex_key("D") == 1, "'D' (13) is prime"
    assert module_0.hex_key("F") == 0, "'F' is not prime"
    assert module_0.hex_key("FFFFFFFFF") == 0, "No prime digits in 'FFFFFFFFF'"
    assert module_0.hex_key("222222") == 6, "All '2's are prime"
    assert module_0.hex_key("BBBBBB") == 6, "All 'B's are prime"

    # Case sensitivity: lowercase letters are not counted
    assert module_0.hex_key("bd") == 0, "Lowercase 'b','d' should not be counted"

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 00:23:25.340727
# Unit test for function hex_key
def test_hex_key():
    # Empty string has no prime digits
    assert module_0.hex_key("") == 0
    # Single characters
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("3") == 1
    assert module_0.hex_key("5") == 1
    assert module_0.hex_key("7") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1
    # Non-prime hex digits
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("4") == 0
    assert module_0.hex_key("6") == 0
    assert module_0.hex_key("8") == 0
    assert module_0.hex_key("9") == 0
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("C") == 0
    assert module_0.hex_key("E") == 0
    assert module_0.hex_key("F") == 0
    # Mixed strings
    assert module_0.hex_key("AB") == 1          # only B is prime
    assert module_0.hex_key("1077E") == 2       # 7 and 7
    assert module_0.hex_key("ABED1A33") == 4    # B, D, 3, 3
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D
    assert module_0.hex_key("2020") == 2        # 2 and 2
    assert module_0.hex_key("FFFF") == 0        # no primes
    assert module_0.hex_key("DDDD") == 4        # all primes
    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()