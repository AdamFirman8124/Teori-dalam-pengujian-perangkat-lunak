

# Generated at 2022-06-13 07:38:43.071724
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avue = AnsibleVaultEncryptedUnicode("foo")
    avue2 = AnsibleVaultEncryptedUnicode("foo")
    assert (avue != avue2)


# Generated at 2022-06-13 07:38:48.651628
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    assert (not AnsibleVaultEncryptedUnicode.__gt__(None))
    str_data = "ABC123"
    str_data_vault = AnsibleVaultEncryptedUnicode(str_data)
    assert (not AnsibleVaultEncryptedUnicode.__gt__(str_data_vault,None))
    assert (not AnsibleVaultEncryptedUnicode.__gt__(None,str_data_vault))
    assert (not AnsibleVaultEncryptedUnicode.__gt__(str_data_vault,str_data))

# Class that modifies yaml.Loader to output dictionaries that are subclasses of AnsibleMapping

# Generated at 2022-06-13 07:38:59.113022
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    plain_string = to_bytes('This is foo')
    plain_string_2 = to_bytes('This is bar')
    plain_string_3 = to_bytes('This is baz')
    plain_string_4 = to_bytes('This is qux')
    vault = VaultLib(['--vault-password-file', '/dev/null'])
    encrypted_string = AnsibleVaultEncryptedUnicode.from_plaintext(plain_string, vault, '/dev/null')
    encrypted_string_2 = AnsibleVaultEncryptedUnicode.from_plaintext(plain_string_2, vault, '/dev/null')

# Generated at 2022-06-13 07:39:08.831288
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    """
    Method find of class AnsibleVaultEncryptedUnicode should return a correct value.
    """
    secret = "secret"
    vault = yaml.AnsibleVault('secret')
    seq = "ansible-vault encrypted string"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert(avu.find(None) == -1)
    assert(avu.find("secret") == -1)
    assert(avu.find("ansible-vault encrypted string") == 0)
    assert(avu.find("ansible-vault encrypted string", 0, 6) == 0)



# Generated at 2022-06-13 07:39:18.485030
# Unit test for method count of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_count():
    # Example of expected usage
    from ansible.parsing.vault import VaultLib

    try:
        vault_pass = open('test_AnsibleVaultEncryptedUnicode_count.vault_passwd').read()
    except IOError:
        vault_pass = None
    vault = VaultLib(vault_pass)

    sequence = AnsibleVaultEncryptedUnicode.from_plaintext('abcabcabcabcabcabcabcabcabcabcabc', vault, vault_pass)

    assert(sequence.count('a') == 9)
    assert(sequence.count('a', 0, 6) == 2)
    assert(sequence.count('a', 0, 13) == 3)
    assert(sequence.count('a', 0, 9) == 3)

# Generated at 2022-06-13 07:39:25.651146
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():

    # Test for the case when the value of self.data is less than the value of
    # the string param.
    avue_string = AnsibleVaultEncryptedUnicode("abc")
    avue_string.vault = object()
    string = "def"
    assert avue_string.__lt__(string) is True

    # Test for the case when the value of self.data is equal to the value of
    # the string param.
    avue_string = AnsibleVaultEncryptedUnicode("abc")
    avue_string.vault = object()
    string = "abc"
    assert avue_string.__lt__(string) is False

    # Test for the case when the value of self.data is greater than the value of
    # the string param.
    avue_string = AnsibleVault

# Generated at 2022-06-13 07:39:35.196105
# Unit test for method __lt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___lt__():
    mystring = AnsibleVaultEncryptedUnicode('this is my password')

    assert mystring.__lt__('This is my password') == False
    assert mystring.__lt__('this is my password') == False
    assert mystring.__lt__('this is my password.') == True
    assert mystring.__lt__('this is my psssord.') == True
    assert mystring.__lt__('this is my psss word.') == True
    assert mystring.__lt__('') == False


# Generated at 2022-06-13 07:39:46.360324
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    vault_obj = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n32663666303639663866613261393132376237393961383537333734376261643939316466336139\n61636532623337356637353666323265383938353066616362793961393530366634656566313665\n6535333261393234320a393061376465663066616562393137393361383537336434353664353639\n32396438303864356262383435306661373337366635363766653538363630346530333163363236\n3035323761333933340a\n')
    vault_

