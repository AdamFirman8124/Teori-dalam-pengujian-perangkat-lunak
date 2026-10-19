

# Generated at 2022-06-13 07:38:47.097276
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    avu = AnsibleVaultEncryptedUnicode
    assert not avu('a').__lt__(avu('b'))
    assert avu('a').__lt__(avu('b')) == 'a'.__lt__('b')
    assert not avu('a').__lt__('b')
    assert not avu('b').__lt__(avu('a'))
    assert avu('b').__lt__(avu('a')) == 'b'.__lt__('a')
    assert avu('b').__lt__('a')



# Generated at 2022-06-13 07:38:51.149427
# Unit test for method __ge__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ge__():
    avu1 = AnsibleVaultEncryptedUnicode("some data")
    avu2 = AnsibleVaultEncryptedUnicode("some data")
    assert avu1 >= avu2
    assert avu2 >= avu1
    avu1 = AnsibleVaultEncryptedUnicode("some data")
    avu2 = AnsibleVaultEncryptedUnicode("some more data")
    assert not avu1 >= avu2
    assert avu2 >= avu1


# Generated at 2022-06-13 07:38:59.743308
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from ansible.parsing import vault as vaultlib
    test_cases = [
        ('a', 'b'),
        ('a', 'A'),
        ('Ab', 'aB'),
        ('A1', 'a2'),
        ('Aa', 'aA'),
        ('Aa', 'ab'),
        ('AB', 'aa'),
    ]

    # Create an instance of the class AnsibleVaultEncryptedUnicode
    vault = vaultlib.VaultLib(password='qwerty')
    avu_obj = AnsibleVaultEncryptedUnicode.from_plaintext('1', vault, 'qwerty')

    # The test case

# Generated at 2022-06-13 07:39:06.417909
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    assert hasattr(AnsibleVaultEncryptedUnicode, 'count')
    assert AnsibleVaultEncryptedUnicode('test').count('test') == 1

if __name__ == '__main__':
    sys.path.insert(0, '.')
    import pytest
    pytest.main([__file__, '-vvs', '-x', '--pdb'])

# Generated at 2022-06-13 07:39:20.331972
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    from ansible.utils import get_crypt_at_beginning

    secret = 'testsecret'
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256' + '\n' + get_crypt_at_beginning(to_bytes('abcdefghijkl'))
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vaultlib.VaultLib(secret)

    # testing slice with end == 0
    assert avu.__getslice__(0, 0) == ''

    # testing slice with start == len(plaintext) and end == len(plaintext)
    assert avu.__getslice__(12, 12) == ''

    # testing slice with start == len(plaintext)

# Generated at 2022-06-13 07:39:27.111076
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    string = u'test_AnsibleVaultEncryptedUnicode_rfind_substr_start'
    avu = AnsibleVaultEncryptedUnicode(string)
    assert avu.rfind(u'test') == 0
    assert avu.rfind(u'test', 0, -1) == 0
    assert avu.rfind(u'test', 0, -6) == -1
    assert avu.rfind(u'test', 0, -7) == 0
    assert avu.rfind(u'est_', 0, -7) == 1
    assert avu.rfind(u'_substr') == 24
    assert avu.rfind(u'_substr_') == -1
    assert avu.rfind(u'_substr', 0, -8) == 24


# Generated at 2022-06-13 07:39:29.997617
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    assert AnsibleVaultEncryptedUnicode("ciphertext").__add__("more") == AnsibleVaultEncryptedUnicode("ciphertextmore")
    assert "more" + AnsibleVaultEncryptedUnicode("ciphertext") == AnsibleVaultEncryptedUnicode("moreciphertext")



# Generated at 2022-06-13 07:39:37.381867
# Unit test for method __ge__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ge__():
    avu = AnsibleVaultEncryptedUnicode(u'aaaaaaaa')
    assert not avu >= u'aaaaaaab'
    assert avu >= u'aaaaaaaa'
    assert avu >= u'aaaaaaa'
    assert avu >= u'aaaaa'
    assert avu >= avu
    assert avu >= AnsibleVaultEncryptedUnicode(u'aaaaaaaa')



# Generated at 2022-06-13 07:39:40.201891
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    seq = AnsibleVaultEncryptedUnicode.from_plaintext('', vault=None)
    num = seq.count('a')
    assert num == 0



# Generated at 2022-06-13 07:39:44.048415
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    test_str = "test"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(test_str, vault, vault_password)
    avu1 = "test"
    assert to_native(avu1) != to_native(avu)

