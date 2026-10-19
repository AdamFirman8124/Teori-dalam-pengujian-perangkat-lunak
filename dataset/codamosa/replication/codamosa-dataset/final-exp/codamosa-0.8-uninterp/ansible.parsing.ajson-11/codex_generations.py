

# Generated at 2022-06-13 06:41:33.283850
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(['test'], password_files=['test/test-vault-password'])
    vault_encoded = vault.encode('test')
    value = AnsibleVaultEncodedUnicode(vault_encoded)
    value.vault = vault
    assert AnsibleJSONDecoder.object_hook({'test': value})['test'] == 'test'

    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': vault_encoded}) == {'__ansible_vault': vault_encoded}
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': vault_encoded}) == {'__ansible_unsafe': vault_encoded}

# Generated at 2022-06-13 06:41:37.510883
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    raw = '''{
        "__ansible_vault": "abc"
    }'''

    decoder = AnsibleJSONDecoder()
    result = decoder.decode(raw)
    assert isinstance(result['__ansible_vault'], AnsibleVaultEncryptedUnicode)


# Generated at 2022-06-13 06:41:47.349472
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Prepare test case
    obj = json.loads(r"""{"__ansible_unsafe": "test unsafe", "__ansible_vault": "test vault"}""",
                     cls=AnsibleJSONDecoder)

    # Run test
    result = obj.get('__ansible_unsafe')

    # Assert
    assert result.__class__.__name__ == 'AnsibleUnsafeText', 'Class of result is wrong'
    assert result == 'test unsafe', 'JPassword is wrong'

    # Run test
    result = obj.get('__ansible_vault')

    # Assert
    assert result.__class__.__name__ == 'AnsibleVaultEncryptedUnicode', 'Class of result is wrong'
    assert result == 'test vault', 'JPassword is wrong'

# Unit

# Generated at 2022-06-13 06:41:54.016120
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {
        '__ansible_vault': 'vaultpassword',
        '__ansible_unsafe': True,
    }

    data = json.dumps(data, cls=AnsibleJSONEncoder)
    result = json.loads(data, cls=AnsibleJSONDecoder)
    assert result['__ansible_vault'] == 'vaultpassword'
    assert result['__ansible_unsafe'] == True

# Generated at 2022-06-13 06:42:04.060943
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    m_decoder = AnsibleJSONDecoder()
    m_secrets = b'$ANSIBLE_VAULT;1.1;AES256\n633861653131666668626630336466663935663762363265363333346331643839383033623\n3934353334386465666631326138316236633135313531386563626235316561383035643331\n3733333564363164653031383336376331623065363737346539373565326231643239323164\n6336663630333536613466343933663731653532626133366665343761663239306663613039\n63623866336536663231616635653835666562\n'

# Generated at 2022-06-13 06:42:15.454867
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class TestJSONDecoder(AnsibleJSONDecoder):
        def object_hook(self, pairs):
            return pairs

    test_decoder = TestJSONDecoder()


# Generated at 2022-06-13 06:42:20.547433
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_password = 'theVaultPassword'
    json_text = '{"__ansible_vault": "dGVzdA==\n", "__ansible_unsafe": true}'

    AnsibleJSONDecoder.set_secrets([secret_password])
    secret_data = json.loads(json_text, cls=AnsibleJSONDecoder)

    assert secret_data['__ansible_vault'] == 'test'
    assert secret_data['__ansible_unsafe']  # will be True

# Generated at 2022-06-13 06:42:25.658396
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Create instance of AnsibleJSONDecoder
    ansible_json_decoder = AnsibleJSONDecoder()

    # Create an AnsibleVaultEncryptedUnicode with a dummy encrypted value

# Generated at 2022-06-13 06:42:34.546045
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    def _callback(pairs):
        pairs['__ansible_unsafe'] = 'value'
        return pairs

    decoder = AnsibleJSONDecoder(object_hook=_callback)
    assert decoder.object_hook({'__ansible_vault': 'value'}) == 'value'
    assert decoder.object_hook({'__ansible_unsafe': 'value'}) == wrap_var('value')
    assert decoder.object_hook({'__ansible_other': 'value'}) == {'__ansible_other': 'value'}


__all__ = ['AnsibleJSONDecoder', 'AnsibleJSONEncoder']