# Generated at 2022-06-13 07:39:57.431038
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    avu_a = AnsibleVaultEncryptedUnicode("1")
    avu_b = AnsibleVaultEncryptedUnicode("2")
    avu_c = AnsibleVaultEncryptedUnicode("1")

    assert avu_a < avu_b
    assert avu_a <= avu_b

    assert avu_a < avu_c
    assert avu_a <= avu_c

    assert avu_b > avu_a
    assert avu_b >= avu_a

    assert avu_b > avu_c
    assert avu_b >= avu_c

    assert not avu_a > avu_b
    assert not avu_a > avu_c

    assert not avu_a > avu_c
    assert not avu_a

# Generated at 2022-06-13 07:40:06.015909
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.vars import vars_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    vault = VaultLib("mysecret")
    inven_loader = InventoryManager(loader=vars_loader, sources=['tests/vault/test_vault_var_precedence.yml'])
    vars_manager = VariableManager(loader=vars_loader, inventory=inven_loader)
    encrypted_vault_var_precedence_secret = vars_manager.get_vars()['encrypted_vault_var_precedence_secret']

# Generated at 2022-06-13 07:40:21.999777
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import copy
    import random

    # Create a dict with a string, a vault encrypted string and a non-string variable
    # Source: https://www.peterbe.com/plog/generate-test-data-python
    random.seed(1)
    data = dict(
        test_string="1234ABCD",
        test_vault=AnsibleVaultEncryptedUnicode.from_plaintext(
            seq='1234ABCD',
            vault=VaultLib(password='1234'),
            secret='1234')
    )
    data['test_dict'] = copy.deepcopy(data)

    # Make sure the test cases are formatted correctly

# Generated at 2022-06-13 07:40:33.236630
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    # No vault, so, encrypted
    plaintext = "123"
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, None, None)
    assert avu.is_encrypted()
    # No vault so, unencrypted
    ciphertext = "123"
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    assert not avu.is_encrypted()
    # With vault, encrypted and starts with vault header
    ciphertext = VaultLib.VAULT_HEADER_MARKER.encode('utf-8') + b'123'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    avu.vault = VaultLib()
    assert avu.is_encrypted()
   

# Generated at 2022-06-13 07:40:40.497123
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    password = 'passphrase'
    base_data = 'Test string'
    data = 'definitely encrypted {}'.format(base_data)
    vault = AnsibleVault(password)
    ciphertext = vault.encrypt(data)
    secret = AnsibleVaultEncryptedUnicode.from_plaintext(data, vault, password)
    assert base_data.encode('UTF-8') in ciphertext
    assert base_data in secret    # no vault object, not decrypted
    assert secret.data
    assert base_data in secret.data



# Generated at 2022-06-13 07:40:47.648781
# Unit test for method find of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_find():
    # find is not implemented.  There are two implementations:
    # 1. vault.decrypt ciphertext, pass decrypted plaintext to find
    # 2. Parse ciphertext, pass subsquent characters to find
    #
    # Below is and example of implentation 2, however, if the first characters of
    # the ciphertext match the plaintext, then this would fail.
    assert AnsibleVaultEncryptedUnicode(b'!vault |$ANSIBLE_VAULT;1.1;AES256\n\n-----BEGIN OPENSSH PRIVATE KEY-----\n...\n...\n...\n...\n-----END OPENSSH PRIVATE KEY-----\n').find('ssh') == 0



# Generated at 2022-06-13 07:40:50.768682
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    avu1 = AnsibleVaultEncryptedUnicode('123')
    avu2 = AnsibleVaultEncryptedUnicode('1234')
    assert avu1.__gt__(avu2) == False
    assert avu2.__gt__(avu1) == True
    assert avu1.__gt__('1234') == False
    assert '1234'.__gt__(avu1) == True


# Generated at 2022-06-13 07:40:55.239231
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    from ansible.parsing.vault import VaultLib

    secret = 'test'
    vault = VaultLib([])
    seq = 'first'
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
    assert encrypted > 'second'


