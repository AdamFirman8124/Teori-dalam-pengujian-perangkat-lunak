

# Generated at 2022-06-13 07:38:53.345427
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    """
    Test method rfind of class AnsibleVaultEncryptedUnicode.
    The result of rfind should always be -1 since this class is initialized with a ciphertext,
    and a ciphertext is decrypted when data property is accessed, and
    this property is not used by rfind method.
    """
    assert -1 == AnsibleVaultEncryptedUnicode('A').rfind('A')



# Generated at 2022-06-13 07:39:04.034349
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    assert "ab".rfind("a") == 0
    assert "ab".rfind("b") == 1
    assert "ab".rfind("ab") == 0
    assert "ab".rfind("bc") == -1
    assert "ab".rfind("") == 2
    assert "".rfind("") == 0
    assert "".rfind("a") == -1
    assert "abc".rfind("") == 3
    assert "abcba".rfind("b") == 3
    assert "abc".rfind("bc") == 1
    assert "abcba".rfind("bc") == 1
    assert "abc".rfind("bcd") == -1
    assert "abc".rfind("abcd") == -1



# Generated at 2022-06-13 07:39:05.942054
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    text = 'My Secret Text'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(text, vault, 'password')

    assert avu.is_encrypted()

# Generated at 2022-06-13 07:39:14.324543
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    a = AnsibleVaultEncryptedUnicode('1234')
    assert a[0:0] == ''
    assert a[0:1] == '1'
    assert a[1:3] == '23'
    assert a[3:3] == ''
    assert a[-1:-1] == ''
    assert a[-1:] == '4'
    assert a[:-2] == '12'



# Generated at 2022-06-13 07:39:22.015777
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:39:27.122423
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault
    v = ansible.parsing.vault.VaultLib("password")
    avu = AnsibleVaultEncryptedUnicode.from_plaintext("val", v, "password")
    assert avu.is_encrypted()

    # is_encrypted should return false when .vault is None
    avu.vault = None
    assert not avu.is_encrypted()

# ===============================================================
# test helper methods


# Generated at 2022-06-13 07:39:30.737770
# Unit test for method __getslice__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___getslice__():
    # m = AnsibleVaultEncryptedUnicode("")
    assert isinstance(AnsibleVaultEncryptedUnicode("").__getslice__(0, 4), AnsibleVaultEncryptedUnicode)

try:
    from yaml import CSafeDumper as SafeDumper
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeDumper
    from yaml import SafeLoader



# Generated at 2022-06-13 07:39:39.329895
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    class Vault:
        def decrypt(self, *args, **kwargs):
            return 'abc'

        def encrypt(self, *args, **kwargs):
            raise NotImplementedError

    obj1 = AnsibleVaultEncryptedUnicode('abc')
    obj1.vault = Vault()
    obj2 = AnsibleVaultEncryptedUnicode('def')
    obj2.vault = Vault()

    assert obj1 < obj2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:39:48.694632
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    from collections import OrderedDict

    if _sys.version_info < (3, 3):
        from collections import UserDict as DictBase
    else:
        from collections import UserDict

        DictBase = (DictBase,)

    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    secret = b'secret'

    def make_vault(data):
        return AnsibleVaultEncryptedUnicode.from_plaintext(data, vault, secret)

    data = b'one'
    vault_one = make_vault(data)
    vault_two = make_vault(data * 2)
    assert vault_one < vault_two

    try:
        assert vault_one < data
    except AssertionError:
        pass

# Generated at 2022-06-13 07:40:00.055036
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    # Test PY2
    if _sys.version_info[0] == 2:
        # Test no vault
        v = AnsibleVaultEncryptedUnicode('test')
        assert(v.__eq__('test') is False)

        # Test with vault
        v = AnsibleVaultEncryptedUnicode('test')
        v.vault = VaultLib('hey')
        assert(v.__eq__('test') is True)

        # Test with vault and different
        v = AnsibleVaultEncryptedUnicode('test')
        v.vault = VaultLib('hey')
        assert(v.__eq__('something else') is False)

    # Test PY3

