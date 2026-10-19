

# Generated at 2022-06-12 23:06:45.340982
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    ansible_vault_object = object.__new__(AnsibleVaultEncryptedUnicode)
    ansible_vault_object.__ENCRYPTED__ = True
    ansible_vault_object._ciphertext = "foo"

    ansible_unsafe_object = object.__new__(AnsibleUnsafeText)
    ansible_unsafe_object.__UNSAFE__ = True

    assert AnsibleJSONEncoder().default(ansible_vault_object) == {'__ansible_vault': u'foo'}
    assert AnsibleJSONEncoder().default(ansible_unsafe_object) == {'__ansible_unsafe': u'foo'}



# Generated at 2022-06-12 23:06:52.927949
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import OrderedDict
    # https://github.com/ansible/ansible/blob/devel/hacking/test-module-utils-common.sh#L218
    # https://github.com/ansible/ansible/blob/devel/hacking/test-module-utils-common.sh#L230
    # https://github.com/ansible/ansible/blob/devel/hacking/test-module-utils-common.sh#L242

    from ansible.parsing.vault import VaultLib

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:07:03.817941
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder(preprocess_unsafe=True, indent=2).iterencode(dict(a=dict(b=dict(c=dict(d='1'))))) == b'{\n  "a": {\n    "b": {\n      "c": {\n        "d": "1"\n      }\n    }\n  }\n}'

    import uuid
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText
    u_unicode_safe = uuid.uuid4().hex

# Generated at 2022-06-12 23:07:13.974117
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import string_types

    encoder = AnsibleJSONEncoder()
    vault = VaultLib(StringIO(_VAULT_PASS), StringIO(_VAULT_PASS))

    # From test_AnsibleJSONEncoder.py
    # - other types have their own tests
    assert encoder.default('safe') == 'safe'
    assert isinstance(encoder.default(u'safe'), string_types)
    assert encoder.default(dict(a=1)) == dict(a=1)

# Generated at 2022-06-12 23:07:20.838513
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    import datetime

    try:
        from ansible.module_utils.common._collections_compat import Mapping
    except ImportError:
        pass

    from ansible.module_utils.common.collections import is_sequence

    # Create a json encoder, here will use AnsibleJSONEncoder
    e = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    # Test for private type of ansible
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types

    # Test for VaultLib and AnsibleUnsafe
    # 1. encode with default method
    # 2. encode with iterencode

    # Test for VaultLib
    # o is instance of VaultLib

# Generated at 2022-06-12 23:07:32.269149
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode(b'bytes_data') == '"bytes_data"'
    assert AnsibleJSONEncoder().encode(u'test_data') == '"test_data"'
    assert AnsibleJSONEncoder().encode(1) == '1'
    assert AnsibleJSONEncoder().encode(1.0) == '1.0'
    assert AnsibleJSONEncoder().encode(True) == 'true'
    assert AnsibleJSONEncoder().encode(False) == 'false'
    assert AnsibleJSONEncoder().encode(None) == 'null'
    assert AnsibleJSONEncoder().encode([1, 2, 3, 4]) == '[1, 2, 3, 4]'

# Generated at 2022-06-12 23:07:39.606462
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps(True, cls=AnsibleJSONEncoder)) is True
    assert json.loads(json.dumps(False, cls=AnsibleJSONEncoder)) is False
    assert json.loads(json.dumps(1, cls=AnsibleJSONEncoder)) == 1
    assert json.loads(json.dumps(1.0, cls=AnsibleJSONEncoder)) == 1.0
    assert json.loads(json.dumps('1', cls=AnsibleJSONEncoder)) == '1'
    assert json.loads(json.dumps(u'1', cls=AnsibleJSONEncoder)) == '1'
    assert json.loads(json.dumps([], cls=AnsibleJSONEncoder)) == []

