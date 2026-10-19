

# Generated at 2022-06-12 23:06:38.006991
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert json_encoder.default(Mapping()) == {}
    assert json_encoder.default(datetime.date(2016, 10, 1)) == '2016-10-01'
    assert json_encoder.default(datetime.datetime(2016, 10, 1, 12, 00, 00)) == '2016-10-01T12:00:00'



# Generated at 2022-06-12 23:06:47.146006
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault

    test_value_unsafe_string = "test_value_unsafe_string"
    test_value_safe_string = "\n\t1234567890\n\t~!@#$%^&*()-+{}[]|\\:;'\",.<>?/\n\n\n"
    test_value_datetime = datetime.datetime.now()
    test_value_date = datetime.date.today()
    test_value_unsafe_list = [test_value_unsafe_string, test_value_safe_string, 1, test_value_datetime]
    test_value_safe_list = [test_value_safe_string, 2, test_value_date]

# Generated at 2022-06-12 23:06:58.056901
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert '__ansible_unsafe' not in AnsibleJSONEncoder().default(u'a')
    assert '__ansible_vault' not in AnsibleJSONEncoder().default(u'a')
    assert '__ansible_unsafe' in AnsibleJSONEncoder().default({'value': u'a', '__UNSAFE__': True})
    assert '__ansible_vault' in AnsibleJSONEncoder().default(u'a', __ENCRYPTED__=True)
    assert '__ansible_unsafe' not in AnsibleJSONEncoder(vault_to_text=True).default(u'a', __ENCRYPTED__=True)

# Generated at 2022-06-12 23:07:05.006281
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
            'text': dict(type='str', no_log=True),
            'vault_password_file': dict(type='str', no_log=True),
            'json_encoder_kwargs': dict(type='dict', default=dict()),
            'json_vault_to_text': dict(type='bool', default=False),
        },
        add_file_common_args=True
    )

    # test object
    vault = VaultLib(get_vault_password_file=module.load_file_common_argument_spec)

# Generated at 2022-06-12 23:07:10.513064
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    isinstance(encoder, json.JSONEncoder)
    assert encoder.default("") == ""
    assert encoder.default("test") == "test"
    assert encoder.default({"key": "value"}) == {"key": "value"}
    assert encoder.default(["key", "value", "other"]) == ["key", "value", "other"]

# Generated at 2022-06-12 23:07:18.993237
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    my_vault = VaultLib([])
    my_encrypted_text = my_vault.encrypt(b"supersekret")
    class Test:
        item = my_encrypted_text
        def __init__(self, **kwargs):
            for key in kwargs:
                setattr(self, key, kwargs[key])

    e = AnsibleJSONEncoder(sort_keys=True)
    # Test vault encryption

# Generated at 2022-06-12 23:07:27.590922
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_value_dict = {'hostvars': {'host1': {'ansible_inventory': {'hostvars': {'host1': {'key': 'value'}}}}}}
    test_encoder = AnsibleJSONEncoder()
    test_json = json.dumps(test_value_dict, cls=AnsibleJSONEncoder)
    test_value_dict_encoded = json.loads(test_json)
    assert test_value_dict_encoded == test_value_dict


# Generated at 2022-06-12 23:07:36.333516
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing import vault

    myencoder = AnsibleJSONEncoder()

    # vault object
    to_encrypt = "mypassword"
    o = vault.VaultLib([u"test_password"]).encrypt(to_encrypt)

# Generated at 2022-06-12 23:07:41.486840
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # Date
    assert encoder.default(datetime.date.today()) == datetime.date.today().isoformat()
    assert encoder.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()

    # Vault
    from ansible.parsing.vault import VaultSecret
    assert encoder.default(VaultSecret('VaultSecret')) == {'__ansible_vault': 'VaultSecret'}

    # Unsafe
    from ansible.module_utils.basic import AnsibleUnsafe
    assert encoder.default(AnsibleUnsafe('AnsibleUnsafe')) == {'__ansible_unsafe': 'AnsibleUnsafe'}

    # Mapping

# Generated at 2022-06-12 23:07:52.855686
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault

    encoder = AnsibleJSONEncoder()

    # Test dictionary
    mydict = { 'A': 'B', 'C': 'D' }
    assert encoder.default(mydict) == mydict

    # Test AnsibleUnsafe Object
    myunsafe = vault.AnsibleUnsafeText("UNSAFE")
    assert encoder.default(myunsafe) == {'__ansible_unsafe': u'UNSAFE'}

    # Test AnsibleVault Object
    myvault = vault.VaultLib("UNSAFE")
    # Test vault_to_text
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    assert encoder.default(myvault) == 'UNSAFE'
    # Test default behaviour
   

