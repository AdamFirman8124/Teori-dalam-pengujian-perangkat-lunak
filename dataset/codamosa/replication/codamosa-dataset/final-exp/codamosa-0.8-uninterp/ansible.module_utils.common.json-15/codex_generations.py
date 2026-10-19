

# Generated at 2022-06-12 23:06:43.337260
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-12 23:06:51.110395
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:06:54.041984
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    class Foo(object):
        def __getitem__(self, key):
            return 10

    assert encoder.default(Foo()) is Foo()



# Generated at 2022-06-12 23:06:56.429102
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(dict(a=42)) == dict(a=42)

# Generated at 2022-06-12 23:07:02.482274
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    x = u'\uc774\ubbf8\uc9c0'
    data = {x:x}

    encoder = AnsibleJSONEncoder()
    value = encoder.default(data)

    assert value == data
    assert type(value) == dict
    assert type(value.keys()[0]) == unicode
    assert type(value.values()[0]) == unicode


# Generated at 2022-06-12 23:07:12.655301
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import unittest2 as unittest
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence
    from ansible.parsing.vault import VaultLib
    import datetime
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.six import text_type, binary_type

    class AnsibleUnsafe(text_type):
        __UNSAFE__ = True


    class AnsibleVault(text_type):
        __ENCRYPTED__ = True


    class Hostvars(Mapping):
        pass



# Generated at 2022-06-12 23:07:20.137805
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test_encoder_unsafe
    class TestUnsafe(object):
        __UNSAFE__ = True
        def __init__(self, s):
            self.s = s
        def __str__(self):
            return self.s
    json_value = json.dumps(TestUnsafe('passwd'), cls=AnsibleJSONEncoder)
    assert json_value == '{"__ansible_unsafe": "passwd"}'

    # test_encoder_vault
    class TestVault(object):
        __ENCRYPTED__ = True
        def __init__(self, s):
            self._ciphertext = s
        def __str__(self):
            return self._ciphertext

# Generated at 2022-06-12 23:07:30.280583
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test _vault_to_text is False
    ansible_encoder = AnsibleJSONEncoder(False, False)
    # Test __ENCRYPTED__ is False
    result = ansible_encoder.default(object())
    expected = '{}'
    assert result == expected, \
        'Expected to return %s, got %s' % (expected, result)

    # Test __ENCRYPTED__ is True
    result = ansible_encoder.default(object())
    expected = '{}'
    assert result == expected, \
        'Expected to return %s, got %s' % (expected, result)


# Generated at 2022-06-12 23:07:37.948711
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    import collections
    import sys

    from ansible.module_utils.common.collections import is_sequence

    class AnsibleUnsafe(str):
        __UNSAFE__ = True

    class Ansi(str):
        pass

    ansiblestr = AnsibleUnsafe('test')
    anstr = Ansi('test')
    ansi_key_dict = {Ansi('key'): 'value'}
    ansi_dict = {'key': 'value'}
    ansiblestr_dict = {'key': ansiblestr}
    ansunlist = [ansiblestr]
    ansiblestr_unsafe_dict = {AnsibleUnsafe('key'): AnsibleUnsafe('value')}
    ansiblestr_safe_dict = {'key': AnsibleUnsafe('value')}
   

