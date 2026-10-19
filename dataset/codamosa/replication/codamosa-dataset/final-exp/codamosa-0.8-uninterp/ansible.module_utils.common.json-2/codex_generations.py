

# Generated at 2022-06-12 23:06:38.841540
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # check proper encoding of datetime object
    ansible_date_time = datetime.datetime(2017, 6, 8, 14, 28, 8)
    assert AnsibleJSONEncoder().default(ansible_date_time) == '2017-06-08T14:28:08'


# Generated at 2022-06-12 23:06:45.381946
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_encoder = AnsibleJSONEncoder()
    assert test_encoder.default(1) == 1
    assert test_encoder.default("string") == "string"
    assert test_encoder.default(["list"]) == ["list"]
    assert test_encoder.default({"key": "val"}) == {"key": "val"}
    assert test_encoder.default(dict(o=1)) == {"o": 1}
    assert test_encoder.default(dict(o="val")) == {"o": "val"}

# Generated at 2022-06-12 23:06:52.704298
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert to_text(json.dumps(object(), cls=AnsibleJSONEncoder)) == u'{}'
    assert to_text(json.dumps(type("", (object, ), {'__ENCRYPTED__': True})(), cls=AnsibleJSONEncoder)) == u'{}'
    assert to_text(json.dumps(type("", (object, ), {'__UNSAFE__': True})(), cls=AnsibleJSONEncoder)) == u'{}'
    assert to_text(json.dumps(type("", (object, ), {'__UNSAFE__': True, '__ENCRYPTED__': True})(), cls=AnsibleJSONEncoder)) == u'{}'

# Generated at 2022-06-12 23:07:03.565314
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    ansible_json_encoder = AnsibleJSONEncoder()

    unsafe_object = AnsibleUnsafe('test_ansible_unsafe')
    vault_object = VaultLib([('vault_password', 'ansible_vault')])
    enc_vault_text = vault_object.encrypt('test_ansible_vault')
    vault_object = VaultLib([('vault_password', 'ansible_vault')])

    assert ansible_json_encoder.default(unsafe_object) == {'__ansible_unsafe': 'test_ansible_unsafe'}

# Generated at 2022-06-12 23:07:10.505792
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_text
    # test str subclass
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(to_text(r'\r\n')) == '\\\\r\\\\n'
    # test unsafe object
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(to_text(r'\r\n\t', errors='surrogate_or_strict')) == {"__ansible_unsafe": '\\\\r\\\\n\\\\t'}

# Generated at 2022-06-12 23:07:18.992392
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    # test vault object
    # -----------------------------------------------------------------------------------------
    # input parameter
    test_vault_data = VaultLib(['']*1, '1234')
    # expected:
    # should return a dict
    # key: __ansible_vault
    # value: ciphertext of the vault object
    assert isinstance(AnsibleJSONEncoder().default(test_vault_data), dict)

# Generated at 2022-06-12 23:07:24.788892
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    input = {'foo': AnsibleUnsafe('password'), 'bar': {'baz': AnsibleUnsafe('password')}}
    result = AnsibleJSONEncoder(preprocess_unsafe=False).encode(input)
    assert result == '{"foo": {"__ansible_unsafe": "password"}, "bar": {"baz": {"__ansible_unsafe": "password"}}}'


# Generated at 2022-06-12 23:07:35.121840
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    my_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False, skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, sort_keys=True, indent=0, separators=None, encoding='utf-8', default=None)

    class TestClass(object):
        def __init__(self, name):
            self.name = name

    my_class = TestClass('foo')
    assert my_encoder.default(my_class) == {'name': 'foo'}

    my_datetime = datetime.datetime(2017, 11, 23, 0, 0)
    assert my_encoder.default(my_datetime) == '2017-11-23T00:00:00'


# Generated at 2022-06-12 23:07:42.409734
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.encoders import to_bytes, to_text
    from ansible.parsing.vault import VaultLib, VaultSecret

