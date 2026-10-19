

# Generated at 2022-06-12 23:06:44.991504
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import re
    import types

    class AnsibleVault:
        __ENCRYPTED__ = True

    class AnsibleUnsafe:
        __UNSAFE__ = True

    class MyClass:
        def __init__(self, kwarg_1, kwarg_2, kwarg_3=None):
            self.kwarg_1 = kwarg_1
            self.kwarg_2 = kwarg_2
            self.kwarg_3 = kwarg_3

    encoder = AnsibleJSONEncoder()

    # change sort_keys to True for readability
    # without sort_keys, order of dict is not guaranteed
    json_str = json.dumps(list(range(3)), sort_keys=True, indent=4)

# Generated at 2022-06-12 23:06:49.435975
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps(dict(foo='bar'), cls=AnsibleJSONEncoder)) == dict(foo='bar')
    assert json.loads(json.dumps(dict(foo='bar', foo2=dict(bar='baz'), foo3=[1, 2, 3]), cls=AnsibleJSONEncoder)) == dict(foo='bar', foo2=dict(bar='baz'), foo3=[1, 2, 3])

# Generated at 2022-06-12 23:06:59.035633
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test AnsibleUnsafe Object
    ansible_unsafe_object = AnsibleUnsafeText("This is a test")
    ansible_json = AnsibleJSONEncoder()
    unsafe_to_json = ansible_json.default(ansible_unsafe_object)
    assert unsafe_to_json == {"__ansible_unsafe": "This is a test"}

    # Test AnsibleVault Object
    ansible_vault_object = AnsibleVaultEncryptedUnicode("ThisisAEncryptedString")
    vault_to_json = ansible_json.default(ansible_vault_object)
    assert vault_to_json == {"__ansible_vault": "ThisisAEncryptedString"}


# Generated at 2022-06-12 23:07:05.600232
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    myEncoder = AnsibleJSONEncoder()
    result = myEncoder.default(Mapping())
    assert result == dict()

    result = myEncoder.default(datetime.datetime(2012, 11, 15, 23, 42, 38))
    assert result == u'2012-11-15T23:42:38'

    class TestDefault(object):
        __UNSAFE__ = False
        __ENCRYPTED__ = False
        def __init__(self, a):
            self._a = a

    a = TestDefault(10)
    result = myEncoder.default(a)
    assert result == a

    class TestUnsafe(str):
        __UNSAFE__ = True
        __ENCRYPTED__ = False

    b = TestUnsafe(10)
    result = myEncoder.default

# Generated at 2022-06-12 23:07:15.660917
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    vault = VaultLib([])
    ansible_unsafe = AnsibleUnsafeText(b'SECRET', b'Test secret')
    ansible_vault = vault.encrypt(ansible_unsafe)
    test_dict = {'ansible_vault': ansible_vault, 'ansible_unsafe': ansible_unsafe}
    ansible_json_encoder = AnsibleJSONEncoder()
    encoded = ansible_json_encoder.encode(test_dict)

# Generated at 2022-06-12 23:07:25.733553
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    import ansible.module_utils.basic

# Generated at 2022-06-12 23:07:35.305318
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.parsing.convert_bool import boolean

    assert json.dumps(
        {'a': 'b'}, cls=AnsibleJSONEncoder, sort_keys=True
    ) == json.dumps(
        {'a': 'b'}, sort_keys=True
    )

    assert json.dumps(
        {
            'a': AnsibleUnsafe('b')
        },
        cls=AnsibleJSONEncoder,
        sort_keys=True
    ) == json.dumps(
        {
            'a': 'b'
        },
        sort_keys=True
    )


# Generated at 2022-06-12 23:07:41.263696
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test with some simple cases
    aje = AnsibleJSONEncoder()
    assert aje.default(datetime.datetime(2020, 1, 1)) == '2020-01-01T00:00:00'
    assert aje.default(datetime.date(2020, 1, 1)) == '2020-01-01'
    assert aje.default({'foo': 'bar'}) == {'foo': 'bar'}

    # test with dict
    ansible_vault = {'__ansible_vault': '0123456789'}
    ansible_unsafe = {'__ansible_unsafe': '0123456789'}
    aje = AnsibleJSONEncoder(object_pairs_hook=lambda pairs: dict(pairs))

