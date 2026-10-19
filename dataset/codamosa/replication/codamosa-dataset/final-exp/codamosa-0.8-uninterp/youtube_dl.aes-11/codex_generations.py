

# Generated at 2022-06-14 15:07:46.289780
# Unit test for function aes_encrypt
def test_aes_encrypt():
    # Test case 1
    data = [0x32, 0x43, 0xf6, 0xa8,
            0x88, 0x5a, 0x30, 0x8d,
            0x31, 0x31, 0x98, 0xa2,
            0xe0, 0x37, 0x07, 0x34]

# Generated at 2022-06-14 15:07:53.740654
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    test_string = b'abcdefghijklmnopqrstuvwxyz'
    key = b'YELLOW SUBMARINE'
    phrase = b'Basic CBC mode encryption needs padding.'
    enc = aes_cbc_encrypt(bytes_to_intlist(phrase), bytes_to_intlist(key), bytes_to_intlist(test_string))
    enc = intlist_to_bytes(enc)
    dec = aes_cbc_decrypt(bytes_to_intlist(enc), bytes_to_intlist(key), bytes_to_intlist(test_string))
    dec = intlist_to_bytes(dec)
    assert phrase == dec

# Generated at 2022-06-14 15:07:56.977953
# Unit test for function key_schedule_core
def test_key_schedule_core():
    key = [0x2b, 0x7e, 0x15, 0x16]
    expanded_key = [key.pop()]

    for x in range(1, 11):
        expanded_key += key
        key = key_schedule_core(key, x)

    assert(expanded_key == EXPANDED_KEY)



# Generated at 2022-06-14 15:08:03.389901
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    '''
    The following json object has been encrypted with the python package pyaes (https://github.com/ricmoo/pyaes)
    using the the password 'myPassword' and key_size_bytes == 32.
    '''
    data = "jOi6DRqb6y9XIcj8W7dYObyaJfZdupGxR8wN5N5g5jE1HLX3/63Q2hcj/PZ/jKxmhmPn8mwcQKj/t2M9hwhzHfW1jYrGUtZCjtOazx0lhCQc0KlGdQ=="
    password = "myPassword"
    key_size_bytes = 32


# Generated at 2022-06-14 15:08:09.266186
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    data, key, iv = "test" * 100, "test" * 8, "test" * 2
    assert aes_cbc_decrypt(aes_cbc_encrypt(bytes_to_intlist(data), bytes_to_intlist(key), bytes_to_intlist(iv)), 
                          bytes_to_intlist(key), bytes_to_intlist(iv), ) == bytes_to_intlist(data)


# Generated at 2022-06-14 15:08:17.758494
# Unit test for function inc
def test_inc():
    data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    assert inc(data) == [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]

# Generated at 2022-06-14 15:08:23.124382
# Unit test for function inc
def test_inc():
    assert inc([0x00, 0x00, 0x00, 0x00]) == [0x00, 0x00, 0x00, 0x01]
    assert inc([0x00, 0x00, 0x00, 0x01]) == [0x00, 0x00, 0x00, 0x02]
    assert inc([0x00, 0x00, 0x00, 0xFF]) == [0x00, 0x00, 0x01, 0x00]
    assert inc([0x00, 0x00, 0x01, 0x00]) == [0x00, 0x00, 0x01, 0x01]
    assert inc([0x00, 0x00, 0x01, 0x01]) == [0x00, 0x00, 0x01, 0x02]

# Generated at 2022-06-14 15:08:32.767492
# Unit test for function aes_cbc_encrypt

# Generated at 2022-06-14 15:08:44.470994
# Unit test for function aes_cbc_decrypt
def test_aes_cbc_decrypt():
    from cryptography.hazmat.primitives.ciphers.aead import AESCCM
    from cryptography.hazmat.backends import default_backend
    import os

# Generated at 2022-06-14 15:08:50.720860
# Unit test for function key_expansion
def test_key_expansion():
    print("Test key_expansion()")
    key = bytes_to_intlist(compat_b64decode('CSmfjS+2vQN1q3c2/TtPxA=='))
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 240
# Unit test
test_key_expansion()



# Generated at 2022-06-14 15:09:09.630634
# Unit test for function aes_decrypt_text

# Generated at 2022-06-14 15:09:10.147851
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
        return True


# Generated at 2022-06-14 15:09:13.209338
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    assert "attack at dawn" == aes_decrypt_text(
        "4B3F7KFXY/csmZpSxRLRUmA==", "passphrase",
        16)



