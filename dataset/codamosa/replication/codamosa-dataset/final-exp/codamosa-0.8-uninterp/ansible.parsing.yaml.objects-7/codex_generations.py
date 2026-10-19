

# Generated at 2022-06-13 07:38:58.393225
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    myvault = VaultLib(None)
    myvault.secrets['vaultpassword'] = 'password'
    secret = 'vaultpassword'

    # test correct is_encrypted true
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('my content', myvault, secret)
    assert avue.is_encrypted()

    # test correct is_encrypted false
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('my content', None, None)
    assert not avue.is_encrypted()


# Generated at 2022-06-13 07:39:09.603722
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    input_ = '{"obj": "val"}'
    key = 'secret'
    encrypted_input = '$ANSIBLE_VAULT;1.1;AES256\n36383337663437666664366533666463626261393435643439653665363964383733326462316664\n6334316663623166626135313561383239623665363437636331646234653262656539613730663762\n6365356563633763\n'
    expected = True

    # Load the vault for testing
    import vaultlib
    v = vaultlib.vault_load(key)

    # Create an AnsibleVaultEncryptedUnicode from the encrypted data

# Generated at 2022-06-13 07:39:23.392065
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    avu1 = AnsibleVaultEncryptedUnicode('test')
    avu2 = AnsibleVaultEncryptedUnicode('pass')
    assert avu1._ciphertext == b'test'

    # if avu1._ciphertext is not an AnsibleVaultEncryptedUnicode, return True
    assert avu1._ciphertext <= avu2._ciphertext

    # if avu1._ciphertext is an AnsibleVaultEncryptedUnicode
    # return the result of <comparison> after decryption
    assert avu1 <= avu2



# Generated at 2022-06-13 07:39:25.074781
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode.from_plaintext('some string', None, None).is_encrypted() is False


# Generated at 2022-06-13 07:39:29.116332
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ave = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\nxxxxxxxxxxxxxxxxxxxxxx=\n')
    assert ave != 'b'



# Generated at 2022-06-13 07:39:40.026879
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = None
    secret = 'test_AnsibleVaultEncryptedUnicode___eq__'
    ansible_vault_encrypted_unicode_1 = AnsibleVaultEncryptedUnicode.from_plaintext('test_AnsibleVaultEncryptedUnicode___eq__', vault, secret)
    ansible_vault_encrypted_unicode_2 = AnsibleVaultEncryptedUnicode.from_plaintext('test_AnsibleVaultEncryptedUnicode___eq__', vault, secret)
    assert ansible_vault_encrypted_unicode_1 == ansible_vault_encrypted_unicode_2


# Generated at 2022-06-13 07:39:49.105743
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    def value_error():
        raise ValueError()
    # setup
    class TestVault():
        def __init__(self, val):
            self.val = val
        def decrypt(self, ciphertext):
            return self.val
    v1 = TestVault('hello')
    v2 = TestVault('world')
    x = AnsibleVaultEncryptedUnicode('lala')
    y = AnsibleVaultEncryptedUnicode('lala')
    z = AnsibleVaultEncryptedUnicode('lala')
    x.vault = v1
    y.vault = v1
    z.vault = v2
    # test
    x.__le__(y)
    y.__le__(x)
    x.__le__(z)

# Generated at 2022-06-13 07:39:58.316710
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    import vaultlib
    secret = "secret"
    plaintext1 = "Hello"
    plaintext2 = "Hello"

    # create an vault object
    av = vaultlib.VaultLib(secret)

    # create encrypted strings
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext1, av, secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext2, av, secret)

    assert avu1 == plaintext1 == plaintext2 == avu2
    assert avu1 <= plaintext2 == plaintext1 <= avu2


# Generated at 2022-06-13 07:40:06.523608
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import StringIO
    import os
    import tempfile
    import unittest
    import yaml

    # The following tests are dealing with the vault and ansible-vault
    # functionality in the AnsibleVaultEncryptedUnicode class.
    #
    # In order to avoid issues with testing and to keep the code as small
    # as possible we just test the different paths in the __ne__ method.
    #
    # This means we are only testing if the __ne__ method returns True or
    # False for the different paths.  We are not testing the exact strings
    # we are testing with ('a', 'b') and ('a', 'a').  All we care about is
    # that the __ne__ method neither throws an exception nor a traceback.
    #
    # Because of the way the __ne__ method is defined we can safely assume

