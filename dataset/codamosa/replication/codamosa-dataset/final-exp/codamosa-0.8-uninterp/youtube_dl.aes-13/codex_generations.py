

# Generated at 2022-06-14 15:07:54.891713
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    print(aes_decrypt_text('X5X5A5V5IUuG0p5O7bMd_12_MjM0MTQxMzM=',"2dqRd6RgU6A",32))
    print(aes_decrypt_text('EBn0ZHQs9nJ4in1hj_12_NjQ4NzQ2NTQw','2dqRd6RgU6A',32))
    print(aes_decrypt_text('xhvn8mwcPO+FZj1mq_12_ODE4Nzg3ODcy','2dqRd6RgU6A',32))

# Generated at 2022-06-14 15:08:04.142045
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    test_key = [40, 42, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    test_iv = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]

# Generated at 2022-06-14 15:08:13.750320
# Unit test for function aes_encrypt
def test_aes_encrypt():
    key = key_expansion([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
    data = [0x6b, 0xc1, 0xbe, 0xe2, 0x2e, 0x40, 0x9f, 0x96, 0xe9, 0x3d, 0x7e, 0x11, 0x73, 0x93, 0x17, 0x2a]
    encrypted_data = aes_encrypt(data, key)

# Generated at 2022-06-14 15:08:22.837791
# Unit test for function aes_encrypt
def test_aes_encrypt():
    key1 = bytes_to_intlist(compat_b64decode('hNdKj8cq3/qH2xNtBoD+tA=='))
    data1 = bytes_to_intlist(compat_b64decode('aM5zZu5/5j+j5rPn/OD6Og=='))
    expanded_key1 = bytes_to_intlist(compat_b64decode('hNdKj8cq3/qH2xNtBoD+tIHfbu0A0sJw3MEq2cN/yNdKj8cq3/qH2xNtBoD+tA=='))


# Generated at 2022-06-14 15:08:27.929691
# Unit test for function aes_encrypt
def test_aes_encrypt():
    # IV constants updated: https://chromium.googlesource.com/chromium/src/+/9d46f2a2475f93835a8a90c4d4d358a4c08a4cb4
    assert b'encryptedData' == intlist_to_bytes(aes_encrypt(bytes_to_intlist(b'encryptedData'), bytes_to_intlist(b'keyExpansionKeyExpans')))


# Generated at 2022-06-14 15:08:32.323779
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = 'data'.encode('utf-8')
    key = b'1234567812345678'
    iv = b'1234567812345678'
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    print(decrypted_data)


# Generated at 2022-06-14 15:08:44.287679
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    test_data = intlist_to_bytes([0 for i in range(4)])
    assert aes_cbc_encrypt(
        test_data,
        bytes_to_intlist(b'YELLOW SUBMARINE'),
        [0 for i in range(16)]
    ) == [
        0x5A, 0xCC, 0x71, 0xA5, 0x7A, 0xA8, 0x88, 0x30,
        0x4A, 0x4D, 0xA1, 0xA5, 0x82, 0xD0, 0xEE, 0x59
    ]

# Generated at 2022-06-14 15:08:54.592978
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    password = '12345678'
    key_size_bytes = 16
    data = 'pfkSDRGseH1RTnFnYXBpYy4u'

    # decrypt data with aes_decrypt_text
    decrypted_data = aes_decrypt_text(data, password, key_size_bytes)

    # Test
    print('\n')
    print('aes_decrypt_text')

    print('  Output:')
    print('    decrypted_data: ' + decrypted_data)

    print('  Test:')
    assert decrypted_data == 'Test 12345678'

    # Show that all tests ran successfully
    print('Tests ran successfully')

# Generated at 2022-06-14 15:09:03.390521
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
           0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    data = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d,
            0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]

    expanded_key = key_expansion(key)
    decrypted_data = aes_decrypt(data, expanded_key)


# Generated at 2022-06-14 15:09:13.130356
# Unit test for function aes_encrypt
def test_aes_encrypt():
    key = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59,
        0x0c, 0xb7, 0xad, 0xd6, 0xaf, 0x7f, 0x67, 0x98,
        0x08, 0x0f, 0x0e, 0x12, 0x04, 0x81, 0xfe, 0xe5]
    data = [0x3a, 0xd7, 0x7b, 0xb4, 0x0d, 0x7a, 0x36, 0x60,
        0xa8, 0x9e, 0xca, 0xf3, 0x24, 0x66, 0xef, 0x97]

    expanded_key = key_expansion(key)