# Generated at 2022-06-13 07:41:07.775401
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
    #
    # this method is called by the python interpreter when comparing for
    # inequality two AnsibleVaultEncryptedUnicode objects ('==' operator)
    from ansible.parsing.vault import VaultLib
    vault_secret = 'ansible'

    # create two different AnsibleVaultEncryptedUnicode objects,
    # one from a string and the other from a dict
    a1 = AnsibleVaultEncryptedUnicode.from_plaintext('secret_ansible', VaultLib(vault_secret), vault_secret)
    a2 = AnsibleVaultEncryptedUnicode.from_plaintext('secret_ansible', VaultLib(vault_secret), vault_secret)

    # both objects are different objects but their decrypted values

# Generated at 2022-06-13 07:41:10.189877
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    '''Test case for method __gt__ of class AnsibleVaultEncryptedUnicode.'''
    avueu_obj_1 = AnsibleVaultEncryptedUnicode('Test1')
    avueu_obj_2 = AnsibleVaultEncryptedUnicode('Test2')

    assert avueu_obj_1 > avueu_obj_2



# Generated at 2022-06-13 07:41:21.839049
# Unit test for method __gt__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___gt__():
    def setup():
        class AVault(object):
            def decrypt(self, value, obj):
                return to_bytes('1234')

            def is_encrypted(self, value):
                return True

        av = AVault()

        class AVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode): pass

        avu1 = AVaultEncryptedUnicode('abc')
        avu2 = AVaultEncryptedUnicode('1234')

        avu1.vault = av
        avu2.vault = av

        return avu1, avu2

    avu1, avu2 = setup()

    # case 1: data is always decrypted, although it is all encrypted
    assert(avu2 > '1233')
    assert(avu2 > avu1)

# Generated at 2022-06-13 07:41:29.613534
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import vault_manager as manager
    str1 = AnsibleVaultEncryptedUnicode('secret')
    str2 = AnsibleVaultEncryptedUnicode('secret')
    vault = VaultLib([])
    manager.decrypts.append(vault)
    str1.vault = vault
    str2.vault = vault
    # test if 'secret' is contained in str1
    assert 'secret' in str1

    # test if str2 is contained in str1
    assert str2 in str1


# Generated at 2022-06-13 07:41:43.174517
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    assert 'hello'.__add__('world') == 'helloworld'
    assert AnsibleVaultEncryptedUnicode('hello').__add__('world') == 'helloworld'
    assert AnsibleVaultEncryptedUnicode('hello').__add__(AnsibleVaultEncryptedUnicode('world')) == 'helloworld'
    assert AnsibleVaultEncryptedUnicode('hello').__add__(u'world') == 'helloworld'
    assert 'world'.__add__(AnsibleVaultEncryptedUnicode('hello')) == 'helloworld'
    assert u'world'.__add__(AnsibleVaultEncryptedUnicode('hello')) == 'helloworld'



# Generated at 2022-06-13 07:41:52.622851
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 07:42:02.752917
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:42:05.392344
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    e = AnsibleVaultEncryptedUnicode(b'foo')
    assert e.is_encrypted() == False


# Generated at 2022-06-13 07:42:11.283125
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    secret = 'test_AnsibleVaultEncryptedUnicode___contains__'
    ciphertext = b'vault encrypted string with $ANSIBLE_VAULT;1.1;AES256'
    avu = AnsibleVaultEncryptedUnicode(ciphertext)
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(password=secret)
    avu.vault = vault
    assert b"$" in avu



# Generated at 2022-06-13 07:42:15.956959
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    assert AnsibleVaultEncryptedUnicode('1') + ' 2' == '1 2'
    assert AnsibleVaultEncryptedUnicode('1') + AnsibleVaultEncryptedUnicode(' 2') == '1 2'
    assert AnsibleVaultEncryptedUnicode('1') + 2 == '12'
    assert 1 + AnsibleVaultEncryptedUnicode(' 2') == '12'


# Generated at 2022-06-13 07:42:20.157336
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # if __ne__() is not implemented, == is called on AnsibleVaultEncryptedUnicode
    # and the '==' operator on strings will return True if the strings are equal
    # as opposed to False if they are not equal.
    assert AnsibleVaultEncryptedUnicode('foo') != 'bar'



# Generated at 2022-06-13 07:42:35.349489
# Unit test for method __add__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___add__():
    # This method tests the __add__ method of the AnsibleVaultEncryptedUnicode class
    avu1 = AnsibleVaultEncryptedUnicode(to_bytes('$$$1'))
    avu2 = AnsibleVaultEncryptedUnicode(to_bytes('$$$'))
    avu3 = AnsibleVaultEncryptedUnicode(to_bytes('$'))
    avu4 = AnsibleVaultEncryptedUnicode(to_bytes('$$$'))
    avu5 = AnsibleVaultEncryptedUnicode(to_bytes('$$$'))
    avu6 = AnsibleVaultEncryptedUnicode(to_bytes('$$$'))
    avu7 = AnsibleVaultEncryptedUnicode(to_bytes('$$$'))
    avu8 = AnsibleV

