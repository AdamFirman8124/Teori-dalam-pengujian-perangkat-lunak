

# Generated at 2022-06-13 07:38:53.184275
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    # Constants
    test_vault_str = 'test vault string'

    # Code to execute
    avu1 = AnsibleVaultEncryptedUnicode(test_vault_str)
    avu2 = AnsibleVaultEncryptedUnicode(test_vault_str)
    avu3 = AnsibleVaultEncryptedUnicode('another test vault string')

    # Check assumptions
    assert bool(avu1) == True
    assert bool(avu2) == True
    assert bool(avu3) == True

    # Unit tests
    assert avu1 == avu2
    assert avu2 == avu1
    assert avu1 != avu3
    assert avu3 != avu1
    assert avu1 < avu3
    assert not (avu1 < avu2)
   

# Generated at 2022-06-13 07:39:00.628592
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    # check if we have a Vault object
    if not os.path.exists('vault/test.vault'):
        return

    # create Vault
    vault_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vault/test.vault')
    vault = VaultLib('secret', vault_file)

    # create test objects
    s = AnsibleVaultEncryptedUnicode.from_plaintext('abcdefghi', vault, 'secret')
    u = AnsibleVaultEncryptedUnicode.from_plaintext('jklmnopqr', vault, 'secret')
    ss = AnsibleVaultEncryptedUnicode.from_plaintext('stuvwxyz1', vault, 'secret')
    uu = AnsibleVaultEncryptedUn

# Generated at 2022-06-13 07:39:12.110117
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Calling code needs to set the .vault attribute to a vaultlib object
    a = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n' +
                                     '6561613566373331396333643937623766666333323332356666653634363064\n' +
                                     '6366613164326262616661333332373964333331653131373838626230343038\n' +
                                     '38373934376136613139\n')

# Generated at 2022-06-13 07:39:20.452084
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    text = 'test_test'

# Generated at 2022-06-13 07:39:27.162539
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    a = AnsibleVaultEncryptedUnicode('a')
    b = AnsibleVaultEncryptedUnicode('b')
    assert(a < b)
    assert(a < 'b')
    assert(a <= b)
    assert(a <= 'b')
    assert(a != b)
    assert(a != 'b')
    assert(a <= a)
    assert(a <= 'a')
    assert(a == a)
    assert(a == 'a')
    assert(a >= a)
    assert(a >= 'a')


# Generated at 2022-06-13 07:39:27.893496
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass



# Generated at 2022-06-13 07:39:33.204784
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    seq = '''First line.
Second line.
Third line.
Fourth line.
Fifth line.'''

    v = AnsibleVaultEncryptedUnicode.from_plaintext(seq, None, None)
    print(v[3])
    print(v[3:])
    print(v[3:5])
    print(v[:5])
    print(v[::-1])
    print(v[-5:])
    print(v[:-5])
    print(v[-5:-1])
    print(v[-7:])
    print(v[:-7])
    print(v[-7:-1])


# Unit tests for class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:39:37.716109
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    avu = AnsibleVaultEncryptedUnicode("test")
    if avu[1:-1] != "es":
        raise AssertionError("This should be equal to 'es' not '{}'".format(avu[1:-1]))


# Generated at 2022-06-13 07:39:44.152471
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    encrypted = AnsibleVaultEncryptedUnicode("0123456789")
    assert "0" == encrypted[0]
    assert "3" == encrypted[3]
    assert "345" == encrypted[3:6]
    assert "3456" == encrypted[3:7]
    assert "34567" == encrypted[3:8]
    assert "345678" == encrypted[3:9]
    assert "3456789" == encrypted[3:10]



# Generated at 2022-06-13 07:39:47.836792
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    seq = 'passwordwxyzz'
    seq_obj = AnsibleVaultEncryptedUnicode(seq)
    assert seq_obj.rfind('wxyz') == seq.rfind('wxyz')

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 07:39:58.929179
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    AV = AnsibleVaultEncryptedUnicode

    assert AV("foo").__eq__("foo") is True
    assert AV("foo").__eq__("bar") is False
    assert AV("foo").__eq__(AV("foo")) is True
    assert AV("foo").__eq__(AV("bar")) is False



# Generated at 2022-06-13 07:40:04.837064
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    test_vault = vault.AES256VaultLib(None)
    secret = b"secret"
    plaintext = b"plaintext"
    plaintext_unicode = to_text(plaintext)
    plaintext_avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, test_vault, secret)

    assert plaintext_avu == plaintext_unicode
    assert plaintext_avu == plaintext
    assert not plaintext_avu == b"difftxt"




