

# Generated at 2022-06-14 15:07:39.343927
# Unit test for function inc
def test_inc():
    print('Testing increment function')
    print(inc([0, 0, 0, 0]))
    print(inc([0, 0, 0, 1]))
    print(inc([0, 0, 1, 255]))
    print(inc([1, 0, 0, 0]))
    print(inc([255, 255, 255, 255]))
    print('------------------------')



# Generated at 2022-06-14 15:07:48.716880
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    """
    Testcase from http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf

    Example 7: Decryption Process
    """
    data = bytes_to_intlist(compat_b64decode(
        b'8W15pw0uV7fEwrb0/V8WfE1/La0/V9q3qw=='))
    key = bytes_to_intlist(compat_b64decode(
        b'81dMqog3yc+WwzJjPxLruA=='))
    iv = bytes_to_intlist(compat_b64decode(
        b'f7VdHm1ZhSbYmEf/'))

# Generated at 2022-06-14 15:07:59.934168
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:08:02.500503
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    text = 'KpXO8fzGcE+RJxzkM6hKwg=='
    password = 'Password'
    key_size_bytes = 16
    result = aes_decrypt_text(text, password, key_size_bytes)
    print(result)


# Generated at 2022-06-14 15:08:12.958920
# Unit test for function key_expansion

# Generated at 2022-06-14 15:08:22.363016
# Unit test for function aes_encrypt

# Generated at 2022-06-14 15:08:27.697568
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    aes_decrypt_text(
        'LP1TbTvn0nIeZ+jRyeWg/8j+UK0pkByH/85Rmwga8tM=',
        'Yt1m2tW/j8Qv7GbYoN5c5A==',
        24
    )

    print('Unit test passed')


if __name__ == '__main__':
    test_aes_decrypt_text()



# Generated at 2022-06-14 15:08:36.082880
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    key = "password"
    key_size = 32
    nonce = 8 * b"\x00"  # 8 Bytes (64 bit)
    cipher = aes_decrypt_text(b"iWQ5Z5v5fzY=", key, key_size)

    assert cipher == "Test"
    assert aes_decrypt_text(b"iWQ5Z5v5fzY=", "wrong_password", key_size) != "Test"
    assert aes_decrypt_text(b"iWQ5Z5v5fzY=", key, 16) != "Test"
    assert aes_decrypt_text(b"iWQ5Z5v5fzY=", key, 24) != "Test"

# Generated at 2022-06-14 15:08:38.371762
# Unit test for function inc
def test_inc():
    assert(inc([0]*16) == [1] * 16)
    assert(inc([0]*15 + [255]) == [1] * 16)
    assert(inc([255]*16) == [0] * 16)



# Generated at 2022-06-14 15:08:43.203276
# Unit test for function inc
def test_inc():
    data = [0xFF, 0x00, 0x10]
    for i in range(4):
        print(data)
        data = inc(data)
        assert len(data) == 3
    data = [0xFF, 0xFF, 0xFF]
    for i in range(4):
        print(data)
        data = inc(data)
        assert len(data) == 3



# Generated at 2022-06-14 15:08:53.855512
# Unit test for function aes_decrypt
def test_aes_decrypt():

    # keytest
    key_test = intlist_to_bytes([
        0x4a, 0x5d, 0x9d, 0x5b, 0xa4, 0xce, 0x2d, 0xe1, 0x72, 0x8e, 0x3b, 0xf4, 0x80, 0x35, 0x0f, 0x25
    ])
    
    # datatest
    data_test = intlist_to_bytes([
        0x36, 0x90, 0x42, 0x40, 0x88, 0x78, 0xb9, 0xf9, 0xed, 0x3d, 0x62, 0x3e, 0x97, 0x76, 0x9e, 0xe0
    ])

    key_expand = aes_cbc_enc

# Generated at 2022-06-14 15:09:02.102889
# Unit test for function aes_decrypt
def test_aes_decrypt():
    test_data = ['25', 'D7', '25', '2C', 'E0', '14', 'FF', 'B3', '3F', 'C0', '51', '72', 'D6', '75', '61', '83']
    data = [int(test_data[i], 16) for i in range(16)]
    expanded_key = [int(test_data[i], 16) for i in range(16, 176)]
    assert bytes_to_intlist(compat_b64decode(b'0TaQKj05xOsS1OnJBpYfUg==')) == aes_decrypt(data, expanded_key)