# Generated at 2022-06-13 07:40:15.415721
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.utils import vault

    plain_text = "This is a plain text"
    plaintext_value = AnsibleVaultEncryptedUnicode(plain_text)
    assert not plaintext_value.is_encrypted()

    vault_text = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          613333343233303234316333326564333637326534613335386538343139623537643066393932366\n          6562643362336365353837643635326564353765646630396132620a"
    vault_value = AnsibleVaultEncryptedUnicode(vault_text)
    assert vault_value.is_encrypted()


# Generated at 2022-06-13 07:40:27.328277
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import ansible.parsing.vault
    from ansible.parsing.vault import VaultLib

    vault_secret = '$ANSIBLE_VAULT;1.1;AES256\n30613363663036313430393537376130333038623733633461663134643536633963613737323563\n61313037366332306565303938303263316265303934366633386236616361326134623761323038\n333537306531373861\n' # $ANSIBLE_VAULT;1.1;AES256

# Generated at 2022-06-13 07:40:37.917508
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    input_str = 'my_super_secret'
    my_vault = VaultLib('abc')

    ciphertext = my_vault.encrypt(input_str)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = my_vault
    assert avu.is_encrypted() == True

    avu = AnsibleVaultEncryptedUnicode(input_str)
    avu.vault = my_vault
    assert avu.is_encrypted() == False

    assert AnsibleVaultEncryptedUnicode(input_str).is_encrypted() == False


# Generated at 2022-06-13 07:40:43.078527
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultEditor
    from io import StringIO
    from unittest import TestCase

    vault_editor = VaultEditor('test_secret')
    ciphertext_a = vault_editor.encrypt('test_cipher')
    ciphertext_b = vault_editor.encrypt('test_cipher')

    # note: str() generates PY2 unicode, on PY3 it generates str instead.
    # we use StringIO to fake a file with the encrypted data, so we cannot provide
    # a text_type to the constructor.
    avu_a_1 = AnsibleVaultEncryptedUnicode(None)
    avu_a_1.vault = vault_editor
    avu_a_1.data = ciphertext_a
    avu_a_2 = AnsibleVault

# Generated at 2022-06-13 07:40:48.621096
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=None, secret='test')
    sub = encrypted
    expected = 0
    actual = encrypted.rfind(sub)
    assert actual == expected


# Generated at 2022-06-13 07:40:57.419317
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    ''' tests that method rfind support a string and a AnsibleVaultEncryptedUnicode instance as argument '''

    from ansible.parsing.vault import VaultLib
    vault = VaultLib('dummypasswd', 'dummypasswd')
    ciphertext = vault.encrypt('abcdefg')
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    assert avu.rfind('a') == 0
    assert avu.rfind(avu[0]) == 0

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode_rfind()

# Generated at 2022-06-13 07:41:09.093285
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import AnsibleVaultError
    vault = VaultLib([VaultSecret(b'bar')])

    obj = AnsibleVaultEncryptedUnicode(vault.encrypt(b'foo'))
    assert obj.is_encrypted() is True

    obj = AnsibleVaultEncryptedUnicode(b'foo')
    assert obj.is_encrypted() is False


# Generated at 2022-06-13 07:41:17.196633
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    data = 'test'
    assert AnsibleVaultEncryptedUnicode(data).is_encrypted() == False

if __name__ == '__main__':
    # Run tests for method is_encrypted
    test_AnsibleVaultEncryptedUnicode_is_encrypted()
    print('Tests passed')
    sys.exit(0)

# Generated at 2022-06-13 07:41:24.326195
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible import vault
    import base64
    secret = 'testpassword'
    class_name = AnsibleVaultEncryptedUnicode.from_plaintext
    obj = class_name('abc', vault.VaultLib(secret), secret)
    assert obj.is_encrypted() == True
    obj = class_name(base64.b64decode('AQAAnw=='), vault.VaultLib(secret), secret)
    assert obj.is_encrypted() == False
    obj = class_name('', vault.VaultLib(secret), secret)
    assert obj.is_encrypted() == False


