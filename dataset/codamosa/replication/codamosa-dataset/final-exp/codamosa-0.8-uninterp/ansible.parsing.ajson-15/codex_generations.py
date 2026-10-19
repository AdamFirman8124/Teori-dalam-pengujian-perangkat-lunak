

# Generated at 2022-06-13 06:41:29.308214
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    secrets = ['test']
    vault = VaultLib(secrets=secrets)
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    enc = vault.encrypt('test1')
    aveu = AnsibleVaultEncryptedUnicode(enc)
    aveu.vault = vault
    assert json.loads(json.dumps(aveu), cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 06:41:35.793564
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_text = '''
{
    "__ansible_vault": "vaulted_text",
    "__ansible_unsafe": "my_secret_value"
}
    '''

    decoded_dict = json.loads(json_text, cls=AnsibleJSONDecoder)
    assert '__ansible_vault' in decoded_dict
    assert '__ansible_unsafe' in decoded_dict



# Generated at 2022-06-13 06:41:44.892243
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class DummyVaultLib(object):
        pass

    dummy_vault = DummyVaultLib()
    secrets = {
        'default': dummy_vault
    }

    # Set necessary args
    # Save original args
    _original_args = AnsibleJSONDecoder._args
    # Set args to empty list
    AnsibleJSONDecoder._args = []

    # Set necessary vaults
    # Save original vault
    _original_vaults = AnsibleJSONDecoder._vaults
    # Set vault to empty dict
    AnsibleJSONDecoder._vaults = {}

    # Set necessary secrets
    AnsibleJSONDecoder.set_secrets(secrets)

    # Create pairs to test

# Generated at 2022-06-13 06:41:56.576076
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:04.922793
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # === Test for key value pair for vault encrypted data
    vault = VaultLib('password')
    test_data = {'name':'test', 'vault':vault.encrypt('secret')}
    decoder = AnsibleJSONDecoder()
    ansible_vault = AnsibleJSONDecoder.object_hook(test_data) ['vault']
    assert isinstance(ansible_vault, AnsibleVaultEncryptedUnicode)
    assert ansible_vault.vault == vault

    # === Test for key value pair to wrap data as unsafe

# Generated at 2022-06-13 06:42:15.317287
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    keys = ['__ansible_vault', '__ansible_unsafe']
    data = {}
    data['__ansible_vault'] = 'foo'
    data['__ansible_unsafe'] = 'bar'

    decoder = AnsibleJSONDecoder()

    res = decoder.object_hook(data)
    print("type res = ", type(res))
    for key in keys:
        print("res[{}] = {}".format(key, res[key]))
        assert isinstance(res[key], AnsibleVaultEncryptedUnicode) or isinstance(res[key], AnsibleUnsafe)

if __name__ == '__main__':
    test_AnsibleJSONDecoder_object_hook()

# Generated at 2022-06-13 06:42:18.508599
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    d = decoder.object_hook({'test': 'value'})
    assert d == {'test': 'value'}
    d = decoder.object_hook({'__ansible_vault': 'value'})
    assert isinstance(d, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:42:32.862036
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        {
            'root': 'DUMMY_SECRET',
            'engine_name': 'DUMMY_SECRET',
            'engine_version': 'DUMMY_SECRET',
        }
    ]
    val = 'DUMMY_SECRET'
    vault_key = 'DUMMY_SECRET'
    encrypt_val = {'__ansible_vault': 'DUMMY_SECRET', '__ansible_vault_password': 'DUMMY_SECRET'}
    AnsibleJSONDecoder.set_secrets(secrets)
    result = json.loads(json.dumps(encrypt_val), cls=AnsibleJSONDecoder)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert '__ansible_vault' in result

# Generated at 2022-06-13 06:42:36.711984
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:42:49.213868
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    test_pairs_1 = {
        '__ansible_vault': 'asdf',
        '__ansible_unsafe': 'something_unsafe',
        'something': 'something_else'
    }

    test_pairs_2 = {
        '__ansible_vault': 'asdf'
    }

    # Creating a new class, to have a new "static" _vaults
    class object_hook_test_class(AnsibleJSONDecoder):
        def object_hook(self, pairs):
            return AnsibleJSONDecoder.object_hook(self, pairs)
    # Creating a new instance
    test_instance = object_hook_test_class()

    # Adding secrets to the dictionary
    secrets = ['asdf']
    AnsibleJSONDecoder.set_secrets(secrets)

    #

# Generated at 2022-06-13 06:42:59.176405
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleMapping

    decoder = AnsibleJSONDecoder()
    if PY3:
        # json module returns dict in python3
        assert isinstance(decoder.object_hook(dict(__ansible_vault='anyrandomstring')), AnsibleMapping)
        assert isinstance(decoder.object_hook(dict(__ansible_unsafe='anyrandomstring')), dict)
    else:
        # json module returns OrderedDict in python2
        assert isinstance(decoder.object_hook(dict(__ansible_vault='anyrandomstring')), AnsibleMapping)

# Generated at 2022-06-13 06:43:05.015604
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    raw_data = '{"__ansible_vault": "vault_value", "__ansible_unsafe": "unsafe_value", "no_hook_needed": "no_hook_needed_value"}'
    res = AnsibleJSONDecoder().decode(raw_data)
    assert len(res) == 3
    assert res['__ansible_vault'] == 'vault_value'
    assert res['__ansible_unsafe'] == 'unsafe_value'
    assert res['no_hook_needed'] == 'no_hook_needed_value'

# Generated at 2022-06-13 06:43:19.357254
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def _test_AnsibleJSONDecoder_object_hook(input_data, expected_output):
        actual_output = AnsibleJSONDecoder().object_hook(input_data)
        assert actual_output == expected_output

    input_data1 = {'__ansible_vault': '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30663730316563396334326337376632336139396565313431623136336666666133393532376230\n          39353362323766656130663436393331323363353633376233653930666166326565653764396634\n          3133\n          '}

# Generated at 2022-06-13 06:43:23.411702
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    vault = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256')
    unsafe = wrap_var({"name": "Meeseeks"})

    assert decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}) == vault
    assert decoder.object_hook({'__ansible_unsafe': {"name": "Meeseeks"}}) == unsafe
    assert decoder.object_hook({'cow': 'moo', 'cat': {"name": "Meeseeks"}}) == {'cow': 'moo', 'cat': {"name": "Meeseeks"}}