# Generated at 2022-06-12 23:07:52.660496
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test for class VaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    vault = VaultLib([(VaultSecret('ansible'),)])

    # following is a safe example which is encrypted by default
    from ansible.parsing.vault import VaultEncryptedUnicode
    encrypted_password = vault.encrypt('MyPassword123')
    print(json.dumps(encrypted_password, cls=AnsibleJSONEncoder, indent=4, sort_keys=True))
    # output:
    # {
    #     "__ansible_vault": "AQAATU5zZWx2Q0xpcDQ5YjBoZjg0Z0hobDFzdG5KWkVp

# Generated at 2022-06-12 23:08:02.326103
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib

    example_date = datetime.date(year=2018, month=1, day=1)
    example_datetime = datetime.datetime(year=2018, month=1, day=1, hour=0, minute=0, second=0)
    example_dict = dict(sample_dict=dict(field1='value1', field2='value2'))
    example_ansible_dict = ImmutableDict(sample_dict=ImmutableDict([('field1', 'value1'), ('field2', 'value2')]))

# Generated at 2022-06-12 23:08:08.748865
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unit_test_json = AnsibleJSONEncoder(ensure_ascii=False).encode({'data': ['test', 'ascii']})
    assert unit_test_json == '{"data": ["test", "ascii"]}', 'AnsibleJSONEncoder does not support unicode'

