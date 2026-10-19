

# Generated at 2022-06-13 07:39:07.187017
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import ansible.parsing.vault as vault

# Generated at 2022-06-13 07:39:20.997822
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # test cases:
    # 1. ciphertext is a empty string
    # 2. ciphertext is a string not start with $ANSIBLE_VAULT
    # 3. ciphertext is a string start with $ANSIBLE_VAULT

    case_1 = AnsibleVaultEncryptedUnicode(b'')
    case_2 = AnsibleVaultEncryptedUnicode(b'hello')
    case_3 = AnsibleVaultEncryptedUnicode(b'$ANSIBLE_VAULT;9.9;AES256')

    if not case_1.is_encrypted():
        print('test case 1 failed')
    if not case_2.is_encrypted():
        print('test case 2 failed')
    if case_3.is_encrypted():
        print('test case 3 failed')


# Generated at 2022-06-13 07:39:28.943105
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Arrange
    avueu_1 = AnsibleVaultEncryptedUnicode(
        ciphertext='$ANSIBLE_VAULT;1.1;AES256\n'
        '356533613465363936353763363530373636666337623461633531353133356566346137333538\n'
        '353636313236646534306162383937663765633061306133393939333261396530353831636364\n'
        '6236393800\n'
    )

# Generated at 2022-06-13 07:39:33.702804
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test for equality for AnsibleVaultEncryptedUnicode with different attributes
    avu1 = AnsibleVaultEncryptedUnicode('hello world')
    avu1.ansible_pos = (1,1,1)

    avu2 = AnsibleVaultEncryptedUnicode('hello world')
    avu2.ansible_pos = (1,1,1)

    assert avu1 == avu2

    avu3 = AnsibleVaultEncryptedUnicode('hello world')
    avu3.ansible_pos = (1,1,2)

    assert avu1 != avu3

    # Test for equality for AnsibleVaultEncryptedUnicode with different data attribute
    avu1 = AnsibleVaultEncryptedUnicode('hello world')

# Generated at 2022-06-13 07:39:43.627182
# Unit test for method replace of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_replace():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('foo\nbar', vault=None, secret=b'blah')
    mapped = {}
    mapped['old'] = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault=None, secret=b'blah')
    mapped['new'] = AnsibleMapping()
    mapped['new']['_text'] = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault=None, secret=b'blah')
    mapped['new']['var'] = AnsibleMapping()
    mapped['new']['var']['_text'] = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault=None, secret=b'blah')

# Generated at 2022-06-13 07:39:51.130838
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing import vault
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Given a AnsibleVaultEncryptedUnicode object initialized with a ciphertext already decrypted
    avu = AnsibleVaultEncryptedUnicode('plain_text')
    avu.vault = vault.VaultLib([])

    # When avu is compared to a string that is not the decrypted text
    #avu == 'foo_bar'
    result = avu.__ne__('foo_bar')

    # Then the result is True
    assert result, "AnsibleVaultEncryptedUnicode.__ne__() != 'foo_bar' returns True"
    # Otherwise the result is False

# Generated at 2022-06-13 07:39:58.420788
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    # Test case 1:
    # Test data: 'abc'
    # Expected output: 1
    # Test case 2:
    # Test data: 'a'
    # Expected output: 0

    TEST_DATA = [('abc', 1), ('a', 0)]
    sut = AnsibleVaultEncryptedUnicode('xxx')

    for test in TEST_DATA:
        assert sut.count(test[0]) == test[1]



# Generated at 2022-06-13 07:40:06.582414
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:12.164098
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    ciphertext = b'$ANSIBLE_VAULT;1.2;AES256;foo;bar'
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([], True)
    secret = '5'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('plaintext', vault, secret)
    assert avu.__eq__('plaintext') == True


# Generated at 2022-06-13 07:40:24.098419
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:34.511347
# Unit test for method replace of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_replace():
    avue = AnsibleVaultEncryptedUnicode('abc')
    avue2 = AnsibleVaultEncryptedUnicode('b')
    avue3 = AnsibleVaultEncryptedUnicode('c')
    r = avue.replace(avue2, avue3)
    assert r.data == 'acc'


