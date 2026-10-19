

# Generated at 2022-06-14 15:07:45.856934
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:07:54.288749
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:08:02.494868
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist(b'U2FsdGVkX1+Eu6Rjx6x2u6zzsTvTjfm3G/3c7JVBkWY=')
    key = bytes_to_intlist(b'00000000000000000000000000000000')
    iv = bytes_to_intlist(b'00000000000000000000000000000000')
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    assert decrypted_data == [67, 97, 115, 104, 101, 100, 32, 110, 111, 116, 32, 112, 97, 115, 115, 101, 100, 105, 110]



# Generated at 2022-06-14 15:08:10.406920
# Unit test for function aes_encrypt
def test_aes_encrypt():
    data = bytes_to_intlist(b"1qazqazqazqazqaz")
    expanded_key = key_expansion(data)
    result = aes_encrypt(data, expanded_key)
    assert(result == [0x72, 0x7f, 0x39, 0x5b, 0x3d, 0x59, 0x5a, 0x79, 0x72, 0x7f, 0x39, 0x5b, 0x3d, 0x59, 0x5a, 0x79])


# Generated at 2022-06-14 15:08:17.648407
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """
    Test aes_decrypt_text
    """
    key = "password"
    data = b"Ckj3M3r09O1L9X2Q8O1J0K2Q0e0wzMx+JZH8vYKjgZddUU+X1X5U5e5u6p5U6="

    assert aes_decrypt_text(data, key, 32) == b"This is a test"
    assert aes_decrypt_text(data, key, 16) == b"This is a test"
    assert aes_decrypt_text(data, key, 24) == b"This is a test"


# Generated at 2022-06-14 15:08:25.318144
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():

    key = bytes_to_intlist(compat_b64decode(
        b'gI2YbdqnjHkD/wS+EJmGtBIp7M6b/G/fggFdT9/c'))
    iv = bytes_to_intlist(compat_b64decode(
        b'7VjYX1Oz7Vu8+A=='))


# Generated at 2022-06-14 15:08:33.078336
# Unit test for function aes_encrypt
def test_aes_encrypt():
    # Test values from appendix C.1
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    expanded_key = key_expansion(key)
    cleartext_data = bytes_to_intlist('3243f6a8885a308d313198a2e0370734')
    cipher_data = aes_encrypt(cleartext_data, expanded_key)
    cipher_data_hex = intlist_to_bytes(cipher_data).hex()
    assert cipher_data_hex == '3925841d02dc09fbdc118597196a0b32'



# Generated at 2022-06-14 15:08:44.469829
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    import base64
    nonce = '\x00\x00\x00\x00\x00\x00\x00\x00'

# Generated at 2022-06-14 15:08:56.124893
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:09:08.719015
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    assert aes_cbc_decrypt(compat_b64decode('qDqhGpmMU8SsrWc7a9qfRA=='),
                           compat_b64decode('mw1MhV7vFoaPJsW6/X9JDg=='),
                           compat_b64decode('GivhNdqEWQPOWo8y')) == b'hello world'

# Generated at 2022-06-14 15:09:23.833218
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist("Thats my Kung Fu")

# Generated at 2022-06-14 15:09:32.055907
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    from .test_keys import test_keys
    from .compat import compat_b64encode

    for test_key in test_keys:
        data = compat_b64encode(test_key['cleartext']).decode('utf-8')
        password = test_key['password']
        key_size_bytes = test_key['key_size_bytes']
        cleartext = aes_decrypt_text(data, password, key_size_bytes)
        assert cleartext == test_key['cleartext']
# Helper functions

# Generated at 2022-06-14 15:09:36.725715
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key = [219, 19, 77, 247, 255, 155, 47, 162, 24, 47, 164, 33, 92, 214, 177, 129, 186, 241, 195, 84, 127, 144, 19, 4, 154]
    data = [255, 123, 34, 112, 43, 172, 92, 105, 68, 123, 92, 190, 85, 24, 247, 199, 35, 192, 171, 42, 194, 22, 122, 136, 168, 107, 239, 186, 99, 242, 109, 18, 41, 22, 174, 241, 5, 158, 89, 123, 5, 111, 20, 121, 87, 128, 142, 67, 200, 208, 121, 140, 104, 138, 47, 113, 210]
    counter = Counter(16, [0, 0, 0, 0, 0, 0, 0, 0])