# Generated at 2022-06-12 23:08:19.279616
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test that the default method of the AnsibleJSONEncoder works as expected
    '''
    encoder = AnsibleJSONEncoder()
    simple_data = ['foo', True, False, None, {'a': 'b'}]
    for var in simple_data:
        assert encoder.default(var) == var

    # vault object
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-12 23:08:27.323509
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Mapping

    unsafe = AnsibleJSONEncoder.default(AnsibleUnsafe('this is a test'))
    assert unsafe == {'__ansible_unsafe': 'this is a test'}

    # vault object
    vault = AnsibleJSONEncoder.default(VaultLib('this is a test'))
    assert vault['__ansible_vault'] == 'this is a test'

    # hostvars and other objects
    hostvars = AnsibleJSONEncoder.default(Mapping({'key': 'value'}))
    assert hostvars == {'key': 'value'}

    # date object
    date = AnsibleJSONEncoder.default(datetime.date.today())


# Generated at 2022-06-12 23:08:36.506636
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test __ENCRYPTED__
    assert encoder.default(u'1') == u'1'
    assert encoder.default(u'1'.encode('UTF-8').decode('UTF-8')) == u'1'
    assert encoder.default(u'1'.encode('UTF-8')) == u'1'
    obj = u'1'.encode('UTF-8')
    obj.__ENCRYPTED__ = True
    assert encoder.default(obj) == {'__ansible_vault': obj.decode('UTF-8')}

    # test __UNSAFE__
    assert encoder.default(u'1') == u'1'

# Generated at 2022-06-12 23:08:46.674435
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    encoder = AnsibleJSONEncoder()
    assert json.dumps({"test": "test"}, cls=encoder) == '{"test": "test"}'

    # Encoding of datetime
    dt = datetime.datetime.now()
    assert json.dumps(dt, cls=encoder) == '"%s"' % dt.isoformat()

    # Encoding of dict
    dict_data = dict(test=dict(a=1, b=2, c=3))
    assert json.dumps(dict_data, cls=encoder) == '{"test": {"a": 1, "b": 2, "c": 3}}'

    # Encoding of vault_dict


# Generated at 2022-06-12 23:08:56.807517
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert(encoder.default(datetime.datetime(2018, 7, 8, 13, 11, 38, 474928)) == "2018-07-08T13:11:38.474928")
    assert(encoder.default(datetime.date(2018, 7, 8)) == "2018-07-08")

    assert(encoder.default({"foo": "bar", "baz": "qux"}) == {"foo": "bar", "baz": "qux"})
    assert(encoder.default(["quux", "corge", "grault"]) == ["quux", "corge", "grault"])
    assert(encoder.default(u"مرحبا") == u"مرحبا")

    # TODO: test vault

# Generated at 2022-06-12 23:09:02.719118
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder().default(
        {'test': 'hostvars'}
    )
    assert result == {u'test': u'hostvars'}, 'AnsibleJSONEncoder method default failed'
    result = AnsibleJSONEncoder().default(
        datetime.datetime(2018, 9, 19, 22, 30, 30, 0)
    )
    assert result == u'2018-09-19T22:30:30', 'AnsibleJSONEncoder method default failed'


# Generated at 2022-06-12 23:09:13.811863
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.parsing.vault import VaultLib
    import datetime
    # test vault obj
    o1 = VaultLib(path_segment=['MyTest'], cipher='aes256-gcm', salt_size=8,
                  hmac_sha256=True, iterations=1000, keysize=32)
    o1._ciphertext = '08'
    o1.__ENCRYPTED__ = True
    # test vault obj to text
    o2 = VaultLib(path_segment=['MyTest'], cipher='aes256-gcm', salt_size=8,
                  hmac_sha256=True, iterations=1000, keysize=32)
    o2._ciphertext = '08'
    o2

# Generated at 2022-06-12 23:09:23.059411
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    o = "test"
    test_value = AnsibleJSONEncoder().default(o)
    assert isinstance(test_value, (type)) == True
    assert test_value == "test"

    o = datetime.datetime(2019, 12, 10, 20, 52)
    test_value = AnsibleJSONEncoder().default(o)
    assert test_value == '2019-12-10T20:52:00'

    o = datetime.date(2019, 12, 10)
    test_value = AnsibleJSONEncoder().default(o)
    assert test_value == '2019-12-10'

    o = {"A": 1, "B": 2}
    test_value = AnsibleJSONEncoder().default(o)
    assert isinstance(test_value, dict) == True

    o = AnsibleUn

# Generated at 2022-06-12 23:09:32.678037
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    import datetime

    # Encoding of `VaultLib`
    vault_lib = VaultLib(VaultSecret('0123456789abcdef'))
    vault_lib.dump('foobar')
    print(json.dumps(vault_lib, cls=AnsibleJSONEncoder))
    # Output: '{"__ansible_vault": "AQICaS1KYXZhc2JpZGdlCxIET2JqZWN0MgoAAAAFBQAAABwAAAADaXNlY3JldAoAAAAFBQAAAC0AAAAFZm9vYmFyCg=="}'

    # Encoding of `VaultSecret`
    vault

# Generated at 2022-06-12 23:09:46.970100
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    d1 = {'a': 1}
    assert encoder.default(d1) == d1
    d2_source = {'a': datetime.datetime(year=2016, month=6, day=6, hour=6, minute=6)}
    d2 = {'a': '2016-06-06T06:06:00'}
    assert encoder.default(d2_source) == d2
    d3 = {'a': 1, 'b': 2}
    encoder.indent = 4
    assert encoder.default(d3) == d3
    encoder.sort_keys = True
    assert encoder.default(d3) == d3
    encoder.indent = None
    encoder.sort_keys = False

# Generated at 2022-06-12 23:09:54.430371
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    ansible_json_encoder = AnsibleJSONEncoder()

    # Handle vault objects

    # NOTE: ALWAYS inform AWS/Tower when new items get added as they consume them downstream via a callback

# Generated at 2022-06-12 23:10:02.584817
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import UserDict
    from ansible.module_utils.six import binary_type

    plaintext = 'p@ssw0rd!'
    vault = VaultLib([])
    # Check vault encryption
    ciphertext = vault.encrypt(plaintext)
    assert AnsibleJSONEncoder().encode(ciphertext) == '{"__ansible_vault": "' + ciphertext + '"}'
    # Check default behavior
    assert AnsibleJSONEncoder().encode(UserDict()) == '{}'
    assert AnsibleJSONEncoder().encode(binary_type(plaintext, 'utf-8')) == '"' + plaintext + '"'


# Generated at 2022-06-12 23:10:12.222871
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils.urls import url_argument_spec
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import urllib
    from ansible.module_utils.six.moves.urllib.parse import parse_qs
    from ansible.module_utils.six.moves.urllib.parse import urlencode
    from ansible.module_utils.six.moves.urllib.parse import urlsplit
    fakesplit = urlsplit('http://foo.bar/abc')
    http_url = 'http://foo.bar/abc'

# Generated at 2022-06-12 23:10:23.015562
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.vault import VaultSecret

    unsafe_string = AnsibleUnsafeText('This is unsafe!')
    assert unsafe_string.__UNSAFE__ is True
    assert _is_unsafe(unsafe_string) is True

    vault_secret = VaultSecret(b'\x0c\x03h\xd1\x82\x82\xe9\xeb')
    assert vault_secret.__ENCRYPTED__ is True
    assert _is_vault(vault_secret) is True


# Generated at 2022-06-12 23:10:30.176130
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Create AnsibleJSONEncoder object
    ansible_json_encoder = AnsibleJSONEncoder()

    # Test with safe_object
    class safe_object(object):
        pass
    safe_object.__UNSAFE__ = False
    safe_object.__ENCRYPTED__ = False
    safe_object.a = 1
    safe_object.b = 2
    safe_object.c = 3
    actual_result = ansible_json_encoder.default(safe_object)
    expected_result = {'a': 1, 'c': 3, 'b': 2}
    assert actual_result == expected_result

    # Test with insecure_object
    class insecure_object(object):
        pass
    insecure_object.__UNSAFE__ = True

# Generated at 2022-06-12 23:10:39.611264
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test for normal cases
    d = AnsibleJSONEncoder().default(Mapping())
    assert isinstance(d, dict)
    d = AnsibleJSONEncoder().default({"a": "b"})
    assert d == {"a": "b"}
    d = AnsibleJSONEncoder().default({"0": "b"})
    assert d == {"0": "b"}
    d = AnsibleJSONEncoder().default({0: "b"})
    assert d == {0: "b"}
    d = AnsibleJSONEncoder().default({"a": "b", "c": "d"})
    assert d == {"a": "b", "c": "d"}
    d = AnsibleJSONEncoder().default({"a": ["b", "c"]})
    assert d == {"a": ["b", "c"]}

# Generated at 2022-06-12 23:10:42.505933
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(datetime.datetime(2019, 1, 1, 12, 0, 0)) == '2019-01-01T12:00:00'


# Generated at 2022-06-12 23:10:46.023169
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    ansible_unsafe = json_encoder.default("abc123")
    assert ansible_unsafe == "abc123", 'Type of ansible_unsafe should be string'


# Generated at 2022-06-12 23:10:51.847428
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test for method default of class AnsibleJSONEncoder
    '''
    from ansible.parsing.vault import VaultLib

    # Testing if vault object
    my_str = "test_str"
    my_pass = "test_pass"
    my_vault = VaultLib(my_pass)
    my_encrypted_str = my_vault.encrypt(my_str)
    my_encrypted_str_obj = my_encrypted_str

    ansible_jsonencoder = AnsibleJSONEncoder(vault_to_text=False)
    assert isinstance(ansible_jsonencoder.default(my_encrypted_str_obj), dict)

    ansible_jsonencoder = AnsibleJSONEncoder(vault_to_text=True)