# Generated at 2022-06-13 07:40:39.875295
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # This test fails if ansible-vault is uninstalled
    # The test is here if someone wants to check the functionality
    # outside of the whole ansible-vault project.
    from ansible_vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.loader import AnsibleLoader

    # This is how a vault string looks in the final YAML file
    # !vault |
    #      $ANSIBLE_VAULT;1.1;AES256
    #      63376232663733393163636534663131353366343637663038616332306265376331666538353064
    #      333466396431666362333961336334383538656530646662396236336230

# Generated at 2022-06-13 07:40:48.016833
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    secret = "ansible"
    plaintext = "ansible"
    ciphertext = plaintext
    ciphertext = ["VFJAPgAAAAA2S2JrZXkAAAACaW5mbzEyMzQ1Njc4OTY1NA==\n"]
    class FooVault(object):
        def __init__(self, secret):
            self.secret = secret
            self.result = ciphertext[0]
        def encrypt(self, plaintext, secret=None):
            if secret and secret != self.secret:
                raise RuntimeError("secret not matching")
            return self.result
        def decrypt(self, ciphertext, obj=None):
            if self.secret:
                return plaintext
            else:
                return ciphertext

# Generated at 2022-06-13 07:40:51.920806
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    test_str = "test string"
    enc_str = AnsibleVaultEncryptedUnicode.from_plaintext(test_str, "dummy_vault", "test_password")
    assert enc_str.is_encrypted()


# Generated at 2022-06-13 07:40:58.766247
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    text = 'test'
    encrypted_unicode = vault.encrypt(text)
    avu_encrypted = AnsibleVaultEncryptedUnicode(encrypted_unicode)
    avu_encrypted.vault = vault
    assert avu_encrypted.is_encrypted()
    assert str(avu_encrypted) == text
    avu_text = AnsibleVaultEncryptedUnicode(text)
    avu_text.vault = vault
    assert not avu_text.is_encrypted()


# Generated at 2022-06-13 07:41:10.106793
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Create the encrypted string
    iv = b'\xef\xd3\x1c\xec\xb7\xfa\x9d\x47\xdf\x28\xc1\xcc\x7d\x88\x63\x96'
    salt = b'\x23\x1b\xa5\x0d\xce\x8d\x75\x74\x57\x0a\x9d\xe0\x37\x10\x1c\x52'

# Generated at 2022-06-13 07:41:21.805190
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    import random
    import string
    import crypt
    import unittest

    # Create an instance of crypt.AnsibleVaultAES256 that we can use
    # to create an instance of AnsibleVaultEncryptedUnicode with
    # data that can be compared for the test
    vault_aes = crypt.AnsibleVaultAES256()

    # Create two instances of AnsibleVaultEncryptedUnicode with
    # the same value but encrypted with different keys

# Generated at 2022-06-13 07:41:28.767667
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():

    # Create a AnsibleVaultEncryptedUnicode object with a Vault attribute
    avu = AnsibleVaultEncryptedUnicode('msg')
    avu.vault = MockVault(True)

    # Assert it does not equal 'data'
    assert avu != 'data'

    # Create another AnsibleVaultEncryptedUnicode object without Vault attribute
    avu_without_vault = AnsibleVaultEncryptedUnicode('msg')

    # Assert it is equal to 'msg'
    assert avu_without_vault != 'msg'


# Generated at 2022-06-13 07:41:38.532867
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('testvalue')

    # Test case 1: Method is_encrypted returns True for a vault
    # that was just created
    encrypted_str = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes('testvalue'), vault, 'testvalue')
    assert encrypted_str.is_encrypted()

    # Test case 2: Method is_encrypted returns False if the vault
    # has already been decrypted
    encrypted_str.data
    assert not encrypted_str.is_encrypted()

    # Test case 3: Method is_encrypted returns False after
    # encrypting a string
    encrypted_str.data = to_bytes('testvalue')
    assert not encrypted_str.is_encrypted()



# Generated at 2022-06-13 07:41:43.642295
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    r1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault=None, secret=None)
    r2 = AnsibleVaultEncryptedUnicode('foo')
    assert r2 == 'foo'
    assert r1 != 'foo'
    assert r1 != r2



# Generated at 2022-06-13 07:41:55.460916
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Test exception for undefined vault attribute
    with pytest.raises(AssertionError):
        # pylint: disable=protected-access
        avueu = AnsibleVaultEncryptedUnicode('test')
        assert avueu == 'test'

    # Test exception for undefined vault attribute
    with pytest.raises(AssertionError):
        # pylint: disable=protected-access
        avueu = AnsibleVaultEncryptedUnicode('test')
        assert avueu != 'test'

    # Test success for well defined vault attribute
    avueu = AnsibleVaultEncryptedUnicode('test')
    avueu.vault = vault.VaultLib(_secret='test')
    assert avueu == 'test'
    assert avueu != 'test2'



