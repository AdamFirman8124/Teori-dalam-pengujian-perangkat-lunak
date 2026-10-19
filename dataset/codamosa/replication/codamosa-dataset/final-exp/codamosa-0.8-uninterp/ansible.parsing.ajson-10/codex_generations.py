

# Generated at 2022-06-13 06:41:33.447976
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['vault_password']

# Generated at 2022-06-13 06:41:43.286104
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    ansible_vault_encrypted_unicode = '$ANSIBLE_VAULT;1.1;AES256'
    json_input = {
        '__ansible_vault': ansible_vault_encrypted_unicode,
        '__ansible_unsafe': True,
        '__ansible_string_conversion_action': 'ignore'
    }

    decoder = AnsibleJSONDecoder()
    output = decoder.object_hook(json_input)

    assert isinstance(output['__ansible_vault'], AnsibleVaultEncryptedUnicode), \
        "the object in the ansible_vault key is not an AnsibleVaultEncryptedUnicode type object"


# Generated at 2022-06-13 06:41:47.525855
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """Unit test for AnsibleJSONDecoder._object_hook
    """
    ad = AnsibleJSONDecoder()
    assert(ad.object_hook({'__ansible_unsafe':'test'}) == wrap_var('test'))

# Generated at 2022-06-13 06:41:53.388342
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    j_str = '{"__ansible_vault": "mypasswd"}'
    decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets(['mypasswd'])
    res = decoder.decode(j_str)
    assert isinstance(res, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:41:59.399933
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'ansible']
    AnsibleJSONDecoder.set_secrets(secrets)

    data = '''{
        "__ansible_vault": "AAABBB",
        "__ansible_unsafe": "AAAAAA"
    }'''
    d = json.loads(data, cls=AnsibleJSONDecoder)

    assert isinstance(d['__ansible_vault'], AnsibleVaultEncryptedUnicode), \
        "__ansible_vault is not AnsibleVaultEncryptedUnicode object"
    assert isinstance(d['__ansible_unsafe'], wrap_var), \
        "__ansible_unsafe is not wrap_var object"

    return True

# Generated at 2022-06-13 06:42:04.623893
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data = {"__ansible_vault": "test", "__ansible_unsafe": "test"}
    for k in data:
        assert k in decoder.object_hook(data)


# Generated at 2022-06-13 06:42:16.941534
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml import objects
    secret = 'testsecret'

# Generated at 2022-06-13 06:42:31.207854
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # check the text decryption
    decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets(['test'])

# Generated at 2022-06-13 06:42:37.759152
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:50.193703
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Exercise method object_hook of class AnsibleJSONDecoder with a decrypted value
    #  that is a plain string; assert that we get back the same plain string
    secrets = 'hunter2'
    debug_json_decoder = AnsibleJSONDecoder.AnsibleJSONDecoder()
    debug_json_encoder = AnsibleJSONEncoder.AnsibleJSONEncoder()
    debug_json_decoder.set_secrets(secrets)
    plaintext_string = "foobar"
    plaintext_string_json = json.dumps(plaintext_string)
    plaintext_string_decrypted = json.loads(plaintext_string_json, cls=debug_json_decoder.AnsibleJSONDecoder)
    assert plaintext_string == plaintext_string_decrypted

    # Exercise method object_hook of

# Generated at 2022-06-13 06:42:59.947664
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = AnsibleJSONDecoder()
    res = obj.object_hook({'__ansible_unsafe':"test"})
    assert(res == wrap_var("test"))

    res = obj.object_hook({'__ansible_vault':"test"})
    assert(isinstance(res, AnsibleVaultEncryptedUnicode))
    assert(isinstance(res.vault, VaultLib))
    assert(res.vault.secrets is None)

    obj.set_secrets(["test"])
    res = obj.object_hook({'__ansible_vault':"test"})
    assert(isinstance(res, AnsibleVaultEncryptedUnicode))
    assert(res.vault.secrets == ["test"])


# Generated at 2022-06-13 06:43:04.039930
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for a simple string
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'hello'}) == AnsibleVaultEncryptedUnicode('hello')

    # Test for a complex object
    complex_data = {'key': 'value', 'key2': 'value2'}
    expected = {'key': 'value', 'key2': AnsibleVaultEncryptedUnicode('value2')}
    assert AnsibleJSONDecoder.object_hook({'key': 'value', 'key2': {'__ansible_vault': 'value2'}}) == expected

