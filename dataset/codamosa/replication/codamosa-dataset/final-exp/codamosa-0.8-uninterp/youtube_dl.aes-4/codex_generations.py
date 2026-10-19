

# Generated at 2022-06-14 15:07:48.109292
# Unit test for function aes_encrypt
def test_aes_encrypt():

    # Test that aes_encrypt returns the expected output from the NIST the test vectors
    with open("tests/vectors/nist_ciphertext.txt", "r") as f:
        nist_cipher_text = compat_b64decode(f.read())
        nist_key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:07:55.557001
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    import os
    from .aes import aes_decrypt_text as test_aes_decrypt_text

    plaintext = 'Hello world'
    password = 'password123'
    key_size_bytes = 32


# Generated at 2022-06-14 15:08:04.491316
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import binascii
    from .counter import AESCounter

    data = bytes_to_intlist(
        compat_b64decode(
            'r1hEKbZlV6UoM6pO4Oa+I6UuQ7UfJ1Ro79V7GRcInL8='
        )
    )
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    counter = AESCounter.from_nonce_and_counter(b'\x00' * 8, 0)
    decrypted_data = aes_ctr_decrypt(data, key, counter)
    assert intlist_to_bytes(decrypted_data) == b'Yo, VIP Let\'s kick it Ice, Ice, baby Ice, Ice, baby '



# Generated at 2022-06-14 15:08:14.028112
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .aes_counter import AESCounter
    from .utils import bytes_to_intlist, intlist_to_bytes

    counter = AESCounter(intlist_to_bytes(bytes_to_intlist('666f6f62')))
    key = intlist_to_bytes(bytes_to_intlist('12345678901234567890123456789012'))
    data = compat_b64decode('nxoMNVy5wby2QW1a5gvZGk9peq7z8YWY+b7v6Cgx7pM=')
    res = b'aj\xcb\xe9\x16\xc8\x00\x18\xeb\x03\x8f\xcd!\x93\xb3'
    assert res == intlist_

# Generated at 2022-06-14 15:08:18.999712
# Unit test for function aes_decrypt_text

