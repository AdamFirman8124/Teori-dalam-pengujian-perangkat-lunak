

# Generated at 2026-10-25 03:50:30.333672
# Unit test for function count_upper
def test_count_upper():assert module_0.count_upper("") == 0

# Generated at 2026-10-25 03:50:36.877467
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("AXEXIXOXU") == 5
    assert module_0.count_upper("aAeEiI") == 0  # Uppercase vowels are at odd indices
    assert module_0.count_upper("ABECID") == 3

# Generated at 2026-10-25 03:50:42.954443
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("aAeEiIoOuU") == 0  # Uppercase vowels are at odd indices
    assert module_0.count_upper("ABECIDOFU") == 5

# Generated at 2026-10-25 03:50:51.114046
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3       # A, I, U are at even indices
    assert module_0.count_upper("ABECIDOFU") == 5   # All vowels are at even indices
    assert module_0.count_upper("xAxExI") == 0      # Vowels are at odd indices
    assert module_0.count_upper("ABCDEF") == 1      # Only A qualifies

# Generated at 2026-10-25 03:50:56.846097
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("aA") == 0       # Uppercase vowel at an odd index
    assert module_0.count_upper("AEIOU") == 3   # A, I, and U are at even indices
    assert module_0.count_upper("abcdef") == 0
    assert module_0.count_upper("AxExI") == 3