

# Generated at 2022-06-13 07:38:55.842383
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert not AnsibleVaultEncryptedUnicode('abc').__ne__('abc')


# Generated at 2022-06-13 07:39:05.226028
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    # No error raised when ciphertext is not decrypted
    avu = AnsibleVaultEncryptedUnicode("NotDecrypted")
    # The strings that are valid in a ciphertext
    valid_strings = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    # The value of char parameter to test
    values = [valid_strings, valid_strings.encode('utf-8')]
    for char in values:
        result = avu.__contains__(char)
        assert not result
    return


# Generated at 2022-06-13 07:39:09.756653
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode.from_plaintext('ansible-vault', '', 'testing') == 'ansible-vault'


# Generated at 2022-06-13 07:39:23.538314
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    secret = b'a' * 16
    vault_id = 1
    vault = vaultlib.VaultLib(secret)
    vault_passwords = {}
    vault_passwords[vault_id] = secret
    crib = 'Hello '
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(crib, vault, secret)
    assert str(avu) == crib
    assert isinstance(avu, str)
    concat = 'World'
    avu += concat
    crib = 'Hello World'
    assert str(avu) == crib
    assert isinstance(avu, str)
    crib = 'Hello World!'
    avu = avu + '!'
    assert str(avu) == crib
    assert isinstance(avu, str)


# Generated at 2022-06-13 07:39:26.682031
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    text = "plaintext"

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(text, None, None)
    assert avu.is_encrypted() == False

    avu = AnsibleVaultEncryptedUnicode("ciphertext")
    assert avu.is_encrypted() == True


# Generated at 2022-06-13 07:39:28.162209
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode.from_plaintext(b'hello', None, b'pwd') != 'hello'



# Generated at 2022-06-13 07:39:33.806118
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:39:43.655136
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    test_cases = [
        ("", "", ""),
        ("foo", "bar", "foobar"),
        ("foo", "", "foo"),
        ("", "bar", "bar"),
        ("foo", "bar", "foobar"),
        ("foo", "bar", "foobar"),
        ("foobar", "bar", "foobarbar"),
    ]
    vault = vaultlib.VaultLib([])
    secret = "test"
    for (val1, val2, answer) in test_cases:
        avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(val1, vault, secret)
        avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(val2, vault, secret)
        assert((avu1 + avu2).data == answer)

# Generated at 2022-06-13 07:39:48.049689
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    string1 = AnsibleVaultEncryptedUnicode(b'hello')
    string2 = AnsibleVaultEncryptedUnicode(b'world')
    assert string1 != 'hello'
    assert string1 != string2
    string1.data = 'hello'
    assert not(string1 != 'hello')
    assert string1 != string2
    string2.data = 'hello'
    assert not(string1 != string2)


# Generated at 2022-06-13 07:39:57.197343
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    assert AnsibleVaultEncryptedUnicode("123456")[:] == "123456"
    assert AnsibleVaultEncryptedUnicode("123456")[4:] == "5678"
    assert AnsibleVaultEncryptedUnicode("12345678")[-4:] == "5678"
    assert AnsibleVaultEncryptedUnicode("1234567890")[:-3] == "123456"
    assert AnsibleVaultEncryptedUnicode("1234567890")[:] == "1234567890"
    assert AnsibleVaultEncryptedUnicode("1234567890")[-10:] == "1234567890"


# Generated at 2022-06-13 07:40:07.210021
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    avu1 = AnsibleVaultEncryptedUnicode(b'Hello')
    avu2 = AnsibleVaultEncryptedUnicode(b', World!')
    avu3 = avu1 + avu2
    result = to_native(avu3.data)
    assert result == 'Hello, World!'


# Generated at 2022-06-13 07:40:18.654484
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():

    class _MockedVault:
        def __init__(self, encrypt_text, is_encrypted_return):
            self.encrypt_text = encrypt_text
            self.is_encrypted_return = is_encrypted_return
        def encrypt(self, plaintext, password):
            assert plaintext == self.encrypt_text
            return 'ciphertext'
        def is_encrypted(self, ciphertext):
            return self.is_encrypted_return

    def check(data, sub, expect):
        print('check(%s, %s, %s)' % (data, sub, expect))
        avu = AnsibleVaultEncryptedUnicode.from_plaintext(data, _MockedVault(data, False), 'password')
        got = avu.__contains__(sub)

