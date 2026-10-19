

# Generated at 2022-06-12 23:06:45.850486
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # check date time encode
    time = datetime.datetime(2019, 2, 21, 12, 14, 23, 1234)
    assert AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default(time) == time.isoformat()

    # check string encode
    assert AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default('test') == 'test'

    # check int encode
    assert AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default(10) == 10

    # check float encode
    assert AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False).default(10.12) == 10.12

    # check hostvars encode

# Generated at 2022-06-12 23:06:53.257142
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Set up data objects.
    safe_str = 'foo'
    unsafe_str = AnsibleUnsafe(safe_str)
    # Validate encoder for string.
    encoder = AnsibleJSONEncoder()
    assert encoder.encode(safe_str) == '"foo"'
    assert encoder.encode(unsafe_str) == '"foo"'
    # Validate encoder for list.
    safe_list = [safe_str]
    unsafe_list = [unsafe_str]
    assert encoder.encode(safe_list) == '["foo"]'
    assert encoder.encode(unsafe_list) == '["foo"]'
    # Validate encoder for list with nested list.
    safe_nested_list = [[safe_str]]

# Generated at 2022-06-12 23:07:04.177149
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from datetime import date
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault = VaultLib(None)
    enc = AnsibleJSONEncoder()

    assert enc.default(vault.encrypt("dummy")) == {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;dummy\n...==\n'}
    assert enc.default(AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256;dummy\n...==\n")) == {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256;dummy\n...==\n'}

# Generated at 2022-06-12 23:07:09.101676
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    key_name="__ansible_vault"
    value="vault value"
    ansible_vault=_AnsibleVault(value)
    test_dict={key_name:value}
    ansible_json_encoder=AnsibleJSONEncoder()
    assert ansible_json_encoder.default(ansible_vault) == test_dict


# Generated at 2022-06-12 23:07:18.072044
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes
    test_vault = VaultLib([])

# Generated at 2022-06-12 23:07:21.899445
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansibleUnsafeJson = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True).encode('AnsibleUnsafeString')

    assert ansibleUnsafeJson == '"AnsibleUnsafeString"'



# Generated at 2022-06-12 23:07:33.005221
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import time
    import datetime
    import base64
    import random

    encoding = 'ascii'
    vault_password = 'hello'

    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    # Date
    now = datetime.datetime.now()
    assert encoder.default(now) == now.isoformat()
    assert encoder.default(now) != time.mktime(now.timetuple())

    # Time
    now = datetime.datetime.now()
    assert encoder.default(now) == now.isoformat()
    assert encoder.default(now) != time.mktime(now.timetuple())

    # Vault

# Generated at 2022-06-12 23:07:38.792820
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import base64
    text = 'Text for testing'
    vault = VaultLib([])
    encrypted = vault.encrypt(text)
    assert encrypted != text

    encoder = AnsibleJSONEncoder()
    o = base64.b64decode(encrypted.encode('utf-8'))
    assert encoder.default(o) == {"__ansible_vault": encrypted}

    o = base64.b64decode(encrypted.encode('utf-8'))
    o = AnsibleVaultEncryptedUnicode(o)
    assert encoder.default(o) == {"__ansible_vault": encrypted}

# Generated at 2022-06-12 23:07:43.539820
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.dumps(dict(a=1), cls=AnsibleJSONEncoder) == '{"a": 1}'
    assert json.dumps('val', cls=AnsibleJSONEncoder) == '"val"'
    assert json.dumps(["val","val2"], cls=AnsibleJSONEncoder) == '["val", "val2"]'
    assert json.dumps({'a': 'val'}, cls=AnsibleJSONEncoder) == '{"a": "val"}'

# Generated at 2022-06-12 23:07:52.144630
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # TODO: move this to a test class for AnsibleJSONEncoder
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.collections import AnsibleVaultEncryptedUnicode

    plaintext = 'foobar'
    vault_password = 'vault-password'
    vault_bytes = VaultLib(vault_password).encrypt(plaintext)
    vault = AnsibleVaultEncryptedUnicode(vault_bytes, vault_password)
    json.dumps(vault, cls=AnsibleJSONEncoder)
    # TODO: assert something

# Generated at 2022-06-12 23:08:03.720662
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    ''' Basic test class to test the default method of class AnsibleJSONEncoder
    '''

    class TestDefault:
        def __init__(self):
            self.hello = "world"
            self.foo = "bar"

        def __getitem__(self, index):
            if isinstance(index, int):
                raise IndexError(index)

            return self.__dict__[index]

    test_object = TestDefault()
    json.dumps(test_object, cls=AnsibleJSONEncoder)



# Generated at 2022-06-12 23:08:05.624703
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode({'foo': 'bar'}) == '{"foo": "bar"}'


# Generated at 2022-06-12 23:08:06.722298
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    pass


# Generated at 2022-06-12 23:08:17.174562
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    e = AnsibleJSONEncoder()

    # default behavior
    assert e.default('test') == 'test'
    assert e.default(1) == 1

    # AnsibleVault objects
    class AnsibleVault1:
        __ENCRYPTED__ = True
        _ciphertext = b'test'

    assert e.default(AnsibleVault1) == {'__ansible_vault': 'test'}

    # AnsibleVault's subclass
    class AnsibleUnsafe1(AnsibleVault1):
        __UNSAFE__ = True

    assert e.default(AnsibleUnsafe1) == {'__ansible_unsafe': 'test'}

    # AnsibleUnsafe object
    class AnsibleUnsafe2:
        __UNSAFE__ = True

    assert e.default

# Generated at 2022-06-12 23:08:26.194928
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.parsing.convert_bool import boolean

    def _to_text(value, errors='surrogate_or_strict', nonstring='strict'):
        if isinstance(value, string_types):
            return to_text(value, errors=errors, nonstring=nonstring)
        elif isinstance(value, Mapping):
            return dict((_to_text(k, errors=errors, nonstring=nonstring),
                         _to_text(v, errors=errors, nonstring=nonstring))
                        for k, v in value.iteritems())

# Generated at 2022-06-12 23:08:35.892806
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    text = 'test'
    obj_text = AnsibleUnsafe(text)
    assert '__ansible_unsafe' in AnsibleJSONEncoder().default(obj_text)
    assert '__ansible_vault' in AnsibleJSONEncoder().default(AnsibleVaultEncryptedUnicode(text))
    assert '__ansible_vault' in AnsibleJSONEncoder(vault_to_text=True).default(AnsibleVaultEncryptedUnicode(text))
    assert '__ansible_unsafe' in AnsibleJSONEncoder().default(AnsibleVaultEncryptedUnicode(obj_text))
    assert '__ansible_unsafe' in AnsibleJSONEncoder(vault_to_text=True).default(AnsibleVaultEncryptedUnicode(obj_text))

   

# Generated at 2022-06-12 23:08:38.572975
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    out = AnsibleJSONEncoder().default(
        {
            'nested': {
                'attr': 'val'
            }
        }
    )
    assert out['nested']['attr'] == 'val'

# Generated at 2022-06-12 23:08:41.111972
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    value = AnsibleJSONEncoder().default(dict({'a': 2}))
    assert 'a' in value
    assert value['a'] == 2


# Generated at 2022-06-12 23:08:45.052630
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = {'foo': 4, 'bar': 'baz'}
    json_str = json.dumps(obj, cls=AnsibleJSONEncoder, sort_keys=True)
    assert json_str == '{"bar": "baz", "foo": 4}'

# Generated at 2022-06-12 23:08:54.720404
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    data = {'k1': 'v1',
            'k2': ansible.parsing.vault.VaultSecret('v2'),
            'k3': {'k3.1': ansible.parsing.vault.VaultSecret('v3'),
                   'k3.2': 'v4'}}
    ret = json.dumps(data, cls=AnsibleJSONEncoder)
    assert ret == '{"k1": "v1", "k2": {"__ansible_vault": "v2"}, "k3": {"k3.1": {"__ansible_vault": "v3"}, "k3.2": "v4"}}'

# Generated at 2022-06-12 23:09:06.935351
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    value = ansible_json_encoder.default('str')
    assert value == 'str'
    value = ansible_json_encoder.default([1,2,3])
    assert value == [1,2,3]
    value = ansible_json_encoder.default(1)
    assert value == 1


# Generated at 2022-06-12 23:09:12.697451
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    assert aje.default(datetime.datetime(2019, 11, 20)) == '2019-11-20T00:00:00'
    assert aje.default([1, 2, 3]) == [1, 2, 3]
    assert aje.default({'1': '2'}) == {'1': '2'}



# Generated at 2022-06-12 23:09:22.257447
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    encoder = AnsibleJSONEncoder()

    # test the various classes (return the instantiated class)
    assert encoder.default({}) == {}
    assert encoder.default(UserDict()) == {}
    assert encoder.default(VaultLib(to_bytes('test'), 1)) == 'test'

    # test the date and datetime objects
    assert encoder.default(datetime.date(2017, 2, 1)) == '2017-02-01'
    assert encoder.default(datetime.datetime(2017, 2, 1)) == '2017-02-01T00:00:00'

    # test

# Generated at 2022-06-12 23:09:27.679969
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_json_encoder = AnsibleJSONEncoder()
    assert test_json_encoder.default('test') == 'test'
    assert test_json_encoder.default(b'test') == 'test'
    assert test_json_encoder.default(dict(test=1)) == {'test': 1}
    assert test_json_encoder.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()


# Generated at 2022-06-12 23:09:33.009806
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class AnsibleVault(object):
        __ENCRYPTED__ = True

        def __init__(self, ciphertext):
            self._ciphertext = ciphertext
        def __str__(self):
            return "Vault(...)[{0}]".format(len(self._ciphertext))
        def __repr__(self):
            return self.__str__()


# Generated at 2022-06-12 23:09:43.674889
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class MyClass(object):
        def __init__(self, a, b):
            self._a = a
            self._b = b

    data = {'now': datetime.datetime.now(), 'date': datetime.date.today(), 'obj': MyClass(1, 2), 'dict': {'a': 1, 'b': 2}}
    ansible_json_encoder = AnsibleJSONEncoder()
    result = ansible_json_encoder.default(data)
    assert result['now'] == data['now'].isoformat()
    assert result['date'] == data['date'].isoformat()
    assert result['dict'] == data['dict']
    assert 'obj' in result
    assert result['obj']['_a'] == data['obj']._a

# Generated at 2022-06-12 23:09:46.283038
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    s = AnsibleJSONEncoder()
    assert s.default(None) == 'null'
    assert s.default(True) == 'true'
    assert s.default(False) == 'false'
    assert s.default('string') == '"string"'



# Generated at 2022-06-12 23:09:53.021649
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    encoder = AnsibleJSONEncoder()

    assert encoder.default(datetime.date(2001, 1, 1)) == "2001-01-01"
    assert encoder.default(datetime.datetime(2001, 1, 1, 0, 0)) == "2001-01-01T00:00:00"

    assert encoder.default(str('str')) == 'str'

    assert encoder.default(u'unicode') == u'unicode'

    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0

    assert encoder.default(True) == True
    assert encoder.default(False) == False
    assert encoder.default(None) == None

    assert encoder.default([1, 2, 3]) == [1, 2, 3]

   

# Generated at 2022-06-12 23:10:01.913121
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    from ansible.parsing.vault import VaultEditor, VaultSecret

    from ansible.module_utils.basic import AnsibleUnsafeText

    ansible_unencode_text_obj = AnsibleUnsafeText(u"Hello World")
    ansible_encode_text_obj = AnsibleUnsafeText(u"Vault Password", encrypted=True)

    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    o1 = encoder.default(ansible_unencode_text_obj)
    o2 = encoder.default(ansible_encode_text_obj)

    assert o1 == dict(__ansible_unsafe=u"Hello World")
    assert o2 == dict(__ansible_vault=u"Vault Password")

# Generated at 2022-06-12 23:10:06.368533
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default("str") == "str"
    assert encoder.default(u"unicode") == u"unicode"
    assert encoder.default({"a": "b"}) == {"a": "b"}
    assert encoder.default(["c", "d"]) == ["c", "d"]

# Generated at 2022-06-12 23:10:25.544472
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.formatters import string_to_bytes

    j = AnsibleJSONEncoder()
    assert isinstance(j.default(VaultLib([])), dict)
    assert isinstance(j.default(to_bytes('string')), str)
    assert isinstance(j.default(to_unicode('string')), str)
    assert isinstance(j.default(string_to_bytes('string')), str)

# Generated at 2022-06-12 23:10:35.281835
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib

    a_text = 'hello world'
    a_unsafe = AnsibleUnsafeText(a_text)
    a_unsafe._text = a_text
    a_vault = VaultLib('1111')

# Generated at 2022-06-12 23:10:42.091980
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test the default method of the AnsibleJSONEncoder class
    '''
    # convert to a dictionary and then back to a string
    import ansible.parsing.vault as vault
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    v = vault.VaultEncryptedUnicode('mysecret')
    assert encoder.default(v) == {'__ansible_vault': u'mysecret'}

    from ansible.utils.unsafe_proxy import AnsibleUnsafeString
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    v = AnsibleUnsafeString(b'mystring')
    assert encoder.default(v) == {'__ansible_unsafe': u'mystring'}

    # test that passing a hostvars object

# Generated at 2022-06-12 23:10:51.804684
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # class AnsibleUnsafe(str):
    #     __UNSAFE__ = True

    # class AnsibleVault(str):
    #     __ENCRYPTED__ = True

    # class AnsibleVaultText(str):
    #     __ENCRYPTED_TEXT__ = True

    # class AnsibleUnsafeBytes(str):
    #     __UNSAFE__ = True
    #     __BYTES__ = True

    test_ansible_unsafe_string = '{"__ansible_unsafe": "value"}'
    test_ansible_unsafe_string_json = {'__ansible_unsafe': 'value'}
    test_unsafe_string = 'value'

    test_ansible_vault_string = '{"__ansible_vault": "value"}'
    test_

# Generated at 2022-06-12 23:10:54.803612
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(u'unicode_str') == u'unicode_str'
    assert AnsibleJSONEncoder().default(b'byte_str') == u'byte_str'
    assert AnsibleJSONEncoder().default(123) == 123


# Generated at 2022-06-12 23:11:02.162262
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible import constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import u
    text = 'test'
    vault_text = VaultLib({}).encrypt(text)
    vault_text_utf8 = u(vault_text).encode('utf-8')

    # Basic
    encoder = AnsibleJSONEncoder()
    assert text == json.loads(encoder.encode(text))

    # Datetime
    now = datetime.datetime.now()
    now_str = now.isoformat()
    assert now_str == json.loads(encoder.encode(now))

    # Vault
    assert vault_text_utf8 == json.loads(encoder.encode(vault_text))['__ansible_vault']


# Generated at 2022-06-12 23:11:03.595242
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder().default(__file__)
    assert isinstance(result, str)


# Generated at 2022-06-12 23:11:13.505788
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:11:24.209067
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Tests the method default of class AnsibleJSONEncoder
    """
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible._vendor.six.moves.urllib_parse import quote
    from ansible.module_utils.common._collections_compat import OrderedDict

    vault_password = 'test'
    vault = VaultLib([(DEFAULT_VAULT_PASSWORD_FILE, VaultSecret(vault_password, vault_password))])
    vault_data = vault.encrypt(quote(vault_password))
    vault_secret_encoded = vault.encode(vault_password)
    unsafe_password = vault.en

# Generated at 2022-06-12 23:11:29.690142
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    assert AnsibleJSONEncoder().default(VaultLib([b'\xff' * 256])) == {'__ansible_vault': b'\xff' * 256}

    assert AnsibleJSONEncoder(vault_to_text=True).default(VaultLib([b'\xff' * 256])) == b'\xff' * 256

# Generated at 2022-06-12 23:12:00.652981
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    secret = VaultSecret('test')
    vault = VaultLib([secret])

    encoder = AnsibleJSONEncoder()
    ciphertext = encoder.default(vault)


# Generated at 2022-06-12 23:12:07.234809
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Structure
    obj = {"a": 10, "b": [1, 2, 3], "c": {"d": "e"}}

    # Encoder object
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    # Encode should not raise an error
    assert encoder.encode(obj) == json.JSONEncoder().encode(obj)

# Generated at 2022-06-12 23:12:14.517322
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This test case is created to check fix for Ansible issue ANSIBLE-9222
    # In this issue, the json.dumps function returns an error when it
    # is used with a datetime object
    # The AnsibleJSONEncoder class overrides the default() function of
    # json.JSONEncoder to accept datetime objects
    import datetime
    test_datetime = datetime.datetime(2017, 3, 2, 19, 0, 0)
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    result = encoder.default(test_datetime)
    assert result == "2017-03-02T19:00:00"

# Generated at 2022-06-12 23:12:21.938970
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars import AnsibleVaultEncryptedUnicode

    val = 1
    assert val == AnsibleJSONEncoder().encode(val)

    val = [
        'test list',
        b'bytes',
        u'unicode',
        AnsibleUnsafeText(b'\x00\x01\x02')
    ]
    assert repr(val) == AnsibleJSONEncoder().encode(val)

    val = AnsibleUnsafeText(b'\x00\x01\x02')
    assert repr(val) == AnsibleJSONEncoder().encode(val)

    val = AnsibleVaultEncryptedUnicode(b'\x00\x01\x02', 'test')

# Generated at 2022-06-12 23:12:32.625433
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    ansible_json_encoder = AnsibleJSONEncoder()

    # encode object with __ENCRYPTED__ attribute

# Generated at 2022-06-12 23:12:34.930676
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enc = AnsibleJSONEncoder()
    res = enc.default('AAA')
    assert res == 'AAA'
    res = enc.default(['AAA', 'BBB'])
    assert res == ['AAA', 'BBB']
    res = enc.default({'AAA': 1, 'BBB': 'CCC'})
    assert res == {'AAA': 1, 'BBB': 'CCC'}


# Generated at 2022-06-12 23:12:44.283118
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    mock_object = object()
    encoder = AnsibleJSONEncoder()
    # object is a builtin type
    assert encoder.default(object) == "<class 'object'>"
    # object is pre-defined python object
    assert encoder.default(mock_object) == mock_object
    # object is a dictionary
    assert encoder.default(dict(a=1, b=2)) == dict(a=1, b=2)
    # object is a list
    assert encoder.default(list((1,2,3))) == [1,2,3]
    # object is datetime.date
    assert encoder.default(datetime.date.today()) == datetime.date.today().isoformat()
    # object is datetime.datetime
    assert encoder.default(datetime.datetime.now())

# Generated at 2022-06-12 23:12:54.410625
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test the default method of the AnsibleJSONEncoder."""

    # Create a simple mappping object
    mapping = {"a": "b", "c": "d", "e": "f"}

    encoder = AnsibleJSONEncoder(sort_keys=False)

    # The function will return the same mapping object
    result = encoder.default(mapping)
    assert mapping == result

    # Create a ansible unsafe object
    from ansible.module_utils.basic import AnsibleUnsafe
    unsafe = AnsibleUnsafe("{this is a test}")

    # The function will return a dict
    result = encoder.default(unsafe)
    assert {"__ansible_unsafe": "{this is a test}"} == result

    # Create a ansible vault object
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-12 23:12:59.485794
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping

    res = AnsibleJSONEncoder().default({'a': 1})
    assert isinstance(res, dict)
    assert res['a'] == 1

    class Foo(Mapping):
        def __getitem__(self, key):
            return key
        def __iter__(self):
            return iter(['a'])
        def __len__(self):
            return 1

    res = AnsibleJSONEncoder().default(Foo())
    assert isinstance(res, dict)
    assert res['a'] == 'a'



# Generated at 2022-06-12 23:13:09.640007
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    vault_p = VaultLib({})

# Generated at 2022-06-12 23:13:55.506287
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    assert AnsibleJSONEncoder().encode(datetime.datetime.utcnow()) != None


# Generated at 2022-06-12 23:14:03.482264
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes
    from ansible.module_utils.common.vault import VaultLib

    vault1 = VaultLib(password='password').encrypt('Hello World')
    vault2 = VaultLib(password='password').encrypt(b'Hello World')


# Generated at 2022-06-12 23:14:13.607598
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(42) == 42
    assert AnsibleJSONEncoder().default('string') == 'string'
    assert AnsibleJSONEncoder().default(dict(x=42)) == {'x': 42}
    assert AnsibleJSONEncoder().default(datetime.datetime(2019, 12, 25)) == "2019-12-25T00:00:00"

    # Test that AnsibleJSONEncoder().default(o) for classes inheriting from string types
    # returns the result of o.__str__().
    # See https://stackoverflow.com/a/56117775/470844
    class TestClass(str): pass
    TestClass.__str__ = lambda self: 'overridden'
    assert AnsibleJSONEncoder().default(TestClass('test')) == 'overridden'

#

# Generated at 2022-06-12 23:14:22.654703
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Unit test for method default of class AnsibleJSONEncoder:
    # test with parameter ``o`` is an instance of AnsibleUnsafe

    import ansible.module_utils.common.unsafe_proxy

    class UnsafeClass(ansible.module_utils.common.unsafe_proxy.AnsibleUnsafe):
        def __init__(self, value=''):
            super(UnsafeClass, self).__init__(value)

        # define the to_text method
        def to_text(self, **kwargs):
            return to_text(self, **kwargs)

    # test with parameter ``o`` is an instance of AnsibleUnsafe
    unsafe_object = UnsafeClass()
    unsafe_object.__vault__ = 123456
    json_encoder = AnsibleJSONEncoder()
    assert json_encoder

# Generated at 2022-06-12 23:14:33.415879
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.safe_eval import ansible_safe_eval
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.encoding import unsafe_text

    fred = {'name': 'Fred', 'age': 88}
    george = {'name': 'George', 'age': 40}
    my_date = datetime.date(1999, 12, 31)


# Generated at 2022-06-12 23:14:40.750995
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # i.e., FOO=bar
    def _test(o):
        return AnsibleJSONEncoder().default(o)

    from ansible.parsing.vault import VaultLib
    assert _test(VaultLib()) == {'__ansible_vault': ''}

    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
    class MyUnsafe(AnsibleUnsafeBytes):
        pass
    assert _test(MyUnsafe(b'foorbar')) == {'__ansible_unsafe': 'foorbar'}

    assert _test('foorbar') == 'foorbar'
    assert _test(u'foorbar') == 'foorbar'

    # class HostVars(dict):
    #     pass
    # assert _test(HostVars({'foo':

# Generated at 2022-06-12 23:14:50.087469
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    def_dict = {'__ansible_vault': "fgfhfghfghgfhfghghfghf", '__ansible_unsafe': "afsdgsdgsdgsdg"}
    assert(encoder.default({'a': 'b'}) == {'a': 'b'})
    assert(encoder.default([]) == [])
    assert(encoder.default({}) == {})
    assert(encoder.default(getattr(encoder,'_UNSAFE_TOKENS')['vault']) == def_dict)
    assert(encoder.default(getattr(encoder,'_UNSAFE_TOKENS')['unsafe']) == def_dict)

# Generated at 2022-06-12 23:14:59.831402
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Vault:
        __ENCRYPTED__ = True
        _ciphertext = 'test'
    vault_obj = Vault()

    class Unsafe:
        __UNSAFE__ = True
        __ENCRYPTED__ = False
    unsafe_obj = Unsafe()

    dict_obj = dict(a='a')

    assert AnsibleJSONEncoder().default(vault_obj) == {'__ansible_vault': u'test'}
    assert AnsibleJSONEncoder(vault_to_text=True).default(vault_obj) == u'test'
    assert AnsibleJSONEncoder().default(unsafe_obj) == {'__ansible_unsafe': u''}
    assert AnsibleJSONEncoder().default(dict_obj) == dict_obj

# Generated at 2022-06-12 23:15:04.928960
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from dateutil import tz
    from dateutil.parser import parse
    from ansible.parsing.vault import VaultLib

    # ansible_date
    ansible_date = parse('1970-01-01 00:00:01', tzinfos=tz.tzutc)
    assert type(json.dumps(ansible_date, cls=AnsibleJSONEncoder)) == str
    assert type(json.dumps(ansible_date, cls=AnsibleJSONEncoder, preprocess_unsafe=True)) == str

    # ansible_datetime
    ansible_datetime = parse('1970-01-01 00:00:01', tzinfos=tz.tzutc)
    assert type(json.dumps(ansible_datetime, cls=AnsibleJSONEncoder)) == str

# Generated at 2022-06-12 23:15:08.884062
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder(
        preprocess_unsafe=False, vault_to_text=True,
        separators=(', ', ': '), sort_keys=False, indent=0, ensure_ascii=False
    ).default({'a': 'b'})
    assert result ==  {'a': 'b'}