# Generated at 2022-06-13 07:40:15.508547
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    teststring = "test"
    testvault = VaultLib('abc')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(teststring, testvault, "secret")
    assert avu != teststring
    assert avu != "test"
    assert avu != u"test"
    assert avu != b"test"

    # This is a bug in python 2, in PY3 this is consistent
    if (not _sys.version_info > (3, 0)):
        assert "test" != avu

    # expected behaviour:
    assert u"test" != avu
    assert b"test" != avu
    assert avu != teststring

    # expected behaviour:
    avu2 = AnsibleVaultEncryptedUnic

# Generated at 2022-06-13 07:40:30.879894
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:41.404634
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    secret = 'my_secret'
    vault_pass = secret
    text = 'test'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(text, VaultLib(vault_pass), secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(text, VaultLib(vault_pass), secret)
    assert(avu == avu2)
    assert(avu == 'test')
    assert(avu.data == 'test')
    assert(avu.vault.is_encrypted(avu._ciphertext))
    assert('test' == avu)
    assert(avu != 'abc')
    assert(avu.data != 'abc')

# Generated at 2022-06-13 07:40:46.252693
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    # create copied method for unit test
    def __lt__(self, string):
        if isinstance(string, AnsibleVaultEncryptedUnicode):
            return self.data < string.data
        return self.data < string

    # test
    vault = None
    secret = "secret"
    plaintext_1 = "plaintext_1"
    plaintext_2 = "plaintext_2"

    # create an AnsibleVaultEncryptedUnicode object
    ciphertext = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext_1, vault, secret)
    ciphertext.data = plaintext_1
    ciphertext.vault = vault

    # create another AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 07:40:57.344523
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # test for hashed strings
    class test_hash(object):
        def __init__(self, secret):
            self.secret = secret
        def encrypt(self, string, secret=None):
            return 'b639971cc9f4ebc7a8eae49baae7b253'
        def decrypt(self, string, secret=None):
            return self.secret
        def is_encrypted(self, string):
            return True
    # create secret and test
    test_secret = 'test secret'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(test_secret, test_hash(test_secret), 'vault_password')
    assert avu.__ne__(test_secret) == False
    assert avu.__ne__('test secret') == False


# Generated at 2022-06-13 07:41:04.214888
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class DummyVault():
        def encrypt(self, plaintext):
            return plaintext + "cipher"
        def decrypt(self, ob):
            return ob[:-6]

    vault_text = "abcdef"
    vault = DummyVault()
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(vault_text, vault)
    assert avu == vault_text



# Generated at 2022-06-13 07:41:07.633575
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode("encrypted string")
    if avu != "encrypted string":
        raise Exception("String comparison failed")


# Generated at 2022-06-13 07:41:15.289948
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from .vault import VaultLib
    if not hasattr(VaultLib, 'tell_secrets'):
        VaultLib.tell_secrets = VaultLib.decrypt
    vault = VaultLib(None)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, None)
    assert avu == 'test'


# Class that allows you to create AnsibleVaultEncryptedUnicode objects even if vaultlib is not available

# Generated at 2022-06-13 07:41:22.654440
# Unit test for method replace of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_replace():
    avu = AnsibleVaultEncryptedUnicode(None)
    avu.data = 'password'
    assert avu.replace('d', 'D') == 'passworD'
    assert avu.replace(AnsibleVaultEncryptedUnicode('d'), 'D') == 'passworD'
    assert avu.replace('d', AnsibleVaultEncryptedUnicode('D')) == 'passworD'
    assert avu.replace(AnsibleVaultEncryptedUnicode('d'), AnsibleVaultEncryptedUnicode('D')) == 'passworD'


# Generated at 2022-06-13 07:41:26.298959
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    assert AnsibleVaultEncryptedUnicode("~~~1") < AnsibleVaultEncryptedUnicode("~~~2")
    assert AnsibleVaultEncryptedUnicode("~~~1") < "~~~2"


# Generated at 2022-06-13 07:41:34.487750
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib()
    assert AnsibleVaultEncryptedUnicode.from_plaintext("hello world", vault, "secret").__eq__("hello world")
    assert not AnsibleVaultEncryptedUnicode.from_plaintext("hello world", vault, "secret").__eq__("test")

