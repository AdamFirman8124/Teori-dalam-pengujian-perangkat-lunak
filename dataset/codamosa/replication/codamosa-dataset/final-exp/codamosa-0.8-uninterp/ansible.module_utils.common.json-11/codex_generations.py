

# Generated at 2022-06-12 23:06:37.647677
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj1 = AnsibleJSONEncoder().encode('foo')
    assert obj1 == "\"foo\""
    from ansible.parsing.vault import VaultEditor
    obj2 = AnsibleJSONEncoder().encode(VaultEditor('password', 'salt', 'salt', 1)).strip()
    assert obj2 == '{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256;salt\\nsalt"}'


# Generated at 2022-06-12 23:06:46.737456
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    e = AnsibleJSONEncoder()
    assert '__ansible_unsafe' in e.default('foo')
    assert '__ansible_unsafe' in e.default(u'foo')
    assert '__ansible_vault' in e.default(VaultLib().encrypt('foo'))
    assert '__ansible_unsafe' in e.default(u'foo')
    assert e.default(dict(foo='bar')) == {'foo': 'bar'}
    assert e.default(datetime.date(2019, 1, 1)) == '2019-01-01'
    assert e.default(datetime.datetime(2019, 1, 1, 13, 37, 13)) == '2019-01-01T13:37:13'


#

# Generated at 2022-06-12 23:06:57.645936
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:07:04.424862
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    '''
    Test for method `default` of class `AnsibleJSONEncoder`
    '''

    # Tested with python 3.6.9

    # Test case - 1

    assert AnsibleJSONEncoder().default('abc') == 'abc'

    # Test case - 2

    assert AnsibleJSONEncoder().default(b'abc') == 'abc'

    # Test case - 3

    assert AnsibleJSONEncoder().default(u'abc') == 'abc'

    # Test case - 4


# Generated at 2022-06-12 23:07:14.574048
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    from ansible.parsing.vault import VaultSecret
    vault_obj = VaultSecret(b'encrypted')
    assert encoder.default(vault_obj) == {'__ansible_vault': 'encrypted'}
    assert encoder.default(vault_obj._ciphertext) == 'encrypted'

    from ansible.module_utils.six import string_types
    class AnsibleUnsafe(string_types[0]):
        __UNSAFE__ = True

    unsafe_obj = AnsibleUnsafe('unsafe')
    assert encoder.default(unsafe_obj) == {'__ansible_unsafe': 'unsafe'}
    assert encoder.default(unsafe_obj._ciphertext) == 'unsafe'

   

# Generated at 2022-06-12 23:07:17.680632
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_obj = {}
    encoder = AnsibleJSONEncoder()
    # Call default method
    encoder.default(test_obj)
    # Call default method with __ENCRYPTED__ argument
    encoder.default(test_obj, __ENCRYPTED__=True)


# Generated at 2022-06-12 23:07:23.315791
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    ansible_json_encoder = AnsibleJSONEncoder()
    o_vault = VaultSecret('AES256', 'mykey', None)
    o_vault.set_encrypted_data('y6BzsGp8sRRSzsZ+bcBZ9qe3r8B3EwBk')
    o_vault = VaultLib('mykey').load(o_vault._ciphertext)
    o_unsafe = AnsibleUnsafe('mypassword')
    o_datetime = datetime.datetime.now()
    assert ansible_json_encoder.default(o_vault)

# Generated at 2022-06-12 23:07:34.131280
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test for mapping type
    from ansible.module_utils.basic import AnsibleModule, return_values
    from ansible.module_utils.six import iteritems
    ansible_module = AnsibleModule(argument_spec={})
    assert isinstance(ansible_module.return_values, dict)

    encoded_dict = AnsibleJSONEncoder().default(ansible_module.return_values)
    assert isinstance(encoded_dict, dict)
    for key, value in iteritems(encoded_dict):
        assert key in list(return_values), \
            'Key \"{0}\" is not in dictionary returned by return_values method of AnsibleModule'.format(key)

