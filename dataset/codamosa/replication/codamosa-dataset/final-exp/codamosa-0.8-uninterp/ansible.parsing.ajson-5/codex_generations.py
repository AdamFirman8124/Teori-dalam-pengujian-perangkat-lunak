

# Generated at 2022-06-13 06:41:36.311088
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Here we test whether the json decoder if decoding the string
    into the AnsibleVaultEncryptedUnicode object and wrapping it
    in the AnsibleUnsafeText wrapper.
    :return:
    """
    decoder = AnsibleJSONDecoder()
    decoded_json = decoder.decode('{"__ansible_vault": "my_secret"}')
    assert isinstance(decoded_json[0],
                      AnsibleVaultEncryptedUnicode)
    assert isinstance(decoded_json[0], wrap_var('my_secret'))



# Generated at 2022-06-13 06:41:41.727050
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'hello'}) == AnsibleVaultEncryptedUnicode('hello')
    assert decoder.object_hook({'__ansible_unsafe': 'hello'}) == wrap_var('hello')
    assert decoder.object_hook({'a': 'hello'}) == {'a': 'hello'}

# Generated at 2022-06-13 06:41:51.668404
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;foo\nbar\n'}
    r = decoder.object_hook(pairs)
    assert r == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;foo\nbar\n')

    pairs = {'__ansible_unsafe': '$ANSIBLE_UNSAFE'}
    r = decoder.object_hook(pairs)
    assert r == wrap_var('$ANSIBLE_UNSAFE')

# Generated at 2022-06-13 06:41:59.090709
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    """
    object_hook method of class AnsibleJSONDecoder decodes the string
    from json text. main purpose of this method is to identify the unsafe
    and vault string in json text.

    :return: decoded string
    """

    v = AnsibleJSONDecoder._vaults['default'] = VaultLib(secrets=['password'])
    unsafe_str = 'some string'
    vault_str ='$ANSIBLE_VAULT;1.1;AES256\n'
    ansible_json_decoder = AnsibleJSONDecoder()
    assert ansible_json_decoder.object_hook({'__ansible_unsafe': unsafe_str, '__ansible_vault': vault_str}) == {'__ansible_unsafe': unsafe_str, '__ansible_vault': vault_str}

#

# Generated at 2022-06-13 06:42:13.257206
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:20.385217
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:33.777252
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    class DataHolder:
        pass
    pairs = DataHolder()
    pairs.__ansible_vault = '$ANSIBLE_VAULT;1.1;AES256\n313735353135333961306663626439373233353036353963623537653261333132313963356132373\n393366623961636137613163643337336338323032613432626130622e0a'
    pairs.__ansible_unsafe = '$ANSIBLE_UNSAFE'

# Generated at 2022-06-13 06:42:46.715943
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['my-secret-password']
    AnsibleJSONDecoder.set_secrets(secrets)

    unsafe_dict = {"__ansible_unsafe": "obj1"}
    unsafe_json = json.dumps(unsafe_dict)
    decoded_unsafe = json.loads(unsafe_json, cls=AnsibleJSONDecoder)
    assert decoded_unsafe['__ansible_unsafe'] == unsafe_dict['__ansible_unsafe']
    assert decoded_unsafe['__ansible_unsafe'] != u'obj1'
    assert decoded_unsafe['__ansible_unsafe'] == u'obj1'

    vault_dict = {"__ansible_vault": "obj2"}
    vault_json = json.dumps(vault_dict)
    decoded_v

# Generated at 2022-06-13 06:42:57.028437
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:03.947147
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['idontcare'])

    # Test safe var
    obj = decoder.object_hook({})
    assert obj == {}

    # Test unsafe var
    obj = decoder.object_hook({'__ansible_unsafe': {}})
    assert obj == wrap_var({})

    # Test vaulted var
    obj = decoder.object_hook({'__ansible_vault': 'idontcare'})
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:43:12.269800
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({"abc": "abc"}) == {"abc": "abc"}
    assert len(AnsibleJSONDecoder.object_hook({"__ansible_vault": "abc"}).__dict__) == 2

# Backwards compat
AnsibleVaultJSONDecoder = AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:23.434462
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
      Test vault and unsafe handling in object_hook (factory method of json.JSONDecoder)
    """
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['vault-password'])

    # Test vault handling
    vault_string = '$ANSIBLE_VAULT;1.2;AES256;default\n12345'
    data = dict(__ansible_vault=vault_string)
    json_data = json.dumps(data)
    obj = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert isinstance(obj, dict)
    assert isinstance(obj.get('__ansible_vault'), AnsibleVaultEncryptedUnicode)

    # Test unsafe handling
    unsafe_string = 'this is an unsafe string'


