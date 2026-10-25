

# Generated at 2026-10-24 14:11:52.806957
# Unit test for function encode
def test_encode():assert module_0.encode("hello") == "HGLLQ"

# Generated at 2026-10-24 14:12:03.462927
# Unit test for function encode
def test_encode():
    # swapcase runs BEFORE vowel replacement â the trap in this function
    assert module_0.encode("hello") == "HGLLQ"      # HELLO -> E->G, O->Q
    assert module_0.encode("aeiou") == "CGKQW"      # swapcase -> AEIOU, then +2 each
    assert module_0.encode("AEIOU") == "cgkqw"      # swapcase -> aeiou, then +2 each
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    assert module_0.encode("xyz") == "XYZ"          # no vowels: case swap only
    assert module_0.encode("") == ""
    assert module_0.encode("123!@#") == "123!@#"

# Generated at 2026-10-24 14:12:04.847491
# Unit test for function encode
def test_encode():
    # swapcase runs BEFORE vowel replacement â the trap in this function
    assert module_0.encode("hello") == "HGLLQ"      # HELLO -> E->G, O->Q
    assert module_0.encode("aeiou") == "CGKQW"      # swapcase -> AEIOU, then +2 each
    assert module_0.encode("AEIOU") == "cgkqw"      # swapcase -> aeiou, then +2 each
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    assert module_0.encode("xyz") == "XYZ"          # no vowels: case swap only
    assert module_0.encode("") == ""
    assert module_0.encode("123!@#") == "123!@#"

# Generated at 2026-10-24 14:12:06.483674
# Unit test for function encode
def test_encode():
    # swapcase runs BEFORE vowel replacement â the trap in this function
    assert module_0.encode("hello") == "HGLLQ"      # HELLO -> E->G, O->Q
    assert module_0.encode("aeiou") == "CGKQW"      # swapcase -> AEIOU, then +2 each
    assert module_0.encode("AEIOU") == "cgkqw"      # swapcase -> aeiou, then +2 each
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    assert module_0.encode("xyz") == "XYZ"          # no vowels: case swap only
    assert module_0.encode("") == ""
    assert module_0.encode("123!@#") == "123!@#"

# Generated at 2026-10-24 14:12:07.875120
# Unit test for function encode
def test_encode():
    # swapcase runs BEFORE vowel replacement â the trap in this function
    assert module_0.encode("hello") == "HGLLQ"      # HELLO -> E->G, O->Q
    assert module_0.encode("aeiou") == "CGKQW"      # swapcase -> AEIOU, then +2 each
    assert module_0.encode("AEIOU") == "cgkqw"      # swapcase -> aeiou, then +2 each
    assert module_0.encode("Hello World") == "hGLLQ wQRLD"
    assert module_0.encode("xyz") == "XYZ"          # no vowels: case swap only
    assert module_0.encode("") == ""
    assert module_0.encode("123!@#") == "123!@#"