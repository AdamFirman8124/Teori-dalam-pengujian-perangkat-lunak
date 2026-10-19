

# Generated at 2022-06-22 11:50:48.098485
# Unit test for function do_unvault
def test_do_unvault():
    # test with secret
    secret = "!vault |"
    vault="$ANSIBLE_VAULT;1.1;AES256\n343733353964363763643735663164376433303564373364623532346364326439643631626464\n39643338356464386564303933653665306439306664323461323635313936333835306536333266\n3733343132326430343837383762346336"
    assert do_unvault(vault, secret) == "test"

    # test without secret
    secret = None

# Generated at 2022-06-22 11:50:55.351228
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import is_encrypted, VaultSecret, VaultLib
    from ansible.module_utils._text import to_bytes

    # test to fail without secret
    secret = ''
    vaultid = 'filter_default'
    data = 'test'
    data = do_vault(data, secret, vaultid)
    assert is_encrypted(data)

    # create a secret
    secret = 'test'
    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib([(vaultid, vs)])

    # test with secret
    data = do_unvault(data, secret, vaultid)
    assert data == 'test'

# Generated at 2022-06-22 11:51:05.290502
# Unit test for function do_vault
def test_do_vault():
  import jinja2
  import pytest

  def do_vault(data, secret, salt=None, vaultid='filter_default', wrap_object=False):
    # Function do_vault from ansible.plugins.filter.vault.py

    if not isinstance(secret, (string_types, binary_type, Undefined)):
        raise AnsibleFilterTypeError("Secret passed is required to be a string, instead we got: %s" % type(secret))

    if not isinstance(data, (string_types, binary_type, Undefined)):
        raise AnsibleFilterTypeError("Can only vault strings, instead we got: %s" % type(data))

    vault = ''
    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib()

# Generated at 2022-06-22 11:51:16.358055
# Unit test for function do_unvault
def test_do_unvault():
    secret = '123456'
    vaultid = 'filter_default'

# Generated at 2022-06-22 11:51:28.894725
# Unit test for function do_unvault
def test_do_unvault():
    from unittest import TestCase

    class test_do_unvault_class(TestCase):
        def test_pass_1(self):
            self.assertEqual(do_unvault('$ANSIBLE_VAULT;1.1;AES256;foo\n61646d696e626f756e64\n', 'foo'), 'bar')

        def test_pass_2(self):
            data = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;foo\n61646d696e626f756e64\n')
            self.assertEqual(do_unvault(data, 'foo'), 'bar')


# Generated at 2022-06-22 11:51:38.304221
# Unit test for function do_unvault
def test_do_unvault():

    # Test case 1:
    secret = "somesecret"
    old_vault = "$ANSIBLE_VAULT;1.1;AES256\n36333537396430616463636162613237323639376631646336616265393831630a63316133313237323232306362353765326663346232313933653939303466\n3465343465373666663635336564363938633831613839383265333235396665626336613232363330\n6366663538366332636666313436323764313238666439346462626336613232363330636666353836\n63326366663134363237643132386664393464"
    new

# Generated at 2022-06-22 11:51:51.457026
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes, to_text
    import ansible
    # initialize vault object
    secret = VaultSecret('0123456789abcdef')
    vl = VaultLib([('test', secret)])
    # encrypt test string
    #test_encrypted_data = vl.encrypt(to_bytes('test'))
    test_encrypted_data = vl.encrypt(to_text('test'))
    # use jinja filter to encrypt
    test_filter_data = do_vault('test', '0123456789abcdef', vaultid='test', wrap_object=False)
    assert test_filter_data == test_encrypted_data

#

# Generated at 2022-06-22 11:52:03.289013
# Unit test for function do_vault
def test_do_vault():

    secret = 'ansible'
    data = 'This is a secret!'

# Generated at 2022-06-22 11:52:15.080020
# Unit test for function do_unvault
def test_do_unvault():
  from filecmp import cmp
  from tempfile import mkstemp

  def _get_mock_env(tmpdir):
    env = {
      'HOME': tmpdir,
      'USER': "test",
      'USERNAME': "test",
    }
    return env

  # Init the mock env
  from ansible.parsing.dataloader import DataLoader
  from ansible.vars import VariableManager
  from ansible.inventory import Inventory
  from ansible.constants import DEFAULT_VAULT_ID_MATCH
  from ansible.parsing.vault import get_vault_secret

  mock_loader = DataLoader()
  mock_loader.set_vault_secrets([get_vault_secret(None)])
  mock_variable_manager = VariableManager()

