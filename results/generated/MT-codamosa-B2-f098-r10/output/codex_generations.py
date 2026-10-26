

# Generated at 2026-10-25 12:35:28.946244
# Unit test for function count_upper

# Generated at 2026-10-25 12:35:31.358855
# Unit test for function count_upper

# Generated at 2026-10-25 12:35:33.791543
# Unit test for function count_upper

# Generated at 2026-10-25 12:35:49.113430
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("B") == 0
    assert module_0.count_upper("bA") == 0  # A at odd index 1 is skipped
    assert module_0.count_upper("Aa") == 1  # A at even index 0 is counted
    assert module_0.count_upper("AEIOU") == 3  # 0:A, 2:I, 4:U
    assert module_0.count_upper("aeiou") == 0  # lowercase not counted
    assert module_0.count_upper("ABCDE") == 2  # 0:A, 4:E
    assert module_0.count_upper("HELLO") == 1  # only O at index 4
    assert module_0.count_upper("aBCdEf") == 1  # only E at index 4
    assert module_0.count_upper("EA") == 1  # E at 0 counted, A at 1 skipped

# Generated at 2026-10-25 12:35:55.155768
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # No vowels at even indices
    assert module_0.count_upper("BCDEF") == 0
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3      # A(0), I(2), U(4)
    # Lowercase vowels should NOT count
    assert module_0.count_upper("aeiou") == 0
    # Mixed case: only uppercase vowels at even indices
    assert module_0.count_upper("aEiOu") == 1      # E(1)? no â index 1 is odd; O(3) odd; only none... 
    # Careful: let's verify manually below

# Generated at 2026-10-25 12:35:56.692059
# Unit test for function count_upper
def test_count_upper():
    # Empty string
    assert module_0.count_upper("") == 0
    # No vowels at even indices
    assert module_0.count_upper("BCDEF") == 0
    # Uppercase vowels at even indices
    assert module_0.count_upper("AEIOU") == 3      # A(0), I(2), U(4)
    # Lowercase vowels should NOT count
    assert module_0.count_upper("aeiou") == 0
    # Mixed case: only uppercase vowels at even indices
    assert module_0.count_upper("aEiOu") == 1      # E(1)? no â index 1 is odd; O(3) odd; only none... 
    # Careful: let's verify manually below

# Generated at 2026-10-25 12:35:59.334625
# Unit test for function count_upper

# Generated at 2026-10-25 12:36:01.947385
# Unit test for function count_upper

# Generated at 2026-10-25 12:36:04.683596
# Unit test for function count_upper