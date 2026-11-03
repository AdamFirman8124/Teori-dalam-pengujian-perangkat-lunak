

# Generated at 2026-11-02 16:34:12.090574
# Unit test for function count_upper
def test_count_upper():
# nonce:38f94db0
    assert module_0.count_upper('aBCdEf') == 1   # 'E' at index 4
    assert module_0.count_upper('abcdefg') == 0  # no uppercase vowels at even indices
    assert module_0.count_upper('dBBE') == 0     # 'E' at odd index 3
    assert module_0.count_upper('AEIOU') == 3    # 'A', 'I', 'U' at indices 0, 2, 4
    assert module_0.count_upper('') == 0         # empty string
    assert module_0.count_upper('B') == 0        # single non-vowel char
    assert module_0.count_upper('xX') == 0       # no vowels
    assert module_0.count_upper('AbCdE') == 2    # 'A' at index 0, 'E' at index 4
    assert module_0.count_upper('UuUuU') == 2    # 'U' at indices 0 and 4; 'u' is lowercase
    assert module_0.count_upper('O') == 1        # single uppercase vowel

# Generated at 2026-11-02 16:35:36.447775
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # Single character, uppercase vowel
    assert module_0.count_upper("A") == 1
    # Single character, lowercase vowel
    assert module_0.count_upper("a") == 0
    # Single character, consonant
    assert module_0.count_upper("B") == 0
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    # Lowercase vowels should not count
    assert module_0.count_upper("aeiou") == 0
    # Uppercase vowels at odd indices should not count
    assert module_0.count_upper("aEeIiOuU") == 0
    # Mixed case: uppercase vowels at even indices only
    assert module_0.count_upper("AbCdEfG") == 1  # E at index 4
    # No vowels at all
    assert module_0.count_upper("BCDFG") == 0
    # Uppercase vowels at even indices with consonants between
    assert module_0.count_upper("AxBxCxDxE") == 3  # A(0), C(2), E(4)
    # Long string with pattern
    assert module_0.count_upper("AEAEAE") == 3  # A(0), A(2), A(4)
    # Uppercase vowels only at odd positions
    assert module_0.count_upper("xExIxO") == 0
    # Repeated uppercase vowels at even indices
    assert module_0.count_upper("AAEEIIOOUU") == 5  # indices 0,2,4,6,8
    # Consonant uppercase at even indices should not count
    assert module_0.count_upper("BCDFGHI") == 0  # I is at odd index 5... wait, I at index 5? "BCDFGHI": B(0)C(1)D(2)F(3)G(4)H(5)I(6) -> I at even index 6 counts
    assert module_0.count_upper("BCDFGHI") == 1  # I at index 6
    # Uppercase vowel 'Y' not counted
    assert module_0.count_upper("YyYy") == 0
    # String with digits and symbols
    assert module_0.count_upper("A1E2I3") == 3  # A(0), E(2), I(4)
    # Whitespace at even indices
    assert module_0.count_upper(" A E I ") == 0  # spaces at even indices
    # Uppercase vowels spread out
    assert module_0.count_upper("aXbEcIdOfU") == 0  # vowels at odd indices only
    assert module_0.count_upper("AxExIxOxU") == 5  # A(0), E(2), I(4), O(6), U(8)

    print("All tests passed!")

test_count_upper()

# Generated at 2026-11-02 16:36:57.509918
# Unit test for function count_upper
def test_count_upper():
    # Test with alternating uppercase vowels
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    assert module_0.count_upper("aBCdEf") == 1  # E(4)
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0  # no vowels at even indices
    assert module_0.count_upper("") == 0  # empty string
    assert module_0.count_upper("A") == 1  # single uppercase vowel
    assert module_0.count_upper("B") == 0  # single non-vowel
    assert module_0.count_upper("a") == 0  # single lowercase vowel
    assert module_0.count_upper("AEIOUxyz") == 3  # A(0), I(2), U(4)
    assert module_0.count_upper("UAEIO") == 2  # U(0), I(2)
    assert module_0.count_upper("XYZAE") == 1  # A(3 is odd? No: X(0),Z(2),A(4)) -> actually A at index 4
    assert module_0.count_upper("AAAEIOU") == 3  # A(0), A(2), I(4)
    assert module_0.count_upper("aXbXcXdE") == 0  # E at index 7 (odd)
    assert module_0.count_upper("IaEaOaUa") == 3  # I(0), E(2), O(4)
    assert module_0.count_upper("AAAA") == 2  # A(0), A(2)
    print("All test cases passed!")

if __name__ == "__main__":
    test_count_upper()

# Generated at 2026-11-02 16:38:22.988770
# Unit test for function count_upper
def test_count_upper():
    # Basic examples
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels at even indices
    assert module_0.count_upper("dBBE") == 0     # 'E' is at odd index
    assert module_0.count_upper("B") == 0        # single consonant

    # Edge cases
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("A") == 1        # single uppercase vowel
    assert module_0.count_upper("aA") == 0       # vowel at odd index doesn't count
    assert module_0.count_upper("Ab") == 1       # vowel at index 0

    # Multiple vowels at even indices
    assert module_0.count_upper("AEIOU") == 3    # A(0), I(2), U(4)
    assert module_0.count_upper("AEOUI") == 3    # A(0), O(2), I(4)
    assert module_0.count_upper("aeiou") == 0    # lowercase vowels never count
    assert module_0.count_upper("aEIoUu") == 2   # I(2), U(4)
    assert module_0.count_upper("UaEbIcO") == 4  # U(0), E(2), I(4), O(6)

    # No vowels at all
    assert module_0.count_upper("xYz") == 0
    assert module_0.count_upper("BCDFG") == 0

    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 16:40:25.501924
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # No vowels at even indices
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("aBCdEf") == 1
    # Vowels at odd indices should not count
    assert module_0.count_upper("dBBE") == 0
    # All uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3
    # Single character cases
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0
    # Mixed content
    assert module_0.count_upper("AbCdEfG") == 1
    assert module_0.count_upper("U") == 1
    assert module_0.count_upper("xYz") == 0
    # Lowercase vowels at even indices should not count
    assert module_0.count_upper("aeiou") == 0
    # Long string with vowels at even indices
    assert module_0.count_upper("AEIOUaeiou") == 3
    assert module_0.count_upper("AxEIxOxU") == 3
    # Non-letter characters
    assert module_0.count_upper("1A2E3") == 2
    assert module_0.count_upper("a!b?c") == 0
    print("All tests passed!")

test_count_upper()