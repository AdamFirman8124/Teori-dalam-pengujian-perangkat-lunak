

# Generated at 2022-06-12 23:06:46.813708
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test for `vault object`
    master_password = 'myvault'
    secret = 'mysecret'

# Generated at 2022-06-12 23:06:57.751135
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:06:59.406343
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    e = AnsibleJSONEncoder()
    assert e.default("foo") == "foo"
    assert e.default("bar") == "bar"

# Generated at 2022-06-12 23:07:05.887859
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    hostvars = {'ansible_host': '127.0.0.1'}
    date = datetime.date(2019, 7, 30)
    encoded_hostvars = json_encoder.default(hostvars)
    encoded_date = json_encoder.default(date)
    assert isinstance(encoded_hostvars, dict)
    assert isinstance(encoded_date, str)

    try:
        import ansible.utils.unsafe_proxy
        encoder = AnsibleJSONEncoder()
        plaintext = 'test'
        unsafe_proxy = ansible.utils.unsafe_proxy.AnsibleUnsafeText(plaintext)
        assert encoder.default(unsafe_proxy) == plaintext
    except ImportError:
        pass


# Generated at 2022-06-12 23:07:15.892337
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()

    s = 'null'
    assert ansible_json_encoder.default(s) == 'null',\
        "AnsibleJSONEncoder.default() ignore string"

    i = 1
    assert ansible_json_encoder.default(i) == 1,\
        "AnsibleJSONEncoder.default() ignore number"

    d = datetime.datetime(2020, 1, 1)
    assert ansible_json_encoder.default(d) == '2020-01-01T00:00:00',\
        "AnsibleJSONEncoder.default() convert datetime to string"

    # _is_unsafe
    from ansible.parsing.vault import VaultLib
    vault_text = VaultLib.encrypt('foo')
   

# Generated at 2022-06-12 23:07:25.867905
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default('a') == 'a'
    assert ansible_json_encoder.default(1) == 1
    assert ansible_json_encoder.default(True) == True
    assert ansible_json_encoder.default(datetime.datetime(2019, 10, 9)) == '2019-10-09T00:00:00'
    assert ansible_json_encoder.default(datetime.date(2019, 10, 9)) == '2019-10-09'
    vault_secret = 'VaultLib(password=joshua)'

# Generated at 2022-06-12 23:07:30.140427
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enco = AnsibleJSONEncoder()
    obj = {'_ansible_parsed': True, 'foo': 'bar'}
    ret = enco.default(obj)
    assert isinstance(ret, dict)
    assert ret == obj


# Generated at 2022-06-12 23:07:37.878038
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # setup
    crypto_mock = {"__ENCRYPTED__": True, "_ciphertext": to_text("This is a test", errors='surrogate_or_strict')}
    safe_mock = {"__UNSAFE__": True}
    mapping_mock = {'hello': 'world'}
    date_mock = datetime.date(2019, 8, 15)
    obj_mock = {'hello': 'world'}  # type: Mapping

    # execution
    crypto = AnsibleJSONEncoder().default(crypto_mock)
    safe = AnsibleJSONEncoder().default(safe_mock)
    mapping = AnsibleJSONEncoder().default(mapping_mock)
    date = AnsibleJSONEncoder().default(date_mock)
    obj = AnsibleJSONEnc

# Generated at 2022-06-12 23:07:39.412662
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(b'text') == 'text'



# Generated at 2022-06-12 23:07:50.424541
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import base64

    encoder = AnsibleJSONEncoder()

    # default() should work for dict
    assert encoder.default({}) == {}

    # use custom class
    class AnsibleInventoryHostVars(dict):
        pass
    assert encoder.default(AnsibleInventoryHostVars()) == {}

    # use custom class
    class AnsibleUnsafe(str):
        __UNSAFE__ = True
        __ENCRYPTED__ = False
    assert encoder.default(AnsibleUnsafe("foo")) == {'__ansible_unsafe': "foo"}

    # use custom class
    class AnsibleUnsafe(str):
        __UNSAFE__ = True
        __ENCRYPTED__ = False