# Generated at 2022-06-13 07:42:00.958763
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert str(AnsibleVaultEncryptedUnicode('f8e9e9c0a7aefd700931933b6e1c6d83b6c26b6f3979a0f9c4f7cf0a54a4a0a4')) == 'foo'
    assert str(AnsibleVaultEncryptedUnicode('f8e9e9c0a7aefd700931933b6e1c6d83b6c26b6f3979a0f9c4f7cf0a54a4a0a4')) == 'foo'



# FIXME: ansible.yaml.* classes should be migrated to ansible.utils.unsafe_proxy

# Generated at 2022-06-13 07:42:11.504272
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    #type: () -> None
    test_avu = AnsibleVaultEncryptedUnicode("B\xBE\x03\xC3\xFB\xA7:\xDD\xB7\x87\x1B\xA0\xCA\x81\x90\xB2\xB9\x05\xF6\xC6\x1A\xAD\xA8\xE4\xAE\x9B\xF4\xE2\x81\xF8\xB4\xEBr\xe7\x15\xc9\x9em\x00\xd7\xc0)")
    assert test_avu != u"this is not equal"
    assert test_avu != AnsibleVaultEncryptedUnicode("this is not equal")

# Unit

# Generated at 2022-06-13 07:42:17.966803
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    def _test(expected, avu, other):
        test_case = "Assert '{}' == '{}'".format(avu, other)
        assert expected == (avu == other), test_case

    avu = AnsibleVaultEncryptedUnicode(b'foo')
    avu.vault = None

    _test(False, avu, 'bar')
    _test(False, avu, AnsibleVaultEncryptedUnicode(b'bar'))
    _test(True, avu, 'foo')
    _test(True, avu, AnsibleVaultEncryptedUnicode(b'foo'))


# Generated at 2022-06-13 07:42:21.990911
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode('a') != 'a'
    assert 'a' != AnsibleVaultEncryptedUnicode('a')
    assert AnsibleVaultEncryptedUnicode('a') == 'a'
    assert 'a' == AnsibleVaultEncryptedUnicode('a')

# Generated at 2022-06-13 07:42:37.156383
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    class VaultMock(object):
        def __init__(self, password='vault'):
            self.password = password
            self.is_encrypted = lambda x, y: True

        def encrypt(self, value, secret):
            return value + secret

        def decrypt(self, ciphertext, obj=None):
            return ciphertext + self.password

    vault = VaultMock()
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'vault')
    assert b'testvault' == avu.data
    assert avu == 'testvault'
    assert avu == avu
    assert avu == AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, 'vault')

    vault.is_encrypted = lambda x, y: False

# Generated at 2022-06-13 07:42:40.161509
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret = 'testsecret'
    sequence = 'testsequence'
    # Build vault object
    import ansible.parsing.vault as av
    vault = av.VaultLib(password='testsecret', salts='salt')

    encrypted_object = AnsibleVaultEncryptedUnicode.from_plaintext(sequence, vault, secret)
    assert encrypted_object == sequence
    assert not encrypted_object == 'incorrectsequence'


# Generated at 2022-06-13 07:42:43.629205
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode.from_plaintext('test', '', 'secret')
    b = AnsibleVaultEncryptedUnicode.from_plaintext('test', '', 'secret')
    assert a.__ne__(b) == False


# Generated at 2022-06-13 07:42:54.528787
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing import vault
    import random

    for _ in range(100):
        secret = 'password'
        plaintext = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        ciphertext = vault.VaultLib.encrypt(plaintext, secret)
        decrypted_ciphertext = vault.VaultLib.decrypt(ciphertext, secret)
        if isinstance(ciphertext, bytes):
            ciphertext = ciphertext.decode()
        # if not isinstance(plaintext, AnsibleVaultEncryptedUnicode):
            # import pdb; pdb.set_trace()
        # if not isinstance(ciphertext, AnsibleVaultEncryptedUnicode):
            # import pdb; pdb.set_trace

