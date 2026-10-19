

# Generated at 2022-06-12 23:06:47.110182
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # prepare for test
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import is_encrypted

    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    vault_password = 'cubswin:)!'
    desc = 'Test Vault Lib'

    plain_text = "This is a plain text for Ansible JSON Encoder test"

    vault_text = VaultLib(vault_password, desc).encrypt(plain_text)

    is_enc = is_encrypted(vault_text)

    assert is_enc

    assert is_encrypted(AnsibleUnsafe(b'unsafe string')) == False


# Generated at 2022-06-12 23:06:48.503877
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert isinstance(AnsibleJSONEncoder().encode({"key": "value"}), str)



# Generated at 2022-06-12 23:06:58.986796
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    safe_text = AnsibleUnsafeText(u'The "foo" is "bar"')
    unsafe_text = AnsibleUnsafeText(u'The "foo" is "bar"', unsafe=True)
    vault = AnsibleVaultEncryptedUnicode("Foo", "The foo is bar")
    d1 = {"foo": unsafe_text, "bar": safe_text, "vault": vault}

    # AnsibleUnsafeText
    data = AnsibleJSONEncoder().encode(safe_text)
    assert data == u'"The \\"foo\\" is \\"bar\\""'
    data = AnsibleJSONEncoder(vault_to_text=True).encode(safe_text)
    assert data == u'"The \\"foo\\" is \\"bar\\""'

    # unsafe AnsibleUnsafeText
   

# Generated at 2022-06-12 23:07:05.572606
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()

    # Unsafe object
    assert encoder.default(AnsibleUnsafe('<html></html>')) == {'__ansible_unsafe': '<html></html>'}

    # Mapping
    assert encoder.default({'a': 'b'}) == {'a': 'b'}

    # Date
    assert encoder.default(datetime.date(2020, 1, 2)) == '2020-01-02'
    assert encoder.default(datetime.datetime(2020, 1, 2, 3, 4, 5, 6)) == '2020-01-02T03:04:05.000006'

    # Subclass of Mapping
    class MyDict(dict):
        pass



# Generated at 2022-06-12 23:07:07.328375
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default(False) == False

# Generated at 2022-06-12 23:07:16.955558
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(None) is None
    assert ansible_json_encoder.default(True) is True
    assert ansible_json_encoder.default(False) is False

    assert ansible_json_encoder.default(0) == 0
    assert ansible_json_encoder.default(1) == 1
    assert ansible_json_encoder.default(1.1) == 1.1

    assert ansible_json_encoder.default('test') == 'test'
    assert ansible_json_encoder.default(u'test') == 'test'

    assert ansible_json_encoder.default([1, u'2', 3]) == [1, '2', 3]
    assert ansible_json_

