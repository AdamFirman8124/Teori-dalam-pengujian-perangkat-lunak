

# Generated at 2022-06-13 06:41:39.653645
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # set up vault
    secrets = ['test_secret']
    AnsiJSONDec = AnsibleJSONDecoder

    assert AnsiJSONDec.object_hook({'a': 1}) == {'a': 1}

    AnsiJSONDec.set_secrets(secrets)

    assert AnsiJSONDec.object_hook({'a': 1}) == {'a': 1}

    assert isinstance(AnsiJSONDec.object_hook({'__ansible_vault': '1'}), AnsibleVaultEncryptedUnicode)

    assert isinstance(AnsiJSONDec.object_hook({'__ansible_unsafe': '1'}), wrap_var)

# Generated at 2022-06-13 06:41:49.018675
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # test case: __ansible_vault

# Generated at 2022-06-13 06:41:54.176389
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = VaultLib(secrets=['password'])

    assert decoder.decode('[{ "_ansible_vault": "bar" }]') == [{u'_ansible_vault': u'bar', u'__ansible_vault': u'bar'}]

# Generated at 2022-06-13 06:42:04.091898
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.json import AnsibleJSONEncoder

    json_str = '''
    {
        "answer": {
            "__ansible_vault": "5b5a1d5a5f5d5e5a5f5e5d5e5b5d5b5c5a5f5d5a5f5d5a5f5e5d5e5b5a5d5a5f",
            "__ansible_unsafe": true
        }
    }
    '''
    # Create the decoder and the encoder
   

# Generated at 2022-06-13 06:42:15.489316
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:22.888791
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:34.082834
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {'default': 'secret'}
    vault = VaultLib(secrets=secrets)
    enc_text = vault.encrypt('foo')
    d = AnsibleJSONDecoder()
    d.set_secrets(secrets)
    val = d.decode('{"a":1, "__ansible_vault": "%s", "b":2}' % enc_text)
    assert val['__ansible_vault'].vault.secrets == secrets
    assert val['__ansible_vault'] == 'foo'
    assert val['a'] == 1
    assert val['b'] == 2



# Generated at 2022-06-13 06:42:46.714165
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:54.033684
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;user\n123\n'})

    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)
    assert pairs.vault == decoder._vaults['default']

    pairs = decoder.object_hook({'__ansible_unsafe': '<html>'})

    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)
    assert pairs == '<html>'

# Generated at 2022-06-13 06:42:57.785674
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = {'__ansible_vault': '1234567890'}
    assert AnsibleJSONDecoder.object_hook(json_data) == {'__ansible_vault': AnsibleVaultEncryptedUnicode('1234567890')}



# Generated at 2022-06-13 06:43:02.610086
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Mock test

    results = {
        "__ansible_vault": "test_ansible_vault",
        "__ansible_unsafe": "test_ansible_unsafe"
    }

    decoder = AnsibleJSONDecoder()

    assert results == decoder.object_hook(results)



# Generated at 2022-06-13 06:43:10.506318
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'password']
    test_AnsibleJSONEncoder_object_hook(secrets)


# Generated at 2022-06-13 06:43:22.728776
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_dict = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;ansiblesample\n'
                           '30323233636337646665343766353731356334356434316130636264343337316430303164373536\n'
                           '38373261346233666230633233653834393762396165633938663564326138656164346138353461\n'
                           '3463306433393864383334643364623664663764356635613638636433000000',
        '__ansible_unsafe': 'answer=42'
    }

    decoder = AnsibleJSONDecoder()
    value = decoder.object_hook(test_dict)

# Generated at 2022-06-13 06:43:32.512210
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:38.591247
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data = {'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'}
    result = decoder.object_hook(data)
    assert result == {'__ansible_vault': AnsibleVaultEncryptedUnicode('foo'), '__ansible_unsafe': 'bar'}

# Generated at 2022-06-13 06:43:50.413535
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    test_secrets = ['test_password']
    AnsibleJSONDecoder.set_secrets(test_secrets)

# Generated at 2022-06-13 06:43:55.370410
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_unsafe': {'__ansible_unsafe': 'foo'}}) == wrap_var({'__ansible_unsafe': 'foo'})
    assert decoder.object_hook({'__ansible_vault': '$ENC64$foo=='}) is not None

