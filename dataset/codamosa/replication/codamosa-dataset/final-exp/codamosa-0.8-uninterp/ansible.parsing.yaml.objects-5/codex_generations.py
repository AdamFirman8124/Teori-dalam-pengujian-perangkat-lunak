

# Generated at 2022-06-13 07:38:49.035014
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    if sys.version_info[0] >= 3:
        print("\nSKIPPED: Cannot run Python 2 test cases with Python 3 interpreter.\n")
        return

    from ansible.parsing.vault import VaultLib

    vault = VaultLib('123')
    t1 = u'123456789'
    t2 = u'abc'
    t3 = u'123abc'

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(t1, vault, secret='123')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(t2, vault, secret='123')
    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext(t3, vault, secret='123')


# Generated at 2022-06-13 07:38:57.203800
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    # Unencrypted unicode should not be able to be compared directly to encrypted unicode
    encrypted = AnsibleVaultEncryptedUnicode("This is secret")
    unencrypted = "This is secret"
    try:
        assert encrypted < unencrypted
    except TypeError:
        assert True
    else:
        assert False

    # Unencrypted unicode should be able to be compared directly to encrypted unicode
    unencrypted = u"This is not secret"
    assert unencrypted < encrypted

    # Unencrypted unicode should be able to be compared directly to unencrypted unicode
    assert unencrypted < unencrypted



# Generated at 2022-06-13 07:39:03.315088
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    u"Unit test for AnsibleVaultEncryptedUnicode.__gt__()"
    ansible_vault_string = AnsibleVaultEncryptedUnicode.from_plaintext(u'test', vault=None, secret=None)
    assert not ansible_vault_string > u'test'
    ansible_vault_string.vault = 42
    assert not (ansible_vault_string > u'test')
    ansible_vault_string_other = AnsibleVaultEncryptedUnicode.from_plaintext(u'foo', vault=None, secret=None)
    assert ansible_vault_string > ansible_vault_string_other
    assert not (ansible_vault_string_other > ansible_vault_string)


# Generated at 2022-06-13 07:39:13.687378
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:39:21.670628
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    import tempfile
    import os

    class MockVaultLib(object):
        def __init__(self, secret):
            self.secret = secret

        def encrypt(self, plaintext, secret):
            if secret and secret != self.secret:
                raise vault.AnsibleVaultError('Invalid secret given, unable to encrypt')
            return plaintext

        def decrypt(self, ciphertext, obj=None):
            return ciphertext

        def is_encrypted(self, data):
            return False

    secret = 'secret'
    vaultlib = MockVaultLib(secret)

    # Case 1
    password = AnsibleVaultEncryptedUnicode.from_plaintext('abcdefghijklmnopqrstuvwxyz', vaultlib, secret)
    substring = AnsibleVaultEncryptedUnicode.from_plain

# Generated at 2022-06-13 07:39:25.915610
# Unit test for method __le__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___le__():
    s = AnsibleVaultEncryptedUnicode("aaaaa")
    assert (s <= "aaaaa")
    assert (not s <= "aaaab")
    assert (s <= AnsibleVaultEncryptedUnicode("aaaaa"))
    assert (not s <= AnsibleVaultEncryptedUnicode("aaaab"))


# Generated at 2022-06-13 07:39:28.554389
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('password')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello', vault, 'password')
    assert avu != 'world'
    assert not(avu != 'hello')


# Generated at 2022-06-13 07:39:38.563291
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    expected = 'abc'
    secret = 'test'
    vault = VaultLib([], False)
    test_str = AnsibleVaultEncryptedUnicode.from_plaintext(expected, vault, secret)
    actual = test_str == expected
    assert actual
    actual = test_str == 'abcd'
    assert not actual
    actual = test_str == AnsibleVaultEncryptedUnicode.from_plaintext('abcd', vault, secret)
    assert not actual


# Generated at 2022-06-13 07:39:48.217800
# Unit test for method rfind of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_rfind():
    assert AnsibleVaultEncryptedUnicode('abc').rfind('c') == 2
    assert AnsibleVaultEncryptedUnicode('abc').rfind('d') == -1
    assert len(AnsibleVaultEncryptedUnicode('abc').rfind('c')) == 1
    assert AnsibleVaultEncryptedUnicode('abc').rfind('c') != 4
    assert AnsibleVaultEncryptedUnicode('abc').rfind('c') == 2

