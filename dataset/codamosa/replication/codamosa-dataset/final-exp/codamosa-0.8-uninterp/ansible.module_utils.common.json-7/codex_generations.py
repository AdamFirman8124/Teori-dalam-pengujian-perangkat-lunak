

# Generated at 2022-06-12 23:06:38.008405
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import text_type

    x = AnsibleJSONEncoder()
    # Vault object
    y = text_type("$ANSIBLE_VAULT;1.1;AES256")
    assert x.default(y) == '$ANSIBLE_VAULT;1.1;AES256'



# Generated at 2022-06-12 23:06:45.922297
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()

    # Test an old style class
    class Foo:
        def __init__(self, val):
            self.val = val
        def __repr__(self):
            return self.val

    assert encoder.encode(Foo(u"foo")) == u'"foo"'

    # Test an unsafe object
    assert encoder.encode(AnsibleUnsafe(u"foo")) == u'"__ansible_unsafe": "foo"'

    # Test a safe string
    assert encoder.encode(u"foo") == u'"foo"'



# Generated at 2022-06-12 23:06:53.313213
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # Create a VaultLib object
    vault = VaultLib('testpass')

    # Create a JSONEncoder object
    encoder = AnsibleJSONEncoder()

    # Create an object with __ENCRYPTED__ attribute
    encrypted_object = vault.encrypt(b'Ansible-vault')

# Generated at 2022-06-12 23:07:04.221045
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class Foo:
        def __init__(self):
            self.a = 'a'
            self.b = 'b'

    class Bar(dict):
        pass

    assert AnsibleJSONEncoder().default({}) == {}
    assert AnsibleJSONEncoder().default(()) == []
    assert AnsibleJSONEncoder().default([]) == []
    assert AnsibleJSONEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert AnsibleJSONEncoder().default(type(None)) == None
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default('foo') == 'foo'
    assert AnsibleJSONEncoder().default(Foo()) == {'a': 'a', 'b': 'b'}

# Generated at 2022-06-12 23:07:11.691316
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe(str):
        __UNSAFE__ = True
    class AnsibleUnsafeVault(str):
        __UNSAFE__ = True
        __ENCRYPTED__ = True

    result = json.dumps(AnsibleUnsafe("value")).replace('"', '')
    assert result == '{"__ansible_unsafe": "value"}'

    result = json.dumps(AnsibleUnsafeVault("value")).replace('"', '')
    assert result == '{"__ansible_vault": "value"}'

# Generated at 2022-06-12 23:07:19.660396
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault

    dict_test = dict(k1='v1', k2='v2')
    date_test = datetime.datetime.now()
    vault_test = vault.VaultLib('secret')
    class A:
        pass
    object_test = A()
    object_test.a = 'a'

    # Test with all kinds of objects
    assert json.loads(json.dumps(dict_test, cls=AnsibleJSONEncoder)) == dict_test
    assert json.loads(json.dumps(date_test, cls=AnsibleJSONEncoder)) == date_test.isoformat()

# Generated at 2022-06-12 23:07:31.353250
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Correct type of value
    assert AnsibleJSONEncoder().default(dict(a=1)) == dict(a=1)
    assert AnsibleJSONEncoder().default(datetime.date(2019, 9, 3)) == '2019-09-03'
    assert AnsibleJSONEncoder().default([dict(a=1)]) == [dict(a=1)]

    assert AnsibleJSONEncoder().default({
        '__ansible_unsafe': 'This is a ansible unsafe test.'
    }) == {
        '__ansible_unsafe': 'This is a ansible unsafe test.'
    }


# Generated at 2022-06-12 23:07:33.140837
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert (json.dumps(__name__, cls=AnsibleJSONEncoder) == json.dumps(__name__))


# Generated at 2022-06-12 23:07:40.108809
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    is_json_equal = AnsibleJSONEncoder().encode({'foo': 'bar'}) == json.dumps({'foo': 'bar'})
    assert is_json_equal

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six.moves.urllib.parse import quote_plus

    secret = VaultSecret()
    vault_str = VaultLib(secret).encrypt('secret')
    vault = VaultLib(secret).decrypt(binary_type(vault_str))

