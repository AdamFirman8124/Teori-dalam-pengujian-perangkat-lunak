

# Generated at 2022-06-13 07:38:58.917956
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.loader import AnsibleLoader

    s1 = AnsibleVaultEncryptedUnicode('secret')
    s2 = AnsibleVaultEncryptedUnicode('secret')
    assert (s1 > s2) == False
    assert (s2 > s1) == False
    assert (s1 == s2) == True
    assert (s1 != s2) == False

    s3 = AnsibleVaultEncryptedUnicode('another secret')
    assert (s3 > s1) == True
    assert (s1 < s3) == True

    plain = "Unencrypted"
    un = AnsibleVaultEncryptedUnicode(plain)

# Generated at 2022-06-13 07:39:10.065930
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():

    # Test if class doesn't implement the method (always return false)
    org_avu = AnsibleVaultEncryptedUnicode('foo')
    assert org_avu != 'foo'
    assert org_avu != 'bar'

    # Test if class with vault
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 07:39:23.737577
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    s = AnsibleVaultEncryptedUnicode('abcde')
    assert s[0:] == 'abcde'
    assert s[1:] == 'bcde'
    assert s[2:4] == 'cd'
    assert s[0:0] == ''
    assert s[0:-1] == 'abcd'
    assert s[2:-2] == 'c'
    assert s[-100:100] == 'abcde'
    assert s[-100:2] == 'ab'
    assert s[5:100] == ''
    assert s[-5:] == 'abcde'
    assert s[:-5] == ''
    assert s[2:2] == ''
    assert s[1:-4] == 'b'
    assert s[4:-4] == ''

# Generated at 2022-06-13 07:39:28.829053
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    my_vault = VaultLib([])
    my_vault.secret = "testing-secret"

    example_text = "test text"
    test_obj = AnsibleVaultEncryptedUnicode(example_text)
    assert not test_obj.is_encrypted()

    test_obj.data = my_vault.encrypt(example_text, my_vault.secret)
    assert test_obj.is_encrypted()

    test_obj.vault = my_vault
    assert test_obj.is_encrypted()


# Generated at 2022-06-13 07:39:31.536317
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    v = VaultLib('secret')
    val1 = AnsibleVaultEncryptedUnicode.from_plaintext('test', v, 'secret')
    val2 = AnsibleVaultEncryptedUnicode('test')
    assert val1 != val2


