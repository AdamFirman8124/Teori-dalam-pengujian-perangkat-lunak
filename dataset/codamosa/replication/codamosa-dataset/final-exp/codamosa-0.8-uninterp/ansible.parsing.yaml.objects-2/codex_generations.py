

# Generated at 2022-06-13 07:38:50.967405
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    from ansible.parsing.vault import VaultLib
    valt = VaultLib(None)
    cphr = valt.encrypt('some text')
    avu = AnsibleVaultEncryptedUnicode(cphr)
    avu.vault = valt
    # test with unicode
    assert 'text' in avu
    assert not 'TEXT' in avu
    # test with byte string
    assert b'text' in avu
    assert not b'TEXT' in avu
    # test with AnsibleVaultEncryptedUnicode
    avu2 = AnsibleVaultEncryptedUnicode(b'some text')
    assert avu2 in avu
    avu2 = AnsibleVaultEncryptedUnicode(b'SOME TEXT')
    assert not avu2 in avu


# Generated at 2022-06-13 07:38:53.429552
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    data = "this is a test"
    avu = AnsibleVaultEncryptedUnicode(data)
    avu.vault = 'test'
    assert not avu.is_encrypted()



# Generated at 2022-06-13 07:39:03.751459
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    s = '\u0411\u0440\u0430\u0442\u0430\u043d\u0441\u043a\u0430\u044f \u0440\u0443\u0441\u044c'
    # Create an AnsibleVaultEncryptedUnicode instance
    avue = AnsibleVaultEncryptedUnicode(s)

    # Create a AnsibleVaultEncryptedUnicode instance that is smallest unit for
    # method __contains__ of class AnsibleVaultEncryptedUnicode.
    s_avue = AnsibleVaultEncryptedUnicode(s[0])

    assert(s_avue in avue)


# Generated at 2022-06-13 07:39:13.968813
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    # Test that the return value is correct for different types of input
    cip = AnsibleVaultEncryptedUnicode(b'foo')
    assert cip.__contains__(u'foo')
    assert cip.__contains__('foo')
    assert cip.__contains__(u'oo')
    assert cip.__contains__('oo')
    assert cip.__contains__(u'f')
    assert cip.__contains__('f')
    assert cip.__contains__(u'o')
    assert cip.__contains__('o')
    assert cip.__contains__(u'bar') == False
    assert cip.__contains__('bar') == False
    assert cip.__contains__(u'b') == False
    assert cip

# Generated at 2022-06-13 07:39:21.862224
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault
    import ansible.parsing.yaml.loader as loader

# Generated at 2022-06-13 07:39:27.762276
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    assert AnsibleVaultEncryptedUnicode('!vault |$ANSIBLE_VAULT;1.2;AES256;foo\nbar')[0].find('!') == 0
    assert AnsibleVaultEncryptedUnicode('!vault |$ANSIBLE_VAULT;1.2;AES256;foo\nbar')[0].find('$') == 6
    assert AnsibleVaultEncryptedUnicode('!vault |$ANSIBLE_VAULT;1.2;AES256;foo\nbar')[0].find('\n') == 23



# Generated at 2022-06-13 07:39:32.492344
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    vault_pass = 'secret'
    content = '$ANSIBLE_VAULT;1.2;AES256;ansible\n' + '64653565643334306466353733336431356564663338646565306434303866653663666230303734\n' + '3234626262316664306236346437373533323036353932646536303666356533396137326665386261\n' + '6538656135313336633264326439356366636331366231613832626262323935623963323361663764\n' + '356537663730\n' + 'vault_test_cipher'

# Generated at 2022-06-13 07:39:34.605373
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    obj = AnsibleVaultEncryptedUnicode("abcd")
    assert obj[0:1] == "a"

# Generated at 2022-06-13 07:39:43.363867
# Unit test for method __ge__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ge__():
    assert AnsibleVaultEncryptedUnicode.__ge__('', '') == '' >= ''
    assert AnsibleVaultEncryptedUnicode.__ge__('', 'a') == '' >= 'a'
    assert AnsibleVaultEncryptedUnicode.__ge__('a', '') == 'a' >= ''
    assert AnsibleVaultEncryptedUnicode.__ge__('a', 'a') == 'a' >= 'a'
    assert AnsibleVaultEncryptedUnicode.__ge__('a', 'b') == 'a' >= 'b'
    assert AnsibleVaultEncryptedUnicode.__ge__('b', 'a') == 'b' >= 'a'



