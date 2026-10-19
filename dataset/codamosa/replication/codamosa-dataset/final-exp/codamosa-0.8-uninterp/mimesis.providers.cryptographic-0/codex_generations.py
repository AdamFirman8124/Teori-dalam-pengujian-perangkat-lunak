

# Generated at 2022-06-14 00:05:52.549385
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hashGen = Cryptographic()
    assert hashGen.hash() is not None

# Generated at 2022-06-14 00:05:59.317006
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    crypto = Cryptographic('TestClass')

    alg1 = crypto.hash(Algorithm.MD5)
    assert len(alg1) == 32
    assert isinstance(alg1, str)

    alg2 = crypto.hash(Algorithm.SHA1)
    assert len(alg2) == 40
    assert isinstance(alg2, str)

    alg3 = crypto.hash(Algorithm.SHA224)
    assert len(alg3) == 56
    assert isinstance(alg3, str)

    alg4 = crypto.hash(Algorithm.SHA256)
    assert len(alg4) == 64
    assert isinstance(alg4, str)

    alg5 = crypto.hash(Algorithm.SHA384)
    assert len(alg5) == 96

# Generated at 2022-06-14 00:06:04.904671
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    pass_str = crypto.hash(Algorithm.MD5)
    assert crypto.hash(Algorithm.MD5) == pass_str


# Generated at 2022-06-14 00:06:06.414733
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic().hash(Algorithm.SHA512)
    assert len(hash) == 128


# Generated at 2022-06-14 00:06:11.086157
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Arrange
    hash = "31c3ff3a5fbbb23a8d74897d0ad02acb"
    random = Cryptographic()
    # Act
    val = random.hash()
    # Assert
    assert val == hash


# Generated at 2022-06-14 00:06:13.986953
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert len(c.hash()) == 40, "The hash should be 40 characters long"



# Generated at 2022-06-14 00:06:18.502045
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    c = Cryptographic(seed=12345)
    assert c.hash(algorithm=Algorithm.MD5) == '0c0e97d8a82c09a9d228b74d2dc2a64a'

# Generated at 2022-06-14 00:06:21.244402
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    result = c.hash()
    assert result
    assert type(result) is str
    print('Passed test for method Cryptographic.hash')


# Generated at 2022-06-14 00:06:25.920097
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cryptographic = Cryptographic()
    algorithm = Algorithm()
    cryptographic.hash(algorithm.SHA224)
    cryptographic.hash(algorithm.SHA256)
    cryptographic.hash(algorithm.SHA384)
    cryptographic.hash(algorithm.SHA512)

# Generated at 2022-06-14 00:06:26.968834
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    assert type(provider.uuid()) is str

# Generated at 2022-06-14 00:06:47.182387
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    a = Cryptographic()
    assert a.hash().isalnum()