# Generated at 2022-06-12 23:07:28.139075
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test the method default of class AnsibleJSONEncoder for specific types."""
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)

    # Test the conversion of a datetime object to a string
    timestamp = datetime.datetime.now()
    encoded_timestamp = encoder.default(timestamp)
    assert(timestamp.isoformat() == encoded_timestamp)

    # Test the conversion of a vault object to a dict
    # In this case we want the conversion to a dict to occur
    vault = '$ANSIBLE_VAULT;1.1;AES256;admin;asdfgh1234567890\nasdfgh1234567890\nasdfgh1234567890\nasdfgh1234567890\n'
    vault_obj = AnsibleUnsafeText(vault, vault=True)
   

# Generated at 2022-06-12 23:07:36.633452
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class Foo:
        pass
    # This class doesn't have '__UNSAFE__' and '__ENCRYPTED__'
    # It should use default method of super class
    foo = Foo()
    d = AnsibleJSONEncoder().default(foo)
    assert d == foo
    # This class has '__UNSAFE__', but not '__ENCRYPTED__'
    # It should return the following value
    class Unsafe:
        __UNSAFE__ = True
    unsafe = Unsafe()
    d = AnsibleJSONEncoder().default(unsafe)
    assert d == {'__ansible_unsafe': to_text(unsafe, errors='surrogate_or_strict', nonstring='strict')}
    # This class has '__ENCRYPTED__', but not '__UNSA

# Generated at 2022-06-12 23:07:42.269432
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import text_type

    encoder = AnsibleJSONEncoder()

    assert encoder.default(text_type('test_string')) == 'test_string'
    assert encoder.default(1) == 1
    assert encoder.default({}) == {}
    assert encoder.default({'key': 'value'}) == {'key': 'value'}
    assert encoder.default(['value']) == ['value']
    assert encoder.default([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-12 23:07:53.607930
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test the method default of AnsibleJSONEncoder
    '''

    # Define the expected results

# Generated at 2022-06-12 23:07:59.610350
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Myjson(json.JSONEncoder):
        def default(self, o):
            return {'TEST': 'TEST'}
    obj = Myjson()
    assert obj.default('TEST') == {'TEST': 'TEST'}



# Generated at 2022-06-12 23:08:04.883942
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert AnsibleJSONEncoder().encode("foo") == '"foo"'
    assert AnsibleJSONEncoder().encode("f\noo") == '"f\\noo"'

    class C:
        pass
    assert AnsibleJSONEncoder().encode(C()) == '{}'

    class D:
        def __init__(self):
            self.__dict__ = dict(a=1, b=2)
    assert AnsibleJSONEncoder().encode(D()) == '{"a": 1, "b": 2}'

    class D2(D):
        def __init__(self):
            super(D2, self).__init__()
            self.__dict__.update(dict(c=3))

# Generated at 2022-06-12 23:08:15.353609
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(False) == False
    assert encoder.default(0) == 0
    assert encoder.default(0.1) == 0.1
    assert encoder.default([]) == []
    assert encoder.default(()) == ()
    assert encoder.default({}) == {}
    assert encoder.default('') == ''
    assert encoder.default(u'') == u''
    assert encoder.default(None) == None
    assert encoder.default('0') == '0'
    assert encoder.default(u'0') == u'0'
    assert encoder.default('1') == '1'
    assert encoder.default(u'1') == u'1'
    assert encoder.default('-1') == '-1'

# Generated at 2022-06-12 23:08:18.040984
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps({'a': 'b'}, cls=AnsibleJSONEncoder)) == {'a': 'b'}


# Generated at 2022-06-12 23:08:25.405380
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    default_encoder = AnsibleJSONEncoder().default
    assert default_encoder(u'unsafe') == u'unsafe'
    assert default_encoder(u'vault') == u'vault'
    assert default_encoder({u'foo': u'bar'}) == {u'foo': u'bar'}
    assert default_encoder({u'foo': u'unsafe'}) == {u'foo': u'unsafe'}
    assert default_encoder({u'foo': u'vault'}) == {u'foo': u'vault'}


# Unit tests for method _preprocess_unsafe_encode

# Generated at 2022-06-12 23:08:35.198126
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default({'a': 1, 'b': [2, 3], 'c': {'d': 4}}) == {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    assert AnsibleJSONEncoder().default({'a': 1, 'b': [2, 3], 'c': {'d': 4}}) != {'a': 1, 'b': [2, 3], 'c': {'e': 4}}
    assert AnsibleJSONEncoder().default({'a': 1, 'b': [2, 3], 'c': {'d': 4}}) != {'a': 1, 'b': [2, 3], 'c': {'d': 5}}

# Generated at 2022-06-12 23:08:35.815310
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    pass

# Generated at 2022-06-12 23:08:45.855635
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """ This tests that AnsibleJSONEncoder correctly encodes objects that are passed to default"""
    # TODO: add asserts to all of these and move them out of this function
    import ansible.parsing.vault
    v1 = ansible.parsing.vault.VaultLib([])
    encrypted_text = v1.encrypt('my-secret')

    from ansible.parsing.vault import VaultSecret
    from collections import OrderedDict
    value = OrderedDict({'password': VaultSecret(encrypted_text)})
    ansible_json = AnsibleJSONEncoder()
    ansible_json.encode(value)
    vault_to_text = AnsibleJSONEncoder(vault_to_text=True)
    vault_to_text.encode(value)

    import json
    json

# Generated at 2022-06-12 23:08:49.660429
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()
    assert encoder.default(AnsibleUnsafe('test')) == 'test'
    assert encoder.default(dict()) == {}


# Generated at 2022-06-12 23:08:58.982273
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type
    from ansible.parsing.vault import VaultLib, UnsafeText
    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:09:12.318879
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    input = {
        '__ansible_unsafe': 'test',
        '__ansible_vault': 'test',
        '__ansible_selfref': {'__ansible_selfref': 'test'},
    }
    ansible_unsafe = encoder.default(input['__ansible_unsafe'])
    ansible_vault = encoder.default(input['__ansible_vault'])
    ansible_selfref = encoder.default(input['__ansible_selfref'])
    assert input['__ansible_unsafe'] == ansible_unsafe['__ansible_unsafe']
    assert input['__ansible_vault'] == ansible_vault['__ansible_vault']

# Generated at 2022-06-12 23:09:22.074877
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for method default of class AnsibleJSONEncoder
    """
    import ansible.parsing.vault as vault
    encoder = AnsibleJSONEncoder()
    # normal string
    assert encoder.default('ansible') == 'ansible'
    # date object
    date = datetime.date(2019, 6, 25)
    assert encoder.default(date) == '2019-06-25'
    # datetime object
    datetime_obj = datetime.datetime(2019, 6, 25, 10, 32, 33)
    assert encoder.default(datetime_obj) == '2019-06-25T10:32:33'
    # hostvars object
    hostvars = {'ansible': ''}
    assert encoder.default(hostvars) == {'ansible': ''}

