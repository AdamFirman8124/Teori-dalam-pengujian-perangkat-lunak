

# Generated at 2022-06-14 15:07:42.439074
# Unit test for function aes_encrypt
def test_aes_encrypt():
    data = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:07:50.814752
# Unit test for function inc
def test_inc():
    assert inc([0x00, 0x00, 0x00, 0x00]) == [0x00, 0x00, 0x00, 0x01]
    assert inc([0x00, 0x00, 0x00, 0xFF]) == [0x00, 0x00, 0x01, 0x00]
    assert inc([0x00, 0x00, 0xFF, 0xFF]) == [0x00, 0x01, 0x00, 0x00]
    assert inc([0x00, 0xFF, 0xFF, 0xFF]) == [0x01, 0x00, 0x00, 0x00]
    assert inc([0xFF, 0xFF, 0xFF, 0xFF]) == [0x00, 0x00, 0x00, 0x00]

# Generated at 2022-06-14 15:07:58.697296
# Unit test for function aes_decrypt
def test_aes_decrypt():
    # given
    cipher = bytes_to_intlist(compat_b64decode('smKLHV7QA9gYiIeBkf0+qA=='))
    key = bytes_to_intlist('YELLOW SUBMARINE')
    expanded_key = key_expansion(key)

    # when
    result = aes_decrypt(cipher, expanded_key)

    # then
    assert intlist_to_bytes(result) == b'abcdefghijklmnop'



