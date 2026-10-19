

# Generated at 2022-06-14 00:06:35.593475
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert(Cryptographic().hash().isalnum())



# Generated at 2022-06-14 00:06:36.403588
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 40

# Generated at 2022-06-14 00:06:41.402138
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    
    if cr.hash(Algorithm.MD5) != '45e0a7c94a27f832db46eaf1ecb1e144':
        raise Exception("Incorrect hash")


# Generated at 2022-06-14 00:06:50.860726
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    
    c = Cryptographic(seed=42)
    
    # ######################
    # Test Algorithm.MD5 #
    # ######################
    
    # To change hashing algorithm, pass parameter algorithm
    # with needed value of the enum object mimesis.enums.Algorithm
    # Pass Seed and expected hash
    c._seed = 42
    assert c.hash(Algorithm.MD5) == "cf4d4c0d7b07e9b8ee7befcdef99e2ac"
    
    # ######################
    # Test Algorithm.SHA1 #
    # ######################
    
    # To change hashing algorithm, pass parameter algorithm
    # with needed value of the enum object mimesis.enums.Algorithm
    # Pass Seed and expected hash
    c._seed = 42


# Generated at 2022-06-14 00:06:52.034741
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash(): 
    assert Cryptographic().hash()

# Generated at 2022-06-14 00:06:54.857695
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert Cryptographic().hash() == '64b65f84e7f7092f8cc93f7d68fa0bb2e0e56c8b3d3d0ec9b886055b90fbca6e'


# Generated at 2022-06-14 00:06:59.513908
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    data = Cryptographic().hash(Algorithm.HAVAL256)
    assert len(data) == 64

# Generated at 2022-06-14 00:07:06.965374
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    try:
        # Declare an object of class Cryptographic
        c = Cryptographic()
        # Make a call to method hash of object c of class Cryptographic
        result = c.hash()
        # Check if result is of type str
        if(isinstance(result, str)):
            print("Test case passed")
        else:
            print("Test case failed")
            # The method hash should return a string, if otherwise, an error message will be printed
            print("Test case failed as method hash did not return a string")
    except:
        print("Test case failed")
        # An error message will be printed if exception occurs
        print("Exception occured, method hash of class Cryptographic could not be called")
    

# Generated at 2022-06-14 00:07:11.089940
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # check if it is hashing OK
    health = True
    for i in range(0, 10000):
        provider = Cryptographic()
        hash_str = provider.hash()
        if not isinstance(hash_str, str):
            health = False
        if len(hash_str) != 32:
            health = False
    assert health

# Generated at 2022-06-14 00:07:15.583557
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert(Cryptographic().hash(Algorithm.MD5) == '98d9b4375a76918f1ebbd29dcc8a0b29')
    assert(Cryptographic().hash(Algorithm.SHA1) == 'fec46f3d3162d2d3f4e9718c4a0ad065e4e7c94b')

# Generated at 2022-06-14 00:10:06.572866
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert isinstance(Cryptographic().hash(), str)

# Generated at 2022-06-14 00:10:18.049135
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    test_object = Cryptographic(seed = 1000)
    # object of class Algorithm from enum
    test_algorithm = Algorithm.SHA1
    test_result = test_object.hash(test_algorithm)

    # Assert that the result is in the correct format
    assert isinstance(test_result, str)
    assert test_result.isalnum()
    # Assert that the result is correct
    assert test_result == '19d8b99f09d7e289b0c5b744a0d6b31ec6dc2ba6'


# Generated at 2022-06-14 00:10:26.330297
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for method hash of class Cryptographic."""
    c = Cryptographic()
    def test(algorithm, hash_type):
        assert isinstance(c.hash(algorithm), hash_type)
    test(Algorithm.MD5, str)
    test(Algorithm.SHA1, str)
    test(Algorithm.SHA224, str)
    test(Algorithm.SHA256, str)
    test(Algorithm.SHA384, str)
    test(Algorithm.SHA512, str)
    test(Algorithm.BLAKE2B, str)
    test(Algorithm.BLAKE2S, str)
    test(Algorithm.MD4, str)



# Generated at 2022-06-14 00:10:31.941729
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic(seed=0)
    expected = "7e657c1f7a7d1a65b95d723429cce964"
    obtained = crypto.hash(algorithm=Algorithm.MD5)
    assert obtained == expected, "The hash value was wrong."

# Generated at 2022-06-14 00:10:43.883189
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.providers.cryptographic import Cryptographic
    crypto = Cryptographic()
    assert crypto.hash(Algorithm.MD5) == "5a1e05014683b00c3f4d17e4c46b3612"
    assert crypto.hash(Algorithm.SHA1) == "8184928f0d6d7c6e2eb187c8e57b0f9d71620b12"
    assert crypto.hash(Algorithm.SHA224) == "efeb8c89f3b9f58d08abda0aa6fcfdc96b2c2c1d0e8cceb4e88a7044"

# Generated at 2022-06-14 00:10:47.093917
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    Test for 'hash' method of class Cryptographic
    """
    assert Cryptographic().hash() != ''



# Generated at 2022-06-14 00:10:49.575713
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    result = provider.hash(Algorithm.MD5)
    assert isinstance(result, str)


# Generated at 2022-06-14 00:11:01.105685
# Unit test for method hash of class Cryptographic

# Generated at 2022-06-14 00:11:13.684354
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash(): # noqa: N802
    """
    Unit test for method hash of class Cryptographic.
    """
    Cryptographic.hash(Algorithm.SHA256)
    Cryptographic.hash(Algorithm.SHA512)
    Cryptographic.hash(Algorithm.BLAKE2s)
    Cryptographic.hash(Algorithm.BLAKE2b)
    Cryptographic.hash(Algorithm.MD5)
    Cryptographic.hash(Algorithm.SHA3_224)
    Cryptographic.hash(Algorithm.SHA3_256)
    Cryptographic.hash(Algorithm.SHA3_384)
    Cryptographic.hash(Algorithm.SHA3_512)
    Cryptographic.hash(Algorithm.SHA1)
    Cryptographic.hash(Algorithm.SHA224)
    Cryptographic.hash(Algorithm.SHA384)
    Cryptographic.hash

# Generated at 2022-06-14 00:11:19.253486
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    hash = crypto.hash(Algorithm.SHA256)
    assert(hash is not None)
    assert(len(hash) == len('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'))