# Generated at 2022-06-12 23:07:44.921986
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Encode ansible internal data types
    :return: tuple(default, expected)
    """
    encoder = AnsibleJSONEncoder()
    assert encoder.default(True) is True
    assert encoder.default(False) is False
    assert encoder.default({}) == {}
    assert encoder.default(dict(a=1, b=2)) == {"a": 1, "b": 2}
    assert encoder.default((1, 2, 3)) == [1, 2, 3]
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(1) == 1
    assert encoder.default(1.0) == 1.0

# Generated at 2022-06-12 23:07:50.117248
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    assert aje.default("FOO") == "FOO"
    assert aje.default("FOO".encode('utf-8')) == u"FOO"



# Generated at 2022-06-12 23:07:54.893740
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    expected = {'__ansible_unsafe': u'\u00e2'}
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    actual = encoder.default(unicode(u'\u00e2'))
    assert expected == actual


# Generated at 2022-06-12 23:07:58.678828
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode(AnsibleUnsafe('')) == '{"__ansible_unsafe": ""}'
    assert AnsibleJSONEncoder().encode(AnsibleUnsafe('', vault_sensitive=True)) == '{"__ansible_vault": ""}'

# Generated at 2022-06-12 23:08:03.688239
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('my string') == 'my string'
    assert encoder.default('my\nstring') == 'my\nstring'

    # hostvars and other objects
    assert encoder.default({1: 2}) == {1: 2}

    # date object
    assert encoder.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()



# Generated at 2022-06-12 23:08:12.309807
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    safetext = "safe text"
    unsafe = AnsibleUnsafeText(safetext)
    encrypted = AnsibleVaultEncryptedUnsafeText(safetext)

    valid_output = {'__ansible_unsafe': safetext, '__ansible_vault': safetext}

    assert AnsibleJSONEncoder().encode(unsafe) == json.dumps(valid_output, separators=(',', ':'))
    assert AnsibleJSONEncoder(vault_to_text=True).encode(encrypted) == json.dumps(valid_output, separators=(',', ':'))



# Generated at 2022-06-12 23:08:22.643638
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test_type_none
    assert AnsibleJSONEncoder().default(None) == None

    # test_type_dict
    assert AnsibleJSONEncoder().default({'foo': 'bar'}) == {'foo': 'bar'}

    # test_type_date
    date = datetime.date(2015, 1, 10)
    assert AnsibleJSONEncoder().default(date) == '2015-01-10'

    # test_type_datetime
    datetime_obj = datetime.datetime(2015, 1, 10)
    assert AnsibleJSONEncoder().default(datetime_obj) == '2015-01-10T00:00:00'

    # test_type_vault
    vault_obj = 'bar'
    vault_obj.__ENCRYPTED__ = True
    vault_obj._c

# Generated at 2022-06-12 23:08:32.292819
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib, VaultSecret

    def run(o, **kwargs):
        return AnsibleJSONEncoder(**kwargs).default(o)

    # Test safe string
    assert run('hello') == 'hello'

    # Test unsafe text
    assert run('hello'.encode('utf-16')) == {'__ansible_unsafe': to_text('hello'.encode('utf-16'), errors='surrogate_or_strict')}

    # Test unsafe object
    class MyUnsafeText(str):
        __UNSAFE__ = True

    unsafe = MyUnsafeText('hello')
    assert run(unsafe) == {'__ansible_unsafe': 'hello'}

    # Test vault object
    ciphertext = VaultLib().encrypt('hello')
    assert run

# Generated at 2022-06-12 23:08:37.609039
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vault_password = VaultSecret('secret')
    vault = VaultLib([vault_password])
    ciphertext = vault.encrypt('username:password')


# Generated at 2022-06-12 23:08:42.228705
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_str = json.dumps(
        {
            "name": "ansible-playbook",
            "version": "2.6.1"
        },
        cls=AnsibleJSONEncoder
    )
    assert json_str == '{"name": "ansible-playbook", "version": "2.6.1"}'

# Generated at 2022-06-12 23:08:52.814716
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime

    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default(True) is True
    assert AnsibleJSONEncoder().default(False) is False
    assert AnsibleJSONEncoder().default(0) == 0
    assert AnsibleJSONEncoder().default(2.14) == 2.14
    assert AnsibleJSONEncoder().default(datetime.date(2018, 2, 4)) == '2018-02-04'
    assert AnsibleJSONEncoder().default([1, 2, 3]) == [1, 2, 3]

    o = {'a': 1, 'b': 2, 'c': 3}
    assert AnsibleJSONEncoder().default(o) == o
    assert AnsibleJSONEncoder().default(u'abc') == u'abc'

    # instances of M

# Generated at 2022-06-12 23:09:05.454143
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import binary_type

    # Test for VaultSecret
    secret = VaultSecret('mypassword', b'AES256', b'12345678')

    # Test for AnsibleUnsafe
    test_unsafe = AnsibleUnsafe(binary_type('{"x": "y"}'))
    test_unsafe_text = AnsibleUnsafeText('{"x": "y"}')

    test_dict = {'vault': secret, 'unsafe': test_unsafe, 'unsafe_text': test_unsafe_text}
    result = AnsibleJSONEncoder().encode(test_dict)

# Generated at 2022-06-12 23:09:16.555237
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.module_utils.urls import UnsafeSession
    a = AnsibleUnsafe('unsafe_string')
    b = UnsafeSession(None)
    c = {"a": "b"}
    d = (1, 2, 3, 4)
    e = (1, 2, c, d)
    f = [{"a": "b"}, (1, 2, c, d)]
    encoder = AnsibleJSONEncoder()
    assert encoder.default(a) == {"__ansible_unsafe": 'unsafe_string'}
    assert encoder.default(b) == {"__ansible_unsafe": "unsafe_string"}
    assert encoder.default(c) == c
    assert encoder.default(d) == d
   

# Generated at 2022-06-12 23:09:21.684345
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.basic import AnsibleUnsafe, AnsibleVaultEncryptedUnicode

    e = AnsibleJSONEncoder()

    assert e.default(AnsibleUnsafe('unsafe')) == {'__ansible_unsafe': 'unsafe'}
    assert e.default(AnsibleVaultEncryptedUnicode('vault')) == {'__ansible_vault': 'vault'}

# Generated at 2022-06-12 23:09:30.916915
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    encoder = AnsibleJSONEncoder()


# Generated at 2022-06-12 23:09:41.547507
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test all the different types of objects AnsibleUnsafe can contain
    # test with all possible value of `vault_to_text` in constructor
    # test with all possible value of `preprocess_unsafe` in constructor
    # test with all possible value of `kwargs` (kwargs-s) in constructor
    # test with all possible value of `o` in ansiblejsonencoder_default(o)
    # test the `use default encoder` of default() method
    # test for object of class datetime.date
    d = datetime.date(1984, 7, 4)
    en_d = AnsibleJSONEncoder(False, False, separators=(',', ':'))
    assert en_d.default(d) == '1984-07-04'

# Generated at 2022-06-12 23:09:48.585063
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils import basic

    # AnsibleVaultEncryptedUnicode object
    ansible_vault_encrypted_unicode_obj = basic.AnsibleVaultEncryptedUnicode(b'foo')
    json_str = json.dumps(ansible_vault_encrypted_unicode_obj, cls=AnsibleJSONEncoder, sort_keys=True)
    assert json_str == '{"__ansible_vault": "foo"}'

    # AnsibleVaultEncryptedUnicode object with vault_to_text = True
    ansible_vault_encrypted_unicode_obj = basic.AnsibleVaultEncryptedUnicode(b'foo')

# Generated at 2022-06-12 23:09:57.077845
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vault_pass_1 = "Ansible123"
    ciphertext = VaultLib(vault_pass_1).encrypt("This is a test string", {})

    assert {'__ansible_vault': to_text(ciphertext, errors='surrogate_or_strict', nonstring='strict')} == json.loads(
        json.dumps(VaultSecret(u'Ansible123', ciphertext=ciphertext), cls=AnsibleJSONEncoder)
    )

# Generated at 2022-06-12 23:10:04.396714
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test of instance of AnsibleUnsafe
    test_data = 'Secret Value'
    unsafe = AnsibleUnsafe(test_data)
    assert AnsibleJSONEncoder().default(unsafe) == json.dumps({'__ansible_unsafe': test_data})

    # Test of instance of AnsibleVaultEncryptedUnicode
    test_data = 'Secret Value'
    vault = AnsibleVaultEncryptedUnicode(test_data)
    assert AnsibleJSONEncoder().default(vault) == json.dumps({'__ansible_vault': test_data})

    # Test of instance of AnsibleVaultEncryptedUnicode
    test_data = 'Secret Value'
    vault = AnsibleVaultEncryptedUnicode(test_data)

# Generated at 2022-06-12 23:10:11.071537
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    vault_text = "test"
    vault_password = "ansible"
    vault = VaultLib(vault_password)
    vault_str = vault.encrypt(vault_text)
    vault_obj = vault.decrypt(vault_str)
    v = ansible.module_utils.json_utils.AnsibleJSONEncoder()
    assert v.default(vault_obj) == {'__ansible_vault': vault_str}

# Generated at 2022-06-12 23:10:21.065109
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes, to_text, to_unicode
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleUnsafe
    import datetime

    safety_boilerplate = 'Sensitive data obscured'

    class TestUnsafeClass(AnsibleUnsafe):
        __UNSAFE__ = True

    class TestVaultClass(AnsibleUnsafe):
        __ENCRYPTED__ = True

    # NOTE: we can compare encoders like this as they are just json.JSONEncoder subclasses
    # however, ``AnsibleJSONEncoder.iterencode`` is not compatible with the json.JSONEncoder
    # interface, so we don't test it in this unit test

# Generated at 2022-06-12 23:10:30.328548
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('test') == 'test'
    assert AnsibleJSONEncoder().default(u'test') == u'test'
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default(False) == False
    assert AnsibleJSONEncoder().default(None) == None
    assert AnsibleJSONEncoder().default(1.0) == 1.0
    assert AnsibleJSONEncoder().default(1j) == 1j


# Generated at 2022-06-12 23:10:32.800680
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()
    assert a.default({'test': 'ansible'}) == {'test': 'ansible'}



# Generated at 2022-06-12 23:10:40.926161
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert AnsibleJSONEncoder().default(None) == 'null'
    assert AnsibleJSONEncoder().default(False) == 'false'
    assert AnsibleJSONEncoder().default(True) == 'true'
    assert AnsibleJSONEncoder().default(-42) == "-42"
    assert AnsibleJSONEncoder().default(-42.8) == "-42.8"
    assert AnsibleJSONEncoder().default(1 + 2j) == "1+2j"
    assert AnsibleJSONEncoder().default(b'x') == "x"
    assert AnsibleJSONEncoder().default(u'x') == "x"
    assert AnsibleJSONEncoder().default('x') == "x"
    assert AnsibleJSONEncoder().default(u'\u4321') == '1'

# Generated at 2022-06-12 23:10:49.857103
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    o = {'__ansible_facts': {'a': 'b'}}
    assert '"a": "b"' in aje.encode(o)
    assert aje.encode({'a': 'b'}) == '{"a": "b"}'
    o = {'a': 'b'}
    assert aje.encode(o) == '{"a": "b"}'
    assert aje.encode({'a': 'b'}) == '{"a": "b"}'
    # assert aje.encode({'a': 'b'}) == '{"a": "b", "c": "d"}'


# Generated at 2022-06-12 23:10:53.116698
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default({"1": "hi"}) == {"1": "hi"}
    assert ansible_json_encoder.default([1, 2, 3]) == [1, 2, 3]


# Generated at 2022-06-12 23:10:59.999537
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test case 1: obj is instance of AnsibleVaultEncryptedUnicode
    test_obj = "👾"
    obj_with_vault = AnsibleVaultEncryptedUnicode(test_obj)
    assert AnsibleJSONEncoder().default(obj_with_vault) == '"👾"'
    assert AnsibleJSONEncoder(vault_to_text=True).default(obj_with_vault) == '"👾"'
    assert AnsibleJSONEncoder(vault_to_text=False).default(obj_with_vault) == '{"__ansible_vault": "👾"}'

    # Test case 2: obj is instance of AnsibleUnsafeText
    test_obj = "👾"
    obj_with_unsafe = AnsibleUnsafeText(test_obj)

# Generated at 2022-06-12 23:11:10.204847
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    from ansible.module_utils.common.text.converters import json_loads
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import PY3

    helper = AnsibleJSONEncoder()

    class FakeUnsafe:
        __UNSAFE__ = True

    class FakeVault:
        __ENCRYPTED__ = True
        _ciphertext = u'vault'
        def __str__(self):
            return str(self.__class__)

    class FakeDate(datetime.date):
        def __init__(self, *args, **kwargs):
            super(FakeDate, self).__init__(*args)

    class FakeObject:
        pass


# Generated at 2022-06-12 23:11:19.770137
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder(indent = None, sort_keys = False, ensure_ascii = True)
    assert encoder.default(None) == 'null'
    assert encoder.default(True) == 'true'
    assert encoder.default(False) == 'false'
    assert encoder.default(146) == '146'
    assert encoder.default(float(146)) == '146.0'
    assert encoder.default('abc') == '"abc"'
    assert encoder.default([146]) == '[146]'
    assert encoder.default({'a': 146}) == '{"a": 146}'
    # date object
    date = datetime.date(2019, 6, 1)
    assert encoder.default(date) == '2019-06-01'
    # hostvars and other

# Generated at 2022-06-12 23:11:30.434696
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    vault = VaultLib([])
    secret = VaultSecret('dummy_password', 'dummy_password')
    v = '$ANSIBLE_VAULT;1.1;AES256' + '\n' + vault._encrypt_bytes(secret, vault.encrypt('test')) + '\n'
    assert AnsibleJSONEncoder().default(v) == {'__ansible_vault': '$ANSIBLE_VAULT;1.1;AES256\n363033323632323163353033386639353466303335383734623336333935333166306563353262322\n'}

# Generated at 2022-06-12 23:11:34.776798
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultEditor

    assert json.dumps(VaultEditor(None), cls=AnsibleJSONEncoder, sort_keys=True, indent=4) == '{\n    "__ansible_vault": "VaultLib(None)"\n}'


# Generated at 2022-06-12 23:11:50.527296
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:12:00.172725
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.six import binary_type
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    x = AnsibleUnsafe('false')
    x = getattr(x, '__UNSAFE__', False)
    assert x == True

    y = AnsibleJSONEncoder()
    z = y.default(x)
    assert z == {'__ansible_unsafe': u'false'}

    # Test for vault objects
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    plaintext = u'four score and seven years ago'
    password = u'sekret'

    vault = VaultLib([('default', VaultSecret(password))])

    encrypted_text = vault.encrypt(plaintext)

# Generated at 2022-06-12 23:12:10.496487
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes, to_text

    # test AnsibleUnsafe
    if not boolean(os.environ.get('ANSIBLE_TEST_UNSAFE_ENCODE', 'False')):
        unsafe_obj = to_text(b"Unsafe")
    else:
        unsafe_obj = to_bytes(b"Unsafe")
    assert AnsibleJSONEncoder().default(unsafe_obj) == unsafe_obj

    # test AnsibleVault
    vault_lib = VaultLib([])
    secret = vault_lib.encrypt(b'Secret')

# Generated at 2022-06-12 23:12:19.445629
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Unit test for method default of class AnsibleJSONEncoder
    '''
    import datetime
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE, BOOLEANS_FALSE

    assert(AnsibleJSONEncoder().default(None) == None)
    assert(AnsibleJSONEncoder().default(True) == True)
    assert(AnsibleJSONEncoder().default(False) == False)
    assert(AnsibleJSONEncoder().default(1) == 1)
    assert(AnsibleJSONEncoder().default(0) == 0)
    assert(AnsibleJSONEncoder().default(1.1) == 1.1)
    assert(AnsibleJSONEncoder().default(0.0) == 0.0)

# Generated at 2022-06-12 23:12:29.506458
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    value = AnsibleJSONEncoder().encode(4)
    assert value == '4'

    value = AnsibleJSONEncoder().encode(5.5)
    assert value == '5.5'

    value = AnsibleJSONEncoder().encode('ccc')
    assert value == '"ccc"'

    value = AnsibleJSONEncoder().encode({'a': 1, 'b': 2})
    assert value == '{"a": 1, "b": 2}'

    value = AnsibleJSONEncoder().encode(['a', 'b'])
    assert value == '["a", "b"]'

    now1 = datetime.datetime.now()
    now2 = datetime.datetime.now()
    now_time_value = AnsibleJSONEncoder().encode([now1, now2])
   

# Generated at 2022-06-12 23:12:32.674241
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    result = json_encoder.default(3)
    assert result == 3
    result = json_encoder.default("hello")
    assert result == "hello"

# Generated at 2022-06-12 23:12:39.028350
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_values = [
        {'a': 'b'},
        (1, 2, 3),
        set([1, 2, 3]),
        datetime.datetime(2015, 1, 1, 12, 34, 56),
        datetime.date(2015, 1, 1),
    ]

    ansible_json_encoder = AnsibleJSONEncoder()
    for i in test_values:
        assert ansible_json_encoder.default(i) == i

# Generated at 2022-06-12 23:12:41.989583
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # The method default of AnsibleJSONEncoder will be tested.
    # We need to create a class object and then call the __init__ function
    # for the class object.
    test_obj = AnsibleJSONEncoder(True,False)
    test_obj.default(None)
    assert test_obj
    assert test_obj.default


# Generated at 2022-06-12 23:12:48.892633
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    obj_class = type('foo', (object,), {'__ENCRYPTED__': False, '__UNSAFE__': False})
    obj = obj_class()
    assert obj == AnsibleJSONEncoder().default(obj)

    obj_class = type('foo', (object,), {'__ENCRYPTED__': True, '__UNSAFE__': False, '_ciphertext': 'ciphertext'})
    obj = obj_class()
    assert {'__ansible_vault': 'ciphertext'} == AnsibleJSONEncoder().default(obj)


# Generated at 2022-06-12 23:12:58.225877
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:13:17.862520
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(None) == None
    assert encoder.default(1) == 1
    assert encoder.default("1") == "1"
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    assert encoder.default(datetime.datetime(2019, 11, 11, 21, 38)) == '2019-11-11T21:38:00'
    # date object
    assert encoder.default(datetime.date(2019, 11, 11)) == '2019-11-11'
    # invalid value
    assert encoder.default(ToUnicode()) == 'test'

# Generated at 2022-06-12 23:13:28.810319
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    assert aje.default(dict(a=1)) == dict(a=1) # check if aje encodes a dictionary
    assert aje.default(dict(a=1, b=2)) == dict(a=1, b=2) # check if aje encodes a dictionary
    assert aje.default(1) == 1 # check if aje encodes an int
    assert aje.default(1.1) == 1.1 # check if aje encodes a float
    assert aje.default([1, 2, 3]) == [1, 2, 3] # check if aje encodes a list
    assert aje.default((1, 2, 3)) == [1, 2, 3] # check if aje encodes a tuple

# Generated at 2022-06-12 23:13:36.373809
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    # str
    assert json.dumps(u'abc', cls=encoder) == u'"abc"'
    # unicode
    assert json.dumps(u'\u2019', cls=encoder) == u'"\u2019"'
    # datetime
    date = datetime.date(2015, 1, 1)
    assert json.dumps(date, cls=encoder) == '"2015-01-01"'
    # mapping
    mapping = {u'\u2019': u'\u2019'}
    assert json.dumps(mapping, cls=encoder) == '{"\u2019": "\u2019"}'
    # sequence
    sequence = (u'\u2019',)

# Generated at 2022-06-12 23:13:45.916639
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json

    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

    # We override JSONEncoder.default in order to handle our own objects
    # This method will always be called with a known type
    def override_default(self, o):
        if isinstance(o, AnsibleUnsafe):
            return {'__ansible_unsafe': to_text(o, errors='surrogate_or_strict', nonstring='strict')}
        else:
            raise TypeError('%r is not JSON serializable' % o)

    # We just replace the default method and use the original method for the rest
    json.JSONEncoder.default = override_default

# Generated at 2022-06-12 23:13:56.138173
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # We test by examples. Other case are similar
    # Default values
    default_kwargs = dict(sort_keys=False, indent=2, separators=(',', ': '))

    ### Test case with default values
    # Basic python types
    # str
    assert json.dumps(str('abc'), cls=AnsibleJSONEncoder, **default_kwargs) == '"abc"'
    # int
    assert json.dumps(int(123), cls=AnsibleJSONEncoder, **default_kwargs) == '123'
    # float
    assert json.dumps(float(123.1), cls=AnsibleJSONEncoder, **default_kwargs) == '123.1'
    # bool

# Generated at 2022-06-12 23:14:03.903845
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    assert json.dumps(dict(a=None), cls=AnsibleJSONEncoder) == '{"a": null}'
    assert json.dumps(dict(a=None, b="foo"), cls=AnsibleJSONEncoder) == '{"a": null, "b": "foo"}'
    assert json.dumps(dict(a=dict(b=None,c="foo")), cls=AnsibleJSONEncoder) == '{"a": {"b": null, "c": "foo"}}'

    # datetime
    now = datetime.datetime.now()
    assert now.isoformat() == json.dumps(now, cls=AnsibleJSONEncoder)
    assert now.isoformat() == json.dumps(dict(a=now), cls=AnsibleJSONEncoder)

   

# Generated at 2022-06-12 23:14:13.884380
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # Empty dict
    empty_dict = {}
    assert encoder.default(empty_dict) == empty_dict

    # Dict with values
    dict_with_values = {'a': 'b', 'c': 'd'}
    assert encoder.default(dict_with_values) == dict_with_values

    # Date object
    date_object = datetime.datetime.strptime('2019-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
    assert encoder.default(date_object) == '2019-01-01T00:00:00'

    # ValueError
    assert encoder.default(None) == 'null'

# Generated at 2022-06-12 23:14:18.895438
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    AnsibleJsonEncoder.default should return proper values for different types of objects.
    """

    data = {'a': 'b', 'c': [1, 2, 3]}
    assert repr(json.dumps(data, cls=AnsibleJSONEncoder)) == repr('{"a": "b", "c": [1, 2, 3]}')

    data = {'a': 'b', 'c': [1, 2, 3], 'd': {'e': 'f'}}
    assert repr(json.dumps(data, cls=AnsibleJSONEncoder)) == repr('{"a": "b", "c": [1, 2, 3], "d": {"e": "f"}}')


