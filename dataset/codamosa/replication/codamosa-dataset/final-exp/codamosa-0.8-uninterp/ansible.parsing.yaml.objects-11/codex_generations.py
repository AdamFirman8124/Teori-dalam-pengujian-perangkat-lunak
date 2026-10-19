

# Generated at 2022-06-13 07:38:57.022143
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    import os
    vault_password = os.getenv('ANSIBLE_VAULT_PASSWORD')
    if vault_password is None:
        return
    vault = VaultLib(vault_password)
    avu1 = AnsibleVaultEncryptedUnicode(vault.encrypt('foobar'))
    avu2 = AnsibleVaultEncryptedUnicode(vault.encrypt('foobar'))
    assert avu1.__ne__(avu2)



# Generated at 2022-06-13 07:39:07.945446
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    vaultenc = AnsibleVaultEncryptedUnicode('vault-test')
    assert vaultenc < 'vault-test-1'
    assert not (vaultenc < 'vault-test')
    assert not (vaultenc < 'vault-test-')
    assert not (vaultenc < 'vault-testy')
    assert not (vaultenc < '')
    vaultenc2 = AnsibleVaultEncryptedUnicode('vault-test2')
    assert vaultenc < vaultenc2
    assert not (vaultenc < vaultenc)
    assert not (vaultenc < AnsibleVaultEncryptedUnicode('vault-test-2'))
    assert not (vaultenc2 < vaultenc)



# Generated at 2022-06-13 07:39:21.801594
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    v = VaultLib('mypass')
    plaintext = 'text'

# Generated at 2022-06-13 07:39:29.223122
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError

    vault = VaultLib('hello')
    secret = 'my secret password'

    # Test empty text
    try:
        avu = AnsibleVaultEncryptedUnicode(u'')
        assert False, "AnsibleVaultEncryptedUnicode should not accept an empty string"
    except AnsibleVaultError:
        assert True

    # Test encrypted string
    avu = AnsibleVaultEncryptedUnicode(vault.encrypt(to_bytes('my string'), secret))
    assert avu.is_encrypted() == True

    # Test unencrypted string
    avu = AnsibleVaultEncryptedUnicode('my string')
    assert avu.is_encrypted() == False

# Generated at 2022-06-13 07:39:41.527720
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    key = b'\x00\x01'
    secret = b'\x03\x04'
    data = u'vault test'

# Generated at 2022-06-13 07:39:49.982113
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault1 = VaultLib('password1')
    vault2 = VaultLib('password2')

    # When only ciphertext is given, vault object is not set.
    avu1 = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.2;AES256;default\n323531623339616663633765613236643461396132626563633432393932316264653133666633\n306438626331393938336162333665636261626233306635386130666335373635336130643837\n39367d0a")
    assert avu1.is_encrypted() == True


# Generated at 2022-06-13 07:39:52.574923
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    ansible_vault = AnsibleVaultEncryptedUnicode(b'DUMMY DATA')
    assert(ansible_vault.is_encrypted())



# Generated at 2022-06-13 07:40:03.201180
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.plugins.vault.VaultLib as vault


# Generated at 2022-06-13 07:40:09.235767
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # A test case for testing __ne__ method of AnsibleVaultEncryptedUnicode.
    # Arrange
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('1234')
    # Act
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('secret', vault, '1234')
    # Assert
    assert avu != 'secret'


# Generated at 2022-06-13 07:40:17.427717
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('N.C')

# Generated at 2022-06-13 07:40:33.451140
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:35.789355
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avue = AnsibleVaultEncryptedUnicode('ciphertext')
    string = 'test'
    assert avue != string


# Generated at 2022-06-13 07:40:42.054396
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    try:
        import ansible.parsing.vault
    except ImportError:
        return

    avueu = AnsibleVaultEncryptedUnicode.from_plaintext("123", ansible.parsing.vault.VaultLib("1"), "pwd")
    assert (avueu != "123")
    assert (avueu.data == "123")