# Generated at 2022-06-13 07:41:33.146289
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'test-secret'

    plaintext = 'test1'
    vault = VaultLib('test/ansible_vault/test_vault.py')
    avu = AnsibleVaultEncryptedUnicode(vault.encrypt(plaintext, secret))
    avu.vault = vault
    assert avu.is_encrypted()

    plaintext = 'test2'
    vault = VaultLib('test/ansible_vault/test_vault.py')
    avu = AnsibleVaultEncryptedUnicode(vault.encrypt(plaintext, secret))
    avu.vault = vault
    assert avu.is_encrypted()

    plaintext = 'test3'

# Generated at 2022-06-13 07:41:42.162768
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode('foo')
    assert avu.__eq__('foo')


# Generated at 2022-06-13 07:41:52.192283
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault
    from ansible.parsing.vault import VaultLib
    from collections import namedtuple

    # this is an encrypted vault, it will *always* fail to encrypt
    dummy_vault = namedtuple('DummyVault', ['encrypt', 'decrypt', 'is_encrypted'])(
        lambda *args, **kwargs: None,
        lambda *args, **kwargs: None,
        lambda *args: True,
    )

    # bypass the encryption data check
    VaultLib.is_encrypted = lambda *args, **kwargs: True

    # Set vaults to use the dummy vault
    vault.get_vault_secrets = lambda *args, **kwargs: dummy_vault
    vault.get_vault_password = lambda *args, **kwargs: dummy

# Generated at 2022-06-13 07:41:59.043729
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test for scenario when the other object is not of type AnsibleVaultEncryptedUnicode
    assert (AnsibleVaultEncryptedUnicode.from_plaintext('value', None, None) != 'other')

    # Test for scenario when the other object is of type AnsibleVaultEncryptedUnicode
    assert (AnsibleVaultEncryptedUnicode.from_plaintext('value', None, None) != AnsibleVaultEncryptedUnicode.from_plaintext('other', None, None))


# Generated at 2022-06-13 07:42:07.648566
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(None)
    with vault.load('pass2') as f:
        plaintext = f.read()
    pass2_encrypted = vault.encrypt(plaintext, 'pass2')
    pass2_unicode = AnsibleVaultEncryptedUnicode(pass2_encrypted)
    assert pass2_unicode.is_encrypted()
    assert pass2_unicode == plaintext
    pass2_unicode.vault = vault
    assert not pass2_unicode.is_encrypted()
    assert pass2_unicode == plaintext



# Generated at 2022-06-13 07:42:16.144560
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    import sys

    vault = VaultLib('secret')
    ciphertext = vault.encrypt('mytest', 'mytest')

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    if avu == 'mytest':
        assert True
    else:
        assert False

    if avu == b'mytest':
        assert True
    else:
        assert False

    if avu == AnsibleVaultEncryptedUnicode(ciphertext):
        assert True
    else:
        assert False

    if avu == AnsibleVaultEncryptedUnicode(vault.encrypt('mytest', 'mytest')):
        assert True
    else:
        assert False


# Generated at 2022-06-13 07:42:24.937733
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('ansible')
    password = b'ansible'
    plaintext = b'This is an example'
    ciphertext = b'$ANSIBLE_VAULT;1.1;AES256\n313766636434323538326132623865666233616665613434623664333735393363366632369566\n653265643465663034353062343534333563336235333133336265360a34303165343561376139\n383932633762386566633761656134316662323237663832663366393832333237313661336565\n37666462316535343862303634653537\n'
    # Test

