

# Generated at 2022-06-14 15:07:34.368402
# Unit test for function aes_decrypt
def test_aes_decrypt():
    # Test vector from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    data = bytes_to_intlist(b'\x32\x43\xf6\xa8\x88\x5a\x30\x8d\x31\x31\x98\xa2\xe0\x37\x07\x34')

# Generated at 2022-06-14 15:07:43.349448
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = bytes_to_intlist('0123456789abcdef')
    key = bytes_to_intlist('000102030405060708090a0b0c0d0e0f')
    expanded_key = key_expansion(key)
    cipher = aes_encrypt(data, expanded_key)
    assert intlist_to_bytes(aes_decrypt(cipher, expanded_key)) == '0123456789abcdef'
    assert intlist_to_bytes(aes_decrypt(cipher, expanded_key)) == '0123456789abcdef'
    # from https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf

# Generated at 2022-06-14 15:07:52.011132
# Unit test for function inc
def test_inc():
    assert inc([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    assert inc([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Generated at 2022-06-14 15:08:00.330768
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = bytes_to_intlist(compat_b64decode('QlpoOTFBWSZTWQYhAAoAAAACAAAAIAAAAAEAAAwABAAgAAAAAAAAAAW8BAEAAAD/////'))
    expanded_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert aes_decrypt(data, expanded_key) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Generated at 2022-06-14 15:08:07.124790
# Unit test for function aes_encrypt
def test_aes_encrypt():
    """
    Test aes-encrypt and aes-decrypt

    @returns {bool}  True, if unit test passed
    """

# Generated at 2022-06-14 15:08:16.362282
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:08:24.301396
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = [0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34]
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:08:33.502807
# Unit test for function aes_decrypt
def test_aes_decrypt():
    enc_data = bytes_to_intlist("JDEwJDJhJDEwJDE2JDE2JDA2JDA3JDJhJDEyJDFlJDExJDExJDExJDExJDExJDExJDExJDExJDEzJDEzJDEz")
    key = bytes_to_intlist("QVNzd29yZDEyMzQ1Njc4OTA=")
    iv = bytes_to_intlist("JDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEwJDEw")

# Generated at 2022-06-14 15:08:44.514699
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class MockCounter(object):
        def __init__(self):
            self.index = 0
            self.blocks = [
                [0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77],
                [0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10, 0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef]
            ]

        def next_value(self):
            index = self.index
            block = self.blocks[index]
            self.index += 1

# Generated at 2022-06-14 15:08:56.177810
# Unit test for function key_expansion
def test_key_expansion():
    """ Test function key_expansion """
    key1 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:09:13.589811
# Unit test for function aes_ctr_decrypt

# Generated at 2022-06-14 15:09:24.582918
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    def test_for_password(password):
        for key_size_bytes in [16, 24, 32]:
            key = password[:key_size_bytes] + [0] * (key_size_bytes - len(password))
            key = aes_encrypt(key[:BLOCK_SIZE_BYTES], key_expansion(key)) * (key_size_bytes // BLOCK_SIZE_BYTES)

            class Counter(object):
                __value = [0] * BLOCK_SIZE_BYTES

                def next_value(self):
                    temp = self.__value
                    self.__value = inc(self.__value)
                    return temp


# Generated at 2022-06-14 15:09:31.618237
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode(u'K7gNU3sdo+OL0wNhqoVWhr3g6s1xYv72ol/pe/Unols='))
    iv = [0] * 16
    data = bytes_to_intlist(u'7cUZCGk87WG+8Jb9X+zTQ3qr3WdYMDT1M37kHHR+RApIoAz/Kl9OR9E17NxRpARy'.encode('ascii'))

    result = aes_cbc_decrypt(data, key, iv)
    assert result == bytes_to_intlist(u'for true believers only'.encode('ascii'))



# Generated at 2022-06-14 15:09:39.239628
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .utils import hex_to_intlist
    class Counter(object):
        def __init__(self, iv):
            self._iv = iv

        def next_value(self):
            v = self._iv
            self._iv = self._iv[1:] + [self._iv[0] + 1]
            return v

    data = hex_to_intlist('69c4e0d86a7b0430d8cdb78070b4c55a')
    key = hex_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    iv = hex_to_intlist('f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff')

# Generated at 2022-06-14 15:09:50.919010
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    # taken from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    cleartext = '6bc1bee22e409f96e93d7e117393172a' \
                'ae2d8a571e03ac9c9eb76fac45af8e51' \
                '30c81c46a35ce411e5fbc1191a0a52ef' \
                'f69f2445df4f9b17ad2b417be66c3710'
    cleartext = bytes_to_intlist(compat_b64decode(cleartext))
    key = '2b7e151628aed2a6abf7158809cf4f3c'

# Generated at 2022-06-14 15:10:02.512540
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = '09080706050403020100A2B2C2D2E2F101112131415161718191A1B1C1D1E1F'.decode('hex')
    key = '000102030405060708090A0B0C0D0E0F'.decode('hex')
    iv = 'FEDCBA9876543210FEDCBA9876543210'.decode('hex')

    data = bytes_to_intlist(data)
    key = bytes_to_intlist(key)
    iv = bytes_to_intlist(iv)

    res = aes_cbc_encrypt(data, key, iv)

# Generated at 2022-06-14 15:10:08.585842
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(compat_b64decode('V7uZp+I9XC3qcGnZFtYbYw=='))
    iv = bytes_to_intlist(compat_b64decode('ZW0oGfp0o2P2mDQDK8y1mQ=='))
    data = bytes_to_intlist(compat_b64decode('B/7lNCfNpj5deVF6U4KjUg=='))

    encrypted_data = aes_cbc_encrypt(data, key, iv)
    encrypted_data = intlist_to_bytes(encrypted_data)
    encrypted_data = compat_b64encode(encrypted_data)

# Generated at 2022-06-14 15:10:21.068335
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .aes_cbc_encrypt import aes_cbc_encrypt
    from .counter import Counter
    from .keystream import Keystream
    key = [
        0, 1, 2, 3, 4, 5, 6, 7,
        8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31
    ]
    iv = [
        4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4
    ]
    counter = Counter(iv)
    keystream = Keystream(key)


# Generated at 2022-06-14 15:10:33.409942
# Unit test for function inc
def test_inc():
    data = [255,255,255,255,255,255]
    assert(inc(data) == [255,255,255,255,255,0])
    assert(inc(data) == [255,255,255,255,1,0])
    assert(inc(data) == [255,255,255,255,2,0])
    assert(inc(data) == [255,255,255,255,3,0])
    assert(inc(data) == [255,255,255,255,4,0])
    assert(inc(data) == [255,255,255,255,5,0])
    assert(inc(data) == [255,255,255,255,6,0])
    assert(inc(data) == [255,255,255,255,7,0])

# Generated at 2022-06-14 15:10:44.995933
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = bytes_to_intlist(compat_b64decode("uNE7hRzwFJ8="))
    key = bytes_to_intlist(compat_b64decode("r5rzr5rzr5rzr5rz"))
    iv = bytes_to_intlist(compat_b64decode("K7UVwgtyNx8hc6Ge"))
    cipher = bytes_to_intlist(compat_b64decode("z1wAepn+m4b2Q4mBn4iWn4P6v4U6m4S6unYbWwHP0YE="))

    assert aes_cbc_encrypt(cleartext, key, iv) == cipher



# Generated at 2022-06-14 15:10:58.309341
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:11:01.074209
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    result = aes_decrypt_text('3W8NvjqfZGzw/NbGe/WnyaLsR/y/NWJ9X/XTVEWJEXhUO/O/5d02c+x3q6VYDL6h', '6A9E6', 32)
    print(result)

# Generated at 2022-06-14 15:11:07.416096
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .aes import counter_blocks

    class TestCounter():
        index = 0

        def next_value(self):
            self.index += 1
            return [0] * 16

    counter = TestCounter()

    def aes_ctr_decrypt_test(data, key_hex, initial_counter_hex, expected_hex):
        key = bytes_to_intlist(compat_b64decode(key_hex))
        initial_counter = bytes_to_intlist(compat_b64decode(initial_counter_hex))
        expected = bytes_to_intlist(compat_b64decode(expected_hex))

        result = aes_ctr_decrypt(data, key, counter_blocks.CounterBlock(initial_counter))
        assert result == expected


# Generated at 2022-06-14 15:11:19.323497
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # http://www.inconteam.com/software-development/41-encryption/55-aes-test-vectors#aes-cbc-128
    key = bytes_to_intlist(compat_b64decode(b'GZy6sIZ6wl9NJOKB-jnmVg=='))
    iv = bytes_to_intlist(compat_b64decode(b'WuBcHr8c5quwI47FtNxXlQ=='))
    cipher = bytes_to_intlist(compat_b64decode(b'KDlTtXchhZTGufMYmOYGS4/fiwv6nWRyhCOCTR12ucNo='))
    plain = aes_cbc_decrypt(cipher, key, iv)

   

# Generated at 2022-06-14 15:11:28.460853
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    print ('Running test_aes_ctr_decrypt')
    key_len = 16

    plaintext = b'Attack at dawn'
    plainbytes = plaintext.encode('utf-8')
    plainintlist = bytes_to_intlist(plainbytes)
    key = [ord(c) for c in "0" * key_len]
    counter = Counter(0, BLOCK_SIZE_BYTES)
    encrypted = aes_ctr_encrypt(plainintlist, key, counter)
    decrypted = aes_ctr_decrypt(encrypted, key, counter)
    encrypted_bytes = intlist_to_bytes(encrypted)
    decrypted_bytes = intlist_to_bytes(decrypted)
    assert decrypted_bytes == plainbytes


# Generated at 2022-06-14 15:11:35.994064
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .aes import AesCtr
    from .secret import Secret
    from .compat import compat_ord

    # Test data from:
    #     http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf

# Generated at 2022-06-14 15:11:46.964089
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    print('Testing aes_cbc_decrypt')
    key = [
        0x5f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x62, 0x63, 0x64,
        0x5f, 0x62, 0x69, 0x74, 0x73, 0x5f, 0x61, 0x65, 0x73, 0x31,
        0x36, 0x30, 0x31, 0x34, 0x35, 0x36
    ]

# Generated at 2022-06-14 15:12:00.047760
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    encrypted = '4ym4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m4m7bUHk6jtilouVlFqI3qzVhj+iPwRbPcc2nI='
    password = 'fefefefe'

    text = aes_decrypt_text(encrypted, password, 16)
    assert text == b'The quick brown fox jumps over the lazy dog.'

# Generated at 2022-06-14 15:12:10.081234
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    data = 'zW37y8jvTzI0VPCmgp1GmfZ7wvKjYJY/RbFgW0/yLpGVIr/qCnHEtN/j2ZwvN/j4q3e0i4M2QXdzitI5SshjRg=='
    password = 'password'
    key_size_bytes = 32
    test_plaintext = 'test plaintext'

    plaintext = aes_decrypt_text(data, password, key_size_bytes)
    assert plaintext == test_plaintext

# Generated at 2022-06-14 15:12:19.340515
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Example taken from https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29
    key = '140b41b22a29beb4061bda66b6747e14'.decode('hex')
    iv = '4ca00ff4c898d61e1edbf1800618fb28'.decode('hex')
    cipher_text = 'C8A64537A0B3A93FCDE3CDAD9F1CE58B'.decode('hex')
    plain_text = 'Basic CBC mode encryption needs padding.'
    assert aes_cbc_decrypt(cipher_text, key, iv) == plain_text


# Generated at 2022-06-14 15:12:32.906190
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:12:43.488069
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('kPH+bIxk5D2deZiIxcaaaA=='))
    iv = bytes_to_intlist(compat_b64decode('AxY8DCtDaGlsbGljb3RoZQ=='))
    cipher = bytes_to_intlist(compat_b64decode('KDlTtXchhZTGufMYmOYGS4/fzhQ1A=='))
    assert(decrypt_aes_cbc(cipher, key, iv) == bytes_to_intlist(b'Basic CBC mode encryption needs padding.'))



# Generated at 2022-06-14 15:12:53.938800
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .utils import read_file
    key = read_file('test/data/aes/key_128.txt')
    iv = read_file('test/data/aes/iv.txt')
    cipher = read_file('test/data/aes/cbcdecrypt_cipher.txt')

    cipher = bytes_to_intlist(compat_b64decode(cipher))
    key = bytes_to_intlist(compat_b64decode(key))
    iv = bytes_to_intlist(compat_b64decode(iv))
    pt = aes_cbc_decrypt(cipher, key, iv)
    pt = intlist_to_bytes(pt)
    assert pt == b'piggy'


# Generated at 2022-06-14 15:13:06.933965
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:13:19.123918
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    print("Testing function aes_cbc_decrypt...")
    key = "140b41b22a29beb4061bda66b6747e14"
    iv = "4ca00ff4c898d61e1edbf1800618fb28"
    data = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"

    data = bytes_to_intlist(compat_b64decode(data))
    key = bytes_to_intlist(compat_b64decode(key))
    iv = bytes_to_intlist

# Generated at 2022-06-14 15:13:27.714178
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:13:39.093740
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # From http://csrc.nist.gov/groups/ST/toolkit/documents/Examples/AES_CBC.pdf
    key = bytes_to_intlist(bytes(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'))
    iv  = bytes_to_intlist(bytes(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'))

# Generated at 2022-06-14 15:13:46.055044
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = [22, 203, 26, 178, 219, 50, 31, 120, 151, 230, 230, 35, 199, 235, 195, 23]
    expected_output = [119, 237, 211, 198, 240, 7, 113, 130, 246, 175, 206, 189, 122, 87, 217, 150]
    key = [
        137, 209, 8, 98, 106, 137, 236, 50, 217, 142, 110, 240, 84, 171, 129, 211
    ]
    iv = [
        103, 43, 48, 130, 109, 125, 190, 54, 51, 85, 85, 54, 249, 54, 101, 141
    ]

    assert aes_cbc_decrypt(data, key, iv) == expected_output

# Generated at 2022-06-14 15:13:57.055503
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist(compat_b64decode('+sF0Yyv9XjKVhS+SbNlHVozpTZF1jK/1pd4147a7/n0='))
    key = bytes_to_intlist(compat_b64decode('Rm9yYmlkZGVuUGFzc3dvcmQ='))
    iv = bytes_to_intlist(compat_b64decode('Q29ybkRhdGFiYXNlUGFzcw=='))

    decrypted_data = aes_cbc_decrypt(data, key, iv)

# Generated at 2022-06-14 15:14:07.413409
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    """
    Validation of the aes_cbc_decrypt function with
    the official test vectors from the NIST website

    http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    """
    def process(key, iv, encrypted):
        key = bytes_to_intlist(compat_b64decode(key))
        iv = bytes_to_intlist(compat_b64decode(iv))
        encrypted = bytes_to_intlist(compat_b64decode(encrypted))

        decrypted = aes_cbc_decrypt(encrypted, key, iv)
        decrypted = intlist_to_bytes(decrypted)
        return decrypted

    # AES-CBC 128-bit encryption

# Generated at 2022-06-14 15:14:22.616276
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:30.391294
# Unit test for function key_expansion
def test_key_expansion():
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Generated at 2022-06-14 15:14:36.129073
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
    expanded_key = []
    encrypted = aes_cbc_encrypt(b'hello world', key, [0] * 16)
    decrypted = aes_cbc_decrypt(encrypted, key, [0] * 16)
    assert decrypted == b'hello world'
test_key_expansion()



# Generated at 2022-06-14 15:14:47.729164
# Unit test for function key_expansion
def test_key_expansion():
	"""
	Add your test cases here
	"""

# Generated at 2022-06-14 15:14:59.169593
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:09.329994
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes = 32
    key = [0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe, 0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81, 0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7, 0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4]
    expanded_key_size_bytes = (key_size_bytes // 4 + 7) * BLOCK_SIZE_BYTES
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:15:21.129859
# Unit test for function key_expansion
def test_key_expansion():
  r = key_expansion([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  assert r == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,119,122,107,41,234,102,212,111,116,140,155,219,29,169,61,141,142,158,251,198,176,208,64,220,117,241,36,19,101,134,226,232,76,180,69,25,48]


# Generated at 2022-06-14 15:15:30.706711
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:43.297513
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:15:53.062398
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test 'key_expansion' function
    """
    # Test vector from https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf
    data = bytes_to_intlist(compat_b64decode(
        b'YUJQQUNJQkUwRTdDQkIxOTk4NjJDMzE0MTMyRjIzMzJBRDBGMEUwQQ=='))

# Generated at 2022-06-14 15:16:03.763688
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:09.723082
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode('Kv5OEbN5aaf+TY41NfI9Xg=='))
    assert key_expansion(data) == bytes_to_intlist(compat_b64decode('9Xv2R49DKx4J4d4cCz1D2QsRfLIb0Sg1yKj9Ajp3pf+0ZtOgZtYJl0uL7V92w1jhQy494AQPXSP0A8Fxhf/A=='))
    data = bytes_to_intlist(compat_b64decode('GWuCP7xbb4MW4hY4ZCOTbQ=='))
    assert key_expansion(data) == bytes_to_int

# Generated at 2022-06-14 15:16:21.679969
# Unit test for function key_expansion
def test_key_expansion():
    assert bytes_to_intlist(compat_b64decode('kPH+bIxk5D2deZiIxcaaaA==')) == key_expansion([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])

# Generated at 2022-06-14 15:16:32.626004
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = bytes_to_intlist(compat_b64decode(b'4dHx3cQgTTZNOj8Hm7zf/w=='))
    key_192 = bytes_to_intlist(compat_b64decode(b'+OcjKw0g2f30WylOy9FkAHRkKjhBwrCi0Z8Qzr0qDwI='))
    key_256 = bytes_to_intlist(compat_b64decode(b'kzrD3wqN/gGqtW/n/nC9x+x/qtMh7YOnp10+53cFFKw='))


# Generated at 2022-06-14 15:16:38.863385
# Unit test for function key_expansion
def test_key_expansion():
    key = list(map(ord, compat_b64decode('6Cb8DvBHhYBxs5Fl5/glxHg==')))
    expected = list(map(ord, compat_b64decode('6Cb8DvBHhYBxs5Fl5/glxHtSQSQ/Zi4khHc/4BjK3qb4=')))
    expanded_key = key_expansion(key)
    assert expanded_key == expected, 'Unit test of function key_expansion failed'



# Generated at 2022-06-14 15:16:48.483163
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('VEHjVS1kZzkxZ1U3d3hlaVYzYTd0WHVvRkRtcW8='))

# Generated at 2022-06-14 15:16:59.576922
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:08.082994
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:16.452864
# Unit test for function key_expansion
def test_key_expansion():
    # Key Expansion
    print('Key Expansion')
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    key_schedule = key_expansion(key)
    print(('Key size: ' + str(len(key_schedule))))