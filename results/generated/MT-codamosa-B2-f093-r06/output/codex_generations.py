

# Generated at 2026-11-02 21:30:55.485915
# Unit test for function encode
def test_encode():
    # nonce:49cc571c
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert module_0.encode('') == ''
    assert module_0.encode('a') == 'C'
    assert module_0.encode('A') == 'c'
    assert module_0.encode('hello world') == 'HGLLQ WQRLD'
    assert module_0.encode('12345') == '12345'
    assert module_0.encode('Python') == 'pYTHQN'
    assert module_0.encode('AEIOU') == 'cgkqw'
    assert module_0.encode('aeiou') == 'CGKQW'
    assert module_0.encode('Hey!') == 'hGY!'

# Generated at 2026-11-02 21:33:29.900696
# Unit test for function encode
def test_encode():
    # nonce:ddc0103a
    # Canonical cases: swapcase applied first, then vowels shifted by 2 (preserving swapped case)
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'

    # Mixed case handling
    assert module_0.encode('hello') == 'HGllQ'
    assert module_0.encode('HELLO') == 'hgllq'
    assert module_0.encode('HeLLo WoRLD') == 'hGllq wQrld'

    # Vowel-only inputs
    assert module_0.encode('aeiou') == 'CGKQW'
    assert module_0.encode('AEIOU') == 'cjkqw'

    # No vowels: only case is swapped
    assert module_0.encode('xyz XYZ') == 'XYZ xyz'
    assert module_0.encode('Rhythm!') == 'rHYTHM!'

    # Empty string
    assert module_0.encode('') == ''

    # Digits and punctuation pass through untouched
    assert module_0.encode('Python 3.9!') == 'pYTHQN 3.9!'
    assert module_0.encode('abc123') == 'CBC123'

    # Single characters
    assert module_0.encode('a') == 'C'
    assert module_0.encode('A') == 'c'
    assert module_0.encode('b') == 'B'

# Generated at 2026-11-02 21:36:10.698793
# Unit test for function encode
def test_encode():
    # Docstring examples
    assert module_0.encode('test') == 'TGST'
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'

    # Edge cases
    assert module_0.encode('') == ''

    # Case swapping with vowel replacement
    assert module_0.encode('hello') == 'HGLLQ'
    assert module_0.encode('HELLO') == 'hGLLQ'

    # All vowels, both cases
    assert module_0.encode('aeiouAEIOU') == 'CGKQWcgkqw'

    # No vowels
    assert module_0.encode('xyz') == 'XYZ'
    assert module_0.encode('1234!@#$') == '1234!@#$'

    # Mixed alphanumerics and punctuation
    assert module_0.encode('Python 3.9') == 'pYTHQN 3.9'

    # Alternating case
    assert module_0.encode('AbCdEfG') == 'cBcDgFg'

# Generated at 2026-11-02 21:39:26.631727
# Unit test for function encode
def test_encode():
    # Lowercase input: swapcase -> uppercase, vowels shifted by 2
    assert module_0.encode('test') == 'TGST'
    # Mixed case input
    assert module_0.encode('This is a message') == 'tHKS KS C MGSSCGG'
    # Uppercase input: swapcase -> lowercase, vowels shifted by 2
    assert module_0.encode('HELLO') == 'hgllq'
    # All lowercase vowels map to letters two positions ahead
    assert module_0.encode('aeiou') == 'CGKQW'
    # All uppercase vowels, after swapcase, map to lowercase shifted vowels
    assert module_0.encode('AEIOU') == 'cgkqw'
    # No vowels: only the case is swapped
    assert module_0.encode('xyz XYZ') == 'XYZ xyz'
    # Empty string remains empty
    assert module_0.encode('') == ''
    # Digits and punctuation are unaffected apart from case rules
    assert module_0.encode('a1b2!') == 'C1B2!'