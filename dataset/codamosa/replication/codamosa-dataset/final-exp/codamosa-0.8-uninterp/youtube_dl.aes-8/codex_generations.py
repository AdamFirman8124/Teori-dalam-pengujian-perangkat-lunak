

# Generated at 2022-06-14 15:07:42.022534
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:07:49.565648
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data=bytes_to_intlist('5AEA9FEEA78A82DCCB7B283462274A4C')
    key=bytes_to_intlist('B9E2B70D6F5A5D5D6A5B6A5A6C5B6A5A6')
    iv=bytes_to_intlist('06F94C8F87A63BF237E0ECB2C8DF8C9C')
    result=aes_cbc_decrypt(data,key,iv)
    print(result)
    print(intlist_to_bytes(result))

# Generated at 2022-06-14 15:07:56.657600
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:08:03.872430
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    encrypted = 'JQMTxAMSRPiCzB4huY4tJjKpMhbJ/fjrZ/nIg5m5F5/jD1J/zihYQieQIjozX9bnBQ6UjJdw3+qCeV7zMhWpGj7go+b6g=='
    decrypted = aes_decrypt_text(encrypted, 'abcd', len('abcd'))
    assert(decrypted == 'This is a plaintext')

if __name__ == '__main__':
    test_aes_decrypt_text()



# Generated at 2022-06-14 15:08:09.489051
# Unit test for function aes_decrypt
def test_aes_decrypt():
    aes_key = b'abcdefghijklmnop'
    aes_iv = b'abcdefghijklmnop'
    aes_cipher = b'412bfd4f67df8b034cabd4e4a97c0e50'
    aes_expanded_key = b'abcdefghijklmnop412bfd4f67df8b034cabd4e4a97c0e50'
    aes_decrypted = b'abcdefghijklmnop'
    block = bytes_to_intlist(bytearray(compat_b64decode(aes_cipher)))
    expanded_key = bytes_to_intlist(bytearray(compat_b64decode(aes_expanded_key)))
    plaintext = aes_dec

# Generated at 2022-06-14 15:08:17.086429
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    encrypted_data = aes_cbc_encrypt(
        data=bytes_to_intlist(b'hello'),
        key=bytes_to_intlist(b'0123456789ABCDEF'),
        iv=bytes_to_intlist(b'0123456789ABCDEF'))
    encrypted_data = intlist_to_bytes(encrypted_data)
    assert(encrypted_data == b'\xdf\xc0\x7f\xec\x49\x9b\x65k\xcc\x8a\x10w\xde\xa0L\x8b\xe6\x9e'), 'encrypted_data=%s' % str(encrypted_data)



# Generated at 2022-06-14 15:08:19.948124
# Unit test for function key_schedule_core
def test_key_schedule_core():
    expected = [0xA0, 0xFA, 0xFE, 0x17]
    result = key_schedule_core([0x01, 0x02, 0x03, 0x04], 1)
    assert expected == result



# Generated at 2022-06-14 15:08:30.794457
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = [
        0x69, 0x20, 0xE2, 0x99, 0xA5, 0x20, 0x2A, 0x6D, 0x65, 0x6E, 0x63, 0x68,
        0x69, 0x74, 0x6F, 0x2A
    ]
    key = [0x0F, 0x15, 0x71, 0xC9, 0x47, 0xD9, 0xE8, 0x59, 0x0C, 0xB7, 0xAD,
          0xD6, 0x29, 0x7A, 0x94, 0xB0]
    counter = Counter(0)

# Generated at 2022-06-14 15:08:36.552948
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist('Harry Potter')
    key = bytes_to_intlist('0' * 32)
    iv = bytes_to_intlist('0' * 16)
    result = aes_cbc_encrypt(data, key, iv)

# Generated at 2022-06-14 15:08:46.566886
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:08:59.698042
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    assert aes_ctr_decrypt([1, 2, 3], [21, 22, 23], Counter(0)) == [22, 24, 26]