# Generated at 2022-06-12 23:07:50.779105
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    encoder = AnsibleJSONEncoder()
    # assert that a vault object is serialized correctly
    o = AnsibleUnsafeText('foo')
    o.__ENCRYPTED__ = True
    assert encoder.default(o) == {'__ansible_vault': 'Zm9v'}
    # assert that a unsafe object is serialized correctly
    o = AnsibleUnsafeText('foo')
    assert encoder.default(o) == {'__ansible_unsafe': 'foo'}
    # assert that a dict object is serialized same as dict
    o = {'a': 'b'}
    assert encoder.default(o) == {'a': 'b'}
    # assert that a datetime object is serialized same

# Generated at 2022-06-12 23:08:00.858884
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
    from ansible.module_utils.six import string_types
    import datetime

    s = AnsibleJSONEncoder().default(None)
    assert s is None

    s = AnsibleJSONEncoder().default(True)
    assert s is True

    s = AnsibleJSONEncoder().default(False)
    assert s is False

    s = AnsibleJSONEncoder().default(1)
    assert s == 1

    s = AnsibleJSONEncoder().default(0)
    assert s == 0

    s = AnsibleJSONEncoder().default(0.0)
    assert s == 0.0

    s = AnsibleJSONEncoder().default

# Generated at 2022-06-12 23:08:11.303604
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class A:
        pass

    class B:
        pass

    b = B()
    setattr(b, '__ENCRYPTED__', False)
    b.cipher = b'123456789'
    b.__cipher = b.cipher
    b.__ciphertext = b.cipher

    encoder = AnsibleJSONEncoder()
    assert encoder.default(A()) == '<__main__.A object at 0x10a6c9358>'
    assert encoder.default(b) == {'__ansible_vault': 'MTIzNDU2Nzg5'}
    assert encoder.default('0') == '0'
    assert encoder.default(0) == 0
    assert encoder.default(True) == True

# Generated at 2022-06-12 23:08:23.570137
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje_dict = AnsibleJSONEncoder()
    assert aje_dict.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # hostvars
    assert aje_dict.default(dict(subset=dict(subsubset='subsub_value'))) == dict(subset=dict(subsubset='subsub_value'))

    # dict
    d = dict(subset=dict(subsubset='subsub_value'))
    assert aje_dict.default(d) == dict(subset=dict(subsubset='subsub_value'))

    # dict
    d_u = dict(subset=dict(subsubset='subsub_value'))
    d_u['__unsafe__'] = True
    assert aje_dict.default

# Generated at 2022-06-12 23:08:33.477112
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common import AnsibleUnsafe, AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_encryptor = VaultLib('vault_password')
    unsafe_string = AnsibleUnsafe("unsafe string")
    vault_obj = AnsibleVaultEncryptedUnicode(vault_encryptor.encrypt('1234567890'))
    plain_text = 'plain text'
    boolean_value = True
    integer_value = 42
    float_value = 3.14159

# Generated at 2022-06-12 23:08:43.036662
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils.six import string_types
    # tests for class AnsibleUnsafe
    from ansible.parsing.vault import VaultLib, VaultSecret, VaultAES256
    
    encoder = AnsibleJSONEncoder()
    
    # test for class AnsibleUnsafe
    class AnsibleUnsafe(string_types[0]):
        __UNSAFE__ = True
    # class AnsibleUnsafe is subclass of string_types
    assert issubclass(AnsibleUnsafe, string_types[0])
    
    o = AnsibleUnsafe('ansible_unsafe') 
    # since class AnsibleUnsafe is subclass of string_types, the return value should be a string
    assert isinstance(encoder.default(o), string_types[0])
    # try assert

# Generated at 2022-06-12 23:08:53.556498
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    import datetime as dt
    import os

    # data structures
    v = AnsibleVaultEncryptedUnicode(os.urandom(32))
    u = u'\x00'
    u.__UNSAFE__ = True

# Generated at 2022-06-12 23:09:00.450962
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    encoder = AnsibleJSONEncoder()

    # test for __ENCRYPTED__