test_aes_decrypt()



# Generated at 2022-06-14 15:09:12.172948
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # decrypt example 2 from FIPS 197 (AES) using CBC
    key = bytes_to_intlist(compat_b64decode(b"O4fU3&3*3Us3hvf6A3*j1f!6VfU3&3*3"))
    data = bytes_to_intlist(compat_b64decode(b"tZ*9&f#g5dQ1f!gs1tZ*9&f#g5dQ1f!gs"))
    iv = bytes_to_intlist(compat_b64decode(b"j1f!6VfU3&3*3Us3hvf6A3*j1f!6VfU3&"))

    decrypted_data = aes_cbc_decrypt(data, key, iv)
   

# Generated at 2022-06-14 15:09:17.531549
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = bytes_to_intlist(compat_b64decode('V7Q/EtX9VtMAHpO/N3gB3A=='))
    iv = bytes_to_intlist(compat_b64decode('2STFmWKmvCpA+szwCwGl8A=='))
    data = bytes_to_intlist(compat_b64decode('rI+7VrBJx1R7V162cpZVGg=='))
    assert aes_decrypt(data, key) == iv



# Generated at 2022-06-14 15:09:26.676023
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
    key = bytes_to_intlist('140b41b22a29beb4061bda66b6747e14')
    iv = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb28')
    encrypted = aes_cbc_decrypt(data, key, iv)
    assert intlist_to_bytes(encrypted) == b'Basic CBC mode encryption needs padding.'

# Generated at 2022-06-14 15:09:36.508896
# Unit test for function aes_decrypt
def test_aes_decrypt():
    from .key_stream_counter import Counter
    DATA = bytes_to_intlist(bytes(compat_b64decode('Iq2Wlk6feMFw6zA4vIjawSz8U9eZa0nZ')))
    KEY = bytes_to_intlist(bytes(compat_b64decode('d3TlT2LoDjZCd7VuDh24Hg==')))
    IV = bytes_to_intlist(bytes(compat_b64decode('8IjKDfN/2PzO/wc=')))

# Generated at 2022-06-14 15:09:48.803279
# Unit test for function aes_decrypt
def test_aes_decrypt():
    message = intlist_to_bytes([0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37,
                                0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34])


# Generated at 2022-06-14 15:09:57.207934
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:10:02.880991
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = intlist_to_bytes(list(range(16)) + list(range(16)))
    ciphertext = intlist_to_bytes([0] * 16)
    expanded_key = key_expansion(key)
    assert aes_decrypt(bytes_to_intlist(ciphertext), expanded_key) == [0] * 16

# Generated at 2022-06-14 15:10:12.149808
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:10:25.342702
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    message = list(range(0, 39))
    key = list(range(33, 33 + 16))
    iv = list(range(33, 33 + 16))
    print(message)
    print(key)
    print(iv)
    print("Encrypted Message: ")
    message = aes_cbc_encrypt(message, key, iv)
    message = intlist_to_bytes(message)
    print(message)
    print("Decrypted Message: ")
    message = bytes_to_intlist(message)
    message = aes_cbc_decrypt(message, key, iv)
    print(message)



# Generated at 2022-06-14 15:10:36.456434
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:10:49.028950
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    input_str = '12345678901234561234567890123456'
    key_str = '00000000000000000000000000000000'
    iv_str = '00000000000000000000000000000000'
    input_bytes = bytes_to_intlist(input_str.encode('ascii'))
    key = bytes_to_intlist(key_str.encode('ascii'))
    iv = bytes_to_intlist(iv_str.encode('ascii'))
    output_bytes = aes_cbc_encrypt(input_bytes, key, iv)
    cipher_str = 'KQeqxX9vb8O+FkOzp0fjKZf0BZ+wO5U0243JU6hc9p4='

# Generated at 2022-06-14 15:10:57.232035
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:11:06.322239
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist(
        compat_b64decode(b'3qBxEwG6ElMkRfOyhNp9XQ==')
    )
    aes_cbc_encrypt = aes_cbc_encrypt(data, [0] * 32, [0] * 16)
    aes_cbc_encrypt = intlist_to_bytes(aes_cbc_encrypt)
    assert aes_cbc_encrypt == (
        b'\xd8\xdd\x93l;\xcc\xae\xa1\xc5\xd7\xca\xc1\x14\x8b`\xadG\x07C'
    )