test_AnsibleVaultEncryptedUnicode_rfind()

if _sys.version_info[0] < 3:
    class AnsibleVaultEncryptedString(AnsibleVaultEncryptedUnicode):
        '''Same as AnsibleVaultEncryptedUnicode, but with a bytestring (str) data attribute'''


# Generated at 2022-06-13 07:39:59.547016
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    import vaultlib

    secret = 'secret'
    vault = vaultlib.VaultLib(password=secret)

    v = vault.encrypt('ansible')
    avu = AnsibleVaultEncryptedUnicode(v, vault, secret)
    avu.vault = vault
    assert avu.count('ansible') == 1
    assert avu.count('ansible',0,5) == 1
    assert avu.count('ansible',0,4) == 0
    assert avu.count('ansible',4,4) == 0
    assert avu.count('ansible',4,8) == 1
    assert avu.count('ansible',4) == 1
    assert avu.count('ansible',5) == 0
    assert avu.count('ansible',0,1) == 0

# Generated at 2022-06-13 07:40:14.759440
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    with open('/etc/ansible/roles/test/tests/test_loader.py') as f:
        shortData = f.read(100)
        longData = f.read()

    # data is regular UTF-8
    shortAVU = AnsibleVaultEncryptedUnicode(shortData)
    longAVU = AnsibleVaultEncryptedUnicode(longData)
    assert(shortAVU == shortData and longAVU == longData)

    # len is sufficient
    assert(shortAVU < longAVU)
    assert(longAVU > shortAVU)
    assert(not longAVU < shortAVU)
    assert(not shortAVU > longAVU)

    # check two identical files

# Generated at 2022-06-13 07:40:23.322157
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    a1 = AnsibleVaultEncryptedUnicode("abc")
    assert a1 < "abd"
    assert a1 < AnsibleVaultEncryptedUnicode("abd")
    assert a1 < "abd"
    assert not (a1 < "abc")
    assert not (a1 < AnsibleVaultEncryptedUnicode("abc"))
    assert not (a1 < u"abc")
    assert not (a1 < "abc")


# Generated at 2022-06-13 07:40:27.406436
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avue = AnsibleVaultEncryptedUnicode('foo')
    assert b'foo' != avue
    assert avue != b'foo'



# Generated at 2022-06-13 07:40:33.833360
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    a1 = AnsibleVaultEncryptedUnicode('atest')
    b1 = AnsibleVaultEncryptedUnicode('btest')
    assert a1 < b1

    a2 = AnsibleVaultEncryptedUnicode('btest')
    b2 = AnsibleVaultEncryptedUnicode('atest')
    assert not a2 < b2

# Generated at 2022-06-13 07:40:41.454506
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    test_var = AnsibleVaultEncryptedUnicode('kKj22zmhZFipCZmY2mlKiTfT8TKjzkJh')
    test_var.vault = 'Vault(password=None, settings=None)'
    assert test_var == 'db'
    assert test_var == AnsibleVaultEncryptedUnicode('db')
    assert test_var != 'kKj22zmhZFipCZmY2mlKiTfT8TKjzkJh'


# Generated at 2022-06-13 07:40:53.196544
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    # Given 2 AnsibleVaultEncryptedUnicode objects
    avue1 = AnsibleVaultEncryptedUnicode('foo')
    avue2 = AnsibleVaultEncryptedUnicode('foo2')

    # When we compare them
    actual = avue1 < avue2

    # Then we should get correct result
    assert actual

    # Given 2 AnsibleVaultEncryptedUnicode objects
    avue1 = AnsibleVaultEncryptedUnicode('foo2')
    avue2 = AnsibleVaultEncryptedUnicode('foo')

    # When we compare them
    actual = avue1 < avue2

    # Then we should get correct result
    assert not actual



# Generated at 2022-06-13 07:40:54.423429
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert '!' != AnsibleVaultEncryptedUnicode('!')


# Generated at 2022-06-13 07:40:57.382815
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('plaintext', vault.VaultLib(), 'secret')
    assert(avue.is_encrypted())



