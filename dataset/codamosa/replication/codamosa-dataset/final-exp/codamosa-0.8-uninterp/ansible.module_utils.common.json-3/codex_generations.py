

# Generated at 2022-06-12 23:06:40.745977
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import b

    ansible_json_encoder = AnsibleJSONEncoder()

    # test for vault
    test_vault = VaultLib('my_pass')
    test_vault.loads(b('abcdef'))
    value = ansible_json_encoder.default(test_vault)
    assert isinstance(value, dict) and value.get('__ansible_vault') == 'abcdef'

    # test for unsafe
    test_unsafe = test_vault.encode(b('unsafe'))
    value = ansible_json_encoder.default(test_unsafe)
    assert isinstance(value, dict) and value.get('__ansible_unsafe') == 'unsafe'

   

# Generated at 2022-06-12 23:06:42.722571
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    assert (aje.default("foo") == "foo")


# Generated at 2022-06-12 23:06:50.381861
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_hex
    from ansible.module_utils.common.text.formatters import format
    from ansible.module_utils.basic import AnsibleUnsafe

    # create an unsafe string with ansible markups
    unsafe_str = AnsibleUnsafe("{{some_string}}")

    # create a vault object
    passphrase = 'testpassphrase'

# Generated at 2022-06-12 23:07:01.357521
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:07:11.436891
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import ordereddict
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE
    import datetime
    import os

# Generated at 2022-06-12 23:07:19.521350
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ...module_utils.common._collections_compat import ordereddict
    from ...module_utils.basic import AnsibleUnsafe, AnsibleVaultEncryptedUnicode

    date_time_obj = datetime.datetime.now()
    assert '"' + date_time_obj.isoformat() + '"' == AnsibleJSONEncoder().encode(date_time_obj)

    date_obj = datetime.date.today()
    assert '"' + date_obj.isoformat() + '"' == AnsibleJSONEncoder().encode(date_obj)

    mapping_obj = {u'a': u'Märy had ä littlé lamb', 'b': [1, 2, 3]}

# Generated at 2022-06-12 23:07:31.230040
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    def test_1():
        non_ansible_objs = [
            set([1, 2]),
            [1, 2],
            'a',
            None,
            1,
            {'a': 'b'},
            datetime.datetime(2018, 2, 3, 2, 3, 2, 3),
            datetime.date(2018, 2, 3)
        ]

        # Expected results
        non_ansible_expected = [
            {1, 2},
            [1, 2],
            '"a"',
            'null',
            1,
            {'a': 'b'},
            '"2018-02-03T02:03:02.000003"',
            '"2018-02-03"'
        ]

        # Encode

# Generated at 2022-06-12 23:07:38.934903
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_text

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_bytes, to_native
    from ansible.module_utils.parsing.convert_bool import boolean

    results1 = "Hello"
    results2 = "Hello World"
    results3 = "Hello World, How Are YOU?"
    results4 = "Special-Chars-^~%*[]`<>()"
    results5 = "pass1234"
    results6 = "password@#$^!*"

    results7 = VaultLib([])
    results8 = VaultLib([])
    results9 = VaultLib([])
    results10 = VaultLib([])
    results11 = VaultLib([])

# Generated at 2022-06-12 23:07:49.406795
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Arrange
    encoder = AnsibleJSONEncoder()
    s_vault_value = 'This is a text'
    vault_obj = VaultLib(s_vault_value)
    h_value = {'foo': 1234, 'bar': 'text'}
    date_obj = datetime.date(2016, 2, 14)
    d_value = {'foo': 1234, 'bar': 'text'}

    # Act
    a_vault_value = encoder.default(vault_obj)
    h_value_ret = encoder.default(h_value)
    date_obj_ret = encoder.default(date_obj)
    d_value_ret = encoder.default(d_value)

    # Assert
    assert a_vault_value['__ansible_vault']

