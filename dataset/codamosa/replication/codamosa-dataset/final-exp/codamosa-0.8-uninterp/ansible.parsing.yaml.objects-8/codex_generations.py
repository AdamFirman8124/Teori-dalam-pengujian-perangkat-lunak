

# Generated at 2022-06-13 07:38:47.580940
# Unit test for method __radd__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___radd__():
    """
    Test __radd__ method of class AnsibleVaultEncryptedUnicode.
    """
    assert AnsibleVaultEncryptedUnicode(u"abc") + "X" == "Xabc"
    assert "X" + AnsibleVaultEncryptedUnicode(u"abc") == "Xabc"
    assert "X" + AnsibleUnicode(u"abc") == "Xabc"
    assert AnsibleUnicode(u"X") + "abc" == "Xabc"
    assert "X" + "abc" == "Xabc"

# Generated at 2022-06-13 07:38:53.536911
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():

    class MockVault(object):
        def encrypt(self, data, secret):
            return data

        def decrypt(self, data, secret=None, obj=None):
            return data

        def is_encrypted(self, data):
            return True

    mock_vault = MockVault()

    av1 = AnsibleVaultEncryptedUnicode('a')
    av1.vault = mock_vault

    av2 = AnsibleVaultEncryptedUnicode('b')
    av2.vault = mock_vault

    # Addition of encrypted elements
    av3 = av1 + av2
    assert(av3.is_encrypted())
    assert(av3.data == "ab")
    assert(av3.vault.is_encrypted(av3._ciphertext))

    # Addition of unencrypted string

# Generated at 2022-06-13 07:39:04.889725
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(length=None, salt=None, iterations=None)
    secret = 'ansible'
    seq = 'hello'
    ciphertext = vault.encrypt(seq, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    s = 'hello'
    assert (avu == s)
    assert (avu == seq)
    assert (avu == avu.data)

    seq = 'bye'
    ciphertext = vault.encrypt(seq, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert (avu != 'hello')



# Generated at 2022-06-13 07:39:15.047246
# Unit test for method replace of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_replace():
    avu = AnsibleVaultEncryptedUnicode('mypassword')
    assert(avu.replace('mypassword', 'nopassword') == 'nopassword')
    # currently only for other AnsibleVaultEncryptedUnicode
    assert(avu.replace(AnsibleVaultEncryptedUnicode('mypassword'), AnsibleVaultEncryptedUnicode('nopassword')) == 'nopassword')

# End of code from collections.UserString


# Generated at 2022-06-13 07:39:26.386289
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    from ansible.parsing.vault import VaultAES256
    plaintext = b'harry'
    password = b'barry'
    vault = VaultAES256(password)
    encrypted_text = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, password)
    assert encrypted_text + 'pumpkin' == 'pumpkin'
    assert hash(encrypted_text + 'pumpkin') == hash('pumpkin')
    plaintext = 'harry potter'
    password = 'barry'
    vault = VaultAES256(password)
    encrypted_text = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, password)
    assert encrypted_text + 'pumpkin' == 'harry potterpumpkin'

# Generated at 2022-06-13 07:39:30.712355
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'ansible'
    plaintext = 'secret'
    ciphertext = VaultLib(secret).encrypt(plaintext)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu.is_encrypted()

# Make the AnsibleVaultEncryptedUnicode class a YAML safe class
yaml.add_representer(AnsibleVaultEncryptedUnicode, yaml.representer.SafeRepresenter.represent_str)



# Generated at 2022-06-13 07:39:42.312724
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:39:47.183470
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avu = AnsibleVaultEncryptedUnicode('')
    assert(not avu.__le__('a'))
    avu = AnsibleVaultEncryptedUnicode('a')
    assert(avu.__le__('a'))
    assert(avu.__le__('b'))
    assert(not avu.__le__('A'))


# Generated at 2022-06-13 07:39:57.581565
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    # Normal case
    f = AnsibleVaultEncryptedUnicode(b'')
    assert 'a' not in f
    f.data = 'a'
    assert 'a' in f
    f.data = 'b'
    assert 'a' not in f

    # Special case: given parameter is a AnsibleVaultEncryptedUnicode - Impossible to satisfy due to the way vault works
    f = AnsibleVaultEncryptedUnicode(b'')
    g = AnsibleVaultEncryptedUnicode(b'')

    # Normal case
    g.data = 'a'
    assert g in f
    f.data = 'a'
    assert g in f
    f.data = 'b'
    assert g not in f