# Generated at 2022-06-12 23:09:28.668517
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime

    # test for default
    assert AnsibleJSONEncoder().default(123) == 123

    # test for default
    assert AnsibleJSONEncoder().default('abc') == 'abc'

    # test for default
    assert AnsibleJSONEncoder().default({}) == {}

    # test for default
    assert AnsibleJSONEncoder().default([]) == []

    # test for default
    assert AnsibleJSONEncoder().default(datetime.datetime(2019, 4, 1, 8, 57, 0)) == '2019-04-01T08:57:00'


# Generated at 2022-06-12 23:09:30.028889
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    z=1
    assert AnsibleJSONEncoder().default(z) == 1

# Generated at 2022-06-12 23:09:40.717573
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit tests for AnsibleJSONEncoder"""

    # First test: check the case where the object type is that of AnsibleVaultEncryptedUnicode.
    # The expected result is to return the vault value.
    from ansible import constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    password = 'password'
    secret_path_file = './.test/secret.txt'
    secret_path_env = 'secret_path'
    secret_path_auto = 'secret_path_auto'
    secret_key_name = 'secret_key'
    secret_key_value = 'secret_value'

    # Create secret file for reading key from environment
    secret = VaultSecret(VaultLib([password, ' '], 1))

# Generated at 2022-06-12 23:09:43.336318
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder().default(dict(a=1, b=dict(c=2)))
    assert result == dict(a=1, b=dict(c=2))

# Generated at 2022-06-12 23:09:51.346694
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.dumps({'a': 5}, cls=AnsibleJSONEncoder) == '{"a": 5}'
    assert json.dumps({'a': 5.1}, cls=AnsibleJSONEncoder) == '{"a": 5.1}'
    assert json.dumps({'a': 'b'}, cls=AnsibleJSONEncoder) == '{"a": "b"}'
    assert json.dumps({'a': [1, 2, 3]}, cls=AnsibleJSONEncoder) == '{"a": [1, 2, 3]}'
    assert json.dumps({'a': []}, cls=AnsibleJSONEncoder) == '{"a": []}'

# Generated at 2022-06-12 23:09:57.792927
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = dict(
        test=True,
        testkey=dict(
            subkey=45
        ),
        testkey2=datetime.datetime.now(),
        testkey3=[dict(
            subkey=45,
            key=datetime.datetime.now()
        )]
    )

    result = AnsibleJSONEncoder(sort_keys=True).encode(data)

    try:
        json_data = json.loads(result)
    except ValueError:
        assert False, "{0} is not valid JSON data".format(result)

    assert json_data == data



# Generated at 2022-06-12 23:10:05.608809
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(10) == 10
    assert ansible_json_encoder.default("10") == "10"
    assert ansible_json_encoder.default(10.0) == 10.0
    assert ansible_json_encoder.default(["10", 10, 10.0]) == ["10", 10, 10.0]
    assert ansible_json_encoder.default({"name": "siva", "age": 32}) == {"name": "siva", "age": 32}
    assert ansible_json_encoder.default(datetime.date(2019, 2, 1)) == "2019-02-01"
    assert ansible_json_encoder.default(datetime.datetime(2019, 2, 1))

# Generated at 2022-06-12 23:10:13.611774
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils.common._collections_compat import Mapping
    assert AnsibleJSONEncoder().default({'a':'b'}) == {'a':'b'}
    assert AnsibleJSONEncoder().default('c') == 'c'
    assert AnsibleJSONEncoder().default(datetime.date.today()) == str(datetime.date.today())
    assert AnsibleJSONEncoder().default(datetime.datetime.now()) == str(datetime.datetime.now().isoformat())
    assert AnsibleJSONEncoder().default([1,2]) == [1,2]
    assert AnsibleJSONEncoder().default(Mapping()) == {}


# Generated at 2022-06-12 23:10:27.058020
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # VaultLib object is a subclass of str (safe object)
    input_data = VaultLib('test')
    # Base case (no exception)
    output_data_1 = AnsibleJSONEncoder().default(input_data)
    # __ENCRYPTED__ attribute is present
    output_data_2 = AnsibleJSONEncoder().default(input_data)
    # __ENCRYPTED__ attribute is absent
    input_data.__ENCRYPTED__ = False
    output_data_3 = AnsibleJSONEncoder().default(input_data)

    # Test values
    assert output_data_1 == output_data_2 == output_data_3

    # Test exception

# Generated at 2022-06-12 23:10:36.862022
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    datetime_value = datetime.datetime(2038,1,19,3,14,7)
    datetime_string = datetime_value.isoformat()

    test_dict = {
        "foo": "bar",
        "bar": "foo",
        "datetime": datetime_value,
    }

    assert AnsibleJSONEncoder().encode(test_dict) == json.dumps(test_dict)
    assert json.loads(AnsibleJSONEncoder().encode(test_dict)) == test_dict

    assert AnsibleJSONEncoder(preprocess_unsafe=True).encode(test_dict) == json.dumps(test_dict)
    assert json.loads(AnsibleJSONEncoder(preprocess_unsafe=True).encode(test_dict)) == test_dict

    assert Ans

# Generated at 2022-06-12 23:10:46.023562
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword

    # mock a VaultLib object
    class MockVaultLib(VaultLib):
        vault_password = VaultPassword(VaultSecret('dummy vault password'))

        @classmethod
        def load(cls, path=None):
            return MockVaultLib()

        def decrypt(self, ciphertext):
            self.vault_password.used = True
            return 'dummy plain text'

    # following are the test cases
    # each case is a list of two elements: the object to test and the expected value
    #
    # the expected value is a dict which includes the following keys
    #    'unsafe': whether the

# Generated at 2022-06-12 23:10:51.578983
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    #  ansible.module_utils.basic.json_utils
    assert AnsibleJSONEncoder()
    assert AnsibleJSONEncoder().default
    assert AnsibleJSONEncoder().default('test')
    assert AnsibleJSONEncoder().default(datetime.date(2019, 1, 2))
    assert AnsibleJSONEncoder().default('{"test":"test"}')
    assert AnsibleJSONEncoder().default(1234)
    assert AnsibleJSONEncoder().default(1234.5678)

# Generated at 2022-06-12 23:10:59.915953
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import _ordereddict
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import text_type
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import string_types
    import datetime
    import time

    vault_encryption_key = 'ansible-vault-password-abc123'
    vault = VaultLib(vault_encryption_key)
    value = vault.encrypt(b'test')
    encrypted_value = value.encode('utf-8')


# Generated at 2022-06-12 23:11:03.321169
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_data = '{"k": "v"}'
    j = json.loads(json_data)
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)
    assert encoder.default(j) == j


# Generated at 2022-06-12 23:11:10.747566
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Testing for datetime.datetime object
    data = datetime.datetime(2019, 12, 18, 12, 30)
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(data) == '2019-12-18T12:30:00'

    # Testing for dict object
    data = {'key': 'value'}
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(data) == {'key': 'value'}

# Generated at 2022-06-12 23:11:20.358323
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Foo():
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.__UNSAFE__ = kwargs.pop('UNSAFE', False)
            self.__ENCRYPTED__ = kwargs.pop('ENCRYPTED', False)
            self._ciphertext = 'bar'
        def __str__(self):
            return 'str'
    obj = Foo(1, 2, 3, UNSAFE=True)
    jenc = AnsibleJSONEncoder()
    assert '__ansible_unsafe' in jenc.default(obj)
    assert '__ansible_vault' not in jenc.default(obj)
    obj = Foo(1, 2, 3, ENCRYPTED=True)

# Generated at 2022-06-12 23:11:24.457266
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # We are testing the code path for datetime.datetime.isoformat
    date = datetime.datetime.utcnow()
    # Execute the code to test
    encoder = AnsibleJSONEncoder()
    encoder.default(date)



# Generated at 2022-06-12 23:11:32.251596
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.vault import VaultLib

    j = [to_bytes('供应商')]

    # Dump bytes with default.
    assert json.dumps(j, cls=AnsibleJSONEncoder) == '[null]'

    # Dump strings with bytes arg.
    assert json.dumps(j, cls=AnsibleJSONEncoder, ensure_ascii=False) == '["供应商"]'



# Generated at 2022-06-12 23:11:44.804948
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    from ansible.module_utils.six import string_types
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.common.collections import ImmutableDict, MutableMapping
    from ansible.module_utils.basic import AnsibleModule

    class TestVaultLib(VaultLib):
        def __init__(self, passphrase):
            super(VaultLib, self).__init__()

        def encrypt(self, value):
            return VaultSecret(value)

        def decrypt(self, value):
            return value

        def is_encrypted(self, value):
            return isinstance(value, VaultSecret)


# Generated at 2022-06-12 23:11:53.010955
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    it = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    class testVault(object):
        def __init__(self):
            self.__ENCRYPTED__ = True

        def __repr__(self):
            return 'testVault'

    class testUnsafe(object):
        def __init__(self):
            self.__UNSAFE__ = True

        def __repr__(self):
            return 'testUnsafe'

    assert it.default(testVault()) == {'__ansible_vault': None}
    assert it.default(testUnsafe()) == {'__ansible_unsafe': None}

# Generated at 2022-06-12 23:11:55.136080
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder(sort_keys=True).encode({'a': 'd'}) == '{"a": "d"}'


# Generated at 2022-06-12 23:12:02.865671
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(True) is True
    assert AnsibleJSONEncoder().default(False) is False
    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default(1.0) == 1.0
    assert AnsibleJSONEncoder().default(1j) == "1j"
    assert AnsibleJSONEncoder().default("Foo") == "Foo"

    class Foo(object):
        def __repr__(self):
            return "Foo"
    assert AnsibleJSONEncoder().default(Foo()) == "Foo"

    assert AnsibleJSONEncoder().default(set([1,2,3])) == [1,2,3]

# Generated at 2022-06-12 23:12:11.530734
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing import vault
    from ansible.module_utils.six import string_types

    def assert_encoded_equal(o, value):
        assert(o == value)

    def assert_encoded_is_instance(o, value):
        if isinstance(o, dict):
            assert(isinstance(value, dict))
            return

        if isinstance(o, string_types):
            assert(isinstance(value, string_types))
            return

        assert(isinstance(value, dict))

    test_encoder = AnsibleJSONEncoder()
    assert_encoded_equal(test_encoder.default(None), None)
    assert_encoded_is_instance(True, test_encoder.default(True))

# Generated at 2022-06-12 23:12:20.128990
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test encrypted
    class Vault:
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext
            self.__ENCRYPTED__ = True
            self.__UNSAFE__ = True

    assert AnsibleJSONEncoder().default(Vault('ciphertext')) == {'__ansible_vault': 'ciphertext'}

    # Test unsafe
    class Unsafe:
        def __init__(self, value):
            self.value = value
            self.__UNSAFE__ = True

    assert AnsibleJSONEncoder().default(Unsafe('value')) == {'__ansible_unsafe': 'value'}

    # Test mapping
    assert AnsibleJSONEncoder().default(dict(key='value')) == {'key': 'value'}

    # Test date


# Generated at 2022-06-12 23:12:30.458002
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe_object = 'unsafe_object'
    unsafe_object.__UNSAFE__ = True
    vault_object = 'vault_object'
    vault_object.__ENCRYPTED__ = True
    test_case_list = [
        'abc',
        1,
        0.1,
        ['a', 'b', 'c', [1, 2, 3]],
        {'a': 123, 'b': 456},
        unsafe_object,
        vault_object,
    ]
    assert AnsibleJSONEncoder().encode(test_case_list) == '["abc", 1, 0.1, ["a", "b", "c", [1, 2, 3]], {"a": 123, "b": 456}, "unsafe_object", "vault_object"]'

# Generated at 2022-06-12 23:12:39.653705
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six.moves import StringIO

    json_string = '{"date": "2019-09-26T15:06:17.138698", "boolean": true, "vault": "foo"}'
    vault_object = AnsibleVaultEncryptedUnicode(b'foo')
    value = {"vault": vault_object, "date": datetime.datetime.now(), "boolean": True}
    encoder = AnsibleJSONEncoder().encode(value)
    io = StringIO(encoder)
    io.seek(0)
    j = json.load(io)
    assert j == json.loads(json_string)



# Generated at 2022-06-12 23:12:47.005015
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # ansible_facts class
    class AnsibleFacts:
        pass

    # ansible_facts object
    ansible_facts = AnsibleFacts()

    # preprocess_unsafe encode, vault_to_text encode
    encoder = AnsibleJSONEncoder(True, True)

    # ansible_facts object
    json_str = encoder.default(ansible_facts)
    assert isinstance(json_str, dict)

    # merge preprocess_unsafe, vault_to_text encode
    encoder = AnsibleJSONEncoder(True, True)

    # ansible_facts object
    json_str = encoder.default(ansible_facts)
    assert isinstance(json_str, dict)


# Generated at 2022-06-12 23:12:56.847483
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(u'foo') == u'foo'
    assert AnsibleJSONEncoder().default(42) == 42
    assert AnsibleJSONEncoder().default(None) == None
    assert AnsibleJSONEncoder().default(False) == False
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default([u'foo', 42, None, False, True]) == [u'foo', 42, None, False, True]
    assert AnsibleJSONEncoder().default({u'foo': u'bar', u'foo2': u'bar2'}) == {u'foo': u'bar', u'foo2': u'bar2'}



# Generated at 2022-06-12 23:13:12.006297
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    from ansible.module_utils.six import text_type

    v = ansible.parsing.vault.VaultLib(b'foo')
    s = u'test'
    d = datetime.datetime.utcnow()
    l = [1, 2, 3]
    m = {u'foo': u'bar'}

    assert isinstance(AnsibleJSONEncoder().encode(v), text_type)
    assert isinstance(AnsibleJSONEncoder().encode(s), text_type)
    assert isinstance(AnsibleJSONEncoder().encode(d), text_type)
    assert isinstance(AnsibleJSONEncoder().encode(l), text_type)

# Generated at 2022-06-12 23:13:16.612460
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    o = 'string'
    assert encoder.default(o) == o

    o = 123
    assert encoder.default(o) == o

    o = 123.45
    assert encoder.default(o) == o

    o = True
    assert encoder.default(o) == o

    o = False
    assert encoder.default(o) == o

    o = None
    assert encoder.default(o) == o

    o = {'a': 'b'}
    assert encoder.default(o) == o

    o = ['a', 'b']
    assert encoder.default(o) == o

    o = datetime.datetime(1985, 12, 20)

# Generated at 2022-06-12 23:13:23.513799
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    # Test if method default of class AnsibleJSONEncoder return a JSON representation
    # of python built-in type Mapping (a.k.a. dict)
    assert isinstance(ansible_json_encoder.default({}), dict)
    # Test if method default of class AnsibleJSONEncoder return a JSON representation
    # of python type datetime
    assert isinstance(ansible_json_encoder.default(datetime.datetime.now()), str)



# Generated at 2022-06-12 23:13:33.987635
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test standard encoder behavior and custom ``AnsibleJSONEncoder.default`` method"""

    # Standard JSONEncoder.default behavior with standard object
    o = {
        "dict": {
            "a": "b"
        },
        "str": 'str',
        "int": 42,
        "float": 3.14159265358979323846,
        "bool": True,
        "list": [
            {
                "a": "b"
            }
        ],
    }
    json.dumps(o, cls=AnsibleJSONEncoder)

    # Custom ``AnsibleJSONEncoder.default`` behavior with standard object
    # NOTE: for AnsibleJSONEncoder.default, we must check for dict/list/string type,
    # otherwise it falls back to the super class ``default`` method.