# Generated at 2022-06-12 23:09:10.523301
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.inventory.host import Host
    from ansible.playbook.attribute import FieldAttribute
    from ansible.plugins.loader import get_all_plugin_loaders

    host = Host("example.com")
    host["ansible_version"] = FieldAttribute("ansible_version", "1.2.3")

    json_encoded = json.dumps(host, cls=AnsibleJSONEncoder, sort_keys=True)
    assert '"ansible_version": "1.2.3"' in json_encoded

    json_encoded = json.dumps(get_all_plugin_loaders(), cls=AnsibleJSONEncoder, sort_keys=True)
    assert "'dynamic_plugins/action':" in json_encoded

# Generated at 2022-06-12 23:09:20.723254
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Create object with attribute __ENCRYPTED__
    class TestClass1:
        __ENCRYPTED__ = True
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext

    obj1 = TestClass1("ciphertext_object_1")

    # Create object with attribute __ENCRYPTED__ and __UNSAFE__
    class TestClass2:
        __ENCRYPTED__ = True
        __UNSAFE__ = True
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext

    obj2 = TestClass2("ciphertext_object_2")

    # Create object with __UNSAFE__
    class TestClass3:
        __UNSAFE__ = True
        def __init__(self, text):
            self.text

# Generated at 2022-06-12 23:09:29.455074
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes
    secret = VaultSecret('$ANSIBLE_VAULT;1.1;AES256\nblahblahblahblah312312312312312\n')
    unsafe_text = AnsibleUnsafeText('foo bar baz')
    unsafe_bytes = AnsibleUnsafeBytes(b'foo bar baz')
    dict_1 = dict(foo='bar')
    dict_2 = dict(abc='xyz')
    dict_3 = dict(abc=dict_2)

# Generated at 2022-06-12 23:09:40.075903
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import u
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafeBytes

    enc = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)

    # unsafe text should be string with __ansible_unsafe key
    o = AnsibleUnsafeText('abcdef')
    assert enc.default(o) == {'__ansible_unsafe': u('abcdef')}

    # unsafe bytes should be string with __ansible_unsafe key
    o = AnsibleUnsafeBytes(b'abcdef')

# Generated at 2022-06-12 23:09:49.115156
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()

    assert 'test' == ansible_json_encoder.default('test')

    assert '{}' == ansible_json_encoder.default(dict())

    assert True == ansible_json_encoder.default(True)

    assert dict((k, ansible_json_encoder.default(v)) for k, v in {'a': 'b', 'c': 'd'}.items()) == ansible_json_encoder.default({'a': 'b', 'c': 'd'})


# Generated at 2022-06-12 23:10:02.060527
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-12 23:10:11.688133
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_cases = [
        (dict(a=1, b=2, c='c'), dict(a=1, b=2, c='c')),
        (1, 1),
        ('', ''),
        (set(), []),
        (set(['foo', 'bar']), ['foo', 'bar']),
        (set(['foo', 'bar', ['a', 'b']]), ['foo', 'bar', ['a', 'b']]),
        (datetime.datetime(2014, 5, 4, 17, 16, 15), '2014-05-04T17:16:15')
    ]

    ansible_json_encoder = AnsibleJSONEncoder()


# Generated at 2022-06-12 23:10:22.174229
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_no_vault_encoder = AnsibleJSONEncoder()
    json_no_vault_encoder_with_preprocess = AnsibleJSONEncoder(preprocess_unsafe=True)
    json_vault_encoder = AnsibleJSONEncoder(vault_to_text=True)
    json_vault_encoder_with_preprocess = AnsibleJSONEncoder(vault_to_text=True, preprocess_unsafe=True)

    assert json_no_vault_encoder.default(str()) == str()
    assert json_no_vault_encoder.default(str('test')) == str('test')
    assert json_no_vault_encoder.default(b'foo') == b'foo'

