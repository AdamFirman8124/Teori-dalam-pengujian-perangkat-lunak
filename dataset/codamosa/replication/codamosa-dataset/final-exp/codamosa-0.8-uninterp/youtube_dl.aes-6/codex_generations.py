

# Generated at 2022-06-14 15:07:48.113026
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('kPH+bIxk5D2deZiIxcaaaA==')[:16])
    iv = bytes_to_intlist(compat_b64decode('2jmj7l5rSw0yVb/vlWAYkK/YBwk=')[:16])

# Generated at 2022-06-14 15:07:59.798454
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """Unit test for function aes_decrypt_text"""
    
    data = b'QcCQCKBbvItjt1MV7DZJpXuVdJgHFsNBEw1O4b+F0/8='
    password = 'Passwort'
    key_size_bytes = 24
    decrypted_data = 'Test Text'
    
    decrypted = aes_decrypt_text(data, password, key_size_bytes)
    
    assert decrypted == decrypted_data
    
test_aes_decrypt_text()
 


# Generated at 2022-06-14 15:08:06.720605
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(compat_b64decode(b'CFe23a9YDmC2B8Eg+zk/JQ=='))
    iv = bytes_to_intlist(compat_b64decode(b'nTtRjdo+Xzjkqa1Yi0hhSw=='))
    data = bytes_to_intlist(compat_b64decode(b'c29tZS1iYXNlNjQtZW5jb2RlZA=='))
    result = bytes_to_intlist(compat_b64decode(b'hHicOOGn0jQi+gx3f9XAkZKjfZN7Nw5dMNcVQjk/4ME='))

    assert aes_

# Generated at 2022-06-14 15:08:16.204483
# Unit test for function aes_encrypt
def test_aes_encrypt():
    key = bytes_to_intlist(compat_b64decode('6KiH6EVUU4A='))
    data = bytes_to_intlist(compat_b64decode('NZWRW3cq3OQ='))
    expanded_key = key_expansion(key)
    assert aes_encrypt(data, expanded_key) == [0x9e, 0x8e, 0xc2, 0xaa, 0xf7, 0xad, 0x77, 0x51, 0x9a, 0xae, 0x91, 0x10, 0x29, 0xb3, 0x3a, 0xc2]
    key = bytes_to_intlist(compat_b64decode('RmFjdG9yeUtleVBhc3N3b3Jk'))


# Generated at 2022-06-14 15:08:26.543693
# Unit test for function aes_encrypt
def test_aes_encrypt():
    # 2-2.2, page 12 (first block)
    data = [0x00, 0x44, 0x88, 0xcc, 0x11, 0x55, 0x99, 0xdd, 0x22, 0x66, 0xaa, 0xee, 0x33, 0x77, 0xbb, 0xff]
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:08:35.267242
# Unit test for function aes_decrypt
def test_aes_decrypt():
    # AES-128 results
    test = bytes_to_intlist(compat_b64decode('iM8/7/jSktY0V/gq3eZ8viMoDwHgtxyKzFyTdTEb8W0='))
    key = bytes_to_intlist(compat_b64decode('eHh4eHh4eHh4eHh4eHh4eHh4eHg='))

# Generated at 2022-06-14 15:08:46.022404
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class Counter:
        def __init__(self, nonce):
            self.i = 0
            self.nonce = nonce

        def next_value(self):
            self.i += 1
            return bytes_to_intlist(self.nonce + bytearray(self.i.to_bytes(8, 'big')))

    counter = Counter(bytearray(b'\x00' * 8))

# Generated at 2022-06-14 15:08:56.918597
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """
    Test function aes_decrypt_text against some test vectors
    """
    import json
    import base64

# Generated at 2022-06-14 15:09:08.908328
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:09:17.844600
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    my_password = 'This is my password'  # does not have to be 16 Byte
    my_key_size_bytes = 16  # possible values: 16 for 128-Bit, 24 for 192-Bit or 32 for 256-Bit
    my_data = 'pPdBjUPZDtHcFDt/aGKUIw=='  # Base64 encoded string that contains encrypted text
    my_plaintext = aes_decrypt_text(my_data, my_password, my_key_size_bytes)
    print('Plaintext: ' + my_plaintext)


