

# Generated at 2026-11-02 16:53:25.712909
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("junk") == "u"
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("ACQUA") == ""
    assert module_0.get_closest_vowel("beautiful") == "u"

# Generated at 2026-11-02 16:54:31.689756
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("xy") == ""

    # Basic cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""

    # Vowel adjacent to other vowels is not counted
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"

    # No vowels between consonants
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Vowel at edge positions (index 0 or last index) is never returned
    assert module_0.get_closest_vowel("abba") == ""      # 'a' at edges, no inner vowel
    assert module_0.get_closest_vowel("cab") == "a"      # inner vowel valid

    # Mixed case handling
    assert module_0.get_closest_vowel("cAt") == "A"
    assert module_0.get_closest_vowel("CcCc") == ""

    # Multiple valid candidates: rightmost is returned
    assert module_0.get_closest_vowel("tatar") == "a"
    assert module_0.get_closest_vowel("meter") == "e"

    # Word of exactly length 3
    assert module_0.get_closest_vowel("bob") == "o"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 16:55:54.088994
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Words with a vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("beautiful") == "u"
    assert module_0.get_closest_vowel("rhythm") == ""

    # Words where the vowel has a vowel neighbor (should be skipped)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("APPLE") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("ea") == ""

    # Vowel at edge positions should not count (index 0 or len-1 excluded)
    assert module_0.get_closest_vowel("abide") == "i"   # 'i' at index 2, neighbors 'b' and 'd'
    assert module_0.get_closest_vowel("open") == ""     # vowels only at edges
    assert module_0.get_closest_vowel("bUtter") == "e"  # lowercase/uppercase mix

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 16:57:05.171339
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # nonce:c0209beb
    # Standard cases: vowel between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("abCdef") == "e"
    assert module_0.get_closest_vowel("cat") == "a"

    # No qualifying vowel (vowel adjacent to another vowel, or at edges)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("aeiouXYZ") == ""
    assert module_0.get_closest_vowel("abC") == ""
    assert module_0.get_closest_vowel("apple") == ""

    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("A") == ""
    assert module_0.get_closest_vowel("") == ""

    # Mixed case handling
    assert module_0.get_closest_vowel("bEgIn") == "I"
    assert module_0.get_closest_vowel("OrAnGe") == "n" or True  # sanity: 'g' not vowel, check below
    # "OrAnGe": i=4 'G' no; i=3 'n' no; i=2 'A' vowel, word[3]='n' not, word[1]='r' not -> 'A'
    assert module_0.get_closest_vowel("OrAnGe") == "A"

    # All consonants
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("xyz") == ""

    # Single vowel sandwiched between consonants at the last valid index
    assert module_0.get_closest_vowel("abCde") == "C" or True  # 'C' not vowel; verify real result
    # "abCde": i=3 'd' no; i=2 'C' no; i=1 'b' no -> ""
    assert module_0.get_closest_vowel("abCde") == ""

    # Vowel found at the earliest possible interior index
    assert module_0.get_closest_vowel("xay") == "a"

# Generated at 2026-11-02 16:58:44.999745
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""  # 'u' and 'i' adjacent to each other
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("abc") == ""  # no vowels

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("Au") == ""

    # All vowels adjacent -> no qualifying vowel
    assert module_0.get_closest_vowel("aei") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("XaeiouX") == ""
    assert module_0.get_closest_vowel("XeaX") == ""

    # Uppercase vowels are recognized
    assert module_0.get_closest_vowel("bAc") == "A"
    assert module_0.get_closest_vowel("XEXO") == "E"

    # Scans right-to-left: returns rightmost qualifying vowel
    assert module_0.get_closest_vowel("uXeXoX") == "o"
    assert module_0.get_closest_vowel("bXaXeXeX") == "e"

    # First and last characters are never eligible
    assert module_0.get_closest_vowel("aqoXe") == "o"
    assert module_0.get_closest_vowel("aXoXe") == "o"

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("12345") == ""


if __name__ == "__main__":
    test_get_closest_vowel()
    print("All tests passed!")