# Generated at 2022-06-13 07:40:02.012708
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    avu = AnsibleVaultEncryptedUnicode('123456789')

    for start, end in [
        # Tests for comparison of index, end, and length (len(avu))
        (1, 10),
        (10, 20),
        (-10, 10),
        (-20, -10),
    ]:
        # This should return the whole string, because we're using max()
        # to correct for negative indices and slicing past the end of the string
        # so we will always end up returning the whole string
        assert avu.__getslice__(start, end) == '123456789'


# Generated at 2022-06-13 07:40:12.523215
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    # Check if the proper string is returned when
    # adding a string to an AnsibleVaultEncryptedUnicode string
    # FIXME: This test can only be run by Ansible developers as
    #        it depends on the vault password being stored in an
    #        environment variable.
    import base64
    import os
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    if os.getenv("ANSIBLE_VAULT_PASSWORD_FILE"):
        # Use the vault password file
        pw = os.environ["ANSIBLE_VAULT_PASSWORD_FILE"]
    else:
        # Use the vault password
        pw = os.environ["ANSIBLE_VAULT_PASSWORD"]
    cipher

# Generated at 2022-06-13 07:40:27.261853
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:37.741198
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    avu = AnsibleVaultEncryptedUnicode(b'foo')
    avu.data = u'foo'

    # Test with AnsibleVaultEncryptedUnicode
    assert(avu + AnsibleVaultEncryptedUnicode(u'bar') == u'foobar')
    assert(avu + AnsibleVaultEncryptedUnicode(b'bar') == u'foobar')

    # Test with unicode
    assert(avu + u'bar' == u'foobar')

    # Test with byte
    assert(avu + b'bar' == u'foobar')

    # Test with byte
    assert(avu + u'bar' == u'foobar')


# Generated at 2022-06-13 07:40:46.609665
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class Vault:
        def encrypt(self, data, secret):
            return data
        def decrypt(self, data, obj):
            return data
        def is_encrypted(self, data):
            return False

    # Test simple case
    avueu = AnsibleVaultEncryptedUnicode(b'hello')
    avueu.vault = Vault()
    assert avueu == b'hello'

    # Test multiple bytes
    avueu = AnsibleVaultEncryptedUnicode(b'\x01\x02\x03\x04\x05')
    avueu.vault = Vault()
    assert avueu == b'\x01\x02\x03\x04\x05'

    # Test dumb error case
    avueu = AnsibleVaultEncryptedUnicode(None)


# Generated at 2022-06-13 07:40:57.457348
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():

    class fakeVault:
        def decrypt(self, text, obj=None):
            if obj is not None:
                if isinstance(obj, AnsibleVaultEncryptedUnicode):
                    return text.lower()
            return text

    other = AnsibleVaultEncryptedUnicode('plop')
    other.vault = fakeVault()
    assert other[0] == 'p'
    assert other[1] == 'l'
    assert other[2] == 'o'
    assert other[3] == 'p'

    avu = AnsibleVaultEncryptedUnicode('Plop')
    avu.vault = fakeVault()
    assert avu[0] == 'P'
    assert avu[1] == 'l'
    assert avu[2] == 'o'
    assert avu

# Generated at 2022-06-13 07:41:09.144730
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    '''
    AnsibleVaultEncryptedUnicode.__add__ method
    '''
    av = AnsibleVaultEncryptedUnicode('AVEC')
    av.vault = None
    # __add__ with another AnsibleVaultEncryptedUnicode
    av2 = AnsibleVaultEncryptedUnicode('AVEC2')
    av2.vault = None
    av_add = av + av2
    assert av_add == 'AVECAVEC2'
    assert av_add.vault == None
    av2_add = av2 + av
    assert av2_add == 'AVEC2AVEC'
    assert av2_add.vault == None
    # __add__ with a text_type
    av_add2 = av + 'AVEC2'

# Generated at 2022-06-13 07:41:15.105020
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Testing that the return value is correct
    assert (AnsibleVaultEncryptedUnicode("foo") != "foo")
    assert ("foo" != AnsibleVaultEncryptedUnicode("foo"))
    assert (AnsibleVaultEncryptedUnicode("foo") != AnsibleVaultEncryptedUnicode("foo"))


# Generated at 2022-06-13 07:41:19.802112
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode.from_plaintext('plaintext', None, None).is_encrypted() == False
    assert AnsibleVaultEncryptedUnicode.from_plaintext('', None, None).is_encrypted() == False