# Generated at 2022-06-12 23:07:53.658381
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    dict_param = {"one": 'one', "two": 2}
    unsafe_param = AnsibleUnsafeText('This is unsafe!')
    unsafe_param.__UNSAFE__ = True
    vault_param = AnsibleVaultEncryptedUnicode('vault_param')
    vault_param.__ENCRYPTED__ = True
    date_param = datetime.date(2017, 12, 12)

    assert json.loads(json.dumps(dict_param, cls=AnsibleJSONEncoder)) == dict_param
    assert json.loads(json.dumps(unsafe_param, cls=AnsibleJSONEncoder)) == {'__ansible_unsafe': unsafe_param}

# Generated at 2022-06-12 23:08:03.916329
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    utc_time = datetime.datetime.utcnow()
    json_object = {
        'date': utc_time,
        'bool': True,
        'list': [
            utc_time,
            { 'key': 'value' }
        ]
    }

    encoder = AnsibleJSONEncoder()
    result = encoder.default(json_object)
    assert result['date'] == utc_time.isoformat()
    assert result['bool'] == True
    assert type(result['list']) == list
    assert result['list'][0] == utc_time.isoformat()
    assert type(result['list'][1]) == dict
    assert result['list'][1]['key'] == 'value'

# Generated at 2022-06-12 23:08:14.524663
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib("password", b"hello")
    myvault = vault.encrypt("hello")
    myvault.vault_write_header("myvault")

    myvault_plain = to_text(myvault, errors='surrogate_or_strict')

    json_str = json.dumps({'ansible_vault': myvault},
                          cls=AnsibleJSONEncoder,
                          vault_to_text=True)
    assert '"ansible_vault": "hello"' in json_str
    json_str = json.dumps({'ansible_vault': myvault},
                          cls=AnsibleJSONEncoder,
                          vault_to_text=False)

# Generated at 2022-06-12 23:08:19.225132
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default([b'bytes', 'str']) == ['bytes', 'str']
    assert encoder.default(b'bytes') == 'bytes'
    assert encoder.default(u'str') == 'str'

# Unit tests for method iterencode of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:08:27.272238
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils.six import binary_type

    # empty data structure
    assert AnsibleJSONEncoder().default({}) == {}
    assert AnsibleJSONEncoder().default([]) == []

    # internal ansible types
    # - generic mapping
    assert AnsibleJSONEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    # - datetime
    assert AnsibleJSONEncoder().default(datetime.date(2013, 6, 17)) == '2013-06-17'
    # - datetime with timezone

# Generated at 2022-06-12 23:08:31.231047
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    orig_dict = {1: 'a', 2: 'b'}
    new_dict = {u'1': u'a', u'2': u'b'}
    assert encoder.default(orig_dict) == new_dict

# Generated at 2022-06-12 23:08:37.749563
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types

    vault_lib = VaultLib([])
    vault_text = 'foo'
    vault_password = 'bar'
    vault_obj = vault_lib.encrypt(vault_text, vault_password)

    assert AnsibleJSONEncoder(vault_to_text=True).default(vault_obj) == vault_text
    assert isinstance(AnsibleJSONEncoder(vault_to_text=False).default(vault_obj), string_types)

    assert AnsibleJSONEncoder().default(vault_obj) == vault_obj

# Generated at 2022-06-12 23:08:48.019703
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import os
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe


# Generated at 2022-06-12 23:08:57.259885
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    import datetime
    encoder = AnsibleJSONEncoder()
    # test datetime
    now = datetime.datetime.now()
    assert encoder.default(now) == now.isoformat()
    # test vault value
    vault = ansible.parsing.vault.VaultLib('test')
    assert encoder.default(vault.encrypt('test')) == {'__ansible_vault': vault._ciphertext}
    # test vault value to text
    vault_to_text = AnsibleJSONEncoder(vault_to_text=True)
    assert vault_to_text.default(vault.encrypt('test')) == vault._text



