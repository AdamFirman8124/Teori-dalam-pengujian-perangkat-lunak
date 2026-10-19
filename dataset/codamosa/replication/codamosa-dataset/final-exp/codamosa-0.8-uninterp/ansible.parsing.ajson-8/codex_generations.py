

# Generated at 2022-06-13 06:41:32.010658
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:41:42.204284
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    default_password = '$ANSIBLE_VAULT;1.1;AES256\n12345678901234567890123456789012345678901234567890123456789012345\n12345678901234567890123456789012345678901234567890123456789012345\n12345678901234567890123456789012345678901234567890123456789012345\n123456789012345678901234567890123\n'
    decoder.set_secrets([default_password])
    # uncrypted
    obj = decoder.object_hook({'f1': 1, 'f2': 2})

# Generated at 2022-06-13 06:41:54.179708
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    vault_pass = 'test'
    test_secret = 'secret'
    decoder = AnsibleJSONDecoder()

    # Test if an object containing __ansible_vault is converted to an AnsibleVaultEncryptedUnicode object
    test_json = '{"__ansible_vault": "ANSIBLE_VAULT;1.1;AES256;test_vault\n' + test_secret.encode('base64') + "\n" + '"}'
    result = decoder.decode(test_json)
    assert isinstance(result, dict)
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)

    # Test if an object containing __ansible_unsafe is converted to a Proxy object
   

# Generated at 2022-06-13 06:42:00.962093
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    json_vault = {"__ansible_vault": "value1", "__ansible_unsafe": "value2"}

    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(json_vault)
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(result['__ansible_unsafe'], wrap_var)

# Generated at 2022-06-13 06:42:13.324952
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Prepare
    decoder = AnsibleJSONDecoder()
    pairs = {
        "string": "value",
        "integer": 1,
        "__ansible_vault": "test",
        "__ansible_unsafe": "unsafe"
    }

    # Execute
    result = decoder.object_hook(pairs)

    # Verify
    assert result['string'] == "value"
    assert result['integer'] == 1
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert not isinstance(result['__ansible_unsafe'], str)
    assert result['__ansible_unsafe'].__str__() == "unsafe"



# Generated at 2022-06-13 06:42:20.383492
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
   class MyAnsibleJSONDecoder(AnsibleJSONDecoder):
       def __init__(self, *args, **kwargs):
           kwargs['object_hook'] = self.object_hook
           super(MyAnsibleJSONDecoder, self).__init__(*args, **kwargs)

       def object_hook(self, pairs):
           for key in pairs:
               value = pairs[key]

               if key == '__ansible_vault':
                   value = AnsibleVaultEncryptedUnicode(value)
                   if self._vaults:
                       value.vault = self._vaults['default']
                   return value
               elif key == '__ansible_unsafe':
                   return wrap_var(value)

           return pairs



   # create a sample json data
   json_data = json.d

# Generated at 2022-06-13 06:42:33.790402
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    AnsibleJSONDecoder.set_secrets(['test secret'])
    json_data = '{"__ansible_vault": "test vault"}'
    unsafe_var_data = dict(some_value='test output', __ansible_unsafe=True)


# Generated at 2022-06-13 06:42:43.554919
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # __ansible_vault
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\nblabla'}
    assert isinstance(AnsibleJSONDecoder.object_hook(pairs), AnsibleVaultEncryptedUnicode)

    # __ansible_unsafe
    pairs = {'__ansible_unsafe': True}
    assert AnsibleJSONDecoder.object_hook(pairs) is True

    # Just a string
    pairs = {'test': 'test'}
    assert AnsibleJSONDecoder.object_hook(pairs) == {'test': 'test'}

