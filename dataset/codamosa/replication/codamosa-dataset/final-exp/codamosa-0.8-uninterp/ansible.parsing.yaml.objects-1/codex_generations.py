

# Generated at 2022-06-13 07:38:47.271792
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    # str slice start at 0
    aveu = AnsibleVaultEncryptedUnicode("secret77")
    assert aveu[0:5] == "secret"
    # str slice start at 1
    aveu = AnsibleVaultEncryptedUnicode("secret77")
    assert aveu[1:5] == "ecret"
    # str slice start at 1, end at 2
    aveu = AnsibleVaultEncryptedUnicode("secret77")
    assert aveu[1:2] == "e"
    # str slice start at 1, end at 6
    aveu = AnsibleVaultEncryptedUnicode("secret77")
    assert aveu[1:6] == "ecret"
    # str slice start at -1
    aveu = AnsibleVaultEncryptedUn

# Generated at 2022-06-13 07:38:53.301591
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:38:59.329821
# Unit test for method replace of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_replace():
    from ansible.parsing.vault import VaultLib
    secret = 'test'
    ciphertext = VaultLib(password=secret).encrypt('foo')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = VaultLib(password=secret)
    assert avu.replace('f','b') == 'boo'
    assert avu.replace(avu,'b') == 'boo'
    assert avu.replace('f','b',1) == 'boo'
    assert avu.replace(avu,'b',1) == 'boo'



# Generated at 2022-06-13 07:39:06.179173
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(b'ansible')
    assert AnsibleVaultEncryptedUnicode.from_plaintext(b'foo', vault, b'ansible') == b'foo'
    assert AnsibleVaultEncryptedUnicode.from_plaintext(b'foo', vault, b'ansible') != b'bar'


# Generated at 2022-06-13 07:39:16.060984
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    avu = AnsibleVaultEncryptedUnicode(b"abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc")

    # Cases in which rfind result matches the rfind result of the AnsibleVaultEncryptedUnicode data
    assert avu.rfind(b'a') == avu.data.rfind(b'a') == avu.rfind(b'a')
    assert avu.rfind(b'b') == avu.data.rfind(b'b') == avu.rfind(b'b')
    assert avu.rfind(b'c') == avu.data.rfind(b'c') == avu.rfind(b'c')

    # Cases in which rfind result matches the rfind result of the AnsibleVaultEncryptedUn

# Generated at 2022-06-13 07:39:20.242110
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'test')
    assert avu == 'test'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test2', vault, 'test')
    assert avu != 'test'


# Generated at 2022-06-13 07:39:27.049825
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu_1 = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n776f5a57335e7b7d1e7545715c7a2d2b695c7b3836646d3f7b3e556674706466\n64346d6e313244383936794150783547\n')
    avu_2 = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n776f5a57335e7b7d1e7545715c7a2d2b695c7b3836646d3f7b3e556674706466\n64346d6e313244383936794150783547\n')
    avu_3

# Generated at 2022-06-13 07:39:40.785156
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.parsing.vault import VaultLib

    # The following alphabet is used to test __getslice__
    test_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Initialize the Vault password
    vault_secret = 'password'

    # Initialize the vault object
    vault = VaultLib(vault_secret)

    # Encrypt the test alphabet
    test_alphabet_encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(test_alphabet, vault, vault_secret)

    # Some tests of __getslice__
    assert test_alphabet_encrypted[0] == test_alphabet[0]

# Generated at 2022-06-13 07:39:44.884879
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    '''
    Tests method __getslice__ of class AnsibleVaultEncryptedUnicode.
    '''
    test_str = 'test'
    test_slice = AnsibleVaultEncryptedUnicode(test_str)[1:3]
    assert test_slice == 'es'


# Generated at 2022-06-13 07:39:45.895626
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    pass # TODO


# Generated at 2022-06-13 07:40:11.637169
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class TestVault(object):
        def __init__(self, secret):
            self.secret = secret
        def encrypt(self, plaintext, secret=None):
            assert secret == self.secret
            return plaintext
        def decrypt(self, ciphertext, obj=None):
            return ciphertext
        is_encrypted = lambda self, txt: txt == 'encrypted'

    vault = TestVault('some secret')
    plaintext = AnsibleVaultEncryptedUnicode.from_plaintext('plain', vault, vault.secret)
    plaintext2 = AnsibleVaultEncryptedUnicode.from_plaintext('plain2', vault, vault.secret)
    assert plaintext == 'plain'
    assert plaintext != 'plain2'
    assert plaintext == plaintext2
    assert plaintext != 'plain2'
   