# Generated at 2022-06-14 15:11:18.650788
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    test_data = [0] * 16
    key = [0] * 16
    iv = [0] * 16
    # Assert encryption of empty data
    encrypted_data = aes_cbc_encrypt(test_data, key, iv)
    encrypted_data = intlist_to_bytes(encrypted_data)
    assert encrypted_data == b'\x10' * 16

    # Assert encryption of some data
    test_data = [0] * 15
    encrypted_data = aes_cbc_encrypt(test_data, key, iv)
    encrypted_data = intlist_to_bytes(encrypted_data)
    assert encrypted_data == b'\x0f' * 15 + b'\x01'

    # Try with some data and a non-zero key and IV
    iv = [1] * 16

# Generated at 2022-06-14 15:11:23.305040
# Unit test for function key_expansion
def test_key_expansion():
    print('Test function: key_expansion')
    data = bytes_to_intlist(compat_b64decode('/Wu/ZQcGXSi/AJxxbN59o=', True))
    print('data = ', data)
    print('expanded key = ', key_expansion(data))
test_key_expansion()



# Generated at 2022-06-14 15:11:32.209707
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = "My test cleartext"
    cleartext_bytes = [ord(b) for b in cleartext]
    assert cleartext_bytes == [77, 121, 32, 116, 101, 115, 116, 32, 99, 108, 101, 97, 114, 116, 101, 120, 116, 0, 0]

    key = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
           0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10]

# Generated at 2022-06-14 15:11:40.744998
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():

    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:11:49.641856
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(compat_b64decode('OKVRmfL5ZaN0ZmR9AL0YuQ=='))
    iv = bytes_to_intlist(compat_b64decode('Tx+PxD/GvO8dN/K5n5QH+Q=='))
    input_bytes = bytes_to_intlist(compat_b64decode('+eKh3GCGnjPsg+lJYtdfcg=='))
    encrypted_bytes = aes_cbc_encrypt(input_bytes, key, iv)
    assert(intlist_to_bytes(encrypted_bytes) == compat_b64decode('pH6u/SVUc+6UYZk/N2QeHg=='))



# Generated at 2022-06-14 15:12:03.583487
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:15.870668
# Unit test for function key_expansion
def test_key_expansion():
    print("Unit test for function key_expansion")
    # Test with key length 16
    result = key_expansion([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])

