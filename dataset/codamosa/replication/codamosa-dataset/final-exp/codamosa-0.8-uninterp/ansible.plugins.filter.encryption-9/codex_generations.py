

# Generated at 2022-06-22 11:50:48.357258
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    data = "data"
    data_vault = do_vault(data, secret)
    assert isinstance(data_vault, string_types)
    assert data_vault != data
    assert is_encrypted(data_vault)
    assert not is_encrypted(data)
    data = b"data"
    data_vault = do_vault(data, secret)
    assert isinstance(data_vault, binary_type)
    assert data_vault != data
    assert is_encrypted(data_vault)
    assert not is_encrypted(data)
    data_unvault = do_unvault(data_vault, secret)
    assert data_unvault == data


# Generated at 2022-06-22 11:50:57.109006
# Unit test for function do_unvault

# Generated at 2022-06-22 11:51:01.257865
# Unit test for function do_vault
def test_do_vault():
    secret = 'test_secret'
    data = 'This is test data from ansible'

    vault_data = do_vault(data, secret)
    assert isinstance(vault_data, string_types)
    assert vault_data is not None


# Generated at 2022-06-22 11:51:13.283974
# Unit test for function do_unvault
def test_do_unvault():
    secret_val = "A5H5V6R5"

# Generated at 2022-06-22 11:51:26.427412
# Unit test for function do_vault
def test_do_vault():
    secret = 'thevaultsecret'
    data = 'thestringtovault'
    salt = 'thevaultsalt'


# Generated at 2022-06-22 11:51:28.745735
# Unit test for function do_unvault
def test_do_unvault():
    secret = "foobar"
    test_str = "this is a test"
    vault_str = do_vault(test_str, secret)
    result_str = do_unvault(vault_str, secret)
    assert test_str == result_str

# Generated at 2022-06-22 11:51:38.241496
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import sys

    # Our test file.
    vault_filename = 'test_vault.txt'
    secret = 'secret'
    unvault_content = 'unvault\ncontent'

# Generated at 2022-06-22 11:51:39.027618
# Unit test for function do_unvault
def test_do_unvault():
    pass

# Generated at 2022-06-22 11:51:51.965370
# Unit test for function do_vault

# Generated at 2022-06-22 11:52:03.820368
# Unit test for function do_vault
def test_do_vault():
    import os
    secret = os.urandom(32)
    salt = os.urandom(32)
    plaintext_str = "Hello World"
    encrypted_str = "!vault |" + secret + "\n" + plaintext_str

    assert do_vault(plaintext_str, secret) == encrypted_str
    assert do_vault(plaintext_str, secret, salt) == encrypted_str
    assert do_vault(plaintext_str, secret, salt, '0') == encrypted_str
    assert do_vault(plaintext_str, secret, salt, '0', True) == encrypted_str
    assert do_vault(plaintext_str, secret, salt, '1') == encrypted_str
    assert do_vault(plaintext_str, secret, salt, '1', True) == encrypted_str

# Generated at 2022-06-22 11:52:09.892797
# Unit test for function do_vault
def test_do_vault():
    secret = "secret"
    data = "data"
    salt = ""
    vaultid = "vaultid"
    vault = "data"
    assert do_vault(data, secret, salt, vaultid) == vault


# Generated at 2022-06-22 11:52:16.062516
# Unit test for function do_vault
def test_do_vault():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.hostvars import HostVars

    # Verify that a string is returned by the vault filter
    # if the value isn't encrypted
    test_data = 'test_string'
    assert(do_vault(test_data, 'secret') is not None)
    assert(do_vault(test_data, 'secret') != '')
    assert(is_encrypted(do_vault(test_data, 'secret')))

    # Verify that a string is returned by the vault filter
    # if the value is encrypted
    assert(do_vault(do_vault(test_data, 'secret'), 'secret') is not None)

# Generated at 2022-06-22 11:52:26.248328
# Unit test for function do_unvault
def test_do_unvault():
    secret = "password"

# Generated at 2022-06-22 11:52:37.762446
# Unit test for function do_unvault
def test_do_unvault():

    vault_1 = "$ANSIBLE_VAULT;1.1;AES256;filter_default\n63306430666564633262376434353531666430373965353763666332623532353665643065363762\n32653837333538666431343238313739336439626663316231356131343836663239376439343664\n35336336623563396635336566346261666534336361333133313936333233656132306534306665\n66393530663338635d\n"


# Generated at 2022-06-22 11:52:51.082434
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data1 = 'test'
    data2 = 'test1'