# Generated at 2022-06-13 06:43:25.307614
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:31.960434
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest

    pairs = {'__ansible_vault': 'asdf1234'}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    assert result['__ansible_vault'] == 'asdf1234'

    pairs = {'__ansible_unsafe': 'asdf1234'}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    assert result['__ansible_unsafe'] == 'asdf1234'

# Generated at 2022-06-13 06:43:39.418670
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Set some secret to be used in the decoder
    AnsibleJSONDecoder.set_secrets(['foo'])
    # Create a dict to be used in the decoder
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;foo\nblahblah', '__ansible_unsafe': True}
    # Create an AnsibleJSONDecoder instance
    ansible_json_decoder = AnsibleJSONDecoder()
    object_hook = ansible_json_decoder.object_hook(pairs)
    # If the __ansible_vault key exists in the dict, the value of it will be
    # AnsibleVaultEncryptedUnicode obj

# Generated at 2022-06-13 06:43:47.135189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    k = '__ansible_unsafe'
    v = 'unsafe_value'
    test_dict = {k: v}
    test_json = json.dumps(test_dict, cls=AnsibleJSONEncoder)
    decoded_dict = json.loads(test_json, cls=AnsibleJSONDecoder)

    assert test_dict[k] == decoded_dict[k]
    assert test_dict[k] is not decoded_dict[k]