# Generated at 2022-06-12 23:07:40.308840
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.module_utils.six import string_types

    # check that AnsibleUnsafe objects are not encoded as strings by default
    for unsafe in (AnsibleUnsafeBytes(b'some_val'), AnsibleUnsafeText(u'some_val')):
        assert isinstance(AnsibleJSONEncoder().encode(unsafe), string_types) is True

    # check that AnsibleVaultEncryptedUnicode objects are not encoded as strings by default
    vault_lib = VaultLib(password=None)
    vault_secret = VaultSecret(data=None, vault_id=None, vault_password=None, _vault_lib=vault_lib)
    vault_secret._ciphertext = b'vaulted'

# Generated at 2022-06-12 23:07:51.811111
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    # Vaulted string.
    v = ansible.parsing.vault.VaultLib('foo')
    s = 'bar'
    s_vault = v.encrypt(s)

# Generated at 2022-06-12 23:08:04.352843
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    case1 = {
        'key1': 'value1',
        'key2': {'a': '1', 'b': '2'}
    }
    assert encoder.default(case1) == case1

    case2 = {
        'key1': 'value1',
        'key2': AnsibleUnsafe('password')
    }
    assert encoder.default(case2) == {
        'key1': 'value1',
        'key2': {
            '__ansible_unsafe': u'password'
        }
    }

    case3 = AnsibleUnsafe(1)
    assert encoder.default(case3) == {
        '__ansible_unsafe': u'1',
    }

# Generated at 2022-06-12 23:08:14.914737
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test default encoding
    ansible_json_encoder = AnsibleJSONEncoder()
    # We test all types here as it is the only place we do so as the default method is called by
    # both dumps and list encoding.
    o = ansible_json_encoder.default(42)
    assert o == 42

    o = ansible_json_encoder.default(True)
    assert o is True

    o = ansible_json_encoder.default('foobar')
    assert o == 'foobar'

    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultAES256CBC
    from ansible.parsing.vault import VaultAES256GCM

# Generated at 2022-06-12 23:08:24.691966
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test with an AnsibleVaultEncryptedUnicode
    test_encrypted_unicode = '$ANSIBLE_VAULT;1.1;AES256;blahblahblah\n3636363\n'
    test_obj = AnsibleJSONEncoder()
    assert test_obj.default('test') == 'test'
    assert test_obj.default(test_encrypted_unicode) == {'__ansible_vault': u'$ANSIBLE_VAULT;1.1;AES256;blahblahblah\n3636363\n'}

    # Test with an AnsibleUnsafeText
    test_unsafe_text = 'test'
    test_obj = AnsibleJSONEncoder()
    assert test_obj.default(test_unsafe_text) == 'test'

    # Test with a

# Generated at 2022-06-12 23:08:34.473656
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('') == ''
    assert AnsibleJSONEncoder().default(123) == 123
    assert AnsibleJSONEncoder().default(True) is True
    assert AnsibleJSONEncoder().default(False) is False
    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default({
        'a': 'b',
    }) == {'a': 'b'}
    assert AnsibleJSONEncoder().default([1, 'a']) == [1, 'a']
    assert AnsibleJSONEncoder().default(dict(a=1, b=2)) == {'a': 1, 'b': 2}

# Generated at 2022-06-12 23:08:44.431025
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    vault_text = b'$ANSIBLE_VAULT;1.1;AES256;my_account;my_account\nmy_vault_text'
    vault = VaultLib([b'password'])
    vault_object = vault.decrypt(vault_text)
    #
    date_obj = datetime.date(2019, 9, 11)
    #
    # Simple test: List of random types
    random_obj_list = [1, True, None, 1.0, 'string', ['list'], {'dict': '0'}, date_obj, vault_object]
    # Create JSON encoder
    json_encoder = AnsibleJSONEncoder()
    #
    for x in random_obj_list:
        json_

# Generated at 2022-06-12 23:08:54.920373
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import text_type
    from ansible.parsing.vault import VaultSecret

    ansible_json_encoder = AnsibleJSONEncoder()

    # Test cryptographic object
    o = VaultSecret(b"abcde!12345")
    assert isinstance(ansible_json_encoder.default(o), dict)
    assert isinstance(ansible_json_encoder.default(o)['__ansible_vault'], text_type)

    # Test date and time object
    o = datetime.date(2017,12,24)
    assert isinstance(ansible_json_encoder.default(o), text_type)

    # Test default object
    assert ansible_json_encoder.default("abc") == "abc"
    assert ansible_json_encoder.default