# Generated at 2022-06-12 23:08:02.209577
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    test_AnsibleJSONEncoder_default: test default method of AnsibleJSONEncoder
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()
    assert encoder.default(1) == 1
    assert encoder.default(1.1) == 1.1
    assert encoder.default('abc') == 'abc'
    assert encoder.default(AnsibleUnsafe('abc')) == {'__ansible_unsafe': 'abc'}
    assert encoder.default(ImmutableDict({'a': 1})) == {'a': 1}
    vault = VaultLib('test')

# Generated at 2022-06-12 23:08:12.549955
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_text

    # Test that class AnsibleJSONEncoder.default return correct result
    from ansible.parsing.vault import VaultLib

    vault_password = 'password'
    vault_text = '$ANSIBLE_VAULT;1.1;AES256'
    vault_obj = VaultLib([vault_password])
    vault_ciphertext = vault_obj.encrypt(vault_text)
    ansible_vault_obj = vault_obj.decrypt(vault_ciphertext)
    # Test that ansible_vault_obj is an instance of class AnsibleUnsafeText
    assert isinstance(ansible_vault_obj, VaultLib.AnsibleUnsafeText)
    # Test that ansible_vault_obj.

# Generated at 2022-06-12 23:08:22.808207
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test the default method of class AnsibleJSONEncoder
    '''
    import ansible.module_utils.basic
    import ansible.parsing.vault
    import datetime

    # instantiate a AnsibleJSONEncoder object
    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    # let's test a few of the different input types
    test_string = "test"
    test_dict = {'foo': 'bar', 'baz': 'qux'}
    test_date = datetime.date(2020, 8, 4)
    test_datetime = datetime.datetime(2020, 8, 4, 18, 30, 30)

# Generated at 2022-06-12 23:08:27.303033
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()

    data = {
        'a': 1,
        'b': AnsibleUnsafe('test'),
    }
    assert encoder.default(data) == {'a': 1, 'b': {'__ansible_unsafe': u'test'}}

# Generated at 2022-06-12 23:08:36.227149
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enc1 = AnsibleJSONEncoder()
    assert enc1.default('abc') == 'abc'

    class Foo(object):
        def __init__(self, s):
            self.s = s
        def __str__(self):
            return self.s

    enc2 = AnsibleJSONEncoder()
    assert enc2.default(Foo('str')) == {'s':'str'}

    if hasattr(json.JSONEncoder, 'iterencode'):
        class Foo(object):
            def __init__(self, s):
                self.s = s
            def __str__(self):
                return self.s

        enc3 = AnsibleJSONEncoder()
        assert enc3.default(Foo('str')) == {'s':'str'}

# Generated at 2022-06-12 23:08:46.335323
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import os
    import stat
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils._text import to_bytes

    # vault object

# Generated at 2022-06-12 23:08:56.474238
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()
    assert a.default(None) == 'null'
    assert a.default('foo') == '"foo"'
    assert a.default(True) == 'true'
    assert a.default(False) == 'false'
    assert a.default(42) == 42
    assert a.default(42.0) == 42.0
    assert a.default(dict(key='value')) == {'key': 'value'}
    assert a.default(dict(key=42)) == {'key': 42}
    assert a.default(dict(key=42.0)) == {'key': 42.0}
    assert a.default(dict(key=None)) == {'key': 'null'}

# Generated at 2022-06-12 23:09:06.018242
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe(str):
        __UNSAFE__ = True

        def __deepcopy__(self, memo):
            return self

    class AnsibleVault(str):
        __ENCRYPTED__ = True

        def __deepcopy__(self, memo):
            return self

    obj = AnsibleUnsafe('a')
    encoder = AnsibleJSONEncoder()
    assert encoder.default(obj) == {'__ansible_unsafe': u'a'}

    obj = AnsibleVault('a')
    assert encoder.default(obj) == {'__ansible_vault': u'a'}

    obj = {'a': AnsibleUnsafe('a')}
    assert encoder.default(obj) == {'a': {'__ansible_unsafe': u'a'}}

# Generated at 2022-06-12 23:09:14.848827
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('abc') == 'abc'

    assert AnsibleJSONEncoder().default({'key1': 1, 'key2': '2'}) == {'key1': 1, 'key2': '2'}

    assert AnsibleJSONEncoder().default(['1', '2']) == ['1', '2']

    assert AnsibleJSONEncoder().default(datetime.datetime(2019, 9, 1, 0, 0, 0, 0)) == '2019-09-01T00:00:00'

    assert AnsibleJSONEncoder().default(datetime.date(2019, 9, 1)) == '2019-09-01'

# Generated at 2022-06-12 23:09:21.449156
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default('hi') == 'hi'
    assert ansible_json_encoder.default('hi') == 'hi'
    class TestClass:
        def __repr__(self):
            return 'Test class'
    assert ansible_json_encoder.default(TestClass()) == 'Test class'


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "-s"])

# Generated at 2022-06-12 23:09:33.337753
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import binary_type

    test_data = [
        {'name': 'binary', 'input': binary_type(b'binary'), 'output': '"binary"'},
        {'name': 'unicode', 'input': u'unicode', 'output': '"unicode"'},
        {'name': 'bytes', 'input': b'bytes', 'output': '"bytes"'},
        {'name': 'list', 'input': [1, 2, 3], 'output': '[1, 2, 3]'},
        {'name': 'dict', 'input': {'a': 1, 'b': 2}, 'output': '{"a": 1, "b": 2}'},
    ]


# Generated at 2022-06-12 23:09:38.367329
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Method default of class AnsibleJSONEncoder doesn't support instance of
    ``datetime.timedelta``.
    '''
    import datetime
    encoder = AnsibleJSONEncoder()
    assert encoder.default(datetime.timedelta(days=1)) == str(datetime.timedelta(days=1))

