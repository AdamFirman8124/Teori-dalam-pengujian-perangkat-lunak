

# Generated at 2022-06-22 11:50:42.857103
# Unit test for function do_unvault
def test_do_unvault():

    try:
        do_unvault(None, None)
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("An exception should have been raised")

    try:
        do_unvault('dummy_vault', None)
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("An exception should have been raised")

    try:
        do_unvault(None, 'dummy_secret')
    except AnsibleFilterTypeError:
        pass
    else:
        raise AssertionError("An exception should have been raised")

    try:
        do_unvault('dummy_vault', 'dummy_secret')
    except UndefinedError:
        pass

# Generated at 2022-06-22 11:50:51.392313
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.2;AES256;ansible_default\n3463336330653934666533303338353835633461393362323762626238396166366564356333663b0a373662623161343963323162303861333930323636363066643533666434366638\n396466626235613337336435626465633930653633633262613965393464356264643330383964653534643034656433393461396162373262393530313938313433666538666363656430\n", "my_secret") == "this is a string to encrypt"

# Generated at 2022-06-22 11:51:03.517822
# Unit test for function do_vault
def test_do_vault():
     secret_key = "THIS IS A SECRET KEY"
     data_string = "THIS IS A DATA STRING TO BE ENCRYPTED"

# Generated at 2022-06-22 11:51:15.618126
# Unit test for function do_vault

# Generated at 2022-06-22 11:51:17.734671
# Unit test for function do_unvault
def test_do_unvault():
    tdata = 'foo'
    tsecret = 'bar'
    tvaultid = 'default'
    tvault = do_vault(tdata, tsecret, vaultid=tvaultid)
    tunvault = do_unvault(tvault, tsecret, vaultid=tvaultid)
    assert tunvault == tdata

# Generated at 2022-06-22 11:51:30.622719
# Unit test for function do_unvault
def test_do_unvault():
    print("testing do_unvault")
    secret = "thisismysecret"
    vaultid = "filter_default"
    value = "password"
    ansible_filter_error = False

    try:
        vaulted_value = do_vault(value, secret, vaultid=vaultid, wrap_object=False)
    except AnsibleFilterError as e:
        ansible_filter_error = True
        print("AnsibleFilterError: %s" % e)
        assert False, "Encrypting error during unvault"

    if ansible_filter_error is False:
        try:
            unvaulted_value = do_unvault(vaulted_value, secret, vaultid=vaultid)
        except AnsibleFilterError as e:
            ansible_filter_error = True
           

# Generated at 2022-06-22 11:51:40.449380
# Unit test for function do_unvault
def test_do_unvault():
    # if you change these values you'll have to change tests
    secret = 'hello'
    salt = b'$ANSIBLE_VAULT;1.1;AES256'

# Generated at 2022-06-22 11:51:48.469787
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('my_secret', 'my_secret') == '$ANSIBLE_VAULT;1.2;AES256;ansible;2405834771414A3044343944394238443544384539454145424434335135343039443544444443433144383538324836413331364242413643375D3C3D3D56'



# Generated at 2022-06-22 11:51:56.791475
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('foobar', '$ANSIBLE_VAULT', salt="my_salt") == '$ANSIBLE_VAULT;1.1;AES256;my_salt\n3138313535366637336162353137323238306362356630373962636331666335396431306337316665\n3861656231316133633662333434323363343033653537666364373230313166323133396339643465\n363465623664366633326662333563333663373333431383239366132626339386465326332386265\n'


# Generated at 2022-06-22 11:52:04.759635
# Unit test for function do_unvault

# Generated at 2022-06-22 11:52:16.940857
# Unit test for function do_unvault
def test_do_unvault():
    data = "ansible-vault encrypt_string"
    secret = "secret"
    vaultid = "filter_default"
    vaultstr = do_vault(data, secret, vaultid=vaultid)

# Generated at 2022-06-22 11:52:26.539102
# Unit test for function do_unvault
def test_do_unvault():
    filter_module = FilterModule()
    result = filter_module.filters()['unvault']("$ANSIBLE_VAULT;1.1;AES256;administrator@vault-01\n343730373866353939353332303136373738633161623737363637663039636337616232303135\n353765326139623236353638653465393366396361346665623564393530646531353632383435\ndeb0718fd5d5db5c5ce8f98f38b42cc20b1d06c928e26b9aab4c4eeb4a4cf4a4\n", "testsecret")
    assert result == "foo"

