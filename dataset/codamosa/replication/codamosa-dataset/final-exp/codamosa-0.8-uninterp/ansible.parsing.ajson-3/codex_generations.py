

# Generated at 2022-06-13 06:41:34.293670
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    '''
    The object hook is called with the result of every JSON object decoded and its return value is used in place of the given dict.
    this is to support AnsibleVaultEncryptedUnicode to be the decoded value
    for the input of __ansible_vault
    '''

    json_str = '{"__ansible_vault": "mypass"}'
    _vaults_dict = {'default': '', 'secrets': ['mypass']}
    _vaults = VaultLib(secrets=['mypass'])
    _decoder = json.JSONDecoder()

    # First, test that the 'default' key exists in AnsibleJSONDecoder._vaults dict
    assert 'default' in AnsibleJSONDecoder._vaults

    # Second, test that _vaults['default'] is assigned _vaults
   

# Generated at 2022-06-13 06:41:39.449375
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['password123']
    AnsibleJSONDecoder.set_secrets(secrets)

    string = '{"__ansible_vault": "vault"}'
    json_obj = json.loads(string, cls=AnsibleJSONDecoder)

    assert isinstance(json_obj, AnsibleVaultEncryptedUnicode)
    assert json_obj.vault.is_encrypted('vault')


# Generated at 2022-06-13 06:41:48.883386
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest
    # check ansible_vault
    v = {'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;default\n393764353033363266383466313165396633373033383633326736353038623530333530343930\n32336534623466653339663834396239633863646530366636386535646534396465613731366535\n633032646461\n'}
    AnsibleJSONDecoder.set_secrets('test')
    assert isinstance(json.loads(json.dumps(v, cls=AnsibleJSONEncoder), cls=AnsibleJSONDecoder), dict)

    # check ansible_unsafe

# Generated at 2022-06-13 06:41:56.657801
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Parameter key is equal to string '__ansible_vault'
    decoded = AnsibleJSONDecoder.object_hook({'__ansible_vault': 'foo'})
    assert(decoded.__class__.__name__ == 'AnsibleVaultEncryptedUnicode')

    # Parameter key is equal to string '__ansible_unsafe'
    decoded = AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'foo'})
    assert(decoded.__class__.__name__ == 'AnsibleUnsafeText')



# Generated at 2022-06-13 06:42:04.939600
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_secrets = VaultSecret([{'id': '12345', 'password': 'secret'}])
    parsed_data = None


# Generated at 2022-06-13 06:42:13.285843
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder_obj = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    assert decoder_obj.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')
    assert decoder_obj.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')
    assert decoder_obj.object_hook({'normal': 'foo'}) == {'normal': 'foo'}

# Generated at 2022-06-13 06:42:20.383379
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:25.494480
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # Test for detecting __ansible_vault
    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;ansible'}) == \
           AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.2;AES256;ansible')
    # Test for detecting __ansible_unsafe
    assert decoder.object_hook({'__ansible_unsafe': '$ANSIBLE_UNSAFE'}) == \
           wrap_var('$ANSIBLE_UNSAFE')
    # Test for not detecting

# Generated at 2022-06-13 06:42:35.737750
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test case 1:
    import json
    json_input = json.loads("""
{
    "a": {
        "__ansible_vault": "P3JzdGVtKDIuNS4wKSxlbmYK"
    },
    "b": "test"
}
""")
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(json_input)
    assert result['a'].value == "a"
    assert result['b'] == 'test'
    assert result['a'].vault == decoder._vaults['default']
    decoder.set_secrets("test")
    assert result['a'].vault == decoder._vaults['default']

    # Test case 2:

# Generated at 2022-06-13 06:42:48.019272
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Unit test for method object_hook of class AnsibleJSONDecoder when key is '__ansible_vault'
    secret = b'$ANSIBLE_VAULT;1.1;AES256'
    secrets = [b'0'] * 32

    AnsibleJSONDecoder.set_secrets(secrets)
    json_object = json.loads(
        '{"__ansible_vault": "AQAAAABzZWVkYmVlZGJlZWRiZWVkYmVlZA==", "__ansible_vault_password": "0"}',
        cls=AnsibleJSONDecoder,
        object_pairs_hook=dict
    )
    assert AnsibleVaultEncryptedUnicode(secret) == json_object['__ansible_vault']

