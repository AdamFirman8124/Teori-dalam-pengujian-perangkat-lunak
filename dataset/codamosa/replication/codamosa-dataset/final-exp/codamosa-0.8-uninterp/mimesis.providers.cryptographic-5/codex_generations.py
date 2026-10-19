

# Generated at 2022-06-14 00:05:49.715957
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.exceptions import NonEnumerableError

    crypto = Cryptographic()

    assert crypto.hash(Algorithm.SHA512)

    try:
        crypto.hash('InvalidHash')
    except NonEnumerableError:
        assert True


# Generated at 2022-06-14 00:05:56.543774
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """ Unit test for method hash of class Cryptographic"""
    ALGORITHM = [item for item in dir(Algorithm) if not item.startswith("__")]
    c = Cryptographic()

    try:
        for a in ALGORITHM:
            method = getattr(c, "hash")
            data = method(algorithm=Algorithm[a.upper()])
            assert isinstance(data, str)
    except Exception:
        pass


# Generated at 2022-06-14 00:06:00.330918
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    assert provider.hash(0) == "6f0a6be3a35a7875b43048f9e9a07bc9"


# Generated at 2022-06-14 00:06:01.381189
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash()

# Generated at 2022-06-14 00:06:07.749494
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for method hash."""
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic

    crypt = Cryptographic()
    assert isinstance(crypt.hash(Algorithm.SHA_256), str)
    assert isinstance(crypt.hash(Algorithm.SHA_512), str)
    assert isinstance(crypt.hash(Algorithm.SHA_1), str)

# Generated at 2022-06-14 00:06:08.860919
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic('en')
    print(provider.hash())

# Generated at 2022-06-14 00:06:14.671999
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic(seed=0)

    result = provider.hash(Algorithm.MD5)
    expect_result = '57ebefb7f3dde5a8e5f5d9e531e6f740'

    assert result == expect_result

# Generated at 2022-06-14 00:06:20.690795
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
  max_algorithm_value = len(list(Algorithm))
  algo = Cryptographic().hash(Algorithm(random.randrange(1,max_algorithm_value)))
  assert len(algo) > 0


# Generated at 2022-06-14 00:06:26.748795
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash(): # noqa: N802
    """Unit test for method hash of class Cryptographic."""
    c = Cryptographic()

    hash_str = c.hash()
    assert isinstance(hash_str, str), hash_str
    assert c.hash('sha256')

    # Test with enum
    from mimesis.enums import Algorithm
    assert c.hash(Algorithm.SHA256)


# Generated at 2022-06-14 00:06:32.945103
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic."""
    c = Cryptographic(seed=12345)
    test_value = c.hash()
    assert test_value == 'b06c0a7af04e7f4d4d49c7fc178b79f4'