# Generated at 2022-06-13 06:43:54.902189
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['ansible']
    ansible_json_decoder = AnsibleJSONDecoder.set_secrets(secrets)

    # Test case 1: test with __ansible_vault
    json_dict = {'k1': 'v1',
                 'k2': 'v2',
                 '__ansible_vault': 'encrypted string'}
    json_str = json.dumps(json_dict, cls=AnsibleJSONEncoder)
    print(json_str)
    decoded_json_dict = json.loads(json_str, cls=AnsibleJSONDecoder)
    print(decoded_json_dict)

    # Test case 2: test with __ansible_unsafe

# Generated at 2022-06-13 06:44:08.791357
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:21.754123
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['secret'])


# Generated at 2022-06-13 06:44:30.695945
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = '$ANSIBLE_VAULT;1.1;AES256\n36303535643563313230303939643462656464303838303865656562316166623939633539363561\n3831356365396237333537376438613232613637303436323063380a32316233616263353430653739\n3533613961333561633264636232303163396166363461646362373262326634316166323264353439\n313730316232333834653661'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets([secret])
    unicode_string = decoder.decode('{"__ansible_vault": "__VAULT__"}')

# Generated at 2022-06-13 06:44:34.390760
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder('{ "__ansible_vault": "test_value" }', object_hook=AnsibleJSONDecoder.object_hook).decode() == {'__ansible_vault': 'test_value'}



# Generated at 2022-06-13 06:44:41.876744
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:56.381460
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    ##########
    # None case
    ##########
    # Prep
    expected = None
    # Run
    observed = decoder.object_hook(None)
    # Check
    assert observed == expected

    #################
    # List case
    #################
    # Prep
    expected = ['a', 'b', 'c']
    # Run
    observed = decoder.object_hook(expected)
    # Check
    assert observed == expected

    #################
    # Dictionary case
    #################
    # Trivial case
    # Prep
    expected = {
        'x': 'a',
        'y': 'b'
    }
    # Run
    observed = decoder.object_hook(expected)
    # Check
    assert observed == expected

    # Test case


# Generated at 2022-06-13 06:45:08.074916
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_data = '{"__ansible_vault": "dGVzdGluZzEK", "__ansible_unsafe": {"__ansible_vault": "dGVzdGluZzIK"}}'
    test_data = {
        '__ansible_vault': 'dGVzdGluZzEK',
        '__ansible_unsafe': {'__ansible_vault': 'dGVzdGluZzIK'},
    }

    secrets = {'default': [{'cipher': 'AES256', 'vault_id': 'test'}]}
    AnsibleJSONDecoder.set_secrets(secrets)
    vault_lib = VaultLib(secrets=secrets)


# Generated at 2022-06-13 06:45:16.000296
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    encoder = AnsibleJSONEncoder(ensure_ascii=False, sort_keys=True, indent=4)
    s = '{"__ansible_unsafe": "{{lookup}}"}'
    decoder = AnsibleJSONDecoder(encoding='utf-8')
    obj = json.loads(s, cls=decoder)
    assert isinstance(obj["__ansible_unsafe"], AnsibleUnsafeText)
    assert obj["__ansible_unsafe"] ==  u'{{lookup}}'
    assert json.dumps(obj, cls=encoder) == s

# Generated at 2022-06-13 06:45:24.657554
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test 1:
    # Set data to be parsed
    data = {
        "show_version": {
            "__ansible_vault": "2.2.2.2"
        }
    }

    # Execute object_hook method
    result = AnsibleJSONDecoder().object_hook(data)

    # Verify assertion
    assert result['show_version'].value == ''
    assert result['show_version'].vault.secrets == ['default']

    # Test 2:
    # Set data to be parsed
    data = {
        "show_version": {
            "__ansible_vault": "2.2.2.2"
        },
        "__ansible_unsafe": {
            "host": "{{ password }}"
        }
    }

    # Execute object_hook method


