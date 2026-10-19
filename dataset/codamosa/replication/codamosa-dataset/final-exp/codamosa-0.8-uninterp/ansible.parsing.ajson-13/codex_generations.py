

# Generated at 2022-06-13 06:41:30.144771
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;ABCDEF\nblablabla\nblablabla\nblablabla'}) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;ABCDEF\nblablabla\nblablabla\nblablabla')

# Generated at 2022-06-13 06:41:39.907548
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    code = "test code"

# Generated at 2022-06-13 06:41:47.521898
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest

    test_data = [
        ({'__ansible_vault': 'test'}, AnsibleVaultEncryptedUnicode('test')),
        ({'__ansible_unsafe': 'test'}, wrap_var('test'))
    ]

    for input, output in test_data:
        d = AnsibleJSONDecoder()
        assert d.object_hook(input) == output

    with pytest.raises(KeyError):
        d = AnsibleJSONDecoder()
        d.object_hook({'unknown_key': 'test'})

# Generated at 2022-06-13 06:41:57.525283
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'01234567890123456789012345678901']

    # Make Input 'expected'

# Generated at 2022-06-13 06:42:12.031164
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:42:20.237704
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_pass = "password1"
    vault_string = """(FP.W8pq)#b'rqw2!=f@D(n&k/hT/a(wm+a/G?;,}N`*(^Kz'\
c]_8s|&(?*Z@>)|v>TzCh[8i(A_'yj*sH\^W$s]9hYj_iR#{v>`W'p~3t@}-t^F'=\
Wd8Hnq<'KB`o)mj_E[a=:1,n5gSzDxFj5n>p@XCY=,]p<@N!"""
    secrets = [vault_pass]
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:42:25.333987
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    secret = 'secret' * 8
    decoder.set_secrets([secret])

    assert decoder.object_hook({}) == {}

    assert isinstance(decoder.object_hook({'__ansible_vault': 'vault'}), AnsibleVaultEncryptedUnicode)

    assert decoder.object_hook({'__ansible_unsafe': "ansible_host={{ inventory_hostname }}"}) == wrap_var("ansible_host={{ inventory_hostname }}")


# Generated at 2022-06-13 06:42:32.128544
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = 'text'
    json_str = json.dumps({'__ansible_vault': secret}, cls=AnsibleJSONEncoder)
    json_decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets([secret])
    assert json_decoder.decode(json_str)['__ansible_vault'] == secret

# Generated at 2022-06-13 06:42:37.204284
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        {
            'key': 'secret-key',
            'password': 'secret-password',
            'src': '/path/to/secret-key'
        }
    ]

    json_str = '{"__ansible_vault": "ENCRYPTED STRING", "__ansible_unsafe": "UNSAFE"}'
    decoded = json.loads(json_str)
    assert decoded == {'__ansible_vault': 'ENCRYPTED STRING', '__ansible_unsafe': 'UNSAFE'}
    decoded = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert isinstance(decoded, dict)
    assert isinstance(decoded.get('__ansible_vault'), AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:42:49.839887
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Need to add __file__ for python 2.6 compatibility
    import __builtin__
    __builtin__.__file__ = __file__

    from ansible.module_utils.six import PY3

    def _decode_list(data):
        '''Helper method to return a python list from JSON data'''
        rval = []
        for item in data:
            if isinstance(item, unicode):
                item = item.encode('utf-8')
            elif isinstance(item, list):
                item = _decode_list(item)
            elif isinstance(item, dict):
                item = _decode_dict(item)
            rval.append(item)
        return rval


# Generated at 2022-06-13 06:42:59.854825
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    secret = ["test"]
    vault = VaultLib(secrets=secret)
    decoder = AnsibleJSONDecoder()

    # Test __ansible_vault
    decoded = decoder.object_hook({"__ansible_vault": "test"})
    assert isinstance(decoded, AnsibleVaultEncryptedUnicode)
    assert decoded.vault is None

    decoder.set_secrets(secret)
    decoded = decoder.object_hook({"__ansible_vault": "test"})

# Generated at 2022-06-13 06:43:07.630792
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create a vault-encrypted variable
    vault = VaultLib(secrets=['password1'])
    vault_secrete = vault.encrypt(b'ansible')

    # This is the JSON representation of the variable
    json_string = '{"__ansible_vault": "' + vault_secrete.decode() + '"}'

    # Decode the JSON string
    decoded_json = json.loads(json_string, cls=AnsibleJSONDecoder)

    # Assert that the decoded data is a AnsibleVaultEncryptedUnicode
    assert isinstance(decoded_json, AnsibleVaultEncryptedUnicode)
    # Encrypted string will be replaced with decrypted string
    assert decoded_json == b'ansible'

    # Add the vault lib to the decoder
    AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:14.401609
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:19.769959
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        b'$ANSIBLE_VAULT;1.1;AES256\n',
        b'36306633303666303363393162363536616332626162323138616663303431366233633633134313\n',
        b'66336530636261653734656563323636376233653937386232666665\n',
    ]
    AnsibleJSONDecoder.set_secrets(secrets)
    reader = AnsibleJSONDecoder(encoding='utf-8')