# Generated at 2022-06-13 06:42:53.057294
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import string
    import random
    import json
    import unittest

    from ansible.parsing.vault import is_encrypted, _get_file_vault_secret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class AnsibleJSONDecoderTest(unittest.TestCase):

        def setUp(self):
            self.maxDiff = None

        def get_random_string(self, size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        def create_encoded_json_file(self, json_file_content, vault_id, vault_password_path, dont_encrypt=None):
            vault_password_file_content

# Generated at 2022-06-13 06:43:01.169342
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault_id = '$ANSIBLE_VAULT;1.1;AES256'
    vault_password = 'mypassword'
    vault_secrets = [ vault_password ]
    encrypted_value = 'U2FsdGVkX19jr/6UJm7y/45nXuVxLnHWMKjdzZPrdQ0='
    vault_encrypt_test = '%s;0.1;%s' % (vault_id, encrypted_value)
    decrypted_value = AnsibleVaultEncryptedUnicode(vault_encrypt_test)
    decrypted_value.vault = VaultLib(secrets=vault_secrets)
    decrypted_value = decrypted

# Generated at 2022-06-13 06:43:09.471153
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    v = VaultLib(password_file='./password_file')
    e_val = '$ANSIBLE_VAULT;1.1;AES256\n37306637306363316262666265343230653236303231660a6439626336643330656236653235313130626531373864616662383132316334630a353365643937303032333238663131323134323461316361643935306232356334336435383133363939313464353465646631323331323265310a'

# Generated at 2022-06-13 06:43:22.266716
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    enc = AnsibleJSONEncoder()

# Generated at 2022-06-13 06:43:31.334640
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Load the test data
    import os
    import yaml
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_file_path, "test_AnsibleJSONDecoder_data.yml")) as f:
        test_data = yaml.safe_load(f)
    decoder = AnsibleJSONDecoder()
    # Run the test
    for d in test_data:
        for t in d['tests']:
            expected_result = t['result']
            test_result = decoder.object_hook(d['secret_data'])
            assert test_result == expected_result



# Generated at 2022-06-13 06:43:35.917962
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = u'{"__ansible_unsafe": "{{ template_dir }}/secrets.txt", "__ansible_vault": "vault_encrypted_data"}'
    obj = AnsibleJSONDecoder().decode(data)

    assert obj['__ansible_vault'] == 'vault_encrypted_data'
    assert obj['__ansible_unsafe'].data == '{{ template_dir }}/secrets.txt'

# Generated at 2022-06-13 06:43:39.576913
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs = {'__ansible_vault': 'foo'}
    result = decoder.object_hook(pairs)
    assert result._encrypted_value == 'foo'

    pairs = {'__ansible_unsafe': 'foo'}
    result = decoder.object_hook(pairs)
    assert str(result) == 'mutable foo'



# Generated at 2022-06-13 06:43:47.606339
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    json_str = '{"__ansible_vault": "vault_str", "__ansible_unsafe": "unsafe_str"}'
    json_str_expected = '{"__ansible_vault": "vault_str", "__ansible_unsafe": "unsafe_str"}'

    json_object = json.loads(json_str)
    AnsibleJSONEncoder._vaults = {}
    json_object_expected = json.loads(json_str_expected)

    assert json_object == json_object_expected

# Generated at 2022-06-13 06:43:55.171393
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook(None) is None

    result = decoder.object_hook({'__ansible_vault': 'VAULT_DATA', '__ansible_unsafe': 'not_so_unsafe'})
    assert result == {'__ansible_vault': 'VAULT_DATA', '__ansible_unsafe': 'not_so_unsafe'}

    result = decoder.object_hook({'__ansible_vault': {'vault_identifier': 'id', 'vault_data': 'vault_data', 'vault_version': 1}})
    assert result == {'__ansible_vault': {'vault_identifier': 'id', 'vault_data': 'vault_data', 'vault_version': 1}}