# Generated at 2022-06-12 23:07:51.615032
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault
    from ansible.parsing.vault import VaultLib

    # Testing for ansible.parsing.vault.VaultLib class
    vault_text = VaultLib([])
    assert AnsibleJSONEncoder().default(vault_text) == {'__ansible_vault': None}
    assert AnsibleJSONEncoder(vault_to_text=True).default(vault_text) == ''

    # Testing for other types
    test_obj = {
        'boolean': True,
        'string': 'test value',
        'number': 123,
        'list': [1, 2, 3],
        'dict': {'a': 'A', 'b': 'B'},
    }
    assert AnsibleJSONEncoder().default(test_obj)

# Generated at 2022-06-12 23:08:01.464165
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.common.text.formatters.json import AnsibleJSONEncoder

    x = AnsibleUnsafe('汉语/漢語')

    res = json.dumps(x, cls=AnsibleJSONEncoder)

    assert res == '{"__ansible_unsafe": "汉语/漢語"}'

# Generated at 2022-06-12 23:08:03.686694
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = {'test': AnsibleUnsafeText('test')}
    actual = AnsibleJSONEncoder().default(data)
    assert actual == {'test': {'__ansible_unsafe': 'test'}}

# Generated at 2022-06-12 23:08:09.604062
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class AnsibleUnsafe(str):
        """
        This is a helper class intended to mark a string that has been sent
        through the `to_text` function in ansible.module_utils.basic.
        """

        __UNSAFE__ = True

    data = {'a': AnsibleUnsafe('c')}
    result = AnsibleJSONEncoder().default(data)
    assert result['a'] == 'c'


# Generated at 2022-06-12 23:08:20.207070
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.vars.unsafe_proxy import AnsibleUnsafe, wrap_var
    from ansible.module_utils.common.collections import is_sequence

    # set up AnsibleUnsafe object
    ansible_unsafe = AnsibleUnsafe("ABC")
    assert getattr(ansible_unsafe, '__UNSAFE__', False) == True

    # set up vault object
    # Note: AnsibleToken.encrypt_text calls vault.encrypt
    vault = VaultLib(None)
    ansible_vault = vault._token.encrypt_text("xyz")

# Generated at 2022-06-12 23:08:27.754196
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import datetime
    import copy
    src_dict = {
        'a': 'z',
        'b': None,
        'c': datetime.datetime(2017, 11, 25, 10, 23, 41),
        'd': datetime.date(2017, 11, 25),
        'e': datetime.time(10, 23, 41),
        'f': u'unicode_str',
        'g': 'two\nlines',
        'h': [1, 2, 3, 4],
        'i': [{'a': 'b'}, {'c': 'd'}],
        'j': {'a': 'b', 'c': 'd'},
        'k':  VaultLib('secret'),
    }

    encoder = Ans

# Generated at 2022-06-12 23:08:32.861631
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """ Ensure the default method of AnsibleJSONEncoder works as expected """
    class vault(object):
        __ENCRYPTED__ = True
        _ciphertext = 'secret'

    class unsafe(object):
        __UNSAFE__ = True

    class o(object):
        def __init__(self, a, b):
            self._a = a
            self._b = b

        def __repr__(self):
            return "%s(%r, %r)" % (
                self.__class__.__name__, self._a, self._b)

        def __str__(self):
            return "%s" % (self._a)

    import datetime
    d = datetime.date(2018, 7, 18)

# Generated at 2022-06-12 23:08:41.702493
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleVaultEncryptedUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleVaultEncryptedUnicode

    # Normal text
    test_data_1 = u'This is a normal text'
    assert json.dumps(test_data_1, cls=AnsibleJSONEncoder, sort_keys=True) == '"This is a normal text"'

    # Encrypted text
    ansible_vault = VaultLib([])
    encrypted_text = ansible_vault.encrypt(test_data_1)
    test_data_2 = AnsibleVaultEncryptedUnsafeText(encrypted_text)

