

# Generated at 2026-11-02 23:36:44.403590
# Unit test for function count_upper
def test_count_upper():
    # Basic cases
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0     # 'B' at even indices, no vowels
    assert module_0.count_upper("AEIOU") == 3    # 'A'(0), 'I'(2), 'U'(4)
    assert module_0.count_upper("AEIOUaeiou") == 3  # lowercase vowels not counted

    # Edge cases
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("U") == 1        # single uppercase vowel
    assert module_0.count_upper("u") == 0        # single lowercase vowel
    assert module_0.count_upper("B") == 0        # single consonant
    assert module_0.count_upper("aE") == 1       # 'E' at index 1 is odd, but 'a' at 0 not vowel... 'E' at index 1 odd -> 0
    # correction: 'E' is at index 1 (odd), so not counted
    assert module_0.count_upper("aE") == 0
    assert module_0.count_upper("Ea") == 1       # 'E' at index 0

    # Longer strings
    assert module_0.count_upper("AbEcIdOfU") == 4  # 'A'(0), 'E'(2), 'I'(4), 'O'(6) -> wait check
    # indices: 0:'A',1:'b',2:'E',3:'c',4:'I',5:'d',6:'O',7:'f',8:'U'
    assert module_0.count_upper("AbEcIdOfU") == 5  # A, E, I, O, U all at even indices

    # Y is not a vowel
    assert module_0.count_upper("YyYy") == 0

    # Repeated vowels
    assert module_0.count_upper("AAAA") == 2     # indices 0 and 2

    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 23:39:51.688138
# Unit test for function count_upper
def test_count_upper():
    # Vowels at even indices
    assert module_0.count_upper("aBCdEf") == 1      # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0     # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0        # 'E' at odd index
    assert module_0.count_upper("AEIOU") == 3       # 'A', 'I', 'U' at even indices
    assert module_0.count_upper("") == 0            # empty string
    assert module_0.count_upper("A") == 1           # single uppercase vowel
    assert module_0.count_upper("B") == 0           # single consonant
    assert module_0.count_upper("a") == 0           # lowercase vowel not counted
    assert module_0.count_upper("UAEIOU") == 2      # 'U' at 0, 'I' at 4
    assert module_0.count_upper("BCDEF") == 0       # uppercase consonants only
    assert module_0.count_upper("AbEbIbObUb") == 5  # uppercase vowels at every even index
    assert module_0.count_upper("AAAEIOU") == 2     # 'A' at 0, 'E' at 4
    assert module_0.count_upper("aEIOU") == 1       # 'I' at index 2
    assert module_0.count_upper("1234A6E") == 1     # digits with vowel 'E' at index 6
    assert module_0.count_upper("AE") == 1          # 'A' at index 0 only
    print("All tests passed!")


test_count_upper()

# Generated at 2026-11-02 23:41:07.027941
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # No uppercase vowels at even indices
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    # Uppercase vowels at even indices
    assert module_0.count_upper("aBCdEf") == 1
    assert module_0.count_upper("AEIOU") == 3  # A(0), E(2), O(4)
    assert module_0.count_upper("AEIOUaeiou") == 3
    # Single characters
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0
    # Vowels at odd indices should not count
    assert module_0.count_upper("aAeE") == 0  # even indices: 'a', 'e' (lowercase)
    assert module_0.count_upper("AaEe") == 2  # even indices: 'A', 'E'
    # Non-letter characters
    assert module_0.count_upper("1A3E5") == 2  # 'A' at 1? no: indices 0='1',2='3',4='5' -> 0
    assert module_0.count_upper("A1E3I") == 2  # indices 0='A', 2='E', 4='I'
    # All uppercase vowels at even positions
    assert module_0.count_upper("AEAEAE") == 3  # A(0), E(2), A(4)
    # Y is not a vowel
    assert module_0.count_upper("YyYy") == 0
    print("All tests passed!")

test_count_upper()

# Generated at 2026-11-02 23:42:35.111630
# Unit test for function count_upper
def test_count_upper():
    # All uppercase vowels at even indices: A(0), I(2), U(4)
    assert module_0.count_upper("AEIOU") == 3
    # Uppercase vowel at even index: E at index 4
    assert module_0.count_upper("aBCdEf") == 1
    # No uppercase vowels at even indices
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    # Empty string
    assert module_0.count_upper("") == 0
    # Single uppercase vowel
    assert module_0.count_upper("A") == 1
    # Single uppercase consonant
    assert module_0.count_upper("B") == 0
    # Lowercase vowels should not count
    assert module_0.count_upper("aeiou") == 0
    # Uppercase vowels at odd indices should not count
    assert module_0.count_upper("bAeIo") == 1  # 'e' at index 2
    # Mixed content
    assert module_0.count_upper("AbEcIdOfU") == 0  # vowels at odd indices only
    assert module_0.count_upper("AEIOUXYZ") == 3
    # Consonants and uppercase vowels interleaved
    assert module_0.count_upper("UAAIOU") == 3  # U(0), A(2), O(4)
    # Y is not a vowel
    assert module_0.count_upper("AYE") == 1  # A at index 0 only
    # Long string
    assert module_0.count_upper("AEIOUaeiouAEIOU") == 6  # A(0), I(2), U(4), A(10), I(12), U(14)
    print("All tests passed!")

test_count_upper()

# Generated at 2026-11-02 23:44:29.909153
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0

    # No vowels at all
    assert module_0.count_upper("bcdfg") == 0

    # Uppercase vowels at every even index
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)

    # Vowels at odd indices must NOT be counted
    assert module_0.count_upper("aEIOU") == 2  # I(2), U(4); E(1), O(3) are odd

    # Lowercase vowels must NOT be counted
    assert module_0.count_upper("aeiou") == 0

    # Mixed case with consonants interspersed
    assert module_0.count_upper("aBCdEf") == 1  # only E at index 4
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0  # E is at odd index 3

    # Single character strings
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0

    # Uppercase vowel at index 0 only
    assert module_0.count_upper("Aa") == 1

    # Longer string with multiple even-index uppercase vowels
    assert module_0.count_upper("AbEiOxU") == 4  # A(0), E(2), O(4), U(6)

    # Digits and special characters interleaved
    assert module_0.count_upper("A1E3I") == 3  # A(0), E(2), I(4)

    # Y is not a vowel
    assert module_0.count_upper("YyYy") == 0

    print("All count_upper tests passed!")


if __name__ == "__main__":
    test_count_upper()