# Generated at 2022-06-13 07:42:43.920190
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    import ansible.plugins.vault as vault
    _test_contains = lambda self, sub, expected: \
                     self.assertEqual(sub in self.avu, expected)
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('password', vault.VaultLib(), 'secret')
    t = type('Test', (object,), {'assertEqual':_test_contains})
    test = t()
    test.avu = avu
    test.assertEqual('a' in avu, False)
    test.assertEqual('p' in avu, True)
    test.assertEqual('sword' in avu, True)
    test.assertEqual('word' in avu, False)
    test.assertEqual('passwor' in avu, True)
    test

# Generated at 2022-06-13 07:42:54.650138
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    vault_text = '$ANSIBLE_VAULT;1.1;AES256;test\n363464376364376431376464353733646535376438343562366637643663643164393266333561\n3964333735643430623331623164663736366630653363313338343633\n'
    avu = AnsibleVaultEncryptedUnicode(vault_text)
    assert avu.is_encrypted() == True
    assert avu.data == u''
    avu.vault = VaultLib('test')
    assert avu.data == u''
    avu.vault = vault

# Generated at 2022-06-13 07:43:08.033203
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class TestVault(object):
        def __init__(self):
            self.password = 'pwd'

        def is_encrypted(self, value):
            return True

        def encrypt(self, value, secret):
            return 'encrypted'

        def decrypt(self, value, obj):
            return 'decrypted'

    tv = TestVault()
    str1 = AnsibleVaultEncryptedUnicode.from_plaintext('decrypted', tv, tv.password)
    str2 = 'decrypted'
    assert str1 != str2
    #str1 = AnsibleVaultEncryptedUnicode('encrypted')
    #str1.vault = tv
    #assert str1 != str2

# Generated at 2022-06-13 07:43:13.001836
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    sample_text = u'foo'
    vault = VaultLib('ansible')
    encrypted = AnsibleVaultEncryptedUnicode.from_plaintext(sample_text, vault, 'secret')
    assert(encrypted == sample_text)
    assert(encrypted != 'bar')



# Generated at 2022-06-13 07:43:17.402680
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    assert AnsibleVaultEncryptedUnicode.from_plaintext('foo', None, None) != 'foo'

# Add this here so we only pay for it if we are using the custom str subclasses

# Generated at 2022-06-13 07:43:22.721640
# Unit test for method __contains__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___contains__():
    # Test with AnsibleVaultEncryptedUnicode
    av = AnsibleVaultEncryptedUnicode()
    av.data = '11111'
    assert ('1' in av) == True
    assert ('2' in av) == False

    # Test with text string
    av.data = '22222'
    assert ('2' in av) == True
    assert ('3' in av) == False

    # Test with bytes string
    av.data = b'33333'
    assert ('3' in av) == True
    assert ('4' in av) == False
    print("Test method __contains__ of class AnsibleVaultEncryptedUnicode succeed.")


# Generated at 2022-06-13 07:43:28.048098
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    from ansible.parsing.vault import VaultLib

    secret = 'password'
    vault = VaultLib([])
    plaintext = 'hello'

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret)

    assert avu.__ne__(plaintext)



# Generated at 2022-06-13 07:43:37.734135
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    cipher_text = b'$ANSIBLE_VAULT;1.1;AES256\n31366466373664326134396138333338376437633562343166336438663831383666393933663661\n32393237633731613734326235393261356661623763326466653263643939353834646431353362\n61316336363833343037306336'
    vault_password = 'foo'
    vault = VaultLib([])
    avu = AnsibleVaultEncryptedUnicode(cipher_text)
    avu.vault = vault
    avu_plaintext = 'bar'
    assert(avu_plaintext == avu)

