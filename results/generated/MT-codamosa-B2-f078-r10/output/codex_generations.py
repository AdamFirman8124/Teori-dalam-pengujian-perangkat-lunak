

# Generated at 2026-11-02 18:23:40.204931
# Unit test for function hex_key
def test_hex_key():
    # Basic cases with known counts of prime hex digits (2, 3, 5, 7, B, D)
    assert module_0.hex_key("AB") == 1          # only 'B' is prime
    assert module_0.hex_key("1077E") == 2       # two '7's are prime
    assert module_0.hex_key("ABED1A33") == 4    # 'B', 'D', '3', '3' are prime
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2,3,5,7,B,D
    assert module_0.hex_key("2020") == 2        # two '2's
    assert module_0.hex_key("111") == 0         # no prime digits

    # Edge cases
    assert module_0.hex_key("") == 0            # empty string
    assert module_0.hex_key("2") == 1           # single prime digit
    assert module_0.hex_key("4") == 1           # 4 is not prime
    assert module_0.hex_key("BBBB") == 4        # repeated prime hex digit
    assert module_0.hex_key("6699CC") == 0      # no prime digits
    assert module_0.hex_key("DD2") == 3         # D, D, 2 all prime
    assert module_0.hex_key("0123456789ABCDEF") == 6  # full hex range

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 18:24:34.832957
# Unit test for function hex_key
def test_hex_key():
    # Test with examples containing prime hex digits
    assert module_0.hex_key("AB") == 1, "Expected 1 prime ('B')"
    assert module_0.hex_key("1077E") == 2, "Expected 2 primes ('7', '7')"
    assert module_0.hex_key("ABED1A33") == 4, "Expected 4 primes ('B', 'D', '3', '3')"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Expected 6 primes ('2', '3', '5', '7', 'B', 'D')"
    assert module_0.hex_key("2020") == 2, "Expected 2 primes ('2', '2')"

    # Test with empty string
    assert module_0.hex_key("") == 0, "Expected 0 primes for empty string"

    # Test with no prime digits
    assert module_0.hex_key("1469") == 0, "Expected 0 primes"
    assert module_0.hex_key("EFACE0") == 0, "Expected 0 primes"

    # Test with all prime digits
    assert module_0.hex_key("2357BD") == 6, "Expected 6 primes"
    assert module_0.hex_key("2222") == 4, "Expected 4 primes"

    # Test with single characters
    assert module_0.hex_key("2") == 1, "Expected 1 prime"
    assert module_0.hex_key("D") == 1, "Expected 1 prime"
    assert module_0.hex_key("4") == 0, "Expected 0 primes"

    # Test case sensitivity (hex digits are uppercase)
    assert module_0.hex_key("abd") == 0, "Lowercase letters are not in primes tuple"

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 18:26:19.100243
# Unit test for function hex_key
def test_hex_key():
    # Test with typical hexadecimal strings
    assert module_0.hex_key("AB") == 1, "Expected 1 prime digit (B) in 'AB'"
    assert module_0.hex_key("1077E") == 2, "Expected 2 prime digits (7, 7) in '1077E'"
    assert module_0.hex_key("ABED1A33") == 4, "Expected 4 prime digits (B, D, 3, 3) in 'ABED1A33'"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Expected 6 prime digits in '123456789ABCDEF0'"
    assert module_0.hex_key("2020") == 2, "Expected 2 prime digits (2, 2) in '2020'"

    # Test with no prime digits
    assert module_0.hex_key("111") == 0, "Expected 0 prime digits in '111'"
    assert module_0.hex_key("0") == 0, "Expected 0 prime digits in '0'"
    assert module_0.hex_key("") == 0, "Expected 0 prime digits in empty string"

    # Test with all prime digits
    assert module_0.hex_key("2357BD") == 6, "Expected 6 prime digits in '2357BD'"

    # Test case sensitivity
    assert module_0.hex_key("bd") == 0, "Lowercase 'bd' should not count as prime digits"
    assert module_0.hex_key("BD") == 2, "Uppercase 'BD' should count as 2 prime digits"

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 18:28:30.075667
# Unit test for function hex_key
def test_hex_key():
    # Test with all prime hex digits
    assert module_0.hex_key("2357BD") == 6
    # Test with mixed digits
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("1077E") == 2
    # Test with no prime digits
    assert module_0.hex_key("014689AC EF") == 0
    # Test with single prime digit
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("2") == 1
    # Test with non-prime single digit
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("9") == 0
    # Test with full hex range
    assert module_0.hex_key("123456789ABCDEF0") == 6
    # Test with repeated primes
    assert module_0.hex_key("2020") == 2
    # Test with empty string
    assert module_0.hex_key("") == 0
    # Test lowercase-like edge (function only checks uppercase)
    assert module_0.hex_key("FFFFFFFF") == 0
    assert module_0.hex_key("DDDD") == 4
    assert module_0.hex_key("7777") == 4
    print("All tests passed!")

test_hex_key()

# Generated at 2026-11-02 18:31:10.219229
# Unit test for function hex_key
def test_hex_key():
    # Test with typical hexadecimal strings
    assert module_0.hex_key("AB") == 1, "Test case 1 failed"
    assert module_0.hex_key("1077E") == 2, "Test case 2 failed"
    assert module_0.hex_key("ABED1A33") == 4, "Test case 3 failed"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Test case 4 failed"
    assert module_0.hex_key("2020") == 2, "Test case 5 failed"
    
    # Edge cases
    assert module_0.hex_key("") == 0, "Test case 6 failed"
    assert module_0.hex_key("DDDD") == 4, "Test case 7 failed"
    assert module_0.hex_key("FFFF") == 0, "Test case 8 failed"
    assert module_0.hex_key("2") == 1, "Test case 9 failed"
    assert module_0.hex_key("01111") == 0, "Test case 10 failed"
    assert module_0.hex_key("BBBBDDDD") == 8, "Test case 11 failed"
    
    print("All test cases passed!")


test_hex_key()