# Generated at 2022-06-13 07:42:39.469462
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode.__eq__(None, None) is False
    assert AnsibleVaultEncryptedUnicode.__eq__('abc', None) is False
    assert AnsibleVaultEncryptedUnicode.__eq__(None, 'abc') is False
    assert AnsibleVaultEncryptedUnicode.__eq__('abc', 'abc') is True
    assert AnsibleVaultEncryptedUnicode.__eq__('abcdefgh', 'abcdefgh') is True
    assert AnsibleVaultEncryptedUnicode.__eq__('abcdefgh', 'ABCDEFGH') is False
    assert AnsibleVaultEncryptedUnicode.__eq__('abcdefgh', 'abcdefhhh') is False

# Generated at 2022-06-13 07:42:48.355681
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    # Define a valid vault
    vault = VaultLib([])

    # Generate a ciphertext
    plain_text = 'this is plain text'
    secret = 'secret'
    ciphertext = vault.encrypt(plain_text, secret)

    # We should be able to create an AnsibleVaultEncryptedUnicode from the ciphertext
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert not avu.is_encrypted()

    # However, it should not be encrypted until we set the vault attribute
    avu.vault = vault
    assert avu.is_encrypted()


# Generated at 2022-06-13 07:42:57.186673
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    '''
    Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
    '''
    from ansible.parsing.vault import VaultLib
    from ansible.constants import DEFAULT_VAULT_ID_MATCH

    vault_password = 'foo'
    vault = VaultLib(vault_password)

    plaintext = 'plaintext'
    ciphertext = vault.encrypt(plaintext)

    avu_ciphertext = AnsibleVaultEncryptedUnicode(ciphertext)
    avu_ciphertext.vault = vault
    assert avu_ciphertext.is_encrypted()

    avu_plaintext = AnsibleVaultEncryptedUnicode(plaintext)
    avu_plaintext.vault = vault
    assert not avu_plaintext.is_

# Generated at 2022-06-13 07:43:05.339639
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;abcabcabcabcabcabcabcabcabcabcabc\ndGVzdA==')
    assert avu.is_encrypted()
    avu = AnsibleVaultEncryptedUnicode('dGVzdA==')
    assert not avu.is_encrypted()
    avu = AnsibleVaultEncryptedUnicode('')
    assert not avu.is_encrypted()


# Generated at 2022-06-13 07:43:24.333676
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Setup
    vault_pass = 'invalid_password'


# Generated at 2022-06-13 07:43:34.947884
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    vault_pass = VaultSecret('vault-pass')
    vault_id = 'sample'
    vault = VaultLib([vault_pass])
    plaintext = 'This is plaintext'

# Generated at 2022-06-13 07:43:42.196673
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    yaml_str = b"foo"

    class FakeVault:
        def __init__(self):
            pass
        def decrypt(self, str):
            return yaml_str

    v = FakeVault()
    ave = AnsibleVaultEncryptedUnicode.from_plaintext(yaml_str, v, None)
    assert(ave == yaml_str)
    assert(yaml_str == ave)
    assert(ave == AnsibleVaultEncryptedUnicode.from_plaintext(yaml_str, v, None))
    assert(AnsibleVaultEncryptedUnicode.from_plaintext(yaml_str, v, None) == ave)


# Generated at 2022-06-13 07:43:48.557967
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    """ Unit test for AnsibleVaultEncryptedUnicode.is_encrypted """
    # data_str is a one-line file and the below test will pass

# Generated at 2022-06-13 07:43:56.085946
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    secret = "ansible"
    plaintext = "Vault Text: Test"
    ciphertext = vault.encrypt(to_bytes(plaintext), secret)

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert(avu.is_encrypted())

    avu = AnsibleVaultEncryptedUnicode(to_bytes(plaintext))
    assert(not avu.is_encrypted())



# Generated at 2022-06-13 07:44:07.419465
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class TestVault(object):
        def decrypt(self, ciphertext):
            decrypted = "a"
            if ciphertext == "b":
                decrypted = "b"
            return decrypted

    testVault1 = TestVault()
    testVault2 = TestVault()

    avu1 = AnsibleVaultEncryptedUnicode("a")
    avu1.vault = testVault1

    avu2 = AnsibleVaultEncryptedUnicode("b")
    avu2.vault = testVault2

    assert avu1 == "a"
    assert "a" == avu1
    assert "a" == "a"
    assert avu1 == avu1
    assert avu1 == avu2
    assert avu2 == avu1



