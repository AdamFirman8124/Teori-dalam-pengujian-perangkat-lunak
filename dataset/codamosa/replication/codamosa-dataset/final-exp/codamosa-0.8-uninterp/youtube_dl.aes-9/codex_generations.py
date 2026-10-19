

# Generated at 2022-06-14 15:07:34.543249
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # Example from http://php.net/mcrypt_encrypt
    data = [0x6b, 0xc1, 0xbe, 0xe2, 0x2e, 0x40, 0x9f, 0x96, 0xe9, 0x3d, 0x7e, 0x11, 0x73, 0x93, 0x17, 0x2a]
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:07:43.513911
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:07:52.210721
# Unit test for function aes_encrypt
def test_aes_encrypt():
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expanded_key = [
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
        12, 13, 14, 15,
        16, 17, 18, 19,
        20, 21, 22, 23,
        24, 25, 26, 27,
        28, 29, 30, 31
    ]
    expected_result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    actual_result = aes_encrypt(data, expanded_key)
    assert expected_result == actual_result, "{} != {}".format

# Generated at 2022-06-14 15:08:01.537760
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode("/gj6OJ7+A+Sx1Sd6M9Y6ZQQ=="))
    iv = bytes_to_intlist(compat_b64decode("jV7JTZ+p9lobcJjBzEZJbA=="))
    cipher = bytes_to_intlist(compat_b64decode("CTb+8tEJIJ2jz/0qIOMbuw=="))
    decrypted = aes_cbc_decrypt(cipher, key, iv)
    assert intlist_to_bytes(decrypted) == b"foobar"



# Generated at 2022-06-14 15:08:08.672835
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = b"1234"
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Test for the case, where the block count is not a multiple of blocksize
    encrypted_data = aes_cbc_encrypt(compat_b64decode(cleartext), key, iv)
    assert(bytes_to_intlist(encrypted_data) == [
        71, 148, 220, 239, 231, 115, 39, 217, 32, 98, 236, 135, 212, 190, 40, 148
    ])

    # Test for the case, where the block count

# Generated at 2022-06-14 15:08:17.201871
# Unit test for function aes_encrypt