# Generated at 2022-06-13 07:39:35.162764
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''
    Test for method __eq__ of class AnsibleVaultEncryptedUnicode
    '''
    assert AnsibleVaultEncryptedUnicode('1234') == '1234'


# Generated at 2022-06-13 07:39:45.175430
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from textwrap import dedent

    vault = VaultLib('testpassword')
    for varname, comment in [
        ('ciphertext', 'string not encrypted'),
        ('AnsibleVaultEncryptedUnicode(vault.encrypt("ciphertext"))', 'AnsibleVaultEncryptedUnicode object'),
        ('AnsibleVaultEncryptedUnicode(vault.encrypt("ciphertext"))', 'AnsibleVaultEncryptedUnicode object'),
        ('AnsibleVaultEncryptedUnicode(vault.encrypt("ciphertext"))', 'AnsibleVaultEncryptedUnicode object'),
    ]:
        data = dedent("""
        # %s
        %s
        """ % (comment, varname))


# Generated at 2022-06-13 07:39:46.109387
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    '''pass'''
    return



# Generated at 2022-06-13 07:39:52.163585
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    s = to_bytes('abc')
    s_enc = AnsibleVaultEncryptedUnicode(s)
    t = to_bytes('def')
    t_enc = AnsibleVaultEncryptedUnicode(t)

    assert (s > t)
    assert (s_enc > t)
    assert (s > t_enc)

    # Vault data should not be compared as plaintext, but is
    assert (s_enc > t_enc)



# Generated at 2022-06-13 07:40:02.869557
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Test method __eq__ of AnsibleVaultEncryptedUnicode class

    When
      - class AnsibleVaultEncryptedUnicode is instantiated with a valid encoded string
      - the instantiated AnsibleVaultEncryptedUnicode is compared to another string (valid or not)

    Then
      - when the strings are equal, __eq__ returns True
      - otherwise, __ne__ returns False
    """

    # class AnsibleVaultEncryptedUnicode is instantiated with a valid encoded string
    # value = "test"
    # key = b"key"
    # avue = AnsibleVaultEncryptedUnicode.from_plaintext(value, vault, key)
    # avue.vault = vault

    # Not testing the vault encryption, using an encoded string

    # instantiated AnsibleVaultEncryptedUn

# Generated at 2022-06-13 07:40:16.583864
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:27.626578
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    import unittest
    import random
    import megacli

    vault = megacli.VaultLib()
    a = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    b = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    c = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    d = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    e = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    f = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'password')
    g = AnsibleVaultEncrypted

# Generated at 2022-06-13 07:40:39.236747
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib, VaultSecret
    vault = VaultLib()
    secret = VaultSecret('mypassword')

    class AnsibleVaultEncryptedUnicode2(AnsibleVaultEncryptedUnicode):
        '''Unicode like object that is not evaluated (decrypted) until it needs to be'''
        def is_encrypted(self):
            return self.data

    assert not AnsibleVaultEncryptedUnicode2.from_plaintext('foo', vault, secret).is_encrypted()
    assert AnsibleVaultEncryptedUnicode2.from_plaintext('foo|bar', vault, secret).is_encrypted()

# this referrers to which class to use when importing YAML
# into Python.

# Generated at 2022-06-13 07:40:47.609700
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    import vaultlib
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n35376538373436303533616139636633313230613561623235393631633462383966316266363939\n36316231323938333961393034626433353631623562633934663339646636653935373864363934\n346564336562643835656130610a6337376638346435303739663764643561333338636532313535\n32393639643465313331656332346232343235356661613165363430336463353539326438363562\n6334623239663336\n')


# Generated at 2022-06-13 07:40:52.774778
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:41:00.357111
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    # test if we can create an AnsibleVaultEncryptedUnicode with a valid vault
    valid_vault = VaultLib(None)

# Generated at 2022-06-13 07:41:02.724467
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    # ToDo:
    # implement method __gt__ of class AnsibleVaultEncryptedUnicode
    pass



# Generated at 2022-06-13 07:41:15.042481
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(['password'])

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext("hi", vault, 'password')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext("hi", vault, 'password')
    assert (avu1 == avu2)

    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext("there", vault, 'password')
    assert (avu1 != avu3)

    avu4 = AnsibleVaultEncryptedUnicode.from_plaintext("hi", vault, 'wrong_password')
    assert (avu1 != avu4)



# Generated at 2022-06-13 07:41:23.100249
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import unittest
    import crypt
    import getpass
    a = AnsibleVaultEncryptedUnicode("test")
    b = AnsibleVaultEncryptedUnicode("test")
    c = AnsibleVaultEncryptedUnicode("test2")
    d = "test"
    e = "test2"
    vault = crypt.AES256Cipher(
        getpass.getpass("Vault Password: "))
    a.vault = vault
    b.vault = vault
    c.vault = vault
    assert (a != b) == False
    assert (a != c) == True
    assert (c != d) == True
    assert (d != e) == True


# Generated at 2022-06-13 07:41:28.588759
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode._from_string(u'secret')
    assert avu == u'secret'

    try:
        avu == u'error'
    except AssertionError as e:
        assert 'ansible_pos can only be set with a tuple/list of three values' in str(e)
    else:
        assert False, 'An exception should have been raised.'  # pragma: no cover



# Generated at 2022-06-13 07:41:40.956354
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode('XX') == 'XX'
    assert AnsibleVaultEncryptedUnicode('XX') != 'XX '
    assert AnsibleVaultEncryptedUnicode('XX') != 'X'
    assert AnsibleVaultEncryptedUnicode('XX') != 'xxx'
    assert AnsibleVaultEncryptedUnicode('XX') != 'x'
    assert AnsibleVaultEncryptedUnicode('XX') != ''
    assert AnsibleVaultEncryptedUnicode('XX') != 123
    assert AnsibleVaultEncryptedUnicode('XX') != [1,2,3]
    assert AnsibleVaultEncryptedUnicode('XX') != None
    assert AnsibleVaultEncryptedUnicode('XX') != AnsibleVaultEncryptedUnicode('XX ')
   

# Generated at 2022-06-13 07:41:48.530031
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    try:
        vault = ansible.parsing.vault.VaultLib(password='secret')
    except Exception:
        # If an exception occurred, Vault is probably not installed
        return
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'secret')
    assert avu.is_encrypted()
    avu.data = 'foo'
    assert not avu.is_encrypted()


# Generated at 2022-06-13 07:41:56.596338
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    if not sys.version_info[0] == 2:
        pytest.skip("Not running on Python 2.x")

    from ansible.parsing.vault import VaultLib
    avu = AnsibleVaultEncryptedUnicode()
    avu._ciphertext = "!vault | $ANSIBLE_VAULT;1.1;AES256\n33653531376436333665356130303133303730353632626261623733663436613766346663356362386\n33432393237323861343134613163313439663731396164303731363236383635366234633363623235\n326633303534326333633738636436366338313462633062"

# Generated at 2022-06-13 07:41:59.249268
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    vault = VaultLib([])
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'secret')

    assert(avu != 'foo')
    assert(avu != AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'secret'))


# Generated at 2022-06-13 07:42:04.218325
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault = VaultLib('password')
    #
    # encrypted unicode:
    #
    aveu = AnsibleVaultEncryptedUnicode.from_plaintext('before', vault, 'password')
    aveu2 = AnsibleVaultEncryptedUnicode.from_plaintext('before', vault, 'password')
    assert aveu.data == aveu2.data
    assert aveu.data == 'before'
    assert aveu == 'before'
    assert aveu == aveu2
    #
    # unicode:
    #

# Generated at 2022-06-13 07:42:14.316438
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.utils.vault import VaultLib
    vault = VaultLib('test')
    with open('test_is_encrypted.yml', 'w') as f:
        f.write('---\n- a: !vault |\n      $ANSIBLE_VAULT;1.1;AES256\n      61623138343637373633323061393734363734383035653139383036326234353766336562366365\n      343937343035646363666626533373366363530613030656638353362386262633862380a')
    with open('test_is_encrypted.yml', 'r') as f:
        data = yaml.load(f)
    assert(data[0]['a'].is_encrypted())

# Generated at 2022-06-13 07:42:19.575027
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class FakeVault(object):
        @staticmethod
        def encrypt(seq, secret):
            return u"encrypted"

        @staticmethod
        def decrypt(ciphertext, obj):
            if obj:
                return u"decrypted"
            else:
                raise Exception("No obj provided")

        @staticmethod
        def is_encrypted(ciphertext):
            return True

    avu_one = AnsibleVaultEncryptedUnicode("ciphertext")
    avu_one.vault = FakeVault()
    avu_two = AnsibleVaultEncryptedUnicode("ciphertext")
    avu_two.vault = FakeVault()

    sys.stdout.write("Testing AnsibleVaultEncryptedUnicode.__ne__")
    assert avu_one != "foo"

# Generated at 2022-06-13 07:42:26.566930
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Setup the class
    avu = AnsibleVaultEncryptedUnicode("test_cipher_text")
    avu.vault = vaultlib.VaultLib("test_password")

    # Test the method
    assert avu.__eq__("test_plain_text") == "test_plain_text" == avu.data



# Generated at 2022-06-13 07:42:39.432543
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class MockVault:
        def __init__(self, passwd):
            self.passwd = passwd
            self.cipher = None
            self.version = 1

        def encrypt(self, s, pwd=None):
            return 1

        def decrypt(self, s, pwd=None):
            return s

        def is_encrypted(self, s):
            return False

    pwd = MockVault('foo')
    s1 = AnsibleVaultEncryptedUnicode.from_plaintext('bar', pwd, 'foo')
    s2 = AnsibleVaultEncryptedUnicode.from_plaintext('baz', pwd, 'foo')
    assert s1 != s2


# Generated at 2022-06-13 07:42:47.800813
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault_password = b'vault_password'
    vault = VaultLib(vault_password)
    obj = AnsibleVaultEncryptedUnicode.from_plaintext(u'foobar', vault, vault_password)
    #test_obj = AnsibleVaultEncryptedUnicode.from_plaintext(u'foobar', vault, vault_password)
    test_obj = AnsibleVaultEncryptedUnicode.from_plaintext(u'foobar', vault, b'invalid_vault_password')
    assert obj != test_obj


# Generated at 2022-06-13 07:43:06.786403
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    Unit test method __ne__ of AnsibleVaultEncryptedUnicode class.

    The test is done by comparing the result of not equal operator with
    the expected result. We use a not encrypted text with a encrypted
    text for the testing.
    '''
    import ansible.parsing.vault as vault

    secret = 'mysecret'