# Generated at 2022-06-13 07:44:14.101180
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib

    secret = b'foo'
    vault = VaultLib(b'foo')
    secret = vault.encrypt(b'test', secret)
    assert isinstance(secret, AnsibleVaultEncryptedUnicode)
    assert secret.is_encrypted() == True

    secret = b'secret'
    assert isinstance(secret, AnsibleVaultEncryptedUnicode)
    assert secret.is_encrypted() == False


# Generated at 2022-06-13 07:44:18.228360
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Test for method __ne__ (self: AnsibleVaultEncryptedUnicode, other: AnsibleVaultEncryptedUnicode) -> bool
    assert not (AnsibleVaultEncryptedUnicode('abc') !=
        AnsibleVaultEncryptedUnicode('abc'))



# Generated at 2022-06-13 07:44:33.076340
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import vaultlib
    my_vault = vaultlib.VaultLib(b'pa$sw0rd')

    # Test that __ne__ returns True when called with a non AnsibleVaultEncryptedUnicode object.
    # This is because we cannot decrypt the object without a vault.
    avu = AnsibleVaultEncryptedUnicode(my_vault.encrypt(u'hello world'))
    assert avu != u'hello world'

    # Test that __ne__ return True when called with an AnsibleVaultEncryptedUnicode object,
    # but with a different name.  This is because we cannot decrypt the object without a vault.
    avu = AnsibleVaultEncryptedUnicode(my_vault.encrypt(u'hello world'))

# Generated at 2022-06-13 07:44:35.193825
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    uni = AnsibleVaultEncryptedUnicode('test')
    assert ('test' == uni)


# Generated at 2022-06-13 07:44:48.739505
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(password='secret')