# Generated at 2022-06-22 11:52:35.285053
# Unit test for function do_vault
def test_do_vault():
    token = ''
    secret = '$ansible'
    salt = ''
    data = 'foo'
    vault = do_vault(data, secret, salt)
    assert vault == "$ANSIBLE$v1$b2hhMg==$NqNhV9dJzZA+7Zf1Q2Cw/w==", "vault_string should have been %s, was %s" % ('$ANSIBLE$v1$b2hhMg==$NqNhV9dJzZA+7Zf1Q2Cw/w==', vault)
    #check the vault string can be decrypted
    assert do_unvault(vault, secret) == data, "decrypted_string should have been %s, was %s" % (data, do_unvault(vault, secret))

# Generated at 2022-06-22 11:52:48.169490
# Unit test for function do_vault
def test_do_vault():
    data = 'mysecret'
    secret = 'mysecret'
    output_non_wrap = '$ANSIBLE_VAULT;1.1;AES256;vault1\n333766623265363633386535393730313238346635386530373538326339636536396534383535616\n635303565393833383530653365346234366236626132343337343035393933\n'

# Generated at 2022-06-22 11:52:53.932029
# Unit test for function do_vault
def test_do_vault():
    secret = "password"
    salt = None
    vaultid = 'test'
    wrap_object = False
    data = "This is the test data."
    vault_data = do_vault(data, secret, salt, vaultid, wrap_object)
    assert len(vault_data) > len(data)


# Generated at 2022-06-22 11:53:03.442325
# Unit test for function do_unvault
def test_do_unvault():
    vault = """U2FsdGVkX1+p7Gxc5ZfvzZRaz67DutKGpBJ3q1plXyW9xj5Q5MK5hZbYQZ8WgAxi1tSRLiSMCzOAeX8Wt4kCHf4i4RRbby2M/c77WJH/LK/SZNzytF8XC+D4HJ4h4DH"""
    secret = "secret_password"
    vaultid = "vault_filter_default"
    data = "my_secret_data"
    assert do_unvault(vault, secret, vaultid) == data

    vault = AnsibleVaultEncryptedUnicode(vault)

# Generated at 2022-06-22 11:53:14.942716
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultSecret, VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import textwrap
    import pytest

    # Define secret and data
    secret = b'MySecret'
    data = b'MyData'
    salt = b''
    vaultid = b'filter_default'

    # Call do_vault
    vault = do_vault(data, to_native(secret), salt, vaultid)

    # Check do_vault return
    # Check vault is encrypted
    assert is_encrypted(vault)
    assert vault.startswith(b'$ANSIBLE_VAULT;')
    # Check vault is AnsibleVaultEncryptedUnicode

# Generated at 2022-06-22 11:53:21.477923
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import sys
    sys.path.append(os.path.dirname(__file__))
    import test_do_unvault
    if test_do_unvault.passed:
        display.display("PASSED - 'do_unvault' filter tests")
    else:
        display.error("FAILED - 'do_unvault' filter tests")

# Generated at 2022-06-22 11:53:32.000122
# Unit test for function do_vault
def test_do_vault():
    #Test_positive
    result = do_vault("test_data","test_secret")

# Generated at 2022-06-22 11:53:41.836403
# Unit test for function do_unvault

# Generated at 2022-06-22 11:53:56.049872
# Unit test for function do_vault
def test_do_vault():
    # define the secret key
    secret = 'secret'

    # define the salt
    salt = 'salt'

    # define the string to be vaulted
    data = 'secret string'

    # define the vault_id
    vaultid = 'test_default'

    # define the wrap_object flag
    wrap_object = False

    # get the vaulted string
    vault = do_vault(data, secret, salt, vaultid, wrap_object)

    # define the expected vaulted string

# Generated at 2022-06-22 11:54:02.627552
# Unit test for function do_unvault
def test_do_unvault():
    data = "abc123"
    secret = "mysecret"
    vaultid = "filter_default"
    vault = do_vault(data, secret)
    display.display(vault)
    assert is_encrypted(vault)
    data_again = do_unvault(vault, secret)
    display.display(data_again)
    assert data_again == data



# Generated at 2022-06-22 11:54:13.352413
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'YOUR_SECRET'
    vaultid = None
    pass_string = 'test_do_unvault_pass'
    fail_string = 'test_do_unvault_fail'
    pass_vault = do_vault(pass_string, secret)
    fail_vault = do_vault(fail_string, to_native('Not your secret'))

    # Test with a valid secret
    assert do_unvault(pass_vault, secret, vaultid) == pass_string

    # Test with no secret
    try:
        do_unvault(pass_vault, None, vaultid)
    except Exception as e:
        assert str(e) == 'Secret passed is required to be as string, instead we got: NoneType'

    # Test with an invalid secret

