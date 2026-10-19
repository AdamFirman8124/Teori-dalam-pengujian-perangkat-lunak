

# Generated at 2022-06-13 06:41:28.347189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'you cannot see me'}) == wrap_var('you cannot see me')
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'you cannot see me'}) == AnsibleVaultEncryptedUnicode('you cannot see me')

# Generated at 2022-06-13 06:41:34.136779
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Using the example from Ansible 
    # https://docs.ansible.com/ansible/2.4/playbooks_vault.html#using-vault-in-playbooks
    dec = AnsibleJSONDecoder()
    ans = dec.object_hook({"__ansible_unsafe": "VARIABLE"})
    assert wrap_var("VARIABLE").get_wrapped() ==  ans.get_wrapped()

    secrets = "vaultpassword"
    dec = AnsibleJSONDecoder()
    dec.set_secrets(secrets)
    ans = dec.object_hook({"__ansible_vault": "VARIABLE"})
    assert AnsibleVaultEncryptedUnicode("VARIABLE").vault.get_encrypted_data() ==  ans.vault.get_encrypted

# Generated at 2022-06-13 06:41:43.537891
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = [
        # test with vaulted data with and without vault id, with and without vault password
        ({'__ansible_vault': 'VGFza1Bhc3N3b3Jk=='}, False),
        ({'__ansible_vault__': 'VGFza1Bhc3N3b3Jk=='}, True),
        ({'__ansible_vault': 'VGFza1Bhc3N3b3Jk=='}, True),
        ({'__ansible_vault__': 'VGFza1Bhc3N3b3Jk=='}, True),
    ]

    for data in test_data:
        json_str = json.dumps(data[0])
        decoded_json = AnsibleJSONDecoder().decode(json_str)


# Generated at 2022-06-13 06:41:55.453386
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:04.659463
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:11.754243
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({"__ansible_unsafe": "{{ secret }}", "__ansible_vault": "VAULT_ENCRYPTED_VALUE"}) == {"__ansible_unsafe": wrap_var("{{ secret }}"), "__ansible_vault": AnsibleVaultEncryptedUnicode("VAULT_ENCRYPTED_VALUE")}

# Generated at 2022-06-13 06:42:14.743813
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    value = decoder.object_hook({'key': 'value', '__ansible_unsafe': True})
    assert hasattr(value['key'], '__ansible_unsafe__')

# Generated at 2022-06-13 06:42:20.089061
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_secrets = ("test")
    json_text = ('{"__ansible_vault": "ansible-vault string", "__ansible_unsafe": "test"}')
    ansiblejson_decoder = AnsibleJSONDecoder()
    ansiblejson_decoder.set_secrets(test_secrets)
    obj = ansiblejson_decoder.decode(json_text)
    assert obj['__ansible_vault'] == 'ansible-vault string'
    assert obj['__ansible_unsafe'] == 'test'

# Generated at 2022-06-13 06:42:34.052311
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # TODO:implement unit test for AnsibleJSONDecoder.object_hook

    vault_pwd = "vault_pwd"
    AnsibleJSONDecoder.set_secrets([vault_pwd])

    unsafe_value = "unsafe_value"
    unsafe_put = {
        '__ansible_unsafe': unsafe_value
    }
    unsafed = json.loads(
        json.dumps(
            unsafe_put,
            cls=AnsibleJSONEncoder
        ),
        cls=AnsibleJSONDecoder
    )
    assert unsafed.value == unsafe_value


