

# Generated at 2022-06-14 15:07:45.819017
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Test known keys
    key1 = '0'*32
    iv1 = '0'*16
    data1 = '0'*16
    decrypted1 = bytes_to_intlist(aes_cbc_decrypt(bytes_to_intlist(data1), bytes_to_intlist(key1), bytes_to_intlist(iv1)))
    assert decrypted1 == bytes_to_intlist(data1)

    key2 = 'b'*32
    iv2 = '0'*16
    data2 = 'b'*16
    decrypted2 = bytes_to_intlist(aes_cbc_decrypt(bytes_to_intlist(data2), bytes_to_intlist(key2), bytes_to_intlist(iv2)))
    assert decrypted2 == bytes_to_intlist

# Generated at 2022-06-14 15:07:54.257067
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    import binascii
    key = bytes_to_intlist(compat_b64decode(b'YKsWltdkeDSv4e4/4JH4lbLIWdwnKmfN'))
    iv = bytes_to_intlist(compat_b64decode(b'ZU6zDU6e+p6rKj9A5U5P5A=='))
    data = bytes_to_intlist(compat_b64decode(b'9VuAKJWdQ2VwjPqIHV7pfg=='))

    result = intlist_to_bytes(aes_cbc_encrypt(data, key, iv)[:len(data)])

# Generated at 2022-06-14 15:08:03.951045
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:08:13.631029
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    """
    Test aes_ctr_decrypt
    """
    from .compat import compat_b64encode, compat_b64decode
    key = compat_b64decode('KUEhVeS2Y8yXiWxPdXneuQ==')
    cipher = compat_b64decode('uJTvsI+Yvf8WJbx7E9ev9w==')
    ctr = intlist_to_bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
    expected_plain = b'{"a": "b"}'
    assert aes_ctr_decrypt(bytes_to_intlist(cipher), bytes_to_intlist(key), Counter(ctr)) == bytes_to_intlist

# Generated at 2022-06-14 15:08:22.802147
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    # Those tests verify that our implementation matches the ones used by youtube for encrypting their video URLs.
    # This is a known plaintext attack (we know the plaintext, e.g. the URL).

    # https://www.youtube.com/watch?v=Khv_8W_mhUs
    cipher = 'Ig1eM8pzdKMZ3wcqQ2gBJ8OzD_9jhPa1z7CLaaj-0uY.'
    password = 'youtube'
    plaintext = aes_decrypt_text(cipher, password, key_size_bytes=16)

# Generated at 2022-06-14 15:08:32.484385
# Unit test for function aes_encrypt
def test_aes_encrypt():
    data = bytes_to_intlist(compat_b64decode('WApDd9N1NzI+jkZF0DSwPQ=='))
    expanded_key = bytes_to_intlist(compat_b64decode('+mZr3wONtNZFHaKj0Yt22+37Hx1x9RnhArpsgjZhlYuM3rqw3tPJAjKdcIyptL+G'))
    assert aes_encrypt(data, expanded_key) == bytes_to_intlist(b'\xd0\x0b\x9d\x34\x84\x0f\x7c\x20\x6f\x6c\xbd\x0e\x46\x4a\xce\x7e')

# Generated at 2022-06-14 15:08:39.313904
# Unit test for function rijndael_mul
def test_rijndael_mul():
    a = 0x57  # in hex
    b = 0x83  # in hex
    result = rijndael_mul(a, b)
    print(hex(result))  # 0xc1 in hex
    print(chr(result))  # Á in utf-8


# Unit test
test_rijndael_mul()



# Generated at 2022-06-14 15:08:48.591347
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    import unittest
    import sys
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:08:53.803142
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    data = 'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
    password = 'YELLOW SUBMARINE'
    key_size_bytes = 16
    plaintext = aes_decrypt_text(data, password, key_size_bytes)

    if plaintext == b'Yo, VIP Let\'s kick it Ice, Ice, baby Ice, Ice, baby ':
        print('aes_decrypt_text: PASSED')
    else:
        print('aes_decrypt_text: FAILED')



