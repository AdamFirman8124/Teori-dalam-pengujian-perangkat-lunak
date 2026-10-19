

# Generated at 2022-06-12 23:06:41.286511
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test with AnsibleUnsafe
    assert AnsibleJSONEncoder().default(json.dumps("ansible")) == "ansible"
    assert AnsibleJSONEncoder().default(json.dumps("ansible").decode("utf-8")) == "ansible"

    # Test with AnsibleVault
    from ansible.parsing.vault import VaultLib
    assert AnsibleJSONEncoder().default(VaultLib("ansible")) == '{"__ansible_vault": "AQAAAAEAAAAAgAAAAoAAAAFQAAADkAAAACAAAAAAAAAAAA"}'
    assert AnsibleJSONEncoder(vault_to_text=True).default(VaultLib("ansible")) == "ansible"

    # Test with date object

# Generated at 2022-06-12 23:06:46.079007
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test the default of AnsibleJSONEncoder class
    # init the AnsibleJSONEncoder class
    encoder = AnsibleJSONEncoder()

    # set the input object
    o = 'test'

    # get the default
    default = encoder.default(o)

    # assert result
    assert default == 'test', 'The method default() does not work as expected'


# Generated at 2022-06-12 23:06:53.421073
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()

    # Test with unsafe object - should always return a dict
    class AnsibleUnsafe:
        __UNSAFE__ = True

    pre_unsafe = AnsibleUnsafe()
    aje.default(pre_unsafe)
    assert isinstance(pre_unsafe, dict)

    # Test with plain string
    assert isinstance(aje.default('hello world'), str)

    # Test with mapping
    nontrivdict = {'hello': 'world', 'nested': {'foo': 'bar', 'baz': ['a', 'b', 'c']}}
    nontrivdict2 = aje.default(nontrivdict)
    assert nontrivdict == nontrivdict2

    # Test with sequence

# Generated at 2022-06-12 23:07:00.546871
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = "I am unsafe"
    assert AnsibleJSONEncoder.default(AnsibleJSONEncoder, o) == o

    o = "I am encrypted"
    assert AnsibleJSONEncoder.default(AnsibleJSONEncoder, o) == o

    o = "I am a mapping"
    assert AnsibleJSONEncoder.default(AnsibleJSONEncoder, o) == o

    o = "I am a date"
    assert AnsibleJSONEncoder.default(AnsibleJSONEncoder, o) == o

# Generated at 2022-06-12 23:07:08.352795
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:07:14.247357
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Testing with date object
    date = datetime.date(2019, 3, 8)
    assert AnsibleJSONEncoder().default(date) == '2019-03-08'
    # Testing with dictionary object
    host_vars = {'inventory_hostname': 'localhost', 'ansible_host': '127.0.0.1'}
    assert AnsibleJSONEncoder().default(host_vars) == host_vars


# Generated at 2022-06-12 23:07:21.115009
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleVaultEncryptedUnsafeText

    data = [
        ('Hello world', '"Hello world"'),
        (1, '1'),
        (True, 'true'),
        (False, 'false'),
        (None, 'null'),
        ({'a': 1, 'b': 2}, '{"a": 1, "b": 2}'),
        (['a'], '["a"]'),
        (datetime.datetime(2017, 5, 6, 23, 17, 0), '"2017-05-06T23:17:00"')
    ]

    for input_data, expected_output in data:
        aje = AnsibleJSONEncoder()
       

# Generated at 2022-06-12 23:07:32.460380
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    sample_json = {}

    # test _is_unsafe
    assert _is_unsafe(None) is False
    assert _is_unsafe('not unsafe') is False
    assert _is_unsafe([1, 2, 3]) is False
    assert _is_unsafe({'a': 1}) is False
    assert _is_unsafe(AnsibleUnsafe((1, 2, 3))) is True
    assert _is_unsafe(AnsibleUnsafe('unsafe')) is True
    assert _is_unsafe(AnsibleUnsafe(1)) is True
    assert _is_unsafe(AnsibleUnsafe(True)) is True
    assert _is_unsafe(AnsibleUnsafe({'a': 'b'})) is True

