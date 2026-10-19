

# Generated at 2022-06-13 07:38:46.781362
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    class Vault(object):
        def decrypt(self, value, obj=None):
            return value

        def is_encrypted(self, value):
            return True

    class MockInput(object):
        def __init__(self, value, is_encrypted=True):
            self.value = value
            self.is_encrypted = is_encrypted

    plain_text, cipher_text = b'plain-text', b'cipher-text'

    assert AnsibleVaultEncryptedUnicode(cipher_text).count(MockInput(plain_text)) == 0
    assert AnsibleVaultEncryptedUnicode(cipher_text).count(MockInput(cipher_text)) == 0

    avu = AnsibleVaultEncryptedUnicode(cipher_text)
    avu.vault = Vault()
    assert av

# Generated at 2022-06-13 07:38:56.071586
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    # Test for expected result
    test_pw = "test_password"
    vault_lib = VaultLib(test_pw)

    text_to_encrypt = "test"
    encrypted_text = AnsibleVaultEncryptedUnicode.from_plaintext(text_to_encrypt, vault_lib, test_pw)
    assert(text_to_encrypt != encrypted_text)

    # Test for expected result
    text_to_encrypt = "test"
    unencrypted_text = AnsibleVaultEncryptedUnicode(text_to_encrypt)
    assert(text_to_encrypt != unencrypted_text)


# Generated at 2022-06-13 07:39:01.403784
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    import vault
    import os

    vault_password = os.getenv('ANSIBLE_VAULT_PASSWORD')
    if not vault_password:
        raise vault.AnsibleVaultError('ANSIBLE_VAULT_PASSWORD is not set')

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('abcdabcdabcdabcdabcdabcd', vault.VaultLib(vault_password), vault_password)
    assert avu.count('a') == 6
    assert avu.count('abcd') == 3
    assert avu.count('') == 27


# Generated at 2022-06-13 07:39:06.132722
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = 'SHHHH'
    cleartext = 'foo'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(cleartext, vault, secret)
    assert avu == cleartext
    assert avu != 'bar'


# Generated at 2022-06-13 07:39:07.779568
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode('hello_world') != 'hello_world'


# Generated at 2022-06-13 07:39:17.093790
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    avu = AnsibleVaultEncryptedUnicode(u"this is a long sentence but it is encrypted")
    print('type(avu) =', type(avu))
    print('avu[5] =', avu[5])
    print('avu[4:10] =', avu[4:10])
    try:
        print('avu[10:4] =', avu[10:4])
    except ValueError:
        print('avu[10:4] = slice expected at most 2 arguments, got 3')
    print('avu[6:-1] =', avu[6:-1])
    print('avu[6:] =', avu[6:])
    print('avu[:6] =', avu[:6])


# Generated at 2022-06-13 07:39:24.357806
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import tempfile
    import vault

    secret = 'mysecretpassword'
    key = vault.generate_key()

    tmpdir = tempfile.mkdtemp()
    tmpfilename = '%s/vaulted.yml' % tmpdir
    tmpkeyfilename = '%s/vault.key' % tmpdir

    with open(tmpkeyfilename, 'wb') as f:
        f.write(key)

    tmpvault = vault.VaultLib(key)

    iv = vault.generate_iv()
    ciphertext = tmpvault.encrypt('foo', secret, iv=iv)
    encrypted_yaml = {'foo': AnsibleVaultEncryptedUnicode.from_plaintext(ciphertext, tmpvault, secret)}

    # Test that the two objects are equal

# Generated at 2022-06-13 07:39:38.698646
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    x = AnsibleVaultEncryptedUnicode("ABCDEFG")
    x[-1]  # init the property
    assert x[:] == "ABCDEFG"
    assert x[1:] == "BCDEFG"
    assert x[:5] == "ABCDE"
    assert x[1:5] == "BCDE"
    assert x[-1:] == "G"
    assert x[:-1] == "ABCDEF"
    assert x[-5:-1] == "BCDEF"
    assert x[1:-1] == "BCDEF"
    assert x[-7:] == "ABCDEFG"
    assert x[-7:7] == "ABCDEFG"
    assert x[-20:20] == "ABCDEFG"
    assert x[20:30] == ""
    assert x[20:]