# Generated at 2022-06-13 07:44:56.522422
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    Test AnsibleVaultEncryptedUnicode.__eq__ returns true if
    the string data equals the AnsibleUnicode object data
    """
    vault_string_obj = AnsibleVaultEncryptedUnicode()
    vault_string_obj.vault = None
    vault_string_obj.data = "vault_string"

    string_obj = "vault_string"

    assert(vault_string_obj.__eq__(string_obj) == True)


# Generated at 2022-06-13 07:45:08.064473
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:10.914775
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    text_class = AnsibleVaultEncryptedUnicode('my_string')
    assert text_class != 'my_other_string'
    assert text_class != AnsibleVaultEncryptedUnicode('my_other_string')


# Generated at 2022-06-13 07:45:17.393085
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:26.995957
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    #import ansible_vault
    #from ansible_vault import Vault
    from ansible.parsing import vault as ansible_vault

    vault = ansible_vault.Vault('SECRET')
    plaintext = 'plaintext'
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n3239353262626138653435646631316336613335303961303733613761373533363533626361623566\n'

    plaintext_AVU = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, 'SECRET')
    ciphertext_AVU = AnsibleVaultEncryptedUnicode(ciphertext)
    ciphertext_AVU.vault = vault

    # Make sure the encryption works correctly


# Generated at 2022-06-13 07:45:38.192485
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import unittest
    import ansible.parsing.vault as vault

    def test_cmp(plaintext, ciphertext, passphrase, expected):
        avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault.VaultLib(passphrase), passphrase)
        assert compare(expected, avu == ciphertext)

    class AnsibleVaultEncryptedUnicodeTest(unittest.TestCase):
        def test___eq__(self):
            test_cmp('a', 'a', 'pass', True)
            test_cmp('a', 'a', 'other', False)
            test_cmp('a', 'b', 'pass', False)
            test_cmp('a', 'b', 'other', False)
            test_cmp('a', 'a\n', 'pass', False)


# Generated at 2022-06-13 07:45:44.232478
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Setup
    ciphertext = "Some random text"
    utf8_encoded_ciphertext = ciphertext.encode('utf-8')
    vault = MockVaultLib()
    # Execute
    actual = AnsibleVaultEncryptedUnicode(utf8_encoded_ciphertext)
    actual.vault = vault
    actual_result = actual != ciphertext
    # Verify
    assert actual_result == False


# Generated at 2022-06-13 07:45:51.349639
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    v = VaultLib("hunter2")

    u = "just some plaintext"
    avu = AnsibleVaultEncryptedUnicode(v.encrypt(u))
    avu.vault = v

    assert avu.is_encrypted()


# Generated at 2022-06-13 07:45:57.399922
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():

    # Python 3's default encoding is utf-8, even in our testing environment
    # which is simulating Python 2.7, so force us to use ascii
    import sys
    reload(sys)
    sys.setdefaultencoding('ascii')

    import vaultlib
    v = vaultlib.VaultLib([])
    s = AnsibleVaultEncryptedUnicode.from_plaintext('foooo', v, '1234')

    assert s.is_encrypted() == True
    assert isinstance(s, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 07:46:10.538743
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """Test the method __eq__ of class AnsibleVaultEncryptedUnicode.
    We just test the case where self.vault is None, as it is the most likely case to happen."""
    avu = AnsibleVaultEncryptedUnicode('cipheredtext')
    result = avu.__eq__('plaintext')
    assert not result, "AnsibleVaultEncryptedUnicode.__eq__ doesn't work for ciphertext with no vault."



# Generated at 2022-06-13 07:46:21.522271
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu1 = AnsibleVaultEncryptedUnicode(b'foo')
    avu2 = AnsibleVaultEncryptedUnicode(b'foo')
    avu3 = AnsibleVaultEncryptedUnicode(b'bar')
    assert avu1 == avu1
    assert avu1 == avu2
    assert avu1 == 'foo'
    assert avu2 == avu1
    assert avu2 == 'foo'
    assert avu1 != 'bar'
    assert avu1 != avu3
    assert 'foo' != avu3


# Generated at 2022-06-13 07:46:31.933159
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    import re
    # base64 pattern
    base64_pattern = re.compile(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$')

    test_str = 'test'
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode.from_plaintext(test_str, VaultLib(), None)
    assert not ansible_vault_encrypted_unicode.is_encrypted()
    assert ansible_vault_encrypted_unicode.data == test_str

    ansible_vault_encrypted_unicode_with_vault = AnsibleV

# Generated at 2022-06-13 07:46:44.970471
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class MyVault:
        def decrypt(self, text):
            return to_text(text)

        def encrypt(self, text):
            return to_bytes(text)

        def is_encrypted(self, text):
            return True
    my_vault = MyVault()
    avu1 = AnsibleVaultEncryptedUnicode('hello test 1')
    avu2 = AnsibleVaultEncryptedUnicode('hello test 2')
    avu1.vault = my_vault
    avu2.vault = my_vault

    assert (avu1 == 'hello test 1')
    assert (not avu1 == 'hello test 2')
    assert (not avu1 == avu2)



# Generated at 2022-06-13 07:46:49.612098
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    obj = AnsibleVaultEncryptedUnicode("test")
    assert obj == "test"
    obj = AnsibleVaultEncryptedUnicode("test")
    assert not obj == "foo"
    bobj = AnsibleVaultEncryptedUnicode("test")
    assert bobj == bobj
    assert not obj == bobj
    assert not obj == None


# Generated at 2022-06-13 07:47:01.647947
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    unencrypted_text = 'foo'

# Generated at 2022-06-13 07:47:09.889851
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('mysecret')
    # No vault attribute
    avu_no_vault = AnsibleVaultEncryptedUnicode('test')
    assert not avu_no_vault.is_encrypted()
    # Encrypted
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault,'mysecret')
    assert avu.is_encrypted()
    # Not encrypted
    avu = AnsibleVaultEncryptedUnicode('test')
    assert not avu.is_encrypted()
    # Not encrypted
    avu = AnsibleVaultEncryptedUnicode('!vault|2|2')
    assert not avu.is_encrypted()


# Generated at 2022-06-13 07:47:12.913849
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode('foo') != 'bar'
    assert AnsibleVaultEncryptedUnicode('foo') != 'foo'


# Generated at 2022-06-13 07:47:19.592839
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import os

    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import VaultPassword

    # ensure we use a temporary directory to work in, so we don't
    # mess up any existing ansible installation
    test_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vaults')
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)

    # randomize the vault test filename
    filename = os.path.join(test_dir, 'test_ansible_vault_string.yml')

    secret = VaultSecret('password')
    vault = VaultLib([secret])

# Generated at 2022-06-13 07:47:25.215783
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Create an instance of AnsibleVaultEncryptedUnicode with vault set to None
    avu = AnsibleVaultEncryptedUnicode('test_string')
    avu.vault = None

    # Assert that __eq__ returns False
    assert not avu.__eq__('test_string')

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])

# Generated at 2022-06-13 07:47:38.761228
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class MockVault(object):
        def __init__(self, secret='ansible'):
            pass

        def is_encrypted(self, ciphertext):
            return True

        def decrypt(self, ciphertext):
            if isinstance(ciphertext, text_type):
                return text_type(ciphertext)
            return ciphertext.decode('utf-8')

        def encrypt(self, plaintext):
            if isinstance(plaintext, text_type):
                return plaintext.encode('utf-8')
            return plaintext

    vault = MockVault(secret='ansible')

    a = AnsibleVaultEncryptedUnicode.from_plaintext('ansible', vault, 'ansible')
    b = AnsibleVaultEncryptedUnicode('ansible')
    b.vault = vault
   

# Generated at 2022-06-13 07:47:49.840695
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEditor

    vault = VaultLib([])
    secret = VaultSecret([])

    # Whole encrypted string is in single line

# Generated at 2022-06-13 07:47:57.760237
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    # Test that a value that matches the AnsibleVaultEncryptedUnicode will return True
    aveu = AnsibleVaultEncryptedUnicode('test')
    assert 'test' == aveu

    # Test that a value that does not match the AnsibleVaultEncryptedUnicode will return False
    assert 'pass' != aveu

    # Test that a value that does not match the AnsibleVaultEncryptedUnicode will return False
    aveu_bytes = AnsibleVaultEncryptedUnicode(b'test')
    assert b'pass' != aveu_bytes



# Generated at 2022-06-13 07:48:02.133873
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.module_utils.vault import VaultLib

    vault = VaultLib('foo')
    secret = 'this_is_the_secret'

    seq = 'this is an unencrypted string'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)

    assert avu.is_encrypted()



# Generated at 2022-06-13 07:48:12.862650
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    with open("test_AnsibleVaultEncryptedUnicode___eq__.yaml", "r") as yaml_input:
        utilities = yaml.load(yaml_input, Loader=yaml.FullLoader)
    class FakeVault:
        def __init__(self, secret):
            self._secret = secret
        def encrypt(self, plaintext, _secret=None):
            if _secret is None:
                _secret = self._secret
            return "vault-cipher-text"
        def decrypt(self, ciphertext, _secret=None):
            if _secret is None:
                _secret = self._secret
            return "vault-plain-text"
        def is_encrypted(self, data):
            return True

# Generated at 2022-06-13 07:48:15.829330
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    s = AnsibleVaultEncryptedUnicode('randomstring of random length')
    vault = VaultLib('randompassword')
    s.vault = vault
    assert 'randomstring' != s


# Generated at 2022-06-13 07:48:25.649368
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('abcdef')
    avu.vault = VaultLib('abcdef')
    assert avu != ''
    assert avu != 'abcdef'
    assert avu != AnsibleVaultEncryptedUnicode('abcdef')
    assert avu != AnsibleVaultEncryptedUnicode('abcdef')
    assert avu != AnsibleVaultEncryptedUnicode('abc')
    assert avu != u'abc'
    assert avu != b'abc'
    assert avu != 'abc'

