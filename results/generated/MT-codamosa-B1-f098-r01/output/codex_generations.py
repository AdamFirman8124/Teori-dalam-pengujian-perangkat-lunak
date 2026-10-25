

# Generated at 2026-10-24 23:41:39.416707
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("ABCDE") == 2       # A and E
    assert module_0.count_upper("aEiOu") == 0       # Only uppercase vowels count
    assert module_0.count_upper("XAXEXI") == 0      # Vowels are at odd indices
    assert module_0.count_upper("AXEXIX") == 3      # A, E, I are at even indices

# Generated at 2026-10-24 23:41:45.155641
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("AbEcdO") == 2      # A and E
    assert module_0.count_upper("aEiOu") == 2       # E and O
    assert module_0.count_upper("BCDFG") == 0
    assert module_0.count_upper("xAxExI") == 0      # Uppercase vowels are at odd indices

# Generated at 2026-10-24 23:41:51.190604
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("ABCDE") == 2  # A and E are at even indices
    assert module_0.count_upper("AEIOU") == 3  # A, I, and U are at even indices
    assert module_0.count_upper("bAbEbI") == 0  # Uppercase vowels are at odd indices

# Generated at 2026-10-24 23:41:56.749537
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AbEcIdO") == 4       # Uppercase vowels at even indices
    assert module_0.count_upper("xAxExI") == 0        # Uppercase vowels only at odd indices
    assert module_0.count_upper("abcdef") == 0        # Lowercase vowels are not counted
    assert module_0.count_upper("AXBECID") == 3

# Generated at 2026-10-24 23:42:03.913445
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("AbEcIdOfU") == 5  # Uppercase vowels at even indices
    assert module_0.count_upper("aBeCiDoFu") == 0
    assert module_0.count_upper("BA") == 0         # 'A' is at an odd index
    assert module_0.count_upper("XYZ") == 0