# Generated at 2022-06-13 07:43:44.319116
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    seq1 = "'foo bar'"
    seq2 = "'bar foo'"
    vault = None
    secret = None
    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext(seq1, vault, secret)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext(seq2, vault, secret)
    assert avu1.__ne__(avu2)
    assert avu1.__ne__(seq1)
    assert avu1.__ne__(seq2)
    assert avu2.__ne__(seq1)
    assert avu2.__ne__(seq2)



# Generated at 2022-06-13 07:43:50.170948
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:43:57.362389
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    '''
    Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode.
    :return: bool
    '''
    from ansible.parsing.vault import VaultLib

    plaintext = b'foo'

    vault = VaultLib([b'password'])
    assert AnsibleVaultEncryptedUnicode(plaintext).is_encrypted() is False
    assert AnsibleVaultEncryptedUnicode(vault.encrypt(plaintext)).is_encrypted() is True

    return True



# Generated at 2022-06-13 07:44:08.293178
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('hello', 'vault', 'secret')
    msg = 'Method __eq__ of class AnsibleVaultEncryptedUnicode does not respect the equality ' \
          'between a plaintext string and a AnsibleVaultEncryptedUnicode object encrypted with this plaintext string'
    assert 'hello' == avu, msg

    msg = 'Method __eq__ of class AnsibleVaultEncryptedUnicode does not respect the equality between a AnsibleVaultEncryptedUnicode ' \
          'object and another AnsibleVaultEncryptedUnicode object encrypted with the same string'
    assert avu == AnsibleVaultEncryptedUnicode.from_plaintext('hello', 'vault', 'secret'), msg


# Generated at 2022-06-13 07:44:23.774040
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    secret_key = b'123456'
    vault = yaml.vault
    plaintext = u'Hello world'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret_key)
    assert avu == plaintext
    assert avu != 'Hello'
    plaintext = 'Hello world'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret_key)
    assert avu == plaintext
    assert avu != 'Hello'
    plaintext = 'Hello world'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, vault, secret_key)
    assert avu != b'Hello world'


# Generated at 2022-06-13 07:44:31.557381
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    assert AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256!!!').is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256').is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('').is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('test').is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('test!!!').is_encrypted()
    assert not AnsibleVaultEncryptedUnicode('!!!').is_encrypted()


# Generated at 2022-06-13 07:44:42.778786
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib

    vault_password = 'ansible'
    secret = 'this is plaintext'

# Generated at 2022-06-13 07:44:47.535518
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    kwargs = dict(
        new_string='test',
        new_vault_id='id',
        new_vault_secret='secret',
    )
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(**kwargs)
    result = avu.__ne__('test')
    assert result == True


# Generated at 2022-06-13 07:44:54.240394
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():

    # same string, same object, both equal
    v1 = AnsibleVaultEncryptedUnicode("Z2F0ZSBkYXRhIQ==")
    v2 = AnsibleVaultEncryptedUnicode("Z2F0ZSBkYXRhIQ==")
    v1.data = "vault string"
    v2.data = "vault string"
    assert v1 == v2

    # same string, different objects, both equal
    v1 = AnsibleVaultEncryptedUnicode("Z2F0ZSBkYXRhIQ==")
    v2 = AnsibleVaultEncryptedUnicode("Z2F0ZSBkYXRhIQ==")
    v1.data = "vault string"
    v2.data = "vault string"
    assert v1 == v2

   

# Generated at 2022-06-13 07:45:05.601892
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:45:10.876934
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    # Call the class' __ne__ method using the class name with a test payload
    result = AnsibleVaultEncryptedUnicode.__ne__(AnsibleVaultEncryptedUnicode("test"), "test")
    # First we check that the result is a boolean
    assert type(result) == bool
    # We expect a result of True, as we're passing a payload that doesn't match the ciphertext.
    assert result


# Generated at 2022-06-13 07:45:15.072228
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode.from_plaintext(u'foo', 1, 2)
    assert avu != 'foo'
    # i.e, does __ne__ work without blowing up when it's called
    # with a plaintext string, and not an AnsibleVaultEncryptedUnicode
    # object?
    #
    # Answer: Yes, as long as avu.vault is not set, which is as it should be.



# Generated at 2022-06-13 07:45:22.000767
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.vault import VaultLib
    vault = VaultLib('test')
    secret = 'test'
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, secret)
    assert avu.data == 'test'
    assert avu == 'test'
    assert 'test' == avu
    assert avu == avu
    assert not avu == 'foobar'


