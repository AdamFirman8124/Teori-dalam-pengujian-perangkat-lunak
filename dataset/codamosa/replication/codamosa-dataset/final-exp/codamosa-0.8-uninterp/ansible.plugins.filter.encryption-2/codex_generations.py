

# Generated at 2022-06-22 11:50:45.791157
# Unit test for function do_vault
def test_do_vault():
    test_data = 'data'
    test_secret = 'secret'
    test_salt = 'salt'
    test_vaultid = 'test_vaultid'
    test_wrap_object = False
    result = do_vault(test_data, test_secret, test_salt, test_vaultid, test_wrap_object)
    assert result.startswith('$ANSIBLE_VAULT;')



# Generated at 2022-06-22 11:50:52.797064
# Unit test for function do_unvault
def test_do_unvault():
    secret = '3q1AWa75CKpFmBzOd4Biq0q/4M41KxU5b6S'
    vaultid = 'filter_default'

# Generated at 2022-06-22 11:51:04.374194
# Unit test for function do_unvault
def test_do_unvault():

    # Create metadata for ansible-vault encrypted text
    iva = (
        "VaultPasswordFile: /path/to/vault.pwd"
    )

    # This text was encrypted with ansible-vault encrypt_string,
    # and then copied into this file for use with unit test.

# Generated at 2022-06-22 11:51:06.433335
# Unit test for function do_vault
def test_do_vault():
    # This filter just calls a part of the vault module, no easy way to test it
    assert True

# Generated at 2022-06-22 11:51:17.269833
# Unit test for function do_vault
def test_do_vault():
    secret = 'a1b2c3d4e5f6a1b2c3d4e5f6'
    data = 'password'
    result = {'password': '$ANSIBLE_VAULT;1.1;AES256;vault_default\n63303539313336651166366351303438393833663837386162333132316530373733353363653463\n393565646530353062656532333665323664666062653936326335316562616662316464316365633\n706238626161656335323139326361'}
    assert do_vault(data, secret) == result['password']


# Generated at 2022-06-22 11:51:30.196168
# Unit test for function do_unvault
def test_do_unvault():

    data = 'test'
    secret = 'password'

# Generated at 2022-06-22 11:51:39.675279
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:52.297286
# Unit test for function do_vault
def test_do_vault():

    # Verify happy path
    secret = 'password'
    salt = '1234567890'
    vault_id = 'test_do_vault'
    vaulted_value = do_vault('hello', secret, salt=salt, vaultid=vault_id)
    decrypted_vaulted_value = do_unvault(vaulted_value, secret, vaultid=vault_id)
    assert decrypted_vaulted_value == 'hello'

    # Verify the parameter vaultid
    vaulted_value = do_vault('hello', secret, vaultid='fake_id')
    with pytest.raises(AnsibleFilterError):
        do_unvault(vaulted_value, secret)

    # Verify secret is required

# Generated at 2022-06-22 11:52:04.334394
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.compat import AnsibleModule
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    def run_module():
        # initialize needed objects
        module_args = dict(
            data='some string',
            secret='mysecret',
        )

        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=False,
        )

        result = dict(
            changed=False,
            vault='',
        )
        # call the function

# Generated at 2022-06-22 11:52:13.973679
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:26.412781
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import json

    # Imporing the pycryptodomex module
    try:
        import Crypto.Random
    except ImportError:
        display.warning("pycryptodomex python module not found, vault functionality will be degraded. ")

    vault = VaultLib()
    secret = VaultSecret('ansible')
    salt = '9a9a827c'
    vaultid = 'filter_default'

    plaintext = 'Hello World!'

    # Testing the function for plaintext
    result = do_vault(plaintext, secret, salt, vaultid)
    assert result == vault.encrypt(plaintext, secret, vaultid, salt)

    # Testing

# Generated at 2022-06-22 11:52:35.179675
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:47.977601
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:59.312186
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:09.791758
# Unit test for function do_unvault
def test_do_unvault():
    import pytest
    from ansible.parsing.vault import VaultSecret, VaultLib

    secret = VaultSecret(b"a_secret")
    vaultid = 'filter_default'
    vault = VaultLib([(vaultid, secret)])
    data = "mydata"
    vault_data = vault.encrypt(data.encode(), secret, vaultid)
    secret = secret.peek()

    assert do_unvault(vault_data, secret) == data

    # test bad vault
    with pytest.raises(AnsibleFilterTypeError) as exception_info:
        do_unvault(12, secret)

    assert str(exception_info.value) == 'Vault should be in the form of a string, instead we got: <class \'int\'>'

    # test bad secret
   