# Generated at 2022-06-13 07:40:31.917788
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    import os

    test_file = os.path.join(os.path.dirname(__file__), 'vault_test_files', 'vault_test_0.yml')
    with open(test_file, 'r') as f:
        vault_data = yaml.load(f)

    secret = u'ansible'
    vault_secret_file = os.path.join(os.path.dirname(__file__), 'vault_test_files', 'vault_secret.txt')
    vault = VaultLib(vault_secret_file)

    # the vault_data must be decrypted with secret at the top level
    vault._decrypt_data(vault_data, secret)

    # both objects has the same data, so should be equal

# Generated at 2022-06-13 07:40:38.524762
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    Test for method __ne__ of class AnsibleVaultEncryptedUnicode
    '''
    from ansible.parsing.vault import VaultLib

    vault = VaultLib('test')
    secret = 'test'
    string = 'test'
    encrypted_string = AnsibleVaultEncryptedUnicode.from_plaintext(string, vault, secret)
    assert encrypted_string.__ne__(string) is False


# Generated at 2022-06-13 07:40:44.913622
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    class X(AnsibleVaultEncryptedUnicode):
        pass
    x = X(b'foobar')
    assert 'f' in x
    assert 'F' not in x
    assert 'F'.lower() in x
    assert 'bar' in x
    assert 'xyz' not in x
    assert X(b'foobar') in x
    assert X(b'foo') in x
    assert X(b'bar') in x
    assert X(b'xyz') not in x
    assert X(b'') not in x

# Generated at 2022-06-13 07:40:57.114893
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Simple test for the AnsibleVaultEncryptedUnicode.__eq__() function
    """

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, to_text

    vault_password = "vault_password"

    # Create a ansible base object
    abo = AnsibleVaultEncryptedUnicode('')
    # Create a vault object
    vault = VaultLib(vault_password)

    # Test that __eq__ returns False if the object's ansible vault
    # attribute (avu.vault) is None.
    abo.data = "abc"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(abo.data, vault, vault_password)
   

# Generated at 2022-06-13 07:41:09.008726
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test_AnsibleVaultEncryptedUnicode_password')
    avu1 = AnsibleVaultEncryptedUnicode('hello')
    avu2 = AnsibleVaultEncryptedUnicode('world')
    avu2.vault = vault

    # add AnsibleVaultEncryptedUnicode
    avu3 = avu1 + avu2
    assert isinstance(avu3, AnsibleVaultEncryptedUnicode)
    assert avu3.data == 'helloworld'

    # add plaintext string
    avu3 = avu1 + 'world'
    assert isinstance(avu3, AnsibleVaultEncryptedUnicode)
    assert avu3.data == 'helloworld'

    #

# Generated at 2022-06-13 07:41:19.697249
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    # Create a vault object
    vault_obj = AnsibleVaultEncryptedUnicode.from_plaintext('Test Data', vault=None, secret='test')

    # Results of object contains operation
    r1 = 'T' in vault_obj
    r2 = 'T' in AnsibleVaultEncryptedUnicode.from_plaintext('T', vault=None, secret='test')
    r3 = 'T' in AnsibleVaultEncryptedUnicode('T')

    # If any result is False, the test fails
    assert (r1 and r2 and r3) == True



# Generated at 2022-06-13 07:41:29.772341
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # type: () -> None
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(['--vault-id', 'test'])
    plaintext = "abcd"
    ciphertext = vault.encrypt(plaintext, vault._secret)
    aveu = AnsibleVaultEncryptedUnicode(ciphertext)
    aveu.vault = vault
    assert aveu.is_encrypted() == True, "The method is_encrypted of class AnsibleVaultEncryptedUnicode returned False, when it should have returned True"
    plaintext = "abcd"
    aveu = AnsibleVaultEncryptedUnicode(plaintext)
    aveu.vault = vault

# Generated at 2022-06-13 07:41:33.023369
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    mystring = "abcd"
    av = AnsibleVaultEncryptedUnicode(mystring)
    assert ("a" in av) and ("d" in av) and ("x" not in av)


# Generated at 2022-06-13 07:41:44.510164
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault
    ansibleVault = vault.AnsibleVault(password=None, secret=b'1234')

# Generated at 2022-06-13 07:41:48.744115
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Inject import of vault lib which is done in Ansible modules
    sys.modules['ansible.parsing.vault'] = __import__('ansible.parsing.vault')
    vault = sys.modules['ansible.parsing.vault']

    # Create a vault object for testing
    vault_obj = vault.VaultLib('mysecret')

    # Create a AnsibleVaultEncryptedUnicode object
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('the plain text', vault_obj, 'mysecret')

    # Tests
    assert(avu == 'the plain text')
    assert(avu != 'the plain')
    assert(avu != 1)
    assert(avu != 1.0)
    assert(avu != True)



# Generated at 2022-06-13 07:41:51.072532
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    v = AnsibleVaultEncryptedUnicode(b'x')
    assert v != b'y'
    assert v != 'y'
    assert v != u'y'


# Generated at 2022-06-13 07:42:01.653083
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    print(to_native(_sys.modules[__name__]))
    import unittest

    class TestAnsibleVaultEncryptedUnicode(unittest.TestCase):
        def setUp(self):
            from ansible.parsing.vault import VaultLib

            _vault = VaultLib('testme')
            self.YAMLStringWithVault = AnsibleVaultEncryptedUnicode(
                _vault.encrypt('secret')
            )
            self.YAMLStringWithVault.vault = _vault

        def test_ne(self):
            self.assertTrue(self.YAMLStringWithVault != 'secret')

    if __name__ == '__main__':
        unittest.main()


# Generated at 2022-06-13 07:42:04.757191
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import ansible.parsing.vault as vault

    v = vault.VaultLib('password')
    s = AnsibleVaultEncryptedUnicode.from_plaintext('foo', v, 'password')
    assert(s != 'foo')


# Generated at 2022-06-13 07:42:14.355734
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # prepare data
    plaintext = 'a'
    ciphertext = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          38323961353438386338623036396338613662343733663765383865323335396164323139623337\n          31373830656533353639366566326233393164626261666535303531363063316638353061306661\n          31633561306433323931343035393131666632313264336431623937343865376433636161396533\n          62363261326266653036376239\n          '
    password = 'ansible'
    vault = vaultlib.VaultLib([password])
    avue

# Generated at 2022-06-13 07:42:23.728795
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
	from ansible.parsing.vault import VaultLib
	from ansible.parsing.vault import get_vault_secret
	from ansible.parsing.vault import get_file_vault_secret
	from ansible.parsing.vault import AnsibleVaultError

	import sys
	def get_ansible_version(version_tuple):
		if isinstance(version_tuple[-1], str):
			return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
		return '.'.join(map(str, version_tuple))
	ansible_version = get_ansible_version(sys.version_info)

	data="int"
	password='ansible'

# Generated at 2022-06-13 07:42:36.131963
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible_collections.ansible.community.plugins.module_utils.vault import VaultLib

    seq = 'secret'
    secret = 'secret'
    vault = VaultLib('sha1')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert avu.__ne__(seq) == False

    seq = 'secret'
    secret = 'secret'
    vault = VaultLib('sha256')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert avu.__ne__(seq) == False


# Generated at 2022-06-13 07:42:38.052025
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def test_data(data):
        assert data == 'test'
        assert not data == 'test2'

    test_data(AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None))



# Generated at 2022-06-13 07:42:39.902905
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('bar', None, None)
    assert avu == 'bar'


# Generated at 2022-06-13 07:42:55.229273
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib, VaultEditor

    ciphertext = VaultLib.encrypt(b"foo", b"bar")
    assert not AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()
    assert AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode(b'hello').is_encrypted()

test_AnsibleVaultEncryptedUnicode_is_encrypted()



# Generated at 2022-06-13 07:43:07.159706
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.six import text_type

    if sys.version_info[0] == 2:
        ord_ = lambda x: ord(x)
    else:
        ord_ = lambda x: x

    vault = VaultLib(bytes(to_text('some_secret')))

    # AnsibleVaultEncryptedUnicode class should be able to wrap a secret
    # ciphertext obtained by another vaultlib object
    txt = 'This is a secret message'
    ciphertext = vault.encrypt(txt, secret='some_secret').rstrip()
    avu = Ansible

# Generated at 2022-06-13 07:43:13.369405
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(password='password')
    avu1 = AnsibleVaultEncryptedUnicode('test')
    avu1.vault = vault
    assert avu1.is_encrypted()

    avu2 = AnsibleVaultEncryptedUnicode(avu1)
    avu2.vault = vault
    assert avu2.is_encrypted()

    avu3 = AnsibleVaultEncryptedUnicode(vault.encrypt('test2', b'1234'))
    avu3.vault = vault
    assert avu3.is_encrypted()

    avu4 = AnsibleVaultEncryptedUnicode(vault.encrypt('test2', b'1234'))
    assert avu4.is_encrypted()

# Generated at 2022-06-13 07:43:17.768659
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    my_o = AnsibleVaultEncryptedUnicode("some data")
    assert(my_o != "some data")

# --- end of AnsibleVaultEncryptedUnicode methods ---



# Generated at 2022-06-13 07:43:29.957368
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def do_check(a_value, b_value, b_type, expected_result):
        a = AnsibleVaultEncryptedUnicode(a_value)
        a.vault = 'Dummy Vault'
        b = None
        if b_type == AnsibleVaultEncryptedUnicode:
            b = AnsibleVaultEncryptedUnicode(b_value)
            b.vault = 'Dummy Vault'
        else:
            b = b_type(b_value)
        result = (a == b)
        assert result == expected_result, 'a = %r, b = %r, result = %r, expected result = %r' % (a, b, result, expected_result)

    do_check('some string', 'some string', AnsibleVaultEncryptedUnicode, True)
   

# Generated at 2022-06-13 07:43:45.279210
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    ciphertext = vault.encrypt('foo')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted()

    ciphertext = vault.encrypt(r"[%s]\nhosts=192.168.1.0/24" % 'foo')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted()

    ciphertext = vault.encrypt(r'[foo] hosts=192.168.1.0/24')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

# Generated at 2022-06-13 07:43:51.483222
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault_password = 'secret'
    plaintext = 'plaintext'
    vault = VaultLib(vault_password)
    encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, vault_password)
    assert encrypted_unicode == plaintext


# Generated at 2022-06-13 07:43:59.919678
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import vaultlib

    vault = vaultlib.VaultLib('ansible')
    secret = 'foo'
    plaintext = to_text('dynamic', errors='surrogate_or_strict')
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted()
    assert avu.data == to_text('dynamic', errors='surrogate_or_strict')

    avu = AnsibleVaultEncryptedUnicode(to_text('dynamic', errors='surrogate_or_strict'))
    avu.vault = vault
    assert not avu.is_encrypted()

# Generated at 2022-06-13 07:44:09.751832
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:44:16.353167
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange
    class AnsibleVaultStub():
        # stub to by pass the check in __init__
        # and make sure this test does not crash on __ne__
        pass

    # Act
    avueu = AnsibleVaultEncryptedUnicode('test')

    # Assert as there is no easy way to test for equality
    # simply verify that __ne__ does not crash
    assert avueu.__ne__('test')
    assert avueu.__ne__(AnsibleVaultEncryptedUnicode('test'))

    # Make sure that a vault is set to by pass checks in __ne__
    avueu.vault = AnsibleVaultStub()
    assert avueu.__ne__('test')


# Generated at 2022-06-13 07:44:37.601303
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = 'secret'
    seq = 'seq'
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(secret)
    # Test if both objects are equal
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert(avu1.__eq__(avu1))
    # Test if both objects are encrypted and are not equal
    assert(avu1.__eq__(AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)))
    # Test if both objects are not equal
    assert(not avu1.__eq__(AnsibleVaultEncryptedUnicode.from_plaintext(seq + 'X', vault, secret)))
    # Test if both objects are not equal

# Generated at 2022-06-13 07:44:47.617677
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError

    text = 'test'

# Generated at 2022-06-13 07:44:58.982838
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    class MyVault:
        def __init__(self):
            self.current_secret = 'secret1'
            self.old_secrets = ['secret2']

        def encrypt(self, plaintext, secret=None):
            if not plaintext:
                return ''
            return 'encrypted({})'.format(plaintext)

        def decrypt(self, ciphertext, secret=None):
            if not ciphertext:
                return ''
            return 'decrypted({})'.format(ciphertext)

        def is_encrypted(self, ciphertext):
            if not ciphertext:
                return False
            return salt_string(ciphertext, 'encrypted')

    def salt_string(string, salt):
        string = to_text(string)
        return string.startswith(salt)

    vault = MyVault()
    secret

# Generated at 2022-06-13 07:45:09.923990
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault

    secret = b'this is a secret'
    secret_text = to_text(secret)
    avu_secret = AnsibleVaultEncryptedUnicode.from_plaintext(secret_text, vault, secret)
    assert avu_secret.is_encrypted()

    avu_plaintext = AnsibleVaultEncryptedUnicode(secret_text)
    assert not avu_plaintext.is_encrypted()

    avu_ciphertext = AnsibleVaultEncryptedUnicode(avu_secret.vault.encrypt(secret_text, secret))
    assert avu_ciphertext.is_encrypted()

    avu_decrypted = AnsibleVaultEncryptedUnicode.from_plaintext(avu_plaintext.data, vault, secret)

# Generated at 2022-06-13 07:45:11.482233
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:45:17.813199
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import unittest
    import ansible.parsing.vault
    vault = ansible.parsing.vault.VaultLib('secret')


# Generated at 2022-06-13 07:45:25.097832
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault

    plaintext = "Vault is used to encrypt arbitrary data."
    password = "secret"

    vault_obj = vault.VaultLib(password)
    encryptedVault_obj = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault_obj, password)

    assert encryptedVault_obj.is_encrypted()

    decryptedVault = vault_obj.decrypt(encryptedVault_obj, password)

    assert decryptedVault == plaintext



# Generated at 2022-06-13 07:45:30.452722
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    v = VaultLib('password')

    assert True == AnsibleVaultEncryptedUnicode.from_plaintext('password', v, 'password').is_encrypted()
    assert False == AnsibleVaultEncryptedUnicode.from_plaintext('password', None, 'password').is_encrypted()



# Generated at 2022-06-13 07:45:41.817458
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import ansible.parsing.vault as vault
    vault_secret = "vault_secret"
    vault_id = "12345"
    expected = True
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("a", vault, vault_secret)
    assert avu != "b"


yaml.add_representer(AnsibleVaultEncryptedUnicode,
                     lambda dumper, data: dumper.represent_scalar(u'!vault', data._ciphertext),
                     Dumper=yaml.SafeDumper)
yaml.add_constructor(u'!vault',
                     lambda loader, node: AnsibleVaultEncryptedUnicode(to_bytes(loader.construct_scalar(node))),
                     Loader=yaml.SafeLoader)




# Generated at 2022-06-13 07:45:49.882539
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class MockVault:
        def __init__(self):
            self.secret = 'test_secret'

        def is_encrypted(self, indata):
            if not indata.decode('utf-8').startswith('$ANSIBLE_VAULT;'):
                return False
            return True

        def decrypt(self, indata):
            return indata.decode('utf-8')

    # Test for ansible_vault_string_eq
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('abc', MockVault(), 'test_secret')
    assert_equals(avu == 'abc', True)
    assert_equals(avu == 'abd', False)

    # Test for ansible_vault_text_eq
    avu = AnsibleVaultEncryptedUnic

# Generated at 2022-06-13 07:46:23.138401
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode('vault(1.2)$917ed23f78d66b7d$dW8KZISZA3YhqwN7KdDgxuV7HeXLp29NuVtA/Mf8')
    av1 = AnsibleVaultEncryptedUnicode('vault(1.2)$917ed23f78d66b7d$dW8KZISZA3YhqwN7KdDgxuV7HeXLp29NuVtA/Mf8')

# Generated at 2022-06-13 07:46:27.080391
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Check to ensure string comparison works properly when comparing
    # AnsibleVaultEncryptedUnicode to AnsibleVaultEncryptedUnicode
    assert AnsibleVaultEncryptedUnicode('expect') == \
           AnsibleVaultEncryptedUnicode('expect')


# Generated at 2022-06-13 07:46:30.683406
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert(AnsibleVaultEncryptedUnicode.from_plaintext("foo", None, None) == "foo")


# Generated at 2022-06-13 07:46:35.454750
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    x = AnsibleVaultEncryptedUnicode('test data')
    x.vault = '__FakeVault__'
    y = AnsibleVaultEncryptedUnicode('test data')

    assert(x != y)


# Generated at 2022-06-13 07:46:47.679474
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault_password = 'mypassword'
    secret = 'secretstring'

# Generated at 2022-06-13 07:47:00.305408
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # these are all non-encrypted values
    assert not AnsibleVaultEncryptedUnicode.from_plaintext('str', None, None).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode.from_plaintext(1234567890, None, None).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode.from_plaintext(['str'], None, None).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode.from_plaintext({'str': 1}, None, None).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode.from_plaintext(True, None, None).is_encrypted()
    assert not AnsibleVaultEncryptedUnicode.from_plaintext(None, None, None).is_encrypted()
    assert not AnsibleVault

# Generated at 2022-06-13 07:47:06.557266
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.utils.vault import VaultLib

    plaintext = u'SuperSecretCiphertext'
    ciphertext = VaultLib.encrypt(plaintext)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    # We have not set a vault attribute, so it should be encrypted
    assert avu.is_encrypted() is True
    avu.vault = VaultLib(None)
    # Now that a vault is set, we can decrypt
    assert avu.is_encrypted() is False



# Generated at 2022-06-13 07:47:14.991770
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import vault

    vault_pass = 'vault123'
    example_var = 'secret'
    vault = vault.VaultLib(vault_pass)
    ciphertext = vault.encrypt(example_var)

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    # test against string
    assert avu == example_var

    # test against already decrypted AnsibleVaultEncryptedUnicode
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault = vault
    assert avu == avu2

    # test against not decrypted AnsibleVaultEncryptedUnicode
    avu3 = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu != avu3




# Generated at 2022-06-13 07:47:17.918014
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('foo')
    avu.data = 'bar'
    assert avu != 'foo'


# Generated at 2022-06-13 07:47:23.937089
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Given a string
    string_data = text_type('some string')
    # When AnsibleVaultEncryptedUnicode is created using the string data
    avu = AnsibleVaultEncryptedUnicode(string_data)
    # When __ne__ method is called using the string data
    v = avu.__ne__(string_data)
    # Then False should be returned.
    assert v is False


# Generated at 2022-06-13 07:48:04.308045
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import vault

    vault.VaultLib.load_crypto_libs()
    vault_id = vault.VaultLib.generate_vault_id()
    vault_password = 'foo'
    vault_lib = vault.VaultLib([vault_password, None, vault_id])
    vault_encrypted_string = to_text(vault_lib.encrypt('bar'))
    avu = AnsibleVaultEncryptedUnicode(vault_encrypted_string)
    avu.vault = vault_lib
    assert avu != 'bar'


# Generated at 2022-06-13 07:48:14.441861
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    a = AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:48:27.103432
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:48:34.799115
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    # Test if __eq__ is checking against the decrypted data and not the ciphertext
    # If the eq is against the ciphertext, then the encrypted strings are equal
    # and the test would fail
    vault = VaultLib([])
    secret = b'password'
    vaulttext1 = AnsibleVaultEncryptedUnicode.from_plaintext(b'the quick brown fox', vault, secret)
    vaulttext2 = AnsibleVaultEncryptedUnicode.from_plaintext(b'the quick brown fox', vault, secret)
    assert vaulttext1 == vaulttext2
    assert not vaulttext1 != vaulttext2