# Generated at 2022-06-12 23:10:30.679979
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # test parameter vault_to_text of class AnsibleJSONEncoder
    assert AnsibleJSONEncoder(vault_to_text=True).default(VaultLib(b'$ANSIBLE_VAULT;1.1;AES256', b'aaaaaaaaaa')) == b'aaaaaaaaaa'
    assert AnsibleJSONEncoder(vault_to_text=False).default(VaultLib(b'$ANSIBLE_VAULT;1.1;AES256', b'aaaaaaaaaa')) == {'__ansible_vault': b'aaaaaaaaaa'}

    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    # test parameter preprocess_unsafe of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:10:39.885171
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import text_type

    # Test for string
    expected = 'foo'
    actual = AnsibleJSONEncoder().default(expected)
    assert(actual == expected)

    # Test for date
    date_value = datetime.date(2001, 2, 3)
    expected = '2001-02-03'
    actual = AnsibleJSONEncoder().default(date_value)
    assert(actual == expected)

    # Test for date time
    date_time_value = datetime.datetime(2001, 2, 3, 4, 5, 6)
    expected = '2001-02-03T04:05:06'
    actual = AnsibleJSONEncoder().default(date_time_value)
    assert(actual == expected)

    # Test for date time with microsecond
    date_time_

# Generated at 2022-06-12 23:10:49.943103
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # [1]
    # input: __UNSAFE__ attribute
    # expected: {'__ansible_unsafe': 'unsafe_object'}
    value = 'unsafe_object'
    value.__UNSAFE__ = True
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    result = encoder.default(value)
    assert result == {'__ansible_unsafe': 'unsafe_object'}

    # [2]
    # input: datetime object
    # expected: '2018-12-26T21:39:17.637863'
    value = datetime.datetime(2018, 12, 26, 21, 39, 17, 637863)
    encoder = AnsibleJSONEncoder()
    result = encoder.default(value)
    assert result

# Generated at 2022-06-12 23:10:57.934380
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    string = '{"__ansible_vault": "V@ult-CipherText", "__ansible_unsafe": "Unsafe-None"}'
    json_data = json.loads(string)
    assert _is_vault(json_data["__ansible_vault"]) == True
    assert _is_unsafe(json_data["__ansible_unsafe"]) == True
    json_data_new = json.loads(json.dumps(json_data, cls=AnsibleJSONEncoder))
    assert json_data_new["__ansible_vault"] == 'V@ult-CipherText'
    assert json_data_new["__ansible_unsafe"] == 'Unsafe-None'

# Generated at 2022-06-12 23:11:04.950487
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def test_json(expected_json_str, o):
        encoder = AnsibleJSONEncoder()
        json_str = json.dumps(o, cls=encoder)
        assert(json_str == expected_json_str)

    test_json('{"key": "value"}', {'key': 'value'})
    test_json('[1, 2, 3]', [1, 2, 3])
    test_json('[{"key": "value"}]', [{'key': 'value'}])
    test_json('{"key": [1, 2, 3]}', {'key': [1, 2, 3]})


# Generated at 2022-06-12 23:11:14.446355
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # TODO: Remove this test when Jython removes support for 2.7
    # NOTE: The json module in Jython 2.7.1 does not support the datetime.date
    # and datetime.datetime classes in the default method of the json.JSONEncoder class
    # and needs those classes to be added.
    # See https://bugs.jython.org/issue2735

    # Create an instane of AnsibleJSONEncoder
    ansible_json_encoder = AnsibleJSONEncoder()

    # Create an instance of datetime.date
    date = datetime.date(2020, 6, 1)

    # Create an instance of datetime.datetime
    datetime_object = datetime.datetime(2020, 6, 1, 14, 6, 5)

    # Create a dictionary

# Generated at 2022-06-12 23:11:25.397855
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.collections import AnsibleUnsafe
    from ansible.module_utils.common.collections import AnsibleVaultEncryptedUnsafeText
    from ansible.module_utils.six import text_type
    # Test of the method default of class AnsibleJSONEncoder
    # In the previous version (e.g. 2.9.9) the method default of class AnsibleJSONEncoder
    # is only used for arguments that are instances of class datetime.
    # So, we only test arguments of class datetime.
    # AnsibleUnsafe can only be tested by iterencode
    # VaultLib does not have a method default
    # So, we test