# Generated at 2022-06-12 23:09:02.000498
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps(dict(a=[1, 2, 3], b=[1, 2]))) == AnsibleJSONEncoder().default(dict(a=[1, 2, 3], b=[1, 2]))
    assert json.loads(json.dumps(1.0)) == AnsibleJSONEncoder().default(1.0)
    assert json.loads(json.dumps(1)) == AnsibleJSONEncoder().default(1)
    assert json.loads(json.dumps("1")) == AnsibleJSONEncoder().default("1")
    assert json.loads(json.dumps("1.0")) == AnsibleJSONEncoder().default("1.0")
    assert json.loads(json.dumps("true")) == AnsibleJSONEncoder().default("true")

# Generated at 2022-06-12 23:09:09.695637
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_output = AnsibleJSONEncoder().encode([0, 1, 1, 2, 3, 5, 8, 13])
    assert list(json.loads(json_output)) == [0, 1, 1, 2, 3, 5, 8, 13]

    json_output = AnsibleJSONEncoder().encode("test")
    assert json_output == '"test"'

    json_output = AnsibleJSONEncoder().encode({'key': 'value'})
    assert json.loads(json_output) == {'key': 'value'}

# Generated at 2022-06-12 23:09:15.879022
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.vault import VaultSecret

    json_object = AnsibleJSONEncoder().default(to_bytes('string'))
    assert json_object == 'string'

    json_object = AnsibleJSONEncoder().default(VaultSecret('D'))
    assert json_object == {'__ansible_vault': 'D'}

# Generated at 2022-06-12 23:09:24.030795
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    text = AnsibleJSONEncoder().encode("{{Test}}")
    assert text == "{{Test}}"

    text = AnsibleJSONEncoder().encode("{{Test}}".__UNSAFE__)
    assert text == "{{Test}}"

    text = AnsibleJSONEncoder().encode("{{Test}}".__ENCRYPTED__)
    assert text == "{{Test}}"

    text = AnsibleJSONEncoder().encode({"Test": "One", "Two": "Three"})
    assert text == '{"Test": "One", "Two": "Three"}'

    text = AnsibleJSONEncoder().encode({"Test": "One".__UNSAFE__, "Two": "Three"})
    assert text == '{"Test": "One", "Two": "Three"}'

# Generated at 2022-06-12 23:09:43.131457
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe_str = 'foo'

    # When use default method of class AnsibleJSONEncoder, if o is an object of class AnsibleUnsafe,
    # it will return o.__UNSAFE__
    unsafe_value = AnsibleJSONEncoder().default(unsafe_str)

    assert(unsafe_value is not unsafe_str)
    assert(unsafe_value == 'foo')

    # When use default method of class AnsibleJSONEncoder, if o is an object of class string,
    # it will return the original value of string
    safe_value = AnsibleJSONEncoder().default('this is a safe value')

    assert(safe_value == 'this is a safe value')

    # When use default method of class AnsibleJSONEncoder, if o is not a string object,
    # it will return the original value of o
   

# Generated at 2022-06-12 23:09:49.264584
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import text_type
    # this is a mostly bogus test as the AnsibleJSONEncoder is just a re-implementation of the default
    # json encoder and we don't actually have any custom python types that it would apply to
    a_type = type('AnsibleType', (text_type, ), {})
    a = a_type(u'test')
    aje = AnsibleJSONEncoder()
    b = aje.default(a)
    assert isinstance(b, text_type)
    assert 'test' == b


# Generated at 2022-06-12 23:09:53.148811
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(datetime.date(2012, 12, 12)) == '2012-12-12'
    assert encoder.default(datetime.datetime(2012, 12, 12)) == '2012-12-12T00:00:00'