# Generated at 2022-06-22 11:54:25.135960
# Unit test for function do_unvault
def test_do_unvault():
    secret = 'youllnevergetme'
    vaultid = 'filter_test'

    # Data type test
    data_test = ['abc','123','youllnevergetme','Really not!','','#','$','%','^','&','*','(',')','=','+','{','}','[',']','.',',','<','>','?','/','\\','|','"',"'",':',';','`','~']
    for data in data_test:
        assert do_vault(data, secret, vaultid=vaultid).startswith(b"$ANSIBLE_VAULT")
        assert do_unvault(do_vault(data, secret, vaultid=vaultid), secret, vaultid=vaultid) == data

    # Single line data type test

# Generated at 2022-06-22 11:54:37.486949
# Unit test for function do_unvault

# Generated at 2022-06-22 11:54:38.968853
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('test', 'secret')

    assert result


# Generated at 2022-06-22 11:54:45.306847
# Unit test for function do_unvault
def test_do_unvault():
    test_secret = "blah"

    # Case: Vault Secret object

# Generated at 2022-06-22 11:54:56.394649
# Unit test for function do_vault
def test_do_vault():
    data = "my secret string"
    secret = "my secret key"
    salt = ""
    vaultid = ""
    wrap_object = False
    vault = do_vault(data, secret, salt, vaultid, wrap_object)

# Generated at 2022-06-22 11:55:06.574379
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import tempfile
    from ansible.parsing.vault import VaultSecret, VaultLib

    secret = 'myVaultPassword'
    plain_text = 'myPlainText'
    temp_dir = tempfile.mkdtemp()
    salt_path = os.path.join(temp_dir, 'salt')

    with open(salt_path, 'wb') as f:
        f.write(os.urandom(16))

    vs = VaultSecret(secret)
    vl = VaultLib()
    encrypted = vl.encrypt(plain_text, vs, salt_path)

    decrypted = do_unvault(encrypted, secret, salt_path)

    assert plain_text == decrypted



# Generated at 2022-06-22 11:55:17.825045
# Unit test for function do_vault

# Generated at 2022-06-22 11:55:22.203160
# Unit test for function do_vault
def test_do_vault():
    data = 'hello'
    secret = 'password'
    result = do_vault(data, secret)

    # Check if the encrpyted data is AnsibleVaultEncryptedUnicode type
    assert isinstance(result, string_types)

    # Check if the encrypted data starts with $ANSIBLE_VAULT;
    assert result.startswith('$ANSIBLE_VAULT')



# Generated at 2022-06-22 11:55:31.108427
# Unit test for function do_vault
def test_do_vault():
    import jinja2
    from jinja2 import Environment
    env = Environment()
    env.filters['vault'] = do_vault
    env.filters['unvault'] = do_unvault
    template = env.from_string('{{ sens_data | vault(secret, salt="abcd", vaultid="vault123", wrap_object=True) | unvault(secret, vaultid="vault123") }}')
    data = template.render(sens_data='abc', secret='ansible_vault')
    assert data == 'abc'


# Generated at 2022-06-22 11:55:41.189208
# Unit test for function do_vault
def test_do_vault():
    assert do_vault(None, 'secret') == ''
    assert do_vault('', 'secret') == ''

# Generated at 2022-06-22 11:55:47.315322
# Unit test for function do_vault
def test_do_vault():

    secret = "secret"
    data = "test data"
    salt = "test salt"
    vaultid = "filter_default"
    wrap_object = False

    vaulted = do_vault(data, secret, salt, vaultid, wrap_object)
    result = do_unvault(vaulted, secret, vaultid)
    assert result == data



# Generated at 2022-06-22 11:55:59.119243
# Unit test for function do_unvault
def test_do_unvault():
    import pytest

# Generated at 2022-06-22 11:56:01.540367
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    data = 'data'
    vault = do_vault(data, secret)
    assert isinstance(vault, str)


# Generated at 2022-06-22 11:56:10.462985
# Unit test for function do_vault

