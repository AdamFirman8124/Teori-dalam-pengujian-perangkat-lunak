

# Generated at 2022-06-14 00:06:31.594366
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 64


# Generated at 2022-06-14 00:06:35.648053
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    key = Algorithm.SHA256
    res = cr.hash(algorithm=key)
    assert isinstance(res, str)
    assert len(res) == 64


# Generated at 2022-06-14 00:06:36.505982
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
   c = Cryptographic()
   assert c.hash()

# Generated at 2022-06-14 00:06:39.130630
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	print(Cryptographic().hash(algorithm=Algorithm.SHA256))


# Generated at 2022-06-14 00:06:40.961928
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    with pytest.raises(NotImplementedError):
        Cryptographic().hash()

# Generated at 2022-06-14 00:06:44.290317
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    algorithm = Algorithm.SHA256
    crypto = Cryptographic()
    result = crypto.hash(algorithm)
    expected = 'SHA-256'
    assert result == expected


# Generated at 2022-06-14 00:06:51.306340
# Unit test for method hash of class Cryptographic

# Generated at 2022-06-14 00:06:55.068800
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # GIVEN
    crypto = Cryptographic()
    alg = Algorithm.SHA3_256
    # WHEN
    hash = crypto.hash(alg)
    # THEN
    assert len(hash) == 66
    # AND
    assert isinstance(hash,str)
    # AND
    assert len(hash.encode()) == 66

# Generated at 2022-06-14 00:07:03.546301
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    try:
        file = open('../tests/data/cryptographic/algorithm.txt', 'r')
        algorithms = file.read().split(',')
        assert all(map(lambda x: len(x)>0, algorithms))
    finally:
        file.close()
    for algorithm in algorithms:
        c = Cryptographic()
        assert c.hash(Algorithm(algorithm)) == c.hash(Algorithm(algorithm))


# Generated at 2022-06-14 00:07:06.932146
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash() != None

# Generated at 2022-06-14 00:08:06.144298
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    i = 0
    while i < 100:
        print(Cryptographic().hash(Algorithm.SHA1))
        i = i + 1


# Generated at 2022-06-14 00:08:08.507315
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    s = Cryptographic()
    s_hash = s.hash()
    assert len(s_hash) == 40

# Generated at 2022-06-14 00:08:11.101491
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash of class Cryptographic"""
    crypto = Cryptographic() 
    data = crypto.hash()
    print(data)

# Generated at 2022-06-14 00:08:13.872972
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    hashed_value = c.hash()
    assert len(hashed_value) > 0

# Generated at 2022-06-14 00:08:15.936751
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    test_Cryptographic_hash()
    """
    import mimesis
    c=mimesis.Cryptographic()
    print(c.hash())


# Generated at 2022-06-14 00:08:20.732669
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    assert re.search(r"[a-zA-Z0-9]{128}", cr.hash()) != None


# Generated at 2022-06-14 00:08:24.079433
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test hash method of class Cryptographic."""
    c = Cryptographic()
    h = c.hash()
    assert isinstance(h, str)
    assert isinstance(c.hash(Algorithm.SHA224), str)
    assert isinstance(c.hash(Algorithm.SHA256), str)
    assert isinstance(c.hash(Algorithm.SHA384), str)
    assert isinstance(c.hash(Algorithm.SHA512), str)


# Generated at 2022-06-14 00:08:28.664713
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic().hash(), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA1), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA224), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA256), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA384), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA512), str)


# Generated at 2022-06-14 00:08:35.686988
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unittest for the method hash in Cryptographic"""
    assert Cryptographic().hash(Algorithm.SHA256) == "b4a8fa15894d4c69c4a5e5da5a5a5baf94caf5231e80ff38abf2f22f8660b07f"
    assert Cryptographic().hash(Algorithm.SHA512) == "1aa78f8a68c38a7ddcbd0f9a9398d9c9d60a70fcf2e8c5d5d5f5c5ca5dd5b4a4f4d4b4e4c4a4e4d4c4a4b4a5c5d5f5c5e"


# Generated at 2022-06-14 00:08:43.393486
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    print("*" * 10, " Unit test for method hash of class Cryptographic", "*" * 10, "\n")
    cr = Cryptographic()
    t1 = Algorithm.MD5
    t2 = Algorithm.SHA256
    t3 = Algorithm.CRC32
    print("md5: ", cr.hash(t1))
    print("sha256: ", cr.hash(t2))
    print("crc32: ", cr.hash(t3), "\n")
    print("*" * 8, " End of unit test ", "*" * 8, "\n")


# Generated at 2022-06-14 00:09:12.151800
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    gen = Cryptographic()
    x = gen.hash(Algorithm.SHA224)
    assert len(x) == 56
    assert (x[0] == 'd' or x[0] == 'c' or x[0] == 'e')
    assert (x[1] == 'd' or x[1] == 'c' or x[1] == 'e')
    assert (x[2] == 'd' or x[2] == 'c' or x[2] == 'e')
    assert (x[3] == 'd' or x[3] == 'c' or x[3] == 'e')
    assert (x[4] == 'd' or x[4] == 'c' or x[4] == 'e')

# Generated at 2022-06-14 00:09:17.617475
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto_provider = Cryptographic()
    crypto_provider.seed(11)
    assert crypto_provider.hash(Algorithm.MD5) == 'e456752bc74eb188bc867cf1b7a5dfba'