# Generated at 2022-06-12 23:09:58.094635
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    assert json_encoder.default(['a', 'b', 'c']).__class__ is list
    assert json_encoder.default(('a', 'b', 'c')).__class__ is list
    assert json_encoder.default(('a', 'b', 'c')) == ['a', 'b', 'c']



# Generated at 2022-06-12 23:10:06.123618
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default({'dict': "dict"}) == {'dict': "dict"}
    assert encoder.default({"list": ["item1", "item2"]}) == {"list": ["item1", "item2"]}
    assert encoder.default(datetime.datetime(year=2018, month=1, day=1, hour=1, minute=1, second=1, tzinfo=None)) == '2018-01-01T01:01:01'
    assert encoder.default(datetime.date(year=2018, month=1, day=1)) == '2018-01-01'
    assert encoder.default(1) == 1
    assert encoder.default(None) == None
    assert encoder.default(True) == True


# Generated at 2022-06-12 23:10:14.514070
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import u

    # simple test with unsafe string
    class AnsibleUnsafe(str):
        __UNSAFE__ = True

    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(AnsibleUnsafe('abc')) == {u'__ansible_unsafe': u'abc'}
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(AnsibleUnsafe('abc')) == {u'__ansible_unsafe': u'abc'}

    # simple test with vault string
    class AnsibleVault(str):
        __ENCRYPTED__ = True


# Generated at 2022-06-12 23:10:25.757308
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256

    # Test for normal string
    value = 'string'
    encoder = AnsibleJSONEncoder()
    result = encoder.default(value)
    assert result == 'string'

    value = 1
    result = encoder.default(value)
    assert result == 1

    # Test for VaultSecret object
    secret = VaultSecret('secret')
    encrypted_secret = VaultAES256.encrypt(secret, b'123456')
    value = encrypted_secret
    result = encoder.default(value)

# Generated at 2022-06-12 23:10:35.572920
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    assert j.default('') == ''
    assert j.default(None) is None
    assert j.default(False) == False
    assert j.default(True) == True
    assert j.default(-1) == -1
    assert j.default(0) == 0
    assert j.default(1) == 1
    assert j.default('test') == 'test'
    assert j.default(u'test') == u'test'
    assert j.default([1, 2]) == [1, 2]
    assert j.default({1: 'a'}) == {1: 'a'}

    assert j.default(datetime.date.today()) == datetime.date.today().isoformat()
    assert j.default(datetime.datetime.now()) == datetime.dat

# Generated at 2022-06-12 23:10:39.183211
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    encoder = AnsibleJSONEncoder()
    assert encoder.default(AnsibleVaultEncryptedUnicode(b'x')) == {'__ansible_vault': 'x'}

# Generated at 2022-06-12 23:10:49.184404
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a_encoder = AnsibleJSONEncoder()
    assert a_encoder.default([]) == []
    assert a_encoder.default((1, 2, 3)) == [1, 2, 3]
    assert a_encoder.default([1]) == [1]
    assert a_encoder.default((1,)) == [1]
    assert a_encoder.default(set()) == list(set())
    assert a_encoder.default(frozenset()) == list(frozenset())
    assert a_encoder.default({}) == {}
    assert a_encoder.default({'a': 1}) == {'a': 1}
    assert a_encoder.default('') == ''
    assert a_encoder.default(u'') == u''
    assert a_encoder.default(1)

# Generated at 2022-06-12 23:11:10.069337
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Check  object is an instance of its class
    encoder = AnsibleJSONEncoder()
    assert isinstance(encoder, AnsibleJSONEncoder)
    assert encoder.default("Hello") == "Hello"


# Generated at 2022-06-12 23:11:19.619377
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault.VaultLib import VaultLib
    from ansible.parsing.vault import VaultSecret

    assert json.loads(json.dumps(VaultSecret('value'), cls=AnsibleJSONEncoder, ensure_ascii=False)) == {'__ansible_vault': 'value'}


# Generated at 2022-06-12 23:11:24.208012
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils import six
    json.dumps([six.u('☃')], cls=AnsibleJSONEncoder)
    # TODO: Should this assert be added?
    #assert False, 'AnsibleJSONEncoder.default-test not implemented'


