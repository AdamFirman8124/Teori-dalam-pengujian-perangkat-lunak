

# Generated at 2022-06-22 11:50:48.109050
# Unit test for function do_unvault

# Generated at 2022-06-22 11:50:54.919190
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret_password'
    vaultid = 'default'
    plain_data = 'this is plain text'
    encrypted_data = '$ANSIBLE_VAULT;1.1;AES256;default\n306434363232396331646330346361316566336430326263316239333231373035316333633539\n636430313539363562333461323531376635386438616435346535355d0a'
    assert(do_unvault(encrypted_data, secret, vaultid) == plain_data)


# Generated at 2022-06-22 11:51:00.871135
# Unit test for function do_vault
def test_do_vault():
    """Unit test for function do_vault"""
    secret = 'ansible'
    salt = 'ansible'
    # Do the encryption.
    result = do_vault('hello world', secret, salt)
    # Decrypt the data.
    decryption = do_unvault(result, secret)
    # Assert the results.
    assert decryption == 'hello world'



# Generated at 2022-06-22 11:51:12.910229
# Unit test for function do_vault
def test_do_vault():
    v = do_vault('test_data', 'testing', vaultid='test_vault')

# Generated at 2022-06-22 11:51:16.436251
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("test", "secret", wrap_object=True).startswith("$ANSIBLE_VAULT;")


# Generated at 2022-06-22 11:51:29.069178
# Unit test for function do_vault
def test_do_vault():
    data = 'mysecret'
    secret = 'mysecret'

    # Test data encryption
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:51:38.392501
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import is_encrypted, VaultSecret, VaultLib
    from ansible.module_utils._text import to_text, to_bytes

    # Test vault
    secret = 'password'
    data = 'my secret data'
    vault = '$ANSIBLE_VAULT;1.1;AES256;filter_default\n30346439333564653738643055633962365761343435646639393366323261663532363864343339\n62333461656266316434366465653166656131363865333265623132386531616538363335363038\n6362346164343766'

# Generated at 2022-06-22 11:51:49.584767
# Unit test for function do_vault
def test_do_vault():

    secret = "s3cr3t"
    data = "test string"

    assert do_vault(data, secret)

    assert do_vault("{{test_var}}", secret)

    try:
        do_vault(4, secret)
    except AnsibleFilterTypeError:
        assert True
    else:
        assert False

    try:
        do_vault(data, 4)
    except AnsibleFilterTypeError:
        assert True
    else:
        assert False

    try:
        do_vault("{{test_var}}", 4)
    except AnsibleFilterTypeError:
        assert True
    else:
        assert False



# Generated at 2022-06-22 11:51:59.468773
# Unit test for function do_vault
def test_do_vault():
    secret = "the_secret"
    salt = "the_salt"
    data_str = "The data"

# Generated at 2022-06-22 11:52:05.780406
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(None, None) == None
    assert do_unvault(None, "test") == None
    assert do_unvault("test", None) == 'test'

    assert do_unvault("test", "test") == 'test'
    assert do_unvault("test", "test", 'test') == 'test'

    # Test that unvault doesn't decrypt something not encrypted
    assert do_unvault("$ANSIBLE_VAULT;9.9;TEST_TRANSPORT;TEST_ID\nTEST_DATA", "test") == u'$ANSIBLE_VAULT;9.9;TEST_TRANSPORT;TEST_ID\nTEST_DATA'

# Generated at 2022-06-22 11:52:15.210538
# Unit test for function do_vault
def test_do_vault():
    secret = 'testpw'
    data = 'hello'
    salt = 'test'

    vault = do_vault(data, secret, salt)

# Generated at 2022-06-22 11:52:25.424253
# Unit test for function do_unvault
def test_do_unvault():
    import os
    test_dir = os.path.dirname(os.path.abspath(__file__))
    # Use password file to decrypt encrypted file
    test_password_file = os.path.join(test_dir, 'vault_password.txt')
    test_encrypted_file = os.path.join(test_dir, 'vault_encrypted_file.txt')

    # Decrypt encrypted file with password from file
    with open(test_password_file, 'r') as fp:
        password = fp.read()

    with open(test_encrypted_file, 'r') as fp:
        encrypted_data = fp.read()

    assert do_unvault(encrypted_data, password) == "Hello Ansible Vault!\n"