# Generated at 2022-06-14 15:08:27.489254
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    print('Test aes_ctr_decrypt')
    from .aes import next_counter_value
    class Counter(object):
        def __init__(self, seed):
            self.seed = seed

        def next_value(self):
            self.seed = next_counter_value(self.seed)
            return self.seed

    key = bytes_to_intlist('YELLOW SUBMARINE')
    data = bytes_to_intlist(compat_b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='))
    counter = Counter(bytes_to_intlist('\x00' * BLOCK_SIZE_BYTES))
    dec

# Generated at 2022-06-14 15:08:35.908457
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """
    Unit test of function aes_decrypt_text
    """
    import os
    import sys

    curdir = os.path.dirname(__file__)
    sys.path.append(os.path.join(curdir, '../..'))
    import vuvuzela
    import test_utilities as test

    enc = vuvuzela.cipher.AES.encrypt_text
    dec = vuvuzela.cipher.AES.decrypt_text

    for key_size_bytes in [16, 24, 32]:
        for plaintext in test.plaintexts:
            for password in test.passwords:
                plaintext = plaintext.encode('utf-8')
                password = password.encode('utf-8')


# Generated at 2022-06-14 15:08:46.112449
# Unit test for function key_expansion

# Generated at 2022-06-14 15:08:57.019837
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """
    Unit test for aes_decrypt_text to verify that it works with the examples given at
    https://developers.google.com/youtube/v3/live/docs/authentication#creating-a-private-key
    """
    encrypted_private_key = b'CiAJKAeRxiZDItLjw7fpxN6AuG7VF2gjv/PXoFlzc/Z7Y+Mwj0+YuWjOqDSKuL0U'
    private_key_password = b'sample'

    decrypted_key = aes_decrypt_text(encrypted_private_key, private_key_password, 32)

# Generated at 2022-06-14 15:09:08.908681
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    key_size_bytes = 16
    password = '9%5j!n5<5W7,8*v'
    ciphertext = 'MnxV7h8/vX9V7/oi1aZu1h8Q29v/vV7rlqb3Nzc8W7'
    plaintext = 'The Magic Words are Squeamish Ossifrage'
    assert aes_decrypt_text(ciphertext, password, key_size_bytes) == plaintext
    key_size_bytes = 24
    password = '9%5j!n5<5W7,8*v'

# Generated at 2022-06-14 15:09:20.210075
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    cipher = bytes_to_intlist(compat_b64decode(b"L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="))
    key    = bytes_to_intlist(compat_b64decode(b"YELLOW SUBMARINE"))
    nonce  = bytes_to_intlist(b"\x00\x00\x00\x00\x00\x00\x00\x00")

    class Counter():
        def __init__(self, nonce):
            self.nonce = nonce

        def next_value(self):
            counter = self.nonce + [0, 0, 0, 0]

# Generated at 2022-06-14 15:09:21.483745
# Unit test for function inc
def test_inc():
    test_data = [0x00, 0x00, 0x00, 0x00]
    res_data = inc(test_data)
    print("Inc test: ", test_data, res_data)


# Generated at 2022-06-14 15:09:32.672728
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = "140b41b22a29beb4061bda66b6747e14".decode("hex")
    iv = "4ca00ff4c898d61e1edbf1800618fb28".decode("hex")
    data = "28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("hex")
    result = "28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("hex")


# Generated at 2022-06-14 15:09:38.697736
# Unit test for function aes_encrypt
def test_aes_encrypt():
    cipherkey = bytes_to_intlist(compat_b64decode(b"kPH+bIxk5D2deZiIxcaaaA=="))
    iv = bytes_to_intlist(compat_b64decode(b"2gfM7KTuJZP3k0zVPzqEew=="))
    data = bytes_to_intlist(compat_b64decode(b"I0HpZpzwgEw0qWqLl+rB1c="))
    encrypted_data = aes_encrypt(data, cipherkey)
    assert encrypted_data == iv



# Generated at 2022-06-14 15:09:49.095460
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
  enc_b64_str = "yRDJ5Ddajp5S5O+vS6JY2Q==|3SBWO4ok4v4eRitMItCU9g==|W0/fvDsvYOw6HO/JgW+2xQ=="
  password = "g9N6nb2QsHV"
  key_size_bytes = 32
  dec_text = aes_decrypt_text(enc_b64_str, password, key_size_bytes)
  expected = "This is a demonstration!"
  print (dec_text == expected)

test_aes_decrypt_text()


# Generated at 2022-06-14 15:09:57.409014
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = intlist_to_bytes([0x6b, 0xc1, 0xbe, 0xe2, 0x2e, 0x40, 0x9f, 0x96, 0xe9, 0x3d, 0x7e, 0x11, 0x73, 0x93, 0x17, 0x2a])
    key = intlist_to_bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])

# Generated at 2022-06-14 15:10:08.544217
# Unit test for function key_expansion
def test_key_expansion():
    import random
    random.seed(12345)

# Generated at 2022-06-14 15:10:21.017864
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    # cryptotext taken from: https://tools.ietf.org/html/rfc3686#section-2.3
    key = bytes_to_intlist(b'\xAE\x68\x52\xF8\x12\x10\x67\xCC\x4B\xF7\xA5\x76\x55\x77\xF3\x9E')
    data = b'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
    data = bytes_to_intlist(compat_b64decode(data))

# Generated at 2022-06-14 15:10:33.361216
# Unit test for function key_expansion
def test_key_expansion():
    def string_to_intlist(s):
        return bytes_to_intlist(s.encode('ascii'))

    expected = bytes_to_intlist(compat_b64decode(
        '+lYGiJgHh1N/IjNzrN+yHcJTbGAxT1Mvdr4XhWtWBH4=', "'"))

    assert key_expansion(string_to_intlist(
        '00010203050607080A0B0C0D0F101112')) == expected


# Generated at 2022-06-14 15:10:38.836877
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(bytearray(b'Sixteen byte key'))
    iv = bytes_to_intlist(bytearray(b'Sixteen byte IV'))
    cleartext = bytes_to_intlist(bytearray(b'Fourteen bytes long'))

    enc = aes_cbc_encrypt(cleartext, key, iv)
    dec = aes_cbc_decrypt(enc, key, iv)
    assert(cleartext == dec)