# Generated at 2022-06-12 23:09:46.623306
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test default
    assert encoder.default({"a": "b"}) == {"a": "b"}
    assert encoder.default(datetime.datetime(2020, 3, 31, 14, 00, 00)) == "2020-03-31T14:00:00"
    assert encoder.default(datetime.date(2020, 3, 31)) == "2020-03-31"
    assert encoder.default(datetime.time(14, 00, 00)) == "14:00:00"
    assert encoder.default(datetime.timedelta(days=2)) == "2 days, 0:00:00"


# Generated at 2022-06-12 23:09:53.306459
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    pw = vault.encrypt('test')
    # basic call
    x = AnsibleJSONEncoder().default(pw)
    assert isinstance(x, dict)

    # write to a file-like string
    s = StringIO()
    json.dump(pw, s, cls=AnsibleJSONEncoder)
    assert json.loads(s.getvalue()) == x

    # write to a file
    f = 'test.json'
    with open(f, 'w') as fh:
        json.dump(pw, fh, cls=AnsibleJSONEncoder)

# Generated at 2022-06-12 23:10:02.133576
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert json.dumps({'a': [1, 2, 3]}, cls=AnsibleJSONEncoder) == '{"a": [1, 2, 3]}'

    class Dummy(object):
        pass
    assert encoder.default(Dummy()) == '<__main__.Dummy object at 0x7f73f25d11d0>'

    from ansible.module_utils.unicode import AnsibleUnsafe
    assert encoder.default(AnsibleUnsafe('{"b": 2}')) == {'__ansible_unsafe': '{"b": 2}'}

# Generated at 2022-06-12 23:10:11.765965
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type

    vault_password = VaultLib('foo')

# Generated at 2022-06-12 23:10:22.322628
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils._text import to_text

    v = VaultLib([])
    text = "This is a secret"
    ciphertext = v.encrypt(text)
    secret = VaultSecret(ciphertext)

    assert(secret.__ENCRYPTED__ == True)
    assert(secret.__UNSAFE__ == False)

    aje = AnsibleJSONEncoder()
    ansible_json_encoded = aje.default(secret)

    assert(ansible_json_encoded['__ansible_vault'] == ciphertext)

    jsonencoded_again = json.dumps(ansible_json_encoded)


# Generated at 2022-06-12 23:10:30.778696
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing import from_vault
    from ansible.module_utils.six import string_types

    # Test Encoding of __ENCRYPTED__ objects
    test_enc_obj = from_vault(to_bytes(u"test_enc_vault", encoding='utf8'))
    assert test_enc_obj.__ENCRYPTED__
    assert isinstance(json.dumps(test_enc_obj, cls=AnsibleJSONEncoder), string_types)
    assert '__ansible_vault' in json.dumps(test_enc_obj, cls=AnsibleJSONEncoder)

    # Testing Encoding of __UNSAFE__ objects
    test_unsafe_obj = to_bytes

