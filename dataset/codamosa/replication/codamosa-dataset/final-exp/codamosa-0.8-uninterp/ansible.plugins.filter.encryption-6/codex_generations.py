

# Generated at 2022-06-22 11:50:48.904250
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret

     # Test for jinja2 string datatype
    vault_string = do_vault("Don't Panic!", "my secret", "my salt", "default", True)
    assert isinstance(vault_string, AnsibleVaultEncryptedUnicode)
    assert isinstance(vault_string.data, binary_type)
    assert isinstance(vault_string.vault_id, Undefined)
    assert isinstance(vault_string.cipher, Undefined)
    assert isinstance(vault_string.vault, VaultLib)
    assert isinstance(vault_string.identifier, byte)

    # Test for jinja2 bytearray datatype

# Generated at 2022-06-22 11:50:58.310650
# Unit test for function do_vault
def test_do_vault():

    result = do_vault("passw0rd!", "secret_password")

# Generated at 2022-06-22 11:51:07.942470
# Unit test for function do_unvault
def test_do_unvault():

    secret = '042d4062-3b99-40e3-9f6f-c18ed8efa2a2'

    # Test 1: case: empty string
    test_input = {
        'vault': '',
        'secret': secret
    }
    expected = ''
    output = do_unvault(**test_input)
    assert expected == output, 'Error decoded. Got {} but expected {}'.format(output, expected)

    # Test 2: case: encrypted string

# Generated at 2022-06-22 11:51:16.720850
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("value", "vault_secret") == "!vault |$ANSIBLE_VAULT;1.1;AES256\n336165646630306332666264643530366465353664653338376263613531353135323531623763316\n39396438343833303537363539376333626130666331333838613032393065303236616437393163\n656637313030343833353230623064636363373432666161623730\n"


# Generated at 2022-06-22 11:51:29.312725
# Unit test for function do_vault
def test_do_vault():
    passwd = 'filter_default_pass'
    vault_file = 'encrypted.yaml'
    j2_template = """
        {%- import_yaml encrypted.yaml as vault_data -%}
        {%- set data = vault_data['secrets']['credentials']['username'] -%}
        {%- set vaulted_data = data | vault(passwd) -%}
        {%- set unvaulted_data = vaulted_data | unvault(passwd) -%}

        Data: {{ data }}

        Vaulted Data:
        {% for item in vaulted_data %}
            {{ item }}
        {% endfor %}

        Unvaulted Data: {{ unvaulted_data }}
    """


# Generated at 2022-06-22 11:51:33.006615
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault(b'vaulted_data', "secret") == b'vaulted_data'
    assert do_unvault('vaulted_data', "secret") == b'vaulted_data'

# Generated at 2022-06-22 11:51:44.951732
# Unit test for function do_vault
def test_do_vault():
    for secret in [u'abc', b'abc']:
        for salt in [u'abc', b'abc']:
            for data in [u'val', b'val', 123]:
                for wrap_object in [True, False]:
                    assert do_vault('val', secret, salt, wrap_object=wrap_object) == do_vault(u'val', secret, salt, wrap_object=wrap_object)
                    assert do_vault('val', secret, wrap_object=wrap_object) == do_vault(u'val', secret, wrap_object=wrap_object)
                    assert do_vault('val', secret, salt, 'myid', wrap_object=wrap_object) == do_vault(u'val', secret, salt, 'myid', wrap_object=wrap_object)
                    assert do_v

# Generated at 2022-06-22 11:51:55.066319
# Unit test for function do_unvault
def test_do_unvault():
    vault_id = "vault_id_1"
    secret = "secret"
    some_string = "some_string"

# Generated at 2022-06-22 11:52:03.741440
# Unit test for function do_vault
def test_do_vault():
    # Invalid secret
    invalid_secret = ['', [1], {}, True, False, 1, 0]

    for bad_secret in invalid_secret:
        try:
            do_vault('test', bad_secret)
        except AnsibleFilterTypeError as e:
            assert 'Secret passed' in str(e)
        except:
            assert False

    # Invalid data
    invalid_data = ['', [1], {}, True, False, 1, 0]

    for bad_data in invalid_data:
        try:
            do_vault(bad_data, 'secret')
        except AnsibleFilterTypeError as e:
            assert 'Can only vault strings' in str(e)
        except:
            assert False