# Generated at 2022-06-12 23:14:25.431832
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = AnsibleJSONEncoder()
    assert obj.default("a string") == "a string"
    assert obj.default({ "k": "v"}) == { "k" : "v"}
    assert obj.default({"__ansible_vault": "value"}) == { "__ansible_unsafe" : "value" }
    assert obj.default(["a", "b", "c"]) == [ "a", "b", "c"]
    assert obj.default(("a", "b", "c")) == ("a", "b", "c")


# Generated at 2022-06-12 23:14:34.699022
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import get_file_vault_secret

    vault_secret_password_file = "/Users/joshua.windsor/github/ansible/source.txt"
    vault_secret_password = get_file_vault_secret(vault_secret_password_file)
    vault_secrets = [VaultSecret('password', vault_secret_password)]

# Generated at 2022-06-12 23:15:07.537117
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test vault object
    assert encoder.default(dict(__ENCRYPTED__='foo')) == {'__ansible_vault': 'foo'}
    assert encoder.default(dict(__ENCRYPTED__='foo', __ENCRYPTED_KEY__='bar')) == {'__ansible_vault': 'foo'}

    # test safe object
    assert encoder.default(dict(__UNSAFE__='foo', __ENCRYPTED__='foo')) == {'__ansible_vault': 'foo'}