# Generated at 2022-06-12 23:07:39.754383
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()

    class test:
        def __init__(self, attr1, attr2):
            self.__UNSAFE__ = True
            self.__ENCRYPTED__ = False
            self.attr1 = attr1
            self.attr2 = attr2

    class test2:
        def __init__(self, attr1, attr2):
            self.__UNSAFE__ = False
            self.__ENCRYPTED__ = True
            self.attr1 = attr1
            self.attr2 = attr2

    class test3:
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2


# Generated at 2022-06-12 23:07:51.034721
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    import ansible.module_utils.basic
    import ansible.module_utils.six.moves.urllib.parse

    # Test case
    # a = {
    #     'b': {
    #         'c': ['d', 'e', 'f'],
    #         'g': {
    #             'h': ansible.module_utils.six.text_type('i'),
    #             'j': ansible.module_utils.six.text_type('k'),
    #             'l': ansible.module_utils.six.moves.urllib.parse.quote_plus(ansible.module_utils.six.text_type('m'))
    #         }
    #     }
    # }

    # Expected result
    # a

# Generated at 2022-06-12 23:07:54.745646
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(datetime.datetime.utcnow())


# Generated at 2022-06-12 23:08:03.719256
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    expected_unsafe = {'__ansible_unsafe': "unsafe"}
    expected_vault = {'__ansible_vault': "vault::0"}
    expected_date = "2017-04-20"
    expected_dict = {'custom': 'dict'}
    # Test UNSAFE
    result = encoder.default(AnsibleUnsafeTest())
    assert result == expected_unsafe
    # Test VAULT
    result = encoder.default(AnsibleVaultTest())
    assert result == expected_vault
    # Test DATE
    result = encoder.default(datetime.date(2017, 4, 20))
    assert result == expected_date
    # Test DICT
    result = encoder.default(expected_dict)
    assert result

# Generated at 2022-06-12 23:08:04.368697
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    pass

# Generated at 2022-06-12 23:08:14.915105
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = {
        '__ansible_vault': b'test_ansible_vault',
        '__ansible_unsafe': 'test_ansible_unsafe',
        'test_date': datetime.date(2019, 11, 8),
        'test_datetime': datetime.datetime(2019, 11, 8),
        'test_mapping': {'test_key': 'test_value'},
        'test_seq': [1, 2],
        'test_int': 1,
        'test_str': 'test_str'
    }
    
    # ansible_unsafe -> json
    ansible_unsafe = AnsibleJSONEncoder(vault_to_text=True)
    ansible_unsafe = json.loads(ansible_unsafe.encode(data))

    assert ans

# Generated at 2022-06-12 23:08:19.614849
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(u'foo') == u'foo'
    assert AnsibleJSONEncoder().default(b'foo') == b'foo'
    assert AnsibleJSONEncoder().default(u'foo'.encode()) == u'foo'
    assert AnsibleJSONEncoder().default(b'foo'.decode()) == u'foo'

# Generated at 2022-06-12 23:08:25.090356
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = {'fortytwo': 42}
    assert json.dumps(o) == AnsibleJSONEncoder().default(o)
    o = {'date': datetime.datetime(2019, 2, 28)}
    assert json.dumps(o) == AnsibleJSONEncoder().default(o)
    o = {'date': datetime.date(2019, 2, 28)}
    assert json.dumps(o) == AnsibleJSONEncoder().default(o)

# Generated at 2022-06-12 23:08:34.948025
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # AnsibleVaultEncryptedUnicode
    vault = VaultLib(None)
    vault_obj = vault.encrypt(u'test')
    assert vault_obj == u'test'
    assert isinstance(vault_obj, u'unicode')
    assert getattr(vault_obj, '__ENCRYPTED__', False)

    # Ensure vault instances are encoded as a dict
    # containing the Vault token and ciphertext

