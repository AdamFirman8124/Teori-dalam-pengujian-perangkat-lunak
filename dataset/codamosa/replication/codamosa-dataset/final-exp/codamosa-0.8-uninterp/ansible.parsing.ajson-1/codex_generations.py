

# Generated at 2022-06-13 06:41:32.714324
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:41:42.756358
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # json decoder can handle not only strings with dicts but also
    # dicts
    test_value = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256\n633636336665333364373331346435653262353262313961366564346637646231633138393830\n613237643234313230336164643437306462303464353134633231636237376263346361373761\n343539653764303262326131393864383765346633\n',
        '__ansible_unsafe': 'You can see this'
    }
    # pylint: disable=protected-access
    result = AnsibleJSONDecoder().object_hook(test_value)

# Generated at 2022-06-13 06:41:54.689004
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys

    # Loading library for unit test
    if sys.version_info[0] >= 3:
        from importlib import reload
    try:
        from ansible.parsing.dataloader import DataLoader
    except ImportError:
        from ansible.utils.module_docs import DATA_LOADER_PATH
        sys.path.insert(0, DATA_LOADER_PATH)
        reload(sys)

        from ansible.parsing.dataloader import DataLoader

    # Creating testing object
    testing_object = DataLoader()

    # Testing object_hook method with __ansible_vault key
    AnsibleJSONDecoder._vaults['default'] = None
    testing_object._decoder = AnsibleJSONDecoder
    testing_object._decoder.set_secrets(secrets=['test'])



# Generated at 2022-06-13 06:42:04.332808
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var
    import json

    # Unit test for method object_hook of class AnsibleJSONDecoder
    # Test if the object_hook method of the AnsibleJSONDecoder class returns a
    # wrapped object with key '__ansible_unsafe'
    decoder = AnsibleJSONDecoder()
    pairs = {
        '__ansible_unsafe': 'value'
    }
    output = decoder.object_hook(pairs)
    assert isinstance(output, wrap_var)
    assert output.__original_value__ == 'value'

    # Test if the object_hook method of the AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:16.732661
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    set_secrets = ["h3lloW0r1d"]
    decoder = AnsibleJSONDecoder()
    decoder.set_secrets(set_secrets)

# Generated at 2022-06-13 06:42:30.948512
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:42:37.195864
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    abc = {
        'ansible_vault': {
            '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n31323334353637383930313233343536'
        },
        'ansible_unsafe': {
            '__ansible_unsafe': "abc"
        }
    }
    AnsibleJSONDecoder.set_secrets('123456')
    observed = AnsibleJSONDecoder(object_pairs_hook=dict).decode(json.dumps(abc))
    expected = { 'ansible_vault': "abcd", 'ansible_unsafe': "abc" }
    assert observed == expected


# Generated at 2022-06-13 06:42:49.839333
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    class TestObj(object):
        def __init__(self, value):
            self.value = value
    # Str2Obj:
    # __ansible_vault -> AnsibleVaultEncryptedUnicode
    # __ansible_unsafe -> wrap_var(value)
    # else -> pairs
    json_str = '{"__ansible_vault": "encrypt_str", "__ansible_unsafe": 1, "key1": "value1"}'
    json_obj = dict(__ansible_vault="encrypt_str", __ansible_unsafe=1, key1="value1")

# Generated at 2022-06-13 06:42:58.904941
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:43:06.483418
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:43:14.315049
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = b'$ANSIBLE_VAULT;1.1;AES256\n3435383666373566613962376337616666653237633738623761666335383939343463336133\n6466373433633231333336633530626566333534396264363266633366393736383361663265\n3162363561306536653338353531346462623965363565393866633563396530623564636262\n630a323938613965616136393666313961356633386165313539386661653130336638373936\n3866643634663335376264626431336538383238373635663732363633643639646430313230\n'
   