# Generated at 2022-06-12 23:09:07.331805
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for AnsibleJSONEncoder.default()"""
    import datetime
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.utils.unsafe_proxy import wrap_var
    encoded = '2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b'
    vault_obj_normal = AnsibleUnsafe(encoded)
    vault_obj_single_quotes = AnsibleUnsafe("'" + encoded + "'")

# Generated at 2022-06-12 23:09:18.151095
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test default
    class Person:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
    encoder = AnsibleJSONEncoder()
    d = Person('Guido', 'van Rossum')
    assert {'first_name': 'Guido', 'last_name': 'van Rossum'} == encoder.default(d)

    # Test if '__ENCRYPTED__' exists in the object, then return key '__ansible_vault' and its value
    from ansible.parsing.vault import VaultEditor
    vault_editor = VaultEditor(b'ansible')
    d = vault_editor.encrypt_text(b'xixi')

# Generated at 2022-06-12 23:09:31.177144
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types
    import datetime
    import json

    vault_pass = 'my_password'
    vault_cipher = 'aes256'
    vault_dir = '~/.ansible/vault'
    vault = VaultLib(vault_pass, vault_dir, vault_cipher)

    encrypted_text = vault.encrypt('my_s3cr3t')

    enc = AnsibleJSONEncoder()
    assert '__ansible_vault' in json.loads(enc.encode(encrypted_text))
    assert isinstance(json.loads(enc.encode(encrypted_text))['__ansible_vault'], string_types)


# Generated at 2022-06-12 23:09:39.334447
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('test string') == 'test string'
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'a': 'test string'}) == {'a': 'test string'}
    class MyClass(object):
        pass
    instance = MyClass()
    instance.test = 'test string'
    assert encoder.default(instance) == {'test': 'test string'}
    assert encoder.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()

# Generated at 2022-06-12 23:09:48.596357
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible_collections.ansible.community.plugins.module_utils.common.text.converters import to_bytes, to_text

    encoded_vault = AnsibleJSONEncoder(indent=2, sort_keys=True).default(to_bytes('$ANSIBLE_VAULT;1.2;AES256;myhost\r\ndatahere\r\n'))
    assert encoded_vault == {"__ansible_vault": "ZC5BTlNJQkxFX1ZBVUxUOzEuMjtBRVMyNTY7bXlob3N0CmRhdGFoZXJlCg==\n"}


# Generated at 2022-06-12 23:09:57.075459
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()

    from ansible.parsing.vault import VaultLib
    vault_password = 'mypassword'
    vault_id = 'myvaultid'
    vault_obj = VaultLib(vault_password, vault_id)
    encrypted_json = vault_obj.encode(json.dumps({'key': 'value'}))
    assert ansible_json_encoder.default(encrypted_json) == {'__ansible_vault': encrypted_json}

    # NOTE: unsafe class is defined in test_encryption_filter
    unsafe_str = unsafe('mypassword')
    assert ansible_json_encoder.default(unsafe_str) == {'__ansible_unsafe': to_text(unsafe_str)}

    # Date
    import dat

# Generated at 2022-06-12 23:10:04.535351
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six import text_type
    from ansible.parsing.vault import VaultLib

    vault_password = 'secret_vault_password'
    vault_cipher_text = '$ANSIBLE_VAULT;1.1;AES256;Ansible;9d1d17f1a6a5e6f5e6c5d5a1c99dc5a1\n766b3535326b3365330b343765316531650a6466316565643139363864316335\n31643262643362366235353430383164323831323334362e0a'

    o = 'test string'
    json_encoder = AnsibleJSONEncoder()
    encoded_

# Generated at 2022-06-12 23:10:13.698369
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.constants as C

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import b

    data = [{'__ansible_vault': 'vault', '__ansible_unsafe': 'unsafe'},
            {'__ansible_vault': 'vault', '__ansible_unsafe': 'unsafe'},
            b('vault'), b('unsafe')]

# Generated at 2022-06-12 23:10:18.850580
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode({'a': 'unsafe'}) == '{"a": "unsafe"}'

    assert AnsibleJSONEncoder().encode({'a': datetime.date.today()}) == '{"a": "%s"}' % datetime.date.today().isoformat()

# Generated at 2022-06-12 23:10:28.339368
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six.moves import StringIO
    from ansible.parsing.dataloader import DataLoader

    data = DataLoader()
    stream = StringIO()
    value = dict(
        vault=data.load_from_file('.vault_pass.99', vault_password='test'),
        unsafe=data.mark_unsafe('{ "key": "value" }'),
        date=datetime.datetime.now(),
        hostvars=data.get_basedir(),
    )
    json.dump(value, stream, cls=AnsibleJSONEncoder, indent=4, sort_keys=True)
    # Test output of test_AnsibleJSONEncoder_default()

# Generated at 2022-06-12 23:10:37.993533
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:10:47.561846
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This method is used by AnsibleModule._ansible_filter_json
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.ansible_utils import AnsibleUnsafe
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.ansible_utils import AnsibleVaultEncryptedUnicode
    import datetime
    encoder = AnsibleJSONEncoder()
    assert encoder.default('test') == 'test'
    assert encoder.default(AnsibleUnsafe('test')) == {'__ansible_unsafe': u'test'}
    
    # NOTE: Backported from ansible-base master to support AnsibleModule._ansible_filter_json

# Generated at 2022-06-12 23:10:55.512246
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder(indent=4)

    class Foo(object):
        def __init__(self, msg):
            self.msg = msg

    foo = Foo('hello world')

    # serialize Foo to json
    foo_json = json_encoder.default(foo)

    assert foo_json['msg'] == 'hello world'



# Generated at 2022-06-12 23:11:03.699093
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # test vault object
    # output should be a dict with key __ansible_vault and value be to_text(o._ciphertext)
    from ansible.parsing.vault import VaultLib
    vault_pass = 'test'
    vault_obj = VaultLib(password=vault_pass)
    value = vault_obj.encrypt('hello world!')
    result = AnsibleJSONEncoder().default(value)

# Generated at 2022-06-12 23:11:13.642758
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('foo') == 'foo'

    assert encoder.default(datetime.date(year=2019, month=1, day=1)) == '2019-01-01'
    assert encoder.default(datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0)) == '2019-01-01T00:00:00'

    assert encoder.default({}) == {}

    class obj(object):
        def __init__(self):
            pass

        def __repr__(self):
            return '<obj>'

    assert encoder.default(obj()) == '<obj>'

    import ansible.parsing.vault as vault


# Generated at 2022-06-12 23:11:22.761716
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test the string
    test_string = 'test_string'
    result = AnsibleJSONEncoder().default(test_string)
    assert result == test_string, "Encoded string does not match original"
    
    # Test the bool
    test_bool = True
    result = AnsibleJSONEncoder().default(test_bool)
    assert result == test_bool, "Encoded bool does not match original"
    
    # Test the list
    test_list = [1,2,3]
    result = AnsibleJSONEncoder().default(test_list)
    assert result == test_list, "Encoded list does not match original"
    


# Generated at 2022-06-12 23:11:32.202219
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Unsafe(str):
        __UNSAFE__ = True

    class Safe(str):
        __UNSAFE__ = False

    class Vault(Safe):
        __ENCRYPTED__ = True

    encoder = AnsibleJSONEncoder()
    value = Unsafe(u'unsafe')
    output = encoder.default(value)
    assert output == {'__ansible_unsafe': u'unsafe'}

    value = Safe(u'safe')
    output = encoder.default(value)
    assert output == u'safe'

    value = Vault(u'vault')
    output = encoder.default(value)
    assert output == {'__ansible_vault': u'vault'}


# Generated at 2022-06-12 23:11:39.147052
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY2

    vault_text = '$ANSIBLE_VAULT;1.1;AES256'
    vault_password = 'mypassword'
    vault_obj = VaultLib(vault_password)

    # Test for vault json
    if PY2:
        vault_encrypted = vault_obj.encode(vault_text.encode('utf-8'))
    else:
        vault_encrypted = vault_obj.encode(vault_text)
    vault_decrypted = vault_obj.decode(vault_encrypted)

    encoder = AnsibleJSONEncoder(vault_to_text=True)
    json_decrypted = encoder.default(vault_decrypted)
    json_encrypted

# Generated at 2022-06-12 23:11:46.807737
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    values = [
        ["value1", "value2"],
        {"key1": "value1", "key2": "value2"},
        {"__ansible_unsafe": "value1", "key2": "value2"},
        {"__ansible_vault": "value1", "key2": "value2"},
        {"__ansible_vault": "value1", "__ansible_unsafe": "value2"},
        {"__ansible_vault": "value1", "__ansible_unsafe": "value2", "key3": "value3"}
    ]
    for value in values:
        data = AnsibleJSONEncoder().default(value)
        assert json.dumps(value, cls=AnsibleJSONEncoder) == json.dumps(data, cls=AnsibleJSONEncoder)


# Generated at 2022-06-12 23:11:56.601253
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from datetime import datetime

    # Date objects should be returned in ISO format and the default method should be used for the others
    assert AnsibleJSONEncoder().default(datetime(2017, 1, 1)) == '2017-01-01T00:00:00'
    assert AnsibleJSONEncoder().default({'name': 'Alex'}) == {"name": "Alex"}
    assert AnsibleJSONEncoder().default(AnsibleUnsafe('unsafe value')) == {"__ansible_unsafe": "unsafe value"}

    # Check the vault object with vault_to_text set to False by default

# Generated at 2022-06-12 23:12:03.187269
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()

    # Test None
    assert None == ansible_json_encoder.default(None)

    # Test dict
    dict_test = dict(test_dict = 'test_dict')
    assert dict_test == ansible_json_encoder.default(dict_test)

    # Test datetime.date
    date_test = datetime.date.today()
    assert date_test.isoformat() == ansible_json_encoder.default(date_test)

    # Test datetime.datetime
    datetime_test = datetime.datetime.now()
    assert datetime_test.isoformat() == ansible_json_encoder.default(datetime_test)

# Generated at 2022-06-12 23:12:11.622281
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.converters import to_bytes_or_unicode

    # test when __ENCRYPTED__ and vault_to_text both True
    vault_to_text = True
    encoder = AnsibleJSONEncoder(vault_to_text=vault_to_text)
    vault_obj = VaultLib()
    o = vault_obj.encrypt(to_bytes('string'))
    expected_value = to_text(o, errors='surrogate_or_strict')
    assert encoder.default(o) == expected

# Generated at 2022-06-12 23:12:29.349068
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Setup
    j = AnsibleJSONEncoder()

    # Test with dates/datetimes
    assert j.default(datetime.date(year=1992, month=2, day=29)) == "1992-02-29"
    assert j.default(datetime.datetime(year=1992, month=2, day=29, hour=2, minute=2, second=2)) == "1992-02-29T02:02:02"

    # Test with dicts
    assert j.default({'a': 'b'}) == {'a': 'b'}

    # Test with unknown types
    class TestClass(object):
        pass
    assert j.default(TestClass()) == {}

    # Test with AnsibleUnsafe
    from ansible.module_utils.urls import AnsibleUnsafe

# Generated at 2022-06-12 23:12:39.836288
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)

# Generated at 2022-06-12 23:12:47.591203
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import __builtin__
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.unsafe_proxy import AnsibleUnsafeBytes
    import datetime

    ansibleencoder = AnsibleJSONEncoder()
    assert ansibleencoder.default(None) is None
    assert ansibleencoder.default(False) is False
    assert ansibleencoder.default(True) is True
    assert ansibleencoder.default(list()) is list()
    assert ansibleencoder.default(dict()) is dict()
    assert ansibleencoder.default(set()) == set()
    assert ansibleencoder.default('str') == 'str'

# Generated at 2022-06-12 23:12:57.273437
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes

    def assert_equal(actual, expected):
        assert actual == expected, 'expected %r, actual %r' % (expected, actual)

    encoder = AnsibleJSONEncoder()

    # vault object
    assert_equal(encoder.default(create_vault('some_password', 'some_variable', 'value')),
                 {'__ansible_vault': to_bytes('some_variable=value')})

    # unsafe object
    assert_equal(encoder.default(create_unsafe('value')),
                 {'__ansible_unsafe': to_bytes('value')})

    # hostvars
    assert_equal(encoder.default(dict(a=1, b=2)), dict(a=1, b=2))

# Generated at 2022-06-12 23:13:03.902448
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(2.5) == 2.5
    assert AnsibleJSONEncoder().default('string') == 'string'

    import datetime
    date = datetime.datetime(
        year=2020, month=10, day=29, hour=16, minute=33, second=10, microsecond=111)
    assert AnsibleJSONEncoder().default(date) == '2020-10-29T16:33:10.000111'

    from ansible.module_utils.six import PY3
    import os
    import sys

    # 2.6 and 2.7 use dict and set objects instead of Mapping and Sequence

# Generated at 2022-06-12 23:13:09.537314
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj= 'This is a string object'
    encoder = AnsibleJSONEncoder()
    assert encoder.default(obj) == 'This is a string object'
    assert encoder.default(obj) == 'This is a string object'
    repr(encoder.default(obj)) == "'This is a string object'"
    obj = 'test'
    assert encoder.default(obj) == 'test'

# Generated at 2022-06-12 23:13:18.178412
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test for vault object
    ansible_vault = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=False)
    test_vault = {'__ansible_vault': to_text(b'\xd1\x1a(\xce\x9f\x8b\x90J\xaf\xa3\xf3\xb2\x9b\x8c\x0f\x1c\r\xe7\x04\xbc', errors='surrogate_or_strict')}

# Generated at 2022-06-12 23:13:29.106503
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test case:
    #   - Test the default method.
    #   - Expected result:
    #       - Encoder can handle objects of Ansible internal type correctly
    #       - Encoder can handle other types correctly
    # Procedure:
    #   - Call default with nb types of objects
    #   - Compare the result with expected value

    # Case 1: hostvars
    hostvars_content = {'key1': 'value1', 'key2': {'key_inner': 'value_inner'}}
    hostvars_encoder = AnsibleJSONEncoder().default(hostvars_content)
    assert hostvars_content == hostvars_encoder

    # Case 2: datetime
    datetime_content = datetime.datetime(2019, 1, 1, 1, 0, 0, 0)
    dat

# Generated at 2022-06-12 23:13:38.361003
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:13:39.418325
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(b'foo') == 'foo'

# Generated at 2022-06-12 23:13:57.151894
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import io
    import os
    import sys
    test_ansible_unsafe = "test_ansible_unsafe"
    test_ansible_unsafe_obj = AnsibleUnsafe(test_ansible_unsafe)

    # notebook testing
    if os.environ.get('TRAVIS_CI'):
        # fix for notebooks
        json.dump(test_ansible_unsafe_obj, sys.stdout)
        return

    # stdout testing
    old_stdout = sys.stdout
    sys.stdout = ansible_json_encoder_stdout = io.StringIO()
    json.dump(test_ansible_unsafe_obj, sys.stdout)
    assert '"__ansible_unsafe": "test_ansible_unsafe"' in ansible_json_encoder_std

# Generated at 2022-06-12 23:14:04.558615
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultPassword
    from ansible.module_utils.six import string_types
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    import datetime

    def test(value):
        encoded = json.dumps(value, cls=AnsibleJSONEncoder)
        return json.loads(encoded)

    # vault object
    assert test(AnsibleUnsafe('baz')) == {'__ansible_vault': 'baz'}

    # unsafe object
    assert test(AnsibleUnsafe('foo')) == {'__ansible_unsafe': 'foo'}

    # hostvars and other objects
    # TODO: is this really intended behavior?

# Generated at 2022-06-12 23:14:15.236217
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import StringIO
    import collections

    class TestClass(object):
        pass

    class TestClassUnsafe(object):
        __UNSAFE__ = True

    class TestClassEncrypted(object):
        __ENCRYPTED__ = True

    encoder = AnsibleJSONEncoder()
    assert encoder.default(None) == 'null'
    assert encoder.default(True) == 'true'
    assert encoder.default(False) == 'false'
    assert encoder.default(123) == '123'
    assert encoder.default(123.456) == '123.456'
    assert encoder.default(TestClass()) == '{}'

# Generated at 2022-06-12 23:14:17.704793
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ''' test_AnsibleJSONEncoder_default: Test for method default'''
    assert isinstance(AnsibleJSONEncoder().default(Mapping()), dict)

# Generated at 2022-06-12 23:14:24.731092
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test if function ``default`` of class ``AnsibleJSONEncoder`` works properly

    In order to test this function of class, we create a bunch of objects
    and check if they were properly encoded.
    """
    from ansible.module_utils.common import date_time
    from ansible.parsing.vault import VaultLib

    # Create unsafes, vault, date and hostvars
    unsafe = date_time.AnsibleUnsafe(u'secret')
    vault = VaultLib([])
    vault._ciphertext = 'cipher'
    today = datetime.datetime.today()
    hostvars = {'a': 1}

    # Create instance of class AnsibleJSONEncoder
    ansible_json_encoder = AnsibleJSONEncoder()
    ansible_json_encoder_vault_

