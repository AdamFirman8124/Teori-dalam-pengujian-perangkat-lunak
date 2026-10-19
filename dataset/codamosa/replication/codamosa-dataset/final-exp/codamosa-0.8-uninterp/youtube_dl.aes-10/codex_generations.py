

# Generated at 2022-06-14 15:07:45.436098
# Unit test for function inc
def test_inc():
    assert inc([255, 255, 255, 255]) == [0, 0, 0, 0]
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([1, 1, 1, 1]) == [1, 1, 1, 2]
    assert inc([10, 10, 10, 10]) == [10, 10, 10, 11]



# Generated at 2022-06-14 15:07:53.897882
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():

    # TODO: Link to specification
    #       https://tools.ietf.org/html/rfc3602#page-6

    # Block (4.4)
    input_ = bytes_to_intlist(compat_b64decode(b'ZWxpY2FsbHkgd2l0aCBtZW1vcnkgbXVzaWM='))
    expected_output = bytes_to_intlist(compat_b64decode(b'xVj8oC2BhQvoPwwDQiQ2JmnWNHZjYw5UgNa1BV7HrG0='))

# Generated at 2022-06-14 15:07:59.433198
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    secret = 'Io5O5zn5smN/N+zS5pS56Wg5pW95pS56WgA=='
    password = 'password'
    decrypted_text = aes_decrypt_text(secret, password, 16)
    plaintext = intlist_to_bytes(decrypted_data)
    return plaintext

# Generated at 2022-06-14 15:08:06.741115
# Unit test for function inc
def test_inc():
    print("Test inc")
    assert(inc([0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]) == [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1])
    assert(inc([0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9]) == [0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0xA])

# Generated at 2022-06-14 15:08:15.953025
# Unit test for function aes_decrypt
def test_aes_decrypt():
    encrypted_block = bytes_to_intlist(compat_b64decode('Uj6xE9MGy5A='))
    expanded_key = bytes_to_intlist(compat_b64decode('B0QxL9jji32/8oBv/c3q/FpjCGZYW8i/1Vh3uq3c9V7sIeejzKs7nT2TZT99Rj40IYvFITjhPfE='))
    decrypted_block = aes_decrypt(encrypted_block, expanded_key)
    assert intlist_to_bytes(decrypted_block) == b'1234567890abcdef'
    print('aes_decrypt passed')



# Generated at 2022-06-14 15:08:20.259834
# Unit test for function key_expansion
def test_key_expansion():
    from .keystore import key_store
    from .tests.test_keystore import KEY_EXPANSION_TESTS

    for key, expected_expanded_key in KEY_EXPANSION_TESTS.items():
        expanded_key = key_expansion(key_store.hashed_key(key))
        assert expanded_key == expected_expanded_key



# Generated at 2022-06-14 15:08:31.068237
# Unit test for function key_expansion
def test_key_expansion():
    key_16 = bytes_to_intlist(bytes(bytearray([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])))

# Generated at 2022-06-14 15:08:42.372838
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class Counter(object):
        def __init__(self, counter):
            self.counter = counter

        def next_value(self):
            block = self.counter + [0] * (BLOCK_SIZE_BYTES - len(self.counter) % BLOCK_SIZE_BYTES)
            self.counter = [block[i] + 1 if i == (len(block) - 1) else block[i] for i in range(len(block))]
            # print(self.counter)
            return self.counter

    data = bytes_to_intlist(compat_b64decode('vwHp7W8mqP/oCqrzvHmJQW8XfDjgRtKSZzWDaH2x8AA='))


# Generated at 2022-06-14 15:08:45.277931
# Unit test for function key_schedule_core
def test_key_schedule_core():
    data = [0x01, 0x02, 0x03, 0x04]
    dat = key_schedule_core(data,1)
    assert len(dat) == 4
    assert dat[0] == 0x01 ^ RCON[1]
    assert dat[1] == SBOX[0x02]
    assert dat[2] == SBOX[0x03]
    assert dat[3] == SBOX[0x04]


# Generated at 2022-06-14 15:08:56.439344
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():

    test_key = bytes_to_intlist('36f18357be4dbd77f050515c73fcf9f2')
    test_nonce = bytes_to_intlist('69dda8455c7dd4254bf353b773304eec')

    class ArithmeticCounter(object):
        def __init__(self, init_value):
            self.value = init_value

        def next_value(self):
            self.value = self.value + 1
            return self.value

    counter = ArithmeticCounter(bytes_to_intlist('874d6191b620e3261bef6864990db6ce'))