# Generated at 2022-06-13 06:43:09.401703
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {'default_password': 'foo'}
    AnsibleJSONDecoder.set_secrets(secrets)
    decoded = json.loads('{"__ansible_vault": "puppet"}', cls=AnsibleJSONDecoder)
    assert decoded == AnsibleVaultEncryptedUnicode('puppet')
    assert decoded.vault == AnsibleJSONDecoder._vaults['default']
    decoded = json.loads('{"__ansible_unsafe": 42}', cls=AnsibleJSONDecoder)
    assert decoded == wrap_var(42)

# Generated at 2022-06-13 06:43:22.276862
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = None

    # Test
    result = decoder.object_hook({'__ansible_vault': 'encrypted_str'})
    assert result == 'encrypted_str'
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault is None

    result = decoder.object_hook({'__ansible_unsafe': 'unsafe_str'})
    assert isinstance(result, wrapper)
    assert result._wrapped == 'unsafe_str'

    result = decoder.object_hook({'__ansible_vault': 'encrypted_str', '__ansible_unsafe': 'unsafe_str'})
    assert result == 'encrypted_str'

# Generated at 2022-06-13 06:43:32.302318
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:38.000245
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    import re

    json_string = '{"__ansible_vault": "BASE64_ENCODED_TEXT"}'

    decoded = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert isinstance(decoded, AnsibleVaultEncryptedUnicode)

    json_string = '{"__ansible_unsafe": "var"}'

    decoded = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert re.match(r'.*UNSAFE_VAR.*', decoded)

# Generated at 2022-06-13 06:43:49.761146
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # test for __ansible_vault
    secrets = '$ANSIBLE_VAULT;1.1;AES256\n6361323764316532623462643762346164313935343834623365386635363664656234666231336333\n65653936386137313435623135303733373230663337393763336539\n'
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:43:56.678365
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # test without vault initialization
    json_data = '{"__ansible_unsafe": {}, "__ansible_vault": "123"}'
    expected_result = {'__ansible_unsafe': {}, '__ansible_vault': '123'}
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert decoded_data == expected_result
    json_data = '{"__ansible_unsafe": {}, "__ansible_vault": "123", "a": "b"}'
    expected_result = {'__ansible_unsafe': {}, '__ansible_vault': '123', 'a': 'b'}
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert dec

# Generated at 2022-06-13 06:44:10.115598
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.errors import AnsibleError
    from ansible.module_utils.common._collections_compat import Mapping

    assert not isinstance(json.loads(json.dumps('string')), Mapping)

    obj_hook_result = AnsibleJSONDecoder().object_hook({
        '__ansible_vault': 'vault',
    })
    assert isinstance(obj_hook_result, AnsibleVaultEncryptedUnicode)
    assert obj_hook_result.vault is None
    assert AnsibleJSONDecoder._vaults == {}

    AnsibleJSONDecoder.set_secrets('test')
    obj_hook_result = AnsibleJSONDecoder().object_hook({
        '__ansible_vault': 'vault',
    })

# Generated at 2022-06-13 06:44:18.046584
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    sample_vault = '$ANSIBLE_VAULT;1.1;AES256;foo\nbar==\n'
    vault = AnsibleVaultEncryptedUnicode(sample_vault)
    vault.vault = VaultLib(secrets='password')

    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': sample_vault}) == vault
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 123}) == wrap_var(123)

# Generated at 2022-06-13 06:44:30.112721
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from unittest.mock import patch

    # Set up mocks
    secrets = ['secret1', 'secret2']
    vault_lib = VaultLib(secrets=secrets)
    vault_lib.decrypt = lambda x: x
    type(vault_lib).secrets = ['secret1']

    with patch.multiple('ansible.parsing.vault.VaultLib', decrypt=vault_lib.decrypt, secrets=vault_lib.secrets):
        decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:44:35.902384
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder('{"__ansible_vault": "ansible"}')
    result = decoder.object_hook({'__ansible_vault': 'ansible'})
    assert 'ansible' in str(result)
    assert 'AnsibleVaultEncryptedUnicode' == result.__class__.__name__
    assert type(result.vault) is VaultLib

# Generated at 2022-06-13 06:44:42.536177
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    plaintext_value = 'Just plain text value'

# Generated at 2022-06-13 06:44:49.290189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoded_data = json.loads(json.dumps(dict(__ansible_unsafe='unsafe')), cls=AnsibleJSONDecoder)

    assert decoded_data == {'__ansible_unsafe': 'unsafe'}
    assert isinstance(decoded_data['__ansible_unsafe'], wrap_var)