# Generated at 2022-06-22 11:53:00.990430
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:10.738540
# Unit test for function do_unvault
def test_do_unvault():
    secret = "ansible"
    vault_strings = [
        "$ANSIBLE_VAULT;1.1;AES256;localhost;41614141414141414141414141414141414141",
        "ansibledata",
        "1234567890123456",
        u"\u2010\u2015\u2020",
        "",
        b"ansibledata",
        None,
        10,
        True,
        False,
        [],
        {},
    ]


# Generated at 2022-06-22 11:53:20.497281
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'secret'
    vaultid = 'filter_default'
    vault = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.2;AES256;test\n123456789')
    data = do_unvault(vault, secret, vaultid)
    assert data == '123456789'

    vault = '$ANSIBLE_VAULT;1.2;AES256;test\n123456789'
    data = do_unvault(vault, secret, vaultid)
    assert data == '123456789'

    data = '123456789'
    data = do_unvault(data, secret, vaultid)
    assert data == '123456789'

    secret = '123456789'

# Generated at 2022-06-22 11:53:32.662707
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:38.646412
# Unit test for function do_vault

# Generated at 2022-06-22 11:53:41.146163
# Unit test for function do_vault
def test_do_vault():
    pass

# Generated at 2022-06-22 11:53:45.643513
# Unit test for function do_unvault
def test_do_unvault():
    res = do_unvault("$ANSIBLE_VAULT;1.1;AES256","this is password")
    assert res == "this is password"

    try:
        res = do_unvault("$ANSIBLE_VAULT;1.1;AES256","this is password")
    except AnsibleFilterError:
        pass
    else:
        assert False and "Error not raised"

    res = do_unvault(None,"this is password")
    assert res is None

# Generated at 2022-06-22 11:53:57.803166
# Unit test for function do_vault
def test_do_vault():

    # Test string without salt - wrap_object should be true by default
    my_secret = 'my_super_secret'
    my_string = 'my_super_string'
    my_salt = 'my_super_salt'
    my_vaultid = 'my_super_id'

    assert do_vault(my_string, my_secret) == do_vault(my_string, my_secret, wrap_object=True)

# Generated at 2022-06-22 11:54:03.386162
# Unit test for function do_unvault
def test_do_unvault():
    data = "vault unvault test"
    secret = "hunter2"
    vaultid = "test_id"
    vault = do_vault(data, secret, vaultid=vaultid)
    unvault = do_unvault(vault, secret, vaultid=vaultid)
    assert data == unvault

# Generated at 2022-06-22 11:54:14.055855
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import get_vault_secret, VaultSecret
    from ansible.parsing.vault import is_encrypted, VaultLib
    from ansible.parsing.vault import VaultSecret
    import os

    vault_secrets = [os.path.join(os.path.dirname(__file__), 'files/vault.key')]

# Generated at 2022-06-22 11:54:25.930088
# Unit test for function do_vault
def test_do_vault():
    import os
    import tempfile
    import stat

    tfile = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-22 11:54:38.848633
# Unit test for function do_vault
def test_do_vault():
    filter_module = FilterModule()
    filters = filter_module.filters()

# Generated at 2022-06-22 11:54:42.713293
# Unit test for function do_vault
def test_do_vault():
    secret = 'hunter2'

    result = do_vault('this is a secret', secret)
    assert type(result) is str
    assert '$ANSIBLE_VAULT' in result

    result = do_vault('this is a secret', secret, wrap_object=True)
    assert type(result) is AnsibleVaultEncryptedUnicode


# Generated at 2022-06-22 11:54:53.899353
# Unit test for function do_vault
def test_do_vault():
    data = do_vault('qwerty', 'ansible')

# Generated at 2022-06-22 11:55:05.452787
# Unit test for function do_vault
def test_do_vault():
    secret = 'tatatas'
    salt = '1234'
    data = 'exemple'
    vaultid = 'filter_default'

    expected_output = "!vault |\n          $ANSIBLE_VAULT;1.2;AES256;filter_default;\n          37646563306436303162643565663037353732623739393033353362643861366330333862376365\n          35353664373133316536326262613931646363313230306538363833653263656133303166627266\n          613630343266613431373430356366383363633039303533\n"

    assert expected_output in do_vault(data, secret, salt, vaultid)

# Unit test

# Generated at 2022-06-22 11:55:11.737886
# Unit test for function do_vault
def test_do_vault():
    """ test_do_vault """
    result = do_vault('SuperSecretPassword', 'super secret password', 'salt', 'my_vaultid')
    # test result (encrypted password)
    assert result == to_native(VaultSecret('super secret password').encrypt(b'SuperSecretPassword'))