# Generated at 2022-06-12 23:08:44.786144
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types

    vault_secret = "password"
    vault_content = "Vaulted password"
    vault_password = "vault_password"

    vault = VaultLib([])
    vault.read_vault_password_file(vault_password)
    ciphertext = vault.encrypt(vault_secret)

    json_encoder = AnsibleJSONEncoder()


# Generated at 2022-06-12 23:08:55.227494
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test with custom class
    class TestClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    class TestClass2(TestClass):
        def __init__(self):
            super(TestClass2, self).__init__()
            self.c = 3

    class TestClass3(TestClass):
        pass

    class TestClass4(TestClass2):
        def __init__(self):
            super(TestClass4, self).__init__()
            self.d = 4

    aje = AnsibleJSONEncoder()
    assert aje.default(TestClass()) == {'a': 1, 'b': 2}
    assert aje.default(TestClass2()) == {'a': 1, 'b': 2, 'c': 3}
    assert aje.default

# Generated at 2022-06-12 23:08:56.894528
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default("AnsibleText")
    assert o == "AnsibleText"



# Generated at 2022-06-12 23:09:11.289599
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_string = '{"info":{"platform": "darwin", "architecture": "ansible_architecture"}}'
    safe_json_string = '{"info":{"platform": "darwin", "architecture": "__ansible_unsafe"}}'
    vault_json_string = '{"info":{"platform": "darwin", "architecture": "__ansible_vault"}}'
    json_object = json.loads(json_string)
    safe_json_object = json.loads(safe_json_string)
    vault_json_object = json.loads(vault_json_string)
    assert json_string == AnsibleJSONEncoder().encode(json_object)
    assert safe_json_string == AnsibleJSONEncoder(preprocess_unsafe=True).encode(json_object)
   

# Generated at 2022-06-12 23:09:21.290072
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes


# Generated at 2022-06-12 23:09:27.921622
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(b'foo') == u'foo'
    assert AnsibleJSONEncoder().default(u'foo') == u'foo'
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default(0) == 0
    assert AnsibleJSONEncoder().default(0.0) == 0.0
    assert AnsibleJSONEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert AnsibleJSONEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

# Generated at 2022-06-12 23:09:38.418041
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.vars import AnsibleUnsafe

    # Prepare for the test
    class obj_abc:
        def __init__(self):
            self.abc = 'abc'
            self.__ENCRYPTED__ = True

    class obj_dict:
        def __init__(self):
            self.a = 'a'
            self.b = 'b'
            self.c = 'c'

    class obj_date:
        def __init__(self):
            self._date = datetime.datetime.today()
            self._date_format = '%Y-%m-%d %H:%M:%S'

    class obj_unsafe:
        def __init__(self):
            self.__UNSAFE__ = True

# Generated at 2022-06-12 23:09:47.367184
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.dumps({u'key': u'somevalue'}, cls=AnsibleJSONEncoder) == '{"key":"somevalue"}'
    assert json.dumps({u'key': [u'somevalue']}, cls=AnsibleJSONEncoder) == '{"key":["somevalue"]}'
    assert json.dumps({u'key': {u'key1': u'somevalue'}}, cls=AnsibleJSONEncoder) == '{"key":{"key1":"somevalue"}}'
    assert json.dumps({u'key': datetime.datetime(2016, 12, 20, 11, 23, 59)}, cls=AnsibleJSONEncoder) == '{"key":"2016-12-20T11:23:59"}'

# Generated at 2022-06-12 23:09:53.485386
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    e = AnsibleJSONEncoder()
    assert e.default('test value') == 'test value'
    assert e.default(1234) == 1234
    assert e.default(12.34) == 12.34
    assert e.default([1,2,3,4]) == [1,2,3,4]
    assert e.default([1.1,2.2,3.3,4.4]) == [1.1, 2.2, 3.3, 4.4]
    assert e.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}


