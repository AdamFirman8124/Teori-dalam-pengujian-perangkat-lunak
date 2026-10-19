

# Generated at 2022-06-13 06:41:39.451984
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = {
        "__ansible_vault": "foo",
        "__ansible_unsafe": "bar"
    }

    # Test that a vault will be created if none were provided
    decoder = AnsibleJSONDecoder()
    decoded = decoder.object_hook(test_data)
    assert(decoded['__ansible_vault'] == 'foo')
    assert(decoded['__ansible_vault'].vault)
    assert(decoded['__ansible_unsafe'] == 'bar')
    assert(decoded['__ansible_unsafe'].__class__.__name__ == 'str')

    # Test that a vault is provided if one exists (and it's used)
    decoder = AnsibleJSONDecoder(object_hook=decoder.object_hook)
    dec

# Generated at 2022-06-13 06:41:48.884113
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for function object_hook
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:41:58.043479
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:42:12.159546
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import collections
    # Create an object
    obj = {
        'a': 'aaa',
        'b': 'bbb',
        'c': 'ccc',
        'd': {
            '__ansible_vault': 'This is an encrypted message',
            '__ansible_unsafe': '__ansible_unsafe',
            'e': 'eee'
        }
    }

    # Use the object_hook for AnsibleJSONDecoder
    obj = AnsibleJSONDecoder().object_hook(obj)

    # Test whether the output is dict
    assert isinstance(obj, dict)

    # Test __ansible_vault
    assert obj['d']['__ansible_vault'].vault
    assert obj['d']['__ansible_vault'].vault.secrets == list()

# Generated at 2022-06-13 06:42:20.311564
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # test decryption of AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 06:42:34.145990
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import wrap_var

    pairs = {}
    pairs[u'__ansible_unsafe'] = u'foo'
    pairs[u'__ansible_vault'] = u'bar'
    pairs[u'hello'] = u'world'

    expected = {}
    expected[u'__ansible_unsafe'] = wrap_var(u'foo')
    expected[u'__ansible_vault'] = AnsibleVaultEncryptedUnicode(u'bar')
    expected[u'hello'] = u'world'

    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:42:46.758650
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import copy
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = "SECRET"

    # Test with variables wrapped with __ansible_vault
    json_input = [
        {
            "__ansible_vault": "Some vault value"
        },
        {
            "__ansible_vault": "foo"
        }
    ]
    decoder = AnsibleJSONDecoder()

    # Test with __ansible_vault
    vault_json_decoded = copy.deepcopy(json_input)
    vault_json_decoded[0] = {"__ansible_vault": AnsibleVaultEncryptedUnicode("Some vault value")}

# Generated at 2022-06-13 06:42:55.531461
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Build a mock pairs dict.
    pairs = dict()
    pairs['__ansible_vault'] = '123456789'
    pairs['__ansible_unsafe'] = 'testing unsafe'

    # Call the object_hook method of the AnsibleJSONDecoder class and compare the results.
    ansiblejsondec = AnsibleJSONDecoder()
    result = ansiblejsondec.object_hook(pairs)

    assert( isinstance(result, dict) )

    assert( result['__ansible_vault'].is_encrypted() )

    assert( isinstance(result['__ansible_unsafe'], wrap_var) )

# Generated at 2022-06-13 06:43:04.705108
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:19.040658
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = VaultSecret([])
    secret._password = 'test_password'

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets([secret])

    assert '__ansible_unsafe' in decoder.object_hook({'__ansible_unsafe':'test_unsafe'})
    assert '__ansible_vault' in decoder.object_hook({'__ansible_vault':'test_vault'})

# Generated at 2022-06-13 06:43:30.595732
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:34.958944
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = json.loads('{"__ansible_vault": "{VAULT|2.0|AES256|6e73b6d03e6f8d6a937e1ad99f06d90a8dfdd3da1df2f67c}"}', cls=AnsibleJSONDecoder)
    assert(isinstance(data, AnsibleVaultEncryptedUnicode))


# Generated at 2022-06-13 06:43:46.934574
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        {'id': 'default',
         'vault_id': 'default',
         'password': 'p@$$w0rd'
        }
        ]
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()

    # Test for encrypted string

# Generated at 2022-06-13 06:43:54.869579
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys
    if sys.version_info[:2] != (2, 7):
        return
    import unittest

    SECRET = 'j9eYG!_#E(S%Jjuu'

# Generated at 2022-06-13 06:44:08.731767
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    AnsibleJSONDecoder._vaults['default'] = VaultLib(secrets=['fake_password'])

