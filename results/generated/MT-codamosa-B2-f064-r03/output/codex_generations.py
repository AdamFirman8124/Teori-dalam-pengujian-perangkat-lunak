

# Generated at 2026-10-24 19:44:45.312982
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("happy") == 2       # 'a' and final 'y'
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("rhythm") == 0      # non-final 'y' is not counted
    assert module_0.vowels_count("xyz") == 0
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 19:44:52.011119
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("yellow") == 2  # Non-final y is not counted
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 19:44:58.726228
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("happy") == 2       # 'a' and final 'y'
    assert module_0.vowels_count("rhythm") == 0      # non-final 'y' is not counted
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 19:45:05.075832
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("happy") == 2  # 'a' and final 'y'
    assert module_0.vowels_count("yellow") == 2  # non-final 'y' is not counted
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 19:45:11.935460
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("HELLO") == 2
    assert module_0.vowels_count("happy") == 2       # 'a' and final 'y'
    assert module_0.vowels_count("yellow") == 2      # 'e' and 'o'; non-final 'y' excluded
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("") == 0