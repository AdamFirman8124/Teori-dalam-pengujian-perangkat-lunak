

# Generated at 2026-11-02 13:31:57.521628
# Unit test for function hex_key
def test_hex_key():
    # Test with string containing no prime digits
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("014689ACEF") == 0

    # Test with single prime digit
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("3") == 1
    assert module_0.hex_key("5") == 1
    assert module_0.hex_key("7") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # Test with all prime digits
    assert module_0.hex_key("2357BD") == 6

    # Test with standard examples
    assert module_0.hex_key("AB") == 1          # B is prime
    assert module_0.hex_key("1077E") == 2       # two 7s are prime
    assert module_0.hex_key("ABED1A33") == 4    # B, D, 3, 3 are prime
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D
    assert module_0.hex_key("2020") == 2        # two 2s

    # Test with repeated digits
    assert module_0.hex_key("2222") == 4
    assert module_0.hex_key("BBBB") == 4

    # Test with mixed digits
    assert module_0.hex_key("F1E5D7") == 3      # 5, D, 7
    assert module_0.hex_key("FFFF") == 0
    assert module_0.hex_key("9999999999") == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 13:34:01.975846
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("AB") == 1          # 'B' is prime
    assert module_0.hex_key("1077E") == 2       # '7' appears twice
    assert module_0.hex_key("ABED1A33") == 4    # 'B', 'D', '3', '3'
    assert module_0.hex_key("123456789ABCDEF0") == 6  # '2', '3', '5', '7', 'B', 'D'
    assert module_0.hex_key("2020") == 2        # two '2's
    assert module_0.hex_key("") == 0            # empty string has no primes
    assert module_0.hex_key("111") == 0         # '1' is not prime
    assert module_0.hex_key("DD") == 2          # 'D' appears twice
    assert module_0.hex_key("F") == 0           # 'F' is not prime
    print("All tests passed!")

if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 13:35:09.037260
# Unit test for function hex_key
def test_hex_key():
    # Basic examples
    assert module_0.hex_key("AB") == 1, "Expected 1 prime digit (B) in 'AB'"
    assert module_0.hex_key("1077E") == 2, "Expected 2 prime digits (7, 7) in '1077E'"
    assert module_0.hex_key("ABED1A33") == 4, "Expected 4 prime digits (B, 3, D, 3) in 'ABED1A33'"
    assert module_0.hex_key("123456789ABCDEF0") == 6, "Expected 6 prime digits (2, 3, 5, 7, B, D)"
    assert module_0.hex_key("2020") == 2, "Expected 2 prime digits (2, 2) in '2020'"

    # Edge cases
    assert module_0.hex_key("") == 0, "Empty string should return 0"
    assert module_0.hex_key("111") == 0, "No prime digits in '111'"
    assert module_0.hex_key("FFFF") == 0, "No prime digits in 'FFFF'"
    assert module_0.hex_key("2222") == 4, "All digits prime in '2222'"
    assert module_0.hex_key("DD") == 2, "All digits prime in 'DD'"
    assert module_0.hex_key("0") == 0, "Single non-prime digit '0'"
    assert module_0.hex_key("5") == 1, "Single prime digit '5'"
    assert module_0.hex_key("aB") == 1, "Lowercase 'a' not prime, uppercase 'B' is prime"

    print("All tests passed!")


if __name__ == "__main__":
    test_hex_key()

# Generated at 2026-11-02 13:36:07.981905
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("2020") == 2
    assert module_0.hex_key("123456789ABCDEF0") == 6
    assert module_0.hex_key("1122334455667788") == 6
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("D") == 1
    assert module_0.hex_key("BBBB") == 4
    assert module_0.hex_key("7777777") == 7
    assert module_0.hex_key("13579BDF2468ACE0") == 8
    assert module_0.hex_key("FFFF") == 0
    assert module_0.hex_key("2468ACE") == 0
    print("All test cases passed!")

test_hex_key()

# Generated at 2026-11-02 13:36:22.280300
# Unit test for function hex_key
def test_hex_key():
    # Empty string has no prime digits
    assert module_0.hex_key("") == 0

    # No prime digits present
    assert module_0.hex_key("14") == 0
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("0189CF") == 0

    # Single prime digit
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("B") == 1
    assert module_0.hex_key("D") == 1

    # Known examples
    assert module_0.hex_key("AB") == 1          # only B is prime
    assert module_0.hex_key("1077E") == 2       # 7, 7
    assert module_0.hex_key("ABED1A33") == 4    # B, D, 3, 3
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D
    assert module_0.hex_key("2020") == 2        # 2, 2

    # Repeated prime digits
    assert module_0.hex_key("3333") == 4
    assert module_0.hex_key("777BDDB") == 6

    # Lowercase letters are not counted (case-sensitive)
    assert module_0.hex_key("bd") == 0
    assert module_0.hex_key("bD") == 1

    # Mixed content
    assert module_0.hex_key("FF2D5") == 3       # 2, D, 5

    print("All hex_key tests passed!")


if __name__ == "__main__":
    test_hex_key()