# Generated at 2022-06-13 07:43:17.460663
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test with two equal objects, one of them is a AnsibleVaultEncryptedUnicode object
    s = AnsibleVaultEncryptedUnicode.from_plaintext('abc', 'vault', 'secret')
    str1 = 'abc'
    assert (s == str1) is True

    # Test with two unequal objects, both are AnsibleVaultEncryptedUnicode objects
    s = AnsibleVaultEncryptedUnicode.from_plaintext('abc', 'vault', 'secret')
    s2 = AnsibleVaultEncryptedUnicode.from_plaintext('abcd', 'vault', 'secret')
    assert (s == s2) is False

    # Test with two unequal objects, one of them is a AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 07:43:29.648403
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    if sys.version_info[0] > 2:
        import unittest

        class TestAnsibleVaultEncryptedUnicode(unittest.TestCase):
            def test_is_encrypted(self):
                '''
                Verify that is_encrypted correctly detects that a given string is encrypted.
                '''
                # Create an AVU string, encrypted or not
                ciphertext = b"d2hpdGUgY2xvdWQK"
                avu = AnsibleVaultEncryptedUnicode(ciphertext)
                avu.vault = None

                # Test if it detects that a non-encrypted string is not encrypted
                self.assertFalse(avu.is_encrypted(), "Non-encrypted string incorrectly detected as encrypted")