# Generated at 2022-06-13 06:44:20.488218
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    jp = """{
    "__ansible_unsafe": "{{ test_var }}",
    "__ansible_vault": "AQAAAAEAbQAAAAAABYkyd+x6Uc1wUf0GjKP6C"
}"""

    acut = AnsibleJSONDecoder()
    ecut = AnsibleJSONDecoder()
    ecut.set_secrets(['default_pwd'])
    jd = json.loads(jp, cls=acut)
    assert jd['__ansible_unsafe'] == '{{ test_var }}'
    assert jd['__ansible_vault'] == 'AQAAAAEAbQAAAAAABYkyd+x6Uc1wUf0GjKP6C'


# Generated at 2022-06-13 06:44:21.119487
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pass

# Generated at 2022-06-13 06:44:30.800298
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = {
        "__ansible_vault": "my_encrypted_string",
        "__ansible_unsafe": "my_unsafe_string"
    }
    decoder = AnsibleJSONDecoder()
    decoded = decoder.object_hook(test_data)

    assert isinstance(decoded, dict)
    assert isinstance(decoded["__ansible_vault"], AnsibleVaultEncryptedUnicode)
    assert decoded["__ansible_vault"].vault is None
    assert isinstance(decoded["__ansible_unsafe"], wrap_var)
    assert decoded["__ansible_unsafe"].as_bytes() == "my_unsafe_string"

# Generated at 2022-06-13 06:44:39.247868
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # arrange
    json_stream = """{ "test": "{{test}}" }"""

    # act
    decoded = AnsibleJSONDecoder().decode(json_stream)

    # assert
    assert decoded['test'] == "{{test}}"

    # arrange
    json_stream = """{ "test": "$${test}" }"""

    # act
    decoded = AnsibleJSONDecoder().decode(json_stream)

    # assert
    assert decoded['test'] == "$${test}"

    # arrange
    json_stream = """{ "test": "$${{test}}" }"""

    # act
    decoded = AnsibleJSONDecoder().decode(json_stream)

    # assert
    assert decoded['test'] == "$${test}"



# Generated at 2022-06-13 06:44:49.678365
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault_data = 'my secret data'
    vault_key = 'my secret key'
    decoder.set_secrets([vault_key])

    true_dict = {}

# Generated at 2022-06-13 06:44:55.344956
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pairs = {'__ansible_vault': 'mypassword'}
    ansible_json_decoder = AnsibleJSONDecoder()
    res = ansible_json_decoder.object_hook(pairs)
    assert isinstance(res, AnsibleVaultEncryptedUnicode)

    pairs = {'__ansible_unsafe': 'mypassword'}
    ansible_json_decoder = AnsibleJSONDecoder()
    res = ansible_json_decoder.object_hook(pairs)
    assert isinstance(res, AnsibleUnsafeText)

# Generated at 2022-06-13 06:45:02.577554
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo']
    decoder = AnsibleJSONDecoder
    decoder.set_secrets(secrets)
    assert decoder.object_hook({'__ansible_vault': 'bar'}) == AnsibleVaultEncryptedUnicode('bar')
    assert decoder.object_hook({'__ansible_unsafe': 'bar'}) == wrap_var('bar')
    assert decoder.object_hook({'foo': 'bar'}) == {'foo': 'bar'}

# Generated at 2022-06-13 06:45:13.684426
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:18.327679
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': '1234'}) == {'__ansible_vault': '1234'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': '1234'}) == {'__ansible_unsafe': '1234'}



# Generated at 2022-06-13 06:45:27.279184
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:45:35.838688
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # test for case __ansible_vault
    data = {'__ansible_vault': 'test', 'k1': 'v1'}
    assert decoder.object_hook(data) == AnsibleVaultEncryptedUnicode('test')
    # test for case __ansible_unsafe
    data = {'__ansible_unsafe': {'k1': 'v1'}}
    assert decoder.object_hook(data) == wrap_var({'k1': 'v1'})

# Generated at 2022-06-13 06:45:45.693409
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:53.967603
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Verify that __ansible_vault and __ansible_unsafe fields
    # are unwrapped and/or decrypted by object_hook, without
    # changing any other fields

    import unittest

    class AnsibleJSONDecoderTestCase(unittest.TestCase):
        def test_ansible_vault(self):
            from ansible.parsing.vault import VaultLib

            secret = "this is a super secret"
            vault_id = "secrets"
            vault = VaultLib([(vault_id, secret)])

            # Encrypted data