# Generated at 2022-06-12 23:07:59.749979
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    import ansible.module_utils.common.unsafe_proxy as unsafe_proxy

    def generate_string():
        # These string will be converted to AnsibleUnsafe string
        s = ""
        for i in range(0, 256):
            s += unichr(i)
        return s

    # These items should return with same value.

# Generated at 2022-06-12 23:08:11.848777
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-12 23:08:22.348925
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Testing unsafe
    ansible_unsafe = AnsibleJSONEncoder().encode({'__ansible_unsafe': 'A {B} C'})
    assert json.loads(ansible_unsafe) == {"__ansible_unsafe": "A {B} C"}

    # Testing vault
    ansible_vault = AnsibleJSONEncoder(vault_to_text=True).encode({'__ansible_unsafe': 'A B C'})
    assert json.loads(ansible_vault) == {"__ansible_unsafe": "A B C"}

    ansible_vault_2 = AnsibleJSONEncoder(vault_to_text=False).encode({'__ansible_vault': 'A B C'})

# Generated at 2022-06-12 23:08:31.759032
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert AnsibleJSONEncoder().default(False) == False
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default(5) == 5
    assert AnsibleJSONEncoder().default({"a": "b"}) == {"a": "b"}

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    class VaultCrypto(VaultLib):
        def __init__(self):
            self._secrets = {}
            self._contexts = {}

        def encrypt(self, plaintext, key=None, context=None):
            return plaintext