# Generated at 2022-06-13 07:39:45.806787
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    assert AnsibleVaultEncryptedUnicode.from_plaintext("test","test_vault","test_secret").rfind("test") == 0


# Generated at 2022-06-13 07:40:03.294837
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    """
    Create an AnsibleVaultEncryptedUnicode object and test the AnsibleVaultEncryptedUnicode.rfind().
    """

    # create an AnsibleVaultEncryptedUnicode object
    avu = AnsibleVaultEncryptedUnicode("abcdef")

    try:
        # test the rfind() method
        rfind_result = avu.rfind("c")
        if (rfind_result != 2):
            raise Exception("AnsibleVaultEncryptedUnicode.rfind test failed")

    except Exception as err:
        # print the error message and exit
        print("unit test [test_AnsibleVaultEncryptedUnicode_rfind] caught exception: " + str(err))
        raise


# Generated at 2022-06-13 07:40:12.256458
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    assert AnsibleVaultEncryptedUnicode("abc")[:-1] == "ab"
    assert AnsibleVaultEncryptedUnicode("abc")[-1] == "c"
    assert AnsibleVaultEncryptedUnicode("abc")[1:] == "bc"
    assert AnsibleVaultEncryptedUnicode("abc")[-2:] == "bc"
    assert AnsibleVaultEncryptedUnicode("abc")[2:2] == ""
    assert AnsibleVaultEncryptedUnicode("abc")[:-1] == "ab"
    assert AnsibleVaultEncryptedUnicode("abc")[-1] == "c"


# Generated at 2022-06-13 07:40:26.406024
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ''' this test verifies that we return the correct value when
        different types are passed, by type I mean a regular string
        and one that is AnsibleVaultEncryptedUnicode'''
    result = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;ABCD\n1234567890abcdef1234567890abcdef\n123456789012345678901234567890123456789012\n")
    result.vault = None

    if 'a' == result:
        return False
    elif result == 'a':
        return False
    elif result != 'a':
        return True
    elif 'a' != result:
        return True
    else:
        return False



# Generated at 2022-06-13 07:40:34.496841
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:42.411220
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode("").is_encrypted() == False
    assert AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256;ansible-vault\n123456789").is_encrypted() == True
    assert AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;AES256;ansible-vault\n").is_encrypted() == False
    assert AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1;AES256;ansible-vault\n").is_encrypted() == True


# Generated at 2022-06-13 07:40:53.246782
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu_a = AnsibleVaultEncryptedUnicode(u'abc')
    avu_z = AnsibleVaultEncryptedUnicode(u'xyz')
    avu_n = AnsibleVaultEncryptedUnicode(u'123')

    assert not avu_a == avu_z
    assert avu_a != avu_z

    assert not avu_a == avu_n
    assert avu_a != avu_n

    assert not avu_z == avu_n
    assert avu_z != avu_n



# Generated at 2022-06-13 07:40:56.440807
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    p = 'plaintext'
    y = AnsibleVaultEncryptedUnicode.from_plaintext(p, AnsibleVaultLib(), b'plaintext-pass')
    assert y == p



# Generated at 2022-06-13 07:41:01.456795
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange

    # Act
    #   Method
    res = AnsibleVaultEncryptedUnicode.__ne__(None)
    #   Reference
    ref = False

    # Assert
    assert res is ref



# Generated at 2022-06-13 07:41:14.110616
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.parsing.vault import VaultEditor
    secret = 'password'
    plaintext_seq = '0123456789'
    plaintext_seq_expected1 = '456789'
    plaintext_seq_expected2 = '0123456789'

    seq = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext_seq, VaultEditor(password_file=None), secret)

    assert isinstance(seq, AnsibleVaultEncryptedUnicode)

    assert seq.data == plaintext_seq
    assert seq[4:] == plaintext_seq_expected1
    assert seq[:10] == plaintext_seq_expected2


# Generated at 2022-06-13 07:41:21.769531
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = VaultLib(password='password')
    cleartext = "hunter2"
    avu = AnsibleVaultEncryptedUnicode(vault.encrypt(cleartext))
    result = avu.__eq__(cleartext)
    assert(result)

    cleartext = "hunter3"
    result = avu.__eq__(cleartext)
    assert(result is False)

    cleartext = "hunter2"
    avu.vault = None
    result = avu.__eq__(cleartext)
    assert(result is False)