# Generated at 2022-06-14 15:09:31.380872
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    iv = [
        0x3D, 0xAF, 0xBA, 0x42, 0x9D, 0x9E, 0xB4, 0x30,
        0xB4, 0x22, 0xDA, 0x80, 0x2C, 0x9F, 0xAC, 0x41,
    ]

# Generated at 2022-06-14 15:09:39.131263
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    iv = bytes_to_intlist(b'\x00' * 16)
    data = b'YELLOW SUBMARINEYELLOW SUBMARINE'
    data = bytes_to_intlist(data)
    encrypted = aes_cbc_encrypt(data, key, iv)


# Generated at 2022-06-14 15:09:50.873794
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    import binascii
    encrypted_data = [187, 22, 152, 134, 230, 230, 81, 215, 74, 199, 74, 218, 104, 24, 35, 31,
                      246, 239, 115, 168, 81, 59, 111, 129, 213, 103, 83, 11, 251, 186, 189, 8]

    iv = [108, 64, 68, 58, 218, 156, 229, 137, 151, 71, 50, 153, 48, 34, 62, 6]
    key = [6, 63, 64, 116, 18, 104, 34, 46, 31, 57, 206, 119, 110, 247, 123, 69,
           213, 114, 73, 134, 248, 90, 196, 87, 10, 110, 189, 95, 150, 91, 98, 190]

    decrypted_data = aes_cbc

# Generated at 2022-06-14 15:10:02.464246
# Unit test for function key_expansion
def test_key_expansion():

    try_test = ['000102030405060708090a0b0c0d0e0f',
                '000102030405060708090a0b0c0d0e0f1011121314151617',
                '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f']


# Generated at 2022-06-14 15:10:11.951958
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:10:24.192263
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cbc_key = bytes_to_intlist(b'0123456789abcdeffedcba9876543210')
    cbc_iv = bytes_to_intlist(b'0123456789abcdef0123456789abcdef')
    cbc_data = bytes_to_intlist(b'example of plaintext')
    cbc_encrypted_data = bytes_to_intlist(b'\xa2\x0f\xec\x7d\xa9c\xc7\x9b\xbc\xef\xce\x7f\x97\x0c\xb2v\xc7\x9e9\x8f\xcf\xb3\x89')
    assert aes_cbc_encrypt(cbc_data, cbc_key, cbc_iv)