# Generated at 2022-06-14 15:08:24.966727
# Unit test for function inc
def test_inc():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c = [15, 16, 96, 80, 112, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
    e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    assert(inc(a) == b)

# Generated at 2022-06-14 15:08:33.885230
# Unit test for function aes_decrypt
def test_aes_decrypt():
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
    import unittest

    from .compat import compat_b64decode

    class TestYTDLEncrypt(unittest.TestCase):
        def test_aes_decrypt(self):
            with open('test_data/test_aes_decrypt.csv', 'r') as f:
                for i in f.readlines():
                    line = i.strip().split(';')
                    key, iv, ciphertext = line[0], line[1], line[2]
                    expected = bytes_to_intlist(compat_b64decode(line[3]))


# Generated at 2022-06-14 15:08:44.604268
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():

    class Counter(object):

        def __init__(self, init_value):
            self.counter = init_value
            self.counter_middle = self.counter[8:16]
            self.counter_left = self.counter[0:8]

        def next_value(self):
            self.counter_left[7] += 1

            # handle overflow
            for i in reversed(range(8)):
                if self.counter_left[i] == 0:
                    continue

                break

            counter_block = self.counter_left + self.counter_middle
            return counter_block


# Generated at 2022-06-14 15:08:50.478100
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    for key, data_b64 in CIPHER_TESTS.items():
        assert len(key) in (16, 24, 32,)
        assert aes_cbc_decrypt(compat_b64decode(data_b64), bytes_to_intlist(key), BLOCK) == BLOCK


# Generated at 2022-06-14 15:09:10.749749
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    class FakeCounter(object):
        def __init__(self, fake_value):
            self.fake_value = fake_value

        def next_value(self):
            return self.fake_value

    fake_counter_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test = "Test String".encode("ascii")
    test_counter = FakeCounter(fake_counter_value)

    key = [43, 126, 21, 22, 40, 174, 210, 166, 171, 247, 21, 136, 9, 207, 79, 60]
    expanded_key = key_expansion(key)

    # Our test string broken into bytes, and zero padded to fill a block

# Generated at 2022-06-14 15:09:16.520703
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    data = ''.join(('U2FsdGVkX1+pDu0Nt/qi9X3q/tN8kpf/IbhoP/o/Q',
                    'G/2rFm9OKgXcTmzwlmOoPw=='))
    password = 'test1234ABCD'

    decrypted_data = aes_decrypt_text(data, password, 32)
    if decrypted_data == b'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False


# Generated at 2022-06-14 15:09:26.067162
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    # Known answer tests from http://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29
    data = bytes_to_intlist(b"L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
    key = bytes_to_intlist(b"YELLOW SUBMARINE")
    counter = Counter(bytes_to_intlist(b"\x00" * 8))
    assert aes_ctr_decrypt(data, key, counter) == bytes_to_intlist(b"Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, baby ")


# Generated at 2022-06-14 15:09:36.013574
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==\n".encode("utf-8")
    data = bytes_to_intlist(compat_b64decode(data))
    key = bytes_to_intlist("YELLOW SUBMARINE")
    class Counter:
        def __init__(self, nonce):
            self.nonce = nonce
            self.counter = 0
        def next_value(self):
            c = self.counter
            self.counter += 1
            if self.counter == 0:
                self.nonce += 1
            return self.nonce.to_bytes(8, "big") + c.to_bytes

# Generated at 2022-06-14 15:09:42.780148
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    INPUT = b'aqLuEZfR1wLlx6Fo3P6REHj6UPO1cUyFk0HTpwKi1eU='
    PASSWORD = 'password'

    output = aes_decrypt_text(INPUT, PASSWORD, 32)
    assert output == b'Test Input'



# Generated at 2022-06-14 15:09:53.125108
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = bytes_to_intlist(b'\x36\x12\x2b\xca\x48\x64\x59\x84\xef\x85\x76\x77\x34\x8b\x75\x95\xcb\x9e\x3d\x2f\x28\xa1\x8b\x20\x09\x6a\x6c\x45\xb5\x1b\x49\xf5\xb6')
    key = bytes_to_intlist(b'\x4b\x65\x79\x77\x6f\x72\x64\x21\x21\x21\x21\x21\x21\x21\x21\x21')

# Generated at 2022-06-14 15:10:03.411150
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = bytes_to_intlist(compat_b64decode(
        'Kk2+mu4Fz4lXmKt/Z8EJw=='))
    expanded_key = key_expansion(bytes_to_intlist(
        b'\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))
    counter = Counter()

    assert intlist_to_bytes(
        aes_ctr_decrypt(data, expanded_key, counter)) == b'\xd4\x81\xca\x97'



# Generated at 2022-06-14 15:10:12.438149
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    # from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    data = bytes_to_intlist(compat_b64decode(
        'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='))
    key = bytes_to_intlist(compat_b64decode('YELLOW SUBMARINE'))
    class Counter(object):
        def __init__(self, value):
            self.value = value

        def next_value(self):
            self.value += 1

# Generated at 2022-06-14 15:10:24.657452
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key='GQdJw6iZE8I1n0CBfRS0YA=='
    counter=8278405588551790388
    data='H6F8f6U+v6/nM9pHcB8='
    decrypt_data=b'aaaabbbbccc'
    data=bytes_to_intlist(compat_b64decode(data))
    key=bytes_to_intlist(compat_b64decode(key))
    decrypt_data=bytes_to_intlist(decrypt_data)
    class Counter:
        def __init__(self, counter):
            self._counter = counter
            self._counter_bytes = [0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:10:35.962222
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    # Test vectors from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf page 20
    encrypted = 'U2FsdGVkX18iiJ2DAYU0VcQ2+8PjwufRZhFiOZJ9AfRGX8pDz86Pf3Jqy3nJwyK7V8kfhwuU7+nBC6b9r6BhMg=='
    password = 'password'

    decrypted = aes_decrypt_text(encrypted, password, 16)
    assert(decrypted == 'Hello World!')


# Generated at 2022-06-14 15:10:43.900762
# Unit test for function inc
def test_inc():
    assert(inc([0x00, 0x00, 0x01, 0x00]) == [0x00, 0x00, 0x02, 0x00])
    assert(inc([0x00, 0x00, 0x00, 0x00]) == [0x00, 0x00, 0x00, 0x01])
    assert(inc([0x00, 0x00, 0x00, 0xFF]) == [0x00, 0x00, 0x01, 0x00])
    assert(inc([0x00, 0x00, 0xFF, 0xFF]) == [0x00, 0x01, 0x00, 0x00])



# Generated at 2022-06-14 15:10:47.616217
# Unit test for function inc
def test_inc():
    assert inc([0] * 16) == [0x1] * 16
    assert inc([1] * 16) == [0x2] * 16
    assert inc([255] * 16) == [0] * 16
    assert inc([255] * 15 + [254]) == [255] * 15 + [255]
    assert inc([1] * 16) == [0x2] * 16
    print("test_inc passed")
test_inc()


# Generated at 2022-06-14 15:10:51.195760
# Unit test for function inc
def test_inc():
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([0, 0, 0, 255]) == [0, 0, 1, 0]
    assert inc([0, 0, 255, 255]) == [0, 1, 0, 0]
    assert inc([0, 255, 255, 255]) == [1, 0, 0, 0]



# Generated at 2022-06-14 15:10:54.725343
# Unit test for function inc
def test_inc():
    test_data = [0xFF] * 16
    test_inc = inc(test_data)
    if test_inc == [0]*14 + [1] + [0]:
        print('[Passed] test_inc')
    else:
        print('[Failed] test_inc')
test_inc()



# Generated at 2022-06-14 15:10:59.159279
# Unit test for function inc
def test_inc():
    data = [0] * 16
    assert inc(data) == [0] * 15 + [1]

    data = [0] * 16
    data[-1] = 255
    assert inc(data) == [0] * 15 + [0]

    data = [0xff] * 16
    assert inc(data) == [0] * 16



# Generated at 2022-06-14 15:11:06.176788
# Unit test for function inc
def test_inc():
    assert(inc([0x00, 0x00, 0x00]) == [0x00, 0x00, 0x01])
    assert(inc([0x00, 0x00, 0xff]) == [0x00, 0x01, 0x00])
    assert(inc([0x00, 0xff, 0xff]) == [0x01, 0x00, 0x00])
    assert(inc([0x0f, 0xff, 0xff]) == [0x10, 0x00, 0x00])
    assert(inc([0xfe, 0xff, 0xff]) == [0xff, 0x00, 0x00])
    assert(inc([0xff, 0xff, 0xff]) == [0x00, 0x00, 0x00])


# Generated at 2022-06-14 15:11:16.356203
# Unit test for function inc
def test_inc():
    print("Testing inc()...", end="")
    assert(inc([0, 0, 0]) == [0, 0, 1])
    assert(inc([0, 1, 0]) == [0, 1, 1])
    assert(inc([1, 0, 0]) == [1, 0, 1])
    assert(inc([0, 0, 255]) == [0, 1, 0])
    assert(inc([0, 255, 255]) == [1, 0, 0])
    assert(inc([255, 255, 255]) == [0, 0, 0])
    print("Passed.")


# Generated at 2022-06-14 15:11:18.235936
# Unit test for function inc
def test_inc():
    print("Test inc...")
    assert inc([0xFF, 0xFF, 0xFF, 0xFF]) == [0, 0, 0, 0]
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    print("Pass")



# Generated at 2022-06-14 15:11:27.834259
# Unit test for function inc

# Generated at 2022-06-14 15:11:35.405879
# Unit test for function key_expansion
def test_key_expansion():
    assert key_expansion(bytes_to_intlist(compat_b64decode('O3BxOZQ4X4mmPKv4OORHfA=='))) == bytes_to_intlist(compat_b64decode('O3BxOZQ4X4mmPKv4OORHfArKkzdHBb+Ae9pJXKmFh/YSVmEFl+1p0k7ic31zwW5V8YvzC9cVAA='))

# Generated at 2022-06-14 15:11:47.776929
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:00.561563
# Unit test for function key_expansion
def test_key_expansion():
    # AES 128 bit
    assert(key_expansion(bytes_to_intlist(compat_b64decode('mZRKjdmmM1w6A+T/U1QYTQ=='))) ==
           bytes_to_intlist(compat_b64decode('mZRKjdmmM1w6A+T/U1QYTQD0e0I6uC+SJ0w6O1z6TdQYTQD0e0I6uC+SJ0w6O1z6TdQYTQD0e0I6uC+SJ0w6O1z6TdQYTQD0e0I6uC+SJ0w6O1z6TdQYT')))

    # AES 192 bit

# Generated at 2022-06-14 15:12:13.330053
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:20.777650
# Unit test for function key_expansion
def test_key_expansion():
    print("Testing key_expansion...")
    key = bytes_to_intlist(compat_b64decode(b"K7lN9bECGnVU8noOZwYC+w=="))
    expected = bytes_to_intlist(compat_b64decode(b"K7lN9bECGnVU8noOZwYC+yhB/nV7TzK/vLN7G4k4Epo="))
    expanded_key = key_expansion(key)
    assert expanded_key == expected, "Expanded key does not match expected"
test_key_expansion()



# Generated at 2022-06-14 15:12:32.118268
# Unit test for function key_expansion
def test_key_expansion():
    if not aes_test():
        return False

    data = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:44.736921
# Unit test for function key_expansion
def test_key_expansion():
    # 16-Byte key
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:51.291107
# Unit test for function key_expansion
def test_key_expansion():
    from .utils import bytes_to_intlist

    test = bytes_to_intlist(compat_b64decode(
        b'uCvAtpA7eR+D4k8SJX9TF/x/3qUuQ6J8V7NuENvKpVF+NlDp8W7X9kvk+Bfj/MLI'))
    test2 = bytes_to_intlist(compat_b64decode(
        b'hkGMZzJ+pwYKjPv26hVAiJg1bZ5r5X+1vZpkMqq03P5yOwjD5rtbB3qgmqUK2dJh'))
    assert(key_expansion(test) == test2)

    test = bytes_

# Generated at 2022-06-14 15:12:59.940344
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:07.802232
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('6vkyA7O1BteGNzFcZ0iXvg=='))
    expected = bytes_to_intlist(compat_b64decode('6vkyA7O1BteGNzFcZ0iXvnPq3Bq4ks4gHGWTeIY6Uvs'))
    assert key_expansion(key) == expected



# Generated at 2022-06-14 15:13:11.942709
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test if key_expansion works as expected.
    """
    import ssl
    key_list = [ssl.RAND_bytes(x) for x in (16, 24, 32)]
    keys = [bytes_to_intlist(x) for x in key_list]
    for key in keys:
        assert key_expansion(key)



# Generated at 2022-06-14 15:13:24.673747
# Unit test for function key_expansion
def test_key_expansion():
    print('Testing key_expansion')
    # test data from custom test vector
    key = bytes_to_intlist(compat_b64decode(b'A/12/+i+h1/7Hf4Cz1/4q3sDukP+pfnhRk6nnSai6b8='))
    expanded_key = key_expansion(key)
    print('Asserting that the expanded key is correct.')

# Generated at 2022-06-14 15:13:31.239275
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'2b7e151628aed2a6abf7158809cf4f3c')
    assert (len(key) == 4 * 4)

# Generated at 2022-06-14 15:13:42.719674
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:52.911031
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:02.964232
# Unit test for function key_expansion
def test_key_expansion():
    key_1 = bytes_to_intlist(b'asdfghjkl123456')
    expanded_key_1 = key_expansion(key_1)

    key_2 = bytes_to_intlist(b'asdfghjkl1234567asdfghjk')
    expanded_key_2 = key_expansion(key_2)
    key_3 = bytes_to_intlist(b'asdfghjkl1234567asdfghjkl12345678')
    expanded_key_3 = key_expansion(key_3)

# Generated at 2022-06-14 15:14:11.264258
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode(b'9vI4lFdqOt4='))

# Generated at 2022-06-14 15:14:17.557004
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:28.200010
# Unit test for function key_expansion
def test_key_expansion():
    # test case from http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf

    test_key = bytes_to_intlist(compat_b64decode('TlTtTbTpT9TtTbTpT9TtTbTpT9TtTbTpT9TtTbTpT9TtTbTpT9TtTbTpT9TtTbTpT9TtTbTp'))

# Generated at 2022-06-14 15:14:34.420375
# Unit test for function key_expansion
def test_key_expansion():
    for key_size in [16, 24, 32]:
        for key in range(2 ** (key_size * 8)):
            key_list = bytes_to_intlist(intlist_to_bytes(key, key_size // 4))
            assert key_list == key_expansion(key_list)[:key_size // 4]



# Generated at 2022-06-14 15:14:43.671449
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:59.880541
# Unit test for function key_expansion
def test_key_expansion():
    key128 = [143, 194, 34, 208, 145, 203, 230, 143, 177, 246, 97, 206, 145, 92, 255, 84]

# Generated at 2022-06-14 15:15:08.945192
# Unit test for function key_expansion
def test_key_expansion():
    # NIST AES example vectors
    data = bytes_to_intlist(compat_b64decode('2b7e151628aed2a6abf7158809cf4f3c'))
    key = [0x8e, 0x73, 0xb0, 0xf7, 0xda, 0x0e, 0x64, 0x52, 0xc8, 0x10, 0xf3, 0x2b, 0x80, 0x90, 0x79, 0xe5, 0x62, 0xf8,
           0xea, 0xd2, 0x52, 0x2c, 0x6b, 0x7b]
    assert key_expansion(data) == key



# Generated at 2022-06-14 15:15:20.498140
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:29.375477
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:31.207176
# Unit test for function key_expansion
def test_key_expansion():
    """
    @TODO
    """
    pass



# Generated at 2022-06-14 15:15:43.843144
# Unit test for function key_expansion
def test_key_expansion():
    import unittest

    class TestKeyExpansion(unittest.TestCase):
        def test_128(self):
            key = [
                0x2b, 0x7e, 0x15, 0x16,
                0x28, 0xae, 0xd2, 0xa6,
                0xab, 0xf7, 0x15, 0x88,
                0x09, 0xcf, 0x4f, 0x3c
            ]

# Generated at 2022-06-14 15:15:53.432991
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    assert len(key) == 16
    key = key_expansion(key)
    assert len(key) == 176

    key = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
    assert len(key) == 16
    key = key_expansion(key)
    assert len(key) == 176

# Generated at 2022-06-14 15:16:02.057861
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')

# Generated at 2022-06-14 15:16:12.011327
# Unit test for function key_expansion
def test_key_expansion():
    vector = "54686520717569636b2062726f776e20666f78206a756d7073206f76657220746865206c617a7920646f672e"
    key = bytes_to_intlist(compat_b64decode(vector))
    expected = "5468616e204a65616e2d42617074686f6d20502d416e64726f69643b70617373776f72642f62696e64696e672f6373696b6569642f63736b2d312e31"
    expected = bytes_to_intlist(compat_b64decode(expected))
    result = key_expansion(key)
    assert result == expected



# Generated at 2022-06-14 15:16:23.965974
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:47.075549
# Unit test for function key_expansion
def test_key_expansion():
    print("testing function key_expansion")
    import random
    import io

    def _get_random_bytes(number):
        r = []
        for _ in range(number):
            r.append(random.randint(0, 255))
        return r

    key_sizes = [16, 24, 32]
    for i in range(100):
        key_size_bytes = key_sizes[random.randint(0, 2)]
        key = _get_random_bytes(key_size_bytes)
        result = key_expansion(key)
        assert len(result) == 176 if key_size_bytes == 16 else 208 if key_size_bytes == 24 else 240

# Generated at 2022-06-14 15:16:57.459486
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('eoM7FqzBjMl0P6Uhlb6C9A=='))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 240
    assert intlist_to_bytes(expanded_key) == compat_b64decode('5wGbbkI/7nFo9iWlDxjHkBmGt7E91tQgjmf1hTLY2QkI1rX/GcB7Pxn0eNy7mdszsNnuq3nqEf0QrKI+Z9XcgA==')



# Generated at 2022-06-14 15:17:06.462608
# Unit test for function key_expansion
def test_key_expansion():
    key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    key1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    key2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    r = key_expansion(key)
    r1 = key_expansion(key1)
    r2 = key_expansion(key2)
   

# Generated at 2022-06-14 15:17:18.575369
# Unit test for function key_expansion