# Generated at 2022-06-12 23:10:39.940696
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Basic test for the default method of AnsibleJSONEncoder
    test_case_json_dict = {
        'unsafe_object': dict,
        'vault_object': dict,
        'hostvars': dict,
        'datetime_object': datetime.datetime,
        'unknown_object': None,
    }
    unsafe_object = dict(__UNSAFE__=True)
    vault_object = dict(__ENCRYPTED__=True)

# Generated at 2022-06-12 23:10:49.986387
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    plaintext = 'plaintext'
    encrypted = vault.encrypt(plaintext)


# Generated at 2022-06-12 23:11:02.503946
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime

    # Test case for non-string
    a = AnsibleJSONEncoder(preprocess_unsafe=False)
    a.default('Some string')
    a.default(1234)
    a.default(1234.5)
    a.default({})
    a.default([])
    a.default(True)
    a.default(False)
    a.default(None)
    a.default('[')

    # Test case for string
    a = AnsibleJSONEncoder(preprocess_unsafe=False)
    a.default('Some string')
    a.default(u'Some string')
    a.default('[')

    # Test case for datetime
    today_datetime = datetime.datetime.now()

# Generated at 2022-06-12 23:11:08.343407
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import string_types

    encoder = AnsibleJSONEncoder()
    assert not isinstance(encoder.default("test"), string_types)
    assert not isinstance(encoder.default(string_types("test")), string_types)
    assert not isinstance(encoder.default(datetime.datetime.now()), string_types)


# Generated at 2022-06-12 23:11:12.780729
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """ Unit tests for method default of class AnsibleJSONEncoder. """
    # initialize a class object of AnsibleJSONEncoder
    aje = AnsibleJSONEncoder()

    # test whether the return value is the expected result
    assert aje.default(datetime.datetime(2017, 2, 3, 4, 5, 6)) == '2017-02-03T04:05:06'

# Generated at 2022-06-12 23:11:17.533249
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    assert(encoder.default(dict()) == dict())
    assert(encoder.default(Mapping()) == dict())
    assert(encoder.default(datetime.date(2001, 2, 3)) == '2001-02-03')
    assert(encoder.default(datetime.datetime(2001, 2, 3, 4, 5)) == '2001-02-03T04:05:00')
    assert(encoder.default('test') == 'test')
    assert(encoder.default(123) == 123)
    assert(encoder.default(None) == None)
    assert(encoder.default(True) == True)

# Generated at 2022-06-12 23:11:28.181932
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    # AnsibleUnsafe
    u = AnsibleUnsafe('my_unsafe')
    # vault object
    v = VaultLib('my_vault')

# Generated at 2022-06-12 23:11:37.867392
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import pytest
    from ansible.module_utils.six import text_type

    import ansible.module_utils.common.unsafe_proxy

    # Regression for bug 1286
    assert AnsibleJSONEncoder().encode(ansible.module_utils.common.unsafe_proxy.AnsibleUnsafeText(u"some text")) == '"some text"'

    assert AnsibleJSONEncoder().encode({'foo': 'bar'}) == '{"foo": "bar"}'
    assert AnsibleJSONEncoder().encode(datetime.datetime.strptime("2018-01-01T08:00:00-0500", "%Y-%m-%dT%H:%M:%S%z")) == '"2018-01-01T08:00:00-05:00"'


# Generated at 2022-06-12 23:11:46.132784
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import integer_types, binary_type
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    encoder = AnsibleJSONEncoder()

    int_obj = 1
    assert encoder.default(int_obj) == int_obj
    for int_obj in integer_types:
        assert encoder.default(int_obj) == int_obj

    # bytes
    bytes_obj = b'bytes_obj'
    assert encoder.default(bytes_obj) == bytes_obj
    assert encoder.default(binary_type(bytes_obj)) == bytes_obj

    # date and datetime objects