# Generated at 2022-06-12 23:15:15.516110
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(123456789) == 123456789
    assert AnsibleJSONEncoder().default(123.456789) == 123.456789
    assert AnsibleJSONEncoder().default(True) == True
    assert AnsibleJSONEncoder().default("hello world!") == "hello world!"
    assert AnsibleJSONEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert AnsibleJSONEncoder().default({'test': 1}) == {'test': 1}
    assert AnsibleJSONEncoder().default(datetime.datetime.now()) == datetime.datetime.now().isoformat()

    #FIXME: json.JSONEncoder does not support custom class with __str__ implemented
    #assert AnsibleJSONEncoder().default(datetime.datetime.now()) ==

# Generated at 2022-06-12 23:15:20.127130
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # create an object to test
    test_obj = {
        'foo': 'bar',
        'baz': 'baz',
    }

    # create an instance of the class to test
    test_class = AnsibleJSONEncoder()

    # run the default method and perform test based on result
    result = test_class.default(test_obj)
    for key, value in result.items():
        assert result[key] == test_obj[key]



# Generated at 2022-06-12 23:15:27.813791
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert json.dumps(dict(a='b'), cls=ansible_json_encoder) == '{"a": "b"}'
    assert json.dumps(dict(a=dict(c='d')), cls=ansible_json_encoder) == '{"a": {"c": "d"}}'
    assert json.dumps(dict(a=[dict(c='d')]), cls=ansible_json_encoder) == '{"a": [{"c": "d"}]}'