# Generated at 2022-06-22 11:53:11.823574
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, 'N1Qra0Jwc0puYjZ1YU9r') == None


# Generated at 2022-06-22 11:53:22.108180
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:27.211729
# Unit test for function do_vault
def test_do_vault():
    secret = "password"
    data = "secret"
    salt = "salt"
    vault = do_vault(data, secret, salt)
    data_test = AnsibleVaultEncryptedUnicode(vault)
    unvault = data_test.data
    assert unvault == "secret"


# Generated at 2022-06-22 11:53:35.837370
# Unit test for function do_unvault
def test_do_unvault():
    result = do_unvault(vault="$ANSIBLE_VAULT;1.1;AES256;test\n33363834653265633138616236633464386263346535393832653833656566383336306434336564\n30656433666439346633326336333237616463396236313237633262613931316230663239396162\n623537333566366437393338353538653833", secret="test")
    assert result == "test"

# Generated at 2022-06-22 11:53:41.392551
# Unit test for function do_unvault
def test_do_unvault():
    """
    @summary: Test for unvaulting a string
    """
    secret = 'test secret'
    data = 'test data'
    vaultid = 'test_id'

    assert data == do_unvault(do_vault(data, secret, vaultid), secret, vaultid)

# Generated at 2022-06-22 11:53:55.691326
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultSecret, VaultLib

    test_vault = '$ANSIBLE_VAULT;1.1;AES256;test\n633633666332326634323338613238366566326333623936343065653562366132343332623164\n643435336433323830366330336439642d643639382d346630302d38343365612d303733656535\n653230363637653265306636373766656461312d37383433633532353165313532343538363433\n386634393636303363363262313162'
    test_secret = 'test'

    vs = VaultSecret(test_secret)
    vl = Vault

# Generated at 2022-06-22 11:54:07.778341
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'

# Generated at 2022-06-22 11:54:18.402870
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'

# Generated at 2022-06-22 11:54:22.053834
# Unit test for function do_vault
def test_do_vault():
    data = 'test'
    secret = 'secret'
    vault = do_vault(data, secret)
    assert vault.startswith('$ANSIBLE_VAULT')


# Generated at 2022-06-22 11:54:34.169703
# Unit test for function do_vault
def test_do_vault():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible import constants as C
    from ansible.plugins.loader import become_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import filter_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import test_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.dynamic_inventory import InventoryModule

    data = 'Hello world'
    secret = 'thisisasecret'
    vaultid = 'filter_default'
    wrap_object = False
    vault_result

# Generated at 2022-06-22 11:54:43.362761
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:51.607239
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    data = "data"
    result = do_vault(data, secret)
    assert result == b"$ANSIBLE_VAULT;1.1;AES256\n366265366435653634633961613263333861346331646234316236383136616262353335343966\n366130366536633261613931323164346635383634613630646635656539376265656633313066\n396535\n"

# unit test for function do_unvault

# Generated at 2022-06-22 11:55:02.985971
# Unit test for function do_unvault
def test_do_unvault():
    data_in_file = 'ECRYPTv0AAAAAAP3qw3mQAQb/O8Kv/npfFZpRXZ1JzDgfYKiUrE3q2GLyCeW8JiESlq5e5JC9XrH5W8aAQ5kd+w=='

    # Test valid input
    data_out = do_unvault(data_in_file, 'foo')
    assert data_out == 'bar'

    # Test with empty vault
    data_out = do_unvault('', 'foo')
    assert data_out == ''

    # Test with null value
    data_out = do_unvault(None, 'foo')
    assert data_out is None

# Generated at 2022-06-22 11:55:11.303289
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    f = FilterModule()
    unvault = f.filters()["unvault"]

    # Test unvault with clear data
    clear_data = 'data to encrypt and decrypt'
    assert clear_data == unvault(clear_data, 'foo')

    # Test with encrypted data (legacy)
    secret = 'foo'
    data = 'data to encrypt and decrypt'
    vs = VaultSecret(secret)
    vl = VaultLib([('foo', vs)])
    ve = VaultEditor(vl)

