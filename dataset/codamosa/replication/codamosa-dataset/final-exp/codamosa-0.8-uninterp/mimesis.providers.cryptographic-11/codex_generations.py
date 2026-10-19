

# Generated at 2022-06-14 00:05:50.876644
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    hash = cr.hash()
    assert isinstance(hash, str)


# Generated at 2022-06-14 00:05:54.130194
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic().hash()
    assert(len(hash)==40 and hash.isalnum())


# Generated at 2022-06-14 00:06:03.475868
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash(algorithm=Algorithm.SHA1)) == 40
    assert len(Cryptographic().hash(algorithm=Algorithm.SHA224)) == 56
    assert len(Cryptographic().hash(algorithm=Algorithm.SHA256)) == 64
    assert len(Cryptographic().hash(algorithm=Algorithm.SHA384)) == 96
    assert len(Cryptographic().hash(algorithm=Algorithm.SHA512)) == 128
    assert len(Cryptographic().hash(algorithm=Algorithm.MD5)) == 32


# Generated at 2022-06-14 00:06:04.498024
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash().encode()) == 32

# Generated at 2022-06-14 00:06:07.636750
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash(): # noqa: N802
    """Test for method hash of class Cryptographic."""
    hash = Cryptographic().hash()



# Generated at 2022-06-14 00:06:15.688785
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method :func:`~mimesis.providers.cryptographic.Cryptographic.hash`."""
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic
    c = Cryptographic()
    alg = Algorithm.MD5
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)
    assert c.hash(alg) == c.hash(alg)

# Generated at 2022-06-14 00:06:17.377093
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Arrange
    crypto = Cryptographic()

    # Act
    result = crypto.hash()

    # Assert
    assert result


# Generated at 2022-06-14 00:06:18.449114
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 40

# Generated at 2022-06-14 00:06:22.398967
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for method hash of class Cryptographic"""
    # Arrange
    c = Cryptographic()
    enc = Algorithm.SHA256

    # Act
    actual = c.hash(enc)

    # Assert
    assert actual is not None
    assert type(actual) == str

# Generated at 2022-06-14 00:06:26.970775
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test hash method."""
    
    crypto = Cryptographic(seed=42)
    assert crypto.hash().startswith('0')  # Only to check that it starts with 0
    

# Generated at 2022-06-14 00:06:39.910249
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert (Cryptographic().hash() == '00000000000000000000000000000000')



# Generated at 2022-06-14 00:06:44.425832
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 40
    assert len(Cryptographic().hash(Algorithm.SHA1)) == 40
    assert len(Cryptographic().hash(Algorithm.SHA224)) == 56
    assert len(Cryptographic().hash(Algorithm.SHA256)) == 64


# Generated at 2022-06-14 00:06:49.342591
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method Cryptographic.hash."""
    # Arrange
    # Act
    result = Cryptographic(seed=1337).hash(Algorithm.SHA256)
    # Assert
    assert result == 'e18fa71c042ac0e57ec7e36be1b45e3bc9bc4816d8c7fcee3a6d7ac2a0a8b7a0'

# Generated at 2022-06-14 00:06:55.823937
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for Cryptographic.hash()"""
    from mimesis.enums import Algorithm
    assert Cryptographic().hash()
    assert Cryptographic().hash(Algorithm.MD5)
    assert Cryptographic().hash(Algorithm.SHA1)
    assert Cryptographic().hash(Algorithm.SHA224)
    assert Cryptographic().hash(Algorithm.SHA256)
    assert Cryptographic().hash(Algorithm.SHA384)
    assert Cryptographic().hash(Algorithm.SHA512)



# Generated at 2022-06-14 00:07:02.868554
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    algoriths = Algorithm.__members__.items()
    for algorith in algoriths:
        print(Cryptographic().hash(algorith[1]))
    #print(Cryptographic().hash())



# Generated at 2022-06-14 00:07:10.019318
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic().hash(), str)
    assert isinstance(Cryptographic().hash(None), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA3_256), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA1), str)
    assert isinstance(Cryptographic().hash(Algorithm.SHA2_256), str)

# Generated at 2022-06-14 00:07:17.313210
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    import mimesis.enums
    c=Cryptographic()
    assert(len(c.hash())==128)
    assert(len(c.hash(mimesis.enums.Algorithm.MD5))==32)
    assert(len(c.hash(mimesis.enums.Algorithm.SHA1))==40)
    assert(len(c.hash(mimesis.enums.Algorithm.SHA224))==56)
    assert(len(c.hash(mimesis.enums.Algorithm.SHA256))==64)
    assert(len(c.hash(mimesis.enums.Algorithm.SHA384))==96)
    assert(len(c.hash(mimesis.enums.Algorithm.SHA512))==128)


# Generated at 2022-06-14 00:07:21.301939
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Unit test for method hash of class Cryptographic

    :return:
    """
    cryptographic = Cryptographic()
    algorithm = Algorithm.SHA256
    assert cryptographic.hash(algorithm) is not None