# Generated at 2022-06-12 23:11:40.788435
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    This tests the default method of the AnsibleJSONEncoder class.
    '''
    # Test with encrypted value
    o = {'foo': {'__ansible_vault': 'cipher_text'}}
    assert(AnsibleJSONEncoder().default(o) == {'foo': {'__ansible_vault': 'cipher_text'}})
    assert(AnsibleJSONEncoder(True).default(o) == {'foo': {'__ansible_vault': 'cipher_text'}})
    assert(AnsibleJSONEncoder(True, True).default(o) == {'foo': 'cipher_text'})
    assert(AnsibleJSONEncoder(False, True).default(o) == {'foo': 'cipher_text'})

    # Test with unsafe value

# Generated at 2022-06-12 23:11:48.125446
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test the default method of AnsibleJSONEncoder
    '''
    from ansible.parsing.vault import VaultLib
    secret = 'value'
    vault_password = 'password'
    vault_secret = VaultLib(vault_password).encrypt(secret)
    instance = AnsibleJSONEncoder()

    # Test for the vault object
    assert instance.default(vault_secret) == {'__ansible_vault': vault_secret._ciphertext}

    # Test for regular object
    assert instance.default(secret) == secret

    # Test for the unsafe object
    unsafe_test_str = '@@test@@'
    class Unsafe(str):
        __UNSAFE__ = True

# Generated at 2022-06-12 23:11:57.903128
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import pprint
    d1 = {"test1":"1234", "test2":"42", "test3":{"test4":"15", "test5":{"test6":"77"}}}
    d1_encoded = json.dumps(d1, cls=AnsibleJSONEncoder, sort_keys=True)
    pprint.pprint(d1_encoded)
    assert d1_encoded == '{"test1": "1234", "test2": "42", "test3": {"test4": "15", "test5": {"test6": "77"}}}'
    d2 = {"test1":"1234", "test2":"42", "test3":{"test4":"15", "test5":{"test6":"77"}}, "test7": datetime.date(2017, 1, 12)}
    d2_encoded = json.d

# Generated at 2022-06-12 23:12:07.938250
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.compat import text_type
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    # vault object
    encoder=AnsibleJSONEncoder()
    o = VaultLib("")

# Generated at 2022-06-12 23:12:16.928783
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import datetime

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    from ansible.module_utils.hashivault import vault
    from ansible.module_utils.hashivault.util import hashivault_argspec
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.hashivault import HAS_HASHIVAULT

    parser = hashivault_argspec()
    argspec = parser.parse_args(['test', 'foo=bar'])
    password = boolean(argspec.password, strict=False)
    args = argspec.__dict__
    args['password'] = password
    args['vault_password'] = vault.VaultLib(args)._get_vault_password()
    args['client'] = vault