# Generated at 2022-06-14 15:09:26.361222
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:09:36.249575
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .utils import hex_to_b64
    key = bytes_to_intlist("140b41b22a29beb4061bda66b6747e14")
    iv = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb28")
    ciphertext = hex_to_b64("28a226d160dad07883d04e008a7897ee\
2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
    plaintext = aes_cbc_decrypt(compat_b64decode(ciphertext), key, iv)
    assert intlist_to_bytes(plaintext) == b"Basic CBC mode encryption needs padding."



# Generated at 2022-06-14 15:09:43.471588
# Unit test for function inc
def test_inc():
    assert inc([0,0,0,0]) == [0,0,0,1]
    assert inc([0,0,0,255]) == [0,0,1,0]
    assert inc([0,0,255,255]) == [0,1,0,0]
    assert inc([255,255,255,255]) == [0,0,0,0]

test_inc()


# Generated at 2022-06-14 15:09:48.079220
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    test_text = "Hello World!"
    key = intlist_to_bytes([
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
    ])
    iv = intlist_to_bytes([
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
    ])


# Generated at 2022-06-14 15:09:56.663829
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
           0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
          0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:10:07.992564
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = "2b7e151628aed2a6abf7158809cf4f3c";
    key = "2b7e151628aed2a6abf7158809cf4f3c";
    iv = "000102030405060708090A0B0C0D0E0F";
    p = "6bc1bee22e409f96e93d7e117393172a" + "ae2d8a571e03ac9c9eb76fac45af8e51" + "30c81c46a35ce411e5fbc1191a0a52ef" + "f69f2445df4f9b17ad2b417be66c3710";

# Generated at 2022-06-14 15:10:20.367503
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('4oDRkp3lq3jKgCQt1JLGwQ=='))
    data = bytes_to_intlist(compat_b64decode('Rvn/y01rI+j/8TkdJfvT+g=='))
    iv = bytes_to_intlist(compat_b64decode('n/b2G5/FI/qHJjK9a4t4gw=='))

    decrypted_data = bytes_to_intlist(
        compat_b64decode(
            '+LmItnWrSPwet2FmBxjK6oDU6bZgl6+ZffI9EOaKjJ0='
        )
    )


# Generated at 2022-06-14 15:10:32.685341
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .crypto import aes_cbc_encrypt
    from .compat import compat_b64decode

    # http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    #      Appendix F.3.2 CBC-AES256.Encrypt
    #  F.3.2.1 CBC-AES256.Encrypt
    data = bytes_to_intlist(compat_b64decode(b'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='))

# Generated at 2022-06-14 15:10:38.670723
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('KjV7n/ycPb/e/TtT1Tn/Rw=='))
    sub_keys = bytes_to_intlist(compat_b64decode('Y85OPbV7eW8fv5Uq1gU5+6U5HwjKjV7n/ycPb/e/TtT1Tn/Rw=='))

    assert key_expansion(key) == sub_keys

# Generated at 2022-06-14 15:10:50.316212
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:11:03.758531
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:11:16.308995
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:11:25.549835
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    from .cbc import Cbc
    key = bytes_to_intlist('YELLOW SUBMARINE')
    cbc = Cbc()
    cbc.key = key
    iv = '0123456789abcdef'
    iv = bytes_to_intlist(iv)
    with open('../data/10.txt', 'r') as f:
        lines = f.readlines()
    src = compat_b64decode(''.join(lines))
    data = bytes_to_intlist(src)
    encrypted = aes_cbc_encrypt(data, key, iv)
    encrypted2 = bytes_to_intlist(cbc.encrypt(src, iv=iv))
    assert len(encrypted) == len(encrypted2)
    assert encrypted == encrypted2
    print('encrypted: ', len(encrypted))