# Generated at 2022-06-22 11:52:37.056957
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:50.401095
# Unit test for function do_vault
def test_do_vault():
    f = FilterModule()
    assert f.filters()['vault']('test', 'hunter2') == "$ANSIBLE_VAULT;1.2;AES256;filter_default\n30393930353438633932313734633531353730316363613164326263386164363734653131373066\n6538326231666334656433313936643363613664383937643337386430616230643361630a373834\n61396434633864656530643933326561323065643233616464383530643665366433353064653062\n63343162616564356137313463373564633731636665650a"

# Generated at 2022-06-22 11:53:02.709097
# Unit test for function do_vault
def test_do_vault():
    # Test that non-string arguments throw an exception
    try:
        do_vault(1, "secret")
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("do_vault did not raise AnsibleFilterTypeError when passed a non-string argument")
    try:
        do_vault("data", 1)
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("do_vault did not raise AnsibleFilterTypeError when passed a non-string argument")
    # Test that string arguments are encrypted
    test_string = "my secret string"
    vault_value = do_vault(test_string, "secret")
    # Test that the decrypted string matches the argument

# Generated at 2022-06-22 11:53:08.068972
# Unit test for function do_vault
def test_do_vault():
    secret = '$ANSIBLE_VAULT;1.2;AES256;test_vault_id_name\n35393962303833323763633239363061353365643630666539396232376165663437626261336465\n37646234333563646437363732306561666365633235316531353262623037313631323361346538\n353762326262616463663261623663663935376232'
    salt = 'test_salt'
    data = 'test_data'
    vaultid = 'test_vaultid'
    wrap_object = False

# Generated at 2022-06-22 11:53:17.825687
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.module_utils.six.moves import xrange
    from ansible.module_utils.basic import AnsibleModule, to_bytes
    from ansible.parsing.vault import VaultSecret, VaultLib, VaultAES256

    def v2_encrypt_data(data, secret, vaultid='default', salt=None):
        vs = VaultSecret(to_bytes(secret))
        vl = VaultLib()
        vault = vl.encrypt(to_bytes(data), vs, vaultid, salt)
        return vault

    # Test Parameter

# Generated at 2022-06-22 11:53:30.057528
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("ANSIBLESSL", "BLAH", vaultid='testcases', wrap_object=False) == "ANSIBLE VAULT;1.1;AES256\n303636646533393830383336323137636539663337312d63363461323163323230333838633232330a633463623137636632316238626165613466323235396532633138336261356436393664336138620a36306639353764646339306437353964343836643738396233353233613931333536313064653938\n"

# Generated at 2022-06-22 11:53:35.428027
# Unit test for function do_vault
def test_do_vault():

    secret = 'my_secret'
    from_data = 'my_data'
    salt = VaultSecret.generate_salt()
    vault = do_vault(from_data, secret, salt, 'filter_test')

    display.vvvv("Vaulted data: %s" % vault)

    assert isinstance(vault, string_types)



# Generated at 2022-06-22 11:53:45.340566
# Unit test for function do_vault
def test_do_vault():
    secret = "A1b2_c3d4"
    plain_text = "this is the plain text"
    salt = "$5$rounds=43000$tVuZtY4Ebx4i4XyF$"
    vaulted_text = do_vault(plain_text, secret, salt)

# Generated at 2022-06-22 11:53:55.032777
# Unit test for function do_unvault
def test_do_unvault():
    h = FilterModule()
    h.filters()
    secret = 'testsecret'
    vaultid = 'abc'
    data = 'testdata'
    vault = do_vault(data, secret, vaultid=vaultid, wrap_object=True)
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)
    unvault = do_unvault(vault, secret)
    assert isinstance(unvault, string_types)
    assert unvault == data

