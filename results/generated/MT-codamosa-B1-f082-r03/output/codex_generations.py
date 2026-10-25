

# Generated at 2026-10-24 10:44:43.324046
# Unit test for function prime_length
def test_prime_length():
    # lengths 0 and 1 -> not prime
    assert module_0.prime_length("") is False
    assert module_0.prime_length("a") is False

    # smallest prime length
    assert module_0.prime_length("ab") is True

    # prime lengths
    for n in (2, 3, 5, 7, 11, 13, 97, 101):
        assert module_0.prime_length("a" * n) is True, f"len={n} should be prime"

    # composite lengths (including perfect squares)
    for n in (4, 6, 8, 9, 10, 12, 25, 49, 100):
        assert module_0.prime_length("a" * n) is False, f"len={n} should not be prime"

    # content is irrelevant, only length matters
    assert module_0.prime_length("hello") is True   # len 5
    assert module_0.prime_length("hello!") is False  # len 6


if __name__ == "__main__":
    test_prime_length()
    print("all tests passed")

# Generated at 2026-10-24 10:44:45.902767
# Unit test for function prime_length

# Generated at 2026-10-24 10:44:48.415250
# Unit test for function prime_length

# Generated at 2026-10-24 10:44:50.845678
# Unit test for function prime_length

# Generated at 2026-10-24 10:44:53.268054
# Unit test for function prime_length

# Generated at 2026-10-24 10:44:55.689923
# Unit test for function prime_length

# Generated at 2026-10-24 10:44:58.282964
# Unit test for function prime_length

# Generated at 2026-10-24 10:45:00.700557
# Unit test for function prime_length

# Generated at 2026-10-24 10:45:03.117249
# Unit test for function prime_length

# Generated at 2026-10-24 10:45:05.536397
# Unit test for function prime_length

# Generated at 2026-10-24 10:45:07.953206
# Unit test for function prime_length

# Generated at 2026-10-24 10:45:16.544243
# Unit test for function prime_length
def test_prime_length():assert module_0.prime_length("") == False