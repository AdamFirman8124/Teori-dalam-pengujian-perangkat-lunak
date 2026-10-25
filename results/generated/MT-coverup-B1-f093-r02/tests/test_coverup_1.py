# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

def test_encode_replaces_vowels_and_swaps_case():
    from f093 import encode

    # "aeiou" -> swapcase -> "AEIOU" -> A->C, E->G, I->K, O->Q, U->W
    assert encode("aeiou") == "CGKQW"
    # "AEIOU" -> swapcase -> "aeiou" -> a->c, e->g, i->k, o->q, u->w
    assert encode("AEIOU") == "cgkqw"
    # "Hello" -> swapcase -> "hELLO" -> E->G, O->Q
    assert encode("Hello") == "hGLLQ"
    # Non-vowel letters are only case-swapped
    assert encode("xyz") == "XYZ"
    # Non-letter characters pass through unchanged
    assert encode("a1! e") == "C1! G"
    # Empty string edge case
    assert encode("") == ""