# Generated at 2022-06-13 07:41:37.752073
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    secret1 = 'ansible'
    secret2 = 'password'

# Generated at 2022-06-13 07:41:49.463698
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib, is_encrypted

    key = '1234567890123456789012345678901234567890123456789012345678901234'
    vault_pass = 'ansible'
    plaintext = 'test'

    vault = VaultLib(key)

    ciphertext = vault.encrypt(plaintext, vault_pass)
    assert is_encrypted(ciphertext)

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu.is_encrypted()

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu.is_encrypted()

    avu.data = plaintext
    assert not avu.is_encrypted()

    avu.data = ciphertext
   

# Generated at 2022-06-13 07:41:57.282464
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = '$ANSIBLE_VAULT;1.1;AES256\n6234363136646665646331643232386532396533303865383130646338366565623465363735326430\n6134333230313363666566323034356236336466393937303466616438356564386634333339633437\n6632616266303331333131613262636335646132376164666331393938626231626136373166346639\n306435633162646263386131373635386234636364383862333432366239656539\n'

# Generated at 2022-06-13 07:42:03.317129
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange
    key = 'my_encryption_key'
    secret = key.encode()
    vault = vaultlib.VaultLib(secret)
    original = 'Hello World'
    encrypted_text = AnsibleVaultEncryptedUnicode.from_plaintext(original, vault, secret)

    # Act
    result = encrypted_text._ciphertext != original

    # Assert
    assert result


# Generated at 2022-06-13 07:42:13.545810
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault
    test_vault = vault.VaultLib(password='test_password')

    # Test with undeclared encrypted data
    test_plaintext = u'test'
    test_enc_text = test_vault.encrypt(test_plaintext)
    test_avu = AnsibleVaultEncryptedUnicode(test_enc_text)
    assert(test_avu.is_encrypted())

    # Test with declared encrypted data
    test_enc_text_declared = b'$ANSIBLE_VAULT;1.1;AES256' + test_enc_text
    test_avu = AnsibleVaultEncryptedUnicode(test_enc_text_declared)
    assert(test_avu.is_encrypted())

    # Test with undeclared

# Generated at 2022-06-13 07:42:18.309831
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode(u'')
    ansi_str = 'asdf'
    unic_str = u'asdf'
    avu_str = AnsibleVaultEncryptedUnicode(u'asdf')

    assert avu != ansi_str
    assert avu != unic_str
    assert avu != avu_str
    assert ansi_str != avu
    assert unic_str != avu
    assert avu_str != avu


# Generated at 2022-06-13 07:42:26.380034
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(
        'foo bar', vault=None, secret='secret'
    )

    # unequal
    assert avu != 'foobar'
    assert 'foobar' != avu
    assert avu != 'foo bar'
    assert 'foo bar' != avu

    # equal
    assert avu == 'foo bar'
    assert 'foo bar' == avu

    # unequal to None, as the avu is always != None
    assert avu != None
    assert None != avu

    # unequal to bool
    assert avu != False
    assert False != avu
    assert avu != True
    assert True != avu

    # unequal to other types
    assert avu != 1
    assert 1 != avu
    assert avu != 1.0
   

# Generated at 2022-06-13 07:42:35.914334
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError
    import binascii
    plaintext = u"test plain text"
    secret = "secret"
    ciphertext = plaintext.encode('utf-8')
    ciphertext = VaultLib.encrypt(VaultLib(), ciphertext, secret)
    assert(isinstance(ciphertext, bytes))
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = VaultLib()
    assert(avu.is_encrypted() == True)
    plaintext = avu.data
    assert(isinstance(plaintext, text_type))
    assert(plaintext == u"test plain text")
    ciphertext = b'\x00' * 20


# Generated at 2022-06-13 07:42:44.098572
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():

    class TestVault():
        '''
        class to mock vaultlib
        '''

        def __init__(self):
            pass

        def is_encrypted(self, data):
            if data != "vaulted":
                return True
            else:
                return False

    # test case 1: a non encrypted string
    plaintext = "not_encrypted"
    vault1 = TestVault()
    avu1 = AnsibleVaultEncryptedUnicode(plaintext)
    avu1.vault = vault1
    assert avu1.is_encrypted() == False

    # test case 2: an encrypted string
    ciphertext = "vaulted"
    vault2 = TestVault()
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault = vault2