# Generated at 2022-06-13 06:42:46.847857
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    with pytest.raises(AttributeError) as excinfo:
        decoder.object_hook({})
    assert 'object has no attribute' in str(excinfo.value)

    hook = AnsibleJSONDecoder.object_hook
    assert hook({'__ansible_vault': 'hello world'}) == AnsibleVaultEncryptedUnicode('hello world')
    assert hook({'__ansible_unsafe': 'hello world'}) == wrap_var('hello world')

# Generated at 2022-06-13 06:42:57.575952
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:03.818267
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    input_string = r'''{"msg": "Hello World!", "__ansible_vault": "ANSIBLE_VAULT;1.2;AES256;foo\nbar==\n", "ignore": "__ansible_vault is ignored"}'''
    decoded = json.loads(input_string, cls=AnsibleJSONDecoder)
    assert isinstance(decoded['msg'], str)
    assert decoded['__ansible_vault'] == 'bar=='
    assert isinstance(decoded['ignore'], str)



# Generated at 2022-06-13 06:43:08.552975
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_encoded_string = '{"__ansible_vault":"$ANSIBLE_VAULT;1.1;AES256\n0000000000000000000000000000000000000000000000000000000000000000"}' # noqa
    password = 'test_password'
    AnsibleJSONDecoder.set_secrets(password)

    decoded_json = AnsibleJSONDecoder().decode(json_encoded_string)
    assert decoded_json['__ansible_vault'] == AnsibleVaultEncryptedUnicode(json_encoded_string)

# Generated at 2022-06-13 06:43:20.256814
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    mock_data = {"foo": "bar", "bar": "foo", "__ansible_vault": "encrypted_string", "__ansible_unsafe": "unsafe_string"}
    mock_pairs = {"foo": "bar", "bar": "foo", "__ansible_vault": "encrypted_string", "__ansible_unsafe": "unsafe_string"}
    mock_vault = {'default': 'VaultLib'}
    ansible_json_decoder = AnsibleJSONDecoder()
    ansible_json_decoder._vaults = mock_vault
    assert ansible_json_decoder.object_hook(mock_pairs) == mock_data

# Generated at 2022-06-13 06:43:30.674924
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret, VaultPassword
    vault = VaultLib(secrets=[VaultSecret(password="red")])

# Generated at 2022-06-13 06:43:38.279635
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # AnsibleVaultEncryptedUnicode
    secrets = ['password']
    decoder.set_secrets(secrets)
    payload = '''
    {   "default": "{{ vault_password_file }}",
        "__ansible_vault": "vault_password_file"
    }
    '''
    result = decoder.decode(payload)
    assert result['__ansible_vault'] is not None

    # wrap_var
    payload = '''
    {   "__ansible_unsafe": "This is unsafe"
    }
    '''
    result = decoder.decode(payload)
    assert result['__ansible_unsafe'].is_safe is False

# Generated at 2022-06-13 06:43:50.111358
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:43:59.529349
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys
    import textwrap

    # TODO: Refactor this class and the unit test
    #       defined in ansible.module_utils.common.json_utils
    #       so that these tests are not repeated

    # Python 2

# Generated at 2022-06-13 06:44:10.601438
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'password']
    AnsibleJSONDecoder.set_secrets(secrets=secrets)
    data = dict(__ansible_vault=b'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          39656635666363623538656635373961393764336635643631343963653337356434346162386130\n          63356265653663303831636531653436656531633532316161343732643039326166643334653638\n          61643063353332626634353966663534633034323162653537343632613961363133356537366138\n          3230\n          ')

# Generated at 2022-06-13 06:44:18.344572
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(['testpass'])

    # AnsibleVaultEncryptedUnicode with vault value test
    assert '{ "__ansible_vault": "vault" }' == json.dumps(decoder.object_hook({ "__ansible_vault": "vault" }))
    assert type(decoder.object_hook({ "__ansible_vault": "vault" })['__ansible_vault']) == AnsibleVaultEncryptedUnicode
    assert decoder.object_hook({ "__ansible_vault": "vault" })['__ansible_vault']._vault is not None