# Generated at 2022-06-13 07:41:09.094298
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault = None
    secret = 'somesecret'

    a = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;test_character_string', vault, secret)
    b = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;test_character_string', vault, secret)
    c = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;test_character_string', vault, secret)

    assert a == b
    assert a == c
    assert b == c

    assert a == 'test_character_string'
    assert b == 'test_character_string'
    assert c == 'test_character_string'

    assert a != 'different_character_string'
   

# Generated at 2022-06-13 07:41:10.566849
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass



# Generated at 2022-06-13 07:41:24.507276
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
   from ansible.parsing.vault import VaultLib
   from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
   
   # a vault with password "ansible"
   v=VaultLib("ansible")
   # encrypt the string "foo"
   e=AnsibleVaultEncryptedUnicode.from_plaintext("foo",v,"ansible")
   # set the vault
   e.vault=v
   # test if is_encrypted() returns True
   assert e.is_encrypted()

   # a vault with password "ansible"
   v=VaultLib("ansible")
   # encrypt the string "foo"
   e=AnsibleVaultEncryptedUnicode.from_plaintext("foo",v,"ansible")
   # set the vault
   e

# Generated at 2022-06-13 07:41:32.737169
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n3330643133656563383336303934353737653635363133663330373032333737356631316262633038\n3033643736306438303864356530646462383364346165636238653964356661396530623639333535\n363635303334653630333830383761646461306630333338663934\n'
    avu1 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    assert avu1 == avu2


# Generated at 2022-06-13 07:41:39.768727
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    avue2 = AnsibleVaultEncryptedUnicode.from_plaintext('test', None, None)
    assert avue == avue2
    assert avue == 'test'
    assert 'test' == avue
    assert avue != avue2[::-1]
    assert avue != 'atest'
    assert 'atest' != avue

if __name__ == '__main__':
    test_AnsibleVaultEncryptedUnicode___eq__()

# Generated at 2022-06-13 07:41:50.804377
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Given
    avu_1 = AnsibleVaultEncryptedUnicode(b'abc')
    avu_1.vault = None
    avu_2 = AnsibleVaultEncryptedUnicode(b'def')
    avu_2.vault = None

    # When
    avu_1_ne_avu_2 = avu_1.__ne__(avu_2)
    avu_1_ne_abc = avu_1.__ne__('abc')
    avu_1_ne_def = avu_1.__ne__('def')

    # Then
    assert avu_1_ne_avu_2 is True
    assert avu_1_ne_abc is False
    assert avu_1_ne_def is True


# Generated at 2022-06-13 07:41:57.911208
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    key = 'password'
    plaintext = 'secret'
    vault = vaultlib.VaultLib(key)
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, key)
    # Verify that the comparison with a non encrypted string fails
    try:
        encrypted != plaintext
        assert False, 'Expected that comparison between encrypted and plaintext are always False'
    except Exception:
        pass
    # Verify that the comparison with the encrypted string fails
    try:
        encrypted != encrypted
        assert False, 'Expected that comparison between encrypted and itself are always False'
    except Exception:
        pass


# Define a tag for AnsibleVaultEncryptedUnicode in order to be able to
# deserialize from yaml

# Generated at 2022-06-13 07:42:08.677100
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode(b'gAAAAABXRdsMkC1HJtO5Zjg0V5p5Otq3j0pUbFyDmX7v-8fumW4aKjQZJ4V7KKrm8aPWKVnwPJveuD7hi9vD8Wx4cjKQGZ1fw-c_w8=')

# Generated at 2022-06-13 07:42:16.690424
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    good_vault = VaultLib([])
    bad_vault = None

    # encrypted

# Generated at 2022-06-13 07:42:19.966695
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('testing', VaultLib(), '12345')
    assert avu.is_encrypted()



# Generated at 2022-06-13 07:42:35.141716
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import os
    import tempfile
    import shutil
    import vaultlib
    import crypt_helper
    import crypt

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 07:42:43.893547
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # The `__ne__` method of class `AnsibleVaultEncryptedUnicode` expects a
    # string to compare against.
    # It returns `True` if the string is not encrypted and `False` if it is.
    plaintext = 'plaintext'

