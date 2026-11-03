

# Generated at 2026-11-02 14:07:36.710388
# Unit test for function get_closest_vowel
def test_get_closest_vowel():# nonce:f372fb1d
    # Words shorter than 3 characters return ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("b") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("Ab") == ""

    # Canonical examples
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""

    # Vowel must sit strictly between two non-vowels
    assert module_0.get_closest_vowel("XaX") == "a"
    assert module_0.get_closest_vowel("aba") == ""      # edge vowels don't count
    assert module_0.get_closest_vowel("aaa") == ""      # adjacent vowels disqualify
    assert module_0.get_closest_vowel("aeiou") == ""    # no consonant neighbors
    assert module_0.get_closest_vowel("bcda") == ""     # trailing vowel not checked
    assert module_0.get_closest_vowel("abcd") == ""     # leading vowel not checked

    # Rightmost qualifying vowel is returned
    assert module_0.get_closest_vowel("bAbEb") == "E"
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("strength") == "e"

    # Mixed-case handling
    assert module_0.get_closest_vowel("bEg") == "E"
    assert module_0.get_closest_vowel("QUICK") == ""
    assert module_0.get_closest_vowel("worD") == "o"

    # Non-letter characters count as non-vowels
    assert module_0.get_closest_vowel("1a1") == "a"
    assert module_0.get_closest_vowel("a1e") == ""

    # No vowels present ('y' is not treated as a vowel)
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("xyz") == ""

# Generated at 2026-11-02 14:09:24.233756
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel between consonants -> returns that vowel
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("example") == "a"

    # No qualifying vowel (vowel adjacent to another vowel)
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("apple") == ""

    # No vowels at all
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Words shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("ae") == ""

    # Vowel at edge positions should not count (loop excludes index 0 and len-1)
    assert module_0.get_closest_vowel("open") == ""      # 'o' at index 0 not checked
    assert module_0.get_closest_vowel("idea") == ""      # 'e' at index 3 has 'a' after? check: i=2 'e', word[3]='a' is vowel -> skip; i=1 'd' no
    assert module_0.get_closest_vowel("baked") == "e"    # i=3 'e', word[4]='d' ok, word[2]='k' ok

    print("All tests passed!")


if __name__ == "__main__":
    test_get_closest_vowel()

# Generated at 2026-11-02 14:11:00.757777
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    assert module_0.get_closest_vowel("yogurt") == "U"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("banana") == "a"
    assert module_0.get_closest_vowel("Alone") == "o"
    assert module_0.get_closest_vowel("bcdfg") == ""
    assert module_0.get_closest_vowel("XeZeY") == "E"
    assert module_0.get_closest_vowel("Ok") == ""
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bAc") == "A"
    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 14:12:44.224035
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic cases: vowel between two consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("quick") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # Word shorter than 3 characters
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ae") == ""

    # Single vowel between consonants
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("bat") == "a"
    assert module_0.get_closest_vowel("bEd") == "E"

    # No vowels at all
    assert module_0.get_closest_vowel("rhythm") == ""
    assert module_0.get_closest_vowel("bcdfg") == ""

    # Adjacent vowels disqualify candidates
    assert module_0.get_closest_vowel("aeiou") == ""
    assert module_0.get_closest_vowel("aa") == ""

    # Vowel at edges (index 0 or last) cannot qualify
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("ea") == ""

    # Finds the closest (rightmost) qualifying vowel
    assert module_0.get_closest_vowel("general") == "a"
    assert module_0.get_closest_vowel("BEAUTIFUL") == "U"

    # Mixed case handling
    assert module_0.get_closest_vowel("bOok") == "O"
    assert module_0.get_closest_vowel("bEst") == "E"

    print("All tests passed!")


test_get_closest_vowel()

# Generated at 2026-11-02 14:14:28.570855
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Vowel found between two consonants, searching from the right
    assert module_0.get_closest_vowel("yogurt") == "u"
    # Uppercase vowel between consonants
    assert module_0.get_closest_vowel("FULL") == "U"
    # No vowel surrounded by consonants (vowels adjacent to vowels)
    assert module_0.get_closest_vowel("quick") == ""
    # Word shorter than 3 characters
    assert module_0.get_closest_vowel("ab") == ""
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("bc") == ""
    # Vowel at the very start (left neighbor is boundary) -> not valid
    assert module_0.get_closest_vowel("apple") == "e"
    # Only consonants
    assert module_0.get_closest_vowel("bcdfg") == ""
    # Vowel at last index is never checked
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("Kitten") == "e"
    # All vowels, none isolated between consonants
    assert module_0.get_closest_vowel("aeiou") == ""
    # Mixed case check
    assert module_0.get_closest_vowel("bEd") == "E"
    # Rightmost valid vowel wins
    assert module_0.get_closest_vowel("banana") == "a"

    print("All tests passed!")


if __name__ == "__main__":
    test_get_closest_vowel()