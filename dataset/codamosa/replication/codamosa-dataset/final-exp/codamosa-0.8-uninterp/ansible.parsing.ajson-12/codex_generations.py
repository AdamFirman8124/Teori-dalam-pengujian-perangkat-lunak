

# Generated at 2022-06-13 06:41:32.286335
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()
    decrypted_val = decoder.object_hook({"__ansible_vault": "encoded_vault_field"})
    assert isinstance(decrypted_val, AnsibleVaultEncryptedUnicode)
    assert decrypted_val.vault is None

    class Secret():
        def load(vault, id, password):
            return password
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets([Secret()])
    decrypted_val = decoder.object_hook({"__ansible_vault": "encoded_vault_field"})
    assert isinstance(decrypted_val, AnsibleVaultEncryptedUnicode)
    assert decrypted_val.vault


# Generated at 2022-06-13 06:41:42.399762
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()
    ansible_json_decoder._vaults = {'default': 'Vault-1'}
    pairs = {'__ansible_vault': '__ANSIBLE_VAULT__', 'a': 'b'}
    pairs = ansible_json_decoder.object_hook(pairs)
    assert pairs['__ansible_vault'] == '__ANSIBLE_VAULT__'
    assert pairs['__ansible_vault'].vault == 'Vault-1'
    assert pairs['a'] == 'b'
    pairs = {'__ansible_unsafe': '__ANSIBLE_UNSAFE__'}
    pairs = ansible_json_decoder.object_hook(pairs)
    assert pairs['__ansible_unsafe']._

