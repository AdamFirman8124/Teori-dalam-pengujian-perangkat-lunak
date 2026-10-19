

# Generated at 2022-06-13 06:41:31.869603
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Mocked data
    from collections import namedtuple
    from ansible.parsing.vault import VaultLib
    vault_password = '$ANSIBLE_VAULT;1.1;AES256\n'
    vault = VaultLib(vault_password=vault_password)
    vault_dict = {
        '__ansible_vault':
            vault_password
        }
    unsafe_dict = {'__ansible_unsafe': 'unsafe'}
    vault_unencoded_text = namedtuple("VaultUnencodedText", "decoded")(decoded="mocked")
    vault.decrypt = lambda x: vault_unencoded_text.decoded

    # Pre-configure vault decryption
    AnsibleJSONDecoder.set_secrets(secrets=vault_password)

   

# Generated at 2022-06-13 06:41:42.033966
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test for handling of __ansible_vault
    plaintext = 'foo'
    test_vault = VaultLib('secret')
    ciphertext = test_vault.encrypt(plaintext)

    assert(ciphertext != plaintext)

    pairs = {'__ansible_vault': ciphertext}
    result = AnsibleJSONDecoder().object_hook(pairs)['__ansible_vault']

    assert(type(result) == AnsibleVaultEncryptedUnicode)
    assert(result.vault == test_vault)
    assert(result == ciphertext)

    # Test for handling of __ansible_unsafe
    pairs = {'__ansible_unsafe': '<script>alert("XSS")</script>'}
    result = AnsibleJSONDecoder().object_hook(pairs)

# Generated at 2022-06-13 06:41:54.022607
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:01.229998
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    data1 = {"__ansible_vault": "a"}
    result1 = decoder.object_hook(data1)
    assert result1['__ansible_vault'].encode(b'utf-8') == b'a'
    data2 = {"__ansible_unsafe": "a"}
    result2 = decoder.object_hook(data2)
    assert result2['__ansible_unsafe'] == "a"

# Generated at 2022-06-13 06:42:13.094030
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    ajd = AnsibleJSONDecoder()
    # Test case for ansible_vault
    is_ansible_vault_encrypt = ajd.object_hook({"__ansible_vault": "encrypted_text"})
    assert isinstance(is_ansible_vault_encrypt, AnsibleVaultEncryptedUnicode)

    # Test case for ansible_unsafe
    # TODO: Setup the magicmock to test the object_hook method using wrap_var return value
    # is_ansible_unsafe = ajd.object_hook({"__ansible_unsafe": "unsafe_value"})
    # assert is_ansible_unsafe == wrap_var("unsafe_value")

# Generated at 2022-06-13 06:42:20.386490
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from traceback import format_exc
    from _ast import Raise
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.common.json import AnsiBleJSONEncoder

    def _test_object_hook(hook, msg, test, expect=None):
        try:
            got = json.loads(test, object_hook=hook)
        except ValueError:
            got = format_exc()
        if got == expect or (AnsiBleJSONEncoder(encoding='utf-8', sort_keys=True).encode(got) == AnsiBleJSONEncoder(encoding='utf-8', sort_keys=True).encode(expect)):
            print('ok %d - %s' % (1, msg))

# Generated at 2022-06-13 06:42:25.495002
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_value = '''$ANSIBLE_VAULT;1.1;AES256
61643833316438333164383331423937336466396237623434396134433630383539396466336361
35393263663930623331663532623234313964336665643331383664333939643635636465386332
34373739
!
'''
    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    decoder.set_secrets('password')

    try:
        json.loads(ansible_vault_value, cls=decoder)
    except Exception:
        pass

# Generated at 2022-06-13 06:42:35.704841
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [
        {'vault_id': 'test'},
        {'vault_id': 'test1', 'secrets': ['a', 'b']}
    ]
    json_str = '''{
        "k1": "v1",
        "__ansible_vault": "vault1",
        "k2": "v2",
        "__ansible_unsafe": "unsafe",
        "k4": "v4"
    }'''
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    result = decoder.decode(json_str)
    assert isinstance(result['k1'], str)
    assert isinstance(result['k2'], str)