# Generated at 2022-06-12 23:13:40.083086
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # dict instance
    encoder = AnsibleJSONEncoder()
    output = encoder.default(dict(a=1, b=2))
    assert output == dict(a=1, b=2)

    # datetime instance
    date = datetime.datetime(2019, 6, 27, 13, 30)
    output = encoder.default(date)
    assert output == '2019-06-27T13:30:00'

    # list instance
    l = [1, 2, 3]
    output = encoder.default(l)
    assert output == l

    # set instance
    s = set(['a', 'b', 'c'])
    output = encoder.default(s)
    assert output == s

    # bool instance
    b = False
    output = encoder.default(b)

# Generated at 2022-06-12 23:13:52.550329
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib, VaultSecret

    vault_obj = VaultLib([])
    vault_obj.encrypt(b'foobar')
    my_vault = VaultSecret(b'$ANSIBLE_VAULT;1.1;AES256;foo\r\niJpGkV7+gxFnhscwH8qTqQ==\r\n')

    # create an instance of AnsibleJSONEncoder and assign to variable extended_json_encoder
    extended_json_encoder = AnsibleJSONEncoder()
    # call method default of class AnsibleJSONEncoder and assign to variable encoded_dict
    encoded_dict = extended_json_encoder.default(vault_obj)
    # assert encoded_dict equals {'__ansible_vault': '$ANSIBLE_VA

