

# Generated at 2022-06-14 15:07:47.577154
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    input = 'DZ27gtX9tXOIHJWyGvizFtLlBxHfVtRK0c4bV7Eu4C0=\n'
    password = 'password'
    # key_size_bytes can be 16 for 128-Bit, 24 for 192-Bit or 32 for 256-Bit
    key_size_bytes = 32
    output = aes_decrypt_text(input, password, key_size_bytes)
    print(output)

# Generated at 2022-06-14 15:07:55.216580
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    from .aes_cbc_encrypt import aes_cbc_encrypt as aes_cbc_encrypt_std
    for message in ['YELLOW SUBMARINE', '\x00' * 1024]:
        message_bytes = bytes_to_intlist(message)
        key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
        iv = [0x00] * 16

        encrypted_data = aes_cbc_encrypt(message_bytes, key, iv)

# Generated at 2022-06-14 15:08:04.312018
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = [82, 101, 39, 34, 33, 38, 84, 32, 32, 32, 32, 32, 32, 32, 32, 32]
    data = bytes_to_intlist(b'3\x83\x84\x02\xfe\x94\x1c\x7e\x07\xa0\xeb\x5d')
    # print(decrypt(data, [83, 111, 109, 101, 72, 97, 114, 100, 87, 111, 114, 107, 33, 33, 33, 33], Counter.new([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))

# Generated at 2022-06-14 15:08:13.862361
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [43, 126, 21, 22, 40, 174, 210, 166, 171, 247, 21, 136, 9, 207, 79, 60]
    iv = [103, 35, 148, 239, 76, 213, 47, 118, 255, 222, 123, 176, 106, 134, 98, 92]
    case1 = [163, 215, 203, 191, 6,  102, 100, 26,  121, 201,  67,  89,  154,  119,  2,  131]
    case2 = [163,  215, 203, 191, 6, 102, 100, 26, 121, 201,  67, 89, 154, 119,  2, 131, 20,  20,  20,  20,  20,  20, 20, 20, 20, 20,  20,  20,  20]

# Generated at 2022-06-14 15:08:22.907447
# Unit test for function aes_decrypt_text

# Generated at 2022-06-14 15:08:32.588970
# Unit test for function key_expansion

# Generated at 2022-06-14 15:08:44.378091
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = bytes_to_intlist(compat_b64decode(('7nKPmsiXn7/u1H+DYNpr4Zz4n/PtHwMHHoDqKp+d'
                                              'NTlhKj5Q5R1eBm5xo/m52qY3j+//p5JsgXhA==')))
    key = bytes_to_intlist(compat_b64decode('V0jEWS+i7Vu/F1D+gV4zj4RAxOs='))

# Generated at 2022-06-14 15:08:55.976140
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:09:05.536695
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    test_data = 'kFf8cId9zvMV7ia5/Za5V8WwD5eoIqx3rPxBQ8WOFDg='
    test_password = 'l00l'
    test_key_size_bytes = 32
    test_decrypted_data = aes_decrypt_text(test_data, test_password, test_key_size_bytes)
    assert test_decrypted_data == b'\x07\xc0\x07\xc0\x07\xc0\x07\xc0'


# Generated at 2022-06-14 15:09:14.581110
# Unit test for function aes_decrypt

# Generated at 2022-06-14 15:09:32.413310
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key_text = '2b7e151628aed2a6abf7158809cf4f3c'
    key = bytes_to_intlist(compat_b64decode(key_text))
    iv_text = '000102030405060708090A0B0C0D0E0F'
    iv = bytes_to_intlist(compat_b64decode(iv_text))
    clear_text = bytes_to_intlist(compat_b64decode('6bc1bee22e409f96e93d7e117393172a'))
    cipher_text = bytes_to_intlist(compat_b64decode('7649abac8119b246cee98e9b12e9197d'))