# Generated at 2022-06-13 06:43:30.715185
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    encoded = b'{"__ansible_vault": "foo", "__ansible_unsafe": "bar"}'
    expected_ansible_vault_obj = AnsibleVaultEncryptedUnicode('foo')
    expected_ansible_unsafe_obj = wrap_var('bar')
    decoded = AnsibleJSONDecoder(encoded)
    assert decoded._decode_dict == [expected_ansible_vault_obj, expected_ansible_unsafe_obj]

# Imported for backwards compat
AnsibleJSONEncoder = json.JSONEncoder

# Generated at 2022-06-13 06:43:38.569903
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = "my-secret-password"
    json_encoded_string = get_json_encoded_string(secret)

# Generated at 2022-06-13 06:43:42.696532
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def assert_value(key, value, expected):
        pairs = {}
        pairs[key] = value
        result = AnsibleJSONDecoder.object_hook(pairs)
        assert value == expected, result

    assert_value(
        key='__ansible_vault',
        value='test_ansible_vault',
        expected=AnsibleVaultEncryptedUnicode('test_ansible_vault'),
    )

    assert_value(
        key='__ansible_unsafe',
        value='test_ansible_unsafe',
        expected=wrap_var('test_ansible_unsafe')
    )

# Generated at 2022-06-13 06:43:51.105564
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {}
    data['__ansible_vault'] = 'vault'
    data['__ansible_unsafe'] = wrap_var('datetime')

    secret = 'secret'
    vault = VaultLib(secrets=secret)
    AnsibleJSONDecoder.set_secrets(secret)
    result = AnsibleJSONDecoder().object_hook(data)

    assert result['__ansible_vault'] == 'vault'
    assert result['__ansible_vault'].vault == vault
    assert result['__ansible_unsafe'] == 'datetime'
    assert getattr(result['__ansible_unsafe'], '__ansible_unsafe__') == True

# Generated at 2022-06-13 06:43:56.987579
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    result = AnsibleJSONDecoder.object_hook({
        '__ansible_vault': 'some_vault_string',
        '__ansible_unsafe': 'some_unsafe_string'
    })

    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(result['__ansible_unsafe'], wrap_var)

    # Call the object_hook method again
    result = AnsibleJSONDecoder.object_hook(result)

    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(result['__ansible_unsafe'], wrap_var)

# Generated at 2022-06-13 06:44:10.308476
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:22.146164
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:44:30.725800
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    def assert_item_is_instance_of(item, expected_instance_type):
        assert isinstance(item, expected_instance_type)


# Generated at 2022-06-13 06:44:36.957572
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    with open('test/units/parsing/yaml/ansible_vault_encrypted.json', 'r') as test_file:
        decoder = AnsibleJSONDecoder()
        decoder._vaults['default'] = VaultLib(secrets='Username: Password')
        test_dict = json.load(test_file, cls=decoder)
        assert(test_dict['password'] == 'Password')

# Generated at 2022-06-13 06:44:43.406918
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:51.284855
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_string = '{"__ansible_vault": "id"}'
    secrets = "test"
    vault_lib = VaultLib(secrets)
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    decodedString = decoder.decode(test_string)
    assert decodedString.from_json
    assert isinstance(decodedString, AnsibleVaultEncryptedUnicode)
    assert decodedString == vault_lib.decrypt(decodedString)
    assert isinstance(json.dumps(decodedString, cls=AnsibleJSONEncoder), str)

# Generated at 2022-06-13 06:44:57.228814
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    import yaml
    
    secret = "12345"
    raw = """
    a: 1
    b:
      __ansible_vault: !vault |
        $ANSIBLE_VAULT;1.1;AES256
        3132333435363738393031323334353637383930313233343536373839303132
        333435363738393031323334353637383930=
    c: !unsafe "123"
    """
    
    vault = VaultLib(secrets=[secret])
    encrypted_data = vault.encrypt(raw)
    encrypted_data = yaml.safe_load(encrypted_data)
    
    #