# Generated at 2022-06-13 06:44:02.147994
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    encoded = '''
    {
      "__ansible_vault": "ANSIBLE_VAULT;1.1;AES256"
    }
    '''
    decoded = json.loads(encoded, cls=AnsibleJSONDecoder)
    assert isinstance(decoded, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:44:11.627567
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    default_value = 'test_default_value'
    ansible_vault_value = 'test_ansible_vault_value'
    ansible_unsafe_value = 'test_ansible_unsafe_value'

    ajd = AnsibleJSONDecoder()
    values = {
        'default': default_value,
        '__ansible_vault': ansible_vault_value,
        '__ansible_unsafe': ansible_unsafe_value
    }

    result = ajd.object_hook(values)

    assert result['default'] == default_value
    assert result['__ansible_vault'] == ansible_vault_value

    assert result['__ansible_unsafe'] == ansible_unsafe_value
    # Assert the unsafe value is wrapped in _UnsafeString


# Generated at 2022-06-13 06:44:19.489650
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class _TestAnsibleJSONDecoder_object_hook(object):

        def __init__(self):
            self._vaults = AnsibleJSONDecoder._vaults

        def test_vault(self):
            json.JSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).decode("{'__ansible_vault': 'my_vault'}")
            assert 'default' in self._vaults

        def test_unsafe(self):
            import os
            obj = json.JSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).decode("{'__ansible_unsafe': '$HOME'}")
            assert obj.data == os.getenv("HOME")

    _TestAnsibleJSONDecoder_object_hook.test_vault()
    _

# Generated at 2022-06-13 06:44:31.410716
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import tempfile

    fd, tmpfile = tempfile.mkstemp(prefix='ansible_vault_', text=True, suffix='.txt')

# Generated at 2022-06-13 06:44:39.778662
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault = {'foo': 'vault_bar'}
    # vault data
    data = r'{"a": 1, "b": 2, "__ansible_vault": "YWJj"}'
    # create unsafe variable
    data = r'{"a": 1, "b": 2, "__ansible_unsafe": "YWJj"}'
    # create unsafe variable with vault
    data = r'{"a": 1, "b": 2, "__ansible_vault": "YWJj", "__ansible_unsafe": "YWJj"}'

    try:
        AnsibleJSONDecoder.set_secrets(vault)
        result = json.loads(data, cls=AnsibleJSONDecoder)
    except:
        pass

# Generated at 2022-06-13 06:44:49.015816
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    json_str = '{"message":"hello","__ansible_vault":"foobar","__ansible_unsafe":"baz"}'
    json_obj = json.loads(json_str, cls=AnsibleJSONDecoder)

    assert(json_obj['message'] == "hello")
    assert(json_obj['__ansible_vault'] == "foobar")
    assert(json_obj['__ansible_unsafe'] == "baz")


# Generated at 2022-06-13 06:45:00.424675
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    # test AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:45:11.594051
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_input = '{"__ansible_vault":"$ANSIBLE_VAULT;1.1;AES256\n32386439336564353562613638363331383539646430663364353466613830663939616238633239\n38333562616235626162306231613432326564663562613661653933616232656565393063336262\n34636261643439373331353235313162623266363037313533353733343835353637393361316236\n63343362323332653466303362393937303061396133333462643066\n"}'

# Generated at 2022-06-13 06:45:21.588030
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    result = decoder.object_hook({'__ansible_unsafe': 'value'})
    assert type(result) == AnsibleJSONEncoder.AnsibleUnsafeText
    assert result == 'value'

    result = decoder.object_hook({'__ansible_vault': 'value'})
    assert type(result) == AnsibleVaultEncryptedUnicode
    assert result.decrypted_vault_id == 'default'
    assert result == 'value'

    result = decoder.object_hook({'__ansible_vault': 'value', '__ansible_unsafe': 'value'})
    assert type(result) == AnsibleVaultEncryptedUnicode
    assert result.decrypted_vault_id == 'default'

# Generated at 2022-06-13 06:45:27.897125
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test __ansible_unsafe proxy object
    result = json.loads('{ "__ansible_unsafe": { "key": "value" } }', cls=AnsibleJSONDecoder)
    assert isinstance(result, AnsibleJSONDecoder.UnsafeProxy)
    assert result['key'] == 'value'

    # Test __ansible_vault encrypted string with vault password
    secrets = list('foo')