# Lookup dict for AnsibleVaultEncryptedUnicode.from_plaintext()

# Generated at 2022-06-13 07:40:47.416803
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')
    str1 = AnsibleVaultEncryptedUnicode.from_plaintext('some string', vault, 'password')
    str2 = AnsibleVaultEncryptedUnicode.from_plaintext('some string', vault, 'password')
    str3 = AnsibleVaultEncryptedUnicode.from_plaintext('some other string', vault, 'password')

    assert str1 != str3
    assert not str1 != str2


# Generated at 2022-06-13 07:40:57.781586
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import vault_manager
    test_avue = AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT;1.1;AES256\n623031623166623431666230353862623666613766373532343033653662373836613065313963\n613065633661373962653364623463333230386363363135623763393339326134313363653065\n6432396161643332623666323461636338636266373338393937626565356335\n')
    test_avue.vault = vault_manager.get_vault()
    assert test_avue.is_encrypted()


# Generated at 2022-06-13 07:41:04.272339
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Create AnsibleVaultEncryptedUnicode
    a = AnsibleVaultEncryptedUnicode('testing')

    # Verify that a != 'testing'
    assert a != 'testing'

    # Create AnsibleVaultEncryptedUnicode
    b = AnsibleVaultEncryptedUnicode('testing')

    # Verify that a != b
    assert a != b



# Generated at 2022-06-13 07:41:17.487898
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Py2 doesn't complain about comparing a unicode with a byte string
    # Py3 complains about it.
    # We're trying to emulate Py3 behaviour.
    uni = AnsibleVaultEncryptedUnicode(b'abc')
    bstr = b'abc'
    if uni != bstr:
        pass
    else:
        raise AssertionError("Failed AnsibleVaultEncryptedUnicode test")

    # Py2: x != u'abc'
    # Py3: b'x' != 'abc'
    uni = AnsibleVaultEncryptedUnicode(b'x')
    bstr = b'abc'
    if uni != bstr:
        pass
    else:
        raise AssertionError("Failed AnsibleVaultEncryptedUnicode test")


# Generated at 2022-06-13 07:41:28.999124
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    print ('test_AnsibleVaultEncryptedUnicode__eq__', end=' ')
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('abcd')
    # AnsibleVaultEncryptedUnicode("!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          37643433313661663735663934623661376165663835386536363533666531643861613633636465\n          36633136613137346630356534396163386234396233323063303839343538626132316662353630\n          38313639633930383462623164380a31356534396537643666303566323933623265393035656235\

# Generated at 2022-06-13 07:41:35.524626
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import hvac
    vault = hvac.vault.VaultClient(url='http://localhost:8200', token='foo')
    secret = 'bar'

    # Test with non vault encrypted value
    seq1 = 'hello world'
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(seq1, vault, secret)
    assert avu1.is_encrypted() is False

    # Test with vault encrypted value
    seq2 = 'secret'
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(seq2, vault, secret)
    assert avu2.is_encrypted() is True


# Generated at 2022-06-13 07:41:45.242451
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    cipher_text = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          3533333834633861383139313331316338383764366231646236313932623965643939623862336531330a\n          65656134326633633665353464383638663532656130326533356237323033373365303661303731306537\n          3066393730663735\n"
    str_val = 'foo'
    avu = AnsibleVaultEncryptedUnicode(cipher_text)
    assert avu != str_val


# Generated at 2022-06-13 07:41:57.461444
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import AnsibleVaultError

    vaultSecret = VaultSecret("password")
    vault = VaultLib([vaultSecret])

    # Test with a AnsibleVaultEncryptedUnicode object
    seq = u'test_data'
    avue1 = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault=vault, secret=vaultSecret)
    avue2 = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault=vault, secret=vaultSecret)
    assert avue1 != avue2