# Generated at 2022-06-13 06:44:25.180161
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:36.118874
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = "foo"
    text_to_decode = '{"__ansible_vault": "AQAAAAIAAAADb3JpZ2luYWwAAAAEYmF0aGVybGlja3Rlc3RzAAAACGJhdGhlcmxpY2t0ZXN0cwAAAAJkAAABzZXJ2aWNlX2Nvbm5lY3Rpb24uaGFuZGxlcgAAAAcxZXJ2aWNlX2Nvbm5lY3Rpb24uaGFuZGxlcnAAAACg="}'

# Generated at 2022-06-13 06:44:41.743913
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class AVU:

        def __init__(self, value):
            self.value = value

    ob = AnsibleJSONDecoder.object_hook({'__ansible_vault': 'unittest_str',
                                         '__ansible_unsafe': 'unittest_str'})
    assert isinstance(ob['__ansible_vault'], AVU)
    assert ob['__ansible_vault'].value == 'unittest_str'
    assert isinstance(ob['__ansible_unsafe'], wrap_var)
    assert ob['__ansible_unsafe'].value == 'unittest_str'



# Generated at 2022-06-13 06:44:51.648814
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:44:56.100215
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:07.687044
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:18.140291
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    # test AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:45:23.014361
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    j = '''{ "__ansible_vault": "vault-value", "__ansible_unsafe": "unsafe-value" }'''
    d = AnsibleJSONDecoder().decode(j)
    assert d['__ansible_vault'] == 'vault-value'
    assert d['__ansible_unsafe'] == 'unsafe-value'

s = AnsibleJSONEncoder()


# Generated at 2022-06-13 06:45:26.395973
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    d = AnsibleJSONDecoder()
    pairs = d.object_hook(dict(__ansible_vault='abcd', __ansible_unsafe='hello'))
    assert isinstance(pairs['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert pairs['__ansible_unsafe'] == wrap_var('hello')

# Unit test of class AnsibleJSONEncoder

# Generated at 2022-06-13 06:45:38.016339
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    from ansible.parsing.vault import VaultEditor
    # vault_password = 'mypassword'
    vault_password = '$ANSIBLE_VAULT;1.1;AES256\r\n3332646261366162396334356438336265643934356539633639643061363564353266656332393\r\n66616538643963613834326261383063643563383662376362643537336534353732343161366563\r\n38643737396432306338373931323464363130353330653335663163353438316161333532353265\r\n3839383034333231666365\r\n'

# Generated at 2022-06-13 06:45:48.604607
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:56.194104
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultSecret

    # This is a skip test for Ansible vault.
    if not hasattr(AnsibleVaultEncryptedUnicode, 'vault'):
        return

    secret = VaultSecret('testvault')
    AnsibleJSONDecoder.set_secrets(secret)

    # Test vault
    variable = AnsibleJSONDecoder.decode('{"__ansible_vault": "testvault"}')
    assert variable.__class__.__name__ == 'AnsibleVaultEncryptedUnicode'
    assert variable.vault.secrets == 'testvault'

    # Test unsafe
    variable = AnsibleJSONDecoder.decode('{"__ansible_unsafe": "testunsafe"}')
    assert variable == wrap_var('testunsafe')

   

# Generated at 2022-06-13 06:46:01.584809
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    result = AnsibleJSONDecoder.object_hook({'__ansible_vault': 'test'})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert str(result) == 'test'

    result = AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'test'})
    assert repr(result) == 'test'



# Generated at 2022-06-13 06:46:08.374136
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    dec = AnsibleJSONDecoder()
    assert dec.object_hook({'key': 'value'}) == {'key': 'value'}
    assert dec.object_hook({'__ansible_vault': 'value'}).data == 'value'
    assert dec.object_hook({'__ansible_unsafe': 'value'}) == wrap_var('value')



# Generated at 2022-06-13 06:46:13.130130
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()
    stdout, stderr = ansible_json_decoder.object_hook('__ansible_vault')
    assert isinstance(stdout, AnsibleVaultEncryptedUnicode)
    assert stderr is None

# Generated at 2022-06-13 06:46:20.010991
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'test_secrets'
    value = 'test_value'
    ansible_vault = {'__ansible_vault': value}
    ansible_vault_expected = AnsibleVaultEncryptedUnicode(value)
    ansible_vault_expected.vault = VaultLib(secrets=secrets)
    ansible_unsafe = {'__ansible_unsafe': value}
    ansible_unsafe_expected = wrap_var(value)

    # Test AnsibleVaultEncryptedUnicode
    AnsibleJSONDecoder.set_secrets(secrets)
    ansible_vault_decoder = AnsibleJSONDecoder()
    ansible_vault_decoded = ansible_vault_decoder.object_hook(ansible_vault)
    assert ansible_v

