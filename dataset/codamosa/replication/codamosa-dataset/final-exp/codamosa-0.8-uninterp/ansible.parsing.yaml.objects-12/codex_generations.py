

# Generated at 2022-06-13 07:38:45.175571
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_key = 'test'
    vault_id = '$ANSIBLE_VAULT;1.1;AES256'
    data = 'This is a test string'
    vault = VaultLib(vault_key)
    plaintext = vault.decrypt(
        vault.encrypt(data, vault_key), vault_key)
    assert plaintext == data
    return code



# Generated at 2022-06-13 07:38:47.862726
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('bar', None, None)
    assert avu1 == 'bar'
    assert avu1 == avu2


# Generated at 2022-06-13 07:38:58.321862
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    # Check that we can slice a AnsibleVaultEncryptedUnicode
    # and it doesn't raise an exception. We first create a sequence
    # of byte strings and then wrap them in a AnsibleVaultEncryptedUnicode
    # The check is that they slice the same.
    class FakeVault(object):
        def is_encrypted(self, ciphertext):
            return True
        def decrypt(self, ciphertext, obj=None):
            return ciphertext
        def encrypt(self, plaintext, secret):
            return plaintext


# Generated at 2022-06-13 07:39:01.605887
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    a = AnsibleVaultEncryptedUnicode(u'abc')
    b = AnsibleVaultEncryptedUnicode(u'abd')

    assert a <= b


# Generated at 2022-06-13 07:39:06.962605
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    from ansible.parsing.vault import VaultLib
    import getpass
    vault = VaultLib([])
    secret = getpass.getpass("Vault password: ")
    av = AnsibleVaultEncryptedUnicode.from_plaintext("test", vault, secret)
    bv = "test"
    assert av <= bv

# Generated at 2022-06-13 07:39:20.728925
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    eval_str = u'abcdefghijk\n'
    avu_password = u'AvU_Password'

# Generated at 2022-06-13 07:39:28.822474
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    if sys.version_info.major == 2:  # pragma: no cover, not needed in python3
        class UnicodeSubclass(unicode):
            pass

    elif sys.version_info.major == 3:
        class UnicodeSubclass(str):
            pass

    import vault
    import json
    import tempfile
    import os
    vault_password_file = tempfile.NamedTemporaryFile(delete=False)
    vault_password_file.write('%s\n' % vault.get_default_password_file())
    vault_password_file.close()
    os.chmod(vault_password_file.name, 0o600)
    vault_file = tempfile.NamedTemporaryFile(delete=False)
    vault_file.close()

# Generated at 2022-06-13 07:39:36.698619
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    v1 = AnsibleVaultEncryptedUnicode('v1')
    v2 = AnsibleVaultEncryptedUnicode('v2')
    assert v1 < 'v2'
    assert v1 < v2
    assert 'v1' < v2
    assert not (v1 < 'v1')
    assert not (v1 < v1)
    assert not ('v1' < v1)


# Generated at 2022-06-13 07:39:42.680962
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    # Encrypted text with passphrase
    vault = AnsibleVaultLib(b'vaultpassword')
    vault_1 = AnsibleVaultEncryptedUnicode.from_plaintext(u'encrypted1', vault, b'test')
    vault_2 = AnsibleVaultEncryptedUnicode.from_plaintext(u'encrypted2', vault, b'test')
    output = vault_1 + vault_2
    assert output == u'encrypted1encrypted2'

# Generated at 2022-06-13 07:39:50.421810
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.path import unfrackpath

    vault_password_file = 'ansible-vault-password'
    vault_password_file = unfrackpath(vault_password_file)
    vault = VaultLib(vault_password_file, None, None)
    # Change encoding to utf-8 to pass Travis CI
    plaintext = '你好'
    secret = 'ansible-vault-password'
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu < '你好'
    assert not ("" < avu)




# Generated at 2022-06-13 07:40:05.501739
# Unit test for method __ge__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ge__():
    ptext = '5'

