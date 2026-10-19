

# Generated at 2022-06-22 11:50:46.467467
# Unit test for function do_unvault
def test_do_unvault():

    secret = 'mysecret'
    vaultid = 'filter_default'

    data = 'myvaultdata'
    vault = do_vault(data, secret, vaultid=vaultid, wrap_object=False)
    decrypteddata = do_unvault(vault, secret, vaultid=vaultid)
    assert data == decrypteddata

    data = 'myvaultdatasalt'
    vault = do_vault(data, secret, salt='salt', vaultid=vaultid, wrap_object=False)
    decrypteddata = do_unvault(vault, secret, vaultid=vaultid)
    assert data == decrypteddata

# Generated at 2022-06-22 11:50:55.798690
# Unit test for function do_vault
def test_do_vault():
    ''' function do_vault test'''

# Generated at 2022-06-22 11:50:56.902741
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, None) == None

# Generated at 2022-06-22 11:51:05.607522
# Unit test for function do_unvault
def test_do_unvault():
    """Test that the unvault filter works properly"""
    filtered_data = do_unvault("$ANSIBLE_VAULT;1.1;AES256\r\n3530326163303564373736663037636636336326662633666373061663337653162316662326563\r\n33306639646461613735633662306439666431353065326363633635356262636630343663346164\r\n3035656665\r\n", "my_secret")
    assert filtered_data == "my_data"



# Generated at 2022-06-22 11:51:09.864484
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.2;AES256;test_id;test_fake_key\n61646d696e0a', 'test_key') == 'admin'


# Generated at 2022-06-22 11:51:20.392497
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'
    vaultid = 'filter_default'

    # Test with a simple string
    string = 'string'
    result = do_unvault(string, secret, vaultid)
    assert result == 'string'

    # Test with an encrypted string

# Generated at 2022-06-22 11:51:24.858732
# Unit test for function do_vault
def test_do_vault():
    vault_filter = FilterModule()
    filters = vault_filter.filters()
    result = filters.get('vault')('ansible', 'ansible')
    assert '$ANSIBLE_VAULT;1.1;AES' in result


# Generated at 2022-06-22 11:51:32.097810
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Template
    t = Template('{{ "foo" | vault("password") }}')

# Generated at 2022-06-22 11:51:42.978224
# Unit test for function do_vault
def test_do_vault():
    secret = "test"
    data = "Test Data"
    assert do_vault(data, secret) == '$ANSIBLE_VAULT;1.2;AES256;default\n613237613161333132314565313736643466656134306632313330663166663033383439326331363035\n39623033653136623634376637323066643733326163386265396262320a343735303834383638373966\n363561383236643263663165373263356239666139323961366131616236636564386638616531373065\n356534393064363365646535310a'


# Generated at 2022-06-22 11:51:48.063115
# Unit test for function do_vault
def test_do_vault():
    """
    Proper usage of the do_vault() method.
    """
    vault = do_vault('this_is_a_secret', 'this_is_a_secret_too')
    assert is_encrypted(to_bytes(vault))



# Generated at 2022-06-22 11:52:02.566652
# Unit test for function do_unvault
def test_do_unvault():
    secret = "test"
    vaultid = "test"

# Generated at 2022-06-22 11:52:07.678188
# Unit test for function do_vault
def test_do_vault():
    secret = "my_secret_password"
    data = "[my_secret_data]"

    test = do_vault(data, secret)
    assert is_encrypted(test)


# Unit test function do_unvault

# Generated at 2022-06-22 11:52:15.161428
# Unit test for function do_vault
def test_do_vault():
    data = 'mySecret'
    secret = 'myPassword'
    salt = 'salt_string'
    vaultid = 'filter_default'
    wrap_object = True

# Generated at 2022-06-22 11:52:25.688536
# Unit test for function do_vault
def test_do_vault():
    secret = '$2a$12$jvvz0M1reZtcU5j6UJNfbuGw4UOCo6xH/c3/B3I5Sgk9E5RkhfBxe'
    clear_text = 'this is clear text'

# Generated at 2022-06-22 11:52:34.300686
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:38.504942
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('Hello World!', 'secret123')

# Generated at 2022-06-22 11:52:51.358527
# Unit test for function do_vault
def test_do_vault():
    import ansible.compat.tests.mock as mock

    filters = FilterModule()

    def setup(secret, data):
        m = mock.mock_open()
        with mock.patch('ansible.module_utils.basic.open_file', m, create=True):
            return filters.filters()['vault'](data, secret)