# Generated at 2022-06-14 15:10:35.700495
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    """
    AES CBC decrypt
    """
    key = bytes_to_intlist(bytearray(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'))
    data = bytes_to_intlist(b'4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')


# Generated at 2022-06-14 15:10:48.246008
# Unit test for function key_expansion
def test_key_expansion():
    def do_test(data, expected):
        data = bytes_to_intlist(compat_b64decode(data))
        expected = bytes_to_intlist(compat_b64decode(expected))
        result = key_expansion(data)
        assert result == expected
    # Test case obtained from http://www.inconteam.com/software-development/41-encryption/55-aes-test-vectors#aes-ecb-var-key

# Generated at 2022-06-14 15:10:58.274774
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:11:06.672764
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Test vector from FIPS 197
    key = bytes_to_intlist(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
    iv = bytes_to_intlist(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")

# Generated at 2022-06-14 15:11:20.875028
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .AES import aes_key, aes_cbc_encrypt, gen_counter_block
    from .Hexdump import hex2bin, hexdump

    # http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    # F.5.1 CBC-AES128.Encrypt
    ct = bytes_to_intlist(compat_b64decode('K2jK9Xx1Dv8e6WYwOiTfAA=='))

# Generated at 2022-06-14 15:11:29.989683
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:11:33.203227
# Unit test for function inc
def test_inc():
    assert inc([0,0,0,0]) == [0,0,0,1]
    assert inc([0,0,0,255]) == [0,0,1,0]
    assert inc([255,255,255,255]) == [0,0,0,0]
    assert inc([0,1,255,255]) == [1,0,0,0]

test_inc()

# Generated at 2022-06-14 15:11:45.646534
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test whether the key expansion generates the correct key schedule
    """

# Generated at 2022-06-14 15:11:58.868332
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    import random
    from .utils import bytes_to_intlist, intlist_to_bytes

    num_iterations = 100
    key_lengths = (16, 24, 32)
    plaintext_lengths = (1, 17, 31, 32, 100, 101)
    for _ in range(num_iterations):
        key = [random.randint(0, 255) for _ in range(random.choice(key_lengths))]
        plaintext = [random.randint(0, 255) for _ in range(random.choice(plaintext_lengths))]
        iv = [random.randint(0, 255) for _ in range(16)]
        ciphertext = aes_cbc_encrypt(plaintext, key, iv)

# Generated at 2022-06-14 15:12:07.774625
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test the function key_expansion
    """
    from .crypto_js import CRYPTO_JS_KEY_EXPANSION
    key = bytes_to_intlist(compat_b64decode(CRYPTO_JS_KEY_EXPANSION))
    expanded_key = key_expansion(key[:16])
    assert expanded_key == key

    key = bytes_to_intlist(compat_b64decode(CRYPTO_JS_KEY_EXPANSION))
    expanded_key = key_expansion(key[:24])
    assert expanded_key == key

    key = bytes_to_intlist(compat_b64decode(CRYPTO_JS_KEY_EXPANSION))
    expanded_key = key_expansion(key[:32])
    assert expanded_key == key

# Generated at 2022-06-14 15:12:19.033786
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    print("aes_cbc_decrypt unit test start!")
    key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = [64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    decrypted_data = aes_cbc_decrypt(bytes_to_intlist('dka5e5EG5G5f5Q5Q5w5z5z5z5'.encode('utf-8')), key, iv)
    assert(data == decrypted_data)
   

# Generated at 2022-06-14 15:12:30.695463
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:12:42.340234
# Unit test for function aes_decrypt
def test_aes_decrypt():

    def test_16_1():
        c = [0x04, 0xE0, 0x48, 0x28, 0x66, 0xCB, 0xF8, 0x06, 0x81, 0x19, 0xD3, 0x26, 0xE5, 0x9A, 0x7A, 0x4C]
        k = [0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C]

# Generated at 2022-06-14 15:12:49.688008
# Unit test for function inc
def test_inc():
    assert(inc([10, 10, 10, 10]) == [10, 10, 10, 11])
    assert(inc([10, 10, 10, 255]) == [10, 10, 11, 0])
    assert(inc([10, 10, 255, 255]) == [10, 11, 0, 0])
    assert(inc([10, 255, 255, 255]) == [11, 0, 0, 0])
    assert(inc([255, 255, 255, 255]) == [0, 0, 0, 0])



# Generated at 2022-06-14 15:13:00.399238
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Test vectors as found in https://www.ietf.org/rfc/rfc3602.txt
    # Section 1, Test Case #1
    test_vector1 = bytes_to_intlist(compat_b64decode((
        'QkUgU1VSRSBUTyBEUklOSyBZT1VSIE9WQUxUSU5F')))
    encryption_key1 = (
        0xAE, 0x68, 0x52, 0xF8,
        0x12, 0x10, 0x67, 0xCC,
        0x4B, 0xF7, 0xA5, 0x76,
        0x55, 0x77, 0xF3, 0x9E)

# Generated at 2022-06-14 15:13:11.326406
# Unit test for function aes_decrypt
def test_aes_decrypt():
    import base64
    # key = 0x80000000000000000000000000000000
    key = bytes_to_intlist(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    key_expanded = key_expansion(key)
    # cipher = 0x95f8a5e5dd31d900e4e40 Thread order is important for this unit test, causes
    # cipher = 0x8dd7a8b6e1e6589beaa6 change in value of s2

# Generated at 2022-06-14 15:13:22.162100
# Unit test for function aes_decrypt
def test_aes_decrypt():
    def test_vector(key, cleartext, expected_ciphertext):
        expanded_key = key_expansion(key)

        ciphertext = aes_encrypt(cleartext, expanded_key)
        assert ciphertext == expected_ciphertext, (
            'Incorrect ciphertext:\n'
            'Key: %s\n'
            'Cleartext: %s\n'
            'Expected:  %s\n'
            'Actual:    %s' % (
                intlist_to_bytes(key),
                intlist_to_bytes(cleartext),
                intlist_to_bytes(expected_ciphertext),
                intlist_to_bytes(ciphertext)))

        decrypted_cleartext = aes_decrypt(ciphertext, expanded_key)
        assert decrypted

# Generated at 2022-06-14 15:13:32.985287
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:13:42.377262
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    iv = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Generated at 2022-06-14 15:13:50.601425
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:14:00.946512
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    iv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # data = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    data = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
    # data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # data = [42,42,42,42

# Generated at 2022-06-14 15:14:10.193565
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:14:23.319136
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:14:35.622274
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = bytes_to_intlist(b'abcdefghijklmnop')
    expanded_key = bytes_to_intlist(
        b'2b7e151628aed2a6abf7158809cf4f3c98c9b6c3a18d3b8e'
        b'875f3bf3fdba2f1cdfd9ab76b59a9f085b5bd8c5cee2b1c1'
        b'8a90c09f9fb62b6615543d5f8e5c5e2a53be1fca6b1a8cb')
    decrypted_data = aes_decrypt(data, expanded_key)

# Generated at 2022-06-14 15:14:50.232603
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist("140b41b22a29beb4061bda66b6747e14")
    iv = [0] * BLOCK_SIZE_BYTES
    data = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee"
                            "2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")

    decrypted_data = aes_cbc_decrypt(data, key, iv)

# Generated at 2022-06-14 15:15:00.549271
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    import unittest
    import sys

    class AESTest(unittest.TestCase):
        def test_aes_cbc_decrypt(self):
            key = bytes_to_intlist(compat_b64decode(b'jOEYMmsFb/061I+YwY00Dg=='))
            iv = bytes_to_intlist(compat_b64decode(b'Qz0Y7q3ZqxFWs8iXDhHJRQ=='))

# Generated at 2022-06-14 15:15:10.338054
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():

    # Test case 1 (vector #1)
    input_key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    input_iv = bytes_to_intlist('000102030405060708090a0b0c0d0e0f')

# Generated at 2022-06-14 15:15:22.071811
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:15:30.213784
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('/1eayCmOvONp+0gFjGY1tQ=='))
    iv = bytes_to_intlist(compat_b64decode('7GJ1+kQnkQIhfCtDzWhWIA=='))
    data = bytes_to_intlist(compat_b64decode('pPX8zdZDx1QJ6QeL6gAKU6CgHqqvjlRgPJhBzQ8Wc/s='))
    decrypted = aes_cbc_decrypt(data, key, iv)

# Generated at 2022-06-14 15:15:42.897393
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:15:49.370934
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .aes_cbc_encrypt import aes_cbc_encrypt
    from .aes_cbc_encrypt import _test_aes_cbc_encrypt

    # Test cipher consistency
    for test_data in _test_aes_cbc_encrypt():
        assert aes_cbc_decrypt(test_data[:, 0], test_data[:, 1], test_data[:, 2]) == test_data[:, 3]



# Generated at 2022-06-14 15:15:59.767253
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist("140b41b22a29beb4061bda66b6747e14".decode("hex"))
    cipher = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("hex"))
    iv = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb28".decode("hex"))
    plain = aes_cbc_decrypt(cipher, key, iv)

# Generated at 2022-06-14 15:16:11.182282
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    print('\nTesting function aes_cbc_decrypt')

# Generated at 2022-06-14 15:16:23.271563
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    import random
    import re

    # print("\nTesting aes_cbc_decrypt:\n")

    # Test known values
    data = bytes_to_intlist('140b41b22a29beb4061bda66b6747e14')
    key = bytes_to_intlist('140b41b22a29beb4061bda66b6747e14')
    iv = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb28')
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    assert decrypted_data == bytes_to_intlist('28a226d160dad07883d04e008a7897ee')

    # Test random values

# Generated at 2022-06-14 15:16:36.099779
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test case for key_expansion function

    @returns {bool}
    """
    key = [125, 253, 84, 242, 195, 17, 123, 189, 1, 165, 54, 93, 77, 171, 160, 226]
    data = [99, 4, 125, 153, 17, 66, 250, 161, 100, 196, 72, 112, 155, 3, 49, 168, 87, 225, 143, 163, 46, 49, 99, 17, 168, 125, 158, 213, 126, 49, 5, 250, 45, 247, 167, 87, 49, 85, 222, 32, 137, 195, 182, 127, 219, 91, 117, 139, 45, 246, 218, 154, 106, 120, 241, 49, 155, 115, 15, 63]
    result = key_expansion(key)
    return

# Generated at 2022-06-14 15:16:46.479817
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:58.455360
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:07.301918
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88,
           0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:17:19.336342
# Unit test for function key_expansion