# Generated at 2022-06-13 06:45:36.379631
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    secrets = ['secret1']
    vault = VaultLib(secrets=secrets)
    json_decoder = AnsibleJSONDecoder()
    json_decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:45:46.725737
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_data = b"_vault_data"
    vault_pass = "abcd1234"
    vault_data = "secret_content"
    vault_id = "default"

    enc_vault_data = "!vault |\n          $ANSIBLE_VAULT;" + secret_data.decode("utf8")
    dec_vault_data = "secret_content"
    dec_unsafe_data = "!unsafe /path/to/file"

    # For test pupose this is a dummy VaultLib
    # It only implements the encrypt and decrypt method
    # The encrypt method only adds the character '!'
    # The decrypt method only removes the character '!'
    class DummyVaultLib(VaultLib):
        def encrypt(self, text):
            return "!" + text


# Generated at 2022-06-13 06:45:55.655489
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    import json
    import ansible.constants as C

    # Test the value of the '__ansible_vault' key defined in the json file
    test_json_file = "./tests/sanity/parsing/yaml/files/vault_test_unsafe_roles.json"
    test_vault_password_file = "./tests/sanity/parsing/yaml/files/vault_test_password.txt"
    test_decoded_json = json.load(open(test_json_file, 'r'), cls=AnsibleJSONDecoder)


# Generated at 2022-06-13 06:46:06.383896
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class TestAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self, *args, **kwargs):
            AnsibleVaultEncryptedUnicode.__init__(self, *args, **kwargs)
            self.args = args
            self.kwargs = kwargs

    # Reset AnsibleVaultEncryptedUnicode.__init__ to default
    AnsibleVaultEncryptedUnicode.__init__ = AnsibleVaultEncryptedUnicode.orig_init


# Generated at 2022-06-13 06:46:09.519115
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import json

    original_json = '{"__ansible_unsafe": "<html><body>Secret</body></html>"}'
    result = json.loads(original_json, cls=AnsibleJSONDecoder)
    assert isinstance(result[u'__ansible_unsafe'], AnsibleUnsafeText)
    assert result[u'__ansible_unsafe'] == u'<html><body>Secret</body></html>'

# Generated at 2022-06-13 06:46:20.636795
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Initialize an AnsibleJSONDecoder object to be able to test object_hook
    decoder = AnsibleJSONDecoder()

    # Test the case when the object is not a string
    result = decoder.object_hook({})
    assert result == {}, "Result is not an empty object"

    # Test the case of when object is an AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-13 06:46:26.443360
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')
    assert decoder.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')

# Generated at 2022-06-13 06:46:35.344703
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    j = '''{"__ansible_vault": "AES256"}'''
    data = json.loads(j, cls=AnsibleJSONDecoder)
    assert (data == AnsibleVaultEncryptedUnicode('AES256'))
    j = '''{"__ansible_unsafe": "AES256"}'''
    data = json.loads(j, cls=AnsibleJSONDecoder)
    assert (data == wrap_var('AES256'))
    j = '''{"__ansible_unsafe": "AES256", "__ansible_vault": "AES256"}'''
    data = json.loads(j, cls=AnsibleJSONDecoder)
    assert (data == AnsibleVaultEncryptedUnicode('AES256'))

# Generated at 2022-06-13 06:46:46.706050
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup test
    dec = AnsibleJSONDecoder()

    # Smoke test for the object_hook method of AnsibleJSONDecoder class
    result = dec.object_hook({})

    assert result == {}

    # Test for method object_hook of class AnsibleJSONDecoder
    # Vaults and unsafe proxies are indicated by keys, not values.
    # The custom object_hook should not trigger for normal keys.
    for key in ['__ansible_vault', '__ansible_unsafe']:
        pairs = {key: 'foo'}
        result = dec.object_hook(pairs)
        assert result == pairs

    # Test for method object_hook of class AnsibleJSONDecoder
    # Vaults are indicated by the __ansible_vault key and a non-dict value.
    # The custom object_hook should trigger and return an Ans