# Generated at 2022-06-12 23:08:37.097208
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Check JSON ansible_vault and ansible_unsafe parsing"""
    import json
    import base64
    import random
    import string
    import sys

    # if this test fails on Windows, don't fix it.  This test runs on a Linux
    # box, so should never be run on Windows
    if sys.platform == 'win32':
        return

    # Generate random AnsibleVault
    b_key = bytearray(random.getrandbits(8) for i in range(32))
    b_salt = bytearray(random.getrandbits(8) for i in range(64))
    b_iv = bytearray(random.getrandbits(8) for i in range(32))

    # Generate random plaintext

# Generated at 2022-06-12 23:08:47.419959
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import ansible.parsing.vault.VaultLib as VaultLibModule
    import datetime

    with VaultLib('secret'):
        test_safe_str = "this_is_safe"
        assert ansible.utils.unsafe_proxy.safe_text(test_safe_str) == test_safe_str

        test_unsafe_str = "this_is_unsafe"
        assert ansible.utils.unsafe_proxy.unsafe_text(test_unsafe_str) == ansible.utils.unsafe_proxy.AnsibleUnsafeText(test_unsafe_str)

        test_vault_str = "this_is_vault"
        assert VaultLib.encrypt(test_vault_str) == ansible.parsing

# Generated at 2022-06-12 23:08:57.423895
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe, AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    json_encoder = AnsibleJSONEncoder()
    assert json_encoder.default(AnsibleUnsafe('{ "is_unsafe": true }')) == {'__ansible_unsafe': to_text('{ "is_unsafe": true }', errors='surrogate_or_strict', nonstring='strict')}
    assert json_encoder.default(mock_Mapping()) == {'ANSIBLE_MOCK_MAPPING': 'ANSIBLE_MOCK_MAPPING'}

    vault = VaultLib([])

# Generated at 2022-06-12 23:09:07.569168
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.module_utils.common.text.ansible_types as at

    assert json.dumps(at.AnsibleUnsafe(u'Unsafe'), cls=AnsibleJSONEncoder) == json.dumps(u'Unsafe')
    assert json.dumps(at.AnsibleUnsafePassword(u'UnsafePassword'), cls=AnsibleJSONEncoder) == json.dumps(u'UnsafePassword')
    assert json.dumps(at.AnsibleVaultEncryptedUnicode(u'AnsibleVault'), cls=AnsibleJSONEncoder) == json.dumps({"__ansible_vault": "AnsibleVault"})

# Generated at 2022-06-12 23:09:18.347230
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import text_type
    class _AnsibleUnsafeStr(text_type):
        __UNSAFE__ = True

    class _AnsibleUnsafe(object):
        __UNSAFE__ = True

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    class _AnsibleVault(object):
        __ENCRYPTED__ = True

        def __init__(self, ciphertext):
            self._ciphertext = ciphertext  # pylint: disable=protected-access

        def __str__(self):
            return self._ciphertext


# Generated at 2022-06-12 23:09:25.885778
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.common._text import to_bytes
    unsafeunicode_data = u'\u2713'
    safeunicode_data = u'\u2714'
    safebytes_data = to_bytes(u'\u2714', errors='surrogate_or_strict')
    safebinary_data = b'\xe2\x9c\x93'

    assert isinstance(test_AnsibleJSONEncoder_default.__annotations__, dict)

    encoder = AnsibleJSONEncoder()

    # verify safe objects
    assert encoder.default(safeunicode_data) == u'\u2714'

# Generated at 2022-06-12 23:09:29.592236
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test encrypted
    encoder = AnsibleJSONEncoder()
    assert encoder.default(encoder) == {'__ansible_vault': u'Cg=='}

    # Test unsafe
    assert encoder.default(False) == False


# Generated at 2022-06-12 23:09:42.040768
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    ansiblejsonencoder = AnsibleJSONEncoder()

    # Encrypted strings
    ciphertext = VaultLib('mypassword').encrypt('mypassword')
    ansible_string = ansiblejsonencoder.default(ciphertext)
    assert isinstance(ansible_string, dict)
    assert '__ansible_vault' in ansible_string

    # Plain strings
    ansible_string = ansiblejsonencoder.default('hello')
    assert isinstance(ansible_string, str)
    assert ansible_string == 'hello'

    # Special objects
    class AnsibleSpecialObject(object):
        def __init__(self):
            self.__unsafe__ = False

        def __repr__(self):
            return "AnsibleSpecialObject"

# Generated at 2022-06-12 23:09:50.441742
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test when we use AnsibleUnsafeText in value
    encoder = AnsibleJSONEncoder()
    d1 = {"key1":"value1", "key2":2, "key3":datetime.datetime.now()}
    res = encoder.default(d1)
    assert res == {"key1":"value1", "key2":2, "key3":datetime.datetime.now().isoformat()}

    # Test when we use datetime.datetime.now() in value
    d2 = {"key1":"value1", "key2":2, "key3":AnsibleUnsafeText(datetime.datetime.now())}
    res = encoder.default(d2)

# Generated at 2022-06-12 23:09:58.265475
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import inspect
    import sys

    if sys.version_info[0] >= 3:
        # The __getattribute__ method of class AnsibleJSONEncoder will not be
        # found by python 3 for some reason.  See this thread for some
        # discussion of the issue:
        # https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance
        # As a workaround, as suggested in the thread, use a mixin class.
        class TestMixin(object):
            def _test_default(self, ansible_value, json_value):
                o = ansible_value
                value = self.default(o)
                assert value == json_value

        class TestAnsibleJSONEncoder(TestMixin, AnsibleJSONEncoder):
            pass

        t = Test

# Generated at 2022-06-12 23:10:06.468140
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.basic import AnsibleUnsafe, AnsibleVaultEncryptedUnicode

    plaintext = "I am plain text."
    unsafe = AnsibleUnsafe(plaintext)
    ciphertext = "VFZSRU5EVkZOVDAxMDBDQVNLNzl1d01hTXJhb1Z6T3ZqTjZDdDFkdTZRPT0K"
    vault = AnsibleVaultEncryptedUnicode(ciphertext)

    assert _is_vault(vault)
    assert _is_unsafe(unsafe)

    assert plaintext == str(unsafe)

    # test vault object
    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:10:12.642254
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert(ansible_json_encoder.default(dict(a=1, b="hi"))) == {'a': 1, 'b': 'hi'}
    assert(ansible_json_encoder.default(["a", "b", 3])) == ["a", "b", 3]
    assert(ansible_json_encoder.default(True)) == True
    assert(ansible_json_encoder.default(12345)) == 12345

# Generated at 2022-06-12 23:10:23.529681
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import ensure_str
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes

    # Test custom __vault__ object
    encrypted_text = '$ANSIBLE_VAULT;1.2;AES256;ansible\n39336535343130363963316262366433373864326562336361333737626261633365363339646367660a33633462326262646331413663373635663630653865383666363239383139343761303730376232633837\n'


# Generated at 2022-06-12 23:10:31.561488
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    # Create unsafe string
    unsafe = AnsibleUnsafe('unsafe')
    # Create vault string
    vault = VaultLib().encrypt('vault')
    # Create dictionary
    dictionary = {'item1': 'Value 1', 'item2': 'Value 2'}
    # Create list
    list1 = [unsafe, vault, 'Item 3', 4, dictionary]

    # Check results
    assert AnsibleJSONEncoder().default(unsafe) == {"__ansible_unsafe": u"unsafe"}

# Generated at 2022-06-12 23:10:38.385773
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.module_utils.basic


    class testAnsibleUnsafe(ansible.module_utils.basic.AnsibleUnsafe):

        def __init__(self):
            pass


    ansible_json_encoder = AnsibleJSONEncoder()
    ansible_json_encoder.vault_to_text = True
    enc_obj = ansible_json_encoder.encode(testAnsibleUnsafe())
    json_data = json.loads(enc_obj)
    assert json_data.get('__ansible_unsafe')



# Generated at 2022-06-12 23:10:48.066884
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test the default method of AnsibleJSONEncoder
    '''

    j = AnsibleJSONEncoder()
    assert j.default({"a": "b"}) == {"a": "b"}
    assert j.default(["a", "b"]) == ["a", "b"]
    assert j.default(dict(a="b")) == {"a": "b"}
    assert j.default(["a", "b"]) == ["a", "b"]

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEncryptedUnicode


# Generated at 2022-06-12 23:10:55.783432
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # create class instance
    en = AnsibleJSONEncoder()

    # ensure default is called when no special handling is needed
    # and class not recognized
    class C:
        pass
    c = C()
    value = en.default(c)

    assert value is c

    # test __ENCRYPTED__ handling
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('test')
    value = en.default(vault.encrypt('my secret'))


# Generated at 2022-06-12 23:11:01.653764
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = b'{"a": 1}'
    o = json.loads(j)
    assert AnsibleJSONEncoder().encode(o) == j


# Generated at 2022-06-12 23:11:11.870816
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    date1 = datetime.datetime(2015, 1, 1, 12, 0, 0)
    date2 = datetime.date(2015, 1, 1)
    date_dict = {'date1': date1, 'date2': date2}
    assert encoder.default(date1) == '2015-01-01T12:00:00'
    assert encoder.default(date2) == '2015-01-01'
    assert encoder.default(date_dict) == {'date1': '2015-01-01T12:00:00', 'date2': '2015-01-01'}
    assert encoder.default([date1, date2]) == ['2015-01-01T12:00:00', '2015-01-01']


# Generated at 2022-06-12 23:11:22.289814
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import range

    def _test_encoder(obj):
        return json.loads(json.dumps(obj, cls=AnsibleJSONEncoder, preprocess_unsafe=False))

    assert _test_encoder(VaultLib(b'V1' * 15, b'V1' * 32)) == {'__ansible_vault': b'V1' * 15 + b'V1' * 32}


# Generated at 2022-06-12 23:11:32.501938
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # pylint: disable=invalid-name
    """
    test for method AnsibleJSONEncoder.default
    """
    import datetime
    o = {'__ansible_unsafe': 'unsafe'}
    ansiblejsonencoder = AnsibleJSONEncoder()
    result = ansiblejsonencoder.default(o)
    assert result, 'failed'

    # unsafe object
    o = ansiblejsonencoder.default('unsafe')
    assert o, 'failed'

    # vault object
    o = ansiblejsonencoder.default('ansible_vault')
    assert o, 'failed'

    # hostvars and other objects
    o = ansiblejsonencoder.default(Mapping({'__ansible_vault': 'ansible_vault'}))
    assert o, 'failed'

   

# Generated at 2022-06-12 23:11:39.546971
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(o = {'key':'value'}) == {'key':'value'}
    assert ansible_json_encoder.default(o = {'key':'value', 'key1':'value1'}) == {'key':'value', 'key1':'value1'}
    assert ansible_json_encoder.default(o = {1:'value'}) == {1:'value'}
    assert ansible_json_encoder.default(o = 1) == 1
    assert ansible_json_encoder.default(o = 1.0) == 1.0
    assert ansible_json_encoder.default(o = 'string') == 'string'
    assert ansible_json_encoder.default

# Generated at 2022-06-12 23:11:47.191138
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import json
    import sys
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    class SampleVaultClass(VaultLib):
        def __init__(self, password='', **kwargs):
            raise NotImplementedError()

    def _get_vault_secret(password, secret):
        return secret

    class SampleVaultSecret(VaultSecret):
        def __init__(self, password=None, secret=None, salt=b'salt', secret_type=None):
            self._password = password
            self._secret = secret
            self._salt = salt
            if secret_type is None:
                self._secret_type = 'AES256'

# Generated at 2022-06-12 23:11:56.985897
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # basic python types
    assert json.dumps(dict(), cls=AnsibleJSONEncoder) == '{}'
    assert json.dumps(5, cls=AnsibleJSONEncoder) == '5'
    assert json.dumps([], cls=AnsibleJSONEncoder) == '[]'
    assert json.dumps('hello', cls=AnsibleJSONEncoder) == '"hello"'
    assert json.dumps(False, cls=AnsibleJSONEncoder) == 'false'
    assert json.dumps(None, cls=AnsibleJSONEncoder) == 'null'
    # the rest
    assert json.dumps(object(), cls=AnsibleJSONEncoder) == '{}'

# Generated at 2022-06-12 23:12:06.560814
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert(
        json.loads(
            json.dumps(AnsibleJSONEncoder().default(dict()))
        ) == {}
    )
    assert(
        json.loads(
            json.dumps(AnsibleJSONEncoder().default(dict(foo='bar')))
        ) == dict(foo='bar')
    )
    assert(
        json.loads(
            json.dumps(AnsibleJSONEncoder().default(dict(foo=dict(bar='foobar1'))))
        ) == dict(foo=dict(bar='foobar1'))
    )

# Generated at 2022-06-12 23:12:15.247408
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import ensure_binary

    # ensure we can encode an AnsibleVaultEncryptedUnicode
    assert ensure_binary(AnsibleJSONEncoder().encode(AnsibleVaultEncryptedUnicode('My super secret'))) == ensure_binary('{"__ansible_vault": "My super secret"}')

    # ensure we can encode an unicode string
    assert ensure_binary(AnsibleJSONEncoder().encode(u'test')) == b'"test"'

    # ensure we can encode an int
    assert ensure_binary(AnsibleJSONEncoder().encode(123)) == b'123'

    # ensure we can encode an dictionary

# Generated at 2022-06-12 23:12:20.557879
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing import vault
    from ansible.parsing.yaml.objects import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()

    assert encoder.default(AnsibleUnsafe("unsafe_string")) == {'__ansible_unsafe': 'unsafe_string'}
    assert encoder.default(vault.VaultSecret("vault_string")) == {'__ansible_vault': 'vault_string'}
    assert encoder.default({'k': 'v'}) == {'k': 'v'}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-12 23:12:38.483020
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence
    # Mapping
    ansible_json_encoder_mapping_instance = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    mapping_test_object = {'test': 'instance'}
    assert ansible_json_encoder_mapping_instance.default(mapping_test_object) == mapping_test_object
    # Mapping
    ansible_json_encoder_mapping_instance_preprocess_unsafe_true = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=False)

# Generated at 2022-06-12 23:12:46.212551
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import string_types
    import datetime
    import time

    e = AnsibleJSONEncoder()
    assert e.default({}) == {}
    assert e.default([]) == []
    assert e.default([[]]) == [[]]
    assert e.default(ImmutableDict()) == {}
    assert e.default(ImmutableDict(a=1)) == {'a': 1}
    assert e.default(datetime.date.today()) == '{0}'.format(datetime.date.today())
    assert e.default(datetime.datetime.now()) == '{0}'.format(datetime.datetime.now())
    assert e.default(time.time()) == time.time()


# Generated at 2022-06-12 23:12:53.111503
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe_str = '''
    a = b
    c = d
    '''
    unsafe = to_text(unsafe_str)
    unsafe._set_unsafe()
    ansiblejsonencoder = AnsibleJSONEncoder(unsafe)
    ansiblejsonencoder.default(unsafe)
    # The method default of class AnsibleJSONEncoder is a new custom encoder, it does not have
    # any assertions for testing. It will be tested in default_json_handler.py


# Generated at 2022-06-12 23:13:01.154012
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe

    # "root" string
    value = AnsibleUnsafe("hello world")
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    assert encoder.default(value) == {'__ansible_unsafe': 'hello world'}

    # "first level" string
    value = ["hello world", AnsibleUnsafe("hello world")]
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    assert encoder.default(value) == ['hello world', {'__ansible_unsafe': 'hello world'}]

    # "second level" string
    value = [{'foo': ['hello world', AnsibleUnsafe("hello world")]}]

# Generated at 2022-06-12 23:13:07.192106
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) == None

    def test_dict(o):
        assert AnsibleJSONEncoder().default(o) == o

    test_dict({})

    # test hostvars
    test_dict({'fco': {'hostvars': {'127.0.0.1': {'ansible_host': '127.0.0.1', 'ansible_port': 5986}}}})



# Generated at 2022-06-12 23:13:16.475925
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
 
    class UnsafeClass(unicode):
        """This class exists to test AnsibleJSONEncoder method default
        It exists to emulate the AnsibleUnsafe class"""
        __UNSAFE__ = True
        __ENCRYPTED__ = False

    class EncryptedClass(unicode):
        """This class exists to test AnsibleJSONEncoder method default
        It exists to emulate the AnsibleVaultEncryptedUnicode class"""
        __UNSAFE__ = False
        __ENCRYPTED__ = True

    class DictionarySubclass(dict):
        """This class exists to test AnsibleJSONEncoder method default
        Because Ansible uses custom dictionary subclasses.
        """
        pass


# Generated at 2022-06-12 23:13:26.976837
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj_dict = AnsibleJSONEncoder().default({'a': 'b'})
    # When object is dict type, return the same object
    assert obj_dict == {'a': 'b'}

    from ansible.parsing.vault import VaultLib

    vault_obj = VaultLib()
    vault_key = vault_obj.encrypt('password')
    # When object is AnsibleVaultEncryptedUnicode type, return __ansible value
    ansible_vault_obj = AnsibleJSONEncoder().default(vault_key)

# Generated at 2022-06-12 23:13:36.100129
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.basic import AnsibleVaultEncryptedUnicode
    _AnsibleJSONEncoder = AnsibleJSONEncoder(mapping=True)
    assert(_AnsibleJSONEncoder.default({}) == {})
    assert(_AnsibleJSONEncoder.default(datetime.datetime.now()) == '1970-01-01T00:00:00.000000')
    assert(_AnsibleJSONEncoder.default(AnsibleUnsafe('hello')) == {'__ansible_unsafe': 'hello'})
    assert(_AnsibleJSONEncoder.default(AnsibleVaultEncryptedUnicode('hello')) == {'__ansible_vault': 'hello'})

# Generated at 2022-06-12 23:13:45.159492
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(None) is None

    # Ignore encrypted object
    class AnsibleVault:
        __ENCRYPTED__ = True
    encrypted_obj = AnsibleVault()
    assert ansible_json_encoder.default(encrypted_obj) is encrypted_obj

    # Accept list and tuple
    class Wrapper:
        def __init__(self, inner_obj):
            self.inner_obj = inner_obj
    assert ansible_json_encoder.default([1, 2]) == [1, 2]
    assert ansible_json_encoder.default((1, 2)) == (1, 2)

# Generated at 2022-06-12 23:13:55.635082
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Unit test values
    ansible_unsafe = 'ansible_unsafe'
    ansible_vault = 'ansible_vault'
    date = datetime.date(2015, 1, 1)
    datetime = datetime.datetime(2015, 1, 1, 0, 0, 0)
    ansible_mapping = {'ansible': 'mapping'}
    # Expected values after encoding
    ansible_unsafe_encoded = {'__ansible_unsafe': 'ansible_unsafe'}
    ansible_vault_encoded = {'__ansible_vault': ansible_vault}
    date_encoded = '2015-01-01'
    datetime_encoded = '2015-01-01T00:00:00'

# Generated at 2022-06-12 23:14:19.904988
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Foo:
        pass

    f = Foo()
    d = {'foo': True, 'bar': False, 'baz': 1, 'foobar': 'hello', 'range': range(0, 4),
         'obj': {'foo': 'hello', 'bar': 1, 'baz': 'world'},
         'vault': Foo(),
         'unsafe': Foo(),
         'vault_text': Foo(),
         'date': datetime.date(year=2020, month=1, day=1)}
    d['vault'].__ENCRYPTED__ = True
    d['vault']._ciphertext = 'encrypted_data'
    d['vault_text'].__ENCRYPTED__ = True
    d['vault_text']._ciphertext = 'encrypted_data'
   

# Generated at 2022-06-12 23:14:30.234125
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert AnsibleJSONEncoder().default(object()) == "Object"
    assert AnsibleJSONEncoder().default(int(0)) == 0
    assert AnsibleJSONEncoder().default('string') == 'string'
    assert AnsibleJSONEncoder().default({'key1': 'value1', 'key2': 'value2'}) == {'key1': 'value1', 'key2': 'value2'}
    assert AnsibleJSONEncoder().default([{'key1': 'value1'}, {'key2': 'value2'}]) == [{'key1': 'value1'}, {'key2': 'value2'}]
    assert AnsibleJSONEncoder().default({}) == {}
    assert AnsibleJSONEncoder().default([]) == []
    assert AnsibleJSONEncoder().default(True) == True
    assert Ans

# Generated at 2022-06-12 23:14:37.471559
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys
    import unittest
    from ansible.module_utils._text import to_bytes, to_text

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # We want the default test runner to be used to execute the test suite
    # The default test runner will execute all the test cases in the specified python module
    # The test case class name must start with Test and the test method name must start with test
    # Test runner looks for the test case class within the python module specified in command line
    # If the test case class name or test method name does not follow the above naming convention, it is ignored
    # python -m unittest TestAnsibleJSONEncoder
    # python -m unittest TestAnsibleJSONEncoder.TestAnsibleJSONEncoder.test

# Generated at 2022-06-12 23:14:46.809183
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.text import to_text
    from ansible.parsing.vault import VaultLib
    vault_pwd = b'ansible'

# Generated at 2022-06-12 23:14:56.853843
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    class DummyVault:
        __ENCRYPTED__ = True
        _ciphertext = 'adsfadsf'
    class DummyVaultDict:
        __ENCRYPTED__ = True
        _ciphertext = {'asdf': 'asdf'}
    class DummyUnsafe:
        __UNSAFE__ = True
    class DummyUnsafeDict:
        __UNSAFE__ = True
    assert json_encoder.default(DummyVault()) == {'__ansible_vault': 'adsfadsf'}
    assert json_encoder.default(DummyVaultDict()) == {'__ansible_vault': {'asdf': 'asdf'}}

# Generated at 2022-06-12 23:15:05.870235
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib
    import base64
    import datetime

    plaintext = to_text(b"test_plaintext", errors='surrogate_or_strict')
    plaintext_bytes = b"test_plaintext"

    assert plaintext == "test_plaintext"
    assert plaintext_bytes == b"test_plaintext"


# Generated at 2022-06-12 23:15:09.495597
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    JsonEncoder = AnsibleJSONEncoder()
    class A:
        pass
    a = A()
    assert JsonEncoder.default(a) == '<ansible.module_utils.parsing.convert_ansible.A object at 0x7ff2becb8a90>'

# Generated at 2022-06-12 23:15:17.828666
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    # for testing purposes, use ``__ENCRYPTED__`` in lieu of ``ansible.parsing.vault.VaultSecret``
    test_vault_secret = type('VaultSecret', (object,), {'__ENCRYPTED__': True, '_ciphertext': b'Hello, world'})

    encoder = AnsibleJSONEncoder(vault_to_text=True)
    assert encoder.default(test_vault_secret()) == 'Hello, world'

    encoder = AnsibleJSONEncoder(vault_to_text=False)
    assert encoder.default(test_vault_secret()) == {'__ansible_vault': b'Hello, world'}

    # mock ``AnsibleUnsafe``
   

# Generated at 2022-06-12 23:15:27.461956
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test with safe string
    fake_safe_string = 'fake_safe_string'
    assert AnsibleJSONEncoder().default(fake_safe_string) == fake_safe_string

    # Test with vault string
    fake_vault_string = to_text('fake_vault_string')
    fake_vault_string.__ENCRYPTED__ = True
    fake_vault_string.__VAULT_VERSION__ = '1.1'
    fake_vault_string.__VAULT_CIPHER__ = 'AES256'
    fake_vault_string.__VAULT_SECRET_KEY__ = 'fake_vault_secret_key'
    fake_vault_string.__VAULT_SALT__ = 'fake_vault_salt'
    fake_vault_string.__VA

# Generated at 2022-06-12 23:15:38.017057
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.common._json_compat import AnsibleUnsafeText
    from ansible.module_utils.common._json_compat import AnsibleUnsafeBytes
    from ansible.module_utils.common._json_compat import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.common._json_compat import AnsibleVaultEncryptedBytes

    json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    json_str = json.dumps({'a': {'b': {'c': AnsibleUnsafeText('Text')}}}, cls=AnsibleJSONEncoder)
    assert json_str == '{"a": {"b": {"c": {"__ansible_unsafe": "Text"}}}}'
    json_

# Generated at 2022-06-12 23:16:13.573609
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Arrange
    ansible_unsafe = AnsibleUnsafe(b"test")
    ansible_vault = AnsibleVaultEncryptedUnicode(b'test')
    dictionary = {1: ansible_unsafe, 2: ansible_vault, 'b': 'string'}
    ansible_json_encoder = AnsibleJSONEncoder()

    # Act
    result = ansible_json_encoder.default(dictionary)

    # Assert
    assert(isinstance(result, dict))
    assert(result[1] == {'__ansible_unsafe': 'test'})
    assert(result[2] == {'__ansible_vault': 'test'})


# Generated at 2022-06-12 23:16:19.733198
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test __ENCRYPTED__ is True
    import ansible.parsing.vault as vault
    vault_value = vault.VaultLib("test")
    encrypted_value = vault_value.encrypt("test_value")
    assert encoder.default(encrypted_value) == {'__ansible_vault': encrypted_value._ciphertext}

    # test __UNSAFE__ is True
    from ansible.module_utils.basic import AnsibleUnsafe
    unsafe_value = AnsibleUnsafe("test")
    assert encoder.default(unsafe_value) == {'__ansible_unsafe': to_text(unsafe_value, errors='surrogate_or_strict', nonstring='strict')}

    # test isinstance(o, Mapping

# Generated at 2022-06-12 23:16:28.097789
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault
    """
    Check the method default of class AnsibleJSONEncoder
    """
    # create a vault object

# Generated at 2022-06-12 23:16:36.472060
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test method default of class AnsibleJSONEncoder
    '''