# Generated at 2022-06-14 15:11:33.685544
# Unit test for function key_expansion
def test_key_expansion():
    key1 = "140b41b22a29beb4061bda66b6747e14"
    key2 = "140b41b22a29beb4061bda66b6747e141b5e7e2bae5dae4"
    key3 = "140b41b22a29beb4061bda66b6747e14"

    expanded1 = "140b41b22a29beb4061bda66b6747e141b5e7e2bae5dae4"
    expanded1 += "d3eec2196d1213be44444444444444444444444444444444"
    expanded2 = "140b41b22a29beb4061bda66b6747e141b5e7e2bae5dae4"

# Generated at 2022-06-14 15:11:46.404750
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('u/QwGj7Ks+tA0wjhPdYGEA=='))
    iv = bytes_to_intlist(compat_b64decode('35wH/ZJdstWfB8iMn2NxUA=='))
    ciphertext = bytes_to_intlist(compat_b64decode('i8/ybpyxmjtwIqm3ll6U5r6U5RKU5RKSQcq1yMv6yOIxKjX6qykpPJVl0vixbKD0LKS+jKkW8yv6Qg0Ej'))

# Generated at 2022-06-14 15:11:59.470021
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')
    iv = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')

# Generated at 2022-06-14 15:12:08.292041
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist("140b41b22a29beb4061bda66b6747e14")
    iv = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb28")
    data = bytes_to_intlist("28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")

    decrypted_data = aes_cbc_decrypt(data, key, iv)

# Generated at 2022-06-14 15:12:19.149502
# Unit test for function key_expansion
def test_key_expansion():
    print()
    print("Test key expansion")
    key_data = [0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C]

# Generated at 2022-06-14 15:12:30.789901
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:42.633445
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:12:55.852979
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:13:08.503956
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cipher_key = bytes_to_intlist('6c3ea0477630ce21a2ce334aa746c2cd')
    iv = bytes_to_intlist('c782dc4c098c66cbd9cd27d825682c81')
    cleartext = bytes_to_intlist('424547494e205445535420434f4e54524f4c4f41444552')
    encrypted = bytes_to_intlist('567fec057e8e67c970c1d6179c615d93e8a2fe2c7ff05aec75f5950db7b9af3c')
    assert aes_cbc_encrypt(cleartext, cipher_key, iv) == encrypted



# Generated at 2022-06-14 15:13:19.963507
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:13:30.925554
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key_128 = bytes_to_intlist(b'\x01\x23\x45\x67\x89\xab\xcd\xef\x12\x34\x56\x78\x9a\xbc\xde\xf0')
    iv_128 = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    data = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    expected_cipher = bytes_

# Generated at 2022-06-14 15:13:39.795042
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    iv = [0] * 16
    data = bytes_to_intlist(b'This is a test!')

    encrypted_data = aes_cbc_encrypt(data, key, iv)
    expected_encrypted_data = [
        104, 33, 39, 0, 8, 46, 51, 118, 170, 233, 65, 192, 139, 132, 126, 177,
        219, 21, 225, 187, 46, 137, 221
    ]
    assert encrypted_data == expected_encrypted_data



# Generated at 2022-06-14 15:13:49.208496
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:13:59.760133
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    b64_data = 'R1KwVHP+jGYrraNU6MvUHQ=='
    data = compat_b64decode(b64_data)
    data = bytes_to_intlist(data)
    key = bytes_to_intlist('b398dc2f8c35865b3c3b0f3d92f0c1b8'.decode('hex'))
    iv = bytes_to_intlist('86A85A6425B18B218D086FBAF6E30802'.decode('hex'))

    expected_b64_encrypted_data = 'iLakwVgCd+f5Ft2QugYi9g=='
    expected_encrypted_data = compat_b64decode(expected_b64_encrypted_data)
    expected_

# Generated at 2022-06-14 15:14:09.117594
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = compat_b64decode('gcyq6SvU5hh5WF6vl1AOwg==')
    iv = [0] * 16
    data = compat_b64decode(
        'Fexy+bw1hYnY+g8WfhZvc9lQmJ+OLmCfLWgDyGdrJn96zy4e4v3+q3N6X9tvbA==')