# Generated at 2022-06-14 15:12:27.544584
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:36.349344
# Unit test for function key_expansion
def test_key_expansion():
    print("test_key_expansion")

    def _get_key_expansion(key, key_size_bytes, block_size_bytes):
        key = bytes_to_intlist(compat_b64decode(key))
        assert len(key) == key_size_bytes
        expanded_key = key_expansion(key)
        assert len(expanded_key) == (key_size_bytes // 4 + 7) * block_size_bytes
        return expanded_key

    key_size_bytes = 16
    block_size_bytes = 16

    key = ("qC/cJiUUOAAW12pVp0re/w==")
    assert b''.join(map(chr, _get_key_expansion(key, key_size_bytes, block_size_bytes))) == compat_b64dec

# Generated at 2022-06-14 15:12:48.719999
# Unit test for function key_expansion
def test_key_expansion():
    data1 = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    data2 = key_expansion(data1)
    assert intlist_to_bytes(data2[:16]) == '2b7e151628aed2a6abf7158809cf4f3c'
    assert intlist_to_bytes(data2[16:32]) == 'a0fafe1788542cb123a339392a6c7605'
    assert intlist_to_bytes(data2[32:48]) == 'f2c295f27a96b9435935807a7359f67f'

# Generated at 2022-06-14 15:12:58.056931
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:10.222381
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist("2b7e151628aed2a6abf7158809cf4f3c")
    expanded_key = key_expansion(key)
    expanded_key = intlist_to_bytes(expanded_key)

# Generated at 2022-06-14 15:13:21.806287
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7,
           0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:13:32.540494
# Unit test for function key_expansion
def test_key_expansion():
    test_key_expansion_generic(16, "2b7e151628aed2a6abf7158809cf4f3c", "8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b")
    test_key_expansion_generic(24, "8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b", "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")

# Generated at 2022-06-14 15:13:42.302178
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:54.238276
# Unit test for function key_expansion
def test_key_expansion():
    data = [0xA1, 0x68, 0xC8, 0x2A, 0xA4, 0x71, 0xC4, 0x2F, 0x01, 0xBB, 
0x3A, 0x57, 0xA3, 0x7A, 0xC5, 0x21]

# Generated at 2022-06-14 15:14:01.237258
# Unit test for function key_expansion
def test_key_expansion():
    for key in (b'\1' + 16*b'\0', b'\2' + 24*b'\0', b'\3' + 32*b'\0'):
        expanded_key = key_expansion(bytes_to_intlist(key))
        assert len(expanded_key) == 176 or len(expanded_key) == 208 or \
            len(expanded_key) == 240
        assert bytes_to_intlist(key) == expanded_key[:len(key) // 4]
        test_key_expansion_sessionkey(key)



# Generated at 2022-06-14 15:14:10.415582
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:23.524888
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')

# Generated at 2022-06-14 15:14:36.077684
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('C82DBD029F8CAE35DF58478EDB2F3D60'))
    result = bytes_to_intlist(compat_b64decode('C82DBD029F8CAE35DF58478EDB2F3D60F9CECF7211B8B8DDFE2B0B39B26F0F840841D10C0CF1E9D6AC279C0AE47F0DDE2742F081D24DE84F8DE511908D7E93F'))
    #result = [198, 45, 189, 2, 159, 140, 174, 53, 223, 88, 71, 142, 237, 178, 243, 208, 249, 206, 207, 114, 17, 184, 184

# Generated at 2022-06-14 15:14:44.609298
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:56.997704
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test key_expansion
    """
    print("Testing key_expansion")
    key = bytes_to_intlist(compat_b64decode(b'6xE+ztwAVfJh41q7qHEyLA=='))
    expanded_key = bytes_to_intlist(compat_b64decode(b'6xE+ztwAVfJh41q7qHEyLAwbhj0kx1J5m1GWBYm2QcQP/oEzmVDhP/oEzmVDhP/oEzmVDhP/oEzmVDhP/oEzmVDhP/oEzmVDhP/oEzmVDhP/oEzmVDg=='))
    result = key_expansion(key)

# Generated at 2022-06-14 15:15:07.238400
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x8e\x73\xb0\xf7\xda\x0e\x64\x52\xc8\x10\xf3\x2b\x80\x90\x79\xe5\x62\xf8\xea\xd2\x52\x2c\x6b\x7b')

# Generated at 2022-06-14 15:15:14.286277
# Unit test for function key_expansion
def test_key_expansion():
    import random

    key_lengths = [128, 192, 256]
    for _ in range(100):
        key = [random.randint(0, 255) for _ in range(random.choice(key_lengths))]
        expanded_key = key_expansion(key)
        assert len(expanded_key) == len(key) + 4 * (BLOCK_SIZE_BYTES - len(key) % BLOCK_SIZE_BYTES)



# Generated at 2022-06-14 15:15:25.007351
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    key = bytes_to_intlist(compat_b64decode('CpumgtT/U/q3cq/KlF/NQ=='))

    expanded_key = key_expansion(key)
    print(expanded_key)
    print(expeanded_key)
    print(len(expanded_key))
    #expanded_key = bytes_to_intlist(compat_b64decode('AQgBADsB/X8H+/4F/f4Asf

# Generated at 2022-06-14 15:15:44.333975
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:15:53.760122
# Unit test for function key_expansion
def test_key_expansion():
    import unittest
    class TestKeyExpansion(unittest.TestCase):
        def test_key_expansion(self):
            import binascii
            for key_size in (16, 24, 32):
                with self.subTest(key_size=key_size):
                    key = intlist_to_bytes(range(key_size))
                    expanded_key = key_expansion(bytes_to_intlist(key))

# Generated at 2022-06-14 15:16:02.195055
# Unit test for function key_expansion
def test_key_expansion():
    # AES 128
    test_key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:16:12.790330
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:24.629942
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test case from FIPS 197 A.5.
    """
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:16:28.266650
# Unit test for function key_expansion
def test_key_expansion():
    key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    key = key_expansion(key)
    assert key == list(range(176))


# Generated at 2022-06-14 15:16:38.063255
# Unit test for function key_expansion
def test_key_expansion():
    import unittest
    class TestKeyExpansion(unittest.TestCase):
        def test_key_expansion_128bit(self):
            data = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')

# Generated at 2022-06-14 15:16:47.884627
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:59.223661
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:17:07.866388
# Unit test for function key_expansion
def test_key_expansion():
    key_16 = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]