# Generated at 2022-06-13 07:45:26.621182
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():

    import vault
    # Bad: no vault
    test = AnsibleVaultEncryptedUnicode("")
    assert not test.is_encrypted()

    # Good: some vault
    test = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256")
    test.vault = vault.VaultLib("notasecret", "yaml")
    assert test.is_encrypted()


# Generated at 2022-06-13 07:45:42.864543
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    assert AnsibleVaultEncryptedUnicode('abcdef') != 'abcdef'



# Generated at 2022-06-13 07:45:48.339570
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    avu = AnsibleVaultEncryptedUnicode('test')
    assert avu != 'test'
    avu.vault = 'test'
    assert avu != 'test'

    # when vault is set, __ne__ will return the ``__eq__`` results
    # this becomes a problem if the ``__eq__`` is overriden.
    avu.__class__.__eq__ = None
    avu.vault = 'test'
    assert avu != 'test'


# Generated at 2022-06-13 07:45:50.332760
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    obj = AnsibleVaultEncryptedUnicode('hello')
    assert obj != 'hello'


# Generated at 2022-06-13 07:45:58.500066
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    class TestVault(object):
        def __init__(self, password):
            self._password = password
        def encrypt(self, seq, secret):
            if len(seq) > 0:
                return to_bytes('abc')
            else:
                return to_bytes('')
        def decrypt(self, seq, obj=None):
            return to_text(seq)
        def is_encrypted(self, seq):
            return seq == to_bytes('abc')

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('x', TestVault(''), '')
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('x', TestVault(''), '')
    assert(avu1 != avu2)
    assert(avu1 != '')
   

# Generated at 2022-06-13 07:46:08.423415
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    secret = 'secret test'
    vault = VaultLib([])
    assert vault is not None
    # simple test on a simple text
    clear_text = 'abcd'
    ansible_vault_text = AnsibleVaultEncryptedUnicode.from_plaintext(clear_text, vault, secret)
    # check if we have the correct value
    assert clear_text == ansible_vault_text.data
    # check that the data is encrypted
    assert ansible_vault_text.is_encrypted() is True
    # test on multi line text
    clear_text = 'abcd\nabcd'
    ansible_vault_text = AnsibleVaultEncryptedUnicode.from_plaintext(clear_text, vault, secret)
    #

# Generated at 2022-06-13 07:46:20.291119
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    '''Test for method AnsibleVaultEncryptedUnicode.__ne__'''

    # TODO: Setup and test the following:
    # * ignore_me: The value to be compared against this one
    # * expected_result: The expected result of this comparison

    avu1 = AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault=None, secret=None)
    avu2 = AnsibleVaultEncryptedUnicode.from_plaintext('bar', vault=None, secret=None)

    assert avu1 != 'foo'
    assert avu1 != avu2



# Generated at 2022-06-13 07:46:21.979302
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    unencrypted = AnsibleVaultEncryptedUnicode('not encrypted')
    assert not unencrypted.is_encrypted()



# Generated at 2022-06-13 07:46:27.527841
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    a = AnsibleVaultEncryptedUnicode(u'abc')
    b = AnsibleVaultEncryptedUnicode(u'abc')
    assert not (a != b)
    b = AnsibleVaultEncryptedUnicode(u'abcd')
    assert a != b
    b = AnsibleVaultEncryptedUnicode(u'ab')
    assert a != b



# Generated at 2022-06-13 07:46:41.953242
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    import ansible.constants as C
    import textwrap

    class FakeVault(VaultLib):
        def __init__(self, secret, vault_id=None):
            self._vault_secret = secret
            self._vault_id = vault_id

        def decrypt(self, value, obj=None):
            if self._vault_id:
                return 'This is a test unencrypted text with __dict__.'
            else:
                return 'This is a test unencrypted text.'

        def encrypt(self, value, secret=None):
            pass

    plaintext = 'test'
    vault = FakeVault(secret='testvault')

    avu = AnsibleVaultEncryptedUnicode(plaintext)
    assert avu == plaintext



# Generated at 2022-06-13 07:46:48.848589
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    from ansible.parsing.vault import VaultLib
    # Create a VaultLib object
    vault = VaultLib([])

    # Create a AnsibleVaultEncryptedUnicode object
    avu = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')

    # Test is_encrypted()
    assert avu.is_encrypted()

    # Test is_encrypted() with missing vault attribute
    delattr(avu, 'vault')
    assert not avu.is_encrypted()


