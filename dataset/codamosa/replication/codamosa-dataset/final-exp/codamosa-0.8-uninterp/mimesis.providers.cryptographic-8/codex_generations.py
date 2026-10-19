

# Generated at 2022-06-14 00:06:44.872961
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    assert cr.hash()


# Generated at 2022-06-14 00:06:54.996205
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    import random
    test_pass = False
    c = Cryptographic()
    try:
        print("Testing Cryptographic().hash()")
        algorithms = ['md5','sha1','sha224','sha512','sha384','sha256']
        for i in range(0,20):
            print("Now testing if the hash of algorithm " + algorithms[random.randint(0,5)] + " is a random value")
            h = c.hash(Algorithm(algorithms[random.randint(0,5)]))
            #print(h)
            assert type(h) == str
    except AssertionError:
        print("Test Failed!")
        test_pass = False
    else:
        print("Test Passed!")
        test_pass = True
    return test_pass


# Generated at 2022-06-14 00:07:05.343485
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # test creating new hash
    hash = Cryptographic().hash(Algorithm.MD5)
    assert hash, 'MD5 hash is None'
    assert len(hash) == 32, 'MD5 hash length is not 32'
    assert isinstance(hash, str), 'MD5 hash is not of class str'

    # test creating new hash
    hash = Cryptographic().hash(Algorithm.BLAKE2B)
    assert hash, 'BLAKE2B hash is None'
    assert len(hash) == 128, 'BLAKE2B hash length is not 128'
    assert isinstance(hash, str), 'BLAKE2B hash is not of class str'


# Generated at 2022-06-14 00:07:12.509840
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	crypto = Cryptographic()

	assert len(crypto.hash(Algorithm.MD5)) == 32
	assert len(crypto.hash(Algorithm.SHA_1)) == 40
	assert len(crypto.hash(Algorithm.SHA_224)) == 56
	assert len(crypto.hash(Algorithm.SHA_256)) == 64
	assert len(crypto.hash(Algorithm.SHA_384)) == 96
	assert len(crypto.hash(Algorithm.SHA_512)) == 128



# Generated at 2022-06-14 00:07:21.228205
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic."""
    crypto = Cryptographic()
    algorithms = {
        Algorithm.MD5: 'MD5',
        Algorithm.SHA1: 'SHA1',
        Algorithm.SHA224: 'SHA224',
        Algorithm.SHA256: 'SHA256',
        Algorithm.SHA384: 'SHA384',
        Algorithm.SHA512: 'SHA512'
    }
    for algorithm in algorithms:
        assert algorithms[algorithm] in crypto.hash(algorithm)

# Generated at 2022-06-14 00:07:23.997709
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    inst = Cryptographic()
    hash = inst.hash()

    # Length of the hash
    assert len(hash) == 32

    # Type of the hash
    assert isinstance(hash, str)

    # Value of the hash
    assert hash == 'd7e3f38b30525f2a0fdea64e23bd4d4c'

# Generated at 2022-06-14 00:07:25.998935
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    print(provider.hash(Algorithm.BLAKE2B))
    print(provider.hash(Algorithm.SHA3_512))


# Generated at 2022-06-14 00:07:29.452851
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    result = provider.hash(Algorithm.SHA3_512)
    assert(result is not None)

# Generated at 2022-06-14 00:07:31.072881
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic.hash(), str)


# Generated at 2022-06-14 00:07:36.214868
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Given
    c = Cryptographic()

    # When
    result = c.hash()

    # Then
    assert isinstance(result, str)
    assert len(result) == 256


# Generated at 2022-06-14 00:10:18.068131
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    hash = crypto.hash()
    # assert isinstance(hash, str)



# Generated at 2022-06-14 00:10:27.181903
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic
    crypto = Cryptographic()
    crypto.seed(1)
    crypto.hash(Algorithm.MD5) # test_Cryptographic_hash_0
    crypto.hash(Algorithm.BLAKE2B) # test_Cryptographic_hash_1
    crypto.hash(Algorithm.BLAKE2S) # test_Cryptographic_hash_2
    crypto.hash(Algorithm.SHA1) # test_Cryptographic_hash_3
    crypto.hash(Algorithm.SHA224) # test_Cryptographic_hash_4
    crypto.hash(Algorithm.SHA256) # test_Cryptographic_hash_5
    crypto.hash(Algorithm.SHA384) # test_Cryptographic_hash_6
    crypto.hash

# Generated at 2022-06-14 00:10:31.712328
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    hash = crypto.hash()
    assert crypto.hash(algorithm=Algorithm.sha256) == hash

# Generated at 2022-06-14 00:10:34.052156
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic.hash() is not None
    assert Cryptographic.hash(Algorithm.SHA256) is not None


# Generated at 2022-06-14 00:10:45.143223
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash(): #noqa
    # Verify different hash values for different algorithms
    x = Cryptographic()
    md5 = x.hash(Algorithm.MD5)
    sha1 = x.hash(Algorithm.SHA1)
    sha224 = x.hash(Algorithm.SHA224)
    sha256 = x.hash(Algorithm.SHA256)
    sha384 = x.hash(Algorithm.SHA384)
    sha512 = x.hash(Algorithm.SHA512)
    assert isinstance(md5, str)
    assert isinstance(sha1, str)
    assert isinstance(sha224, str)
    assert isinstance(sha256, str)
    assert isinstance(sha384, str)
    assert isinstance(sha512, str)
    assert md5 != sha1
    assert sha1 != sha224

# Generated at 2022-06-14 00:10:46.750925
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash()

# Generated at 2022-06-14 00:10:51.780027
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash(Algorithm.SHA224) == 'f8d76c7f0e0df988a2a2da8e3d4f4a4b90c4b4d8c8a2547339'

# Generated at 2022-06-14 00:10:56.210553
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    print("Testing Cryptographic_hash()")
    c = Cryptographic()
    hash = c.hash()
    assert(hash != None)


# Generated at 2022-06-14 00:11:03.816144
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # first test
    provider = Cryptographic()
    result = provider.hash(algorithm=Algorithm.MD5)
    assert isinstance(result, str) is True

    # second test
    provider = Cryptographic(seed=123)
    result = provider.hash(algorithm=Algorithm.SHA1)
    assert isinstance(result, str) is True

# Generated at 2022-06-14 00:11:06.831789
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    u = Cryptographic().hash()
    assert(len(u) == 64)