# Generated at 2022-06-13 06:45:00.514613
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """Unit test for AnsibleJSONDecoder.object_hook.

    """
    class MyJSONDecoder(AnsibleJSONDecoder):

        def __init__(self):
            pass

        def object_hook(self, pairs):
            return pairs

    class MyTestObj(object):

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return 'MyTestObj({0!r})'.format(self.name)

        def __eq__(self, other):
            return type(self) == type(other) and self.name == other.name

    testobj1 = MyTestObj('A')
    testobj2 = MyTestObj('B')
    testobj3 = MyTestObj('C')

    # Test '__ansible_vault'
    decoder

# Generated at 2022-06-13 06:45:07.687209
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # decode string to dict
    enc = '{"__ansible_vault": "dGVzdA==\n","__ansible_unsafe": true}'
    decoded = json.loads(enc, cls=AnsibleJSONDecoder)

    # ensure object hook set vault object
    assert decoded['__ansible_vault'].vault is not None

    # ensure object hook unwrap unsafe variables
    assert decoded['__ansible_unsafe'] == True

# Generated at 2022-06-13 06:45:18.142556
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.constructor import AnsibleBaseConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 06:45:27.257431
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 06:45:34.058217
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({}) == {}

    assert AnsibleJSONDecoder.object_hook(
        {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;abc123',
         '__ansible_vault_version': 1}) == \
        AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;abc123')

# Generated at 2022-06-13 06:45:44.645758
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader

    # Create data loader with vault password to read vault file
    loader = DataLoader()
    vault_file = 'tests/test_data/vault-test-file.yml'
    vault_passwd = 'vault_password'
    loader.set_vault_secrets([(vault_file, vault_passwd)])

    # Create a vault lib instance with vault password
    vault = VaultLib(secrets=[vault_passwd])

    # Test Ansible Vault

# Generated at 2022-06-13 06:45:53.895263
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.module_utils._text import to_text

    d = to_text(AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).decode('{"__ansible_unsafe":"1234567","__ansible_vault":"1234567"}'))

    assert wrap_var("1234567") == d["__ansible_unsafe"]
    assert isinstance(d["__ansible_vault"], AnsibleVaultEncryptedUnicode)
    assert VaultLib() == d["__ansible_vault"].vault

# Generated at 2022-06-13 06:46:02.405180
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secret = '$ANSIBLE_VAULT;1.1;AES256;'
    secret += '330680527777326a75686e6e59464f4d49776c3644423146684738534a7a7553627031526d7a486e6e'
    secret += '6b3278506c36723656530a6d5a5a69397673587431537a684c4e4652476a63306669633834576c734'
    secret += 'd4a4a42785549694976424c4b6b4f7891363745394833797a0a353571615975505468414a4944714e'

# Generated at 2022-06-13 06:46:16.144766
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = '{"__ansible_vault": "ENC[AES256,abcdefg]","__ansible_unsafe":"meh"}'
    json_data = json.loads(data, cls=AnsibleJSONDecoder)
    decrypted = json_data['__ansible_vault']
    assert isinstance(decrypted, AnsibleVaultEncryptedUnicode)
    assert decrypted == 'ENC[AES256,abcdefg]'
    assert json_data['__ansible_unsafe'] == 'meh'

    # special case for http://docs.python.org/2/library/json.html#json.JSONDecoder
    data = '{"a": "b", "c": "d", "e": {}}'

# Generated at 2022-06-13 06:46:18.839237
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')

# Generated at 2022-06-13 06:46:33.761846
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Generate a mock secret and some mock data
    secret = 'ABCD1234'
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;test_key\n346234234623462346234623462346234623462346234623462346234623462\n3423462346234623462346234623462346234623462346234623462342346234\n'}
    pairs_wrap = {'__ansible_unsafe': AnsibleJSONEncoder(secret).encode(pairs)}

    # Test that object_hook decrypt the encrypted data
    secret_dict = AnsibleJSONDecoder.object_hook(AnsibleJSONDecoder(), pairs)

# Generated at 2022-06-13 06:46:38.598320
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # test for an unchanged pair
    unchanged_pair = {'foo': 'bar'}
    decoded = decoder.object_hook(unchanged_pair)
    assert decoded == unchanged_pair

    # test for an unsafe pair
    unsafe_pair = {'__ansible_unsafe': 'hello world'}
    decoded = decoder.object_hook(unsafe_pair)
    assert decoded != unsafe_pair