# Generated at 2022-06-13 07:42:08.536669
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import tempfile
    import os
    from ansible.parsing.vault import VaultLib

    # create a temporary file for test
    [handle_fd, handle_path] = tempfile.mkstemp()
    os.close(handle_fd)

    # create VaultLib object
    temp_password = 'temporary password'
    vault = VaultLib(temp_password)

    # test encrypted
    icecream = "Chocolate Chip"
    encrypt_icecream = AnsibleVaultEncryptedUnicode.from_plaintext(icecream, vault, temp_password)
    assert encrypt_icecream.__eq__(icecream)
    assert encrypt_icecream.data == icecream

    # test unencrypted
    encrypt_icecream = AnsibleVaultEncryptedUnicode(icecream)
    assert not encrypt_icecream.__

# Generated at 2022-06-13 07:42:14.749014
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode('')
    avu.vault = FakeVault('FakeVault')

    # test avu:
    assert avu == avu.data

    # test unicode:
    assert avu == 'FakeVault'

    # test bytestring
    assert avu == to_bytes('FakeVault')

    # test int
    assert not avu == 123


# Generated at 2022-06-13 07:42:16.718370
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode('') != b'abc'
    assert AnsibleVaultEncryptedUnicode('abc') != b'abc'



# Generated at 2022-06-13 07:42:25.263358
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:35.514553
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # This encrypts plaintext_string using secret_string and a vault object from vaultlib
    plaintext_string = b'This is a plain text string'
    secret_string = b'thisisasecretkey12'
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(secret_string)
    ciphertext_string = vault.encrypt(plaintext_string)

    # First, test with a version of the ciphertext that has been mangled.
    # This mangled ciphertext should be considered not encrypted.
    # It's mangled by writing the bytes at offset 24 with new bytes (0x41).
    mangled_ciphertext_string = ciphertext_string[:24] + b'AAAA' + ciphertext_string[28:]

# Generated at 2022-06-13 07:42:43.972714
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    test_str = 'test'

    # Create AnsibleVaultEncryptedUnicode object
    foo = AnsibleVaultEncryptedUnicode(test_str)

    # Create list as value to compare
    test_list = []
    assert foo != test_list, 'Failed match between AnsibleVaultEncryptedUnicode and empty list'

    # Create dict as value to compare
    test_dict = {}
    assert foo != test_dict, 'Failed match between AnsibleVaultEncryptedUnicode and empty dict'

    # Create tuple as value to compare
    test_tuple = ()
    assert foo != test_tuple, 'Failed match between AnsibleVaultEncryptedUnicode and empty tuple'

    # Create set as value to compare
    test_set = set()

