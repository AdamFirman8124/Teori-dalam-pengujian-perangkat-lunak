

# Generated at 2022-06-14 00:05:53.502621
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Testing Cryptographic.hash."""
    from hashlib import md5, sha1
    from random import random
    from uuid import UUID
    from mimesis.enums import Algorithm
    i = random()
    a = Cryptographic(i).hash()
    b = md5(UUID(int=(int(i * 16**6) % (1 << 128))).bytes).hexdigest()
    c = sha1(UUID(int=(int(i * 16**6) % (1 << 128))).bytes).hexdigest()
    assert a in [b, c]
    assert len(Cryptographic(i).hash(Algorithm.MD5)) == len(b)
    assert len(Cryptographic(i).hash(Algorithm.SHA1)) == len(c)

# Generated at 2022-06-14 00:05:54.139348
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    pass

# Generated at 2022-06-14 00:06:05.842858
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    for i in range(1000):
        # A003,A004
        hash_result = Cryptographic()._Cryptographic__hash(Algorithm.SHA1)
        assert isinstance(hash_result, str)

        hash_result = Cryptographic()._Cryptographic__hash(Algorithm.SHA224)
        assert isinstance(hash_result, str)

        hash_result = Cryptographic()._Cryptographic__hash(Algorithm.SHA256)
        assert isinstance(hash_result, str)

        hash_result = Cryptographic()._Cryptographic__hash(Algorithm.SHA384)
        assert isinstance(hash_result, str)

        hash_result = Cryptographic()._Cryptographic__hash(Algorithm.SHA512)
        assert isinstance(hash_result, str)


# Generated at 2022-06-14 00:06:12.642412
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    print("\n -- START --")
    c=Cryptographic()
    try_list=[c.hash(),c.hash(),c.hash(),c.hash(),c.hash()]
    print("\n[md5]: ",try_list.count("9e107d9d372bb6826bd81d3542a419d6"))
    print("\n[sha1]: ",try_list.count("2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"))
    print("\n[sha256]: ",try_list.count("d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"))

# Generated at 2022-06-14 00:06:16.572091
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Test method Cryptographic.hash(algorithm)
    """
    # Arrange
    # Act
    result = Cryptographic.hash(Algorithm.MD5)

    # Assert
    assert(isinstance(result, str))

# Generated at 2022-06-14 00:06:23.375082
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():     # noqa: E501
    """
    Test for Cryptographic.hash method
    """
    from mimesis.enums import Algorithm

    cr = Cryptographic()
    key = cr._validate_enum(Algorithm.SHA3_256, Algorithm)
    if hasattr(hashlib, key):
        fn = getattr(hashlib, key)
        return fn(cr.uuid().encode()).hexdigest()  # type: ignore
    else:
        return False


# Generated at 2022-06-14 00:06:32.108032
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    generator = Cryptographic(seed=42)
    h = generator.hash(Algorithm.MD5)
    assert h == 'b9a9f2f4e4f4c4a8b442902b40f5f5d5'
    h = generator.hash(Algorithm.SHA1)
    assert h == 'e0bc7bcb1b21608b7e3babd47b7da26282377f8b'
    h = generator.hash(Algorithm.SHA224)
    assert h == 'b64e9b92e27ea8f10e1c5f5ce5d5c925fe5f5b1d5db1f9e9dfa8b7f6'
    h = generator.hash(Algorithm.SHA256)

# Generated at 2022-06-14 00:06:40.830851
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # noqa: C901
    """Test for `hash` method of the class Cryptographic."""
    import random
    import string

    random.seed(0)
    string.whitespace = ' ' * 10
    string.printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    crypto = Cryptographic()
    assert crypto.hash() == '9c9a4e4c17d4f84516a4a62d7ab99ccc'

# Generated at 2022-06-14 00:06:43.340109
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.MD5) != Cryptographic().hash(Algorithm.MD5)

# Generated at 2022-06-14 00:06:47.985272
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    h = c.hash(Algorithm.MD5)
    assert isinstance(h, str) and h != ""

# Generated at 2022-06-14 00:07:22.054909
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 40


# Generated at 2022-06-14 00:07:32.353261
# Unit test for method hash of class Cryptographic

# Generated at 2022-06-14 00:07:43.860352
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    # Tests for class Cryptographic
    c = Cryptographic()
    assert c.hash() == '4a07e4d4add01f17efdd93e5d5f5e5c5'
    assert c.hash(Algorithm.SHA256) == '633cf0c7e1687d9f6996b446251a1a41c96acf3d87d093a2a10c7c60d9f27b7c'
    assert c.hash(Algorithm.MD5) == '3c5f30b5fd66dd5d5ad5b5ec5b5e5c5f'

# Generated at 2022-06-14 00:07:48.224996
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    hash = c.hash()
    assert len(hash) == 64
    assert type(hash).__name__ == 'str'


# Generated at 2022-06-14 00:07:55.577320
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.SHA224) == "ec1e6acd5f5a53497e5d72b79e25d2ffceb9625fe63462c36d4d4f39"
    assert Cryptographic().hash(Algorithm.SHA512) == "3c8e6b407f0ddaac6d3c3fe858a2e7d9d9ecec7a7f1afb223228ab94d545fa96a7e866e162fbdc7b9a472a662652c78a18a60d7a68299cfd2fd1778a8e5716f9"

# Generated at 2022-06-14 00:07:59.328609
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    length = 100
    count = 0

    while count < length:
        try:
            Cryptographic.hash()
            count = count + 1
        except:
            count = count - 1

    assert count == length


# Generated at 2022-06-14 00:08:02.427491
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test Cryptographic.hash method."""
    c1 = Cryptographic(seed=1)
    c2 = Cryptographic(seed=2)
    assert c1.hash() != c2.hash()


# Generated at 2022-06-14 00:08:07.490680
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.schema import Field

    class User(metaclass=Field):
        password = Cryptographic().hash(algorithm=Algorithm.MD5)

    assert isinstance(User.password(), str)
    assert len(User.password()) == 32


# Generated at 2022-06-14 00:08:09.977062
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cryptographic = Cryptographic()
    isinstance(cryptographic.hash(), str)


# Generated at 2022-06-14 00:08:14.086739
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic."""
    crypto = Cryptographic()
    assert crypto.hash() == crypto.hash()