# Generated at 2022-06-22 11:55:22.967962
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import _vault_decrypt_text

# Generated at 2022-06-22 11:55:26.438464
# Unit test for function do_vault
def test_do_vault():

    data = 'This is my secret data'
    secret = 'mysecretpassword'

    vault = do_vault(data, secret, None, 'test_vault_id')

    print(vault)



# Generated at 2022-06-22 11:55:33.223479
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    salt = None
    vaultid = 'test'
    wrap_object = True
    data = 'password'
    display.verbosity = 3

# Generated at 2022-06-22 11:55:42.822746
# Unit test for function do_vault
def test_do_vault():
    secret = "test_vault"

    data_1 = "test_data"
    data_2 = ["test_data_1", "test_data_2"]
    data_3 = {"k1": "test_data_1", "k2": "test_data_2"}

    # result_1
    result_1 = do_vault(data_1, secret)
    print(result_1)

    # result_2
    result_2 = do_vault(data_2, secret)
    print(result_2)

    # result_3
    result_3 = do_vault(data_3, secret)
    print(result_3)

    # result_4
    result_4 = do_vault("{{ data }}", secret)
    print(result_4)



# Generated at 2022-06-22 11:55:53.592494
# Unit test for function do_vault
def test_do_vault():
    vault = do_vault('secret', 'password')
    print(vault)
    assert vault == '$ANSIBLE_VAULT;1.1;AES256;ansible_undefined169220304e6d8b6cfdbd0a33a9b917c4b2d4b1c14f4359f98a3a8daf76ba80e2dd2da29e1d5c1c5d78cb5c5f5cb5a3a8e181fe3e7c2a9a73fa7ad8d6edf5f5c5\n'
    #assert ansible.module_utils.basic.AnsibleVaultEncryptedUnicode == type(vault)



# Generated at 2022-06-22 11:55:54.969012
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'secret') == ''


# Generated at 2022-06-22 11:56:05.580108
# Unit test for function do_unvault

# Generated at 2022-06-22 11:56:14.013929
# Unit test for function do_vault
def test_do_vault():

    # testing do_vault
    data = "userinfo"
    secret = "pass"
    salt = "salt"
    vaultid = "filter_default"


# Generated at 2022-06-22 11:56:25.122745
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('secret', 'secret') == '$ANSIBLE_VAULT;1.2;AES256;test_data\n6338653062396635336236626234616264336632373735373963623366393837333762326637\n3134383733663734623832396361623233376334623238303361613232313833656134313765\n3530396363633761373336613032663331623761643662636233343231366131636661323332\n3337346231316537653765366331343465373831613333633639303366363162366262613032\n3266\n'