# Generated at 2022-06-22 11:52:15.388529
# Unit test for function do_vault
def test_do_vault():
    secret = "s3cr3t"
    data = "secret_data"


# Generated at 2022-06-22 11:52:23.955777
# Unit test for function do_vault
def test_do_vault():
    def vault(secret, data):
        return do_vault(secret=secret, data=data)

    assert "!vault |" in vault("foobar", "barfoo")
    assert "!vault |" in vault("foobar", "barfoo")
    assert "!vault |" in vault("foobar", "barfoo")
    assert "!vault |" in vault("foobar", "barfoo")


# Generated at 2022-06-22 11:52:35.628537
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.six.moves import reload_module
    from ansible.module_utils.six import PY3
    import ansible.parsing.yaml.objects

    reload_module(ansible.parsing.yaml.objects)

    # The test ensures the encrypted result is compatible with previous ansible versions.
    # Please make sure the version of ansible the test is executed against is corresponding to the
    # `expected` results
    # Also the test requires PyYAML to be installed
    secret = 'testsecret'
    # the test data is from ansible/test/units/utils/test_vault.py
    data = 'password'
    vault_obj = do_vault(data, secret, wrap_object=True)

# Generated at 2022-06-22 11:52:48.670808
# Unit test for function do_unvault
def test_do_unvault():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))

    import ansible.constants as C
    import ansible.parsing.yaml.objects as objects

    unvault_secret = 'test_password'
    secret = VaultSecret(unvault_secret)
    vl = VaultLib([('test_vault_id', secret)])

    # Encrypt a secret, then decrypt it back to the same value
    test_secret = b'plain_test_secret'
    encrypted_test_secret = vl.encrypt(test_secret, secret, 'test_vault_id')
    assert test_secret == do_unvault(encrypted_test_secret, unvault_secret)

# Generated at 2022-06-22 11:52:52.186402
# Unit test for function do_unvault
def test_do_unvault():
    # basic working and error check
    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256;fcole3\n363765653736656261666339623661373835303636336639343537616133316664336266393362\n383965376361623461623763653164363530383462333861300a3735653062316432333433386336\n37363038333566306361626432316537393564313931346131613238316331376566353336346564\n35643765376163360a643861323861613835643534656637', 'fcole') == 'fc'

# Generated at 2022-06-22 11:53:02.012576
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:11.436143
# Unit test for function do_vault
def test_do_vault():
    result = do_vault("this_is_a_password", "this_is_a_secret")

# Generated at 2022-06-22 11:53:18.260787
# Unit test for function do_vault
def test_do_vault():
    assert isinstance(do_vault('string', 'test'), str)
    assert isinstance(do_vault('string', 'test', vaultid='foobar'), str)

# Generated at 2022-06-22 11:53:23.993707
# Unit test for function do_vault
def test_do_vault():
    vl = VaultLib()
    vs = VaultSecret('secret')
    result = do_vault(data='test_vault', secret='secret', salt='salt', vaultid='filter_default', wrap_object=False)
    decrypted_data = vl.decrypt(result)
    assert decrypted_data == 'test_vault'


# Generated at 2022-06-22 11:53:35.837119
# Unit test for function do_unvault
def test_do_unvault():
    ''' unit test for function do_unvault '''
    # pylint: disable=unused-argument,no-self-argument
    # pylint: disable=blacklisted-name,protected-access
    class FilterModule(object):
        ''' Mock class '''
        def filters(self):
            ''' mock function '''
            return {'unvault': do_unvault}

    for filter_type in ['string', 'unicode']:
        for data_type in ['string', 'unicode']:

            secret = "abcd1234"
            data = "password_is_password"

            if filter_type == 'unicode':
                secret = u'abcd1234'
            if data_type == 'unicode':
                data = u"password_is_password"

            vault = do_v