# Generated at 2022-06-13 07:43:38.524452
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import os
    import tempfile
    from ansible.parsing.vault import VaultLib, VaultSecret
    cleartext = 'Hello'
    vault = VaultLib(VaultSecret(str(os.urandom(16))))
    ciphertext = vault.encrypt(cleartext)
    encrypted_string = AnsibleVaultEncryptedUnicode(ciphertext)
    encrypted_string.vault = vault
    assert encrypted_string.is_encrypted()
    cleartext = 'Goodbye'
    ciphertext = cleartext
    encrypted_string = AnsibleVaultEncryptedUnicode(ciphertext)
    encrypted_string.vault = vault
    assert not encrypted_string.is_encrypted()


# Generated at 2022-06-13 07:43:51.828895
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    class MockedVault(VaultLib):
        def __init__(self):
            self.fake_key = text_type('1234567890')

        def get_password(self, prompt, confirm=False):
            return self.fake_key

        def is_encrypted(self, data):
            return True

        def encrypt(self, data, vault_password=None):
            return data

        def decrypt(self, data, vault_password=None):
            return data

    my_vault = MockedVault()
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello world', my_vault, 'foo')
    assert 'hello world' == avu



# Generated at 2022-06-13 07:44:00.078760
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def create_avu(text):
        # Make sure that the new object has a Vault attribute

        # Create a new class that inherits from AnsibleVaultEncryptedUnicode that makes
        # the .vault readable
        class MyAVEU(AnsibleVaultEncryptedUnicode):
            # Make sure that the vault is readable
            @property
            def vault(self):
                return super(MyAVEU, self).vault

        # Create a Vault object
        vault = mock.Mock()
        vault.encrypt.return_value = text
        vault.decrypt.return_value = text

        # Create the AnsibleVaultEncryptedUnicode object and return it
        return MyAVEU.from_plaintext(text, vault, mock.Mock())