# Generated at 2022-06-13 07:43:06.120197
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    """
    This test will validate the __eq__ method of AnsibleVaultEncryptedUnicode class

    :return:
    """
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])

    obj1 = AnsibleVaultEncryptedUnicode.from_plaintext(u'Ansible', vault, u'test')
    obj2 = AnsibleVaultEncryptedUnicode.from_plaintext(u'Ansible', vault, u'test')

    assert obj1 == obj2

    obj2 = AnsibleVaultEncryptedUnicode.from_plaintext(u'Chef', vault, u'test')
    assert obj1 != obj2

    assert obj1 != u'Ansible'



# Generated at 2022-06-13 07:43:18.073829
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    plaintext1 = "Gugus"
    plaintext2 = "Gugus2"
    t1 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext1)
    t2 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext2)
    assert t1 == t1
    assert t2 == t2
    assert not t1 == t2
    assert not t2 == t1


# Generated at 2022-06-13 07:43:30.250165
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Pass in a unencrypted value
    avu = AnsibleVaultEncryptedUnicode(
        u'$ANSIBLE_VAULT;1.1;AES256\n393738306566663765363333653335623333633664613037383538336437306463316666396437\n37306534643631653730636330666465356664323333373337396565643831303831333261633562\n3664633039643565396638346536626533623330616365636162646233333633364303938643631\n303361623537353364353466643935663161636266373366\n')
    plaintext = u'hello'

# Generated at 2022-06-13 07:43:32.937290
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode(b'foo') != AnsibleUnicode('bar')


# Generated at 2022-06-13 07:43:36.193427
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('test')
    assert (avu != 'test') == False


# Generated at 2022-06-13 07:43:49.054755
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    # First test a none vault object
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('This is a test', None, '')
    assert(avue.__eq__('This is a test') == False)
    # Now use a real vault
    vault.password = 'password'
    avue = AnsibleVaultEncryptedUnicode.from_plaintext('This is a test', vault, '')
    assert(avue.__eq__('This is a test') == True)
    # Check a non match
    assert(avue.__eq__('This is not a test') == False)



# Generated at 2022-06-13 07:43:59.208415
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    secret = '$ANSIBLE_VAULT;1.1;AES256'
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n343932373164663634396637333739666165643738656435383464376130653530333266653938\n663839386634643530363963386639643236313835366162626365316334343931346130313835\n363234626538666163316530653163356538343530336565343733316663313635623431613337\n3662336531623239353663346333643430353634323637363531336537\n'
    avu

# Generated at 2022-06-13 07:44:09.398282
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # setup
    ciphertext = [
        '$ANSIBLE_VAULT;1.1;AES256',
        '62653734356537633763616363643738636537396338323234626465386337356634643866336465',
        '63623937393564343961386161663534623738383236646265363266653266643639376465373936',
        '653236',
        ''
    ]
    avu = AnsibleVaultEncryptedUnicode(to_bytes('\n'.join(ciphertext)))
    avu.vault = 'fake_vault'

    # run
    result = avu.__ne__('a')

    # assert
    assert result is True



# Generated at 2022-06-13 07:44:11.717586
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('encrypted_string')
    assert avu != 'plain_string'



# Generated at 2022-06-13 07:44:19.528665
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('sha256', 'my_secret')
    a = AnsibleVaultEncryptedUnicode.from_plaintext(u"this is a test", vault, 'my_secret')
    b = AnsibleVaultEncryptedUnicode.from_plaintext(u"this is a test", vault, 'my_secret')
    c = AnsibleVaultEncryptedUnicode.from_plaintext(u"this is a TEST", vault, 'my_secret')
    d = u"this is a test"
    assert a == b
    assert a == d
    assert a != c
    assert a != 1



# Generated at 2022-06-13 07:44:34.051450
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    # Checks if __eq__ works for AnsibleVaultEncryptedUnicode
    a = AnsibleVaultEncryptedUnicode("test")
    b = AnsibleVaultEncryptedUnicode("test")
    c = "test"
    if not (a == b):
        print("Incorrectly thinks that AnsibleVaultEncryptedUnicode is not equal to itself")
        print("a = ", a)
        print("b = ", b)
    elif not (a == c):
        print("Incorrectly thinks that AnsibleVaultEncryptedUnicode is not equal to an identical string")
        print("a = ", a)
        print("c = ", c)
    elif a == "not_equal":
        print("Incorrectly thinks that AnsibleVaultEncryptedUnicode is equal to a different string")


