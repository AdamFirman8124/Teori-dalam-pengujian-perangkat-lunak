

# Generated at 2026-11-02 23:50:35.792366
# Unit test for function count_upper
def test_count_upper():
    # Test with empty string
    assert module_0.count_upper("") == 0

    # Test with uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)

    # Test with uppercase vowels at odd indices only (should not count)
    assert module_0.count_upper("aXbXcXd") == 0

    # Test from HumanEval examples
    assert module_0.count_upper("aBCdEf") == 1  # E at index 4
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0

    # Test with mixed case vowels
    assert module_0.count_upper("aEiOu") == 1  # E at index 1 (odd), wait: a(0) E(1) i(2) O(3) u(4) -> 0 at even... 
    # Recalculate: indices 0='a', 2='i', 4='u' -> none are uppercase vowels
    assert module_0.count_upper("aEiOu") == 0

    # Test with repeated uppercase vowels at even indices
    assert module_0.count_upper("AEAEAE") == 3  # A(0), A(2), A(4)

    # Test with single character
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0

    # Test with vowels including Y (Y is not a vowel here)
    assert module_0.count_upper("AYEYIYOYU") == 3  # A(0), I(4), U(8)

    # Test long string with no vowels at even indices
    assert module_0.count_upper("bdfhjlnprtvxz") == 0

    # Test string of numbers and symbols
    assert module_0.count_upper("1E3I5U") == 3  # E(1)? no wait: 1(0) E(1) 3(2) I(3) 5(4) U(5) -> even indices: 1,3,5 -> 0
    # Recalculate: even indices are 0,2,4 -> '1','3','5' -> 0 vowels
    assert module_0.count_upper("1E3I5U") == 0

    # Test string where uppercase vowels are exactly at even positions
    assert module_0.count_upper("EIEIO") == 3  # E(0), E(2), O(4)

    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 23:51:35.593766
# Unit test for function count_upper
def test_count_upper():
    # Basic cases
    assert module_0.count_upper("aBCdEf") == 1  # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0  # 'E' at odd index
    assert module_0.count_upper("AEIOU") == 3  # 'A', 'I', 'U' at even indices

    # Edge cases
    assert module_0.count_upper("") == 0  # empty string
    assert module_0.count_upper("A") == 1  # single uppercase vowel
    assert module_0.count_upper("a") == 0  # single lowercase vowel
    assert module_0.count_upper("B") == 0  # single consonant

    # Vowels at odd indices only
    assert module_0.count_upper("bAbIbU") == 0  # vowels at odd positions

    # All even positions are uppercase vowels
    assert module_0.count_upper("AAAA") == 2  # indices 0 and 2

    # Mixed content
    assert module_0.count_upper("UaEaIaO") == 3  # 'U', 'E', 'I' at even indices
    assert module_0.count_upper("XYZ") == 0  # no vowels at all

    # Longer string
    assert module_0.count_upper("AEIOUaeiouAEIOU") == 5  # indices 0,2,4,10,12 -> A,I,U,A,U

    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 23:52:17.602627
# Unit test for function count_upper
def test_count_upper():
    # Test with a string containing uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    
    # Test with empty string
    assert module_0.count_upper("") == 0
    
    # Test with no uppercase vowels at even indices
    assert module_0.count_upper("bcdfg") == 0
    
    # Test with lowercase vowels (should not count)
    assert module_0.count_upper("aeiou") == 0
    
    # Test with mixed case
    assert module_0.count_upper("AbE") == 1  # A(0) counted, E(2) counted... wait, E at index 2
    
    # Test single character
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("E") == 1
    assert module_0.count_upper("I") == 1
    assert module_0.count_upper("O") == 1
    assert module_0.count_upper("U") == 1
    assert module_0.count_upper("B") == 0
    
    # Test with two characters
    assert module_0.count_upper("AE") == 1  # A at 0 counted, E at 1 not (odd index)
    
    # Test with example from prompt style
    assert module_0.count_upper("aBCdEf") == 1  # E at index 4
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    
    # Test with uppercase vowels at odd indices only (should not count)
    assert module_0.count_upper("bA") == 0  # A at index 1 (odd)
    
    # Test with numbers and special characters
    assert module_0.count_upper("A1E3I") == 3  # A(0), E(2), I(4)
    assert module_0.count_upper("A!E?I") == 3
    
    # Test longer string
    assert module_0.count_upper("AEIOUaeiouAEIOU") == 6  # A(0), I(2), U(4), A(10), I(12), U(14)
    
    # Test with 'Y' (not a vowel in this implementation)
    assert module_0.count_upper("Y") == 0
    
    print("All test cases passed!")


test_count_upper()

# Generated at 2026-11-02 23:53:33.563379
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("aBCdEf") == 1
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    assert module_0.count_upper("AEIOU") == 3
    assert module_0.count_upper("AEIOUaeiou") == 3
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("b") == 0
    assert module_0.count_upper("AbCdEf") == 2
    assert module_0.count_upper("XyZ") == 0
    assert module_0.count_upper("OaEiOu") == 2
    assert module_0.count_upper("U") == 1

# Generated at 2026-11-02 23:54:12.674922
# Unit test for function count_upper
def test_count_upper():
    # Uppercase vowel at even index counts
    assert module_0.count_upper("aBCdEf") == 1      # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0     # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0        # 'E' at odd index 3, not counted
    assert module_0.count_upper("AEIOU") == 3       # 'A'(0), 'I'(2), 'U'(4)
    assert module_0.count_upper("aeiou") == 0       # lowercase vowels not counted
    assert module_0.count_upper("") == 0            # empty string
    assert module_0.count_upper("A") == 1           # single uppercase vowel
    assert module_0.count_upper("a") == 0           # single lowercase vowel
    assert module_0.count_upper("aAeEiIoOuU") == 0  # uppercase vowels all at odd indices
    assert module_0.count_upper("UuUu") == 2        # 'U' at indices 0 and 2
    assert module_0.count_upper("BCDFG") == 0       # no vowels at all
    assert module_0.count_upper("AbEcIdOfU") == 5   # uppercase vowels at every even index

    print("All test cases passed!")


test_count_upper()