# Generated at 2022-06-12 23:11:53.835599
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test encrypt data
    enc = AnsibleJSONEncoder()
    assert enc.default(b'abc') == 'abc'

    # Test dictionary
    assert enc.default({'a':1, 'b':'foo', 'c':'bar'}) == {'a':1, 'b':'foo', 'c':'bar'}

    # Test date
    assert enc.default(datetime.date(2019, 1, 1)) == '2019-01-01'

    # Test date time
    assert enc.default(datetime.datetime(2019, 1, 1, 23, 59, 59)) == '2019-01-01T23:59:59'

# Generated at 2022-06-12 23:11:58.428767
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert {'ansible_unsafe_str': 'AnsibleUnsafe("", "!", "!!")'} == (
        json.loads(
            json.dumps(
                {'ansible_unsafe_str': 'AnsibleUnsafe("", "!", "!!")'},
                cls=AnsibleJSONEncoder
            )
        )
    )

# Generated at 2022-06-12 23:12:08.708499
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # In order to test the result returned by method default of class AnsibleJSONEncoder
    # I need to register the encoder class to the moduleutils.

    def _register_encoder():
        json.encoder.c_make_encoder = None

    _register_encoder()

    encoder = json.JSONEncoder()

    # Here is a test to check the result returned by method default of class AnsibleJSONEncoder.
    # I tested the from_json and json.loads functions, but the results are different.
    # The iterencode method returns a generator object, so I need to use json.loads to convert the generator object into a string.
    # When I use json.loads to convert the generator object into a string, the output is not the same.
    # I don't know what the problem is, I just know it is something about the object that

# Generated at 2022-06-12 23:12:21.038279
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword

    # Test 1: vault object
    # Arrange
    o = VaultLib([VaultSecret('$ANSIBLE_VAULT;1.1;AES256;testuser', '\n'.join(['a' * 80, 'b' * 80]))],
                 password=VaultPassword('testpassword'))
    o = o.decrypt(o.secrets[0])
    encoder = AnsibleJSONEncoder()
    # Act
    value = encoder.default(o)
    # Assert

# Generated at 2022-06-12 23:12:27.226045
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # success
    encoder = AnsibleJSONEncoder()
    assert encoder.default(datetime.datetime(1947, 8, 15, 12, 0, 0)) == '1947-08-15T12:00:00'
    assert encoder.default(datetime.date(2010, 2, 15)) == '2010-02-15'
    assert encoder.default({'key': 'value'}) == {'key': 'value'}
    # failure
    assert encoder.default(None) == None

# Generated at 2022-06-12 23:12:38.379546
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class Hostvars(dict): pass

    try:
        import json
    except ImportError:
        import simplejson as json
    from ansible.module_utils.common.collections import is_sequence

    class AnsibleUnsafe(str):
        def __str__(self):
            return "__ANSIBLE_SAFE__"

    class AnsibleVault(str):
        def __str__(self):
            return "__ANSIBLE_SAFE__"

    class AnsibleUnsafeEncoder(json.JSONEncoder):
        """
        A extended JSONEncoder which can handle ``unsafe`` objects.
        """

        def default(self, o):
            if getattr(o, '__UNSAFE__', False):
                # unsafe object
                value = {'__ansible_unsafe': str(o)}
            el

# Generated at 2022-06-12 23:12:46.090673
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    vl = VaultLib('123')
    vault_obj = vl.encrypt(b'foo')
    unsafe_obj = AnsibleUnsafe(b'foo')

    safe_dict = {'foo': 'bar'}
    unsafe_dict = {'foo': unsafe_obj}

    obj = {'vault': vault_obj,
           'unsafe': unsafe_obj,
           'safe_dict': safe_dict,
           'unsafe_dict': unsafe_dict}

    expected = json.dumps(obj, indent=4, sort_keys=True, separators=(',', ': '), cls=AnsibleJSONEncoder)

# Generated at 2022-06-12 23:12:56.183673
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = {
        'date': datetime.date(2018, 7, 31),
        'datetime': datetime.datetime(2018, 7, 31),
        'datetime_timezone': datetime.datetime(2018, 7, 31, 5, 20, tzinfo=datetime.timezone.utc),
        'dict': {'key': 'value'},
    }

    expected = {
        'date': '2018-07-31',
        'datetime': '2018-07-31T00:00:00',
        'datetime_timezone': '2018-07-31T05:20:00+00:00',
        'dict': {'key': 'value'},
    }
    assert expected == json.loads(json.dumps(obj, cls=AnsibleJSONEncoder))