# Generated at 2022-06-13 07:44:09.783578
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test only the method not any inherited methods
    def test_eq(self, other):
        if self.vault:
            return super(AnsibleVaultEncryptedUnicode, self).__eq__(other)

    import unittest
    class TestAnsibleVaultEncryptedUnicode(unittest.TestCase):
        def test_1(self):
            avu1 = AnsibleVaultEncryptedUnicode('foo')
            avu1.vault = 'Vault'
            self.assertEqual('foo', avu1)
            self.assertNotEqual('bar', avu1)
            self.assertNotEqual(avu1, 'bar')
            avu1.vault = None
            self.assertEqual(False, avu1.__eq__(avu1))


# Generated at 2022-06-13 07:44:18.835727
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import unittest
    # set up test environment
    reference = AnsibleVaultEncryptedUnicode("hello")
    # tests
    class TestTrue(unittest.TestCase):
        def test_a(self):
            test = AnsibleVaultEncryptedUnicode("hEllo")
            self.assertTrue(reference != test)
    class TestFalse(unittest.TestCase):
        def test_a(self):
            test = AnsibleVaultEncryptedUnicode("hEllo")
            test.vault = "DummyVaultClass()"
            self.assertFalse(reference != test)
    class TestException(unittest.TestCase):
        def test_a(self):
            test = AnsibleVaultEncryptedUnicode("world")

# Generated at 2022-06-13 07:44:24.443110
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Testing: sub class of AnsibleUnicode that is not decrypted until it needs to be

    # Return the right value with different args
    assert AnsibleVaultEncryptedUnicode.__ne__(text_type(''), text_type('a'))



# Generated at 2022-06-13 07:44:35.517596
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # The __ne__ method of class AnsibleVaultEncryptedUnicode must return false if:
    #     the AnsibleVaultEncryptedUnicode was created properly (with a vault) and
    #     the AnsibleVaultEncryptedUnicode was passed as an argument
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    # End of initialization for the test
    v1 = AnsibleVaultEncryptedUnicode.from_plaintext('abc', vault, 'test')
    assert not v1.__ne__(v1)


# Generated at 2022-06-13 07:44:54.357557
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(['--vault-password-file', '/dev/null'])
    plaintext = 'hello world'
    secret = 'mysecret'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert avu.__ne__(plaintext)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert not avu.__ne__(AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret))


# Generated at 2022-06-13 07:44:59.056152
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # This method is only defined to prevent __ne__ from being inherited
    # from UserString.
    vaulted = AnsibleVaultEncryptedUnicode(b'This is not the content.\n')
    assert AnsibleVaultEncryptedUnicode(b'This is not the content.\n') != vaulted


# Generated at 2022-06-13 07:45:01.076179
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    obj = AnsibleVaultEncryptedUnicode('hello')
    assert obj != 'world'


# Generated at 2022-06-13 07:45:02.256539
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:45:05.450878
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    AVU = AnsibleVaultEncryptedUnicode
    assert not (AVU('test') != 'test')
    assert AVU('test') != ''


# Generated at 2022-06-13 07:45:11.132434
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    """
    Test AnsibleVaultEncryptedUnicode.is_encrypted()
    """
    try:
        from ansible.parsing.vault import VaultLib
    except ImportError:
        _sys.stderr.write('ansible python module is not installed')
        _sys.exit(-1)


# Generated at 2022-06-13 07:45:23.618179
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test with invalid arguments
    data = "test_AnsibleVaultEncryptedUnicode"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(data, None, 'ansible')
    assert avu.__eq__(42) == False

    # Test with plaintext argument which is equal to avu.data
    data = "test_AnsibleVaultEncryptedUnicode"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(data, None, 'ansible')
    assert avu.__eq__(data) == True

    # Test with plaintext argument which is not equal to avu.data
    data = "test_AnsibleVaultEncryptedUnicode"