# Generated at 2022-06-14 15:09:17.219618
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    assert aes_decrypt_text("gRLx1x3HqkyzsM+ktMn6nA==",'pwd', 16) == b'ebf6cc'

# Generated at 2022-06-14 15:09:26.943323
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    import os

    import base64

    from .pycrypto_aes_cipher import PyCryptoAesCtr
    from .utils import bytes_to_intlist

    from pycryptodome.Cipher import AES

    # https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29
    key = b'Sixteen byte key'
    nonce = b'\x00\x00\x00\x00\x00\x00\x00\x01'

# Generated at 2022-06-14 15:09:35.228911
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    COMPLIANCE_TESTS = (
        ('iF8_PJdMMfcdD6Bh-jBZut6eZG6xzU6hXU6TKj6TcTk', 'test', 32),
        ('S8_FbHx9phhX0gNPQik4BA', 'test', 16),
    )

    for test_data, password, key_size_bytes in COMPLIANCE_TESTS:
        decrypted = aes_decrypt_text(test_data, password, key_size_bytes)
        assert decrypted == password



# Generated at 2022-06-14 15:09:47.333821
# Unit test for function aes_ctr_decrypt
def test_aes_ctr_decrypt():
    test_key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab,
                0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
    test_counter_block = [0xf0, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6, 0xf7,
                          0xf8, 0xf9, 0xfa, 0xfb, 0xfc, 0xfd, 0xfe, 0xff]

# Generated at 2022-06-14 15:09:56.116008
# Unit test for function key_expansion

# Generated at 2022-06-14 15:10:07.590065
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    assert aes_decrypt_text(
        'AQAAAABQAAQAAAAIAQAAAAMAAAAEAAAABgAAAAYAAAAHAAAACAAAAAkAAAAJAAAACgAAABAAAAAQAAAA==',
        '',
        16
    ) == ''
    assert aes_decrypt_text(
        'AQAAAABQAAQAAAAIAQAAAAMAAAAEAAAABgAAAAYAAAAHAAAACAAAAAkAAAAJAAAACgAAABAAAAAQAAAA==',
        '',
        24
    ) == ''
    assert aes_decrypt_text(
        'AQAAAABQAAQAAAAIAQAAAAMAAAAEAAAABgAAAAYAAAAHAAAACAAAAAkAAAAJAAAACgAAABAAAAAQAAAA==',
        '',
        32
    ) == ''



# Generated at 2022-06-14 15:10:19.092050
# Unit test for function aes_decrypt_text
def test_aes_decrypt_text():
    test_data = 'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
    test_key = 'YELLOW SUBMARINE'
    test_plaintext = b'Yo, VIP Let\'s kick it Ice, Ice, baby Ice, Ice, baby '
    assert aes_decrypt_text(test_data, test_key, 16) == test_plaintext
    assert aes_decrypt_text(test_data, test_key, 24) == test_plaintext
    assert aes_decrypt_text(test_data, test_key, 32) == test_plaintext



# Generated at 2022-06-14 15:10:35.341768
# Unit test for function key_expansion
def test_key_expansion():
    """Unit test for function key_expansion"""
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    data = intlist_to_bytes(key_expansion(key))
    assert data == b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c\xa0\xfa\xfe\x17\x88\x54\x2c\xb1\x23\xa3\x39\x39\x2a\x6c\x76'

# Generated at 2022-06-14 15:10:47.780614
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x00010203, 0x04050607, 0x08090a0b, 0x0c0d0e0f]

# Generated at 2022-06-14 15:10:52.915339
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'Thats my Kung Fu')
    encrypted_string = '9YHvRV7xJ8c4mxwIc0tsfv0V7lLJ3IH+7X9z0+q8O6M='
    assert encrypted_string == compat_b64encode(intlist_to_bytes(key_expansion(key))).decode()



# Generated at 2022-06-14 15:11:03.126362
# Unit test for function key_expansion
def test_key_expansion():
    """
    AES key expansion test vectors from
    https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf
    """
    assert intlist_to_bytes(key_expansion(bytes_to_intlist('000102030405060708090A0B0C0D0E0F'.encode()))) == compat_b64decode('AQIDBAUGBwgJCgsMDQ4PEA==')

# Generated at 2022-06-14 15:11:15.663991
# Unit test for function key_expansion