# Generated at 2022-06-14 15:08:04.946370
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    encrypted = bytes_to_intlist(compat_b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='))
    key = bytes_to_intlist(compat_b64decode('YELLOW SUBMARINE'))
    counter = Counter.from_state([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    assert intlist_to_bytes(aes_ctr_decrypt(encrypted, key, counter)) == b'Yo, VIP Let\'s kick it Ice, Ice, baby Ice, Ice, baby '


# Generated at 2022-06-14 15:08:06.794040
# Unit test for function inc
def test_inc():
    data = [255, 255, 255]
    data_next = inc(data)
    assert data_next == [255, 255, 0]



# Generated at 2022-06-14 15:08:15.457049
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
# Function input arguments initialized
    data = bytes_to_intlist(b'\x54\x68\x69\x73\x20\x69\x73\x20\x61\x20\x74\x65\x73\x74\x20\x6d\x65\x73\x73\x61\x67\x65\x20\x70\x61\x64\x64\x65\x64\x20\x77\x69\x74\x68\x20\x70\x61\x64\x64\x69\x6e\x67')

# Generated at 2022-06-14 15:08:23.716932
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    data = [0x76, 0x49, 0xab, 0xac, 0x81, 0x19, 0xb2, 0x46, 0xce, 0xe9, 0x8e, 0x9b, 0x12, 0xe9, 0x19, 0x7d]

    expanded_key = key_expansion(key)
    result = aes_decrypt(data, expanded_key)


# Generated at 2022-06-14 15:08:30.793538
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = [int(d, 16) for d in '7649abac8119b246cee98e9b12e9197d'.split()]
    key = [int(d, 16) for d in '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'.split()]
    expanded_key = key_expansion(key)
    print(aes_decrypt(data, expanded_key))



# Generated at 2022-06-14 15:08:36.137998
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    if __name__ == '__main__':
        data = '9XHyiF/Nk/j45BupwZMVaIx/nh6UHKe6+AOMyX9/QkM='
        password = 'Md5Be5r5rKj5p3qe3qH26qH2'
        key_size_bytes = 16

        print(aes_decrypt_text(data, password, key_size_bytes))


matrix_to_bytes = bytes_to_intlist
bytes_to_matrix = intlist_to_bytes



# Generated at 2022-06-14 15:08:46.232355
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(b'1234567890123456')
    iv = bytes_to_intlist(b'ABCDEFGHIJKLMNOP')
    data = bytes_to_intlist(b'qwerqwerqwerqwerqwerqwerqwerqwer')

    encrypted1 = aes_cbc_encrypt(data[:15], key, iv)
    encrypted2 = aes_cbc_encrypt(data[15:], key, encrypted1)
    assert intlist_to_bytes(encrypted1) == b'\xab\xeb\x8b\x8b\x7f\x84\x0a\x08g\x12\xec\x1d\x95\xde4\x14'

# Generated at 2022-06-14 15:09:01.586680
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode(b'C9l2Bh1oxcgq3FmT6TJ2Pg=='))
    result = key_expansion(key)

# Generated at 2022-06-14 15:09:10.187962
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(b'1234567890123456')
    iv = bytes_to_intlist(b'1234567890123456')
    decrypted_data = bytes_to_intlist(b'\x00decrypted_data\x00')
    encrypted_data = bytes_to_intlist(b'\x00encrypted_data\x00')
    assert aes_cbc_encrypt(decrypted_data, key, iv) == encrypted_data
    assert aes_cbc_decrypt(encrypted_data, key, iv) == decrypted_data



# Generated at 2022-06-14 15:09:21.705753
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    iv = intlist_to_bytes(bytes_to_intlist(compat_b64decode(
        b"f2/v6/WUHhycFuKjxzgzqg==")))
    key = intlist_to_bytes(bytes_to_intlist(compat_b64decode(
        b"f2/v6/WUHhycFuKjxzgzqg==")))

# Generated at 2022-06-14 15:09:32.894550
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Test case where data has one full block
    data = bytes_to_intlist(b'w\xa7\xab\x8b\x16\xb3\xad\x917l\xf3\xd3\x84')

# Generated at 2022-06-14 15:09:37.348855
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    #print("Testing function aes_cbc_decrypt...", end="")

    # Test vectors from https://csrc.nist.gov/publications/detail/sp/800-38a/final

    # Key = "2b7e151628aed2a6abf7158809cf4f3c" (hex-encoded)
    key = "2b7e151628aed2a6abf7158809cf4f3c".decode('hex_codec')
    key = bytes_to_intlist(key)

    # IV =  "000102030405060708090a0b0c0d0e0f" (hex-encoded)
    iv = "000102030405060708090a0b0c0d0e0f".decode('hex_codec')


# Generated at 2022-06-14 15:09:49.511559
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    print('TEST: aes_cbc_decrypt')

    # Test vectors from
    # https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29

# Generated at 2022-06-14 15:10:00.578207
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:10:10.640381
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode("gX9XuF6c+U6xJwg8/vnRZu0dZjXT32FqPR4vYQ9L1x4="))
    iv = bytes_to_intlist(compat_b64decode("W8iHM9h7lFAs+dftQxwW8w=="))
    data = bytes_to_intlist(compat_b64decode("IniNt/xhIw8/LNzFm1fZD5FZpCe5YIY9NEDc5iHr5w5L5l5QgD/H6Z+aNg2M9F4q"))

# Generated at 2022-06-14 15:10:23.357290
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:10:34.976777
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee"
                            "2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
    expected = bytes_to_intlist("Basic CBC mode encryption needs padding.") + [17] * 15
    key = bytes_to_intlist("140b41b22a29beb4061bda66b6747e14")
    iv = bytes_to_intlist("4ca00ff4c898d61e1edbf1800618fb28")
    assert expected == aes_cbc_decrypt(data, key, iv)



# Generated at 2022-06-14 15:10:49.605868
# Unit test for function key_expansion
def test_key_expansion():
    # 16-Byte key
    cleartext = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Generated at 2022-06-14 15:10:57.971133
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:11:05.536541
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:11:18.205584
# Unit test for function key_expansion

# Generated at 2022-06-14 15:11:27.461350
# Unit test for function key_expansion

# Generated at 2022-06-14 15:11:35.098730
# Unit test for function key_expansion
def test_key_expansion():
    """ Assert that key_expansion() works as expected. """

# Generated at 2022-06-14 15:11:47.458688
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:00.313471
# Unit test for function key_expansion
def test_key_expansion():
    def test_key_expansion_helper(key):
        key = bytes_to_intlist(compat_b64decode(key))
        expanded = key_expansion(key)
        return bytes_to_intlist(compat_b64decode(expanded))

    # 1. Test vectors from NIST Special Publication 800-38a (2001),
    #    Appendix F.1.1, AES-128 (http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf)
    key = '2b7e151628aed2a6abf7158809cf4f3c'

# Generated at 2022-06-14 15:12:13.116429
# Unit test for function key_expansion
def test_key_expansion():
    key = intlist_to_bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F])
    test_key = intlist_to_bytes([0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63])
    expanded_key = key_expansion(key)
    assert expanded_key == test_key, "key_expansion failed"

