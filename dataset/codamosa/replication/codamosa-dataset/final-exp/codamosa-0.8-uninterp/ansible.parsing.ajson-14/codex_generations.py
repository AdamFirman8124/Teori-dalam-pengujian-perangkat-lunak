

# Generated at 2022-06-13 06:41:31.868007
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Test method AnsibleJSONDecoder.object_hook()
    '''
    testvault = {'foo': 'test'}
    testsecret = 'testsecret'
    AnsibleJSONDecoder.set_secrets(testsecret)

    # Test AnsibleVaultEncryptedUnicode creation
    data = '{"__ansible_vault": "test1", "foo": "bar"}'
    result = json.loads(data, cls=AnsibleJSONDecoder)
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert result['__ansible_vault'].vault == AnsibleJSONDecoder._vaults['default']

    # Test wrap_var

# Generated at 2022-06-13 06:41:42.032333
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_file = 'tests/utils/vault/test.yaml'

# Generated at 2022-06-13 06:41:54.016619
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest
    import sys
    import datetime

    assert sys.version_info[0] == 2

    assert AnsibleJSONDecoder.object_hook(None) is None

    # input should be a dictionary
    with pytest.raises(TypeError) as excinfo:
        AnsibleJSONDecoder.object_hook("test")
    assert "expected string or buffer" in str(excinfo.value)

    # key must be a string
    with pytest.raises(TypeError) as excinfo:
        AnsibleJSONDecoder.object_hook({1: "value"})
    assert "str" in str(excinfo.value)

    # value must be a string

# Generated at 2022-06-13 06:42:04.061541
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    text = """{
        "_meta": {
        "hostvars": {
            "hostname": {
            "ansible_user": "root",
            "ansible_password": "PASSWORD"
            }
        }
        },
        "all": {
        "children": [
            "ungrouped"
        ]
        },
        "ungrouped": {}
    }"""

# Generated at 2022-06-13 06:42:15.455469
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:42:19.891160
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    assert not hasattr(json, 'JSONDecoder')
    json.JSONDecoder = AnsibleJSONDecoder

    test_var = '{"__ansible_vault": "hello"}'
    result = json.loads(test_var)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result == 'hello'

    test_var = '{"__ansible_unsafe": "hello"}'
    result = json.loads(test_var)
    assert result == 'hello'

    delattr(json, 'JSONDecoder')

# Generated at 2022-06-13 06:42:33.956008
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:46.716506
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    # Test with __ansible_vault

# Generated at 2022-06-13 06:42:53.360605
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': '123'}
    expected = pairs
    expected['__ansible_vault'] = AnsibleVaultEncryptedUnicode(pairs['__ansible_vault'])
    expected['__ansible_vault'].vault = decoder._vaults['default']

    # Execute
    result = decoder.object_hook(pairs)

    # Verify
    assert result == expected

# Generated at 2022-06-13 06:43:01.368754
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class MyDecoder(AnsibleJSONDecoder):
        def __init__(self, *args, **kwargs):
            super(MyDecoder, self).__init__(*args, **kwargs)
            self._vaults['default'] = VaultLib(secrets=['mysecret'])

    # wrap_var
    data = {u'key': u'value', u'__ansible_unsafe': u'my secret'}
    result = MyDecoder().decode(json.dumps(data))
    assert isinstance(result, dict)
    assert isinstance(result['key'], unicode)
    assert result['key'] == u'value'
    assert not isinstance(result['__ansible_unsafe'], unicode)
    assert result['__ansible_unsafe'] == u'my secret'

# Generated at 2022-06-13 06:43:10.512697
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    path = 'test/vault.yml'
    vault_id = 'nosecret'
    secret = 'hush'
    vault = VaultLib([(vault_id, secret)])
    cleartext = "Vaulted Text:\n{0}".format(secret)
    ciphertext = vault.encrypt(cleartext, vault_id)
    vdata = {'__ansible_vault': ciphertext}
    vresult = json.loads(json.dumps(vdata), cls=AnsibleJSONDecoder)
    assert(vresult.data == cleartext)


# Generated at 2022-06-13 06:43:16.729665
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_input = {}
    result = AnsibleJSONDecoder.object_hook(test_input)
    assert result == test_input

    test_input = {'__ansible_vault': 'vault_value'}
    result = AnsibleJSONDecoder.object_hook(test_input)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    test_input = {'__ansible_unsafe': 'unsafe_value'}
    result = AnsibleJSONDecoder.object_hook(test_input)
    assert result == 'unsafe_value'

    test_input = {'__ansible_unsafe': unsafe_value}
    result = AnsibleJSONDecoder.object_hook(test_input)
    assert result is unsafe_value

# Generated at 2022-06-13 06:43:21.697024
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()


# Generated at 2022-06-13 06:43:31.961196
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Testing all edge cases
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'value1'}) == {'__ansible_vault': 'value1'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'value1'}) == {'__ansible_unsafe': 'value1'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_asd': 'value1'}) == {'__ansible_asd': 'value1'}
    assert AnsibleJSONDecoder.object_hook({'value': 'value1'}) == {'value': 'value1'}
    assert AnsibleJSONDecoder.object_hook([12, 'value1']) == [12, 'value1']
    assert AnsibleJSONDecoder.object_

# Generated at 2022-06-13 06:43:43.538881
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:43:53.206422
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.unsafe_proxy import wrap_var

    class DummyVault(object):
        """
        Dummy vault class for testing
        """
        @property
        def password(self):
            pass

        def decrypt(self, value):
            return value.replace('$ANSIBLE_VAULT;', '')

    decoder = AnsibleJSONDecoder()
    decoder._vaults = {
        'lnk1': DummyVault(),
        'lnk2': None,
    }
    # Test safe value
    data = {'__ansible_unsafe': 123}
    result = decoder.object_hook(data)
    assert isinstance(result, AnsibleMapping)

# Generated at 2022-06-13 06:44:06.904086
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
        object_hook method of AnsibleJSONDecoder should return AnsibleVaultEncryptedUnicode or wrap_var or pairs.
    """
    test_json = {}
    AnsibleJSONDecoder._vaults = {}
    assert AnsibleJSONDecoder.object_hook(test_json) == test_json
    test_json['__ansible_vault'] = "123456789.5"
    enc_str = AnsibleJSONDecoder.object_hook(test_json)
    assert isinstance(enc_str, AnsibleVaultEncryptedUnicode)
    assert enc_str.vault is None
    test_json['__ansible_vault'] = "123456789.5"
    AnsibleJSONDecoder._vaults['default'] = "123456789.5"
    enc_str = Ans

# Generated at 2022-06-13 06:44:18.762212
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Test with value that is not in required format
    data = { "name": "test" }
    ansible_json_decoder_obj = AnsibleJSONDecoder()
    expected_result = { "name": "test" }
    result = ansible_json_decoder_obj.object_hook(data)
    assert result == expected_result

    # Test with __ansible_vault key
    data = { "__ansible_vault": "test_value" }
    ansible_json_decoder_obj = AnsibleJSONDecoder()
    expected_result = AnsibleVaultEncryptedUnicode("test_value")
    result = ansible_json_decoder_obj.object_hook(data)
    assert result == expected_result

    # Test with __ansible_unsafe key

# Generated at 2022-06-13 06:44:27.566027
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256;user\r\n"
                                                 "61646d696e2e2067726f757020657665722074686520717569636b746f776f2e0a\r\n")
    assert json.loads(json.dumps(ansible_vault), cls=AnsibleJSONDecoder) == ansible_vault

    unsafe = wrap_var("blah blah blah")
    assert json.loads(json.dumps(unsafe), cls=AnsibleJSONDecoder) == unsafe

# Generated at 2022-06-13 06:44:38.113454
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    decoder = AnsibleJSONDecoder()
    json_str = '{"__ansible_unsafe": "__string__", "__ansible_vault": "__ansible_vault__"}'
    json_dict = {'__ansible_unsafe': '__string__', '__ansible_vault': '__ansible_vault__'}
    decoder.set_secrets([b'123'])
    assert json.loads(json_str, object_hook=AnsibleJSONDecoder.object_hook) == json_dict
    ansible_res = AnsibleVaultEncryptedUnicode(json_dict['__ansible_vault'])
    ansible_res.vault = decoder._vaults

# Generated at 2022-06-13 06:44:49.745274
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    v = 'test value'
    e = 'test encrypted value'
    u = 'test unsafe value'
    s = {'v': v, 'e': e, 'u': u}
    
    # simulate a vault password and vault object 
    jd = AnsibleJSONDecoder()
    jd._vaults['default'] = VaultLib('secret')

    # test a vault encrypted value
    pairs = {'__ansible_vault': e}
    o = jd.object_hook(pairs)
    assert v == o
    assert 'default' in o.vault.secrets

    # test a normal value
    pairs = {'v': v}
    o = jd.object_hook(pairs)
    assert s['v'] == o['v']
    assert len(o.keys()) == 1

    #

# Generated at 2022-06-13 06:44:56.014277
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from collections import namedtuple

    # This is a lot like a dict, but json.dumps produces a different
    # output than with a dict.

# Generated at 2022-06-13 06:44:59.576441
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoded = decoder.object_hook({'__ansible_unsafe': b'\xc2\xad'})
    assert decoded == wrap_var('?')



# Generated at 2022-06-13 06:45:00.440569
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pass

# Generated at 2022-06-13 06:45:11.604492
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    A = {'__ansible_vault': 'foo'}
    B = {'__ansible_unsafe': 'foo'}
    C = {'test': 'foo'}
    D = {'test': '{{ test }}'}
    E = {'test': ['{{ test }}']}

    json_decoder = AnsibleJSONDecoder()
    json_decoder.set_secrets(None)


# Generated at 2022-06-13 06:45:21.594727
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """ ansible/parsing/json/__init__.py """

    json_str = '{"__ansible_vault": "vault_str", "__ansible_unsafe": "unsafe_str"}'
    json_obj = json.loads(json_str, cls=AnsibleJSONDecoder)

    # Check if json_obj is of AnsibleVaultEncryptedUnicode class
    assert repr(json_obj['__ansible_vault']).startswith('<ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode object')
    assert json_obj['__ansible_vault'] == 'vault_str'

    # Check if json_obj is of SafeText class

# Generated at 2022-06-13 06:45:27.915578
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class MockSecrets(object):
        def __init__(self):
            self._secrets = ['supersecret']
        def get_secret(self, vault_id):
            return self._secrets[vault_id]

    secrets = MockSecrets()
    AnsibleJSONDecoder.set_secrets(secrets)


# Generated at 2022-06-13 06:45:39.509397
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Case 1: '__ansible_vault' key is not present in the object
    assert decoder.object_hook({}) == {}

    # Case 2: '__ansible_vault' key has no value
    assert decoder.object_hook({'__ansible_vault': ''}) == {'__ansible_vault': AnsibleVaultEncryptedUnicode('')}

    # Case 3: '__ansible_unsafe' key has no value
    assert decoder.object_hook({'__ansible_unsafe': ''}) == {'__ansible_unsafe': wrap_var('')}

    # Case 4: '__ansible_vault' key is present

# Generated at 2022-06-13 06:45:48.842616
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret, VaultVersionedSecret
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    secrets = ['0123456789abcdef']
    secrets_b = ['fedcba9876543210']

# Generated at 2022-06-13 06:45:56.381993
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Create an example dictionary with a __ansible_vault entry
    pairs = {
        '__ansible_vault': '!vault |\n          test_p@ssw0rd\n          ',
    }

    # Create a new AnsibleJSONDecoder object
    decoder = AnsibleJSONDecoder()

    # Use the object_hook method of the AnsibleJSONDecoder object to
    # process the example dictionary
    result = decoder.object_hook(pairs)

    # Assert that there is a __ansible_vault entry in the result
    assert result.has_key('__ansible_vault')

    # Assert that the value of the __ansible_vault entry is an
    # AnsibleVaultEncryptedUnicode object
    assert type(result['__ansible_vault']) is Ans

# Generated at 2022-06-13 06:46:07.877281
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    vault_lib = VaultLib(password='test')

    # {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;test\n65626231656232303136353762336331663633353165383736326434646433653564333232376437\n34663538373730386436333461363962336339303633643763623964666231396237613961666162\n343264656165643830366336636361363939\n'}


# Generated at 2022-06-13 06:46:08.513789
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    pass

# Generated at 2022-06-13 06:46:13.231137
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}) == AnsibleVaultEncryptedUnicode(
        '$ANSIBLE_VAULT;1.1;AES256')

# Generated at 2022-06-13 06:46:20.061445
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # Test if the given string is decoded correctly if it is encoded by AnsibleJSONEncoder
    ansible_vault_str = AnsibleJSONEncoder().encode({'__ansible_vault': 'ansible-vault-str'})
    assert decoder.decode(ansible_vault_str) == AnsibleVaultEncryptedUnicode('ansible-vault-str')

    # Test if the given string is decoded correctly if it is encoded by AnsibleJSONEncoder
    ansible_unsafe_str = AnsibleJSONEncoder().encode({'__ansible_unsafe': 'ansible-unsafe-str'})
    assert decoder.decode(ansible_unsafe_str) == wrap_var('ansible-unsafe-str')

    # Test if

# Generated at 2022-06-13 06:46:31.832653
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:46:35.589757
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    """
    Invoke AnsibleJSONDecoder.object_hook()
    """

    # Instantiate the AnsibleJSONDecoder class
    ansible_json_decoder = AnsibleJSONDecoder()

    # Invoke the object_hook() method
    result = ansible_json_decoder.object_hook()

    assert result is None


# Generated at 2022-06-13 06:46:42.494380
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def _assert_vault_object(data, secret):
        '''
        Parse json string and check that AnsibleVaultEncryptedUnicode
        object is created if json object has '__ansible_vault' key.
        '''
        decoder = AnsibleJSONDecoder()
        decoder.set_secrets(secret)
        obj = decoder.decode(data)
        assert(isinstance(obj, AnsibleVaultEncryptedUnicode))

    def _assert_unsafe_object(data):
        '''
        Parse json string and check that wrapping of unsafe objects
        is executed if json object has '__ansible_unsafe' key.
        '''
        decoder = AnsibleJSONDecoder()
        decoder.decode(data)
        obj = decoder.decode(data)


# Generated at 2022-06-13 06:46:44.109108
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    assert d.object_hook( {'__ansible_vault': "abcd"} ) == AnsibleVaultEncryptedUnicode("abcd")

# Generated at 2022-06-13 06:46:56.477920
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    text = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n61306530393839613431646238333934333633643666336232366232333033306133663537623333\n62303033363034653534303936373466336361613534653737336332613738356366316337313230\n30363765653033323366343765316663306234383261653933306536326539346462613232363837\n32643562386166656331663464353629')

    assert decoder.object_hook({"__ansible_vault": text._text}) == text

# Generated at 2022-06-13 06:47:03.847505
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    a = {"__ansible_unsafe": {'a': 1, 'b': 2, 'c': 3}}
    b = AnsibleJSONDecoder.object_hook(a)
    assert b == wrap_var(a['__ansible_unsafe'])
    c = {"__ansible_vault": "abc"}
    d = AnsibleJSONDecoder.object_hook(c)
    assert isinstance(d, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:47:17.660485
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:26.848360
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = []

# Generated at 2022-06-13 06:47:41.368494
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import StringIO

    payload = StringIO('''