# Generated at 2022-06-13 06:46:00.972787
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.errors import AnsibleError

    json_data = b'{"__ansible_vault": "vault_data"}'
    expected_value = AnsibleVaultEncryptedUnicode("vault_data")
    actual_value = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert actual_value['__ansible_vault'] == expected_value

    ansible_error_raised = False
    try:
        json_data = b'{"__ansible_vault": "vault_data"}'
        AnsibleJSONDecoder().object_hook(json.loads(json_data))
    except AnsibleError:
        ansible_error_raised = True
    assert ansible_error_raised

# Generated at 2022-06-13 06:46:14.748821
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Importing another way so we can import AnsibleJSONEncoder.
    import ansible.module_utils.common.json
    encoder = ansible.module_utils.common.json.AnsibleJSONEncoder()
    decoder = AnsibleJSONDecoder()
    # Placeholder for __ansible_unsafe values
    test_unsafe_value = 'test_unsafe_value'
    # Placeholder for __ansible_vault values
    test_vault_value = 'test_vault_value'

    # Test plain object
    test_object = {'hello': 'world'}
    assert decoder.object_hook(test_object) == test_object

    # Test handling of __ansible_unsafe objects
    test_unsafe_object = {'__ansible_unsafe': test_unsafe_value}

# Generated at 2022-06-13 06:46:21.745534
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import datetime
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    decoder = AnsibleJSONDecoder()

    # value is not a dict
    assert decoder.object_hook(1) == 1

    # key != '__ansible_vault' and key != '__ansible_unsafe'
    assert decoder.object_hook({'k': 'v'}) == {'k': 'v'}

    # key == '__ansible_vault' and not value
    assert decoder.object_hook({'__ansible_vault': None}) == {}

    # key == '__ansible_vault' and value is string