# Generated at 2022-06-14 15:10:52.624040
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes_list = [16, 24, 32]
    key_list = [
        [143, 194, 34, 208, 145, 203, 230, 143, 177, 246, 97, 206, 145, 92, 255, 84],
        [231, 43, 118, 206, 55, 39, 22, 63, 104, 174, 108, 222, 181, 47, 213, 106, 6, 85, 194, 244, 7, 38, 166, 154, 200, 245, 127, 19, 212, 146, 109],
        [41, 163, 31, 76, 124, 142, 22, 191, 84, 231, 232, 175, 74, 198, 73, 53, 88, 124, 102, 17, 138, 231, 110, 53, 209, 65, 156, 113, 24, 24, 168]
    ]

# Generated at 2022-06-14 15:10:55.371281
# Unit test for function inc
def test_inc():
    vector = [1, 255, 0, 0]
    assert inc(vector) == [2, 0, 0, 0]
    vector = [1, 255, 255, 255]
    assert inc(vector) == [2, 0, 0, 0]



# Generated at 2022-06-14 15:11:03.847416
# Unit test for function inc
def test_inc():
    data = [0x01, 0x00, 0x00, 0x00]
    assert inc(data) == [0x02, 0x00, 0x00, 0x00]
    data = [0x20, 0x00, 0x00, 0x00]
    assert inc(data) == [0x20, 0x00, 0x00, 0x01]
    data = [0x00, 0x01, 0x01, 0x01]
    assert inc(data) == [0x00, 0x01, 0x01, 0x02]
    data = [0xff, 0xff, 0xff, 0xff]
    assert inc(data) == [0x00, 0x00, 0x00, 0x00]
    print('Test passed')


# Generated at 2022-06-14 15:11:16.405411
# Unit test for function key_expansion

# Generated at 2022-06-14 15:11:20.100866
# Unit test for function inc
def test_inc():
    assert inc([255, 255, 255, 255]) == [0, 0, 0, 0]
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([0, 0, 0, 1]) == [0, 0, 0, 2]
    assert inc([1, 2, 3, 4]) == [1, 2, 3, 5]
    assert inc([1, 2, 3, 255]) == [1, 2, 4, 0]
    assert inc([1, 255, 255, 255]) == [2, 0, 0, 0]