# Generated at 2022-06-13 06:46:34.988387
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils.common.json import from_json
    import ansible.vars.unsafe_proxy
    my_decoder = AnsibleJSONDecoder()
    my_decoder.set_secrets(['test_secret'])

    assert my_decoder.object_hook({'__ansible_vault': '$VAULT;9;hBeXSlY1vM8k/SWyhxwxwA=='}) == AnsibleVaultEncryptedUnicode('$VAULT;9;hBeXSlY1vM8k/SWyhxwxwA==')
    assert from_json('[{"__ansible_vault": "$VAULT;9;hBeXSlY1vM8k/SWyhxwxwA=="}]', cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 06:46:40.235662
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Scenario - 1
    # Objective: To test if the unsafe string is converted to UnsafeProxy.
    # Input: The given string is {"__ansible_unsafe": "Ansible"}
    # Expected Output: The string should be converted to UnsafeProxy Object.
    test_str = '{"__ansible_unsafe": "Ansible"}'
    json_data = json.loads(test_str, cls=AnsibleJSONDecoder)
    assert isinstance(json_data, dict)
    assert isinstance(json_data['__ansible_unsafe'], wrap_var)
    assert json_data['__ansible_unsafe'].data == "Ansible"

    # Scenario - 2
    # Objective: To test if the string is converted to AnsibleVaultEncryptedUnicode when vault is not dec

# Generated at 2022-06-13 06:46:54.551957
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # Initialize object
    ansible_json_decoder = AnsibleJSONDecoder()

    # Generate a dictionary with a secret
    dictionary = dict()

# Generated at 2022-06-13 06:47:00.221844
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder
    result = decoder.object_hook({'__ansible_vault':'test'})
    assert result.__class__.__name__ == 'AnsibleVaultEncryptedUnicode'
    assert result._text == 'test'
    result = decoder.object_hook({'__ansible_unsafe':'test'})
    assert result == 'test'
    result = decoder.object_hook({'notansible':'test'})
    assert result == {'notansible':'test'}

# Generated at 2022-06-13 06:47:12.744395
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    data = {
        '__ansible_vault': 'AQAAC1NUUXJIc3N3ZVExUHgwelV6dW1GY2M0R1RnNVhoZV9HQWFXM3ZVVUZsNi9vVkpFNnh1TUhHZz09',
        '__ansible_unsafe': 'TEST_SECRET'
    }
    secrets = ['TEST_SECRET']
    AnsibleJSONDecoder.set_secrets(tuple(secrets))
    decoder = AnsibleJSONDecoder()
    ansible_decoded_data = decoder.decode(json.dumps(data))
    assert ansible_decoded_data['__ansible_vault'].vault is not None

# Generated at 2022-06-13 06:47:22.733084
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Wrap an unsafe object
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;foo;4612345678345690878901234567890',
             '__ansible_unsafe': '$ANSIBLE_UNSAFE'}
    json_decoder = AnsibleJSONDecoder()
    pairs = json_decoder.object_hook(pairs)

    assert isinstance(pairs, dict)
    assert pairs['__ansible_vault'] == '$ANSIBLE_VAULT;1.2;AES256;foo;4612345678345690878901234567890'
    assert pairs['__ansible_unsafe'] == '$ANSIBLE_UNSAFE'


# Generated at 2022-06-13 06:47:27.296701
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    text = '{"__ansible_vault": "my vault text","__ansible_unsafe": "my unsafe text"}'
    actual = AnsibleJSONDecoder().decode(text)
    assert actual['__ansible_vault'] == AnsibleVaultEncryptedUnicode('my vault text')
    assert actual['__ansible_unsafe'] == wrap_var('my unsafe text')



# Generated at 2022-06-13 06:47:41.835815
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret']

# Generated at 2022-06-13 06:47:50.122732
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import copy
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultSecret

    secrets = [VaultSecret('a', 'b')]
    pytest_args = {
        '__ansible_unsafe':{
            'type':'text',
            'value':'c'
        }
    }
    pytest_result = {
        '__ansible_unsafe': AnsibleUnsafeText(value='c')
    }
    pytest_args_vault = copy.deepcopy(pytest_args)
    pytest_args_vault['__ansible_vault'] = '0123'

    x = AnsibleJSONDecoder()
    x.set_secrets(secrets)
    assert x.object_