# Generated at 2022-06-13 07:42:54.647729
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''AnsibleVaultEncryptedUnicode.__eq__ should return True or False'''

    # class AnsibleVaultEncryptedUnicode
    # def __eq__(self, other):
    #     if self.vault:
    #         return other == self.data
    #     return False
    #
    # return other == self.data
    # return other.decrypted == self.decrypted
    # return other.decrypted == self.decrypted


    # Tests:
    #   AnsibleVaultEncryptedUnicode.__eq__(self, other)
    #   * when self.vault:
    #     * self.data == other
    #     * other.decrypted == self.decrypted
    #   * when not self.vault:
    #     False
    #   * when

# Generated at 2022-06-13 07:43:06.592759
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # create a vault for testing
    vault = VaultLib([])

    # generate some plaintext/ciphertext
    secret = 'test'
    plaintext = 'plaintext'
    ciphertext = vault.encrypt(plaintext, secret)
    assert ciphertext != plaintext

    # create an AnsibleVaultEncryptedUnicode with ciphertext content
    avue = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avue.is_encrypted()
    assert avue.data == plaintext

    # create an AnsibleVaultEncryptedUnicode with plaintext content
    avue = AnsibleVaultEncryptedUnicode(plaintext)
    assert not avue.is_encrypted()
    assert avue.data == plaintext

# Unit test

# Generated at 2022-06-13 07:43:17.458744
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    passphrase = 'this is a password'
    vault = VaultLib(passphrase=passphrase)
    secret = 'this is a secret'

    ciphertext = to_bytes(vault.encrypt(to_bytes('this is a plaintext'), secret))
    ciphertext2 = to_bytes(vault.encrypt(to_bytes('this is a plaintext2'), secret))
    ciphertext3 = to_bytes(vault.encrypt(to_bytes('this is a plaintext'), secret))

    avu1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext2)
    avu3 = AnsibleVaultEncryptedUnicode(ciphertext3)

    assert not av

# Generated at 2022-06-13 07:43:32.241935
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('my_secret')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'a', vault, 'my_secret')
    assert avu != 'a'

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'', vault, 'my_secret')
    assert avu != 'a'

    assert '' != avu == 'a'



# Generated at 2022-06-13 07:43:41.427600
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib('123')

    # Test passing a string object
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, '123')
    assert avu1 == 'test'
    assert avu1 != 'tesT'

    # Test passing another AnsibleVaultEncryptedUnicode object with the same plaintext
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, '123')
    assert avu1 == avu2
    assert avu1 != 'tESt'

    # Test passing another AnsibleVaultEncryptedUnicode object with different plaintext

# Generated at 2022-06-13 07:43:54.429602
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault_mod
    vault = vault_mod.VaultLib([])
    secret = '$ANSIBLE_VAULT;1.2;AES256;test.vault\n31323334353637383930313233343536373839303132333435363738393031323334353637383930\n31323334353637383930313233343536373839303132333435363738393031323334353637383930\n31323334353637383930313233343536373839303132333435363738393031323334353637383930\n'
    secret = secret.encode('utf8')
    avu = AnsibleVaultEncryptedUnicode.from_plain

# Generated at 2022-06-13 07:44:01.193330
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # Test fixture from fixtures/vault_fixture.yaml

# Generated at 2022-06-13 07:44:09.653704
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # import here to prevent circular import
    from ansible.parsing.vault.vault import VaultLib

    secret = 'test'
    vault = VaultLib('!')
    test_str = 'test'

    # Test string that is not encrypted
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(test_str, vault, secret)
    assert avu.is_encrypted() is False

    # Test string that is encrypted
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(test_str, vault, secret)
    assert avu.is_encrypted() is False


# ==============================================================
# YAML Loader/Dumper
# ==============================================================


# Generated at 2022-06-13 07:44:15.968532
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib("mysecret")
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", vault, "mysecret")
    assert isinstance(avu, AnsibleVaultEncryptedUnicode)
    assert avu.data == "foo"
    assert avu != "foo"
    assert avu != "bar"
    assert "bar" != avu
    assert "foo" != avu



# Generated at 2022-06-13 07:44:23.425879
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault

    plaintext = 'my secret'
    secret = 'my secret'
    ciphertext = ansible.parsing.vault.VaultLib('1.1').encrypt(plaintext, secret)

# Generated at 2022-06-13 07:44:29.311447
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(password='ansible', identifier=None)
    value = AnsibleVaultEncryptedUnicode.from_plaintext("some_secret", vault, "test")
    assert value.is_encrypted()



# Generated at 2022-06-13 07:44:33.072614
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    obj = AnsibleVaultEncryptedUnicode(u'this is a test')
    assert not obj.__ne__(u'this is a test')


# Generated at 2022-06-13 07:44:43.592856
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    HEX_SECRET = '8d3caf2d6f71c6f190ae3a27e9de1df6d74c0158b2f8b98d0b7bc16c1f40149f'

# Generated at 2022-06-13 07:45:01.690442
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'pass'
    v = VaultLib(secrets=[secret])
    plaindata = to_bytes('foobar')
    plaintext = AnsibleVaultEncryptedUnicode(plaindata)
    plaintext.vault = v
    ciphertext = v.encrypt(plaindata, secret)
    ciphertext = AnsibleVaultEncryptedUnicode(ciphertext)
    ciphertext.vault = v
    # unencrypted data is not encrypted
    assert not plaintext.is_encrypted()
    # encrypted data is encrypted
    assert ciphertext.is_encrypted()
    # plain text data is unencrypted
    assert not plaintext.data.is_encrypted()
    # decrypted cipher text data is unencrypted
    assert not ciphertext.data.is_encrypted()


# Generated at 2022-06-13 07:45:11.697245
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    Test method __ne__ of class AnsibleVaultEncryptedUnicode

    :return:
    '''

    from ansible.parsing.vault import VaultLib
    import random
    import os
    import string

    os.environ['ANSIBLE_VAULT_PASSWORD_FILE'] = './test/unittests/vault_passtest'

    clear_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
    vault = VaultLib(password_file='./test/unittests/vault_passtest')
    vault_str = AnsibleVaultEncryptedUnicode.from_plaintext(clear_str, vault, None)

    # test string comparison