#

# Generated at 2022-06-12 23:13:01.830142
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import unittest

    from ansible.module_utils.six import PY3
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.compat.ipaddress import ip_address

    from ansible.module_utils.common import prefix_vars


# Generated at 2022-06-12 23:13:12.258044
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    import time

    to_test_success = [
        AnsibleUnsafeText(u'test1'),
        u'test2',  # common text
        {'a': 1},  # dict
        [1, 2, 3],  # list
        123,  # integer
        {'a': dict(b=1, c='5', d=5.5)},  # nested dict
        [1, ['a', {'b': [1, 2]}]],  # nested list
        datetime.datetime(year=2019, month=1, day=1, minute=56),  # datetime
        datetime.date(year=2019, month=1, day=1),  # date
        datetime.time(minute=10),  # time
    ]

# Generated at 2022-06-12 23:13:14.851227
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test for AnsibleJSONEncoder().default(o)
    from ansible.module_utils.basic import AnsibleUnsafe
    # Test for AnsibleJSONEncoder().default(o)
    encoder = AnsibleJSONEncoder()
    assert encoder.default(AnsibleUnsafe('something')) == 'something'
    assert encoder.default('something') == 'something'


# Generated at 2022-06-12 23:13:24.868203
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleVault(object):
        def __init__(self, ciphertext=None, version=None, b_ciphertext=None):
            self.ciphertext = ciphertext
            self.version = version
            self.b_ciphertext = b_ciphertext
            self.__ENCRYPTED__ = True

    class AnsibleUnsafe(object):
        def __init__(self, value=None):
            self.value = value
            self.__UNSAFE__ = True

    class AnsibleVaultUnsafe(object):
        def __init__(self, value=None):
            self.value = value
            self.__ENCRYPTED__ = True
            self.__UNSAFE__ = True