# Generated at 2022-06-14 15:09:10.459437
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    iv = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    ciphered_data = [16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]
    encrypt = aes_cbc_decrypt(ciphered_data, key, iv)
    print("[+] Ciphered data is:",ciphered_data)
    print("[+] Encrypted data is:",encrypt)
    #assert decrypt == plain_text


# Generated at 2022-06-14 15:09:21.933624
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    encrypted = [185, 114, 45, 207, 111, 37, 7, 198, 242, 125, 225, 82, 60, 123, 219, 195, 177, 160, 162, 160, 44, 123,
                 119, 108, 58, 203, 13, 97, 14, 187, 191, 200, 107, 131, 206, 89, 104, 44, 140, 68, 85, 194, 151, 201,
                 170, 50, 58, 165, 137, 210, 141, 163, 209, 119, 15, 106, 142, 99]
    iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:09:33.143737
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from .utils import bytes_to_intlist,intlist_to_bytes
    key = bytes_to_intlist(compat_b64decode('K7gNU3sdo+OL0wNhqoVWhr3g6s1xYv72ol/pe/Unols='))
    iv = bytes_to_intlist(compat_b64decode('i/7n+eKd8afBKZse2jX9pA=='))
    data = bytes_to_intlist(compat_b64decode('RV5KQlo/Nn+r9Y9x13LkiA=='))
    # Returns b'{"response": [null, "QUFJQ0FVVEgtUkVUVVJOLUxJTktF"}'

# Generated at 2022-06-14 15:09:39.998934
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    """
    Unit test for function aes_cbc_decrypt
    """

# Generated at 2022-06-14 15:09:51.414488
# Unit test for function aes_cbc_decrypt

# Generated at 2022-06-14 15:10:03.084822
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import base64

    def next_value():
        if next_value.i // BLOCK_SIZE_BYTES >= len(next_value.nonce):
            nonce_block, next_value.i = next_value.i // BLOCK_SIZE_BYTES, 0
            return next_value.nonce + [nonce_block >> 8, nonce_block & 0xff]
        else:
            next_value.i += 1
            return next_value.nonce

    next_value.i, next_value.nonce = 0, [2, 3, 5, 7, 11, 13, 17, 19]

    data = bytes_to_intlist(compat_b64decode(
        'GL6Uhv7VuAJ8Ut/jVfz/6Q=='))
    key = bytes_

# Generated at 2022-06-14 15:10:12.271078
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key  = [43,126,21,22,40,174,210,166,171,247,21,136,9,207,79,60]