# Generated at 2022-06-13 06:41:52.209987
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Test object_hook method of class AnsibleJSONDecoder
    '''
    pairs = json.loads('{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;ansible\r\ntest\r\nexample"}')
    assert isinstance(pairs, dict)

    pairs = json.loads('{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;ansible\r\ntest\r\nexample"}', cls=AnsibleJSONDecoder)
    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:41:56.709941
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = [
        {'__ansible_unsafe': 'badstuff!!'},
        {'__ansible_vault': 'badvaultstuff!!'}
    ]

    for item in test_data:
        obj = json.loads(json.dumps(item), cls=AnsibleJSONDecoder)
        assert obj == item

# Generated at 2022-06-13 06:42:00.976409
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(('password',))

# Generated at 2022-06-13 06:42:13.948430
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # first test: normal case
    decoder = AnsibleJSONDecoder()
    obj = {
        "__ansible_vault": "test_value",
        "__ansible_unsafe": "test_value",
        "__ansible_not_unsafe": "test_value"
    }
    result = decoder.object_hook(obj)
    assert result == {
        "__ansible_vault": AnsibleVaultEncryptedUnicode('test_value'),
        "__ansible_unsafe": wrap_var('test_value'),
        "__ansible_not_unsafe": 'test_value'
    }

    # second test: object_hook is not called when not needed, no new object is created

# Generated at 2022-06-13 06:42:20.529647
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:25.649979
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:35.754605
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    def object_hook(pairs):
        return pairs

    json_decoder = AnsibleJSONDecoder(object_hook=object_hook)

    pairs = json_decoder.object_hook({
        '__ansible_vault': 'vault_data'
    })

    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)
    assert pairs.vault is None
    assert str(pairs) == 'vault_data'

    # init a decoder with secret provided
    json_decoder = AnsibleJSONDecoder()
    json_decoder.set_secrets(['secrets'])

    pairs = json_decoder.object_hook({
        '__ansible_vault': 'vault_data'
    })


# Generated at 2022-06-13 06:42:48.055977
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    sample_json = '''
    {
      "encrypted": {
        "__ansible_vault": "AbCdEf123456"
      },
      "unsafe": {
        "__ansible_unsafe": true,
        "__ansible_module_name": "setup"
      }
    }
    '''

    decoder = AnsibleJSONDecoder()
    json_obj = json.loads(sample_json, cls=decoder)

    assert isinstance(json_obj['encrypted'], AnsibleVaultEncryptedUnicode)
    assert json_obj['encrypted'].value == 'AbCdEf123456'

    assert json_obj['unsafe']['__ansible_unsafe'] is wrap_var(True)

# Generated at 2022-06-13 06:42:58.318227
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['foo']
    ansible_json_decoder = AnsibleJSONDecoder.set_secrets(secrets)
    a = [{"foo": "bar", "baz": {"a": "b"}, "blah": [1, 2, 3]}]
    b = json.dumps(a, indent=4, cls=AnsibleJSONEncoder)
    c = json.loads(b, cls=AnsibleJSONDecoder)
    assert isinstance(c, list)
    for i in c:
        assert isinstance(i, dict)
        assert not isinstance(i['foo'], AnsibleVaultEncryptedUnicode)
        assert not isinstance(i['baz'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:43:06.170335
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for value '__ansible_vault'
    json_decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;foobar'}
    decoded_value = json_decoder.object_hook(pairs)
    assert isinstance(decoded_value, AnsibleVaultEncryptedUnicode)
    assert decoded_value.data == '$ANSIBLE_VAULT;1.1;AES256;foobar'

    # Test for vault
    json_decoder = AnsibleJSONDecoder()
    vault = VaultLib(secrets=['f00b4r'])
    json_decoder._vaults['default'] = vault

# Generated at 2022-06-13 06:43:13.463074
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    TEST_SECRETS = 'secret'

# Generated at 2022-06-13 06:43:21.416976
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Secret string that is tested for successfully decoding
    secret_string = 'test_set_secret_string'

    # Dict with key and value for secret string
    test_dict = {'__ansible_vault': secret_string}

    # Json string for testing the decoder
    test_json = '{"__ansible_vault": "' + secret_string + '"}'

    # Object of class AnsibleJSONDecoder
    decoder = AnsibleJSONDecoder()

    # Set secret string for the decoder
    decoder.set_secrets(secret_string)

    # Assert if decode method of decoder object returns a dict.
    assert(decoder.decode(test_json) == test_dict)

# Generated at 2022-06-13 06:43:31.673038
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          646461376139326465316662506537663332636461353736653063323131653965653533663831\n          636534353637663266653362636231306634353336353839\n          3472616e6b65723d666f7860\n          "\

    vault_dict = {"__ansible_vault": vault}

    json_string = json.dumps(vault_dict)
    decoded_dict = json.loads(json_string, cls=AnsibleJSONDecoder)

    assert decoded_dict == vault_dict

    secrets = ['vault-password']

# Generated at 2022-06-13 06:43:39.230241
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # `AnsibleVaultEncryptedUnicode` instances are created
    # when decoding JSON files of ansible-playbook commands
    # when the command includes the option `--vault-password-file`
    # or the environment variable `ANSIBLE_VAULT_PASSWORD_FILE`
    # or the file `~/.ansible/vault_pass.txt` exists.
    # The constructor of `AnsibleVaultEncryptedUnicode` class
    # calls `VaultLib` class to decrypt the encrypted value.
    # In the unit test, we use a dummy secret value for now
    # to pass the test.
    AnsibleJSONDecoder.set_secrets(
        secrets=['dummy_secret_value',]
    )

    # Example of a value in a JSON file
    # of an ansible-playbook

# Generated at 2022-06-13 06:43:47.135765
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    result = AnsibleJSONDecoder.object_hook({'__ansible_vault': 'encrypted', '__ansible_unsafe': "unsafe"})
    assert result['__ansible_vault'] == 'encrypted'
    assert type(result['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert result['__ansible_unsafe'] == "unsafe"
    assert type(result['__ansible_unsafe']) == AnsibleVaultEncryptedUnicode



# Generated at 2022-06-13 06:43:54.942797
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = str(b'\x01\x00\x00\x00\x05\x00\x00\x0012345').encode('hex')
    secrets = [secret,]
    jd = AnsibleJSONDecoder()
    jd.set_secrets(secrets)
    obj = json.loads('''{
        "A": "B",
        "__ansible_vault": "64f712ca92625f38582e0a7e8cceb59a7b12e0b2d7fb8f1c",
        "__ansible_unsafe": "C"
    }''', cls=jd)
    assert isinstance(obj['A'], str)

# Generated at 2022-06-13 06:44:08.848438
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = '$ANSIBLE_VAULT;6.0;AES256'
    secrets += '\naGFzaHZhbHVl\nZW50aXRsZWU='
    AnsibleJSONDecoder.set_secrets(secrets)
    json_str = '{"__ansible_vault": "ZA==", "__ansible_unsafe": "bW92ZQ=="}'
    result = AnsibleJSONDecoder().decode(json_str)
    # the result should be a dict with the __ansible_vault key replaced by an instance of AnsibleVaultEncryptedUnicode
    # and the __ansible_unsafe key replaced by the decoded value of the b64 encoded string
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:44:20.570246
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    encoder = json.JSONEncoder(cls=AnsibleJSONEncoder)
    encoder.set_secrets(['hunter2'])

    v = AnsibleVaultEncryptedUnicode('hello'.encode('utf8'))
    v.vault = VaultLib(secrets=['hunter2'])
    v_encoded = encoder.default(v)

    decoder = json.JSONDecoder()
    decoder.object_hook = AnsibleJSONDecoder.object_hook
    v_decoded = decoder.decode(v_encoded)

    assert v_encoded == '{"__ansible_vault": "b61d'
    assert v_decoded['__ansible_vault'] == 'hello'
    assert v_decoded['__ansible_vault'].vault is not None

# Generated at 2022-06-13 06:44:30.498618
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_key = '$ANSIBL~1'
    decode_secrets = [secret_key]

# Generated at 2022-06-13 06:44:36.536015
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoded = json.loads('{"__ansible_unsafe": "test_value"}', cls=AnsibleJSONDecoder)
    assert decoded == wrap_var('test_value')

    decoded = json.loads('{"__ansible_vault": "test_value"}', cls=AnsibleJSONDecoder)
    assert decoded == AnsibleVaultEncryptedUnicode('test_value')



# Generated at 2022-06-13 06:44:40.796118
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {
        '__ansible_vault': 'my_vault_value',
        '__ansible_unsafe': "my_unsafe_value",
    }
    result = decoder.object_hook(pairs)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    result = decoder.object_hook(result.to_data())
    assert result == pairs

# Generated at 2022-06-13 06:44:55.264903
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_password = 'secret'
    vault_text = b'$ANSIBLE_VAULT;1.2;AES256;default\n3633656434663564383437383634303832626264373563656335646236616637353037383666\n353033656163346532636361326133393234316362376533303362636639343332366163366638\n3834383861316566\n'
    vault_text = vault_text.decode('utf-8')

# Generated at 2022-06-13 06:45:06.736226
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test case for when encrypted string is passed
    class TestVaultLib:
        def __init__(self, secrets):
            self.secrets = secrets

        def load(self):
            return str(self.secrets)

    test_AnsibleJSONDecoder = AnsibleJSONDecoder()
    test_AnsibleJSONDecoder.set_secrets(TestVaultLib('secret'))
    decoded_object = test_AnsibleJSONDecoder.object_hook({ "__ansible_vault": "jA0EAwMCqj+rW8yHlY5mjobecO+gUoeR6fZGmUHJ6pZWrGX9c/pzDYz/C6TEfv2D" })


# Generated at 2022-06-13 06:45:15.598401
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = "test"
    json_str = """{
        {
            "__ansible_vault": "ansible_vault_value"
        }
    }"""
    AnsibleJSONDecoder.set_secrets(secret)
    ansible_json = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert isinstance(ansible_json['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert "ansible_vault_value" in ansible_json['__ansible_vault']
    assert secret in ansible_json['__ansible_vault'].vault.secrets


# Generated at 2022-06-13 06:45:24.401152
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import unittest
    class AnsibleJSONDecoderTest(unittest.TestCase):
        def test_AnsibleJSONDecoder_object_hook(self):
            decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:45:36.256963
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import text_type
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    test_str = 'test_str'
    test_bytes = 'test_bytes'
    test_vault_encrypted_str = '$ANSIBLE_VAULT;1.1;AES256;test\ntest\n'
    test_vault_encrypted_bytes = b'$ANSIBLE_VAULT;1.1;AES256;test\ntest\n'

    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_unsafe': test_str}) == AnsibleUnsafeText(test_str)

# Generated at 2022-06-13 06:45:46.642853
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_obj = {"__ansible_vault": "hello", "__ansible_unsafe": "world"}
    json_str = json.dumps(json_obj)
    # default object_hook is None
    obj = json.loads(json_str)
    assert obj['__ansible_vault'] == 'hello'
    assert obj['__ansible_unsafe'] == 'world'
    # specify our own object_hook
    obj = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert isinstance(obj['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert obj['__ansible_vault'].vault
    assert str(obj['__ansible_vault']) == 'hello'

# Generated at 2022-06-13 06:45:51.412826
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret
    vault_secret = VaultSecret('my_secret', b'12345')
    AnsibleJSONDecoder.set_secrets(vault_secret)
    in_string = b'{"__ansible_vault": "pXLk59aP8A/N3qSgIwPUlw=="}'
    result = AnsibleJSONDecoder().decode(in_string)
    assert (result == b'12345')
    assert (result.vault == AnsibleJSONDecoder._vaults['default'])

# Generated at 2022-06-13 06:45:56.605614
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook( { '__ansible_vault': 'test' } ) == AnsibleVaultEncryptedUnicode( 'test' )
    assert decoder.object_hook( { '__ansible_unsafe': 'test' } ) == wrap_var( 'test' )

# Generated at 2022-06-13 06:46:01.489963
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Need to initialize the '_vaults' class variable with an object of class VaultLib
    # before calling the test_object_hook() method since the object_hook() method
    # uses the '_vaults' class variable internally
    # The test_object_hook() method internally calls the object_hook() method of the
    # AnsibleJSONDecoder class
    AnsibleJSONDecoder._vaults['default'] = VaultLib()
    assert test_object_hook()



# Generated at 2022-06-13 06:46:14.197514
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = b'''
    {
        "__ansible_vault": "vault_data",
        "__ansible_unsafe": "unsafe_data",
        "other_data": "something",
        "another_var": "another_value"
    }
    '''
    expected = {
        '__ansible_vault': 'vault_data',
        '__ansible_unsafe': 'unsafe_data',
        'other_data': 'something',
        'another_var': 'another_value'
    }
    assert expected == ANSIBLE_JSON_DECODER.decode(test_data)

ANSIBLE_JSON_DECODER = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:46:17.076841
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_arg = json.dumps({'__ansible_unsafe': "{{ vars_var }}"})
    unsafe_proxy = AnsibleJSONDecoder().object_hook(json.loads(json_arg))
    assert isinstance(unsafe_proxy, wrap_var)

# Generated at 2022-06-13 06:46:21.848613
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class MockVaultLib(object):
        def decrypt(self, *args, **kwargs):
            return ''

    secrets = ['password']
    json_string = '{"__ansible_vault": "123abc", "__ansible_unsafe": "456def", "__ansible_vault2": "789ghi"}'
    json_object = {"__ansible_vault": "123abc", "__ansible_unsafe": "456def", "__ansible_vault2": "789ghi"}
    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    decoder._vaults = {'default': MockVaultLib()}

    assert decoder.decode(json_string) == json_object

# Generated at 2022-06-13 06:46:27.865085
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault_secret = '$ANSIBLE_VAULT;1.1;AES256'
    value = AnsibleJSONEncoder.safe_encode(value=vault_secret, secret=vault_secret)
    assert decoder.object_hook({'__ansible_vault': value}) == AnsibleVaultEncryptedUnicode(value)

# Generated at 2022-06-13 06:46:35.054695
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'}
    new_pairs = decoder.object_hook(pairs)
    assert new_pairs['__ansible_vault'] == 'foo'
    assert new_pairs['__ansible_unsafe'] == 'bar'
    assert type(new_pairs['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert type(new_pairs['__ansible_unsafe']) == AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:46:46.533930
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import unittest

    class TestAnsibleJSONDecoder_object_hook(unittest.TestCase):

        def test_object_hook(test_self):
            from ansible.parsing.yaml.dumper import AnsibleDumper

            d = AnsibleJSONDecoder()
            ad = AnsibleDumper()

# Generated at 2022-06-13 06:46:54.087374
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:47:01.658917
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:47:12.468943
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest
    import os

    test_data = '''
    {
        "__ansible_vault": "vault_data",
        "__ansible_unsafe": {"key1": "value1", "key2": "value2"}
    }
    '''

    # Set up a vault secret and decoder
    secret = os.urandom(16).encode('hex')
    AnsibleJSONDecoder.set_secrets(secrets=[secret])
    decoder = AnsibleJSONDecoder()

    # Decode the test data
    test_data = decoder.decode(test_data)
    assert isinstance(test_data['__ansible_vault'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:47:22.858505
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test data for test_AnsibleJSONDecoder_object_hook
    ansible_vault_encrypted_unicode = {'__ansible_vault': 'test value'}

    # Start test_AnsibleJSONDecoder_object_hook
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(ansible_vault_encrypted_unicode)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == None
    assert unicode(result) == u'test value'
    assert str(result) == 'test value'
    assert bytes(result) == 'test value'
    assert ansible_vault_encrypted_unicode['__ansible_vault'] == result.vault_data
    assert result == 'test value'
    assert result

# Generated at 2022-06-13 06:47:30.751810
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    v = '$ANSIBLE_VAULT;1.1;AES256\n33623432383364353465396533393231316132353366393566663836303666313331386637303463\n38343561323133613561326133616233343734356466363064663362623063313734306236653937\n6438326134633530646633356466\n'
    d = {'__ansible_vault': v}
    decoder = AnsibleJSONDecoder()

    # Check to see if the encrypted vault value is properly converted to
    # the appropriate AnsibleVaultEncryptedUnicode object
    assert '__ansible_vault' in decoder.object_hook(d)

# Generated at 2022-06-13 06:47:42.726393
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create a vault and add a safe secret to it
    vault = VaultLib(['myvaultpass'])
    vault.update({'secret_stuff': 'deploy_ssh_key: "foobar"'})
    secrets = vault.dump()

    # Test the decoder with an empty dict, it should return a dict
    decoder = AnsibleJSONDecoder()
    assert(isinstance(decoder.object_hook({}), dict))

    # Test the decoder with a vault encrypted variable __ansible_vault
    # It should return an AnsibleVaultEncryptedUnicode object with
    # the decoded variable
    decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:47:49.115225
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    test_case_1 = {"__ansible_vault": "ansible vault encrypted string"}
    result_1 = AnsibleJSONDecoder.object_hook(test_case_1)
    assert "__ansible_vault" in result_1
    assert isinstance(result_1['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert result_1['__ansible_vault'].vault is None
    assert result_1['__ansible_vault'] == "ansible vault encrypted string"

    result_2 = json.loads(json.dumps(test_case_1), cls=AnsibleJSONDecoder)
    assert "__ansible_vault" in result_2

# Generated at 2022-06-13 06:48:01.413828
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:05.451505
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = '''
{"foo": "bar", "__ansible_unsafe": "VALIDATED CONTENT", "baz": {"__ansible_vault": "AQAAAAEAACZQb2NrZXRwcmVzc2lvbgAAAABhY2Nlc3MAAQAAAA=="}}