# Generated at 2022-06-12 23:14:00.347216
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import binary_type
    encoder = AnsibleJSONEncoder()
    # test vault object
    assert encoder.default(VaultSecret('aaaa')) == {'__ansible_vault': b'aaaa'}
    # test datetime
    assert encoder.default(datetime.datetime.utcnow()) == datetime.datetime.utcnow().isoformat()
    # test Mapping
    assert encoder.default(dict(k=1)) == {u'k': 1}
    # test binary_type
    assert encoder.default(binary_type(b'111')) == u'111'

# Generated at 2022-06-12 23:14:08.860359
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import string_types, text_type

    secret = VaultSecret('Vault(testpass)')

    assert isinstance(secret._ciphertext, bytes)

    # For Python3, AnsibleJSONEncoder.default should encode strings to utf-8 strings
    if hasattr(secret._ciphertext, 'decode'):
        assert isinstance(secret._ciphertext.decode('utf-8'), string_types)
    else:
        assert isinstance(secret._ciphertext, string_types)

    # For Python2, AnsibleJSONEncoder.default should encode unicode to utf-8 strings
    secret = VaultSecret('Vault(ȵȵȵȵȵȵ)')


# Generated at 2022-06-12 23:14:19.218831
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import binary_type

    assert AnsibleJSONEncoder().default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder(sort_keys=True).default(dict(a=1, b=2)) == dict(a=1, b=2)
    assert AnsibleJSONEncoder().default(None) is None
    objs = [
        ('str', ('str',)),
        ('bstr', (b'str',)),
        ('unicde', ('str',)),
        ('lstr', ('str',)),
        ('lbstr', (b'str',)),
        ('lunicde', ('str',)),
    ]