# Generated at 2022-06-14 15:11:25.408524
# Unit test for function key_expansion
def test_key_expansion():
    data = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
    expected_output = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 42, 192, 79, 216, 176, 75, 47, 125, 132, 36, 155, 197, 184, 166, 209, 229, 209, 36, 55, 47, 214, 191, 236, 16, 4, 97, 240, 102, 45, 39, 152, 178, 203, 0, 168, 5, 200, 76, 31, 0, 84, 168, 224, 124, 166, 153, 41, 194, 84, 124, 1, 209, 154, 78, 69, 208, 186, 240, 152, 203]

# Generated at 2022-06-14 15:11:33.650005
# Unit test for function key_expansion
def test_key_expansion():
    def helper(key, expected_expanded_key):
        expanded_key = key_expansion(bytes_to_intlist(compat_b64decode(key)))
        assert expanded_key == bytes_to_intlist(compat_b64decode(expected_expanded_key))

    helper(
        b'-l1_uV7X9nRIiDV7-LwLg',
        b'A0ZvOcW_4HOYi4sX4Q2I0E8SPt1NfOO-LwLg'
    )

# Generated at 2022-06-14 15:11:46.405683
# Unit test for function key_expansion
def test_key_expansion():
    from .utils import hex_to_intlist
    data = hex_to_intlist("2b7e151628aed2a6abf7158809cf4f3c")

# Generated at 2022-06-14 15:11:59.469905
# Unit test for function key_expansion
def test_key_expansion():
    """
    Test vectors (in hexadecimal notation) from:
    http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf
    """
    # 16-Byte key
    key_16 = bytes_to_intlist(compat_b64decode('v0bzOLl0oNbS6W8KvYX9Cg=='))
    expanded_key_16 = bytes_to_intlist(compat_b64decode('v0bzOLl0oNbS6W8KvYX9CgAAmoQFgEK3qz0iDlHdVpepuKjZtLh8eHg=='))

    # 24-Byte key

# Generated at 2022-06-14 15:12:08.326466
# Unit test for function key_expansion
def test_key_expansion():
    data = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
            0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:12:21.272296
# Unit test for function key_expansion
def test_key_expansion():
    key_128 = bytes_to_intlist(bytearray("2b7e151628aed2a6abf7158809cf4f3c".decode("hex")))

# Generated at 2022-06-14 15:12:32.557645
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(compat_b64decode('LK5O5aalQ2C5o5d5'))
    key_size_bytes = len(key)
    rcon_iteration = 1
    while len(key) < 240:
        temp = key[-4:]
        temp = key_schedule_core(temp, rcon_iteration)
        rcon_iteration += 1
        key += xor(temp, key[-key_size_bytes: 4 - key_size_bytes])

        for _ in range(3):
            temp = key[-4:]
            key += xor(temp, key[-key_size_bytes: 4 - key_size_bytes])

        if key_size_bytes == 32:
            temp = key[-4:]
            temp = sub_

# Generated at 2022-06-14 15:12:45.148792
# Unit test for function key_expansion
def test_key_expansion():
    assert len(key_expansion(bytes_to_intlist(compat_b64decode('gBhf+ZsLzZsDtEwR')))) == 16 * (14 + 1)
    assert len(key_expansion(bytes_to_intlist(compat_b64decode('b4Kj4H4I/+f/D8/o')))) == 16 * (14 + 1)
    assert len(key_expansion(bytes_to_intlist(compat_b64decode('z2aZ7Jq3Ewj0LlG0')))) == 24 * (14 + 1)

# Generated at 2022-06-14 15:12:55.608947
# Unit test for function key_expansion
def test_key_expansion():
    key = (
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f
    )

# Generated at 2022-06-14 15:13:08.685519
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    result = intlist_to_bytes(key_expansion(key))

# Generated at 2022-06-14 15:13:20.092496
# Unit test for function key_expansion
def test_key_expansion():
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:13:28.129172
# Unit test for function key_expansion
def test_key_expansion():
    # Tests from https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf

    # AES-128
    key = [
        0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c
    ]

# Generated at 2022-06-14 15:13:39.530815
# Unit test for function key_expansion
def test_key_expansion():
    key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Generated at 2022-06-14 15:13:45.794177