# Generated at 2022-06-14 15:09:48.997019
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    expected_data = bytearray(b'\x43\xF1\xD2\x23\xB2\xB6\x2B\x54\x04\x52\x1D\x7C\xA8\x8A\x31\x29')
    class Counter:
        def __init__(self):
            self.value = bytearray(b'\xC0\x65\x73\x2B\x05\xCA\xF1\xC4\x02\x9D\x06\x33\xD8\x53\xE2\x51')

        def next_value(self):
            self.value[15] += 1
            return bytes_to_intlist(self.value)


# Generated at 2022-06-14 15:09:57.320451
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .counter import BaseCounter

    class Counter(BaseCounter):
        def __init__(self, initial_value=0):
            self.value = initial_value

        def next_value(self):
            self.value += 1
            return [0] * 16

    c = Counter()

    # Source: https://csrc.nist.gov/publications/detail/sp/800-38a/final

# Generated at 2022-06-14 15:10:02.831957
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    """
    Test function aes_ctr_decrypt
    """
    key = bytes_to_intlist(compat_b64decode('qCpv3aW]/gjk$h])/R'))
    data1 = bytes_to_intlist(compat_b64decode('DGbuKjYzM9ehG[+8Bxlw6w=='))
    data2 = bytes_to_intlist(compat_b64decode('775+jL7xwIa0xyQm'))

    class Counter(object):
        """
        Simple counter instance that returns each time
        the same block, [83, 72, 65, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        """

# Generated at 2022-06-14 15:10:12.150146
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:10:24.295990
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    """
    @return {bool} True if tests passed
    """
    from .aes_cbc_decrypt import aes_cbc_decrypt
    from .aes_ctr_decrypt import aes_ctr_decrypt
    from .tools.hex import hex_to_binary
    from .tools.binary import binary_to_hex

    def test_aes_cbc_encrypt_one(key, data, expected_result):
        actual_result = binary_to_hex(aes_cbc_encrypt(data, key, [0] * 16))
        assert actual_result == expected_result, 'Expected %s, got %s' % (expected_result, actual_result)


# Generated at 2022-06-14 15:10:35.787934
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key = bytes_to_intlist(compat_b64decode('KUEhfPBIOfU6jjVkKjfUYw=='))
    expanded_key = key_expansion(key)
    # On-the-fly counter (have to implement next_value to work)
    counter = SimpleCounter(17)
    ciphertext = bytes_to_intlist(compat_b64decode('pHPK/RJ0LVVxXQyQc1I7KQ=='))

    result = aes_ctr_decrypt(ciphertext, key, counter)
    assert result == [70, 237, 247, 157,  75, 192, 222, 41,  75,  18,  58,  50,
                      96,  48, 167,  11]

# Generated at 2022-06-14 15:10:45.547244
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(compat_b64decode('1234567890123456'))
    iv = bytes_to_intlist(compat_b64decode('1234567890123456'))
    data = bytes_to_intlist(compat_b64decode('1234567890123456'))
    encrypted = aes_cbc_encrypt(data, key, iv)
    decrypted = aes_cbc_decrypt(encrypted, key, iv)
    assert bytes(decrypted) == bytes(data)



# Generated at 2022-06-14 15:10:57.757817
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    expected="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "

# Generated at 2022-06-14 15:11:06.379580
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import sys
    if sys.version_info < (3, 0):
        # Python 2
        import codecs
        unhexlify = codecs.getdecoder('hex_codec')[0]
        b = lambda x: x
    else:
        # Python 3
        from codecs import getdecoder, getencoder
        unhexlify = getdecoder('hex')[0]
        b = getencoder('utf-8')[0]

    # Test vector from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    key = unhexlify('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4')

# Generated at 2022-06-14 15:11:18.649983
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    password = 'password'
    data = 'ApEFyg4BH4QJZOtXvYtBjWF5r5xQyki6OWLN/JN5w1RE='
    key_size_bytes = 16
    assert aes_decrypt_text(data, password, key_size_bytes) == 'Unit test'

    password = 'password'
    data = 'BxlD6y7GpvfehWwFzKj3q6ZY9B0e2hacr5xQyki6KWLN/JN5w1RE='
    key_size_bytes = 24
    assert aes_decrypt_text(data, password, key_size_bytes) == 'Unit test'

    password = 'password'