# Generated at 2022-06-22 11:53:59.762347
# Unit test for function do_vault
def test_do_vault():
    secret = "testing"
    salt = "salt-sample"
    data = "Hello world"
    vault = do_vault(data, secret, salt, '')
    assert isinstance(vault, str)
    assert vault.strip()
    assert vault_check(vault)


# Generated at 2022-06-22 11:54:08.722731
# Unit test for function do_vault
def test_do_vault():
    '''
    Test do_vault
    '''

    # Test all good

# Generated at 2022-06-22 11:54:12.479805
# Unit test for function do_vault
def test_do_vault():
    assert do_vault(data='password', secret='verysecretpassword') == "!vault |\n          $ANSIBLE_VAULT;1.2;AES256;filter_default\n          353231653937353436343661643437633562613939346664363236613930396264323935666434\n          353266396235326263323862633036663530346639303166613730653138626533\n          \n          "


# Generated at 2022-06-22 11:54:23.980071
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("hello", "secret") == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          35303962356266326266666165383334316566373738333836366262613166636232383830653362\n          66666465333764316661623133353638363866643163396664316363326637303939356164326362\n          3038393364390a666539326661613332363131306133623033666437616362323164613337633764\n          3330386166653266303330636531646334353936343836303131323765333062646661633862326\n          5363\n"

# Generated at 2022-06-22 11:54:34.726384
# Unit test for function do_vault
def test_do_vault():
    '''
      Test that do_vault is working as expected
    '''

    raw_string = u'This is a test'
    vaultid = 'test_default'
    secret = '$ANSIBLE_VAULT;1.1;AES256\n6437623031613461316137376433666336306439343139633338623463323235383131633165353634\nasdjv;jkhasdljkfh;asljkdfh;'
    salt = 'salt_for_testing'
    vaulted_string = do_vault(raw_string, secret, salt, vaultid)

    # Check if the output is a string

# Generated at 2022-06-22 11:54:43.683431
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('Test String', 'testsecret123') == '$ANSIBLE_VAULT;1.1;AES256;ansible\n393130313339326263303565643838303231383561386138636332623431363565313338633062356\n3962303135653564363766643738313464383537333039366434356564393130623139353438303733\n3436616363313134656330663862653363356333643303266383035666164656561633831366133613\n33032656332383162323939613561303965343536626265326532373439663562303237\n'


# Generated at 2022-06-22 11:54:54.835894
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:58.879860
# Unit test for function do_unvault
def test_do_unvault():
    data = "secrets"
    secret = "ansible"
    vaultid = "filter_default"
    vault = do_vault(data,secret)
    assert do_unvault(vault, secret, vaultid) == data

# Generated at 2022-06-22 11:55:09.977280
# Unit test for function do_unvault

# Generated at 2022-06-22 11:55:15.652973
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault(data='test_do_vault', secret='your_secret')
    print(vault)


# Generated at 2022-06-22 11:55:27.129291
# Unit test for function do_vault
def test_do_vault():
    # Test for Undefined error
    secret = Undefined()
    result = do_vault('test', secret)
    assert result is Undefined, "test_do_vault: expected: %s, actual: %s" %(Undefined, result)

    # Test for invalid type of secret passed
    secret = 'secret'
    data = 'test'
    vaultid = 'test_default'
    result = do_vault(data, secret, vaultid=vaultid)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault.vault_id == 'test_default', "test_do_vault: expected: %s, actual: %s" %('test_default', result.vault.vault_id)

    # Test for invalid type of data passed

# Generated at 2022-06-22 11:55:39.062628
# Unit test for function do_vault
def test_do_vault():
    assert '' == do_vault('', 'secret')
    assert '' == do_vault(None, 'secret')

# Generated at 2022-06-22 11:55:45.829503
# Unit test for function do_vault
def test_do_vault():
    vault_secret = 'secret'
    vault_salt = 'salt'
    vault_id = 'test'
    # string
    try:
        data = 'string'
        result = do_vault(data, vault_secret, vault_salt, vault_id)
    except AnsibleFilterError as e:
        print('unit test failed: %s' % e)
    if isinstance(result, AnsibleVaultEncryptedUnicode):
        print('unit test passed for string')

    # dict
    try:
        data = dict(a=1, b=2)
        result = do_vault(data, vault_secret, vault_salt, vault_id, wrap_object=True)
    except AnsibleFilterError as e:
        print('unit test failed: %s' % e)

