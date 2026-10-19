

# Generated at 2022-06-14 15:10:09.020867
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key_bytes = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'
    cipher = compat_b64decode(b'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    cipher_bytes = bytes_to_intlist(cipher)
    key_ints = bytes_to_intlist(key_bytes)

# Generated at 2022-06-14 15:10:21.562606
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = intlist_to_bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    key = intlist_to_bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Generated at 2022-06-14 15:10:33.845557
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    print("\n\nTesting aes_ctr_decrypt() ...")
    data = [0x69, 0xc4, 0xe0, 0xd8, 0x6a, 0x7b, 0x04, 0x30, 0xd8, 0xcd,
            0xb7, 0x80, 0x70, 0xb4, 0xc5, 0x5a]
    counter = AesCounter(bytes_to_intlist("101112131415161718191a1b1c1d1e1f"))
    key = bytes_to_intlist("000102030405060708090a0b0c0d0e0f")
    decrypted_data = aes_ctr_decrypt(data, key, counter)

# Generated at 2022-06-14 15:10:41.716863
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist("aoeutheonsthuensot")
    iv = bytes_to_intlist("aoeutheonsthuensot")
    data = []
    data += bytes_to_intlist("asdfasdfasdfasdf")
    data += bytes_to_intlist("qwerqwerqwerqwer")

    expected_output = bytes_to_intlist("asdfasdfasdfasdf")
    expected_output += bytes_to_intlist("qwerqwerqwerqwer")

    encrypted = aes_cbc_encrypt(data, key, iv)
    decrypted = aes_cbc_decrypt(encrypted, key, iv)
    assert len(decrypted) == len(data)
    assert decrypted == expected_output




# Generated at 2022-06-14 15:10:46.574631
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    import base64
    assert b'In the beginning, God created the heavens and the earth.' == aes_decrypt_text(
        base64.b64encode(b'mXn7Jl1MSEuV7M+rQnJw7w=='), 'pass', 16)



# Generated at 2022-06-14 15:10:56.958223
# Unit test for function aes_decrypt
def test_aes_decrypt():
    iv = bytes_to_intlist(compat_b64decode('PlL4X4ilMrjbBNkBHf/ZJw=='))
    c = bytes_to_intlist(compat_b64decode('WsJ5GeD8Mmcsj/rpkbA+o/8eDlL+I/nVm9aF/z7x3AQ='))
    assert aes_decrypt(c, iv) == [0,0,0,0]

    key = bytes_to_intlist(compat_b64decode('yWODfjjiO9dYgbnsQ2A0Zg=='))

# Generated at 2022-06-14 15:11:05.923054
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist(compat_b64decode('O4kqXdVpPWsZi+lIPmJwSg=='))
    key = bytes_to_intlist(compat_b64decode('teBHsoan8hjW2QNQ+1D/Gg=='))
    iv = bytes_to_intlist(compat_b64decode('FZgH+iTrjii0JfJJD+0C9Q=='))

    assert aes_cbc_decrypt(data, key, iv) == bytes_to_intlist(b'\xa1\xe2\xfe')

test_aes_cbc_decrypt()



# Generated at 2022-06-14 15:11:18.478706
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    clear_aes = b'Clear text'
    enc_aes = b'K\x94\xa8w\xde\xab\x9d\x1e\xfa\x14\xee\xa8w\xde\xab\x9d\x1e\xfa\x14\xee\xa8w\xde\xab\x9d\x1e'
    key_aes = b'Sixteen byte key'
    iv_aes = b'Sixteen byte iv'
    key_int = bytes_to_intlist(key_aes)
    enc_int = bytes_to_intlist(enc_aes)
    clear_int = bytes_to_intlist(clear_aes)
    iv_int = bytes_to_intlist(iv_aes)
   

# Generated at 2022-06-14 15:11:27.732850
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
	cipher = "Qxj3qhAH9XfhT9GVRQJbM3qBJ0mZwY+RzYN/pJBvxBOz9X+Od56Aa6N5J6hHQEjK".encode('ascii')
	iv = "a9e0e6c95698bdf1f84a339d925a6c96".encode('ascii')
	key = "27a71a6cd5b6de6890d178e7e66b14f0".encode('ascii')
	plain = "0D0B87856A045F2A2B1F0F11A0A4B4A4".encode('ascii')

# Generated at 2022-06-14 15:11:34.843931
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    message = bytes_to_intlist(compat_b64decode('CxU1MxUxU1QzExQzEzM0NzMzBTMzMw='))
    key = bytes_to_intlist(compat_b64decode('Mm45MEp0NkZtM3JqcDZtNGp0Nkt0M0Rz'))
    iv = bytes_to_intlist('V2VsY29tZSB0byBteSBtaXNzaW9uIQ==')

    decrypted_message = bytes_to_intlist('Welcome to my mission!')

    assert aes_cbc_decrypt(message, key, iv) == decrypted_message



# Generated at 2022-06-14 15:13:51.308444
# Unit test for function inc
def test_inc():
    assert(inc([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]) == [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    assert(inc([0xFF, 0xFF]) == [0x00, 0x00])
    assert(inc([0x01, 0x01]) == [0x01, 0x02])



# Generated at 2022-06-14 15:14:01.153501
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .compat import compat_bytes
    from .utils import format_bytes
    import base64
    cipher = "vladimir_krasnov_01".encode('utf-8')
    cipher_key = "0123456789abcdef".encode('utf-8')
    iv = "0123456789abcdef".encode('utf-8')
    cipher_text = "QWw0dmtmMHQ3L3F0ZWVuODFR".encode('utf-8')
    class Counter:
        def __init__(self):
            self._counter = 0
        def next_value(self):
            self._counter += 1
            return self._counter
    counter = Counter()

# Generated at 2022-06-14 15:14:10.353081
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    from .counter import Counter
    from .cipher_mode_of_operation import ModeOfOperation
    from .padding_mode import pad_with_iso7816

    def b64(b):
        return compat_b64decode(b.encode('ascii'))

    expected_decrypted = "Some plaintext"
    key = b64("3sf2iPLoKPFMQnQf")
    iv = b64("ZG1n9X-YH-p7oWjh")
    ciphertext = b64("pEddS83ZoIb8KroG")

    counter = Counter(ModeOfOperation.MODE_CTR, iv, len(iv) * 8, pad_with_iso7816)

# Generated at 2022-06-14 15:14:19.350317
# Unit test for function inc
def test_inc():
    print("Test inc():")
    print(inc([0, 0, 0, 0]))
    print(inc([1, 0, 0, 0]))
    print(inc([0, 1, 0, 0]))
    print(inc([0, 0, 1, 0]))
    print(inc([0, 0, 0, 1]))
    print(inc([255, 255, 255, 255]))

    a = [0, 1, 2, 3]
    b = inc(a)
    print("a is changed", a, b)



# Generated at 2022-06-14 15:14:26.204402
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    text = aes_decrypt_text(
        b'FvjUcfR6UpD6k+CWKHpZJePoff9XFzgTKGntQYnIHcF0n1wJf8VQW0HvJ7dz+xkx',
        'this is my password',
        32)
    assert text == b'hello world, this is my first message'



# Generated at 2022-06-14 15:14:36.945220
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F]
    print(key)
    key_expansion_result = key_expansion(key)
    assert len(key_expansion_result) == 176
    print(key_expansion_result)
    # (key_expansion_result[176/16*i] == key[i] for i in range(int(len(key_expansion_result) / 16)))


# Generated at 2022-06-14 15:14:43.128481
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    result=aes_decrypt_text("q3hqCyJpZc+nE21C0/zWMcR/wG+dTDYQ","chhopen1",16)
    print(result)
    with open("test.mp4","w")as f:
        f.write(result)
if __name__ == '__main__':
    test_aes_decrypt_text()

# Generated at 2022-06-14 15:14:55.874559
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    """
    Unit test for function aes_decrypt_text
    """
    from .aes import add_pkcs7_padding, remove_pkcs7_padding

    # pylint: disable=R0914

# Generated at 2022-06-14 15:15:02.493908
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = bytes_to_intlist(compat_b64decode(b'MzssNg=='))
    key = bytes_to_intlist('dddddddddddddddddddddddddddddddd')
    ctr = Counter(bytes_to_intlist('cccccccccccccccc'))
    assert intlist_to_bytes(aes_ctr_decrypt(data, key, ctr)) == '12345555'
test_aes_ctr_decrypt()

# Generated at 2022-06-14 15:15:05.304820
# Unit test for function inc
def test_inc():
    data = [0, 0, 0, 0]
    data = inc(data)
    if data == [0, 0, 0, 1]:
        print("Inc OK")
    else:
        print("Inc ERROR")



# Generated at 2022-06-14 15:15:28.961239
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:41.781905
# Unit test for function key_expansion
def test_key_expansion():
    """Unit test for key_expansion"""

    key = bytes_to_intlist("2b7e151628aed2a6abf7158809cf4f3c")

# Generated at 2022-06-14 15:15:46.773023
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128
    data = bytes_to_intlist(compat_b64decode(b'8LvF/r+rD9XrJveWQ0v7kQ=='))
    assert intlist_to_bytes(key_expansion(data)) == compat_b64decode(b'8Lvl/r+rD9XrJveWQ0v7kQkQFCBiIoOmfgJn1cEAA1Rw+pPljJd19YVZHegS+jCCk9n/T1T+VpTf4t+sVt4sPDQ==')

    # AES-192

# Generated at 2022-06-14 15:15:55.289971
# Unit test for function key_expansion
def test_key_expansion():
    assert(len(key_expansion(bytes_to_intlist(b'\x00'*32))) == 240)

# Generated at 2022-06-14 15:16:03.237379
# Unit test for function key_expansion
def test_key_expansion():
    def _assert_equal(data, expected):
        assert [ord(b) for b in key_expansion(bytes_to_intlist(data))] == [ord(b) for b in expected]


# Generated at 2022-06-14 15:16:09.359166
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:17.516912
# Unit test for function key_expansion
def test_key_expansion():
    from .test_utils import (assert_equals, convert_bytes_to_intlist, convert_intlist_to_bytes,
    convert_intlist_to_base64)

    test_values = [
        [b'0'*16, convert_bytes_to_intlist("2b7e1516 28aed2a6 abf71588 09cf4f3c")],
        [b'0'*24, convert_bytes_to_intlist("8e73b0f7 da0e6452 c810f32b 809079e5 62f8ead2")],
        [b'0'*32, convert_bytes_to_intlist("603deb10 15ca71be 2b73aef0 857d7781 1f352c07 3b6108d7")],
    ]


# Generated at 2022-06-14 15:16:26.385886
# Unit test for function key_expansion
def test_key_expansion():
    key_0 = bytes_to_intlist(compat_b64decode(
        b'hvfwrWl8WBqs1jK9X4JJfA=='))

# Generated at 2022-06-14 15:16:32.768971
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode('ZW6mvwuYa0U6dbZO6p0y8A=='))
    expanded_key = key_expansion(data)
    assert len(expanded_key) == 240
    assert expanded_key[0:4] == [212, 247, 158, 99]
    assert expanded_key[236:240] == [173, 129, 155, 145]


# Generated at 2022-06-14 15:16:44.861260
# Unit test for function key_expansion
def test_key_expansion():
    # key = 16 bytes
    key = bytes_to_intlist(b'YELLOW SUBMARINE')
    exp = key + [0x4e, 0x99, 0x06, 0xe8, 0xfc, 0xb6, 0x6c, 0xc9, 0xfa, 0xf4, 0x93, 0x10, 0x62, 0x0f, 0xfe, 0xe8, 0xf4, 0x96, 0xe8, 0x06, 0xcc, 0x05, 0x79, 0x90, 0x20, 0x9b, 0x09, 0xa4, 0x33, 0xb6, 0x6c, 0x1b]
    assert key_expansion(key) == exp

    # key = 24 bytes

# Generated at 2022-06-14 15:16:55.450540
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes = 16
    key = bytes_to_intlist(b'A' * key_size_bytes)


# Generated at 2022-06-14 15:17:04.981465
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('ZW0dvM897JCW8Yf2'))
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:17:17.704894
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
    expanded = key_expansion(key)