# Generated at 2022-06-13 06:47:59.310006
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Given
    def _create_json_with_unsafe_field():
        return """
        {
            "__ansible_unsafe": "{{ vault_password }}"
        }
        """

    json_with_unsafe_field = _create_json_with_unsafe_field()

    # When
    decoded_json = json.loads(json_with_unsafe_field, cls=AnsibleJSONDecoder)

    # Then
    assert(hasattr(decoded_json, '__ansible_unsafe'))

# Generated at 2022-06-13 06:48:09.736110
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    dec = AnsibleJSONDecoder()
    # Test empty object
    assert dec.object_hook({}) == {}
    # Test __ansible_vault
    assert type(dec.object_hook({'__ansible_vault': 'foo'})) == AnsibleVaultEncryptedUnicode
    assert dec.object_hook({'__ansible_vault': 'foo'}) == 'foo'
    # Test __ansible_unsafe
    assert dec.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')
    # Test various combinations
    assert type(dec.object_hook({'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'})) == AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:48:20.384600
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    an = AnsibleJSONDecoder(strict=False)
    # Testing for string of json containing __ansible_unsafe key.
    string = '{"__ansible_unsafe": "{\\"ansible_ssh_host\\":\\"127.0.0.1\\"}"}'
    data = json.loads(string, object_hook=an.object_hook)
    assert data == wrap_var({"ansible_ssh_host": "127.0.0.1"})

    # Testing for string of json containing __ansible_vault key.
    string = '{"__ansible_vault": "AQAAABAAAAAMV2dhEAAAAAO3VtYW4vYW5zaWJsZS9pb3MucGhw"}'
    ansible_vault_encrypted_unicode = AnsibleV

# Generated at 2022-06-13 06:48:31.994848
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys
    import os

    # Generate a random string for use as vault password
    import random
    import string
    password = ''.join(random.choice(string.ascii_uppercase +
                                     string.ascii_lowercase +
                                     string.digits) for _ in range(32))

    vault_file_name = 'json_vault_file.yml'
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(password)
    with open(vault_file_name, 'w') as encrypted:
        encrypted.write("{'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256'}\n")
    with open(vault_file_name) as encrypted:
        data = encrypted.read()
        #print("

# Generated at 2022-06-13 06:48:44.084556
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:56.528191
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    secret = "This is a secret"
    data = json.dumps({
        '__ansible_vault': secret
    }, cls=AnsibleJSONEncoder)
    res = json.loads(data, cls=AnsibleJSONDecoder)
    assert isinstance(res['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert res['__ansible_vault'].vault is None
    res['__ansible_vault'].vault = decoder._vaults['default']
    assert res['__ansible_vault'].decrypt() == secret

# Generated at 2022-06-13 06:49:04.247288
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Arrange
    pairs = {
        '__ansible_vault': 'AESv1.1$ffcfc80b347e4444a36d6e60c7eb1f93$njmEQgDm9lFtA/nHm0fKtjUkD+WwZbvz0GcP0o+92KtJ1Md0MCPXc+YuhPr2QhyWw0o3J48ZKj+kLrGKfhRMA==',
        '__ansible_unsafe': True
    }
    expected = AnsibleVaultEncryptedUnicode(pairs['__ansible_vault'])
    expected.vault = VaultLib(secrets=['secret1', 'secret2'])

    # Act
    decoder = Ans

# Generated at 2022-06-13 06:49:13.267241
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    # test for a value `__ansible_vault`
    test_value = {'__ansible_vault': 'Test Value'}
    json_decoder = AnsibleJSONDecoder()
    assert AnsibleVaultEncryptedUnicode('Test Value') == json_decoder.object_hook(test_value)

    # test for a value `__ansible_unsafe`
    test_value = {'__ansible_unsafe': 'Test Value'}
    json_decoder = AnsibleJSONDecoder()
    assert wrap_var('Test Value') == json_decoder.object_hook(test_value)

    # test for a value not in whitelist
    test_value = {'test-value': 'Test Value'}
    json_decoder = AnsibleJSONDecoder()
    assert test_value == json_

# Generated at 2022-06-13 06:49:23.860874
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

    # some arbitrary data

# Generated at 2022-06-13 06:49:36.056776
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.parsing.vault import VaultSecret

    ansible_module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
        add_file_common_args=True,
    )

    # Test with ansible_vault
    raw_data = to_text('{"__ansible_vault":"test"}')
    decoded = json.loads(raw_data, cls=AnsibleJSONDecoder)
    assert decoded == {'__ansible_vault': 'test'}
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)

    # Test without ansible_vault
    raw