# Generated at 2022-06-13 06:42:45.842862
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Tests
    test_input = dict()
    test_input['__ansible_vault'] = 'aGVsbG8gd29ybGQ='
    test_input['__ansible_unsafe'] = 'hello world'

    json_output = json.dumps(test_input, cls=AnsibleJSONEncoder)
    output = json.loads(json_output, cls=AnsibleJSONDecoder)

    assert output['__ansible_vault'].vault != None
    assert output['__ansible_unsafe'] == wrap_var('hello world')


# Generated at 2022-06-13 06:42:56.725738
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'"__ansible_vault"': 'I2FudWxpYmUgdiA3IGJveAo=', '__ansible_unsafe': 'RGVtbyBpcyBpbiB0aGUgZGF5cyBvZiB5b3VuZyBhZ2U='}
    assert decoder.object_hook(pairs) == {'__ansible_vault': 'I2FudWxpYmUgdiA3IGJveAo=', '__ansible_unsafe': 'RGVtbyBpcyBpbiB0aGUgZGF5cyBvZiB5b3VuZyBhZ2U='}


# Generated at 2022-06-13 06:43:05.927479
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = []
    secrets.append('password')
    secrets.append('ssh-key')
    secrets.append('public-key')

    obj = AnsibleJSONDecoder()
    obj.set_secrets(secrets)

    obj1 = AnsibleJSONDecoder()
    obj1.set_secrets(secrets)

# Generated at 2022-06-13 06:43:13.177035
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    encrypted_text = '$ANSIBLE_VAULT;1.1;AES256\n' \
                     '35366466396432653936646339346365386132366139343637623633653165323337663564626231\n' \
                     '37306536636532626266663133366331643837393330323063353565326533303736373533\n' \
                     '0c86d7b870e080fb0f7b0cfd6c8051a48f9d9ff0bce1457aea95df0a0fa47eab\n'
    decoded_text = 'plain text'

    vault = VaultLib(['vaultpassword'])
    enc = Ansible

# Generated at 2022-06-13 06:43:21.775340
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:25.598585
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    s = {"__ansible_vault": "fake value"}
    decoded = decoder.object_hook(s)
    assert isinstance(decoded, AnsibleVaultEncryptedUnicode)



# Generated at 2022-06-13 06:43:30.792260
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_string = '{"__ansible_vault": "test", "__ansible_unsafe": "test"}'
    data = json.loads(json_string, cls=AnsibleJSONDecoder)
    assert isinstance(data['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(data['__ansible_unsafe'], wrap_var)


# Generated at 2022-06-13 06:43:38.632728
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    plaintext = 'plaintext'

# Generated at 2022-06-13 06:43:50.411591
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = 'foo'

# Generated at 2022-06-13 06:43:59.768315
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder(strict=True)
    # test ansible_vault encrypted string
    secrets = ["secret1", "secret2"]
    decoder.set_secrets(secrets)

# Generated at 2022-06-13 06:44:10.742233
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ''' Test the AnsibleJSONDecoder object_hook method '''
    secret = "some secret"
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secret)

# Generated at 2022-06-13 06:44:22.358233
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    dict_ = dict(__ansible_vault='abcdef')

    # Test with a vault with secrets set
    secrets = ['password']
    AnsibleJSONDecoder.set_secrets(secrets)
    assert AnsibleJSONDecoder().object_hook(dict_) is not dict_
    assert AnsibleJSONDecoder().object_hook(dict_).vault is not None
    assert AnsibleJSONDecoder().object_hook(dict_).vault.secrets == secrets
    assert AnsibleJSONDecoder().object_hook(dict_).vault.secrets_path is None
    assert AnsibleJSONDecoder().object_hook(dict_).vault.password_file is None

    # Test with a vault with no secrets set
    dict_ = dict(__ansible_vault='abcdef')
    AnsibleJSONDecoder.set

# Generated at 2022-06-13 06:44:35.068937
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    try:
        import pytest
    except ImportError:
        import unittest
        import sys
        # pytest not installed
        class TestAnsibleJSONDecoderObjectHook(unittest.TestCase):

            def test_AnsibleJSONDecoder_object_hook(self):
                enc = AnsibleJSONEncoder()
                dec = AnsibleJSONDecoder()
                rawstr = "password123"
                vaultstr = enc.encode(rawstr)

                AnsibleJSONDecoder.set_secrets([rawstr])
                decoded_pairs = dec.decode(vaultstr)

                self.assertEqual(decoded_pairs, "password123")
                self.assertEqual(decoded_pairs, rawstr)
        sys.argv.append('-v')
        unittest.main

# Generated at 2022-06-13 06:44:38.161737
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = json.loads('{"__ansible_vault": "string"}', cls=AnsibleJSONDecoder)
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj == 'string'



# Generated at 2022-06-13 06:44:44.472595
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'myvalue'}) == AnsibleVaultEncryptedUnicode('myvalue')
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'myvalue'}) == wrap_var('myvalue')
    assert AnsibleJSONDecoder.object_hook({'mykey': 'myvalue'}) == {'mykey': 'myvalue'}