# Generated at 2022-06-13 07:47:27.336111
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:47:30.848459
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    assert not AnsibleVaultEncryptedUnicode.from_plaintext('foo', vault, 'test') == 'foo'


# Generated at 2022-06-13 07:47:37.556795
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    if 'AnsibleVaultLib' not in globals():
        pytest.skip('Cannot test AnsibleVaultEncryptedUnicode because "ansible.parsing.vault" is unavailable')
    assert AnsibleVaultEncryptedUnicode('foobar').is_encrypted() is False
    assert AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256').is_encrypted() is True



# Generated at 2022-06-13 07:47:48.206347
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    vault_password = 'mysecret'
    vault_data = 'mypassword'
    ciphertext = None
    plaintext = None
    encrypted = None

    # Test that __ne__ evaluates to True when comparing to a string object
    avu = AnsibleVaultEncryptedUnicode(vault_password)
    assert(avu != 'mypassword')

    # Test that __ne__ evaluates to True when comparing to a AnsibleVaultEncryptedUnicode object
    # that does not have a vault object associated
    avu = AnsibleVaultEncryptedUnicode(vault_password)
    avu2 = AnsibleVaultEncryptedUnicode(vault_password)
    assert(avu != avu2)

    # Test that __ne__ evaluates to True when comparing to a AnsibleVaultEncryptedUnicode object
   

# Generated at 2022-06-13 07:47:54.682281
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    from ansible.parsing.vault import VaultLib
    vault1 = VaultLib('password')
    vault2 = VaultLib('password')
    plaintext = 'hello'
    ciphertext = vault1.encrypt(plaintext)
    encrypted_unicode = AnsibleVaultEncryptedUnicode(ciphertext)
    encrypted_unicode.vault = vault2
    assert encrypted_unicode == plaintext


# Generated at 2022-06-13 07:48:03.314025
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    # Test with a plaintext
    plaintext = "plaintext"
    ciphertext = plaintext
    assert not AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()

    # Test with a ciphertext
    plaintext = "plaintext"
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    vault_password = "foo"
    ciphertext = vault.encrypt(plaintext, vault_password)
    assert AnsibleVaultEncryptedUnicode(ciphertext).is_encrypted()

#
# This is a PyYAML loader that outputs classes which are subclasses of the
# builtin types.  It also records where objects were loaded from, which can
# be used for more helpful error messages.
#


# Generated at 2022-06-13 07:48:13.732451
# Unit test for method is_encrypted of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode_is_encrypted():
    import base64
    from ansible.parsing.vault import VaultLib

    data = b'This is a secret'
    vault = VaultLib([])
    serialized_data = AnsibleVaultEncryptedUnicode.from_plaintext(data, vault, 'not_a_real_secret')

    assert serialized_data.is_encrypted()

    serialized_data.vault = None
    assert not serialized_data.is_encrypted()
    assert serialized_data.data == data

    # check that we can detect an encrypted payload
    serialized_data.data = vault.encrypted_data_prefix + base64.b64encode(serialized_data.data) + vault.encrypted_data_suffix.encode('utf8')
    assert serialized_data.is_encrypted()

# Generated at 2022-06-13 07:48:23.776869
# Unit test for method __ne__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___ne__():
    pass_secret = 'ansible'
    secret = to_bytes(pass_secret)
    vault = yaml.vault.VaultLib(secret)
    v1 = AnsibleVaultEncryptedUnicode.from_plaintext('test1', vault, secret)
    v2 = AnsibleVaultEncryptedUnicode.from_plaintext('test', vault, secret)

    assert(v1 != v2)
    assert(v2 != v1)
    assert(v1 != 'test1')
    assert('test1' != v1)
    assert(v2 != 'test')
    assert('test' != v2)


# Generated at 2022-06-13 07:48:29.606941
# Unit test for method __eq__ of class AnsibleVaultEncryptedUnicode
def test_AnsibleVaultEncryptedUnicode___eq__():
    import vaultlib

    vault = vaultlib.VaultLib('password')
    ciphertext = vault.encrypt('my data')
    avu = AnsibleVaultEncryptedUnicode.from_plaintext('my data', vault, 'password')

    assert ciphertext == avu
    assert avu == ciphertext
    assert avu == 'my data'
