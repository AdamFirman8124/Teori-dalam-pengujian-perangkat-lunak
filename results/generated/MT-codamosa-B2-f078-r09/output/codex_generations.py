

# Generated at 2026-11-02 12:45:01.746142
# Unit test for function hex_key
def test_hex_key():
    # Test with string containing multiple prime hex digits
    assert module_0.hex_key("AB") == 1  # B is prime
    
    # Test with mixed digits
    assert module_0.hex_key("1077E") == 2  # two 7s are prime
    
    # Test with longer string
    assert module_0.hex_key("ABED1A33") == 4  # B, D, 3, 3 are prime
    
    # Test with all hex digits
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D are prime
    
    # Test with repeated prime digits
    assert module_0.hex_key("2020") == 2  # two 2s are prime
    
    # Test with no prime digits
    assert module_0.hex_key("1111") == 0
    assert module_0.hex_key("FFFFFFFF") == 0
    assert module_0.hex_key("0") == 0
    
    # Test with empty string
    assert module_0.hex_key("") == 0
    
    # Test single prime digit
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("3") == 1
    assert module_0.hex_key("5") == 1
    assert module_0.hex_key("7") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1
    
    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 12:48:08.954017
# Unit test for function hex_key
def test_hex_key():
    # Test with all prime hex digits
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("2222") == 4
    assert module_0.hex_key("2357BD") == 6

    # Test with no prime hex digits
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("1469") == 0
    assert module_0.hex_key("ACEF") == 0

    # Test with mixed prime and non-prime hex digits
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF0") == 6
    assert module_0.hex_key("2020") == 2

    # Test with repeated non-prime characters
    assert module_0.hex_key("0000") == 0
    assert module_0.hex_key("1111") == 0

    # Test with lower/upper boundary values
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1
    assert module_0.hex_key("C") == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 12:50:01.739564
# Unit test for function hex_key
def test_hex_key():
    # Single prime hex digits
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

    # Multiple characters
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF0") == 6
    assert module_0.hex_key("2020") == 2

    # Edge cases
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("1111") == 0
    assert module_0.hex_key("2222") == 4

    print("All hex_key tests passed!")


test_hex_key()

# Generated at 2026-11-02 12:51:30.896812
# Unit test for function hex_key
def test_hex_key():
    # Test with all prime hex digits
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF0") == 6
    assert module_0.hex_key("2020") == 3

    # Test with no prime hex digits
    assert module_0.hex_key("014689ACEF") == 0

    # Test empty string
    assert module_0.hex_key("") == 0

    # Test single characters
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("3") == 1
    assert module_0.hex_key("5") == 1
    assert module_0.hex_key("7") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # Test non-prime single characters
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

    # Test lowercase input (should not count as primes)
    assert module_0.hex_key("bd") == 0

    # Test repeated primes
    assert module_0.hex_key("2222") == 4
    assert module_0.hex_key("BBBB") == 4
    assert module_0.hex_key("DDDD") == 4

    # Test mixed string
    assert module_0.hex_key("2A3D4B5") == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()