# Generated at 2022-06-14 00:06:49.066490
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Unit test for Cryptographic_hash()."""
    result = Cryptographic().hash()
    assert(len(result) == 32)


# Generated at 2022-06-14 00:06:50.826817
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert re.match(r'[a-fA-F0-9]+', Cryptographic().hash())

# Generated at 2022-06-14 00:06:55.302338
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic
    
    Cryp = Cryptographic()
    Cryp.hash(algorithm=Algorithm.MD5) == 'a1afc9c3b9e3483a96c4d4ef4b2e8a45'
    
    
    
    
    

# Generated at 2022-06-14 00:07:06.393114
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    _ = Cryptographic()
    assert _.hash(algorithm=Algorithm.MD5) == "18464a4e06bf9f9c329b9701c84f1b0a"
    assert _.hash(algorithm=Algorithm.SHA1) == "d6b7a6ad0a6f7b1e56a39d0e310cab232cdb7a03"
    assert _.hash(algorithm=Algorithm.SHA224) == "c10b55d94f40dcb7ac1a1377c5b5e5f04f5e5ee22affc6867d8bea1"

# Generated at 2022-06-14 00:07:11.062064
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash() in ['MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA3_224', 'SHA3_256', 'SHA3_384', 'SHA3_512', 'SHA512', 'BLAKE2b', 'BLAKE2s']


# Generated at 2022-06-14 00:07:13.469626
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypt = Cryptographic()
    print(crypt.hash())
    print(crypt.hash(Algorithm.BLAKE2S))


# Generated at 2022-06-14 00:07:22.306284
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Meta
    assert isinstance(Cryptographic.Meta.name, str)
    assert Cryptographic.Meta.name == 'cryptographic'

    # Test for invalid arguments
    assert Cryptographic().hash() != Cryptographic().hash()
    assert Cryptographic().hash(Algorithm.SHA256) == Cryptographic().hash(Algorithm.SHA256)
    assert Cryptographic().hash(Algorithm.SHA256) != Cryptographic().hash(Algorithm.SHA512)
    assert Cryptographic().hash(Algorithm.SHA256) != Cryptographic().hash(Algorithm.SHA1)
    assert Cryptographic().hash(Algorithm.SHA256) != Cryptographic().hash(Algorithm.MD5)


# Generated at 2022-06-14 00:07:25.849464
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # Arrange
    exp_hash = 'd32b4338ab4e4a4d9b84c0ddfdfaa5f7'
    alg = Algorithm.MD5

    # Act
    res_hash = Cryptographic().hash(alg)

    # Assert
    assert res_hash == exp_hash


# Generated at 2022-06-14 00:07:32.599674
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Use method "hash" of class "Cryptographic" to generate random hash,
    and compare results with previous ones.
    """
    # initialize Cryptographic provider
    crypto = Cryptographic()
    # generate random hash
    hash_hex = crypto.hash()
    # compare results
    assert hash_hex == 'c68aad0e64db6b0afe6eea787ecb72ffa1e8a0e7'

# Generated at 2022-06-14 00:13:28.594168
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    print_data = [c.hash() for i in range(10)]
    assert len(print_data) == 10

# Generated at 2022-06-14 00:13:32.676962
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic().hash(Algorithm.SHA512)
    assert isinstance(hash, str)


# Generated at 2022-06-14 00:13:36.443462
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    data = Cryptographic().hash(Algorithm.MD5)
    assert len(data) == 32
    assert isinstance(data, str)


# Generated at 2022-06-14 00:13:41.245324
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
  for item in Algorithm:
    print(item.name)
    print(Cryptographic.hash(item))
    #assert type(Cryptographic.hash(item)) is str


# Generated at 2022-06-14 00:13:54.124171
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.cryptographic import Cryptographic
    crypto = Cryptographic()
    # crypto.hash()  # Should work
    # crypto.hash(Algorithm.MD5)  # Should work
    # crypto.hash(Algorithm.SHA3_224)  # Should work
    # crypto.hash(Algorithm.SHA3_512)  # Should work
    # crypto.hash(Algorithm.SHA512)  # Should work
    # crypto.hash(Algorithm.SHA384)  # Should work
    # crypto.hash(Algorithm.SHA256)  # Should work
    # crypto.hash(Algorithm.SHA224)  # Should work
    # crypto.hash(Algorithm.SHA1)  # Should work


# Generated at 2022-06-14 00:13:55.583155
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic().hash(), str)


# Generated at 2022-06-14 00:14:03.850734
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """This function tests the Cryptographic class method hash."""
    obj=Cryptographic(seed=True)
    assert obj.hash() == 'ecabd2640d7de0d1d376a7c6b98dd8f7'
    assert obj.hash(algorithm=Algorithm.MD5) == 'ecabd2640d7de0d1d376a7c6b98dd8f7'


# Generated at 2022-06-14 00:14:08.572287
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    print("Expected hash : 567ba0b0d28e79044b02db8b79a6a7e2")
    print("Actual hash : " + crypto.hash(Algorithm.MD5))


# Generated at 2022-06-14 00:14:10.784954
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cryptographic = Cryptographic()
    x = cryptographic.hash()
    # actually we just check if the variable initialized properly
    assert x is not None


# Generated at 2022-06-14 00:14:24.357547
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cp = Cryptographic()