# Generated at 2022-06-13 06:43:18.156386
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = 'secrets'
    AnsibleJSONDecoder.set_secrets(secrets)

    value = {"__ansible_vault": "abc"}
    result = AnsibleJSONDecoder.object_hook(value)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault.secrets == secrets

    value = {"__ansible_unsafe": "abc"}
    result = AnsibleJSONDecoder.object_hook(value)
    assert isinstance(result, wrap_var)

# Generated at 2022-06-13 06:43:22.898465
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    input_data = None
    output_data = None

    decoder = AnsibleJSONDecoder()

    # load vault password from stdin (must be the first thing tested?)
    decoder._vaults['default'] = VaultLib(secrets=['test_vault_secret'])

    input_data = b'{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256"}'
    output_data = decoder.decode(input_data)
    assert isinstance(output_data, AnsibleVaultEncryptedUnicode)

    input_data = b'{"__ansible_unsafe": "password"}'
    output_data = decoder.decode(input_data)
    assert isinstance(output_data, AnsibleVaultEncryptedUnicode)

    output_data = decoder

# Generated at 2022-06-13 06:43:32.339798
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    test_data = {
        "__ansible_vault": "2.2$I5wCZzYIfB1e9QJhK4b4WyCBTRWHCrbIhJE1nSjKZ7Y",
        "var": "value"
    }
    expected_data = {
        "__ansible_vault": "2.2$I5wCZzYIfB1e9QJhK4b4WyCBTRWHCrbIhJE1nSjKZ7Y",
        "__ansible_unsafe": False,
        "var": "value"
    }
    decoded_data = AnsibleJSONDecoder.object_hook(test_data)

    assert expected_data == decoded_data

