

# Generated at 2026-10-24 14:41:25.262669
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("AB") == 1  # only index 0 checked
    assert module_0.count_upper("aA") == 0  # odd index is ignored
    assert module_0.count_upper("AEIOU") == 3  # indices 0,2,4 -> A,I,U
    assert module_0.count_upper("ABCDE") == 2  # indices 0,2,4 -> A,E
    assert module_0.count_upper("HELLO") == 1  # indices 0,2,4 -> H,L,O
    assert module_0.count_upper("BCDFG") == 0
    assert module_0.count_upper("aEiOu") == 0  # lowercase vowels don't count

# Generated at 2026-10-24 14:41:41.845665
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("AB") == 1  # only index 0 checked
    assert module_0.count_upper("aA") == 0  # odd index is ignored
    assert module_0.count_upper("AEIOU") == 3  # indices 0,2,4 -> A,I,U
    assert module_0.count_upper("ABCDE") == 2  # indices 0,2,4 -> A,E
    assert module_0.count_upper("HELLO") == 1  # indices 0,2,4 -> H,L,O
    assert module_0.count_upper("BCDFG") == 0
    assert module_0.count_upper("aEiOu") == 0  # lowercase vowels don't count

# Generated at 2026-10-24 14:41:43.253348
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("A") == 1
    assert module_0.count_upper("a") == 0
    assert module_0.count_upper("AB") == 1  # only index 0 checked
    assert module_0.count_upper("aA") == 0  # odd index is ignored
    assert module_0.count_upper("AEIOU") == 3  # indices 0,2,4 -> A,I,U
    assert module_0.count_upper("ABCDE") == 2  # indices 0,2,4 -> A,E
    assert module_0.count_upper("HELLO") == 1  # indices 0,2,4 -> H,L,O
    assert module_0.count_upper("BCDFG") == 0
    assert module_0.count_upper("aEiOu") == 0  # lowercase vowels don't count

# Generated at 2026-10-24 14:41:50.653065
# Unit test for function count_upper
def test_count_upper():
    # Even-index vowels (indices 0, 2, 4) get counted
    assert module_0.count_upper("AEIOU") == 2      # A (0), E (2)
    assert module_0.count_upper("aBCdEf") == 1     # E (4)
    assert module_0.count_upper("abcdefg") == 0    # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0       # E at index 3 (odd) doesn't count
    assert module_0.count_upper("") == 0           # empty string
    assert module_0.count_upper("A") == 1          # single vowel at index 0
    assert module_0.count_upper("B") == 0          # single consonant
    assert module_0.count_upper("AAAEIOU") == 3    # A(0), A(2), E(4)
    print("All tests passed!")

test_count_upper()

# Generated at 2026-10-24 14:41:52.290372
# Unit test for function count_upper
def test_count_upper():
    # Even-index vowels (indices 0, 2, 4) get counted
    assert module_0.count_upper("AEIOU") == 2      # A (0), E (2)
    assert module_0.count_upper("aBCdEf") == 1     # E (4)
    assert module_0.count_upper("abcdefg") == 0    # no uppercase vowels
    assert module_0.count_upper("dBBE") == 0       # E at index 3 (odd) doesn't count
    assert module_0.count_upper("") == 0           # empty string
    assert module_0.count_upper("A") == 1          # single vowel at index 0
    assert module_0.count_upper("B") == 0          # single consonant
    assert module_0.count_upper("AAAEIOU") == 3    # A(0), A(2), E(4)
    print("All tests passed!")

test_count_upper()