# Generated at 2022-06-14 15:09:14.617067
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = "hello world :-)"
    cleartext = bytes_to_intlist(cleartext.encode('utf-8'))
    key = "1234567890123456"
    key = bytes_to_intlist(key.encode('utf-8'))
    iv = '1234567890123456'
    iv = bytes_to_intlist(iv.encode('utf-8'))

    encrypted = aes_cbc_encrypt(cleartext, key, iv)
    encrypted_bytes = intlist_to_bytes(encrypted)
    encrypted_b64 = compat_b64decode(encrypted_bytes)

# Generated at 2022-06-14 15:09:25.270697
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .decryption import Counter
    from .utils import hex_to_intlist, intlist_to_bytes

    key = hex_to_intlist('140b41b22a29beb4061bda66b6747e14')
    data = hex_to_intlist(
        '4ca00ff4c898d61e1edbf1800618fb28'
        '28a226d160dad07883d04e008a7897ee'
        '2e4b7465d5290d0c0e6c6822236e1daa'
        'fb94ffe0c5da05d9476be028ad7c1d81'
    )
    iv = hex_to_intlist('000102030405060708090A0B0C0D0E0F')

    counter

# Generated at 2022-06-14 15:09:35.344202
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:09:45.719385
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = bytes_to_intlist(b'1234567890abcdef')
    key = bytes_to_intlist(b'0f1571c947d9e8590cb7add6af7f6798')
    iv = bytes_to_intlist(b'0102030405060708')
    encrypted_data = aes_cbc_encrypt(cleartext, key, iv)
    expected_cipher = b'c9f9b7dc55bbc8f27a26fa039c5cfa34'
    assert bytes_to_intlist(compat_b64decode(expected_cipher)) == encrypted_data



# Generated at 2022-06-14 15:09:55.145467
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key_hex = '140b41b22a29beb4061bda66b6747e14'
    iv_hex = '4ca00ff4c898d61e1edbf1800618fb28'
    cleartext = 'Basic CBC mode encryption needs padding.'
    expected_cipher_hex = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

    key = bytes_to_intlist(compat_b64decode(key_hex))

# Generated at 2022-06-14 15:10:06.738896
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('K7gNU3sdo+OL0wNhqoVWhr3g6s6Sp83x ahead of curve'))
    iv = bytes_to_intlist(compat_b64decode('mPRD5uHy+nE3qDNY5qi3mA=='))
    cipher = bytes_to_intlist(compat_b64decode('gB8x/xH/j2AL6zYgPJj8s+svo6UQT1TZV7Tg8PxWVlw='))

    assert aes_cbc_decrypt(cipher, key, iv) == bytes_to_intlist(compat_b64decode('B'))

# Generated at 2022-06-14 15:10:18.733803
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    """
    Test aes_cbc_encrypt using example from
    http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf

    Appendix F.2.2 CBC-AES128.Encrypt
    """
    key_bytes = bytes_to_intlist(compat_b64decode(b"zLF6/bY/Y1RZdAkKj8p/Ng=="))
    iv_bytes = bytes_to_intlist(compat_b64decode(b"Fw4TygHs/55nopmjmpmbgw=="))
    data_bytes = bytes_to_intlist(
        b"Single block msg")


# Generated at 2022-06-14 15:10:30.054756
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    iv = bytes_to_intlist('000102030405060708090A0B0C0D0E0F')
    cipher = bytes_to_intlist('7649ABAC8119B246CEE98E9B12E9197D8964E0B149B078E3'
        + '905A14EDABA754A26')
    plain = bytes_to_intlist('6bc1bee22e409f96e93d7e117393172a')
    assert aes_cbc_decrypt(cipher, key, iv) == plain


# Encryption functions


# Generated at 2022-06-14 15:10:38.498629
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = compat_b64decode('gCfR35U6pYxyiE64UoGk2g==')
    iv = compat_b64decode('y0xuP7IbPYdwj0rMZC6OnQ==')
    cypher = compat_b64decode('ZjzWyaBfCg6R9X6HmU6mKjz5C5DGs/n/nZrHHeZ/kwk=')
    print("hello")
    print('\n'.join('{:02x}'.format(x) for x in aes_cbc_decrypt(cypher, key, iv)))
    return 



# Generated at 2022-06-14 15:10:50.193762
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]