# Generated at 2022-06-13 07:45:35.282582
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ciphertext = b"$ANSIBLE_VAULT;1.2;AES256;fred\n"
    ciphertext += b"8d8b1be1e9eb9c64dcbacde6bfa1b00d7916ccb444438f16d0b55e2f7e9c0c9e\n"
    ciphertext += b"15c2dfb2d6bcc40e0c0e70b1f161191c3233d3b3d75c0e2afe2ce7d21f32ccb6\n"
    ciphertext += b"56f1d1c7935c6f0ccd8f056e2fd1ec9ae6a12b4f4d4d45b91654b4f350ce28d8\n"
   

# Generated at 2022-06-13 07:45:39.290937
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
	assert AnsibleVaultEncryptedUnicode("test") != "test"

if __name__ == '__main__':
   print("test_AnsibleVaultEncryptedUnicode___ne__()")
   test_AnsibleVaultEncryptedUnicode___ne__()

# Generated at 2022-06-13 07:45:46.237847
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test when ciphertext is not encrypted
    ansibleVaultEncryptedUnicodeObj = AnsibleVaultEncryptedUnicode("test")
    assert ansibleVaultEncryptedUnicodeObj != "test"

    # Test when ciphertext is encrypted
    from ansible.parsing.vault import VaultLib
    ansibleVaultEncryptedUnicodeObj.vault = VaultLib("test")
    assert ansibleVaultEncryptedUnicodeObj == "test"

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Generated at 2022-06-13 07:46:19.664433
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'pass')
    assert avu == 'test'
    assert avu == 'foo' is False

# Generated at 2022-06-13 07:46:23.203779
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode("a") != "a"
    assert AnsibleVaultEncryptedUnicode("a") != "b"


# Generated at 2022-06-13 07:46:33.527248
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import random
    import string
    import unittest
    from ansible.parsing.vault import VaultLib

    import ansible.parsing.yaml.objects as ya
    class AnsibleVaultEncryptedUnicode_T(ya.AnsibleVaultEncryptedUnicode):
        vault = None
        _ciphertext = None

        @classmethod
        def from_plaintext(cls, seq, vault, secret):
            if not vault:
                raise vault.AnsibleVaultError('Error creating AnsibleVaultEncryptedUnicode, invalid vault (%s) provided' % vault)

            ciphertext = vault.encrypt(seq, secret)
            avu = cls(ciphertext)
            avu.vault = vault
            return avu


# Generated at 2022-06-13 07:46:38.136826
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    vault = vaultlib.VaultLib('ansible')
    plaintext = 'secret string'
    secret = 'password'
    # Encrypt a string
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext,
                                                            vault,
                                                            secret)
    # Ensure that it can be decrypted again
    try:
        decrypted = encrypted.data
        assert plaintext == decrypted
    except vault.AnsibleVaultError as e:
        print(e)
        assert False

    # The encrypted string should be identified as encrypted
    assert encrypted.is_encrypted()

    # The encrypted string should not be identified as encrypted
    # if the vault implementation is not provided
    encrypted.vault = None
    assert not encrypted.is_encrypted()


# The types that ansible will try to decode

# Generated at 2022-06-13 07:46:41.216796
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Arrange
    vault = vaultlib.VaultLib('password')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('secret', vault, 'password')

    # Act
    result = avu.is_encrypted()

    # Assert
    assert result
    assert isinstance(result, bool)



# Generated at 2022-06-13 07:46:46.448971
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('mysecret')
    ciphertext = vault.encrypt(b'this is a string')
    avus = AnsibleVaultEncryptedUnicode(ciphertext)
    avus.vault = vault

    assert avus == b'this is a string'