# Generated at 2022-06-13 06:46:53.785514
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import ansible.parsing.vault
    ansible.parsing.vault.VaultLib = VaultLib
    json_string = '{"key": "value", "ansible_vault": "password", "ansible_unsafe": "password"}'
    ansible_json_decoder = AnsibleJSONDecoder()
    secrets = {'password': 'some secret is here'}
    ansible_json_decoder.set_secrets(secrets)
    ansible_json_decoder.decode(json_string)



# Generated at 2022-06-13 06:47:01.377722
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Tests for the object_hook method of the AnsibleJSONDecoder class

    # Simple test for object_hook
    value = 'fake_value'
    pairs = {'__ansible_unsafe': value}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    assert result == wrap_var(value)

    # Test for object_hook with __ansible_vault
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets("password")
    values = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n61646D696E20636F6F6B65206E756D6265722E\n'}
    result = decoder.object_hook(values)
    assert result  == Ans

# Generated at 2022-06-13 06:47:11.984392
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:23.605965
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:30.318036
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_decoder = AnsibleJSONDecoder()
    result_dict = json_decoder.object_hook({'__ansible_vault': '12345'})
    result_string = json_decoder.object_hook({'__ansible_unsafe': '12345'})
    result_none = json_decoder.object_hook({'__ansible_notexists': '12345'})

    assert isinstance(result_dict, AnsibleVaultEncryptedUnicode)
    assert result_dict == '12345'
    assert isinstance(result_string, AnsibleVaultEncryptedUnicode)
    assert result_string == '12345'
    assert not result_none

# Generated at 2022-06-13 06:47:42.538560
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:47:47.125071
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test with correct values
    pairs = {'__ansible_vault': 'test'}
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook(pairs) == AnsibleVaultEncryptedUnicode(pairs['__ansible_vault'])
    pairs = {'__ansible_unsafe': 'test'}
    assert type(decoder.object_hook(pairs)) == str
    # Test without correct values
    pairs = {}
    assert decoder.object_hook(pairs) == {}



# Generated at 2022-06-13 06:47:59.630737
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # Test unwrapping a variable marked as unsafe
    assert decoder.object_hook({'__ansible_unsafe': '12345'}) == wrap_var('12345')

    secrets = '$ANSIBLE_VAULT;1.2;AES256;myusername\n' \
              '966201674393464616461326431373331383865393331323161396537376164343633663765616231\n' \
              '37666335666633353638343837306635303762626162386336333635656539663433376231386261\n' \
              '3264353162373361\n'
    AnsibleJSONDecoder.set_secrets(secrets)

# Generated at 2022-06-13 06:48:06.271609
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_encrypted_unicode = AnsibleJSONDecoder.object_hook({'__ansible_vault': 'vault_value'})
    assert isinstance(ansible_vault_encrypted_unicode, AnsibleVaultEncryptedUnicode)
    ansible_unsafe = AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'unsafe_value'})
    assert hasattr(ansible_unsafe, '__ansible_unsafe__')
    assert ansible_unsafe.__ansible_unsafe__() == 'unsafe_value'

# Generated at 2022-06-13 06:48:12.950262
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    testCases = [
        {
            'input': {'__ansible_vault': 'secret'},
            'expectedOutput': AnsibleVaultEncryptedUnicode('secret')
        },
        {
            'input': {'__ansible_unsafe': 'unsafe'},
            'expectedOutput': wrap_var('unsafe')
        },
        {
            'input': {'not_vault': 'secret'},
            'expectedOutput': {'not_vault': 'secret'}
        }
    ]

    def callback(pairs):
        assert(len(testCases))

        tc = testCases.pop(0)
        assert(pairs == tc.get('input'))
        return tc.get('expectedOutput')

    AnsibleJSONDecoder.object_hook = callback
    ansible