# Generated at 2022-06-13 07:40:11.135921
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.parsing.vault import VaultLib
    secret = b'qwerty123'
    plaintext = u'plaintext'
    vault = VaultLib(secret)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert plaintext == avu[:], \
        "AnsibleVaultEncryptedUnicode.__getslice__() failed to decrypt"


# Generated at 2022-06-13 07:40:23.287875
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    import string
    import random
    import vault.cli

    # Generate a random string
    def random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    # Generate random password
    passwd = random_string()

    # Create a vault
    vault = vault.cli.VaultLib(password=passwd)

    # Create a encrypted str1
    str1 = random_string()
    encrypted_str1 = AnsibleVaultEncryptedUnicode.from_plaintext(str1, vault, passwd)

    # Create a encrypted str2
    str2 = random_string()
    encrypted_str2 = AnsibleVaultEncryptedUnicode.from_plaintext(str2, vault, passwd)

    # Test __le__

# Generated at 2022-06-13 07:40:26.609028
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('abc', vault=None, secret='abc')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('def', vault=None, secret='abc')
    assert not avu1 <= avu2
    assert not avu2 <= avu1
    assert avu1 <= 'def'
    assert avu2 <= 'ghi'
    assert avu1 <= 'abc'


# Generated at 2022-06-13 07:40:31.460682
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    """ Test for AnsibleVaultEncryptedUnicode.__getslice__ """

    avu = AnsibleVaultEncryptedUnicode('abcd')
    assert avu.__getslice__(0, 4) == 'abcd'
    assert avu.__getslice__(1, 3) == 'bc'
    assert avu.__getslice__(1, -1) == 'bc'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:40:35.115548
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    assert AnsibleVaultEncryptedUnicode.__getslice__(None, 0, 0) == None
    assert AnsibleVaultEncryptedUnicode.__getslice__(None, -2, -1) == None


# Generated at 2022-06-13 07:40:44.838406
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible_vault import VaultLib

    secret = 'pass123'
    vault = VaultLib(secret)
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext('abc', vault=vault, secret=secret)
    assert encrypted == 'abc'

    # set ciphertext to something else, then .data is different, but .ciphertext is equal
    encrypted.ciphertext = 'def'
    assert encrypted.data == 'abc'
    assert encrypted.ciphertext == 'def'
    assert encrypted.ciphertext == 'def'
    assert encrypted == 'abc'

    # as data is not 'def', __eq__ should return False
    assert encrypted != 'def'


yaml.add_representer(AnsibleUnicode,
        yaml.representer.SafeRepresenter.represent_unicode)

# Generated at 2022-06-13 07:40:57.115336
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.plugins.vault import VaultLib
    vault = VaultLib()
    secret = 'blah'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('abcdefghijklmnop', vault, secret)
    avu.vault = VaultLib()
    assert avu.__getslice__(3,-3) == 'defghi'
    # Test the first character
    assert avu.__getslice__(0,1) == 'a'
    # Test the last character
    assert avu.__getslice__(-1,-1) == 'p'
    # Test the empty string
    assert avu.__getslice__(0,0) == ''
    # Test the empty string, with args that match the full string

# Generated at 2022-06-13 07:41:09.009937
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:41:16.349774
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avu1 = AnsibleVaultEncryptedUnicode("abc")
    assert(avu1 <= "abc")


# Generated at 2022-06-13 07:41:25.950670
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test with
    # - same plaintext (password provided)
    #  - different vault object
    #  - no password provided (__eq__ should return False)
    #  - same password
    # - different plaintext
    class DummyVault1(object):
        def decrypt(self, ciphertext, obj=None):
            return 'same plaintext'
        def is_encrypted(self, ciphertext):
            return True

    class DummyVault2(object):
        def decrypt(self, ciphertext, obj=None):
            return 'same plaintext'
        def is_encrypted(self, ciphertext):
            return True

    class DummyVault3(object):
        def decrypt(self, ciphertext, obj=None):
            return 'different plaintext'
        def is_encrypted(self, ciphertext):
            return

# Generated at 2022-06-13 07:41:31.029934
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test case is to check the method __eq__ of class AnsibleVaultEncryptedUnicode
    # Test case is to check the method __eq__ of class AnsibleVaultEncryptedUnicode (==)
    assert AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=None, secret='test') == AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=None, secret='test')