# Generated at 2022-06-12 23:09:57.447474
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()
    str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    assert a.default(str) == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'


# Generated at 2022-06-12 23:10:04.746791
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.basic import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import binary_type
    class TestClass(object):
        def __init__(self, field1, field2, field3):
            self.field1 = field1
            self.field2 = field2
            self.field3 = field3
        def __repr__(self):
            return 'TestClass(%r, %r, %r)' % (self.field1, self.field2, self.field3)
        def __eq__(self, other):
            return self.field1 == other.field1 and self.field2 == other.field2 and self.field3 == other.field3


# Generated at 2022-06-12 23:10:10.692979
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = {
        'placeholder': [
            'Symbol: __ansible_vault',
            '__ansible_unsafe',
        ],
    }
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    json_str = json.dumps(data, cls=AnsibleJSONEncoder)
    assert encoder.default(data) == json.loads(json_str)



# Generated at 2022-06-12 23:10:13.272288
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Case: AnsibleVaultAES256, AnsibleVaultAES256.__ENCRYPTED__ == True
    # Return: output of ansibleJSONEncoder.default
    assert None != AnsibleJSONEncoder().default(AnsibleUnsafe(''))


# Generated at 2022-06-12 23:10:25.757320
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    a = AnsibleJSONEncoder(sort_keys=True, indent=2)
    x = a.default([1,2,3])
    assert x == [1,2,3]

    x = a.default({"b": "ansible"})
    assert x == {"b": "ansible"}

    x = a.default(1.1)
    assert x == 1.1

    class C:
        pass

    c = C()
    c.__UNSAFE__ = True
    x = a.default(c)
    assert x == {'__ansible_unsafe': u"'\\u0026'"}


# Generated at 2022-06-12 23:10:35.571722
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    import datetime

# Generated at 2022-06-12 23:10:45.048299
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import string_types
    vault_password = VaultLib([])
    vault_password.password = 'foobar'

# Generated at 2022-06-12 23:10:51.146426
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert '__ansible_unsafe' in json.dumps({'x': 'y'}, cls=AnsibleJSONEncoder, indent=2)
    assert '__ansible_vault' in json.dumps({'x': 'y'}, cls=AnsibleJSONEncoder, indent=2)
    assert '__ansible_unsafe' not in json.dumps({'x': 'y'}, cls=AnsibleJSONEncoder, indent=2, vault_to_text=True)