# Generated at 2022-06-13 06:42:46.723935
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:57.538713
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test with a simple case
    test_case = b'{\n    "__ansible_vault": "vault_data",\n    "author": "Fred"\n}'
    parsed = json.loads(test_case, cls=AnsibleJSONDecoder)
    assert isinstance(parsed['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert parsed['__ansible_vault'] == 'vault_data'
    assert parsed['author'] == 'Fred'

    # Test with a simple case where unsafe markers are present
    test_case = b'{\n    "__ansible_vault": "vault_data",\n    "__ansible_unsafe": 1,\n    "author": "Fred"\n}'

# Generated at 2022-06-13 06:43:05.787738
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Create a json string with ansible vault and unsafe elements
    input_str = '{"a":"b","__ansible_vault":"$ANSIBLE_VAULT;1.1;AES256\n666666\n","__ansible_unsafe":"$ANSIBLE_VAULT;1.1;AES256\n777777"}'

    # Init decoder with ansible vault password
    decoder = AnsibleJSONDecoder(vault_password='secret')

    # Here we need to use the method .decode('utf-8') to decode the string
    # If don't do that, the bad input will be seen as a dict, which was
    # also decoded by json.JSONDecoder, and led to a TypeError exception
    # in ansible.utils.unsafe_proxy.

# Generated at 2022-06-13 06:43:19.935475
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for an ansible vault
    value = json.loads('{"__ansible_vault": "vault"}', cls=AnsibleJSONDecoder)
    assert value == AnsibleVaultEncryptedUnicode("vault")

    # Test for ansible unsafe
    value = json.loads('{"__ansible_unsafe": "unsafe"}', cls=AnsibleJSONDecoder)
    assert value == wrap_var("unsafe")

    # Test for ansible unsafe and ansible vault
    value = json.loads('{"__ansible_unsafe": "unsafe", "__ansible_vault": "vault"}', cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 06:43:30.435629
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret1 = {"vault_password_file": "/root/ansible-dc.key"}
    secret2 = {"vault_password": "ansible-dc"}
    secret3 = {"vault_password": "changeit"}

    AnsibleJSONDecoder.set_secrets(secret1)
    plaintext_value = 'Hello world'
    vaulted_value = AnsibleJSONEncoder().encode(plaintext_value)
    decoded_value = AnsibleJSONDecoder().decode(vaulted_value)
    assert plaintext_value == decoded_value
    AnsibleJSONDecoder.set_secrets(secret2)
    assert plaintext_value == decoded_value

    vaulted_value = AnsibleJSONEncoder().encode(plaintext_value)
    decoded_value = AnsibleJSONDecoder().dec

# Generated at 2022-06-13 06:43:38.389739
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:50.211841
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = "random_string"
    secrets_obj = test_obj = {'ANSIBLE_VAULT': {'__ansible_vault': 'sometext',
                                                '__ansible_unsafe': 'somevalue'},
                              'ANSIBLE_VAULT_IDENTITY': 'test_vault'}
    # Construct AnsibleJSONDecoder Object with secrets
    AnsibleJSONDecoder.set_secrets(secrets)
    ansible_json_decoder = AnsibleJSONDecoder(**secrets_obj)
    result = ansible_json_decoder.object_hook(test_obj)

    # Test object_hook method
    assert('ANSIBLE_VAULT' in result)
    assert(isinstance(result.get('ANSIBLE_VAULT'), AnsibleVaultEncryptedUnicode))

# Generated at 2022-06-13 06:43:59.610618
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    This function returns True if AnsibleJSONDecoder.object_hook() method
    passes the unit test and False otherwise.
    '''
    try:
        from ansible.parsing.yaml.objects import AnsibleUnsafeText
    except ImportError:
        from ansible.parsing.yaml.objects import AnsibleUnsafe
    import json

    secret = "12345"
    v = VaultLib(secrets=[secret])

# Generated at 2022-06-13 06:44:10.659581
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:19.007017
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_json_dict = {}
    test_json_dict['enc'] = '__ansible_vault'
    test_json_dict['value'] = '$ANSIBLE_VAULT;1.1;AES256'
    test_json_dict['h400'] = 'ad053b2ca277540a47c1efb03b18f57038a6a08d24d10297a0a3a2e9c7dfd24e'
    test_json_dict['h400_tag'] = 'somesecretsecret'

    # Test for AnsibleVaultEncryptedUnicode
    test_decoder = AnsibleJSONDecoder()
    result = test_decoder.object_hook(test_json_dict)

    assert(type(result) is AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:44:30.000932
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # AnsibleJSONDecoder().object_hook() expects input as return of json.loads(s).
    # There are four different types of input: dict, list, int, str.
    # AnsibleJSONDecoder().object_hook() should return the same type of input.

    secret = 'secret'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secret)

    # Test for `dict`

    # the entries are zipped into a list and then passed to the dict() constructor.
    # Input (__ansible_vault):
    #   {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;dan\n3132333435363738393031323334353637383930313233343536373839303132333435363738

# Generated at 2022-06-13 06:44:40.660642
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:44:55.195339
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret1', 'secret2']
    AnsiJsonDec = AnsibleJSONDecoder()
    AnsiJsonDec.set_secrets(secrets)

    # Test of the __ansible_vault hook
    test_dict = {"__ansible_vault": "secret1\nsome string\nsecret2"}
    assert test_dict["__ansible_vault"] == "secret1\nsome string\nsecret2"
    test_dict_2 = AnsiJsonDec.object_hook(test_dict)
    assert type(test_dict_2["__ansible_vault"]) == AnsibleVaultEncryptedUnicode
    assert test_dict_2['__ansible_vault'].vault.secrets == secrets

# Generated at 2022-06-13 06:45:01.936961
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    a = {"__ansible_vault": "string", "__ansible_unsafe": "string"}
    a_encoded = json.dumps(a)
    a_decoded = json.loads(a_encoded, cls=AnsibleJSONDecoder)

    assert isinstance(a_decoded["__ansible_vault"], AnsibleVaultEncryptedUnicode)
    assert isinstance(a_decoded["__ansible_unsafe"], AnsibleUnsafeText)

# Generated at 2022-06-13 06:45:12.555551
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    test_data = dict(
        ansible_vault = dict(
            obj = dict(
                __ansible_vault = '$ANSIBLE_VAULT;1.1;AES256',
                __ansible_vault_data = 'foo'
            ),
            expected = AnsibleVaultEncryptedUnicode('foo')
        ),
        ansible_unsafe = dict(
            obj = dict(
                __ansible_unsafe = 'foo'
            ),
            expected = wrap_var('foo')
        )
    )

    for item in test_data.itervalues():
        assert AnsibleJSONDecoder.object_hook(item['obj']) == item['expected']

# vim: set et ts=4 sw=4 ft=python:

# Generated at 2022-06-13 06:45:22.287254
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert json.loads('{"a": "test"}', cls=AnsibleJSONDecoder) == {"a": "test"}
    assert json.loads('{"__ansible_vault": "test"}', cls=AnsibleJSONDecoder) == {"__ansible_vault": "test"}
    assert json.loads('{"__ansible_unsafe": "test"}', cls=AnsibleJSONDecoder) == {"__ansible_unsafe": "test"}
    # __ansible_vault is the first key
    assert json.loads('{"__ansible_vault": "test", "a": "test"}', cls=AnsibleJSONDecoder) == {"__ansible_vault": "test"}
    # ansible_unsafe is the first key

# Generated at 2022-06-13 06:45:26.743298
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    AnsibleJSONDecoder.set_secrets([])
    value = {
        '__ansible_vault': 'AAAA',
        '__ansible_unsafe': 'ZZZZ',
    }
    decoder = AnsibleJSONDecoder()

    # Expected result
    expected = {
        AnsibleVaultEncryptedUnicode('AAAA'): None,
        wrap_var('ZZZZ'): None,
    }

    # Assert
    assert decoder.object_hook(value) == expected


# Generated at 2022-06-13 06:45:38.375127
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:48.064661
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:55.847185
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault = {'__ansible_vault': u'$ANSIBLE_VAULT;1.2;AES256;' + base64.b64encode(
        b'601a7a171c1e1e1d' + b'13011208181a3c3a' + b'20151b1e1a27190f' + b'281135153c2d2b2f' + b'1d1c1e032b2e2c2f' + b'131d5c5e5b564e4f')}
    ansible_unsafe = {'__ansible_unsafe': 12345}
    playbook_vars = {'var1': 1, 'var2': 2, 'var3': 3, 'var4': 4, 'var5': 5}

   

# Generated at 2022-06-13 06:46:06.534715
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # tests for vault and unsafe proxy
    for item in [{
        "__ansible_unsafe": "foo",
        "__ansible_vault": "bar"},
        {
        "__ansible_vault": "bar",
        "__ansible_unsafe": "foo"},
    ]:
        decoded = AnsibleJSONDecoder().decode(json.dumps(item))
        # if the class instance of the value is not AnsibleVaultEncryptedUnicode
        # or not AnsibleUnsafeText, then vault or unsafe has not been loaded
        assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
        assert isinstance(decoded['__ansible_unsafe'], AnsibleUnsafeText)

    # test for other items
    decoded = Ansible

# Generated at 2022-06-13 06:46:14.931660
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    jd = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder().object_hook)
    returned_value = jd.decode('{"__ansible_unsafe": "ansible"}')
    assert returned_value == {'__ansible_unsafe': 'ansible'}



# Generated at 2022-06-13 06:46:20.859115
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets_dict = {
        'password': 'pass',
        'user': 'admin'
    }

    secrets_str = 'password=pass\nuser=admin\n'

    decoder = AnsibleJSONDecoder()

    # test __ansible_unsafe
    encoded = json.dumps({'__ansible_unsafe': '{{ user }}'})
    decoded = json.loads(encoded, cls=AnsibleJSONDecoder)
    assert decoded == wrap_var('{{ user }}')

    # test __ansible_vault (with vault secrets string)

# Generated at 2022-06-13 06:46:32.107330
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    from ansible.vars.unsafe_proxy import wrap_var

    secrets = os.environ.get('ANSIBLE_VAULT_PASSWORD_FILE')
    d = AnsibleJSONDecoder()
    d.set_secrets(secrets)

    # This is a standard json that should return unmodified
    t = {
        "key1": "example",
        "key2": 1,
        "key3": [
            "a",
            "b",
            "c"
        ],
        "key4": {
            "inner_key1": "example2",
            "inner_key2": 2
        }
    }
    assert d.object_hook(t) == t

    # This is an unsafe object that should be wrapped

# Generated at 2022-06-13 06:46:38.296201
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    secrets = {'default': 'foo'}
    decoder.set_secrets(secrets)
    vault_dict = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;default\nFoobarBase64EncodedString\n'}
    vault_object = decoder.object_hook(vault_dict)
    assert isinstance(vault_object, AnsibleVaultEncryptedUnicode)
    assert vault_object.vault.secrets['default'] == 'foo'



# Generated at 2022-06-13 06:46:43.717482
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook(dict(__ansible_vault="ciphertext"))
    assert len(pairs) == 1
    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:46:56.346328
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # prepare AnsibleJSONDecoder object
    obj = AnsibleJSONDecoder()

    # prepare objects
    obj_ansible_vault = {
        '__ansible_vault': 'foo'
    }
    obj_ansible_unsafe = {
        '__ansible_unsafe': 'foo'
    }

    # invoke object_hook with Ansible Vault object
    ansible_vault_obj = obj.object_hook(obj_ansible_vault)

    # assert Ansible Vault object
    assert isinstance(ansible_vault_obj, AnsibleVaultEncryptedUnicode)
    assert ansible_vault_obj.vault == None

    # invoke object_hook with Ansible Unsafe object
    ansible_unsafe_obj = obj.object_hook(obj_ansible_unsafe)



# Generated at 2022-06-13 06:47:03.204657
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json
    import os

    from ansible_collections.misc.not_a_real_collection.plugins.modules import test_unsafe_json

    this_dir, this_filename = os.path.split(__file__)
    data_file_path = os.path.join(this_dir, 'data', 'unsafe_json_data.json')
    with open(data_file_path, 'r') as f:
        data = json.load(f)

    # JSON does not have an ordered dict. So, the keys can be in any order when the data is loaded
    pairs = dict(data['__ansible_unsafe'])
    pairs = dict(data['__ansible_vault'])

    assert pairs == data


# Generated at 2022-06-13 06:47:14.147240
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class TestObj:
        unsafe = wrap_var('non_unsafe_class_attribute')

    obj = TestObj()
    obj.safe = 'safe_value'
    obj.unsafe = wrap_var('unsafe_value')

    secrets = 'hunter42'
    encoder = AnsibleJSONDecoder.set_secrets(secrets)

    # test for AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:23.643955
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Check that it returns the input dict as is if '__ansible_vault' is not one of the keys.
    input_dict = {'foo': 'bar', 'baz': 'qux'}
    assert input_dict == decoder.object_hook(input_dict)

    # Check that it returns a AnsibleVaultEncryptedUnicode object if the dict contains the key
    # '__ansible_vault'
    input_dict = {'__ansible_vault': 'vault_string', 'foo': 'bar', 'baz': 'qux'}
    assert isinstance(decoder.object_hook(input_dict), AnsibleVaultEncryptedUnicode)
    assert decoder.object_hook(input_dict).bytes == 'vault_string'

# Generated at 2022-06-13 06:47:31.566229
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['arun', 'hema', 'love']
    encoded_vault_secret = '$ANSIBLE_VAULT;1.1;AES256\n3537386532353165323532393337383936356566373930333864626163313830336231393639656133313862363136656435336162386263\n3163353432626339653465366231623233666139613665336531656237353466303164353339373032626161653936346337623362353761\n39666537333735393666373530396536346466373064\n'
    decoded_vault_secret = b''
    vault_decoder = AnsibleJSONDecoder()
    vault_dec

# Generated at 2022-06-13 06:47:45.115092
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = {'__ansible_vault': 'test123', 'test2': 123}
    ansible_json_decoder = AnsibleJSONDecoder()
    assert ansible_json_decoder.object_hook(obj) == {'__ansible_vault': AnsibleVaultEncryptedUnicode('test123'), 'test2': 123}

# Generated at 2022-06-13 06:47:49.692404
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'fake'
    AnsibleJSONDecoder.set_secrets(secrets)
    encoder = AnsibleJSONEncoder()
    pairs = encoder.default({u'__ansible_vault': 'fake'})
    ansible_vault = AnsibleJSONDecoder().object_hook(json.loads(pairs))
    assert isinstance(ansible_vault, AnsibleVaultEncryptedUnicode)
    assert ansible_vault.vault.secrets == 'fake'

# Generated at 2022-06-13 06:47:54.784189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = '{"__ansible_vault": "value"}'
    json_obj = json.loads(obj, cls=AnsibleJSONDecoder)
    assert isinstance(json_obj, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:48:02.817313
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    result = decoder.object_hook({'__ansible_vault': 'ABC'})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.data == 'ABC'
    assert result.vault is None

    result = decoder.object_hook({'__ansible_unsafe': {'value': 'x', 'key': 'y'}})
    assert isinstance(result, dict)
    assert result['__ansible_unsafe']['value'] == 'x'
    assert result['__ansible_unsafe']['key'] == 'y'

# Generated at 2022-06-13 06:48:10.651348
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_cases = [
        ({u'__ansible_unsafe': u'My string'}, u'My string'),
        ({u'__ansible_vault': u'My string'}, u'My string'),
        ({u'__ansible_vault': u'My string'}, u'My string'),
        ({u'__ansible_vault': u'My string', u'__ansible_unsafe': u'My string'}, u'My string'),
        ({u'__ansible_unsafe': u'My string', u'__ansible_vault': u'My string'}, u'My string'),
    ]

    for test_case in test_cases:
        result = AnsibleJSONDecoder.object_hook(test_case[0])
        assert result == test_case[1]


# Unit test

# Generated at 2022-06-13 06:48:21.267775
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret1']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

    # Vault
    test_dict = decoder.decode('{"__ansible_vault": "encoded_vault"}')
    # Make sure that vault is decoded
    assert isinstance(test_dict, AnsibleVaultEncryptedUnicode)
    # Make sure that vault is decoded
    assert test_dict.vault is not None
    # Make sure we got the same vault instance
    assert test_dict.vault is decoder._vaults['default']

    # Unsafe
    test_dict = decoder.decode('{"__ansible_unsafe": "unsafe_value"}')
    assert isinstance(test_dict, wrap_var)
    assert test_dict == wrap_

# Generated at 2022-06-13 06:48:28.016846
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    AnsibleJSONDecoder.set_secrets([''])

# Generated at 2022-06-13 06:48:34.513886
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = {
        "__ansible_vault": "vaulted text",
        "__ansible_unsafe": "unsafe text",
        "text": "normal text",
    }
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(json_data)
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert result['__ansible_vault'].vault is None
    assert result['__ansible_unsafe'] == wrap_var("unsafe text")
    assert result['text'] == "normal text"


# Generated at 2022-06-13 06:48:48.241992
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = {
        "_meta": {
            "hostvars": {
                "test_host": {
                    "__ansible_vault": "vault_password",
                    "__ansible_unsafe": "unsafe_password"
                }
            }
        }
    }

    result = AnsibleJSONDecoder.object_hook(test_data)
    assert isinstance(result['_meta']['hostvars']['test_host']['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(result['_meta']['hostvars']['test_host']['__ansible_unsafe'], wrap_var)



# Generated at 2022-06-13 06:48:53.679257
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder().object_hook({'__ansible_vault':'test__ansible_vault', '__ansible_unsafe':'test__ansible_unsafe'})
    assert(decoder['__ansible_vault'] is not None)
    assert(decoder['__ansible_unsafe'] is not None)

# Generated at 2022-06-13 06:49:11.136375
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # test with a simple vault
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['testpw'])
    json_val_vault = '{"__ansible_vault":"$ANSIBLE_VAULT;1.2;AES256;default34665\n3036333539663733306636383138653636353161653864613339316132323665366233383430\n6537353362646538346436383563653239623934363132643565\n"}'

# Generated at 2022-06-13 06:49:22.896752
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create an empty vault and add the password to it
    vault = VaultLib(secrets=['password'])

    # Convert the vault object to a string
    vault_string = AnsibleJSONEncoder().encode(vault)

    # Create the ansible vault string
    value = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.2;AES256;default%0A" + vault_string)

    # Create the json string
    json_string = json.dumps(dict(__ansible_vault=value))

    # Create the AnsibleJSONDecoder object
    decoder = AnsibleJSONDecoder()

    # Add the vault to the vault dictionary of AnsibleJSONDecoder
    decoder._vaults['default'] = vault

    # Call object_hook on the json string
    decoder.raw_

# Generated at 2022-06-13 06:49:35.479371
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:44.441286
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:55.244676
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import unittest2 as unittest

    class AnsibleJSONDecoder_object_hook_TestCase(unittest.TestCase):

        def test_object_hook(self):

            v = '76616c7565'
            vault = '$ANSIBLE_VAULT;1.1;AES256\n'
            vault += '383464313631653235316532393466666530316535393335343431636662363865636436326536\n'
            vault += '316434376162666432343334326334663039396636373762323938633362323962626164633131\n'

# Generated at 2022-06-13 06:50:05.614860
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_pass = 'secret'

# Generated at 2022-06-13 06:50:13.737049
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_password = 'secret'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets([vault_password])


# Generated at 2022-06-13 06:50:25.580107
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    jsn = {'__ansible_vault': 'VGVzdCBmb3IgVmF1bHQuCg=='}
    out = decoder.decode(json.dumps(jsn))
    assert(isinstance(out['__ansible_vault'], AnsibleVaultEncryptedUnicode))
    assert(out['__ansible_vault'].vault is None)
    assert(out['__ansible_vault'] == 'Test for Vault.\n')

# Generated at 2022-06-13 06:50:36.749627
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class FakeVault:
        def decrypt(self, value):
            return 'bar'

    data = {'__ansible_vault': 'foo'}
    ansible_vault_json = json.dumps(data)

    # test value is not wrapped
    assert type(json.loads(ansible_vault_json, cls=AnsibleJSONDecoder)) == dict

    # test value is wrapped
    AnsibleJSONDecoder.set_secrets(['foo'])
    assert type(json.loads(ansible_vault_json, cls=AnsibleJSONDecoder)) == AnsibleVaultEncryptedUnicode

    # test value is wrapped but not decrypted
    class TestVault:
        def decrypt(self, value):
            raise Exception
    AnsibleJSONDecoder._vaults['default'] = Test

# Generated at 2022-06-13 06:50:48.838260
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock

    data = '{"__ansible_vault": "vault-data"}'
    with patch('ansible.module_utils.common.json.AnsibleVaultEncryptedUnicode') as mock_vault:
        mock_vault.return_value = mock_vault
        AnsibleJSONDecoder._vaults = {'default': MagicMock()}
        AnsibleJSONDecoder.object_hook(json.loads(data))
        assert mock_vault.call_args[0][0] == 'vault-data'
        assert mock_vault.return_value.vault == AnsibleJSONDecoder._vaults['default']


# Generated at 2022-06-13 06:51:03.272676
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()

    # case 1:
    input_data = {'__ansible_vault': '12345'}
    result = ansible_json_decoder.object_hook(input_data)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:51:16.090356
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test AnsibleVaultEncryptedUnicode is returned
    decoder = AnsibleJSONDecoder()
    pairs = dict()

# Generated at 2022-06-13 06:51:23.394787
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    dec = AnsibleJSONDecoder()