# Generated at 2022-06-14 15:10:24.407066
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = bytearray(b"\x36\x16\xc7\x2e\xce\x8e\xd5\x13\xfc\x99\x1b\x1a\x2f\xcd\x7e\xa5\xcf\xef\xfa\x7b\x0e\x7f\x25\x64\xa5\xe3")
    key = bytearray(b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c")

# Generated at 2022-06-14 15:10:32.685315
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data = bytes_to_intlist('hello world')
    key = [145, 85, 94, 188, 54, 165, 84, 131, 141, 65, 201, 43, 47, 40, 84, 109]
    iv = [222, 113, 238, 55, 170, 162, 140, 72, 89, 51, 63, 157, 182, 13, 215, 98]
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    print(intlist_to_bytes(decrypted_data))


# Generated at 2022-06-14 15:10:45.102533
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    expected_result = "My hovercraft is full of eels."
    key_size_bytes = 16
    password = "password"
    data = "V/M1DdlrzV7p/9KUYpt6Uu/6ngz2cKTP45a88g2F8Ls="

    result = aes_decrypt_text(data, password, key_size_bytes)
    assert result == expected_result



# Generated at 2022-06-14 15:10:51.959992
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import sys
    from .utils import intlist_to_bytes, bytes_to_intlist
    data = bytes_to_intlist(compat_b64decode(b'6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4B6y4A='))
    key = bytes_to_intlist(compat_b64decode(b'cAQABAAEAAQCq+3qBhCpzGn1EAkRfBstwPvGEhP2Qig='))

# Generated at 2022-06-14 15:10:58.116349
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import _aes_ctr_decrypt
    for size in (16, 32, 64):
        for _ in range(10000):
            data = [0] * size
            key = [0] * 16
            counter = Counter()
            res = aes_ctr_decrypt(data, key, counter)
            assert res == _aes_ctr_decrypt.aes_ctr_decrypt(data, key, counter)
test_aes_ctr_decrypt()



# Generated at 2022-06-14 15:11:04.354137
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    key = "0x2b7e151628aed2a6abf7158809cf4f3c"
    encrypted_text = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
    encrypted_text_intlist = intlist_to_bytes(bytes_to_intlist(compat_b64decode(encrypted_text)))
    cipher_text = "0x6bc1bee22e409f96e93d7e117393172a"
    class Counter(object):
        def next_value(self):
            return intlist_to_bytes(bytes_to_intlist(cipher_text))
    counter = Counter()
    assert aes_

# Generated at 2022-06-14 15:11:07.482112
# Unit test for function inc
def test_inc():
    block = [0] * 16
    for i in range(0x11_0000):
        block = inc(block)
    assert block == bytearray(16)



# Generated at 2022-06-14 15:11:19.456424
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    ciphertext = b'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='

    class TestCounter:
        def __init__(self, player_id):
            self.player_id = player_id

        def next_value(self):
            self.player_id = intlist_to_bytes(
                (bytes_to_intlist(self.player_id) + [1])[:16])
            return bytes_to_intlist(self.player_id)

    player_id = b'\x00' * 16

# Generated at 2022-06-14 15:11:22.656608
# Unit test for function inc
def test_inc():
    l = [0,0,0,0]
    print(inc(l))
    print(inc(l))
    print(inc(l))
    print(inc(l))
    print(inc(l))



# Generated at 2022-06-14 15:11:29.878718
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = bytes_to_intlist('85E813540F0AB405')
    key = bytes_to_intlist('36F18357BE4DBD77F050515C73FCF9F2')
    counter = Counter.new(bytes_to_intlist('69DDA8455C7DD4254BF353B773304EEC'))
    aes_ctr_decrypt(data, key, counter)
    assert bytes_to_intlist('36F18357BE4DBD77F050515C73FCF9F2') == aes_ctr_decrypt(data, key, counter)

# Generated at 2022-06-14 15:11:41.878708
# Unit test for function aes_decrypt_text

# Generated at 2022-06-14 15:11:46.187400
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    password = 'asdf'
    data = 'aXSg2QeO+Aq3gkfP4i4jA=='

    assert aes_decrypt_text(data, password, 32) == '3'
# End of unit test for function aes_decrypt_text



# Generated at 2022-06-14 15:12:01.695825
# Unit test for function key_expansion
def test_key_expansion():
    expanded_key = key_expansion(b'2b7e151628aed2a6' + b'abf7158809cf4f3c')

# Generated at 2022-06-14 15:12:05.503821
# Unit test for function inc
def test_inc():
    print("\t[.] Testing function inc")
    data = [255, 255, 0]
    data_inc = inc(data)
    if data_inc == [255, 255, 1]:
        print("\t\t[+] Ok")
    else:
        print("\t\t[-] Fail")



# Generated at 2022-06-14 15:12:08.391349
# Unit test for function inc
def test_inc():
    assert inc([1, 2, 3]) == [1, 2, 4]
    assert inc([1, 2, 255]) == [1, 3, 0]
    assert inc([1, 255, 255]) == [2, 0, 0]



# Generated at 2022-06-14 15:12:10.014832
# Unit test for function inc
def test_inc():
    from random import randint
    for i in range(10):
        data = [randint(0, 255) for i in range(4)]
        inc = inc(data)
        assert(sum(inc) - sum(data) == 1)



# Generated at 2022-06-14 15:12:11.344746
# Unit test for function inc
def test_inc():
    for i in range(100):
        assert inc(list(bytes([i])))==list(bytes([i+1]))


# Generated at 2022-06-14 15:12:13.807453
# Unit test for function inc
def test_inc():
    assert inc([0, 0, 0, 0]) == [0, 0, 0, 1]
    assert inc([0, 0, 1, 255]) == [0, 0, 2, 0]
    assert inc([255, 255, 255, 255]) == [0, 0, 0, 0]
    assert inc([2, 3, 4, 5]) == [2, 3, 4, 6]



# Generated at 2022-06-14 15:12:22.373677
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    data = key_expansion(key)

# Generated at 2022-06-14 15:12:24.766455
# Unit test for function inc
def test_inc():
    for i in range(1, 256):
        data = [0] * 16
        data[-i] = 255
        assert inc(data) == [0] * (16 - i) + [1] * i
    assert inc([0xff] * 16) == [0] * 16



# Generated at 2022-06-14 15:12:34.717313
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:41.593850
# Unit test for function inc
def test_inc():
    data1 = [ord(x) for x in "data"]
    print(data1)
    data2 = inc(data1)
    print(data1, "->", data2)
    if data2 == [ord(x) for x in "daua"]:
        print("test_inc() passed!")
    else:
        print("test_inc() NOT passed!")



# Generated at 2022-06-14 15:12:54.539463
# Unit test for function key_expansion
def test_key_expansion():
    assert key_expansion(bytes_to_intlist(b'\x00' * 16)) == bytes_to_intlist(b'\x00' * 176)
    assert key_expansion(bytes_to_intlist(b'\x00' * 24)) == bytes_to_intlist(b'\x00' * 208)
    assert key_expansion(bytes_to_intlist(b'\x00' * 32)) == bytes_to_intlist(b'\x00' * 240)
    # see http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf, Appendix C

# Generated at 2022-06-14 15:13:01.728880
# Unit test for function key_expansion
def test_key_expansion():
    key_sample_bytes = [4, 211, 31, 130, 13, 10, 214, 2, 157, 134, 122, 232, 9, 105, 217, 138]

# Generated at 2022-06-14 15:13:12.107595
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:22.730375
# Unit test for function key_expansion
def test_key_expansion():
    from .utils import hex_to_intlist

# Generated at 2022-06-14 15:13:33.545016
# Unit test for function key_expansion

# Generated at 2022-06-14 15:13:42.453944
# Unit test for function key_expansion
def test_key_expansion():
    from .compat import compat_b64decode
    from .utils import bytes_to_intlist, intlist_to_bytes


# Generated at 2022-06-14 15:13:48.319747
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(compat_b64decode('+m1lxz1JyKv199OtNdwCNo+KBPY/SZhT3At+Nd/btp8='))
    key_expansion(data)



# Generated at 2022-06-14 15:13:58.822568
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:14:08.577388
# Unit test for function key_expansion
def test_key_expansion():
    """
    Unit test for function key_expansion
    """
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:14:22.502176
# Unit test for function key_expansion
def test_key_expansion():
    def test(data, expected_result, name):
        result = key_expansion(data)
        if result == expected_result:
            print('Test for key_expansion(' + name + ') passed')
        else:
            print('Test for key_expansion(' + name + ') failed')
            print('Expected: ' + str(expected_result))
            print('Actual:   ' + str(result))


# Generated at 2022-06-14 15:14:37.181737
# Unit test for function key_expansion
def test_key_expansion():
    import pytest

# Generated at 2022-06-14 15:14:47.239173
# Unit test for function key_expansion
def test_key_expansion():
    from .aes_test_vectors import key_expansion_test_vectors
    for key, expected_expanded_key in key_expansion_test_vectors:
        key = bytes_to_intlist(compat_b64decode(key.encode()))
        expanded_key = key_expansion(key)
        expected_expanded_key = expected_expanded_key.encode()
        assert intlist_to_bytes(expanded_key) == compat_b64decode(expected_expanded_key), \
            'Key expansion failed for key: {}'.format(key)
        print('Key expansion ok for key: {}'.format(key))


# Generated at 2022-06-14 15:14:57.458255
# Unit test for function key_expansion
def test_key_expansion():
    for key_size in [16, 24, 32]:
        for i in range(10):
            key = [i] * key_size
            expanded_key = key_expansion(key)
            expanded_key_size_bytes = (key_size // 4 + 7) * BLOCK_SIZE_BYTES
            assert len(expanded_key) == expanded_key_size_bytes, '%d should be %d' % (len(expanded_key), expanded_key_size_bytes)
            assert expanded_key[:key_size] == key, '%s should be %s' % (expanded_key[:key_size], key)

# Generated at 2022-06-14 15:15:07.656416
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
           0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
           0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17]
    # Key Expansion test
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:15:19.000845
# Unit test for function key_expansion
def test_key_expansion():
    test_encryption_key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    test_expanded_key = key_expansion(test_encryption_key)

# Generated at 2022-06-14 15:15:25.870816
# Unit test for function key_expansion
def test_key_expansion():
    data = bytes_to_intlist(b'Two One Nine Two')
    expanded = key_expansion(data)
    assert len(expanded) == 240
    
    data = bytes_to_intlist(b'Sixteen Byte Key')
    expanded = key_expansion(data)
    assert len(expanded) == 176
    
    data = bytes_to_intlist(b'Thats my Kung Fu')
    expanded = key_expansion(data)
    assert len(expanded) == 208



# Generated at 2022-06-14 15:15:32.054059
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:44.599470
# Unit test for function key_expansion
def test_key_expansion():
    # normal
    test_key = [0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00]

# Generated at 2022-06-14 15:15:53.929522
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:02.947049
# Unit test for function key_expansion
def test_key_expansion():
    data = sub_bytes([0x69, 0x20, 0xe2, 0x99, 0xa5, 0x20, 0x2a, 0x6d, 0x65, 0x6e, 0x63, 0x68, 0x69, 0x74, 0x6f, 0x2a])
    assert len(data) == 240

# Generated at 2022-06-14 15:16:16.471484
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:25.691545
# Unit test for function key_expansion
def test_key_expansion():
    data1 = [
        83, 97, 108, 116, 101, 100, 95, 95,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
    ]
    result = key_expansion(data1)

# Generated at 2022-06-14 15:16:30.695930
# Unit test for function key_expansion
def test_key_expansion():
    key = aes_key
    expected = key_expanded

    key = bytes_to_intlist(compat_b64decode(key))
    expected = bytes_to_intlist(compat_b64decode(expected))
    actual = key_expansion(key)
    assert expected == actual


# Generated at 2022-06-14 15:16:34.104367
# Unit test for function key_expansion
def test_key_expansion():
    assert len(key_expansion(list(range(16)))) == 176
    assert len(key_expansion(list(range(24)))) == 208
    assert len(key_expansion(list(range(32)))) == 240



# Generated at 2022-06-14 15:16:45.552265
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
           0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:16:57.558455
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:04.834845
# Unit test for function key_expansion
def test_key_expansion():
    key_ = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:17:17.605941
# Unit test for function key_expansion
def test_key_expansion():
    print('Testing key_expansion')
    key_size_bytes_list = [16, 24, 32]
    key_list = [
        bytes_to_intlist(compat_b64decode('w5FoqP4oUZp6UurXiDxJ9g==')),  # 16-Byte key
        bytes_to_intlist(compat_b64decode('3baqx8XjEURCe/lYsP+DvQ==')),  # 24-Byte key
        bytes_to_intlist(compat_b64decode('cazOwAaR0kOM2QZf1+ZSkA=='))  # 32-Byte key
    ]