'''
    json_data_expected = '{"baz": {"__ansible_vault": "AQAAAAEAACZQb2NrZXRwcmVzc2lvbgAAAABhY2Nlc3MAAQAAAA==", "value": "secret"}, "foo": "bar", "__ansible_unsafe": "VALIDATED CONTENT"}'

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets({'vault_password': 'secret'})


# Generated at 2022-06-13 06:48:12.447615
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class myAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):

        def __init__(self, data, vault):
            super(myAnsibleVaultEncryptedUnicode, self).__init__(data)
            self._vault = vault

    jd = AnsibleJSONDecoder(vault_secrets=['FAKE'])

    class AnsibleVaultEncryptedUnicodeStub(object):

        def __init__(self, data, vault):
            self.data = data
            self.vault = vault

    class VaultLibStub(object):

        def __init__(self, secrets):
            self.secrets = secrets


# Generated at 2022-06-13 06:48:22.684112
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import unittest

    # create instances of class AnsibleJSONDecoder
    ansible_json_decoder_0 = AnsibleJSONDecoder()
    ansible_json_decoder_1 = AnsibleJSONDecoder()

    # set values of secret
    # AnsibleJSONDecoder.set_secrets not implemented.
    #ansible_json_decoder_0.set_secrets("'n")
    #ansible_json_decoder_1.set_secrets("'n")

    # create instances of class AnsibleVaultEncryptedUnicode and set values
    ansible_vault_encrypted_unicode_0 = AnsibleVaultEncryptedUnicode()
    ansible_vault_encrypted_unicode_0.vault = ansible_json_decoder_0
    ansible_vault_encrypted_

# Generated at 2022-06-13 06:48:33.152682
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class MyVault(object):
        def decrypt(self, val):
            return val.replace('hello', 'world')

    test_data_1 = {'ansible': {'var': '__ansible_vault'}}
    serialized_test_data_1 = json.dumps(test_data_1, cls=AnsibleJSONEncoder)
    expected_result_1 = '{"ansible": {"var": "__ansible_vault"}}'
    assert serialized_test_data_1 == expected_result_1

    deserialized_test_data_1 = json.loads(serialized_test_data_1, cls=AnsibleJSONDecoder)
    expected_result_1 = {u'ansible': {u'var': u'__ansible_vault'}}
    assert deserial

# Generated at 2022-06-13 06:48:53.063518
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # For encrypted string
    json_string = '{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;test01\n37313761376334396231666265333563393763636163323865312c39366338323931653430\n3864316230323137663134666433323361303264\n","key1": "value1", "key2": "value2"}'
    dict_string = decoder.decode(json_string)

# Generated at 2022-06-13 06:48:57.351123
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Unit test for method object_hook of class AnsibleJSONDecoder
    """
    json_str = r'''{ "__ansible_unsafe": "this is unsafe" }'''
    value = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert value['__ansible_unsafe'] == 'this is unsafe'

# Generated at 2022-06-13 06:49:07.725096
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    data = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;foo\nbar'}
    decoded = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook).decode(json.dumps(data))
    assert isinstance(decoded, dict), 'AnsibleJSONDecoder.object_hook did not return a dict'
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode), 'AnsibleJSONDecoder.object_hook did not return an AnsibleVaultEncryptedUnicode'

# Generated at 2022-06-13 06:49:13.684846
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    payload = {"__ansible_unsafe": "password"}
    message = decoder.object_hook(payload)
    assert isinstance(message, object)
    assert isinstance(message['__ansible_unsafe'], object)
    payload = {"__ansible_vault": "password"}
    message = decoder.object_hook(payload)
    assert isinstance(message, object)
    assert isinstance(message['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(decoder, object)

# Generated at 2022-06-13 06:49:24.231638
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class AnsibleJSONDecoder_object_hook_TestCase(unittest.TestCase):
        def test_ansible_vault_prefixed_key(self):
            decoder = AnsibleJSONDecoder()
            decoded = decoder.object_hook({'__ansible_vault': 'abc'})
            self.assertTrue(isinstance(decoded, AnsibleVaultEncryptedUnicode))
            self.assertEqual(decoded, 'abc')
            self.assertEqual(decoded.vault, None)

        def test_ansible_vault_prefixed_key_with_passwords(self):
            decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:49:36.347069
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_string = '{"__ansible_vault": "ANSIBLE_VAULT;1.1;AES256 \n636165386537653633393065373734306334366331343739373864336239633465613761346132 \n306635636336306135643835663262643766633035373263386666653366663665363264653638 \n373263326632393962343366353639663465626538353465663633396635346162326233386234 \n336162336436616561356236303763326364313465616163313232326533306531626264323937 \n63666335633831613263316338658\n"}'
    json_data = json

# Generated at 2022-06-13 06:49:45.031731
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import yaml

    class TestCls:
        def __init__(self):
            self.test_str = "1234"

    # AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:49:55.638670
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:05.813134
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Set ansible vault secrets
    secrets = 'test'
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:50:15.680997
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    import pytest

    # Test with empty vault
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;some_id\n3333333333333333333333333333333333333', '__ansible_unsafe': wrap_var('some text')}
    out = decoder.object_hook(pairs)
    assert AnsibleVaultEncryptedUnicode == type(out['__ansible_vault'])
    assert AnsibleVaultEncryptedUnicode(pairs['__ansible_vault']) == out['__ansible_vault']
    assert wrap_var('some text') == out['__ansible_unsafe']

    # Test with a vault
    vault_password = 'vault_password'
    secret_

# Generated at 2022-06-13 06:50:34.939777
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['bar', 'baz'])

    encrypted_data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30383736346631333164663635356138303635346661323631623538373338363639336264343734\n          30346535376635313762643665643734353266616562303036636130336534393033343262333330\n          3266613437353461\n          '

    result = decoder.object_hook({'__ansible_vault': encrypted_data})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault is not None

# Generated at 2022-06-13 06:50:47.896377
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:55.293470
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test vault variable
    value = decoder.object_hook({'__ansible_vault': 'AAA'})
    assert value.vault is None
    assert value.vault_id == 'default'
    assert value.vault_password is None
    assert value == 'AAA'

    # Test unsafe variable
    json_obj = {'__ansible_unsafe': True}
    value = decoder.object_hook(json_obj)
    assert value == json_obj

    # Test non-Ansible variable
    json_obj = {'AAA': 'BBB'}
    value = decoder.object_hook(json_obj)
    assert value == json_obj

# Generated at 2022-06-13 06:51:00.523056
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:51:07.413365
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}
    assert decoder.object_hook(pairs) == AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')
    pairs = {'__ansible_unsafe': '$ANSIBLE_UNSAFE'}
    assert decoder.object_hook(pairs) == wrap_var('$ANSIBLE_UNSAFE')
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256', '__ansible_unsafe': '$ANSIBLE_UNSAFE'}

# Generated at 2022-06-13 06:51:18.752443
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    AVU = AnsibleVaultEncryptedUnicode
    msg1 = "Vault password must be set via the 'secrets' argument"
    msg2 = "'secrets' parameter must be a list or tuple"

    # no vault passwords
    assert AnsibleJSONDecoder.object_hook({}) == {}

    # invalid vault password
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'foo'}) == {'__ansible_vault': 'foo'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'foo'}) == {'__ansible_vault': 'foo'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'foo'}) == {'__ansible_vault': 'foo'}
    assert Ans

# Generated at 2022-06-13 06:51:26.132361
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = '123456789012'
    test_vault = '!vault |\n' + secret
    obj = json.loads(test_vault, cls=AnsibleJSONDecoder)
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj.vault.secrets == [secret]