# Generated at 2022-06-12 23:08:02.704103
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    o = {'host': 'www.example.com',
         'username': 'user',
         'password': 'password',
         'port': 22,
         'ssh_key': 'string-ssh-key',
         'datetime': datetime.datetime.utcnow()
        }
    j = AnsibleJSONEncoder()
    value = j.default(o)
    assert isinstance(value, dict)
    assert value == o

# Generated at 2022-06-12 23:08:11.673347
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    e = AnsibleJSONEncoder()
    o = {'foo': 'bar'}

    # Test default with a mapping
    v = e.default(o)
    assert v == {'foo': 'bar'}

    # Test default with a sequence
    o = ['a', 'b', 'c']
    v = e.default(o)
    assert v == ['a', 'b', 'c']

    # Test default with a datetime
    o = datetime.datetime(2017, 4, 14, 0, 0, 0)
    v = e.default(o)
    assert v == '2017-04-14T00:00:00'



# Generated at 2022-06-12 23:08:22.177121
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.collections import ImmutableDict
    from io import BytesIO
    from ansible.constants import DEFAULT_VAULT_ID_MATCH

    key = to_bytes('ansible')
    vault = VaultLib([key])

    data = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default(vault.encrypt(to_bytes('This is an unsafe string.')))

# Generated at 2022-06-12 23:08:31.425120
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('foo') == 'foo'
    assert AnsibleJSONEncoder().default([1,2,3]) == [1,2,3]
    assert AnsibleJSONEncoder().default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder(sort_keys=True).default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder(sort_keys=True).default(dict(b=2, a=1)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder().default(dict(a=1, b=2, c=3, d=4)) == dict(a=1, b=2, c=3, d=4)
   

# Generated at 2022-06-12 23:08:38.292669
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean
    t = datetime.date.today()
    d = {'aaa': 111,
         'bbb': 'xxx',
         'ccc': boolean(True)}
    d.update(ccc=Mapping(ddd='yyy'))
    d.update(ccc=Mapping(eee=222))
    d.update(ccc=Mapping(fff=boolean(False)))
    d.update(ccc=Mapping(ggg=t))
    a = AnsibleJSONEncoder()
    r = a.default(d)
    assert r == d

# Generated at 2022-06-12 23:08:47.457776
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_obj = AnsibleJSONEncoder()
    assert json_obj.default(None) == 'null'
    assert json_obj.default(1) == 1
    assert json_obj.default("hello") == '"hello"'
    assert json_obj.default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert json_obj.default(dict(a=1, b=2, __ansible_vault='hello')) == dict(a=1, b=2, __ansible_vault='hello')
    assert json_obj.default("hello") == '"hello"'
    assert json_obj.default("hello") == '"hello"'



# Generated at 2022-06-12 23:08:53.162053
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode({'k': 'v'}) == '{"k": "v"}'
    assert AnsibleJSONEncoder().encode({'k': 'v', 'k2': 'v2'}) == '{"k": "v", "k2": "v2"}'
    assert AnsibleJSONEncoder().encode([0, 1, 2]) == '[0, 1, 2]'


# Generated at 2022-06-12 23:08:59.746965
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-12 23:09:10.524506
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.dumps({"s_class_obj": set()}, cls=AnsibleJSONEncoder) == '{"s_class_obj": []}'
    assert json.dumps(set(), cls=AnsibleJSONEncoder) == '[]'
    assert json.dumps({"f_class_obj": frozenset()}, cls=AnsibleJSONEncoder) == '{"f_class_obj": []}'
    assert json.dumps(frozenset(), cls=AnsibleJSONEncoder) == '[]'
    assert json.dumps({"v_class_obj": {"__ansible_vault": "vault_value"}}, cls=AnsibleJSONEncoder) == '{"v_class_obj": {"__ansible_vault": "vault_value"}}'
   

# Generated at 2022-06-12 23:09:20.683035
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Unit test for AnsibleJSONEncoder.default method to test if the correct
    # value is returned for different input values.
    test_ansible_encoder = AnsibleJSONEncoder()
    test_dict = {'test': 'test'}
    test_dict['test1'] = {'test1': 'test1'}
    test_list = [1, 2, 3]
    test_list.append('test')
    test_list.append({'test': 'test'})
    test_list.append(test_dict)
    test_int = 10

    # Testing for different datetime objects
    test_date = datetime.date(2015, 5, 4)
    test_datetime = datetime.datetime(2016, 6, 4, 10, 20)

    # Testing for a Mapping object
    test_m

# Generated at 2022-06-12 23:09:34.864585
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword
    import base64


# Generated at 2022-06-12 23:09:42.334251
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type, text_type

    assert AnsibleJSONEncoder().default(dict(a=1, b=2)) == {'a': 1, 'b': 2}
    assert AnsibleJSONEncoder().default(binary_type('foo')) == 'foo'
    assert AnsibleJSONEncoder().default(text_type('foo')) == 'foo'
    assert AnsibleJSONEncoder().default(True) is True
    assert AnsibleJSONEncoder().default(None) is None


# Generated at 2022-06-12 23:09:50.641913
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_encoder = AnsibleJSONEncoder()
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('secret')
    test_cases = [
        ('test', 'test'),
        ('test', ansible_encoder.default('test')),
        ({'key': 'test'}, ansible_encoder.default({'key': 'test'})),
        ({'key': 'test'}, ansible_encoder.default({'key': ansible_encoder.default('test')})),
        ({'key': 'test'}, ansible_encoder.default({'key': vault.encrypt('test')})),
        ({'key': ['test']}, ansible_encoder.default({'key': ['test'], 'vault': vault})),
    ]

# Generated at 2022-06-12 23:09:52.666354
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    sample_data = {'test01': 'test01'}
    assert encoder.default(sample_data) == sample_data


# Generated at 2022-06-12 23:09:54.166331
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = json.dumps('value', cls=AnsibleJSONEncoder)
    assert o == '"value"'

# Generated at 2022-06-12 23:10:02.774517
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class MyClass(object):
        """Some random class for testing."""
        def __init__(self, *args, **kwargs):
            self.kwargs = kwargs

    a = MyClass(foo=1, bar=2)
    b = datetime.date(2017, 4, 11)
    c = datetime.datetime(2017, 4, 11, 19, 59, 0)
    d = {'a': 1, 'b': 2}

    assert AnsibleJSONEncoder(separators=('~', '!'), sort_keys=True).encode({'a': a}) == '{"a": {"kwargs": {"bar": 2, "foo": 1}}}'

# Generated at 2022-06-12 23:10:12.365689
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib, VaultSecret

    vault_with_decrypted = VaultLib(VaultSecret('vault-password', VaultSecret.MD5))
    vault_with_decrypted.unlock('vault-password')
    unsafe_password = vault_with_decrypted.encrypt('vault-password')


# Generated at 2022-06-12 23:10:23.193626
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Create ansiblejsonencoder object
    ansiblejsonencoder = AnsibleJSONEncoder()
    # Create ansibleunsafe object
    ansibleunsafe = type('AnsibleUnsafe', (str, ), dict(__UNSAFE__=True, __ENCRYPTED__=False))
    # Create ansiblevault object
    ansiblevault = type('AnsibleVault', (ansibleunsafe, ), dict(__UNSAFE__=True, __ENCRYPTED__=True))
    ansiblevault._ciphertext = 'ansiblevault'
    hostvar = type('hostvar', (dict, ), dict())

    # Test with unsafe string, should return a dict with __ansible_unsafe in it's key

# Generated at 2022-06-12 23:10:31.328365
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = 1
    o_encoded = AnsibleJSONEncoder().default(o)
    assert o_encoded == o
    o = 1.0
    o_encoded = AnsibleJSONEncoder().default(o)
    assert o_encoded == o
    o = 'str'
    o_encoded = AnsibleJSONEncoder().default(o)
    assert o_encoded == o
    o = u'unicøde'
    o_encoded = AnsibleJSONEncoder().default(o)
    assert o_encoded == o
    o = False
    o_encoded = AnsibleJSONEncoder().default(o)
    assert o_encoded == o
    o = [1, 'str', {'k': 'v'}]
    o_encoded = AnsibleJSONEncoder().default(o)

# Generated at 2022-06-12 23:10:40.199426
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:10:56.151498
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import unittest
    import datetime
    import collections

    class TestCase(unittest.TestCase):
        def test_default(self):
            # note: it will change the result of json.dump
            # if new value is added, it may break the test in other place

            # simple types
            self.assertEqual('null', json.dumps(None, cls=AnsibleJSONEncoder))
            self.assertEqual('1', json.dumps(1, cls=AnsibleJSONEncoder))
            self.assertEqual('1.1', json.dumps(1.1, cls=AnsibleJSONEncoder))
            self.assertEqual('true', json.dumps(True, cls=AnsibleJSONEncoder))

# Generated at 2022-06-12 23:11:04.202023
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib

    text_obj = AnsibleJSONEncoder(sort_keys=True).default('test string')
    assert text_obj == 'test string'

    unsafe_obj = AnsibleJSONEncoder(sort_keys=True).default(dict(__ansible_unsafe='test string'))
    assert unsafe_obj == {'__ansible_unsafe': 'test string'}

    vault_obj = VaultLib(b'$ANSIBLE_VAULT')

# Generated at 2022-06-12 23:11:09.057566
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = {'a':1, 'b':2}
    json_data = '{"a": 1, "b": 2}'
    assert json.loads(json_data) == data

    ansjson_data = AnsibleJSONEncoder().encode(data)
    assert ansjson_data == json_data



# Generated at 2022-06-12 23:11:16.282166
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import pytest
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import binary_type, text_type

    encoder = AnsibleJSONEncoder()

    assert encoder.default(None) is None
    assert encoder.default("") == ""
    assert encoder.default("test") == "test"
    assert encoder.default(42) == 42
    assert encoder.default(3.14) == 3.14
    assert encoder.default(42.0) == 42.0
    assert encoder.default("{}") == "{}"
    assert encoder.default("{") == "{"
    assert encoder.default("\\") == "\\"
    assert encoder.default("[]") == "[]"


# Generated at 2022-06-12 23:11:18.624952
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    value = AnsibleJSONEncoder(sort_keys=True).default('A')
    assert value == 'A'


# Generated at 2022-06-12 23:11:29.220607
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.constants import ANSIBLE_VAULT_IDENTIFIER
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    v = VaultLib([])
    secret = VaultSecret('foo')
    kwargs = dict(password=secret, ident=ANSIBLE_VAULT_IDENTIFIER)
    v.encrypt_value('bar', **kwargs)
    v.finalize()

# Generated at 2022-06-12 23:11:38.629159
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Foo:
        def __init__(self):
            self.a = 1
            self.b = 2

    class Bar(str):
        __ENCRYPTED__ = False
        __UNSAFE__ = True

    assert json.loads(json.dumps(['a', Foo(), ['b', 'c'], {'d': 'e'}, 1, 2], cls=AnsibleJSONEncoder, sort_keys=True, indent=4)) == [
        'a',
        {'a': 1, 'b': 2},
        ['b', 'c'],
        {'d': 'e'},
        1,
        2
    ]

# Generated at 2022-06-12 23:11:46.467530
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.parsing.vault import VaultLib
    # Dict
    assert AnsibleJSONEncoder().default({"foo": "bar"}) == {"foo": "bar"}
    # AnsibleUnsafe
    assert AnsibleJSONEncoder().default(AnsibleUnsafe("foo")) == {'__ansible_unsafe': u'foo'}
    # AnsibleUnsafe with no_log
    assert AnsibleJSONEncoder().default(AnsibleUnsafe("foo", no_log=True)) == {'__ansible_unsafe': u'foo'}
    # AnsibleUnsafe with no_log and __ENCRYPTED__

# Generated at 2022-06-12 23:11:50.737383
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = {
        'a': ['a', 'b', 'c'],
        'b': 'b',
        'c': {
            'd': 'e',
        },
    }

    print(json.dumps(o, cls=AnsibleJSONEncoder))


if __name__ == "__main__":
    test_AnsibleJSONEncoder_default()

# Generated at 2022-06-12 23:12:00.240901
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_instance = AnsibleJSONEncoder()
    assert test_instance.default("info") == "info"
    assert test_instance.default(u"info") == "info"
    assert test_instance.default(5) == 5
    assert test_instance.default(5.6) == 5.6
    assert test_instance.default(True) == True
    assert test_instance.default({"info": "test"}) == {"info": "test"}
    assert test_instance.default(("info", "test")) == ["info", "test"]
    assert test_instance.default(datetime.datetime(2014, 4, 9, 16, 44, 35)) == "2014-04-09T16:44:35"

# Generated at 2022-06-12 23:12:24.692280
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # Test 1: Test default class
    class AnsibleTestDefault(object):
        def __init__(self, value):
            self._value = value

        def __repr__(self):
            return repr(self._value)

    test1 = AnsibleTestDefault(1)
    assert encoder.default(test1) == 1

    # Test 2: Test class with __ENCRYPTED__ flag
    class AnsibleTestENC(object):
        __ENCRYPTED__ = True

        def __init__(self, value):
            self._value = value

        def __repr__(self):
            return repr(self._value)

    test2 = AnsibleTestENC(2)

# Generated at 2022-06-12 23:12:35.891227
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.unsafe_proxy import AnsibleUnsafe

    def test(obj, expected, expected_type):
        res = AnsibleJSONEncoder().default(obj)
        assert res == expected, '{} != {}'.format(res, expected)
        assert type(res) is expected_type, '{} != {}'.format(type(res), expected_type)

    def test_vault(obj, expected):
        # test optional vault_to_text
        res = AnsibleJSONEncoder(vault_to_text=True).default(obj)
        assert res == expected, '{} != {}'.format(res, expected)
        assert type(res) is unicode, '{} != {}'.format(type(res), unicode)

       

# Generated at 2022-06-12 23:12:38.583452
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_j_e = AnsibleJSONEncoder()
    assert ansible_j_e.default(object()) == json.JSONEncoder.default(ansible_j_e, {})

# Generated at 2022-06-12 23:12:46.385482
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    import ansible.module_utils.common._collections_compat as collections_compat
    from datetime import date, datetime
    # This is an example of an encrypted vault object

# Generated at 2022-06-12 23:12:56.478985
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys

    if sys.version_info[0] >= 3:
        long = int

    import datetime

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-12 23:13:03.373605
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe(unicode):
        def __new__(cls, val):
            return unicode.__new__(cls, val)

    # Redefine __init__ method to make happy AnsibleJSONEncoder
    AnsibleUnsafe.__init__ = lambda self, val='': None

    # Set attribute for AnsibleJSONEncoder.default method
    AnsibleUnsafe.__UNSAFE__ = True
    AnsibleUnsafe.__ENCRYPTED__ = False

    my_unsafe = AnsibleUnsafe('test')

    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(my_unsafe) == {'__ansible_unsafe': u'test'}

# Generated at 2022-06-12 23:13:08.263223
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test non-string types
    ansible_dict = AnsibleJSONEncoder().default({'test': 'test'})
    assert ansible_dict.get('test') == 'test'

    # Test string types
    ansible_str = AnsibleJSONEncoder().default("testing")
    assert ansible_str == "testing"


# Generated at 2022-06-12 23:13:15.297710
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert json.dumps({'date': datetime.date(2010, 5, 6)}, cls=AnsibleJSONEncoder) == json.dumps({'date': '2010-05-06'}, cls=AnsibleJSONEncoder)
    assert json.dumps({'datetime': datetime.datetime(2010, 5, 6, 23, 59, 59)}, cls=AnsibleJSONEncoder) == json.dumps({'datetime': '2010-05-06T23:59:59'}, cls=AnsibleJSONEncoder)


# Generated at 2022-06-12 23:13:18.512348
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # pylint: disable=missing-docstring
    import ansible.parsing.vault
    encoder = AnsibleJSONEncoder()
    assert encoder.default(ansible.parsing.vault.VaultLib('test1')) == {'__ansible_vault': 'test1'}

# Generated at 2022-06-12 23:13:29.390053
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Initialize instance of AnsibleJSONEncoder class
    aje = AnsibleJSONEncoder()

    # Case 1: Any string
    # Assertion
    assert aje.default("any string") == "any string"

    # Case 2: Vault object
    my_vault = "my_ciphertext"
    # Assertion
    assert aje.default(my_vault) == 'my_ciphertext'

    # Case 3: Mapping object
    mapping_object = {'key1': 'value1', 'key2': 'value2'}
    # Assertion
    assert aje.default(mapping_object) == {'key1': 'value1', 'key2': 'value2'}

    # Case 4: Date object
    from datetime import date
    date_object = date.today()


# Generated at 2022-06-12 23:14:09.606045
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert AnsibleJSONEncoder().default("foo".encode("utf-8")) == "foo"
    assert AnsibleJSONEncoder().default("foo".encode("utf-8")) == "foo"
    assert AnsibleJSONEncoder().default("foo".encode("ascii")) == "foo"
    assert AnsibleJSONEncoder().default(u"foo") == "foo"
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default(1.0) == 1.0


# Generated at 2022-06-12 23:14:19.865255
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    o = ansible_json_encoder.default("hello")
    assert o == 'hello'
    o = ansible_json_encoder.default({"hello":"world"})
    assert o == {"hello":"world"}
    o = ansible_json_encoder.default({"__UNSAFE__":"hello"})
    assert o == {'__ansible_unsafe': 'hello'}
    o = ansible_json_encoder.default({"__ENCRYPTED__":"hello"})
    assert o == {'__ansible_vault': 'hello'}
    o = ansible_json_encoder.default(datetime.date(2019, 12, 25))
    assert o == "2019-12-25"
    o = ansible_

# Generated at 2022-06-12 23:14:30.191256
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    # check AnsibleUnsafe
    assert json.dumps(AnsibleUnsafe('password')) == '"password"'
    assert json.dumps(AnsibleUnsafe('password'), cls=AnsibleJSONEncoder) == '{"__ansible_unsafe": "password"}'

    # check AnsibleVaultEncryptedUnicode
    vault = VaultLib([])
    vault_password = vault.encrypt(b'password')
    assert json.dumps(vault_password) == '"password"'
    assert json.dumps(vault_password, cls=AnsibleJSONEncoder) == '"password"'

# Generated at 2022-06-12 23:14:37.443465
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import string
    from ansible.parsing.vault import VaultLib

    secret1 = VaultLib.encrypt("secret1")
    secret2 = VaultLib.encrypt("secret2")
    d1 = {'a': "pippo", 'b': secret1, 'c': {'aa': "pluto"}}
    d2 = {'a': "pippo", 'c': {'aa': "pluto", 'bb': secret2}}
    d3 = {'a': "pippo", 'c': [{'aa': "pluto", 'bb': secret2}]}
    d4 = {'a': "pippo", 'c': [1,2,3], 'd': {'aa': "pluto", 'bb': secret2}}

    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:40.778303
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('hello world') == 'hello world'
    assert encoder.default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert encoder.default(u'\u1234') == u'\u1234'

# Generated at 2022-06-12 23:14:47.455934
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert getattr(AnsibleJSONEncoder().default(object()), '__ENCRYPTED__', False) is False
    assert getattr(AnsibleJSONEncoder().default(object()), '__UNSAFE__', False) is False
    assert isinstance(AnsibleJSONEncoder().default({}), dict)
    assert isinstance(AnsibleJSONEncoder().default([]), list)
    assert isinstance(AnsibleJSONEncoder().default(object()), dict)



# Generated at 2022-06-12 23:14:57.553504
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    b = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True)
    a_ = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=False)
    b_ = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)
    # vault object
    test_value = '\n-----BEGIN RSA PRIVATE KEY-----\naaa\nbbb\nccc\nddd\neee\nffa\nggg\nhhh\niii\njjj\nkkk\nlll\nmmm\n-----END RSA PRIVATE KEY-----\n'
    ansible_vault = AnsibleVaultEnc