# Generated at 2022-06-14 15:12:21.995057
# Unit test for function key_expansion
def test_key_expansion():
    test_key = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
    pwd = 'Password1'

# Generated at 2022-06-14 15:12:34.755323
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:47.246308
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    assert intlist_to_bytes(key_expansion(key)) == b'2b7e151628aed2a6abf7158809cf4f3c762e7160363da5e789af0d62b6a7b13c'

    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c762e7160363da5e789af0d62b6a7b13c')

# Generated at 2022-06-14 15:12:53.915953
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:06.934250
# Unit test for function key_expansion
def test_key_expansion():
    # 16 Byte key
    key1 = bytes_to_intlist(compat_b64decode('C6j1i+TbTpsvY9o7nL8PDQ=='))
    key_schedule1 = key_expansion(key1)
    expected_key_schedule1 = bytes_to_intlist(compat_b64decode(
        'C6j1i+TbTpsvY9o7nL8PDQm7gOiTm8HJw/fzNSGW2t/9/yJ8hOERuGHtNBLl7VuC3qwsr7wLJp4='))
    assert key_schedule1 == expected_key_schedule1

    # 24 Byte key

# Generated at 2022-06-14 15:13:19.123812
# Unit test for function key_expansion
def test_key_expansion():
    def test_one(key, answer):
        assert key_expansion(bytes_to_intlist(compat_b64decode(key))) == answer


# Generated at 2022-06-14 15:13:30.335065
# Unit test for function key_expansion
def test_key_expansion():
    assert key_expansion([0] * 16) == [0] * 240
    assert key_expansion([0] * 24) == [0] * 208
    assert key_expansion([0] * 32) == [0] * 176

# Generated at 2022-06-14 15:13:41.854988
# Unit test for function key_expansion
def test_key_expansion():
    if test_key_expansion.counter == 0:
        test_key_expansion.counter = 1
        return
    key = aes_decrypt(
        bytes_to_intlist(compat_b64decode(b'CK7UhLitwNxNP3QsjKXarA==')),
        bytes_to_intlist(compat_b64decode(b'CK7UhLitwNxNP3QsjKXarA==')))

# Generated at 2022-06-14 15:13:52.563225
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:02.666005
# Unit test for function key_expansion
def test_key_expansion():
    import binascii
    key_16 = bytes_to_intlist(binascii.unhexlify('00010203050607080a0b0c0d0f101112'))
    key_24 = bytes_to_intlist(binascii.unhexlify('00010203050607080a0b0c0d0f10111214151617'))
    key_32 = bytes_to_intlist(binascii.unhexlify('00010203050607080a0b0c0d0f1011121415161719202122'))

    expanded_key_16 = key_expansion(key_16)
    expanded_key_24 = key_expansion(key_24)
    expanded_key_32 = key_expansion(key_32)

   

# Generated at 2022-06-14 15:14:11.073860
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:01.048530
# Unit test for function key_expansion
def test_key_expansion():
    import random
    import binascii
    for i in range(10):
        key = [random.randint(0,255) for _ in range(random.randint(16,32))]
        result = key_expansion(key)
        assert len(result) % 16 == 0
        print(binascii.b2a_hex(intlist_to_bytes(result)))


