

# Generated at 2026-11-02 21:22:03.958577
# Unit test for function count_upper
def test_count_upper():
    # nonce:874c9725
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4 (even) counts
    assert module_0.count_upper("abcdefg") == 0  # only lowercase vowels, none count
    assert module_0.count_upper("dBBE") == 0     # 'E' at odd index 3, doesn't count
    assert module_0.count_upper("A") == 1        # single uppercase vowel at index 0
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("AEIOU") == 3    # 'A'(0), 'I'(2), 'U'(4) count
    assert module_0.count_upper("aeiou") == 0    # lowercase vowels never count
    assert module_0.count_upper("AbE") == 2      # 'A'(0) and 'E'(2) count
    assert module_0.count_upper("BCDFG") == 0    # no vowels at all
    assert module_0.count_upper("UaEaIaOaA") == 5  # all even indices are uppercase vowels
    assert module_0.count_upper("aAaAaA") == 3   # 'A' at indices 1,3,5 don't count... 
    # correction: 'A' at indices 1,3,5 are odd; even indices are 'a' -> 0

# Generated at 2026-11-02 21:23:51.493596
# Unit test for function count_upper
def test_count_upper():
# nonce:33586201
    assert module_0.count_upper("aBCdEf") == 1
    assert module_0.count_upper("abcdefg") == 0
    assert module_0.count_upper("dBBE") == 0
    assert module_0.count_upper("AEIOU") == 3   # indices 0,2,4 -> 'A','I','U'
    assert module_0.count_upper("AEIOUAE") == 4 # indices 0,2,4,6 -> 'A','I','U','A'
    assert module_0.count_upper("B") == 0
    assert module_0.count_upper("E") == 1
    assert module_0.count_upper("bE") == 0      # 'E' is at odd index
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("aeiou") == 0   # lowercase vowels don't count
    assert module_0.count_upper("AxBxCxDx") == 1
    assert module_0.count_upper("12345") == 0

# Generated at 2026-11-02 21:25:26.800985
# Unit test for function count_upper
def test_count_upper():
    # Basic cases
    assert module_0.count_upper("aBCdEf") == 1   # 'E' at index 4
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0     # 'E' at odd index
    assert module_0.count_upper("AEIOU") == 2    # 'A' at 0, 'I' at 2, 'U' at 4 -> actually 3
    # Correction: 'A'(0), 'I'(2), 'U'(4) are all at even indices
    assert module_0.count_upper("AEIOU") == 3

    # Edge cases
    assert module_0.count_upper("") == 0         # empty string
    assert module_0.count_upper("A") == 1        # single uppercase vowel
    assert module_0.count_upper("a") == 0        # single lowercase vowel
    assert module_0.count_upper("B") == 0        # single consonant

    # Vowels at even indices
    assert module_0.count_upper("AEIOUaeiou") == 3   # A(0), I(2), U(4)
    assert module_0.count_upper("aEiOu") == 0        # E(1), O(3) at odd indices

    # Mixed characters
    assert module_0.count_upper("UAA") == 2      # U(0), A(2)
    assert module_0.count_upper("XAEIOUX") == 2  # A(1)? no -> A(1) odd, I(3) odd, U(4) even -> 1
    # Correction: A at index 1 (odd), E at 2 (even), I at 3 (odd), O at 4 (even), U at 5 (odd)
    assert module_0.count_upper("XAEIOUX") == 2  # E(2), O(4)

    # Long string alternating
    assert module_0.count_upper("AaEaIaOaU") == 5  # A(0), E(2), I(4), O(6), U(8)

    # Uppercase consonants don't count
    assert module_0.count_upper("BCDFG") == 0

    # Y is not a vowel
    assert module_0.count_upper("YAY") == 0

    # Repeated uppercase vowels at even indices
    assert module_0.count_upper("AAAA") == 2     # A(0), A(2)

    print("All tests passed!")


if __name__ == "__main__":
    test_count_upper()

# Generated at 2026-11-02 21:27:52.846156
# Unit test for function count_upper
def test_count_upper():
    # provided examples
    assert module_0.count_upper('aBCdEf') == 1   # 'E' at index 4
    assert module_0.count_upper('abcdefg') == 0  # no uppercase vowels at even indices
    assert module_0.count_upper('dBBE') == 0     # 'E' at odd index 3
    # empty string
    assert module_0.count_upper('') == 0
    # single characters
    assert module_0.count_upper('A') == 1
    assert module_0.count_upper('a') == 0
    assert module_0.count_upper('B') == 0
    # uppercase vowel at odd index should not count
    assert module_0.count_upper('aA') == 0
    # all uppercase vowels
    assert module_0.count_upper('AEIOU') == 3    # A(0), I(2), U(4)
    assert module_0.count_upper('EaEaE') == 3    # E(0), E(2), E(4)
    # no vowels at all
    assert module_0.count_upper('bcd') == 0
    # long string
    assert module_0.count_upper('AbEcIdOfU') == 4  # A(0), E(2), I(4), U(6)

if __name__ == "__main__":
    test_count_upper()
    print("All tests passed!")

# Generated at 2026-11-02 21:29:11.406134
# Unit test for function count_upper
def test_count_upper():
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3  # A(0), I(2), U(4)
    assert module_0.count_upper("aBCdEf") == 1  # E(4)
    assert module_0.count_upper("abcdefg") == 0  # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0  # E at odd index
    assert module_0.count_upper("B") == 0  # no vowel
    assert module_0.count_upper("U") == 1  # U at even index
    assert module_0.count_upper("AbE") == 1  # A(0)
    assert module_0.count_upper("AbCdEf") == 2  # A(0), E(4)
    assert module_0.count_upper("aBCdEFEF") == 2  # E(4), E(6)
    # Edge cases
    assert module_0.count_upper("") == 0  # empty string
    assert module_0.count_upper("bcdfg") == 0  # no vowels at all
    assert module_0.count_upper("OaEiOu") == 3  # O(0), E(2), O(4)
    print("All tests passed!")

test_count_upper()