# Generated at 2022-06-13 06:45:06.375922
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup test
    secrets = ['foo']
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    test_data = {'__ansible_vault': 'vault_value'}
    # Run method being tested
    result = decoder.object_hook(test_data)
    # Expected result
    result_expected = AnsibleVaultEncryptedUnicode('vault_value')
    result_expected.vault = VaultLib(secrets=secrets)
    # Assert result
    assert result == result_expected


# Generated at 2022-06-13 06:45:11.454154
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    encoder = AnsibleJSONEncoder(ensure_ascii=False)
    ansible_encrypted = encoder.encode(
        AnsibleVaultEncryptedUnicode('secret', vault_id='test')
    )
    assert 'secret' == AnsibleJSONDecoder.object_hook({
        '__ansible_vault': json.loads(ansible_encrypted)
    })

# Generated at 2022-06-13 06:45:21.466928
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault_secrets = "password"
    decoder.set_secrets(vault_secrets)

# Generated at 2022-06-13 06:45:27.876903
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var

    vault_id = 'default'
    vault_secret = 'Password1'
    vault_password_file = './vault.key'  # TODO: Needs to be a real file

    secrets = [vault_secret]
    vault_handler = VaultLib(secrets=secrets)
    vault_handler.read_vault_password_file(vault_password_file)

    # This is the value of the '__ansible_vault' key in the dictionary

# Generated at 2022-06-13 06:45:39.457913
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:48.811720
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import io
    import json

    # when __ansible_vault is set, use provided secrets
    secrets = 'some_secrets'
    AnsibleJSONDecoder.set_secrets(secrets)

    # when __ansible_vault is set, use provided secrets
    data = json.loads('{"__ansible_vault": "vaulted"}', cls=AnsibleJSONDecoder)
    assert(data.vault)
    assert(data.vault._secrets == secrets)

    # when __ansible_unsafe is set, return a wrapped var
    data = json.loads('{"__ansible_unsafe": "unsafe"}', cls=AnsibleJSONDecoder)
    assert(isinstance(data, wrap_var))

    # when __ansible_unsafe is not set, return a wrapped var

# Generated at 2022-06-13 06:45:53.546619
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoded = json.loads('{"__ansible_unsafe": "unsafe"}',
                         cls=AnsibleJSONDecoder)
    assert decoded == wrap_var('unsafe')

# Generated at 2022-06-13 06:45:56.828069
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [{'2': 3}]
    AnsibleJSONDecoder.set_secrets(secrets)
    pairs = {u'__ansible_vault': u'vaulttext'}
    assert AnsibleJSONDecoder().object_hook(pairs) == AnsibleVaultEncryptedUnicode(u'vaulttext')

# Generated at 2022-06-13 06:46:04.714821
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Load data from string and prepare to check its correctness
    json_string = '{"key1": "value1", "key2": "value2"}'
    loaded_data = json.loads(json_string)

    # Load data using AnsibleJSONDecoder and prepare to check its correctness
    dec = AnsibleJSONDecoder()
    decoded_data = dec.decode(json_string)

    # Check correctness of loaded data
    assert loaded_data == {'key1': 'value1', 'key2': 'value2'}
    assert decoded_data == {'key1': 'value1', 'key2': 'value2'}



# Generated at 2022-06-13 06:46:18.657686
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.vault import VaultSecret

    assert not isinstance({}, AnsibleVaultEncryptedUnicode)

    secrets = {'vault_password': VaultSecret('abc')}
    data = {'__ansible_vault': 'abc'}

    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    AnsibleJSONDecoder.set_secrets(secrets)
    decoded = decoder.decode(json.dumps(data))
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)

    AnsibleJSONDecoder._vaults = {}

    decoded = decoder.decode(json.dumps(data))

# Generated at 2022-06-13 06:46:30.727343
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')
    assert decoder.object_hook({'__ansible_unsafe': 'I am unsafe'}) == AnsibleUnsafeText('I am unsafe')
    assert decoder.object_hook({'normal_key': 'normal_value'}) == {'normal_key': 'normal_value'}

# Generated at 2022-06-13 06:46:39.079845
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_password = 'secret'
    value_to_decode = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;ansible_test\n366139306438333764363730343130326138613631396238633834663037343932633461363663\n353761643032653633666262613431323235366233313336333536653934303334353563616438\n363462626466626161333663346236633237386665336230356563373433636336316233353066\n6338653463346238616636313562396363\n'
    }