# Generated at 2022-06-13 07:45:16.472230
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Test method __eq__ from class AnsibleVaultEncryptedUnicode
    """
    avu = AnsibleVaultEncryptedUnicode("some text")
    assert avu.__eq__("some text")
    assert not avu.__eq__("other text")
    assert not avu.__eq__("")

    avu = AnsibleVaultEncryptedUnicode("")
    assert not avu.__eq__("some text")
    assert not avu.__eq__("other text")
    assert avu.__eq__("")



# Generated at 2022-06-13 07:45:18.792524
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    my_test = AnsibleVaultEncryptedUnicode('test')
    assert my_test == 'test'


# Generated at 2022-06-13 07:45:27.782990
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = 'my_secret'

# Generated at 2022-06-13 07:45:39.192648
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Case 1: Check that none of the two arguments is None
    avue = AnsibleVaultEncryptedUnicode(b'plaintext')
    assert avue != None                                                                              # pylint: disable=singleton-comparison

    # Case 2: Check that none of the two arguments is False
    assert avue != False                                                                             # pylint: disable=singleton-comparison

    # Case 3: Check that none of the two arguments is True
    assert avue != True                                                                              # pylint: disable=singleton-comparison

    # Case 4: Check that only one argument is empty string
    assert avue != ''

    # Case 5: Check that none of the two arguments is 0
    assert avue != 0

    # Case 6: Check that only one argument is empty list

# Generated at 2022-06-13 07:45:48.303310
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import os, tempfile
    try:
        import vault
    except ImportError:
        print('skipping test_AnsibleVaultEncryptedUnicode___ne__, cannot import vault')
        return

    plain_text = 'some vaulted password'
    number = 3

    tmp_dir = tempfile.mkdtemp()
    vault_file = os.path.join(tmp_dir, 'vault.yml')
    secret_file = os.path.join(tmp_dir, 'secret.txt')

    for action in ('create', 'reencrypt', 'encrypt', 'decrypt'):
        if action == 'create':
            if os.path.exists(vault_file):
                os.unlink(vault_file)
            if os.path.exists(secret_file):
                os.unlink

# Generated at 2022-06-13 07:45:55.291851
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # GIVEN
    text = "[defaults]\n"
    text += "hostfile = /etc/ansible/hosts\n"
    text += "roles_path = /etc/ansible/roles:/usr/share/ansible/roles\n"
    text += "library = c:\windows\system32\ansible\library"
    text += "\n"
    aveu = AnsibleVaultEncryptedUnicode(text)

    # WHEN
    result = aveu.is_encrypted()

    # THEN
    assert(result == True)



# Generated at 2022-06-13 07:46:07.187461
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    v = VaultLib("testing")

# Generated at 2022-06-13 07:46:20.428939
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    vault = VaultLib(password='blah')
    text = "this is some plaintext"
    ciphertext = vault.encrypt(text)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted()

    text = "this is some plaintext"
    ciphertext = vault.encrypt(text)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = None
    assert not avu.is_encrypted()


# A YAML representer for AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:46:42.975535
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode('test') != AnsibleVaultEncryptedUnicode('test')
    assert AnsibleVaultEncryptedUnicode('test') != 'test'


# Generated at 2022-06-13 07:46:51.039973
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    if hasattr(sys, 'gettrace'):
        # skip this if we're not testing the installed version of Ansible
        return
    from ansible.parsing.vault import VaultLib
    v = VaultLib([])
    passphrase = b'passphrase' # b'' if you want to disable passphrase
    iv = b'1234567890abcdef'
    p = v.encrypt(b'secret', passphrase, iv, b'sha256')
    a = AnsibleVaultEncryptedUnicode(p)
    a.vault = v
    assert(a != 'secret')

    k = v.decrypt(p, passphrase=passphrase, iv=iv)
    assert(k == b'secret')


# Generated at 2022-06-13 07:47:02.244182
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    my_vault = VaultLib('12345')
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('asd', my_vault, '1234')
    assert(avu1 == 'asd')
    assert(avu1.data == 'asd')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('qwe', my_vault, '1234')
    assert(avu2 != 'asd')
    assert(avu2.data != 'asd')
    assert(avu1 == avu1)
    assert(avu2 != avu1)
    assert(avu2 == avu2)


# Generated at 2022-06-13 07:47:07.377699
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create a test sequence
    seq = AnsibleVaultEncryptedUnicode('string')
    # Check that when vault is set it correctly returns
    # the value after decrypting
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('vault password')
    seq.vault = vault
    assert seq == 'string'
    # Check that when vault is NOT set it returns False
    seq.vault = None
    assert seq == False


# Generated at 2022-06-13 07:47:14.812662
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class Dummy:
        def decrypt(self, ciphertext, obj=None):
            return ciphertext

    class Dummy2:
        def decrypt(self, ciphertext, obj=None):
            return None

    avu = AnsibleVaultEncryptedUnicode
    avu.vault = Dummy()
    avu.data = 'abc'
    assert avu() != 'abc'

    avu.vault = Dummy2()
    avu.data = 'abc'
    assert avu() != 'abc'

    avu.vault = None
    avu.data = 'abc'
    assert avu() != 'abc'



# Generated at 2022-06-13 07:47:25.363471
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create an initial AnsibleVaultEncryptedUnicode object
    test_string_initial = 'this is a test'
    avu_initial = AnsibleVaultEncryptedUnicode(test_string_initial)
    assert avu_initial == test_string_initial

    # Create a second AnsibleVaultEncryptedUnicode object
    test_string_second = 'this is a test'
    avu_second = AnsibleVaultEncryptedUnicode(test_string_second)
    assert avu_second == test_string_second

    # The two AnsibleVaultEncryptedUnicode objects are not equal yet because the .vault attribute has not been set.
    assert avu_initial != avu_second

    # Set the .vault attribute of the ansible vault objects

# Generated at 2022-06-13 07:47:36.969202
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.vault
    vault = ansible.vault.VaultLib('abcdef')
    unencrypted = 'unencrypted string'

# Generated at 2022-06-13 07:47:47.104805
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Check equality and inequality with plain strings
    a = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=None, secret=None)
    assert( 'test' == a )
    assert( 'notest' != a)

    try:
        # Check against a string that is not equal
        assert( 'notest' == a )
    except AssertionError:
        pass
    else:
        raise AssertionError('Expected AssertionError')
    finally:
        pass

    try:
        # Check against a string that is not equal
        assert( 'test' != a )
    except AssertionError:
        pass
    else:
        raise AssertionError('Expected AssertionError')
    finally:
        pass



# Generated at 2022-06-13 07:47:51.307670
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.vault
    vault = ansible.vault.VaultLib('vaultpassword')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'vaultpassword')
    assert(avu == 'test')



# Generated at 2022-06-13 07:47:56.992255
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ae = AnsibleVaultEncryptedUnicode('test')
    ae.vault = None
    assert ae != 'test'
    ae.vault = 'test'
    assert ae == 'test'
    ae2 = AnsibleVaultEncryptedUnicode('test')
    ae2.vault = 'test'
    assert ae != ae2