# Generated at 2022-06-22 11:55:15.388942
# Unit test for function do_vault
def test_do_vault():
    secret = "abc123"
    data = "secret"
    actual = do_vault(data, secret)

    # Check the actual
    assert actual != data
    assert actual != secret
    assert actual.startswith("$ANSIBLE_VAULT;")



# Generated at 2022-06-22 11:55:29.837858
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'testsecret'

    data = 'testdata'
    vault = do_vault(data, secret)
    assert data == do_unvault(vault, secret)

    data2 = "test\n\r\tdat\na"
    vault2 = do_vault(data2, secret)
    assert data2 == do_unvault(vault2, secret)
    assert data2 == do_unvault(vault2, secret)

# Generated at 2022-06-22 11:55:34.574712
# Unit test for function do_vault
def test_do_vault():
    test = 'abcdefghijklmnopqrstuvwxyz'
    secret = 'secret'
    vault = do_vault(test, secret)
    assert isinstance(vault, string_types)
    assert is_encrypted(vault)


# Generated at 2022-06-22 11:55:44.186767
# Unit test for function do_vault
def test_do_vault():
    secret = 'batman'
    data = "Robin's bike was stolen!"

# Generated at 2022-06-22 11:55:53.592686
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'hello') == b'$ANSIBLE_VAULT;1.1;AES256\n39643562366266373063633235373531353336366135356133646135366638653066333135616666\na6b623e6a7d6b31c937e0619aab0f11c2a580a08a6c7dd8e8a6d7de6e98f9cd9\n'
    assert do_vault(None, 'hello') == None
    assert do_vault(123, 'hello') == None


# Generated at 2022-06-22 11:56:03.899588
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:13.155056
# Unit test for function do_vault
def test_do_vault():

    import pytest

    with pytest.raises(AnsibleFilterError, match="Secret passed is required to be a string, instead we got"):
        do_vault("data", 1)

    with pytest.raises(AnsibleFilterError, match="Can only vault strings, instead we got: <class 'int'>"):
        do_vault(1, "secret")

    with pytest.raises(AnsibleFilterError, match="Can only vault strings, instead we got: <class 'dict'>"):
        do_vault({}, "secret")

    with pytest.raises(AnsibleFilterError, match="Unable to encrypt: Secret is required to be a string, bytes or unicode"):
        do_vault("data", None)


