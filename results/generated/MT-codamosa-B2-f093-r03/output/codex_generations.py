

# Generated at 2026-11-02 20:44:08.982653
# Unit test for function encode
def test_encode():
    # Standard cases with mixed case and vowels
    assert module_0.encode('TEST') == 'tgst'
    assert module_0.encode('Mudasir') == 'mWDCSKR'
    assert module_0.encode('YES') == 'ygs'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert module_0.encode('I DoNt KnOw WhAt tO WrItE') == 'k dQnT kNqW wHcT Tq wRkTg'

    # Edge cases
    assert module_0.encode('') == ''                       # empty string
    assert module_0.encode('aeiouAEIOU') == 'CEGKQWcegkqw'  # all vowels, both cases
    assert module_0.encode('123!@#') == '123!@#'            # no letters, unchanged
    assert module_0.encode('xyzXYZ') == 'XYZxyz'            # no vowels, only swapcase
    assert module_0.encode('a') == 'C'                      # single lowercase vowel
    assert module_0.encode('A') == 'c'                      # single uppercase vowel
    assert module_0.encode('bcdfg') == 'BCDFG'              # consonants only

# Generated at 2026-11-02 20:46:39.518033
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Uppercase input gets swapped to lowercase, vowels shifted +2
    assert module_0.encode("TEST") == "tgst"
    assert module_0.encode("YES") == "ygs"

    # Mixed case with vowels in both cases
    assert module_0.encode("Mudasir") == "mWDCSKR"
    assert module_0.encode("Goings") == "gQKNGS"

    # No vowels at all, only case swap
    assert module_0.encode("BCD") == "bcd"
    assert module_0.encode("bcD") == "BCd"

    # All vowels
    assert module_0.encode("aeiou") == "cgkwY"[0:0] + "CGKWY".lower()  # -> 'cgkwy'
    assert module_0.encode("AEIOU") == "cgkwy"

    # Vowels remain vowels after swapcase, shifted by 2 in ASCII
    assert module_0.encode("hello") == "GLLQ"  # swapcase -> HELLO -> H,G,L,L,Q
    assert module_0.encode("Python") == "pYTHQn"  # swapcase -> pYTHON -> p,Y,TH,Q,n

    # Digits and punctuation unaffected except case swap
    assert module_0.encode("a1b2") == "C1B2"

    # Repeated characters
    assert module_0.encode("aaa") == "CCC"
    assert module_0.encode("AAA") == "ccc"

# Generated at 2026-11-02 20:48:16.357161
# Unit test for function encode
def test_encode():
    # Canonical examples
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'

    # Empty string
    assert module_0.encode('') == ''

    # Lowercase vowels get swapped to uppercase then shifted
    assert module_0.encode('aeiou') == 'CGKQW'

    # Uppercase vowels get swapped to lowercase then shifted
    assert module_0.encode('AEIOU') == 'cgkqw'

    # Mixed case consonants only
    assert module_0.encode('xyz') == 'XYZ'
    assert module_0.encode('aBcD') == 'CbCd'

    # Digits and punctuation unaffected
    assert module_0.encode('1234!@#') == '1234!@#'

    # Mixed letters, digits, spaces
    assert module_0.encode('hello world 123') == 'HGLLQ WQRLD 123'

    # Single vowel
    assert module_0.encode('a') == 'C'
    assert module_0.encode('A') == 'c'

    # Non-vowel letters swap case only
    assert module_0.encode('Python') == 'pYTHQn'

# Generated at 2026-11-02 20:49:53.215223
# Unit test for function encode
def test_encode():
    # Vowels shifted by 2, case swapped
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert module_0.encode('hello') == 'HGLLQ'
    assert module_0.encode('HELLO') == 'hgllq'
    assert module_0.encode('aeiou') == 'CGKQW'
    assert module_0.encode('AEIOU') == 'cgkqw'
    # Non-alphabetic characters unaffected
    assert module_0.encode('123!@#') == '123!@#'
    # No vowels: only case swap
    assert module_0.encode('xyz') == 'XYZ'
    assert module_0.encode('XYZ') == 'xyz'
    # Empty string
    assert module_0.encode('') == ''
    # Mixed content
    assert module_0.encode('Python3.6') == 'pYTHQN3.6'
    print("test_encode passed!")

test_encode()

# Generated at 2026-11-02 20:51:49.809370
# Unit test for function encode
def test_encode():
    # nonce:f2f124f8
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert module_0.encode('') == ''
    assert module_0.encode('hello') == 'HGLLQ'
    assert module_0.encode('AEIOU') == 'cgkqw'
    assert module_0.encode('aeiou') == 'CGKQW'
    assert module_0.encode('Python') == 'pYTHQN'
    assert module_0.encode('AbC') == 'cBc'
    assert module_0.encode('123!@#') == '123!@#'