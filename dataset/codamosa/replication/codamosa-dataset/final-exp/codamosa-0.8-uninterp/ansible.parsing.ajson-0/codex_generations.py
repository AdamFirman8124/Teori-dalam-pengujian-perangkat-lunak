

# Generated at 2022-06-13 06:41:33.114130
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Ansible's JSON Encoder writes AnsibleVaultEncryptedUnicode as
    # the string {"vault": "xxxx"}
    # but we want to be able to parse those too (as long as we have the vault password)
    vault_encoded = '{"__ansible_vault": "xxxx"}'
    vault_result = decoder.decode(vault_encoded)
    assert isinstance(vault_result, AnsibleVaultEncryptedUnicode)

    # in addition, we have the "__ansible_unsafe" object to represent things
    # which might not be safe to evaluate
    unsafe_encoded = '{"__ansible_unsafe": "{{some_unsafe_var}}"}'

# Generated at 2022-06-13 06:41:39.559236
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = '''{
        "__ansible_vault": "vault-encrypted string",
        "__ansible_unsafe": "unsafe string"
    }'''

    result = AnsibleJSONDecoder().object_hook(json.loads(json_data))
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert result['__ansible_vault'] == 'vault-encrypted string'
    assert result['__ansible_unsafe'] == wrap_var('unsafe string')

# Generated at 2022-06-13 06:41:43.124434
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    s = '{"__ansible_vault": "value"}'
    decoder = AnsibleJSONDecoder()
    result = decoder.decode(s)
    assert result == AnsibleVaultEncryptedUnicode('value')

# Generated at 2022-06-13 06:41:55.047189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_json_data = {'__ansible_vault': b'ansible_vault_encrypted_data'}
    assert AnsibleJSONDecoder.object_hook(ansible_vault_json_data) == ansible_vault_json_data

    ansible_vault_json_data = {'__ansible_vault': b'ansible_vault_encrypted_data', 'x': 'y'}
    assert AnsibleJSONDecoder.object_hook(ansible_vault_json_data) == ansible_vault_json_data

    ansible_unsafe_json_data = {'__ansible_unsafe': '{{password}}'}
    assert AnsibleJSONDecoder.object_hook(ansible_unsafe_json_data) == ansible_unsafe_json_data