# Generated at 2022-06-13 07:39:48.330350
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    secret = VaultSecret(password_file=None, password=b'password')
    vault = VaultLib(secret)

# Generated at 2022-06-13 07:39:58.001023
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    secret = u'foo'

    # Create an AnsibleVaultEncryptedUnicode and encrypt some unicode.
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'a', vault=None, secret=secret)

    # Test that .__ne__ returns the correct result for each method.
    assert(avu.__ne__(u'b'))
    assert(avu.__ne__(u'a'))
    assert(avu.__ne__(u'A'))
    assert(avu.__ne__(u'z'))
    assert(avu.__ne__(u'Z'))


# Generated at 2022-06-13 07:40:07.156534
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    avu = AnsibleVaultEncryptedUnicode("test")
    ret = avu.rfind("test")
    assert ret == 0

    avu = AnsibleVaultEncryptedUnicode("testtest")
    ret = avu.rfind("test", 5)
    assert ret == 5


# Generated at 2022-06-13 07:40:11.407007
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # FIXME: probably need to append values to a list and test for equality
    # FIXME: for a AnsibleVaultEncryptedUnicode object with a vault object
    # FIXME: it does not do anything
    # FIXME: it will raise a exception if the vault object is not defined
    pass


# Generated at 2022-06-13 07:40:18.966500
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.dumper import AnsibleDumper

    vault_password = '123'
    vault = VaultLib(vault_password)

    plaintext = 'secret text 01'
    plaintext_2 = 'secret text 02'
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_bytes_2 = plaintext_2.encode('utf-8')

    ciphertext = vault.encrypt(plaintext_bytes)
    ciphertext_2 = vault.encrypt(plaintext_bytes_2)
    ciphertext_str = ciphertext.decode('utf-8')
    ciphertext_str_2 = ciphertext_2.decode('utf-8')

    # This will be used to decode ciphertext back

# Generated at 2022-06-13 07:40:32.028188
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode('foo')
    assert ansible_vault_encrypted_unicode.__getslice__(2, 3) == 'o'
    assert ansible_vault_encrypted_unicode.__getslice__(3, 2) == ''
    assert ansible_vault_encrypted_unicode.__getslice__(4, 3) == ''
    assert ansible_vault_encrypted_unicode.__getslice__(-1, 1) == 'f'
    assert ansible_vault_encrypted_unicode.__getslice__(-1, -1) == ''
    assert ansible_vault_encrypted_unicode.__getslice__(0, 3) == ansible_vault_encrypted_unicode.data


#

# Generated at 2022-06-13 07:40:38.991186
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.vault import Vault
    vault = Vault('correct_passphrase')
    ciphertext = vault.encrypt('secret')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted() is True
    assert 'ansible' in avu

    avu.vault = None
    assert avu.is_encrypted() is False
    assert 'ansible' not in avu


# Generated at 2022-06-13 07:40:44.170051
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(b"foo", False)
    assert b"f" in encrypted


if yaml.__with_libyaml__:
    # override the default string if libyaml is being used
    # the C loader converts to Unicode anyway, so this can be non-Unicode
    class AnsibleUnsafeLoader(yaml.CSafeLoader):
        ''' a custom unsafe yaml loader that uses our custom AnsibleMapping '''

        # AnsibleMapping = AnsibleDict
        def __init__(self, *args, **kwargs):
            super(AnsibleUnsafeLoader, self).__init__(*args, **kwargs)

            self.add_constructor('tag:yaml.org,2002:map', type(self).construct_yaml_map)