# Generated at 2022-06-13 07:41:29.938544
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    import pprint
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 07:41:41.061493
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
  original_string = "abcd"
  ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(original_string)

  print(original_string < ansible_vault_encrypted_unicode)
test_AnsibleVaultEncryptedUnicode___lt__()

print(yaml.__version__)

print(yaml.dump(AnsibleVaultEncryptedUnicode.data()))


# Generated at 2022-06-13 07:41:51.462582
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import tempfile
    import shutil
    import os
    import six
    from ansible.parsing.vault import VaultLib
    import yaml
    import ansible.constants as C

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 07:42:02.082870
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('mypassword')
    plain = 'foo'
    encrypted = vault.encrypt(plain)
    assert encrypted != plain
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plain, vault, 'mypassword')
    assert avu.is_encrypted()
    if isinstance(encrypted, text_type):
        encrypted = encrypted.encode('utf-8')
    avu = AnsibleVaultEncryptedUnicode(encrypted)
    assert avu.is_encrypted()

    plain2 = vault.decrypt(encrypted)
    avu = AnsibleVaultEncryptedUnicode(encrypted)
    avu.vault = vault
    assert avu.is_encrypted()
    assert avu.data == plain2
    av

# Generated at 2022-06-13 07:42:12.125158
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    vault_password = 'hunter2'

# Generated at 2022-06-13 07:42:19.422534
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    plaintext = "Hello World!"
    secret = "secret"
    vault = VaultLib([secret])
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

    # check for matching crypto data
    assert avu == avu
    assert avu == ciphertext
    assert avu != "ciphertext"

    # check for matching plaintext
    assert avu == plaintext
    assert avu != "plaintest"

    # the following lines fail due to:
    # AssertionError: ansible_pos can only be set with a tuple/list of three values: source, line number, column number
    # avu == (avu.vault._ciphertext, 0, 0)
    # avu == (c

# Generated at 2022-06-13 07:42:27.055632
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(['password'])
    encrypted_foo = AnsibleVaultEncryptedUnicode.from_plaintext(
        'foo', vault, 'password'
    )
    encrypted_foo_2 = AnsibleVaultEncryptedUnicode.from_plaintext(
        'foo', vault, 'password'
    )
    encrypted_bar = AnsibleVaultEncryptedUnicode.from_plaintext(
        'bar', vault, 'password'
    )

    assert not encrypted_foo < 'foo'
    assert not encrypted_foo_2 < 'foo'
    assert not encrypted_bar < 'bar'

    assert encrypted_bar < 'foo'
    assert encrypted_bar < encrypted_foo_2



# Generated at 2022-06-13 07:42:40.549597
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():

    if not sys.version_info[0] < 3:
        return

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    vault = VaultLib('!vault |$ANSIBLE_VAULT;1.1;AES256')

    # set secret
    secret = VaultSecret('super_secure_password')

    # set plaintext
    plaintext = 'hello world'

    # create vaulted strings
    vaulted1 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    vaulted2 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

    # test simple comparasion vaulted < vaulted
    assert(vaulted1 < vaulted2)

    # test compar

# Generated at 2022-06-13 07:42:51.527919
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib("password")
    plaintext = "this is plaintext"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, "password")
    print("avu.data = %s" % avu.data)
    print("avu.__eq__(\"this is plaintext\") = %s" % avu.__eq__("this is plaintext"))
    print("avu.__ne__(\"this is plaintext\") = %s" % avu.__ne__("this is plaintext"))
    print("avu.__eq__(u\"this is plaintext\") = %s" % avu.__eq__(u"this is plaintext"))

# Generated at 2022-06-13 07:42:59.398539
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    avueu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n37303730613237636438303665653335393436333637333233336339306332626562323762376161320a393464383338363930316162353661656436653764663331303232363366633331323337303538650a36353263633333353866343637616162373637666565353736376465323034303733653132616562610a32353936373465353732666239333632313861316136313732623162663965633961646436623064')

    # First make sure is_encrypted raises an exception if vault attribute

