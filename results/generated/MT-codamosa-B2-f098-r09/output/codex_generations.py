

# Generated at 2026-11-02 21:03:15.049897
# Unit test for function count_upper
def test_count_upper():
    # Test with uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 2  # A(0), I(2) counted; E(1), O(3), U(4... even but U counted? No, index 4 is even -> "U" in "AEIOU") 
    # Let's verify: indices 0,2,4 -> 'A', 'I', 'U' -> count = 3
    assert module_0.count_upper("AEIOU") == 3

    # Test with lowercase vowels at even indices (should not count)
    assert module_0.count_upper("aeiou") == 0

    # Test with uppercase vowels at odd indices (should not count)
    assert module_0.count_upper("aEiOu") == 0

    # Test with mixed case
    assert module_0.count_upper("AbCdEf") == 1  # only A at index 0
    assert module_0.count_upper("ABCDEF") == 1  # only A at index 0
    assert module_0.count_upper("UOAIEX") == 3  # U(0), A(2), E(4)

    # Test with no vowels
    assert module_0.count_upper("BCDFG") == 0
    assert module_0.count_upper("xyz") == 0

    # Test with empty string
    assert module_0.count_upper("") == 0

    # Test with single characters
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0

    # Test with two characters
    assert module_0.count_upper("AE") == 1  # A at index 0 only
    assert module_0.count_upper("EA") == 1  # E at index 0 only

    # Test with longer string
    assert module_0.count_upper("AbEcIdOfU") == 4  # A(0), E(2), I(4), O(6); U at index 8 not present
    assert module_0.count_upper("aEiOaEiO") == 0  # all vowels at odd indices

    # Test with digits and special characters
    assert module_0.count_upper("A1B2C3") == 1
    assert module_0.count_upper("!A?E#O") == 2  # A(1)? No - ! is index 0, A index 1... 
    # indices: 0='!', 1='A', 2='?', 3='E', 4='#', 5='O' -> none at even indices
    assert module_0.count_upper("!A?E#O") == 0
    assert module_0.count_upper("A!E?O#") == 3  # A(0), E(2), O(4)

    print("All test cases passed!")


test_count_upper()

# Generated at 2026-11-02 21:03:29.716232
# Unit test for function count_upper
def test_count_upper():
    # Basic test cases
    assert module_0.count_upper('aBCdEf') == 1   # 'E' at index 4
    assert module_0.count_upper('abcdefg') == 0  # no uppercase vowels
    assert module_0.count_upper('dBBE') == 0     # 'E' at odd index
    assert module_0.count_upper('AEIOU') == 2    # 'A' at 0, 'I' at 2 (O, U at odd indices)

    # Edge cases
    assert module_0.count_upper('') == 0              # empty string
    assert module_0.count_upper('A') == 1             # single uppercase vowel
    assert module_0.count_upper('a') == 0             # single lowercase vowel
    assert module_0.count_upper('B') == 0             # single consonant

    # Vowels at even indices only
    assert module_0.count_upper('AEIOUXY') == 2       # A(0), I(2), O(4) -> wait, O at 4 counts

    # Mixed case checks
    assert module_0.count_upper('aAeEiIoOuU') == 0    # uppercase vowels at odd indices
    assert module_0.count_upper('AaEeIiOoUu') == 5    # uppercase vowels at even indices

    # Consonants and non-letters
    assert module_0.count_upper('1234A678E') == 2     # digits skipped, A(4), E(8)
    assert module_0.count_upper('!A#E%I') == 3        # special chars, A(1)? no: A at 1, E at 3, I at 5

# Generated at 2026-11-02 21:04:16.239700
# Unit test for function count_upper
def test_count_upper():
    # nonce:58ce7323
    # Empty string
    assert module_0.count_upper("") == 0
    
    # No vowels at all
    assert module_0.count_upper("bcdfg") == 0
    
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    assert module_0.count_upper("aBCdE") == 1  # E(4)
    
    # Lowercase vowels should not count
    assert module_0.count_upper("aeiou") == 0
    assert module_0.count_upper("abcdefg") == 0
    
    # Vowels at odd indices should not count
    assert module_0.count_upper("aEiOu") == 0
    assert module_0.count_upper("xExExE") == 3  # E at 1,3,5 are odd -> 0? No: indices 1,3,5 odd
    # Correction: "xExExE" -> even indices: x(0), x(2), x(4) -> 0
    assert module_0.count_upper("xExExE") == 0
    
    # All uppercase vowels at even positions
    assert module_0.count_upper("AAAA") == 2  # A(0), A(2)
    assert module_0.count_upper("EEEEEE") == 3  # E(0), E(2), E(4)
    
    # Mixed content
    assert module_0.count_upper("AbCdEfG") == 1  # E(4)
    assert module_0.count_upper("OaUeIi") == 2  # O(0), U(2)
    
    # Single character
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0
    
    # Consonants only at even indices
    assert module_0.count_upper("BCDF") == 0
    
    # Uppercase vowels interleaved
    assert module_0.count_upper("IAmOaTest") == 2  # I(0), O(4)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_count_upper()

# Generated at 2026-11-02 21:04:52.718025
# Unit test for function count_upper
def test_count_upper():
    # Uppercase vowels at even indices
    assert module_0.count_upper('aBCdEf') == 1      # 'E' at index 4
    assert module_0.count_upper('abcdefg') == 0     # no uppercase vowels
    assert module_0.count_upper('dBBE') == 0        # 'E' at odd index 3
    assert module_0.count_upper('AEIOU') == 3       # 'A','E','U' at indices 0,2,4
    assert module_0.count_upper('AEIOUaeiou') == 3  # lowercase vowels don't count
    assert module_0.count_upper('') == 0            # empty string
    assert module_0.count_upper('U') == 1           # single uppercase vowel
    assert module_0.count_upper('u') == 0           # single lowercase vowel
    assert module_0.count_upper('AaAaA') == 3       # alternating vowels
    assert module_0.count_upper('BCDFG') == 0       # consonants only
    assert module_0.count_upper('O!E!U!') == 3      # non-letters don't interfere
    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 21:06:02.161336
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("aBCdEf") == 1  # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0  # 'E' at odd index
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    assert module_0.count_upper("") == 0  # empty string
    assert module_0.count_upper("A") == 1  # single uppercase vowel
    assert module_0.count_upper("a") == 0  # single lowercase vowel
    assert module_0.count_upper("BCDEF") == 1  # 'E' at index 2
    assert module_0.count_upper("aAeEiIoOuU") == 5  # uppercase vowels at even indices
    assert module_0.count_upper("AEIOUaeiou") == 3  # uppercase vowels in first half
    assert module_0.count_upper("XYZ") == 0  # no vowels at all
    assert module_0.count_upper("UaEaIaOaA") == 5  # uppercase vowels at even indices
    assert module_0.count_upper("aaAA") == 1  # 'A' at index 2
    print("All test cases passed!")


test_count_upper()