# Generated at 2022-06-13 06:46:52.920854
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    secrets = ["hunter2"]

    # Execute
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:47:00.820254
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        {'vault_id': 'default', 'password': 'secret'}
    ]
    encoder = AnsibleJSONEncoder()

    with open('tests/unit/parsing/vault/test_vault.txt') as input_file:
        vault_text = input_file.read()
        vault_text_json = encoder.encode(vault_text)
        vault_dict = {'__ansible_vault': vault_text_json}
        decoder = AnsibleJSONDecoder()
        decoder.set_secrets(secrets)
        vault_obj = decoder.decode(encoder.encode(vault_dict))
        vault_obj = decoder.object_hook(vault_obj)


# Generated at 2022-06-13 06:47:09.871072
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_text = 'foo'
    plaintext = 'bar'
    enc_plaintext = AnsibleVaultEncryptedUnicode(secret_text)
    AnsibleJSONDecoder.set_secrets(secret_text)

    sample_unsafe = {
        '__ansible_unsafe': plaintext,
    }
    decoded_unsafe = AnsibleJSONDecoder().object_hook(sample_unsafe)
    # Check if unsafe item is wrapped
    assert isinstance(decoded_unsafe, wrap_var)
    assert decoded_unsafe.unwrap() == plaintext

    sample_vault = {
        '__ansible_vault': secret_text,
    }
    decoded_vault = AnsibleJSONDecoder().object_hook(sample_vault)
    # Check if vault text is decrypted

# Generated at 2022-06-13 06:47:19.257207
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_json = '''{
        "__ansible_unsafe": {
            "additional_item": "__ansible_unsafe value"
        },
        "__ansible_vault": "vault_value"
    }'''

    decoder = AnsibleJSONDecoder()
    result = decoder.decode(test_json)

    # Check "__ansible_unsafe" variable
    assert(result.get('__ansible_unsafe') == {
        'additional_item': '__ansible_unsafe value'
    })

    # Check "__ansible_vault" variable
    assert(result.get('__ansible_vault').value == 'vault_value')

# Generated at 2022-06-13 06:47:29.090203
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:37.721076
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({"__ansible_unsafe": "UNSAFE_VALUE"}) == wrap_var("UNSAFE_VALUE")
    assert decoder.object_hook({"__ansible_vault": "VAULT_VALUE"}) == AnsibleVaultEncryptedUnicode("VAULT_VALUE")
    assert decoder.object_hook({"key": "value"}) == {"key": "value"}



# Generated at 2022-06-13 06:47:43.652815
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = '''
    {
        "__ansible_vault": "this is encrypted"
    }
   '''

    cls = AnsibleJSONDecoder
    cls.set_secrets(['password'])

    # TODO: we need a more good way to test this
    assert (cls.object_hook(json.loads(data))['__ansible_vault']).decode('utf-8') == 'this is encrypted'