# Generated at 2022-06-14 15:09:02.909143
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Examples from https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29

    # Example #1
    key = bytes_to_intlist(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')
    iv = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')

# Generated at 2022-06-14 15:09:21.149200
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:09:27.783118
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    test_data = bytes_to_intlist(b'1234567890123456')
    test_key = bytes_to_intlist(b'000102030405060708090A0B0C0D0E0F')
    test_iv  = bytes_to_intlist(b'00000000000000000000000000000000')
    test_solution = bytes_to_intlist(b'A11505B0FAF4576B1B6BDB2BC28F5E33')
    assert aes_cbc_encrypt(test_data, test_key, test_iv) == test_solution
    return True



# Generated at 2022-06-14 15:09:33.761752
# Unit test for function key_expansion
def test_key_expansion():
    CIPHER_KEY_16 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
                     0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

    CIPHER_KEY_24 = [0x8e, 0x73, 0xb0, 0xf7, 0xda, 0x0e, 0x64, 0x52,
                     0xc8, 0x10, 0xf3, 0x2b, 0x80, 0x90, 0x79, 0xe5,
                     0x62, 0xf8, 0xea, 0xd2, 0x52, 0x2c, 0x6b, 0x7b]

   

# Generated at 2022-06-14 15:09:44.231394
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    assert aes_cbc_encrypt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [
                               142, 164, 186, 208, 230, 252, 142, 164, 186, 208, 230, 252, 142, 164, 186, 208]
    print("Function aes_cbc_encrypt passed")

# Generated at 2022-06-14 15:09:54.137668
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert aes_cbc_encrypt(data, key, iv) == [126, 247, 124, 55, 168, 139, 223, 213, 44, 153,
                                              9, 147, 190, 79, 73, 154]

    # Test for padding

# Generated at 2022-06-14 15:10:05.781064
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:10:17.014158
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = bytes_to_intlist(b'00112233445566778899aabbccddeeff' + b'00112233445566778899aabbccddeeff')
    key = bytes_to_intlist(b'000102030405060708090a0b0c0d0e0f')
    iv = bytes_to_intlist(b'17396d113679043d926a27148516c047')

    ciphertext = aes_cbc_encrypt(cleartext, key, iv)

# Generated at 2022-06-14 15:10:29.360558
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = b'This is a test for the encrypt function'
    key = bytes_to_intlist(compat_b64decode('R7VuQk5q8d7G/ZPm4dLpLg=='))
    iv = bytes_to_intlist(compat_b64decode('2Q/vUzL1UcvN9IYWp/n1vw=='))
    encrypted_data = aes_cbc_encrypt(data, key, iv)

# Generated at 2022-06-14 15:10:31.324440
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    """
    Test for aes_cbc_encrypt
    """
    from .aes_cbc import test_aes_cbc_encrypt

    return test_aes_cbc_encrypt(aes_cbc_encrypt)



# Generated at 2022-06-14 15:10:40.011778
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    print('Testing function aes_cbc_encrypt')
    encrypted = aes_cbc_encrypt([0] * 32, bytes_to_intlist(b'YELLOW SUBMARINE'), bytes_to_intlist(b'YELLOW SUBMARINE'))
    print('Input: [0] * 32, YELLOW SUBMARINE, YELLOW SUBMARINE')
    print('Output:', encrypted)

# Generated at 2022-06-14 15:10:44.954538
# Unit test for function inc
def test_inc():
    print("test inc")
    ic = [0, 0, 0]
    for i in range(256):
        print(ic)
        ic = inc(ic)
    print(ic)
    assert(ic == [0, 0, 1])



# Generated at 2022-06-14 15:10:47.551159
# Unit test for function inc
def test_inc():
    inc([0])
    inc([0,0])
    inc([5])
    inc([1,3,5,7,9,11,13,15])
    inc([1,255])
    inc([1,255,255,255])
    inc([255,255,255,255])



# Generated at 2022-06-14 15:10:49.315530
# Unit test for function inc
def test_inc():
    data = [0] * 16
    for i in range(1, 512):
        data = inc(data)
        print(data)

# test_inc()



# Generated at 2022-06-14 15:10:51.634348
# Unit test for function inc
def test_inc():
    assert inc([0] * 16) == [1] * 16
    assert inc([1, 255, 255]) == [2, 0, 0]
    assert inc([255] * 16) == [0] * 16



# Generated at 2022-06-14 15:10:54.202130
# Unit test for function inc
def test_inc():
    assert inc([1]) == [2]
    assert inc([1, 2]) == [1, 3]
    assert inc([1, 255]) == [2, 0]
    assert inc([255, 255]) == [0, 0]


# Generated at 2022-06-14 15:11:02.904682
# Unit test for function inc
def test_inc():
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([0] * 4) == [0] * 4

    # 0xffffffff == 4294967295
    assert inc([255, 255, 255, 255]) == [0, 0, 0, 0]
    # 0xffffffffffffffff == 18446744073709551615
    assert inc([255] * 16) == [0] * 16

    # 0xfffffffffffffffe == 18446744073709551614
    assert inc([255] * 15 + [254]) == [255] * 15 + [255]

    # 0x9c080b020ca1cab6

# Generated at 2022-06-14 15:11:11.165283
# Unit test for function inc
def test_inc():
    a = [255] * 16
    b = [255] * 16
    c = [255] * 16
    for i in range(0, 0xffff):
        b = inc(b)

# Generated at 2022-06-14 15:11:22.173350
# Unit test for function key_expansion
def test_key_expansion():
    from .aes import key_expansion, aes_encrypt, aes_decrypt
    from .utils import bytes_to_intlist

    for key_str in ['000102030405060708090a0b0c0d0e0f',
                    '000102030405060708090a0b0c0d0e0f1011121314151617',
                    '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f']:
        key_intlist = [int(key_str[i:i+2], 16) for i in range(0, len(key_str), 2)]
        expanded_key_intlist = key_expansion(key_intlist)
        expanded_

# Generated at 2022-06-14 15:11:25.151367
# Unit test for function inc
def test_inc():
    data = [0]*16
    for i in range(1000):
        data = inc(data)
        print(data[-1])
        if data[-1] == 1:
            break
# test_inc()



# Generated at 2022-06-14 15:11:32.874044
# Unit test for function inc
def test_inc():
    data = [0, 0, 0, 0]
    assert inc(data) == [0, 0, 0, 1]
    assert inc(data) == [0, 0, 0, 2]
    assert inc(data) == [0, 0, 0, 3]
    assert inc(data) == [0, 0, 0, 4]
    assert inc(data) == [0, 0, 0, 5]
    assert inc(data) == [0, 0, 0, 6]
    assert inc(data) == [0, 0, 0, 7]
    assert inc(data) == [0, 0, 0, 8]
    assert inc(data) == [0, 0, 0, 9]
    assert inc(data) == [0, 0, 0, 10]
    assert inc(data) == [0, 0, 0, 11]

# Generated at 2022-06-14 15:13:19.193646
# Unit test for function key_expansion
def test_key_expansion():

    def _convert_bytes_to_ints(data):
        return [ord(c) for c in data]

    def _convert_ints_to_bytes(data):
        return bytes(bytearray(data))


# Generated at 2022-06-14 15:13:27.855109
# Unit test for function key_expansion
def test_key_expansion():
    print('test_key_expansion')
    key = [0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe, 0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81, 0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7, 0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4]

# Generated at 2022-06-14 15:13:39.379088
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:49.026399
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:59.660921
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:09.127020
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c,
    ]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:14:22.721346