# Generated at 2022-06-13 06:45:36.866177
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = "dummy_secret"
    secret_file = "dummy_secret_file"
    AnsibleJSONDecoder.set_secrets(secrets=secret)

    encoder = AnsibleJSONEncoder()
    string_to_be_encrypted = "dummy_string"
    encrypted_value = encoder.encode(string_to_be_encrypted)
    decoder = AnsibleJSONDecoder()

    pairs = {'__ansible_vault': encrypted_value}
    assert decoder.object_hook(pairs) == AnsibleVaultEncryptedUnicode(encrypted_value)

# Generated at 2022-06-13 06:45:47.002358
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = {'vault_pass': 'password'}

    # Test encrypted value

# Generated at 2022-06-13 06:45:54.991144
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    vault_text = 'secret'
    vault_json = json.dumps([{'__ansible_vault': vault_text}], cls=AnsibleJSONEncoder)

    assert(vault_json == '[[{"__ansible_vault": "%s"}]]' % vault_text)

    result = decoder.decode(vault_json)
    assert(result[0][0]['__ansible_vault'] == vault_text)

    decoder.set_secrets(['secret'])
    result = decoder.decode(vault_json)
    assert(result[0][0]['__ansible_vault'] == vault_text)

# Generated at 2022-06-13 06:46:06.895443
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib

    v = VaultLib([('default', 'mysecret')])


# Generated at 2022-06-13 06:46:17.154181
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:46:20.509886
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class A:
        def __init__(self, b):
            self.b = b

    decoder = AnsibleJSONDecoder(object_hook = lambda pairs: A(pairs['b']))
    assert(decoder.decode('{"b":99}').b == 99)



# Generated at 2022-06-13 06:46:32.046855
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Arrange
    # Use AnsibleJSONEncoder to encode the data to test
    encoder = AnsibleJSONEncoder()
    encdata = {}
    # Encrypt a string
    encdata['__ansible_vault'] = encoder.encode({"__ansible_vault": "vaultdata"})
    # Wrap as unsafe
    encdata['__ansible_unsafe'] = encoder.encode({"__ansible_unsafe": "unsafedata"})
    # Dump to a string
    testdata = json.dumps(encdata)

    # Act
    decoder = AnsibleJSONDecoder()
    # Use the _ansible_object_hook method to decode testdata
    decdata = decoder.decode(testdata)

    # Assert
    # Check Vault
    # decdata will

