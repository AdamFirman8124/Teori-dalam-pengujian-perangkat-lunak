

# Generated at 2026-11-03 02:36:13.763917
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("Alone") == 3      # A, o, e
    assert module_0.vowels_count("bcdfg") == 0      # no vowels

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2        # e + y at end
    assert module_0.vowels_count("keY") == 2        # e + Y at end
    assert module_0.vowels_count("ACEDY") == 3      # A, E + Y at end

    # 'y'/'Y' elsewhere does not count
    assert module_0.vowels_count("bye") == 1        # only e
    assert module_0.vowels_count("yellow") == 2     # e, o
    assert module_0.vowels_count("yYy") == 1        # only trailing y counts

    # Mixed case vowels
    assert module_0.vowels_count("aEiOu") == 5
    assert module_0.vowels_count("XYZ") == 1        # trailing Z not y; X,Y,Z -> Y is not last? Y is middle, Z last -> 0? No: X,Y,Z -> last is Z, vowels: none... actually none of X,Y,Z in vowels, last is Z -> 0

# Generated at 2026-11-03 02:36:46.438660
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2  # a, e
    assert module_0.vowels_count("Alone") == 3  # a, o, e
    assert module_0.vowels_count("hello") == 2  # e, o
    assert module_0.vowels_count("bcdfg") == 0  # no vowels

    # Uppercase vowels
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # Words ending in 'y' get +1
    assert module_0.vowels_count("acy") == 2    # a + y ending
    assert module_0.vowels_count("ACEDY") == 4  # A, E + Y ending
    assert module_0.vowels_count("xyz") == 1    # y ending only
    assert module_0.vowels_count("y") == 1      # single 'y'
    assert module_0.vowels_count("Y") == 1      # single 'Y'

    # 'y' not at the end doesn't count
    assert module_0.vowels_count("yes") == 1    # only e
    assert module_0.vowels_count("yellow") == 2 # e, o
    assert module_0.vowels_count("aeiouy") == 6 # 5 vowels + ending y

    # No y at end, mixed case
    assert module_0.vowels_count("Python") == 1 # o
    assert module_0.vowels_count("TEST") == 1   # E

    print("All tests passed!")


test_vowels_count()

# Generated at 2026-11-03 02:37:40.753250
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("Alone") == 3
    assert module_0.vowels_count("hello world") == 3

    # All vowels, both cases
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("aEiOu") == 5

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("xyz") == 0

    # 'y'/'Y' at the end counts as a vowel
    assert module_0.vowels_count("key") == 2
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("PY") == 1

    # 'y'/'Y' not at the end does not count
    assert module_0.vowels_count("byte") == 1
    assert module_0.vowels_count("yellow") == 2

    # Mixed content
    assert module_0.vowels_count("Python3") == 1
    assert module_0.vowels_count("!") == 0

# Generated at 2026-11-03 02:38:33.412332
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2, "Expected 2 vowels in 'abcde'"
    assert module_0.vowels_count("hello") == 2, "Expected 2 vowels in 'hello'"
    assert module_0.vowels_count("AEIOU") == 5, "Expected 5 vowels in 'AEIOU'"
    assert module_0.vowels_count("aeiou") == 5, "Expected 5 vowels in 'aeiou'"
    
    # No vowels
    assert module_0.vowels_count("bcdfg") == 0, "Expected 0 vowels in 'bcdfg'"
    assert module_0.vowels_count("rhythm") == 0, "Expected 0 vowels in 'rhythm'"
    
    # 'y' at the end counts as a vowel
    assert module_0.vowels_count("xyz") == 1, "Expected 1 in 'xyz' (y at end)"
    assert module_0.vowels_count("XYZ") == 1, "Expected 1 in 'XYZ' (Y at end)"
    assert module_0.vowels_count("ACEDY") == 3, "Expected 3 in 'ACEDY' (A, E, Y)"
    assert module_0.vowels_count("happy") == 2, "Expected 2 in 'happy' (a, y)"
    assert module_0.vowels_count("y") == 1, "Expected 1 in 'y'"
    assert module_0.vowels_count("Y") == 1, "Expected 1 in 'Y'"
    
    # 'y' not at the end should not count
    assert module_0.vowels_count("yar") == 0, "Expected 0 in 'yar' (y at start)"
    assert module_0.vowels_count("bystander") == 2, "Expected 2 in 'bystander' (a, e)"
    
    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdOfU") == 5, "Expected 5 vowels in 'AbEcIdOfU'"
    
    # Vowels with punctuation/numbers
    assert module_0.vowels_count("a1e2i3") == 3, "Expected 3 vowels in 'a1e2i3'"
    assert module_0.vowels_count("Easy!") == 2, "Expected 2 in 'Easy!' (E, a)"
    
    # Repeated vowels
    assert module_0.vowels_count("aaa") == 3, "Expected 3 vowels in 'aaa'"
    assert module_0.vowels_count("eeyy") == 3, "Expected 3 in 'eeyy' (e, e, y)"
    
    print("All tests passed!")

test_vowels_count()

# Generated at 2026-11-03 02:39:04.913549
# Unit test for function vowels_count
def test_vowels_count():
    # Basic vowel counting
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("Alone") == 3      # A, o, e
    assert module_0.vowels_count("AEIOU") == 5      # all uppercase vowels
    assert module_0.vowels_count("aeiou") == 5      # all lowercase vowels
    
    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("xyz") == 0        # y not at end doesn't count
    
    # 'y' at end adds one
    assert module_0.vowels_count("key") == 2        # e + trailing y
    assert module_0.vowels_count("y") == 1          # single trailing y
    assert module_0.vowels_count("Y") == 1          # single trailing uppercase Y
    assert module_0.vowels_count("ACEDY") == 3      # A, E + trailing Y
    assert module_0.vowels_count("aeiouy") == 6     # 5 vowels + trailing y
    
    # 'y' not at end does not add
    assert module_0.vowels_count("yellow") == 2     # e, o (y is not at end)
    assert module_0.vowels_count("syzygy") == 0     # no vowels, y not at very end
    
    # Mixed case and repeated vowels
    assert module_0.vowels_count("bYbYe") == 2      # Y (not at end), e
    assert module_0.vowels_count("aEiOuY") == 6     # 5 vowels + trailing Y
    
    # Empty string raises IndexError (s[-1] on empty string)
    try:
        module_0.vowels_count("")
        assert False, "Expected IndexError for empty string"
    except IndexError:
        pass