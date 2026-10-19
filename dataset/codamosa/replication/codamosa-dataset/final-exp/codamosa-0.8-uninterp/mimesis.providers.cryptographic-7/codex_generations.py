

# Generated at 2022-06-14 00:05:45.194635
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    obj = Cryptographic()
    assert obj.hash() == 'e4e2b4c9f9d8b20c077c65aeee29d6b217a6fbaa6ddf19b1eca9b1d8af011c37'


# Generated at 2022-06-14 00:05:48.341633
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash() of class Cryptographic."""
    c = Cryptographic()
    assert len(c.hash()) == 40


# Generated at 2022-06-14 00:05:52.458356
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    try:
        h =Cryptographic().hash()
        assert h is not None
    except Exception:
        assert True


# Generated at 2022-06-14 00:05:54.413028
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()

    assert crypto.hash() != crypto.hash()

# Generated at 2022-06-14 00:06:00.170731
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic"""
    alg: Algorithm = Algorithm['MD5']

    inst = Cryptographic()

    # Test direct access
    result = inst.hash()
    assert result is not None

    # Test via method
    result = inst.hash(algorithm=alg)
    assert result is not None


# Generated at 2022-06-14 00:06:01.701454
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypt = Cryptographic()
    assert crypt.hash(Algorithm.SHA1)

# Generated at 2022-06-14 00:06:03.928568
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    h1 = Cryptographic().hash()
    h2 = Cryptographic().hash()
    assert(h1 != h2)



# Generated at 2022-06-14 00:06:12.045548
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Tests method hash of class Cryptographic."""
    crypto = Cryptographic()
    # Importing Algorithm enums
    from mimesis.enums import Algorithm
    # Creating a test set

# Generated at 2022-06-14 00:06:16.171231
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    #algorithm = Algorithm(choice("hashlib.algorithms_guaranteed"))
    algorithm = Algorithm("sha256")
    assert len(crypto.hash(algorithm)) == 64

# Generated at 2022-06-14 00:06:17.662484
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic().hash()
    assert len(hash) == 64

# Generated at 2022-06-14 00:07:09.935794
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Check methods hash of class Cryptographic."""
    # The method uuid() is tested above
    # The method token_bytes() is tested above
    # The method token_hex() is tested above
    # The method token_urlsafe() is tested above
    # The method mnemonic_phrase() is tested above



# Generated at 2022-06-14 00:07:17.448421
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    engine = Cryptographic(seed=101)
    assert (engine.hash() == '23a3b7c14bf19645ef8e78c58f3cb3fa76149f22080d8c5f5bd5c5abd49a9ac2')
    assert (engine.hash(algorithm=Algorithm.SHA224) == '099e1c9d7c9a9f96a92f3d3b89a7e8246a8060c7d2a2e1f715b8dd25')
    assert (engine.hash(algorithm=Algorithm.SHA256) == '23a3b7c14bf19645ef8e78c58f3cb3fa76149f22080d8c5f5bd5c5abd49a9ac2')