# Generated at 2022-06-12 23:14:29.151715
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from units.compat.mock import patch, Mock

    with patch.object(json.JSONEncoder, 'default') as mock_super_default:
        o = Mock()
        o.__ENCRYPTED__ = True
        o.__UNSAFE__ = True
        AnsibleJSONEncoder().default(o)
        mock_super_default.assert_not_called()

        o = Mock()
        o.__ENCRYPTED__ = True
        o.__UNSAFE__ = False
        AnsibleJSONEncoder().default(o)
        mock_super_default.assert_not_called()

        o = Mock()
        o.__ENCRYPTED__ = False
        o.__UNSAFE__ = True
        AnsibleJSONEncoder().default(o)

# Generated at 2022-06-12 23:14:41.060446
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    my_dict = dict(foo=1, bar=1, baz=1)
    my_list = [1, 2, 3]
    my_date = datetime.date(2016, 2, 11)
    unencryptable = set('foo')

    enc = AnsibleJSONEncoder()

    encoded = json.dumps({'my_dict': my_dict, 'unencryptable': unencryptable}, cls=enc)
    assert isinstance(encoded, str)
    assert encoded == '{"unencryptable": "set([\'foo\'])", "my_dict": {"bar": 1, "baz": 1, "foo": 1}}'


# Generated at 2022-06-12 23:14:44.840016
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()

    assert encoder.default(AnsibleUnsafe('ascii_only')) == {'__ansible_unsafe': 'ascii_only'}