# Generated at 2022-06-13 07:40:21.653077
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # FIXME: remove this test when AnsibleVaultEncryptedUnicode is moved to its own module
    from ansible.module_utils.vault import VaultLib
    vault_id = 'ansible_test_vault'
    vault_password = 'ansible123'
    vault = VaultLib(vault_password)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'The quick brown fox jumps over the lazy dog', vault, vault_password)
    assert avu.is_encrypted() == True
    # make sure it's not encrypted after decrypting
    avu.data
    assert avu.is_encrypted() == False


# Generated at 2022-06-13 07:40:30.945589
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    c = to_bytes("0123456789")
    u = AnsibleVaultEncryptedUnicode(c)
    f = AnsibleVaultEncryptedUnicode(to_bytes("3"))
    assert u.rfind(f) == 3
    assert u.rfind(f, 1) == 3
    assert u.rfind(f, 2) == 3
    assert u.rfind(f, 3) == 3
    assert u.rfind(f, 4) == -1
    assert u.rfind(f, 1, 1) == -1
    assert u.rfind(f, 1, 2) == -1
    assert u.rfind(f, 1, 3) == 3
    assert u.rfind(f, 4, 4) == -1
    assert u.rfind(f, 4, 5)

# Generated at 2022-06-13 07:40:35.400746
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleMapping()
    avu.vault = "placeholder"
    avu_data = "placeholder"
    avu.data = avu_data

    assert (avu != "other")
    assert not (avu != avu_data)


# Generated at 2022-06-13 07:40:45.064513
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing import vault

    def assertVaultEqualPlain(plain, encrypted):
        vault = vault_create()
        encrypted_text = vault.encrypt(plain)
        vault_encrypted_obj = vault.decrypt(encrypted_text)
        vault_plaintext_obj = vault.decrypt(plain)
        plain_obj = AnsibleVaultEncryptedUnicode(plain)
        plain_obj.vault = vault
        # Call the method with an AnsibleVaultEncryptedUnicode object and compare the result
        assert plain_obj == vault_encrypted_obj
        assert plain_obj == vault_plaintext_obj
        assert plain_obj != encrypted
        assert plain_obj != plain

    def assertVaultEqualEncrypted(plain, encrypted):
        vault = vault_create()

# Generated at 2022-06-13 07:40:49.824307
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class DummyVault(object):

        @classmethod
        def is_encrypted(cls, ciphertext):
            return False

    ciphertext = '$ANSIBLE_VAULT;1.2;AES256;key123\n1234567890123456\n'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = DummyVault
    assert avu != '1234567890123456'

    DummyVault.is_encrypted = lambda ciphertext: True
    assert avu != '1234567890123456'


# Generated at 2022-06-13 07:40:57.746830
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # import vault for testing purposes
    from ansible.parsing import vault

    # test case 1
    unencrypted_text = "hello"
    u = AnsibleVaultEncryptedUnicode(unencrypted_text)
    assert not u.is_encrypted()

    # test case 2
    # encrypt some text
    vault_pass = "password"
    v = vault.VaultLib(vault_pass)
    encrypted_text = v.encrypt(unencrypted_text)
    u = AnsibleVaultEncryptedUnicode(encrypted_text)
    # check that is_encrypted returns True
    assert u.is_encrypted()