# Generated at 2022-06-13 06:44:52.138027
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Testing AnsibleVaultEncryptedUnicode object with a value
    value = 'ansible'
    vault = '$ANSIBLE_VAULT;1.1;AES256;sam\n36623561366135373065643534376433313337633134353164656662643939346533343865383061\n343262646630373466393661366366333303466383439363532366462386134366631333832623861\n65643131616563616232343032647d\n'
    assert isinstance(vault, str)
    assert Ansi

# Generated at 2022-06-13 06:44:58.152821
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert AnsibleVaultEncryptedUnicode == type(decoder.object_hook({'__ansible_vault': 'abcd'}))
    assert wrap_var('abcd') == decoder.object_hook({'__ansible_unsafe': 'abcd'})

# Generated at 2022-06-13 06:45:09.743693
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """ Test that we can get a valid dictionary when an AnsibleVaultEncryptedUnicode
    has been decoded as JSON.
    """

    secrets = [b'vaultpass']
    AnsibleJSONDecoder.set_secrets(secrets=secrets)
    test_data = {'hello': 'world',
                 '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n'
                                    '65616c7470617373\n'
                                    '7777772e7b226578\n'
                                    '63686172223a5b22\n'
                                    '7777772e7d0a\n'
                                    '0a',
                 '__ansible_unsafe': '$$${{ "hello": "world" }}'}
    json

# Generated at 2022-06-13 06:45:19.936535
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    """
    Test AnsibleJSONDecoder.object_hook method with the following cases:

    1. The input `pairs` is not a dictionary:
        - Input `pairs` is a string type
        - Input `pairs` is a list type
    2. The input `pairs` is a dictionary and does not contain '__ansible_vault' or '__ansible_unsafe'
    3. The input `pairs' is a dictionary and contains '__ansible_vault'
    4. The input `pairs' is a dictionary and contains '__ansible_unsafe'
    """

    decoder = AnsibleJSONDecoder()

    # Test #1 and #2:
    assert decoder.object_hook('string') == 'string'
    assert decoder.object_hook([1, 2]) == [1, 2]

# Generated at 2022-06-13 06:45:27.620115
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    f = u"$ANSIBLE_VAULT;1.1;AES256"
    sec = u"b2Jhcg=="
    sc = u"gAAAAABbQ11HwPku6GdD6RprzYSXirX_i7Hk-BZ4b-v4NY4_4sAriJT2zCeTFBvSRI9XJUbEMylZPEs1dI_N4xC4sG0BQT0-cTvBXRWX9bJCV1qZU3c="
    text = u"{\"__ansible_vault\": \"{0} {1}\n{2}\n\"}".format(f, sec, sc)
    secrets = ['test123']
    dec = AnsibleJSONDecoder()
    dec.set_sec

# Generated at 2022-06-13 06:45:35.740334
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'test'
    AnsibleJSONDecoder.set_secrets(secrets)
    encoder = AnsibleJSONEncoder()
    jsonData = {'__ansible_vault': {'__ansible_vault_encrypted_string': 'test'}}
    jsonString = encoder.encode(jsonData)

    decoder = AnsibleJSONDecoder()
    dataFromString = decoder.decode(jsonString)

    assert dataFromString['__ansible_vault'].vault.secrets == secrets, "Fail"