# Generated at 2022-06-22 11:53:42.363251
# Unit test for function do_vault
def test_do_vault():
    secret = "This is a secret"
    salt = "I am a salt"
    vaultid = "filter_default"
    data_one = "This is data"
    data_two = "I am data"
    one = do_vault(data_one, secret, salt, vaultid)
    two = do_vault(data_two, secret, salt, vaultid)
    assert one != two


# Generated at 2022-06-22 11:53:56.544043
# Unit test for function do_vault
def test_do_vault():
    import pytest
    from ansible.parsing.vault import VaultSecret, VaultLib

    test_data = "test"

    # single password provided
    vs = VaultSecret('secret')
    vl = VaultLib()
    test_vault = do_vault(test_data, vs.unlock(), salt=None, vaultid='filter_default', wrap_object=False)
    assert test_vault == vl.encrypt(to_bytes(test_data), vs, vaultid='filter_default', salt=None)
    assert test_vault == vl.decrypt(do_vault(test_data, vs.unlock(), salt=None, vaultid='filter_default', wrap_object=False))

    # multiple passwords provided
    vs = VaultSecret(['secret', 'secrets'])
    vl = Vault

# Generated at 2022-06-22 11:54:05.119275
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'

    # Testing valid inputs
    data = 'data'
    vault = do_vault(data, secret)

    # Testing invalid input
    try:
        data = ['data']
        vault = do_vault(data, secret)
        assert False
    except AnsibleFilterTypeError:
        assert True

    # Testing invalid input
    try:
        secret = ['secret']
        vault = do_vault(data, secret)
        assert False
    except AnsibleFilterTypeError:
        assert True



# Generated at 2022-06-22 11:54:14.847384
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:26.655227
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('ansible', 'changeme', 'salt', 'vault_id') == '!vault |\n  $ANSIBLE_VAULT;1.2;AES256;vault_id;salt;\n  7677327052326e6933687a4b326945666e4f343379334b4d4f2b4a4d304b524f304b30686247317047\n  \n  39735a706a384b70326956715a414e6638776b736c6449703d0a\n'.encode('utf-8')

# Generated at 2022-06-22 11:54:31.995838
# Unit test for function do_unvault
def test_do_unvault():
    """
    test for function do_unvault
    """
    text_to_encrypt = "my_secret_string"
    secret = "my_secret_key"
    do_unvault(do_vault(text_to_encrypt, secret), secret)

# Generated at 2022-06-22 11:54:42.221469
# Unit test for function do_vault
def test_do_vault():
    data = 'abcdef'
    secret = 'abcdefg'

    # call do_vault
    expected_result = '$ANSIBLE_VAULT;1.1;AES256\n38373633363336633637353865636262613661323064663837363336333663363735386563626261366132306466\n35373864386261343138633362396362303236616333626262333264663833623661393136613431366163326466\n3638303161616535343336643566323934656530663438376566313465333936346364'


# Generated at 2022-06-22 11:54:49.363977
# Unit test for function do_vault
def test_do_vault():
    secret = "test"
    data = "test"
    vault = do_vault(data, secret)
    assert vault == '$ANSIBLE_VAULT;1.1;AES256\n643832373136636636646630376437623936353264653661333061306436343539313463396537\ne363065373139656638613163356335393063316530356463366565316639\n'


# Generated at 2022-06-22 11:55:00.686667
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:10.436699
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:22.102105
# Unit test for function do_vault
def test_do_vault():
    test_secret = "test_secret"

# Generated at 2022-06-22 11:55:36.081458
# Unit test for function do_unvault

# Generated at 2022-06-22 11:55:44.594257
# Unit test for function do_vault
def test_do_vault():
    import os
    import hashlib
    import hmac
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.vault import VaultSecret

    data = 'data'
    secret = 'test_secret'
    salt = '4f72b2a7'
    vaultid = 'filter_default'
    wrap_object = True

    vs = VaultSecret(secret)
    hm = hmac.new(vs.secret, salt.encode('utf-8'), digestmod=hashlib.sha256)
    hmac_digest = hm.hexdigest()[0:64]