# Generated at 2022-06-13 07:41:08.254417
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    Tests for AnsibleVaultEncryptedUnicode.__ne__() method

    AnsibleVaultEncryptedUnicode.__ne__() method returns True if encrypted data
    is not same as plaintext and False if same.
    '''
    # Case 1: encrypted data is same as plaintext
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('simple string', None, None)
    assert(avu.data == avu.data)

    # Case 2: encrypted data is not same as plaintext
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('simple string', None, None)
    assert(avu != 'simple string')


# Generated at 2022-06-13 07:41:19.881997
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    assert AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 10) == 7
    assert AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 7) == 7
    # print AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 6)
    assert AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 6) == -1
    assert AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 5) == -1
    assert AnsibleVaultEncryptedUnicode('python').rfind('on', 0, 4) == -1


# Generated at 2022-06-13 07:41:29.967126
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    # Test case 1:
    # The passed keyword is a AnsibleVaultEncryptedUnicode object
    a = AnsibleVaultEncryptedUnicode('A1A')
    b = AnsibleVaultEncryptedUnicode('A')
    c = AnsibleVaultEncryptedUnicode('1')
    assert a.rfind(b) == 1
    assert a.rfind(c) == 2
    # Test case 2:
    # The passed keyword is a string
    a = AnsibleVaultEncryptedUnicode('A1A')
    b = 'A'
    c = '1'
    assert a.rfind(b) == 1
    assert a.rfind(c) == 2
    # Test case 3:
    # The start position is set

# Generated at 2022-06-13 07:41:37.023533
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    test_avu = AnsibleVaultEncryptedUnicode("abc")
    test_avu.vault = 1
    assert(test_avu == "abc")


# Generated at 2022-06-13 07:41:44.251857
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    # first create a vault encrypted string for the test
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')
    enc_text = AnsibleVaultEncryptedUnicode.from_plaintext('my secret', vault, 'password')

    # test 1: insted of a AnsibleVaultEncryptedUnicode object the method is called with the plaintext
    assert enc_text == 'my secret'
    assert enc_text != 'other text'

    # test 2: insted of a AnsibleVaultEncryptedUnicode object the method is called with a AnsibleVaultEncryptedUnicode object
    # create another vault encrypted string
    enc_text2 = AnsibleVaultEncryptedUnicode.from_plaintext('my secret', vault, 'password')

    # test 2.1: test with two

# Generated at 2022-06-13 07:41:49.036222
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    a = AnsibleVaultEncryptedUnicode('a')
    b = AnsibleVaultEncryptedUnicode('b')
    c = AnsibleVaultEncryptedUnicode('b')
    assert(a != b)
    assert(b == c)
    assert(b != a)


# Generated at 2022-06-13 07:41:57.043238
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    try:
        from ansible.parsing.vault import VaultLib
    except ImportError:
        raise SkipTest("VaultLib not available, skipping tests\n")

    from ansible.parsing.vault import VaultLib

    def create_vault_encrypted_unicode(ciphertext):
        obj = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)
        obj._ciphertext = ciphertext
        return obj

    vault = VaultLib('foo')
    secret = 'bar'
    ciphertext = vault.encrypt('foo', secret)
    nonciphertext = 'foo'

    assert not create_vault_encrypted_unicode(nonciphertext).is_encrypted()
    assert create_vault_encrypted_unicode(ciphertext).is_encrypted()

# Generated at 2022-06-13 07:42:06.072252
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class VaultStub():
        def __init__(self, ciphertext):
            self.ciphertext = to_bytes(ciphertext)

        def encrypt(self, plaintext, secret):
            return self.ciphertext

        def decrypt(self, ciphertext, obj=None):
            return to_text(self.ciphertext)

        def is_encrypted(self, ciphertext):
            return False

    avueu = AnsibleVaultEncryptedUnicode('test_string')
    avueu.vault = VaultStub('test_string')
    assert(avueu == 'test_string')
    assert(not avueu == 'test_string_not_equal')
    assert(not avueu != 'test_string')
    assert(avueu != 'test_string_not_equal')

#

# Generated at 2022-06-13 07:42:15.181204
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:24.011328
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    f = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes("Password"), False, "")
    assert f == "Password"
    f = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes("Password"), True, "")
    assert f != "Password"
    f = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes("Password"), False, "")
    assert f != "password"
    f = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes("Password"), False, "")
    g = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes("Password"), False, "")
    assert f == g


# Generated at 2022-06-13 07:42:33.357435
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    expected = True
    plaintext = 'test'
    vault = VaultLib('vaultpassword')
    vaulted = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, 'encryptionpassword')
    new_vaulted = AnsibleVaultEncryptedUnicode(vaulted._ciphertext)
    new_vaulted.vault = vault
    result = vaulted == new_vaulted

    assert(expected == result)


# Generated at 2022-06-13 07:42:39.082396
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class AnsibleVaultTest():
        def __init__(self, password):
            self.password = password
            self.iv = None
            self.key = None
            self.auth_key = None
            self.cipher = None
            self.digest = None

        def encrypt(self, data):
            return data

        def decrypt(self, data):
            return data

        def is_encrypted(self, data):
            return False

    class TestAVUE(AnsibleVaultEncryptedUnicode):
        def __init__(self, data):
            self._ciphertext = data
            self.vault = AnsibleVaultTest("secret")

        def __repr__(self):
            return self.data

        def __str__(self):
            return self.data

    # Create a AVU object with

# Generated at 2022-06-13 07:42:49.591513
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = b'$ecret'
    vault = VaultLib(password=secret)

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(b'foo', vault, secret)

    assert avu1.is_encrypted() is True
    assert avu1 == b'foo'
    assert avu1 == u'foo'
    assert avu1 == avu1
    assert avu1 == 'foo'
    assert avu1 != b'bar'
    assert avu1 != u'bar'
    assert avu1 != 'bar'
    assert avu1 != AnsibleVaultEncryptedUnicode.from_plaintext(b'bar', vault, secret)

try:
    import vaultlib
    from vaultlib import VaultLib
except ImportError:
    vaultlib = False

# Generated at 2022-06-13 07:43:08.818701
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class DummyVault:
        def __init__(self, secret):
            self._secret = secret

        def encrypt(self, data, secret):
            if secret != self._secret: raise ValueError("Bad secret")
            return "ENC[{}]".format(data)

        def decrypt(self, data, obj):
            if isinstance(data, text_type):
                data = to_bytes(data)
            if not data.startswith("ENC[") or not data.endswith("]"):
                raise ValueError("Cannot decrypt")

            return to_text(data[4:-1], errors='surrogate_or_strict')

        def is_encrypted(self, data):
            return data.startswith("ENC[") and data.endswith("]")

    secret = "secret"
    avue

# Generated at 2022-06-13 07:43:14.240462
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode(b'foo')
    s = ''
    assert avu != s

    avu = AnsibleVaultEncryptedUnicode(b'')
    s = 'foo'
    assert avu != s

    avu = AnsibleVaultEncryptedUnicode(b'foo')
    s = 'foo'
    assert avu != s



# Generated at 2022-06-13 07:43:21.576287
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Case:
    #   AnsibleVaultEncryptedUnicode.__ne__ used for unicode with vault
    #   returning false.
    # Expected result:
    #   False
    avu = AnsibleVaultEncryptedUnicode(b'\xec\xa6\x8b\x98\x91\x84\x89\x85\x8e\x9f\x9c\xc3\x8d')
    avu.vault = AnsibleVaultLib()
    assert avu.__ne__(u'\u6b322')
    # Case:
    #   AnsibleVaultEncryptedUnicode.__ne__ used for unicode with vault
    #   returning true.
    # Expected result:
    #   True

# Generated at 2022-06-13 07:43:29.780331
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    secret = 'secret'
    vault = VaultLib('!')
    plaintext = 'secret_text_string'
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    if not avu == plaintext:
        raise AssertionError('__eq__: "%s" != "%s"' % (avu, plaintext))


# Generated at 2022-06-13 07:43:34.777456
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    result = (AnsibleVaultEncryptedUnicode('BhpaUY7fUY8Zot2MnRmRJTmT6NBECmEB') != 'foo')
    assert result is True


# Generated at 2022-06-13 07:43:49.361392
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault_password = 'iloveyou'

    vault_string = AnsibleVaultEncryptedUnicode.from_plaintext('hello\nworld', vault_password)
    assert vault_string == 'hello'
    assert not(vault_string == 'world')

    vault_string = AnsibleVaultEncryptedUnicode.from_plaintext('hello\nworld', vault_password)
    assert vault_string != 'world'
    assert not(vault_string != 'hello')

    vault_string = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault_password)
    assert vault_string != 'world'
    assert not(vault_string != 'hello')

    vault_string = AnsibleVaultEncryptedUnicode.from_plaintext('world', vault_password)
    assert vault_string

# Generated at 2022-06-13 07:43:58.822965
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import crypt
    import os

    test_secret = os.urandom(16)

    # Test directly
    plaintext = 'test'
    ciphertext = crypt.encrypt(test_secret, plaintext)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = crypt.VaultLib(test_secret)
    assert avu == plaintext
    assert avu != 'foo'

    # Test with a variable and a vault
    vars = dict(
        plaintext=AnsibleVaultEncryptedUnicode(ciphertext),
        x='test',
    )
    vars['plaintext'].vault = crypt.VaultLib(test_secret)
    assert vars['plaintext'] == 'test'
    assert vars['plaintext'] != 'foo'



# Generated at 2022-06-13 07:44:05.840543
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.plugins.vault.VaultLib
    plaintext = u"test_text"
    secret = "test_secret"
    vault = ansible.plugins.vault.VaultLib.VaultLib([])
    vault.password = secret
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert(avu == plaintext)
    assert(not (avu != plaintext))



# Generated at 2022-06-13 07:44:12.801455
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing import vault

    plaintext = 'foo'
    vault = vault.VaultLib('pass')
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, 'pass')
    assert encrypted.is_encrypted()


# Generated at 2022-06-13 07:44:16.807987
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Check __ne__ returns False when other is equal
    avu = AnsibleVaultEncryptedUnicode('test')
    avu.vault = None
    assert avu != text_type('test')

    # Check __ne__ returns True otherwise
    assert avu != text_type('other')



# Generated at 2022-06-13 07:44:35.586892
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode.from_plaintext(u'A', None, None)
    b = 'A'
    assert(a.__ne__(b))
    b = u'A'
    assert(not a.__ne__(b))
    b = AnsibleVaultEncryptedUnicode.from_plaintext(u'A', None, None)
    assert(not a.__ne__(b))
    b = AnsibleVaultEncryptedUnicode.from_plaintext(u'B', None, None)
    assert(a.__ne__(b))


# Generated at 2022-06-13 07:44:46.058867
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible_collections.notstdlib.moveitallout.plugins.vault import VaultLib
    from ansible.parsing.vault import VaultLib as VaultLibOld

    vault = VaultLib()
    plaintext = "thisisplaintext"
    ciphertext = vault.encrypt(plaintext, 'password')

    # Test method is_encrypted with valid ciphertext
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert(avu.is_encrypted() == True)

    # Test method is_encrypted with invalid ciphertext
    ciphertext_invalid = vault.encrypt(plaintext, 'password')+"invalid"
    avu = AnsibleVaultEncryptedUnicode(ciphertext_invalid)
    avu.vault = vault


# Generated at 2022-06-13 07:44:47.781712
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    v = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    assert v != 'test'


# Generated at 2022-06-13 07:44:59.153644
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    def create_AVU(vault, value):
        avu = AnsibleVaultEncryptedUnicode('vault:!vault')
        avu.vault = vault
        avu._ciphertext = value
        return avu

    class Vault:
        def __init__(self, decrypted_value):
            self.decrypted_value = decrypted_value
            self.decrypt_called = 0

        def decrypt(self, value, secret):
            self.decrypt_called += 1
            return self.decrypted_value

        def is_encrypted(self, value):
            return True

    class DifferentVault:
        def __init__(self, decrypted_value):
            self.decrypted_value = decrypted_value
            self.decrypt_called = 0


# Generated at 2022-06-13 07:45:10.085236
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    def perform_test(v, s, e, expected_return):
        avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello', v, s)
        if e:
            assert avu.vault.encrypt(avu.data, s) != avu._ciphertext
        else:
            assert avu.vault.encrypt(avu.data, s) == avu._ciphertext
        assert avu.is_encrypted() == expected_return

    kdf = 'pbkdf2'
    cipher = 'AES256'
    for secret in ['password', 'secret']:
        for encrypt in [True, False]:
            # use the Vault object that is used in Ansible itself
            from ansible.parsing.vault import VaultSecret

# Generated at 2022-06-13 07:45:18.345055
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = 'mysecret'
    vault = vaultlib.VaultLib(secret)
    plaintext = 'mytext'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert(avu == plaintext)
    assert(avu.data == plaintext)
    assert(avu != 'wrong')
    assert(avu.data != 'wrong')


# Generated at 2022-06-13 07:45:27.543790
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Equals string
    avueu1 = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, 'secret')
    assert avueu1.__eq__('test')
    # Equals same AnsibleVaultEncryptedUnicode (same data)
    avueu2 = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, 'secret')
    assert avueu1.__eq__(avueu2)
    # Not equals different AnsibleVaultEncryptedUnicode (different data)
    avueu3 = AnsibleVaultEncryptedUnicode.from_plaintext('test1', None, 'secret')
    assert not avueu1.__eq__(avueu3)
    # Not equals if vault is not set
    avueu4 = Ansible

# Generated at 2022-06-13 07:45:37.229102
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib as VaultLibClass
    from ansible.parsing.vault import VaultSecret
    import os
    vault = VaultLibClass(filename='ansible-vault')
    vault_secret = VaultSecret(password='password')
    yaml_obj = AnsibleVaultEncryptedUnicode.from_plaintext('secret', vault, vault_secret)
    assert yaml_obj.is_encrypted()
    assert not yaml_obj.data == 'secret'
    yaml_obj1 = AnsibleVaultEncryptedUnicode(yaml_obj.data)
    assert yaml_obj1.is_encrypted()



# Generated at 2022-06-13 07:45:46.939814
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Load a test vault password file
    vault_pass_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

# Generated at 2022-06-13 07:45:56.158981
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # comparison with None
    # test with data == None
    avu = AnsibleVaultEncryptedUnicode(None)
    avu.vault = None
    msg = 'AVU with data == None %s None' % repr(avu)
    assert avu != None, msg

    # test with data != None
    avu = AnsibleVaultEncryptedUnicode('foo')
    avu.vault = None
    msg = 'AVU with data != None %s None' % repr(avu)
    assert avu != None, msg

    # comparison with other string types
    # test with data == None
    avu = AnsibleVaultEncryptedUnicode(None)
    avu.vault = None
    msg = 'AVU with data == None %s ""' % repr(avu)

# Generated at 2022-06-13 07:46:11.203520
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    import os
    from ansible.parsing.vault import VaultLib

    # First make sure vaulthash is set to valid value
    vault = VaultLib([('default', 'password')])
    vaulthash = vault.vault.encrypt('password')
    os.environ['ANSIBLE_VAULT_PASSWORD_FILE'] = os.path.join(os.path.dirname(__file__), 'files', 'vaultpassword')
    if not vault.vault.is_encrypted(vaulthash):
        raise AssertionError('Vault was not encrypted')

    # Now test that decrypted instance returns False
    avu = AnsibleVaultEncryptedUnicode('myplaintext')
    avu.vault = vault

# Generated at 2022-06-13 07:46:17.670631
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    This unit test validates that the __ne__ method checks the values
    of strings and not just their type.
    '''
    result = AnsibleVaultEncryptedUnicode("abc")
    assert result != "abc"
    assert not result != "abc"