# Generated at 2022-06-13 06:45:39.888310
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # AnsibleVaultEncryptedUnicode
    secret = '$ANSIBLE_VAULT;1.1;AES256\n6438313330643466336435616462323661656436346237313337383938333664373031613932366266\n6339616562316437383538323265636632393533386334396337343466383262616135633934633164\n303336353334356562633463\n'
    obj = json.loads(secret, cls=AnsibleJSONDecoder)
    assert isinstance(obj, AnsibleVaultEncryptedUnicode)
    assert obj.data == vault_password
    assert obj.vault.secrets == {'default': vault_password}

    # do not process this if you

# Generated at 2022-06-13 06:45:51.897014
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os
    vaultfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'vault.json')

    # We need to read the vault file to get the vault password
    vault_data = open(vaultfile).read()
    secrets = json.loads(vault_data)
    secrets = secrets.get('default_password')

    # Let's use the secret to decode the vault
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:45:56.683942
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook({'foo': 'bar'}) == {'foo': 'bar'}
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'foo'}) == AnsibleVaultEncryptedUnicode('foo')
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'foo'}) == wrap_var('foo')

# Generated at 2022-06-13 06:46:04.476190
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret_test']
    # Setup
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)
    pairs = {'__ansible_vault': 'test', '__ansible_unsafe': 'safe'}
    # Execute
    value = decoder.object_hook(pairs)
    # Assert
    assert value == 'test'
    assert value.vault == decoder._vaults['default']
    assert value.vault.secrets == secrets
    assert value.vault.secrets_filename == ['__ansible_vault', '__ansible_vault_secret_test']

# Generated at 2022-06-13 06:46:18.548735
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret = 'secret'
    vault_id = 'vault_id'
    vault_secrets = {vault_id: secret}
    AnsibleJSONDecoder.set_secrets(vault_secrets)

    decoder = AnsibleJSONDecoder()

    encrypted_value = '$ANSIBLE_VAULT;1.1;AES256;vault_id'
    result = decoder.object_hook({'__ansible_vault': encrypted_value})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault
    assert result.vault.secrets == vault_secrets

    safe_value = 'safe_value'
    result = decoder.object_hook({'__ansible_unsafe': safe_value})
    assert isinstance(result, wrap_var)

# Generated at 2022-06-13 06:46:33.410724
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_vault_key = 'test_vault_key'
    test_vault_secret = 'test_vault_secret'
    test_vault_variable = 'test_vault_variable_decoded'

# Generated at 2022-06-13 06:46:41.130062
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Make sure vault test works
    class MyDecoder(AnsibleJSONDecoder):
        vault_secrets = [b'foo']

    secret = b'$ANSIBLE_VAULT;1.1;AES256\n61626365626365626364656263646564\n' \
             b'6263656263656263656263656263656263646564\n'
    secret = AnsibleVaultEncryptedUnicode(secret)
    assert secret.decrypt() == b'abcdefghijklmnopqrstuvwxyz'

    # single line secret, missing newline
    json_input = b'{"__ansible_vault": "' + secret + b'"}'

# Generated at 2022-06-13 06:46:47.865751
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_json_decoder = AnsibleJSONDecoder()
    dict = ansible_json_decoder.object_hook({"__ansible_vault": "test", "__ansible_unsafe": "test"})
    assert dict["__ansible_vault"] == "test"
    assert dict["__ansible_unsafe"] == "test"

# Generated at 2022-06-13 06:46:51.688689
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({'__ansible_unsafe': 'value'})
    assert(result.secret == 'value')
    assert(isinstance(result, wrap_var))


# Generated at 2022-06-13 06:46:55.738303
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_unsafe': 'password'}
    res = decoder.object_hook(pairs)
    assert res == {'__ansible_unsafe': wrap_var('password')}


__all__ = ['AnsibleJSONEncoder', 'AnsibleJSONDecoder']

# Generated at 2022-06-13 06:47:06.078327
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['ansible']
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets.copy())


# Generated at 2022-06-13 06:47:23.067708
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    args = ()
    ansible_vault = dict(key='encrypted')

# Generated at 2022-06-13 06:47:29.886168
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secret_string = 'secret string'
    vault_string = '$ANSIBLE_VAULT;1.1;AES256' + '\n' + \
        AnsibleJSONEncoder.encode(secret_string)

    # Case 1: No secrets are not provided
    decoded_secret_string = AnsibleJSONDecoder().decode(vault_string)
    assert decoded_secret_string == vault_string

    # Case 2: Provide secrets
    AnsibleJSONDecoder.set_secrets(secret_string)
    decoded_secret_string = AnsibleJSONDecoder().decode(vault_string)
    assert decoded_secret_string == secret_string