# Generated at 2022-06-14 15:11:28.231540
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .utils import bytes_to_intlist, intlist_to_bytes
    from binascii import unhexlify

    class Counter(object):
        def __init__(self, initial_value=0):
            self.cur_value = initial_value

        def next_value(self):
            self.cur_value += 1
            return intlist_to_bytes(
                bytes_to_intlist(compat_b64decode('AYBXs8s='))[::-1],
                True
            )[::-1]

    c = Counter()
    key = unhexlify('000102030405060708090a0b0c0d0e0f')

# Generated at 2022-06-14 15:11:35.729369
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import sys
    import base64

    def test_one(encrypted, decrypted, key, iv):
        encrypted = list(map(ord, base64.b64decode(encrypted)))
        decrypted = list(map(ord, base64.b64decode(decrypted)))
        key = list(map(ord, base64.b64decode(key)))
        iv = list(map(ord, base64.b64decode(iv)))

        class Counter:
            def __init__(self, iv):
                self.iv = iv

            def next_value(self):
                self.iv[15] += 1
                return self.iv

        counter = Counter(iv)

# Generated at 2022-06-14 15:11:47.702756
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    encrypted = 'ERnq3qnSR7Q2UnyxdCJnTMY9XB4EbLxZJHHnZpsD2SdSvTSZe+wTfT1YCoTl9oNv'
    encrypted += 'Ch1L65H+J/dvAI8/1/e0y+o2zqX0m5J5P5+Znb0m5Cs0U6lRU6RbU+PYU0lv3qc5'
    encrypted += 'G6nZ1CjuBv6UgR6AeP6IYn6xs9vRh8EIPWZp1gZno+6rKvFK8mswbmYFn0ot+2QO'

# Generated at 2022-06-14 15:11:58.283560
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    key_size_bytes = 16
    password = b"p1"
    # password = b"password"
    data = b"%7B%22m%22%3A%22hello%2C%20world%22%7D"
    # data = b"zGZiwjaJwNiV7MudfeoYQVOjyLhD2Qx32b+X9qrqr3ZjoTvriCnWUM+FTdYJLKjR"

    plaintext = aes_decrypt_text(data, password, key_size_bytes)
    print(plaintext)

# Generated at 2022-06-14 15:12:07.030119
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .utils import bytes_to_intlist, intlist_to_bytes
    from .compat import compat_b64decode
    from .hex_helpers import hex_to_intlist, intlist_to_hex

    class Counter(object):
        def __init__(self, seed):
            self.current_seed = seed

        def next_value(self):
            c = self.current_seed
            self.current_seed = [c[15], c[14], c[13], c[12], c[11], c[10], c[9], c[8], c[7], c[6], c[5], c[4], c[3], c[2], c[1], c[0] + 1]
            return c


# Generated at 2022-06-14 15:12:18.560442
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class Counter(object):
        def __init__(self, value):
            self._count = value

        def next_value(self):
            self._count += 1
            return self._count

    cipher = compat_b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    counter = Counter(1)
    res = intlist_to_bytes(aes_ctr_decrypt(bytes_to_intlist(cipher), key, counter))
    assert res == b"Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, baby "



# Generated at 2022-06-14 15:12:26.518334
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    password = b'lol'
    data = b'''R8YwzTP/p4NgdZ+4NjD1baavXJbHx+yKUAjDMpCzvg6U/Th6mz+6TdTwnsDylH9X'''
    expected = b'<xml>content</xml>'
    key_size_bytes = 16
    assert aes_decrypt_text(data, password, key_size_bytes) == expected



# Generated at 2022-06-14 15:12:37.481620
# Unit test for function inc
def test_inc():
    input_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    output_data = inc(input_data)
    assert output_data == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    output_data = inc(output_data)
    assert output_data == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]



# Generated at 2022-06-14 15:12:46.428495
# Unit test for function inc
def test_inc():
    data = [0, 0, 0]
    data = inc(data)