# Generated at 2022-06-12 23:11:34.595525
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This is a test, built to test the effect of the default method of class AnsibleJSONEncoder
    # against some test input
    import datetime
    import dateutil.parser
    import dateutil.tz
    class test_mapping(Mapping):
        def __len__(self):
            return 1
        def __iter__(self):
            return iter(['key'])
        def __getitem__(self, key):
            return 'value'

# Generated at 2022-06-12 23:11:42.232939
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    vault = VaultLib([])
    unsafe = AnsibleUnsafe('unsafe')
    vaulted = vault.encrypt(unsafe)

    test_encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:11:49.194922
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    d1 = dict(a=1,b=2,c='str',d=dict(a=1))
    d2 = dict(a=1,b=2,c='str',d=dict(a=1),e=dict(z=5))

    result1 = AnsibleJSONEncoder(sort_keys=True, indent=4).default(d1)
    result2 = AnsibleJSONEncoder(sort_keys=True, indent=4, preprocess_unsafe=True).default(d1)
    result3 = AnsibleJSONEncoder(sort_keys=True, indent=4, preprocess_unsafe=True).default(d2)


# Generated at 2022-06-12 23:11:59.006386
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # An instance of AnsibleJSONEncoder
    _encoder = AnsibleJSONEncoder()

    # An instance of datetime.date
    _date = datetime.date(2018, 12, 1)

    # An instance of datetime.date
    _datetime = datetime.datetime(2018, 12, 1, 17, 23, 59)

    # A dict
    _dict = { "complex": { "complex": { "complex": "a" } } }

    # A simple string
    _str = "string"

    expected_result = {
        _date: '2018-12-01',
        _datetime: '2018-12-01T17:23:59',
        _dict: '{"complex": {"complex": {"complex": "a"}}}',
        _str: '"string"'
    }


# Generated at 2022-06-12 23:12:00.131382
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(1) == 1


# Generated at 2022-06-12 23:12:10.462645
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.constants as C
    from ansible.parsing.vault import VaultEditor

    # Create test data for input to method default (two items of type VaultEditor, one of type Dict)
    data = [VaultEditor(password=C.DEFAULT_VAULT_PASSWORD), VaultEditor(password=C.DEFAULT_VAULT_PASSWORD), {"key1":"value1", "key2":"value2"}]
    # Create instance of AnsibleJSONEncoder class
    json_encoder = AnsibleJSONEncoder()
    # Encode data
    data_encoded = json_encoder.encode(data)
    # Decode data
    data_decoded = json.loads(data_encoded)
    # Test the values of the decoded data

# Generated at 2022-06-12 23:12:19.371545
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(42) == 42
    assert AnsibleJSONEncoder().default('some string') == 'some string'
    # JSONEncoder cannot handle UTF-8 characters in strings.  This can be fixed by
    # adding the following to the general outputter.  The UTF-8 is the Euro symbol
    # Python 2.6 or 2.7:
    # import json
    # import sys
    # if sys.version_info[0] < 3:
    #     import codecs
    #     import locale
    #     encoding = locale.getpreferredencoding()
    #     sys.stdout = codecs.getwriter(encoding)(sys.stdout, 'strict')
    # else:
    #     import io
    #     sys.stdout = io.TextIOWrapper(sys.stdout.

# Generated at 2022-06-12 23:12:44.904242
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib  # pylint: disable=wrong-import-position
    from ansible.module_utils.basic import AnsibleUnsafe  # pylint: disable=wrong-import-position

    vault_password = 'ansible'

    vault = VaultLib([vault_password])
    vaulttext = vault.encrypt('value')
    vaultobject = vault.decrypt(vaulttext)
    unsafe = AnsibleUnsafe('value')

    encoder = AnsibleJSONEncoder()
    assert encoder.default(vaulttext) == vaulttext
    # vault.encrypt() always returns a string
    assert isinstance(vaulttext, str)
    assert isinstance(vaultobject, str)

# Generated at 2022-06-12 23:12:46.536328
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a_obj = AnsibleJSONEncoder().default(None)
    assert a_obj == 'null'

