

# Generated at 2022-06-14 00:06:00.112680
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """
    test_Cryptographic_hash()
    """
    random = Cryptographic(seed=1776)

    if random.hash(Algorithm.MD5) != '5b140815b7f5b6d5bc5d5bc5c5bc5d5b':
        print("test_Cryptographic_hash:  FAILED")
        return
    
    print("test_Cryptographic_hash:  PASSED")
    return


# Generated at 2022-06-14 00:06:04.689333
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic()
    hash = cr.hash(Algorithm.SHA224)
    print(hash)



# Generated at 2022-06-14 00:06:08.842969
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    crypto = Cryptographic()
    value = crypto.hash(algorithm=Algorithm.MD5)
    assert isinstance(value, str)
    assert len(value) == 32


# Generated at 2022-06-14 00:06:12.868122
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    c = Cryptographic()
    assert c.hash(Algorithm.MD5) != c.hash(Algorithm.MD5)


# Generated at 2022-06-14 00:06:15.818785
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    i = 0
    while 1:
        if i > 100:
            exit(0)
        print(Cryptographic(seed=None).hash())
        i = i + 1

# Generated at 2022-06-14 00:06:18.170823
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    cr = Cryptographic('en')
    for i in range(50):
        assert len(cr.hash()) == 64


# Generated at 2022-06-14 00:06:20.123708
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic('es')
    assert provider.hash(Algorithm.MD5) is not None

# Generated at 2022-06-14 00:06:21.289802
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    provider = Cryptographic('en')
    assert provider.hash()



# Generated at 2022-06-14 00:06:23.392783
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    """Get hash."""
    crypto = Cryptographic()
    print(crypto.hash())


# Generated at 2022-06-14 00:06:27.033454
# Unit test for method hash of class Cryptographic
def test_Cryptographic_hash():
    assert len(Cryptographic().hash()) == 64
    assert len(str(Cryptographic().uuid())) == 36
