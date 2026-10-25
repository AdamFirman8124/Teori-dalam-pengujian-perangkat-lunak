# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

def test_encode_replaces_vowels_and_swaps_case():
    from f093 import encode

    # "aeiou" -> swapcase -> "AEIOU" -> each vowel shifted by 2:
    # A->C, E->G, I->K, O->Q, U->W
    assert encode("aeiou") == "CGKQW"
    # "AEIOU" -> swapcase -> "aeiou" -> shifted -> "cgkqw"
    assert encode("AEIOU") == "cgkqw"
    # Mixed: "Hello" -> swapcase -> "hELLO" -> E->G, O->Q -> "hGLLQ"
    assert encode("Hello") == "hGLLQ"
    # Non-vowels pass through after swapcase:
    # "a1! e" -> swapcase -> "A1! E" -> A->C, E->G -> "C1! G"
    assert encode("a1! e") == "C1! G"
    # Empty string edge case
    assert encode("") == ""
