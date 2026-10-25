

# Generated at 2026-10-25 02:08:27.948077
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("AbEcIdOfU") == 5   # All vowels are at even indices
    assert module_0.count_upper("xAxExI") == 0      # Uppercase vowels are at odd indices
    assert module_0.count_upper("aeiou") == 0       # Lowercase vowels are not counted

# Generated at 2026-10-25 02:08:37.155499
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("AbEcI") == 3       # A, E, I are at even indices
    assert module_0.count_upper("aBeDi") == 0       # No uppercase vowels at even indices
    assert module_0.count_upper("xAxEx") == 0       # Uppercase vowels are at odd indices

# Generated at 2026-10-25 02:08:42.854216
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AbEcIdOfU") == 5  # Uppercase vowels at even indices
    assert module_0.count_upper("xAxExIxOxU") == 0  # Uppercase vowels at odd indices
    assert module_0.count_upper("abcdefgh") == 0
    assert module_0.count_upper("ABCDEF") == 2  # A at index 0 and E at index 4

# Generated at 2026-10-25 02:08:46.888277
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("ABCDEF") == 2  # A and E at even indices
    assert module_0.count_upper("aEiOu") == 0   # lowercase vowels are not counted
    assert module_0.count_upper("BAEIOU") == 2  # E and O at even indices
    assert module_0.count_upper("AEIOU") == 3   # A, I, and U at even indices

# Generated at 2026-10-25 02:08:52.069460
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("B") == 0
    assert module_0.count_upper("AbEcIdOfU") == 5
    assert module_0.count_upper("bAcEiOu") == 0  # Uppercase vowels are at odd indices
    assert module_0.count_upper("AXEIOU") == 2  # A and E occur at even indices