# Generated at 2022-06-12 23:14:34.445500
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:14:41.438016
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    assert encoder.default('unsafe') == 'unsafe'
    assert '__ansible_unsafe' not in encoder.default('unsafe')
    assert encoder.default(['unsafe']) == ['unsafe']
    assert '__ansible_unsafe' not in encoder.default(['unsafe'])
    assert encoder.default({'unsafe': 'unsafe'}) == {'unsafe': 'unsafe'}
    assert '__ansible_unsafe' not in encoder.default({'unsafe': 'unsafe'})
    assert encoder.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()

# Generated at 2022-06-12 23:14:51.660396
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()

    # test for getattr(o, '__ENCRYPTED__', False)
    from ansible.parsing.vault import VaultLib
    vault_string = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          353537326237376133613762326638343633623239626262616336376539643163376364636662663236612\n          3616136633433383032626532630a373462366636313561663436363061363435613062313430323134623963\n          66643830633633306662333561653266623338656364633136613238653161\n          0a"
    vault_

# Generated at 2022-06-12 23:15:01.802143
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types

    enc = AnsibleJSONEncoder()
    def is_string(s):
        return isinstance(s, string_types)

    assert is_string(enc.default(datetime.datetime.now()))
    assert is_string(enc.default(datetime.date.today()))
    assert isinstance(enc.default({'k': 'v'}), dict)
    assert isinstance(enc.default(dict(k='v')), dict)
    assert isinstance(enc.default([1, 2, 3]), list)
    assert isinstance(enc.default(VaultLib(b'\x00' * 16)), dict)