# Generated at 2022-06-22 11:55:56.092871
# Unit test for function do_unvault
def test_do_unvault():
    display.verbosity = 3

# Generated at 2022-06-22 11:55:59.877189
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("secret_value", "secret_password") == "AQAAAAEAACaETMPF+0gJwQLC8OoOzLqu1+DmuQ=="


# Generated at 2022-06-22 11:56:02.874046
# Unit test for function do_vault
def test_do_vault():
    data = b'hello world'
    secret = b'this is my secret'
    vault = do_vault(data, secret)
    assert isinstance(vault, string_types)
    assert is_encrypted(vault)


# Generated at 2022-06-22 11:56:10.115134
# Unit test for function do_unvault
def test_do_unvault():

    test_string = 'Hello world'
    secret_passphrase = 'secret_passphrase'
    vaultid = 'filter_default'

    # Test case 1: input string is not encrypted
    actual_output = do_unvault(test_string, secret_passphrase, vaultid)
    assert test_string == actual_output

    # Test case 2: input string is encrypted
    vault_string = do_vault(test_string, secret_passphrase, None, vaultid)
    actual_output = do_unvault(vault_string, secret_passphrase, vaultid)
    assert test_string == actual_output



# Generated at 2022-06-22 11:56:22.024402
# Unit test for function do_unvault
def test_do_unvault():
    import textwrap

# Generated at 2022-06-22 11:56:24.587678
# Unit test for function do_unvault
def test_do_unvault():

    assert do_unvault('$ANSIBLE_VAULT;1.1;AES256','vault','filter_default') == 'vault'


# Generated at 2022-06-22 11:56:27.882556
# Unit test for function do_vault
def test_do_vault():
    data = 'my secret string'
    secret = 'my_secret'
    vault = do_vault(data, secret)
    assert is_encrypted(vault)


# Generated at 2022-06-22 11:56:36.010930
# Unit test for function do_vault
def test_do_vault():
    secret = b'123'
    no_wrap = False
    data = u"data"

    ret = do_vault(data, secret, wrap_object=no_wrap)
    assert isinstance(ret, string_types)
    assert ret.startswith("$ANSIBLE_VAULT")

    no_wrap = True
    ret = do_vault(data, secret, wrap_object=no_wrap)
    assert isinstance(ret, AnsibleVaultEncryptedUnicode)
    assert ret.startswith("$ANSIBLE_VAULT")



# Generated at 2022-06-22 11:56:41.089520
# Unit test for function do_vault
def test_do_vault():
    secret = "foo"
    data = "bar"
    result = do_vault(data, secret)
    assert result.startswith(b"$ANSIBLE_VAULT;")


# Generated at 2022-06-22 11:56:52.817818
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:04.150728
# Unit test for function do_vault

# Generated at 2022-06-22 11:57:14.010502
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:16.551427
# Unit test for function do_unvault
def test_do_unvault():
    unvault = do_unvault(do_vault('string1', 'secret1'), 'secret1')
    assert unvault == 'string1'


# Generated at 2022-06-22 11:57:28.604396
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('password', 'secret') == '$ANSIBLE_VAULT;1.1;AES256\n3261633237613463383161613839323135666539613561333438633233346438613637373330363\n373962313439396436663864336363343136616331323132303431626533356162336634336564\n393633366232626563623636653930656666636631643531306566653462653530383938386230\n633465346564636439643335'

# Generated at 2022-06-22 11:57:40.200642
# Unit test for function do_vault
def test_do_vault():
    data = 'hello world'
    secret = 'foo'
    salt = 'bar'
    vaultid = 'test'

    try:
        do_vault(data, secret, salt, vaultid, False)
    except Exception as e:
        raise AssertionError('%s raised when calling do_vault on a string' % e)

    try:
        do_vault(data, secret, salt, vaultid, True)
    except Exception as e:
        raise AssertionError('%s raised when calling do_vault on a string' % e)

    try:
        do_vault(data, secret, salt, vaultid, None)
    except Exception as e:
        raise AssertionError('%s raised when calling do_vault on a string' % e)