# Generated at 2022-06-13 06:49:48.576513
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook('a string') == 'a string'
    assert AnsibleJSONDecoder.object_hook([]) == []
    assert AnsibleJSONDecoder.object_hook(1) == 1
    assert AnsibleJSONDecoder.object_hook(['a string']) == ['a string']
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;1234567890123456', 'key': 'value'}) == {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;1234567890123456', 'key': 'value'}

# Generated at 2022-06-13 06:49:58.002225
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test default value
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': '1234'}) == {'__ansible_vault': '1234'}

    # Test AnsibleVaultEncryptedUnicode
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets('password')
    dec_obj = decoder.object_hook({'__ansible_vault': '1234'})
    assert isinstance(dec_obj, AnsibleVaultEncryptedUnicode)
    assert dec_obj.vault is not None
    assert dec_obj.vault.decrypt('1234') == '1234'

    # Test AnsibleUnsafeText

# Generated at 2022-06-13 06:50:06.815704
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Set the ansible vault secret to 'test'
    AnsibleJSONDecoder.set_secrets(['test'])

    # Object which has an encrypted object

# Generated at 2022-06-13 06:50:14.761728
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import six

# Generated at 2022-06-13 06:50:30.264847
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:48.314341
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    value = {
            "__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256",
            "__ansible_unsafe": "This is a value"
    }
    decoder = AnsibleJSONDecoder()
    decoded = decoder.object_hook(value)

    assert isinstance(decoded["__ansible_vault"], AnsibleVaultEncryptedUnicode)
    assert decoded["__ansible_unsafe"] == "This is a value"


# Generated at 2022-06-13 06:50:56.369196
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ["$ANSIBLE_VAULT;1.1;AES256;test\n3539376664373363626262316665326432396564326334616464313330326364663031663038643266\n3631353938333234323539383034663330323461626439666463613231383233336136333635336265\n63333566343037393365666637323261366331613663633165\n"]
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:51:05.103195
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_string = '$ANSIBLE_VAULT;1.1;AES256'
    ansible_vault_string += '663831656466343533373836383131636464376231396135313232626463376232653035653966373365'
    ansible_vault_string += '643261313464353462653165323532353263356235666439373864'
    data = {
        '__ansible_vault': ansible_vault_string
    }

    ansible_json_decoder = AnsibleJSONDecoder()
    data = ansible_json_decoder.object_hook(data)
    assert isinstance(data, dict)

# Generated at 2022-06-13 06:51:16.301042
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    # empty object
    assert decoder.object_hook({}) == {}
    # non empty object
    assert decoder.object_hook({'a': 'b'}) == {'a': 'b'}
    # non empty object with special key
    assert isinstance(decoder.object_hook({'__ansible_vault': 'secret_data'}), AnsibleVaultEncryptedUnicode)
    assert isinstance(decoder.object_hook({'__ansible_unsafe': 'secret_data'}), wrap_var)
    # non empty object with special key and value

# Generated at 2022-06-13 06:51:23.526067
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # ansible_vault
    input = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n1234567890123456789012345678901234567890123456789012345678901234\n1234\n'}
    decoder = AnsibleJSONDecoder()
    decoded = decoder.decode(json.dumps(input))
    assert isinstance(decoded, dict)
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert decoded['__ansible_vault'].vault is None

# Generated at 2022-06-13 06:51:36.781593
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    pairs = {'__ansible_vault': 'vault_password', '__ansible_unsafe': 'Unsafe stuff'}
    result = decoder.object_hook(pairs)

    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert isinstance(result, wrap_var)

    pairs = {'__ansible_vault': 'vault_password'}
    result = decoder.object_hook(pairs)

    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert not isinstance(result, wrap_var)

    pairs = {'__ansible_unsafe': 'Unsafe stuff'}
    result = decoder.object_hook(pairs)