# Generated at 2022-06-12 23:11:10.498718
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.common.collections import AnsibleVaultEncryptedUnicode

    now = datetime.datetime.now()
    plain = 'text'
    unsafe = AnsibleUnsafe(plain)
    vault = AnsibleVaultEncryptedUnicode(plain)

    assert AnsibleJSONEncoder().default(plain) == plain
    assert AnsibleJSONEncoder().default(unsafe) == {'__ansible_unsafe': plain}
    assert AnsibleJSONEncoder(vault_to_text=True).default(vault) == plain
    assert AnsibleJSONEncoder(vault_to_text=False).default(vault) == {'__ansible_vault': vault._ciphertext}
    assert Ans

# Generated at 2022-06-12 23:11:19.121430
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = AnsibleJSONEncoder()
    example = {'a': 1, 'b': False, 'c': 'string', 'd': [1, 2], 'e': {'f': 'g'}, 'h': datetime.datetime.utcnow(), 'i': AnsibleUnsafe('string')}
    result = obj.default(example)
    if result['i']:
        if result['i']['__ansible_unsafe'] == example['i']:
            print('Object AnsibleJSONEncoder was properly converted in JSON format')
        else:
            print('ERROR! Object AnsibleJSONEncoder was not properly converted')
    else:
        print('ERROR! Object AnsibleJSONEncoder was not properly converted')