# Generated at 2022-06-14 15:09:38.990433
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    aes_cbc_encrypt(bytes_to_intlist('YEllOw SuBMaRInE'), bytes_to_intlist('Thats my Kung Fu'), bytes_to_intlist('Two One Nine Two'))
    aes_cbc_encrypt(bytes_to_intlist('PADDING PADDING PADDING PADDI'), bytes_to_intlist('Thats my Kung Fu'), bytes_to_intlist('Two One Nine Two')).length
    aes_cbc_encrypt(bytes_to_intlist('PADDING PADDING PADDING PADDI'), bytes_to_intlist('Thats my Kung Fu'), bytes_to_intlist('Two One Nine Two'))

# Generated at 2022-06-14 15:09:49.667533
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist(b'somedata')
    key = bytes_to_intlist(b'1234567890123456')
    iv = bytes_to_intlist(b'1234567890123456')

    encrypted_data = aes_cbc_encrypt(data, key, iv)
    expected_encrypted_data = bytes_to_intlist(b'\xcf\xd1\x19Dg\xb6\xf5\xa1k\x9a`\x0e\xb5\x12\x08\x1a\x06\x96\xe3\x87\xfa')
    assert(encrypted_data == expected_encrypted_data)


# Generated at 2022-06-14 15:09:57.713723
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = [234, 232, 237, 218, 239, 125, 142, 165, 232, 237, 218, 239, 125, 142, 165, 231]

# Generated at 2022-06-14 15:10:08.746165
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:10:14.583345
# Unit test for function aes_decrypt
def test_aes_decrypt():
    assert aes_decrypt(
        bytes_to_intlist(compat_b64decode('sWp7eJ+nEuV7Sf8TQhZ7vQ==')),
        bytes_to_intlist('0123456789ABCDEF'),
    ) == bytes_to_intlist('PLAIN TEXT...')



