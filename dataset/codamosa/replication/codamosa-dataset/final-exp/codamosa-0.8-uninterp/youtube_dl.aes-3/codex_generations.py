

# Generated at 2022-06-14 15:07:44.471256
# Unit test for function aes_encrypt
def test_aes_encrypt():
    import pytest
    from .compat import compat_b64decode
    from .utils import bytes_to_intlist, intlist_to_bytes
    import os

    data_file = os.path.join(os.path.dirname(__file__), 'tests/test_data_aes_cbc.txt')
    with open(data_file, mode='r') as f:
        data = int(f.readline(), 10)
        loops = int(f.readline(), 10)
        for i in range(loops):
            count = int(f.readline(), 10)
            key = list(map(int, f.readline().split()))[:16]
            iv = list(map(int, f.readline().split()))[:16]

# Generated at 2022-06-14 15:07:53.418006
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
    iv = bytes_to_intlist(b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef')
    data = bytes_to_intlist(b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff')

    assert intlist_to_bytes

# Generated at 2022-06-14 15:08:03.362536
# Unit test for function key_expansion
def test_key_expansion():
    # AES-128
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:08:13.218053
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    import requests
    url = 'http://3.93.128.89:12012'
    n = 5  # number of flag
    for i in range(n):
        flags = requests.get(url).json()
        print(flags)
        flags_encrypt = flags['cipher']
        flags_iv = flags['iv']
        flags_iv_bytes = compat_b64decode(flags_iv)
        flags_iv_intlist = bytes_to_intlist(flags_iv_bytes)
        flags_encrypt_bytes = compat_b64decode(flags_encrypt)
        flags_encrypt_intlist = bytes_to_intlist(flags_encrypt_bytes)
        key = [0] * 32

        def counter():
            nonlocal key
            key[19] = key[19] + 1


# Generated at 2022-06-14 15:08:20.170728
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    DATA = 'OOsty0z8Wwg1QvYSLdKM0Zo8IxWXLyAZvrjk/aA/Gn8='
    key = '1234567890123456'.encode('utf-8')
    data = base64.standard_b64decode(DATA)
    iv = data[:16]
    cipher = data[16:]
    decrypted_data = aes_decrypt_text(data, key, 16)
    assert decrypted_data == cipher


# Generated at 2022-06-14 15:08:31.026303
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    password = b"Test123"
    cipher_key = bytes_to_intlist(password)[:32]
    counter_block = [0] * 16
    cipher = aes_encrypt(counter_block, key_expansion(cipher_key))
    cipher = aes_ctr_decrypt(cipher, cipher_key, Counter())
    assert cipher == counter_block

    clear_text = b"Hello world"
    cipher_text = aes_encrypt_text(clear_text, password)
    decrypted_text = aes_decrypt_text(cipher_text, password)
    assert decrypted_text == clear_text

    clear_text = compat_b64decode(b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=')

# Generated at 2022-06-14 15:08:42.373406
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    data = b'{"k": "x", "nonce": "u", "ct": "6StJUyT+T3qYPlDf9bS+x"...'
    key = b'{ "kty": "oct", "k": "jGksm1E7b9SxSxo7" }'
    counter = Counter(b'{"d": {"kty": "oct", "k": "9JPLBhV7Bwb8euPu"}...')
    assert aes_ctr_decrypt(bytes_to_intlist(data),
                           bytes_to_intlist(key),
                           counter) == bytes_to_intlist(b'{"d": {"kty": "oct", "k": "jGksm1E7b9SxSxo7"}...')



# Generated at 2022-06-14 15:08:53.665870
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    assert aes_decrypt_text(
        'cHp6eWwzaG1vbmQ=', 'HALLO', 16) == 'Hallo Welt'
    assert aes_decrypt_text(
        'ExI5PE5c1n5n5Z9X79ZMP71VJFTNZeFf8Bwj/p+C/Pk0A/NxNk', 'PASSWORD', 24) == 'Hallo Welt'
    assert aes_decrypt_text(
        'm8+7LXFmQT7HJhSzEmFDtVuTkc3q7Vf4h4sD7VuXZ1A=', 'PASSWORD', 32) == 'Hallo Welt'

# Generated at 2022-06-14 15:09:02.807418
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    iv  = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Generated at 2022-06-14 15:09:12.630227
# Unit test for function aes_ctr_decrypt

# Generated at 2022-06-14 15:09:27.492309
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
  test_key ='000102030405060708090a0b0c0d0e0f'.decode('hex')
  test_iv='101112131415161718191a1b1c1d1e1f'.decode('hex')
  test_data='00112233445566778899aabbccddeeff'.decode('hex')
  expected='69c4e0d86a7b0430d8cdb78070b4c55a'.decode('hex')
  data = aes_cbc_encrypt(test_data, test_key, test_iv)
  assert(data == expected)
test_aes_cbc_encrypt()



# Generated at 2022-06-14 15:09:32.118573
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = 'Hello World!\0\0\0\0'
    key = '1234567890123456'
    iv = [0] * 16

    encrypted_data = aes_cbc_encrypt(bytes_to_intlist(data.encode('latin-1')), bytes_to_intlist(key.encode('latin-1')), iv)
    print(intlist_to_bytes(encrypted_data).hex())


if __name__ == '__main__':
    test_aes_cbc_encrypt()

# Generated at 2022-06-14 15:09:39.498394
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist(compat_b64decode('CxOJdT+nQ8b9Y3qh3rbqcrCpOeW8mqxq'))
    key = bytes_to_intlist(compat_b64decode('lDYh2BJPlxU6jCQ6AL4U6J5o4MkXFp5V'))
    iv  = bytes_to_intlist(compat_b64decode('lDYh2BJPlxU6jCQ6AL4U6J5o4MkXFp5V'))

# Generated at 2022-06-14 15:09:49.965097
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = bytes_to_intlist(compat_b64decode('kPH+bIxk5D2deZiIxcaaaA=='))
    iv = bytes_to_intlist(compat_b64decode('2jmj7l5rSw0yVb/vlWAYkK/YBwk='))
    data = bytes_to_intlist(compat_b64decode('3p8sf9S7lSLx6Ss896jVzw=='))
    _data = aes_cbc_decrypt(data, key, iv)
    assert intlist_to_bytes(_data) == compat_b64decode('hello')



# Generated at 2022-06-14 15:09:59.283834
# Unit test for function aes_decrypt
def test_aes_decrypt():
    data = bytes_to_intlist(b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff')
    expanded_key = [0] * 240
    decrypted_data = aes_decrypt(data, expanded_key)
    #assert decrypted_data == bytes_to_intlist(b'\x69\xc4\xe0\xd8\x6a\x7b\x04\x30\xd8\xcd\xb7\x80\x70\xb4\xc5\x5a')

# Generated at 2022-06-14 15:10:09.796615
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    # From: https://cryptopals.com/sets/2/challenges/10
    iv = bytes_to_intlist(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
    key = bytes_to_intlist(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")


# Generated at 2022-06-14 15:10:22.373076
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    data = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    key = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    iv = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Generated at 2022-06-14 15:10:34.465592
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    key = [0xc4, 0x6e, 0xc1, 0xb1, 0x8c, 0xe8, 0xa8, 0x78, 0x72, 0x5a, 0x37, 0xe7, 0x80, 0xdf, 0xb7, 0x35, 0x1f, 0x68, 0xed, 0x2e, 0x19, 0x4c, 0x79, 0xfb, 0xc6, 0xae, 0xbe, 0xe1, 0xa6, 0x67, 0x97]

# Generated at 2022-06-14 15:10:42.102240
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    iv = bytes_to_intlist(compat_b64decode('n2n/fNDkY/AJ1tZ9XV7zgQ=='))
    key = bytes_to_intlist(compat_b64decode('JxzXA7VkRfOe+7tKjJRYHg=='))
    cipher = bytes_to_intlist(compat_b64decode('rPMkVdbgyEiJyQh+FxpASQb7fP/ZGdT2n6nZU6fhU6pI/MnInWbrUKsN4/4GyYEaLZ8EoWmKtzJ1qDm1nBlm8w=='))

# Generated at 2022-06-14 15:10:50.537563
# Unit test for function aes_decrypt
def test_aes_decrypt():
    key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    expanded_key = key_expansion(key)
    state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    state = aes_decrypt(state, expanded_key)
    print("State Value : " , state)
    print("State Type : " , type(state))
    print("State Length : " , len(state))
    print("\n")
    

# Generated at 2022-06-14 15:11:06.752383
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    from .aes.key import Key
    from .aes.counter import Counter

    key = Key(compat_b64decode(b'QFe4kBgIBAQQBDI0MAQIDAwMCBAMCAwECAQECAQE='))
    iv = bytes_to_intlist(compat_b64decode(b'abcdabcdabcdabcd'))
    data = bytes_to_intlist(b'abcdef')
    expected_encrypted_data = compat_b64decode(b'lgG7bDhjKdCYsYsTgTtTQQ==')

    encrypted_data = aes_cbc_encrypt(data, key.intlist(), iv)
    assert expected_encrypted_data == intlist_to_bytes(encrypted_data)



# Generated at 2022-06-14 15:11:18.894079
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    cleartext = bytes_to_intlist(compat_b64decode('VFZsb29kQUJBUHJicng4eWVuY0lTdTlwQTdT'))
    key = bytes_to_intlist(compat_b64decode('QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVph'))
    iv = bytes_to_intlist(compat_b64decode('QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVph'))

# Generated at 2022-06-14 15:11:28.460957
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist('140b41b22a29beb4061bda66b6747e14')
    iv = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb28')
    plaintext = bytes_to_intlist('Basic CBC mode encryption needs padding.')
    encrypted_data = bytes_to_intlist('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
    encrypted_data_out = aes_cbc_encrypt(plaintext, key, iv)
    # print

# Generated at 2022-06-14 15:11:35.994164
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    key = bytes_to_intlist(compat_b64decode(
        'pyIQUioT7XlszuHMg+n7yw=='))
    iv = bytes_to_intlist(compat_b64decode('hKI5+5l6NJ5QwChTPFH6JQ=='))
    data = bytes_to_intlist(compat_b64decode(
        'zFvBNyx5UHpNsg3qGAE6Og=='))
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    encrypted_data = aes_cbc_encrypt(decrypted_data, key, iv)
    decrypted_data = aes_cbc_decrypt(encrypted_data, key, iv)
    assert bytes_to_

# Generated at 2022-06-14 15:11:46.667551
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    # Test vector: https://tools.ietf.org/html/rfc3713#section-8
    key = bytes_to_intlist('0123456789abcdedfedcba9876543210')
    iv = bytes_to_intlist('fedcba9876543210')
    cleartext = bytes_to_intlist('A   CBC mode test vector    ')
    expected_cipher = 'EB1D0A9A55219BCA4C2B3F0F5424B5E9'
    expected_cipher = bytes_to_intlist(compat_b64decode(expected_cipher))
    cipher = aes_cbc_encrypt(cleartext, key, iv)
    assert cipher == expected_cipher



# Generated at 2022-06-14 15:11:57.458467
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    # Set 1 / Challenge 7
    key = bytes_to_intlist('YELLOW SUBMARINE')
    data = b'''
    AES in CBC mode.
    Here is a nice picture of the submarine Voladora: http://bit.ly/Psjnf7
    '''
    iv = [0] * 16
    cipher = aes_cbc_encrypt(data, key, iv)
    with open('data/7.txt') as file:
        expected_cipher = bytes_to_intlist(compat_b64decode(file.read()))

    assert(cipher == expected_cipher)



# Generated at 2022-06-14 15:12:04.898279
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
    """Test encryption using AES in CBC mode"""
    data   = bytes_to_intlist('1234567890123456')
    key    = bytes_to_intlist('4xjhlzgwxto4pk5g')
    iv     = bytes_to_intlist('1010101010101010')
    result = aes_cbc_encrypt(data, key, iv)
    assert ''.join('{:02x}'.format(x) for x in result) == '895c3d9daa223fd9c953e95b48f4a4f4'


# Generated at 2022-06-14 15:12:06.733230
# Unit test for function inc
def test_inc():
    data = [0] * 16
    data[0] = 255
    print(data)
    inc_data = inc(data)
    print(inc_data)



# Generated at 2022-06-14 15:12:18.104763
# Unit test for function aes_cbc_encrypt
def test_aes_cbc_encrypt():
  iv = bytes_to_intlist(compat_b64decode('Nk0zJhPoU/j6Ue7LlRdWrg=='))
  key = bytes_to_intlist(compat_b64decode('8jb7Zsz2T4j3Vq0e8ayukQ=='))
  data = '{"t":"live_master" }'
  data_intlist = bytes_to_intlist(data.encode('utf-8'))
  encrypteddata = aes_cbc_encrypt(data_intlist, key, iv)
  encryptedbytes = intlist_to_bytes(encrypteddata)
  encryptedstr = encryptedbytes.decode('utf-8')
  print(encryptedstr)

# Generated at 2022-06-14 15:12:23.882046
# Unit test for function inc
def test_inc():
    data = [0, 0, 0, 0]
    print(data)
    for i in range(5):
        data = inc(data)
        print(data)
    data = [255, 255, 255, 255]
    print(data)
    for i in range(5):
        data = inc(data)
        print(data)



# Generated at 2022-06-14 15:12:36.021031
# Unit test for function key_expansion

# Generated at 2022-06-14 15:12:48.436231
# Unit test for function key_expansion
def test_key_expansion():
    key_16 = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f]

# Generated at 2022-06-14 15:12:57.877712
# Unit test for function key_expansion
def test_key_expansion():
    print('Testing key_expansion')

# Generated at 2022-06-14 15:13:10.182279
# Unit test for function key_expansion
def test_key_expansion():
    import functools
    import itertools
    import operator


# Generated at 2022-06-14 15:13:21.765475
# Unit test for function key_expansion
def test_key_expansion():
    assert len(key_expansion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 176, 'Key length is not 176 bytes'
    assert len(key_expansion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 208, 'Key length is not 208 bytes'

# Generated at 2022-06-14 15:13:32.492356
# Unit test for function key_expansion
def test_key_expansion():
    test_key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c,
    ]

# Generated at 2022-06-14 15:13:43.902661
# Unit test for function key_expansion
def test_key_expansion():
    # Test vector from FIPS-197, Appendix C
    data = bytes_to_intlist(compat_b64decode('U0hLUm5KSUVndE9iZ1puak1nUzQ5U2Z6eEpBPT0='))
    expected_result = bytes_to_intlist(compat_b64decode('U0hLUm5KSUVndE9iZ1puak1nUzQ5U2Z6eEpBQTNtV1RZR2dZVHJxUkxNQVk4MXNPSW9nSzc0SjVYeFgwZ1pNemt3OEl1NTg1bTdnTk9qWkJlTTRlRzZaY1dVQQ=='))
    assert key

# Generated at 2022-06-14 15:13:53.670537
# Unit test for function key_expansion
def test_key_expansion():
    key = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:14:03.636746
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:14:11.744954
# Unit test for function key_expansion
def test_key_expansion():
    assert len(key_expansion([0] * 16)) == 176
    assert len(key_expansion([0] * 24)) == 208
    assert len(key_expansion([0] * 32)) == 240
#Exported in order to be used for other functions

# Generated at 2022-06-14 15:14:25.433113
# Unit test for function key_expansion
def test_key_expansion():
    for key_size_bytes in [16, 24, 32]:
        for round in range(10):
            key = bytearray([round + 1] * key_size_bytes)
            expanded_key = key_expansion(key)
            assert len(expanded_key) >= 176
            assert len(key) == key_size_bytes
            assert len(expanded_key) == (key_size_bytes // 4 + 7) * BLOCK_SIZE_BYTES
            decrypted_data = aes_cbc_decrypt(expanded_key, expanded_key, expanded_key[:BLOCK_SIZE_BYTES])
            assert decrypted_data == key



# Generated at 2022-06-14 15:14:37.755609
# Unit test for function key_expansion
def test_key_expansion():
    """
    Tests the key_expansion function
    """

# Generated at 2022-06-14 15:14:45.505433
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:14:57.631342
# Unit test for function key_expansion
def test_key_expansion():
    KEY = [0x8e, 0x73, 0xb0, 0xf7, 0xda, 0x0e, 0x64, 0x52, 0xc8, 0x10, 0xf3, 0x2b, 0x80, 0x90, 0x79, 0xe5, 0x62, 0xf8, 0xea, 0xd2, 0x52, 0x2c, 0x6b, 0x7b]

# Generated at 2022-06-14 15:15:07.798696
# Unit test for function key_expansion
def test_key_expansion():
    data = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa,0xbb, 0xcc, 0xdd, 0xee, 0xff]
    data = key_expansion(data)

# Generated at 2022-06-14 15:15:15.350512
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:23.351170
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    plaintext = bytes_to_intlist(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    assert key_expansion(key) == plaintext
test_key_expansion()


# Generated at 2022-06-14 15:15:31.987453
# Unit test for function key_expansion
def test_key_expansion():
    key_size_bytes_list = [16, 24, 32]
    for key_size_bytes in key_size_bytes_list:
        expected_expanded_key = [0] * key_size_bytes
        expanded_key = key_expansion(expected_expanded_key)
        # Test if expanded_key is correct
        assert len(expanded_key) == len(expected_expanded_key) + BLOCK_SIZE_BYTES
        # Test if content of expanded_key is correct
        assert expanded_key[key_size_bytes: key_size_bytes + 8] == [
            0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6]

# Generated at 2022-06-14 15:15:43.184627
# Unit test for function key_expansion
def test_key_expansion():
    assert intlist_to_bytes(key_expansion(b'\x00' * 16)) == b'\x00' * 176
    assert intlist_to_bytes(key_expansion(b'\x00' * 24)) == b'\x00' * 208
    assert intlist_to_bytes(key_expansion(b'\x00' * 32)) == b'\x00' * 240
    assert intlist_to_bytes(key_expansion(b'\x00' * 48)) == b'\x00' * 240
    assert intlist_to_bytes(key_expansion(b'\x00' * 64)) == b'\x00' * 240



# Generated at 2022-06-14 15:15:52.983418
# Unit test for function key_expansion
def test_key_expansion():
    KEY1 = bytes_to_intlist(compat_b64decode(
        "p3qKjGrE+Pc0J2M8h1zKpvN8KjRfNbFctX9hZiPljQk="))
    EXPANDED_KEY1 = bytes_to_intlist(compat_b64decode(
        """p3qKjGrE+Pc0J2M8h1zKpvN8KjRfNbFctX9hZiPljQkbQEi0c5x5Q2I
        aEoKax3qUlpZ6UUrD6iCW7RTL1j6Me/IxCS2/A/k6Eag=
        """))

# Generated at 2022-06-14 15:16:11.136111
# Unit test for function key_expansion
def test_key_expansion():
    key = [43,126,21,22,40,174,210,166,171,247,21,136,9,207,79,60]

# Generated at 2022-06-14 15:16:18.917460
# Unit test for function key_expansion
def test_key_expansion():
    import os
    import random
    key = bytes_to_intlist(os.urandom(16))
    assert key == key_expansion(key)
    key = bytes_to_intlist(os.urandom(24))
    assert key == key_expansion(key)
    key = bytes_to_intlist(os.urandom(32))
    assert key == key_expansion(key)



# Generated at 2022-06-14 15:16:30.984661
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0xdc, 0x73, 0x9f, 0xc7, 0xfb, 0x5d, 0x39, 0xde,
        0x2f, 0x9b, 0xcb, 0xcb, 0x3c, 0x7e, 0xf8, 0x94,
    ]

# Generated at 2022-06-14 15:16:39.810987
# Unit test for function key_expansion

# Generated at 2022-06-14 15:16:48.986584
# Unit test for function key_expansion
def test_key_expansion():
    print("Testing key_expansion")
    def test(key_string, test_data_string):
        test_data = bytes_to_intlist(compat_b64decode(test_data_string))
        key = bytes_to_intlist(key_string.encode('ascii'))
        expanded_key = key_expansion(key)
        if test_data == expanded_key:
            print("OK")
        else:
            print("Error")
    # AES Specification Example key expansion (128-bit)

# Generated at 2022-06-14 15:16:56.929738
# Unit test for function key_expansion
def test_key_expansion():
    assert len(key_expansion([0, 0, 0, 0])) == BLOCK_SIZE_BYTES * 11
    assert len(key_expansion([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == BLOCK_SIZE_BYTES * 13
    assert len(key_expansion([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == BLOCK_SIZE_BYTES * 15



# Generated at 2022-06-14 15:17:06.148768
# Unit test for function key_expansion
def test_key_expansion():
    key_sizes = [16, 24, 32]
    for key_size in key_sizes:
        key = [0] * key_size
        expected_expanded_key = [0, 0, 0, 0] * 44
        expanded_key = key_expansion(key)
        assert expanded_key == expected_expanded_key

    key = [0] * 16
    expected_expanded_key = [0, 0, 0, 0] * 44
    expanded_key = key_expansion(key)
    assert expanded_key == expected_expanded_key

    key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Generated at 2022-06-14 15:17:18.316214
# Unit test for function key_expansion