# Generated at 2022-06-13 06:44:09.261750
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import six
    import json

    # test for AnsibleVaultEncryptedUnicode
    test_vault_item = '{"__ansible_vault": "vault value"}'
    decoded = json.loads(test_vault_item, cls=AnsibleJSONDecoder)
    assert isinstance(decoded, dict)
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert decoded['__ansible_vault'].vault is not None

    # test for unsafe proxy
    test_unsafe_item = '{"__ansible_unsafe": "unsafe value"}'
    decoded = json.loads(test_unsafe_item, cls=AnsibleJSONDecoder)
    assert isinstance(decoded, dict)

# Generated at 2022-06-13 06:44:20.918473
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create secrets
    secrets = ['test_secret']

    # Create a JSON string
    json_string = """
    {
        "__ansible_vault": "test"
    }
    """

    # Perform the test
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)
    result = decoder.decode(json_string)

    # Verify the result
    assert '__ansible_vault' in result
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert result['__ansible_vault'].encoded_data == "test"
    assert result['__ansible_vault'].vault == decoder._vaults['default']

# Generated at 2022-06-13 06:44:26.213355
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:38.542140
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    AnsibleJSONDecoder.object_hook test
    """
    import os
    import tempfile
    import shutil
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    tmp_dir = tempfile.mkdtemp(prefix="ansible_test_AnsibleJSONDecoder_object_hook")
    vault_password_file = os.path.join(tmp_dir, "test.pass")

# Generated at 2022-06-13 06:44:48.957301
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # __ansible_vault
    secret = 'the vault password'

# Generated at 2022-06-13 06:44:58.503664
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_cases = [
        # test strings
        ({"__ansible_unsafe": "hello"}, "hello"),
        # test lists
        ({"__ansible_unsafe": ["hello"]}, ['hello']),
        # test dictionaries
        ({"__ansible_unsafe": {'hello': 'world'}}, {'hello': 'world'}),
    ]

    for case, expected in test_cases:
        assert AnsibleJSONDecoder().object_hook(case) == expected



# Generated at 2022-06-13 06:45:05.878291
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    assert decoder.object_hook( { '__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256' } ) == { '$ANSIBLE_VAULT;1.2;AES256' }
    assert decoder.object_hook( { '__ansible_unsafe': 'unsafe' } ) == { 'unsafe' }

# Test the AnsibleJSONEncoder class.

# Generated at 2022-06-13 06:45:16.392281
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = '''
    {
        "__ansible_vault": "test_str",
        "__ansible_unsafe": "test_str"
    }
    '''

    # Create the object of AnsibleJSONDecoder
    json_obj = AnsibleJSONDecoder()

    # Convert the json_data to dictionary
    json_dict = json.loads(json_data, cls=AnsibleJSONDecoder)

    # Check if the object is not None
    assert json_obj is not None

    # Check if the json_dict is not None
    assert isinstance(json_dict, dict) is True

    # Check for the class type of the value in the dictionary
    assert json_dict['__ansible_vault'] is AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:45:24.905209
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    assert(isinstance(json.loads('{"__ansible_unsafe": []}', cls=AnsibleJSONDecoder), dict))
    assert(str(json.loads('{"__ansible_unsafe": []}', cls=AnsibleJSONDecoder)) == "{'__ansible_unsafe': []}")

    assert(isinstance(json.loads('{"__ansible_vault": "test"}', cls=AnsibleJSONDecoder), dict))
    assert(str(json.loads('{"__ansible_vault": "test"}', cls=AnsibleJSONDecoder)) == "{'__ansible_vault': 'test'}")

    # TODO(mnaser): We will make this test more robust once AnsibleVaultEncodedUnicode()
    #               works with the VaultLib() object properly


# Generated at 2022-06-13 06:45:36.661763
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # test if encrypted vars are being decoded correctly
    # test if unsafe vars are being wrapped correctly
    items = {
        'test_value1': 'test_string',
        'test_value2': {
            'test_value3': 'test_string'
        },
        'test_value4': [
            'test_string',
            {
                'test_value6': 'test_string'
            }
        ]
    }

    # Encrypt the vars
    vault = VaultLib(secrets=['mysecrets'])
    vault_data = vault.serialize(items)

    # Prepare the data to be decoded
    data = {}
    data['__ansible_vault'] = vault_data
    data['__ansible_unsafe'] = [1, 2]

    # Decode the data

# Generated at 2022-06-13 06:45:43.516171
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoded_data = {
        "foo": "bar",
        "__ansible_vault": "foo",
        "__ansible_unsafe": {
            "bar": "baz"
        }
    }

    assert AnsibleJSONDecoder.object_hook(decoded_data) == {
        "foo": "bar",
        "__ansible_vault": "foo",
        "__ansible_unsafe": {
            "bar": "baz"
        }
    }

# Generated at 2022-06-13 06:45:50.800601
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['hunter2', 'foobar']
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()

    assert decoder.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')

    assert decoder.object_hook({'__ansible_unsafe': 'bar'}) == wrap_var('bar')

    assert decoder.object_hook({'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'}) == {'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'}

# Generated at 2022-06-13 06:45:57.479984
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import sys

    ansible_vault_decode_stdin = "ansible-vault-decode-stdin"
    ansible_vault_decode_stderr_template = "ERROR! the field 'vault_password' is required but was not set"
    ansible_vault_decode_stderr = "ansible-vault-decode-stderr"
    ansible_vault_decode_stdout = "ansible-vault-decode-stdout"
    ansible_vault_decode_stdout_dict_template = "{{\"__ansible_vault\": \"$ANSIBLE_VAULT;1.1;AES256\n%s\", \"key\": \"value\"}}\n"

# Generated at 2022-06-13 06:46:13.842268
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Initilize the decoder
    decoder = AnsibleJSONDecoder()
    # Test the default values
    assert decoder._vaults == {}

    # Test the function
    # Test ansible_vault
    pairs = {
        'foo': 'bar',
        '__ansible_vault': 'foo',
    }
    value = decoder.object_hook(pairs)
    assert value.__class__ == AnsibleVaultEncryptedUnicode.__class__
    assert value == 'foo'

    # Test ansible_unsafe
    pairs = {
        'foo': 'bar',
        '__ansible_unsafe': 'foo',
    }
    value = decoder.object_hook(pairs)
    assert value.__class__ == str.__class__
    assert value == 'foo'



# Generated at 2022-06-13 06:46:20.290107
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    j = '{"password":"$ANSIBLE_VAULT;1.1;AES256;user\n393764663732646135323365353237666137653865643661303430653865323935363730613734613961340a346666346266646338366363366236313064383963353963653931633831316132653837613862640a663362656466333162366561646439653464383338646539313531653132393566613337623832303d\n"}'


# Generated at 2022-06-13 06:46:35.280764
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({"__ansible_vault": "foo"}) == AnsibleVaultEncryptedUnicode("foo")
    assert decoder.object_hook({"__ansible_unsafe": "foo"}) == wrap_var("foo")
    assert decoder.object_hook({"__ansible_vault": "foo", "__ansible_unsafe": "bar"}) == AnsibleVaultEncryptedUnicode("foo")
    assert decoder.object_hook({"foo": "bar"}) == {"foo": "bar"}
    assert decoder.object_hook({"__ansible_unsafe": "foo", "__ansible_vault": "bar"}) == wrap_var("foo")
    assert decoder.object_hook({}) == {}

# Generated at 2022-06-13 06:46:46.653614
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {
        'a': 'b',
        '__ansible_vault': 'foobar'
    }

    secrets = {
        '__ansible_vault': 'changeit'
    }

    obj = AnsibleJSONDecoder.object_hook(data)
    assert isinstance(obj['a'], str)
    assert isinstance(obj['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert obj['__ansible_vault'].vault is None

    AnsibleJSONDecoder.set_secrets(secrets)
    obj = AnsibleJSONDecoder.object_hook(data)
    assert isinstance(obj['__ansible_vault'].vault, VaultLib)
    assert obj['__ansible_vault'].vault is not None

# Generated at 2022-06-13 06:46:54.112546
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import shutil
    import tempfile
    import filecmp

    # Create temporary directory
    temp_dir = tempfile.mkdtemp(prefix='ansible_vault_test_')
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create a vault password file
    vault_pass_file_path = os.path.join(temp_dir, 'vault_password_file.txt')
    with open(vault_pass_file_path, mode='w') as vault_pass_file:
        vault_pass_file.write('my-secret-password')

    # Create a multi vault password file
    vault_pass_file_path_multi = os.path.join(
        temp_dir, 'vault_password_file_multi.txt')
   

# Generated at 2022-06-13 06:47:00.917579
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import ansible.parsing.vault as vault_module

    # Test with empty VaultLib()
    test_json = '{"__ansible_vault": "This is a test"}'

    vault_lib = VaultLib()
    with vault_module.unlocked_vault_secrets('password') as v:
        v.update(vault_lib.secrets)

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(vault_lib.secrets)
    result = decoder.decode(test_json)

    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == vault_lib
    assert result == u"This is a test"

# Generated at 2022-06-13 06:47:09.896275
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_str = '''
    { "__ansible_vault": "ZGFnc2FnZ2Q=" }
    '''
    json_obj = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert json_obj == 'dagsagggd'
    json_str = '''
    { "__ansible_vault": "ZGFnc2FnZ2Q=" , "__ansible_unsafe": "dagsagggd" }
    '''
    json_obj = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert hasattr(json_obj["__ansible_vault"], 'unvault')
    assert json_obj["__ansible_unsafe"].get_text_type() == 'UNSAFE'

#

# Generated at 2022-06-13 06:47:18.202023
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    kwargs = {}
    kwargs['object_hook'] = []
    jsondecoder = AnsibleJSONDecoder(**kwargs)
    assert jsondecoder
    assert jsondecoder._vaults == {}

    pairs = {}
    pairs['__ansible_vault'] = 'foo'
    pairs['__ansible_unsafe'] = 'baz'
    pairs['key1'] = 'value'
    pairs['key2'] = {'key3': 'value3', 'key4': 'value4'}

    result = jsondecoder.object_hook(pairs)
    assert result == pairs

# Generated at 2022-06-13 06:47:27.214413
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''test the object_hook method of AnsibleJSONDecoder'''

    import yaml

    def as_dict(pairs):
        return pairs

    # fake vault encrypted text

# Generated at 2022-06-13 06:47:41.693730
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:49.266027
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test case 1, __ansible_vault key
    secrete1 = 'decrypted value'
    decoder.set_secrets([secrete1])
    pairs = {'__ansible_vault': 'encrypt_value'}
    decoded = decoder.object_hook(pairs)
    assert decoded.vault.secrets[0] == secrete1
    assert decoded.unprotected() == secrete1

    # Test case 2, __ansible_unsafe key
    pairs = {'__ansible_unsafe': 'unsafe value'}
    decoded = decoder.object_hook(pairs)
    assert decoded == 'unsafe value'



# Generated at 2022-06-13 06:48:01.523147
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:09.599126
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    
    # Test object_hook() with __ansible_vault
    input_dict_with_vault = '{"__ansible_vault": "foo"}'
    result = decoder.object_hook(json.loads(input_dict_with_vault))
    assert result.payload_type == 'encrypted'
    assert result.payload == 'foo'
    assert result.encryption_type == 'ansible_vault'

    # Test object_hook() with __ansible_unsafe
    input_dict_with_unsafe = '{"__ansible_unsafe": "foo"}'
    result = decoder.object_hook(json.loads(input_dict_with_unsafe))
    assert result.payload_type == 'unsafe'
    assert result.pay

# Generated at 2022-06-13 06:48:20.278611
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'test'
    test_vector = [{'__ansible_vault': 'VAULT_SECRET_STRING'}, {'__ansible_unsafe': 'UNSAFE_SECRET_STRING'}]
    decoder = AnsibleJSONDecoder()

    def object_hook(pairs):
        for key in pairs:
            value = pairs[key]

            if key == '__ansible_vault':
                value = AnsibleVaultEncryptedUnicode(value)
                if decoder._vaults:
                    value.vault = decoder._vaults['default']
                return value
            elif key == '__ansible_unsafe':
                return wrap_var(value)

        return pairs

    decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:48:31.959925
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class MyDecoder(AnsibleJSONDecoder):

        def __init__(self, *args, **kwargs):
            self.return_value = None
            super(MyDecoder, self).__init__(*args, **kwargs)

        def object_hook(self, pairs):
            self.return_value = pairs
            return pairs

    decoder = MyDecoder()
    # Test the return value with no kwargs
    pairs = decoder.decode('{}')
    assert pairs == {}
    # Test the return value with a __ansible_vault kwargs
    pairs = decoder.decode('{"__ansible_vault": "test"}')
    assert pairs == {'__ansible_vault': 'test'}

# Generated at 2022-06-13 06:48:44.082092
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret string']

    ansible_decoder = AnsibleJSONDecoder.set_secrets(secrets)
    test_json = """{
        "__ansible_unsafe": "{{ var | b64encode }}",
        "_meta": {
            "hostvars": {
                "localhost": {
                    "foo": "bar"
                }
            }
        },
        "localhost": {
            "ansible_connection": "local",
            "ansible_host": "127.0.0.1",
            "__ansible_vault": "this is a vault value"
        }
    }"""

    json_dict = json.loads(test_json)
    ansible_dict = ansible_decoder.object_hook(json_dict)


# Generated at 2022-06-13 06:48:51.109276
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def _json_loads(data):
        return json.loads(data, cls=AnsibleJSONDecoder)

    assert _json_loads('{"__ansible_unsafe": "foo"}')['__ansible_unsafe'] == wrap_var('foo')
    assert _json_loads('{"__ansible_vault": "VFJSUzIxNiVmRUU="}')['__ansible_vault'] == AnsibleVaultEncryptedUnicode('VFJSUzIxNiVmRUU=')

# Generated at 2022-06-13 06:48:54.985966
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_str = '{"__ansible_vault": "encrypted_value"}'

    vault_obj = AnsibleJSONDecoder.object_hook(json.loads(json_str))

    assert vault_obj['__ansible_vault'] == "encrypted_value"
    assert isinstance(vault_obj['__ansible_vault'], AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:49:02.744286
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class MockArgs(object):
        def __init__(self, secrets):
            self.ask_vault_pass = None
            self.vault_password_files = []
            self.new_vault_password_file = None
            self.output_file = None
            self.vault_ids = []
            self.secrets = secrets
    json_args = MockArgs(secrets=['abcd'])
    AnsibleJSONDecoder.set_secrets(json_args)

    decoder = AnsibleJSONDecoder(strict=False)
    orig_dict = {'a': 'b', '__ansible_vault': 'c'}

    decoded_dict = decoder.object_hook(orig_dict)


# Generated at 2022-06-13 06:49:10.198467
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test simple strings
    my_json = '{"a": "1", "b": 2}'
    my_json_decoded = json.loads(my_json, cls=AnsibleJSONDecoder)
    assert 'a' in my_json_decoded
    a_value = my_json_decoded.get('a')
    assert isinstance(a_value, str)
    assert a_value == '1'
    assert 'b' in my_json_decoded
    b_value = my_json_decoded.get('b')
    assert isinstance(b_value, int)

    # Test ansible_vault

# Generated at 2022-06-13 06:49:19.755050
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    # test __ansible_vault
    pairs = {'__ansible_vault': 'testvalue'}
    res = decoder.object_hook(pairs)
    assert type(res) is AnsibleVaultEncryptedUnicode
    assert res.vault is None

    # test __ansible_unsafe
    pairs = {'__ansible_unsafe': 'testvalue'}
    res = decoder.object_hook(pairs)
    assert type(res) is str
    assert res.ansible_safe is False

    # test default
    pairs = {'__ansible_vault': 'testvalue', '__ansible_unsafe': 'testvalue2'}
    res = decoder.object_hook(pairs)
    assert type(res) is dict

# Generated at 2022-06-13 06:49:27.288603
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook([]) == []
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook({}) == {}
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook("foo") == "foo"
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook("123") == "123"
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook(123) == 123
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).object_hook(12.3) == 12.3

   

# Generated at 2022-06-13 06:49:41.781423
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    original_data_set = dict(
        a="a",
        b="b",
        c=[1,2,3],
        d=dict(
            e="e",
            f="f",
            g=[4,5,6]
        )
    )


# Generated at 2022-06-13 06:49:50.677987
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    input_dict = dict(__ansible_vault='hahaha', __ansible_unsafe="hehehe")
    secrets = ['hahaha']
    d = AnsibleJSONDecoder()
    d._vaults['default'] = VaultLib(secrets=secrets)
    output_dict = d.object_hook(input_dict)
    assert isinstance(output_dict, dict)
    assert isinstance(output_dict['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(output_dict['__ansible_unsafe'], wrap_var)


# Generated at 2022-06-13 06:49:58.887520
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Given
    data = {"__ansible_vault": "value",
            "__ansible_unsafe": "value"}
    secrets = [{"some": "cipher", "other": "secret"}]
    # When
    AnsibleJSONDecoder.set_secrets(secrets)
    result = AnsibleJSONDecoder().object_hook(data)
    # Then
    assert isinstance(result, dict)
    assert isinstance(result["__ansible_vault"], AnsibleVaultEncryptedUnicode)
    assert isinstance(result["__ansible_unsafe"], ansible.utils.unsafe_proxy.AnsibleUnsafeText)
    with pytest.raises(AttributeError):
        result["__ansible_vault"].unencrypted_value



# Generated at 2022-06-13 06:50:06.017388
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    fake_vault_secrets = ['fake_secret']
    AnsibleJSONDecoder.set_secrets(fake_vault_secrets)

    pairs = {
        '__ansible_vault': 'fake_encrypted_value',
        '__ansible_unsafe': 'fake_unsafe_value'
    }

    result = AnsibleJSONDecoder.object_hook(pairs)

    assert '__ansible_vault' in result
    assert result['__ansible_vault'].vault.secrets == fake_vault_secrets

    assert '__ansible_unsafe' in result



# Generated at 2022-06-13 06:50:14.053969
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    raw_data = '{"top_level": "top_level_value", "__ansible_unsafe": "unsafe_value", "__ansible_vault": "vault_value"}'
    test_decoder = AnsibleJSONDecoder()
    test_decoder.set_secrets(dict(vault_password=b'password'))
    test_data = json.loads(raw_data, cls=AnsibleJSONDecoder)
    assert test_data['top_level'] == 'top_level_value'
    assert test_data['__ansible_unsafe'] == 'unsafe_value'
    assert test_data['__ansible_vault'] == 'vault_value'

# Generated at 2022-06-13 06:50:29.413440
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test vault

# Generated at 2022-06-13 06:50:35.717105
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    test_str = json.dumps({'__ansible_vault': 'ansible_vault_encrypted', '__ansible_unsafe': 'ansible_unsafe'})

    json_obj = decoder.decode(test_str)
    assert isinstance(json_obj['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(json_obj['__ansible_unsafe'], bytes)



# Generated at 2022-06-13 06:50:37.203838
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    s = '{"__ansible_vault": "test" }'

    decoder = AnsibleJSONDecoder(s)

# Generated at 2022-06-13 06:50:52.207595
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # This unit test is not executable as a standalone test,
    # because it has not been designed to be run with pytest.
    # It is intended to be run with Ansible, because Ansible
    # executes this unit test, after importing the class
    # AnsibleJSONDecoder.

    class Test:
        def __init__(self):
            pass

        def obj_hook(obj):
            ansible_vault = AnsibleVaultEncryptedUnicode(obj)

            return ansible_vault

    class TestVaultLib(VaultLib):
        def __init__(self):
            pass

        def _load_secrets(self, path):
            return ["mypassword"]

    class TestAnsibleJSONDecoder(AnsibleJSONDecoder):
        def __init__(self):
            pass


# Generated at 2022-06-13 06:51:02.581456
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = [{'__ansible_vault': 'encrypted_data'},
             {'__ansible_unsafe': 'unsafe_data'}]
    for pair in pairs:
        decoder_result = decoder.object_hook(pair)
        if '__ansible_vault' in pair:
            assert isinstance(decoder_result, AnsibleVaultEncryptedUnicode)
            assert decoder_result.data == pair['__ansible_vault']
        if '__ansible_unsafe' in pair:
            assert decoder_result.value == pair['__ansible_unsafe']

# Generated at 2022-06-13 06:51:12.682151
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import yaml

    raw = '''
        {
            "a": "b",
            "c": "d",
            "__ansible_vault": "foo",
            "__ansible_unsafe": "bar"
        }
        '''
    expected = {
        'a': 'b',
        'c': 'd',
        '__ansible_vault': AnsibleVaultEncryptedUnicode('foo'),
        '__ansible_unsafe': wrap_var('bar')
    }

    assert expected == yaml.load(raw, Loader=yaml.Loader)

# Generated at 2022-06-13 06:51:21.004976
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test '__ansible_vault'
    vault = 'test_ansible_vault'
    json_string = json.dumps({'__ansible_vault': vault})
    decoded_json = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert isinstance(decoded_json, AnsibleVaultEncryptedUnicode)
    assert decoded_json == vault

    # Test '__ansible_unsafe'
    unsafe = 'test_ansible_unsafe'
    json_string = json.dumps({'__ansible_unsafe': unsafe})
    decoded_json = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert decoded_json == unsafe

# Generated at 2022-06-13 06:51:35.174968
# Unit test for method object_hook of class AnsibleJSONDecoder