# Generated at 2022-06-13 06:46:39.981083
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Unit test for method object_hook of class AnsibleJSONDecoder
    """
    # Initialize the instances
    vaults = { 'default': VaultLib(secrets=('Foo',)) }
    jsondecoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    jsondecoder._vaults = vaults

    # Test1: Test without vault and without unsafe
    pairs = {
        "key": "value"
    }

    # Invoke method object_hook
    result = jsondecoder.object_hook(pairs)

    # Test assertions
    assert 'key' in result
    assert result['key'] == 'value'

    # Test2: Test with vault and without unsafe
    pairs = {
        "__ansible_vault": "value"
    }

# Generated at 2022-06-13 06:46:54.296979
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    foo_dict = {'foo': 1}
    result = decoder.object_hook(foo_dict)
    assert result == foo_dict
    bar_dict = {'__ansible_unsafe': 1}
    result = decoder.object_hook(bar_dict)
    assert result == wrap_var(1)

# Generated at 2022-06-13 06:46:56.448381
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # FIX: actual assertion
    result = AnsibleJSONDecoder.object_hook({'__ansible_vault': ''})
    assert True


# Generated at 2022-06-13 06:47:07.143666
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class TestCase(object):
        def __init__(self, test_input, expected_result):
            self.test_input = test_input
            self.expected_result = expected_result


# Generated at 2022-06-13 06:47:15.734366
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Input string 
    test_str = '[{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;ANSIBLE_VAULT"},{"__ansible_unsafe": "ANSIBLE_UNSAFE"}]'

    # Using json loads to store the decoded string
    test_obj = json.loads(test_str, cls=AnsibleJSONDecoder)

    # Type of objects in the decoded string are 
    # AnsibleVaultEncryptedUnicode and dict
    assert isinstance(test_obj[0], AnsibleVaultEncryptedUnicode)
    assert isinstance(test_obj[1], dict)

# Generated at 2022-06-13 06:47:26.030045
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_pass = ['vault_key1', 'vault_key2']

# Generated at 2022-06-13 06:47:40.012339
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def hook(pairs):
        v = pairs['__ansible_vault']
        assert v.vault is not None
        return v.vault.decrypt(pairs)

    json_encoder = AnsibleJSONEncoder()
    json_decoder = AnsibleJSONDecoder()

    secrets = ['my_secret']
    json_decoder.set_secrets(secrets)

    result = {
        '__ansible_vault': json_encoder.encode('my_secret'),
    }
    assert json_decoder.object_hook(hook(result)) == secrets[0]


# Generated at 2022-06-13 06:47:47.647173
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    _vaults = {}

    def _object_hook(pairs):
        for key in pairs:
            value = pairs[key]

            if key == '__ansible_vault':
                value = AnsibleVaultEncryptedUnicode(value)
                if _vaults:
                    value.vault = _vaults['default']
                return value
            elif key == '__ansible_unsafe':
                return wrap_var(value)

        return pairs

    # test for __ansible_vault

# Generated at 2022-06-13 06:47:53.146007
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    tpairs = {'__ansible_vault': 'data'}
    tpairs_result = {'__ansible_vault': AnsibleVaultEncryptedUnicode('data')}
    assert decoder.object_hook(tpairs) == tpairs_result

# Generated at 2022-06-13 06:48:03.599536
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():    
    # Positive tests
    # - Create a class instance
    decoder = AnsibleJSONDecoder()
    # - Test a dictionary containing a vaulted string

# Generated at 2022-06-13 06:48:07.358488
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pairs = {'__ansible_vault': 'value', '__ansible_unsafe': 'value'}
    obj = AnsibleJSONDecoder.object_hook(pairs)
    if obj['__ansible_vault'] != 'value' or obj['__ansible_unsafe'] != 'value':
        raise ValueError("Failed")

# Generated at 2022-06-13 06:48:10.891919
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({'__ansible_vault': 'secret'})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    result = decoder.object_hook({'__ansible_unsafe': 'secret'})
    assert result.__ansible_unsafe__



# Generated at 2022-06-13 06:48:21.456985
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'pass'
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    data = u'{"__ansible_vault": "AES256_CBC_PKC%2B5H%2Bj5gSf5m5WM5m5l5%2Bt5g4V7p4Gw4%2Bj5gSf5m5WM5m5l5%2Bt5g4V7p4Gw4%2Bj5lA%3D%3D"}'
    res = decoder.decode(data)

# Generated at 2022-06-13 06:48:32.555553
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:46.023802
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create a dict with __ansible_vault key
    pairs = {'__ansible_vault': '{AES256}0SNSbzhaPknSq3wqD1xLcCfJY1TZj8WpX9paZlPcwehjzva6sWd2sLx/TJm1YGAf'}
    # Create an AnsibleJSONDecoder object
    decoder = AnsibleJSONDecoder()
    # Call object_hook on json.decoder.py for dict pairs
    ansible_vault_encrypted_unicode = decoder.object_hook(pairs)
    # Check if ansible_vault_encrypted_unicode is an AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 06:48:48.771441
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [u'list', u'of', u'secrets']
    Ansi

# Generated at 2022-06-13 06:49:00.578966
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import textwrap

    my_secrets = dict(foo='bar')
    AnsibleJSONDecoder.set_secrets(my_secrets)
    my_json_input = textwrap.dedent(u"""\
        {
            "__ansible_vault": "vault text",
            "__ansible_unsafe": "unsafe text"
        }
    """)
    my_decoded_result = {
        u'__ansible_unsafe': wrap_var(u"unsafe text"),
        u'__ansible_vault': u'vault text'
    }
    my_decoded_json = json.loads(my_json_input, cls=AnsibleJSONDecoder)
    assert my_decoded_result == my_decoded_json

# Generated at 2022-06-13 06:49:06.700442
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    test_cases = (
        ('{}', {}),
        ('{"__ansible_vault": "xxx"}', AnsibleVaultEncryptedUnicode('xxx')),
        ('{"__ansible_unsafe": "xxx"}', wrap_var('xxx')),
    )

    for test_case in test_cases:
        decoded_value = AnsibleJSONDecoder().decode(test_case[0])
        assert decoded_value == test_case[1]



# Generated at 2022-06-13 06:49:12.261171
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test with unsafe variable
    json_text = '{"__ansible_unsafe": "This is an unsafe variable"}'
    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook(decoder.decode(json_text))
    assert pairs['__ansible_unsafe'] == u'This is an unsafe variable'

    # Test with vault variable
    json_text = '{"__ansible_vault": "This is a vault variable"}'
    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook(decoder.decode(json_text))
    assert pairs['__ansible_vault'] == u'This is a vault variable'

# Generated at 2022-06-13 06:49:23.082917
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from collections import OrderedDict

    class MockVaultLib:
        load = lambda self, x: 'decrypted:' + x

    decoder = AnsibleJSONDecoder()
    decoder._vaults = {'default': MockVaultLib()}

    data = OrderedDict([
        ('__ansible_unsafe', '!vars something'),
        ('__ansible_vault', 'test'),
        ('__ansible_vault', 'test2')
    ])

    ret = decoder.object_hook(data)
    assert isinstance(ret['__ansible_unsafe'], AnsibleVaultEncryptedUnicode)
    assert isinstance(ret['__ansible_unsafe'].vault, MockVaultLib)

# Generated at 2022-06-13 06:49:34.864491
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    '''
    Test the object hook to return a new object
    '''

    import collections

    class TestVault(object):
        '''
        Test class for vault object hook
        '''
        pass

    class TestDict(collections.MutableMapping):
        '''
        Test class for dictionary object hook
        '''
        pass

    # Test object hook for AnsibleVaultEncryptedUnicode object
    test_decoder = AnsibleJSONDecoder()
    ansible_vault_unicode = test_decoder.object_hook({'__ansible_vault': 'test'})
    assert isinstance(ansible_vault_unicode, AnsibleVaultEncryptedUnicode)
    assert ansible_vault_unico

# Generated at 2022-06-13 06:49:44.006065
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var
    ansible_json_decoder = AnsibleJSONDecoder()
    vault_secret = "my vault secret"
    ansible_json_decoder.set_secrets(vault_secret)
    vault_secret_object = "__ansible_vault"
    test_dict = {vault_secret_object: "vault encrypted string"}
    result_dict = ansible_json_decoder.object_hook(test_dict)
    assert result_dict.keys() == [vault_secret_object]
    assert type(result_dict[vault_secret_object]) == AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:49:45.642983
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONEncoder().encode({'__ansible_vault': '123'}) == '{"__ansible_vault": "123"}'
    assert AnsibleJSONDecoder().decode('{"__ansible_vault": "123"}') == {u'__ansible_vault': '123'}

# Generated at 2022-06-13 06:49:50.226047
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:58.871656
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_text = """
        {
            "var_name_1": {
                "__ansible_vault": "ENC[something]"
            },
            "var_name_2": {
                "__ansible_vault": "ENC[something]",
                "__ansible_unsafe": true
            },
            "var_name_3": {
                "__ansible_unsafe": true
            },
            "var_name_4": "something"
        }
        """
    decoder = AnsibleJSONDecoder()
    decoded_results = json.loads(json_text, cls=decoder)

    assert isinstance(decoded_results['var_name_1'], AnsibleVaultEncryptedUnicode)
    assert decoded_results['var_name_1'] == 'ENC'
   

# Generated at 2022-06-13 06:50:07.337553
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Test without __ansible_vault
    json_string = '{"a": 1, "b": {"k1": "v1"}}'
    expected = {"a": 1, "b": {"k1": "v1"}}
    result = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert expected == result

    # Test with __ansible_vault
    json_string = '{"a": 1, "b": "__ansible_vault", "c": 2}'
    expected = {"a": 1, "b": AnsibleVaultEncryptedUnicode("__ansible_vault"), "c": 2}

# Generated at 2022-06-13 06:50:27.811582
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    enc = AnsibleJSONEncoder()
    dec = AnsibleJSONDecoder()
    secrets = {'default': 'foobar'}
    data = {'__ansible_vault': secrets['default']}
    secret = secrets['default']

    # Encode
    encrypted = enc.encode(data)

    # Set secrets
    AnsibleJSONDecoder.set_secrets(secrets)

    # Decode
    decrypted = dec.decode(encrypted)
    assert decrypted.vault.secrets[decrypted.vault.password_key] == secret
    assert decrypted.vault.secrets[decrypted.vault.password_key_name] == secret

# Generated at 2022-06-13 06:50:33.092329
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    add_to_builtins('my_var', 'my_value')

    decoder = AnsibleJSONDecoder()

    # Object with __ansible_vault attribute
    obj = decoder.object_hook({'__ansible_vault': 'ABC...', 'var': 'test'})
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj.vault.secrets == None

    # Object with __ansible_unsafe attribute
    obj = decoder.object_hook({'__ansible_unsafe': True, 'var': 'test'})
    assert obj.var == 'test'

    # Object without any attribute
    obj = decoder.object_hook({'var': 'test'})
    assert obj == {'var': 'test'}

    # Object with unknown attribute

# Generated at 2022-06-13 06:50:40.981031
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    obj = {'__ansible_unsafe': 'unsafe'}
    assert decoder.object_hook(obj) == wrap_var('unsafe')
    obj = {'__ansible_unsafe': 'unsafe', '__ansible_vault': 'vault'}
    assert decoder.object_hook(obj) == AnsibleVaultEncryptedUnicode('vault')



# Generated at 2022-06-13 06:50:51.604186
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.six import StringIO

    s = StringIO()

# Generated at 2022-06-13 06:51:03.233817
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({u'__ansible_vault': u'$ANSIBLE_VAULT;1.2;AES256;foo'}) == {u'__ansible_vault': AnsibleVaultEncryptedUnicode(u'$ANSIBLE_VAULT;1.2;AES256;foo')}
    assert decoder.object_hook({u'__ansible_vault': u'foo'}) == {u'__ansible_vault': AnsibleVaultEncryptedUnicode(u'foo')}
    assert decoder.object_hook({u'__ansible_unsafe': u'foo'}) == {u'__ansible_unsafe': u'foo'}

# Generated at 2022-06-13 06:51:16.089553
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_data = json.dumps("$ANSIBLE_VAULT;1.1;AES256\n35393532633062333636346635373033396534383364326565653564386231353862353734623066\n3366353635616134613839376536633566326539383533303739646234620a373637666138383264\n30666661383930383563306132653762646535623631656263623033323336636332643935636636\n39306666623563396133313161323265643636306466386463366162326634\n", cls=AnsibleJSONEncoder)
    data = '{ "__ansible_vault": %s }' % vault_data

# Generated at 2022-06-13 06:51:20.753722
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = '''
    {
        "__ansible_vault": "ansible-vault-value"
    }
    '''
    json_data = json.loads(test_data, cls=AnsibleJSONDecoder)
    assert isinstance(json_data['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert json_data['__ansible_vault'].vault is None

# Generated at 2022-06-13 06:51:34.903532
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Data to decode
    data = json.dumps({
        "key1": "value1",
        "key2": "value2",
        "__ansible_vault": "encrypted data",
        "__ansible_unsafe": 0,
    })
    # Initialize the class
    decoder = AnsibleJSONDecoder()
    # Set secrets for the decoder
    decoder.set_secrets(["password"])
    # Decode the data
    decoded = decoder.decode(data)
    # Check the result
    assert decoded['key1'] == "value1"
    assert decoded['key2'] == "value2"
    assert decoded['__ansible_vault'] == "encrypted data"
    assert decoded['__ansible_unsafe'] == 0
