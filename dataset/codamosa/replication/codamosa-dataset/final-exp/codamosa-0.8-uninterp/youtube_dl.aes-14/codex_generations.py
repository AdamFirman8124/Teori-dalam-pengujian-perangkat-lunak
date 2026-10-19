

# Generated at 2022-06-14 15:07:37.005381
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key = bytes_to_intlist(compat_b64decode(b'KUzpLYwr1D7LbLACM6Zn0Q=='))
    cipher = bytes_to_intlist(compat_b64decode(b'5Wy/0Dv/iKj1FPN/c8WZf9/v4Y4hHfjKc8WZf9/v4Y4hHfjK'))

    class Counter(object):
        def __init__(self, key_stream_block):
            self.key_stream_block = key_stream_block
            self.next_counter_block = [0] * BLOCK_SIZE_BYTES
            self._update_next_counter_block()

        def next_value(self):
            next_counter_block

# Generated at 2022-06-14 15:07:44.318082
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    from .crypto import hex_to_bytes
    key = hex_to_bytes("2b7e151628aed2a6abf7158809cf4f3c")
    iv = hex_to_bytes("000102030405060708090A0B0C0D0E0F")
    data = hex_to_bytes("6bc1bee22e409f96e93d7e117393172a")

    result = aes_cbc_encrypt(data, key, iv)

    assert bytes_to_intlist(hex_to_bytes("7649abac8119b246cee98e9b12e9197d")) == result



# Generated at 2022-06-14 15:07:53.318208
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .utils import bytes_to_intlist, intlist_to_bytes

    class Counter:
        def __init__(self, start_val):
            self.val = start_val

        def next_value(self):
            x = self.val
            self.val = (self.val + 1) % 256
            return [x] * 16

    def test_decrypt(data, key, start_val, expected_plaintext):
        key = bytes_to_intlist(compat_b64decode(key))
        data = bytes_to_intlist(compat_b64decode(data))
        expected_plaintext = bytes_to_intlist(compat_b64decode(expected_plaintext))

        counter = Counter(start_val)

# Generated at 2022-06-14 15:08:03.288842
# Unit test for function aes_encrypt
def test_aes_encrypt():
    print("Testing aes_encrypt...")

# Generated at 2022-06-14 15:08:13.175761
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class IncrementalCounter(object):
        def __init__(self):
            self.c = [5] * BLOCK_SIZE_BYTES

        def next_value(self):
            self.c[0] += 1
            return self.c

    data = bytes_to_intlist(b"doodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoodoo")
    key = bytes_to_intlist(b"doodoodoodoodoodoodoodoodood")
    counter = IncrementalCounter()
    decrypted = aes_ctr_decrypt(data, key, counter)
    assert intlist_to_bytes(decrypted) == b"abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
test_aes_ctr_decrypt()



# Generated at 2022-06-14 15:08:22.510252
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    """
    unit test for function aes_cbc_decrypt
    """

# Generated at 2022-06-14 15:08:32.140677
# Unit test for function inc
def test_inc():
    err=[]
    if inc([1,1,1,1]) != [1,1,1,2]:
        err.append("inc([1,1,1,1]) != [1,1,1,2]")
    if inc([1,1,1,255]) != [1,1,2,0]:
        err.append("inc([1,1,1,255]) != [1,1,2,0]")
    if inc([1,1,255,255]) != [1,2,0,0]:
        err.append("inc([1,1,255,255]) != [1,2,0,0]")

# Generated at 2022-06-14 15:08:38.959971
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:08:48.326458
# Unit test for function aes_encrypt
def test_aes_encrypt():
    assert aes_encrypt([1, 2, 3, 4], []) == [1, 2, 3, 4]

    key = [0x10, 0x32, 0x54, 0x76, 0x98, 0xba, 0xdc, 0xfe, 0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef]
    data = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:08:54.392022
# Unit test for function inc
def test_inc():
    data = [1, 2, 3, 4, 5]
    assert inc(data) == [1, 2, 3, 4, 6]

    data = [1, 2, 3, 4, 255]
    assert inc(data) == [1, 2, 3, 5, 0]

    data = [1, 2, 3, 4, 0]
    assert inc(data) == [1, 2, 3, 4, 1]