# Generated at 2022-06-13 06:46:36.694045
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder._vaults = {
        'vault_id': VaultLib(secrets=['test_secret'])
    }

    pairs = {
        '__ansible_vault': 'test_value',
        '__ansible_vault_id': 'vault_id',
        '__ansible_unsafe': 'test_value'
    }

    pairs = decoder.object_hook(pairs)

    assert isinstance(pairs['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert pairs['__ansible_vault'].vault == decoder._vaults['vault_id']

    assert isinstance(pairs['__ansible_unsafe'], wrap_var)

# Generated at 2022-06-13 06:46:41.676504
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    AnsibleJSONDecoder.set_secrets(['secrets'])
    decoded = AnsibleJSONDecoder().object_hook({
            '__ansible_unsafe': 'unsafe',
            '__ansible_vault': 'vault'
        })

    assert decoded['__ansible_vault'].value == 'vault'
    assert decoded['__ansible_vault'].vault.secrets == ['secrets']
    assert decoded['__ansible_unsafe'] == wrap_var('unsafe')

# Generated at 2022-06-13 06:46:45.728808
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    kwargs = {'object_hook': AnsibleJSONDecoder.object_hook}
    assert AnsibleJSONDecoder(*kwargs, **kwargs).object_hook == AnsibleJSONDecoder.object_hook

# Generated at 2022-06-13 06:46:48.343615
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pass

# Generated at 2022-06-13 06:46:57.736467
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    text = '''
    {
        "__ansible_vault": "vault_value",
        "__ansible_unsafe": "AnsibleUnsafeText",
        "key": "value"
    }
    '''
    from ansible.parsing.vault import VaultLib

    result = json.loads(text, cls=AnsibleJSONDecoder)
    assert isinstance(result, dict)
    assert len(result) == 3
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(result['__ansible_vault'].vault, VaultLib)
    assert isinstance(result['__ansible_unsafe'], wrap_var)
    assert result['key'] == 'value'

# Generated at 2022-06-13 06:47:07.490582
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test with __ansible_vault
    pairs = {'__ansible_vault': 'value'}
    output = decoder.object_hook(pairs)

    assert(isinstance(output, AnsibleVaultEncryptedUnicode))
    assert(output == 'value')

    # Test with __ansible_unsafe
    pairs = {'__ansible_unsafe': 'value'}
    output = decoder.object_hook(pairs)

    assert(output == wrap_var('value'))

    # Test with no match
    pairs = {'unknown': 'value'}
    output = decoder.object_hook(pairs)

    assert(output == pairs)

# Generated at 2022-06-13 06:47:17.795638
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    import unittest.mock
    # test a simple string
    pairs = {'a': 'b'}
    pairs_result = pairs
    assert pairs_result == AnsibleJSONDecoder.object_hook(pairs)

    # test an unsafe value
    pairs = {'__ansible_unsafe': 42}
    pairs_result = wrap_var(42)
    assert pairs_result == AnsibleJSONDecoder.object_hook(pairs)

    # test a vault value
    pairs = {'__ansible_vault': 'c'}
    pairs_result = AnsibleVaultEncryptedUnicode('c')
    assert pairs_result == AnsibleJSONDecoder.object_hook(pairs)
    assert pairs_result.vault != None

    # test a vault value with a vault context

# Generated at 2022-06-13 06:47:26.939042
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:47:41.433544
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os

    test_file = os.path.join(os.path.dirname(__file__), 'data', 'json_quoted_ansible_unsafe.json')

    with open(test_file, 'rb') as f:
        json_data = json.load(f, cls=AnsibleJSONDecoder)

    # The test data is loaded from data/json_quoted_ansible_unsafe.json
    assert json_data['a'] == '|-\na: 1\nb: 2\n'
    assert json_data['b'] == ['Zm9v', 'YmFy']
    assert json_data['c']['d'] == 'Zm9v'

    # The test data is loaded from data/json_ansible_unsafe.json

# Generated at 2022-06-13 06:47:50.438861
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {
        "__ansible_vault": "foo",
        "__ansible_unsafe": "bar",
        "__ansible_vault2": "baz"
    }
    secrets = ['secret1']
    decoder = AnsibleJSONDecoder.set_secrets(secrets)
    data2 = decoder.decode(json.dumps(data))

    assert data2["__ansible_vault"] == AnsibleVaultEncryptedUnicode(data["__ansible_vault"])
    assert data2["__ansible_vault"].vault == VaultLib(secrets=secrets)
    assert data2["__ansible_vault2"] == data["__ansible_vault2"]

# Generated at 2022-06-13 06:48:02.028952
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = {
        'test_object': {
            'vault_key': '1234',
            '__ansible_vault': '123456789',
            '__ansible_unsafe': '__unsafe__',
        }
    }
    # json_data -> {'test_object': {'vault_key': '1234', '__ansible_vault': '123456789', '__ansible_unsafe': '__unsafe__'}}
    result = AnsibleJSONDecoder(json_data).object_hook(json_data)
    # type of result -> dict
    # result -> {'test_object': {'vault_key': '1234', '__ansible_vault': '123456789', '__ansible_unsafe': AnsibleUnsafeText('__uns

# Generated at 2022-06-13 06:48:07.434488
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    AnsibleJSONDecoder.set_secrets(['test'])
    test_data = json.loads(
        """
        [
            {
                "contents": "my_secret",
                "__ansible_vault": "my_secret"
            }
        ]
        """,
        cls=AnsibleJSONDecoder
    )
    test_value = test_data[0]['contents']

    assert isinstance(test_value, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:48:15.962965
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs1 = decoder.object_hook({'__ansible_vault': 'vault1'})
    isinstance(pairs1, AnsibleVaultEncryptedUnicode)
    assert pairs1.data == 'vault1'

    pairs2 = decoder.object_hook({'__ansible_unsafe': 'unsafe'})
    isinstance(pairs2, AnsibleVaultEncryptedUnicode)
    assert pairs2.data == 'unsafe'

    pairs3 = decoder.object_hook({'k': 'v'})
    assert pairs3 == {'k': 'v'}

# Generated at 2022-06-13 06:48:30.464650
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import tempfile
    import os

    # These tests use real vault contents

# Generated at 2022-06-13 06:48:36.039096
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo']
    json_decoder = AnsibleJSONDecoder()
    json_decoder.set_secrets(secrets)
    test_data = {'__ansible_vault': 'foo'}
    result = json_decoder.object_hook(test_data)
    assert result.vault.secrets == secrets
    assert result.vault.secrets != ['bar']

# Generated at 2022-06-13 06:48:43.372698
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(['__ansible_vault', '__ansible_unsafe'])
    assert decoder.object_hook({'__ansible_vault': 'value'}) == AnsibleVaultEncryptedUnicode('value')
    assert decoder.object_hook({'__ansible_unsafe': 'value'}) == wrap_var('value')

# Generated at 2022-06-13 06:48:54.587095
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping


# Generated at 2022-06-13 06:48:56.819626
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    my_json_decoder = AnsibleJSONDecoder()
    my_json_decoder.object_hook({'__ansible_vault': 'some_value'})

# Generated at 2022-06-13 06:49:07.507428
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Assert that AnsibleVaultEncryptedUnicode is returned, when provided a
    # key named __ansible_vault
    value = '$ANSIBLE_VAULT;1.2;AES256;secrets'
    pairs = {'__ansible_vault': value}
    hook = AnsibleJSONDecoder.object_hook(pairs)
    assert isinstance(hook, AnsibleVaultEncryptedUnicode)

    # Assert that AnsibleVaultEncryptedUnicode is returned, when provided a
    # key named __ansible_vault, and provided a vault object
    value = '$ANSIBLE_VAULT;1.2;AES256;secrets'
    pairs = {'__ansible_vault': value}
    vault = VaultLib()

# Generated at 2022-06-13 06:49:19.968506
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    assert AnsibleJSONDecoder().object_hook({'__ansible_vault': '$value', '__ansible_unsafe': '$value'}) == {'__ansible_vault': '$value', '__ansible_unsafe': '$value'}

# Generated at 2022-06-13 06:49:25.187253
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.common._collections_compat import MutableMapping

    def test_function(input, output):
        assert isinstance(output, MutableMapping)
        assert output['__ansible_vault'] == 'test'

    decoder = AnsibleJSONDecoder(object_hook=test_function)

    json_string = '{"__ansible_vault": "test"}'
    res = decoder.decode(json_string)

# Generated at 2022-06-13 06:49:35.199392
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {'__ansible_vault': u'$AES128$Ec4A4uDvI8mGnfHq3.dLAXcteDEQu2M7VuwHtRi7Vv0=', '__ansible_unsafe': 2}
    decoded = AnsibleJSONDecoder(data)
    assert decoded.__class__.__name__ == 'AnsibleVaultEncryptedUnicode'
    assert decoded.vault.__class__.__name__ == 'VaultLib'
    assert decoded.vault.decrypt(decoded) == 'test_value'


# Generated at 2022-06-13 06:49:44.307775
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:55.163618
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:05.577188
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """Tests object_hook method of class AnsibleJSONDecoder"""

# Generated at 2022-06-13 06:50:13.701996
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # preparing test data
    data = '{__ansible_vault: $ANSIBLE_VAULT;1.1;AES256;ansible\n 383861353061353765333063636239616132633661323835346561623963343363356138356562\n 33386331323639663464326231386334613541316463373961613064646262646164326331633466\n 623164613237643234633365303961396562306566353631643965336230356536663032353131\n 383439626266633235633434633163346665303361303032316436\n}'

    # creating test object
    ansiblejsondecoder = AnsibleJSONDecoder(data)

# Generated at 2022-06-13 06:50:29.062463
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class TestAnsibleJSONDecoder(AnsibleJSONDecoder):
        _vaults = {}
        def __init__(self, *args, **kwargs):
            kwargs['object_hook'] = self.object_hook
            super(TestAnsibleJSONDecoder, self).__init__(*args, **kwargs)

    secret = 'foo'
    TestAnsibleJSONDecoder.set_secrets({"default":secret})

    data = {"__ansible_vault":"foo"}
    data_out = TestAnsibleJSONDecoder().decode(json.dumps(data))
    assert isinstance(data_out, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:50:33.742045
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test data
    data = '{"__ansible_vault": "vault", "__ansible_unsafe": "unsafe"}'
    secrets = ('secrets', )

    # Set secrets
    AnsibleJSONDecoder.set_secrets(secrets)
    # Initialize object AnsibleJSONDecoder
    decoder = AnsibleJSONDecoder()
    # Retrieve object from JSON string
    object = decoder.decode(data)

    assert object['__ansible_vault'].vault.secrets == secrets
    assert isinstance(object['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert object['__ansible_unsafe'] == 'unsafe'


# Generated at 2022-06-13 06:50:46.710847
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    ansible_vault = '$ANSIBLE_VAULT;1.1;AES256;ansible\n6339363236636439383338356138663564633065643334633332376139626166363833303462\n6235333065313935636538316366633034386533373636373934323033303736653230633533\n3830373537356665353766353436643436396466326565636366653039633536613438633663\n3432366235666133376434336133316266643939366134386265306465366664653763376339\n653330316334\'\n'
    ansible_unsafe = 'ansible_unsafe'


# Generated at 2022-06-13 06:51:10.792439
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = dict(__ansible_vault='test_value')
    test_result = dict(__ansible_vault=AnsibleVaultEncryptedUnicode('test_value'))

    decoder = AnsibleJSONDecoder()
    assert test_result == decoder.object_hook(test_data)


__all__ = ['AnsibleJSONDecoder', 'AnsibleJSONEncoder']

# Generated at 2022-06-13 06:51:20.317854
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:51:34.497705
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
  ansible_vault_value = '$ANSIBLE_VAULT;1.1;AES256\n35363262313861346262333962363131643232656661643938353133373235316233636337396534\n30336665396531363164613961626136366364363963386134353638613035666432343231613665\n3161393464666361643339363664316262\n'