# Generated at 2022-06-13 06:47:43.961472
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # To test method object_hook, AnsibleVaultEncryptedUnicode class should be mocked because
    # it has __init__ method with arguments.
    class MockAnsibleVaultEncryptedUnicode(object):
        vault = None

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "AnsibleVaultEncryptedUnicode: %s" % self.value

    # Monkey patch base class AnsibleJSONDecoder so that it uses mocked
    # AnsibleVaultEncryptedUnicode class.
    AnsibleJSONDecoder.AnsibleVaultEncryptedUnicode = MockAnsibleVaultEncryptedUnicode

    decoder = AnsibleJSONDecoder()

    # Test for __ansible_unsafe

# Generated at 2022-06-13 06:47:50.228631
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup AnsibleJSONDecoder.set_secrets()
    secrets = None
    test_AnsibleJSONDecoder = AnsibleJSONDecoder()
    test_AnsibleJSONDecoder.set_secrets(secrets)

    # Unit test for method object_hook of class AnsibleJSONDecoder with AnsibleVaultEncryptedUnicode
    # Test data for AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 06:48:01.992861
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    decoder = AnsibleJSONDecoder()

    # Case: Secret is not provided, fails
    pairs = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n3564363537303461373537336634303562373538636463626261623932316662643562363737\n39373439633932353537646539666432343132633762393239363736353834660a3736663530\n6335306635303466383438336263323135333164336436333233396236653866653133346538\n6331333434616332326163373165643238333834383764323535333066\n'}