# Generated at 2022-06-12 23:10:57.874014
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for the ``default`` method of ``AnsibleJSONEncoder``.

    This is done by first converting the input object to a JSON string using JSONEncoder and then decoding it using
    JSONDecoder. This method makes sure that we don't use incorrect value of ``default`` method of ``AnsibleJSONEncoder``.
    """
    def assert_equal(input_object):
        ansible_json_encoder = AnsibleJSONEncoder()
        output_json_string = json.dumps(input_object, cls=ansible_json_encoder)
        output_object = json.loads(output_json_string)
        assert input_object == output_object

    # string
    assert_equal("test")
    # integer
    assert_equal(10)
    # float
    assert_equal(1.1)


# Generated at 2022-06-12 23:11:07.038130
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible
    JSONEncoder = AnsibleJSONEncoder()
    assert JSONEncoder.default(ansible.utils.unsafe_proxy.AnsibleUnsafeText('hello')) == {'__ansible_unsafe': 'hello'}
    assert JSONEncoder.default(ansible.vars.unsafe_proxy.AnsibleVaultEncryptedUnicode('hello')) == {'__ansible_vault': 'hello'}
    assert JSONEncoder.default(datetime.date.today()) == datetime.date.today().isoformat()
    assert JSONEncoder.default(datetime.datetime.utcnow()) == datetime.datetime.utcnow().isoformat()

# Generated at 2022-06-12 23:11:14.108400
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret

    d = {'unsafe': VaultSecret('hello')}
    assert AnsibleJSONEncoder().default(d) == d
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(d) == d
    assert AnsibleJSONEncoder(vault_to_text=True).default(d) == d
    assert AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True).default(d) == d

    d = {'unsafe': 'hello'}
    assert AnsibleJSONEncoder().default(d) == d
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(d) == d
    assert AnsibleJSONEncoder(vault_to_text=True).default(d) == d
   

# Generated at 2022-06-12 23:11:22.957377
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert AnsibleJSONEncoder().default("test") == "test"

    class Unsafe:
        __UNSAFE__ = 1

    class Encrypted:
        __ENCRYPTED__ = 1
        _ciphertext = "vault"

    assert AnsibleJSONEncoder().default(Unsafe()) == {"__ansible_unsafe": "NQ=="}
    assert AnsibleJSONEncoder(vault_to_text=True).default(Encrypted()) == "vault"
    assert AnsibleJSONEncoder(vault_to_text=False).default(Encrypted()) == {"__ansible_vault": "vault"}

# Generated at 2022-06-12 23:11:33.109429
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib, VaultSecret, VaultPassword
    from ansible.module_utils.six import text_type
    import base64
    import datetime


# Generated at 2022-06-12 23:11:40.456405
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    input_list = [
        {'a': 'foo', 'b': 'bar'},
        'string',
        b'bytes',
        datetime.datetime(2000, 1, 1),
        True,
        None,
    ]
    output_list = [
        {'a': 'foo', 'b': 'bar'},
        'string',
        'bytes',
        '2000-01-01T00:00:00',
        True,
        None,
    ]
    for i in range(len(input_list)):
        assert j.default(input_list[i]) == output_list[i]


# Generated at 2022-06-12 23:11:53.251243
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_object = {
        'datetime': datetime.datetime.now(),
        'date': datetime.date.today(),
        'none': None
    }
    result = AnsibleJSONEncoder().encode(test_object)
    assert '__ansible_unsafe' not in result
    assert '__ansible_vault' not in result
    assert '__ansible_hostname' not in result
    assert '__ansible_hostvars' not in result

# Generated at 2022-06-12 23:11:56.128933
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default("hello world") == "hello world"
    assert AnsibleJSONEncoder().default("hello world".replace("hello", "HELLO")) == "HELLO world"

# Generated at 2022-06-12 23:12:04.833737
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test the class of AnsibleJSONEncoder
    encoder_cls = encoder.__class__
    assert encoder_cls == AnsibleJSONEncoder

    # test the default method
    data_dict = {'a': 1, 'b': ['x', 'y', 'z'], 'c': {'first': 'one', 'second': {'i': '1', 'ii': '2'}}}
    result = encoder.default(data_dict)
    assert result == {'a': 1, 'b': ['x', 'y', 'z'], 'c': {'first': 'one', 'second': {'i': '1', 'ii': '2'}}}
    assert type(result) == dict


# Generated at 2022-06-12 23:12:11.182462
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    o = {'random': 'object1', 'random1': 'object2'}
    assert encoder.default(o) == {'random': 'object1', 'random1': 'object2'}

    # Test for hostvars object type
    from ansible.module_utils.facts.hostvars import HostVars
    hv = HostVars(hostname='hostname')
    hv.update({'random': 'object1', 'random1': 'object2'})
    assert encoder.default(hv) == {'random': 'object1', 'random1': 'object2'}

# Generated at 2022-06-12 23:12:18.374059
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test default method of AnsibleJSONEncoder."""

    # test encode an instance of AnsibleUnsafe that is not an AnsibleUnsafe
    test_data_1 = b"ansible_unsafe"
    test_data_1_class = AnsibleUnsafe(test_data_1)
    test_data_1_ansible_json_encoder = AnsibleJSONEncoder()
    result_1 = test_data_1_ansible_json_encoder.default(test_data_1_class)
    assert result_1 == {'__ansible_unsafe': test_data_1.decode('utf-8')}