# Generated at 2022-06-22 11:57:50.630549
# Unit test for function do_vault
def test_do_vault():
    secret_string = 'test_string'

# Generated at 2022-06-22 11:58:02.427689
# Unit test for function do_vault
def test_do_vault():
    data = "foo bar"
    secret = "secret"
    salt = "secret"
    vaultid = "test_vault"

# Generated at 2022-06-22 11:58:14.293184
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.compat.tests import unittest

    vaultid = 'test_id'
    secret = 'secret'

# Generated at 2022-06-22 11:58:20.958555
# Unit test for function do_vault
def test_do_vault():
    secret = "password"
    data = "secrets"
    salt = 'salt'
    vaultid = 'test'
    vault = do_vault(data, secret, salt, vaultid, False)
    assert vault != ''
    assert vault != data
    assert vault != salt
    assert vault == do_vault(data, secret, salt, vaultid, False)
    assert vault != do_vault(data, secret, False, False)
    assert vault != do_vault(data, salt, salt, vaultid, False)
    assert vault != do_vault(secret, secret, salt, vaultid, False)


# Generated at 2022-06-22 11:58:30.600213
# Unit test for function do_unvault
def test_do_unvault():
    import pytest
    from ansible.parsing.vault import VaultSecret, VaultLib
    vs = VaultSecret('secret')
    vl = VaultLib()
    vault = vl.encrypt('encryptme', vs)
    data = ''
    vs = VaultSecret('secret')
    vl = VaultLib([('test', vs)])
    if is_encrypted(vault):
        try:
            data = vl.decrypt(vault)
        except Exception as e:
            raise AnsibleFilterError("Unable to decrypt: %s" % to_native(e), orig_exc=e)
    else:
        data = vault

    assert data == 'encryptme'

# Generated at 2022-06-22 11:58:39.277272
# Unit test for function do_unvault
def test_do_unvault():
    secret = "ansib1e-secr"
    vaultid = 'ansib1e-vau1t'
    plain_string = "test-string"

# Generated at 2022-06-22 11:58:48.689494
# Unit test for function do_vault
def test_do_vault():
    vault_data = do_vault('hello', secret='password', salt='a b c')
    assert vault_data == '$ANSIBLE_VAULT;1.1;AES256\n343936656664353066623039386435303634633232343263386164666136333532316130373331613\n66133336663635313331343133653734396262396663353730640a3938313863323739666435376634\n3931363730366465306262323031396561303462393731306331366263636661323532343035653639\n32326166393861383034320a3933383530663936646636353066', "Vault data is not properly encrypted"



# Generated at 2022-06-22 11:58:58.623475
# Unit test for function do_unvault
def test_do_unvault():

    vault_secret = "vault secret"
    input_vault_id = "vault_id is filter_default"
    output_vault_id = "filter_default"
    plain_data = "this is plain data"
    plain_data_unicode = u"this is plain data unicode"
    plain_data_bytes = b"this is plain data bytes"

    # test_aes_256_gcm96
    aes_256_gcm96 = do_vault(plain_data, vault_secret)

    assert is_encrypted(aes_256_gcm96)
    assert not is_encrypted(plain_data)

    assert do_unvault(aes_256_gcm96, vault_secret) == plain_data

# Generated at 2022-06-22 11:59:05.734502
# Unit test for function do_vault
def test_do_vault():
    secret = "mySecret"
    salt = b'salt'
    my_vault = do_vault("this is some super secret data", secret, salt=salt, vaultid='filter_default')

    assert isinstance(my_vault, string_types)

    my_unvault = do_unvault(my_vault, secret, vaultid='filter_default')
    assert my_unvault == "this is some super secret data"

# Unit test to validate the function do_unvault