# Generated at 2022-06-13 07:41:35.319801
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('abcd',
                                                      ansible.parsing.vault.VaultLib(),
                                                      's3cr3t')
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:41:38.896998
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avue1 = AnsibleVaultEncryptedUnicode('apple')
    avue2 = AnsibleVaultEncryptedUnicode('coconut')
    avue3 = AnsibleVaultEncryptedUnicode('coconut')
    assert( not ( avue1 <= avue2 ) )
    assert( avue2 <= avue3 )
    assert( avue2 < avue3 )
    assert( not ( avue1 < avue2 ) )


# Generated at 2022-06-13 07:41:48.582884
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    from .vault import VaultLib
    vault = VaultLib(b'password')

    avue = AnsibleVaultEncryptedUnicode.from_plaintext(b"test", vault, b"test")
    assert avue.__le__(b"test")

    val_1 = AnsibleVaultEncryptedUnicode.from_plaintext(b"test", vault, b"test")
    val_2 = AnsibleVaultEncryptedUnicode.from_plaintext(b"test", vault, b"test")
    assert val_1.__le__(val_2)


# Generated at 2022-06-13 07:41:54.716718
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    def encrypted_init_helper(cipher, match_secret, non_match_secret):
        avu1 = AnsibleVaultEncryptedUnicode(cipher)
        avu1.vault = vault
        avu1_match_result = avu1 != avu1_match_secret
        avu1_non_match_result = avu1 != avu1_non_match_secret
        return (avu1_match_result, avu1_non_match_result)

    vault = AnsibleVault()
    cipher = vault.encrypt('grep pam_faillock /etc/pam.d/password-auth', 'ansible')
    avu1_match_secret = AnsibleVaultEncryptedUnicode(cipher)
    avu1_match_secret.vault = vault


# Generated at 2022-06-13 07:41:59.750719
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import vaultlib
    vault = vaultlib.VaultLib('test')

    # test unencrypted
    testobj = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'secret')
    assert not testobj.is_encrypted()

    # test encrypted
    testobj.data = vault.encrypt('foo', 'secret')
    assert testobj.is_encrypted()


# Generated at 2022-06-13 07:42:03.947069
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():

    # Building some variables
    my_data = 'abcdefg'

    # Run the test
    test_avu = AnsibleVaultEncryptedUnicode(my_data)
    actual = (test_avu != my_data)
    expected = False
    assert expected==actual



# Generated at 2022-06-13 07:42:14.045216
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    assert 2 == 2


# Generated at 2022-06-13 07:42:26.223750
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Setup test environment
    import ansible.parsing.vault as vault
    import VaultLib
    global password
    password = 'secret'
    my_vault = VaultLib.VaultEditor(password)

# Generated at 2022-06-13 07:42:39.235402
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.yaml.vault import VaultLib
    import getpass

    # Create VaultLib object with secret as password
    vault = VaultLib(getpass.getpass('Vault password: '))

    # Create a AnsibleVaultEncryptedUnicode object with yaml_tag !vault.
    # It is a sub class of AnsibleUnicode so the constructor of AnsibleUnicode
    # is called to create object avu.
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'secret')
    assert avu == 'test'
    assert avu != 'te'
    assert avu != 'test_'