#!/usr/bin/python
import json
import sys

print(json.dumps(json.loads(sys.argv[1],
                            object_hook=lambda x: {k: AnsibleVaultEncryptedUnicode(v) for k, v in x.items() if k == '__ansible_vault'}),
                 indent=2))
''')

# Generated at 2022-06-13 06:47:48.127228
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = VaultLib(secrets=['foo'])
    ansible_vault_encrypt_key = '__ansible_vault'
    ansible_unsafe_key = '__ansible_unsafe'

# Generated at 2022-06-13 06:48:00.286035
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'HASHpass']

# Generated at 2022-06-13 06:48:10.805293
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder_obj = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:48:21.379337
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {'vault_password': 'test'}
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:48:32.490057
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """
    Test case:
        [{
          "msg": "This is an encrypted string.",
          "__ansible_vault": "vault_string"
        }]
    """
    test_vault_value = "7d4a6aa9d6b5b6cc1e6c304f6d5ca582"
    # Test values
    test_values = {
        "msg": "This is an encrypted string.",
        "__ansible_vault": test_vault_value,
    }
    # Create a test JSONDecoder object
    test_json_decoder = AnsibleJSONDecoder()

    # Call object_hook method of AnsibleJSONDecoder
    result = test_json_decoder.object_hook(pairs=test_values)

    # Check result
    assert result == Ansible

# Generated at 2022-06-13 06:48:35.797878
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoded = json.loads('{"__ansible_unsafe": "foo"}', cls=AnsibleJSONDecoder)
    assert decoded == wrap_var("foo")



# Generated at 2022-06-13 06:48:50.465412
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Given
    import sys
    if sys.version_info[0] >= 3:
        unicode = str

    class TestVaultLib(object):
        def read_bytes(self, value):
            return 'b' + value + 'b'

    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:49:06.294990
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # test to return AnsibleVaultEncryptedUnicode class
    assert isinstance(decoder.object_hook({"__ansible_vault": "my_content"}), AnsibleVaultEncryptedUnicode)
    # test to return AnsibleUnsafeProxy class
    assert str(decoder.object_hook({"__ansible_unsafe": "my_content"})) == "<ansible.parsing.yaml.objects.AnsibleUnsafeProxy object at 0x7f4d7d4b3c88>"
    # test to return pairs
    decoder._vaults['default'] = "vault_default"

# Generated at 2022-06-13 06:49:14.334902
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    decoder = AnsibleJSONDecoder()

    # Test for unsafe strings
    unsafe_str_value = 'hello world!'
    unsafe_str_pairs = {'__ansible_unsafe': unsafe_str_value}
    unsafe_str_expected = AnsibleUnsafeText(unsafe_str_value)

    # Test for vault strings
    vault_data = 'This is a vault'
    vault_pairs = {'__ansible_vault': vault_data}
    vault_expected = AnsibleVaultEncryptedUnicode(vault_data)

    # Test for unsafe_strings
    unsafe_str_result = decoder.object_hook(unsafe_str_pairs)
    assert unsafe_str_result == unsafe_str_expected

# Generated at 2022-06-13 06:49:20.018187
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = b'1234567890asdfghjkl;'

# Generated at 2022-06-13 06:49:23.089892
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = { "vault_password": "ciao" }

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secret)

    assert decoder.object_hook({'__ansible_vault': 'test'}).decrypt() == 'test'
    assert decoder.object_hook({'__ansible_unsafe': 'test'}).value == 'test'


# Generated at 2022-06-13 06:49:35.619050
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Below values are randomly picked up and only to test the method
    """
    @type: dict
    @returns: dict
    """
    d = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n',
        'name': 'geerlingguy.ntp',
        '__ansible_unsafe': '$ANSIBLE_VAULT;1.1;AES256\n'
    }
    decoder = AnsibleJSONDecoder()
    decoded = decoder.object_hook(d)

    assert type(decoded) is dict
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:49:38.828596
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    x = json.loads("""{"__ansible_vault": "foo"}""", cls=AnsibleJSONDecoder)
    assert isinstance(x, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:49:46.416850
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:56.689810
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # set secrets
    secrets = {"default": "secret"}
    AnsibleJSONDecoder.set_secrets(secrets)

    # test both branches of object_hook
    # __ansible_vault
    text = '{"__ansible_vault": "vault encrypted data"}'
    data = json.loads(text, cls=AnsibleJSONDecoder)
    assert isinstance(data, AnsibleVaultEncryptedUnicode)
    assert getattr(data, 'vault') == AnsibleJSONDecoder._vaults['default']
    # __ansible_unsafe
    text = '{"__ansible_unsafe": "this is unsafe"}'
    data = json.loads(text, cls=AnsibleJSONDecoder)
    assert isinstance(data, wrap_var)

# Generated at 2022-06-13 06:50:06.457652
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create instance of class AnsibleJSONDecoder with default constructor
    ansible_json_decoder = AnsibleJSONDecoder()

    # Create dict with one element
    pairs = dict()
    pairs['__ansible_vault'] = 'test_value'

    # Execute method object_hook of class AnsibleJSONDecoder, store method result in variable result
    result = ansible_json_decoder.object_hook(pairs)

    # Check that result is instance of type AnsibleVaultEncryptedUnicode
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

    # Check that AnsibleVaultEncryptedUnicode.vault is not None
    assert result.vault is not None

    # Test exception handling
    # Create dict with one element
    pairs = dict()

# Generated at 2022-06-13 06:50:10.702332
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = [0, 1]
    AnsibleJSONDecoder.set_secrets(secret)

    decoder = AnsibleJSONDecoder()
    assert decoder.decode('{"__ansible_vault": "c2VjcmV0"}') == AnsibleVaultEncryptedUnicode(b'c2VjcmV0')



# Generated at 2022-06-13 06:50:30.876461
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    dec = AnsibleJSONDecoder()
    # test cidr
    pairs = {
        '__ansible_unsafe': {
            '__ansible_cidr': '192.168.0.0/24'
        }
    }

    result = dec.object_hook(pairs)
    assert result['__ansible_unsafe']['__ansible_cidr'] == '192.168.0.0/24'

    # test datetime
    pairs = {
        '__ansible_unsafe': {
            '__ansible_datetime': '2018-08-15T11:38:57.000000Z'
        }
    }
    result = dec.object_hook(pairs)

# Generated at 2022-06-13 06:50:39.711966
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # input is a dictionary of key-value pairs
    raw_dictionary = {'__ansible_vault': 'vault string', '__ansible_unsafe': {'secret': 'abc'}}
    decoded_dictionary = decoder.object_hook(raw_dictionary)
    assert isinstance(decoded_dictionary['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(decoded_dictionary['__ansible_unsafe'], AnsibleUnsafeText)

# Generated at 2022-06-13 06:50:44.366013
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    encoder = AnsibleJSONEncoder()
    decoder = AnsibleJSONDecoder()
    data = {'test': 'test', 'unsafe_test': wrap_var('unsafe_test')}
    assert decoder.decode(encoder.encode(data)) == data

# Generated at 2022-06-13 06:50:53.774981
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    from ansible.module_utils.six import StringIO


# Generated at 2022-06-13 06:50:59.813839
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_value = '$ANSIBLE_VAULT;1.1;AES256;user\n33326162396633316463386134653534373536323132356163636231613131353735313135663332\n34376130323031613961663862613034313134623034373335323735633536613435653465336663\n6636336331386132636330\n'

# Generated at 2022-06-13 06:51:07.080649
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var


# Generated at 2022-06-13 06:51:18.425436
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Prepare test data
    # vault data
    vault = {'key1': 'val1'}
    vault_str = json.dumps(vault)
    vault_encrypted = '$ANSIBLE_VAULT;1.1;AES256\n63643539656536643466383465363364353439643638336436663464393065626264623238636166\n63323636346362326133353631313466313233346634393966643833303962636633623363633162\n34326561613331323962363932373766653965306462653365363563333931653063623830333531\n3864653335\n'
    # unsafe data

# Generated at 2022-06-13 06:51:32.709517
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    vault_editor = VaultEditor()
    text = vault_editor.encrypt('hello world')
    assert isinstance(text, AnsibleVaultEncryptedUnicode)
    assert text.vault is not None

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['hello'])
    assert decoder._vaults

    unsafe_text = 'unsafe'
    unsafe_json = json.dumps({'__ansible_unsafe': unsafe_text})
    ret = decoder.decode(unsafe_json)