# Generated at 2022-06-12 23:11:29.741215
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils import basic
    from ansible.module_utils.six import ensure_text, ensure_native
    from ansible.parsing.vault import VaultLib

    # Assert with an unsafe object
    unsafe_value = basic._UNSAFE_EXAMPLE
    assert isinstance(unsafe_value, getattr(basic, 'AnsibleUnsafeText', None))
    assert json.loads(json.dumps(unsafe_value, cls=AnsibleJSONEncoder)) == 'look at me!!!'

    # Assert with an encrypted object
    vault_pwd = VaultLib.generate_key()
    vault_value = VaultLib(vault_pwd)
    plaintext = 'encrypted output'
    encrypted_value = vault_value.encrypt(plaintext)

# Generated at 2022-06-12 23:11:37.823840
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    encoder = AnsibleJSONEncoder()
    string_result = encoder.default(AnsibleUnsafeText(u'# This string is safe'))
    assert isinstance(string_result, unicode)

    # '''Do not encode this string'''
    # '''Do not encode this string'''
    unsafe_result = encoder.default(AnsibleUnsafeText(u'''Do not encode this string'''))
    assert isinstance(unsafe_result, dict)
    assert set(['__ansible_unsafe']) <= set(unsafe_result.keys())


# Generated at 2022-06-12 23:11:46.093150
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class TestVaultObj(object):
        __ENCRYPTED__ = True
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext
    class TestUnsafeObj(object):
        __UNSAFE__ = True
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext
    plain = 'plain text'
    vault = TestVaultObj('ciphertext')
    unsafe = TestUnsafeObj('123456')
    date = datetime.date.today()
    assert AnsibleJSONEncoder().default(plain) == plain
    assert AnsibleJSONEncoder().default(vault) == {'__ansible_vault': 'ciphertext'}