# Generated at 2022-06-13 07:40:15.254474
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    plaintext = u"a\0b\0c\0"
    ciphertext = plaintext.encode('utf-8').replace(b'\0', b'\xff')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = FakeVault(ciphertext)

    assert avu[:] == plaintext
    assert avu[1:] == u"\0b\0c\0"
    assert avu[1:2] == u"\0"
    assert avu[:-1] == u"a\0b\0c"
    assert avu[1:-1] == u"\0b\0c"
    assert avu[1:-1:2] == u"\0c"

# Generated at 2022-06-13 07:40:21.904566
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''Ensure that __eq__() works correctly when called'''

# Generated at 2022-06-13 07:40:28.291170
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    vault = vaultlib.VaultLib('mypassword')

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext("myvalue", vault, "mypassword")

    if not avu1.is_encrypted():
        raise Exception("is_encrypted should be True")

    avu2 = AnsibleVaultEncryptedUnicode("myvalue")
    if avu2.is_encrypted():
        raise Exception("is_encrypted should be False")



# Generated at 2022-06-13 07:40:32.119730
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    AVES = AnsibleVaultEncryptedUnicode
    assert (AVES('secret') == 'secret') is True
    assert (AVES('secret') == 'super secret') is False


# Generated at 2022-06-13 07:40:42.553469
# Unit test for method __ge__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ge__():
    from ansible_vault import VaultLib
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', VaultLib(), 'vaultpassword')
    assert(avu1 >= 'foo')
    #assert(not avu1 >= 'bar') # FIXME: test is always false.
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', VaultLib(), 'vaultpassword')
    assert(avu1 >= avu2)
    #assert(not avu1 >= AnsibleVaultEncryptedUnicode.from_plaintext('bar', VaultLib(), 'vaultpassword')) # FIXME: test is always false.
    #assert(avu1 >= 'foo' and not avu1 >= 'bar') # FIXME: test is always false.

# Generated at 2022-06-13 07:40:55.691775
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import base64
    from ansible.parsing.vault import VaultLib

    # An encrypted string that starts with $ANSIBLE_VAULT;1.1;AES256;
    # (that is, a string encrypted by ansible-vault encrypt_string)
    # should be considered encrypted by AnsibleVaultEncryptedUnicode.is_encrypted
    b64_ciphertext = b'JDJlJDEwJGFjLnE4ZlJMQzJwUE8xUFFxZkpOeXpEek5Lb3lndHV2Q2VRJENZV1RKbFhBV2s2LlY2N1NlRmJh'
    ansible_vault_hdr = b'$ANSIBLE_VAULT;1.1;AES256;'


# Generated at 2022-06-13 07:41:03.148491
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    avu1 = AnsibleVaultEncryptedUnicode('test')
    avu2 = AnsibleVaultEncryptedUnicode('test')
    avu3 = AnsibleVaultEncryptedUnicode('test2')

    assert avu1 < avu3
    assert avu1 < 'test2'
    assert not avu1 < 'test'
    assert not avu1 < avu2



# Generated at 2022-06-13 07:41:09.253785
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    s = 'string'
    s2 = 'string2'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(s, VaultLib(), 'password')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(s2, VaultLib(), 'password')
    assert avu != s
    assert avu != avu2



# Generated at 2022-06-13 07:41:21.380539
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    if sys.version_info < (3,0):
        assert u'1' + AnsibleVaultEncryptedUnicode.from_plaintext(u'2', None, None) == u'12'
        assert u'1' + AnsibleVaultEncryptedUnicode.from_plaintext(u'2', None, None).data == u'12'
        assert AnsibleVaultEncryptedUnicode.from_plaintext(u'1', None, None).data + u'2' == u'12'
        assert AnsibleVaultEncryptedUnicode.from_plaintext(u'1', None, None) + u'2' == u'12'
    else:
        assert '1' + AnsibleVaultEncryptedUnicode.from_plaintext('2', None, None) == '12'

# Generated at 2022-06-13 07:41:32.833253
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    msg = 'Error for class AnsibleVaultEncryptedUnicode.__ne__'
    avu = AnsibleVaultEncryptedUnicode('abc123')
    avu.vault = None
    assert avu != u'abc123', msg
    assert avu != 'abc123', msg
    assert avu != 123, msg
    assert avu != u'abc234', msg
    assert avu != 'abc234', msg
    assert avu != 234, msg
    assert not avu != u'abc123', msg
    assert not avu != 'abc123', msg



# Generated at 2022-06-13 07:41:37.341200
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Check several cases where __ne__ should return True
    # First check that it returns False when it should
    test_obj = AnsibleVaultEncryptedUnicode('test')
    assert test_obj != 'test'

    # Now check that it returns False when it should
    assert test_obj != 'test_obj'


# Generated at 2022-06-13 07:41:44.482527
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = "this is my secret"

# Generated at 2022-06-13 07:41:53.131760
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import sys
    import crypt

    if sys.version_info[0] == 2:
        from ansible.parsing.vault import VaultLib
    else:
        # Python3 has no dependency to PyCrypto
        # We can use a simple dummy class to return
        # arbitrary encrypted strings
        class DummyVaultLib(object):
            def __init__(self, password=None, salt_size=None, algo='', cipher='', keysize=None, iterations=None):
                pass

            def get_vault_header(self):
                return '$ANSIBLE_VAULT;1.1;AES256'


# Generated at 2022-06-13 07:42:02.836115
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import crypt
    import crypt.vault
    av = crypt.vault.VaultLib([])
    plain = "some plain text"
    cipher_plain = AnsibleVaultEncryptedUnicode.from_plaintext(plain, av, b'secret')
    assert cipher_plain.is_encrypted() == True
    cipher_cipher = AnsibleVaultEncryptedUnicode.from_plaintext(cipher_plain.data, av, b'secret')
    assert cipher_cipher.is_encrypted() == True
    assert cipher_cipher.data == cipher_plain.data

# Backward compatible names
_AnsibleUnsafeText = AnsibleUnicode
_AnsibleUnsafeBytes = AnsibleVaultEncryptedUnicode



# Generated at 2022-06-13 07:42:12.839278
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    # Ensure that negative starts and ends are handled correctly
    avu = AnsibleVaultEncryptedUnicode(b'test')
    assert avu.__getslice__(0, 4) == 'test'
    assert avu.__getslice__(0, None) == 'test'
    assert avu.__getslice__(-4, 4) == 'test'
    assert avu.__getslice__(-4, None) == 'test'
    assert avu.__getslice__(-4, -1) == 'tes'
    assert avu.__getslice__(1, -1) == 'est'
    assert avu.__getslice__(1, None) == 'est'
    assert avu.__getslice__(1, 1) == ''
    assert avu.__getsl

# Generated at 2022-06-13 07:42:16.416260
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """Test for AnsibleVaultEncryptedUnicode."""
    from ansible.parsing.vault import VaultLib

    secret = VaultLib()
    string = u'hello!'
    unicode = AnsibleVaultEncryptedUnicode.from_plaintext(string, secret, b'secret')

    assert unicode != string

# Generated at 2022-06-13 07:42:19.281199
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    av = AnsibleVaultEncryptedUnicode("abc")
    assert av == "abc"
    assert "abc" == av
    assert "abx" != av
    assert av != "abx"


# Generated at 2022-06-13 07:42:22.078706
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ciphertext = to_bytes('This is a test')
    avue = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avue != ciphertext
    assert ciphertext != avue


# Generated at 2022-06-13 07:42:25.993989
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    s = AnsibleVaultEncryptedUnicode('test')
    assert s != 'test'
    s.data = 'test'
    assert s != 'test'


# Generated at 2022-06-13 07:42:37.296839
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test which password is invalid
    if len(_sys.argv) != 2:
        raise AssertionError("Please specify a valid Ansible Vault password")
    password = _sys.argv[1]
    encrypted_string = AnsibleVaultEncryptedUnicode.from_plaintext('test_string', vault=None, secret=password)
    assert encrypted_string == 'test_string'

# Generated at 2022-06-13 07:42:42.303291
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''
    Test method __eq__ of class AnsibleVaultEncryptedUnicode
    This method is called when the comparison operator == is used to compare a AnsibleVaultEncryptedUnicode object
    and another object.
    :return: None
    '''
    from ansible_vault import VaultLib
    import tempfile

    vault = VaultLib()
    secret = 'test'
    # Test with a non-encrypted object
    test_object = AnsibleVaultEncryptedUnicode('test_string')
    assert test_object.__eq__(secret) == False
    assert test_object.__ne__(secret) == True
    # Test with an encrypted object
    test_object = AnsibleVaultEncryptedUnicode.from_plaintext(secret, vault=vault, secret=secret)