# Generated at 2022-06-12 23:13:34.786265
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Function to test the method default of class AnsibleJSONEncoder
    '''
    ansible_json_encoder = AnsibleJSONEncoder()

    # Tested via test_collections() in collections.py
    assert ansible_json_encoder.default(Mapping()) == {}
    assert ansible_json_encoder.default([]) == []
    assert ansible_json_encoder.default((1,)) == [1]
    assert ansible_json_encoder.default(None) is None
    assert ansible_json_encoder.default(1) == 1
    assert ansible_json_encoder.default('a') == 'a'
    assert ansible_json_encoder.default(1.0) == 1.0
    assert ansible_json_encoder.default(True) is True


# Generated at 2022-06-12 23:13:50.711684
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def assertEqual(value, expected):
        assert value == expected, "%s == %s" % (value, expected)

    encoder = AnsibleJSONEncoder()

    # test for the vault object
    class Vault:
        __ENCRYPTED__ = True
        _ciphertext = 'vault'

    encrypted_value = encoder.default(Vault())
    assertEqual(encrypted_value, {'__ansible_vault': 'vault'})

    # test for the unsafe object
    class Unsafe:
        __UNSAFE__ = True

    unsafe_value = encoder.default(Unsafe())
    assertEqual(unsafe_value['__ansible_unsafe'], 'class')

    # test for mapping object, which is hostvars for example

# Generated at 2022-06-12 23:13:59.801538
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) == json.JSONEncoder.default(None)
    assert AnsibleJSONEncoder().default(1) == json.JSONEncoder.default(1)
    assert AnsibleJSONEncoder().default("1") == json.JSONEncoder.default("1")
    assert AnsibleJSONEncoder().default([1, 2, 3]) == json.JSONEncoder.default([1, 2, 3])
    assert AnsibleJSONEncoder().default({"1": 1, "2": 2, "3": 3}) == json.JSONEncoder.default({"1": 1, "2": 2, "3": 3})
    assert AnsibleJSONEncoder().default(datetime.datetime(2019, 1, 1)) == json.JSONEncoder.default(datetime.datetime(2019, 1, 1))
   

# Generated at 2022-06-12 23:14:07.900948
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This class is for testing only
    class TestClass(object):
        def __init__(self):
            self.id = '42'

    # datetime.timedelta has a bug (missing __getnewargs__).
    td = datetime.datetime.now() - datetime.datetime.now()
    # datetime.timedelta has a bug (missing __getnewargs__).
    td2 = datetime.datetime.now() - datetime.datetime.now()
    td2.microsecond = 0

# Generated at 2022-06-12 23:14:18.244823
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    assert ansible_json_encoder.default(VaultLib(None, 1, [VaultSecret(1, 'myciphertext')])) == {'__ansible_vault': 'myciphertext'}
    assert ansible_json_encoder.default(AnsibleUnsafeText('test')) == {'__ansible_unsafe': 'test'}

# Generated at 2022-06-12 23:14:25.011177
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys

    if sys.version_info < (3, 0):
        import StringIO as io
    else:
        import io

    encoder = AnsibleJSONEncoder()
    assert json.loads(encoder.encode(True))
    assert not json.loads(encoder.encode(False))

    assert encoder.encode('\u94d0') == '"\\u94d0"'
    assert encoder.encode('\u94d0\u94d0') == '"\\u94d0\\u94d0"'

    assert json.loads(encoder.encode([])) == []
    assert json.loads(encoder.encode({})) == {}

    import datetime
    now = datetime.datetime.now()
    assert encoder.encode(now) == now.isoformat

# Generated at 2022-06-12 23:14:34.534690
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import AnsibleVaultError, VaultLib
    from ansible.parsing.vault import VaultSecret

    vault_pass = 'foo'
    ciphertext = VaultLib.encrypt(vault_pass, 'not_a_secret')

    assert json.dumps(ciphertext, cls=AnsibleJSONEncoder) == '"not_a_secret"'
    assert json.dumps(ciphertext, cls=AnsibleJSONEncoder, vault_to_text=True) == '"not_a_secret"'

    vault_secret = VaultSecret(vault_pass)
    assert json.dumps(vault_secret, cls=AnsibleJSONEncoder) == json.dumps({'__ansible_vault': ciphertext})


# Generated at 2022-06-12 23:14:41.483476
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_text

    vault_password_file = None
    enc = AnsibleJSONEncoder(vault_to_text=True)
    res = enc.default(VaultLib(vault_password_file).encrypt(to_bytes('test', errors='surrogate_or_strict')))
    # If this test fails please update the AWS and Tower callback plugins to use the new string
    assert '$ANSIBLE_VAULT' in res

    enc = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:51.707941
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves.urllib.parse import quote_plus
    vault_password = 'mysecret'
    vault = VaultLib(vault_password)

# Generated at 2022-06-12 23:15:01.847260
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Test if the method default of class AnsibleJSONEncoder works.
    """
    plain_list = [1, 2, 3]
    plain_dict = {'a': 'a', 'b': 'b'}
    unsafe_string = 'unsafe'
    ansible_vault = 'ansible_vault'

    ansible_json_encoder = AnsibleJSONEncoder()
    json_unsafe = ansible_json_encoder.default(unsafe_string)
    json_ansible_vault = ansible_json_encoder.default(ansible_vault)
    json_plain_list = ansible_json_encoder.default(plain_list)
    json_plain_dict = ansible_json_encoder.default(plain_dict)
    assert json_unsafe == 'unsafe'

# Generated at 2022-06-12 23:15:06.328326
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import base64

    # encrypt safe text
    vault_text = VaultLib.encrypt(b'test_secret', b'ansible')
    b64_vault_text = base64.b64encode(vault_text)

    # encrypt unsafe text

# Generated at 2022-06-12 23:15:22.410871
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.six.moves import builtins
    from ansible.parsing.vault import VaultLib
    import ansible.module_utils.basic
    import ansible.module_utils.six

    _module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())

    raw = "abc123"
    vault = VaultLib([])
    encrypted = vault.encrypt(raw)

    # vault object
    ansible_vault = ansible.module_utils.six.text_type(encrypted)
    ansible_vault.__ENCRYPTED__ = True

# Generated at 2022-06-12 23:15:33.227763
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import is_sequence

    # test no objects in list
    assert is_sequence(json.JSONEncoder().encode([1,2,3]))

    # test no objects in dict
    assert is_sequence(json.JSONEncoder().encode({'k1':'v1','k2':'v2','k3':'v3'}))

    # test vault object
    from ansible.parsing.vault import VaultLib, VaultSecret
    vault = VaultLib([])
    vault_secret = VaultSecret()

# Generated at 2022-06-12 23:15:42.998223
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence

    import datetime

    date = datetime.date(2016, 11, 3)
    datetime = datetime.datetime(2016, 11, 3)
    playbook_plugin_json = {'__ansible_unsafe': '{"redact_regexp":"^(.*)$","redact_string":"REDACTED"}'}
    hostvars_json = {'ansible_system': 'Linux', 'ansible_distribution': 'Centos'}
    vault_json = '{"__ansible_vault": "vault_value"}'
    value = [u"value"]
    value_

# Generated at 2022-06-12 23:15:51.696338
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def default_test(o, expected):
        object = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
        value = object.default(o)
        if value != expected:
            raise AssertionError('AnsibleJSONEncoder.default(%s) returned %s, but %s is expected' % (o, value, expected))
    # Instances of ansible.parsing.vault.VaultSecret
    default_test(u'1', u'1')
    default_test(u'中文', u'中文')
    default_test(u'\0', u'\u0000')
    default_test('1', u'1')
    default_test('中文', u'中文')

# Generated at 2022-06-12 23:16:01.098293
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:16:04.789306
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    o = u'\u1234'
    result = AnsibleJSONEncoder(ensure_ascii=False).default(o)
    assert result == u'\u1234'
    result = AnsibleJSONEncoder().default(o)
    assert result == u'\u1234'


# Generated at 2022-06-12 23:16:12.587695
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.utils.unsafe_proxy as unsafe_proxy
    import ansible.parsing.vault as ansible_vault
    from ansible.utils.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    ansible_json_encoder = AnsibleJSONEncoder()

    # args: (text_object, vault_id, _log_encrypt, _log_decrypt)
    vault_lib = VaultLib([])
    vault_secret = VaultSecret(vault_lib)

    # encrypt and write a file named ./test_password
    vault_secret.encrypt_string(u'test_password')
    with open('./test_password', 'r') as f:
        test_password = f.read()

    # test unsafe
    unsafe_proxy_obj = unsafe_

# Generated at 2022-06-12 23:16:18.986599
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    #Test for default method of class AnsibleJSONEncoder
    def _get_default_value(obj):
        # Executing the default method with obj as argument
        return AnsibleJSONEncoder().default(obj)

    # Case 1 : when obj is a datetime object
    # Creating a datetime object
    test_datetime = datetime.datetime(year=2019, month=10, day=25, hour=10)
    # Converting the datetime object expected_output as a string
    expected_output = "2019-10-25T10:00:00"
    # Asserting that both are equal
    assert _get_default_value(test_datetime) == expected_output

    # Case 2 : when obj is a date object
    # Creating a date object

# Generated at 2022-06-12 23:16:27.298936
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder().default(None)
    assert result is None

    result = AnsibleJSONEncoder().default(False)
    assert result is False

    result = AnsibleJSONEncoder().default(True)
    assert result is True

    result = AnsibleJSONEncoder(sort_keys=True).default({'b': 1, 'a': 2})
    assert result == {'a': 2, 'b': 1}

    result = AnsibleJSONEncoder().default(1)
    assert result == 1

    result = AnsibleJSONEncoder().default(1.0)
    assert result == 1.0

    result = AnsibleJSONEncoder().default([1, 2, "test"])
    assert result == [1, 2, "test"]

    result = AnsibleJSONEncoder().default((1, "test"))
   

# Generated at 2022-06-12 23:16:32.392228
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault

    json_string = json.dumps('string')
    assert(json_string == AnsibleJSONEncoder().default('string'))

    json_vault = json.dumps({'__ansible_vault': vault.encrypt('test')})
    assert(json_vault == AnsibleJSONEncoder().default(vault.VaultLib('test')))