# Generated at 2022-06-22 11:53:02.248892
# Unit test for function do_vault
def test_do_vault():
    secret = 'my secret'
    data = 'my data'
    expected = '$ANSIBLE_VAULT;1.2;AES256;foo\n333163656666303162356134313233353733333734323131626130373539646636356566656663390a32653038313564316231356461303664343735643338393631633835633034373035633237\n'

    actual = do_vault(data, secret, salt='foo', vaultid='foo')
    assert expected == actual, "Vaulting data expected: %s, got: %s" % (expected, actual)



# Generated at 2022-06-22 11:53:05.640617
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:16.181925
# Unit test for function do_vault
def test_do_vault():
    ''' this is a test for do_vault '''

# Generated at 2022-06-22 11:53:26.755144
# Unit test for function do_vault
def test_do_vault():
    foo = FilterModule()
    assert foo.filters()['vault']('test stuff', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n30610231636133656263646233343436303537333464363934646637373966303632303531376266\n37346361646235326534333530636337373764306638393866386234313233393733393830353536\n653138343633\n'


# Generated at 2022-06-22 11:53:35.685556
# Unit test for function do_unvault
def test_do_unvault():
    test_secret = 'testsecret'
    test_vault = '$ANSIBLE_VAULT;1.2;AES256;linux\r\niMJr0Y9M9D/jTvqf3Nq/gQ==\r\n2jw/sz6Ug71/9XV7OuL/Pg==\r\n'
    test_vault_expected_decrypted = u'test_data'
    assert test_vault_expected_decrypted == do_unvault(test_vault, test_secret)



# Generated at 2022-06-22 11:53:43.708550
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("password", "secret", salt="salt") == '$ANSIBLE_VAULT;1.1;AES256;salt\r\ndmF1bHRwYXNzd29yZAo=\r\n'
    assert do_vault("password12345678901234567890123456789", "secret", salt="salt") == '$ANSIBLE_VAULT;1.1;AES256;salt\r\nZm9vYmFyMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwCg==\r\n'


# Generated at 2022-06-22 11:53:53.465121
# Unit test for function do_vault
def test_do_vault():
    # Correct case
    assert do_vault(data='aabb', secret='secret', vaultid='filter_default') == '$ANSIBLE_VAULT;1.1;AES256;filter_default\n3063306234386637353030623834366637303534663864633861353031353939616135343035396339\n'
    # Incorrect case
    try:
        do_vault(data='aabb', secret=[], vaultid='filter_default')
    except AnsibleFilterTypeError:
        pass
    else:
        assert False


# Generated at 2022-06-22 11:54:03.845174
# Unit test for function do_unvault
def test_do_unvault():
    # Parse command line args
    import argparse
    parser = argparse.ArgumentParser(description='Test do_unvault')
    parser.add_argument('--unvault_vault_id', required=True, help='unvault_vault_id')
    parser.add_argument('--unvault_vault_secret', required=True, help='unvault_vault_secret')
    parser.add_argument('--unvault_vault_data', required=True, help='unvault_vault_data')
    args = parser.parse_args()

    unvault_vault_id = args.unvault_vault_id
    unvault_vault_secret = args.unvault_vault_secret
    unvault_vault_data = args.unvault

# Generated at 2022-06-22 11:54:14.192938
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    salt = None
    vaultid = 'test_default'
    wrap_object = False

    # simple value
    data = 'mypasswd'

# Generated at 2022-06-22 11:54:26.087747
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foobar', "secret", salt='foo') == '$ANSIBLE_VAULT;1.1;AES256\n6161303961636662316238353465336630323537323739356134373839353962623766316264373533\n3938346535383736666533316633373635373632613436343637404040404040404040404040404040\n40404040404040404040404040404040404040404040404040404040404040404040404040404040\n4040404040404040404040404040\n'

# Generated at 2022-06-22 11:54:29.153118
# Unit test for function do_unvault
def test_do_unvault():
    """ test function do_vault """

    data = "mySecret"
    secret = "password"
    assert(do_unvault(do_vault(data, secret), secret) == data)



# Generated at 2022-06-22 11:54:40.338005
# Unit test for function do_vault

# Generated at 2022-06-22 11:54:51.673755
# Unit test for function do_vault
def test_do_vault():
    # Test that the proper object type is returned when the wrap_object arg is True
    assert isinstance(do_vault('foo', 'foo', wrap_object=True), AnsibleVaultEncryptedUnicode)
    # Test that the proper data is returned when the wrap_object arg is True
    assert do_vault('foo', 'foo', wrap_object=True).data == 'foo'
    # Test that the proper string is returned when the wrap_object arg is False

# Generated at 2022-06-22 11:55:05.466432
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Environment
    from jinja2.exceptions import TemplateError
    from ansible.parsing.vault import VaultLib

    test_env = Environment()

    test_vault = do_vault('123456', 'pa$$word', salt='foobar')
    test_unvault = do_unvault(test_vault, 'pa$$word')


# Generated at 2022-06-22 11:55:12.850891
# Unit test for function do_vault
def test_do_vault():
    secret = "my secret"
    data = "my data"

    expected = b'$ANSIBLE_VAULT;1.1;AES256\n393039333664373633323261646266366232356435663631356531633266366635333464633361666\n2066346435626463366665643833304234343933306162613062326438633162343961303366303336\n66616263303735316139393965383538333936346233613066383861666364620a\n'
    actual = do_vault(data, secret, wrap_object=True)
    assert actual == expected


# Generated at 2022-06-22 11:55:20.642840
# Unit test for function do_vault
def test_do_vault():

    test_data = {
        'plaintext': 'Hello, World!',
        'vaultid': 'test',
        'salt': 'salt',
        'secret': 'secret',
    }

    encrypted = do_vault(test_data['plaintext'], test_data['secret'], test_data['salt'], test_data['vaultid'])
    decrypted = do_unvault(encrypted, test_data['secret'], test_data['vaultid'])

    assert test_data['plaintext'] == decrypted

# Generated at 2022-06-22 11:55:30.041483
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:31.941055
# Unit test for function do_vault
def test_do_vault():
    raise ValueError("TODO: test_do_vault was not implemented")

# Generated at 2022-06-22 11:55:41.545929
# Unit test for function do_vault
def test_do_vault():
    from nose.plugins.skip import SkipTest
    try:
        from unittest.mock import patch
        from ansible.parsing.vault import VaultSecret
    except ImportError:
        raise SkipTest("unittest.mock is not installed")

    test_data = b''.join((b'a' for _ in range(0,10000)))
    # Create a mock encrypt function to do the encryption
    encrypt_mock = patch.object(VaultSecret, 'encrypt')
    # Encrypt needs a password, so create a dummy one
    encrypt_mock.return_value = VaultSecret(b'password').encrypt(test_data, b'salt', b'vault_id')
    # Do the encryption
    data = do_vault(test_data, 'password', 'salt', 'vault_id')


# Generated at 2022-06-22 11:55:53.647099
# Unit test for function do_vault
def test_do_vault():
    x = "ansible1234"

# Generated at 2022-06-22 11:56:05.213052
# Unit test for function do_unvault

# Generated at 2022-06-22 11:56:13.799358
# Unit test for function do_vault
def test_do_vault():
    import os
    import random
    import string
    import unittest
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import StringIO

    class TestVaultLib(VaultLib):

        def __init__(self):
            self.id = 'test'
            self.secrets = {}

        def get_password(self, vault_id, ask_vault_pass=True):
            secret = self.secrets.get(vault_id)
            if not secret:
                raise AnsibleError('Secret for vault_id %s not found' % vault_id)
            return secret

        def vault_id_matches(self, vault_id, vault_ids):
            if self.id == vault_id:
                return True
            else:
                return False

   

# Generated at 2022-06-22 11:56:25.291535
# Unit test for function do_unvault
def test_do_unvault():
    vault = '$ANSIBLE_VAULT;1.1;AES256;graylog_yaml\n61613861366132386139363433393837353462616366633533653335346635306566653835616334\n356663336562393235353336356333616134330a6430386365643762613761326132336163363363\n36633034643431616665623232663065666436326661346136623134363564303336643162646266\n316361373933\n'
    secret = 'VaultTest'

    result = do_unvault(vault, secret)
    assert isinstance(result, string_types)
    assert result == 'test'

# Generated at 2022-06-22 11:56:38.214044
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:49.908735
# Unit test for function do_unvault
def test_do_unvault():
    some_secret = VaultSecret('mysecret')
    vaultlib = VaultLib([('somelabel', some_secret)])
    # verify decryption when vaultid is specified
    assert(do_unvault('$ANSIBLE_VAULT;9.9;somelabel;bG9sOiAxM{==}', 'mysecret', vaultid='somelabel') == 'lol: 12')
    assert(do_unvault('$ANSIBLE_VAULT;9.9;somelabel;aGVsbG8gd29ybGQ=;{==}', 'mysecret', vaultid='somelabel') == 'hello world')

# Generated at 2022-06-22 11:56:56.697052
# Unit test for function do_unvault
def test_do_unvault():
    data = to_bytes('Hello World')

    secret = "This1is2My3Secret"
    vaultid = "test_vault_id"

    vault = do_vault(data, secret, vaultid=vaultid, wrap_object=False)

    data2 = do_unvault(vault, secret, vaultid=vaultid)
    assert data == data2

# End of unit test for function do_unvault

# Generated at 2022-06-22 11:57:06.465311
# Unit test for function do_vault
def test_do_vault():
    # Correct values
    secret = "secret"
    text = "Test message"
    salt = "random salt"
    vaultid = 'filter_default'
    assert do_vault(text, secret, salt, vaultid, False) == do_vault(text, secret, salt, vaultid, True)
    assert do_vault(text, secret, None, vaultid, False) == do_vault(text, secret, None, vaultid, True)
    assert do_vault(text, secret, None, None, False) == do_vault(text, secret, None, None, True)
    with Display(verbosity=0):
        assert do_vault("", secret, salt, vaultid, False) == do_vault("", secret, salt, vaultid, True)

# Generated at 2022-06-22 11:57:17.827188
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'this is a secret'
    unvault = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          3535303139313631366132396566333764653034643565313831343038633862626432346139313335\n          3636646566346439646233396238623564633532653163396231366138613230646230393336656636\n          313832303939666373738643331626539336231393136636231666330646438343164353333653833\n          61623233656534393533666465363064353066653633613662323465323531\n          "
    assert do

# Generated at 2022-06-22 11:57:29.572786
# Unit test for function do_vault
def test_do_vault():

    secret = "yolo"
    plaintext = "SECRETS"
    salt = "helloworld"
    vaultid = "test"

# Generated at 2022-06-22 11:57:40.811364
# Unit test for function do_unvault
def test_do_unvault():
    sample_secret = "s3cr3t"

# Generated at 2022-06-22 11:57:50.253839
# Unit test for function do_vault
def test_do_vault():
    # Pylint does not like the unused import
    # pylint: disable=ungrouped-imports
    # Importing locally to avoid needing the virtualenv to be setup
    import pytest
    filtered = do_vault("this is my password", "onlyoncetome")
    if not isinstance(filtered, AnsibleVaultEncryptedUnicode):
        pytest.fail("Vault data is not an AnsibleVaultEncryptedUnicode: %s" % filtered)
    if "this is my password" == filtered.data:
        pytest.fail("Vault data was not encrypted: %s" % filtered.data)
    do_vault(None, "onlyoncetome")
    do_vault(None, None)
    do_vault("onlyoncetome", None)

# Generated at 2022-06-22 11:57:57.542716
# Unit test for function do_vault
def test_do_vault():
    ''' Ansible vault jinja2 filters unit tests '''
    secret = 'hello'
    salt = 'salt'
    vaultid = 'filter_default'
    wrap_object = False
    try:
        vault = do_vault(secret, secret, salt, vaultid, wrap_object)
    except AnsibleFilterError as e:
        display.warning(str(e))
    assert is_encrypted(vault)


# Generated at 2022-06-22 11:57:59.084819
# Unit test for function do_vault
def test_do_vault():
    do_vault('mysecret', 'mysecretkey123')


# Generated at 2022-06-22 11:58:15.830271
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:22.083140
# Unit test for function do_vault
def test_do_vault():
    # test normal string
    assert do_vault('test_str', 'secret', 'test_salt') == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256;test_salt\n          616332346166656164633961643766346533623830373331653237383333643963626362663263\n          653165313332396639616231306564396633363032333564363036643835386461626433613666\n          336163366466356564663038653436333965636466333262653532316133343336613035616564\n          333437396461633234616665\n          "
    # test decrypted unicode string
    assert do

# Generated at 2022-06-22 11:58:32.193479
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:34.385528
# Unit test for function do_vault
def test_do_vault():
    result = do_vault("password", "secret")
    assert result



# Generated at 2022-06-22 11:58:36.887781
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault('my test string', 'my test password')
    assert isinstance(vault, string_types)



# Generated at 2022-06-22 11:58:48.847313
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.parsing.vault import VaultLib
    # test case with wrap_object=False
    secret = "foobar"
    salt = "random"
    data = "vault_data"
    vaultid = 'default'
    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib()
    try:
        vault = vl.encrypt(to_bytes(data), vs, vaultid, salt)
    except Exception as e:
        raise AnsibleFilterError("Unable to encrypt: %s" % to_native(e), orig_exc=e)
    #assert that the vaultdata is encrypted in the form of AnsibleVaultEncryptedUnicode
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-22 11:58:58.746131
# Unit test for function do_unvault
def test_do_unvault():
    import random
    from ansible.parsing.vault import VaultSecret

    random_data = ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12)
    )
    random_secret = ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12)
    )

    data = random_data.encode('utf-8')
    vs = VaultSecret(to_bytes(random_secret))
    vl = VaultLib()
    vault = vl.encrypt(data, vs)
    data_unvaulted = do_unvault(vault, random_secret, "filter_default")

    assert data == data_unvaulted

