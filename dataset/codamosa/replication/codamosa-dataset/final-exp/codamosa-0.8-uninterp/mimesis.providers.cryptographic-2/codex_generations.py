

# Generated at 2022-06-14 00:06:00.808208
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    h = c.hash(Algorithm.SHA256)
    print(h)
    # a8d378e1a9b9e5f5d5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5
    # because of the seed of the object c

# Generated at 2022-06-14 00:06:02.299976
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert True, "this is test for method hash of class Cryptographic"


# Generated at 2022-06-14 00:06:10.711985
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Hash
    s = Cryptographic("en")
    print(s.hash())
    print(s.hash(algorithm=Algorithm.SHA1))
    print(s.hash(algorithm=Algorithm.SHA224))
    print(s.hash(algorithm=Algorithm.SHA256))
    print(s.hash(algorithm=Algorithm.SHA384))
    print(s.hash(algorithm=Algorithm.SHA512))
    print(s.hash(algorithm=Algorithm.MD5))
    print(s.hash(algorithm=Algorithm.BLAKE2S))
    print(s.hash(algorithm=Algorithm.BLAKE2B))


# Generated at 2022-06-14 00:06:13.428879
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.providers.cryptographic import Cryptographic
    cg = Cryptographic()
    cg.hash()

# Generated at 2022-06-14 00:06:15.446559
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert isinstance(c.hash(), str)


# Generated at 2022-06-14 00:06:17.348727
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic().hash(), str)



# Generated at 2022-06-14 00:06:19.655711
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    alg = Algorithm.MD5
    assert isinstance(c.hash(alg), str)


# Generated at 2022-06-14 00:06:21.668330
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 32
    assert len(Cryptographic().hash(Algorithm.SHA512)) == 128

"""
Public API for Crypto Module
"""


# Generated at 2022-06-14 00:06:26.514903
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Generate hash for different hashing algorithms."""
    crypto = Cryptographic()
    for alg in Algorithm.__members__.values():
        print(f"Hash function {alg.name}: {crypto.hash(alg)}")
    crypto.reset_seed()


# Generated at 2022-06-14 00:06:32.333875
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic."""
    assert Cryptographic().hash() == 'fba91d91343f20dfb831c3da1fe80e15d3763fe7118b1f2a6f9d6d914f760c8b'


# Generated at 2022-06-14 00:07:23.953734
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash_object = Cryptographic().hash(Algorithm.SHA256)
    assert hash_object is not None
    assert len(hash_object) == 64


# Generated at 2022-06-14 00:07:25.281738
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # args
    algorithm = None
    # init
    obj = Cryptographic()
    # run
    ret = obj.hash(algorithm)
    # check
    assert (len(ret) == 40)

# Generated at 2022-06-14 00:07:35.406589
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
  c = Cryptographic(seed=12345)
  assert len(c.uuid()) == len("df24b6f0-e0b1-4b03-a973-e62e6d8b6294")
  assert c.hash() == 'dd4c8e4e1f2d1c4053d934b8ab88b3af3f4d4a4e4a8a751238982a91d6d53ea9'
  assert c.hash(algorithm=Algorithm.SHA256) == 'dd4c8e4e1f2d1c4053d934b8ab88b3af3f4d4a4e4a8a751238982a91d6d53ea9'


# Generated at 2022-06-14 00:07:37.871292
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    assert cr.hash() == cr.hash()


# Generated at 2022-06-14 00:07:48.617571
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash_list = {
        "sha224", "sha384", "sha256", "sha512", "blake2b", "md5", "blake2s",
        "sha1", "sha3_224", "sha3_512", "sha3_256", "sha3_384"
    }
    c = Cryptographic()
    h = c.hash(Algorithm.MD5)
    assert isinstance(h, str)
    assert hashlib.sha512(h.encode()).hexdigest() in hash_list

# Generated at 2022-06-14 00:07:51.972201
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.SHA256)=="5a74e3a3bff0e948c6200cdfb56f2543e1d6fa8a77b76c6ad619f460bc9d47e8"


# Generated at 2022-06-14 00:07:56.200467
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic

    crypto = Cryptographic('en')
    # Using default algorithm
    hash_ = crypto.hash()
    assert isinstance(hash_, str)
    # Override algorithm
    hash_ = crypto.hash(algorithm=Algorithm.MD5)
    assert isinstance(hash_, str)

# Generated at 2022-06-14 00:07:57.679147
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    print(provider.hash())


# Generated at 2022-06-14 00:08:08.309993
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash(Algorithm.MD5) == 'a0b6ef8f8fd9b2ef1c6c5ddae8453b63'
    assert crypto.hash(Algorithm.SHA1) == 'ea9efe2cda6f5e01d847f109e1604b5f5c5d5fb8'
    assert crypto.hash(Algorithm.SHA224) == '12a8cdcf94b3b049a178714abfcbcad9e43657a027c13f87ff2e4b'

# Generated at 2022-06-14 00:08:14.673287
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    print(c.hash(Algorithm.MD5))     # '9e8c280274c45e7efc6ce5024a1d30cf'
    print(c.hash(Algorithm.SHA1))    # 'a790a8a96c45b6276589daf6ed9bf4998b2c2f52'
    print(c.hash(Algorithm.SHA224))  # 'ad67c3a9a8b8a5dd95e4c93a4bffd4c4d4be4f1b2a5e9592b77c8b0e'
    print(c.hash(Algorithm.SHA256))  # 'd2fbb99016ee27dc695c0b7fdbcbc32d5cb5b531f1a

# Generated at 2022-06-14 00:08:49.996332
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # When
    result = Cryptographic('en').hash(algorithm=Algorithm.SHA256)
    # Then
    assert len(result) == 64



# Generated at 2022-06-14 00:08:53.636717
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    result = c.hash(Algorithm.MD5)

    valid_hash = hashlib.md5(c.uuid().encode()).hexdigest()
    assert result == valid_hash



# Generated at 2022-06-14 00:08:56.638986
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    result = c.hash(algorithm=Algorithm.MD5)
    assert isinstance(result, str)
    assert len(result) == 32


# Generated at 2022-06-14 00:08:59.795499
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert (len(Cryptographic().hash()) == 64)


# Generated at 2022-06-14 00:09:03.266581
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    _cp = Cryptographic()
    _hash = _cp.hash()
    print(f'_hash={_hash}')

# Generated at 2022-06-14 00:09:13.587612
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash() == '633e91a0599f1af2c01ce966b7782c93f13eb8b3c3d3d7e8844b4516434b1c2e'
    assert Cryptographic().hash(Algorithm.SHA224) == 'd501f1eec825095a7a9c70a923b6c027b1fcd8e4d4e4e4b2c55b4699'
    assert Cryptographic().hash(Algorithm.SHA256) == 'dc38a5cf5e5af5a5c27ed8d3e3b931d1209c4a8e0c0cad799cd4ddaacdf2c0b8'

# Generated at 2022-06-14 00:09:16.305341
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Test return type
    assert type(Cryptographic().hash()) == str


# Generated at 2022-06-14 00:09:18.247629
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    assert isinstance(provider.hash(), str)


# Generated at 2022-06-14 00:09:24.614539
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for method hash of class Cryptographic."""
    a = Cryptographic()
    answer = a.hash()
    # assert isinstance(answer, str)
    assert answer is not None
    assert len(answer) > 0


# Generated at 2022-06-14 00:09:28.023758
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    result = provider.hash(Algorithm.SHA3_512)
    assert len(result) == 128