# Generated at 2022-06-22 11:56:24.643587
# Unit test for function do_vault
def test_do_vault():
    assert(do_vault('password', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n39306331306337663762306539323735373862363136383637373330656432303633333331356166\n30396638376336623536613332396332623230313237363936386436623137313262666532643534\n3136610a353866626262333538356331343935326638656331323332636662363364663536346236\n32333337626233636631663038346437373031613662626163383562393166663466616665633663\n3833613039')


# Generated at 2022-06-22 11:56:36.245753
# Unit test for function do_vault
def test_do_vault():

    vault = do_vault('my secret data', 'mysecret', 'salt', 'filter_default')


# Generated at 2022-06-22 11:56:44.798544
# Unit test for function do_unvault
def test_do_unvault():

    # Unvault a non-vaulted string, return that string
    non_vault = 'Hello, World'
    non_vault_return = do_unvault(non_vault, 'ansible')
    assert non_vault == non_vault_return

    # Unvault a vaulted string and return the decrypted string
    secret = 'ansible'

# Generated at 2022-06-22 11:56:56.395142
# Unit test for function do_unvault
def test_do_unvault():
    try:
        do_unvault('foo', None)
        raise
    except AnsibleFilterTypeError:
        pass

    try:
        do_unvault(None, 'foo')
        raise
    except AnsibleFilterTypeError:
        pass

    try:
        do_unvault(None, None)
        raise
    except AnsibleFilterTypeError:
        pass

    try:
        do_unvault(1234, 'foo')
        raise
    except AnsibleFilterTypeError:
        pass

    try:
        do_unvault('foo', 1234)
        raise
    except AnsibleFilterTypeError:
        pass

    assert do_unvault('$ANSIBLE_VAULT;6.5;AES128;foo') == 'foo'

# Generated at 2022-06-22 11:57:09.270309
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:17.114880
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultSecret, VaultLib
    import unittest

    class TestDoUnvault(unittest.TestCase):
        def setUp(self):
            self.super_secret = 'super_secret_stuff'
            self.super_secret_bytes = VaultSecret(to_bytes(self.super_secret))
            self.vault = VaultLib([('default', self.super_secret_bytes)])
            self.data = 'the unvaulted stuff'

        def test_unvault_string(self):
            ciphertext = self.vault.encrypt(to_bytes(self.data))
            self.assertIsInstance(ciphertext, binary_type, 'Encrypted should be a binary/bytes')

# Generated at 2022-06-22 11:57:27.653084
# Unit test for function do_vault
def test_do_vault():
    import os
    import json
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_secret = os.environ.get('ANSIBLE_VAULT_PASSWORD_FILE') or os.path.expanduser('~/.ansible_vault_pass.txt')
    assert os.path.isfile(vault_secret), \
        "Environment variable 'ANSIBLE_VAULT_PASSWORD_FILE' is not set or file '%s' doesn't exist" % vault_secret

    with open(vault_secret, 'r') as f:
        secret = f.read()

    # Test basic invalid encoding cases

# Generated at 2022-06-22 11:57:32.141990
# Unit test for function do_vault
def test_do_vault():

    test_string = 'Password is 12345'

    result = do_vault(test_string, 'testsecret')

    assert is_encrypted(result)



# Generated at 2022-06-22 11:57:37.975288
# Unit test for function do_unvault
def test_do_unvault():
    vault_secret = "test_secret"
    vault_data = "vaulted_data"
    vault_id = "test_vault_id"
    vault_obj = do_vault(vault_data, vault_secret, vaultid=vault_id)
    assert is_encrypted(vault_obj)
    assert do_unvault(vault_obj, vault_secret, vaultid=vault_id) == vault_data

# Generated at 2022-06-22 11:57:48.494056
# Unit test for function do_vault
def test_do_vault():

    import tempfile
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader, variables={})

    ansible_vault_password_file = tempfile.NamedTemporaryFile(delete=False)
    ansible_vault_password_file.write(b'secret')
    ansible_vault_password_file.close()
    environ_vault_password = 'secret'

    def do_vault_test(name, expected_return, **kwargs):
        return_value = do_vault(data='secret', secret=environ_vault_password, **kwargs)
        assert expected_return == return_value, '%s - unexpected return value' % name
        return_value = do_

# Generated at 2022-06-22 11:58:00.755163
# Unit test for function do_vault
def test_do_vault():
    import subprocess
    import ansible.parsing.vault
    temp_file = 'temp.txt'
    #replace current vault library with test vault library
    subprocess.call('cp %s %s.bak' % (ansible.parsing.vault.VAULT_LIB, ansible.parsing.vault.VAULT_LIB), shell=True)
    subprocess.call('cp tests/unit/do_vault/vault.so %s' % (ansible.parsing.vault.VAULT_LIB), shell=True)
    #create test data and write to file
    test_data = 'test'
    with open(temp_file, 'w') as f:
        f.write(test_data) 
    #encrypt data with do_vault function
    result = do_v

# Generated at 2022-06-22 11:58:01.926077
# Unit test for function do_vault
def test_do_vault():
    do_vault(
        data="1234567890",
        secret="1234567890"
    )


# Generated at 2022-06-22 11:58:02.546071
# Unit test for function do_vault
def test_do_vault():
    pass

# Generated at 2022-06-22 11:58:14.471509
# Unit test for function do_vault
def test_do_vault():
    vault_filter = FilterModule()
    filters = vault_filter.filters()
    with open(__file__, "r") as f:
        src = f.read()

    secret = "This is a secret"
    ctxt = "context"
    vault = filters['vault'](src, secret)
    unvault = filters['unvault'](vault, secret)
    assert (unvault == src)
    assert (isinstance(vault, string_types))
    # test different vaultid
    vaultid = "different_vaultid"
    vault = filters['vault'](src, secret, vaultid=vaultid)
    unvault = filters['unvault'](vault, secret, vaultid=vaultid)
    assert (unvault == src)

# Generated at 2022-06-22 11:58:29.785159
# Unit test for function do_unvault
def test_do_unvault():
    # Basic test
    assert "mysecret" == do_unvault(
        "!vault |\n          $ANSIBLE_VAULT;1.2;AES256;ansible\n          31373931303765393231333365613761633362343265366339633537376666616232623432363437\n          36663361303738353039363635646366396364623036633532396561653237326439356537663635\n          63666230353365326365643066656433383263383033373331373634316434393266383666363530\n          ",
        "secret"
    )


# Generated at 2022-06-22 11:58:33.493742
# Unit test for function do_vault
def test_do_vault():
    secrets = {'filter_default': VaultSecret('mysecret')}
    vl = VaultLib(secrets = secrets)
    result = vl.encrypt('some_data')
    assert result == do_vault('some_data','mysecret','filter_default')


# Generated at 2022-06-22 11:58:37.159754
# Unit test for function do_vault
def test_do_vault():
    # part1 test
    assert do_vault('root', 'mysecret') != None
    # part2 test
    assert do_vault('root', 'mysecret', wrap_object=True) != None


# Generated at 2022-06-22 11:58:45.276422
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('my_pass', 'my_secret') == '$ANSIBLE_VAULT;1.1;AES256;my_secret;f69709a75a92706f3b3f8b3e4b4f4b2a;1023942917332677\n3966343163653363323438366232626663656163376439376539333535666638653831613231366\nef5a446c0278e0c032463cc39ce04c1f\n'


# Generated at 2022-06-22 11:58:56.359885
# Unit test for function do_vault
def test_do_vault():
    fm = FilterModule()
    filters = fm.filters()
    assert(filters.get('vault'))
    # Test simple string
    assert filters['vault']('foo', 'pass', wrap_object=False) == '$ANSIBLE_VAULT;1.1;AES256\n33303537343966343061376630326435616134313362626534383035653365643333333231303765\n39653836383131636465363232386131393065373764396163623337326637646362366333636665a\n'
    # Test unicode string

# Generated at 2022-06-22 11:59:07.709708
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'


# Generated at 2022-06-22 11:59:13.950440
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('hello', 'secret') == b'$ANSIBLE_VAULT;1.1;AES256\n646163393835356233323439363435363433636430373836623865333835383436626435653066\n31323762616663313162663433306636336137663939326164330a333332313538656562333836\n306136313265663861393566303837616262626530306362643734643930363537613766643730\n65336133353461666137376332610a'


# Generated at 2022-06-22 11:59:25.024774
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    data = 'correct horse battery staple'

# Generated at 2022-06-22 11:59:32.107605
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:42.928450
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:00.261300
# Unit test for function do_vault
def test_do_vault():
    secret = u'password'
    data = u'secret'

# Generated at 2022-06-22 12:00:10.806446
# Unit test for function do_vault
def test_do_vault():
    from . import vault_filters
    secret = vault_filters.do_vault("test_string", "secret")
    assert secret == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          63313666633033623637303539396636623166656235363061356565653239363336653538633135\n          30623662323265303730356630306338313563636134336531613233653736653835393430303330\n          3030656461646339636338383630346130623631396138316166\n          ", "Unable to encrypt"


# Generated at 2022-06-22 12:00:22.000841
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret
    secret = 'secret'
    vs = VaultSecret(secret)
    data = 'data'
    ret = do_vault(data, secret)
    # ret: $ANSIBLE_VAULT;1.1;AES256;ansible;70332341663066643437666435333764366363623035336634303431646461303665323064636236303766393534663537636436373836383034346331396237633835
    assert is_encrypted(ret)
    assert b'$ANSIBLE_VAULT;1.1;AES256;ansible;' in ret

# Generated at 2022-06-22 12:00:31.787306
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:42.453482
# Unit test for function do_vault
def test_do_vault():
    testcases = [
        ("testdata", "secret", "salt", "filter_default", False),
        ("testdata", "secret", "salt", "filter_default", True),
        ("testdata", "secret", None, "filter_default", False),
        ("testdata", "secret", None, "filter_default", True),
        ("testdata", "secret", "salt", None, False),
    ]

    def run_testcase(secret, data, salt, vaultid, wrap_object):
        vault = do_vault(data, secret, salt, vaultid, wrap_object)
        display.vvv("Vault: %s" % vault)
        assert vault is not None
        if isinstance(vault, AnsibleVaultEncryptedUnicode):
            assert vault.vault is not None
        un