# Generated at 2022-06-12 23:11:55.659105
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping

    assert(hasattr(AnsibleJSONEncoder, 'default'))

    # Case 1: json.JSONEncoder.default returns None
    json_encoder = json.JSONEncoder()
    ansible_json_encoder = AnsibleJSONEncoder()
    assert(json_encoder.default(0j) == ansible_json_encoder.default(0j))
    assert(json_encoder.default(1j) == ansible_json_encoder.default(1j))

    # Case 2: json.JSONEncoder.default returns not None
    json_encoder = json.JSONEncoder()
    ansible_json_encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:11:58.116674
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for method default of class AnsibleJSONEncoder"""

    assert AnsibleJSONEncoder().default(AnsibleJSONEncoder()) == str(AnsibleJSONEncoder())

# Generated at 2022-06-12 23:12:04.833040
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    obj = AnsibleJSONEncoder()
    ansible_vault_value = 'name: value'
    ansible_vault_obj = AnsibleJSONEncoder(vault_to_text=True)
    assert obj.default(my_dict) == my_dict
    assert ansible_vault_obj.default(ansible_vault_value) != ansible_vault_value

# Generated at 2022-06-12 23:12:12.217334
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:12:17.173762
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    dict_value = dict(a=1, b=2)
    assert json_encoder.default(dict_value) == dict(a=1, b=2)

    encoded_dict_value = json_encoder.encode(dict_value)
    assert encoded_dict_value == '{"a": 1, "b": 2}'



# Generated at 2022-06-12 23:12:36.988602
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default({'foo': 'bar'}) == {'foo': 'bar'}



# Generated at 2022-06-12 23:12:45.807763
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import MutableSequence

    class TestVault(VaultLib):
        _ciphertext = 'VaultTest'

    class TestVaultSequence(MutableSequence, TestVault):
        pass

    v = TestVault()
    v_text = TestVaultSequence()
    v_text._ciphertext = 'VaultTestText'

    string_encoder = AnsibleJSONEncoder()
    value1 = string_encoder.default(v)
    value2 = string_encoder.default(v_text)

    assert value1 == {'__ansible_vault': u'VaultTest'}
    assert value2 == 'VaultTestText'

# Generated at 2022-06-12 23:12:55.886475
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert(json.dumps(AnsibleJSONEncoder().default(dict()),
                      cls=AnsibleJSONEncoder) == '{}')
    assert(json.dumps(AnsibleJSONEncoder().default(5),
                      cls=AnsibleJSONEncoder) == '5')
    assert(json.dumps(AnsibleJSONEncoder().default('hello'),
                      cls=AnsibleJSONEncoder) == '"hello"')

    # test with vault object
    assert(json.dumps(AnsibleJSONEncoder().default(dict(__ENCRYPTED__=True, _ciphertext=b'hello')),
                      cls=AnsibleJSONEncoder) == '{"__ansible_vault": "hello"}')

    # test with unsafe object

# Generated at 2022-06-12 23:13:01.609721
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe:
        __UNSAFE__ = True
        value = 'value'
        def __init__(self, value):
            self.value = value

        def __unicode__(self):
            return self.value

        def __str__(self):
            return self.value

        def __repr__(self):
            return self.value

    class AnsibleVault:
        __ENCRYPTED__ = True
        def __init__(self, _ciphertext):
            self._ciphertext = _ciphertext


# Generated at 2022-06-12 23:13:12.092394
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Unsafe:
        __UNSAFE__ = True
        def __init__(self, string):
            self.string = string

    class Safe:
        __UNSAFE__ = False

    class Vault:
        __UNSAFE__ = False
        __ENCRYPTED__ = True

    params = dict(
        hostvars={'foo': 'bar'},
        unsafe=Unsafe('bar'),
        safe=Safe(),
        vault=Vault(),
        datetime=datetime.datetime.now()
    )

    assert json.loads(json.dumps(params, cls=AnsibleJSONEncoder)) == params
    assert json.loads(json.dumps(params, cls=AnsibleJSONEncoder, preprocess_unsafe=True)) == params

# Generated at 2022-06-12 23:13:16.681590
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    import datetime
    # preprocess_unsafe is False by default
    a = AnsibleJSONEncoder()
    b = AnsibleUnsafeText('test')
    c = AnsibleUnsafeBytes('test')
    d = AnsibleUnsafeBytes('test')
    d.__UNSAFE__ = False
    e = AnsibleUnsafeBytes('test')
    e.__UNSAFE__ = False
    e.__ENCRYPTED__ = True
    e.__VAULT_VERSION__ = 1
    e.__VAULT_NOTES__ = ''
    e.__VAULT_RECIPIENT__ = ''
    m = Mapping()
    # test for AnsibleUnsafeText
    value = a.default(b)
    assert value

# Generated at 2022-06-12 23:13:27.318398
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Mapping

    def eq(a, b):
        assert a == b

    # regular types
    assert json.dumps(123) == '123'
    assert json.dumps(12.3) == '12.3'
    assert json.dumps('string') == '"string"'
    assert json.dumps(u'string') == '"string"'
    assert json.dumps(True) == 'true'
    assert json.dumps(False) == 'false'
    assert json.dumps(None) == 'null'
    assert json.dumps(binary_type('123')) == '"123"'

# Generated at 2022-06-12 23:13:28.015999
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) == None


# Generated at 2022-06-12 23:13:33.711994
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test AnsibleJSONEncoder.default
    obj = {
        'a': 'b',
    }
    encodedObj = json.dumps(obj, cls=AnsibleJSONEncoder)
    assert encodedObj == '{"a": "b"}'

    obj = {
        'a': datetime.datetime(2017, 1, 1, 0, 0, 0)
    }
    encodedObj = json.dumps(obj, cls=AnsibleJSONEncoder)
    assert encodedObj == '{"a": "2017-01-01T00:00:00"}'



# Generated at 2022-06-12 23:13:39.891959
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.crypto import ANSIBLE_VAR_PREFIX, ANSIBLE_VAULT_IDENTITY_LIST_KEY


# Generated at 2022-06-12 23:14:21.718898
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    This test cannot be triggered because the method default is ALWAYS called by previous method
    iterencode. But to be sure that it is work we call it manually.
    """
    from ansible.parsing import vault
    import datetime
    test_date = datetime.datetime(2012, 12, 12, 12, 12, 12)
    json_encoder = AnsibleJSONEncoder()
    assert json_encoder.default(test_date) == "2012-12-12T12:12:12"
    vault_secret = vault.VaultSecret('test')
    assert json_encoder.default(vault_secret) == {'__ansible_vault': 'test'}

# Generated at 2022-06-12 23:14:32.505076
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing import vault

    # Encryption
    vault_key="test"
    vault_secret="test2"
    vault_content="this is a secret"

    vault_path="test/test.yml"

    # Create vault instance
    v = VaultLib(vault_key)

    # Encrypt data
    vault_data = v.encrypt(vault_content)

    # Encrypt headers
    vault_hdr = vault.make_header(
        vault_key,
        new_vault_password=vault_secret,
        old_vault_password=vault_secret,
        vault_content=vault_path
    )

    # Get the vault item
    v_item = vault.VaultEditor.decrypt_