# Generated at 2022-06-12 23:15:38.411440
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic

    vault_text = "vault text"
    vault = VaultLib([])
    vault_encrypted = vault.encrypt(to_bytes(vault_text))

    # test for vault
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    result = encoder.default(vault_encrypted)
    assert result == vault_text
    assert isinstance(result, basic.AnsibleUnsafeText)

    # test for dict
    encoder = AnsibleJSONEncoder

# Generated at 2022-06-12 23:15:46.867941
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # create an instance
    encoder = AnsibleJSONEncoder()

    # create an object
    obj = object()

    # test unsafe object
    o = object.__new__(UnsafeTest)
    result = encoder.default(o)
    assert result == {}

    # test vault object and use base64.b64encode
    o = object.__new__(VaultTest)
    result = encoder.default(o)
    assert result == {}

    # test date object
    today = datetime.date.today()
    result = encoder.default(today)
    assert result == today.isoformat()

    # test object
    result = encoder.default(obj)
    assert result == obj

    # test object with class that has to_json method
    o = object.__new__(MappingTest)


# Generated at 2022-06-12 23:15:56.982749
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vault = VaultLib([b'$pbkdf2-sha256$10000$H1xFt4C4QVTASKjHfI0Mmg$b9Xq3i/dvtlsa2/xuGmKjA7OuNwNGEV7Ip/N6c9U1Rg'])
    secret = VaultSecret(vault.encrypt('test'))

    test_class = type('TestClass', (object,), {'test_attr': 'test'})

    assert json.dumps({'foo': 'bar'}, cls=AnsibleJSONEncoder) == '{"foo": "bar"}'