# Unit

# Generated at 2022-06-22 11:55:57.494256
# Unit test for function do_vault
def test_do_vault():
    import os
    import sys
    import unittest
    from tempfile import TemporaryDirectory
    from ansible.parsing.vault import VaultSecret, VaultLib
    from ansible.module_utils.six.moves import builtins

    class TestVaultModule(unittest.TestCase):

        def setUp(self):
            self.vault_id = "test_id"
            self.vault = VaultLib()
            tmpdir = TemporaryDirectory()
            # create a custom ansible.cfg for this test to avoid loading default user config
            self.ansible_cfg_path = os.path.join(tmpdir.name, "ansible.cfg")
            with open(self.ansible_cfg_path, "w") as f:
                f.write("[defaults]\n")

# Generated at 2022-06-22 11:56:08.464190
# Unit test for function do_unvault

# Generated at 2022-06-22 11:56:10.777202
# Unit test for function do_vault
def test_do_vault():
    fm = FilterModule()
    dv = fm.filters()['vault']

    vault = dv('hello', 'password')

    assert vault is not None


# Generated at 2022-06-22 11:56:22.773881
# Unit test for function do_vault
def test_do_vault():
    secret = "hunter2"
    salt = "saltysalt"
    test_data = [
        {
            'in': 'test',
            'want': False
        },
        {
            'in': AnsibleVaultEncryptedUnicode.from_encrypted_text('$ANSIBLE_VAULT;1.1;AES256;test\n33353164643936356264336635303163323064323162336365383038663361623966376663313230\n66323462643636386538313732353165323531666537663462666331323666343232376563306233\n3036636438343565\n', secret, salt),
            'want': True
        }
    ]


# Generated at 2022-06-22 11:56:34.744769
# Unit test for function do_vault
def test_do_vault():

    plaintext = 'Hello world'
    secret = 'mysecret'
    salt = 'salt'
    vaultid = 'test'

# Generated at 2022-06-22 11:56:44.423213
# Unit test for function do_vault
def test_do_vault():
    """ test_do_vault()
    Test that the vault filter encrypts a string.
    Note that this test uses the pytest_assertrepr_compare hook to
    display the encrypted string if the test fails, to help debug.
    """
    import pytest

    o = do_vault('data', 'my secret', 'my salt')

    def pytest_assertrepr_compare(op, left, right):
        if op == "==":
            return ['Encrypted value: %s' % repr(left), 'Expected: %s' % repr(right)]

    assert isinstance(o, AnsibleVaultEncryptedUnicode)
    assert o.data == 'data'
    assert o.vault._vault_secrets[o.vaultid].secret == 'my secret'
    assert o.vault._

# Generated at 2022-06-22 11:56:54.879851
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    data = 'mydata'
    vault = do_vault(data, secret)
    assert isinstance(vault, string_types)
    assert vault != data
    try:
        do_vault('mydata', [])
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError('Failed to detect wrong type in filter do_vault')



# Generated at 2022-06-22 11:57:05.464715
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    vaultid = 'filter_default'

    # testing with wrap_object set to True
    data = 'data'
    wrap_object = True
    result = do_vault(data, secret, salt, vaultid, wrap_object)
    assert result.__class__.__name__ == 'AnsibleVaultEncryptedUnicode'
    wrap_object = False
    result = do_vault(data, secret, salt, vaultid, wrap_object)
    assert result.__class__.__name__ == 'str'

    #testing with different data types
    data = [1,2,3]