# Generated at 2022-06-12 23:08:52.237812
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    class MyMapping(object):
        def __init__(self, **kwargs):
            self.k = kwargs
        def __getitem__(self, key):
            return self.k[key]
        def __setitem__(self, key, value):
            self.k[key] = value
        def __iter__(self):
            return self.k.__iter__()

    datetime_now = datetime.datetime.utcnow()
    assert AnsibleJSONEncoder(sort_keys=True).default(datetime_now) == '%sZ' % datetime_now.isoformat()[:-3]

    from ansible.parsing.vault import VaultLib
    vault_string = 'Vault test string'

# Generated at 2022-06-12 23:08:57.834473
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This test is only for making sure that the class is working.
    # Please do not add more tests here.
    # Add more tests in test_utils.py
    import unittest
    class TestAnsibleJSONEncoder(unittest.TestCase):
        def test_default(self):
            import base64
            from ansible.parsing.vault import VaultLib
            vault = VaultLib(["--vault-password-file", "test/test_utils_vault/vault_password.txt"])

            # Test for class ansible.parsing.vault.VaultSecret
            # Encrypt "test"

# Generated at 2022-06-12 23:09:08.122203
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    assert AnsibleJSONEncoder().default(AnsibleUnsafe("a")) == {
        "__ansible_unsafe": "a"
    }

    assert AnsibleJSONEncoder().default("a") == "a"

    assert AnsibleJSONEncoder().default(AnsibleUnsafe("トレッドミル")) == {
        "__ansible_unsafe": "トレッドミル"
    }

    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(AnsibleUnsafe("a")) == {
        "__ansible_unsafe": "a"
    }

    assert AnsibleJSONEncoder(preprocess_unsafe=True).default("a") == "a"

    assert AnsibleJSONEncoder

# Generated at 2022-06-12 23:09:21.962019
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import datetime

    # test for vault object
    encoder = AnsibleJSONEncoder(indent=2)
    vault = VaultLib([1,2,3], b'$ANSIBLE_VAULT;1.1;AES256\n33316366373531300d0c6f74756e697573646f6d69756d0d0c3965306635313732610a001d00f348a8aa845e638be87dc86d3fc3b3d3\n', b'password')
    date_time = datetime.datetime(2018, 1, 30, 10, 30, 19)
    test_dict = {'__ansible_vault': vault, 'date_time': date_time}
    expect_dict

# Generated at 2022-06-12 23:09:31.269762
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import text_type
    from ansible.module_utils.six.moves.urllib.parse import quote_plus
    # create a test class to test if AnsibleJSONEncoder's default method works
    class TestEncoderClass:
        def __init__(self, value):
            self._value = value
        def __str__(self):
            return self._value
        def __unicode__(self):
            return self._value

    # test instance of text_type
    class_instance = TestEncoderClass('instance of text_type')
    assert isinstance(class_instance, text_type)
    # VaultSecret
    vault_secret_input = 'this is a vault secret'

# Generated at 2022-06-12 23:09:41.547129
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_unsafe = AnsibleUnsafe('foobar', unsafe=True)
    ansible_vault = AnsibleVaultEncryptedUnicode('foobar', unsafe=True)

    dump = json.dumps({
        'unsafe': ansible_unsafe,
        'vault': ansible_vault,
        'datetime': datetime.datetime.now(),
        'hostvars': {'10.0.0.1': {'foo': 'bar'}},
    }, cls=AnsibleJSONEncoder)

    load = json.loads(dump)

    assert load['unsafe']['__ansible_unsafe'] == 'foobar'
    assert load['vault']['__ansible_vault'] == 'foobar'