# Generated at 2022-06-13 07:42:53.321090
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = b"asdf"
    plaintext = b"baobab"

# Generated at 2022-06-13 07:43:05.338585
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import sys
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(password='test')

    if (sys.version_info > (3, 0)):
        # Python3
        plain_text = 'test'
        ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext(plain_text, vault,'test')
        assert ansible_vault_encrypted_unicode.is_encrypted()

        plain_text = u'test'.encode('utf-8')
        ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext(plain_text, vault,'test')
        assert ansible_vault_encrypted_unicode.is_encrypted()

        plain_text = 'test'

# Generated at 2022-06-13 07:43:17.001818
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultLibOptions
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword
    vault_secret = VaultSecret('secret')
    vault_password = VaultPassword(None, 'password')
    vault_options = VaultLibOptions(vault_password, 1)
    vault = VaultLib(vault_options, vault_secret)
    avu_empty = AnsibleVaultEncryptedUnicode('')
    avu_empty.vault = vault
    avu_zero = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;0.1;AES256')
    avu_zero.vault = vault
    avu_enc = Ans

# Generated at 2022-06-13 07:43:29.576777
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    When a AnsibleVaultEncryptedUnicode object is compared for inequality
    with a string, it returns False only if the AnsibleVaultEncryptedUnicode
    object is not encrypted, and the string matches the plaintext of the object.
    '''

    # All these tests are successful
    assert AnsibleVaultEncryptedUnicode("") != "asdf"
    assert AnsibleVaultEncryptedUnicode("asdf") != "asdff"
    assert AnsibleVaultEncryptedUnicode("asdf") != AnsibleUnicode("asdff")

    # All these tests are unsuccessful, as the ansiblevault unicode is encrypted
    # and not equal to the plaintext string
    assert not(AnsibleVaultEncryptedUnicode("") != "")

# Generated at 2022-06-13 07:43:34.561578
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode('hello') != AnsibleVaultEncryptedUnicode('hello')
    assert not AnsibleVaultEncryptedUnicode('hello') != AnsibleVaultEncryptedUnicode('')


# Generated at 2022-06-13 07:43:42.598510
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    """AnsibleVaultEncryptedUnicode method is_encrypted should return the correct boolean value"""

    class VaultMock(object):
        """Mock the Vault class"""
        def is_encrypted(self, plaintext):
            return False

    import mock
    sys.modules['ansible.parsing.vault'] = mock.Mock(spec=['VaultLib'])
    sys.modules['ansible.parsing.vault'].VaultLib = VaultMock
    from ansible.parsing.vault import VaultLib

    avu = AnsibleVaultEncryptedUnicode('foo')
    assert avu.is_encrypted() is False
    avu.vault = VaultLib()
    assert avu.is_encrypted() is False
    assert avu.is_encrypted

# Generated at 2022-06-13 07:43:47.878301
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    plaintext = 'plaintext'
    ciphertext = vault.encrypt(plaintext)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert (avu == plaintext)
    assert (avu != ciphertext)
    assert (avu != 'not a match')


# Generated at 2022-06-13 07:43:53.338591
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'secret'
    vault = VaultLib(secret)
    seq = 'dont decrypt this'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:44:07.914154
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n3938663437373530343566656138623265346235656637373532386465303734333766643263633565\n3631323530386438656664643138333162313938663437373530343566656138623265346235656637\n373532386465303734333766643263633565363131\n')
    assert avu.is_encrypted()

# Generated at 2022-06-13 07:44:11.630263
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode("ciphers are cool")
    avu.vault = yaml
    # Act
    actual = avu.__ne__("ciphers are cool")
    # Assert
    assert not actual



# Generated at 2022-06-13 07:44:17.999528
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    plaintext = 'plaintext'
    secret = 'password'
    vault_class = type(sys.modules['ansible.plugins.vault'].VaultLib)
    vault = vault_class(filename=None, password=secret)
    encrypted_text = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert encrypted_text != 'plaintext'
    assert encrypted_text != AnsibleVaultEncryptedUnicode.from_plaintext('plaintext', vault, 'wrongsecret')



# Generated at 2022-06-13 07:44:23.687983
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode(b'hello') != b'hello'
    assert AnsibleVaultEncryptedUnicode(b'hello') != u'hello'
    assert AnsibleVaultEncryptedUnicode(b'hello') != to_text(b'hello')
    assert AnsibleVaultEncryptedUnicode(u'hello') != b'hello'
    assert AnsibleVaultEncryptedUnicode(u'hello') != u'hello'
    assert AnsibleVaultEncryptedUnicode(u'hello') != to_text(b'hello')
    assert AnsibleVaultEncryptedUnicode(to_text(b'hello')) != to_text(b'hello')


# Generated at 2022-06-13 07:44:28.887796
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Check that, when data is None, False is returned
    # (this is obviously not the encrypted text, but we need to check that
    # it works in case AnsibleVaultEncryptedUnicode is constructed with None)
    msg = "AnsibleVaultEncryptedUnicode(None) should return False in __eq__"
    assert AnsibleVaultEncryptedUnicode(None) == None, msg

    # Check that, when data is not None and not an AnsibleVaultEncryptedUnicode,
    # False is returned
    msg = "AnsibleVaultEncryptedUnicode(None) should return False in __eq__"
    assert AnsibleVaultEncryptedUnicode('abc') == 'abc', msg

    # Check that, when data is an AnsibleVaultEncryptedUnicode,
    # the result is

# Generated at 2022-06-13 07:44:39.971577
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = b'ansible'
    password = b'password'

# Generated at 2022-06-13 07:44:49.210142
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert not AnsibleVaultEncryptedUnicode('foo').is_encrypted()
    assert AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256').is_encrypted()

if __name__ == '__main__':
    from ansible.vault import VaultLib
    vault = VaultLib('foo')
    # Test the AnsibleVaultEncryptedUnicode.from_plaintext() constructor
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('baz', vault, 'foo')
    assert avu[1] == 'A'
    assert avu.data == 'baz'
    # Test the AnsibleVaultEncryptedUnicode constructor

# Generated at 2022-06-13 07:44:59.954452
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
  x = AnsibleVaultEncryptedUnicode(text_type(b'\x16\x02\x00\x00\xb3\x91\x16\x96p\xfd\xf9\xa8\xe1\x1cd\x03\xbb\x8c\x13\x00\x19\x9f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x00\x00\x00\x00\x00\x00\x00\x90\x01\x00\x00\x00\x00\x00\x00\x13\x00\x19\x9f'))
  y = 'x'
  assert str(x) != y

# Generated at 2022-06-13 07:45:05.450879
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    avue = AnsibleVaultEncryptedUnicode.from_plaintext('foo', VaultLib('secret'), 'secret')
    assert 'foo' != avue
    assert AnsibleVaultEncryptedUnicode('foo') != avue
    assert avue != 'foo'

# Generated at 2022-06-13 07:45:08.510475
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    v = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    assert v == 'test'
    assert v != 'other'
    assert not (v == 'other')


# Generated at 2022-06-13 07:45:17.270889
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    v = VaultLib([])
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', v, 'secret')
    assert avu.is_encrypted()


# Generated at 2022-06-13 07:45:22.357175
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansiblevault import VaultLib
    vault = VaultLib('password')
    ciphertext = vault.encrypt('foo', salt=None)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert(avu == 'foo')



# Generated at 2022-06-13 07:45:29.176877
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:35.548079
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    e = AnsibleVaultEncryptedUnicode.from_plaintext('password', vault=None, secret=None)

    assert e.__eq__('password')
    assert e.__eq__(u'password')
    assert not e.__eq__('123')
    assert not e.__eq__(u'123')
    assert not e.__eq__(None)



# Generated at 2022-06-13 07:45:44.952278
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class MockVault():
        def encrypt(self, seq, secret):
            return seq
        def decrypt(self, seq, obj):
            return seq
        def is_encrypted(self, ciphertext):
            return False

    vault = MockVault()
    secret = 'secret'

    avue = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault, secret)
    assert avue == avue.data
    assert avue.__eq__('hello')
    assert avue.__eq__(avue)

    assert not avue.__ne__(avue.data)
    assert not avue.__ne__('hello')
    assert not avue.__ne__(avue)


# Generated at 2022-06-13 07:45:54.198268
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Test with the library (pip install pycrypto)
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultAES256CBC

    secret = VaultSecret('secret')
    vault_ciphers = {
        'aes256-cbc': VaultAES256CBC,
        'aes256': VaultAES256,
    }
    vault_lib = VaultLib(vault_ciphers, secret)

    ciphertext = vault_lib.encrypt('test_string')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu.is_encrypted()

    # Test that it is also

# Generated at 2022-06-13 07:46:01.557378
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing import vault as ansible_vault
    from ansible.parsing.vault import VaultLib

    vault = ansible_vault.VaultLib([u'ansible', u'ansible'])
    secret = vault.get_decryption_key()
    secure_str = u'MySuperSecretString!'
    secure = AnsibleVaultEncryptedUnicode.from_plaintext(secure_str, vault, secret)

    assert (secure == u'') is False
    assert (secure == u'MySuperSecretString!') is False
    assert (secure == AnsibleVaultEncryptedUnicode.from_plaintext(secure_str, vault, secret)) is False

# Generated at 2022-06-13 07:46:08.886822
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError

    secret = '$ecret!'

    # Encrypted matches cleared
    ciphertext = VaultLib(password=None).encrypt(secret, secret)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(secret, VaultLib(password=secret), secret)
    assert(avu == secret)
    assert(avu == ciphertext)

    # Cleared matches cleared
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(secret, None, None)
    assert(avu == secret)

    # Both encrypted, but different
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(secret, VaultLib(password=secret), secret)


# Generated at 2022-06-13 07:46:23.794518
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    plaintext = "I will be encrypted."
    vault = "dont_add_to_module_utils"
    secret = "dont_add_to_module_utils"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    # test a non AnsibleVaultEncryptedUnicode object
    string = "I will be compared."
    assert avu.__ne__(string), "AnsibleVaultEncryptedUnicode.__ne__(string) should return True"
    # test an AnsibleVaultEncryptedUnicode object
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

# Generated at 2022-06-13 07:46:34.104001
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(None)
    secret = 'testsecret'
    plaintext = 'testplaintext'
    ciphertext = vault.encrypt(plaintext, secret)

    # test with matching instances
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu1.vault = vault
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault = vault
    assert avu1 == avu2

    # test with non matching instances
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu1.vault = vault
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault

# Generated at 2022-06-13 07:46:45.846791
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('abc')
    avu.vault = 'foo' # a not-None value
    assert(avu != 'foo')
    assert(not (avu != 'abc'))


# Generated at 2022-06-13 07:46:49.251069
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    obj = AnsibleVaultEncryptedUnicode.from_plaintext('fake_str', vault, 'fake_password')
    assert obj.is_encrypted()



# Generated at 2022-06-13 07:47:01.322479
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    # data
    password = 'password'
    vault = VaultLib(password)

# Generated at 2022-06-13 07:47:07.231635
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # Secret to be encrypted and decrypted
    secret = 'Test secret...'

    # The vault encrypts a file based on the password
    vault = VaultLib('ansible')

    # A new AnsibleVaultEncryptedUnicode object is created using a secret
    seq = AnsibleVaultEncryptedUnicode.from_plaintext(secret, vault, 'ansible')

    # Verify that the method is_encrypted returns True
    assert seq.is_encrypted()


# Generated at 2022-06-13 07:47:13.863567
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create a secret for encryption and decryption
    secret_key = "BASE64ENCRYPTEDSECRET=="
    vault = VaultLib(secret_key)

    # Create an AnsibleVaultEncryptedUnicode object
    ciphertext = vault.encrypt("some_secret", secret_key)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    # The AnsibleVaultEncryptedUnicode object is equal to the plaintext string
    # with which it was created
    assert avu == "some_secret"


# Generated at 2022-06-13 07:47:20.270831
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib('vaultsecret')
    encrypted_string = AnsibleVaultEncryptedUnicode.from_plaintext(u'bar', vault, b'secret')

    assert encrypted_string != u'bar'
    assert encrypted_string != 'foo'
    assert encrypted_string != AnsibleVaultEncryptedUnicode.from_plaintext(u'bar', vault, b'bar')

# Generated at 2022-06-13 07:47:26.178658
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('secret', VaultLib('password'), 'password')
    assert avu == to_text('secret')
    assert not (avu != to_text('secret'))
    assert avu != to_text('not_secret')
    assert not (avu == to_text('not_secret'))

# Loader below is a modified version of AnsibleLoader in ansible.parsing.yaml.loader
# It is necessary to perform the __setstate__ operation on objects in the data.
# If a vault object is encrypted it will be decrypted.


# Generated at 2022-06-13 07:47:27.522722
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:47:38.676494
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    fh = open('../test/test-vault.yml', 'rb')
    yaml_text = to_text(fh.read(), errors='surrogate_or_strict')
    res = yaml.load(yaml_text, Loader=AnsibleVaultSafeLoader)

    # Each AnsibleVaultEncryptedUnicode is expected to have its vault attribute set.
    for evu in res['vars'].values():
        assert isinstance(evu, AnsibleVaultEncryptedUnicode)
        # Test to verify that the vault attribute is set
        assert evu.vault is not None
        # Test to verify that its really a vaultlib obj
        assert isinstance(evu.vault, VaultLib)

    # Test to verify

# Generated at 2022-06-13 07:47:49.736098
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import ZERO_UUID
    from ansible.parsing.vault import get_file_vault_secret
    from ansible.parsing.vault import get_vault_secret
    from ansible.parsing.vault import is_encrypted
    from ansible.parsing.vault import is_binary_string
    # ansible/lib/ansible/parsing/vault/init.py

    obj1 = AnsibleVaultEncryptedUnicode("value1")
    obj2 = AnsibleVaultEncryptedUnicode("value2")


# Generated at 2022-06-13 07:48:12.466131
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Test method __eq__() of class AnsibleVaultEncryptedUnicode.
    """

    # Test if comparison works when object is not encrypted
    string = "this is a test"
    avu = AnsibleVaultEncryptedUnicode(string)
    assert avu == "this is a test"

    # Test if comparison works when object is encrypted
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("this is a test", vault=None, secret="changeme")
    assert avu == "this is a test"


# Generated at 2022-06-13 07:48:18.898903
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Testing for __eq__ is done by first constructing an AnsibleVaultEncryptedUnicode object
    # from a plaintext string. We then assert that this object is equal to the plaintext that
    # it was created from. We also assert that __eq__ returns False if the argument is a different
    # string.
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('ansible')
    secret = 'ansible-secret'
    plaintext = 'super-secret'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert avu == plaintext
    assert avu != 'something-else'


# Generated at 2022-06-13 07:48:25.531778
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test123')
    ciphertext = vault.encrypt('data')
    a = AnsibleVaultEncryptedUnicode(ciphertext)
    a.vault = vault
    b = a.__eq__('data')
    assert b == True, 'Expected b == True'


# Generated at 2022-06-13 07:48:32.675244
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test with string, should return False
    testString = b'Test String'
    vaultObject = AnsibleVaultEncryptedUnicode(testString)
    assert vaultObject != testString

    # Test with AnsibleVaultEncryptedUnicode, should return True
    testVaultObject = AnsibleVaultEncryptedUnicode(testString)
    assert vaultObject == testVaultObject