# Generated at 2022-06-12 23:15:09.199323
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps(True, cls=AnsibleJSONEncoder)) is True
    assert json.loads(json.dumps(1, cls=AnsibleJSONEncoder)) == 1
    assert json.loads(json.dumps('a', cls=AnsibleJSONEncoder)) == 'a'
    assert json.loads(json.dumps({'a': 1}, cls=AnsibleJSONEncoder)) == {'a': 1}
    assert json.loads(json.dumps(['a', 1], cls=AnsibleJSONEncoder)) == ['a', 1]

    # binary value
    binary_value = u'\u00e9'.encode('utf-8')

# Generated at 2022-06-12 23:15:35.335874
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils import basic
    from ansible.module_utils.six import binary_type

    assert AnsibleJSONEncoder().default(basic.AnsibleModule(
        argument_spec={},
    )) == {'_ansible_module': True}

    assert AnsibleJSONEncoder().default(basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )) == {'_ansible_module': True, "supports_check_mode": True}


# Generated at 2022-06-12 23:15:44.682944
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes

    assert AnsibleJSONEncoder().default(AnsibleUnsafeText(b'some bytes', nonstring='passthru')) == b'some bytes'
    assert AnsibleJSONEncoder().default(AnsibleUnsafeText(u'unicode', encoding='ascii')) == u'unicode'
    assert AnsibleJSONEncoder().default(AnsibleUnsafeBytes(b'some bytes', nonstring='passthru', encoding='utf-8')) == b'some bytes'