# Generated at 2022-06-12 23:16:05.889415
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def foo():
        pass

    assert AnsibleJSONEncoder().default(foo) == foo.__name__
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default('bar') == 'bar'
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert AnsibleJSONEncoder().default("foo") == "foo"
    assert (AnsibleJSONEncoder().default(datetime.datetime(2011, 1, 1, 1, 1, 1)) ==
            datetime.datetime(2011, 1, 1, 1, 1, 1).isoformat())


# Generated at 2022-06-12 23:16:08.294584
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    print('supported json modules:', json.__name__)
    j = AnsibleJSONEncoder()
    data = {'hello': 'world'}
    print(j.encode(data))



# Generated at 2022-06-12 23:16:15.055785
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Set up
    import unittest
    class TestAnsibleJSONEncoder(unittest.TestCase):
        def setUp(self):
            self.encoder = AnsibleJSONEncoder()

        def test_default_o_is_dict(self):
            o = dict(a=10, b=20, c= [1, 2, 'hello'])
            self.assertEqual(self.encoder.default(o), o)

        def test_default_o_is_str(self):
            o = 'hello'
            self.assertEqual(self.encoder.default(o), o)

        def test_default_o_is_byte(self):
            o = b'hello'
            self.assertEqual(self.encoder.default(o), o.decode('utf-8'))