# Generated at 2022-06-22 11:58:59.745241
# Unit test for function do_vault
def test_do_vault():
    import doctest
    doctest.testmod()



# Generated at 2022-06-22 11:59:07.374296
# Unit test for function do_vault
def test_do_vault():
    for filter_ in FilterModule().filters():
        if filter_ == do_vault:
            test_str = 'Some_data'
            test_secret = 'test_secret'
            test_salt = 'test_salt'
            test_vaultid = 'test_vaultid'
            test_wrap_object = True
            assert is_encrypted(do_vault(test_str, test_secret, test_salt, test_vaultid, test_wrap_object))
            break

# Generated at 2022-06-22 11:59:18.924220
# Unit test for function do_vault
def test_do_vault():
    secret = "12345678"
    salt = "12345678"
    vaultid = "filter_default"
    wrap_object = False
    data = "my string data"

# Generated at 2022-06-22 11:59:30.161532
# Unit test for function do_vault
def test_do_vault():
    secret = 'foobar'
    data = 'this is a test'

    # validate that this is not encrypted yet
    assert not is_encrypted(data)

    # encrypt data, should return AnsibleVaultEncryptedUnicode
    vault = do_vault(data, secret, wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

    # validate that this is encrypted now
    assert is_encrypted(vault)

    # decrypt data, should return AnsibleVaultEncryptedUnicode
    data = do_unvault(vault, secret)
    assert data == 'this is a test'

# Generated at 2022-06-22 11:59:34.926537
# Unit test for function do_unvault

# Generated at 2022-06-22 11:59:43.631719
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:53.909816
# Unit test for function do_unvault

# Generated at 2022-06-22 12:00:02.325165
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    secret = 'foo'
    data = 'bar'
    vault = do_vault(data, secret)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-22 12:00:09.117682
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault('$ANSIBLE_VAULT;1.2;AES256;vault_default_unittest\r\n'
                      '64616461306637303635346430396432613631316237326166323436366239363331323139663430\r\n'
                      '3965323861396234353132666633303361663533356664613862390a396638316336666630393032\r\n'
                      '39333831646638303437306337326532663162326639616234303137613963353565366334393462\r\n'
                      '303766383933386438353162653730\r\n',
                      'unittest_default_secret')

# Generated at 2022-06-22 12:00:20.758771
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'
    vaulted_text = '$ANSIBLE_VAULT;1.1;AES256;test;3136363763623065366135653836383663633535336434839356465353030613'
    vaulted_text_unicode = u'$ANSIBLE_VAULT;1.1;AES256;test;3136363763623065366135653836383663633535336434839356465353030613'
    vault = do_vault(secret, secret, vaultid='test')
    assert vault == vaulted_text
    vault_unicode = do_vault(secret, secret, vaultid='test')
    assert vault_unicode == vaulted_text_unicode

# Generated at 2022-06-22 12:00:25.880155
# Unit test for function do_vault
def test_do_vault():
    data = 'test_data'
    secret = 'test_secret'
    salt = 'test_salt'
    vaultid = 'test_vaultid'

    assert do_vault(data, secret, salt, vaultid) is not None


# Generated at 2022-06-22 12:00:35.614320
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'foo'
    vaultid = 'test_do_unvault'
    data = 'bar'
    # We have to use the old vault interface as the new one expects a VaultSecret
    # which we can't create without the vault password...
    # TODO: Use the new vault interface
    vault = '$ANSIBLE_VAULT;1.$%s.%s$%s' % (vaultid, do_vault(data, secret, vaultid='filter_default'), do_vault(secret, secret, vaultid='filter_default'))
    assert to_native(data) == do_unvault(vault, secret, vaultid)