# Generated at 2022-06-14 15:10:27.122226
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = bytes_to_intlist(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')
    data = bytes_to_intlist(b'\x32\x43\xf6\xa8\x88\x5a\x30\x8d\x31\x31\x98\xa2\xe0\x37\x07\x34')
    expected = bytes_to_intlist(b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff')
    result = aes_decrypt

# Generated at 2022-06-14 15:10:37.744082
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = 'Some text I want to encrypt.'
    data = bytes_to_intlist(data.encode('utf8'))
    key = 'very secret key.'
    key = bytes_to_intlist(key.encode('utf8'))
    iv = [0] * 16
    iv.extend(range(16))
    iv = iv[:16]

    encrypted_data = aes_cbc_encrypt(data, key, iv)

# Generated at 2022-06-14 15:10:44.355948
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = 'uV7SfjI0uV7SfjI0uV7SfjI0uV7SfjI0uV7SfjI0uV7SfjI0uV7SfjI0uV7SfjI0'.encode()
    key = bytes_to_intlist(key)
    data = 'Qi9eNnRn0/Ny/fepq3AqnBpEZNnRn0/Ny/fepq3AqnBpEZNnRn0/Ny/fepq3AqnBpEZ'.encode()
    data = bytes_to_intlist(data)

# Generated at 2022-06-14 15:10:53.356631
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
           0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
    cipher = [0x69, 0xc4, 0xe0, 0xd8, 0x6a, 0x7b, 0x04, 0x30,
              0xd8, 0xcd, 0xb7, 0x80, 0x70, 0xb4, 0xc5, 0x5a]
    assert aes_decrypt(cipher, key_expansion(key)) == key



# Generated at 2022-06-14 15:11:50.486701
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    input_data = bytes_to_intlist('6bc1bee22e409f96e93d7e117393172a')
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    iv = bytes_to_intlist('000102030405060708090a0b0c0d0e0f')

    print(intlist_to_bytes(aes_cbc_decrypt(input_data, key, iv)))
    # intlist_to_bytes

# Generated at 2022-06-14 15:12:02.224660
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode(
        b'gVQi5zgxu26fZ+Y4u4iEgw=='))
    data = bytes_to_intlist(compat_b64decode(
        b'5U6Jq3gbfuUfeOfXy6O+pzzLJjtgRslisCn8KhY1YpGMSS/TaR/c+QP8oMz/NTV1'))
    iv = bytes_to_intlist(compat_b64decode(
        b'9rPmjmBJBhoT1xmEpkKj0Q=='))

# Generated at 2022-06-14 15:12:06.964083
# Unit test for function inc
def test_inc():
    assert inc([10]) == [11]
    assert inc([0xff]) == [0]
    assert inc([0xff, 0xff]) == [0, 0]
    assert inc([0xff, 0xff, 0xff]) == [0, 0, 1]
    assert inc([0xff, 0xfe]) == [0xff, 0xff]
    assert inc([0xff, 0xfe, 0xfd]) == [0xff, 0xff, 0xfe]



# Generated at 2022-06-14 15:12:18.561549
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
	# define key
	KEY_B64 = 'Q2Fjz66Bd5k5W5D5Y4f4Y4K4A4FG4G4E4'
	key = intlist_to_bytes(bytearray(compat_b64decode(KEY_B64.encode())))
	expanded_key = key_expansion(bytes_to_intlist(key))
	
	key_hex =  format(intlist_to_bytes(key).hex())
	print("Key(128):", key_hex)
	print("Expanded key", format(intlist_to_bytes(expanded_key).hex()))
	
	# define initial vector and encrypting message
	IV = 'z0Zbvjn2q3ZhTzG+'
	IV = intlist_

# Generated at 2022-06-14 15:12:22.295462
# Unit test for function inc
def test_inc():
    data = [0xFF, 0xFF, 0xFF, 0xFF]
    for i in range(256):
        print(data)
        data = inc(data)

test_inc()


# Generated at 2022-06-14 15:12:24.920085
# Unit test for function inc
def test_inc():
    data = [1,255,255,2]
    assert(inc(data) == [2,0,0,3])

# Generated at 2022-06-14 15:12:29.354672
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:12:32.687776
# Unit test for function inc
def test_inc():
    assert(inc([0, 0, 0]) == [0, 0, 1])
    assert(inc([0, 1, 255]) == [0, 2, 0])
    assert(inc([255, 255, 255]) == [0, 0, 0])



# Generated at 2022-06-14 15:12:45.149637
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:12:54.931622
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # CBC decryption is the reverse of encryption
    data = bytes_to_intlist('0123456789ABCDEF')
    key = bytes_to_intlist('0F1571C947D9E859')
    iv = bytes_to_intlist('C0DEC0DEC0DEC0DE')
    ciphertext = [0xcf, 0xd0, 0x5b, 0x11, 0x16, 0x7b, 0x3a, 0xf7, 0xae, 0x34, 0x3c, 0x53, 0x7a, 0x95, 0x3b, 0x16]
    assert aes_cbc_decrypt(ciphertext, key, iv) == data

# Generated at 2022-06-14 15:13:10.059117
# Unit test for function key_expansion
def test_key_expansion():
    data1 = bytes_to_intlist(compat_b64decode('/4KJTEGQvCKj7NBxD+GwNe7VmpJvKcB7'))
    data2 = bytes_to_intlist(compat_b64decode('/4KJTEGQvCKj7NBxD+GwNe7VmpJvKcB7+cHk/6YKj6vFm9m2CT3qHfT7B8Ar/j0L'))

# Generated at 2022-06-14 15:13:21.683964
# Unit test for function key_expansion
def test_key_expansion():
    print("Testing key expansion...")

    import hashlib


# Generated at 2022-06-14 15:13:32.399588
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:43.856600
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes = 16
    key = intlist_to_bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])

# Generated at 2022-06-14 15:13:53.638024
# Unit test for function key_expansion
def test_key_expansion():
    data = 0x2b7e151628aed2a6abf7158809cf4f3c

# Generated at 2022-06-14 15:14:03.597150
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:10.539051
# Unit test for function key_expansion
def test_key_expansion():
    key=compat_b64decode('wLZBKwxnwW2D9wsd4+4o4A==')
    iv = compat_b64decode('wLZBKwxnwW2D9wsd4+4o4A==')
    data=compat_b64decode('wLZBKwxnwW2D9wsd4+4o4A==')
    key = bytes_to_intlist(key)
    iv = bytes_to_intlist(iv)
    data=bytes_to_intlist(data)
    aes_cbc_encrypt(data, key, iv)