# Generated at 2022-06-12 23:09:50.101019
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('foo') == 'foo'

    # Test default behavior
    # NOTE: The AnsibleJSONEncoder returns a dict representation of the following
    # classes and mappings:
    #
    #     - AnsibleVaultEncryptedUnicode
    #     - AnsibleUnsafeText # if not preprocessed
    #     - mappings
    #
    # AnsibleUnsafeText is only returned as a dict if encoding an ``AnsibleUnsafe``
    # in ``AnsibleJSONEncoder.iterencode``.
    #
    # The tests for ``AnsibleUnsafeText`` if not preprocessed are commented out to
    # not break the entire test suite, as even though the tests pass, they fail in
    # ``tox`` and ``jenkins``.

# Generated at 2022-06-12 23:09:56.465210
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for class AnsibleJSONEncoder method default
    """
    encoder = AnsibleJSONEncoder()
    assert encoder.default(dict(a=1, b=2)) == {'a': 1, 'b': 2}
    assert encoder.default(list([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(datetime.date(2017, 3, 1)) == "2017-03-01"
    assert encoder.default(datetime.datetime(2017, 3, 1, 9, 0)) == "2017-03-01T09:00:00"

# Generated at 2022-06-12 23:10:04.171552
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.ajson import AnsibleUnsafeText
    from ansible_collections.misc.not_a_real_collection.plugins.modules.test_module import TestModule


# Generated at 2022-06-12 23:10:13.467838
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    d = {'foo': 123, 'bar': {'a': 1, 'b': 2}, 'baz': [1, 2, 3]}
    assert json.dumps(d, cls=AnsibleJSONEncoder) == '{"foo": 123, "bar": {"a": 1, "b": 2}, "baz": [1, 2, 3]}'

    # vault object
    vault = VaultLib([])

# Generated at 2022-06-12 23:10:24.602366
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test __ENCRYPTED__
    vault = AnsibleJSONEncoder(vault_to_text=False)
    vault_text = AnsibleJSONEncoder(vault_to_text=True)
    class FakeEncrypted:
        __ENCRYPTED__ = True
        _ciphertext = 'My secret'
    assert(vault.default(FakeEncrypted()) == {'__ansible_vault': 'My secret'})
    assert(vault_text.default(FakeEncrypted()) == 'My secret')

    # Test __UNSAFE__
    unsafe = AnsibleJSONEncoder()
    class FakeUnsafe:
        __UNSAFE__ = True
    assert(unsafe.default(FakeUnsafe()) == {'__ansible_unsafe': 'My secret'})


# Generated at 2022-06-12 23:10:30.216231
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    AnsibleJSONEncoder().default({})
    AnsibleJSONEncoder().default({'__ENCRYPTED__': True})
    AnsibleJSONEncoder().default({'__UNSAFE__': True})
    AnsibleJSONEncoder().default({'__ENCRYPTED__': True, '__UNSAFE__': True})
    AnsibleJSONEncoder().default(datetime.datetime.now())
    AnsibleJSONEncoder().default(datetime.date.today())
    AnsibleJSONEncoder().default('str')

# Generated at 2022-06-12 23:10:39.646293
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test for class ``AnsibleUnsafeText``
    from ansible.module_utils.common.text.converters import to_bytes
    ansible_unsafe_text = to_bytes('foo')
    json_encoder = AnsibleJSONEncoder()
    output = json_encoder.default(ansible_unsafe_text)
    assert isinstance(output, bytes)
    assert output == b'foo'

    # test for class ``AnsibleVaultEncryptedUnicode``
    from ansible.parsing.vault import VaultLib, VaultSecret
    vault_secret = VaultSecret('$ANSIBLE_VAULT;1.1;AES256')
    vault_lib = VaultLib(vault_secret)
    ansible_vault_encrypted_unicode = vault_lib.encrypt(u'foo')

# Generated at 2022-06-12 23:10:52.797061
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe():
        __UNSAFE__ = True
        __ENCRYPTED__ = False
        def __init__(self, data):
            self._data = data
        def __str__(self):
            return str(self._data)
        def __repr__(self):
            return '%s(%s)' % (self.__class__, repr(self._data))
        def __eq__(self, other):
            return self._data == other
        def __ne__(self, other):
            return self._data != other

    class AnsibleUnsafeText():
        __UNSAFE__ = True
        __ENCRYPTED__ = False
        def __init__(self, data):
            self._data = to_text(data, errors='surrogate_or_strict')


# Generated at 2022-06-12 23:11:01.164936
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils._text import to_bytes, to_text

    encoder = AnsibleJSONEncoder()

    pw = "my secret password"
    vault = VaultLib([to_bytes(pw)])

    vault_text = to_text(vault.encrypt(to_bytes("my secret text")))
    vault_object = vault.decrypt(vault_text)

    assert encoder.default(7) == 7


# Generated at 2022-06-12 23:11:11.374511
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import text_type

    plaintext = 'hello world'
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n353937666465303131633962303232333731343363353536373532623032393961303261663233\n643766656434663734616662626130663139633331623365316531643130353266633163346630\n633938663135\n'
    vault_secret = VaultSecret('AES256', ciphertext)
    vault = VaultLib(None)

# Generated at 2022-06-12 23:11:19.228716
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(to_text(b'\x00', errors='surrogate_or_strict')) == u'\x00'
    assert AnsibleJSONEncoder().default(to_text(b'\x00', errors='surrogate_or_strict', nonstring='strict')) == u'\x00'
    assert AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True).default(to_text(b'\x00', errors='surrogate_or_strict', nonstring='strict')) == u'\x00'


# Generated at 2022-06-12 23:11:29.840282
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils._text import to_native

    class Foo:
        def __init__(self, x):
            self.x = x
        def __repr__(self):
            return "Foo(%r)" % self.x

    o = Foo([1,2])
    print(json.dumps(o, cls=AnsibleJSONEncoder))
    # example output:
    # Foo([1, 2])

    o = Foo(1)
    print(json.dumps(o, cls=AnsibleJSONEncoder))
    # example output:
    # Foo(1)

    o = Foo({1: 'one'})
    print(json.dumps(o, cls=AnsibleJSONEncoder))
    # example output:
    # Foo({1: 'one'})

# Generated at 2022-06-12 23:11:39.033559
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # check if we can encode a boolean
    o = True
    r = AnsibleJSONEncoder().default(o)
    assert r == o

    # check if we can encode a string
    o = 'one'
    r = AnsibleJSONEncoder().default(o)
    assert r == o

    # check if we can encode a number
    o = 1
    r = AnsibleJSONEncoder().default(o)
    assert r == o

    # check if we can encode a float
    o = 1.0
    r = AnsibleJSONEncoder().default(o)
    assert r == o

    # check if we can encode a list
    o = [1, 2]
    r = AnsibleJSONEncoder().default(o)
    assert r == o

    # check if we can encode a dict

# Generated at 2022-06-12 23:11:44.187635
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    m = {'a': {
        'b': 'c'
    }}
    assert json_encoder.default(m) == {'a': {
        'b': 'c'
    }}
    assert json_encoder.default(m['a']) == {
        'b': 'c'
    }
    d = datetime.date(2020, 3, 12)
    assert json_encoder.default(d) == '2020-03-12'

# Generated at 2022-06-12 23:11:50.416421
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.module_utils.basic
    e = AnsibleJSONEncoder()

    # SafeString
    assert e.default(ansible.module_utils.basic.AnsibleModule.jsonify({'string': 'myString'})) == {'string': 'myString'}
    assert e.default(ansible.module_utils.basic.AnsibleModule.jsonify(('string',))) == ('string',)
    assert e.default(ansible.module_utils.basic.AnsibleModule.jsonify(True)) == True
    assert e.default(ansible.module_utils.basic.AnsibleModule.jsonify(False)) == False
    assert e.default(ansible.module_utils.basic.AnsibleModule.jsonify(1)) == 1

# Generated at 2022-06-12 23:12:00.101442
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # make sure that vault objects are encoded correctly
    v = VaultLib('testpassword')
    assert AnsibleJSONEncoder().default(v.encrypt('testvalue')) == '$ANSIBLE_VAULT;1.1;AES256;test\naW4gYmFyIGNvdXRpbmEgZGUgYmF0YWxpc3RpYw==\n'

    # make sure that date objects are encoded correctly
    import datetime
    assert AnsibleJSONEncoder().default(datetime.datetime(2017, 2, 3, 17, 25, 49, 101000)) == '2017-02-03T17:25:49.101000'

    # make sure that both unicode strings and bytes are handled correctly

# Generated at 2022-06-12 23:12:10.428004
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Temporarily skip the tests which are not yet confirmed the behavior.
    #     (e.g., self._preprocess_unsafe and self._vault_to_text are not confirmed)
    return

    def _from_value_to_crypt_value(value):
        class _Crypt(object):
            def __init__(self, value):
                self._ciphertext = value
        crypt = _Crypt(value)
        setattr(crypt, '__ENCRYPTED__', True)
        return crypt

    def _from_value_to_unsafe_value(value):
        class _Unsafe(str):
            def __init__(self, value):
                str.__init__(self, value)
        unsafe = _Unsafe(value)
        setattr(unsafe, '__UNSAFE__', True)

# Generated at 2022-06-12 23:12:30.214750
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # input
    insecure_unicode = 'hello, $ANSIBLE_VAULT'
    insecure_bytes = insecure_unicode.encode('utf-8')
    from ansible.parsing.vault import VaultLib
    v = VaultLib(['secret'])
    v._encrypt_bytes(insecure_bytes, True)
    encrypted_unicode = v
    encrypted_bytes = v.encode('utf-8')
    foo = Foo()
    bar = Bar()

    # logic
    # The default encoder shall work and do nothing for any uninherited object
    # The default encoder shall call __dict__ for any object inherited from object.
    # The default encoder shall call to_string for any object inherited from str.
    # The default encoder shall call __dict__ for any object inherited from tuple.
    # The default

# Generated at 2022-06-12 23:12:40.579141
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import pprint

    jenc = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    o = dict(a=1, b=2, c=3)
    s = jenc.default(o)
    s = json.dumps(s)
    pprint.pprint(s)

    from ansible.parsing.vault import VaultLib, VaultSecret

# Generated at 2022-06-12 23:12:50.133344
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.json_utils import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.parsing.convert_bool import boolean
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default("") == "", "failed to encode string type"
    assert ansible_json_encoder.default(boolean(True)) == True, "failed to encode boolean type"
    assert ansible_json_encoder.default(100) == 100, "failed to encode integer type"
    assert ansible_json_encoder.default(1.5) == 1.5, "failed to encode float type"

# Generated at 2022-06-12 23:12:59.136700
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.common._collections_compat import MutableSequence, MutableSet

    vault = VaultLib([])
    vault_secret = 'foo'
    vault_encrypted_secret = vault.encrypt(vault_secret)

    # Test Unicode
    assert json.loads(json.dumps(vault_encrypted_secret, cls=AnsibleJSONEncoder)) == vault_secret

    # Test byte string
    vault_secret = b'bar'
    vault_encrypted_secret = vault.encrypt(vault_secret)
    assert json.loads(json.dumps(vault_encrypted_secret, cls=AnsibleJSONEncoder)) == vault_secret

    # Test

# Generated at 2022-06-12 23:13:07.642124
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(datetime.datetime(2018, 8, 11, 6, 50, 45, 937929)) == '2018-08-11T06:50:45.937929'
    assert AnsibleJSONEncoder().default(datetime.date(2018, 8, 11)) == '2018-08-11'
    assert AnsibleJSONEncoder().default({"test": "value"}) == {"test": "value"}
    assert AnsibleJSONEncoder().default(['test', 'value']) == ['test', 'value']
    assert AnsibleJSONEncoder().default(b'\xef\xbb\xbfhello') == '��hello'


# Generated at 2022-06-12 23:13:16.829949
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode

    vault = VaultLib([])
    card_number = vault.encrypt("1234123412341234")
    assert(isinstance(card_number, AnsibleVaultEncryptedUnicode))


# Generated at 2022-06-12 23:13:27.415444
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Put basic data types and some extended data types into a list
    # The list is used to create a dict and then encode the dict.
    #
    # The list contains:
    #     xxxxxxxxxx
    #   0    1    2    3    4    5    6    7    8    9
    #   +----+----+----+----+----+----+----+----+----+
    #   basic data types
    #   |
    #   extended data types
    #
    # The string representation of each item in the list will be checked against
    # the corresponding encoded item in a dict.
    #
    # The output of the unit test is printed on screen.
    #
    # Note, this unit test is not very complete. It just checks some items in the list.


    # Create test data:
    import datetime


# Generated at 2022-06-12 23:13:34.412009
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test default method of AnsibleJSONEncoder
    '''
    from ansible.vars import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    vault_encrypted_value = VaultLib.encrypt(b'test', b'encryptme')
    vault_text_value = to_text(vault_encrypted_value)
    vault_object = AnsibleVaultEncryptedUnicode(vault_text_value)

    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert ansible_json_encoder.default(vault_object) == {'__ansible_vault': vault_text_value}

# Generated at 2022-06-12 23:13:42.139289
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:13:54.013580
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Use the default encoder as default
    assert json.dumps(dict(ansible_dict=dict(a='b')), cls=AnsibleJSONEncoder) == '{"ansible_dict": {"a": "b"}}'
    assert json.dumps(dict(ansible_str_to_str=dict(a='b')), cls=AnsibleJSONEncoder) == '{"ansible_str_to_str": {"a": "b"}}'
    assert json.dumps(dict(ansible_str_to_dict=dict(a=dict(b='c'))), cls=AnsibleJSONEncoder) == '{"ansible_str_to_dict": {"a": {"b": "c"}}}'

    # Test a dict that has a dict inside of it

# Generated at 2022-06-12 23:14:19.018139
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.basic import AnsibleUnsafe

    data = {
        'a_string': 'string',
        'a_unicode_string': u'unicode',
        'a_unsafe_string': AnsibleUnsafe('unsafe'),
        'a_vault_string': VaultLib([1, 2, 3])
    }


# Generated at 2022-06-12 23:14:28.805747
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_sequence

    test_class = type(str("TestClass"), (object,), {'a': 1})
    test_class_dunder_encrypted = type(str("TestClassDunderEncrypted"), (object,), {'a': 1, '__ENCRYPTED__': True})
    test_class_dunder_unsafe = type(str("TestClassDunderUnsafe"), (object,), {'a': 1, '__UNSAFE__': True})


# Generated at 2022-06-12 23:14:36.589206
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    import datetime

    # Basic
    a = AnsibleJSONEncoder()
    assert a.default(True) == True
    assert a.default(1)    == 1
    assert a.default(1.0)  == 1.0
    assert a.default([1,2,3]) == [1,2,3]
    assert a.default({'key':'value'}) == {u'key': u'value'}

    # Complex
    assert a.default([{'key':'value', 'key2':'value2'}]) == [{u'key': u'value', u'key2': u'value2'}]

# Generated at 2022-06-12 23:14:45.534459
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Ensure AnsibleJSONEncoder.default() works as expected.
    """
    from ansible.parsing.vault import VaultLib

    enc = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True)

    # Ensure unsafe values are encoded properly
    from ansible.module_utils.basic import AnsibleUnsafeText
    assert '__ansible_unsafe' in json.loads(
        enc.encode(AnsibleUnsafeText("unsafe text")))
    assert '__ansible_unsafe' in json.loads(
        enc.encode(AnsibleUnsafeText("unsafe text"))).keys()
    assert 'unsafe text' in json.loads(
        enc.encode(AnsibleUnsafeText("unsafe text"))).values()

    # Ensure that the