# Generated at 2022-06-13 06:48:10.016554
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''Unit test function to test class AnsibleJSONDecoder 
    '''
    print('****** test_AnsibleJSONDecoder_object_hook')

    def _test_object_hook(self, pairs):
        assert(type(pairs) is dict)
        return json.JSONDecoder.object_hook(self, pairs)

    test_case = dict()
    test_case["__ansible_vault"] = "123"
    test_case["__ansible_unsafe"] = "456"

    decoder = AnsibleJSONDecoder()
    decoder.object_hook = _test_object_hook

    json.loads(json.dumps(test_case), cls=decoder)
    
if __name__ == "__main__":
    test_AnsibleJSONDecoder_object_hook()

# Generated at 2022-06-13 06:48:20.344474
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.vars.hostvars import HostVars

    secrets = [
        {'id': 'test', 'secret': 'test'},
        {'id': 'test1', 'secret': 'test1'}
    ]

    encoder = AnsibleJSONEncoder()
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(secrets)
    encrypted = encoder.encode({'__ansible_vault': 'foo', '__ansible_unsafe': 'bar'})
    decoded = decoder.decode(encrypted)
    assert isinstance(decoded['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(decoded['__ansible_unsafe'], HostVars)

# Generated at 2022-06-13 06:48:22.183089
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:32.423432
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook is None
    ansible_json_decoder = AnsibleJSONDecoder()
    assert ansible_json_decoder.object_hook is not None
    pairs = {'key1': 'value1', 'key2': 'value2'}
    assert ansible_json_decoder.object_hook(pairs) == pairs
    pairs = {'__ansible_vault': 'vault1'}
    assert isinstance(ansible_json_decoder.object_hook(pairs), AnsibleVaultEncryptedUnicode)
    pairs = {'__ansible_unsafe': 'unsafe1'}
    assert isinstance(ansible_json_decoder.object_hook(pairs), wrap_var)

# Generated at 2022-06-13 06:48:44.148305
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:08.151457
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    decoder.object_hook({'__ansible_vault': '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          37333035663036333534623435653038396562386336653232393436393861613666643737336439\n          35383764306634643166656335636235643866323363306264346661393166393839346337343565\n          383232623663393465353163376230646231313836666661383935\n          '})


# Generated at 2022-06-13 06:49:10.563775
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'yes': True})['yes'] is True
    assert decoder.object_hook({'no': False})['no'] is False

# Generated at 2022-06-13 06:49:13.407155
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {'__ansible_vault': 'Encrypted text here'}
    expected = AnsibleVaultEncryptedUnicode('Encrypted text here')
    assert decoder.object_hook(pairs) == expected

# Generated at 2022-06-13 06:49:23.970866
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:36.151429
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:49:43.784647
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    json_data = '{"__ansible_vault": "mysecret",'
    json_data += '"__ansible_unsafe": "myunsafe"}'

    secret = 'hello'
    decoder = AnsibleJSONDecoder.set_secrets(secrets=[secret])
    data = decoder.decode(json_data)

    assert isinstance(data, dict)
    assert '__ansible_vault' in data
    assert '__ansible_unsafe' in data
    assert data['__ansible_vault'].decrypt(secret) == 'mysecret'
    assert data['__ansible_unsafe'] == 'myunsafe'

# Generated at 2022-06-13 06:49:54.915924
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Test with ansible_vault/ansible_unsafe
    test_data = {
        "__ansible_vault": "foo",
        "__ansible_unsafe": "bar",
    }
    ansible_json_decoder = AnsibleJSONDecoder()
    pairs = ansible_json_decoder.object_hook(test_data)
    assert isinstance(pairs[list(pairs.keys())[0]], AnsibleVaultEncryptedUnicode)
    assert isinstance(pairs[list(pairs.keys())[1]], str)

    # Test without ansible_vault/ansible_unsafe
    test_data = {
        "foo": "bar",
    }
    ansible_json_decoder = AnsibleJSONDecoder()
    pairs = ansible_json_dec

# Generated at 2022-06-13 06:50:05.397868
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Arrange
    expected = 'This is a secret'
    vault = '$ANSIBLE_VAULT;1.1;AES256\n' \
            '3239356661643861663534303337616230373262386264656633666634303133353762366231643136\n' \
            '6530623939363635336461333132316665343531343065343865343136616232646530326561623964\n' \
            '323038623236343439643530663862316566633030663938313761333539\n'


# Generated at 2022-06-13 06:50:13.529855
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:28.923953
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    class DummyVault(object):
        def __init__(self, secrets):
            self.secrets = secrets
            self.password = secrets
            self.secrets_type = 'none'

        def decrypt(self, data):
            return data

    class DummySecrets(object):
        def get_vault_secrets(self, vault_ids, ask_vault_pass=True,
                              vault_password_files=None,
                              auto_prompt=None, unset_vault_password=False):
            return DummyVault(self)

    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(DummySecrets())


# Generated at 2022-06-13 06:51:04.758306
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = {
        "__ansible_vault": "12345",
        "__ansible_unsafe": "12345"
    }

    json_data = json.dumps(test_data, cls=AnsibleJSONEncoder)
    json_data = json.loads(json_data, cls=AnsibleJSONDecoder)

    assert isinstance(json_data['__ansible_vault'], AnsibleVaultEncryptedUnicode)
    assert isinstance(json_data['__ansible_unsafe'], str)

# Generated at 2022-06-13 06:51:16.160647
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup test object
    obj1 = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;my_secure', 'key1': 'value1'}
    obj2 = {'__ansible_unsafe': 'unsafe_value'}

    class DummyVaultLib(object):
        def __init__(self):
            pass

        def decrypt(self, string):
            return 'decrypted_value'

    secrets = ['password']
    AnsibleJSONDecoder.set_secrets(secrets)

    # Perform test
    test_obj1 = AnsibleJSONDecoder().object_hook(obj1)
    test_obj2 = AnsibleJSONDecoder().object_hook(obj2)

    # Assert correct data is returned

# Generated at 2022-06-13 06:51:21.190384
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    example_response = '{"returncode": 0, "message": "Success", "param": "{{ ansible_env.HOME }}", "__ansible_unsafe": [{"__ansible_vault": "encrypted", "__ansible_unsafe": "unsafe"}]}'
    decode_response = json.loads(example_response)
    decoder = AnsibleJSONDecoder()
    assert decode_response == decoder.object_hook(json.loads(example_response))

# Generated at 2022-06-13 06:51:28.605564
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Test object_hook
    '''

    obj = '{"__ansible_vault": "secret"}'
    pairs = AnsibleJSONDecoder.object_hook(json.loads(obj))
    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)

    obj = '{"__ansible_unsafe": "secret"}'
    pairs = AnsibleJSONDecoder.object_hook(json.loads(obj))
    assert isinstance(pairs, object)