# Generated at 2022-06-13 06:43:27.709447
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test for ansible_unsafe_proxy
    obj1 = decoder.object_hook({'__ansible_unsafe': 'hello'})
    if not obj1._val == 'hello':
        raise Exception("Faulty value returned from object_hook")

    # Test for ansible_vault
    obj2 = decoder.object_hook({'__ansible_vault': 'world'})
    if not obj2.vaulted_content == 'world':
        raise Exception("Faulty value returned from object_hook")

# Generated at 2022-06-13 06:43:32.039323
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    message = '{"__ansible_vault": "some_encrypted_value"}'
    expected_result = {u'__ansible_vault': AnsibleVaultEncryptedUnicode(u'some_encrypted_value')}
    result = AnsibleJSONDecoder().decode(message)
    assert result == expected_result

# Generated at 2022-06-13 06:43:37.166951
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo', 'bar']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)
    decoded = decoder.decode('{"__ansible_unsafe": "unsafe", "__ansible_vault": "vault"}')
    assert decoded['__ansible_unsafe'].unwrap() == 'unsafe'
    assert decoded['__ansible_vault'].vault == decoder._vaults['default']


# Generated at 2022-06-13 06:43:40.607655
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    secret = "password1"
    secrets = [ secret ]
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:43:44.459322
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ajd = AnsibleJSONDecoder()
    json_str = ({'a': 'aa', 'b': 'bb', '__ansible_vault': 'test', '__ansible_unsafe': 'b'})
    ajd.object_hook(json_str)

# Generated at 2022-06-13 06:43:53.875353
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    text1 = r'''{
    "__ansible_vault": "C:\Users\sharmarj\Ansible\sample.yml",
    "__ansible_unsafe": " $ whoami",
    "default": "default"
    }'''
    text2 = r'''{
    "default": "default"
    }'''
    json_data = json.loads(text1, cls=AnsibleJSONDecoder)
    for key in json_data.keys():
        assert isinstance(json_data[key], (AnsibleVaultEncryptedUnicode, str))
    json_data = json.loads(text2, cls=AnsibleJSONDecoder)
    assert not isinstance(json_data['default'], (AnsibleVaultEncryptedUnicode, str))

# Generated at 2022-06-13 06:44:09.701993
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    obj = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n33363930663333633131623665383234346461323936306665653938363336393537653634353930\n63333934376332316534393361306262663134633963323163346234653833326363616464303565\n37363430663162393939656438343733396634373133633035333439623163313832386131653562\n66393964663362316632313764663432626261333563642\n'}
    result = decoder.object_hook(obj)

# Generated at 2022-06-13 06:44:21.443599
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys, os
    sys.path.append(os.path.dirname(__file__))

    from unit.compat import get_encoded_dict, get_encoded_list

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['secret'])


# Generated at 2022-06-13 06:44:32.216133
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

    # Test to wrap a variable
    pairs = {'__ansible_unsafe': 'foo'}
    result = decoder.object_hook(pairs)
    assert isinstance(result, wrap_var)

    # Test to create an AnsibleVaultEncryptedUnicode object
    pairs = {'__ansible_vault': 'foo'}
    result = decoder.object_hook(pairs)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    # Test to get the input pairs
    pairs = {'foo': 'foo'}
    result = decoder.object_hook(pairs)
    assert result == pairs

# Generated at 2022-06-13 06:44:40.768345
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder_object = AnsibleJSONDecoder()
    test_pairs = {'test_key': 'test_value'}
    result = decoder_object.object_hook(test_pairs)
    assert result == {'test_key': 'test_value'}
    test_pairs = {'test_key': 'test_value', '__ansible_vault': 'test_value'}
    try:
        result = decoder_object.object_hook(test_pairs)
        assert result == {'test_key': 'test_value', '__ansible_vault': 'test_value'}
    except ValueError:
        pass
    test_pairs = {'test_key': 'test_value', '__ansible_unsafe': 'test_value'}
    result = decoder_object