# Generated at 2022-06-13 07:46:25.373482
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    val = AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          32323733303136386265346638666662376437326630346237346632323666363534613032633735\n          316230663435336637376566316163320a3361376538653736303362633337353764303335376662\n          62323661303166303130643463396166653831666639363865623931356366660a32366232356165\n          32393864333238616262626563343631323932336163656638353861')
    assert val != 'foo'



# Generated at 2022-06-13 07:46:30.972753
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 07:46:40.104240
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from crypt.vault import VaultLib

    plain_text = 'Secret string'
    vault_password = 'vaultpass'

    cipher_text = VaultLib(vault_password).encrypt(plain_text)
    encrypted_unicode = AnsibleVaultEncryptedUnicode(cipher_text)

    assert not encrypted_unicode.is_encrypted()

    encrypted_unicode.vault = VaultLib(vault_password)

    assert encrypted_unicode.is_encrypted()



# Generated at 2022-06-13 07:46:50.044057
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # Test a vaulted string

# Generated at 2022-06-13 07:47:01.973049
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    # Assert if the method returns false for None cases
    v = VaultLib([])
    av = AnsibleVaultEncryptedUnicode.from_plaintext('123', v, 'secret')
    assert not av.__eq__(None)

    # Assert if the method returns false for empty string cases
    v = VaultLib([])
    av = AnsibleVaultEncryptedUnicode.from_plaintext('', v, 'secret')
    assert not av.__eq__('')

    # Assert if the method returns true for valid case
    v = VaultLib([])
    av = AnsibleVaultEncryptedUnicode.from_plaintext('123', v, 'secret')
    assert av.__eq__('123')