# Generated at 2022-06-13 07:42:54.184102
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Arrange
    avu = AnsibleVaultEncryptedUnicode(u'foo')
    # Act

    # Assert
    assert avu != None



# Generated at 2022-06-13 07:43:06.119379
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:43:17.117319
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    if hasattr(_sys, 'pypy_version_info'):
        # skip this test, as it tries to import cryptography and PyPy might not be able to.
        return
    from ansible.parsing.vault import VaultLib

    secret = "foo"
    plaintext = "this is a secret string"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, VaultLib(_sys.stdin), secret)

    # when passwords match, the plaintext is revealed and compares equal
    assert avu != plaintext

    # when passwords don't match, avu is not decrypted and we fall back to the
    # ciphertext which comes out gibberish
    assert avu != "this is not a secret string"


# Generated at 2022-06-13 07:43:29.626862
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:43:39.048512
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # A AnsibleVaultEncryptedUnicode has a .vault attribute that can decrypt it
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('Hello World', vault=None, secret=None)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('Hello World', vault=None, secret=None)

    assert avu1 != avu2
    assert not (avu1 == avu2)



# Generated at 2022-06-13 07:43:45.874272
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('hello')
    assert (avu != 'hello')

    avu.vault = True
    assert (avu != 'hello')

    class FAKE():
        pass

    avu.vault = FAKE()
    assert (avu != 'hello')


# Generated at 2022-06-13 07:43:49.053720
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    s1 = AnsibleVaultEncryptedUnicode('secret')
    s2 = AnsibleVaultEncryptedUnicode('secret')

    assert s1 != s2

# Generated at 2022-06-13 07:43:58.726761
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test if AnsibleVaultEncryptedUnicode#__eq__ works with
    # a string as other parameter

    vault = vaultlib.VaultLib('abcdefghijklmnopqrstuvwxyz123456')
    secret = '123456789012345678901234'

# Generated at 2022-06-13 07:44:09.068699
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;5.5;0.5;test;test\n12345==\n') != 'test'
    assert AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;5.5;0.5;test;test\n12345==\n') != '12345=='
    assert AnsibleVaultEncryptedUnicode('12345==') != 'test'
    assert AnsibleVaultEncryptedUnicode('12345==') != '12345=='
    assert AnsibleVaultEncryptedUnicode('test') != 'test'
    assert AnsibleVaultEncryptedUnicode('test') != '12345=='



# Generated at 2022-06-13 07:44:18.437351
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    plaintext = u"foo"

# Generated at 2022-06-13 07:44:35.728962
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    obj = AnsibleVaultEncryptedUnicode.from_plaintext('TestClass', 'encrypt_string', '$ANSIBLE_VAULT;1.2;AES256;TestClassKey\nc2VjcmV0cw==\n')
    print('TestClass, is encrypted: ' + str(obj.is_encrypted()))
    obj = AnsibleVaultEncryptedUnicode('TestClass')
    print('TestClass, is encrypted: ' + str(obj.is_encrypted()))
    obj = AnsibleVaultEncryptedUnicode('TestClass')
    obj.vault = 'encrypt_string'
    print('TestClass, is encrypted: ' + str(obj.is_encrypted()))



# Generated at 2022-06-13 07:44:41.602366
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    v = VaultLib("ansible")
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext("test", v, b"test")
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext("test", v, b"test")
    assert avu1 != avu2