# Generated at 2022-06-14 15:09:11.229709
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .counter import Counter
    from .aes_cbc_decrypt import aes_cbc_decrypt
    result = aes_ctr_decrypt(
        bytes_to_intlist(compat_b64decode(('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/'
                                           'kXX0KSvoOLSFQ==').encode())),
        bytes_to_intlist(compat_b64decode('YELLOW SUBMARINE'.encode())),
        Counter(intlist_to_bytes(bytes_to_intlist(compat_b64decode('AAAAAAAAAAAAAAAA'.encode()))))
    )
    print(intlist_to_bytes(result))
    assert hash

# Generated at 2022-06-14 15:09:22.637632
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    input = [0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a]
    #output = [0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a, 0x0a]

# Generated at 2022-06-14 15:09:33.820169
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:09:39.806728
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    data = 'Vn9XbptCpVZ1DOtFf5g5+nKqJ85YnhcS5PiqVF9Kk+4='
    password = 'hans'
    key_size = 16
    
    print(aes_decrypt_text(data, password, key_size))
test_aes_decrypt_text()


# Generated at 2022-06-14 15:09:51.280579
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    vector = [
        # cleartext, key, iv
        ('00112233445566778899aabbccddeeff', '000102030405060708090a0b0c0d0e0f', '101112131415161718191a1b1c1d1e1f',
         '69c4e0d86a7b0430d8cdb78070b4c55a'),
    ]
    for cleartext, key, iv, cipher in vector:
        key = bytes_to_intlist(compat_b64decode(key))
        iv = bytes_to_intlist(compat_b64decode(iv))
        data = bytes_to_intlist(compat_b64decode(cleartext))

# Generated at 2022-06-14 15:10:00.476516
# Unit test for function aes_decrypt
def test_aes_decrypt():
    pwd=compat_b64decode('74veF/OcYwY')
    data = [0] * 32
    iv = [0] * 32
    key = bytes_to_intlist(pwd)
    key = key[:32]
    print(key)
    print(data)
    testdata = aes_cbc_encrypt(data,key,iv)
    print(testdata)
    testdata = aes_cbc_decrypt(testdata,key,iv)
    print(intlist_to_bytes(testdata))
test_aes_decrypt()


# Generated at 2022-06-14 15:10:10.603967
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    plaintext = intlist_to_bytes(range(0, 32))
    key = intlist_to_bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    iv = intlist_to_bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Generated at 2022-06-14 15:10:23.357513
# Unit test for function aes_encrypt
def test_aes_encrypt():
    print("Testing aes_encrypt")
    data = bytes_to_intlist("3925841d02dc09fbdc118597196a0b32")
    expanded_key = bytes_to_intlist("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")
    assert aes_encrypt(data, expanded_key) == bytes_to_intlist("39ffedc5b8781f83749b8b437e2adf5a")
    data = bytes_to_intlist("09cf4f3c7da4397dbc9243dc323f7b15")

# Generated at 2022-06-14 15:10:32.541886
# Unit test for function aes_encrypt
def test_aes_encrypt():
    assert aes_encrypt(
        bytes_to_intlist(compat_b64decode('QP/xJstS2wqWzqLDq3D9pA==')),
        bytes_to_intlist(compat_b64decode('UHW8UvT35Tgy9sE6a/84Yfrggkvq3qyCxmBJw/Bpb8o='))
    ) == bytes_to_intlist(compat_b64decode('1+xJstS2wqWzqLDq3D9pA=='))



# Generated at 2022-06-14 15:10:44.309218
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import time
    import random
    import base64
    import binascii
    from pprint import pprint


# Generated at 2022-06-14 15:13:06.408446
# Unit test for function aes_decrypt
def test_aes_decrypt():
    b64key = "CFE188018F5EB6A5A55D66A6E5E5A5A6"
    b64key = compat_b64decode(b64key)
    key = bytes_to_intlist(b64key)

    b64ciphertext = "0C2F9B2DDD67AE6E6679C91FBDC6BA5F"
    b64ciphertext = compat_b64decode(b64ciphertext)
    ciphertext = bytes_to_intlist(b64ciphertext)
    
    b64output = "00000000000000000000000000000001"
    b64output = compat_b64decode(b64output)
    output = bytes_to_intlist(b64output)