# Generated at 2022-06-13 07:44:59.439165
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # 1. is_encrypted should return False if no vault is provided
    avu = AnsibleVaultEncryptedUnicode(to_text('hello'))
    assert avu.is_encrypted() is False
    # 2. For testing, let's create a mock vault
    # TODO: use a proper fixture for mocking, see https://github.com/ansible/ansible/issues/27639
    from ansible.parsing.vault import VaultLib
    key = to_bytes('foo')
    vault = VaultLib(key)
    avu.vault = vault
    # 3. is_encrypted should return True when the encrypted ciphertext is provided
    ciphertext = vault.encrypt(to_text('hello'), key)
    avu = AnsibleVaultEncryptedUnicode(ciphertext)

# Generated at 2022-06-13 07:45:10.319490
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:23.497875
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:34.464524
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    vault = yaml.load("""\
    $ANSIBLE_VAULT;1.2;AES256
    30616233346236663839653737653832303635376238373436363337656339306338343232613431
    64663739353164326361333365313230346539363538333732393238663565373063663461
    """)
    plaintext = u'test'
    secret = u'foo'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)
    assert avu != plaintext


if __name__ == '__main__':
    import pytest
    sys.exit(pytest.main(args=[__file__]))

# Generated at 2022-06-13 07:45:44.949113
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib

    plain_text = 'my secret'
    encrypted_text = '$ANSIBLE_VAULT;1.1;AES256\n6334356436343764393032626432656332643332346463303863653130653562346461393638613861\n3634393735356238616135306432656466386232373038383938346365366161303662303361316361\n6635336166623438373335393366343737346564623565396131636164616566666237663562376132\n353961616265306438353438376331303433636633363131643533\n'
   

# Generated at 2022-06-13 07:45:46.821466
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode(to_bytes('ansible')).__eq__(u'ansible') is True


# Generated at 2022-06-13 07:45:56.045051
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    """Test method ``__ne__`` of class ``AnsibleVaultEncryptedUnicode``.

    Initialize the class object with the expected value.
    Test ``__ne__`` with a value equal to the expected value.
    Test ``__ne__`` with a value that is not equal to the expected value.

    Args:
        None

    Returns:
        None

    Raises:
        ``sys.exit`` if the test fails.
    """
    try:
        avu = AnsibleVaultEncryptedUnicode("sometext")
        assert avu != "othertext"
        assert not avu != "sometext"
    except AssertionError:
        _sys.exit("FAIL: test_AnsibleVaultEncryptedUnicode___ne__")
test_AnsibleVaultEncryptedUnic

# Generated at 2022-06-13 07:46:07.631337
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault.vault import VaultLib
    vaultLib = VaultLib()
    plaintext = 'test'
    vault_secret = 'vault_secret'

# Generated at 2022-06-13 07:46:18.778847
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault = VaultLib('s3kr1t')
    vault_string = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault=vault, secret='s3kr1t')
    assert(not (vault_string != vault_string.data))
    assert(vault_string != 'test')
    assert(not (vault_string != vault_string))



# Generated at 2022-06-13 07:46:26.084317
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    plaintext = 'mytext'
    secret = 'vault_secret'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, yaml.vault, secret)
    assert not avu == plaintext
    assert not avu == AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, yaml.vault, secret)


# Generated at 2022-06-13 07:46:41.995216
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    pass


# Generated at 2022-06-13 07:46:48.895362
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    plaintext1 = "abcdef12345"
    plaintext2 = "abcdef12345"
    plaintext3 = "abcdef1234567"
    plaintext4 = "abcdef12345"
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext1, vault=None, secret=None)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext2, vault=None, secret=None)
    avu3 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext3, vault=None, secret=None)
    avu4 = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext4, vault=None, secret=None)

    # Method __eq__ returns True only if both sides are an AnsibleVault

# Generated at 2022-06-13 07:46:54.321925
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    with pytest.raises(AssertionError):
        AnsibleVaultEncryptedUnicode.from_plaintext('woot', None, 'nofoo')
    v = VaultLib('password')
    u = AnsibleVaultEncryptedUnicode.from_plaintext('woot', v, 'foo')
    assert not (u == 'woot')

# Generated at 2022-06-13 07:46:57.336725
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    s = AnsibleVaultEncryptedUnicode(b'foobar')
    assert s != 'foo'
    assert s != 'foobar'
#