# Generated at 2022-06-22 11:52:25.614551
# Unit test for function do_unvault
def test_do_unvault():
    # Tests for do_unvault() for simple strings
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256\n353066356464623132353036356437363364396561356464613435316430343431663337663035\n363734623134313739376236313765653966643632666361623066376365393763303730663435\n656331366366353864626332612a1b5d5f566f5b5c5d5b5d5c5f5d5d5d5f5e5f5d5e566f', 'abc') == 'abc'

    # Tests for do_unvault() when we have AnsibleVaultEncryptedUnicode object


# Generated at 2022-06-22 11:52:36.013342
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.module_utils.six import PY3

    vaultid = 'filter_default'
    secret = 'secret'

    # test case when string is unencrypted
    data1 = 'This is unencrypted string'
    decrypted_data = do_unvault(data1, secret, vaultid)
    if not decrypted_data == data1:
        raise AnsibleFilterError("Unable to decrypt string")

    # test case when string is encrypted
    data2 = do_vault(data1, secret, vaultid=vaultid)
    decrypted_data = do_unvault(data2, secret, vaultid)
    if decrypted_data != data1:
        raise AnsibleFilterError("Unable to decrypt string")

    encrypted_object = AnsibleVaultEncryptedUnicode(data2)

# Generated at 2022-06-22 11:52:49.189700
# Unit test for function do_vault
def test_do_vault():
    secret = 'thisismysecret'
    data = 'data'
    salt = 'salt'
    vaultid = 'my_vault'
    wrap_object = True
    assert do_vault(data, secret, salt, vaultid, wrap_object) == '$ANSIBLE_VAULT;1.2;AES256;my_vault\n3839373437643038343766383665393865363536636430393364336233356536666537323861636665\n3531343035396435343135630a63366137313335653664386665646431343436313466646433316131\n3030626132316461333335643436663232343436393937303763653338363365\n'


# Generated at 2022-06-22 11:52:59.497934
# Unit test for function do_unvault
def test_do_unvault():
    assert 'test' == do_unvault('$ANSIBLE_VAULT;1.1;AES256\n6131373133616561393162333263356631623935643165633763303135313531653364306661313531312\n3130353737663032633238313236616230376132306164653934653165353330343637646463386566\n', 'test')
    # for unicode

# Generated at 2022-06-22 11:53:09.860627
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Template
    import json

    # Test a few different object types
    data_test = {
        'string': 'a string',
        'number': 1,
        'binary': to_bytes('a binary string'),
        'unicode': 'a unicode string',
    }

    secret = 'test'
    vaultid = 'myvault'
    salt = 'salt'

    failures = []

    for data_type in data_test:
        data = data_test[data_type]

        # Encrypt data
        encrypted_data = do_vault(data, secret, salt=salt, vaultid=vaultid)

        # Check the encrypted output type

# Generated at 2022-06-22 11:53:19.709478
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:22.082824
# Unit test for function do_vault
def test_do_vault():
    assert do_vault({'a': 'b'}, 'secret', wrap_object=True) is not None

# Generated at 2022-06-22 11:53:33.099238
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:38.871331
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:46.590457
# Unit test for function do_vault
def test_do_vault():
    test_secret = 'abcdefgh'
    test_data = 'test_data'

# Generated at 2022-06-22 11:53:48.126366
# Unit test for function do_vault
def test_do_vault():
    assert '$ANSIBLE_VAULT;1.1;AES256' in do_vault('toto', 'toto')


# Generated at 2022-06-22 11:54:02.124856
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import is_encrypted, VaultSecret, VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = 'testsecret'
    data = 'test_data_unvault'
    vaultid = 'test_unvault'

    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib()
    vault = vl.encrypt(to_bytes(data), vs, vaultid)

    assert to_native(vault) == do_unvault(vault, secret, vaultid)
    assert is_encrypted(vault) is True

    # Wrap the vault data with AnsibleVaultEncryptedUnicode class
    vault = AnsibleVaultEncryptedUnicode(vault)

# Generated at 2022-06-22 11:54:11.543955
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'some_secret'