# Generated at 2022-06-12 23:12:24.313747
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default(False) == False
    assert AnsibleJSONEncoder().default({'a': True}) == {'a': True}
    assert AnsibleJSONEncoder().default(Mapping()) == {}
    assert AnsibleJSONEncoder().default(datetime.date(2010, 4, 19)) == u'2010-04-19'
    assert AnsibleJSONEncoder().default(datetime.datetime(2010, 4, 19)) == u'2010-04-19T00:00:00'


# Generated at 2022-06-12 23:12:30.865735
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default('foo') == 'foo'
    assert ansible_json_encoder.default(1) == 1
    assert ansible_json_encoder.default(1.2) == 1.2
    assert ansible_json_encoder.default(True) == True
    assert ansible_json_encoder.default(False) == False

# Generated at 2022-06-12 23:12:41.105686
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test method ``AnsibleJSONEncoder.default``"""

    # class to test on
    class AnsibleUnsafeTestObject(object):
        __UNSAFE__ = True

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

        def __repr__(self):
            return self.value

    # tests
    encoder = AnsibleJSONEncoder()

    o = AnsibleUnsafeTestObject('unsafe')
    value = encoder.default(o)
    assert value == {'__ansible_unsafe': 'unsafe'}

    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    encrypted_o = vault.encrypt('vault_text', 'faketext')
    value

# Generated at 2022-06-12 23:12:50.940426
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test = {'key1': 'value1',
            'key2': [1, 2, 3],
            'key3': {
                'key31': 'value31',
                'key32': 'value32',
                'key33': {
                    'key331': 'value331',
                    'key332': 'value332',
                }
            }}
    result = AnsibleJSONEncoder().default(test)
    assert result == test


# Generated at 2022-06-12 23:12:53.158332
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(UnicodeUnsafe('a')) == {'__ansible_unsafe': 'a'}


# Generated at 2022-06-12 23:13:16.753597
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.encryption import AnsibleUnsafe
    from ansible.module_utils.common.encryption import VaultEncryptedUnicode

    # data for testing

# Generated at 2022-06-12 23:13:18.221709
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
  value = AnsibleJSONEncoder().default('test')
  assert value == 'test'


# Generated at 2022-06-12 23:13:29.148314
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''Test method default of AnsibleJSONEncoder class'''

    # Sample dictionary
    obj = {'key': 'value', 'key2': 0.5}
    # Sample object
    obj1 = object()
    # Sample object containing object
    obj2 = object()
    obj2.obj1 = obj1
    # Sample object containing list
    obj3 = object()
    obj3.list = ['hello', obj2]

    class MyObj(object):
        '''Contains dictionary as attribute'''

        def __init__(self):
            self.val = obj

    date_obj = datetime.datetime(2018, 7, 1)
    date_obj1 = datetime.date(2018, 7, 1)
    ansible_unsafe_obj = MyObj()

# Generated at 2022-06-12 23:13:38.397666
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import AnsibleMapping
    from ansible.parsing.vault import VaultLib
    assert AnsibleJSONEncoder().default(AnsibleMapping({'a': 1, 'b': 2})) == {"a": 1, "b": 2}

# Generated at 2022-06-12 23:13:50.119339
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    encoder = AnsibleJSONEncoder()

    # Test for Vault
    vault_password = 's3cr3t'
    vault = VaultLib(vault_password)
    cipher = vault.encrypt('value')
    password = cipher.decode('utf-8')
    # json.JSONEncoder.default(self, o)
    ansible_vault = encoder.default(password)
    d = json.loads(ansible_vault)
    value = vault.decrypt(d.get('__ansible_vault'))
    assert value == 'value'

    # Test for datetime
    ansible_date = encoder.default(datetime.datetime(2019, 1, 2, 3, 4, 5))

# Generated at 2022-06-12 23:13:59.355775
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six.moves import StringIO as six_StringIO
    from ansible.parsing.vault import VaultLib as ansible_VaultLib
    from ansible.parsing.vault import ansible_VaultSecret
    import datetime

    Mapping = dict # we don't care about the particular mapping type here

    # Test the base case:
    a = '__ENCRYPTED__'
    b = AnsibleJSONEncoder().default(a)
    assert(b == '__ENCRYPTED__')

    # Test a vault object:
    c = ansible_VaultSecret('ansible')
    d = AnsibleJSONEncoder().default(c)
    # __ansible_vault was never set to be encrypted, so we should end up with:

# Generated at 2022-06-12 23:14:07.185058
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_data = [
        {'vault_to_text': True,
         'o': '$ANSIBLE_VAULT;1.1;AES256;ansible;thisisadummytext',
         'exp_result': '$ANSIBLE_VAULT;1.1;AES256;ansible;thisisadummytext'
         },
        {'vault_to_text': False,
         'o': '$ANSIBLE_VAULT;1.1;AES256;ansible;thisisadummytext',
         'exp_result': {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;ansible;thisisadummytext'}
         }
    ]


# Generated at 2022-06-12 23:14:13.808465
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    aje = AnsibleJSONEncoder()
    safe = aje.default(AnsibleVaultEncryptedUnicode('foo', errors='strict'))
    assert safe == {"__ansible_vault": 'foo'}

    unsafe = aje.default(AnsibleUnsafeText('foo', errors='strict'))
    assert unsafe == {"__ansible_unsafe": 'foo'}

    # normal string
    normal = aje.default('foo')
    assert normal == 'foo'


# Generated at 2022-06-12 23:14:15.028448
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = datetime.datetime.now()
    obj_str = AnsibleJSONEncoder().default(obj)
    assert isinstance(obj_str, str)



# Generated at 2022-06-12 23:14:21.500163
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = AnsibleJSONEncoder(sort_keys=True, indent=4)
    # date
    assert o.default(datetime.datetime(2018, 10, 4, 10, 22, 1)) == '2018-10-04T10:22:01'
    # hostvars
    assert o.default({'a': 'b'}) == {'a': 'b'}
    # vault object
    o = AnsibleJSONEncoder(sort_keys=True, indent=4, vault_to_text=True)
    assert o.default(o.default('b')) == 'b'

# Generated at 2022-06-12 23:14:39.549593
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default({'test': 'hello'}) == {'test': 'hello'}
    assert AnsibleJSONEncoder().default(('hello', 'world')) == ['hello', 'world']
    assert AnsibleJSONEncoder().default(('hello', {'test': 'world'})) == ['hello', {'test': 'world'}]



# Generated at 2022-06-12 23:14:49.427711
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import b
    from ansible.parsing.vault import VaultLib
    from ansible_collections.community.crypto.plugins.module_utils.crypto import AnsibleUnsafe

    # Roundtrip
    value = AnsibleUnsafe('test\n')
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, ensure_ascii=False)
    assert json.loads(encoder.default(value)) == encoder.default(value)

    # Vault object
    vault_pass = b('test\n')
    vault_obj = VaultLib(vault_pass)
    enc_value = to_text(vault_obj.encrypt(value))
    encrypted_value = AnsibleUnsafe(enc_value)
    encrypted_value.__ENCRYPTED

# Generated at 2022-06-12 23:14:59.679754
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe = ansible_module_utils.unsafe_proxy.AnsibleUnsafeText(u'foo\n')
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(unsafe) == {'__ansible_unsafe': u'foo\n'}
    # to_text should convert the unsafe_proxy.AnsibleUnsafeText to text, the end result should be the same
    unsafe_text = ansible_module_utils.unsafe_proxy.AnsibleUnsafeText(u'foo\n')
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(to_text(unsafe_text)) == u'foo\n'

    vault_text = ansible_module_utils.vault.VaultLib([u'foo\n']).encrypt(u'foo')

# Generated at 2022-06-12 23:15:04.771590
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert ansible_encoder.default(datetime.date(2019, 4, 23)) == "2019-04-23"
    assert ansible_encoder.default(datetime.datetime(2019, 4, 23, 16, 57, 15)) == "2019-04-23T16:57:15"
    assert ansible_encoder.default(datetime.datetime(2019, 4, 23, 16, 57, 15, 5)) == "2019-04-23T16:57:15.000005"
    assert ansible_encoder.default(['test', 'test', 'test']) == ['test', 'test', 'test']
    assert ansible_encoder.default("test") == "test"


# Generated at 2022-06-12 23:15:12.749172
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test for __ENCRYPTED__ vault object
    from ansible.parsing.vault import VaultLib
    vault_password = 'ansible'
    vault = VaultLib(vault_password)
    plaintext_vault = vault.encrypt('mysecret')
    json_vault_object = json.dumps(plaintext_vault, cls=AnsibleJSONEncoder)

# Generated at 2022-06-12 23:15:20.654974
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json

    # Test that the AnsibleJSONEncoder handles booleans and integers
    assert json.dumps(True, cls=AnsibleJSONEncoder) == 'true'
    assert json.dumps(False, cls=AnsibleJSONEncoder) == 'false'
    assert json.dumps(123, cls=AnsibleJSONEncoder) == '123'

    # Test that the AnsibleJSONEncoder does not modify existing string types
    assert json.dumps('foobar', cls=AnsibleJSONEncoder) == '"foobar"'
    assert json.dumps(u'foobar', cls=AnsibleJSONEncoder) == '"foobar"'
    assert str(json.dumps('foobar', cls=AnsibleJSONEncoder)) == '"foobar"'

    # Test that

# Generated at 2022-06-12 23:15:31.498236
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    encoder = AnsibleJSONEncoder()

    vault_obj = VaultLib()
    vault_obj.decrypt(b'$ANSIBLE_VAULT;1.1;AES256;a\nae1f9e24b5dab7c4923c5ebc8505b5c5b5169dc6ee75ac622dd9b9c30f25621044\n')

    dt_obj = datetime.datetime.now()

    class AnsibleUnsafe(str):
        __UNSAFE__ = True
        __ENCRYPTED__ = False

    class AnsibleVault(str):
        __UNSAFE__ = False
        __ENCRYPTED__ = True

    # test str types
    assert encoder.default

# Generated at 2022-06-12 23:15:41.510269
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Checking for basic functionality
    sample_str = "This is sample str"
    encoder = AnsibleJSONEncoder()
    assert encoder.default(sample_str) == sample_str

    # Checking behavior for AnsibleUnsafe
    sample_unsafe = ansible.module_utils.basic.AnsibleUnsafe(sample_str)
    assert encoder.default(sample_unsafe) == sample_str
    assert isinstance(encoder.default(sample_unsafe), six.string_types)
    # Checking behavior for AnsibleVaultEncryptedUnicode
    sample_vault = ansible.module_utils.basic.AnsibleVaultEncryptedUnicode(sample_str)
    assert encoder.default(sample_vault) == {'__ansible_vault': sample_str}

# Generated at 2022-06-12 23:15:48.515965
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:15:53.655118
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Here are the object cases we need to test:
    # * AnsibleVaultEncryptedUnicode
    # * AnsibleVaultEncryptedBytes
    # * AnsibleUnsafeBytes
    # * AnsibleUnsafeText
    # * date objects
    # * hostvars and other objects
    # * All other objects (will use the default json encoder)

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import AnsibleVaultEncryptedBytes
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    vault_lib = VaultLib('password')
    vault_obj_text = Ans

# Generated at 2022-06-12 23:16:31.508810
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import HashableDict
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import text_type

    dt = datetime.datetime(year=2015, month=6, day=1, hour=22, minute=55, second=0)
    assert AnsibleJSONEncoder().default(dt) == dt.isoformat()

    assert AnsibleJSONEncoder().default(VaultLib([VaultSecret('foo')], 'password')) == {'__ansible_vault': 'foo'}

