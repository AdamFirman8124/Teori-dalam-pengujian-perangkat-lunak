# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

def test_encode_replaces_vowels_and_swaps_case():
    from f093 import encode

    assert encode("aeiou") == "CGKQW"
    assert encode("AEIOU") == "cgkqw"
    assert encode("Hello") == "hGLLQ"
    assert encode("a1! e") == "C1! G"
    assert encode("XYZ xyz") == "xyz XYZ"
    assert encode("") == ""