# Generated at 2022-06-14 15:11:29.460528
# Unit test for function inc
def test_inc():
    data = [0] * 16
    data = inc(data)
    assert data == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = inc(data)
    assert data == [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = inc(data)
    assert data == [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = inc(data)
    assert data == [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:11:30.595166
# Unit test for function inc
def test_inc():
    x = [0, 0, 0, 0]
    for i in range(16):
        x = inc(x)
        print(x)

#test_inc()


# Generated at 2022-06-14 15:11:31.983345
# Unit test for function inc
def test_inc():
    data = [0x0, 0xf, 0xff]
    result = [0x1, 0x10, 0x1]
    for i in range(3):
        assert(inc(data[i]) == result[i])



# Generated at 2022-06-14 15:11:33.416360
# Unit test for function inc
def test_inc():
    expected = [1,0,0,0]
    actual = [0,255,255,255]
    actual = inc(actual)
    assert expected == actual



# Generated at 2022-06-14 15:11:36.162667
# Unit test for function inc
def test_inc():
    data = [0, 0, 0, 0]
    data = inc(data)
    assert data == [0, 0, 0, 1]

    data = [0, 0, 0, 255]
    data = inc(data)
    assert data == [0, 0, 1, 0]

    data = [0, 255, 255, 255]
    data = inc(data)
    assert data == [1, 0, 0, 0]



# Generated at 2022-06-14 15:11:48.612826
# Unit test for function key_expansion
def test_key_expansion():
    data = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:00.844272
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:12:13.382119
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:22.189954
# Unit test for function key_expansion
def test_key_expansion():
    # Example from https://csrc.nist.gov/publications/detail/fips/197/final
    data = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:33.074990
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:41.855057
# Unit test for function key_expansion
def test_key_expansion():
    assert bytes_to_intlist(compat_b64decode('KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY=')) == key_expansion(
        bytes_to_intlist(
            compat_b64decode('NkJCQzIzQTI2QTQ0RjdFRjlEODMyRjQ2Q0JEQ0RFNkU3NkM3OTI3NTg4Mw==')))



# Generated at 2022-06-14 15:12:52.976000
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist("2b7e151628aed2a6abf7158809cf4f3c")

# Generated at 2022-06-14 15:13:00.745274
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode("4sTws4sTws4sTws4sTws4sTws4sTws+"))
    assert intlist_to_bytes(key_expansion(data)) == compat_b64decode("4sTws4sTws4sTws4sTws4sTws4sTws+H7VuwR8jL7VuwR8jL7VuwR8jL7VuwR8jL7VuwR8j")

    data = bytes_to_intlist(compat_b64decode("4sTws4sTws4sTws4sTws4sTws4sTw4"))
    assert intlist_to_bytes(key_expansion(data)) == compat_

# Generated at 2022-06-14 15:13:11.544237
# Unit test for function key_expansion
def test_key_expansion():
    # test 128-bit
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
    key = key_expansion(key)
    assert len(key) == 176

# Generated at 2022-06-14 15:13:22.282477
# Unit test for function key_expansion
def test_key_expansion():
    key = list(range(16))
    expected = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63
    ]
    assert expected == key_expansion(key)

    key = list(range(24))

# Generated at 2022-06-14 15:13:37.256310
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:13:47.338866
# Unit test for function key_expansion
def test_key_expansion():
    # test vector from:
    # http://www.inconteam.com/software-development/41-encryption/55-aes-test-vectors
    key = bytes_to_intlist(compat_b64decode(b'GZy6sIZ6wl9NJOKB-jnmVQ'))
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:13:54.691084
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:04.801690
# Unit test for function key_expansion
def test_key_expansion():
    # test vector from: https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    expanded_key = key_expansion(key)
    assert hexlist_to_bytestr(expanded_key[:16]) == '2b7e151628aed2a6abf7158809cf4f3c'

# Generated at 2022-06-14 15:14:11.656100
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('L7uE4o/p7Jm+g/8djMdHmI+b/qXuq/0/0+DkfT/BHNt/w=='))
    expected = bytes_to_intlist(compat_b64decode('L7uE4o/p7Jm+g/8djMdHmI+b/qXuq/0/0+DkfT/BHNt/w==SdAWKFLlkrgYM9bO/zo1WDHmDI6itvf6'))
    assert key_expansion(key) == expected



# Generated at 2022-06-14 15:14:24.533047
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:14:37.233182
# Unit test for function key_expansion
def test_key_expansion():
    test_key = [
        0x02, 0x01, 0x01, 0x03,
        0x03, 0x02, 0x01, 0x01,
        0x01, 0x03, 0x02, 0x01,
        0x01, 0x01, 0x03, 0x02
    ]

# Generated at 2022-06-14 15:14:49.450029
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode("63Cf2cfd5b5bf410"))
    decrypted_data = key_expansion(data)
    assert len(decrypted_data) == 176

# Generated at 2022-06-14 15:15:00.079727
# Unit test for function key_expansion
def test_key_expansion():
    import struct
    # Test vector from https://csrc.nist.gov/csrc/media/publications/fips/198/2/fips-198-2.pdf
    test = struct.pack("<32B", 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f)
    actual = key

# Generated at 2022-06-14 15:15:10.142000
# Unit test for function key_expansion
def test_key_expansion():
    key_size = 16
    key_string = "140b41b22a29beb4061bda66b6747e14"
    key_data = bytes_to_intlist(compat_b64decode(key_string))
    key_data = key_data[:key_size]