# Generated at 2022-06-13 07:42:49.732262
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''
    Tests for method __eq__ of class AnsibleVaultEncryptedUnicode
    '''

    v = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert v == 'foo'
    assert 'foo' == v

    v = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert v != 'bar'
    assert 'bar' != v

    v = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert v == AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None) == v


# Generated at 2022-06-13 07:42:58.234171
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    from ansible.parsing.vault import VaultLib

    vault_password_file = "./test/unit/vault_password_file"
    vault_secret = open(vault_password_file).read().rstrip()


# Generated at 2022-06-13 07:43:01.908600
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avu1 = AnsibleVaultEncryptedUnicode('foo')
    avu2 = AnsibleVaultEncryptedUnicode('foo')
    assert avu1 <= avu2



# Generated at 2022-06-13 07:43:09.862525
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Case 1: AnsibleUnicode
    assert AnsibleVaultEncryptedUnicode('Hello') != 'Hello'
    assert AnsibleVaultEncryptedUnicode('Hello') != AnsibleUnicode('Hello')

    # Case 2: AnsibleVaultEncryptedUnicode
    assert AnsibleVaultEncryptedUnicode('Hello') != AnsibleVaultEncryptedUnicode('Hello')

    # Case 3: Other
    assert AnsibleVaultEncryptedUnicode('Hello') != u'Hello'
    assert AnsibleVaultEncryptedUnicode('Hello') != 'Hello'
    assert AnsibleVaultEncryptedUnicode('Hello') != None


# Generated at 2022-06-13 07:43:24.777240
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    test_vault_password = u'test_password'
    test_vault_secrets = [
        u'test_secret',
        u'test_secret_with_special_character_+',
        u'test_secret_with_special_character_-',
        u'test_secret_with_special_character_/',
        u'test_secret_with_special_character_=',
    ]
    test_vault = ansible.parsing.vault.VaultLib(test_vault_password)
    for test_vault_secret in test_vault_secrets:
        input_string = AnsibleVaultEncryptedUnicode.from_plaintext(test_vault_secret, test_vault, test_vault_password)
       

# Generated at 2022-06-13 07:43:31.509147
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = '123'
    ciphertext = VaultLib(dev_random_bytes=16).encrypt(u'hello world', password=secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert(not avu.is_encrypted())
    avu.vault = VaultLib(dev_random_bytes=16)
    assert(avu.is_encrypted())


# Generated at 2022-06-13 07:43:34.126600
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    obj1 = AnsibleVaultEncryptedUnicode("abc")
    obj2 = AnsibleVaultEncryptedUnicode("abc")

    assert obj1 != obj2


# Generated at 2022-06-13 07:43:42.955957
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault
    # We need to create vault then, for the purpose of testing
    vault_password = 'ansible'
    vault_obj = vault.VaultLib(vault_password)

    # cases to be tested

# Generated at 2022-06-13 07:43:56.161721
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avuu = AnsibleVaultEncryptedUnicode(b'bar')
    assert avuu == avuu.data == 'bar'
    assert avuu != avuu.data != 'foo'
    # This was a bug in ansible-2.9.9
    assert not(avuu == avuu.data == 'foo')
    assert not(avuu != avuu.data != 'bar')



# Generated at 2022-06-13 07:44:06.387141
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    if not hasattr(AnsibleVaultEncryptedUnicode, '__le__'):
        raise AssertionError('__le__ method not implemented')
    try:
        a = AnsibleVaultEncryptedUnicode('foo')
        b = AnsibleVaultEncryptedUnicode('foo')
        c = AnsibleVaultEncryptedUnicode(u'bar')

        if not a <= b:
            raise AssertionError('__le__ failed for equal strings')

        if a <= c:
            raise AssertionError('__le__ failed for non-equal strings')
    except Exception:
        raise AssertionError('__le__ failed for some reason')



# Generated at 2022-06-13 07:44:16.152844
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    # Initialize a vault object
    vault = VaultLib('mysecret')
    # Create an AnsibleVaultEncryptedUnicode object
    aveu = AnsibleVaultEncryptedUnicode.from_plaintext('myvalue', vault, 'mysecret')
    # Test equality with unencrypted unicode
    assert aveu.__eq__(u'myvalue')
    # Test equality with encrypted unicode
    assert aveu.__eq__(AnsibleVaultEncryptedUnicode.from_plaintext('myvalue', vault, 'mysecret'))
    # Test inequality with encrypted unicode
    assert not aveu.__eq__(AnsibleVaultEncryptedUnicode.from_plaintext('othervalue', vault, 'mysecret'))
    #

# Generated at 2022-06-13 07:44:23.026896
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    test_string = 'Now is the time for all good persons to become a programer.'
    test_string_bytes = to_bytes(test_string)

    test_password = 'my_vault_password'
    test_password_bytes = to_bytes(test_password)

    vl = VaultLib(test_password)

    avue = AnsibleVaultEncryptedUnicode.from_plaintext(test_string_bytes, vl, secret=test_password_bytes)

    assert avue.is_encrypted()
    assert avue.data == test_string

# Test the AnsibleVaultEncryptedUnicode methods that do not rely on the data

# Generated at 2022-06-13 07:44:31.773232
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class MockVault(object):
        def decrypt(self, ciphertext, obj=None):
            return 'data'

    ciphertext = 'data'
    vault = MockVault()
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(ciphertext, vault, 'secret')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(ciphertext, vault, 'secret')
    assert avu1 == avu2



# Generated at 2022-06-13 07:44:42.860849
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:44:51.445783
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')

    u = AnsibleVaultEncryptedUnicode.from_plaintext(u'TEST', vault, None)
    assert u.is_encrypted()


# Generated at 2022-06-13 07:44:54.973130
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a1 = AnsibleVaultEncryptedUnicode('foo')
    a2 = AnsibleVaultEncryptedUnicode('foo')
    assert (a1 != a2)    # Required in pytest



# Generated at 2022-06-13 07:44:59.812255
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test for scenario:
    #    Test AnsibleVaultEncryptedUnicode.__ne__ when supplied with another string.
    # Test data:
    #    supplied string: "hello"
    # Expected results:
    #    expected result: False
    avu = AnsibleVaultEncryptedUnicode("hello")
    result = avu.__ne__("hello")
    assert result == False


# Generated at 2022-06-13 07:45:10.241671
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    class MockVault(object):
        def __init__(self, cyphertext=None, plaintext=None):
            self.cyphertext = cyphertext
            self.plaintext = plaintext

        def encrypt(self, s, *args, **kwargs):
            return self.cyphertext

        def decrypt(self, s, *args, **kwargs):
            return self.plaintext

    password = unicode("password")
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", MockVault("foo"), password)
    assert avu <= "foo"
    assert "foo" <= avu
    assert avu <= "bar"
    assert "bar" <= avu
    assert "bar" <= "foo"


# Generated at 2022-06-13 07:45:40.793225
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(b"foobar", VaultLib(b"foobar"), b"lol")

    assert avu.is_encrypted()

    avu = AnsibleVaultEncryptedUnicode("foobar")
    assert not avu.is_encrypted()

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(b"foobar", False, b"lol")
    assert not avu.is_encrypted()

    avu._ciphertext = b"foobar"
    assert not avu.is_encrypted()


# The following constants are used with the AnsibleSafeLoader.
#
# ANSIBLE_SAFE_LOADERS_BY_TAG - a list representing the loader to use for each

# Generated at 2022-06-13 07:45:49.277703
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create AnsibleVualtEncryptedUnicode object
    avu = AnsibleVaultEncryptedUnicode('test')

    # Create and set vault
    vault = yaml.vault.VaultLib(yaml.vault.VaultLib.ALGORITHMS[0])
    avu.vault = vault

    # Create equal AnsibleVaultEncryptedUnicode object
    avu2 = AnsibleVaultEncryptedUnicode('test')
    avu2.vault = vault

    # Check that __eq__ works
    assert avu == avu2

if __name__ == "__main__":
    test_AnsibleVaultEncryptedUnicode___eq__()

# Generated at 2022-06-13 07:45:57.689962
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword

    secret = VaultSecret('secret', 'password')
    vault = VaultLib([secret])
    plaintext = 'plaintext'
    ciphertext = vault.encrypt(plaintext, secret)
    vaultedtext = AnsibleVaultEncryptedUnicode(ciphertext)
    vaultedtext.vault = vault

    assert vaultedtext.is_encrypted()

    plain_vaultedtext = AnsibleVaultEncryptedUnicode(plaintext)
    plain_vaultedtext.vault = vault

    assert not plain_vaultedtext.is_encrypted()


# Generated at 2022-06-13 07:46:04.032280
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    testcases = [('foo', 'foo', True), ('bar', 'foo', False), (5, 'foo', False)]

    for p, q, expected in testcases:
        q = AnsibleVaultEncryptedUnicode.from_plaintext(q, vault=vault, secret='secret')
        assert q.__eq__(p) == expected
        assert q == p == expected


# Generated at 2022-06-13 07:46:04.950806
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert ansible_vault_encrypted_unicode___eq__() == 'OK'


# Generated at 2022-06-13 07:46:11.104654
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # ToDo: Add unit tests to test if decryption works as expected
    secret = "This is my secret."

# Generated at 2022-06-13 07:46:25.760541
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    import sys


    if sys.version_info < (3,):
        assert AnsibleVaultEncryptedUnicode(b"ASDQWE123456axc_asd").__ne__("ASDQWE123456") == True
        assert AnsibleVaultEncryptedUnicode(b"ASDQWE123456").__ne__("ASDQWE123456") == False
        assert AnsibleVaultEncryptedUnicode(b"ASDQWE123456").__ne__("ASDQWE123456axc_asd") == True

# Generated at 2022-06-13 07:46:35.386050
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from __main__ import vault_secrets
    from ansible.vault import VaultLib
    vault = VaultLib(vault_secrets)
    p1 = vault.encrypt("qwerty")
    p2 = vault.encrypt("asdfgh")
    p3 = vault.encrypt("qwerty")
    s1 = AnsibleVaultEncryptedUnicode(p1)
    s1.vault = vault
    s2 = AnsibleVaultEncryptedUnicode(p2)
    s2.vault = vault
    s3 = AnsibleVaultEncryptedUnicode(p3)
    s3.vault = vault
    assert s1 != s2
    assert s1 != s3
    assert s2 != s3

# Generated at 2022-06-13 07:46:46.933796
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = VaultLib('foo')
    secret = 'bar'

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)
    avu3 = AnsibleVaultEncryptedUnicode('foo')
    avu4 = AnsibleVaultEncryptedUnicode.from_plaintext('not this', vault, secret)
    s = 'foo'

    # equal
    assert avu1 == avu2 == s
    assert not avu1 == avu3
    assert not avu1 == avu4
    assert not avu1 == 'bar'
    assert not avu3 == 'bar'

    # not equal
    assert avu1 != avu3
   

# Generated at 2022-06-13 07:46:59.585653
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    expected = True

# Generated at 2022-06-13 07:47:40.619091
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    import base64
    import pickle

    secret = 'test'
    plaintext = to_text('''
    ---
    a: "foo"
    b: "bar"
    c: "baz"
    ''')

    # base64 encoded vault.AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 07:47:50.662186
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible import vault
    # test if is false when object not encrypted
    avu = AnsibleVaultEncryptedUnicode("foo")
    assert not avu.__eq__("foo")
    # test if is false when object is not equal
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", vault.AES256VaultLib("hunter2"), "pass")
    assert not avu.__eq__("bar")
    # test if is true when object is equal
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", vault.AES256VaultLib("hunter2"), "pass")
    assert avu.__eq__("foo")

# Generated at 2022-06-13 07:47:57.907702
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Testing AnsibleVaultEncryptedUnicode
    ac = AnsibleVaultEncryptedUnicode("test")
    ac.vault = yaml.reader.Reader()
    ac.vault.vault.vault_id = "test_id"
    ac.vault.vault.load(str("test_password"))
    ac.vault.vault.is_encrypted = lambda a: False
    ac.vault.vault.decrypt = lambda a, b: "test"
    assert "abcd" != ac


# Generated at 2022-06-13 07:48:05.667239
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Trivial test code used to test the __ne__ method of class AnsibleVaultEncryptedUnicode
    #
    # Because the __ne__ method is a class method, we must first create an
    # instance of the class, before we can call the __ne__ method.

    # Because we are testing a class method, we need to import the
    # AnsibleVaultEncryptedUnicode class from the ansible.parsing.yaml.objects
    # module.
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Create a AnsibleVaultEncryptedUnicode instance
    avu = AnsibleVaultEncryptedUnicode('encrypted_text')

    # Test the __ne__ method
    assert(not avu.__ne__('encrypted_text'))
   

# Generated at 2022-06-13 07:48:14.931790
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import unittest
    from ansible.parsing.vault import VaultLib

    class TestAnsibleVaultEncryptedUnicode(unittest.TestCase):

        def setUp(self):
            pass
    
        def tearDown(self):
            pass

        def test___eq__(self):
            avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'TestUnicodeObject', VaultLib(password='vault_pass'), secret=None)
            self.assertEqual(avu, u'TestUnicodeObject')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnsibleVaultEncryptedUnicode)
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-13 07:48:24.569941
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    secret = 'foobar'
    vault = VaultLib(secret)

    unencrypted_text = 'spam'
    unenc_avu = AnsibleVaultEncryptedUnicode(unencrypted_text)
    unenc_avu.vault = vault
    assert not unenc_avu.is_encrypted()

    enc_avu = AnsibleVaultEncryptedUnicode.from_plaintext('eggs', vault, secret)
    assert enc_avu.is_encrypted()

# Generated at 2022-06-13 07:48:30.323832
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
  assert AnsibleVaultEncryptedUnicode.from_plaintext(u'foo', vault=None, secret=None) != 'bar'
  assert AnsibleVaultEncryptedUnicode.from_plaintext(u'foo', vault=None, secret=None) != None


# Generated at 2022-06-13 07:48:34.084713
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'test')
    assert(avu.__ne__('test'))
    assert(not avu.__ne__('foo'))