# Generated at 2022-06-13 07:44:50.514178
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultError

    # Create vault and secret
    vault = VaultLib()
    secret = VaultSecret('mysecret')

    # Create encrypted unicode
    seq1 = 'this is a secret'
    seq2 = 'this is a secret'
    seq3 = 'this is another secret'
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(seq1, vault, secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(seq2, vault, secret)
    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext(seq3, vault, secret)


# Generated at 2022-06-13 07:45:00.498663
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    v = VaultLib(VaultSecret("vault_password"))

    # __eq__() returns True when ansible_pos are equal in both AVUs
    a = AnsibleVaultEncryptedUnicode("plaintext")
    a.vault = v
    b = AnsibleVaultEncryptedUnicode("plaintext")
    b.vault = v
    assert a == b

    # __eq__() returns True when plaintext are equal in both AVUs
    a = AnsibleVaultEncryptedUnicode("plaintext")
    a.vault = v
    b = AnsibleVaultEncryptedUnicode("plaintext")
    assert a == b

    # __eq__() returns False when plaintext are not equal in

# Generated at 2022-06-13 07:45:10.948642
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing import vault
    vault_pass = 'ansible'
    vault_obj = vault. VaultLib(vault_pass)
    vault_obj.changed = True
    plaintext = 'The quick brown fox jumps over the lazy dog.'
    ciphertext = b"$ANSIBLE_VAULT;1.1;AES256\n[truncated for brevity]\n"

    # Test plaintext match
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault_obj, vault_pass)
    assert plaintext == avu == AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault_obj, vault_pass)
    assert not (plaintext != avu)

    # Test ciphertext match
    avu = AnsibleVaultEncryptedUnic

# Generated at 2022-06-13 07:45:22.505996
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import os
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY3
    secret = os.urandom(16)
    vault = VaultLib(1)
    vault.update(secret)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, secret)
    if PY3:
        avu2 = AnsibleVaultEncryptedUnicode('ciphertext')
    else:
        avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('test2', vault, secret)

    assert avu == 'test'
    assert avu != avu2


# Generated at 2022-06-13 07:45:26.684429
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo bar', None, None) != 'foo bar'
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo bar', None, None) == 'foo bar'



