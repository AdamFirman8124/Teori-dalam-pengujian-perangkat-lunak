

# Generated at 2026-10-25 03:13:45.728518
# Unit test for function hex_key

# Generated at 2026-10-25 03:13:48.143317
# Unit test for function hex_key

# Generated at 2026-10-25 03:13:50.558283
# Unit test for function hex_key

# Generated at 2026-10-25 03:14:04.278466
# Unit test for function hex_key
def test_hex_key():
    assert module_0.hex_key("AB") == 1
    assert module_0.hex_key("1077E") == 2
    assert module_0.hex_key("ABED1A33") == 4
    assert module_0.hex_key("123456789ABCDEF0") == 6
    assert module_0.hex_key("2020") == 2
    assert module_0.hex_key("") == 0
    assert module_0.hex_key("000000") == 0
    assert module_0.hex_key("2357BD") == 6
    assert module_0.hex_key("04689ACEF") == 0

# Generated at 2026-10-25 03:14:05.615826
# Unit test for function hex_key
def test_hex_key():
    # Single prime digits
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("D") == 1

    # Single non-prime digits
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("F") == 0

    # Known examples
    assert module_0.hex_key("AB") == 1                # only B is prime
    assert module_0.hex_key("1077E") == 2             # 7 and 7
    assert module_0.hex_key("AED1F") == 2             # E? no; D counts, E no -> D only... 
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2,3,5,7,B,D
    assert module_0.hex_key("2020") == 2              # two 2s

    # Edge cases
    assert module_0.hex_key("") == 0                  # empty string
    assert module_0.hex_key("BBBB") == 4              # all primes
    assert module_0.hex_key("0011") == 0              # no primes

    print("All tests passed!")

test_hex_key()

# Generated at 2026-10-25 03:14:07.042936
# Unit test for function hex_key
def test_hex_key():
    # Single prime digits
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("D") == 1

    # Single non-prime digits
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("F") == 0

    # Known examples
    assert module_0.hex_key("AB") == 1                # only B is prime
    assert module_0.hex_key("1077E") == 2             # 7 and 7
    assert module_0.hex_key("AED1F") == 2             # E? no; D counts, E no -> D only... 
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2,3,5,7,B,D
    assert module_0.hex_key("2020") == 2              # two 2s

    # Edge cases
    assert module_0.hex_key("") == 0                  # empty string
    assert module_0.hex_key("BBBB") == 4              # all primes
    assert module_0.hex_key("0011") == 0              # no primes

    print("All tests passed!")

test_hex_key()

# Generated at 2026-10-25 03:14:08.407928
# Unit test for function hex_key
def test_hex_key():
    # Single prime digits
    assert module_0.hex_key("2") == 1
    assert module_0.hex_key("D") == 1

    # Single non-prime digits
    assert module_0.hex_key("0") == 0
    assert module_0.hex_key("1") == 0
    assert module_0.hex_key("A") == 0
    assert module_0.hex_key("F") == 0

    # Known examples
    assert module_0.hex_key("AB") == 1                # only B is prime
    assert module_0.hex_key("1077E") == 2             # 7 and 7
    assert module_0.hex_key("AED1F") == 2             # E? no; D counts, E no -> D only... 
    assert module_0.hex_key("123456789ABCDEF0") == 6  # 2,3,5,7,B,D
    assert module_0.hex_key("2020") == 2              # two 2s

    # Edge cases
    assert module_0.hex_key("") == 0                  # empty string
    assert module_0.hex_key("BBBB") == 4              # all primes
    assert module_0.hex_key("0011") == 0              # no primes

    print("All tests passed!")

test_hex_key()