# Generated at 2022-06-22 11:56:33.601708
# Unit test for function do_vault
def test_do_vault():
    data = 'foo'
    secret = 'bar'
    salt = 'baz'
    vaultid = 'filter_default'

    result = do_vault(data, secret, salt, vaultid, wrap_object=False)
    assert isinstance(result, str)

    result = do_vault(data, secret, salt, vaultid, wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-22 11:56:43.537744
# Unit test for function do_vault
def test_do_vault():
    """Test for the do_vault filter"""
    vault_filter = FilterModule()
    result = vault_filter.filters()['vault']('teststr', 'secret', 'salt', 'vaultid', True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode) is True
    assert isinstance(result.vault, VaultLib) is True
    assert result.vault.secrets[0][0] == 'vaultid'
    assert result.vault.secrets[0][1].secret == b'secret'
    assert result.vault.secrets[0][1].salt == b'salt'
    # This assert is dependent on the vault key used in the test.

# Generated at 2022-06-22 11:56:50.797456
# Unit test for function do_vault
def test_do_vault():

    secret = 'ansible'
    salt = 'salt'
    data = 'mysql_password'
    vaultid = 'filter_default'
    wrap_object = False

# Generated at 2022-06-22 11:56:57.944754
# Unit test for function do_vault
def test_do_vault():
    # Test vault with a string
    test_secret = 'secret'
    test_value = 'test'
    assert test_value == do_unvault(do_vault(test_value, test_secret, vaultid='filter_default'), test_secret)
    # Test vault with a binary string
    test_secret = b'secret'
    test_value = b'test'
    assert test_value == do_unvault(do_vault(test_value, test_secret, vaultid='filter_default'), test_secret)
    # Test vault with a unicode string
    test_secret = u'secret'
    test_value = u'test'

    assert test_value == do_unvault(do_vault(test_value, test_secret, vaultid='filter_default'), test_secret)
   

# Generated at 2022-06-22 11:57:06.528749
# Unit test for function do_unvault
def test_do_unvault():
    from jinja2 import Environment
    from jinja2 import Template

    vl = VaultLib()
    vs = VaultSecret('secret')
    vl.secrets = {
        'filter_default': vs
    }

    env = Environment(extensions=['ansible.plugins.jinja2_filters.do_unvault'], undefined=Undefined)
    env.filters['unvault'] = do_unvault

    template = Template('''{{ "foobar" | unvault(secret="secret") }}''')
    assert template.render(vl=vl) == 'foobar'

# Generated at 2022-06-22 11:57:17.826991
# Unit test for function do_vault
def test_do_vault():

    secret = 'secret'
    data = 'data'
    salt = 'salt'
    vaultid = 'id1'

    vault = do_vault(data=data, secret=secret, salt=salt, vaultid=vaultid)

    assert isinstance(vault, string_types)
    assert vault.startswith('$ANSIBLE_VAULT')
    assert vault.endswith(to_bytes(data))

    vault = do_vault(data=data, secret=secret, salt=salt)

    assert isinstance(vault, string_types)
    assert vault.startswith('$ANSIBLE_VAULT')
    assert vault.endswith(to_bytes(data))

    vault = do_vault(data=data, secret=secret)

    assert isinstance(vault, string_types)

# Generated at 2022-06-22 11:57:26.842649
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('ansible', 'ansible', wrap_object=True) == \
           '$ANSIBLE_VAULT;1.1;AES256;ansible6407231799001402564\n' \
           '3666383664666432386465343132613337386433353264643037343062386266393262326664\n' \
           '353239616564393465353737336566623338613639623262303239333063666163310a\n'



# Generated at 2022-06-22 11:57:39.158444
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:49.238370
# Unit test for function do_vault
def test_do_vault():
    import json
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from jinja2.exceptions import UndefinedError

    f = FilterModule()
    result = to_native(f.filters()['vault']('plaintext', 'secret'))
    enc_data = json.loads(result)

    # Json has four keys
    assert isinstance(enc_data, dict)
    assert len(enc_data.keys()) == 4

    # Check whether secret is encrypted
    assert enc_data['data'] != 'plaintext'

    # Check whether secret is decrypted back to plaintext
    assert f.filters()['unvault'](enc_data, 'secret') == 'plaintext'

    # Test non-string secret

# Generated at 2022-06-22 11:57:58.923290
# Unit test for function do_vault
def test_do_vault():
    secret = 'mysecret'
    salt = 'salt'
    vaultid = 'vaultid'
    data1 = 'this is a test of data to be encrypted'
    data2 = 'this is another test of data to be encrypted'
    vaulted_data1 = do_vault(data1, secret, salt, vaultid)
    vaulted_data2 = do_vault(data2, secret, salt, vaultid)
    assert vaulted_data1 != vaulted_data2
    assert vaulted_data1 != data1
    assert vaulted_data2 != data2


# Generated at 2022-06-22 11:58:07.329973
# Unit test for function do_vault
def test_do_vault():
    secret = "Secret"
    data = "Data"
    vaulted = do_vault(data, secret)
    assert isinstance(vaulted, str)
    assert vaulted != data
    assert len(vaulted) > len(data)


# Generated at 2022-06-22 11:58:19.153986
# Unit test for function do_vault
def test_do_vault():
    # Basic data
    data = 'test'
    # Default secret
    secret = 'ansible_vault_filter'
    # Default salt
    salt = 'random_salt'
    # Default vaultid
    vaultid = 'filter_default'
    # Default wrap_object
    wrap_object = False
    # Expected data

# Generated at 2022-06-22 11:58:30.739896
# Unit test for function do_vault
def test_do_vault():
    from ansible.parsing.vault import VaultSecret, VaultLib
    vl = VaultLib()
    vs = VaultSecret('foo')

    assert do_vault('bar', 'foo') == to_native(vl.encrypt('bar', vs))
    assert do_vault('bar', 'foo', wrap_object=True) == AnsibleVaultEncryptedUnicode(to_native(vl.encrypt('bar', vs)))
    assert do_vault('bar', 'foo', vaultid='test') == to_native(vl.encrypt('bar', vs, vaultid='test'))
    assert isinstance(do_vault('bar', 'foo'), string_types)


# Generated at 2022-06-22 11:58:39.380933
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:48.749851
# Unit test for function do_vault

# Generated at 2022-06-22 11:58:58.669907
# Unit test for function do_unvault
def test_do_unvault():
    """
    Testing do_unvault function included in this script
    """
    import pytest
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from jinja2.utils import generate_lorem_ipsum

    s_secret = generate_lorem_ipsum(1)
    s_secret_data = generate_lorem_ipsum(5)
    i_data_len = len(to_bytes(s_secret_data))

    secret = VaultSecret(s_secret.encode('utf-8'))
    vault = VaultLib([('default', secret)])

# Generated at 2022-06-22 11:59:09.360563
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:11.327142
# Unit test for function do_vault
def test_do_vault():
    secret = "foobar"
    data = "Hello World"
    res = do_vault(data, secret)
    assert isinstance(res, string_types) is True


# Generated at 2022-06-22 11:59:22.852108
# Unit test for function do_vault
def test_do_vault():
    display.quiet()
    data = 'foo'
    secret = 'SECRET'


# Generated at 2022-06-22 11:59:30.727865
# Unit test for function do_vault
def test_do_vault():
    '''
    Test cases for the do_vault filter
    '''

    test_obj = FilterModule()
    filter_func = test_obj.filters()['vault']

    # Test success case
    test_data = "this is vault text"
    test_secret = "ansible"
    test_salt = "salttext"
    test_vaultid = "test_vaultid"

# Generated at 2022-06-22 11:59:44.978263
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    data = 'text'

# Generated at 2022-06-22 11:59:55.057176
# Unit test for function do_vault
def test_do_vault():
    import pytest

    # Test basic encryption
    data = 'This is a secret'
    secret = 'Vault secret'
    vaultid = 'testid'
    salt = 'salt'
    vault = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=False)
    assert vault.startswith('$ANSIBLE_VAULT;1.1;')

    # Test encryption of list containing string
    data = ['Secret 1', 'Secret 2']
    vault = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=False)
    assert vault.startswith('$ANSIBLE_VAULT;1.1;')

    # Test encryption of list containing list
    data = [['Secret 1', 'Secret 2']]
    vault = do

