

# Generated at 2026-10-24 14:57:19.819429
# Unit test for function prime_length
def test_prime_length():
    # length 0 and 1 -> not prime
    assert module_0.prime_length("") == False
    assert module_0.prime_length("a") == False

    # prime lengths -> True
    assert module_0.prime_length("ab") == True          # 2
    assert module_0.prime_length("abc") == True         # 3
    assert module_0.prime_length("abcde") == True       # 5
    assert module_0.prime_length("abcdefg") == True     # 7
    assert module_0.prime_length("abcdefghijk") == True # 11

    # non-prime lengths -> False
    assert module_0.prime_length("abcd") == False       # 4
    assert module_0.prime_length("abcdef") == False     # 6
    assert module_0.prime_length("abcdefgh") == False   # 8
    assert module_0.prime_length("abcdefghi") == False  # 9
    assert module_0.prime_length("abcdefghij") == False  # 10

# Generated at 2026-10-24 14:57:21.370614
# Unit test for function prime_length
def test_prime_length():
    # length 0 and 1 -> not prime
    assert module_0.prime_length("") == False
    assert module_0.prime_length("a") == False

    # prime lengths -> True
    assert module_0.prime_length("ab") == True          # 2
    assert module_0.prime_length("abc") == True         # 3
    assert module_0.prime_length("abcde") == True       # 5
    assert module_0.prime_length("abcdefg") == True     # 7
    assert module_0.prime_length("abcdefghijk") == True # 11

    # non-prime lengths -> False
    assert module_0.prime_length("abcd") == False       # 4
    assert module_0.prime_length("abcdef") == False     # 6
    assert module_0.prime_length("abcdefgh") == False   # 8
    assert module_0.prime_length("abcdefghi") == False  # 9
    assert module_0.prime_length("abcdefghij") == False  # 10

# Generated at 2026-10-24 14:57:22.741762
# Unit test for function prime_length
def test_prime_length():
    # length 0 and 1 -> not prime
    assert module_0.prime_length("") == False
    assert module_0.prime_length("a") == False

    # prime lengths -> True
    assert module_0.prime_length("ab") == True          # 2
    assert module_0.prime_length("abc") == True         # 3
    assert module_0.prime_length("abcde") == True       # 5
    assert module_0.prime_length("abcdefg") == True     # 7
    assert module_0.prime_length("abcdefghijk") == True # 11

    # non-prime lengths -> False
    assert module_0.prime_length("abcd") == False       # 4
    assert module_0.prime_length("abcdef") == False     # 6
    assert module_0.prime_length("abcdefgh") == False   # 8
    assert module_0.prime_length("abcdefghi") == False  # 9
    assert module_0.prime_length("abcdefghij") == False  # 10

# Generated at 2026-10-24 14:57:24.085138
# Unit test for function prime_length
def test_prime_length():
    # length 0 and 1 -> not prime
    assert module_0.prime_length("") == False
    assert module_0.prime_length("a") == False

    # prime lengths -> True
    assert module_0.prime_length("ab") == True          # 2
    assert module_0.prime_length("abc") == True         # 3
    assert module_0.prime_length("abcde") == True       # 5
    assert module_0.prime_length("abcdefg") == True     # 7
    assert module_0.prime_length("abcdefghijk") == True # 11

    # non-prime lengths -> False
    assert module_0.prime_length("abcd") == False       # 4
    assert module_0.prime_length("abcdef") == False     # 6
    assert module_0.prime_length("abcdefgh") == False   # 8
    assert module_0.prime_length("abcdefghi") == False  # 9
    assert module_0.prime_length("abcdefghij") == False  # 10

# Generated at 2026-10-24 14:57:25.580088
# Unit test for function prime_length
def test_prime_length():
    # length 0 and 1 -> not prime
    assert module_0.prime_length("") == False
    assert module_0.prime_length("a") == False

    # prime lengths -> True
    assert module_0.prime_length("ab") == True          # 2
    assert module_0.prime_length("abc") == True         # 3
    assert module_0.prime_length("abcde") == True       # 5
    assert module_0.prime_length("abcdefg") == True     # 7
    assert module_0.prime_length("abcdefghijk") == True # 11

    # non-prime lengths -> False
    assert module_0.prime_length("abcd") == False       # 4
    assert module_0.prime_length("abcdef") == False     # 6
    assert module_0.prime_length("abcdefgh") == False   # 8
    assert module_0.prime_length("abcdefghi") == False  # 9
    assert module_0.prime_length("abcdefghij") == False  # 10