# Generated at 2022-06-14 15:13:18.372697
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .crypto import aes_cbc_encrypt
    def check():
        key = bytes_to_intlist('140b41b22a29beb4061bda66b6747e14')
        iv = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb28')
        cipher = bytes_to_intlist('28a226d160dad07883d04e008a7897ee\
2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
        plain = bytes_to_intlist('Basic CBC mode encryption needs padding.')

        assert cipher == aes_cbc_encrypt(plain, key, iv)
        assert plain == aes_

# Generated at 2022-06-14 15:13:27.445021
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:13:38.800259
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [143, 194, 34, 208, 145, 203, 230, 143, 177, 246, 97, 206, 145, 92, 255, 84]
    iv = [103, 35, 148, 239, 76, 213, 47, 118, 255, 222, 123, 176, 106, 134, 98, 92]
    cipher = [232, 128, 123, 175, 137, 78, 168, 139, 31, 184, 18, 220, 17, 185, 39, 156, 214, 31, 217, 208, 90, 227, 152, 160, 49, 228, 245, 17, 135,
              115, 27, 229, 195, 157, 113, 111, 222, 28, 49, 150, 113, 78, 4, 134, 95, 75, 224, 118, 95, 49, 123, 85, 95, 229, 172, 53, 35, 98]

    data

# Generated at 2022-06-14 15:13:48.577043
# Unit test for function aes_decrypt
def test_aes_decrypt():
    # key:
    # 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c
    # Data:
    # 6b c1 be e2 2e 40 9f 96 e9 3d 7e 11 73 93 17 2a
    # 49 00 3c a0 7d 36 a1 ef e0 8f 07 ad d4 1a 31 c7
    # 85 10 81 3f 5d fc ac 67 28 3d 7d 08 0f a9 5e e0
    # c3 7c 8f f3 a9 7a 11 6e 64 40 c0 37 3f e8 59 c7
    
    data = bytes_to_intlist('6b c1 be e2 2e 40 9f 96 e9 3d 7e 11 73 93 17 2a')
    data += bytes_to_int

# Generated at 2022-06-14 15:13:59.206595
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .utils import bytes_to_intlist, intlist_to_bytes
    import binascii

    iv = bytes_to_intlist(b'\x00' * BLOCK_SIZE_BYTES)
    key = bytes_to_intlist(b'\x00' * BLOCK_SIZE_BYTES)
    data = bytes_to_intlist(binascii.unhexlify('66e94bd4ef8a2c3b884cfa59ca342b2e'))

    decrypted_data = aes_cbc_decrypt(data, key, iv)
    assert intlist_to_bytes(decrypted_data).decode('ascii') == '{"lr'

    iv = bytes_to_intlist(b'\x00' * BLOCK_SIZE_BYTES)

# Generated at 2022-06-14 15:14:07.987345
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist(b'test')
    data = data + [0] * (BLOCK_SIZE_BYTES - len(data))
    key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    iv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    decrypted = aes_cbc_decrypt(data,key,iv)
    print(decrypted)
    #assert decrypted == [116, 101, 115, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Generated at 2022-06-14 15:14:21.067987
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    from .utils import compat_b64decode
    from .sjcl import SJCL
    from .sjcl import SJCL_CONFIG
    from .utils import bytes_to_intlist
    from .utils import intlist_to_bytes
    from .utils import hex_to_bytes
    from .utils import bytes_to_hex


# Generated at 2022-06-14 15:14:28.298215
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key='140b41b22a29beb4061bda66b6747e14'.decode('hex')
    iv=  '4ca00ff4c898d61e1edbf1800618fb28'.decode('hex')
    data='28a226d160dad07883d04e008a7897ee'.decode('hex')
    output='5b68629feb8606f9a6667670b75b38a5'.decode('hex')
    assert aes_cbc_encrypt(data,key,iv) == output



# Generated at 2022-06-14 15:14:40.115572
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    cipher = intlist_to_bytes(aes_cbc_encrypt(b"AuthHeader",
        [i for i in range(16)], [i for i in range(16)]))
    key = [
        0x59, 0x69, 0x8e, 0x8b, 0x08, 0x52, 0x2f, 0x0d,
        0x77, 0x7d, 0x13, 0x0e, 0xf3, 0x2e, 0x07, 0xf0
    ]

# Generated at 2022-06-14 15:14:57.086457
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode("KjKuV0E2TnI2V2MwTkhTUE1YTnkzcDJHRXpkMGZuOTVnL3Bqc3I3ZWE1eGpKRGNCTlRxRVFxR2l2QVVrNWZwRw=="))