# Generated at 2022-06-13 06:42:54.198073
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'test'}) == AnsibleVaultEncryptedUnicode('test')
    assert decoder.object_hook({'__ansible_unsafe': 'test'}) == wrap_var('test')
    assert decoder.object_hook({'test': 'test'}) == {'test': 'test'}



# Generated at 2022-06-13 06:43:03.616193
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Test that AnsibleVaultEncryptedUnicode is properly detected
    and replaced with an AnsibleVaultEncryptedUnicode object.
    """
    my_decoder = AnsibleJSONDecoder()
    pairs1 = {
        "name": "John",
        "__ansible_vault": "vault:$ANSIBLE_VAULT;1.1;AES256",
        "__ansible_unsafe": "hello"
    }
    pairs2 = {
        "name": "John",
        "__ansible_vault": "vault:$ANSIBLE_VAULT;1.1;AES256",
        "__ansible_unsafe": "hello"
    }
    ansible_vault_value = 'vault:$ANSIBLE_VAULT;1.1;AES256'


# Generated at 2022-06-13 06:43:09.496475
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    obj1 = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}
    assert isinstance(AnsibleJSONDecoder().object_hook(obj1), AnsibleVaultEncryptedUnicode)

    obj2 = {'__ansible_unsafe': '__ansible_unsafe__'}
    assert isinstance(AnsibleJSONDecoder().object_hook(obj2), AnsibleBaseYAMLObject)

    obj3 = {'key': 'value'}
    assert AnsibleJSONDecoder().object_hook(obj3) == obj3

# Generated at 2022-06-13 06:43:22.294851
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Testing case 1:
    #   An unencrypted vault secret should be converted to an
    #   AnsibleVaultEncryptedUnicode object with a vault property
    #   containing the vault secret.
    value = 'Hello, World!'
    value_wrapper = json.dumps({'__ansible_vault': value})
    vaults = AnsibleJSONDecoder.set_secrets([value])
    assert vaults
    assert AnsibleJSONDecoder._vaults['default'].secrets
    decoded_value = AnsibleJSONDecoder.object_hook(json.loads(value_wrapper))
    assert isinstance(decoded_value, AnsibleVaultEncryptedUnicode)
    assert decoded_value.vault

    # Testing case 2:
    #   A variable marked as unsafe should be wrapped in an unsafe wrapper.
   

# Generated at 2022-06-13 06:43:29.997397
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest

    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 06:43:38.177658
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    import os
    import sys
    import tempfile
    import unittest

    # Test data
    b_text = b'{"test_secrets": "test_value", "__ansible_vault": "vault_value"}'
    b_vault = b'vault_value'
    b_secrets = b'test_secret'

    # Save test data in temporary file
    fd, f_name = tempfile.mkstemp()
    with os.fdopen(fd, 'wb') as f:
        f.write(b_text)

    # Decode test data
    f = open(f_name, 'rb')
    dict_ = json.load(f, cls=AnsibleJSONDecoder)

    # Check if data are correct
    assert dict_['test_secrets']

# Generated at 2022-06-13 06:43:50.015973
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test case :
    # Input:
    # 'pairs': {
    #   '__ansible_vault': 'WyJvcmRwbGF5Ig==',
    # }
    # Output:
    # object_hook(pairs): AnsibleVaultEncryptedUnicode(value)
    def test_object_hook_vault(mocker):

        pairs = {'__ansible_vault': 'WyJvcmRwbGF5Ig=='}

        decoder = AnsibleJSONDecoder()
        assert decoder.object_hook(pairs) is not None

    # Test case :
    # Input:
    # 'pairs': {
    #   '__ansible_unsafe': {
    #       'foo': 'bar',
    #   },
    # }
    #

# Generated at 2022-06-13 06:43:59.488508
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs = {}
    pairs['__ansible_vault'] = '$ANSIBLE_VAULT;1.1;AES256\n' \
                               '3833653537376135666339616663613630363530643932613036346639313166636233353530\n' \
                               '3435663433373834653231653338366134666438366664396538643433356465\n'

    value = decoder.object_hook(pairs)
    assert isinstance(value, AnsibleVaultEncryptedUnicode)
    assert value.vault is None

    pairs['__ansible_unsafe'] = '$ANSIBLE_VAULT;1.1;AES256\n' \
                

# Generated at 2022-06-13 06:44:11.760801
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault_content = {'foo': 'bar'}
    vault_secrets = ["bar"]
    vault_key = 'dGVzdCBrZXk='
    vault_json = '{"__ansible_vault" : "%s"}' % vault_key
    content_json = json.dumps(vault_content, cls=AnsibleJSONEncoder)
    vault_value = AnsibleVaultEncryptedUnicode(vault_json, VaultLib(secrets=[vault_secrets[0]]))
    unsafe_value = wrap_var(vault_content)

    # Input should have AnsibleVaultEncryptedUnicode type
    result = decoder.object_hook({'__ansible_vault' : vault_key})

# Generated at 2022-06-13 06:44:15.778059
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()
    assert isinstance(ansible_json_decoder, AnsibleJSONDecoder)
    assert ansible_json_decoder.object_hook({'__ansible_unsafe': "{{ password }}"}) == 'password'

# Generated at 2022-06-13 06:44:27.612859
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {'x': 'ansible_vault_pw'}
    data['__ansible_vault'] = VaultLib.encrypt(json.dumps(data))
    data['__ansible_unsafe'] = 'secret'

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['ansible_vault_pw'])

    decoded = decoder.decode(json.dumps(data))

    assert decoded['x'] == 'ansible_vault_pw'
    assert decoded['__ansible_vault'].vault
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert not isinstance(decoded['__ansible_unsafe'], AnsibleUnsafeText)

# Generated at 2022-06-13 06:44:35.783880
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.module_utils.common._collections_compat import Mapping

    assert isinstance(json.loads('{"valid": "json"}', cls=AnsibleJSONDecoder), Mapping)
    assert isinstance(json.loads('{"__ansible_vault": "vaulted"}', cls=AnsibleJSONDecoder), AnsibleVaultEncryptedUnicode)
    assert isinstance(json.loads('{"__ansible_unsafe": "unsafe"}', cls=AnsibleJSONDecoder), AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:44:46.632399
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    class MyVaultLib(VaultLib):

        def decrypt(self, text):
            return text.upper()

    def assert_object_hook():
        d = AnsibleJSONDecoder()

        assert d.object_hook({'a':'b'}) == {'a': 'b'}
        assert d.object_hook({'a':{'__ansible_unsafe':'b'}}) == {'a': wrap_var('b')}

        d = AnsibleJSONDecoder()
        d._vaults['default'] = VaultLib(secrets=["hi"])

# Generated at 2022-06-13 06:44:50.306093
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault = VaultLib(secrets=['123456789012345678901234567890'])

    # Test empty json object
    v = '{"__ansible_vault": "9b4c4b1e99b83d93fa4e"}'
  

# Generated at 2022-06-13 06:44:55.170597
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class TestClass(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    assert AnsibleJSONDecoder.object_hook({'__dict__': {"key": "value"}}) == TestClass(key='value')
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': "1234"}) == AnsibleVaultEncryptedUnicode(1234)
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': "1234"}) == wrap_var(1234)

# Generated at 2022-06-13 06:45:06.631463
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # Test __ansible_vault

# Generated at 2022-06-13 06:45:15.496437
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook({'__ansible_unsafe': '{"__ansible_unsafe": "value"}'})
    value = json.loads(pairs['__ansible_unsafe'])
    assert value['__ansible_unsafe'] == 'value'
    pairs = decoder.object_hook({'__ansible_vault': {'vault_id': 1, 'encrypted_value': 'enc'}})
    assert pairs['__ansible_vault'].vault_id == 1
    assert pairs['__ansible_vault'].vault_encrypted_value == 'enc'


# Generated at 2022-06-13 06:45:24.332892
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # test __ansible_vault is converted to AnsibleVaultEncryptedUnicode
    test_data = {
        "__ansible_vault": "test_data"
    }
    json_data = json.dumps(test_data, cls=AnsibleJSONEncoder)
    result = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert isinstance(result["__ansible_vault"], AnsibleVaultEncryptedUnicode)

    # test __ansible_unsafe is converted to wrap_var

# Generated at 2022-06-13 06:45:36.200951
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()
    decoder._vaults = {
        'not_used_vault': None,
        'default': 1,
        'another_vault': 2
    }


# Generated at 2022-06-13 06:45:46.601431
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create json strings
    json_str_1 = '{"__ansible_vault": "AES256", "__ansible_unsafe": "AES256"}'
    json_str_2 = '{"__ansible_vault": "AES128", "__ansible_unsafe": "AES128"}'

    # Create objects
    obj_1 = AnsibleVaultEncryptedUnicode("AES256")
    obj_2 = AnsibleVaultEncryptedUnicode("AES128")
    obj_3 = wrap_var("AES256")
    obj_4 = wrap_var("AES128")

    # Create dicts
    dict_1 = {
        '__ansible_vault': "AES256",
        '__ansible_unsafe': "AES256"
    }
    dict

# Generated at 2022-06-13 06:45:56.168043
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    import os

    JSON_DIR = os.path.join(os.path.dirname(__file__), 'json')
    ANSIBLE_VAULT_DATA_FILE = os.path.join(JSON_DIR, 'ansible_vault_data')
    ANSIBLE_UNSAFE_DATA_FILE = os.path.join(JSON_DIR, 'ansible_unsafe_data')

    # create the vault password file
    with open(ANSIBLE_VAULT_DATA_FILE, 'w') as f:
        password = os.urandom(20)
        f.write(password.decode())

    # create the unsafe data
    unsafe_value = object()

# Generated at 2022-06-13 06:46:06.983316
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = VaultLib(secrets=['1234'])

# Generated at 2022-06-13 06:46:19.650701
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [{'password': 'VaultPwd'}]
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()

    json_data = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;admin;345StHtrW7f8gUMnbnX9XA==;b6o0zs+k', '__ansible_unsafe': 'foo'}


# Generated at 2022-06-13 06:46:34.615517
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Example of how the decrypt worked in Ansible 2.2
    assert decoder.object_hook({'__ansible_vault': 'test'}) == AnsibleVaultEncryptedUnicode('test')

    # Example of how the object_hook should handle '__ansible_vault' pair
    assert decoder.object_hook({'__ansible_vault': 'test', 'key1': 'value1'}) == AnsibleVaultEncryptedUnicode('test')

    # Example of how the object_hook should handle '__ansible_vault' pair
    assert decoder.object_hook({'__ansible_vault': 'test', 'key1': 'value1', 'key2': 'value2'}) == AnsibleVaultEncryptedUnicode('test')

    #

# Generated at 2022-06-13 06:46:40.027674
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Check simple AnsibleVaultEncryptedUnicode with vault
    pairs = {"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;vault123\n346237346461626363666339616565396233353965353332626631366132316432313030666435\n363761636232303837353638393836326132633661376137623232393734643262333263333965\n3638633963303934363163663366\n"}
    decoded_value = AnsibleJSONDecoder().object_hook(pairs)
    assert isinstance(decoded_value, AnsibleVaultEncryptedUnicode)
    assert decoded_value.vault is not None

# Generated at 2022-06-13 06:46:54.361113
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Instantiate an instance of the AnsibleJSONDecoder class
    decoder = AnsibleJSONDecoder()

    # Test the single key case: '__ansible_vault'
    single_key_tuple = ('__ansible_vault', 'ABCDEFG')
    single_key_dict = {'__ansible_vault': 'ABCDEFG'}

    assert(decoder.object_hook(single_key_tuple) == single_key_dict)
    assert(type(decoder.object_hook(single_key_tuple)['__ansible_vault']) == AnsibleVaultEncryptedUnicode)
    assert(decoder.object_hook(single_key_tuple)['__ansible_vault'] == 'ABCDEFG')

    # Test the single key case: '__ansible_uns

# Generated at 2022-06-13 06:46:59.462967
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:08.963956
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault = AnsibleVaultEncryptedUnicode()
    vault.vault = AnsibleJSONDecoder._vaults['default']
    vault.vault._secrets = ['pass']

    # dict with __ansible_vault value
    pairs = {'__ansible_vault': 'vault_value'}
    result = decoder.object_hook(pairs)
    assert result == vault, \
        "AnsibleJSONDecoder.object_hook([__ansible_vault: vault_value]) should return vault object"

    # dict without __ansible_vault value
    pairs = {'__ansible_unsafe': 'unsafe_value'}
    result = decoder.object_hook(pairs)

# Generated at 2022-06-13 06:47:18.201456
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    obj = {'__ansible_vault': 'encrypted password', '__ansible_unsafe': '$ANSIBLE_VAULT', '__other': 'other'}
    decoded_obj = decoder.object_hook(obj)

    assert decoded_obj['__ansible_vault']
    assert isinstance(decoded_obj['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert decoded_obj['__ansible_unsafe']
    assert isinstance(decoded_obj['__ansible_unsafe'], wrap_var.UnsafeProxy)
    assert decoded_obj['__other'] == 'other'

# Generated at 2022-06-13 06:47:23.332209
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = {'test': {'test': {'test': {'test': 'test'}}, 'test': {'test': 'test'}, 'test': 'test'}}
    obj['__ansible_unsafe'] = obj
    #obj['__ansible_vault'] = 'test'

    assert json.loads(json.dumps(obj, cls=AnsibleJSONEncoder), cls=AnsibleJSONDecoder) == obj

# Generated at 2022-06-13 06:47:41.759266
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secret_string = "asdf"
    secret_string_json = json.dumps(secret_string)

    # test AnsibleJSONEncoder creates a __ansible_vault attribute
    test_input = {
        '__ansible_vault': {
            'enc': 'aes256',
            'str': secret_string
        },
    }
    expected_output = {
        '__ansible_vault': secret_string
    }
    actual_output = json.loads(json.dumps(test_input), cls=AnsibleJSONDecoder)
    assert json.dumps(actual_output) == json.dumps(expected_output)
    assert actual_output['__ansible_vault'].vault.decrypt(secret_string_json) == secret_string

# Generated at 2022-06-13 06:47:48.404241
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test data for AnsibleVaultEncryptedUnicode
    ansible_vault_dict = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;xxx',
        'data': 'SECRET DATA'
    }

    # Test data for wrap_var
    wrap_var_dict = {
        '__ansible_unsafe': True
    }

    # Test for AnsibleVaultEncryptedUnicode
    test_cls = AnsibleJSONDecoder()
    test_cls.set_secrets('SECRETS')
    test_result = test_cls.object_hook(ansible_vault_dict)
    assert test_result.vault == test_cls._vaults['default']
    assert test_result['data'] == 'SECRET DATA'

# Generated at 2022-06-13 06:47:59.632627
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_str = ('{"__ansible_vault": "{plain:vault_encrypted_str}", "__ansible_unsafe": "unsafe_str"}')
    secrets = 'secrets'

    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    json_dict = decoder.decode(json_str)

    assert json_dict['__ansible_vault'].vault.secrets == secrets
    assert isinstance(json_dict['__ansible_unsafe'], wrap_var)
    assert json_dict['__ansible_unsafe'].__dict__['_obj'] == 'unsafe_str'

# Generated at 2022-06-13 06:48:07.204923
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    """
    Test for dictionary pair: '__ansible_vault': 'value'
    """
    pairs = {'__ansible_vault': 'value'}
    ret = decoder.object_hook(pairs)

    assert ret is not None
    assert isinstance(ret, AnsibleVaultEncryptedUnicode)
    assert ret.vault == {}

    """
    Test for dictionary pair: 'key': 'value'
    """
    pairs = {'key': 'value'}
    ret = decoder.object_hook(pairs)

    assert ret is not None
    assert ret == pairs

# Generated at 2022-06-13 06:48:18.013525
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.module_utils._text import to_native

    # test object_hook
    key = '__ansible_vault'
    value = '$ANSIBLE_VAULT;1.1;AES256'
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({key: value})
    message = to_native(result)
    assert result.vault is None, message
    assert isinstance(result, AnsibleVaultEncryptedUnicode), message

    # test object_hook: assign vault
    vaults = {}
    vaults['default'] = VaultLib(secrets=['12345678'])

# Generated at 2022-06-13 06:48:32.809417
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {"__ansible_vault": "encoded"}
    pairs = decoder.object_hook(pairs)
    assert(type(pairs["__ansible_vault"]) == AnsibleVaultEncryptedUnicode)
    pairs = {"__ansible_unsafe": "foo"}
    pairs = decoder.object_hook(pairs)
    assert(type(pairs["__ansible_unsafe"]._unsafe_proxy) == str)
    # Test with a bad key to confirm it is not swallowed
    pairs = {"__ansible_invalid": "foo"}
    pairs = decoder.object_hook(pairs)
    assert(type(pairs) == dict)
    assert(pairs["__ansible_invalid"] == "foo")

# Generated at 2022-06-13 06:48:45.019363
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    json_data = '''{
        "foo": "bar",
        "__ansible_vault": "foo",
        "__ansible_unsafe": "bar"
    }'''

    AnsibleJSONDecoder.set_secrets({'default': 'default_id'})
    result = json.loads(json_data, cls=AnsibleJSONDecoder)

    assert result['foo'] == 'bar'
    assert result['__ansible_vault'] == '!!vault |\n          foo'
    assert result['__ansible_unsafe'].has_been_wrapped()
    assert result['__ansible_unsafe'].get_wrapped_var() == 'bar'



# Generated at 2022-06-13 06:48:48.664089
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    output = decoder.object_hook({'__ansible_vault': 'test_string'})
    assert output == AnsibleVaultEncryptedUnicode('test_string')

# Generated at 2022-06-13 06:48:58.282629
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    vault_secrets = [{'vault_id': 'default', 'secret': 'ansible'}]

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(vault_secrets)

    a = decoder.object_hook({u'__ansible_unsafe': u'Unsafe message'})
    assert isinstance(a, AnsibleUnsafeText)
    assert a == 'Unsafe message'

    a = decoder.object_hook({u'__ansible_vault': u'Vault: message'})
    assert isinstance(a, AnsibleVaultEncryptedUnicode)
    assert a == 'Vault: message'


# Generated at 2022-06-13 06:49:08.221398
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['dummy_pass']
    encoder = AnsibleJSONEncoder()
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)


# Generated at 2022-06-13 06:49:21.072922
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({ "__ansible_unsafe": "hello.world" })
    assert result == {"__ansible_unsafe": "hello.world"}
    assert result['__ansible_unsafe'] == 'hello.world'

# Generated at 2022-06-13 06:49:21.633772
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert True

# Generated at 2022-06-13 06:49:27.892053
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder().object_hook({'x': 'y'}) == {u'x': u'y'}
    assert AnsibleJSONDecoder().object_hook({'x': u'\u00ac'}) == {u'x': u'\u00ac'}
    assert AnsibleJSONDecoder().object_hook({'__my_enc': '##'}) == {u'__my_enc': u'##'}
    assert AnsibleJSONDecoder().object_hook({'__ansible_vault': '##'}) == {u'__ansible_vault': u'##'}
    assert AnsibleJSONDecoder().object_hook({'__ansible_vault': '##'})['__ansible_vault'].vault == None

# Generated at 2022-06-13 06:49:39.348803
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    x = json.loads('{"__ansible_vault": "hello"}', cls=AnsibleJSONDecoder)
    assert isinstance(x, AnsibleVaultEncryptedUnicode)
    assert x.vault is None

    secrets = [b'test']
    AnsibleJSONDecoder.set_secrets(secrets)
    x = json.loads('{"__ansible_vault": "hello"}', cls=AnsibleJSONDecoder)
    assert isinstance(x, AnsibleVaultEncryptedUnicode)
    assert isinstance(x.vault, VaultLib)


# Generated at 2022-06-13 06:49:46.600791
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = VaultLib()


# Generated at 2022-06-13 06:49:56.269961
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': 'some_vault', '__ansible_unsafe': 'some_value'}
    result = decoder.object_hook(pairs)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault is None

    secret = "sample_password"
    AnsibleJSONDecoder.set_secrets(secret)
    result = decoder.object_hook(pairs)
    assert result.vault.secrets == secret

    pairs = {'some_key': 'some_value'}
    result = decoder.object_hook(pairs)
    assert result == pairs


# Generated at 2022-06-13 06:50:06.212479
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder([])
    ae = 'VaultLib'

# Generated at 2022-06-13 06:50:16.320245
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES128;ansible\n613264313661323363386163656638623730333739376664620a373331323363376362626132313961643132333763343738316232383065\n613463646632306462646361356466386333636238613661646266616338646563396230663584f\n',
    }

    result = decoder.object_hook(pairs)
    assert '__ansible_vault' in result
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:50:19.110939
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    data = json.loads('''{
    "name": "Sample playbook",
    "description": "This is a sample playbook",
    "__ansible_vault": "vault-value"
}''', cls=AnsibleJSONDecoder)

    assert(isinstance(data['__ansible_vault'], AnsibleVaultEncryptedUnicode))



# Generated at 2022-06-13 06:50:33.205227
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test to wrap the variables with class `UnsafeProxy` when it contains the key '__ansible_unsafe'
    decoder = AnsibleJSONDecoder()
    unsafe_var = {'__ansible_unsafe': 'unsafe'}

    assert decoder.object_hook(unsafe_var) == wrap_var(unsafe_var['__ansible_unsafe'])

    # Test to wrap the variables with class `AnsibleVaultEncryptedUnicode` when it contains the key '__ansible_vault'
    decoder = AnsibleJSONDecoder()
    vault_var = {'__ansible_vault': 'vault'}

    assert type(decoder.object_hook(vault_var)) == AnsibleVaultEncryptedUnicode
    assert decoder.object_hook(vault_var)

# Generated at 2022-06-13 06:50:53.917452
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    ret = decoder.object_hook({})
    assert ret == {}
    ret = decoder.object_hook({'__ansible_unsafe':'unsafe'})
    assert ret.__class__.__name__ == 'AnsibleUnsafeText'
    assert ret.__str__() == 'unsafe'



# Generated at 2022-06-13 06:50:58.324787
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['password'])

    pairs = {
        'foo': 'bar',
        '__ansible_vault': 'AES256!',
        '__ansible_unsafe': True
        }

    obj = decoder.object_hook(pairs)
    assert obj['foo'] == 'bar'
    assert obj['__ansible_vault'] == 'AES256!'
    assert obj['__ansible_unsafe'] is True

# Generated at 2022-06-13 06:51:06.348313
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = encrypt_text(['string1', 'string2'])
    secrets = '\n'.join(secrets)

    decoder = AnsibleJSONDecoder.__new__(AnsibleJSONDecoder)
    AnsibleJSONDecoder.set_secrets(secrets)


# Generated at 2022-06-13 06:51:12.128904
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['test password 1', 'test password 2']
    AnsibleJSONDecoder.set_secrets(secrets)
    result = json.loads('{"test": "value", "__ansible_vault": "test value", "__ansible_unsafe": "test value"}', cls=AnsibleJSONDecoder)
    assert(result['__ansible_unsafe'] == 'test value')


# Generated at 2022-06-13 06:51:21.108702
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import tempfile
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib

    # Create a tempfile and write a vault-encrypted string to it
    _, vault_filename = tempfile.mkstemp()
    vault = VaultLib(secrets=[os.environ['ANSIBLE_VAULT_PASSWORD']])
    with open(vault_filename, 'w') as f:
        f.write(vault.encrypt('password123'))

    # Load the vault string from the file and verify that it's a VaultEncrypted
    with open(vault_filename, 'r') as f:
        decoder = AnsibleJSONDecoder(f.read())

# Generated at 2022-06-13 06:51:35.240825
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Given
    decoder = AnsibleJSONDecoder()