# Generated at 2022-06-13 07:41:39.434095
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:41:42.221601
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    assert avu.__ne__(None)
    assert avu.__ne__(avu)
    assert avu.__ne__('')


# Generated at 2022-06-13 07:41:48.227444
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from ansible.parsing.vault import VaultLib
    import getpass

    data = 'abc'
    first = AnsibleVaultEncryptedUnicode.from_plaintext(data, VaultLib(password=getpass.getpass('Vault password: ')), 'test secret')
    second = 'bcd'

    return first < second


# Generated at 2022-06-13 07:41:56.289581
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pwd = 'secret123'
    # eq
    assert AnsibleVaultEncryptedUnicode.from_plaintext('blubber', vault=vaultlib.VaultLib(pwd), secret=pwd) == 'blubber'
    assert 'blubber' == AnsibleVaultEncryptedUnicode.from_plaintext('blubber', vault=vaultlib.VaultLib(pwd), secret=pwd)
    # ne
    assert 'blub' != AnsibleVaultEncryptedUnicode.from_plaintext('blubber', vault=vaultlib.VaultLib(pwd), secret=pwd)
    assert 'blubber' != AnsibleVaultEncryptedUnicode.from_plaintext('blub', vault=vaultlib.VaultLib(pwd), secret=pwd)


# Generated at 2022-06-13 07:42:05.505349
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    import base64
    input_data = 'foo'
    secret = 'bar'
    ciphertext = 'AgECAAAAAADzN0SJQN8+/Kj0XDYGptjKMyxETxbiPVEoTaJfcoK5E5RoDVPCb5YFkMAWMnqI3qxEt+bHpJHSyV7bPzc+nKj'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(input_data, VaultLib(), secret)
    assert avu.is_encrypted()
    avu.data = ciphertext
    assert avu.is_encrypted()
    avu.data = base64.b64decode(ciphertext)

# Generated at 2022-06-13 07:42:08.537352
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    a = AnsibleVaultEncryptedUnicode("lorem ipsum dolor")
    b = AnsibleVaultEncryptedUnicode("sit amet")
    assert a < b