# Generated at 2022-06-12 23:14:40.114812
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common._json_compat import AnsibleUnsafe
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.urls import ConnectionInfo

    unsafe = AnsibleUnsafe('a string')
    unsafe.__UNSAFE__ = True
    conn_info = ConnectionInfo('http', 'localhost', 80, 'user', 'pass')

    ansible_json_encoder = AnsibleJSONEncoder()
    ansible_json_encoder_to_text = AnsibleJSONEncoder(vault_to_text=True)

    assert ansible_json_encoder.default(unsafe) == {'__ansible_unsafe': 'a string'}

# Generated at 2022-06-12 23:14:43.342742
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    o = {'__ansible_unsafe': AnsibleUnsafe('abcd')}
    assert o == ansible_json_encoder.default(o)



# Generated at 2022-06-12 23:14:53.411161
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    def _create_unsafe_obj():
        class MyUnsafe(str):
            __UNSAFE__ = True
        return MyUnsafe('my_unsafe_obj')

    def _create_vault_obj():
        class AnsibleVault(unicode):
            __ENCRYPTED__ = True
        return AnsibleVault(u'my_vault_obj')

    class MyDate(datetime.date):
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def isoformat(self):
            return '2018-01-01'

    class MyDict(dict):
        def __init__(self):
            self['key'] = 'value'


# Generated at 2022-06-12 23:15:03.312983
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Standard cases:
    #   - int
    #   - float
    #   - bool
    #   - str
    #   - list
    #   - tuple
    #   - dict
    #   - datetime
    #   - date
    #   - set
    #   - frozenset
    #   - None
    # Specific case:
    #   - vault object
    #   - unsafe object
    a = [1, 2.0, True, 'test', [1, 2], (1, 2), {'a': 1, 'b': 2}, datetime.datetime(2019, 1, 1), datetime.date(2019, 1, 1), {1, 2}, frozenset({1, 2}), None]

# Generated at 2022-06-12 23:15:11.664463
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.utils.unsafe_proxy import wrap_var

    json_unsafe_string = '{"__ansible_unsafe": "test"}'

    unsafe_text = AnsibleUnsafe('test')
    unsafe_unicode = AnsibleUnsafe(u'\u263A')
    unsafe_bytearray = AnsibleUnsafe(b'\xFF\xFE\xFD')
    unsafe_nonstring = AnsibleUnsafe(1)

    vault_text = VaultSecret(VaultLib([], None).encrypt('test'))
    vault_unicode = VaultSecret(VaultLib([], None).encrypt(u'\u263A'))
    vault_byt

# Generated at 2022-06-12 23:15:19.832697
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.vault import VaultLib

    ansible_encoder = AnsibleJSONEncoder()
    std_encoder = json.JSONEncoder()
    vault_password = 'vault_password'
    vault_obj = VaultLib(vault_password)
    message_unsafe = 'Admin Password' #<--- AnsibleUnsafe
    ansible_unsafe = ansible_encoder.default(message_unsafe)
    std_unsafe = std_encoder.default(message_unsafe)
    assert ansible_unsafe == {'__ansible_unsafe': u'Admin Password'}
    assert ansible_unsafe != std_unsafe
    message_vault = vault_obj.encrypt

# Generated at 2022-06-12 23:15:28.266849
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Given
    o = {'__ansible_unsafe': 'hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha'}
    encoder = AnsibleJSONEncoder()

    # When
    json_data = encoder.default(o)

    # Then
    assert json_data == o


# Generated at 2022-06-12 23:15:38.789379
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible import constants as C
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import string_types
    from ansible.parsing.vault import VaultLib

    def _test(value, **kwargs):
        assert isinstance(value, (string_types, ImmutableDict))

        r = json.dumps(value, cls=AnsibleJSONEncoder, **kwargs)
        assert json.loads(r) == value

    vault_password = 'VaultPassword'
    vault_a = VaultLib([vault_password], C.DEFAULT_VAULT_ID_MATCH)
    vault_b = vault_a.encrypt(vault_password)

    _test(u'This is a unicode string!')