# Unit test for function key_expansion
def test_key_expansion():
    import random

    for key_size_bytes in [16, 24, 32]:
        key = [random.randrange(256) for _ in range(key_size_bytes)]
        expanded_key = key_expansion(key)
        assert len(expanded_key) == (key_size_bytes // 4 + 7) * BLOCK_SIZE_BYTES
        assert all(0 <= expanded_key[i] < 256 for i in range(len(expanded_key)))



# Generated at 2022-06-14 15:13:54.327737
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:10.614709
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:23.745830
# Unit test for function key_expansion
def test_key_expansion():
    print("Test key_expansion()")
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

# Generated at 2022-06-14 15:14:36.185725
# Unit test for function key_expansion
def test_key_expansion():
    """
    Unit test for function key_expansion
    """
    # Test with 16 Byte key
    key_bytes = [
        43, 126, 21, 22, 40, 174, 210, 166, 171, 247, 21, 136, 9, 207, 79, 60
    ]
    key_intlist = bytes_to_intlist(key_bytes)


# Generated at 2022-06-14 15:14:47.833422
# Unit test for function key_expansion

# Generated at 2022-06-14 15:14:59.199628
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:09.342607
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
    expanded_key = key_expansion(key)


# Generated at 2022-06-14 15:15:21.184838
# Unit test for function key_expansion

# Generated at 2022-06-14 15:15:29.808355
# Unit test for function key_expansion
def test_key_expansion():
    key = [
        0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c
    ]
    expanded_key = key_expansion(key)

# Generated at 2022-06-14 15:15:42.539111
# Unit test for function key_expansion
def test_key_expansion():
    # Test 1
    test_key = bytes_to_intlist(compat_b64decode('kPv59vyqzj00x11LXJZTjJ2UHW48jzHN'))

# Generated at 2022-06-14 15:15:46.095532
# Unit test for function key_expansion
def test_key_expansion():
    # key_expansion - 128 bits
    data_in_bytes = bytes_to_intlist(b'\x2b\x7e\x15\x16' + b'\x28\xae\xd2\xa6' + b'\xab\xf7\x15\x88' + b'\x09\xcf\x4f\x3c')

# Generated at 2022-06-14 15:16:02.814984
# Unit test for function key_expansion
def test_key_expansion():
    """
    See https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf Appendix A for
    reference implementation for AES-128/AES-192/AES-256 key expansion
    """

# Generated at 2022-06-14 15:16:13.229795
# Unit test for function key_expansion
def test_key_expansion():
    # AES 128
    assert key_expansion(
        bytes_to_intlist(compat_b64decode('rCdvxuWwM8Q2Q+cIzKLhXA=='))) == bytes_to_intlist(compat_b64decode('rCdvxuWwM8Q2Q+cIzKLhXAkGpqlEgxkGwCpzmfD+yLe1Qa9X5W5gqZjKrHr+2QEcj7gFzqEdexD4i4HjO9Xle+dNR57hZS'))
    # AES 192

# Generated at 2022-06-14 15:16:24.827053
# Unit test for function key_expansion
def test_key_expansion():
  """ Run unit tests for the above functions """
  from .utils import bytes_to_intlist
  from .compat import compat_b64decode
  from .gdata import GDATA
  for cipher_key, encrypted_data, iv in GDATA:
    # Get encrypted bytes
    cipher_key = bytes_to_intlist(compat_b64decode(cipher_key))
    expanded_key= key_expansion(cipher_key)
    assert len(expanded_key) == 176
    cipher_key = bytes_to_intlist(compat_b64decode(cipher_key))
    expanded_key= key_expansion(cipher_key)
    assert len(expanded_key) == 208

# Generated at 2022-06-14 15:16:35.447340
# Unit test for function key_expansion
def test_key_expansion():
    sample_data1 = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
    result1 = key_expansion(sample_data1)


# Generated at 2022-06-14 15:16:46.034606
# Unit test for function key_expansion
def test_key_expansion():
    result = key_expansion(bytes_to_intlist("2b7e151628aed2a6abf7158809cf4f3c"))

# Generated at 2022-06-14 15:16:58.058178
# Unit test for function key_expansion
def test_key_expansion():
    key = bytes_to_intlist('2b7e151628aed2a6abf7158809cf4f3c')
    expected_expanded_key = '2b7e151628aed2a6abf7158809cf4f3cef06095a8b9d8cfd0a846fa3b33e31d663714c93ea0306e4ff5a5c6823b906d5f8a567f6c8ac84a873f88c8e613f794c98b0f0ca662d90883be2dcf53120972abf1a71a026a19a355e3684326655bbda2b288bf2cfb056d255a1e93a3b549aa1ec14551d7'.replace(' ', '')

# Generated at 2022-06-14 15:17:05.210575
# Unit test for function key_expansion

# Generated at 2022-06-14 15:17:17.750505
# Unit test for function key_expansion