# Generated at 2022-06-12 23:14:55.722031
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six import text_type

    # Test encrypting text
    password = 'password'
    plain_text = b"Hello World!"

# Generated at 2022-06-12 23:15:05.057077
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import base64
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    encoder = AnsibleJSONEncoder()
    plaintext = b'This is a test'
    password = b'secret'

# Generated at 2022-06-12 23:15:12.921628
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    import datetime

    def _test_encoder(text, expect):
        result = json.dumps(text, cls=AnsibleJSONEncoder)
        assert result == expect

    _test_encoder('test', '"test"')
    _test_encoder(['test', 'test'], '["test", "test"]')
    _test_encoder({'test': 'test'}, '{"test": "test"}')
    _test_encoder(AnsibleUnsafe('test'), '{"__ansible_unsafe": "test"}')
    _test_encoder(datetime.datetime(2018, 10, 5), '"2018-10-05T00:00:00"')

# Generated at 2022-06-12 23:15:20.795277
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():  # pylint: disable=invalid-name
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import b
    v = VaultLib(b('password'))
    e = AnsibleJSONEncoder()
    # test encrypt object
    vault_dict = {'1': {'vault': v.encrypt(b('123'))}}
    assert e.encode(vault_dict) == '{"1": {"vault": {"__ansible_vault": "AQAAAAvRAkI1ZDgzYmY0YWY2YjE2M2Q2M2ExNzRmYjRmYjJkYmY3Yw=="}}}'
    # test unicode object