# Generated at 2022-06-13 07:46:52.979953
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    ansible_vault_error = False
    try:
        import ansible.parsing.vault as vaultlib_mod
    except ImportError:
        ansible_vault_error = True

    # if ansible.parsing.vault is not installed, the __eq__ function
    # is defined by the class to return False.  So if the import fails
    # we don't need to test the method.
    if ansible_vault_error:
        return

    test_vault = vaultlib_mod.VaultLib("sekrit", 1, ["aes256"])
    test_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext("sekrit", test_vault, secret="sekrit")
    assert not test_vault_encrypted_unicode == "sekrit"

# Generated at 2022-06-13 07:47:03.991501
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import random
    import string
    import unittest

    from ansible_test.unit.mock.vault_test import MockVaultLib

    def _test_AnsibleVaultEncryptedUnicode___eq__(ciphertext, secret, expected_output, ansible_pos=None):
        ciphertext = to_bytes(ciphertext)
        secret = to_bytes(secret)
        avu = AnsibleVaultEncryptedUnicode(ciphertext)
        avu.vault = MockVaultLib(secret)
        if ansible_pos is not None:
            avu.ansible_pos = ansible_pos
        actual_output = avu == expected_output

# Generated at 2022-06-13 07:47:06.482305
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    av = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, 'secret')
    # Should fail without vault
    assert av != 'foo'
    return av


# Generated at 2022-06-13 07:47:14.928350
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          31323334363739653064626436653966440a34643563656664643065643934623563346538643837\n          3831373665626162323036656434663938326265623063396564336634333166650a623965656364\n          39336435636162383736333437313638376639353835626537383438323265346361386637336138\n          623738\n          ').is_encrypted()

# Generated at 2022-06-13 07:47:55.172678
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class TestVault:
        ''' mock for a vault class that does not decrypt correctly '''
        secret = 'test-secret'
        def encrypt(self, plaintext, secret):
            return 'encrypted-data'
        def decrypt(self, ciphertext, obj):
            return 'decrypted-data'
        def is_encrypted(self, ciphertext):
            return True

    sample_secret = 'test-secret'
    sample_ciphertext = 'encrypted-data'
    sample_plaintext = 'decrypted-data'
    sample_plaintext_unicode = to_text(sample_plaintext)

    # create encryption class instance
    test_vault = TestVault()

    # create encrypted unicode class instance

# Generated at 2022-06-13 07:47:58.793923
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    if not avu == 'test':
        raise AssertionError("AnsibleVaultEncryptedUnicode __eq__ failed")


# Generated at 2022-06-13 07:48:06.170074
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    from ansible.utils.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    password = text_type('some_password')
    password_bytes = to_bytes(password)
    secret = VaultSecret(password_bytes)
    vault = VaultLib(password_bytes)
    secret.password = password_bytes

    # initialize an AnsibleVaultEncryptedUnicode object avu1
    ansible_vault_encrypted_data = vault.encrypt(b'123', secret)
    avu1 = AnsibleVaultEncryptedUnicode(ansible_vault_encrypted_data)
    avu1.vault = vault

    # initialize an AnsibleVaultEncryptedUnicode object avu2

# Generated at 2022-06-13 07:48:15.620509
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    # $ANSIBLE_VAULT;1.1;AES256
    # 35306436333131353566306437626534386236633162663539646634326632346364303661336234
    # 62656262366163633236336364346232376536643966306435656666643335306436333131353566
    # 30643762653438623663316266353964663432663234636430366133623464663533646637343732
    # 65333331373633353633373362

# Generated at 2022-06-13 07:48:28.647058
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class FakeVault(object):
        def decrypt(self, ciphertext):
            return 'plaintext'

        def is_encrypted(self, ciphertext):
            return True

    class FakeObj(object):
        def __eq__(self, other):
            return other == 'plaintext'

    ciphertext = b'ciphertext'

    fake_vault1 = FakeVault()
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu1.vault = fake_vault1
    assert avu1 == 'plaintext'
    assert not avu1 == 'ciphertext'

    fake_vault2 = FakeVault()
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault = fake_vault2