# Generated at 2022-06-22 11:57:16.455792
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:28.508965
# Unit test for function do_vault
def test_do_vault():
    secret = 'ansible'
    data1 = 'secret'

    # Wrap object is False
    vault = do_vault(data1, secret, wrap_object=False)
    vault = vault.strip("\n")
    assert(vault.startswith("$ANSIBLE_VAULT;"))
    assert(vault.endswith("=="))

    # Wrap object is True
    vault = do_vault(data1, secret, wrap_object=True)
    assert(isinstance(vault, AnsibleVaultEncryptedUnicode))

    # Pass vault as AnsibleVaultEncryptedUnicode
    vault = do_vault(vault, secret)
    assert(isinstance(vault, AnsibleVaultEncryptedUnicode))

    # Check Undefined is raised

# Generated at 2022-06-22 11:57:40.131073
# Unit test for function do_unvault
def test_do_unvault():
    from pytest import raises
    from ansible.module_utils.six import b
    from ansible.parsing.vault import is_encrypted
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # string is not encrypted
    assert test_secret == do_unvault(test_secret, test_secret)
    assert AnsibleVaultEncryptedUnicode(test_secret) == do_unvault(AnsibleVaultEncryptedUnicode(test_secret), test_secret)

    assert not is_encrypted(test_secret)

    # is_encrypted is passing because it's an AnsibleVaultEncryptedUnicode
    assert not is_encrypted(AnsibleVaultEncryptedUnicode(test_secret))

    # Not encrypted

# Generated at 2022-06-22 11:57:50.488801
# Unit test for function do_vault
def test_do_vault():
    secret = "MeuSegredo"
    vaultid = "default_vault"
    data = "this is my data"
    salt = None
    wrap_object = True


# Generated at 2022-06-22 11:58:02.318342
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    data = 'unvaulted_data'
    vaultid = 'filter_default'
    wrap_object = False

# Generated at 2022-06-22 11:58:10.406602
# Unit test for function do_vault
def test_do_vault():

    assert do_vault('mydata', 'mysecret', salt='puppet', vaultid='filter_default') == u"$ANSIBLE_VAULT;1.1;AES256;puppet\n63386261623138613863353733363835386531326230626237356135336538306365336532313430\n643166623362333265666235343664316262636631376366336633664346665\ntest_do_vault.py\n"



# Generated at 2022-06-22 11:58:20.671051
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(
        vault='$ANSIBLE_VAULT;1.1;AES256\n63313233376237373934306337633539663439633661353438353062643161623431336132653661\n35303238333834613162333038663361333432626563396265396433653635653834643162623138\n31336532626563316363343637333439366634383032383361376130623532393963343036353436\n3361343637303766\n',
        secret='password',
    ) == 'Hello world'

# Generated at 2022-06-22 11:58:31.768292
# Unit test for function do_vault
def test_do_vault():
    # Test case when correct values are passed
    assert do_vault('Test', 'MySecret') == '$ANSIBLE_VAULT;1.1;AES256\n3635383366386334363336393966333234623333636238636535373036323363363735376162386130\n6564383939376566633764663364333930346536313563303236656534616537323031666532623361\n3766353765663039353361306133383064373361323463\n', \
        "Vaulting failed unexpectedly"

    # Test case with empty string passed

# Generated at 2022-06-22 11:58:46.818053
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:57.709046
# Unit test for function do_unvault
def test_do_unvault():
    import jinja2

    # Parameter or variable values for unit test
    data = "abcdefghijklmnopqrstuvwxyz1234567890"
    secret = "changeme"
    vaultid = "test_vault"

    # Generate the encrypted value
    j_env = jinja2.Environment(undefined=jinja2.StrictUndefined)
    j_env.filters["vault"] = do_vault
    encrypted_value = j_env.from_string("{{ '%s' | vault('%s', '%s') }}" % (data, secret, vaultid)).render().strip()
    display.display("Encrypted value: %s" % encrypted_value)

    # Decrypt the value using function do_unvault
    decrypted_value = do_unvault

# Generated at 2022-06-22 11:59:08.133586
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    data = 'foo'
    secret = 'test'
    salt = '12345'