# Generated at 2022-06-13 07:42:48.592844
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=VaultLib(password='password'), secret='password')
    assert avu.is_encrypted() == True


# Generated at 2022-06-13 07:43:08.233663
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    Test case for class AnsibleVaultEncryptedUnicode method __ne__
    '''
    test_obj_1 = AnsibleVaultEncryptedUnicode(ciphertext=b'$ANSIBLE_VAULT;1.1;AES256\n32323232323232323232323232323232323232323232323232323232323232320\n')
    test_obj_2 = AnsibleVaultEncryptedUnicode(ciphertext=b'$ANSIBLE_VAULT;1.1;AES256\n32323232323232323232323232323232323232323232323232323232323232320\n')

# Generated at 2022-06-13 07:43:17.970344
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    in_obj = AnsibleVaultEncryptedUnicode("abc")
    # out_obj = AnsibleVaultEncryptedUnicode("abc")
    # slice ranges
    start_min, start_max = 0, 7
    end_min, end_max = -3, 3
    # testing loop
    for startv in range(start_min, start_max + 1):
        for endv in range(end_min, end_max + 1):
            in_slice = slice(startv, endv)
            out_slice = in_obj.__getslice__(startv, endv)

# Generated at 2022-06-13 07:43:24.115891
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode("!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n         6261616666646433363736343130653634373566333538663833646161323337\n         6537613462323562343239333964663637663662343466353235653735363164\n         3032306532333631353831303737\n         ").is_encrypted()

# Generated at 2022-06-13 07:43:29.405734
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    sequence = 'hello'
    vault_secret = 'secret'
    vault = AnsibleVaultEncryptedUnicode.from_plaintext(sequence, VaultLib(vault_secret), vault_secret)
    assert ('hello' != vault)


# Generated at 2022-06-13 07:43:43.433496
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'secret'
    plaintext = 'plaintext'

    try:
        vault = VaultLib([])
        ciphertext = vault.encrypt(plaintext, secret)
    except Exception as e:
        raise AssertionError('Failed to construct ciphertext: %s' % e)

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted()
    assert text_type(avu) == plaintext

    avu = AnsibleVaultEncryptedUnicode(plaintext)
    assert not avu.is_encrypted()
    assert text_type(avu) == plaintext



# Generated at 2022-06-13 07:43:46.563047
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
    """
    assert AnsibleVaultEncryptedUnicode.__ne__('a', 'b')


# Generated at 2022-06-13 07:43:54.123687
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Arrange
    class FakeVaultObject:
        def __init__(self):
            self.vault_password = ""

        def encrypt(self, plaintext, secret):
            # return encrypted version of plaintext
            return plaintext + "-encrypted"

        def decrypt(self, ciphertext, obj):
            # return plaintext
            return ciphertext

        def is_encrypted(self, ciphertext):
            if ciphertext.endswith("-encrypted"):
                return True
            return False

    avu_instance = AnsibleVaultEncryptedUnicode("Hello World")
    avu_instance.vault = FakeVaultObject()

    # Act
    result = avu_instance == "Hello World"

    # Assert
    assert result is True



# Generated at 2022-06-13 07:43:56.874100
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault
    assert AnsibleVaultEncryptedUnicode.from_plaintext('test', ansible.parsing.vault.VaultLib(password=''), '') == 'test'


# Generated at 2022-06-13 07:44:07.914265
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible import errors as ans_errors
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = '$ecret'
    vault = VaultLib(secret)
    plaintext = 'plaintext'

    test_yaml_str = '%s' % (AnsibleVaultEncryptedUnicode.yaml_tag) + \
        '\n%s' % (vault.encrypt(plaintext, secret))
    # Parse the test_yaml_str
    test_dict = yaml.load(test_yaml_str, Loader=AnsibleLoader)

# Generated at 2022-06-13 07:44:10.237462
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    avue = AnsibleVaultEncryptedUnicode(b'abc')
    eq_(avue[:], avue)



# Generated at 2022-06-13 07:44:33.351482
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # this vault password is the same as the normal vault password
    # on the Jenkins node
    vault_password = "ansible"
    vault_secret = "mZtPvZt2YXJ1GZxu3htq"

# Generated at 2022-06-13 07:44:40.927271
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.parsing.vault import VaultLib

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('Foo', vault=VaultLib(None), secret=None)

    assert avu[:] == 'Foo'
    assert avu[1:2] == 'o'
    assert avu[0:] == 'Foo'
    assert avu[:1] == 'F'
    assert avu[-1:] == 'o'
    assert avu[:-1] == 'Fo'



# Generated at 2022-06-13 07:44:43.264092
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode("FAKE")
    avu.vault = DummyVault()
    assert avu != "FAKE"


# Generated at 2022-06-13 07:44:51.654802
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.utils import vault
    vault_password = 'secret'
    secret = 'supersekrit'

    # Test ansible format
    ciphertext = ('$ANSIBLE_VAULT;1.1;AES256\n'
                  '39626669633433326637666661356239313762616563376232333166636330373335646264313166\n'
                  '39656239316237336532376339663166663338616130636230326266636339626438313138643362\n'
                  '30393138373264393664663835646634396433333137656330613031613565\n')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)

# Generated at 2022-06-13 07:44:55.486258
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
  a = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
  b = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
  assert a == b


# Generated at 2022-06-13 07:45:02.532253
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''Test for method __ne__ of class AnsibleVaultEncryptedUnicode'''
    from ansible.vars import vault_lookup
    from ansible.parsing.vault import VaultLib
    vault_secret = 'password'
    cipher = vault_lookup('!vault', None, None, None, vault_secret)
    vault = VaultLib(vault_secret)
    val_encrypted = vault.encrypt(cipher, vault_secret)
    avu = AnsibleVaultEncryptedUnicode(to_bytes(val_encrypted, errors='surrogate_or_strict'))
    avu.vault = vault
    assert avu != 'password'