# Generated at 2022-06-12 23:12:56.604003
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default(0) == 0
    assert AnsibleJSONEncoder().default(1.1) == 1.1
    assert AnsibleJSONEncoder().default('hello') == 'hello'
    assert AnsibleJSONEncoder().default(u'hello') == u'hello'
    assert AnsibleJSONEncoder().default(list()) == list()
    assert AnsibleJSONEncoder().default(dict()) == dict()
    assert AnsibleJSONEncoder().default(AnsibleUnsafe(u'good')) == {'__ansible_unsafe': 'good'}

# Generated at 2022-06-12 23:13:03.457154
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    valStr = "unsafeValue"
    valUnsafeDict = {"__ansible_unsafe": valStr}
    valVaultStr = "vaultValue"
    valVaultDict = {"__ansible_vault": valVaultStr}
    valVaultObj = object()
    valVaultObj._ciphertext = valVaultStr.encode()
    valVaultObj.__ENCRYPTED__ = True

    encoder = AnsibleJSONEncoder()
    assert encoder.default("value") == "value"
    assert encoder.default("value".encode("utf-8")) == "value".encode("utf-8")
    assert encoder.default(valStr) == valStr
    assert encoder.default(valUnsafeDict) == valUnsafeDict
    assert encoder.default

# Generated at 2022-06-12 23:13:08.117762
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.six import text_type
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean

    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import dict_diff
    from ansible.module_utils.network.common.utils import replace_list
    from ansible.module_utils.network.common.utils import remove_empties

    # Test passing Mapping as input to method default
    assert AnsibleJSONEncoder().default(boolean("true")) == boolean("true")

    # Test passing Connection as input to method default

# Generated at 2022-06-12 23:13:17.172184
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.urls import url_argument_spec
    from ansible.module_utils.urls import AnsibleUnsafeUrl, AnsibleUnsafeText
    from ansible.module_utils.urls import AnsibleUnsafeBytes
    from ansible.module_utils.urls import AnsibleUnsafe, AnsibleUnsafeJson

    # Test unsafe types
    encoder = AnsibleJSONEncoder()
    assert encoder.default(AnsibleUnsafeText('foo')) == {'__ansible_unsafe': u'foo'}
    assert encoder.default(AnsibleUnsafeBytes(b'foo')) == {'__ansible_unsafe': u'foo'}

# Generated at 2022-06-12 23:13:27.978244
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import text_type
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    encoder = AnsibleJSONEncoder()
    vault = 'my secret'
    vault_safe = VaultLib([])
    vault_safe.decrypt(vault)
    hostvars = {'key1': 'value1', 'key2': 'value2'}

    assert encoder.default(vault_safe) == {'__ansible_vault': vault}
    assert encoder.default(hostvars) == hostvars

# Generated at 2022-06-12 23:13:32.080914
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test the datetime
    now = datetime.datetime.now()
    assert isinstance(AnsibleJSONEncoder().default(now), str)

    # Test the mapping
    mapping = {'key': 'value'}
    assert AnsibleJSONEncoder().default(mapping) == mapping

    # Test the vault
    vault = 'test_vault'
    unsafe = AnsibleJSONEncoder().default(vault)
    assert unsafe == vault

# Generated at 2022-06-12 23:13:38.798634
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    vault = VaultLib('secret')

# Generated at 2022-06-12 23:13:50.812844
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common import make_vault_password
    from ansible.module_utils.common.collections import is_sequence
    import ansible.module_utils.basic
    import ansible.parsing.dataloader
    import datetime

    # Test 'default' method of AnsibleJSONEncoder class

    # Test case: vault object
    vault = make_vault_password('This is a vault password')
    basic_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    basic_module._ansible_vault = ansible.parsing.dataloader.DataLoader()
    basic_module.no_log = True
    basic_module._ansible_no_log = True
    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:32.855282
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    import pytest
    class o():
        def __init__(self,v):
            self.v=v
        def __repr__(self):
            return '<AnsibleJSONEncoder.test_AnsibleJSONEncoder_default.o>'
    assert AnsibleJSONEncoder().default(o('One')) == 'One'
    assert AnsibleJSONEncoder().default(datetime.date.today()) == datetime.date.today().isoformat()
    assert AnsibleJSONEncoder().default(datetime.datetime.utcnow()) == datetime.datetime.utcnow().isoformat()