# Generated at 2022-06-22 12:00:02.768527
# Unit test for function do_vault
def test_do_vault():

    # Test with valid secret and data
    data = "this is secret data"
    secret = "this is my secret"
    vault = do_vault(data, secret)

    # Validate vault variable is not empty and it is an encrypted variable
    assert vault
    assert is_encrypted(vault)

    # Test with invalid data type secret
    secret = 1
    try:
        vault = do_vault(data, secret)
        assert False
    except AnsibleFilterTypeError:
        assert True

    # Test with invalid data type data
    secret = "this is my secret"
    data = {"secret_data": "value"}
    try:
        vault = do_vault(data, secret)
        assert False
    except AnsibleFilterTypeError:
        assert True



# Generated at 2022-06-22 12:00:09.461381
# Unit test for function do_vault
def test_do_vault():
    # if secret is not string
    try:
        do_vault('data', 123)
    except AnsibleFilterTypeError:
        pass
    else:
        assert False
    # if data is not string
    try:
        do_vault(123, 'secret')
    except AnsibleFilterTypeError:
        pass
    else:
        assert False
    # if data is not valid
    try:
        do_vault('data', 'secret')
    except UndefinedError:
        pass
    else:
        assert False
    # if data is empty
    try:
        do_vault('', 'secret')
    except UndefinedError:
        pass
    else:
        assert False
    # if data is invalid

# Generated at 2022-06-22 12:00:21.006880
# Unit test for function do_vault
def test_do_vault():
    secret = 'test'
    salt = 'test'

# Generated at 2022-06-22 12:00:24.185547
# Unit test for function do_vault
def test_do_vault():
    # Test basics
    do_vault('foo', 'bar', wrap_object=True)



# Generated at 2022-06-22 12:00:36.099465
# Unit test for function do_vault
def test_do_vault():

    # Good strings
    secret = "Ansible"
    data = "This is a test string"
    salt = None

    # Bad arguments
    bad_vaultids = [None, 1234]
    bad_secrets = [None, 1234]
    bad_data = [None, 1234]
    bad_salts = [1234]

    # Get vault object
    vault = do_vault(data, secret, salt)

    # Check object type
    assert isinstance(vault, AnsibleVaultEncryptedUnicode)

    # Check vault object
    assert vault.vault.is_encrypted(vault)
    assert vault.data == data

    # Test wrapping
    assert do_vault(data, secret, salt, wrap_object=True) == vault