# Generated at 2022-06-22 11:59:08.249086
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils.common.text.converters import to_unicode
    assert do_vault(to_unicode('hello world'), 'secret')


# Generated at 2022-06-22 11:59:15.212669
# Unit test for function do_vault
def test_do_vault():
    fake_secret = '$ANSIBLE_VAULT;1.1;AES256'
    fake_salt = '$ANSIBLE_VAULT;1.1;AES256'
    fake_data = 'foo bar'

# Generated at 2022-06-22 11:59:22.180939
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'secret') == """$ANSIBLE_VAULT;1.1;AES256
3364376262616231333339356662346435313765363965336465663633353264346533393865326
33623130666534653539343231663533363566383332666366633533646233303565383333383939
63303231366234
""".strip()


# Generated at 2022-06-22 11:59:29.911884
# Unit test for function do_vault
def test_do_vault():
    secret = 'foo'
    result = do_vault('bar', secret)

# Generated at 2022-06-22 11:59:36.225773
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('foo', 'secret')
    assert '$ANSIBLE_VAULT' in result


# Generated at 2022-06-22 11:59:47.612373
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'test'
    vaultid = 'test'
    vault1 = '$ANSIBLE_VAULT;1.2;AES256;ansible\n393633306637313737663330323936313862626631623538336133613931333139373562623763356333\n343737336538653637646232393365356637363639346237303839383661646565633466323762656636\n61366463343061653939613165383939653538636262386134645a\n'

# Generated at 2022-06-22 11:59:57.497424
# Unit test for function do_vault
def test_do_vault():
    data = do_vault("secret_data", "password")

# Generated at 2022-06-22 12:00:04.976580
# Unit test for function do_unvault
def test_do_unvault():
    settings = dict(
        secret='password',
        vaultid='vaultid',
        salt='salt',
        wrap_object=True
    )
    secret = settings['secret']
    vaultid = settings['vaultid']
    salt = settings['salt']
    wrap_object = settings['wrap_object']
    vault = do_vault('dummy', secret, salt, vaultid, wrap_object)

    assert(do_unvault(vault, secret, vaultid) == 'dummy')

# Generated at 2022-06-22 12:00:11.896540
# Unit test for function do_unvault
def test_do_unvault():
    result = do_unvault('$ANSIBLE_VAULT;1.1;AES256;jeff;3438393837396334646331636336643933306636353964386334373833323066613734396332353535346161653339633065666638303832633031333934333065333264333533', 'Dude')
    assert result == "This is a test string"

# Generated at 2022-06-22 12:00:22.705491
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils._text import to_bytes

    secret = to_bytes('foo')
    data = to_bytes('bar')
    salt = b'49233c61-3d3e-48f5-8c02-bde2d2915a79'
    vaultid = '1'
    wrap_object = False

    vs = VaultSecret(secret)
    vl = VaultLib()
    vault = vl.encrypt(data, vs, vaultid, salt)

    env = jinja2.Environment()
    out = env.from_string('{{ data|vault(secret, salt, vaultid, wrap_object) }}').render(locals())
    assert out == vault


# Generated at 2022-06-22 12:00:32.001347
# Unit test for function do_unvault
def test_do_unvault():
    # module = AnsibleModule(
    #     argument_spec=dict(
    #         data=dict(required=True)
    #     ),
    #     supports_check_mode=True
    # )
    # print('Got data: %s' % module.params['data'])
    filter = FilterModule()

    # Test undef value
    # assert filter.filters()['unvault'](module.params['data'], 'password', vaultid='test_id') == 'test'
    assert filter.filters()['unvault'](Undefined) == Undefined

    # Test strings

# Generated at 2022-06-22 12:00:39.810114
# Unit test for function do_vault
def test_do_vault():
    assert('$ANSIBLE_VAULT;1.1;AES256;testid\n343536336565386233316331323531353736363266613739626662373231633234633166386430\n393435666134313337646635396432373162633661383761376638333866346535366364653065\n383061633365\n' == do_vault(
        'mysecret',
        'mysecret'))