# Generated at 2022-06-14 15:12:54.044383
# Unit test for function inc
def test_inc():
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([0, 0, 0, 1]) == [0, 0, 0, 2]
    assert inc([0, 0, 0, 255]) == [0, 0, 1, 0]
    assert inc([0, 0, 255, 0]) == [0, 1, 0, 0]
    assert inc([0, 255, 0, 0]) == [1, 0, 0, 0]
    assert inc([255, 0, 0, 0]) == [0, 0, 0, 0]


# Generated at 2022-06-14 15:13:00.487420
# Unit test for function inc
def test_inc():
    data = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    data = inc(data)
    if data != [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        print("[Error] Unit test for inc(data) failed")
        return False
    else:
        print("[Success] Unit test for inc(data) passed")
        return True


# Generated at 2022-06-14 15:13:05.112758
# Unit test for function inc
def test_inc():
    assert inc([1, 2, 3, 4, 5, 6, 7, 8, 255, 255]) == [1, 2, 3, 4, 5, 6, 7, 8, 0, 0]
    assert inc([1, 255]) == [2, 0]
    assert inc([255]) == [0]
    assert inc([]) == []
# def test_inc_xor():
#     assert inc_xor([0, 0], [1, 1]) == [1, 1]
#     assert inc_xor([0, 0], [0, 1]) == [0, 1]
#     assert inc_xor([0, 1], [0, 1]) == [0, 0]
#     assert inc_xor([0, 1], [0, 0]) == [0, 1]
#     assert inc_xor([1, 0],

# Generated at 2022-06-14 15:13:08.242479
# Unit test for function inc
def test_inc():
    assert(inc([255, 255, 255, 255]) == [0, 0, 0, 0])
    assert(inc([255, 255, 255, 1]) == [0, 0, 0, 2])
    assert(inc([255, 255, 255, 0]) == [0, 0, 1, 0])
    assert(inc([1, 1, 1, 1]) == [1, 1, 1, 2])
    assert(inc([0, 0, 0, 1]) == [0, 0, 0, 2])



# Generated at 2022-06-14 15:13:19.964089
# Unit test for function key_expansion
def test_key_expansion():
    input = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c,
    ]

# Generated at 2022-06-14 15:13:22.637644
# Unit test for function inc
def test_inc():
    assert inc([0x11, 0x11, 0x11, 0x11]) == [0x12, 0x11, 0x11, 0x11]
    assert inc([0xFF, 0xFF, 0xFF, 0xFF]) == [0x00, 0x00, 0x00, 0x00]
    assert inc([0xFF, 0x00, 0xFF, 0x00]) == [0x00, 0x01, 0x00, 0x01]


# Generated at 2022-06-14 15:13:28.116100
# Unit test for function inc
def test_inc():
    data = bytes.fromhex(
        "2b7e151628aed2a6abf7158809cf4f3c")
    # data = bytes.fromhex("00")
    # data = bytes.fromhex("ff")
    data = [x for x in data]
    data = inc(data)
    print(bytes(data).hex())



# Generated at 2022-06-14 15:13:32.208802
# Unit test for function inc
def test_inc():
    # Test 1
    data = [0x0, 0x0, 0x0, 0x0]
    print("Test 1 [0x0, 0x0, 0x0, 0x0] -> ", end='')
    print(inc(data))

    # Test 2
    data = [0xFF, 0xFF, 0xFF, 0xFF]
    print("Test 2 [0xFF, 0xFF, 0xFF, 0xFF] -> ", end='')
    print(inc(data))

    # Test 3
    data = [0x10, 0xB1, 0xC8, 0xD6]
    print("Test 3 [0x10, 0xB1, 0xC8, 0xD6] -> ", end='')
    print(inc(data))

# Generated at 2022-06-14 15:13:45.391858
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:54.080513
# Unit test for function key_expansion
def test_key_expansion():
    print('Unit test for function key_expansion')
    for s in [16, 24, 32]:
        key = list(range(s))
        expanded_key = key_expansion(key)
        if len(expanded_key) == 176 and s == 16:
            assert expanded_key[-16:] == [32, 99, 125, 105, 28, 25, 248, 159,
                                          126, 139, 179, 236, 224, 45, 243, 123]
        elif len(expanded_key) == 208 and s == 24:
            assert expanded_key[-16:] == [232, 146, 138, 211, 156, 21, 63, 115,
                                          75, 122, 35, 172, 27, 194, 133, 153]