# Generated at 2022-06-13 06:46:50.206935
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = {
        "__ansible_vault": "mock_encrypted_string",
        "__ansible_unsafe": "mock_unsafe_string"
    }
    decoder = AnsibleJSONDecoder()
    data = decoder.decode(json.dumps(json_data))
    assert data[0].vault is None
    assert isinstance(data[0], AnsibleVaultEncryptedUnicode) is True
    assert data[1].secret is None
    assert isinstance(data[1], wrap_var.AnsibleUnsafe) is True



# Generated at 2022-06-13 06:46:58.761145
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:08.311966
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test a dictionary that contains __ansible_unsafe and __ansible_vault
    dict_to_decode = {
        "__ansible_vault": "AQD1GxH8Ij+9McSVfJzDZ0gVQwzRZaGx7cBIs6JTd7+3XyHb+Fnf/j\n",
        "b": "2",
        "c": "3",
        "__ansible_unsafe": "{{ { 'test': [1, 2] } }}",
        "e": "5"
    }
    decoded_dict = AnsibleJSONDecoder.object_hook(dict_to_decode)
    assert type(decoded_dict.get("__ansible_vault")) is AnsibleVaultEncryptedUnic

# Generated at 2022-06-13 06:47:18.625617
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = json.loads('{"__ansible_unsafe": "meaning of life", "__ansible_vault": "V2VsY29tZSB0byBibGFja3poYXJk"}', cls=AnsibleJSONDecoder)

    assert json_data[0] == AnsibleVaultEncryptedUnicode('V2VsY29tZSB0byBibGFja3poYXJk')
    assert json_data[1] == 'meaning of life'


# Generated at 2022-06-13 06:47:28.753297
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    encrypted_text = '$ANSIBLE_VAULT;1.1;AES256\n3530643539343761376461383366333361326661656136623137376163316364353432626566623166\n3938376662383465366232666331373666343765393338373562303533643163643565303566623361\n6537326263626566366461613434356363323165326262653265613933643663396664326131643465\n3164656638396530633264383564313763636330633265643635313831336132633566333865663630\n33666630663530\n'

# Generated at 2022-06-13 06:47:33.315248
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['password']

    ansible_json_decoder = AnsibleJSONDecoder()
    ansible_json_decoder.set_secrets(secrets=secrets)
    pairs = {'__ansible_vault': 'password'}
   

# Generated at 2022-06-13 06:47:45.868252
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        b'$ANSIBLE_VAULT;1.1;AES256',
        b'63727970746f7b59684a6c614149444b7447786c64436b4e6e476f6a61596b4e4b7856694d533d',
    ]
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    decoded = decoder.decode(
        '{"__ansible_vault": "63727970746f7b59684a6c614149444b7447786c64436b4e6e476f6a61596b4e4b7856694d533d"}'
    )
    assert(), "not implemented"

# Generated at 2022-06-13 06:47:51.895129
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    import sys

    # Import ansible.parsing.vault
    ansible_path = os.path.dirname(__file__)
    sys.path.append(ansible_path + '/../..')
    import ansible.parsing.vault
    import ansible.parsing.vault_lib
    from ansible.parsing.vault import VaultLib
    import ansible.parsing.dataloader

    # Import ansible.parsing.yaml
    import ansible.parsing.yaml

    # Mocking ansible.module_utils.common.json.AnsibleJSONEncoder.encode() method

# Generated at 2022-06-13 06:48:02.461652
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    decoder = AnsibleJSONDecoder()

    # Test normal dictionary
    assert decoder.object_hook({'key': 'value'}) == {'key': 'value'}

    # Test dictionary with __ansible_vault key