# Generated at 2022-06-14 00:09:24.789004
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash() == '07d49f62bc7f4491a6a68d0d2e6c1e6e0a622f27b1e9b8e841ef89afc2a0a06d'
    assert crypto.hash() == '9f9e1d23a576cf05a89efc71e36d7bdc48a3a3bdf1c20aa9d7d9db239d2b744a'


# Generated at 2022-06-14 00:09:27.644596
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash of class Cryptographic"""
    assert len(Cryptographic().hash()) == 32


# Generated at 2022-06-14 00:09:38.088139
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash."""
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic
    c = Cryptographic()
    print(c.hash(algorithm=Algorithm.MD4))
    print(c.hash(algorithm=Algorithm.MD5))
    print(c.hash(algorithm=Algorithm.SHA1))
    print(c.hash(algorithm=Algorithm.SHA224))
    print(c.hash(algorithm=Algorithm.SHA256))
    print(c.hash(algorithm=Algorithm.SHA384))
    print(c.hash(algorithm=Algorithm.SHA512))
    print(c.hash(algorithm=Algorithm.SHA3_224))
    print(c.hash(algorithm=Algorithm.SHA3_256))


# Generated at 2022-06-14 00:09:44.087903
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """test_Cryptographic_hash()
    test method hash() of class Cryptographic
    """
    test_algorithm = Algorithm.SHA256
    provider = Cryptographic()  # type: ignore
    hash = provider.hash(test_algorithm)

    assert hash
    assert isinstance(hash, str)
    assert len(hash) == 64

    # test when algorithm is None
    hash = provider.hash()
    assert hash
    assert isinstance(hash, str)
    assert len(hash) == 64


# Generated at 2022-06-14 00:09:48.427411
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    a = Cryptographic()
    assert isinstance(a.hash(), str)
    assert isinstance(a.hash(Algorithm.MD5), str)


# Generated at 2022-06-14 00:09:54.824927
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))
    print(Cryptographic().hash(Algorithm.SHA_224))

# Generated at 2022-06-14 00:09:56.368740
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash(Algorithm.SHA512)

# Generated at 2022-06-14 00:10:01.810102
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    alg = Algorithm.SHA1
    assert Cryptographic().hash(alg).isalnum()
    
    # now we check if it is the right hash algorithm
    import hashlib
    fn = getattr(hashlib, alg.name)
    assert fn(Cryptographic().uuid().encode()).hexdigest() == Cryptographic().hash(alg)

# Generated at 2022-06-14 00:10:39.990617
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash() is not None



# Generated at 2022-06-14 00:10:41.364882
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash() != ''

# Generated at 2022-06-14 00:10:42.373718
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    print(Cryptographic().hash())


# Generated at 2022-06-14 00:10:44.802575
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    p = Cryptographic()
    assert p.hash()

# Generated at 2022-06-14 00:10:57.563278
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 64
    assert len(Cryptographic(seed=1).hash()) == 64
    assert Cryptographic().hash() != Cryptographic().hash()
    assert Cryptographic(seed=1).hash() != Cryptographic(seed=1).hash()
    assert Cryptographic(seed=1).hash(Algorithm.SHA3_512) \
           != Cryptographic(seed=1).hash(Algorithm.MD5)
    assert Cryptographic().hash() != Cryptographic(seed=1).hash()
    assert Cryptographic(seed=1).hash(Algorithm.SHA224) \
           != Cryptographic().hash(Algorithm.SHA224)
    assert Cryptographic(seed=1).hash(Algorithm.SHA3_224) \
           != Cryptographic(seed=2).hash(Algorithm.SHA3_224)


# Generated at 2022-06-14 00:11:04.260255
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for method hash of class Cryptographic."""

    mimesis.seed('7f08d1b0-7d2a-495c-b3f3-e3dda894792c')

    assert len(mimesis.Cryptographic().hash()) == 64


# Generated at 2022-06-14 00:11:06.310706
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hasher = Cryptographic()
    assert hasher.hash() != None


# Generated at 2022-06-14 00:11:20.062060
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	from mimesis.enums import *
	obj = Cryptographic()
	assert obj.hash(Algorithm.BLAKE2B) == '0d31c57459543a11c3fb3d9f6c57a6b569affd37e2e2a1e5a6b8e8fbbc6bcfd7'
	assert obj.hash(Algorithm.BLAKE2S) == '4b4f5967f79e9d504412bace14a0a8a3d3f90e7f83e07a8dd8f465d39d9a89a0'

# Generated at 2022-06-14 00:11:29.888924
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Test generate hash from class Cryptographic
    """
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic

    crypto = Cryptographic()
    # Generate SHA1 hash
    sha1 = crypto.hash(Algorithm.SHA1)

    assert isinstance(sha1, str)
    assert len(sha1) == 40

    # Generate SHA256 hash
    sha256 = crypto.hash(Algorithm.SHA256)

    assert isinstance(sha256, str)
    assert len(sha256) == 64

    # Generate SHA512 hash
    sha512 = crypto.hash(Algorithm.SHA512)

    assert isinstance(sha512, str)
    assert len(sha512) == 128

# Generated at 2022-06-14 00:11:35.025192
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash() == '225dd8982ee7d87b1d9a7fad1e8a79fcb7f9ce9c0f7d84e8e2c735cf5a5c886d'