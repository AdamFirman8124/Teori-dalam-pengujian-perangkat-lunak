

# Generated at 2026-10-24 20:00:15.662852
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("BA") == 0       # A is at an odd index
    assert module_0.count_upper("ABECI") == 3    # A, E, and I are at even indices
    assert module_0.count_upper("ABCDEF") == 2   # A and E are at even indices
    assert module_0.count_upper("xyz") == 0

# Generated at 2026-10-24 20:00:23.511313
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("XAXEXI") == 0      # Vowels are at odd indices
    assert module_0.count_upper("AbEdIf") == 3      # A, E, I are at even indices
    assert module_0.count_upper("aeiou") == 0       # Lowercase vowels are not counted
    assert module_0.count_upper("BCDFG") == 0       # Uppercase consonants are not counted

# Generated at 2026-10-24 20:00:31.575548
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("ABECI") == 3   # A, E, and I are at even indices
    assert module_0.count_upper("BADE") == 0    # A and E are at odd indices
    assert module_0.count_upper("AEIOU") == 3   # A, I, and U are at even indices

# Generated at 2026-10-24 20:00:38.862269
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("aEiOu") == 0       # Lowercase vowels are not counted
    assert module_0.count_upper("ABCDEFGH") == 2    # A and E
    assert module_0.count_upper("BCDFG") == 0

# Generated at 2026-10-24 20:00:41.282788
# Unit test for function count_upper

# Generated at 2026-10-24 20:00:43.698285
# Unit test for function count_upper

# Generated at 2026-10-24 20:00:46.115220
# Unit test for function count_upper