# Generated at 2022-06-13 06:48:08.999551
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    AnsibleJSONDecoder.object_hook()
    '''
    decoder = AnsibleJSONDecoder()
    vault = {'password': 'foo'}
    AnsibleJSONDecoder.set_secrets(vault)
    #Expect AnsibleVaultEncryptedUnicode
    dec = decoder.object_hook({'__ansible_vault': 'bar'})
    assert isinstance(dec, AnsibleVaultEncryptedUnicode)
    #Expect AnsibleUnsafeText otherwise
    dec = decoder.object_hook({'__ansible_unsafe': 'bar'})
    assert dec._text == 'bar'

# Generated at 2022-06-13 06:48:19.664663
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {
        'foo': 'bar',
        'baz': None,
        '__ansible_vault': 'The rain in spain stays mainly in the plain',
        '__ansible_unsafe': 'The rain in spain stays mainly in the plain',
        'l33t': {'__ansible_vault': 'The rain in spain stays mainly in the plain', '__ansible_unsafe': 'The rain in spain stays mainly in the plain'},
        'list': [
            'The rain in spain stays mainly in the plain',
            {'__ansible_vault': 'The rain in spain stays mainly in the plain', '__ansible_unsafe': 'The rain in spain stays mainly in the plain'},
        ]
    }


# Generated at 2022-06-13 06:48:31.549703
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {
        'default': {'vault_password': 'test'}
    }
    j = '{"__ansible_vault": "test"}'
    d = json.loads(j, cls=AnsibleJSONDecoder)
    assert d == AnsibleVaultEncryptedUnicode('test')
    assert d.vault_password == secrets['default']['vault_password']

    secrets = {
        'default': {'vault_password': 'test'}
    }
    j = '{"__ansible_vault": "test", "__ansible_unsafe": "test"}'
    d = json.loads(j, cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 06:48:42.746427
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # set vault
    secrets = 'pass'
    AnsibleJSONDecoder.set_secrets(secrets)

    # ansible_vault
    ansible_vault = AnsibleJSONDecoder().object_hook('__ansible_vault')
    assert str(ansible_vault) == '$ANSIBLE_VAULT;1.1;AES256', 'ansible_vault failed'

    # ansible_unsafe
    ansible_unsafe = AnsibleJSONDecoder().object_hook('__ansible_unsafe')
    assert str(ansible_unsafe) == '<ansible.utils.unsafe_proxy.AnsibleUnsafeText object at 0x7f7eb456fe80>', 'ansible_unsafe failed'

    # other

# Generated at 2022-06-13 06:48:54.329237
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Case 1: __ansible_vault
    secret = ['12345']
    AnsibleJSONDecoder.set_secrets(secret)

# Generated at 2022-06-13 06:49:08.116098
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets('foobar')

    # AnsibleVaultEncryptedUnicode
    data = {
        '__ansible_vault': 'vault string'
    }
    assert decoder.object_hook(data) == AnsibleVaultEncryptedUnicode('vault string')
    assert decoder.object_hook(data).vault.secrets == ['foobar']

    # original behavior with __ansible_unsafe
    data = {
        '__ansible_unsafe': '$ANSIBLE_VAULT'
    }
    assert decoder.object_hook(data) == wrap_var('$ANSIBLE_VAULT')

    # original behavior with

# Generated at 2022-06-13 06:49:15.620462
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # test empty object
    assert AnsibleJSONDecoder.object_hook({}) == {}

    # test secure string

# Generated at 2022-06-13 06:49:24.926957
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # GIVEN a string with a vault and an unsafe
    jsonString = '{"__ansible_vault": "VaultBlob", "__ansible_unsafe": { "foo": "bar" }}'
    decoder = AnsibleJSONDecoder()

    # WHEN the string is decoded
    retval = decoder.decode(jsonString)

    # THEN the vault is AnsibleVaultEncryptedUnicode and the unsafe is unsafe wrapped
    assert type(retval['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert type(retval['__ansible_unsafe']) == dict
    assert type(retval['__ansible_unsafe']['foo']) == str


# Generated at 2022-06-13 06:49:39.688463
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = ['testsecret123']


# Generated at 2022-06-13 06:49:46.826293
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # create a vault secret
    vault_secret = {'vault_password': 'secret'}

    # create an AnsibleJSONDecoder object
    ansible_json_decoder_object = AnsibleJSONDecoder()

    # set the vault secret for decoder
    AnsibleJSONDecoder.set_secrets(vault_secret)

    # create a json object with vault data
    json_object= {
            '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256',
            '__ansible_vault_identity': '658c0c71b131e6d4ba6f935cd967e6b7c6b2d0b0',
            '__ansible_vault_id': 'default',
            'vault_test': 'value'
            }



# Generated at 2022-06-13 06:49:57.059336
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    json_data = '''{
    "__ansible_vault": "my_secret",
    "__ansible_unsafe": { "var": "stuff" }
}'''
    decoder = AnsibleJSONDecoder()
    decoded = decoder.decode(json_data)
    decoded['__ansible_unsafe'] = wrap_var(decoded['__ansible_unsafe'])
    assert '__ansible_vault' in decoded
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert '__ansible_unsafe' in decoded

# Generated at 2022-06-13 06:50:06.485348
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """Test AnsibleJSONDecoder's object_hook.
    """
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.parsing.yaml import load, dump
    from io import StringIO

    # test __ansible_vault

# Generated at 2022-06-13 06:50:14.509220
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    
    s = '{"_ansible_parsed": true}'
    obj = json.loads(s, cls=AnsibleJSONDecoder)
    assert obj['_ansible_parsed'] == True

    s = '{"__ansible_unsafe": "hello"}'
    obj = json.loads(s, cls=AnsibleJSONDecoder)
    assert obj['__ansible_unsafe'] == "hello"

    s = '{"__ansible_unsafe": null}'
    obj = json.loads(s, cls=AnsibleJSONDecoder)
    assert obj['__ansible_unsafe'] == None
    
    s = '{"key": "this is my vault password"}'
    obj = json.loads(s, cls=AnsibleJSONDecoder)


# Generated at 2022-06-13 06:50:30.050430
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class TestAnsibleVaultEncryptedUnicode:
        def __init__(self, value):
            self.value = value

    vault_password = 'secrets'

# Generated at 2022-06-13 06:50:35.020930
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    json_str = '{"__ansible_unsafe": "string", "__ansible_vault": "str"}'
    expected_result = {'__ansible_vault': AnsibleVaultEncryptedUnicode('str'),
                       '__ansible_unsafe': 'string'}
    assert AnsibleJSONDecoder().object_hook(json.loads(json_str)) == expected_result

# Generated at 2022-06-13 06:50:51.814118
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder({'bar': 'foo'})
    assert decoder.object_hook({'bar': 'foo'}) == {'bar': 'foo'}

    # The call to object_hook must change the value of the element if
    # __ansible_vault is found
    assert decoder.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')

    # The call to object_hook must change the value of the element if
    # __ansible_unsafe is found
    assert decoder.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')

# Generated at 2022-06-13 06:50:57.244300
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({"__ansible_vault": "value"}) == AnsibleVaultEncryptedUnicode("value")
    assert decoder.object_hook({"__ansible_unsafe": "value"}) == wrap_var("value")

# Generated at 2022-06-13 06:51:03.273024
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    text = '{"__ansible_vault": "string"}'
    decoded = json.loads(text, cls=AnsibleJSONDecoder)

    # Check if the object is an AnsibleVaultEncryptedUnicode
    if not isinstance(decoded, AnsibleVaultEncryptedUnicode):
        raise AssertionError("The object_hook method of class AnsibleJSONDecoder does not create an AnsibleVaultEncryptedUnicode")

# Generated at 2022-06-13 06:51:14.013033
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Load json content into memory
    with open('tests/unit/parsing/vault/json_decoder_test.json') as json_file:
        json_content = json.load(json_file, cls=AnsibleJSONDecoder)

    # Assertions
    assert json_content['ansible_vault'].vault
    assert isinstance(json_content['ansible_vault'].vault, VaultLib)
    assert json_content['ansible_vault']._decoded_value == 'test123'
    assert json_content['unsafe']._decoded_value == 'test123'


if __name__ == "__main__":
    test_AnsibleJSONDecoder_object_hook()

# Generated at 2022-06-13 06:51:17.973775
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    """
        Unit test for method object_hook of class AnsibleJSONDecoder
        :return: No return value
    """
    result = AnsibleJSONDecoder.object_hook({'__ansible_vault': "Hello World!"})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result == "Hello World!"

# Generated at 2022-06-13 06:51:23.908515
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    unit test for method object_hook of class AnsibleJSONDecoder
    '''
    import sys
    import os

    cwd = os.path.dirname(os.path.abspath(__file__))
    test_vars = os.path.join(cwd, 'test_vars')
    if test_vars not in sys.path:
        sys.path.append(test_vars)

    import test_utils
    test_utils.run_module(['-v'], 'test_JSONDecoder_object_hook', test_vars)

if __name__ == '__main__':
    test_AnsibleJSONDecoder_object_hook()

# Generated at 2022-06-13 06:51:36.911359
# Unit test for method object_hook of class AnsibleJSONDecoder