# Generated at 2022-06-12 23:14:54.971720
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_data = (
        'test_str',
        b'test_bytes',
        [b'test_list_bytes', 'test_list_str'],
        collections.namedtuple('TestNamedTuple', 'test_named_tuple_attr')(test_named_tuple_attr='test_named_tuple_attr_value'),
        datetime.datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1, microsecond=1),
        datetime.date(year=2020, month=1, day=1),
    )
    # call the method default of class AnsibleJSONEncoder
    test_result = list(map(AnsibleJSONEncoder().default, test_data))
    # assert result

# Generated at 2022-06-12 23:15:04.540095
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    test_string = 'foo'
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(test_string) == 'foo'
    test_string = VaultLib([VaultSecret('secret')]).encrypt(test_string)

# Generated at 2022-06-12 23:15:07.427195
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Foo(object):
        def __eq__(self, other):
            if isinstance(other, dict):
                return False
            return True

    assert json.dumps(Foo(), cls=AnsibleJSONEncoder) == '{}'

# Generated at 2022-06-12 23:15:08.932278
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(1) == 1
    assert encoder.default({}) == {}



# Generated at 2022-06-12 23:15:17.209056
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json

    import datetime

    from ansible.module_utils.urls import open_url

    def test_json_encoder_default_None():
        assert json.dumps(None, cls=AnsibleJSONEncoder) == 'null'

    def test_json_encoder_default_bool():
        assert json.dumps(True, cls=AnsibleJSONEncoder) == 'true'
        assert json.dumps(False, cls=AnsibleJSONEncoder) == 'false'

    def test_json_encoder_default_list():
        assert json.dumps(['a', 'b', 'c'], cls=AnsibleJSONEncoder) == '["a", "b", "c"]'

    def test_json_encoder_default_dict():
        assert json.dumps

