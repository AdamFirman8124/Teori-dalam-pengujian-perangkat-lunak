

# Generated at 2026-11-01 21:13:05.793302
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode('') == ''

    # Vowels: swapcase first, then replaced by character two ASCII positions ahead
    assert module_0.encode('a') == 'C'    # 'a' -> 'A' -> 'C'
    assert module_0.encode('A') == 'c'    # 'A' -> 'a' -> 'c'
    assert module_0.encode('e') == 'G'
    assert module_0.encode('E') == 'g'
    assert module_0.encode('i') == 'K'
    assert module_0.encode('I') == 'k'
    assert module_0.encode('o') == 'Q'
    assert module_0.encode('O') == 'q'
    assert module_0.encode('u') == 'W'
    assert module_0.encode('U') == 'w'

    # Non-vowel letters only swap case
    assert module_0.encode('b') == 'B'
    assert module_0.encode('B') == 'b'
    assert module_0.encode('xyz') == 'XYZ'
    assert module_0.encode('XYZ') == 'xyz'

    # Mixed-case words
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('hello') == 'HGLLQ'
    assert module_0.encode('PYTHON') == 'pythqn'
    assert module_0.encode('Mudasir') == 'mWDCSKR'
    assert module_0.encode('YES') == 'ygs'
    assert module_0.encode('GOING') == 'gqkng'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'

    # Digits, punctuation and whitespace are unchanged
    assert module_0.encode('123!@# ') == '123!@# '

    # Repeated vowels of mixed case
    assert module_0.encode('aaAA') == 'CCcc'

    print("All tests passed!")


test_encode()

# Generated at 2026-11-01 21:14:21.058628
# Unit test for function encode
def test_encode():
    # nonce:1cf1a5ef
    # Empty string
    assert module_0.encode('') == ''

    # Basic examples: swapcase + vowels shifted 2 letters ahead
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCG'

    # Single letters: case swap and vowel replacement
    assert module_0.encode('a') == 'C'
    assert module_0.encode('A') == 'c'
    assert module_0.encode('b') == 'B'
    assert module_0.encode('B') == 'b'

    # All vowels, lowercase and uppercase
    assert module_0.encode('aeiou') == 'CGKQW'
    assert module_0.encode('AEIOU') == 'cgkqw'

    # Mixed letters, digits and punctuation
    assert module_0.encode('hello world') == 'HGLLQ WQRLD'
    assert module_0.encode('PYTHON 123') == 'pythqn 123'
    assert module_0.encode('Hello, World! 123') == 'hGLLQ, wQRLD! 123'

# Generated at 2026-11-01 21:15:04.472902
# Unit test for function encode
def test_encode():
    # Empty string
    assert module_0.encode("") == ""

    # Lowercase input: swapcase makes vowels uppercase, then shifted +2
    assert module_0.encode("hello") == "HGLLQ"

    # Uppercase input: swapcase makes vowels lowercase, then shifted +2
    assert module_0.encode("HELLO") == "hgllq"

    # All lowercase vowels -> uppercase shifted vowels
    assert module_0.encode("aeiou") == "CGKQW"

    # All uppercase vowels -> lowercase shifted vowels
    assert module_0.encode("AEIOU") == "cgkqw"

    # Mixed case with spaces
    assert module_0.encode("I Do It") == "k dQ kT"

    # No vowels: only case is swapped
    assert module_0.encode("xyz") == "XYZ"
    assert module_0.encode("BCDFG") == "bcdfg"

    # 'y' is not treated as a vowel
    assert module_0.encode("why") == "WHY"

    # Digits and punctuation are unaffected
    assert module_0.encode("Testing 123!") == "tGSTKNG 123!"

    # Multi-word sentence
    assert module_0.encode("Python Programming") == "pYTHQN pRQGRcMMKNG"

    # Mirrored case string maps symmetrically
    assert module_0.encode("aA") == "Cc"


test_encode()

# Generated at 2026-11-01 21:15:57.111352
# Unit test for function encode
def test_encode():
    # nonce:50d266aa
    # Basic example: swapcase then vowel shift (+2 in ASCII after swap)
    assert module_0.encode("test") == "TGST"
    assert module_0.encode("This is a message") == "tHKS KS C MGSSCG"

    # Empty string
    assert module_0.encode("") == ""

    # Vowels only: lowercase becomes uppercase then shifted
    assert module_0.encode("aeiou") == "CGKQW"
    # Uppercase vowels become lowercase then shifted
    assert module_0.encode("AEIOU") == "cgkqw"

    # Consonants only: just swapcased
    assert module_0.encode("bcdfg") == "BCDFG"
    assert module_0.encode("HELLO") == "hGllQ"

    # Single characters
    assert module_0.encode("a") == "C"
    assert module_0.encode("A") == "c"
    assert module_0.encode("z") == "Z"

    # Mixed letters and digits / punctuation preserved
    assert module_0.encode("Python 3.9") == "pYtHQn 3.9"
    assert module_0.encode("12345!@#$%") == "12345!@#$%"
    assert module_0.encode("Hi, Bob!") == "hK, bQB!"

    # 'y' and 'w' are not treated as vowels here
    assert module_0.encode("why") == "WHY"

    print("All tests passed!")

# Generated at 2026-11-01 21:16:45.510490
# Unit test for function encode
def test_encode():
    # Basic case: swapcase + vowel replacement
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('Test') == 'tGST'

    # Mixed case message with vowels and consonants
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'

    # All lowercase vowels
    assert module_0.encode('aeiou') == 'CGKQW'

    # All uppercase vowels
    assert module_0.encode('AEIOU') == 'cgkqw'

    # No vowels at all, just case swap
    assert module_0.encode('bcdfg') == 'BCDFG'
    assert module_0.encode('BCDFG') == 'bcdfg'

    # Empty string
    assert module_0.encode('') == ''

    # Non-alphabetic characters are unchanged
    assert module_0.encode('123!@#') == '123!@#'
    assert module_0.encode('a1b2') == 'C1B2'

    # Single characters
    assert module_0.encode('a') == 'C'
    assert module_0.encode('A') == 'c'
    assert module_0.encode('z') == 'Z'

    # Vowels at boundaries of a word
    assert module_0.encode('apple') == 'CPPLG'