# Generated at 2022-06-22 11:56:22.419453
# Unit test for function do_vault
def test_do_vault():
    data = 'testdata'
    secret = 'test'
    salt = 'salt'

    assert do_vault(data, secret, salt) == VaultLib.encrypt(data, secret, salt)

    data = 'testdata'
    secret = 'test'
    salt = None

    assert do_vault(data, secret, salt) == VaultLib.encrypt(data, secret)

    data = 'testdata'
    secret = None
    salt = 'salt'

    try:
        do_vault(data, secret, salt)
    except AnsibleFilterTypeError:
        pass
    else:
        # Should have caught exception
        assert False

    data = None
    secret = 'test'
    salt = 'salt'


# Generated at 2022-06-22 11:56:34.453790
# Unit test for function do_unvault

# Generated at 2022-06-22 11:56:44.276061
# Unit test for function do_vault
def test_do_vault():
    # Test for expected success
    cases = (
        # Test for input which is not a string
        (['data'], 'secret', 'salt', ValueError),
        # Test for input which is not a string
        (None, ['secret'], 'salt', ValueError),
        # Test for input which is not a string
        ({'key': 'value'}, 'secret', 'salt', ValueError),
        # Test for input which is not a string
        (1, 'secret', 'salt', ValueError),
        # Test for input which is not a string
        (1.1, 'secret', 'salt', ValueError),
    )


# Generated at 2022-06-22 11:56:57.601100
# Unit test for function do_unvault
def test_do_unvault():
    from ansible.parsing.vault import VaultEditor
    from ansible.plugins.filter.vault import do_unvault

    # valid un-vault output
    vault_editor = VaultEditor(password_file='tests/test_vault_editor/vault_password')
    vault_editor._load_vault_password()
    password = vault_editor.get_vault_password()

    result = do_unvault(vault='$ANSIBLE_VAULT;1.1;AES256', secret=password)
    assert result == ''

    result = do_unvault(vault=AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256'), secret=password)
    assert result == ''

    # result = do_unvault(vault='$ANS

# Generated at 2022-06-22 11:57:06.240254
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("s3cr3t", "mysecret") == "+\nCVzt8qAa1yb+NycnJx8nJycnJycnJycnJycnJycnKW8Iskg0LIow=="
    assert do_vault("s3cr3t", "mysecret", wrap_object=True) == AnsibleVaultEncryptedUnicode("+\nCVzt8qAa1yb+NycnJx8nJycnJycnJycnJycnJycnKW8Iskg0LIow==")


# Generated at 2022-06-22 11:57:17.780463
# Unit test for function do_unvault

# Generated at 2022-06-22 11:57:21.526128
# Unit test for function do_unvault
def test_do_unvault():
    value = "ansible"
    secret = "password"
    vaulted = do_vault(value, secret)
    assert do_unvault(vaulted, secret) == value

# Generated at 2022-06-22 11:57:26.944733
# Unit test for function do_vault
def test_do_vault():
    from ansible_collections.ansible.community.plugins.filter.vault import FilterModule
    filters = FilterModule().filters()
    test_text = 'test_text'
    result_text = filters.get('vault')(test_text, 'top_secret')
    assert isinstance(result_text, str) and len(result_text) > 0


# Generated at 2022-06-22 11:57:39.311857
# Unit test for function do_vault
def test_do_vault():
    from ansible.module_utils import basic
    from ansible.module_utils.six import PY2
    from ansible.plugins.filter import vault

    f = vault.FilterModule().filters()


# Generated at 2022-06-22 11:57:49.382741
# Unit test for function do_unvault
def test_do_unvault():
    import os
    import yaml
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
    from ansible.module_utils.yaml.parser import AnsibleParserError
    def yaml_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=MutableMapping):
        class AnsibleVaultSafeLoader(Loader):
            pass
        AnsibleVaultSafeLoader.add_constructor(
            u'tag:yaml.org,2002:map',
            type(Loader.construct_yaml_map)(Loader.construct_yaml_map.__func__),
        )

# Generated at 2022-06-22 11:58:01.519666
# Unit test for function do_unvault
def test_do_unvault():
    clear_data = 'password'
    secret = 'secret'
    vaultid = 'unit_test'
    vault = do_vault(clear_data, secret, vaultid=vaultid)


# Generated at 2022-06-22 11:58:04.308152
# Unit test for function do_vault
def test_do_vault():
    do_vault('password', 'vault-password', salt='salt', vaultid='someid')
    do_vault(u'password', 'vault-password', salt='salt', vaultid='someid')


# Generated at 2022-06-22 11:58:16.348364
# Unit test for function do_unvault