# Generated at 2022-06-12 23:15:50.509125
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import text_type

    # vault object

# Generated at 2022-06-12 23:16:00.165727
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    class unsafe(unicode):
        __UNSAFE__ = True

    class unsafe_instance(unicode):
        __UNSAFE__ = True
        __ENCRYPTED__ = True

    class mapping(Mapping):
        pass

    class datetime_instance(datetime.datetime):
        pass

    class date_instance(datetime.date):
        pass

    class unknown():
        pass

    encoder = AnsibleJSONEncoder()

    assert encoder.default(unsafe('test')) == {'__ansible_unsafe': 'test'}
    assert encoder.default(unsafe_instance('test')) == {'__ansible_vault': 'test'}

# Generated at 2022-06-12 23:16:08.400904
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder().default(['a', 2]) == ['a', 2]
    class Foo(object):
        def __init__(self):
            self.a = 'A'
            self.b = 'B'
    assert AnsibleJSONEncoder().default(Foo()) == dict(a='A', b='B')
    assert AnsibleJSONEncoder().default(datetime.datetime(2000, 1, 1, 12, 0, 0)) == '2000-01-01T12:00:00'
    assert AnsibleJSONEncoder().default(datetime.date(2000, 1, 1)) == '2000-01-01'

# Generated at 2022-06-12 23:16:15.147287
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test Vault
    # ---------------------

    vault = '$ANSIBLE_VAULT;1.2;AES256;ansible\r\n3331613831333134313461646636323665363065343833383332390a386132643039356663326636\r\n38303133333336366435303364336563646534306132363162610a3864643661623963346536376566\r\n38363866653339373330353737363835646137633239633832620a38303766343633627d4d4b2e4451\r\n6a513d485444444a4f4e41\r\n'