# Generated at 2022-06-12 23:12:24.693948
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Tests AnsibleJSONEncoder.default()
    '''

    from ansible.playbook.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import text_type

    vault_obj = VaultLib([('vault_password', text_type('ansible'))])

    plaintext = 'TEST'
    ciphertext = vault_obj.encrypt(plaintext)
    vault_secret = VaultSecret(ciphertext)
    vault_secret.__ENCRYPTED__ = True

    encoded_text = AnsibleJSONEncoder().default(vault_secret)
    assert encoded_text == {'__ansible_vault': ciphertext}

    plaintext = "TEST"

# Generated at 2022-06-12 23:12:32.574316
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    instance = AnsibleJSONEncoder()
    fake_date = datetime.datetime(2018, 5, 9, 6, 3, 59, 999997)
    fake_dict = {
        "key1": "value1",
        "key2": [1, 2, 3]
    }
    assert instance.default(fake_date) == '2018-05-09T06:03:59.999997'
    assert instance.default(fake_dict) == {'key1': 'value1', 'key2': [1, 2, 3]}

# Generated at 2022-06-12 23:12:41.200990
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    en = AnsibleJSONEncoder()
    x = 'x'
    assert en.default(x) == x
    x = datetime.datetime(2020, 3, 7, 14, 55, 12)
    assert en.default(x) == "2020-03-07T14:55:12"
    x = AnsibleUnsafeText(x)
    assert en.default(x) == {'__ansible_unsafe': '2020-03-07T14:55:12'}
    x = {"field1": "value1", "field2": 2}
    assert en.default(x) == x
    x = 'x'
    assert en.default(x) == x

# Generated at 2022-06-12 23:12:51.088948
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test str
    safe_passwd = 'password'
    assert isinstance(safe_passwd, str)
    assert isinstance(safe_passwd, str)

    # Test unsafe object
    class AnsibleUnsafeStr(str):
        def __init__(self, *args, **kwargs):
            super(AnsibleUnsafeStr, self).__init__(*args, **kwargs)
            self.__UNSAFE__ = True
    unsafe_passwd = AnsibleUnsafeStr('password')
    assert not isinstance(unsafe_passwd, str)
    assert isinstance(unsafe_passwd.__UNSAFE__, bool)
    assert not isinstance(unsafe_passwd, str)

    # Test vault object

# Generated at 2022-06-12 23:12:59.802699
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder(sort_keys=True, indent=2)
    # Test class AnsibleUnsafe
    assert json.loads(encoder.encode({'foo': 'bar'})) == \
        {'foo': 'bar'}
    # Test class AnsibleVaultEncryptedUnicode

# Generated at 2022-06-12 23:13:26.531074
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    import datetime
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.vault import VaultLib

    # Test passwords are encrypted with vault_id=None (a random password is generated)
    vault = VaultLib([])
    encrypted_password = vault.encrypt('testpassword')

# Generated at 2022-06-12 23:13:36.053433
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type

    # test type: bool
    test_bool = AnsibleJSONEncoder.default(None, True)
    assert test_bool == True

    # test type: dict (key: str, value: bool)
    test_dict = AnsibleJSONEncoder.default(None, {'key': True})
    assert test_dict == {'key': True}

    # test type: list
    test_list = AnsibleJSONEncoder.default(None, [1, 2, 3])
    assert test_list == [1, 2, 3]

    # test type: str
    test_str = AnsibleJSONEncoder.default(None, 'str')
    assert test_str == 'str'

    # test type: binary_type
    test_binary_type = AnsibleJSONEnc

# Generated at 2022-06-12 23:13:44.875446
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.parsing.convert_bool import boolean

    encoder = AnsibleJSONEncoder()
    assert encoder.default(dict(foo=True)) == dict(foo=True)
    assert encoder.default(dict(foo=False)) == dict(foo=False)
    assert encoder.default(dict(foo=boolean(True))) == dict(foo=True)
    assert encoder.default(dict(foo=boolean(False))) == dict(foo=False)
    assert encoder.default(dict(foo=boolean('true'))) == dict(foo=True)

# Generated at 2022-06-12 23:13:55.417135
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from collections import OrderedDict
    encoder = AnsibleJSONEncoder()


# Generated at 2022-06-12 23:14:03.424944
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe, AnsibleVaultEncryptedUnicode

    # Test AnsibleUnsafe
    # Test for objects with __unsafe__: default(object)
    obj = AnsibleUnsafe(u'password')
    assert isinstance(obj, unicode)
    encoder = AnsibleJSONEncoder()
    result = encoder.default(obj)
    assert isinstance(result, dict)
    assert result == {'__ansible_unsafe': "password"}

    # Test AnsibleVaultEncryptedUnicode
    # Test for objects with __encrypted__: default(object)

# Generated at 2022-06-12 23:14:12.102060
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret

    ansible_json_encoder = AnsibleJSONEncoder()

    # test for vault secret
    assert ansible_json_encoder.default(VaultSecret('vault_secret')) == {'__ansible_vault': 'vault_secret'}

    # test for sequence
    assert ansible_json_encoder.default([]) == []

    # test for mapping
    assert ansible_json_encoder.default({}) == {}

    # test for date object
    assert ansible_json_encoder.default(
        datetime.date(day=15, month=10, year=2018)) == '2018-10-15'


# Generated at 2022-06-12 23:14:21.924123
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys

    # pylint: disable=unused-argument,protected-access
    class test_case():
        def __init__(self, val):
            self._val = val

        def __UNSAFE__(self):
            return True

        def __ENCRYPTED__(self):
            return True

        def __ANSIBLEDOCS__(self):
            return True

        def __ansible_module__(self):
            return True

        def __getitem__(self, item):
            return self._val

        def __getattr__(self, attr):
            return self._val

        def __repr__(self):
            return "test_case"

    test_obj = test_case("testing")

    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:32.741221
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # pylint: disable=unused-variable
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    # pylint: enable=unused-variable
    import datetime
    from ansible.module_utils.six import text_type

    # encrypt_value
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    fake_vault_text = 'test vault'
    fake_vault = VaultSecret(fake_vault_text)
    vault_encrypted = VaultLib({}).encrypt(fake_vault_text)
    vault_encrypted.update_payload(fake_vault_text)
    fake_vault_encrypted = VaultSecret(vault_encrypted['vault_string'])


# Generated at 2022-06-12 23:14:40.261928
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = {
        "date_obj": datetime.date(2019, 5, 9),
        "datetime_obj": datetime.datetime(2019, 5, 9, 2, 0, 11),
        "dict_obj": {
            "key": "value"
        },
        "list_obj": [1, 2, 3],
        "int_type": 1,
    }
    encoder = AnsibleJSONEncoder()
    assert encoder.default(o) == {
        "date_obj": "2019-05-09",
        "datetime_obj": "2019-05-09T02:00:11",
        "dict_obj": {
            "key": "value"
        },
        "list_obj": [1, 2, 3],
        "int_type": 1,
    }

#

# Generated at 2022-06-12 23:14:50.329512
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ae = AnsibleJSONEncoder()
    assert ae.default('abc') == "abc"
    assert ae.default(['abc', 1, None, True, False]) == ["abc", 1, None, True, False]
    assert ae.default({'a': 'abc', 'b': 123}) == {'a': 'abc', 'b': 123}
    assert ae.default({'a': 'abc', 'b': 123, 'c': None}) == {'a': 'abc', 'b': 123, 'c': None}
    assert ae.default({'a': 'abc', 'b': 123, 'c': {}}) == {'a': 'abc', 'b': 123, 'c': {}}
    # datetime

# Generated at 2022-06-12 23:15:33.329463
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_unsafe = """Plaintext representation of an AnsibleUnsafe string"""

    class Vault(str):
        __ENCRYPTED__ = True

    class Unsafe(str):
        __UNSAFE__ = True

    ansible_vault = Vault(ansible_unsafe)
    ansible_unsafe = Unsafe(ansible_unsafe)

    # Tests for vault
    # Check for a non-vault object
    assert '__ansible_vault' not in AnsibleJSONEncoder().default(ansible_unsafe)

    # Check for a vault object, with vault_to_text = False
    assert '__ansible_vault' in AnsibleJSONEncoder().default(ansible_vault)

    # Check for a vault object, with vault_to_text = True

# Generated at 2022-06-12 23:15:43.106932
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode
    from ansible.parsing.vault import VaultLib

    ansible_unsafe_object = to_unicode(b"test")
    ansible_unsafe_object.__UNSAFE__ = True

    ansible_vault_object = VaultLib(b"somekey")
    ansible_vault_object.__ENCRYPTED__ = True

    encoder = AnsibleJSONEncoder()

    assert encoder.default(ansible_unsafe_object) == {'__ansible_unsafe': b"test"}
    assert encoder.default(ansible_vault_object) == {'__ansible_vault': to_bytes(ansible_vault_object._ciphertext)}

# Generated at 2022-06-12 23:15:51.901544
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Setup
    encoder = AnsibleJSONEncoder()

    # Test
    value = encoder.default(b'hello world')
    assert value == 'hello world'

    value = encoder.default(123)
    assert value == 123

    value = encoder.default((1, 2, 3))
    assert value == (1, 2, 3)

    value = encoder.default([1, 2, 3])
    assert value == [1, 2, 3]

    value = encoder.default({'key': 'value'})
    assert value == {'key': 'value'}

    class Mock(object):
        def __init__(self, value):
            self.value = value

    value = encoder.default(Mock('value'))
    assert value == 'value'


# Generated at 2022-06-12 23:16:01.261126
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.text import AnsibleUnsafe
    from ansible.module_utils.common.text.formatters import vault
    from ansible.module_utils.common.collections import ImmutableDict

    e = AnsibleJSONEncoder()

    assert e.default(AnsibleUnsafe('test')) == {'__ansible_unsafe': 'test'}
    assert e.default(vault.VaultLib('test')) == {'__ansible_vault': 'test'}
    assert e.default(ImmutableDict(foo='bar')) == {'foo': 'bar'}

    class Foo(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b


# Generated at 2022-06-12 23:16:09.785967
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode
    from ansible.parsing.vault import VaultLib, VaultSecret

    encoder = AnsibleJSONEncoder()

    # check date to datetime conversion
    date = datetime.date(2016, 9, 12)
    assert encoder.default(date) == '2016-09-12'

    # check unsafe to dict conversion
    unsafe = to_unicode(b'TestUnsafe')
    unsafe.__UNSAFE__ = True
    assert encoder.default(unsafe) == {'__ansible_unsafe': 'TestUnsafe'}

    # check unsafe as string to dict conversion
    unsafe = to_bytes(u'TestUnsafe')
    unsafe.__UNSAFE__ = True
    assert encoder.default

# Generated at 2022-06-12 23:16:11.938233
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    date_string = j.default(datetime.datetime.fromtimestamp(1451606400))
    assert date_string == "2016-01-01T00:00:00"



# Generated at 2022-06-12 23:16:16.074178
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe(str):
        __UNSAFE__ = True

    class AnsibleVault(AnsibleUnsafe):
        __ENCRYPTED__ = True

    answer = '42'
    unsafe = AnsibleUnsafe(answer)
    vault = AnsibleVault(answer)

    assert AnsibleJSONEncoder().default(unsafe) == answer
    assert AnsibleJSONEncoder().default(vault) == {'__ansible_vault': answer}

# Generated at 2022-06-12 23:16:21.471806
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    encoder = AnsibleJSONEncoder()

    # Test `vault` object
    vault_obj = {'__ENCRYPTED__': True, '_ciphertext': to_text('vault text')}
    # Test if vault object is converted to dict using __ansible_vault
    assert encoder.default(vault_obj) == dict(__ansible_vault=u'vault text')
    # Test if vault object is converted to text when vault_to_text is True
    vault_to_text_encoder = AnsibleJSONEncoder(vault_to_text=True)
    assert vault_to_text_encoder.default(vault_obj) == u'vault text'

    # Test `unsafe` object
    unsafe_obj = {'__UNSAFE__': True}
    assert enc

# Generated at 2022-06-12 23:16:30.373953
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''test default method of AnsibleJSONEncoder'''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.vault import VaultLib
    module = AnsibleModule(argument_spec={})
    encoder = AnsibleJSONEncoder()

    assert encoder.default(module) == '__ansible_module_generated_v2.9.0.dev0'
    assert encoder.default({'a': 'test'}) == {'a': 'test'}
    assert encoder.default(['a', 'test']) == ['a', 'test']

# Generated at 2022-06-12 23:16:34.804722
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default({"a": 1}) == {"a": 1}
    assert AnsibleJSONEncoder().default([1, 2]) == [1, 2]
    test_instance = AnsibleJSONEncoder()
    assert test_instance.default({"a": 1}) == {"a": 1}
    assert test_instance.default([1, 2]) == [1, 2]