# Generated at 2022-06-22 11:54:20.160012
# Unit test for function do_vault
def test_do_vault():
    filter_instance = FilterModule()
    result = filter_instance.filters()['vault']('test_data', 'vault_secret')

# Generated at 2022-06-22 11:54:30.965597
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    salt = 'test'
    data = 'test'

# Generated at 2022-06-22 11:54:39.766240
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    salt = 'salt'
    data = 'sample'
    vault = '$ANSIBLE_VAULT;1.1;AES256;salt;K9Rz5AQoM6MLLEjPQgO35OaZV7+ZjKpABVgDd9XEBuVUA'
    vaultid = 'filter_default'

    assert do_vault(data, secret) == vault
    assert do_vault(data, secret, salt=salt) == vault
    assert do_vault(data, secret, vaultid=vaultid) == vault


# Generated at 2022-06-22 11:54:51.003944
# Unit test for function do_vault
def test_do_vault():
    import binascii
    from ansible.utils.display import Display

    display = Display()

    # Test the do_vault function
    data = 'secret data that needs to be encrypted'
    secret = 'secret'
    salt = binascii.hexlify(b'salt for vault')

    vault = do_vault(data, secret, salt)
    display.display(vault, color='blue')

# Generated at 2022-06-22 11:54:58.761611
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:00.967485
# Unit test for function do_vault
def test_do_vault():
    secret='foo'
    salt='blah'
    data='bar'
    result = do_vault(data, secret)
    print(result)


# Generated at 2022-06-22 11:55:03.668525
# Unit test for function do_vault
def test_do_vault():
    assert '$ANSIBLE_VAULT;1.1;AES256' in do_vault('secret', 'vault_password')



# Generated at 2022-06-22 11:55:12.371024
# Unit test for function do_vault
def test_do_vault():

    assert do_vault('test', 'password', vaultid='test') == '$ANSIBLE_VAULT;1.1;AES256\n396530306334623863313661633233393434613832616139633763633563646561613361646436\n643765386466376432363633363262643162366162373233356564333736643530623038343961\n383762646435326332626462366362373039393762646435\n'

# Generated at 2022-06-22 11:55:27.739817
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret, VaultLib

    secret = 'test'
    salt = b'4DG4WMTB'
    vaultid = 'testvaultid'
    clear_text = 'test'

    vs = VaultSecret(to_bytes(secret))
    vl = VaultLib()
    vault_text = vl.encrypt(to_bytes(clear_text), vs, vaultid, salt)

    assert clear_text == do_unvault(vault_text, secret, vaultid)
    assert clear_text == do_unvault(vault_text, secret)
    assert clear_text == do_unvault(vault_text, secret, vaultid)

    # now test setting salt
    salt = b'4DG4WMTB'
    assert clear_text

# Generated at 2022-06-22 11:55:39.712975
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from jinja2 import Template, UndefinedError

    secret = 'ansible'