# Generated at 2022-06-13 07:47:03.708725
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault = VaultLib("mysecret")
    iv_bytes, salt_bytes, ciphertext = vault.encrypt("test string")

    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault

    assert avu.is_encrypted() is True


# Generated at 2022-06-13 07:47:12.172386
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    ''' is_encrypted() should return True iff content is a vault encrypted string '''

    # Test 1 - content = vault encrypted string
    try:
        from ansible.parsing.vault import VaultLib
    except ImportError:
        pass
    else:
        vault_file = '/tmp/ansible-vault-test-file'
        vault = VaultLib(['--vault-password-file', '%s' % vault_file])
        unencrypted_string = u'There once was a little boat'
        encrypted_string = vault.encrypt(unencrypted_string)

        # Create a "vault encrypted string" for testing
        content = AnsibleVaultEncryptedUnicode(encrypted_string)
        content.vault = vault

        # Test
        assert content.data == unencrypted_string

# Generated at 2022-06-13 07:47:15.975463
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('ansible')

    s = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, None)
    assert s == 'foo'

    s = AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None)
    assert s != 'foo'



# Generated at 2022-06-13 07:47:26.283987
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:47:26.910386
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    pass

# Generated at 2022-06-13 07:47:38.313967
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import vault

    ciphertext = b"$ANSIBLE_VAULT;1.1;AES256\n36333632613335383265376566643965666664333736643433313963343930333530326432346134\na\n"

    # Initialize an AnsibleVaultEncryptedUnicode
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = vault.VaultLib('hunter2')

    # Test method __eq__ with a AnsibleVaultEncryptedUnicode object
    # avu2 is initialized with the same password as avu
    avu2 = AnsibleVaultEncryptedUnicode(ciphertext)
    avu2.vault = vault.VaultLib('hunter2')
    assert avu == avu2

# Generated at 2022-06-13 07:48:03.044973
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Test 1
    test_cases = [
        ['$ANSIBLE_VAULT;1.1;AES256', True],
        # Test 2
        ['\n$ANSIBLE_VAULT;1.1;AES256\n', True],
        # Test 3
        ['\n$ANSIBLE_VAULT;1.1;AES256\n\n', True],
    ]
    for line_breaks_case in test_cases:
        test_case_ciphertext = line_breaks_case[0]
        encrypted_expected = line_breaks_case[1]

        avueu = AnsibleVaultEncryptedUnicode(test_case_ciphertext)
        encrypted_actual = avueu.is_encrypted()

# Generated at 2022-06-13 07:48:13.537461
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import unittest
    class AnsibleVaultEncryptedUnicodeSubclass(AnsibleVaultEncryptedUnicode):
        pass

    class TestAnsibleVaultEncryptedUnicode(unittest.TestCase):
        def test_bytestring_equal_bytestring_false(self):
            bytestring1 = text_type('bytestring1')
            bytestring2 = text_type('bytestring2')
            avu = AnsibleVaultEncryptedUnicode(bytestring1)
            self.assertFalse(avu.__eq__(bytestring2))

        def test_bytestring_equal_bytestring_true(self):
            bytestring = text_type('bytestring')
            avu = AnsibleVaultEncryptedUnicode(bytestring)


# Generated at 2022-06-13 07:48:19.396836
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Regression test for https://github.com/ansible/ansible/issues/31126
    # see also https://github.com/ansible/ansible/pull/31244
    try:
        yaml.load("""
            - !vault |
                $ANSIBLE_VAULT;1.1;AES256
                1234567890123456789012345678901234567890123456789012345678901234
        """, Loader=yaml.SafeLoader)
    except:
        pass
    # The vault object was not created.
    # No exception should have been thrown when calling is_encrypted()
    assert True

# Generated at 2022-06-13 07:48:24.858856
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    vault_text = AnsibleVaultEncryptedUnicode.from_plaintext('$ANSIBLE_VAULT;1.1;AES256', vault, 'password')
    assert vault_text.is_encrypted()



# Generated at 2022-06-13 07:48:34.812947
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode('test')
    ansible_vault_encrypted_unicode1 = AnsibleVaultEncryptedUnicode('test')
    ansible_vault_encrypted_unicode2 = AnsibleVaultEncryptedUnicode('test1')
    assert(ansible_vault_encrypted_unicode == ansible_vault_encrypted_unicode1)
    assert(ansible_vault_encrypted_unicode != ansible_vault_encrypted_unicode2)
    assert(ansible_vault_encrypted_unicode != 'test')