# Generated at 2022-06-14 15:10:58.494088
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes_list = [16, 24, 32]

    for key_size_bytes in key_size_bytes_list:
        expanded_key_size_bytes = (key_size_bytes // 4 + 7) * BLOCK_SIZE_BYTES
        expanded_key = key_expansion(bytes([i for i in range(key_size_bytes)]))
        assert len(expanded_key) == expanded_key_size_bytes

# Generated at 2022-06-14 15:11:05.533232
# Unit test for function key_expansion
def test_key_expansion():
    # key = [0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C]
    key = bytes_to_intlist(compat_b64decode('KM6D/4fX9eyI8P06WUafPg=='))
    print(len(key))
    print([hex(x).upper()[2:] for x in key_expansion(key)])
    return 0

# Generated at 2022-06-14 15:11:16.686661
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('vip8WxEO17o/d+Yev1M7vXGmD+z6EClF'))
    expected = bytes_to_intlist(compat_b64decode('vip8WxEO17o/d+Yev1M7vXGmD+z6EClFS6o3BaV3F4ZEyN/2dmOna/J/aI3Zrse/b1ppcJYlYkANWIgNfCkws='))
    assert key_expansion(key) == expected


# Unit tests for function key_schedule_core

# Generated at 2022-06-14 15:11:26.307828
# Unit test for function key_expansion
def test_key_expansion():
    KEY_TEXT = 'pqc9XFvPH36QYnM3q3h1/WQSj/wPtGD5'
    KEY = bytes_to_intlist(compat_b64decode(KEY_TEXT))


# Generated at 2022-06-14 15:11:32.857685
# Unit test for function key_expansion
def test_key_expansion():
    if not test_key_expansion:
        return
    key = bytes_to_intlist(compat_b64decode('CK7XJx09bqcFv3qwEJ3Lh62kOiXOyRzu'))
    expanded_key = key_expansion(key)
    assert intlist_to_bytes(expanded_key) == compat_b64decode('CK7XJx09bqcFv3qwEJ3Lh62kOiXOyRzuA4IbVCn4QZHV7ZuwWpIH7F1S6p9v6Uy3')



# Generated at 2022-06-14 15:11:42.996595
# Unit test for function key_expansion

# Generated at 2022-06-14 15:11:50.126962
# Unit test for function key_expansion
def test_key_expansion():
    print("Testing key_expansion")

# Generated at 2022-06-14 15:12:01.917832
# Unit test for function key_expansion
def test_key_expansion():
    import hashlib
    def md5(data):
        m = hashlib.md5()
        m.update(intlist_to_bytes(data))
        return bytes_to_intlist(m.digest())

    key_sizes = [16, 24, 32]
    keys = [
        md5([i % 256 for i in range(key_size * 8)])
        for key_size in key_sizes
    ]

# Generated at 2022-06-14 15:12:14.857918
# Unit test for function key_expansion
def test_key_expansion():
    # key_expansion
    key = [0x10, 0x32, 0x54, 0x76, 0x98, 0xba, 0xdc, 0xfe, 0x87, 0x65, 0x43, 0x21, 0xf0, 0xde, 0xbc, 0x9a]

# Generated at 2022-06-14 15:12:22.927299
# Unit test for function key_expansion
def test_key_expansion():
    K = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:12:35.351974
# Unit test for function key_expansion
def test_key_expansion():
    global BLOCK_SIZE_BYTES
    BLOCK_SIZE_BYTES = 16
    global AES_SBOX

# Generated at 2022-06-14 15:12:47.795615
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:57.383890
# Unit test for function key_expansion
def test_key_expansion():
    # Test for key_size_bytes == 16
    data = bytes_to_intlist(b'\x21\x31\x75\x34\x0e\x76\x8d\x9e\xc7\x40\x75\x77\x51\x00\x00\x00')
    assert(data == [33, 49, 117, 52, 14, 118, 141, 158, 199, 64, 117, 119, 81])
    data = key_expansion(data)

# Generated at 2022-06-14 15:13:09.976139
# Unit test for function key_expansion
def test_key_expansion():
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 176