# Generated at 2022-06-14 00:07:25.590180
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash()
    assert crypto.hash(Algorithm.MD5)
    assert crypto.hash(Algorithm.SHA1)
    assert crypto.hash(Algorithm.SHA224)
    assert crypto.hash(Algorithm.SHA256)
    assert crypto.hash(Algorithm.SHA384)
    assert crypto.hash(Algorithm.SHA512)


# Generated at 2022-06-14 00:07:31.532521
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test method Cryptographic.hash."""
    crypto = Cryptographic(seed=12345)
    hash1 = crypto.hash()
    hash2 = crypto.hash()
    assert len(hash1) == 64
    assert len(hash2) == 64
    assert hash1 != hash2


# Generated at 2022-06-14 00:07:56.660443
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():

    hash = Cryptographic().hash()
    assert len(hash) == 64


# Generated at 2022-06-14 00:08:05.941409
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic('en')

    assert c.hash()
    assert c.hash(Algorithm.MD4)
    assert c.hash(Algorithm.MD5)
    assert c.hash(Algorithm.SHA1)
    assert c.hash(Algorithm.SHA224)
    assert c.hash(Algorithm.SHA256)
    assert c.hash(Algorithm.SHA384)
    assert c.hash(Algorithm.SHA512)
    assert c.hash(Algorithm.BLAKE2B)
    assert c.hash(Algorithm.BLAKE2S)


# Generated at 2022-06-14 00:08:06.972027
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    a = Cryptographic()

    assert isinstance(a.hash(), str)

# Generated at 2022-06-14 00:08:08.835868
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    ans = cr.hash()
    assert isinstance(ans, str)

# Generated at 2022-06-14 00:08:20.733136
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash(Algorithm.MD5) == '3e3ff166b107c5319d9c349a1a0e3fc3'
    assert c.hash(Algorithm.SHA1) == 'a871116d1deb0b44f4b43a4e4a4f0e4a0a33c06f'
    assert c.hash(Algorithm.SHA224) == '697bc19bc52fbb58e6c8a6129d2c9aa908f20982c8a513a6253543dd'

# Generated at 2022-06-14 00:08:22.100637
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	assert(Cryptographic().hash() not in ["No algorithm is specified"])


# Generated at 2022-06-14 00:08:25.635023
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash(Algorithm.MD5)
    assert Cryptographic().hash(Algorithm.SHA_224)
    assert Cryptographic().hash(Algorithm.SHA_256)
    assert Cryptographic().hash(Algorithm.SHA_384)
    assert Cryptographic().hash(Algorithm.SHA_512)


# Generated at 2022-06-14 00:08:30.899932
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
	from mimesis.enums import Algorithm
	algo = Algorithm.MD5
	c=Cryptographic()
	result=c.hash(algo)
	print(result)
	print(type(result))
#test_Cryptographic_hash()



# Generated at 2022-06-14 00:08:32.803404
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    algorithm = Algorithm.MD5
    assert isinstance(c.hash(algorithm), str)
    assert c.hash(algorithm) != c.hash(algorithm)


# Generated at 2022-06-14 00:08:37.036409
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypt = Cryptographic()
    output = crypt.hash()
    assert isinstance(output, str)