# Generated at 2022-06-13 07:40:54.339731
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    f = AnsibleVaultEncryptedUnicode.is_encrypted
    assert not f(None)
    assert not f(99)
    assert not f('whatever')
    from ansible.parsing.vault import VaultLib
    v = VaultLib([])
    assert not f(AnsibleUnicode('test'))
    assert v.is_encrypted('$ANSIBLE_VAULT;3434;test\ntest')
    assert f(AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;3434;test\ntest'))



# Generated at 2022-06-13 07:40:57.637355
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    assert AnsibleVaultEncryptedUnicode('test').count('test') == 1
    assert AnsibleVaultEncryptedUnicode('').count('test') == 0

# Unit tests for method endswith of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:41:09.255088
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.utils.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import get_vault_secrets
    from ansible.errors import AnsibleParserError

    try:
        p = get_vault_secrets(['tests/test_vault.yml'], get_vault_secrets.VAULT_IDENTITY_LIST)[0]
    except AnsibleParserError:
        mapping = {'vault_password_file': '@test/test_vault.yml'}

# Generated at 2022-06-13 07:41:16.508430
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing import vault
    avue1 = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;dziewulskit86\n33613339616166306261613962653036396634356464306230626532623163623239333135613833\n373039343565663439346235373537333934386665303732')

# Generated at 2022-06-13 07:41:29.376200
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    print("Testing AnsibleVaultEncryptedUnicode.rfind()")
    if AnsibleVaultEncryptedUnicode("hello").rfind("ll"):
        print("PASSED")
    else:
        print("FAILED")
    if AnsibleVaultEncryptedUnicode("hello").rfind("l"):
        print("PASSED")
    else:
        print("FAILED")
    if AnsibleVaultEncryptedUnicode("hello").rfind("lo"):
        print("PASSED")
    else:
        print("FAILED")
    if not AnsibleVaultEncryptedUnicode("hello").rfind("z"):
        print("PASSED")
    else:
        print("FAILED")


# Generated at 2022-06-13 07:41:39.187092
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    def _create_AnsibleVaultEncryptedUnicode(seq, vault):
        avu = AnsibleVaultEncryptedUnicode(seq)
        avu.vault = vault
        return avu

    from ansible.parsing.vault import VaultLib
    secret = '${VAULT_PASS}'
    vault = VaultLib(secret)

# Generated at 2022-06-13 07:41:49.137139
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    from ansible.parsing.vault import VaultLib
    import os

    vault = VaultLib(os.environ['ANSIBLE_VAULT_PASSWORD_FILE'])

    v1 = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault, 'SEA!')

    assert v1 <= 'world'

    # test again after encryption
    v1.vault = None
    assert v1 <= v1

    assert not v1 <= v1.data

if __name__ == '__main__':
    # Unit test execuion
    test_AnsibleVaultEncryptedUnicode___le__()