# Generated at 2022-06-14 15:13:21.517180
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test key expansion
    """

# Generated at 2022-06-14 15:13:32.192290
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03,
           0x04, 0x05, 0x06, 0x07,
           0x08, 0x09, 0x0a, 0x0b,
           0x0c, 0x0d, 0x0e, 0x0f]
    print("# AES-128")
    print("Key expansion, 128-bit key:")
    print(hex(key_expansion(key)))

    key.extend([0x10, 0x11, 0x12, 0x13])
    print("\n# AES-192")
    print("Key expansion, 192-bit key:")
    print(hex(key_expansion(key)))

    key.extend([0x14, 0x15, 0x16, 0x17])


# Generated at 2022-06-14 15:13:43.615703
# Unit test for function key_expansion
def test_key_expansion():
    data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Generated at 2022-06-14 15:13:53.500823
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:03.471583
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')

# Generated at 2022-06-14 15:14:11.593879
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:27.755361
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:39.687627
# Unit test for function key_expansion
def test_key_expansion():
    import random
    import binascii

    def sub_nibbles(n1, n2):
        return ((n1 % 16) - (n2 % 16)) % 16, ((n1 // 16) - (n2 // 16)) % 16

    def check_uint16(key, key_size, one_key_size, round_keys):
        # check invertibility
        round_keys = round_keys[:]  # make a copy
        for i in range(len(round_keys)):
            round_keys[i] = intlist_to_bytes(round_keys[i])
        for i in range(10):
            plain_text = b'\x00' * 16
            cipher_text = encrypt(plain_text, key_size, key, one_key_size, round_keys)
            plain_text_

# Generated at 2022-06-14 15:14:52.345599
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:02.222606
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode(
        b'hJY7Ze1GzfjF7PuLzWZNkg=='
    ))
    key_size = 16

# Generated at 2022-06-14 15:15:11.644490
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'1234123412341234')
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:15:23.039182
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode("CziLjkDr2RtROVlHZ1w3dw=="))
    result = bytes_to_intlist(compat_b64decode("qm7nUeT8U6i2u6G+RV7/BXQrztmxN90rKRfzI7Dvo/Nw/JEZu+/lIYTToyr2XJjxG+HuIybeO7yvDpZBpEJg04fZ+Y7MhhE1X+a7HlCPrq0p+l0JF6o7657cTQ2QT+0V"))
    assert key_expansion(key) == result



# Generated at 2022-06-14 15:15:31.857203
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:44.481730
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes = 16
    key = KEY_SIZE_BYTES*[0x00]
    expanded_key_size_bytes = 176
    expanded_key = key_expansion(key)
    assert(len(key)==key_size_bytes)
    assert(len(expanded_key)==expanded_key_size_bytes)

    key_size_bytes = 24
    key = KEY_SIZE_BYTES*[0x00]
    expanded_key_size_bytes = 208
    expanded_key = key_expansion(key)
    assert(len(key)==key_size_bytes)
    assert(len(expanded_key)==expanded_key_size_bytes)

    key_size_bytes = 32
    key = KEY_SIZE_BYTES*[0x00]
   

# Generated at 2022-06-14 15:15:53.862506
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode(b'Rk5H5p5xGxrzDg2aw6+3q6g=='))

# Generated at 2022-06-14 15:15:57.860228
# Unit test for function key_expansion
def test_key_expansion():
    # Taken from http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf
    # Appendix F.5 AES-192 Key Expansion
    data = bytes_to_intlist(compat_b64decode(b'u/2xDaV7PuDvMJ8V+ZDqmZFzfBfLdTlFbTqe3Tf+y68='))

# Generated at 2022-06-14 15:16:16.638276
# Unit test for function key_expansion
def test_key_expansion():
    data = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:16:25.982942
# Unit test for function key_expansion
def test_key_expansion():
    result = key_expansion(b'\x54\x68\x61\x74\x73\x20\x6D\x79\x20\x4B\x75\x6E\x67\x20\x46\x75')

# Generated at 2022-06-14 15:16:31.434000
# Unit test for function key_expansion
def test_key_expansion():
    # key expansion with different size keys
    key = bytes_to_intlist(compat_b64decode('gNkkNuxhGSABARO1H8OSGg=='))
    assert len(key) == 16  # 128-bit-key
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 176  # is expanded to 176 bytes

    key = bytes_to_intlist(compat_b64decode('7xUiAz1cw7QmFm/uV7mE5Q=='))
    assert len(key) == 24  # 192-bit-key
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 208  # is expanded to 208 bytes


# Generated at 2022-06-14 15:16:43.149247
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:50.991494
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:01.476013
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:09.289829
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    key_expansion_result = key_expansion(key)

# Generated at 2022-06-14 15:17:20.681232
# Unit test for function key_expansion
def test_key_expansion():
    print('Test key expansion')
    assert key_expansion(bytes_to_intlist(compat_b64decode(b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH'))) == bytes_to_intlist(compat_b64decode(b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ111122223333444455556666777788889999aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooo'))