# Generated at 2022-06-14 00:07:24.696258
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method hash of class Cryptographic."""
    from mimesis.enums import Algorithm
    from mimesis.exceptions import NonEnumerableError

    sut = Cryptographic()
    for alg in Algorithm:
        assert len(sut.hash(alg)) == 64

    for unsupported in ['kenny', 123, True, None]:
        with pytest.raises(NonEnumerableError) as e:
            sut.hash(unsupported)

        assert e.type == NonEnumerableError
        assert e.value.enum == Algorithm

# Generated at 2022-06-14 00:07:26.451073
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    md5_hash = cr.hash(Algorithm.MD5)
    assert len(md5_hash) == 32


# Generated at 2022-06-14 00:07:35.805258
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    a = Cryptographic(seed=123456789)
    assert a.hash(algorithm=Algorithm.SHA512) == 'a9c8cb036cb2a7f19a108fca1c0a8dc0b97f51d89dfd478f9e8b8a2b3494a38a13e55d0f51dd97cbe20f50d928782411eafe3a3f0c3f1e0653b3d3e3f4b4e1d4'
    assert a.hash(algorithm=Algorithm.SHA256) == 'c6b85714b2c7d90826f51c9da8e53c69077b15a6b74d735f3e4e0b0bcb1f903e'
    assert a

# Generated at 2022-06-14 00:07:43.860263
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic(seed=123)
    result = c.hash(Algorithm.SHA256)
    expected = '0a0c8b2e2ef167d32a2ab34b3e8e0737fabcdf42c9f864d258e839a0f7f5d5e5'
    assert result == expected

# Generated at 2022-06-14 00:07:54.813399
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic('Cryptographic')
    assert cr.hash(Algorithm.SHA1) == 'fd937cbba8ea0cbe4e6e4d6b98fb6b4e6e14d71f'
    assert cr.hash(Algorithm.MD5) == 'e0d0b1f8b2c3f63d1327f1f9ca0c010bb3'
    assert cr.hash(Algorithm.SHA224) == '659b1fb1851c2b9ba3397e6fa681907422f7ebd15b6a4b1f9a96e7e'

# Generated at 2022-06-14 00:07:57.242239
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """The pseudo-random data provider Cryptographic method hash
    """
    expected = "72bde8c10a4224e60e136c20cc8fc7d0"
    actual = Cryptographic().hash(Algorithm.MD5)
    assert(actual == expected)

# Generated at 2022-06-14 00:07:58.619824
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash(Algorithm.SHA1)) == 40


# Generated at 2022-06-14 00:08:02.139542
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Test for hash() of class Cryptographic
    cryptographic = Cryptographic('en')
    algorithm = Algorithm.md5
    assert(len(cryptographic.hash(algorithm)) == 32)


# Generated at 2022-06-14 00:08:46.712193
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 64
    assert len(Cryptographic().hash(Algorithm.SHA256)) == 64
    assert len(Cryptographic().hash(Algorithm.SHA1)) == 40
    assert len(Cryptographic().hash(Algorithm.MD5)) == 32

# Generated at 2022-06-14 00:08:50.660438
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    Cryptographic.random_seed(5)
    assert Cryptographic().hash() == 'b4d4c4108ec848a7c6f9baf928c6a8b6'


# Generated at 2022-06-14 00:08:53.241033
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    _hash = provider.hash(Algorithm.SHA256)
    assert _hash


# Generated at 2022-06-14 00:08:59.963235
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic(seed=123)
    c.hash(Algorithm.BLAKE2B)
    # c.hash()  # TODO: Fix, raise NonEnumerableError
    c.hash(Algorithm.BLAKE2S)
    c.hash(Algorithm.MD5)
    c.hash(Algorithm.SHA1)
    c.hash(Algorithm.SHA224)
    c.hash(Algorithm.SHA256)
    c.hash(Algorithm.SHA384)
    c.hash(Algorithm.SHA512)



# Generated at 2022-06-14 00:09:02.332128
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    h = Cryptographic()

    assert h.hash() != None


# Generated at 2022-06-14 00:09:05.820330
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic.hash() == '4da4b4f4-041f-4a45-8ebc-520a11b4a2f2'

# Generated at 2022-06-14 00:09:08.795636
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert isinstance(c.hash(Algorithm.MD5), str), "It's not string"


# Generated at 2022-06-14 00:09:12.012628
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    CRYP = Cryptographic()

    res = CRYP.hash()
    assert type(res) is str
    assert len(res) != 7



# Generated at 2022-06-14 00:09:14.315952
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic(seed=1024)
    for i in range(20):
        hashes = cr.hash(Algorithm.SHA256)
        # Checking for len as the most basic assert for the function
        assert len(hashes) == 64
        print(hashes)
        print("\n")

# Generated at 2022-06-14 00:09:17.459050
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	crypto = Cryptographic()
	assert crypto.hash('md5') in hashlib.algorithms_available
	assert crypto.hash('sha1') in hashlib.algorithms_available
	assert crypto.hash('sha224') in hashlib.algorithms_available
	assert crypto.hash('sha256') in hashlib.algorithms_available
	assert crypto.hash('sha384') in hashlib.algorithms_available
	assert crypto.hash('sha512') in hashlib.algorithms_available