# Generated at 2022-06-12 23:16:22.175588
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    o = AnsibleUnsafe('$ANSIBLE_VAULT;1.2;AES256;foobar\n373534373536656273376537333666646362326539653264343733366638393166626239336664\n326438363830356539663762372b79493d')
    ansible_json_encoder = AnsibleJSONEncoder()
    result = ansible_json_encoder.default(o)
    assert '__ansible_unsafe' in result
    # assert result['__ansible_unsafe'] == '$ANSIBLE_VAULT;1.2;AES256;foobar\n373534373536656

# Generated at 2022-06-12 23:16:31.149301
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    test_vault = 'user_pass'
    test_vault_unsafe = 'user_pass_unsafe'
    test_json_vault = '{"__ansible_vault": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}'
    test_unsafe = AnsibleUnsafe('my_password')
    test_vault_obj = AnsibleVaultEncryptedUnsafeText(test_vault)
    test_ansible_unsafe_obj = AnsibleUnsafe(test_vault_unsafe)
    test_json_ansible_unsafe_obj = '{"__ansible_unsafe": "user_pass_unsafe"}'

    encoder = AnsibleJSONEncoder()
    value = encoder.default(test_vault_obj)
    assert value == test_vault


# Generated at 2022-06-12 23:16:38.186655
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    import pytest
    import time
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    from ansible.vars.unsafe_proxy import AnsibleVaultEncryptedUnsafeText

    encoder = AnsibleJSONEncoder()
    expected = json.dumps({"__ansible_vault": "Encrypted"}, ensure_ascii=True)
    actual = json.dumps(AnsibleVaultEncryptedUnsafeText("Encrypted"), cls=encoder, ensure_ascii=True)
    assert expected == actual

    expected = '"{\\"__ansible_unsafe\\": \\"ascii\\"}"'
    actual = json.dumps(AnsibleUnsafe("ascii"), cls=encoder, ensure_ascii=True)
    assert expected