# Generated at 2022-06-12 23:15:31.705321
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    test_hostvars = {'host1': 'host1_value'}
    test_date = datetime.date(2017, 1, 1)
    test_datetime = datetime.datetime(2017, 1, 1, 12, 34)

    # testing vault object
    test_encoder = AnsibleJSONEncoder()
    result = test_encoder.default(VaultLib([b'123456']).encrypt('test_plain_text'))

# Generated at 2022-06-12 23:15:41.679908
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    ansible_unsafe_encoder = AnsibleJSONEncoder(preprocess_unsafe=True)

    assert json_encoder.default(['foo', 'bar']) == ['foo', 'bar']
    assert json_encoder.default({'foo': 'bar'}) == {'foo': 'bar'}
    assert json_encoder.default(u'foobar') == 'foobar'
    assert json_encoder.default(b'foobar') == 'foobar'
    assert json_encoder.default(u'foobar'.encode('utf-8')) == 'foobar'

# Generated at 2022-06-12 23:16:18.568922
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import json

    class User:
        def __init__(self, name, affiliation):
            self.name = name
            self.affiliation = affiliation

        def __repr__(self):
            return 'User(%r, %r)' % (self.name, self.affiliation)

    users = [User('alice', 'alice.com'), User('bob', 'bob.com')]

    json_str = json.dumps(users, cls=AnsibleJSONEncoder)
    assert json_str == '[{"name": "alice", "affiliation": "alice.com"}, '\
                       '{"name": "bob", "affiliation": "bob.com"}]'

# Generated at 2022-06-12 23:16:26.896975
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type, text_type

    def _check_string_types(s):
        assert isinstance(s, (binary_type, text_type)), 'Expected a string, got %s' % type(s)
        return True

    # Vault object
    t = datetime.datetime.now()
    v = VaultLib('secret')
    o = v.encrypt('test')
    assert _check_string_types(o)
    assert not isinstance(o, binary_type)
    assert not isinstance(o, text_type)
    # return a string
    encoder = AnsibleJSONEncoder()
    assert isinstance(encoder.default(o), text_type)
    # return

# Generated at 2022-06-12 23:16:35.698945
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import text_type
    from ansible.module_utils.common.collections import AnsibleUnsafe

    test_class = type('test_class', (object,), dict(a=1))

    # date, datetime
    dt = datetime.datetime.utcnow()
    d = datetime.date.today()

    # hostvars
    hostvars = dict(ansible_facts=dict(ansible_os_family='RedHat', ansible_system='Linux'))

    # vault text
    vault_text = VaultLib.encrypt('test')
    vault_text_encoded = {'__ansible_vault': vault_text._ciphertext}

    # unsafe text
    unsafe_text = Ans