# Generated at 2022-06-22 11:55:43.708376
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    data = 'testtest'

    vault = None

    vault = do_vault(data=data, secret=secret, wrap_object=False)
    assert isinstance(vault, string_types)

    vault = do_vault(data=data, secret=secret, wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-22 11:55:50.739880
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    salt = 'salt'

    encountered_exception = False
    try:
        vault = do_vault(data, secret, salt)
        print('vault:\n\t%s' % vault)
    except UndefinedError as e:
        print('vault:\n\t{}'.format(str(e)))
        encountered_exception = True
    finally:
        assert encountered_exception is False


# Generated at 2022-06-22 11:56:02.660457
# Unit test for function do_vault
def test_do_vault():
    f = FilterModule()
    filters = f.filters()

# Generated at 2022-06-22 11:56:06.605182
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    salt = "salt"
    vaultid = "testvault"
    wrap_object = True
    data = "hello"
    assert VaultLib().decrypt(do_vault(data, secret, salt, vaultid, wrap_object)) == data

# Generated at 2022-06-22 11:56:14.596234
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('secret_value', 'vault_secret') == '$ANSIBLE_VAULT;1.1;AES256\n3763643966373661666237613634343162393934623238363262613338323334313631643233636\n61316665663061303133386339613061306262656133313161333664366164386439363064323665\n36653066333364653131306534626539353331356538313339373639363163303637663734356630\n61333333386262616338393334363530633933636232323061666662383630663661623663333665\n\n'

# Generated at 2022-06-22 11:56:24.076040
# Unit test for function do_unvault
def test_do_unvault():
    secret = "Asecret"

# Generated at 2022-06-22 11:56:35.775984
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    expected = '$ANSIBLE_VAULT;1.1;AES256\n3630636430373432656366623432373734353866333735663735376132383839613231623031633061\n3637646539666430656665353466643863306331386133613239623263633034303337633162323938\n6232343466653539333761373131613234333964333136666433653763366632393937643434666437\n38353736643034653166373663396463\n'

    assert do_vault(data, secret) == expected

# Generated at 2022-06-22 11:56:44.698585
# Unit test for function do_vault
def test_do_vault():
    ''' ansible-test network-integration --local do_vault '''

    from ansible.module_utils import basic
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch

    def setup_module():
        return basic.AnsibleModule(
            argument_spec=dict(
                data=dict(type='str'),
                secret=dict(type='str'),
                salt=dict(type='str'),
                vaultid=dict(type='str')
            ),
            supports_check_mode=True
        )

    def test_invalid_secret_type(secret, salt, vaultid, expected):
        with pytest.raises(AnsibleFilterTypeError) as execinfo:
            do_vault(secret, secret, salt, vaultid)
        result = exec

# Generated at 2022-06-22 11:56:59.717372
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'mysecret'
    vaultid = 'filter_default'

# Generated at 2022-06-22 11:57:09.150048
# Unit test for function do_vault
def test_do_vault():
    import string
    import random
    import unittest.mock
    random_secret = ''.join(random.choice(string.ascii_letters) for i in range(30))
    random_data = ''.join(random.choice(string.ascii_letters) for i in range(30))
    random_salt = ''.join(random.choice(string.ascii_letters) for i in range(30))
    random_vaultid = ''.join(random.choice(string.ascii_letters) for i in range(10))

    args = [random_secret, random_data, random_salt, random_vaultid]
    kwargs = {'wrap_object': True}

    test_class = FilterModule()
    test_class.filters = unittest.mock.Magic

# Generated at 2022-06-22 11:57:17.058929
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:21.210884
# Unit test for function do_vault
def test_do_vault():
    print("Testing do_vault")
    secret = "secret"
    data = "data"
    vault = do_vault(data, secret)
    assert is_encrypted(vault)


# Generated at 2022-06-22 11:57:31.636504
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:37.081429
# Unit test for function do_vault
def test_do_vault():
    data = 'super secret'
    secret = 'ansible'

# Generated at 2022-06-22 11:57:47.662827
# Unit test for function do_unvault
def test_do_unvault():

    # Encrypted string
    vault1 = '$ANSIBLE_VAULT;1.1;AES256\n6339373066303263306232636133373864326563306330653330653762626562393162333661643266\n3833266436646361333534666434363331393637626663386237666232303066386534316632326334\n343661613430653638383932616334623962323566363935663036\n'

    # Unencrypted string
    vault2 = '1234567890'

    secret = 'ilikeansible'

    output1 = do_unvault(vault1, secret, vaultid='test_vault')

# Generated at 2022-06-22 11:57:55.824159
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.exit_json(ansible_facts=dict(
        ansible_filter_result=do_vault("Ansible", "password", "salt"),
        ansible_filter_result_wrap_object=do_vault("Ansible", "password", "salt", wrap_object=True),
    ))

if __name__ == '__main__':
    test_do_vault()

# Generated at 2022-06-22 11:58:04.758511
# Unit test for function do_unvault
def test_do_unvault():
    testyaml = ('''\
---
# file: test.yml
# Some test data:
#   - name: this is a string
#   - value: this is an encrypted string
#       !vault |
#           $ANSIBLE_VAULT;1.1;AES256
#           31373635333739333131353735333563363236633735646164353637333762333735633162636534
#           39313061396239663562653766333463666562346165353266
#           396531333933346536313065663137653038663266363465663933363361
#   - age: 99
''')
    secret = 'random string of characters'
    vaultid = 'test_default'
    vaultid_not_

# Generated at 2022-06-22 11:58:16.507540
# Unit test for function do_vault
def test_do_vault():
    # Test a simple data input to be encrypted
    assert is_encrypted(do_vault("test", "secret")) is True
    # Test a defined variable from jinja2 template to be encrypted
    assert is_encrypted(do_vault("{{ variable1 }}", "secret")) is True
    # Test a undefined variable from jinja2 template to be encrypted
    assert is_encrypted(do_vault("{{ variable2 }}", "secret")) is True
    # Test a secret not defined from jinja2 template to be encrypted
    assert is_encrypted(do_vault("{{ variable1 }}", "{{ secret }}")) is True
    # Test a secret defined from jinja2 template to be encrypted
    assert is_encrypted(do_vault("{{ variable1 }}", "{{ secret }}", salt="salt")) is True
    # Test a secret defined from

# Generated at 2022-06-22 11:58:42.007302
# Unit test for function do_unvault
def test_do_unvault():
    test_values = [
        "test",
        AnsibleVaultEncryptedUnicode("test")
    ]
    test_secrets = [
        "test"
    ]
    test_vaultids = [
        "test",
        "filter_default",
    ]
    for value in test_values:
        for secret in test_secrets:
            for vaultid in test_vaultids:
                data = do_vault(value, secret, vaultid=vaultid)
                unvault = do_unvault(data, secret, vaultid=vaultid)
                assert unvault == value

# Generated at 2022-06-22 11:58:50.965524
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    secret = "secret"
    data = "test"
    salt = "salt"
    vaultid = "vaultid"

    vault = do_vault(data, secret, salt, vaultid, True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)
    assert vault.vaultid == vaultid
    assert vault.salt == salt
    assert vault.data != data

    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:58:54.751332
# Unit test for function do_vault
def test_do_vault():

    secret = "test_secret"
    data = "test_data"
    salt = "test_salt"
    wrap_object = False

    vault = do_vault(data, secret, salt, wrap_object=wrap_object)

    assert type(vault) == str



# Generated at 2022-06-22 11:59:05.796017
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:17.140381
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import is_encrypted, VaultLib
    import os
    import jinja2
    import textwrap
    from tempfile import mkdtemp
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import sys
    import json

    if sys.version_info >= (3, 0):
        from io import StringIO
        Directories = {}
    else:
        from StringIO import StringIO
        Directories = os.path


# Generated at 2022-06-22 11:59:27.549699
# Unit test for function do_vault
def test_do_vault():
    result = do_vault("test", "password", "salt", "test_vault_id", False)

# Generated at 2022-06-22 11:59:38.941249
# Unit test for function do_vault
def test_do_vault():
    filters = FilterModule()

# Generated at 2022-06-22 11:59:48.164996
# Unit test for function do_vault
def test_do_vault():
    # Test with non-string variables
    try:
        do_vault(1, 2, 3, 4)
        assert False, "Non-string value passed"
    except AnsibleFilterTypeError:
        assert True, "Non-string value passed"

    # Test with valid string passphrase
    assert do_vault("passphrase", "secret"), "Unable to Encrypt"

    # Test with invalid string passphrase
    try:
        do_vault("passphrase", "secret", "salt")
        assert False, "Invalid passphrase passed"
    except AnsibleFilterTypeError:
        assert True, "Invalid passphrase passed"


# Generated at 2022-06-22 11:59:58.038570
# Unit test for function do_vault
def test_do_vault():

    # Should not throw exceptions
    do_vault("test", "test", "test", "test", True)
    do_vault("test", "test", "test", "test")
    # Should return AnsibleVaultEncryptedUnicode object
    assert isinstance(do_vault("test", "test", "test", "test", True), AnsibleVaultEncryptedUnicode)
    # Should return string
    assert isinstance(do_vault("test", "test", "test", "test"), str)
    # Do not throw exceptions
    do_vault("test", "test", "test")
    do_vault("test", "test")
    # Should return AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-22 12:00:09.621801
# Unit test for function do_vault
def test_do_vault():

    # tests with bad arguments
    bad_args = [
        [1, 2],
        [1, 'pwd'],
        ['a', 1],
        [[1, 2], 'a'],
        ['a', [1, 2]],
        [None, 'a'],
        ['a', None],
        [None, None]
        ]

    for args in bad_args:
        try:
            do_vault(*args)
        except AnsibleFilterTypeError as e:
            pass
        else:
            assert False, "Expected AnsibleFilterTypeError"

    # tests with good arguments