# Generated at 2022-06-13 06:47:46.950684
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_obj = '{"__ansible_vault": "value"}'
    decoded_json = json.loads(test_obj, cls=AnsibleJSONDecoder)

    assert isinstance(decoded_json, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:47:55.809212
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({"__ansible_vault": "test_ansible_vault"}) == AnsibleVaultEncryptedUnicode("test_ansible_vault")
    assert AnsibleJSONDecoder.object_hook({"__ansible_unsafe": "test_ansible_unsafe"}) == wrap_var("test_ansible_unsafe")
    assert AnsibleJSONDecoder.object_hook({"foo": "bar"}) == {"foo": "bar"}

# Generated at 2022-06-13 06:48:06.837111
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:48:13.285011
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class JSONTest(object):
        def test_safe(self):
            test_obj = {
                'unencrypted': 'value',
                '__ansible_unsafe': {
                    'encrypted': 'value'
                }
            }
            test_data = json.dumps(test_obj)

            decoded = json.loads(test_data, cls=AnsibleJSONDecoder)
            direct_decoded = json.loads(test_data)

            assert decoded == direct_decoded

        def test_vault(self):
            test_obj = {
                'unencrypted': 'value',
                '__ansible_vault': 'vaulted_value'
            }
            test_data = json.dumps(test_obj)

            # This will raise AnsibleParserError
            decoded = json.loads

# Generated at 2022-06-13 06:48:21.175364
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    enc = AnsibleJSONEncoder()
    dec = AnsibleJSONDecoder()

    # Test VAULT
    secrets = [u'foo']
    dec.set_secrets(secrets)

    obj = {'vault': u'foo'}
    assert dec.object_hook({'__ansible_vault': enc.encode(obj)}) == obj

    # Test UNSAFE
    obj = {'unsafe': {"password": "foo", "hashed": False}}
    assert dec.object_hook({'__ansible_unsafe': enc.encode(obj)}) == obj

# Generated at 2022-06-13 06:48:32.388048
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['testsecret']
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:48:43.474391
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Set up
    ansible_vault = {'__ansible_vault': 'vaulted_value',
                     'key2': 'value2'}
    ansible_unsafe = { '__ansible_unsafe': 'unsafe_value',
                     'key2': 'value2'}

    # Execute
    ansible_vault_result = AnsibleJSONDecoder().object_hook(ansible_vault)
    ansible_unsafe_result = AnsibleJSONDecoder().object_hook(ansible_unsafe)

    # Test
    assert ansible_vault_result == AnsibleVaultEncryptedUnicode('vaulted_value')
    assert ansible_unsafe_result == wrap_var('unsafe_value')

# Generated at 2022-06-13 06:48:48.102654
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pass

# Generated at 2022-06-13 06:48:52.958794
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder().object_hook({
        '__ansible_unsafe': 'secret',
        '__ansible_vault': 'secret',
    }) == {
        '__ansible_unsafe': 'secret',
        '__ansible_vault': 'secret',
    }



# Generated at 2022-06-13 06:49:01.183009
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # __ansible_vault
    # >>> import json
    # >>> json.loads('{"__ansible_vault": "@9!$aA1"}', cls=AnsibleJSONDecoder)
    # u'@9!$aA1'
    jstr = '{"__ansible_vault": "@9!$aA1"}'
    cls = AnsibleJSONDecoder
    cls.set_secrets(['@9!$aA1'])
    assert u'@9!$aA1' == json.loads(jstr, cls=cls)

    # __ansible_unsafe
    # >>> import json
    # >>> json.loads('{"__ansible_unsafe": "{{ lookup(\\"file\\", \\"/etc/passwd\\") }}"}', cls=Ans

# Generated at 2022-06-13 06:49:09.625196
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml import objects
    import sys

    if sys.version_info[0] < 3:
        # In Python 2.x, the assertRaises() context manager does not return
        # the exception instance, and that makes it difficult to test
        # the exception message.
        import pytest
        function = pytest.mark.skip(reason='Python 2.x does not return the exception instance in assertRaises()')(AnsibleJSONDecoder.object_hook)
    else:
        function = AnsibleJSONDecoder.object_hook

    with pytest.raises(objects.AnsibleVaultError) as excinfo:
        function(dict(__ansible_vault='abc'))
    assert 'attempted to read vault variable' in str(excinfo.value)


# Generated at 2022-06-13 06:49:14.253772
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [{'vault_id': 'default', 'secret': 'my_secret'}]
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

    vault_value = decoder.object_hook({'__ansible_vault': "some vault value"})
    assert isinstance(vault_value, AnsibleVaultEncryptedUnicode)

test_AnsibleJSONDecoder_object_hook()


# Generated at 2022-06-13 06:49:19.989715
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret

    #test data
    data = {'test': 42, '__ansible_vault': 'd3JvdXAgdGVzdAo=', '__ansible_unsafe': 'test'}
    encoded_data = json.dumps(data, cls=AnsibleJSONEncoder, indent=2)

    #making sure that object hook is able to decode data with __ansible_vault and __ansible_unsafe in it
    decoded_data = json.loads(encoded_data, cls=AnsibleJSONDecoder)

    assert data['__ansible_vault'] == decoded_data['__ansible_vault']
    assert data['__ansible_unsafe'] == decoded_data['__ansible_unsafe']

# Generated at 2022-06-13 06:49:27.403603
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test unsafe variable
    data = '{"__ansible_unsafe": "vars"}'
    result = AnsibleJSONDecoder().decode(data)
    assert result == wrap_var('vars')

    # Test vault
    _vaults = {'default': None}
    AnsibleJSONDecoder._vaults = _vaults
    data = '{"__ansible_vault": "vault"}'
    result = AnsibleJSONDecoder().decode(data)
    assert result == AnsibleVaultEncryptedUnicode('vault')
    assert result.vault is None

    # Test vault with secrets
    _vaults = {}
    AnsibleJSONDecoder._vaults = _vaults
    secrets = 'secrets'
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:49:41.854719
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pdb; pdb.set_trace()
    data = {
        "__ansible_vault": "!vault |\n$ANSIBLE_VAULT;1.2;AES256;default\n66373935363761656236653735346130386536303135373962356138633662643534663533383936\n62326539646539613639636239363338346262366331613038396566383033326565653538323430\n38626435383330653237383335\n",
        "__ansible_unsafe": "!unsafe 'some_str'",
    }
    json_str = json.dumps(data)

# Generated at 2022-06-13 06:49:49.758021
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'test': 'value'}) == {'test': 'value'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'value'}) == wrap_var('value')
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'value'}).vault.secrets == []
    assert AnsibleJSONDecoder({'__ansible_unsafe': 'value'}).decode() == wrap_var('value')