# Generated at 2022-06-13 07:41:59.876937
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:08.111214
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''Test of method __ne__ of class AnsibleVaultEncryptedUnicode'''
    class mock_vault():
        def __init__(self):
            pass
        def decrypt(self, ciphertext):
            return to_text(ciphertext)
        def encrypt(self, plaintext, secret):
            return to_bytes(plaintext)
        def is_encrypted(self, data):
            return False

    # create the object
    vault = mock_vault()
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo',vault, '')

    # Test that __ne__ returns False
    # avu != 'foo'
    assert(avu != 'foo')

    # Test that __ne__ returns True
    # avu != 'bar'

# Generated at 2022-06-13 07:42:16.387861
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from collections import Sequence
    from ansible.module_utils.six import text_type
    from ansible.module_utils._text import to_bytes, to_text, to_native
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:25.058846
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    '''Unit test for method rfind of class AnsibleVaultEncryptedUnicode'''

    print("Starting test_AnsibleVaultEncryptedUnicode_rfind")
    print("Creating AnsibleVaultEncryptedUnicode")
    avu = AnsibleVaultEncryptedUnicode("test_AnsibleVaultEncryptedUnicode")

    print("Performing rfind")
    rf = avu.rfind("sible")
    if (rf == 8):
        print("test_AnsibleVaultEncryptedUnicode_rfind PASSED")
    else:
        print("test_AnsibleVaultEncryptedUnicode_rfind FAILED")
        sys.exit(1)

# Register AnsibleVaultEncryptedUnicode with the yaml module
yaml.add_represent

# Generated at 2022-06-13 07:42:32.391073
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    # Tests for class AnsibleVaultEncryptedUnicode with function rfind

    str1 = 'Happy New Year'
    str2 = 'Happy New Year'
    str3 = AnsibleVaultEncryptedUnicode(str1)

    assert str3.rfind(str2) == 0
    assert str3.rfind('Year') == 7


# Generated at 2022-06-13 07:42:40.805816
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    ''' Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode '''
    #Mock AnsibleVault encrypted string
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n1234567890123456789012345678901234567890123456789012345678901234\n')

    #Test if checking that the string is encrypted returns true
    assert avu.is_encrypted()


# Generated at 2022-06-13 07:42:51.802127
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test when ciphertext is not encrypted
    vault = None
    ciphertext = 'Hello'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.vault is vault
    assert avu.data == ciphertext
    assert avu != ciphertext
    del avu

    # Test when ciphertext is encrypted
    vault = AnsibleVaultAES256(b'\x00' * 32)
    ciphertext = vault.encrypt('Hello')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.vault is vault
    assert avu.data == 'Hello'
    assert avu != 'Hello'
    del avu


# Generated at 2022-06-13 07:43:04.589296
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    test_vault = VaultLib([])
    vaulted_u1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', test_vault, 'password')
    vaulted_u2 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', test_vault, 'password')
    assert(vaulted_u1 <= vaulted_u2)


# Generated at 2022-06-13 07:43:06.859809
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    string = 'hello'
    iv = AnsibleVaultEncryptedUnicode(string)
    assert (iv != string)
    assert (string != iv)

# Generated at 2022-06-13 07:43:17.496515
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    import crypt
    import crypt.vaultlib
    import crypt.vaultsecret

    ansible_vault_encrypted_unicode_1 = AnsibleVaultEncryptedUnicode('foo')
    ansible_vault_encrypted_unicode_2 = AnsibleVaultEncryptedUnicode('bar')

    # ansible_vault_encrypted_unicode_1 and ansible_vault_encrypted_unicode_2 are both of type AnsibleVaultEncryptedUnicode
    #
    # Example:
    #
    #     assert (ansible_vault_encrypted_unicode_1 <= ansible_vault_encrypted_unicode_2) is True
    assert (ansible_vault_encrypted_unicode_1 <= ansible_vault_encrypted_unicode_2) is True

    ansible_vault_

# Generated at 2022-06-13 07:43:25.218606
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('text', vault.VaultLib('p4ssw0rd'), 'secret')
    assert avu == 'text'
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('not_text', vault.VaultLib('p4ssw0rd'), 'secret')
    assert avu != avu2
    assert avu != 'not_text'


# Generated at 2022-06-13 07:43:35.665760
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing import vault

    # vault.VaultLib is used to encrypt/decrypt data
    vault = vault.VaultLib([])

    # Create a string to encrypt
    data = 'abc'

    # Encrypt the data
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(data, vault,
                                                            secret=None)

    # test that the object is encrypted
    assert encrypted.is_encrypted()

    # test that the object is still encrypted
    assert encrypted.is_encrypted()

    # test that the object is still encrypted
    assert encrypted.is_encrypted()

    # Decrypt the data
    decrypted = encrypted.data

    # test that the object is no longer encrypted
    assert not encrypted.is_encrypted()

    # test that the object is no longer encrypted
    assert not encrypted

# Generated at 2022-06-13 07:43:42.544203
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    from ansible.parsing.vault import VaultLib

    secret = 'mysecret'
    vault = VaultLib(secret)

    # put some data in the vault
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)

    # compare two identical encrypted data
    assert encrypted == encrypted

    # compare two different encrypted data
    encrypted2 = AnsibleVaultEncryptedUnicode.from_plaintext('bar', vault, secret)
    assert encrypted != encrypted2

    # compare encrypted data with plain text
    assert encrypted != 'foo'
    assert encrypted2 != 'bar'


# Generated at 2022-06-13 07:43:47.505839
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class MockVault:
        @classmethod
        def encrypt(cls, seq, secret):
            return seq + secret
        @classmethod
        def decrypt(cls, ciphertext, obj=None):
            return ciphertext
        @classmethod
        def is_encrypted(cls, ciphertext):
            return True

    avu = AnsibleVaultEncryptedUnicode("foo")
    avu.vault = MockVault
    eq_(avu == "foo", True)
    eq_(avu == "bar", False)

# === End of class AnsibleVaultEncryptedUnicode ===



# Generated at 2022-06-13 07:43:49.628956
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    assert to_bytes(AnsibleVaultEncryptedUnicode.from_plaintext('1234', None, None)) <= to_bytes(AnsibleVaultEncryptedUnicode.from_plaintext('1235', None, None))


# Generated at 2022-06-13 07:43:57.161563
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    secret='ansible'
    vault = VaultLib(secret)
    encrypted_string = vault.encrypt('test')
    avu1 = AnsibleVaultEncryptedUnicode(encrypted_string)
    avu1.vault = vault
    avu1.data
    avu2 = AnsibleVaultEncryptedUnicode(encrypted_string)
    avu2.vault = vault
    avu2.data
    assert avu1 == avu2
    assert not avu1 != avu2


# Generated at 2022-06-13 07:44:07.151293
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    class AnsibleVaultEncryptedUnicode_test():
        def __init__(self, value):
            self.value = value
        def __le__(self, other):
            return self.value <= int(other)
    avtu_1 = AnsibleVaultEncryptedUnicode_test(5)
    avtu_2 = AnsibleVaultEncryptedUnicode_test(10)
    avtu_3 = AnsibleVaultEncryptedUnicode_test(5)
    avtu_4 = "5"
    assert(avtu_1 <= avtu_2)
    assert(avtu_1 <= avtu_3)
    assert(avtu_1 <= avtu_4)


# Generated at 2022-06-13 07:44:21.709202
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Setup test data
    ciphertext = to_bytes('vaultencryptedstring')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.__UNSAFE__ = True
    avu.__ENCRYPTED__ = True
    expected = True

    # create mock object
    mock_vault = MockVault()

    # mock object methods
    mock_vault.decrypt = Mock(side_effect=AnsibleVaultError('Invalid vault password'))
    mock_vault.is_encrypted = Mock(return_value=True)

    # assign mock object to avu
    avu.vault = mock_vault

    # execute test
    result = avu.__eq__('vaultencryptedstring')

    # assert test result
    assert result == expected
    assert mock_v

# Generated at 2022-06-13 07:44:36.195787
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    # unit test for AnsibleVaultEncryptedUnicode __le__
    def get_fields(avu):
        return (avu.vault, avu._ciphertext)

    from ansible.parsing.vault import VaultLib

    vault = VaultLib()

    assert AnsibleVaultEncryptedUnicode(ciphertext="b"*80).__le__("a"*80) == False

    # Vault is None
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext="b"*80)
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext="a"*80)
    assert avu1.__le__(avu2) == False
    assert get_fields(avu1) == (None, "b"*80)
    assert get_fields

# Generated at 2022-06-13 07:44:40.693041
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault = VaultLib("pass")
    avu = AnsibleVaultEncryptedUnicode
    assert avu("!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          61366337363364393565653263393536346532326633393634373566303230663738333261336235\n          3336643466353931626265623362623630386461656234353330663964\n          ").__eq__("") == False

# Generated at 2022-06-13 07:44:49.820980
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    secret = "secret1234"
    v = VaultLib("password")
    ciphertext = v.encrypt("foobar", secret)
    plaintext = v.decrypt(ciphertext, secret)
    assert(plaintext == "foobar")
    assert(type(ciphertext) == bytes)
    avueu = AnsibleVaultEncryptedUnicode.from_plaintext("foobar", v, secret)
    avueu2 = AnsibleVaultEncryptedUnicode.from_plaintext("foobar", v, secret)
    avueu3 = AnsibleVaultEncryptedUnicode.from_plaintext("foobar2", v, secret)
    assert(avueu == avueu2)

# Generated at 2022-06-13 07:44:53.480196
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    assert not AnsibleVaultEncryptedUnicode(None) <= None
    assert not AnsibleVaultEncryptedUnicode(None) <= AnsibleVaultEncryptedUnicode(None)
    assert AnsibleVaultEncryptedUnicode(None) <= ''
    assert AnsibleVaultEncryptedUnicode(None) <= '0'
    assert not AnsibleVaultEncryptedUnicode(None) <= True


# Generated at 2022-06-13 07:45:02.314548
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:08.501732
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:12.576608
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    s = AnsibleVaultEncryptedUnicode()
    s.vault = None
    assert not s.is_encrypted()
    s.vault = vaultlib.VaultLib()
    assert not s.is_encrypted()


# Generated at 2022-06-13 07:45:24.487577
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    yaml_string = """
---
string1: !!python/object/apply:ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode
  args: ["encrypted_string"]
string1_cipher: "encrypted_string"
string2: !!python/object/apply:ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode
  args: ["other_encrypted_string"]
string2_cipher: "other_encrypted_string"
string3: !!python/object/apply:ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode
  args: ["encrypted_string"]
string3_cipher: "encrypted_string"
    """
    from ansible.parsing.yaml.loader import AnsibleLoader

# Generated at 2022-06-13 07:45:35.775494
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    class FakeVault(object):
        def __init__(self, passwd):
            self.password = passwd
        def decrypt(self, encrypted, **kwargs):
            return encrypted.replace(b'ENCRYPTED', self.password)
        def encrypt(self, plain, **kwargs):
            return b'ENCRYPTED' + plain
        def is_encrypted(self, string):
            return string.startswith(b'ENCRYPTED')

    vault = FakeVault(b'password')
    string = AnsibleVaultEncryptedUnicode.from_plaintext(b'a-b-ENCRYPTED-c-d-ENCRYPTED-e', vault, b'password')
    assert string.data == b'a-b-foo-c-d-bar-e'


# Generated at 2022-06-13 07:45:54.520507
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu1 = AnsibleVaultEncryptedUnicode("!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          33333066613236353464663035646635653839306564343336646630653164383530313336613333\n          6165663734353631643730663161626237636236363862376239310a316630373766356661366336\n          66326263316231646532393336303663396536343061396639643564633563373165393565383536\n          36363934356162386139300a\n", vault=None)
    assert avu1.__eq__("foobar") == False

# Generated at 2022-06-13 07:46:01.851994
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    encrypted_str = '$ANSIBLE_VAULT;1.1;AES256;ansible\n363663386232306331383132326461333763393163396231633738333062626237393163623931630a35643561343964396261366131623964303635366439626535643966326462366631623766656432630a6430656130303163623334633531653030326234396631363633376463356233663930366466383364\n'

# Generated at 2022-06-13 07:46:09.137110
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = "ansible"
    vault = VaultLib("ansible")
    ciphertext = b"$ANSIBLE_VAULT;1.1;AES256;ansible\n383065303231336535666131653735613265353630333966363062626232613066343164\n31346639316133393632613130356237303366653332300a363162623334656264363038\n323936353364373436303335343133393766333935663832623236306532333232386636\n6564626131613962663963663963386634620a6633626462390a"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(b"hello", vault, secret)
    av

# Generated at 2022-06-13 07:46:21.926405
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test failing case
    foo = AnsibleVaultEncryptedUnicode(ciphertext="foo")
    failed_message = "foo != foo should be false"

    # Method under test
    assertion_message = "AnsibleVaultEncryptedUnicode.__ne__() Failed"
    assert foo != "foo", assertion_message

    # Test failing case
    bar = AnsibleVaultEncryptedUnicode(ciphertext="bar")
    failed_message = "foo != bar should be true"

    # Method under test
    assertion_message = "AnsibleVaultEncryptedUnicode.__ne__() Failed"
    assert foo != bar, assertion_message


# Generated at 2022-06-13 07:46:27.807874
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode('undef')
    b = AnsibleVaultEncryptedUnicode('undef')
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    a.vault = b.vault = vault
    assert a != b
    assert a != 'undef'
    assert 'undef' != a



# Generated at 2022-06-13 07:46:36.071488
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from .yaml.vault import VaultSecret
    secret = 'secret'
    plaintext = 'plaintext'
    ciphertext = VaultLib(VaultSecret(secret)).encrypt(plaintext, secret)
    assert AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode(plaintext).is_encrypted()



# Generated at 2022-06-13 07:46:48.014538
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Testing __eq__ method of AnsibleVaultEncryptedUnicode class
    plain_text = "passme123"

# Generated at 2022-06-13 07:47:00.396846
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    Test for method AnsibleVaultEncryptedUnicode.__ne__
    """

    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    plain_secret = '123'
    secret = vault.encrypt(plain_secret)
    avu = AnsibleVaultEncryptedUnicode(secret)
    # set vault object to avu object
    avu.vault = vault

    # case 1:
    # the other value is not an AnsibleVaultEncryptedUnicode object
    assert avu.__ne__(plain_secret) is True

    # case 2:
    # the other value is not an AnsibleVaultEncryptedUnicode object
    assert avu.__ne__('123') is True

    # case 3:
    # the other value is an

# Generated at 2022-06-13 07:47:08.842763
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode(
        u'$ANSIBLE_VAULT;1.1;AES256\n'
        '31373263373161363636353330383361323131613931623138376163313837366232353866383739\n'
        '3730353439653464333739663036316364386533653034623665360a393165316330356534386130\n'
        '65616265656636643066343834623739383038656632373566373262656166663466313362366561\n'
        '626634396535636132373932\n'
    )
    avu.vault = vaultlib

# Generated at 2022-06-13 07:47:12.649365
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Compute expected value
    expected = True
    
    # Construct object to be tested
    avu = AnsibleVaultEncryptedUnicode('fuckyou')
    # Call method being tested
    actual = avu.__ne__('what???')

    # Check if expected result is correct
    assert expected == actual


# Generated at 2022-06-13 07:47:26.163412
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Setup
    one = AnsibleVaultEncryptedUnicode("hello")
    one.vault = None
    one_data = AnsibleVaultEncryptedUnicode("world")
    one_data.vault = None
    two = AnsibleVaultEncryptedUnicode("world")
    two.vault = None

    # Exercise
    actual1 = (one == one_data)
    actual2 = (two == one_data)

    # Verify
    assert actual1 == False
    assert actual2 == True


# Generated at 2022-06-13 07:47:37.607381
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])

    # Empty string should not be considered encrypted
    assert not AnsibleVaultEncryptedUnicode(b'').is_encrypted()

    # The first char is control char
    assert AnsibleVaultEncryptedUnicode(b'\n$ANSIBLE_VAULT;1.1;AES256\n'
                                        b'$ANSIBLE_VAULT;1.1;AES256\n').is_encrypted()

    # The first char is not control char
    assert not AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT;1.1;AES256\n'
                                            b'$ANSIBLE_VAULT;1.1;AES256\n').is_encrypted()

    # The first two char

# Generated at 2022-06-13 07:47:46.235425
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foobar', vault=ansible.parsing.vault.VaultLib('foobar'), secret='secret')
    assert avu.is_encrypted() == True

    from ansible.parsing.vault import VaultEditor
    ve = VaultEditor(ansible.parsing.vault.VaultLib('foobar'))
    plaintext = ve.decrypt(avu._ciphertext)
    assert avu.is_encrypted() == False
    assert plaintext == 'foobar'



# Generated at 2022-06-13 07:47:53.887191
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # test case 1
    from ansible.utils.encrypt import get_vault
    vault = get_vault()
    secret = 'password'
    plaintext = 'sensitive data'
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    avu._ciphertext = ciphertext
    assert avu.data == 'sensitive data'
    assert avu == 'sensitive data'
    assert avu != 'sensitive data1'



# Generated at 2022-06-13 07:48:03.010542
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    pw = VaultLib.generate_password()
    plaintext = "secret"
    a = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n          xxxxxxxxxxxxxxxx=\n          '

# Generated at 2022-06-13 07:48:13.498060
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext

    vault = VaultLib([], PlayContext())

    # create a secret string to encrypt.
    # the secret string is made of a list of 6 bytes, repeated 3 times.
    secret = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]*3
    secret_string = to_bytes(''.join([chr(c) for c in secret]))
    # create an encrypted string from the secret string.
    secret_encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(secret_string, vault, 'password')
    # test that the encrypted string is successfully encrypted
    assert secret_encrypted.is_encrypted()
    # decode the encrypted string to recover the secret

# Generated at 2022-06-13 07:48:20.111172
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Initialize vault
    #
    # The vault used in the test was generated with ansible-vault
    # using the default password 'default'.
    import os
    import tempfile
    import ansible.parsing.vault

# Generated at 2022-06-13 07:48:32.467384
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():

    (fn, tmp) = tempfile.mkstemp(prefiex="avu-test-")
    os.close(fn)
    vault = vaultlib.VaultLib(filename=tmp, vault_password='test')

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault, 'test')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('not hello', vault, 'test')
    assert avu1 != avu2
    assert avu2 != avu1

    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault, 'test')
    assert avu1 != avu3
    assert avu3 != avu1

    os.remove(tmp)

_ACCUMULATOR_TAGS = fro