# Generated at 2022-06-14 15:15:07.317651
# Unit test for function key_expansion
def test_key_expansion():
    import unittest
    import struct

# Generated at 2022-06-14 15:15:14.962904
# Unit test for function key_expansion
def test_key_expansion():
    # Test keys taken from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf Appendix F.5
    key1 = bytes_to_intlist(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')

# Generated at 2022-06-14 15:15:20.753027
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:29.566472
# Unit test for function key_expansion
def test_key_expansion():
    # Key expansion test vectors from https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf
    data = bytes_to_intlist(compat_b64decode(b'SmFpVU1NOE1iMVV0ZWtGYWN0'))
    result = key_expansion(data)
    expected = bytes_to_intlist(compat_b64decode(b'SmFpVU1NOE1iMVV0ZWtGYWN0Q3o5QWZFa1NxOVNkZjN5VXR5RTVrRVF0dz09'))
    assert result == expected, 'Key expansion failed (aes128)'

# Generated at 2022-06-14 15:15:39.003636
# Unit test for function key_expansion
def test_key_expansion():
    for key_length in (16, 24, 32):
        for key in (b'\x00', b'\x00\x01', b'\x00\x01\x02', b'\x00\x01\x02\x03'):
            key = bytes_to_intlist(key) * (key_length // 4)
            assert len(key) == key_length
            aes_expanded_key = key_expansion(key)
            assert len(aes_expanded_key) == (key_length // 4 + 7) * BLOCK_SIZE_BYTES



# Generated at 2022-06-14 15:15:50.554994
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:00.494093
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128
    assert bytes_to_intlist(compat_b64decode('Dh9yhDrf/rq3FFL/Ypd+BUYZRJnX9/Ds'))\
        == key_expansion(bytes_to_intlist(b'secretKeyBYTES'))
    # AES-192
    assert bytes_to_intlist(compat_b64decode('Dh9yhDrf/rq3FFL/Ypd+BUYZRJnX9/Ds'))\
        == key_expansion(bytes_to_intlist(b'secretKeyBYTES'))
    # AES-256

# Generated at 2022-06-14 15:16:11.784954
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:23.816742
# Unit test for function key_expansion
def test_key_expansion():
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data = bytes_to_intlist(data)
    data = key_expansion(data)

# Generated at 2022-06-14 15:16:36.344568
# Unit test for function key_expansion
def test_key_expansion():

    key1 = bytes_to_intlist(compat_b64decode('CY9rzUYh03PK3k6DJie09g=='))
    exp_key1 = bytes_to_intlist(compat_b64decode('CY9rzUYh03PK3k6DJie09gZCfvkBJt7bDVyK+znM0Cx7jXbG8GK9fVvT7kVxi3d0'))
    key2 = bytes_to_intlist(compat_b64decode('ZmFsYWRvLnRlc3RnZXNzaW9u'))

# Generated at 2022-06-14 15:16:44.953226
# Unit test for function key_expansion
def test_key_expansion():
    sampleKey = bytes_to_intlist(compat_b64decode("Mk+oQJ7ZrrRfrF9D7zyx+Q=="))
    sampleExpandedKey = bytes_to_intlist(compat_b64decode("NX9zobBxN/TUIg7hYwwYH2V7r09rWOxmV7GZAsFm9f7xuRIdLOIyLlJGAGfOvck8"))
    key = key_expansion(sampleKey)
    assert key == sampleExpandedKey, "Key expansion function failed"
    return True



# Generated at 2022-06-14 15:16:56.881247
# Unit test for function key_expansion
def test_key_expansion():
    import unittest
    class KeyExpansionTestCase(unittest.TestCase):
        def test_a(self):
            data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
                    0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:17:06.108252
# Unit test for function key_expansion
def test_key_expansion():
    # From http://www.inconteam.com/software-development/41-encryption/55-aes-test-vectors#aes-test-vectors
    print('test_key_expansion')
    test_key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:17:18.289981
# Unit test for function key_expansion
def test_key_expansion():
    assert bytes_to_intlist(compat_b64decode(b'wxWZeevM90pX/4E4j+eH5A==')) == key_expansion(bytes_to_intlist(compat_b64decode(b'Kp8GigM56+vq3Kq7wg==')))