# Generated at 2022-06-12 23:14:36.873703
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import datetime

    # import class in order to test
    from ansible.parsing.ajson import AnsibleJSONEncoder

    mystring = AnsibleJSONEncoder.default(AnsibleJSONEncoder(), datetime.datetime(2017,5,5,5,5,5,5))
    assert mystring == '2017-05-05T05:05:05.000005'

# Generated at 2022-06-12 23:14:45.858246
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    This tests the AnsibleJSONEncoder's default method.
    '''
    from ansible.module_utils.common._json_compat import AnsibleUnsafeText
    from ansible.module_utils.common._json_compat import AnsibleUnsafeBytes
    from ansible.parsing.vault import VaultLib

    # test it doesn't error on the base types
    ansible_encoder = AnsibleJSONEncoder()
    test = ansible_encoder.default(10)
    assert test == 10
    test = ansible_encoder.default('10')
    assert test == '10'
    # test list
    test = ansible_encoder.default(['10'])
    assert test == ['10']
    # test dict

# Generated at 2022-06-12 23:14:54.747714
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    test_vault = VaultLib(b'SECRET')
    test_vault_cipher = test_vault.encrypt(b'test')
    test_vault_object = to_bytes(test_vault_cipher, errors='surrogate_or_strict')

    assert AnsibleJSONEncoder().default(test_vault_object) == {'__ansible_vault': test_vault_cipher}
    assert AnsibleJSONEncoder(vault_to_text=True).default(test_vault_object) == test_vault_cipher

# Generated at 2022-06-12 23:15:04.351360
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    date = datetime.datetime(2019, 2, 7, 13, 58, 24, 273953)

# Generated at 2022-06-12 23:15:11.973394
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe = '$foo'
    vault = '$ANSIBLE_VAULT;1.2;AES256;foo\nbar\n'
    date = datetime.date(2000, 1, 2)
    datetime = datetime.datetime(2000, 1, 2, 3, 4, 5)

    json_encoder = AnsibleJSONEncoder()
    assert(json_encoder.default(unsafe) is unsafe)
    assert(json_encoder.default(vault)['__ansible_vault'] == vault)
    assert(json_encoder.default(date) == '2000-01-02')
    assert(json_encoder.default(datetime) == '2000-01-02T03:04:05.000000')

# Generated at 2022-06-12 23:15:20.110417
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:15:30.907312
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    test_data = {
        'date': datetime.date(2000, 1, 1),
        'datetime': datetime.datetime(2000, 1, 1, 10, 30),
        'mapping': {'a': 1},
        'sequence': [1, 2, 3],
        'unsafe': 'correct horse',
        'vault': 'correct battery staple',
    }

    def _assert(o, expected):
        actual = ansible_json_encoder.default(o)
        assert expected == actual

    for k, v in test_data.items():
        _assert(v, v)

# Generated at 2022-06-12 23:15:40.969738
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # input
    class MockClass:
        def __init__(self, obj):
            self.__ansible_vault = obj

    # run method
    safe_password = ansible_json_encoder.AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert safe_password.default(safe_password) == "{'__ansible_vault': 'preprocess_unsafe=False, vault_to_text=False'}"

    for preprocess_unsafe in (True, False):
        for vault_to_text in (True, False):
            ansible_json_encoder.AnsibleJSONEncoder(preprocess_unsafe=preprocess_unsafe, vault_to_text=vault_to_text)

# Generated at 2022-06-12 23:15:47.317529
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    data = {
        'date_obj': datetime.datetime(2020, 3, 3),
        'dict_obj': encoder.default({'key': 'value'}),
        'str_obj': encoder.default('string'),
        'int_obj': encoder.default(123),
    }

    assert data == {
        'date_obj': '2020-03-03T00:00:00',
        'dict_obj': {'key': 'value'},
        'str_obj': 'string',
        'int_obj': 123,
    }