# Generated at 2022-06-13 07:42:11.569918
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    Test method __ne__ from AnsibleVaultEncryptedUnicode
    """
    from ansible.parsing.vault import VaultLib
    va = VaultLib()
    va.secrets = {'default': 'test_password'}
    test = AnsibleVaultEncryptedUnicode.from_plaintext('secret', va, 'default')
    assert test != 'secret'


# Generated at 2022-06-13 07:42:16.454251
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    seq = 'Hello'
    secret = 'secret'
    vault = VaultLib([])

    avu_encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert avu_encrypted.is_encrypted()

    avu_plaintext = AnsibleVaultEncryptedUnicode(seq)
    assert not avu_plaintext.is_encrypted()


# Generated at 2022-06-13 07:42:25.089547
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:32.214355
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256;key\nblablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablabla==\n'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu == 'key'
    assert avu != 'not key'


# Generated at 2022-06-13 07:42:53.191973
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault_content = '\$ANSIBLE_VAULT;1.1;AES256\n35303434613264383335303833313363306665653136623264336533616266363631653834623462\n39393431633665653734633039333866383333623436303536306232333465613461333365393538\n31396462663736333233393239626231363638303738643366386161323934363537376233656164\n666538\n'
    secret = 'secret'
    plaintext = 'This is a test message.\n'


# Generated at 2022-06-13 07:42:56.482141
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    u = AnsibleVaultEncryptedUnicode(b'\x01')
    assert u != '\x01'
    assert u != '\x02'
    assert not (u != '\x01')


# Generated at 2022-06-13 07:43:08.034513
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test with a secret shorter than the key
    secret = to_bytes('12345678')
    vault_pass_bytes = b'MyVaultKey'

# Generated at 2022-06-13 07:43:15.511173
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # This test will always pass as long as
    # AnsibleVaultEncryptedUnicode.is_encrypted is defined properly
    #
    # This test is here because AnsibleVaultEncryptedUnicode is a new
    # class and it initial method implementation had a bug where the
    # is_encrypted method always returned False.
    secret = 'my_secret_password'
    plaintext = 'my_secret_string'
    avu = AnsibleVaultEncryptedUnicode(ciphertext=plaintext)
    assert avu.is_encrypted() is False


# Generated at 2022-06-13 07:43:28.648678
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Create a AnsibleVaultEncryptedUnicode from plaintext
    vault = AnsibleVaultLib(b'abcdefghijklmnopqrstuvwxyz0123456789')
    secret = vault.get_secret(vault.default_password)
    plaintext = 'Hello, World!'
    string = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

    # __ne__ should return true if the text is different
    other = AnsibleUnicode('Hello, Earth!')
    assert string != other

    # __ne__ should return false if the text is the same
    other = AnsibleUnicode(plaintext)
    assert not string != other


# Generated at 2022-06-13 07:43:43.895438
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.vault import VaultAES256

    vault_secret = 'vault_secret'
    plain_text = 'Hello World'

# Generated at 2022-06-13 07:43:55.854283
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:43:59.976300
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    aveu1 = AnsibleVaultEncryptedUnicode('bar')
    aveu2 = AnsibleVaultEncryptedUnicode('baz')

    assert aveu1 != aveu2


# Generated at 2022-06-13 07:44:01.735609
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode.from_plaintext('password', None, None)
    b = 'password'

    assert a.__ne__(b)


# Generated at 2022-06-13 07:44:08.921043
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    secret = 'password'
    vault = VaultLib(secret)
    ciphertext = vault.encrypt('plain text')
    encrypted = AnsibleVaultEncryptedUnicode(ciphertext)
    encrypted.vault = vault
    assert encrypted.is_encrypted()
    assert not encrypted.data.is_encrypted()

    non_encrypted = AnsibleVaultEncryptedUnicode('plain text')
    assert not non_encrypted.is_encrypted()
    assert not non_encrypted.data.is_encrypted()


# Generated at 2022-06-13 07:44:29.091492
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    secret = 'jelly'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(secret, VaultLib(password=secret), secret)
    assert avu == secret



# Generated at 2022-06-13 07:44:40.178894
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    seq = u'i am a unicorn'
    secret = 'secret'
    vault = VaultLib()
    encrypted_unicode_object = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert encrypted_unicode_object == seq


# Here is the order of the subclasses in this list:
# * The most specific subclass first
# * The most general subclass last
# * Subclasses of 'list' must be in the same order as subclasses of 'dict'
# * Subclasses of 'text_type' must be in the same order as subclasses of 'basestring'
#
# The order is used in AnsibleLoader when parsing YAML to assign
# the parent class that a subclass is based on.
#
# Note: str and bytes

# Generated at 2022-06-13 07:44:47.413649
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    '''
    Test if is_encrypted correctly detects encrypted or plaintext.
    '''
    plaintext = 'SECRET_PASSWORD'
    assert not AnsibleVaultEncryptedUnicode(plaintext).is_encrypted()

    # this is a trivial and probably invalid test, but good enough for now
    assert AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT').is_encrypted()


# This function will not be called directly from YAML, but
# go through the constructor AnsibleVaultEncryptedUnicode(ciphertext)
# which will set the vault attribute.

# Generated at 2022-06-13 07:44:51.743513
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    encrypted_unicode_1 = AnsibleVaultEncryptedUnicode.from_plaintext('A', None, None)
    encrypted_unicode_2 = AnsibleVaultEncryptedUnicode.from_plaintext('B', None, None)

    assert encrypted_unicode_1 != 'A'
    assert encrypted_unicode_2 != 'B'
    assert encrypted_unicode_1 != encrypted_unicode_2



# Generated at 2022-06-13 07:45:01.315210
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:08.242158
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode("test") == AnsibleVaultEncryptedUnicode("test")
    assert AnsibleVaultEncryptedUnicode("test") == "test"
    assert "test" == AnsibleVaultEncryptedUnicode("test")
    assert not AnsibleVaultEncryptedUnicode("test") == "tessit"
    assert not "tessit" == AnsibleVaultEncryptedUnicode("test")


# Generated at 2022-06-13 07:45:15.555706
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault
    secret = b'password'
    clear_text = 'hello'
    ciphertext1 = vault.encrypt(clear_text, secret)
    ciphertext2 = vault.encrypt(clear_text, secret)

    # unencrypted ciphertext is not encrypted
    plaintext = AnsibleVaultEncryptedUnicode(clear_text)
    assert not plaintext.is_encrypted()

    # encrypted ciphertext with ciphertext is encrypted
    encrypted = AnsibleVaultEncryptedUnicode(ciphertext1, vault, secret)
    assert encrypted.is_encrypted()

    # encrypted ciphertext with different ciphertext is encrypted
    encrypted = AnsibleVaultEncryptedUnicode(ciphertext2, vault, secret)
    assert encrypted.is_encrypted()



# Generated at 2022-06-13 07:45:26.023638
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    v = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n353837626231643264373430336363316666353937626662663163656139613366656537643762623\n332003161356539303832616235626264626131613236653034353665626638646262393131306334\n616630336233343838613466383362\n")

# Generated at 2022-06-13 07:45:35.075257
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vaultlib

    vault = vaultlib.VaultLib([])
    secret = vault.DEFAULT_PASSWORD

    clear = 'this is clear text'
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(clear, vault, secret)
    assert(encrypted.is_encrypted() == True)
    assert(encrypted.data == clear)
    assert(encrypted.is_encrypted() == False)
    assert(vault.is_encrypted(clear) == False)

_GLOBAL_DEFAULT_YAML_ROUNDTRIP_SAFE = True


# Generated at 2022-06-13 07:45:42.820690
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultError

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test',
                                                      vault=VaultLib(),
                                                      secret='test')
    assert avu.is_encrypted()

    # check the validation of vault obj
    with pytest.raises(AnsibleVaultError):
        AnsibleVaultEncryptedUnicode.from_plaintext('test',
                                                    vault=None,
                                                    secret='test')

# Generated at 2022-06-13 07:46:28.453069
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault = VaultLib('secret')
    secret = 'password'
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, secret)
    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext('boo', vault, secret)

    # true assumptions
    assert avu1 == avu2
    assert avu2 == avu1
    assert avu1 == 'foo'
    assert 'foo' == avu1
    assert avu2 == 'foo'
    assert 'foo' == av

# Generated at 2022-06-13 07:46:33.972369
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible_vault as vault
    # if self  vault is set
    if vault:
        # if self evaluates to other
        avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'secret')
        if 'test' == avu:
            # return true
            return True
    # else
    # return false
    return False


# Generated at 2022-06-13 07:46:41.675050
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    secret = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
    plaintext = u'\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004\u0004'

# Generated at 2022-06-13 07:46:46.050270
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'secret'
    plaintext = "this is a plaintext"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, VaultLib([], secret), secret)
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:46:48.808757
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode('1234')
    avu.vault = None

    assert(avu == '1234')
    assert(avu != '12345')

# Generated at 2022-06-13 07:46:55.136032
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """
    Test the method __ne__ of class AnsibleVaultEncryptedUnicode
    """
    avu1 = AnsibleVaultEncryptedUnicode("A")
    assert(avu1 != "A") == True

    avu2 = AnsibleVaultEncryptedUnicode("A")
    assert(avu2 != "A") == False


# Generated at 2022-06-13 07:46:56.260279
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    result = not AnsibleVaultEncryptedUnicode.__ne__(None, None)
    assert result



# Generated at 2022-06-13 07:47:03.748816
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    secret = 'test'
    vault = VaultLib(secret)
    plaintext = 'abc'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    string = 'abc'
    assert avu != string

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode___ne__()



# Generated at 2022-06-13 07:47:06.594586
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("foo", VaultLib(""), "")
    assert avu.data != "foo"


# Generated at 2022-06-13 07:47:15.301158
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.utils.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vault_secret = VaultSecret('my secret')

    avu = AnsibleVaultEncryptedUnicode.from_plaintext('my secret', VaultLib(), vault_secret)
    assert avu.is_encrypted()

    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;9.9;AES256')
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:48:27.613838
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert 'foo' == avu
    assert avu == 'foo'
    assert 'foo' != avu
    assert avu != 'foo'


# Generated at 2022-06-13 07:48:35.921762
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Compare the AnsibleVaultEncryptedUnicode object with a plain string (which is not encrypted)
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')