# Generated at 2022-06-14 15:14:23.650434
# Unit test for function key_expansion
def test_key_expansion():

    # 16Byte key
    data = [0x2b, 0x7e, 0x15 ,0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:14:36.173164
# Unit test for function key_expansion
def test_key_expansion():
    assert key_expansion(intlist_to_bytes(bytes_to_intlist(b'1234567890123456'))) == \
        intlist_to_bytes(bytes_to_intlist(b'1234567890123456abcdefabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'))
    assert key_expansion(intlist_to_bytes(bytes_to_intlist(b'1234567890123456abcdefab'))) == \
        intlist_to_bytes(bytes_to_intlist(b'1234567890123456abcdefababababababababababababababababababababababababababababababababab'))

# Generated at 2022-06-14 15:14:47.793793
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:15:58.495735
# Unit test for function key_expansion
def test_key_expansion():
    key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    key_expansion_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 16,
    2, 6, 10, 14, 3, 7, 11, 15, 3, 9, 13, 16, 4, 8, 12, 16]
    
    # Test for AES-128

# Generated at 2022-06-14 15:16:10.005708
# Unit test for function key_expansion
def test_key_expansion():
    from .aes_utils import AES_TESTS
    for key, expanded_key in AES_TESTS:
        assert expanded_key == key_expansion(key)
    print("Unit test for function key_expansion passed")
test_key_expansion()


# AssertionError: assert [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

# Generated at 2022-06-14 15:16:15.358068
# Unit test for function key_expansion
def test_key_expansion():
    data = [0x2b, 0x28, 0xab, 0x09, 0x7e, 0xae, 0xf7, 0xcf, 0x15, 0xd2, 0x15, 0x4f, 0x16, 0xa6, 0x88, 0x3c]
    result = key_expansion(data)
    print(result)
    assert len(result) == 240
    assert result[0:4] == [0x2b, 0x28, 0xab, 0x09]
    assert result[-4:] == [0x63, 0xe1, 0xf0, 0x2a]
    assert result[240 - 8:240 - 4] == [0x23, 0x83, 0xd1, 0x8e]

# Generated at 2022-06-14 15:16:22.649159
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode(b'JUmAj88ppHpwvDkKR7yUAQ=='))
    key_expanded = bytes_to_intlist(compat_b64decode(b'JUmAj88ppHpwvDkKR7yUAQE/8+fI6DSZRcOl1rKmjg8='))
    assert key_expansion(key) == key_expanded



# Generated at 2022-06-14 15:16:33.238638
# Unit test for function key_expansion
def test_key_expansion():
    assert intlist_to_bytes(key_expansion(bytes_to_intlist(b'\x00' * 32))) == compat_b64decode(b'JWbaM+U6A1ICsjv1rT7W8JLaxZ+jK2H3eJXAQ2RTKjzI7a+yvJYb26fYkIa6GK+lZm5efX+0RfJtZEqsx5h5jqg==')

# Generated at 2022-06-14 15:16:41.661438
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:50.094986
# Unit test for function key_expansion
def test_key_expansion():
    import unittest
    import random

    class TestKeyExpansion(unittest.TestCase):
        """Test function key_expansion"""
        def test_base(self):
            key = bytes([
                0x2b, 0x7e, 0x15, 0x16,
                0x28, 0xae, 0xd2, 0xa6,
                0xab, 0xf7, 0x15, 0x88,
                0x09, 0xcf, 0x4f, 0x3c,
            ])

# Generated at 2022-06-14 15:16:57.542262
# Unit test for function key_expansion
def test_key_expansion():
    # Test key
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

    # Expected expanded key

# Generated at 2022-06-14 15:17:04.836950
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:17.606555
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('o6G3+KKI4Jy0s4CgYKhZQ=='))