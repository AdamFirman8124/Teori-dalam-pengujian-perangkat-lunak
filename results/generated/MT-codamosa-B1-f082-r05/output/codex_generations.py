

# Generated at 2026-10-24 12:19:45.711606
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

# Generated at 2026-10-24 12:19:47.075439
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

# Generated at 2026-10-24 12:19:48.385796
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

# Generated at 2026-10-24 12:19:49.701631
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

# Generated at 2026-10-24 12:19:51.019371
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