# Generated at 2022-06-13 06:48:23.003635
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()
    # Check if object_hook will replace the __ansible_vault with the expected AnsibleVaultEncryptedUnicode object
    assert ansible_json_decoder.object_hook({'__ansible_vault': 'something'}) == AnsibleVaultEncryptedUnicode('something')

    # If a non-existing key is given, return the original dictionary
    assert ansible_json_decoder.object_hook({'something': 'else'}) == {'something': 'else'}

    # Check if object_hook will replace the __ansible_unsafe with the expected wrap_var object
    assert ansible_json_decoder.object_hook({'__ansible_unsafe': 'something else'}) == wrap_var('something else')


# Generated at 2022-06-13 06:48:31.319441
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data = {'__ansible_vault': 'vaultvalue', '__ansible_unsafe': 'unsafevalue'}

    pairs = decoder.object_hook(data)
    assert isinstance(pairs['__ansible_unsafe'], wrap_var)
    assert isinstance(pairs['__ansible_vault'], AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:48:35.753301
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = {"vault_k4n3": "vault_s3cr3t"}
    json_str = '{"__ansible_vault": "vault_k4n3", "__ansible_unsafe": true}'

    json_dict = json.loads(json_str, cls=AnsibleJSONDecoder, secrets=secrets)
    assert json_dict.get("__ansible_vault") == "vault_s3cr3t"
    assert json_dict.get("__ansible_unsafe") is True


# Generated at 2022-06-13 06:48:53.158094
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:01.089413
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys

    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO

    AnsibleJSONDecoder.set_secrets(secrets=('ansible'))

    data = StringIO("""
{
    "__ansible_vault": "my_secret",
    "__ansible_unsafe": "my_other_secret"
}
""")

    vault = AnsibleJSONDecoder.json_load(fp=data)
    assert isinstance(vault['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(vault['__ansible_unsafe'], (str, unicode, bool, tuple, int, long, list, dict))



# Generated at 2022-06-13 06:49:07.468282
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs = {'__ansible_vault': 'some value'}
    v = decoder.object_hook(pairs)
    assert isinstance(v, AnsibleVaultEncryptedUnicode)
    assert v == u'some value'

    pairs = {'__ansible_unsafe': 'some value'}
    v = decoder.object_hook(pairs)
    assert isinstance(v, wrap_var)
    assert v == u'some value'

# Generated at 2022-06-13 06:49:15.089395
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:24.716848
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Array contains objects, so we need to iterate over list to get
    # objects.
    list_of_objects = json.loads('[{"__ansible_vault": "test"}, {"__ansible_vault": "test"}]', cls=AnsibleJSONDecoder)
    for obj in list_of_objects:
        assert isinstance(obj, AnsibleVaultEncryptedUnicode)
        assert obj.vault is not None

    # Object contains value only
    value_only_object = json.loads('{"__ansible_vault": "test"}', cls=AnsibleJSONDecoder)
    assert isinstance(value_only_object, AnsibleVaultEncryptedUnicode)
    assert value_only_object.vault is not None

# Generated at 2022-06-13 06:49:32.749050
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    items = {
        '__ansible_vault': 'hello world',
        '__ansible_unsafe': {},
    }

    decoder = AnsibleJSONDecoder()
    pairs = decoder.object_hook(items)

    assert isinstance(pairs['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert pairs['__ansible_unsafe'] == {}

# Generated at 2022-06-13 06:49:46.111386
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import textwrap
    from ansible.parsing.vault import VaultLib

    SECRET = 'mysecret'

# Generated at 2022-06-13 06:49:50.141441
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    key = '__ansible_unsafe'
    value = 'secret'
    pairs = {key: value}
    decoder = AnsibleJSONDecoder()

    result = decoder.object_hook(pairs)

    assert result == wrap_var(value)

# Generated at 2022-06-13 06:49:58.833167
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(strict=False)

# Generated at 2022-06-13 06:50:05.984425
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secret = 'my_secret'
    secrets = [secret]
    json_input = '{"__ansible_vault": "AES256$c2VjcmV0X3Rlc3RfcGxhaW5fZW5jcnlwdGlvbg==$13d9d6ecc1f098b8a0b24c1b6a09f81a11c0bd59a278831"}'

    AnsibleJSONDecoder.set_secrets(secrets)
    json.loads(json_input, cls=AnsibleJSONDecoder) # no exception should be raised

# Generated at 2022-06-13 06:50:15.401467
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    assert decoder.object_hook({}) == {}
    assert decoder.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')
    assert decoder.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')
    assert decoder.object_hook({'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'}) == AnsibleVaultEncryptedUnicode('foo')

# Generated at 2022-06-13 06:50:30.972359
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # create a vaulted object
    vault_password = 'mypassword'
    value = 'abcdefg'
    vault = VaultLib(vault_password)
    vaulted_value = vault.encrypt(value)
    vault_pairs = {'__ansible_vault': vaulted_value}
    AnsibleJSONDecoder.set_secrets(vault_password)
    obj = AnsibleJSONDecoder().object_hook(vault_pairs)
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj == value

    # create an unsafe object
    unsafe_pairs = {'__ansible_unsafe': '$(ls /etc/shadow)'}
    obj = AnsibleJSONDecoder().object_hook(unsafe_pairs)

# Generated at 2022-06-13 06:50:44.130579
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret1', 'secret2', 'secret3']

# Generated at 2022-06-13 06:50:53.632460
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.common._collections_compat import Mapping

    obj = AnsibleJSONDecoder.object_hook({'__ansible_vault': None})
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj.value == None

    obj = AnsibleJSONDecoder.object_hook({'__ansible_vault': {'a': 'b'}})
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj.value == {'a': 'b'}

    obj = AnsibleJSONDecoder.object_hook({'__ansible_vault': {'a': 'b'}, '__ansible_unsafe': None})
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:50:59.736568
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    decoder = AnsibleJSONDecoder()

    # Test with __ansible_vault
    value = decoder.object_hook({"__ansible_vault": "test"})
    assert isinstance(value, AnsibleVaultEncryptedUnicode)
    assert value.vault is None
    assert value == "test"

    # Test with __ansible_vault and vault
    decoder.set_secrets("ansible")
    value = decoder.object_hook({"__ansible_vault": "test"})
    assert isinstance(value, AnsibleVaultEncryptedUnicode)
    assert isinstance(value.vault, VaultLib)

# Generated at 2022-06-13 06:51:07.073522
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:51:18.426537
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.six import PY3

    decoder = AnsibleJSONDecoder()

    # PY3 - AnsibleJSONEncoder
    if PY3:
        assert not decoder.object_hook({'__ansible_vault': 'vault'}) == {'__ansible_vault': 'vault'}
        decoder.set_secrets('123456')
        assert isinstance(decoder.object_hook({'__ansible_vault': 'vault'}), AnsibleVaultEncryptedUnicode)

    # not PY3
    else:
        assert decoder.object_hook({'__ansible_vault': 'vault'}) != {'__ansible_vault': 'vault'}
        decoder.set_secrets('123456')

# Generated at 2022-06-13 06:51:32.709947
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = "abcd"
    payload = '{"__ansible_vault": "AES256:abcd", "message": "test"}'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secret)
    assert(decoder.decode(payload)['__ansible_vault'].data == "")
    assert(decoder.decode(payload).vault.decrypt('{"__ansible_vault": "AES256:abcd", "message": "test"}') == '{"__ansible_vault": "AES256:abcd", "message": "test"}')
    assert(decoder.decode(payload).vault.decrypt(payload) == '{"__ansible_vault": "AES256:abcd", "message": "test"}')