# Generated at 2022-06-12 23:15:26.577677
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Testing strings
    s0 = AnsibleJSONEncoder().default('test_string_0')
    assert s0 == 'test_string_0'
    s1 = AnsibleJSONEncoder().default(u'test_unicode_1')
    assert s1 == u'test_unicode_1'

    # Testing safe objects
    s2 = AnsibleJSONEncoder().default({'test_dict_2': 'dict_value_2'})
    assert s2 == {'test_dict_2': 'dict_value_2'}
    s3 = AnsibleJSONEncoder().default(['test_list_3', 'list_value_3'])
    assert s3 == ['test_list_3', 'list_value_3']

# Generated at 2022-06-12 23:15:37.203858
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # check base class
    assert issubclass(AnsibleJSONEncoder, json.JSONEncoder)

    # create the encoder
    encoder = AnsibleJSONEncoder()

    # check for None
    assert encoder.default(None) is None

    # check for json.JSONEncoder
    value = json.JSONEncoder()
    assert encoder.default(value) is not value

    # check for dict
    value = {'key': 'value'}
    assert encoder.default(value) is not value

    # check for datetime.date
    value = datetime.date(year=2019, month=1, day=1)
    assert encoder.default(value) is not value

    # check for datetime.datetime

# Generated at 2022-06-12 23:15:46.090208
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # create a dictionary with the test data
    test_data = {
        'string': 'string',
        'unicode_string': u'unicode_string',
        'dict': {
            'string': 'string',
            'unicode_string': u'unicode_string',
            'dict': {
                'string': 'string',
                'unicode_string': u'unicode_string',
                'list': [
                    {
                        'string': 'string',
                        'unicode_string': u'unicode_string',
                    }
                ]
            },
            'list': ['string', u'unicode_string']
        },
        'list': ['string', u'unicode_string']
    }

    # create a AnsibleJSONEncoder object
    enc = AnsibleJSONEncoder()

    test_

# Generated at 2022-06-12 23:16:04.378103
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # make a vault object to pass as a parameter
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.utils.unsafe_proxy import create_unsafe_text
    vault_secret = VaultSecret()
    vault_val = VaultLib(vault_secret)
    test_data = 'my_secret_password'
    vaulted_secret = vault_val.encrypt(test_data)
    vault_object = AnsibleUnsafe()
    vault_object._include('vault_object')
    vault_object._ciphertext = vaulted_secret
    vault_object._secret = vault_secret
    vault_object.__ENCRYPTED__ = True

    # make

# Generated at 2022-06-12 23:16:12.248842
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = {
        u'a': [ 1, 2, 3 ],
        u'b': u'abc',
        u'c': { u'c1': u'def', u'c2': u'ghi' },
        u'd': datetime.datetime(2019, 1, 1, 12, 0),
        u'e': datetime.date(2019, 1, 1),
    }

    j = AnsibleJSONEncoder(indent=2)
    assert json.loads(j.encode(a)) == a

    # test vault object
    from ansible.parsing.vault import VaultSecret
    ansible_unsafe = VaultSecret(b'abcdefghijklmnopqrstuvwxyz')

# Generated at 2022-06-12 23:16:17.109094
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe

    # test for type AnsibleUnsafe
    assert json.loads(json.dumps(AnsibleUnsafe('hello world'), cls=AnsibleJSONEncoder))['__ansible_unsafe'] == 'hello world'

    # test for some other types
    assert json.loads(json.dumps(datetime.datetime(2019, 1, 1, 12, 12, 12), cls=AnsibleJSONEncoder)) == '2019-01-01T12:12:12'


# Generated at 2022-06-12 23:16:21.334398
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys
    sys.path.append('/path/to/ansible_module_utils/')
    from ansible.module_utils.basic import AnsibleUnsafe
    s = AnsibleUnsafe('password')
    j = AnsibleJSONEncoder().default(s)
    assert(j['__ansible_unsafe']=='password')
    assert(type(j)==dict)


# Generated at 2022-06-12 23:16:30.151267
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # import module snippets
    from ansible.module_utils.six import PY3

    from ansible.module_utils.common.collections import AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedBytes
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode
    from ansible.module_utils.common.text.converters import bytes_to_hex, hex_to_bytes

    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    assert encoder.default(AnsibleVaultEncryptedUnicode(u'foo')) == {'__ansible_vault': hex_to_bytes(u'666f6f')}

# Generated at 2022-06-12 23:16:37.563269
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_data = {
        '__ansible_unsafe__': [
            b"b'",
            b"'",
            u"u'",
            u"'",
            b"b\"",
            b"\"",
            u"u\"",
            u"\"",
        ],
        '__ansible_vault__': b'abc',
        'datetime': datetime.datetime.now(),
        'date': datetime.date.today(),
        'object': object()
    }

    result = json.loads(json.dumps(test_data, cls=AnsibleJSONEncoder))