# Generated at 2022-06-13 06:43:44.004794
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Method to test object_hook method of class AnsibleJSONDecoder
    '''
    json_decoder = AnsibleJSONDecoder()
    json_decoder.set_secrets(['secret_string'])


# Generated at 2022-06-13 06:43:53.810698
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['hunter2']
    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    decoder.set_secrets(secrets)

    #test a vault variable
    pairs = {u'__ansible_vault': u'$ANSIBLE_VAULT;1.1;AES256;some_user\r\n1234567890qwertyuiop\r\n'}
    decoded_vault = decoder.object_hook(pairs)
    assert decoded_vault['__ansible_vault'] == AnsibleVaultEncryptedUnicode(pairs['__ansible_vault'])
    assert decoded_vault['__ansible_vault'].vault == decoder._vaults['default']

    #test a unsafe variable
   

# Generated at 2022-06-13 06:44:03.142810
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    obj = "{\"__ansible_unsafe\": \"{{ '\\\\n'.join([str(x) for x in range(1, 11)]) }}\"}"
    ansible_json = json.loads(obj, cls=AnsibleJSONDecoder)
    assert isinstance(ansible_json, dict)
    assert ansible_json["__ansible_unsafe"] == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"


# Generated at 2022-06-13 06:44:14.313494
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import os.path
    import inspect
    import tempfile
    import yaml
    from ansible.module_utils.common._json_compat import json
    cur_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    secrets_file = os.path.join(cur_dir, 'files', 'ansible-vault-secrets.yml')
    secrets = yaml.safe_load(open(secrets_file))['ansible-vault']
    decoder = AnsibleJSONDecoder()


# Generated at 2022-06-13 06:44:26.496890
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import sys

    class MockVaultLib(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class TestClass(object):
        def test_method(self):
            test_ok = True

        def test_method2(self):
            raise Exception('error')

        def test_method3(self):
            raise Exception('error')

        def test_method4(self):
            return "error"

        def test_method5(self):
            return None

        def test_method6(self):
            return ""

        @property
        def test_property(self):
            return "ok"

        @staticmethod
        def test_static_method():
            return "ok"


# Generated at 2022-06-13 06:44:37.041848
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # construct test data
    test_dict = {
        '__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;testuser\n656262613763643835376164663033373361386434663035393362393761353638\n336135366264393036656632333732333462383531333564626162346337316338\n643733376464626138613562366339343362383238666162626335623539616338\n393830383666316539373532636332366238356566326235356663323166626137\n33\n',
    }
    # test obj_hook function
    obj = AnsibleJSONDecoder().object_hook(test_dict)
   

# Generated at 2022-06-13 06:44:41.751872
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert isinstance(decoder, json.JSONDecoder)
    j = json.loads('{"__ansible_vault": "AES256"}', cls=AnsibleJSONDecoder)
    assert j == 'AES256'



# Generated at 2022-06-13 06:44:56.242404
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = [b'bogus']


# Generated at 2022-06-13 06:45:07.920448
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    class FakeVaultLib(object):
        def __init__(self, secrets=None):
            pass

    secrets = ['test']
    test_json = json.dumps({'__ansible_vault': 'test', '__ansible_unsafe': 'test'}, cls=AnsibleJSONEncoder)
    AnsibleJSONDecoder.set_secrets(secrets)
    data = json.loads(test_json, cls=AnsibleJSONDecoder)
    assert data['__ansible_vault'] == 'test'
    assert isinstance(data['__ansible_vault'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 06:45:18.327684
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    v = '$ANSIBLE_VAULT;1.1;AES256'
    s = '7563616c74'
    def set_secrets(s):
        secrets = [s]
        AnsibleJSONDecoder.set_secrets(secrets)

    set_secrets(s)
    test_case_1 = {'__ansible_vault': v}
    test_case_2 = {'__ansible_unsafe': 'test'}
    test_case_3 = {'__ansible_vault': v, '__ansible_unsafe': 'test'}
    ansible_jsonDecoder = AnsibleJSONDecoder()
    # Condition 1
    ansible_jsonDecoder.set_secrets(s)

# Generated at 2022-06-13 06:45:25.971451
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:45:37.707109
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ["hello", "world"]
    AnsibleJSONDecoder.set_secrets(secrets)

    data1 = {
        '__ansible_unsafe': '$ANSIBLE_VAULT;1.1;AES256;ansible\n6361613461386336363731393665376538333634343163313339363261316530376636613531650a62333632353231636262333062333665656463623131623961326262313837643966336431380a6465343764383965643031383637306466366132313462353163346339666463656438333664\n',
        '__ansible_unsafe_key': '1.1;AES256;ansible'
    }

# Generated at 2022-06-13 06:45:47.573926
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class TestPairs(dict):
        pass

    test_pairs = TestPairs()
    test_pairs['__ansible_vault'] = 'foo'
    test_pairs['__ansible_unsafe'] = 'bar'

    decoder = AnsibleJSONDecoder()
    test_pairs = decoder.object_hook(test_pairs)

    assert isinstance(test_pairs, AnsibleVaultEncryptedUnicode)
    assert isinstance(test_pairs.vault, VaultLib)
    assert test_pairs.vault.secrets == {}

    assert isinstance(test_pairs, AnsibleVaultEncryptedUnicode)
    assert decoder._vaults['default'] == test_pairs.vault

# Generated at 2022-06-13 06:45:55.448767
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_string = '{"__ansible_vault": "vault_value", "__ansible_unsafe": "unsafe_value", "__other_key": "other_value"}'
    secrets = {'default': 'AES256'}

    # Test vault and unsafe values
    decoder = AnsibleJSONDecoder()
    AnsibleJSONDecoder.set_secrets(secrets)
    decoded_obj = decoder.decode(json_string)
    assert decoded_obj['__ansible_vault'].vault.secrets == secrets
    assert decoded_obj['__ansible_unsafe'].value == 'unsafe_value'
    assert decoded_obj['__other_key'] == 'other_value'

    # Test no secrets
    decoder = AnsibleJSONDecoder()
    decoded

# Generated at 2022-06-13 06:46:06.190201
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['ansible']
    unsafe_data = b'{"__ansible_unsafe": "UNSAFE"}'
    vault_data = b'{"__ansible_vault": "VAULT"}'
    jd = AnsibleJSONDecoder.set_secrets(secrets)
    unsafe = AnsibleJSONDecoder(unsafe_data)
    vault = AnsibleJSONDecoder(vault_data)
    assert(unsafe.object_hook()=={'__ansible_unsafe': 'UNSAFE'})
    assert(vault.object_hook()=={'__ansible_vault': 'VAULT'})
    assert(wrap_var(unsafe_data).value=='UNSAFE')
    assert(wrap_var(vault_data).value=='VAULT')

# Generated at 2022-06-13 06:46:16.774725
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['secret1', 'secret2']
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:46:33.621750
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 06:46:41.248588
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:46:55.277960
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import json


# Generated at 2022-06-13 06:47:05.392588
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    value = {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n336431363465653831306231626461333539393564363231303566303864663436366332396237\n65623331323162613961313964613837303365643766376430663233616663395f5d0a\n'}
    vault_passwords = {'default': 'pass123'}
    # set_secrets
    AnsibleJSONDecoder.set_secrets(vault_passwords)
    decoder = AnsibleJSONDecoder()
    decoded_value = decoder.object_hook(value)

# Generated at 2022-06-13 06:47:16.318593
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    secrets = [
        {
            'password': 'secret'
        }
    ]
    AnsibleJSONDecoder.set_secrets(secrets)

    decoder = AnsibleJSONDecoder()

    # test __ansible_vault
    json_data = '{"__ansible_vault": "VFRWQ1Q1NlJrMHZaM1ZsTldSbE9XVmxaalJsWkdWakpLVVRGT1" }'
    data = decoder.decode(json_data)
    assert type(data) is dict
    assert type(data['__ansible_vault']) is AnsibleVaultEncryptedUnicode
    # cannot decrypt because there is no vault secret
    assert data['__ansible_vault'].vault is None

    # test __ansible

# Generated at 2022-06-13 06:47:19.612254
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    json_string = '{"a": 123, "__ansible_vault": "foo"}'
    assert json.loads(json_string, cls=AnsibleJSONDecoder).get('__ansible_vault') == 'foo'


# Generated at 2022-06-13 06:47:28.115348
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_str = '$ANSIBLE_VAULT;1.2;AES256;mattdean'
    ansible_vault_str_ext = '$ANSIBLE_VAULT;1.2;AES256;mattdean\n'

    ansible_unsafe_str = '$ANSIBLE_UNSAFE;1.2'
    ansible_unsafe_str_ext = '$ANSIBLE_UNSAFE;1.2\n'

    json_str = '{"ansible_vault": "%s", "ansible_unsafe": "%s"}' % (
        ansible_vault_str, ansible_unsafe_str)

# Generated at 2022-06-13 06:47:41.921133
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({'__ansible_vault': 'my_secret_data'})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault is None

    secrets = 'my_secret'
    AnsibleJSONDecoder.set_secrets(secrets)
    result = decoder.object_hook({'__ansible_vault': 'my_secret_data'})
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault is not None
    assert result.vault.secrets
    assert result.vault.secrets[0] == secrets

    # Resetting the secrets
    AnsibleJSONDecoder.set_secrets(None)
    result = decoder.object

# Generated at 2022-06-13 06:47:50.148597
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    secrets = [u'unicode_string']
    AnsibleJSONDecoder.set_secrets(secrets)
    d = dict(__ansible_vault='$ANSIBLE_VAULT;1.1;AES256;\n3131313131313...34646\n',
             __ansible_unsafe=dict(unsafe=AnsibleUnsafeText(u"unsafe stuff")))

    s = json.dumps(d, cls=AnsibleJSONEncoder)

# Generated at 2022-06-13 06:48:01.993163
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # Setup our test objects
    vault_secret = 'secret'

# Generated at 2022-06-13 06:48:11.358834
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    import textwrap


# Generated at 2022-06-13 06:48:21.934911
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:48:32.555276
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    """ Test object_hook method of class AnsibleJSONDecoder """
    hook_result = AnsibleJSONDecoder().object_hook({
        '__ansible_vault': 'vault-data: foo'
    })

    assert isinstance(hook_result, AnsibleVaultEncryptedUnicode)
    assert hook_result.vault is None
    assert hook_result == 'vault-data: foo'

    assert AnsibleJSONDecoder().object_hook({
        '__ansible_unsafe': 'unsafe-data: foo'
    }) == wrap_var('unsafe-data: foo')

    assert AnsibleJSONDecoder().object_hook({
        '__foo': 'foo-data: foo'
    }) == {'__foo': 'foo-data: foo'}

# Generated at 2022-06-13 06:48:46.022001
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    '''
    Test AnsibleJSONDecoder.object_hook
    '''

    # Test 1: Unsupported Object Type
    o = {'__ansible_vault': False}
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook(o) == o

    # Test 2: Supported Object Type
    decoder = AnsibleJSONDecoder()
    vault_tokens = {'vault_password': 'vault_password'}
    decoder.set_secrets(vault_tokens)
    o = {'__ansible_vault': '$ANSIBLE_VAULT;1.2;AES256;test\nblahblahblah==\n'}


# Generated at 2022-06-13 06:48:57.079725
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():

    def test_AnsibleJSONDecoder_object_hook_1():
        # Test a vault-encrypted value.
        s = '{ "__ansible_vault": "test", "__ansible_unsafe": "unsafe" }'
        d = AnsibleJSONDecoder().decode(s)
        assert '__ansible_vault' in d
        assert isinstance(d['__ansible_vault'], AnsibleVaultEncryptedUnicode)
        assert d['__ansible_vault'] == 'test'
        assert '__ansible_unsafe' in d
        assert d['__ansible_unsafe'] == wrap_var('unsafe')


# Generated at 2022-06-13 06:49:05.057121
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {
        '__ansible_vault': 'foo',
        '__ansible_unsafe': 'bar'
    }
    secret = decoder.object_hook(pairs)
    assert secret.vault == None
    assert secret.value == 'foo'
    assert secret.as_crypted() == 'foo'
    assert secret.as_plaintext() == 'foo'
    assert secret.is_encrypted() == False
    assert secret.is_bytes() == False

# Generated at 2022-06-13 06:49:11.981580
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:49:23.057273
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

    assert decoder.object_hook({'__ansible_vault': 'thisisaverylongandcomplicatedbase64string'}) == AnsibleVaultEncryptedUnicode('thisisaverylongandcomplicatedbase64string')
    assert decoder.object_hook({'__ansible_unsafe': {'__ansible_unsafe': 'string', '__ansible_vault': 'thisisaverylongandcomplicatedbase64string'}}) == {'__ansible_unsafe': wrap_var('string'), '__ansible_vault': AnsibleVaultEncryptedUnicode('thisisaverylongandcomplicatedbase64string')}
    assert decoder.object_hook({}) == {}

# Generated at 2022-06-13 06:49:35.576809
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    expected_va = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n356533623662363166633133653635383762643937343335653935323736373366323937616438\n6466373364666639303561616334303965336536393133310a6534643063363036663565623966\n386663393135316432353166653039663132353166666137313361383134323165663066616262\n32306531323736373861\n')

# Generated at 2022-06-13 06:49:44.556923
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    secrets = ['testpass']
    vault_text = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          353532353734303233313032356665356662333566666130656236316130323065333739316236\n          3932633430326162663238611a0a63313563346463623364326539363034333964633236316234\n          3735663036313436623664353063323463356664396537643732\n          "
    json_text = '{"a":{"b":{"__ansible_vault": "%s"}},"__ansible_unsafe": "credentials"}' % vault_text.replace("\n", "\\n")

# Generated at 2022-06-13 06:49:57.824128
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook({'__ansible_vault': 'test'}) == AnsibleVaultEncryptedUnicode('test')
    assert decoder.object_hook({'__ansible_unsafe': 'test'}) == wrap_var('test')
    assert decoder.object_hook({'__ansible_vault_not': 'test'}) == {'__ansible_vault_not': 'test'}
    assert decoder.object_hook({'__ansible_unsafe_not': 'test'}) == {'__ansible_unsafe_not': 'test'}
    assert decoder.object_hook({}) == {}

# Generated at 2022-06-13 06:50:06.834411
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    vault = VaultLib(password_file='test.vault.key')
    passwd = 'ansible'

# Generated at 2022-06-13 06:50:14.791494
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder(object_hook=AnsibleJSONDecoder.object_hook)
    pairs = decoder.object_hook({'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\nblahblahblah'})
    assert isinstance(pairs, AnsibleVaultEncryptedUnicode)
    assert pairs._data == '$ANSIBLE_VAULT;1.1;AES256\nblahblahblah'
    value = wrap_var('hello')
    pairs = decoder.object_hook({'hello': 'world', '_ansible_unsafe': value})
    assert pairs['hello'] == 'world'
    assert isinstance(pairs['_ansible_unsafe'], wrap_var)

# Generated at 2022-06-13 06:50:30.341321
# Unit test for method object_hook of class AnsibleJSONDecoder

# Generated at 2022-06-13 06:50:38.970028
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    ansible_vault_encrypted_unicode = {"__ansible_vault": "12"}
    ansible_unsafe_str = {"__ansible_unsafe": "12"}
    ansible_unsafe_dict = {"__ansible_unsafe": {"foo": "bar", "baz": "qux"}}
    ansible_unsafe_list = {"__ansible_unsafe": ["foo", "bar", "baz"]}
    ansible_unsafe_nested = {"__ansible_unsafe": {"foo": "bar", "baz": ["qux", "abc", "xyz"]}}
    ansible_unsafe_nested2 = {"__ansible_unsafe": {"foo": "bar", "baz": {"key1": [1, 2], "key2": {"dict": "dict"}}}}



# Generated at 2022-06-13 06:50:48.731701
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    test_data = [
        (
            {
                u"__ansible_vault": u"vaulted"
            },
            AnsibleVaultEncryptedUnicode(u"vaulted")
        ),
        (
            {
                u"__ansible_unsafe": u"unsafe"
            },
            wrap_var(u"unsafe")
        )
    ]

    for d, res in test_data:
        ansible_json_decoder = AnsibleJSONDecoder()
        assert ansible_json_decoder.object_hook(d) == res

# Generated at 2022-06-13 06:50:56.716036
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    assert AnsibleJSONDecoder.object_hook(None) is None


# Generated at 2022-06-13 06:51:03.780253
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    # object hook test 1
    assert AnsibleJSONDecoder.object_hook({'__ansible_vault': 'vault_value'}) == AnsibleVaultEncryptedUnicode('vault_value')
    assert AnsibleJSONDecoder.object_hook({'__ansible_unsafe': 'unsafe_value'}) == wrap_var('unsafe_value')
    # object hook test 2
    assert AnsibleJSONDecoder.object_hook({'test_key': 'test_value'}) == {'test_key': 'test_value'}

# Generated at 2022-06-13 06:51:16.088249
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()

# Generated at 2022-06-13 06:51:23.173718
# Unit test for method object_hook of class AnsibleJSONDecoder
def test_AnsibleJSONDecoder_object_hook():
    decoder = AnsibleJSONDecoder()
    pairs = {
        '__ansible_vault': 'abcdef=='
    }
    pairs = decoder.object_hook(pairs)
    assert '__ansible_vault' in pairs

    pairs = {
        '__ansible_unsafe': '!vault |$ANSIBLE_VAULT;1.1;AES256;test;6783657234627893486278365873486\r\n35792365873256298346579283658723657834652789635783416589\r\n12365897324562897345682;\r\n'
    }
    pairs = decoder.object_hook(pairs)
    assert '__ansible_unsafe' in pairs