# Generated at 2022-06-14 15:15:24.577451
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test function key_expansion

    Test vectors are from: http://csrc.nist.gov/groups/STM/cavp/documents/aes/KAT_AES.zip
    """
    def test_vector(key, expanded_key):
        assert key_expansion(bytes_to_intlist(compat_b64decode(key))) == bytes_to_intlist(compat_b64decode(expanded_key))


# Generated at 2022-06-14 15:15:32.680278
# Unit test for function key_expansion
def test_key_expansion():
    def get_expected(key, iteration):
        key_bytes = intlist_to_bytes(key)
        iv_bytes = intlist_to_bytes([0] * BLOCK_SIZE_BYTES)
        ctr = AESCTR(key_bytes, iv_bytes)
        ctr.next_value()
        return ctr.next_value()[:]

    # key: 16 Byte, w: 44
    key1 = bytes_to_intlist(compat_b64decode(b'WZMwIj/eV1+/BX0t'))
    expanded_key1 = key_expansion(key1)
    assert len(expanded_key1) == 44 * 4
    for i in range(44):
        assert expanded_key1[i * 4: i * 4 + 4] == get_

# Generated at 2022-06-14 15:15:45.151221
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:55.413539
# Unit test for function key_expansion
def test_key_expansion():
    key_16 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:16:03.329265
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:09.432347
# Unit test for function key_expansion
def test_key_expansion():
    assert bytes_to_intlist(compat_b64decode("zAv0ZYaYWjO20iy7/mGcxw==")) == key_expansion(bytes_to_intlist("00000000000000000000000000000000".encode("utf-8"))), "16-Byte"
    assert bytes_to_intlist(compat_b64decode("zAv0ZYaYWjO20iy7/mGcx8SPvj+wg3D3BSDB3zIW9Y=")) == key_expansion(bytes_to_intlist("000000000000000000000000000000000000000000000000".encode("utf-8"))), "24-Byte"

# Generated at 2022-06-14 15:16:13.718634
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test for function key_expansion
    """
    key_size_bytes = 32
    key = intlist_to_bytes(bytes_to_intlist(b"YELLOW SUBMARINE"))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 240
    assert expanded_key[-16:] == intlist_to_bytes([0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00,
                                               0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff])


# Generated at 2022-06-14 15:16:24.871735
# Unit test for function key_expansion
def test_key_expansion():
    """
    Tests for function key_expansion
    """
    data = [
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
        0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f
    ]

# Generated at 2022-06-14 15:16:25.475906
# Unit test for function key_expansion
def test_key_expansion():
    return



# Generated at 2022-06-14 15:16:31.264601
# Unit test for function key_expansion
def test_key_expansion():
    res = key_expansion(bytes_to_intlist(compat_b64decode('Qk/cKPoX9QW8wbUnh4z4i99CkWCdKG+3qSbS1S/iHqI=')))

# Generated at 2022-06-14 15:16:47.501809
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('CvO8C7+Kj9XBTGJMX0q+rA=='))
    key_expanded = bytes_to_intlist(compat_b64decode('CvO8C7+Kj9XBTGJMX0q+rK4q8DpJfX9/gBijpCmvx8/eWd2NAfYwIwLOfvZ8GjWgAyX9OtiibPxzOgj8FxcBdI1wMulYg=='))
    assert(key_expanded == key_expansion(key))
## End of unit test for function key_expansion



# Generated at 2022-06-14 15:16:56.230046
# Unit test for function key_expansion
def test_key_expansion():
    import os
    key = bytes_to_intlist(os.urandom(16))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 176
    key = bytes_to_intlist(os.urandom(24))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 208
    key = bytes_to_intlist(os.urandom(32))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 240



# Generated at 2022-06-14 15:17:05.544510
# Unit test for function key_expansion
def test_key_expansion():
    """
    Unit test for function key_expansion

    @returns {bool} Unit test passed succesfully
    """
    key_16 = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')

# Generated at 2022-06-14 15:17:17.749723
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128
    assert(intlist_to_bytes(key_expansion([1]*16)) == compat_b64decode("4FE4B7B2DC4AEF8DD83D1E65DB9BBE9F75B0D79E8BBF5E5018CDD1E3F26D2DEC"))
    # AES-192
    assert(intlist_to_bytes(key_expansion([1]*24)) == compat_b64decode("4FE4B7B2DC4AEF8DD83D1E65DB9BBE9F75B0D79E8BBF5E5018CDD1E3F26D2DEC" \
                                                                      "A7D8B77F499E7C9A178A964E1D2C0A2B"))