# Generated at 2022-06-13 07:45:05.951940
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    try:
        from ansible.parsing import vault as vaultlib
    except ImportError:
        vaultlib = None

    if not vaultlib:
        return

    vault = vaultlib.VaultLib('password')
    real = vault.encrypt('test')
    avu = AnsibleVaultEncryptedUnicode(real)
    avu.vault = vault
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:45:10.180125
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # pylint: disable=protected-access
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(b'vaulted')
    assert not ansible_vault_encrypted_unicode.vault
    assert ansible_vault_encrypted_unicode._ciphertext == b'vaulted'
    assert not ansible_vault_encrypted_unicode._data
    assert not ansible_vault_encrypted_unicode.data
    assert ansible_vault_encrypted_unicode.__eq__('vaulted') == False



# Generated at 2022-06-13 07:45:15.952735
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault1 = VaultLib('secret')
    vault2 = VaultLib('secret')
    secret = 'secret'

    plaintext1 = vault1.encrypt('hello', secret)
    plaintext2 = vault2.encrypt('hello', secret)
    assert AnsibleVaultEncryptedUnicode.from_plaintext(plaintext1, vault1, secret) == AnsibleVaultEncryptedUnicode.from_plaintext(plaintext2, vault2, secret)
    assert not AnsibleVaultEncryptedUnicode.from_plaintext(plaintext1, vault1, secret) == 'hello'



# Generated at 2022-06-13 07:45:24.833270
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange
    class DummyVault():
        def encrypt(self, seq, secret):
            return 'enc:%s' % seq

        def decrypt(self, cipher_text, obj=None):
            return 'dec:%s' % cipher_text

        def is_encrypted(self, cipher_text):
            return True

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(
        'test', vault=DummyVault(), secret='unused'
    )

    # Act
    output = avu != 'dec:enc:test'

    # Assert
    assert not output


# Generated at 2022-06-13 07:46:02.015391
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = 'secret'
    plaintext = 'plaintext'
    vault = get_vault_instance(VaultLib)

    # Test plaintext equals plaintext
    encryptedUnicode = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert encryptedUnicode == plaintext

    # Test plaintext does not equal different plaintext
    encryptedUnicode = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert encryptedUnicode != 'wrong'

    # Test encrypted.data equals plaintext
    encryptedUnicode = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert encryptedUnicode.data == plaintext

    # Test encrypted does not equal different plaintext