# Generated at 2022-06-13 07:45:37.896326
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''
    This test is all about testing method ``__ne__`` of class ``AnsibleVaultEncryptedUnicode``.
    And it is a edge case test for it.
    '''
    # create a AnsibleVaultEncryptedUnicode with a valid ciphertext
    # make class ``AnsibleVaultEncryptedUnicode`` work as it should in real life

# Generated at 2022-06-13 07:45:47.687367
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    def _test(vault, ciphertext, secret):
        try:
            plaintext = vault.decrypt(ciphertext, secret)
        except:
            plaintext = 'unknown'
        try:
            avu = AnsibleVaultEncryptedUnicode(ciphertext)
            avu.vault = vault
            avu_plaintext = avu

        except Exception as e:
            raise Exception('Ciphertext: %s, secret: %s, plaintext: %s, error: %s' % (ciphertext, secret, plaintext, e))
        return plaintext == avu_plaintext

# Generated at 2022-06-13 07:45:56.826262
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    '''Ensure that the AnsibleVaultEncryptedUnicode is_encrypted function works'''
    from ansible import vault
    import base64
    import os
    import random

    # test with key that's divisible by 3, which is a requirement of base64
    key = b'A' * random.randint(1, vault.VAULT_PASSWORD_MAX_LEN - 1)
    ciphertext = vault._encrypt_block(key, b'plaintext')

    # make sure that the decrypt routine works
    assert vault._decrypt_block(key, ciphertext) == b'plaintext'

    # make sure that the is_encrypted routine works on the ciphertext
    assert vault.is_encrypted(ciphertext)

    # make sure that data which is not a ciphertext fails the test
    assert not vault.is_encrypted

# Generated at 2022-06-13 07:46:11.819320
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    import sys

    if sys.version_info.major != 3:
        return True

    # Create a VaultLib object (vault)
    vault = VaultLib()

    # Create a VaultSecret object (secret)
    secret = VaultSecret('password')

    # Assert that inserting 'hashed password' into a vault object
    # raises an AnsibleVaultError -- it does
    try:
        vault.encrypt('hashed password', secret)
    except vault.AnsibleVaultError as e:
        assert str(e).startswith('Vault password must be unicode')

    if sys.version_info.major == 2:
        # Test convertion from unicode to str
        test_str = u

# Generated at 2022-06-13 07:46:26.399811
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    test_ciphertext = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          39313266633963336561636661653930303236333063363466623135613961343938326239356465\n          38303565663634653330353134326164643930353130653032653031323364356262636663396231\n          633530653231306130363264343463386132316535363432303465303538663930376634\n          "
    assert AnsibleVaultEncryptedUnicode.from_plaintext("foo", VaultLib(b'12345'), b'password').is_encrypted()
   

# Generated at 2022-06-13 07:46:36.613445
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    '''
    Calling AnsibleVaultEncryptedUnicode.is_encrypted() should return boolean.
    Trimming text (removing leading and trailing whitespaces) should not
    trigger a decryption.
    '''
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(yaml)
    vault_encrypted_str = vault.encrypt('foobar')
    assert vault_encrypted_str.startswith('$ANSIBLE_VAULT;')
    assert vault_encrypted_str.endswith('\n')

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    avu = AnsibleVaultEncryptedUnicode(vault_encrypted_str.strip())
    # call .is_encrypted()
    assert avu.is_encrypted() == True


# Generated at 2022-06-13 07:46:47.360701
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    def test_func(avu, result, secret):
        avu.vault.secret = secret
        assert(avu.__eq__(result) == True)

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import StringIO
    secret = '$ecret'
    vault = VaultLib([])
    vault.secret = secret
    vault.vault_password_file = StringIO(secret)
    vault.load()

    val = 'text'
    result = 'text'
    test_func(AnsibleVaultEncryptedUnicode.from_plaintext(val, vault, secret), result, secret)

    val = 'text'
    result = '$ecret'

# Generated at 2022-06-13 07:47:00.212395
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    # Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
    # with valid parameters.

    from ansible.utils.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    #creating sample Vault secret
    secret = VaultSecret('secretpassword')
    sampleString = 'sampletext'
    ansibleVaultString = AnsibleVaultEncryptedUnicode.from_plaintext(sampleString, VaultLib(), secret)

    #comparing sample plaintext string with encrypted version is equal
    assert ansibleVaultString.__eq__(sampleString) == True

    # Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
    # with invalid parameters.

   

# Generated at 2022-06-13 07:47:05.490839
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():

    from ansible.parsing.vault import VaultLib
    aveu = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.2;AES256;test123\n12345678901234567890123456789012\n")
    vault = VaultLib("ansible")
    vault.password = 'test123'
    aveu.vault = vault
    assert aveu.is_encrypted() == True

# Generated at 2022-06-13 07:47:14.390729
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../lib'))
    import vault


# Generated at 2022-06-13 07:47:25.020060
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode"""
    def __ne__(self, other, result):
        """Test method __ne__ for class AnsibleVaultEncryptedUnicode"""

# Generated at 2022-06-13 07:47:36.769956
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    s = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n32393061663464353136656466656564326262356239303664656231386136626130626338633034\n64303839646661633236326163333566346430393461623832613331333531653264333734666538\n33653665306666376462656632643732623361623634623035373561653732306266613833383234\n31353862313966393764646233333633326431316435396662363963373266633534386633366166\n62346536643433663961')
    s.vault = None

# Generated at 2022-06-13 07:47:43.158032
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import get_vault_secret

    ansiblevault = AnsibleVaultEncryptedUnicode.from_plaintext('a', get_vault_secret(None), None)
    assert text_type('a') == ansiblevault

    ansiblevault = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')
    assert text_type('a') != ansiblevault



# Generated at 2022-06-13 07:48:11.686299
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    plaintext = 'hello world'

# Generated at 2022-06-13 07:48:19.178871
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    ## Test with ansible_vault_lib set and encrypted value

    # Test with pyYaml and encrypted value
    fh = open("./test/files/vault_test_encrypted", "r")
    vault_eol_test = yaml.safe_load(fh)
    fh.close()
    assert isinstance(vault_eol_test["vault_test_encrypted_key"], AnsibleVaultEncryptedUnicode)
    assert vault_eol_test["vault_test_encrypted_key"].is_encrypted()

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:48:26.696477
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import ansible.parsing.vault as vault
    base_string = 'test_data'
    secret = 'secret'
    avu_1 = AnsibleVaultEncryptedUnicode.from_plaintext(base_string, vault, secret)
    avu_2 = AnsibleVaultEncryptedUnicode.from_plaintext(base_string, vault, secret)
    assert avu_1 == avu_2


# Generated at 2022-06-13 07:48:31.502013
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    test = AnsibleVaultEncryptedUnicode.from_plaintext('test', VaultLib(password=u'password'), 'mypassword')
    assert(test.is_encrypted() == True)
    assert(test.data == u'test')