# Generated at 2022-06-14 15:14:21.296684
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist(b'1234567890123456789012345678')
    key = bytes_to_intlist(b"0"*32)
    iv = bytes_to_intlist(b'0'*16)
    encrypted = bytes_to_intlist(b'1E\x831e\x91\x1f\xbe\xcb,\x11x\x18\x83\xcc\r\x8c\xf2\xae\xd1\x1dW8\x1d\x9a\xc2\x8f\xcc\x12')
    assert aes_cbc_encrypt(data, key, iv) == encrypted
test_aes_cbc_encrypt()



# Generated at 2022-06-14 15:14:30.167025
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:42.495772
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:55.312523
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:05.974468
# Unit test for function key_expansion
def test_key_expansion():
    print("test_key_expansion")

# Generated at 2022-06-14 15:15:14.061491
# Unit test for function key_expansion
def test_key_expansion():
    # given
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    # when
    expanded_key = key_expansion(key)
    # then
    assert bytes_to_intlist(compat_b64decode('n6o3w4Y4YJyOD14DQvgU6g==')) == expanded_key



# Generated at 2022-06-14 15:15:24.802512
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:15:31.582308
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88,
        0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:15:34.049669
# Unit test for function key_expansion
def test_key_expansion():
    data = [1] * 32
    assert key_expansion(data) == [1] * 240

# Generated at 2022-06-14 15:15:46.308375
# Unit test for function key_expansion
def test_key_expansion():
    initial_key = bytes_to_intlist(compat_b64decode('zclP8LnGONpbjowLZ5D5Ew=='))

# Generated at 2022-06-14 15:15:58.028505
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:05.186255
# Unit test for function key_expansion
def test_key_expansion():
    from .compat import compat_b64decode
    from .utils import bytes_to_intlist
    from .aes import key_expansion
    import unittest


# Generated at 2022-06-14 15:16:14.513097
# Unit test for function key_expansion
def test_key_expansion():
    print('Test key expansion')
    data = bytes_to_intlist(b'0123456789abcdef')
    res = key_expansion(data)

# Generated at 2022-06-14 15:16:25.015612
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test function key_expansion
    """
    key_1 = "abcdefghijklmnop"
    expanded_key_1 = "abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz012"

    key_2 = "abcdefghijklmnopqrstuvwxyz012345"
    expanded_key_2 = "abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123"


# Generated at 2022-06-14 15:16:35.627264
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Generated at 2022-06-14 15:16:46.117388
# Unit test for function key_expansion
def test_key_expansion():
    TEST_KEY_1 = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c,
    ]

# Generated at 2022-06-14 15:16:58.145263
# Unit test for function key_expansion
def test_key_expansion():
    print('----- Start unit test for function key_expansion -----')
    import random
    import string
    from os import urandom
    from binascii import hexlify
    from binascii import unhexlify
    r = random.SystemRandom()
    # r = random.Random()
    key = [r.randint(0, 255) for _ in range(16)]
    key = bytes_to_intlist(urandom(16))
    data = bytes_to_intlist(urandom(16 * 16))
    print('Encrypting data with aes-cbc and random key')
    cipher = aes_cbc_encrypt(data, key, key)
    print('Expanding key')
    expanded_key = key_expansion(key)
    print('Decrypting data with expanded key and same data')

# Generated at 2022-06-14 15:17:07.078647
# Unit test for function key_expansion
def test_key_expansion():
    def test_with_key(key_str, expected_expanded_key_str):
        key = bytes_to_intlist(compat_b64decode(key_str.encode('utf-8')))
        expected_expanded_key = bytes_to_intlist(compat_b64decode(expected_expanded_key_str.encode('utf-8')))
        expanded_key = key_expansion(key)
        assert expanded_key == expected_expanded_key


# Generated at 2022-06-14 15:17:19.173359
# Unit test for function key_expansion
def test_key_expansion():
    # test key 32 bytes
    input_key = bytes_to_intlist(compat_b64decode('m8LyW/T3mqrY+XBJvD8sxWl1QknsoZG0C6dz+VF4J6M='))
    expanded_key = key_expansion(input_key)