

# Generated at 2022-06-14 00:07:24.967720
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Arrange
    crypto = Cryptographic()

    # Act
    sha1 = crypto.hash(Algorithm.SHA1)
    sha256 = crypto.hash(Algorithm.SHA256)
    sha512 = crypto.hash(Algorithm.SHA512)

    # Assert
    assert len(sha1) == 40
    assert sha1.isalnum()

    assert len(sha256) == 64
    assert sha256.isalnum()

    assert len(sha512) == 128
    assert sha512.isalnum()


# Generated at 2022-06-14 00:07:32.027412
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash(Algorithm.MD5)
    assert crypto.hash(Algorithm.SHA1)
    assert crypto.hash(Algorithm.SHA224)
    assert crypto.hash(Algorithm.SHA256)
    assert crypto.hash(Algorithm.SHA384)
    assert crypto.hash(Algorithm.SHA512)


# Generated at 2022-06-14 00:07:35.992828
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic().hash()
    assert isinstance(hash, str)
    assert len(hash) == 64


# Generated at 2022-06-14 00:07:39.823929
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    data = c.hash(Algorithm.MD5)
    assert isinstance(data, str)
    assert len(data) == 32


# Generated at 2022-06-14 00:07:43.865689
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    cr.hash(Algorithm.SHA256)

# Generated at 2022-06-14 00:07:50.763782
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for hash method."""
    from mimesis.enums import Algorithm
    length = 20
    alg = Algorithm.SHA256
    cg = Cryptographic('en')
    hash_ = cg.hash(Algorithm.SHA256)
    assert isinstance(hash_, str)
    assert len(hash_) == length
    assert isinstance(alg, Algorithm)
    assert type(alg) != str


# Generated at 2022-06-14 00:07:53.967208
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    hashed = c.hash()
    assert hashed == '27d0e5ad5e5c5ae9e5f7c6c0dac8a13f'

# Generated at 2022-06-14 00:07:57.919184
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    CRYPTO = Cryptographic()
    result = CRYPTO.hash()
    assert len(result) == 64

# Generated at 2022-06-14 00:07:59.665110
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    a = Cryptographic()
    print(a.hash())


# Generated at 2022-06-14 00:08:05.852925
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    algorithm_list = Algorithm.__members__
    for key in algorithm_list:
        algorithm = Algorithm[key]
        print(key, algorithm)
        def fn(algorithm):
            print(algorithm)
            from mimesis.enums import Algorithm
            _hash = Cryptographic().hash(algorithm=algorithm)
            print(_hash)
        fn(algorithm)

# Generated at 2022-06-14 00:10:45.681316
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    print('Testing hash')
    a = Cryptographic()
    print(a.hash())


# Generated at 2022-06-14 00:10:59.774077
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    assert cr.hash(Algorithm.MD5) == '9f2a9b30a31d8133d55c46e278cccb78'
    assert cr.hash(Algorithm.SHA1) == '9fe75d3563a71b08e3c1a5a6d5f6ca581d6c5a5e'
    assert cr.hash(Algorithm.SHA224) == 'e45d66ac6020d18a4d4e4e4a4f25a1ea40e1fbcb0fb3892c670eac8b'

# Generated at 2022-06-14 00:11:03.248591
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    result=provider.hash()
    assert isinstance(result,str)


# Generated at 2022-06-14 00:11:06.835888
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    ins = Cryptographic()
    result = ins.hash(algorithm=Algorithm.SHA1)
    assert len(result) == 40


# Generated at 2022-06-14 00:11:20.681944
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    import sys
    import pickle
    if sys.version_info[0] < 3:
        from cStringIO import StringIO
    else:
        from io import BytesIO as StringIO
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.enums import Algorithm
    from mimesis.enums import Algorithm
    pickled_data = b'\x80\x03c__main__\nCryptographic\nq\x00)\x81q\x01.'
    stream = StringIO(pickled_data)
    obj = pickle.load(stream)

# Generated at 2022-06-14 00:11:22.604362
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cry = Cryptographic()
    print(cry.hash())

# Generated at 2022-06-14 00:11:36.474636
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Test function for method hash of class Cryptographic.
    """
    from mimesis.enums import Algorithm

    c = Cryptographic()

    # To test algorithm=None
    h = c.hash()
    assert isinstance(h, str)

    # To test algorithm=Algorithm.MD5
    h = c.hash(Algorithm.MD5)
    assert isinstance(h, str)

    # To test algorithm=Algorithm.SHA512
    h = c.hash(Algorithm.SHA512)
    assert isinstance(h, str)

    # To test algorithm=Algorithm.SHA3_512
    h = c.hash(Algorithm.SHA3_512)
    assert isinstance(h, str)

    # To test algorithm=Algorithm.BLAKE2_S

# Generated at 2022-06-14 00:11:37.924080
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    o = Cryptographic()
    o.hash(Algorithm.SHA256)


# Generated at 2022-06-14 00:11:45.489968
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash of class Cryptographic."""
    instance = Cryptographic()
    assert hasattr(instance, 'hash')
    assert isinstance(instance.hash(), str)
    assert len(instance.hash()) == 64
    assert isinstance(instance.uuid(), str)
    assert instance.uuid() != instance.uuid()
    assert len(instance.uuid()) == 36
    print("Cryptographic: Hash correctly generated!")


# Generated at 2022-06-14 00:11:47.274807
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash(Algorithm.MD5)) == 32


# Generated at 2022-06-14 00:15:22.858929
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    test_instance = Cryptographic()
    assert test_instance.hash(Algorithm.MD5)
    assert test_instance.hash(Algorithm.SHA1)
    assert test_instance.hash(Algorithm.SHA224)
    assert test_instance.hash(Algorithm.SHA256)
    assert test_instance.hash(Algorithm.SHA384)
    assert test_instance.hash(Algorithm.SHA512)

# Generated at 2022-06-14 00:15:25.169091
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.SHA256) is not None

# Generated at 2022-06-14 00:15:30.440055
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cryp = Cryptographic()
    h = cryp.hash()
    assert isinstance(h, str)


# Generated at 2022-06-14 00:15:34.984424
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.MD5) != Cryptographic().hash(Algorithm.MD5)
    assert Cryptographic().hash(Algorithm.SHA256) != Cryptographic().hash(Algorithm.SHA256)