# Generated at 2022-06-12 23:15:06.304337
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import jsonschema
    encoder = AnsibleJSONEncoder()

    # string
    assert encoder.default("string") == "string"

    # int
    assert encoder.default(2) == 2

    # float
    assert encoder.default(2.2) == 2.2

    # bool
    assert encoder.default(True) == True

    # datetime.date
    import datetime
    assert encoder.default(datetime.date(2020,12,25)) == '2020-12-25'

    # object with __ENCRYPTED__
    class AnsibleVault:
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext
            self.__ENCRYPTED__ = True

    class MyException(Exception):
        pass


# Generated at 2022-06-12 23:15:13.891536
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Tests json.JSONEncoder method default.
    :return: None
    """
    ansible_encoder = AnsibleJSONEncoder()
    json_encoder = json.JSONEncoder()
    class TestClass():
        def __init__(self):
            pass

    test_1 = datetime.datetime.now()
    test_2 = ['apple', 'banana']
    test_3 = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}
    test_4 = TestClass()
    test_5 = getattr(test_4, '__ENCRYPTED__', False) # AttributeError: type object 'AnsibleJSONEncoder' has no attribute '__ENCRYPTED__'

# Generated at 2022-06-12 23:15:21.824169
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    example_hostvars = {'example': 'ansible'}
    example_unsafe = 'UNSAFE'
    example_vault = 'VAULT'

    class ExampleHostvars(Mapping):
        def __getitem__(self, key):
            return dict(example_hostvars)[key]

        def __iter__(self):
            return iter(dict(example_hostvars))

        def __len__(self):
            return len(dict(example_hostvars))

        # Do not define __contains__ as it does not support inplace
        # https://stackoverflow.com/questions/37594546/inplace-comparison-of-json-objects-by-key

    class ExampleUnsafe():
        __UNSAFE__ = True
        def __str__(self):
            return