# Generated at 2022-06-22 11:58:27.277370
# Unit test for function do_unvault
def test_do_unvault():
    assert do_unvault("$ANSIBLE_VAULT;1.1;AES256;en_US;0H/cxrrqgfqmYQ2DDiKjZw==;1f7fe928360d9d7b71b2c0ce7ec4c4d31d7f4c4dd512fb7e8b444a2feca7e080c1b9e7c4a4b4f","password")=="password123"

# Generated at 2022-06-22 11:58:33.505253
# Unit test for function do_vault
def test_do_vault():
    assert do_vault('test', 'ansible', 'salt') == '$ANSIBLE_VAULT;1.1;AES256\n3562336338613134373061356132323537386435333563623862643461646366636337306233326130\n65366335656330633161346138353332616232313930383634366661\n'



# Generated at 2022-06-22 11:58:36.729543
# Unit test for function do_vault
def test_do_vault():
    result = do_vault('secret_string', 'secret_key')

    assert result is not None
    assert result.startswith('$ANSIBLE_VAULT;')


# Generated at 2022-06-22 11:58:48.672496
# Unit test for function do_unvault
def test_do_unvault():
    import random
    for _ in range(100):
        key = ''.join(random.sample(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'], 16))

# Generated at 2022-06-22 11:58:56.860889
# Unit test for function do_vault
def test_do_vault():
    data = "password123"
    secret = "password"
    vaultid = "filter_default"
    salt = "salt123"
    wrap_object = False
    salt_type = type(salt)
    secret_type = type(secret)
    expected_type = type(do_vault(data, secret, salt, vaultid, wrap_object))
    assert data != do_vault(data, secret, salt, vaultid, wrap_object)
    assert salt_type == secret_type
    assert isinstance(secret, string_types)
    assert isinstance(data, string_types)
    assert expected_type == type(data)


# Generated at 2022-06-22 11:59:01.410949
# Unit test for function do_vault
def test_do_vault():
    secret = 'secret'
    salt = 'salt'
    vaultid = 'test_vault'
    data = 'password'
    vault = do_vault(data, secret, salt, vaultid)
    assert do_unvault(vault, secret, vaultid) == data

# Generated at 2022-06-22 11:59:12.963543
# Unit test for function do_vault
def test_do_vault():
    # Set up class filter
    filter = FilterModule()
    # Call filter ansible vault filter
    ansible_vault_filter = filter.filters()['vault']
    # Test filter

# Generated at 2022-06-22 11:59:23.834007
# Unit test for function do_vault
def test_do_vault():

    test_data = ['test', 'test_unvault', 'test_unvault1', 'test_unvault2', 'test_unvault3', 'test_unvault4', 'test_unvault5', 'test_unvault6', 'test_unvault7', 'test_unvault8']
    secret = '9088r63j829r093q'

    for i in test_data:
        assert (do_vault(i, secret)[0:12] == '$ANSIBLE_VAULT') and (do_vault(i, secret)[13:15] == ';1') and (do_vault(i, secret)[-49:-31] == salt), "do_vault() has failed, please verify the function"


# Generated at 2022-06-22 11:59:31.339965
# Unit test for function do_vault

# Generated at 2022-06-22 11:59:41.685410
# Unit test for function do_unvault

# Generated at 2022-06-22 11:59:51.837311
# Unit test for function do_vault
def test_do_vault():
    from jinja2 import Environment
    env = Environment()
    env.filters['vault'] = do_vault
    template = env.from_string("{{ 'Hello my name is {{ cookiecutter.first_name }}' | vault('the-password') }}")
    res = template.render(cookiecutter={'first_name': 'Sylvain', 'last_name': 'Girard'})
    assert '$ANSIBLE_VAULT;9.9;AES256' in res


# Generated at 2022-06-22 12:00:01.075329
# Unit test for function do_vault
def test_do_vault():

    secret = 'secret'
    data = 'data'
    salt = 'salt'

    dv = do_vault(data, secret, salt)

# Generated at 2022-06-22 12:00:13.029878
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:23.440952
# Unit test for function do_vault

# Generated at 2022-06-22 12:00:24.134784
# Unit test for function do_unvault
def test_do_unvault():
    pass

# Generated at 2022-06-22 12:00:35.158729
# Unit test for function do_vault
def test_do_vault():
    assert do_vault("a s3cr3t", "my secret", wrap_object=True) == AnsibleVaultEncryptedUnicode(u'$ANSIBLE_VAULT;1.1;AES256\n6337366637353766393436326463613162333239656362616262666537333933613334356130\n34663035343265383038363962313431646463356262620a6136333464656539353066346533\n3430393564336161373164313932636237643632633366336234626466303533663233656438\n6365663037666366353632\n')