# Generated at 2022-06-14 15:14:04.205842
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:12.107637
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('ATnhYW8Ll+6SpcJl1hLboA=='))

# Generated at 2022-06-14 15:14:24.670365
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:37.389236
# Unit test for function key_expansion
def test_key_expansion():
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:14:49.556724
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:00.138466
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:15:10.183450
# Unit test for function key_expansion
def test_key_expansion():
    # according to Appendix D of FIPS 197:
    # <http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf>
    # implementation verified using NIST known answer tests:
    # <http://csrc.nist.gov/groups/STM/cavp/index.html#04>
    def _key_expansion_test(key, expected):
        expanded_key = key_expansion(key)
        if expanded_key != expected:
            raise AssertionError(
                'Invalid expanded key:\nExpected: %s\nGot: %s' % (
                    intlist_to_bytes(expected),
                    intlist_to_bytes(expanded_key)))


# Generated at 2022-06-14 15:15:22.071479
# Unit test for function key_expansion
def test_key_expansion():
    key1 = [0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe, 0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81, 0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7, 0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4]

# Generated at 2022-06-14 15:15:33.025576
# Unit test for function key_expansion
def test_key_expansion():
    # key_expansion_test.c
    KEY = bytes_to_intlist(
        b'testtesttesttest'
        b'testtesttesttest'
        b'testtesttesttest'
        b'testtesttesttest'
    )

# Generated at 2022-06-14 15:15:45.344739
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'Sixteen byte key')
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:15:52.219027
# Unit test for function key_expansion
def test_key_expansion():
    with open('tests/test_key_expansion.txt', 'r') as test_file:
        for line in test_file:
            if line == '\n':
                continue
            test_data = line.split(':')
            key = bytes_to_intlist(compat_b64decode(test_data[0]))
            expanded_key = bytes_to_intlist(compat_b64decode(test_data[1]))
            assert(expanded_key == key_expansion(key))



# Generated at 2022-06-14 15:15:59.966674
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:11.419300
# Unit test for function key_expansion
def test_key_expansion():
    assert key_expansion([1, 2, 3, 4, 5, 6, 7, 8]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8,
        1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8
    ]


# Generated at 2022-06-14 15:16:23.445019
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test vectors:
    https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf
    Appendix F.1.1-3

    @returns {bool}  True if unit test passed
    """
    # 128-bit key
    key = '2b7e151628aed2a6abf7158809cf4f3c'
    key = bytes_to_intlist(compat_b64decode(key))
    key_schedule = [[0] * 44, [0] * 44]

# Generated at 2022-06-14 15:16:34.039700
# Unit test for function key_expansion
def test_key_expansion():
  from .test_utils import assertEqual
  from .aes_test_data import TEST_DATA_EXPANDED_KEY_128, TEST_DATA_EXPANDED_KEY_192, TEST_DATA_EXPANDED_KEY_256
  assertEqual(key_expansion(TEST_DATA_EXPANDED_KEY_128), bytes_to_intlist(b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))
  assertEqual(key_expansion(TEST_DATA_EXPANDED_KEY_192), bytes_to_intlist(b"000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))

# Generated at 2022-06-14 15:16:42.046541
# Unit test for function key_expansion
def test_key_expansion():
    key = [12, 10, 8, 6, 4, 2, 0, 16, 14, 12, 10, 8, 6, 4, 2, 0]

# Generated at 2022-06-14 15:16:50.334369
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Generated at 2022-06-14 15:17:01.151417
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')

# Generated at 2022-06-14 15:17:15.634046
# Unit test for function key_expansion
def test_key_expansion():
    from .data import key_expansions

    for i in range(len(key_expansions)):
        key = bytes_to_intlist(compat_b64decode(key_expansions[i]['key']))
        expected_expanded_key = bytes_to_intlist(compat_b64decode(key_expansions[i]['expanded_key']))
        expanded_key = key_expansion(key)

        assert expanded_key == expected_expanded_key