# Generated at 2022-06-13 06:49:56.306135
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test = AnsibleJSONDecoder()
    data = {'__ansible_vault': 'some encrypted text'}
    result = test.object_hook(data)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.encode('utf-8') == 'some encrypted text'

    data = {'__ansible_unsafe': True}
    result = test.object_hook(data)
    assert isinstance(result, bool) and result is True


# Generated at 2022-06-13 06:50:11.878296
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault = '$ANSIBLE_VAULT;1.1;AES256\n363737383736666465373737666531363165373564373565643734356466383337663635643635\n316331613664353438376164396332376234643364636634396336396265393036363833613230\n346562393336353635613639643666343065663035\n'
    json_str = '{"__ansible_vault": "%s"}' % vault

    # Decoded JSON for above JSON string

# Generated at 2022-06-13 06:50:18.870828
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    d = decoder.object_hook({'__ansible_unsafe': "'test'", '__ansible_vault': 'test'})
    assert isinstance(d['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert d['__ansible_unsafe'] == wrap_var("'test'")

# Generated at 2022-06-13 06:50:33.079785
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:50:41.439915
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # simple test for _object_hook
    # create ansible-vault object
    secret = AnsibleVaultEncryptedUnicode('SECRET')
    test_kv = {'__ansible_vault': 'SECRET'}
    tmp = AnsibleJSONDecoder.object_hook(test_kv)
    assert len(tmp) == 1
    for key in tmp:
        assert key == '__ansible_vault'
        assert tmp[key] == secret

# Generated at 2022-06-13 06:50:51.936670
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    v = VaultLib(secrets='password')
    d = AnsibleJSONDecoder()
    d.set_secrets('password')

    decoded = json.loads('{ "__ansible_vault": "asdf" }', cls=AnsibleJSONDecoder)
    assert(decoded == AnsibleVaultEncryptedUnicode('asdf'))
    assert(decoded.vault == v)

    v = wrap_var('foo')
    assert(v.__class__.__name__ == 'AnsibleUnsafeText')

    decoded = json.loads('{ "__ansible_unsafe": "asdf" }', cls=AnsibleJSONDecoder)
    assert(decoded == v)
    assert(decoded.__class__.__name__ == 'AnsibleUnsafeText')

# Generated at 2022-06-13 06:50:58.811427
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Tests if AnsibleJSONDecoder.object_hook() correctly creates
    an instance of AnsibleVaultEncryptedUnicode class, when `__ansible_vault`
    key is present in the dict, or an instance of AnsibleUnsafeText class
    when the `__ansible_unsafe` key is present in the dict.
    """

    data = '{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;foo" }'
    decoded = AnsibleJSONDecoder().decode(data)
    assert isinstance(decoded, AnsibleVaultEncryptedUnicode)
    assert isinstance(decoded.vault, VaultLib)

    data = '{"__ansible_unsafe": "foo"}'
    decoded = AnsibleJSONDecoder().decode(data)

# Generated at 2022-06-13 06:51:08.444427
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:51:19.301684
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_str = u'{"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": {"__ansible_unsafe": true, "x": "X", "y": "Y", "z": "Z"}, "h": "H"}'
    json_obj = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": {"__ansible_unsafe": True, "x": "X", "y": "Y", "z": "Z"}, "h": "H"}
    ansible_json_obj = json.loads(json_str, cls=AnsibleJSONDecoder)

    # Note: The order of the key-value

# Generated at 2022-06-13 06:51:29.517795
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create input.
    input = {"__ansible_vault": "AES256"}
    # Create the AnsibleJSONDecoder object.
    decoder = AnsibleJSONDecoder()
    # Run the method object_hook of class AnsibleJSONDecoder.
    actual_result = decoder.object_hook(input)
    # Get the expected result.
    expected_result = AnsibleVaultEncryptedUnicode("AES256")
    # Test if the actual and expected results are equal.
    assert actual_result == expected_result