# Generated at 2022-06-13 07:43:09.492396
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    unit test function
    :return:
    '''

# Generated at 2022-06-13 07:43:25.140389
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu1 = AnsibleVaultEncryptedUnicode('')
    avu1.data = 'some text'
    avu2 = AnsibleVaultEncryptedUnicode('')
    avu2.data = 'some other text'
    assert avu1 != avu2
    assert avu1 != 'some other text'
    assert avu1 != 123



# Generated at 2022-06-13 07:43:35.628916
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # This method is used in certain operations related to comparison.
    # Because of that, some code uses `self.__eq__(self.__class__())` to test
    # whether the instance has been initialized or not. For example,
    # https://github.com/ansible/ansible-modules-core/blob/devel/system/ipmi_power.py#L371
    #
    # The test for equality shouldn't return True for `self` and `self.__class__()`
    #
    # Define both methods, so that `self.data` gets initialized
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(
        'Vault password:',
        vault=None,
    )
    ansible_vault_encrypted_unicode.data = 'Bar'

    ansible

# Generated at 2022-06-13 07:43:43.302568
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault

    vault_secret = b'secret'
    bad_vault_secret = b'badsecret'

    # From file
    if _sys.version_info[0] > 2:
        plaintext = 'this is plaintext'
    else:
        plaintext = 'this is plaintext'.encode()
    valut = vault.VaultLib(vault_secret)
    ciphertext = valut.encrypt(plaintext, plaintext)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = valut
    assert avu.is_encrypted()

    # From plaintext
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, valut, vault_secret)
    assert av

# Generated at 2022-06-13 07:43:49.350318
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # This test function was automatically generated - do not edit it by hand.
    args = ([],)
    kwargs = {'end': sys.maxsize}
    expected_value = True
    actual_value = AnsibleVaultEncryptedUnicode.__ne__(*args, **kwargs)
    assert actual_value == expected_value, '%r != %r' % (actual_value, expected_value)

    kwargs = {'end': 0}
    expected_value = True
    actual_value = AnsibleVaultEncryptedUnicode.__ne__(*args, **kwargs)
    assert actual_value == expected_value, '%r != %r' % (actual_value, expected_value)

    kwargs = {'start': 0, 'end': sys.maxsize}
    expected_value = True

# Generated at 2022-06-13 07:43:57.929106
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    import os

    vault_id = '12345'
    vault_password = 'changeme'
    vault = VaultLib([vault_password], vault_id)
    secret = 'secret'
    plaintext = secret

    vault_unicode = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    if vault_unicode.is_encrypted():
        print('AnsibleVaultEncryptedUnicode.is_encrypted() unit test: PASS')
    else:
        print('AnsibleVaultEncryptedUnicode.is_encrypted() unit test: FAIL')
        sys.exit(1)


# Generated at 2022-06-13 07:44:05.201932
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.vault import VaultLib
    v = VaultLib('password')
    v.DEFAULT_VAULT_ID_MATCH = None
    encrypted_string = AnsibleVaultEncryptedUnicode.from_plaintext('test', v, 'password')
    # the string is the encrypted version of string 'test'
    # string 'test' is not encrypted, is_encrypted method should return False
    assert encrypted_string.is_encrypted() == True


# Generated at 2022-06-13 07:44:10.721128
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test 1: unencrypted string
    string1 = "test"
    string2 = "test"
    result1 = string1 == string2
    # Expected result: True
    ansiblevault = AnsibleVaultEncryptedUnicode(string1)
    result2 = ansiblevault == string2
    # Expected result: False
    assert result1 == True
    assert result2 == False

# Generated at 2022-06-13 07:44:16.486143
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange
    avue = AnsibleVaultEncryptedUnicode('some data')

    # Act and Assert
    assert(avue != 'some data')
    assert(avue != avue.data)
    assert(avue != 'some ')
    assert('some ' != avue)
    assert('some data' != avue)
    assert(not(avue != avue))
    assert(not(avue != 'some data'))



# Generated at 2022-06-13 07:44:23.689461
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import yaml
    from ansible.parsing.vault import VaultLib

    vault_password = 'testpassword'

    vault = VaultLib(None)
    plaintext = 'string that should be encrypted'
    ciphertext = vault.encrypt(plaintext, vault_password)

    assert len(plaintext) > 16
    assert len(ciphertext) > 16

    s_plaintext = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, vault_password)
    s_ciphertext = AnsibleVaultEncryptedUnicode(ciphertext)

    assert s_plaintext.vault
    assert s_ciphertext.vault

    assert not s_plaintext.is_encrypted()
    assert s_ciphertext.is_encrypted()



# Generated at 2022-06-13 07:44:29.238299
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    secret = 'changeme'
    plaintext = 'secret string'

    # Create and tag a YAML string
    yaml_str = '!vault |\n'
    yaml_str += '  $ANSIBLE_VAULT;1.1;AES256\n'
    yaml_str += '  35353436336166306232353739393362653365363337616136353133616363376238636239316266\n'
    yaml_str += '  63656537633332656161373636613130333930636139326330626230663033626465636465663335\n'
    yaml_str += '  30383730313037376665313430383738666133326635\n'

    # Construct the

# Generated at 2022-06-13 07:44:52.310366
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('foo', vault=None)
    assert(avu != 'foo')
    assert(avu == 'bar')

    # in case object is not yet decrypted, avoid ValueError

# Generated at 2022-06-13 07:45:01.623864
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault = VaultLib([])

    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext('abc', vault, VaultSecret('a'))
    assert ansible_vault_encrypted_unicode != 'abc'

    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext('abc', vault, VaultSecret('b'))
    assert ansible_vault_encrypted_unicode != 'abc'


# Generated at 2022-06-13 07:45:08.153734
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    test_vault_password = 'test_password'
    test_vault = VaultLib(test_vault_password)

    test_string = 'test_string'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(test_string, test_vault, test_vault_password)

    assert avu.is_encrypted()



# Generated at 2022-06-13 07:45:15.253831
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Create a AnsibleVaultEncryptedUnicode object with a real ansible vault
    import ansible.parsing.vault as vault

    # Create an ansible vault
    password = 'toor'
    _vault = vault.VaultLib(password)
    # instantiate a AnsibleVaultEncryptedUnicode object with a valid vault
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", _vault, password)

    # with a string equal to the data
    assert not (avu != "foo"), "__ne__ should return false when string is equal to data"

    # with a string not equal to the data
    assert avu != "bar", "__ne__ should return true when string is not equal to data"



# Generated at 2022-06-13 07:45:25.782823
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import unittest

    from ansible.utils.vault import VaultLib

    class TestSequenceMethods(unittest.TestCase):
        def setUp(self):
            self.vault = VaultLib('test')
            self.vault_ciphertext = '$ANSIBLE_VAULT;1.1;AES256'
            self.unencrypted_text = 'unencrypted'

        def test_is_encrypted_ciphertext(self):
            avu = AnsibleVaultEncryptedUnicode(self.vault_ciphertext)
            avu.vault = self.vault
            self.assertTrue(avu.is_encrypted())

        def test_is_encrypted_plaintext(self):
            avu = AnsibleVaultEncryptedUnicode(self.unencrypted_text)

# Generated at 2022-06-13 07:45:36.857907
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Method __ne__ of class AnsibleVaultEncryptedUnicode
    # This test case is used to test method __ne__ of class AnsibleVaultEncryptedUnicode.
    # Declare necessary variables for this test case.
    ciphertext = 'abcdefg'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    # Test case:
    # When self.vault is None,
    # the method __ne__ returns True.
    assert avu.__ne__(ciphertext) is True
    # Test case:
    # When other is not a AnsibleVaultEncryptedUnicode object,
    # the method __ne__ returns True.
    assert avu.__ne__(12) is True
    # Test case:
    # When self.vault is not None,
    #

# Generated at 2022-06-13 07:45:46.632809
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vault = VaultLib(password_file=None)
    secret = VaultSecret('password')

    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret).is_encrypted() is True
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret).vault.key == vault.key
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret).vault.key == secret.data

    assert AnsibleVaultEncryptedUnicode('bar').is_encrypted() is False

# Generated at 2022-06-13 07:45:55.892828
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:46:01.901984
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode('hello')
    if not a.__ne__('hello'):
        raise AssertionError('Test failed. AnsibleVaultEncryptedUnicode.__ne__ does not return True for non-equal strings')


# Generated at 2022-06-13 07:46:09.266696
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test for AnsibleVaultEncryptedUnicode.__eq__(other)

    # Arrange
    CLASS_NAME = 'AnsibleVaultEncryptedUnicode'
    class_method = getattr(sys.modules[__name__], CLASS_NAME).__eq__
    method_name = '__eq__'
    first_arg_name = 'other'
    args = dict()
    kwargs = dict()
    args[first_arg_name] = None

    # Act
    # Assert
    #
    # Method __eq__
    #
    # AnsibleVaultEncryptedUnicode.__eq__(other)
    #
    # 1. other is a AnsibleVaultEncryptedUnicode, and is not vaulted
    #
    # Arrange
    other = AnsibleVaultEnc

# Generated at 2022-06-13 07:46:50.228547
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    '''
    Test function for AnsibleVaultEncryptedUnicode
    '''
    from ansible.parsing.vault import VaultLib
    from ansible.errors import AnsibleError as AE

    def exec_test(method, clear_text_bytes, secret):
        vault = VaultLib(secret)
        ciphertext = vault.encrypt(clear_text_bytes, secret)
        avu = AnsibleVaultEncryptedUnicode(ciphertext)
        avu.vault = vault

        if method is None:
            return avu == clear_text_bytes
        else:
            return getattr(avu, method)() == clear_text_bytes

    # Test a few byte sequences

# Generated at 2022-06-13 07:46:56.836966
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    import sys

    vault = VaultLib(password='password')
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('Hi', vault, 'password')
    assert avue.is_encrypted() == True

    avue = AnsibleVaultEncryptedUnicode('Hi')
    assert avue.is_encrypted() == False


# Generated at 2022-06-13 07:47:01.225635
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib
    vault = VaultLib([])
    test = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'test')
    assert test == test
    assert not test == 'test'



# Generated at 2022-06-13 07:47:09.301781
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib, VaultSecret
    from tempfile import NamedTemporaryFile
    import os
    import time


# Generated at 2022-06-13 07:47:19.034322
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    string = to_bytes("string")
    ciphertext1 = to_bytes("$ANSIBLE_VAULT;1.2;AES256;foo\n6363356631633361653935643233323033623231626131373834376162346433666538656661\n")
    ciphertext2 = to_bytes("$ANSIBLE_VAULT;1.2;AES256;foo\n6363356631633361653935643233323033623231626131373834376162346433666538656662\n")

    avu = AnsibleVaultEncryptedUnicode(ciphertext1)
    avu.vault = None

    assert (avu != string)

    avu.vault = None

    assert (avu != string)


# Unit

# Generated at 2022-06-13 07:47:27.665108
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    ''' Unit test function for class AnsibleVaultEncryptedUnicode '''
    import base64
    from ansible.parsing.vault import VaultLib
    secret = 'test_secret'
    vault = VaultLib(password=secret)
    plaintext = 'Hello'
    ciphertext = vault.encrypt(plaintext, secret)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault
    assert avu.is_encrypted() == True
    # change ciphertext to plaintext
    avu._ciphertext = to_bytes(plaintext)
    assert avu.is_encrypted() == True
    # change ciphertext to none encrypted content
    avu._ciphertext = to_bytes(base64.b64encode(to_bytes(plaintext)))
   

# Generated at 2022-06-13 07:47:34.350037
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import vaultlib
    vault = vaultlib.VaultLib()

    # Test Pass
    assert AnsibleVaultEncryptedUnicode.from_plaintext('Hello', vault, 'password') == 'Hello'
    assert 'Hello' == AnsibleVaultEncryptedUnicode.from_plaintext('Hello', vault, 'password')

    # Test Fail
    assert 'Hello' != AnsibleVaultEncryptedUnicode.from_plaintext('Hello', vault, 'password')



# Generated at 2022-06-13 07:47:40.140822
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    a_vault_obj = AnsibleVaultEncryptedUnicode('vault_encrypted_unicode')
    a_vault_obj.vault = True
    assert a_vault_obj.__eq__(False)

    a_vault_obj.data = 'vault_encrypted_unicode'
    assert a_vault_obj.__eq__('vault_encrypted_unicode')


# Generated at 2022-06-13 07:47:51.219934
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def check(a, b):
        assert (a == b) == (a.data == b.data)

    avu_a = AnsibleVaultEncryptedUnicode.from_plaintext('a', type('vault', (), {'is_encrypted': lambda s: True}), 'secret')
    avu_b = AnsibleVaultEncryptedUnicode.from_plaintext('b', type('vault', (), {'is_encrypted': lambda s: True}), 'secret')

    check(avu_a, 'a')
    check(avu_b, 'b')
    check(avu_a, avu_b)
    check(avu_b, avu_a)

# Unit tests for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:48:01.286534
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    u1 = AnsibleVaultEncryptedUnicode('A')
    u2 = AnsibleVaultEncryptedUnicode('A')

    u1.vault = u2.vault = None
    assert u1 != 'A'
    assert u2 != 'A'

    u1.vault = u2.vault = None
    assert u1 != u2

    jar = None
    try:
        import ansible.parsing.vault
        jar = ansible.parsing.vault.VaultLib('mypassword')
    except ImportError as e:
        print('FAIL: unable to import ansible.parsing.vault')
        raise e
    u1.vault = u2.vault = jar
    assert not (u1 == 'A')