# Generated at 2022-06-13 07:46:09.228960
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    # NOTE:  This assumes that the underlying vault object is a
    #        passlib.utils.pbkdf2.pbkdf2 object.  This object
    #        uses fixed salt and the given password as key.  The
    #        given password is used as the key to decrypt the
    #        encrypted text.  The underlying vault object for
    #        this test will therefore be initialized with the
    #        same values used in the test below.

    from ansible.parsing.vault import Vault
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(password='password')

# Generated at 2022-06-13 07:46:21.156962
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import vault_monkeypatch_proper_cryptography_signals
    vault_monkeypatch_proper_cryptography_signals()

    vault = VaultLib()
    secret = '$'

    # Encrypt a value
    value = 'Hello World!'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(value, vault, secret)

    # Compare against the original value
    assert avu == value

    # Compare against an identical AnsibleVaultEncryptedUnicode value
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(value, vault, secret)
    assert avu == avu2


# Generated at 2022-06-13 07:46:29.864996
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    plaintext_data = u'abcdef'
    encrypted_data = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext_data, 'path/to/vault', 'secret')

    test_data_1 = u'abcdef'
    if encrypted_data != test_data_1:
        raise AssertionError('check failed')

    test_data_2 = u'abcde'
    if encrypted_data != test_data_2:
        raise AssertionError('check failed')

    test_data_3 = u'abcdefg'
    if encrypted_data == test_data_3:
        raise AssertionError('check failed')



# Generated at 2022-06-13 07:46:43.978829
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    # Test case: the string is not encrypted.
    avu = AnsibleVaultEncryptedUnicode("abc")
    avu.vault = vault
    assert avu.is_encrypted() == False
    # Test case: the string is encrypted.

# Generated at 2022-06-13 07:46:48.847217
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # no vault, always false
    avu = AnsibleVaultEncryptedUnicode(b"foo")
    assert not avu.is_encrypted()

    # no vault, always false
    avu = AnsibleVaultEncryptedUnicode(b"ANSIBLE_VAULT;1.1;AES256;foo")
    assert avu.is_encrypted()


# Generated at 2022-06-13 07:47:01.134300
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    import os
    import tempfile
    import shutil
    import getpass


# Generated at 2022-06-13 07:47:05.177224
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    The method __ne__ of class AnsibleVaultEncryptedUnicode returns true when the
    encrypted data is not equal to the given argument.
    """
    obj = AnsibleVaultEncryptedUnicode('vaulted data')
    assert obj != 'vaulted data'
    assert not obj != 'vaulted data'


# Generated at 2022-06-13 07:47:11.517907
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    avue = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256' + '\n' + '6361316235316662616565663537303236313638613439383231376335393330313162353431656165' + '\n' + '6439623632303566376431313863626133613665616465323236376430396564666236313665623862' + '\n' + '34333333313731666265' + '\n')
    assert avue.is_encrypted() == True


# Generated at 2022-06-13 07:47:14.725008
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # given
    a = AnsibleVaultEncryptedUnicode.from_plaintext('Hello world',None, None)

    # when
    result = a == 'Hello world'

    # then
    assert result is True


# Generated at 2022-06-13 07:47:53.782594
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault_password = 'test123'
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(vault_password)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test123', vault, vault_password)
    assert avu == 'test123'


# Generated at 2022-06-13 07:48:00.130736
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from vault import VaultLib
    import crypt

    secret = 'ansible_vault_test'
    plaintext = 'Hello world'
    vault = VaultLib(secret)
    ciphertext = crypt.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    assert avu.is_encrypted()

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode_is_encrypted()

# Generated at 2022-06-13 07:48:11.248008
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:48:18.988337
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # VaultLib
    vault = VaultLib()

    # Encrypted data

# Generated at 2022-06-13 07:48:24.630107
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib, VaultSecret
    x = AnsibleVaultEncryptedUnicode.from_plaintext('', VaultLib(), VaultSecret())

    assert x == '', 'Empty init should return False for AnsibleVaultEncryptedUnicode.__eq__'


# Generated at 2022-06-13 07:48:32.212807
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    secret = vault.get_binary_parsed_vault_secret('test')

    avue = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, secret)
    assert not avue != 'test'

    avue = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, secret)
    assert avue != 'not_test'