# Generated at 2022-06-13 07:40:05.564078
# Unit test for method __radd__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___radd__():
    from ansible.parsing.vault import VaultLib

    secrets = [
        'asdf',
        'A'*1024,
        'B'*1024*7,
        ]

    for secret in secrets:
        secret_bytes = to_bytes(secret)
        encryptor = VaultLib([])
        s = encryptor.encrypt(secret_bytes)
        avu = AnsibleVaultEncryptedUnicode(s)
        avu.vault = encryptor

        assert( (secret + avu).data == secret + secret )
        assert( (avu + secret).data == secret + secret )
        assert( (secret + avu).vault == encryptor )
        assert( (avu + secret).vault == encryptor )



# Generated at 2022-06-13 07:40:11.668455
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    data = 'secret'
    assert 'sec' not in AnsibleVaultEncryptedUnicode(data)



# Generated at 2022-06-13 07:40:23.444261
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    avu1 = AnsibleVaultEncryptedUnicode('A')
    assert avu1.find('A') == 0
    assert avu1.find('B') == -1

    avu2 = AnsibleVaultEncryptedUnicode('AB')
    assert avu2.find('A') == 0
    assert avu2.find('B') == 1
    assert avu2.find('A', 1) == -1
    assert avu2.find('C') == -1

    avu3 = AnsibleVaultEncryptedUnicode('ABC')
    assert avu3.find('A') == 0
    assert avu3.find('B') == 1
    assert avu3.find('C') == 2
    assert avu3.find('D') == -1