# Generated at 2022-06-13 06:44:54.609689
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Test object_hook method of class AnsibleJSONDecoder
    '''
    # create an instance of class AnsibleJSONDecoder
    decoder = AnsibleJSONDecoder()

    # this should return a dictionary with key as __ansible_vault and value as AnsibleVaultEncryptedUnicode class
    value = decoder.object_hook({'__ansible_vault': 'my_encrypted_password'})
    assert isinstance(value, AnsibleVaultEncryptedUnicode)

    # this should return a dictionary with key as __ansible_unsafe and value as object with unsafe_proxy set
    value = decoder.object_hook({'__ansible_unsafe': 'my_password'})
    assert isinstance(value, object)
    assert value.unsafe_proxy

# Generated at 2022-06-13 06:45:06.275622
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:45:08.525897
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(object_hook = AnsibleJSONDecoder.object_hook)
    decoder.set_secrets(["password"])
    x = decoder.decode('{"__ansible_vault": "Vault encrypted string"}')
    assert x == AnsibleVaultEncryptedUnicode('Vault encrypted string')

# Generated at 2022-06-13 06:45:16.392230
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = AnsibleJSONEncoder().default({
        '__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;default;9SzCSh4kL7c=;Yw==',
        '__ansible_unsafe': 'unsafe'
    })
    decoded = json.loads(test_data, cls=AnsibleJSONDecoder)
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(decoded['__ansible_unsafe'], wrap_var)

# Generated at 2022-06-13 06:45:23.235051
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder()
    s = '{"key":"value","__ansible_vault":"abc","__ansible_unsafe":"123"}'
    v = d.decode(s)
    assert v["key"] == "value"
    assert v["__ansible_vault"] == "abc"
    assert v["__ansible_unsafe"] == "123"
    assert AnsibleVaultEncryptedUnicode.is_encrypted(v['__ansible_vault'], None) is True
    assert AnsibleJSONEncoder.is_unsafe(v['__ansible_unsafe']) is True

# Generated at 2022-06-13 06:45:36.069083
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test __ansible_vault
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:45:49.477926
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    enc = AnsibleJSONEncoder()
    dec = AnsibleJSONDecoder()
    dec.set_secrets(['test'])

    # Test parsing of AnsibleVaultEncryptedUnicode object
    test_val = enc.default('test')
    test_val['__ansible_vault'] = test_val.pop('__ansible__')
    assert isinstance(dec.object_hook(test_val), AnsibleVaultEncryptedUnicode)

    # Test parsing of unsafe vars
    unsafe_val = enc.default('test')
    unsafe_val['__ansible_unsafe'] = unsafe_val.pop('__ansible__')
    assert 'user_input' in dec.object_hook(unsafe_val)

    # Test parsing JSON that doesn't contain Ansible objects

# Generated at 2022-06-13 06:45:57.228950
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    my_vault_secret = 'mysecret'
    my_vault_content = 'my content'
    my_data = {'__ansible_vault': my_vault_secret}
    AnsibleJSONDecoder.set_secrets(my_vault_secret)
    ansible_vault1 = AnsibleJSONDecoder(my_data)
    ansible_decrypted_vault = ansible_vault1.decode(my_vault_content)
    print (str(ansible_decrypted_vault))
    assert ansible_decrypted_vault == my_vault_content

# Generated at 2022-06-13 06:46:07.156815
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    ansible_vault = {'__ansible_vault': 'foo', '__ansible_vault_password': 'default : foo'}
    ansible_vault_en = json.dumps(ansible_vault)
    ansible_vault_de = decoder.decode(ansible_vault_en)
    assert isinstance(ansible_vault_de, dict)
    assert type(ansible_vault_de['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert ansible_vault_de['__ansible_vault'].vault is None
    assert not ansible_vault_de['__ansible_vault'].vault_password

# Generated at 2022-06-13 06:46:19.723528
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [{'vault_password_file': 'test/test.vault'}]
    AnsibleJSONDecoder.set_secrets(secrets=secrets)

    input_dict = {'__ansible_vault': 'This is test content',
                  '__ansible_unsafe': True}
    output = AnsibleJSONDecoder().object_hook(pairs=input_dict)

    assert isinstance(output, AnsibleVaultEncryptedUnicode)
    assert isinstance(wrap_var(output), AnsibleVaultEncryptedUnicode)
    assert output.vault is not None
    assert output.vault.secrets is not None
    assert wrap_var(output.vault) is not None
    assert wrap_var(output.vault.secrets) is not None


# Generated at 2022-06-13 06:46:27.621017
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {'__ansible_vault': 'super secret',
            '__ansible_unsafe': 'not so secret'}

    decoded = AnsibleJSONDecoder().object_hook(data)

    assert type(decoded['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert type(decoded['__ansible_unsafe']) == AnsibleUnsafeText

# Generated at 2022-06-13 06:46:33.623069
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data = {'__ansible_vault': 'foo'}
    assert isinstance(decoder.object_hook(data), AnsibleVaultEncryptedUnicode)
    data = {}
    assert decoder.object_hook(data) == data



# Generated at 2022-06-13 06:46:34.608357
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder()
    assert d.object_h

# Generated at 2022-06-13 06:46:41.938398
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decrypted = decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;username\n3263393064343839353237633563363561613862373535323637333064656261623232656536333\n34636236623537356633316339313164633131613832306338317c79647a5a5f52736d475231696d\n6548327a6b4865487830666b734f6e6832767276747265736d6b6638\n'})
    assert isinstance(decrypted, AnsibleVaultEncryptedUnicode)
    assert decrypted == 'test'
    assert decrypted.v

# Generated at 2022-06-13 06:46:55.648751
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class Example():
        def __init__(self, example):
            self.example = example
        def __repr__(self):
            return 'object_hook_test(' + repr(self.example) + ')'

    original_data = {
        '__ansible_vault': "test string with ' and \"",
        '__ansible_unsafe': Example('test object with " and \''),
    }

    def encode_decode(data):
        data = json.dumps(data, cls=AnsibleJSONEncoder)
        data = json.loads(data, cls=AnsibleJSONDecoder)
        return data

    data = encode_decode(original_data)
    for key in data:
        assert key in original_data
        original_data_value = original_data[key]
       

# Generated at 2022-06-13 06:47:02.724599
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data1 = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n3132333435363738393031323334353637383930313233343536373839303132333435363738393031323334\n35363738393031323334353637383930313233343536373839303132333435363738393031323334353637383930\n31323334353637383930313233343536373839303132333435363738393031'}
    decoder = AnsibleJSONDecoder()
    decoded_data1 = decoder.object_hook(data1)
    assert type(decoded_data1) == AnsibleVaultEncryptedUnicode
    assert dec

# Generated at 2022-06-13 06:47:18.030149
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': '1234'}) == AnsibleVaultEncryptedUnicode('1234')
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')
    assert AnsibleJSONDecoder.object_hook({'__ansible_no_log': False}) == {'__ansible_no_log': False}

# Generated at 2022-06-13 06:47:27.093393
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = '$ANSIBLE_VAULT;1.1;AES256\n616161616161616161616161616161616161616161616161616161616161616161616161616161616161\n616161616161616161616161616161616161616161616161616161616161616161616161616161616161'
    decoder = AnsibleJSONDecoder.set_secrets(secrets)

    test_pairs = {'__ansible_vault': 'abcdefghijklmn'}
    result = decoder.object_hook(test_pairs)

    assert dict == type(result)
    assert '__ansible_vault' in result
    assert AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:47:41.566276
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = 'hush'
    ansible_json_decoder = AnsibleJSONDecoder()
    ansible_json_decoder.set_secrets([secret])

    for obj in ['__ansible_vault', '__ansible_unsafe']:

        # Both __ansible_vault and __ansible_unsafe are handled by object hook
        key = '__ansible_vault'
        value = 'vault_value'
        pairs = dict()
        pairs[key] = value
        assert ansible_json_decoder.object_hook(pairs) == AnsibleVaultEncryptedUnicode(value)
        assert ansible_json_decoder.object_hook(pairs) == pairs[key]

        # Other objects are not handled
        key = 'key'
        value = 'value'
        pairs

# Generated at 2022-06-13 06:47:47.837662
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'test_secrets'
    AnsibleJSONDecoder.set_secrets(secrets)

    # Testing __ansible_vault
    test_input_1 = {'__ansible_vault': 'value'}
    test_output_1 = AnsibleJSONDecoder.object_hook(test_input_1)

    assert test_output_1.vault
    assert test_output_1.vault == secrets

    # Testing __ansible_unsafe
    test_input_2 = {'__ansible_unsafe': 'value'}
    test_output_2 = AnsibleJSONDecoder.object_hook(test_input_2)

    assert test_output_2._original_value == 'value'

# Generated at 2022-06-13 06:47:57.366395
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = '''
{
"__ansible_vault": "Kakashi"
}
'''

    json_data_obj = '''
{
"__ansible_vault": "Kakashi"
}
'''


    json.loads(json_data, cls=AnsibleJSONDecoder)
    json_obj = json.loads(json_data_obj, cls=AnsibleJSONDecoder)

    assert type(json_obj['__ansible_vault']) == AnsibleVaultEncryptedUnicode



# Generated at 2022-06-13 06:48:03.211151
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data = decoder.object_hook({'__ansible_vault': 'some_value',
                                '__ansible_unsafe': "some_unsafe_value"})
    assert data[0] == AnsibleVaultEncryptedUnicode(u'some_value')
    assert data[1].value == "some_unsafe_value"

# Generated at 2022-06-13 06:48:10.179072
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;toto', '__ansible_unsafe': 'titi'}
    data_expected = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;toto', '__ansible_unsafe': wrap_var('titi')}
    decoder = AnsibleJSONDecoder()
    vault = {'default': AnsibleVaultEncryptedUnicode(data['__ansible_vault'])}
    decoder._vaults = vault
    data_recover = decoder.object_hook(data)
    assert data_expected == data_recover

# Generated at 2022-06-13 06:48:15.352600
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import ansible.parsing.vault
    import shutil
    vault_pass = 'secret'
    vault_id = 'myvault_id'
    vault_file = 'test/test-vault.gpg'

    # create a vault file
    old_vault_file = ansible.parsing.vault.VAULT_FILE
    ansible.parsing.vault.VAULT_FILE = vault_file
    ansible.parsing.vault.write_vault_file(vault_pass, vault_id)

    secret = 'Some very secret text'
    secret_vault = ansible.parsing.vault.encrypt(secret + '\n', vault_pass)


# Generated at 2022-06-13 06:48:26.238841
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(encoding='utf-8')
    pairs = {'__ansible_vault':'value'}
    value = decoder.object_hook(pairs)
    assert value.__class__.__name__ == 'AnsibleVaultEncryptedUnicode'
    assert value._encrypted_data == 'value'

    pairs = {'__ansible_unsafe':'value'}
    value = decoder.object_hook(pairs)
    assert value.__class__.__name__ == 'AnsibleUnsafeText'
    assert value._text == 'value'

# Generated at 2022-06-13 06:48:36.515163
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test AnsibleJSONDecoder.object_hook with a vaulted value
    decoded = json.loads('{"__ansible_vault": "foo"}', cls=AnsibleJSONDecoder)
    assert decoded == AnsibleVaultEncryptedUnicode('foo')

    # Test AnsibleJSONDecoder.object_hook with a non vaulted value
    decoded = json.loads('{"__ansible_vault": "foo", "__ansible_unsafe": "foo"}', cls=AnsibleJSONDecoder)
    assert decoded == {"__ansible_vault": AnsibleVaultEncryptedUnicode('foo'), "__ansible_unsafe": wrap_var('foo')}



# Generated at 2022-06-13 06:49:01.584383
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class Object(object):
        pass

    # "object" was already tested in python_json_test.py, therefore we're just checking if it's handled
    assert AnsibleJSONDecoder.object_hook(dict(foo=None)) == dict(foo=None)

    # test bad object
    assert AnsibleJSONDecoder.object_hook(dict(foo=None, __ansible_vault="bar")) == dict(foo=None)
    assert AnsibleJSONDecoder.object_hook(dict(foo=None, __ansible_unsafe="bar")) == dict(foo=None)

    # test vault object
    assert AnsibleJSONDecoder.object_hook(dict(__ansible_vault="foo")) == AnsibleVaultEncryptedUnicode("foo")

# Generated at 2022-06-13 06:49:05.132091
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_data = '$ANSIBLE_VAULT;1.1;AES256'
    vault = json.dumps({'__ansible_vault': vault_data})

    json.loads(vault, cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 06:49:09.350952
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'abc'}) == AnsibleVaultEncryptedUnicode('abc')
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'abc', '__ansible_unsafe': 'def'}) == {'__ansible_vault': AnsibleVaultEncryptedUnicode('abc'), '__ansible_unsafe': 'def'}

# Generated at 2022-06-13 06:49:16.600549
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import datetime
    json_string = """
    {
        "date": "2018-12-10T00:11:22.456789",
        "__ansible_vault": "vault:mysecret",
        "__ansible_unsafe": "{{ myvar }}"
    }"""
    secrets = ['mysecret']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)
    data = decoder.decode(json_string)
    assert data['date'] == datetime.datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert data['__ansible_vault'].vault == decoder._vaults['default']

# Generated at 2022-06-13 06:49:18.828126
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'myvault'})

# Generated at 2022-06-13 06:49:27.020312
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    va = '$ANSIBLE_VAULT;1.1;AES256\n63353963613861373266626463333632373534663561643235623666373733343935363930626437\n36306639656533326366376638356336613461626332616132303166656265356332376135633761\n613236616337650a6531326565306363623863313333623333656236346262366331646232643539\n36616337326162353738346366393763336361366131626232616632623264656630353465313036\n343963633332316134613662656466\n'

# Generated at 2022-06-13 06:49:40.508132
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    result = AnsibleJSONDecoder.object_hook({'test_key': 'test_value'})
    assert result == {'test_key': 'test_value'}

    vault_dict = {'__ansible_vault': 'my_vault'}
    result = AnsibleJSONDecoder.object_hook(vault_dict)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == None

    unsafe_dict = {'__ansible_unsafe': 'my_unsafe'}
    result = AnsibleJSONDecoder.object_hook(unsafe_dict)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == None

# Generated at 2022-06-13 06:49:45.912212
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    pairs = decoder.object_hook({
        'foo': 'bar',
        '__ansible_vault': 'foo',
        '__ansible_unsafe': 'bar',
    })

    assert isinstance(pairs['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert pairs['__ansible_vault'].vault is None
    assert isinstance(pairs['__ansible_unsafe'], wrap_var)
    assert pairs['__ansible_unsafe'].value == 'bar'

# Generated at 2022-06-13 06:49:56.233736
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:50:06.181559
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({
        '__ansible_vault': 'foo',
        'bar': 'baz',
    }) == {
        AnsibleVaultEncryptedUnicode('foo'): AnsibleVaultEncryptedUnicode('foo'),
        'bar': 'baz',
    }
    assert decoder.object_hook({
        '__ansible_unsafe': 'foo',
        'bar': 'baz',
    }) == {
        wrap_var('foo'): wrap_var('foo'),
        'bar': 'baz',
    }
    assert decoder.object_hook({
        '__ansible_vault': 'foo',
        '__ansible_unsafe': 'bar',
        'baz': 'qux',
    })

# Generated at 2022-06-13 06:50:46.331065
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    json_str = '{"__ansible_vault": "vault", "__ansible_unsafe": "unsafe"}'
    json_dict = {u'__ansible_unsafe': u'unsafe', u'__ansible_vault': u'vault'}

    secrets = 'secret'
    mydecoder = AnsibleJSONDecoder.set_secrets(secrets)
    result = AnsibleJSONDecoder(json_str)

    assert result == json_dict

# Generated at 2022-06-13 06:50:56.813410
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:51:05.956298
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Create dict
    user_1 = dict(
        name='Aki Tuwara',
        age=42,
        address='Tokyo, Japan')

    # Create AnsibleJSONDecoder object
    jd = AnsibleJSONDecoder()

    # Execute method object_hook
    user_1_json = json.dumps(user_1, cls=AnsibleJSONEncoder)
    user_2 = jd.decode(user_1_json)

    # Assert
    assert '__ansible_vault' in user_2.keys()
    assert user_2['__ansible_vault'] == user_1

    # Create dict
    user_3 = dict(
        name='Aki Tuwara',
        age=42,
        address=['Tokyo', 'Japan'])

    # Execute

# Generated at 2022-06-13 06:51:17.401950
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import sys
    import unittest
    from unittest.mock import patch

    class TestClass(unittest.TestCase):
        def setUp(self):
            secrets = [{'password': 'mypassword'}]
            AnsibleJSONDecoder.set_secrets(secrets)



# Generated at 2022-06-13 06:51:20.717546
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pairs = {'__ansible_vault': 'test', '__ansible_unsafe': 'test'}
    test_result = AnsibleJSONDecoder().object_hook(pairs)
    assert isinstance(test_result, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:51:34.903179
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """this is a test for AnsibleJSONDecoder.object_hook()"""

    import json
    import os

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    basedir = os.path.dirname(__file__)

    loader = DataLoader()
    with open(os.path.join(basedir, 'sample_vars.json')) as sample:
        jsn = sample.read()
        json_data = json.loads(jsn)