# Unit test for function key_expansion
def test_key_expansion():
    key = list(map(lambda x: x.to_bytes(1, 'big'), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    expanded_key = key_expansion(key)


# Generated at 2022-06-14 15:14:30.548810
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'1234567890123456')

    key_encrypted = key_expansion(key)
    key_decrypted = key_expansion(key_encrypted)


# Generated at 2022-06-14 15:14:41.336439
# Unit test for function key_expansion
def test_key_expansion():
    key = [0, 0, 0, 0]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:14:54.445438
# Unit test for function key_expansion
def test_key_expansion():
    result = aes_encrypt([0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34], key_expansion([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]))

# Generated at 2022-06-14 15:17:08.034317
# Unit test for function key_expansion
def test_key_expansion():
    def test_key_expansion_helper(key_size_bytes, key_size_bits,
                                  expected_expanded_key_size_bytes, expected_expanded_key_size_bits,
                                  key, expected_expanded_key):
        expanded_key_size_bytes, expanded_key_size_bits = len(expected_expanded_key), len(expected_expanded_key) * 8
        assert expected_expanded_key_size_bytes == expanded_key_size_bytes, (
            'Expected expanded key size bytes: %d, actual: %d' % (
                expected_expanded_key_size_bytes, expanded_key_size_bytes))

# Generated at 2022-06-14 15:17:19.889283
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128 Test
    data = bytes_to_intlist(compat_b64decode(
        "ZWvhzjx11qDlq2Yvz8ywDA=="))
    assert intlist_to_bytes(key_expansion(data)) == compat_b64decode(
        "ZWvhzjx11qDlq2Yvz8ywDA7xIkGpZVYwfg0USiKV2Qo=")
    # AES-192 Test
    data = bytes_to_intlist(compat_b64decode(
        "O/6UqQ2oBX9WzH+sMPfddQ=="))