# Generated at 2022-06-13 07:40:31.949281
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Test __eq__ of class AnsibleVaultEncryptedUnicode
    """
    avu = AnsibleVaultEncryptedUnicode(to_bytes('foo'))
    avu._ciphertext = to_bytes('bar')

    # Test case 1:
    #   Method __eq__ called without having set attribute 'vault'
    assert not avu.__eq__('foo')

    # Test case 2:
    #   Method __eq__ called with attribute 'vault' set to None
    avu.vault = None
    assert not avu.__eq__('foo')

    # Test case 3:
    #   Method __eq__ called with __UNSAFE__ attribute set to True
    avu.__UNSAFE__ = True
    assert not avu.__eq__('foo')

    # Test case

# Generated at 2022-06-13 07:40:42.366266
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    from ansible import constants as C
    from ansible.vault import VaultLib

    vault = VaultLib(C.DEFAULT_VAULT_SECRET_FILE)
    vaulttext = AnsibleVaultEncryptedUnicode.from_plaintext('123456789', vault, b'1234')

    assert vaulttext.rfind('123') == 0
    assert vaulttext.rfind('345') == 2
    assert vaulttext.rfind('789') == 6
    assert vaulttext.rfind('0') == -1
    assert vaulttext.rfind('123', 0, 1) == 0
    assert vaulttext.rfind('123', 0, 2) == 0
    assert vaulttext.rfind('123', 0, 3) == 0
    assert vaulttext.rfind('123', 0, 4) == 0
    assert vaulttext.r

# Generated at 2022-06-13 07:40:48.349569
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    v = AnsibleVaultEncryptedUnicode("a")
    assert v.find("a") == 0
    assert v.find("A") == -1
    v = AnsibleVaultEncryptedUnicode("A")
    assert v.find("a") == -1
    assert v.find("A") == 0

    sub = AnsibleVaultEncryptedUnicode("a")
    assert v.find(sub) == -1
    sub = AnsibleVaultEncryptedUnicode("A")
    assert v.find(sub) == 0

    assert v.find("a") == -1
    assert v.find("A") == 0


# Generated at 2022-06-13 07:40:58.341156
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    plaintext = 'this is a test string'
    test = AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          65343130333165633033363065376665636466303738653736356537333434366161336533613839\n          66346539663534366233323832636539383431393530363533346639383033356231316561303233\n          323935666565396130656230666233613465336264343635613236653066376465\n          \n          this is a test string')

    assert(test.find(text_type('test')) == 9)

# Generated at 2022-06-13 07:41:09.769040
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:41:21.524488
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Following statements will not raise an exception
    # as the __eq__ method is implemented correctly
    assert AnsibleVaultEncryptedUnicode.from_plaintext('1', vault=None, secret='foo') == '1'
    assert AnsibleVaultEncryptedUnicode.from_plaintext('1', vault=None, secret='foo') != '2'
    assert AnsibleVaultEncryptedUnicode.from_plaintext('1', vault=None, secret='foo') != '1'
    # Assertion failed: __eq__ expects False
    assert AnsibleVaultEncryptedUnicode.from_plaintext('1', vault=None, secret='foo') == AnsibleVaultEncryptedUnicode.from_plaintext('1', vault=None, secret='foo')


# Generated at 2022-06-13 07:41:30.856773
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    target_str = AnsibleVaultEncryptedUnicode(u"a very quitent man")
    sub_str1 = AnsibleVaultEncryptedUnicode(u"qu")
    sub_str2 = AnsibleVaultEncryptedUnicode(u"Q")
    sub_str3 = AnsibleVaultEncryptedUnicode(u"quiet")
    sub_str4 = AnsibleVaultEncryptedUnicode(u"q")
    assert 6 == target_str.find(sub_str1)
    assert 6 == target_str.find(sub_str1, start=4)
    assert 6 == target_str.find(sub_str1, start=4, end=8)
    assert -1 == target_str.find(sub_str2)

# Generated at 2022-06-13 07:41:40.166368
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultAES256CMAC
    from ansible.parsing.vault import to_unicode
    from ansible.parsing.vault import to_bytes
    secret = to_bytes("My Secret Password")
    avlt = VaultLib([VaultAES256(secret), VaultAES256CMAC(secret)], to_unicode, to_bytes)

# Generated at 2022-06-13 07:41:55.939166
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(password=u'password')
    ciphertext = vault.encrypt(u'foobar')
    assert AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('foobar').is_encrypted()

## add resolver support functions


# Generated at 2022-06-13 07:42:05.216133
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    for PY_MAJOR in [2, 3]:
        # In Python 3 we need bytes with the b'' prefix
        if PY_MAJOR == 3:
            pass_correct_data = b"something"
            pass_wrong_data = "something"
        else:
            pass_correct_data = "something"
            # In Python 2, it crashes by trying to decode the string as unicode
            pass_wrong_data = u"something"

        test_obj = AnsibleVaultEncryptedUnicode(pass_correct_data)
        assert test_obj.__ne__(pass_correct_data) is True
        assert test_obj.__ne__(pass_wrong_data) is True

        # Setting the vault attribute, enables the __ne__ functionality
        test_obj.vault = True

# Generated at 2022-06-13 07:42:09.342611
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avue = AnsibleVaultEncryptedUnicode('test')
    assert avue.__ne__('test') is not False
    assert avue.__ne__('other') is not True
    with pytest.raises(AttributeError):
        avue.__ne__(None)



# Generated at 2022-06-13 07:42:16.027953
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib()
    secret = 'test'

    s = AnsibleVaultEncryptedUnicode.from_plaintext("foo", vault, secret)
    assert s == s

    t = AnsibleVaultEncryptedUnicode.from_plaintext("foo", vault, secret)
    assert s == t

    u = AnsibleVaultEncryptedUnicode.from_plaintext("bar", vault, secret)
    assert s != u

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode___eq__()

# Generated at 2022-06-13 07:42:23.536674
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def avu_eq(avu, other):
        return (avu == other)

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello', None, None)
    avu.vault = None
    assert avu_eq(avu, 'hello') == False

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello', None, None)
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')
    avu.vault = vault
    assert avu_eq(avu, 'hello') == True


# Generated at 2022-06-13 07:42:38.753671
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import unittest

    class MyTestCase(unittest.TestCase):
        def test___ne__(self):
            avueu = AnsibleVaultEncryptedUnicode(b"c3VwZXJzZWNyZXRzZWNyZXQ")
            self.assertNotEqual(avueu, "supersecretsecret")

    tests = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    results = unittest.TextTestRunner().run(tests)
    if not results.wasSuccessful():
        print("\nFailed:")
        for failure in results.failures:
            print(failure[1])
        _sys.exit(1)

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode___ne__

# Generated at 2022-06-13 07:42:44.641381
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode('any_string')
    assert a != 'any_string'

    a = AnsibleVaultEncryptedUnicode('any_string')
    assert a != AnsibleVaultEncryptedUnicode('any_string')

    a = AnsibleVaultEncryptedUnicode('any_string')
    assert a != None

    a = AnsibleVaultEncryptedUnicode(None)
    assert a != None

    a = AnsibleVaultEncryptedUnicode(None)
    assert a != 'any_string'

    a = AnsibleVaultEncryptedUnicode('any_string')
    assert a != AnsibleVaultEncryptedUnicode(None)


# Generated at 2022-06-13 07:42:54.917540
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:43:06.859750
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib
    # Password: 'secret'
    vault_content = u'$ANSIBLE_VAULT;1.1;AES256\n37333136623933356665393463396365316532386536633162326639626262363663323066653834\n38306632653939376136343036663533333236393931346235653763386161323133653436346135\n363063623237623865663638353734303734\n'
    avu = AnsibleVaultEncryptedUnicode(vault_content)
    assert avu.is_encrypted()
    avu.vault = VaultLib('secret')
    assert avu.data == u'my passphrase'
    assert avu == u

# Generated at 2022-06-13 07:43:17.495372
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import unittest
    import sys
    import ansible.parsing.vault as vault


# Generated at 2022-06-13 07:43:32.278612
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Assert strings are equal
    avu1 = AnsibleVaultEncryptedUnicode('foo')
    avu2 = AnsibleVaultEncryptedUnicode('foo')
    assert avu1 == avu2
    assert avu2 == avu1

    # Assert strings are not equal
    avu1 = AnsibleVaultEncryptedUnicode('foo')
    avu2 = AnsibleVaultEncryptedUnicode('bar')
    assert avu1 != avu2
    assert avu2 != avu1
    assert 'foo' != avu2
    assert avu2 != 'foo'

    # Assert strings are not equal
    avu1 = AnsibleVaultEncryptedUnicode('foo')
    avu2 = AnsibleVaultEncryptedUnicode('bar')
    assert avu1

# Generated at 2022-06-13 07:43:35.096488
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # fail if not overloaded
    avueu = AnsibleVaultEncryptedUnicode('')
    assert avueu.__ne__('')



# Generated at 2022-06-13 07:43:37.494243
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avue = AnsibleVaultEncryptedUnicode("")
    assert (avue != "")
    assert (avue != "a")
    assert (avue != avue)

# Generated at 2022-06-13 07:43:41.626287
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = AnsibleVaultEncryptedUnicode('123')
    vault.vault = 'foo'
    assert vault == '123'
    assert not (vault != '123')
    assert vault != '1234'
    assert not (vault == '1234')
    assert not (vault == object())
    assert vault != object()



# Generated at 2022-06-13 07:43:48.107979
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    if 'yaml' not in sys.modules:
        raise SkipTest("yaml not installed")
    if 'vault' not in sys.modules:
        raise SkipTest("vault not installed")
    if 'binascii' not in sys.modules:
        raise SkipTest("binascii not installed")

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault = VaultLib([ ],'!', 'secret')
    t1 = "test"
    t2 = b"test"
    sec1 = "secret"
    sec2 = b"secret"

    # Test with a valid vault object and type str as secret
    aveu

# Generated at 2022-06-13 07:43:57.999215
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test when both arugments are regular strings

    # the first argument is a normal string
    avu1 = AnsibleVaultEncryptedUnicode('test')
    assert(avu1.__ne__('test') == True)

    # the first argument is a unicode string
    avu2 = AnsibleVaultEncryptedUnicode(u'test')
    assert(avu2.__ne__('test') == True)

    # Test when one argument is a AnsibleVaultEncryptedUnicode and the other
    # is a string

    # the first argument is a AnsibleVaultEncryptedUnicode, the second
    # argument is a normal string
    avu3 = AnsibleVaultEncryptedUnicode('test')
    assert(avu3.__ne__('test') == True)

    # the first

# Generated at 2022-06-13 07:43:58.852939
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:44:06.661548
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible
    if not ansible.__version__.startswith('2.7'):
        raise Exception("Function is_encrypted only valid for Ansible 2.7")

    import ansible.parsing.vault as vault
    import ansible.parsing.vaultlib as vaultlib

    iv = "\xce\x24\x7f\x27\xc1\x07\xea\x7d\x49\x17\xf8\x2a\xba\x42\x45\x1f"
    key = "\x9f\x15\x1b\x1b\x4b\x16\x4b\x05\xfc\x9c\x1f\x47\xe3\xfe\x2c\x3a"


# Generated at 2022-06-13 07:44:16.447139
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault = VaultLib(['--vault-password-file=%s' % 'tests/test_vault.py'])
    my_string = 'foo'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(my_string, vault, 'test',)
    my_string2 = 'bar'
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(my_string2, vault, 'test')

    # __ne__ should succeed unless the vault hasn't been decrypted
    assert avu != my_string
    assert avu != avu2
    assert avu.data != my_string



# Generated at 2022-06-13 07:44:17.926860
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    u = AnsibleVaultEncryptedUnicode("test")
    assert not (u != "test")


# Generated at 2022-06-13 07:44:27.272937
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    ciphertext = b'\x00\x01\x00\x00\x00\x00\x00\x00'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vaultlib.VaultLib('test')
    assert avu == 'hello'
    assert avu == AnsibleVaultEncryptedUnicode.from_plaintext('hello', vaultlib.VaultLib('test'), 'test')
    assert not avu == 'bye'
    assert not avu == AnsibleVaultEncryptedUnicode.from_plaintext('hi', vaultlib.VaultLib('test'), 'test')
    assert not avu == 'hi'

# Generated at 2022-06-13 07:44:38.307386
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    v = vault.VaultLib('secret')
    plaintext = 'i40B6UdN6xLLo6Zn'
    avue = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, v, 'secret')
    assert avue.is_encrypted() is True
    assert avue.data == plaintext

    plaintext = 'i40B6UdN6xLLo6Zn.yml'
    avue = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, v, 'secret')
    assert avue.is_encrypted() is True
    assert avue.data == plaintext

    plaintext = 'YmFyLnR4dA==\n'

# Generated at 2022-06-13 07:44:44.806919
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import sys
    sys.path.append('/home/user/anaconda2/bin/python2')
    import yaml
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(password='test')

    # test the is_encrypted method.
    #
    # test if the object is encrypted or not.
    #
    # 1. if the object is an encrypted string, then the method is_encrypted()
    #    should return True.
    #
    # 2. if the object is an non-encrypted string, then the method is_encrypted()
    #    should return False.
    #
    # 3. if the object is not a string, then the method is_encrypted()
    #    should raise an exception.
    #

    # test case 1:
    #   test if the object is an encrypted

# Generated at 2022-06-13 07:44:49.890401
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create object of class AnsibleVaultEncryptedUnicode
    avu = AnsibleVaultEncryptedUnicode("aGVsbG8=")

    assert avu.__eq__("hello") == True
    assert avu.__eq__("world") == False
    assert avu.__eq__(u"hello") == True
    assert avu.__eq__(u"world") == False


# Generated at 2022-06-13 07:44:54.840379
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    ciphertext = VaultLib().encrypt('foo')
    # By default the vaultlib returns a byte string
    isinstance(ciphertext, to_text('').__class__)
    avu_1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu_1.vault = VaultLib()
    avu_2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu_2.vault = VaultLib()
    # the strings are equal
    assert avu_1 == 'foo'

    assert avu_1 == avu_2



# Generated at 2022-06-13 07:45:02.085809
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnicode
    s = "\x00\x01\x02\x03\x04\x05\x06\x07"
    m = VaultLib("test")
    m.key = "AES256"
    m.password = "test"
    m.update_payload = True
    e = AnsibleVaultEncryptedUnicode.from_plaintext(s, m, "password")
    assert s != e


# Generated at 2022-06-13 07:45:11.904835
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault_password = 'abc123'
    vault = VaultLib(vault_password)
    secret = 'secret'
    plaintext = 'secret'

# Generated at 2022-06-13 07:45:24.134613
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import UnsafeText
    import os
    import getpass

    plaintext = "foo bar"
    vault_password_file = os.path.join(os.path.dirname(__file__), "vault.txt")
    pw = getpass.getpass(prompt="Password: ")
    vault = VaultLib(pw)
    avu_plain = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, vault_password_file)
    assert not avu_plain.is_encrypted()

    ciphertext = vault.encrypt(plaintext, vault_password_file)
    avu_cipher = AnsibleVaultEncryptedUnicode(ciphertext)
    avu_

# Generated at 2022-06-13 07:45:26.370016
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    av = AnsibleVaultEncryptedUnicode("foo")
    assert av != "foo"


# Generated at 2022-06-13 07:45:37.547004
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    avu1 = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n63323239343066306262386439633763363736396465623361373265633963616532363962353265\n39376163653334653664353839643764613363366534643631616639316661646432313438393738\n3363623535\n")
    assert avu1.is_encrypted()

    ansible_vault = VaultLib([])
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext("foo", ansible_vault, "bar")
    assert avu2.is_encrypted()

    avu3

# Generated at 2022-06-13 07:45:51.465180
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    secret = 'ansible'
    string1 = "test"
    string2 = "test2"
    assert AnsibleVaultEncryptedUnicode.from_plaintext(string1, vault, secret) != string2
    assert string1 != AnsibleVaultEncryptedUnicode.from_plaintext(string2, vault, secret)


# register the base classes so they are subbed instead of the python counterparts

# Generated at 2022-06-13 07:45:56.099419
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault
    ciphertext = "fdsgdfgdfgfdsgsdgsdfgsdgsdfgsdgsdfgsdgsdfgsdgsdfgsdgsdfgsdfgsdgsdfgsdfgsdfgsdfgsdgsdfgsdfgsdgsdfgsdgsdfgsdfgsdg"
    secret = "secret"
    vault_obj = vault.VaultLib(secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault_obj
    assert (avu == "abc") == False
    assert (avu != "abc") == True


# Generated at 2022-06-13 07:46:01.271521
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    data_source = 'test'
    line_number = 0
    column_number = 0
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext='test')
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext='test')
    avu1.ansible_pos = (data_source, line_number, column_number)
    avu2.ansible_pos = (data_source, line_number, column_number)
    assert not avu1.__ne__(avu2),'ne test failed'


# Generated at 2022-06-13 07:46:08.615157
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    class UnitTestDummyVault:
        def is_encrypted(self, s):
            return "encrypted" in s

    v = UnitTestDummyVault()
    avue = AnsibleVaultEncryptedUnicode.from_plaintext("test", v, "secret")

    # avue.data has not been changed; this is the original value
    assert not avue.is_encrypted()

    # Explicitly set the data to a random value. is_encrypted
    # should return True because of the is_encrypted method
    # of the vault class

# Generated at 2022-06-13 07:46:17.525955
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import sys
    import vault

    vault_obj = vault.VaultLib('test')
    if sys.version_info[0] < 3:
        non_vault_str = u'foo'
    else:
        non_vault_str = 'foo'

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'foo', vault_obj, 'test_password')

    assert avu != non_vault_str

# Generated at 2022-06-13 07:46:25.541089
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(password=b'testing')

    def _test_vault_encrypted(ciphertext, expected):
        plaintext = vault.decrypt(ciphertext)
        evu = AnsibleVaultEncryptedUnicode(ciphertext)
        evu.vault = vault

        actual = evu.is_encrypted()
        if expected != actual:
            print('Test failed. ciphertext: "%s" expected: %s actual: %s' % (plaintext, expected, actual))
            print('plaintext: %s' % plaintext)
            raise Exception('Unit test failed')


# Generated at 2022-06-13 07:46:31.149179
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:46:45.317895
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY3

    import os
    import tempfile
    pas = os.urandom(16)

    def _test_is_encrypted(value, should_be_encrypted):
        # test with a string
        avu = AnsibleVaultEncryptedUnicode.from_plaintext(value, v, pas)
        assert(avu.is_encrypted() == should_be_encrypted)

        # test with a file
        tmpfile = tempfile.NamedTemporaryFile()
        with open(tmpfile.name, 'w') as fp:
            fp.write(to_text(value))
        avu = AnsibleVaultEncryptedUnicode.from_plaintext(tmpfile.name, v, pas)


# Generated at 2022-06-13 07:46:52.474896
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib

    # Data
    secret = b'secret'
    plaintext = b'plaintext'
    encoded_plaintext = b'ENC[%s]' % vault.b64encode(plaintext)
    encoded_secret = b'ENC[%s]' % vault.b64encode(secret)

    # Tests
    assert AnsibleVaultEncryptedUnicode(plaintext).is_encrypted() == False
    assert AnsibleVaultEncryptedUnicode(encoded_plaintext).is_encrypted() == True
    assert AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, VaultLib('1.1'), secret).is_encrypted() == True

    # Data
    secret = b'\x00' * 32

# Generated at 2022-06-13 07:47:03.666761
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # fake_raw_data is the output of ansible-vault encrypt_string --name 'test_str' 'foobar'

# Generated at 2022-06-13 07:47:24.407742
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    secret = "SECRET"
    plaintext = "foo"

    vault = VaultLib([])
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    assert plaintext == avu
    assert avu == plaintext


# Generated at 2022-06-13 07:47:29.261342
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert(AnsibleVaultEncryptedUnicode("") ==
           AnsibleVaultEncryptedUnicode(""))
    assert(AnsibleVaultEncryptedUnicode("") !=
           AnsibleVaultEncryptedUnicode("something"))
    assert(AnsibleVaultEncryptedUnicode("something") !=
           AnsibleVaultEncryptedUnicode(""))
    assert(AnsibleVaultEncryptedUnicode("something") ==
           AnsibleVaultEncryptedUnicode("something"))
    assert(AnsibleVaultEncryptedUnicode("something") ==
           "something")


# Generated at 2022-06-13 07:47:40.225072
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    data = 'my secret'
    avu = AnsibleVaultEncryptedUnicode(data)
    assert avu != data

# Now add the custom types to yaml, so that we get the
# custom classes and not the defaults.
#
# Also set the loader version to 1.1 to support the new
# '.fail' method on strings.
yaml.add_representer(AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedUnicode.yaml_representer)
yaml.add_constructor(AnsibleVaultEncryptedUnicode.yaml_tag, AnsibleVaultEncryptedUnicode.yaml_constructor)
yaml.add_representer(AnsibleMapping, yaml.dumper.SafeRepresenter.represent_dict)


# Generated at 2022-06-13 07:47:46.968751
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n33323731646262623563313961323761653437326233376263373035653863303461333465\n39303666623138633461327a;aa\n')
    avu.vault = dict()
    assert avu == 'aa'
    assert avu != 'ab'

# Generated at 2022-06-13 07:47:57.720001
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:47:58.751011
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:48:06.144502
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:48:11.859782
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    u_str = 'This is a test'
    s_str = b'This is a test'
    non_encrypted_text = AnsibleVaultEncryptedUnicode(s_str)
    assert not non_encrypted_text.is_encrypted()
    assert AnsibleVaultEncryptedUnicode(u_str) != non_encrypted_text
    assert AnsibleVaultEncryptedUnicode(u_str) == non_encrypted_text.data

# Generated at 2022-06-13 07:48:15.760361
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    assert AnsibleVaultEncryptedUnicode(u"$ANSIBLE_ VAULT;1.1;AES256\n\nblah").is_encrypted()
    assert not AnsibleVaultEncryptedUnicode(u"\n\nblah").is_encrypted()



# Generated at 2022-06-13 07:48:28.757897
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class DummyVault:
        """This stub class is required to pass the test"""
        class Error:
            pass

        class AnsibleVaultError(Error):
            """This stub class is required to pass the test"""
            def __init__(self, msg):
                self.msg = msg

        def __init__(self, password=''):
            self.password = password
            self.vault_version = '1.0'

        def encrypt(self, plaintext, password):
            return to_text(plaintext)

        def decrypt(self, ciphertext, password):
            return to_text(ciphertext)

        def is_encrypted(self, ciphertext):
            return bool(ciphertext)

    #data is not empty string
    non_empty_string = "abcd"
    encrypted_string = AnsibleV