# Generated at 2022-06-14 15:15:09.160083
# Unit test for function key_expansion
def test_key_expansion():
    password = 'password'
    password = compat_b64decode(password)
    password = bytes_to_intlist(password)
    expected_result = 'NX9lk/Zwk/RLl+/zc7V/jGqtm3JxohxVEtbnm7VX9c8='
    expected_result = compat_b64decode(expected_result)
    expected_result = bytes_to_intlist(expected_result)
    result = key_expansion(password)
    assert result == expected_result
# End unit test for function key_expansion
test_key_expansion()                              # run test


# Generated at 2022-06-14 15:15:20.745443
# Unit test for function key_expansion
def test_key_expansion():
    import binascii
    assert binascii.hexlify(bytes(key_expansion(bytes_to_intlist(b'\x00' * 16)))) == b'000102030405060708090a0b0c0d0e0f10111213141516175846f2c880978c33f2cc8b638e50e0a6760d7f0007f0777872c90a0800000000'

# Generated at 2022-06-14 15:15:25.473658
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(b"2b7e151628aed2a6abf7158809cf4f3c")
    actual = key_expansion(data)

# Generated at 2022-06-14 15:15:33.120409
# Unit test for function key_expansion
def test_key_expansion():
    """
    Tests for AES key expansion. Uses:

    http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    """
    # Key sizes from 128 bit to 256 bit
    key_sizes = [16, 24, 32]
    for key_size_bytes in key_sizes:
        # Key from NIST example
        key = compat_b64decode(
            'h/TKH+RkwyLDKj+rXbXz8g==')

# Generated at 2022-06-14 15:15:37.307810
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')

# Generated at 2022-06-14 15:15:45.778639
# Unit test for function key_expansion
def test_key_expansion():
    import json
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), 'data', 'expanded_key.json')
    with open(data_file_path) as data_file:
        data = json.load(data_file)
        for key, value in data.items():
            print(key)
            assert key_expansion(bytes_to_intlist(bytes(compat_b64decode(key)))) == [int(i) for i in value]


# Generated at 2022-06-14 15:15:50.876102
# Unit test for function key_expansion
def test_key_expansion():
    import binascii

    cipher_key = "00010203050607080A0B0C0D0F10111214151617191A1B1C1E1F20".encode('ascii')
    cipher_key = bytes_to_intlist(cipher_key)

# Generated at 2022-06-14 15:16:00.770444
# Unit test for function key_expansion
def test_key_expansion():
    from .utils import intlist_to_hex, hex_to_intlist

    # Test for 16-Byte key
    result = key_expansion([0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe,
                            0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81])

# Generated at 2022-06-14 15:16:07.382774
# Unit test for function key_expansion
def test_key_expansion():
    for key_length in (16, 24, 32):
        for i in range(100):
            key = [key_length] * key_length
            key_decimal = bytes_to_intlist(compat_b64decode(b'z' * key_length))
            assert key_expansion(key) == key_expansion(key_decimal)

    print('key_expansion: OK')



# Generated at 2022-06-14 15:16:26.800269
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15,
        0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:16:37.056237
# Unit test for function key_expansion
def test_key_expansion():
    # Test 1
    key = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')

# Generated at 2022-06-14 15:16:47.272081
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:16:58.812266
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:07.569646
# Unit test for function key_expansion
def test_key_expansion():
    key16 = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c') # 16-Byte cipher key
    key24 = bytes_to_intlist('8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b') # 24-Byte cipher key
    key32 = bytes_to_intlist('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4') # 32-Byte cipher key


# Generated at 2022-06-14 15:17:19.512488
# Unit test for function key_expansion
def test_key_expansion():
    keys = [
        # 16-Byte
        '2B7E151628AED2A6ABF7158809CF4F3C',
        # 24-Byte
        '8E73B0F7DA0E6452C810F32B809079E562F8EAD2522C6B7B',
        # 32-Byte
        '6028CBF2195C856F97C5AD5C5E5BCE48EC8762C5AC94E08',
    ]