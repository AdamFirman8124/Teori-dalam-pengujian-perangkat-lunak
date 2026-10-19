

# Generated at 2022-06-14 00:05:50.006977
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    print(crypto.hash())

# Generated at 2022-06-14 00:05:54.722444
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic('en')
    hashes = [c.hash(Algorithm.MD5) for i in range(100)]

    for val in hashes:
        assert len(val) == 32

# Generated at 2022-06-14 00:06:07.068221
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash(algorithm=Algorithm.SHA512) is not None
    assert crypto.hash(algorithm=Algorithm.SHA256) is not None
    assert crypto.hash(algorithm=Algorithm.MD5) is not None
    assert crypto.hash(algorithm=Algorithm.SHA1) is not None
    assert crypto.hash(algorithm=Algorithm.SHA384) is not None
    assert crypto.hash(algorithm=Algorithm.SHA3_512) is not None
    assert crypto.hash(algorithm=Algorithm.SHA3_384) is not None
    assert crypto.hash(algorithm=Algorithm.SHA3_256) is not None
    assert crypto.hash(algorithm=Algorithm.SHA3_224) is not None

# Generated at 2022-06-14 00:06:10.392126
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    data = Cryptographic().hash(Algorithm.SHA256)
    assert isinstance(data, str)
    assert data is not None
    assert len(data) == 64


# Generated at 2022-06-14 00:06:12.926837
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    print(c.hash())


# Generated at 2022-06-14 00:06:23.751568
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    # initialise seeds
    hash_values = [b'909e4a4f9e867c86', b'99c168e0e2fcf8d1', b'bfdc7d6f9cc6f8b3', b'abb27a84a6539b48', b'634a056b95fea9e4']
    for index,seed_value in enumerate(hash_values):
        c = Cryptographic(seed=seed_value)
        # check length
        assert len(c.hash(Algorithm.SHA1)) == 40
        # check seed
        assert c.hash(Algorithm.SHA1) == 'd1f7ea3c272bfd3db7abae2d35aeb7be9a767f52'
        # alternate index to make sure the change of index causes change

# Generated at 2022-06-14 00:06:30.411667
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    # Should returns MD5 by default
    assert provider.hash()
    # Should returns SHA1
    assert provider.hash(Algorithm.SHA1)
    # Should returns SHA256
    assert provider.hash(Algorithm.SHA256)
    # Should returns SHA384
    assert provider.hash(Algorithm.SHA384)
    # Should returns SHA512
    assert provider.hash(Algorithm.SHA512)
    # Should returns RIPEMD160
    assert provider.hash(Algorithm.RIPEMD160)



# Generated at 2022-06-14 00:06:32.432308
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash_value = Cryptographic().hash()
    assert hash_value is not None


# Generated at 2022-06-14 00:06:36.759190
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
  obj = Cryptographic()
  x = obj.hash()
  assert x == "a9ec436eaf28ae736d0c8e3dbf618a036bae85e0c32b8cc02319fd2b601e1713"

# Generated at 2022-06-14 00:06:41.319698
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    hash_result = crypto.hash(algorithm=Algorithm.MD5)
    print(hash_result)
    assert isinstance(hash_result, type(''))


# Generated at 2022-06-14 00:06:54.069935
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test the method hash of class Cryptographic."""
    cr = Cryptographic("test.TestCrypto")
    h = cr.hash(Algorithm.SHA3_384)
    assert len(h) == 96

# Generated at 2022-06-14 00:06:56.228181
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """ Unit test for method hash of class Cryptographic
    """
    crpt = Cryptographic('en')
    algo = Algorithm(crpt.random.choice([0, 1, 2, 3]))
    crpt.hash(algorithm=algo)

# Generated at 2022-06-14 00:07:00.693905
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
  for i in range(100):
    assert isinstance(Cryptographic().hash(), str)
    assert len(Cryptographic().hash()) == len(Cryptographic().hash())


# Generated at 2022-06-14 00:07:05.991699
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    t_result1 = Cryptographic.hash()
    t_result2 = Cryptographic.hash()
    t_result3 = Cryptographic.hash()
    assert(len(t_result1) == 40 and len(t_result2) == 40 and len(t_result3) == 40)
    assert(t_result1 != t_result2 and t_result1 != t_result3 and t_result2 != t_result3)


# Generated at 2022-06-14 00:07:06.683371
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    pass

# Generated at 2022-06-14 00:07:08.797588
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    h = c.hash()
    t = isinstance(h, str)
    assert t


# Generated at 2022-06-14 00:07:11.061851
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Test for method hash of class Cryptographic"""
    obj = Cryptographic()
    ret = obj.hash(algorithm=Algorithm.MD5)
    assert ret


# Generated at 2022-06-14 00:07:13.124648
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    for i in range(20):
        data = Cryptographic().hash()
        print(data)



# Generated at 2022-06-14 00:07:17.310305
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    Cryptographic_obj = Cryptographic()
    result = Cryptographic_obj.hash(Algorithm.SHA1)
    assert isinstance(result, str)


# Generated at 2022-06-14 00:07:20.234965
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash().__class__ is str


# Generated at 2022-06-14 00:07:45.732865
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    print(c.hash(Algorithm.MD5))
    print(c.hash(Algorithm.SHA1))
    print(c.hash(Algorithm.SHA224))
    print(c.hash(Algorithm.SHA256))
    print(c.hash(Algorithm.SHA384))
    print(c.hash(Algorithm.SHA512))

# Generated at 2022-06-14 00:07:49.091540
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 40
    assert len(Cryptographic().hash(Algorithm.MD5)) == 32


# Generated at 2022-06-14 00:07:54.819672
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    # Test for SHA512
    crypto.hash(Algorithm.SHA512)
    # Test for SHA
    crypto.hash(Algorithm.SHA)
    # For a non-supported algorithm, an exception will be raised
    crypto.hash('non-supported')

# Generated at 2022-06-14 00:07:57.239103
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    from mimesis.enums import Algorithm
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.cryptographic import Cryptographic
    from pytest import raises

    c = Cryptographic('en')
    for alg in Algorithm:  # noqa: C901
        h = c.hash(algorithm=alg)
        print(h)

    with raises(NonEnumerableError):
        c.hash(algorithm='test')

# Generated at 2022-06-14 00:07:59.410367
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic()
    data = provider.hash(Algorithm.MD5)
    assert data is not None


# Generated at 2022-06-14 00:08:01.905168
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    assert crypto.hash() != ""
    assert crypto.hash() != crypto.hash()


# Generated at 2022-06-14 00:08:07.179152
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    hash = Cryptographic(seed=123456789).hash(algorithm=Algorithm.SHA256)
    assert hash == 'a25bd228c46d67a1e3e52c810d0b2a60f3f1b3c3aacd6a2fad7aa43fcfc02b33'

# Generated at 2022-06-14 00:08:09.951985
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    generator = Cryptographic()
    string =  generator.hash(Algorithm.SHA512)
    assert len(string) == 128


# Generated at 2022-06-14 00:08:13.405081
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 64


# Generated at 2022-06-14 00:08:14.576943
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    obj = Cryptographic()
    result = obj.hash()
    assert isinstance(result, str) is True
    assert result