# Generated at 2022-06-22 11:59:15.096515
# Unit test for function do_vault
def test_do_vault():

    # Test different inputs, only string should work
    data = 'this is a test string'
    secret = 'this is a test secret'
    assert do_vault(data, secret)
    # secret can be an AnsibleVaultEncryptedUnicode
    secret = AnsibleVaultEncryptedUnicode('this is a test secret')
    assert do_vault(data, secret)
    # data can be an AnsibleVaultEncryptedUnicode
    data = AnsibleVaultEncryptedUnicode('this is a test string')
    assert do_vault(data, secret)
    # All parameters can be an AnsibleVaultEncryptedUnicode
    data = AnsibleVaultEncryptedUnicode('this is a test string')
    secret = AnsibleVaultEncryptedUnicode('this is a test secret')
   

# Generated at 2022-06-22 11:59:26.140409
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foo', 'touch', 'salt', wrap_object=True) == '$ANSIBLE_VAULT;1.1;AES256;salt\n3639393435663739343836333539326164383262663338363830363439616232343630636437\n6564396535643563376365386635346536366237376563613731363338346639363137366333\n3830386634333566393265313230323731343133613364343533653064353336\n'

# Generated at 2022-06-22 11:59:34.785539
# Unit test for function do_vault
def test_do_vault():
    secret = 'testvault'
    data = 'testdata'
    vault = do_vault(data, secret)

# Generated at 2022-06-22 11:59:43.559443
# Unit test for function do_vault
def test_do_vault():

    assert do_vault('string', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n633236386430616336643366653631343033613435383938346237383538653562336237360a33303235616235353733303834653735666164303933653766393733336632336239620a31363933626239313861373134323161303739663864386636326236636638633167610a3039656261316133356336653636353965356633363966363338333839623065346130\n'

# Generated at 2022-06-22 11:59:53.828139
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    env = jinja2.Environment()
    env.filters['vault'] = do_vault

    assert '$ANSIBLE_VAULT' in env.from_string('{{ "Test Data" | vault("bad_secret") }}').render()
    assert '$ANSIBLE_VAULT' in env.from_string('{{ "Test Data" | vault("bad_secret", salt="test") }}').render()
    assert '$ANSIBLE_VAULT' in env.from_string('{{ "Test Data" | vault("bad_secret", vaultid="test") }}').render()

    assert '$ANSIBLE_VAULT' in env.from_string('{{ "Test Data" | vault("bad_secret" | string, salt="test") }}').render()

# Generated at 2022-06-22 12:00:02.263151
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'Rd1WxmUZo6eZGzbU'
    vaultid = 'vaultid'
    data = 'abc'

    # Test without salt
    result = do_vault(data, secret, vaultid=vaultid)
    assert is_encrypted(result)
    assert do_unvault(result, secret, vaultid=vaultid) == data

    # Test with salt
    result = do_vault(data, secret, salt=salt, vaultid=vaultid)
    assert is_encrypted(result)
    assert do_unvault(result, secret, vaultid=vaultid) == data

    # Test extra arguments

# Generated at 2022-06-22 12:00:14.127235
# Unit test for function do_unvault
def test_do_unvault():
    vault_1 = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n363861656433396261303935656339333235346437356564313762653234373664363330373763\n373835366334636537663735396631346335363930313933343730376534656162663763376165\n393161373338663132306566376236393130\n')

# Generated at 2022-06-22 12:00:23.691364
# Unit test for function do_vault
def test_do_vault():
    secret = "foo"
    data = "bar"
    salt = None
    vaultid = 'test'
    wrap_object = False
    a = do_vault(data, secret, salt, vaultid, wrap_object)
    b = do_vault(data, secret, salt, vaultid, wrap_object)
    assert a == b


# Generated at 2022-06-22 12:00:35.458383
# Unit test for function do_vault
def test_do_vault():
    secret = 'mypassword'
    salt = 'my_salt'
    vaultid = 'filter_default'
    wrap_object = False

    data = 'root:$6$ABCDEFGHIJ$AZ1x2y3z4s5s6s7s8s9s0s1s2s3s4s5s6s7s8s9s0s1s2s3s4s5s6s7s8s9s0s1s2s3s4s5s6s7s8s9s0t'