# Generated at 2022-06-13 06:42:04.471665
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''Unit test for method object_hook of class AnsibleJSONDecoder.'''
    # Imported here to prevent circular import
    import yaml

    secrets = ['password']
    decoder = AnsibleJSONDecoder
    decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:42:15.619612
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # With no settings
    decoder = AnsibleJSONDecoder()
    json_str = '{"__ansible_vault": "AES256$JvzVfFkxC9XblIhW$2vnJ1d+t1HbVOGlfY8DpJg"}'
    result = decoder.decode(json_str)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    # With secrets set
    secrets = ['foo']
    decoder.set_secrets(secrets)
    json_str = '{"__ansible_vault": "AES256$JvzVfFkxC9XblIhW$2vnJ1d+t1HbVOGlfY8DpJg"}'
    result = decoder.decode

# Generated at 2022-06-13 06:42:21.983673
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    actual = decoder.object_hook({'__ansible_vault': 'test', '__ansible_unsafe': 'test'})
    assert 'test' == actual['__ansible_vault'].data
    assert 'test' == actual['__ansible_unsafe'].data



# Generated at 2022-06-13 06:42:34.799251
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_object = AnsibleJSONDecoder()

    # Test non-Ansible vault and unsafe related string return value
    test_dict = {'test_key': 'test_value'}
    result = test_object.object_hook(test_dict)
    assert result == test_dict

    # Test Ansible vault related string return value
    test_dict = {'__ansible_vault': 'ansible_vault_encrypted_string'}
    result = test_object.object_hook(test_dict)
    assert result.vault.secrets == []

    # Test Ansible unsafe related string return value
    test_dict = {'__ansible_unsafe': 'ansible_unsafe_string'}
    result = test_object.object_hook(test_dict)
    assert result.__class__.__name__

# Generated at 2022-06-13 06:42:42.500537
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # This test is only to check if given object is returned correctly
    # If object is AnsibleVaultEncryptedUnicode, this method should return AnsibleVaultEncryptedUnicode
    # NOT AnsibleVaultEncryptedUnicodeDict.
    json_decoder = AnsibleJSONDecoder()
    json_data = {'__ansible_vault': "test"}

    result = json_decoder.object_hook(json_data)

    assert isinstance(result, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:42:52.722266
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    e = AnsibleJSONEncoder()
    d = AnsibleJSONDecoder()

    # Test encoding a variable to json and decoding it back

    # Test variable containing nested dictionaries
    variable = {'foo': 'bar', 'bar': ['baz', {'baz': 'foobar', 'another_dict': {'inner': 3}}]}
    json_string = e.encode(variable)
    decoded_variable = d.decode(json_string)
    assert variable == decoded_variable

    # Test variable containing nested lists
    variable = [1, 2, 3, 4, 5, [4, 3, 2, 1, [2, 3, 4, 5, [5, 4, 3, 2, 1]]]]
    json_string = e.encode(variable)

# Generated at 2022-06-13 06:43:03.181979
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:09.775728
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {'some_vault_id': 'some_vault_password'}
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'test vault content'}) == AnsibleVaultEncryptedUnicode('test vault content')
    assert decoder.object_hook({'__ansible_unsafe': 'test unsafe content'}) == wrap_var('test unsafe content')
    assert decoder.object_hook({'not_recognized': 'test unrecognized content'}) == {'not_recognized': 'test unrecognized content'}



# Generated at 2022-06-13 06:43:15.842919
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = json.dumps(
        {
            '__ansible_vault': 'encoded_value',
            '__ansible_unsafe': 'encoded_value'
        }, cls=AnsibleJSONEncoder
    )

    decoded = json.loads(test_data, cls=AnsibleJSONDecoder)

    vault_loaded = isinstance(decoded.get('__ansible_vault'), AnsibleVaultEncryptedUnicode)
    assert vault_loaded, 'Should load AnsibleVaultEncryptedUnicode'

    unsafe_loaded = isinstance(decoded.get('__ansible_unsafe'), wrap_var)
    assert unsafe_loaded, 'Should load AnsibleUnsafeText'

# Generated at 2022-06-13 06:43:20.639252
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo']
    obj = {
        u'__ansible_vault': u'AnsibleVault text',
        u'__ansible_unsafe': u'not safe'
    }
    AnsibleJSONDecoder.set_secrets(secrets)
    assert 'AnsibleVault text' == json.dumps(obj, cls=AnsibleJSONDecoder)


# Generated at 2022-06-13 06:43:31.033446
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.vault import VaultLib

    vault_pass = '$6$yF6KjkhYbYzFZiCe$9.D5WjKvjnM5f5p5r3qh6YkYjYiM6.Z0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ0.bZ'
    vault = VaultLib(secrets=[vault_pass])

# Generated at 2022-06-13 06:43:38.783351
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'my_ansible_vault_password'
    secrets_encoded = secrets.encode('utf-8')

# Generated at 2022-06-13 06:43:49.811128
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleSequence
    import ansible.parsing.vault as vault
    import json
    secret = 'secret123'
    vault_lib = vault.VaultLib(secrets=[secret])
    ciphertext = vault_lib.encrypt('test')
    map_sequence = AnsibleSequence([ciphertext])
    json_dump = json.dumps(map_sequence, cls=AnsibleJSONEncoder)
    json_load = json.loads(json_dump, cls=AnsibleJSONDecoder)
    assert isinstance(json_load[0], AnsibleVaultEncryptedUnicode)
    assert json_load[0].vault == vault_lib

# Generated at 2022-06-13 06:43:53.608256
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    j = '{"__ansible_unsafe": "test", "__ansible_vault": "test"}'
    o = AnsibleJSONDecoder().decode(j)
    assert o["__ansible_vault"] == AnsibleVaultEncryptedUnicode('test')
    assert o["__ansible_unsafe"] == wrap_var('test')



# Generated at 2022-06-13 06:43:56.222219
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    result = AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'var'})
    assert result == wrap_var('var')

# Generated at 2022-06-13 06:44:09.813403
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).decode('''
    {
        "__ansible_vault": "!vault |\n            $ANSIBLE_VAULT;1.1;AES256\n            33366661626635666430633563373130386438376263653765303964303735313135666135643039\n            663231333437313936343139626364356166333039353063393000\n            ",
        "__ansible_unsafe": "${var_with_dollar_signs}"
    }
    ''') == {"__ansible_vault": 'Vaulted', "__ansible_unsafe": '${var_with_dollar_signs}'}

# Unit test

# Generated at 2022-06-13 06:44:18.734572
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
        AnsibleJSONDecoder._vaults = {
            'default': VaultLib(secrets=['vault'])
        }
        obj = AnsibleJSONDecoder.object_hook({
            '__ansible_vault': 'vault-encrypted-text',
            '__ansible_unsafe': 'unescaped-text',
            'not_encrypted': 'text'
        })

        assert obj['not_encrypted'] == 'text'
        assert obj['__ansible_vault'].vault == AnsibleJSONDecoder._vaults['default']
        assert obj['__ansible_vault'].translate() == 'vault-encrypted-text'
        assert obj['__ansible_unsafe'] == wrap_var('unescaped-text')

# Generated at 2022-06-13 06:44:28.700442
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    success = False
    try:
        ansible_json_decoder = AnsibleJSONDecoder()
        json_str = '{"__ansible_vault": "vault-value", "__ansible_unsafe": "unsafe-value"}'
        json_data = json.loads(json_str, cls=ansible_json_decoder)
        for key in json_data:
            value = json_data[key]
            if key == '__ansible_vault' and isinstance(value, AnsibleVaultEncryptedUnicode):
                success = True
                break
        assert success == True
    except Exception as e:
        assert False and "Exception encountered: {}".format(str(e))


# Generated at 2022-06-13 06:44:38.908867
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class DummyVaultLib:

        def __init__(self, secrets):
            pass

        def load(self, secret):
            return secret

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets('mypass')
    decoder.object_hook = AnsibleJSONDecoder.object_hook

    data = """
        {
            "__ansible_vault": "somevaultcontent",
            "somekey": "somevalue",
            "somesafe": true,
            "__ansible_unsafe": "someunsaftcontent"
        }
    """


# Generated at 2022-06-13 06:44:49.365482
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Test if method object_hook of class AnsibleJSONDecoder works as expected

    The object_hook method of class AnsibleJSONDecoder is given pairs of key/value as input.
    if key is '__ansible_vault', then object_hook method should return object of class AnsibleVaultEncryptedUnicode.
    if key is '__ansible_unsafe', then object_hook method should return the value wrapped in a AnsibleUnsafeText.
    if neither of the above, then the method should return the original input pairs.
    """
    ansible_vault_data = {"__ansible_vault": "abc"}
    assert isinstance(AnsibleJSONDecoder.object_hook(ansible_vault_data), AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:44:53.203547
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.six import PY2


# Generated at 2022-06-13 06:45:04.544591
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """This is a test for method object_hook of class AnsibleJSONDecoder"""
    # For unit test, we do not need any secrets to decrypt vault-encrypted strings.
    # Call load_vaultfile to initialize VaultLib for AnsibleJSONDecoder class
    AnsibleJSONDecoder.set_secrets(secrets=[])

    # Test for an encrypted string

# Generated at 2022-06-13 06:45:15.390242
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = ['secret1']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:45:24.273856
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    import unittest
    import inspect
    from ansible.module_utils.common._json_compat import json_loads, json_dumps

    class TestAnsibleJSONDecoder_object_hook(unittest.TestCase):

        def test_object_hook(self):

            # Create a list of dictionaries with nested lists of dictionaries
            list_of_dicts = []
            for i in range(1,4):
                dict_with_list = dict()
                dict_with_list['dict_name'] = 'dict%d' % i
                dict_with_list['dict_with_list'] = []
                for v in range(1,4):
                    dict_with_list['dict_with_list'].append({'dict_name': 'dict%d' % v})

# Generated at 2022-06-13 06:45:28.885312
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.json import from_json_response
    from ansible.parsing.vault import VaultLib

    # Test __ansible_unsafe
    test_cases = [
        dict(
            dict_input='{"__ansible_unsafe": "JSON string __ansible_ unsafe"}',
            dict_expected=dict(__ansible_unsafe='JSON string __ansible_ unsafe'),
        ),
        dict(
            dict_input='{"__ansible_unsafe": "JSON string __ansible_unsafe"}',
            dict_expected=dict(__ansible_unsafe='JSON string __ansible_unsafe'),
        ),
    ]


# Generated at 2022-06-13 06:45:40.393900
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # vault_data = {"vault_password": "foo"}

    enc_data = {"b": {"__ansible_vault": "ANSIBLE_VAULT;1.1;AES256\n3336383663373664386335326532346363656332343632653330393835663663613861346136620a323865363566666531353334366535313961356535396530301a6139323236363836653934353631323065343836353334653933623736373566383531630a3931363137666336393438356664653236366436353339376535643630373262633131383930386538333937"}}

# Generated at 2022-06-13 06:45:50.992164
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test data
    src_data = {
        '__ansible_vault': 'vault_test',
        '__ansible_unsafe': 'unsafe_test',
        'test': 'test'
    }

    # Expected result
    expected_data = {
        '__ansible_vault': 'vault_test',
        '__ansible_unsafe': 'unsafe_test',
        'test': 'test'
    }

    # Expected result of json.loads(json.dumps(expected_data))
    final_data = {
        '__ansible_vault': 'vault_test',
        '__ansible_unsafe': 'unsafe_test',
        'test': 'test'
    }

    # Convert JSON string to Python objects

# Generated at 2022-06-13 06:45:59.107701
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    secrets = 'password'
    vault = VaultLib(secrets=secrets)
    vault_str = AnsibleVaultEncryptedUnicode('string-to-encrypt', vault=vault)
    vault_dict = {'__ansible_vault': vault_str}
    vault_string = AnsibleJSONEncoder().encode(vault_dict)
    unsafe_str = wrap_var('raw-string')
    unsafe_dict = {'__ansible_unsafe': unsafe_str}
    unsafe_string = AnsibleJSONEncoder().encode(unsafe_dict)
    vault_uns

# Generated at 2022-06-13 06:46:09.135590
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
  json_data = '{"__ansible_vault":"vault value","__ansible_unsafe":"unsafe value"}'
  AnsibleJSONDecoder.set_secrets("ansible")
  myjson = AnsibleJSONDecoder()
  values = myjson.decode(json_data)
  assert len(values) == 2
  assert isinstance(values[0], AnsibleVaultEncryptedUnicode)
  assert values[0].vault is not None
  assert values[1] == "unsafe value"

# Generated at 2022-06-13 06:46:18.482682
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert json.loads(
        '{"foo": "bar", "__ansible_unsafe": "{{ foo }}"}',
        cls=AnsibleJSONDecoder
    ) == {'foo': 'bar', '__ansible_unsafe': 'bar'}

    assert json.loads(
        '{"__ansible_vault": "123456"}',
        cls=AnsibleJSONDecoder
    ) == {'__ansible_vault': '123456'}

    # test to ensure that the vault was properly initialized
    decoder = AnsibleJSONDecoder(object_hook=None)
    assert decoder.object_hook == decoder._vaults['default'].decrypt
    decoder.set_secrets(['password'])
    assert decoder._vaults['default'].secrets == ['password']

# Generated at 2022-06-13 06:46:33.346683
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    jsondecoder = AnsibleJSONDecoder(strict=True)
    jsondecoder.set_secrets("default_secrets")

# Generated at 2022-06-13 06:46:41.097494
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    This test ensures that:
    - ``AnsibleJSONDecoder.object_hook`` can transform the key __ansible_vault into an
      AnsibleVaultEncryptedUnicode object
    - ``AnsibleJSONDecoder.object_hook`` can transform the key __ansible_unsafe into an
      unsafe_proxy object
    """
    secrets = "password"
    secrets_data = '{"__ansible_vault": "vault_cipher_text"}'
    data = '{"__ansible_unsafe": "unsafe_value", "__ansible_vault": "vault_cipher_text"}'

    AnsibleJSONDecoder.set_secrets(secrets)
    vault_obj = json.loads(secrets_data, cls=AnsibleJSONDecoder)

    assert isinstance

# Generated at 2022-06-13 06:46:49.298519
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class DummyVault(object):
        pass

    my_vault = DummyVault()
    my_vault.decrypt = lambda x: 'Hello World'

    AnsibleJSONDecoder._vaults['test'] = my_vault

    dec = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': 'foo', '__ansible_unsafe': 10}
    result = dec.object_hook(pairs)

    assert result['__ansible_vault'] == 'Hello World'
    assert result['__ansible_unsafe'] == 10

# Generated at 2022-06-13 06:46:57.994366
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_str = 'test'
    vault_str = '$ANSIBLE_VAULT;1.1;AES256\n' \
                '313233343536373839303132333435363738393031323334353637383930313233342' \
                '1312e302e332e31393336393732\n' \
                '36646337613037306365326339396362353263323736383138346662363364376635\n' \
                '38643466393565323862366165303566363862333163333862663839\n'

    decoder = AnsibleJSONDecoder()

    # Test for AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:47:04.607158
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    x = json.loads(
        '{"foo": "bar", "__ansible_vault": "ENC[foo]", "__ansible_unsafe": "baz"}',
        cls=AnsibleJSONDecoder)
    assert x['foo'] == 'bar'
    assert x['__ansible_vault'].unencrypted_value == 'ENC[foo]'
    assert x['__ansible_unsafe'] == 'baz'



# Generated at 2022-06-13 06:47:07.987367
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    jsdec = AnsibleJSONDecoder()

    # Test ansible_unsafe
    pairs = dict(__ansible_unsafe='password')
    result = jsdec.object_hook(pairs)
    assert result == dict(__ansible_unsafe=b'password')


# Generated at 2022-06-13 06:47:20.331154
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:28.565013
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:32.604266
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_obj = { "__ansible_unsafe": "{{ password }}" }
    assert AnsibleJSONDecoder(json_obj) == { "__ansible_unsafe": "{{ password }}" }

# Generated at 2022-06-13 06:47:43.841722
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Define secret
    SECRET = 'testsecret'

    # Initialize Class
    cls = AnsibleJSONDecoder()

    # Define encrypted and non-encrypted data to test object_hook

# Generated at 2022-06-13 06:47:49.366841
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({}) == {}
    assert decoder.object_hook({'key': 'value'}) == {'key': 'value'}

    assert isinstance(decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}), AnsibleVaultEncryptedUnicode)
    assert isinstance(decoder.object_hook({'__ansible_unsafe': '$ANSIBLE_VAULT;1.1;AES256'}), wrap_var)

# Generated at 2022-06-13 06:48:01.655860
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.vault import VaultLib

    test_secrets = [ 'test_secret' ]
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(test_secrets)

    test_obj = { '__ansible_vault': 'foo' }
    test_res = decoder.object_hook(test_obj)
    assert test_res == { '__ansible_vault': 'foo' }
    assert hasattr(test_res['__ansible_vault'], 'vault')
    assert isinstance(test_res['__ansible_vault'].vault, VaultLib)
    # Verify that the decoder._vaults entry is correctly set
    assert hasattr(decoder, '_vaults')
    assert 'default' in decoder._vaults
   

# Generated at 2022-06-13 06:48:09.741092
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:20.383315
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = b'$ANSIBLE_VAULT;1.1;AES256\n356130643939646234626536316439636434303865393635653361386133626463373362396130\n306430616335383734373932376366373939623334396231653230363539373738633436336530\n336564653436643836336461376234613239333462653164396364343038653936356533613861\n336264633733623961300a'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets([secret])


# Generated at 2022-06-13 06:48:32.003984
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:48:44.080511
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils import common as module_common

    # set secret for vault
    module_common.AnsibleJSONDecoder.set_secrets('password')

    # __ansible_vault
    json_str = '{"foo": "bar", "vault": {"__ansible_vault": "1", "__ansible_vault_output": "ANSIBLE_VAULT;1.1;AES256\n34653666333161363761346166333435386463386164363832386462306364366239386163666364\n66396437633134343635316231323132646238383331643536336365346531316161303865656662\n37\n"}}'

# Generated at 2022-06-13 06:48:55.412364
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder()

    # Encrypted value
    assert d.object_hook({'__ansible_vault': '1'}) == AnsibleVaultEncryptedUnicode('1')

    # Safe value
    assert d.object_hook({'__ansible_unsafe': '1'}) == wrap_var('1')

    # Not an encrypted value
    assert d.object_hook({'__ansible_other': '1'}) == {'__ansible_other': '1'}



# Generated at 2022-06-13 06:49:03.079748
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets(None)


# Generated at 2022-06-13 06:49:08.314411
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder()

    assert d.object_hook({'__ansible_unsafe': 'value'}) == wrap_var('value')

    assert isinstance(d.object_hook({'__ansible_vault': 'value'}),
                      AnsibleVaultEncryptedUnicode)


# Backwards compat
ansible_json = AnsibleJSONEncoder()

# Generated at 2022-06-13 06:49:15.773621
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys
    if sys.version_info[0] == 2:
        bytes_str = 'bytes'
    else:
        bytes_str = 'str'

    # object_hook with __ansible_vault
    json_str = json.dumps({
        '__ansible_vault': {
            'vault_id': 'default',
            'vault_password': '$ANSIBLE_VAULT;1.1;AES256',
            'value': 'cipher'
        }
    })
    decoded_json = AnsibleJSONDecoder().decode(json_str)
    assert isinstance(decoded_json['__ansible_vault'], AnsibleVaultEncryptedUnicode)

    # object_hook with __ansible_vault, vault_password not encrypted
    json_str = json

# Generated at 2022-06-13 06:49:17.073670
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert True

# Generated at 2022-06-13 06:49:21.926475
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'dummy'}) \
        == AnsibleVaultEncryptedUnicode('dummy')
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'dummy'}) \
        == wrap_var('dummy')

# Generated at 2022-06-13 06:49:30.261508
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_vars = ['secret_var']
    AnsibleJSONDecoder.set_secrets(secret_vars)
    obj = dict(vault_key={"__ansible_vault":  "Ynl0ZSBhcnJheQ=="})
    new_obj = AnsibleJSONDecoder().object_hook(obj)
    assert new_obj["vault_key"].decrypt() == "byte array"


# Generated at 2022-06-13 06:49:44.207163
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret']
    secrets_list = ['secret1', 'secret2', 'secret3']
    secrets_dict = {'default': 'secret', 'other': 'secret'}

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

    # check working with a list
    decoder.set_secrets(secrets_list)
    ok = decoder.object_hook({'__ansible_vault': 'vault'})
    assert ok.vault.secrets == secrets_list

    # check working with a dictionary
    decoder.set_secrets(secrets_dict)
    ok = decoder.object_hook({'__ansible_vault': 'vault'})
    assert ok.vault.secrets == secrets_dict['default']

    # check working with

# Generated at 2022-06-13 06:49:55.082102
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault = VaultLib(secrets=['secret'])
    decoder = AnsibleJSONDecoder()
    test_dict = {'__ansible_vault': 'hello'}
    test_dict2 = {'__ansible_unsafe': 'hello'}

    class SomethingElse(object):
        def __init__(self, value):
            self.value = value

    test_dict_ext = {'__ansible_vault': 'hello', '__ansible_unsafe': SomethingElse('hello')}

    class Vault(object):
        def __init__(self, vault):
            self.vault = vault

    class VaultEncryptedUnicode(object):
        def __init__(self, value):
            self.value = value


# Generated at 2022-06-13 06:50:05.501036
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    json_file = '''{
        "foo": "bar",
        "__ansible_vault": "AQAAAAEAAABbQ0NOSUZBUWpJekFpQmhNdzhDWlNYQ2tVZkRzRjhVNE9jY3pZM3dzbzFBPT0K",
        "__ansible_unsafe": "{{ a }}"
    }'''
    decoded_dict = json.loads(json_file, cls=AnsibleJSONDecoder, encoding='utf-8')
    assert isinstance(decoded_dict, dict)

# Generated at 2022-06-13 06:50:28.696523
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    """Testing method 'object_hook' of class AnsibleJSONDecoder"""

    # initialize test variables
    ansible_vault = "{'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n'}"
    ansible_unsafe = "{'__ansible_unsafe': '$ANSIBLE_VAULT;1.1;AES256\n'}"

    # initialize test object
    decoder = AnsibleJSONDecoder()

    # test object_hook with ansible_vault
    result = decoder.object_hook(json.loads(ansible_vault))
    assert isinstance(result.__ansible_vault, AnsibleVaultEncryptedUnicode) is True

    # test object_hook with ansible_unsafe

# Generated at 2022-06-13 06:50:33.943038
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = {'key1': 'value1', 'key2': 'value2', 'key3': {'k3': 'v3'}, '__ansible_vault': "this is a vault", '__ansible_unsafe': {'secret_key': 'secret_value'}}
    decoded = AnsibleJSONDecoder.object_hook(d)
    assert(isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode))
    assert(isinstance(decoded['__ansible_unsafe'], dict))
    assert(decoded['__ansible_unsafe']['secret_key'] == 'secret_value')
    assert(decoded['key1'] == 'value1')
    assert(decoded['key2'] == 'value2')

# Generated at 2022-06-13 06:50:44.192424
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    arg_pairs = {'__ansible_vault': 'sometext',
                 '__ansible_unsafe': 'something'}
    test_instance = AnsibleJSONDecoder()
    result = test_instance.object_hook(arg_pairs)

    assert result is not None
    assert isinstance(result, dict)
    assert isinstance(result.get('__ansible_vault'), AnsibleVaultEncryptedUnicode)
    assert isinstance(result.get('__ansible_unsafe'), unicode)
    assert result.get('__ansible_unsafe') == 'something'


# Generated at 2022-06-13 06:50:48.659566
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def assert_value(expected, value):
        assert expected == value, \
            "Object hook: expected %s, got %s" % (expected, value)

    # string
    assert_value("test", json.loads('"test"', cls=AnsibleJSONDecoder))

    # dict with one key and value
    assert_value({u'test': u'value'}, json.loads('{"test":"value"}', cls=AnsibleJSONDecoder))

    # dict with more keys and values
    assert_value({u'test': u'value', u'key': u'more'}, json.loads('{"test":"value", "key":"more"}', cls=AnsibleJSONDecoder))

    # dict with vault

# Generated at 2022-06-13 06:50:56.686157
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:51:05.867056
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Setup
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    jd = AnsibleJSONDecoder()

    # AnsibleVaultEncryptedUnicode
    res = jd.object_hook({'__ansible_vault': '1234'})
    assert type(res) is AnsibleVaultEncryptedUnicode

    # AnsibleUnsafeText
    res = jd.object_hook({'__ansible_unsafe': '1234'})
    assert type(res) is AnsibleUnsafeText

    # Unknown key
    res = jd.object_hook({'key': 'value'})
    assert res['key'] == 'value'

    # No keys
    res = jd.object_hook({})
    assert res == {}

    # Empty
    res = jd

# Generated at 2022-06-13 06:51:15.971557
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from tests.unit.parsing.yaml.test_dumper import FakeRole
    from tests.unit.parsing.yaml.test_vault import FakeVaultSecret

    fake_role = FakeRole()
    secret = FakeVaultSecret()

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secret)

    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;test_password\n366234346137613234'}) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.2;AES256;test_password\n366234346137613234')

# Generated at 2022-06-13 06:51:23.338353
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for decrypting vaulted value
    decoder = AnsibleJSONDecoder()
    decoder._vaults = {'default': VaultLib(secrets=['vault_secret'])}