# Generated at 2022-06-13 07:47:08.115659
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    result = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n1234567890123456789012345678901212345678901234567890123456789012\n1234567890123456789012345678901212345678901234567890123456789012\n12345678901234567890123456789012\n')
    result.vault = None
    assert result.__ne__('value') == True


# Generated at 2022-06-13 07:47:16.348550
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import ansible.parsing.vault
    import crypt
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w') as test_vault_file_one:
        test_vault_file_one.writelines([
            "---\n",
            "vault_password_file: %s\n" % test_vault_file_one.name
        ])
        test_vault_file_one.flush()
        vault_id_one = crypt.crypt('', s='a')
        vault_lib_one = ansible.parsing.vault.VaultLib(
            password_files=[test_vault_file_one.name]
        )

# Generated at 2022-06-13 07:47:26.537366
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import vault_identity_file
    import os
    class vault(object):
        def __init__(self):
            self.password = vault_identity_file.read_password_from_identity_file(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/files/test_vault.key')

        def decrypt(self, data, obj):
            return data

        def is_encrypted(self, data):
            return True

    u = AnsibleVaultEncryptedUnicode("somesecret")
    u.vault = vault()
    assert u.__eq__("somesecret")
    assert not u.__eq__("somesecrets")
    assert not u.__eq__("somesecretz")


# Generated at 2022-06-13 07:47:46.185486
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    method __ne__ of class AnsibleVaultEncryptedUnicode
    """
    avu = AnsibleVaultEncryptedUnicode('abc')
    assert avu != "abc"


# Generated at 2022-06-13 07:47:56.949378
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # first use case:  test if is_encrypted() can detect a normal string
    tester = AnsibleVaultEncryptedUnicode.from_plaintext('hello world', vault=None, secret=None)
    assert not tester.is_encrypted()

    # second use case:  test if is_encrypted() can detect an encrypted string
    with sys.modules['ansible.parsing.vault'].VaultLib.load('test') as vault:
        tester = AnsibleVaultEncryptedUnicode.from_plaintext('hello world', vault=vault, secret='test')
        assert tester.is_encrypted()

    # third use case:  test if is_encrypted() can detect a string that looks like it is encrypted

# Generated at 2022-06-13 07:48:04.969695
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    import ansible_vault

    vault = ansible_vault.VaultLib('mypass')

    # Test with a constant string as other
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'mypass')
    assert 'foo' == avu, '=== FAILED TO TEST ==='

    # Test with a non AnsibleVaultEncrypstring as other
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'mypass')
    assert 'foo' != avu, '=== FAILED TO TEST ==='

    # Test with a AnsibleVaultEncrypstring as other that decrypts to the same value
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'mypass')
   

# Generated at 2022-06-13 07:48:14.820940
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    testcases = {
        (None, False): False,
        (None, True): True,
        (b'foo', b'bar'): True,
        (b'foo', b'foo'): False,
        (b'foo', u'bar'): True,
        (b'foo', u'foo'): False,
        (u'foo', b'bar'): True,
        (u'foo', b'foo'): False,
        (u'foo', u'bar'): True,
        (u'foo', u'foo'): False,
        (u'foo', None): True
    }
    for (data, other), expected in testcases.items():
        obj = AnsibleVaultEncryptedUnicode(data)
        result = (obj != other)
        assert expected == result



# Generated at 2022-06-13 07:48:18.379092
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test a string which is not encrypted
    data = AnsibleVaultEncryptedUnicode("hello")
    assert ("hello" == data) == True
    assert ("hello" != data) == False



# Generated at 2022-06-13 07:48:30.157272
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    class TestVault(VaultLib):
        def __init__(self):
            self.secrets = {}

        def encrypt(self, plaintext, secret):
            self.secrets[plaintext] = secret
            return plaintext

        def decrypt(self, ciphertext, obj=None):
            k = obj.data
            return self.secrets[k]

    plaintext = 'foo'
    secret = 'bar'

    vault = TestVault()
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

    assert avu == plaintext
    assert not avu == 'foobar'
