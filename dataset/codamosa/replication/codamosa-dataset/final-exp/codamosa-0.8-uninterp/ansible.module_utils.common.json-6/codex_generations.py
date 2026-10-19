

# Generated at 2022-06-12 23:06:42.107152
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    assert AnsibleJSONEncoder().default(AnsibleUnsafe("unsafe")) == {'__ansible_unsafe': 'unsafe'}


# Generated at 2022-06-12 23:06:45.255480
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enc = AnsibleJSONEncoder()
    assert enc.default(object()) == {}
    assert enc.default(dict()) == {}
    assert enc.default(list()) == []
    assert enc.default(str()) == ''


# Generated at 2022-06-12 23:06:51.945906
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    json_encoder = AnsibleJSONEncoder()
    assert json_encoder.default(u'foo') == u'foo'
    assert json_encoder.default(1) == 1
    assert json_encoder.default(1.1) == 1.1
    assert json_encoder.default([1, 2]) == [1, 2]
    assert json_encoder.default({'bar': u'foo'}) == {'bar': u'foo'}
    assert json_encoder.default(datetime.datetime(2016, 1, 1, 0, 0, 0)) == "2016-01-01T00:00:00"
    assert json_encoder.default(datetime.date(2016, 1, 1)) == "2016-01-01"
    assert json_encoder.default('foo') == 'foo'


# Generated at 2022-06-12 23:07:02.838354
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import StringIO as StringIO
    from ansible.module_utils.six.moves import xrange
    from ansible.module_utils.common.collections import Mapping

    def date_handler(obj):
        return obj.isoformat() if isinstance(obj, datetime.date) else None

    e = AnsibleJSONEncoder()
    a = datetime.datetime.now()
    print(json.dumps(a))
    print(e.encode(a))
    a = datetime.date.today()
    print(json.dumps(a, default=date_handler))

# Generated at 2022-06-12 23:07:13.009174
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils._text import to_native
    import datetime
    from dateutil.tz import tzutc
    from ansible.module_utils.common.collections import Mapping

    # Fake class for testing
    from ansible.module_utils.six import with_metaclass
    class AnsibleUnsafe(with_metaclass(to_bytes, str)):
        __UNSAFE__ = __ENCRYPTED__ = True

    class FakeVariables(Mapping):
        def __init__(self, data):
            self._data = data

        def __getitem__(self, name):
            return self._data[name]


# Generated at 2022-06-12 23:07:19.841096
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ''' test_AnsibleJSONEncoder_default
    This is a unit test for AnsibleJSONEncoder.default.
    '''
    import datetime

    ansible_json_encoder = AnsibleJSONEncoder()
    ansible_unsafe = 'AnsibleUnsafe'
    ansible_vault = 'AnsibleVault'
    a_map = {'key1': 'val1', 'key2': 'val2'}
    now = datetime.datetime.now()

# Generated at 2022-06-12 23:07:31.474526
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class Foo(object):
        def __init__(self, x):
            self.x = x

        def __getattr__(self, attr):
            if attr in ('__UNSAFE__', '__ENCRYPTED__'):
                return False
            raise AttributeError("Foo instance has no attribute '%s'" % attr)

    # __getattr__ is used to implement attributes assigned
    # by AnsibleJSONEncoder, so we need to test that it
    # works properly.
    foo1 = Foo("foo1")
    assert AnsibleJSONEncoder.default(foo1) == "foo1"
    foo2 = Foo("foo2")
    foo2.__UNSAFE__ = True
    assert AnsibleJSONEncoder.default(foo2) == {"__ansible_unsafe": "foo2"}

# Generated at 2022-06-12 23:07:39.104929
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime

    a = AnsibleJSONEncoder()

    # date object
    date_obj = datetime.date(2018, 5, 20)
    assert '2018-05-20' == a.default(date_obj)

    # datetime object
    datetime_obj = datetime.datetime(2018, 5, 20, 10, 10, 0)
    assert '2018-05-20T10:10:00' == a.default(datetime_obj)

    # Mapping object
    dict_obj = {'a': 1, 'b': 2}
    assert dict_obj == a.default(dict_obj)

    # other objects

# Generated at 2022-06-12 23:07:49.821617
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    
    a = AnsibleJSONEncoder()
    if not isinstance(a, object):
        raise AssertionError()
    json_str = a.default('a')
    if json_str != 'a':
        raise AssertionError()
    json_str = a.default(1)
    if json_str != 1:
        raise AssertionError()
    json_str = a.default(1.0)
    if json_str != 1.0:
        raise AssertionError()
    json_str = a.default(['a', 'b'])
    if json_str != ['a', 'b']:
        raise AssertionError()
    json_str = a.default({'a': 1})
    if json_str != {'a': 1}:
        raise AssertionError()
   

# Generated at 2022-06-12 23:08:00.119170
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Test the ``default`` method of ``AnsibleJSONEncoder``
    """
    from ansible.module_utils.six import u
    from ansible.parsing.vault import VaultLib  # noqa


# Generated at 2022-06-12 23:08:12.402099
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types
    from ansible.vars.unsafe_proxy import wrap_var

    class StringSubclass(string_types[0]):
        pass

    plain = StringSubclass(u'plain')
    plain_encoder = AnsibleJSONEncoder()
    plain_encoded = plain_encoder.default(plain)
    assert plain == plain_encoded

    unsafe = wrap_var('unsafe')
    unsafe_encoder = AnsibleJSONEncoder()
    unsafe_encoded = unsafe_encoder.default(unsafe)
    assert {'__ansible_unsafe': 'unsafe'} == unsafe_encoded

    encrypted = wrap_var(VaultLib().encrypt('myvault'))
    encrypted

# Generated at 2022-06-12 23:08:18.627352
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # sub class AnsibleJSONEncoder
    class AnsibleJSONEncoderSub(AnsibleJSONEncoder):
        pass

    # use AnsibleJSONEncoderSub to encode object o
    o = object()
    try:
        json.dumps(o, cls=AnsibleJSONEncoderSub)
    except TypeError as e:
        assert 'is not JSON serializable' in to_text(e)
    else:
        raise AssertionError("This code should not be reached")

# Generated at 2022-06-12 23:08:23.173068
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    json_encoder = AnsibleJSONEncoder()
    date_obj = datetime.date(year=2019, month=1, day=2)
    date_str = '2019-01-02'
    date_encoded_str = json_encoder.default(date_obj)
    assert date_str == date_encoded_str



# Generated at 2022-06-12 23:08:33.061797
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    data = {
        "string": "test",
        "unsafe": b"test",
        "vault": VaultLib("password", "SHA256", "PBKDF2").encrypt("test"),
        "hostvars": {"host1": {"a": "b"}},
        "vault_to_text": VaultLib("password", "SHA256", "PBKDF2").encrypt("test"),
        "date": datetime.date(2015, 8, 23),
        "datetime": datetime.datetime.now()
    }
    data.update({'{0}_unsafe'.format(k): getattr(data[k], '__ENCRYPTED__', False) for k in data})

# Generated at 2022-06-12 23:08:42.273548
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Test method default of AnsibleJSONEncoder class.
    '''
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.common.collections import MutableSequence

    # set up vault object
    vault = VaultLib('secret')
    encrypted_text = vault.encrypt('password')
    vault_obj = vault.new_object(encrypted_text)

    # set up hostvars
    hostvars = {'ansible_facts': {'distribution_release': '16.04'},
                'ansible_system': 'Linux',
                'inventory_hostname': 'test_hostname'}
    hostvars_obj = MutableMapping(hostvars)

    # set

# Generated at 2022-06-12 23:08:52.813538
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test encoder without unsafe/vault conversion
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)

    assert encoder.default('normal-string') == 'normal-string'
    assert encoder.default('unsafe-string') == 'unsafe-string'
    assert encoder.default('vault-string') == 'vault-string'
    assert encoder.default(b'normal-bytes') == 'normal-bytes'
    assert encoder.default(b'unsafe-bytes') == 'unsafe-bytes'
    assert encoder.default(b'vault-bytes') == 'vault-bytes'

    # test encoder with unsafe/vault conversion
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)

# Generated at 2022-06-12 23:08:58.998127
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test vault object
    from ansible.parsing.vault import VaultLib
    try:
        vault = VaultLib([('default', {'vault_password_file': '/dev/null'})])
        vault.unlock('/dev/null')
        test_vault = vault.encrypt('test vault object')
    except Exception:
        # do not test vault object if can not initial VaultLib
        test_vault = False
    # test unsafe object
    from ansible.module_utils.basic import AnsibleUnsafe
    test_unsafe = AnsibleUnsafe('test unsage object')
    # test hostvars and other objects
    test_mapping = {'a': 1, 'b': 2, 'c': 3}
    # test date
    test_date = datetime.date(2019, 2, 14)

# Generated at 2022-06-12 23:09:09.391704
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder_instance = AnsibleJSONEncoder()

    assert encoder_instance.default('str') == 'str'
    assert encoder_instance.default(1) == 1
    assert encoder_instance.default(1.0) == 1.0
    assert encoder_instance.default([1,2,3]) == [1,2,3]
    assert encoder_instance.default((1,2,3,)) == (1,2,3,)
    assert encoder_instance.default(None) == None
    assert encoder_instance.default(False) == False
    assert encoder_instance.default({'key1':'value1', 'key2':'value2'}) == {'key1':'value1', 'key2':'value2'}

# Generated at 2022-06-12 23:09:19.921724
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class AnsibleUnsafe(str):
        __UNSAFE__ = True

    class AnsibleVault(object):

        __ENCRYPTED__ = True

        def __init__(self, ciphertext):
            self._ciphertext = ciphertext

    class Foo(object):

        def __init__(self, a, b):
            self.a = a
            self.b = b


# Generated at 2022-06-12 23:09:24.832300
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()

    from ansible.module_utils.common.text.formatters import Netmask
    a = Netmask('0.0.0.1/24')
    b = aje.default(a)
    assert isinstance(b, str)
    assert b == '0.0.0.1/24'

    a = datetime.datetime.utcnow()
    b = aje.default(a)
    assert isinstance(b, str)
    assert b == a.isoformat()



# Generated at 2022-06-12 23:09:31.852339
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    assert AnsibleJSONEncoder().default(datetime.date(2017,5,5)) == '2017-05-05'
    assert AnsibleJSONEncoder().default(datetime.datetime(2017,5,5,1,1,1,1)) == '2017-05-05T01:01:01.000001'



# Generated at 2022-06-12 23:09:42.530433
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def _test_AnsibleJSONEncoder_default(o, expected_result):
        assert expected_result == AnsibleJSONEncoder().default(o)

    _test_AnsibleJSONEncoder_default(dict([('a', 'a1'), ('b', 'b1')]),
                                     dict([('a', 'a1'), ('b', 'b1')]))
    _test_AnsibleJSONEncoder_default(['a', 'b'], ['a', 'b'])

# Generated at 2022-06-12 23:09:50.799746
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    import datetime

    json_encoder = AnsibleJSONEncoder()

    # string
    assert json_encoder.default('test') == 'test'

    # unicode
    assert json_encoder.default(u'test') == u'test'

    # int
    assert json_encoder.default(10) == 10

    # float
    assert json_encoder.default(1.1) == 1.1

    # datetime
    assert json_

# Generated at 2022-06-12 23:09:59.172043
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    assert(j.default(datetime.datetime(2017, 3, 3, 15, 23)) == '2017-03-03T15:23:00')
    assert(j.default(datetime.date(2017, 3, 3)) == '2017-03-03')


if __name__ == '__main__':
    import unittest

    class TestAnsibleJSONEncoder(unittest.TestCase):
        def setUp(self):
            self.date = datetime.date(2017, 3, 3)
            self.datetime = datetime.datetime(2017, 3, 3, 15, 23)

        def test_default(self):
            j = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:10:07.782087
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enc = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    # test 1
    class test_obj_1(object):
        pass

    obj_1 = test_obj_1()
    obj_1.__dict__['Test1'] = 'value 1'
    obj_1.__dict__['Test2'] = 'value 2'

    assert enc.default(obj_1) == {'Test1': 'value 1', 'Test2': 'value 2'}

    # test 2
    class test_obj_2(object):
        def __init__(self):
            self.a = 'test_obj_2'

    obj_2 = test_obj_2()
    obj_2.__dict__['Test1'] = 'value 1'
    obj_2.__dict__

# Generated at 2022-06-12 23:10:15.298593
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBoolean, AnsibleUnsafeText
    import os

    # Vault text
    vault_text = AnsibleUnsafeText(os.urandom(32), vault_id='1234567')
    assert vault_text.__class__ == AnsibleUnsafeText
    assert vault_text.__UNSAFE__ == True
    assert vault_text.__ENCRYPTED__ == True
    assert vault_text._ciphertext == os.urandom(32)
    assert vault_text._vault_id == '1234567'

    # Vault Boolean
    vault_boolean = AnsibleUnsafeBoolean(False, vault_id='1234567')
    assert vault_boolean.__class__ == AnsibleUnsafeBoolean
    assert vault_boolean.__UN

# Generated at 2022-06-12 23:10:26.536388
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    A_STRING = u'a string'
    A_INT = 42
    A_DICT = {'k': 'v'}
    A_LIST = ['v1', 'v2']

    # Test with unsafe object
    value = AnsibleUnsafe(A_STRING)
    result = AnsibleJSONEncoder(preprocess_unsafe=True).default(value)
    assert result == {
        '__ansible_unsafe': A_STRING
    }

    # Test with encrypted object
    vault_password = 'password'
    ciphertext = VaultLib(vault_password).encrypt(A_STRING)

# Generated at 2022-06-12 23:10:36.361842
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.unsafe_finder import AnsibleUnsafeText

    # Testing for vault object
    enc = AnsibleJSONEncoder(vault_to_text=False)
    secret = VaultSecret('secret')
    secret._ciphertext = b'ciphertext'
    assert enc.default(secret) == {'__ansible_vault': 'ciphertext'}

    # Testing for unsafe object
    enc = AnsibleJSONEncoder(vault_to_text=False)
    secret = AnsibleUnsafeText('unsafe')
    assert enc.default(secret) == {'__ansible_unsafe': 'unsafe'}

    # Testing for non_vault_object and non_unsafe_object

# Generated at 2022-06-12 23:10:45.295094
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import ImmutableDict
    import datetime
    from ansible.parsing.vault import VaultLib

    d = datetime.date.today()
    if hasattr(d, 'isoformat'):
        d = d.isoformat()

    assert AnsibleJSONEncoder().encode({'a': 'b', 'c': 1}) == '{"c": 1, "a": "b"}'

# Generated at 2022-06-12 23:10:46.597979
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result_vars = AnsibleJSONEncoder().encode({"key": "value"})
    assert result_vars == '{"key": "value"}'



# Generated at 2022-06-12 23:10:58.544491
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    aje = AnsibleJSONEncoder()
    assert aje.default(datetime.date(2018, 5, 3)) == '2018-05-03'
    assert aje.default(datetime.date(2018, 5, 3)) != '2018-05-02'
    assert aje.default(datetime.datetime(2018, 5, 3, 22, 55, 56)) == '2018-05-03T22:55:56'
    assert aje.default(datetime.datetime(2018, 5, 3, 22, 55, 56)) != '2018-05-03T22:55'
    assert aje.default({'key': 'value'}) == {'key': 'value'}
    assert aje.default({'key': 'value'}) != {'key': 'valuE'}

# Generated at 2022-06-12 23:11:04.370928
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafeText

    ansible_encoder = AnsibleJSONEncoder()
    assert ansible_encoder.default(AnsibleUnsafeText('test')) == 'test'

    ansible_encoder_vault_to_text = AnsibleJSONEncoder(vault_to_text=True)
    assert ansible_encoder_vault_to_text.default(AnsibleUnsafeText('test')) == 'test'


# Generated at 2022-06-12 23:11:06.230847
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().encode({'a': 1}) == '{"a": 1}'


# Generated at 2022-06-12 23:11:15.171496
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def isIncorrectType(encoder, o):
        if o == None:
            return False
        else:
            return not isinstance(
                encoder.default(o), type(o)
            )

    encoder = AnsibleJSONEncoder()
    assert not isIncorrectType(encoder, None)
    assert not isIncorrectType(encoder, True)
    assert not isIncorrectType(encoder, -1)
    assert not isIncorrectType(encoder, 1)
    assert not isIncorrectType(encoder, -1.1)
    assert not isIncorrectType(encoder, 1.1)
    assert not isIncorrectType(encoder, 'a')
    assert not isIncorrectType(encoder, u'a')
    assert not isIncorrectType(encoder, [])

# Generated at 2022-06-12 23:11:26.232175
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # create safe and unsafe string
    unsafe_str = to_text(b'\x80abcd', errors='surrogate_or_strict')
    safe_str = to_text(b'\x80abcd', errors='ignore')

    # create custom objects
    class custom():
        pass
    custom.unsafe_str = unsafe_str
    custom.safe_str = safe_str
    custom.unsafe_list = [unsafe_str, safe_str]
    custom.unsafe_set = {unsafe_str, safe_str}

    # create unsafe objects
    class unsafe():
        __UNSAFE__ = True
    unsafe.s = unsafe_str
    unsafe.l = [unsafe_str, safe_str]
    unsafe.t = (unsafe_str, safe_str)
    unsafe.d

# Generated at 2022-06-12 23:11:36.322353
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:11:40.279606
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    my_class = object()
    my_class.__ENCRYPTED__ = False
    my_class.__UNSAFE__ = False
    o = encoder.default(my_class)
    assert isinstance(o, object)


# Generated at 2022-06-12 23:11:42.092585
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    actual_val = encoder.default(1)
    assert actual_val == 1

# Generated at 2022-06-12 23:11:49.085204
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    vault_text = '$ANSIBLE_VAULT;1.1;AES256'
    vault = VaultLib([])
    encrypted_text = vault.encode(vault_text)
    assert encrypted_text.__ENCRYPTED__ is True
    assert encrypted_text.__UNSAFE__ is False

    unsafe_text = 'abc'

    unsafe_proxy = AnsibleUnsafeText(unsafe_text)
    assert unsafe_proxy.__ENCRYPTED__ is False
    assert unsafe_proxy.__UNSAFE__ is True

    # Test for vault text

# Generated at 2022-06-12 23:11:58.885972
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(42) == 42
    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default(True)
    assert AnsibleJSONEncoder().default(False) is False
    assert AnsibleJSONEncoder().default((1, 2, 3)) == [1, 2, 3]
    assert AnsibleJSONEncoder().default({'a': 'b'}) == {'a': 'b'}

    # Vault
    assert AnsibleJSONEncoder().default({'__ansible_vault': b'CiAKbG9naW4K'}) == {'__ansible_vault': b'CiAKbG9naW4K'}

# Generated at 2022-06-12 23:12:11.472636
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class FakeVault:
        def __init__(self, d):
            self.__dict__ = d

        __ENCRYPTED__ = True
        _ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n353132333335363138343066316536383338333264626537343933666337623162313834383262353\n3036663661653235326433663362616662303964346665643539646131643137643964313535333999B\n\n'

# Generated at 2022-06-12 23:12:20.100002
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY3


# Generated at 2022-06-12 23:12:30.469240
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class vault(object):
        '''Instances of vault objects should be jsonized as
        {"__ansible_vault": "AABBcc..."}
        '''
        __ENCRYPTED__ = True
        _ciphertext = "AABBcc..."

    class unsafe(object):
        '''Instances of unsafe objects should be jsonized as
        {"__ansible_unsafe": "yes"}
        '''
        __UNSAFE__ = True
        def __str__(self):
            return "yes"

    class hostvars(object):
        '''Instances of hostvars objects should be jsonized as
        {"value": "yes"}
        '''
        def __init__(self, value):
            self.value = value


# Generated at 2022-06-12 23:12:33.238641
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    a = AnsibleJSONEncoder()
    assert(isinstance(a.default(1), int))
    assert(isinstance(a.default("a"), str))
    assert(isinstance(a.default({'k': 'v'}), dict))
    assert(isinstance(a.default(['k']), list))
    assert(isinstance(a.default(1.0), float))
    assert(isinstance(a.default(True), bool))

# Generated at 2022-06-12 23:12:43.004060
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes

    # AnsibleJSONEncoder returns the input object if it is not Vault or Unsafe type
    assert json.dumps(dict(a=1), cls=AnsibleJSONEncoder) == '{"a": 1}'

    # Vault object gets encoded as dict using __ansible_vault as key
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([1])
    ciphertext = vault.encrypt(to_bytes('abc'))
    assert json.dumps(vault.decrypt(ciphertext), cls=AnsibleJSONEncoder) == '{"__ansible_vault": "%s"}' % ciphertext

    # Unsafe objects gets encoded as dict using __ansible_unsafe as key

# Generated at 2022-06-12 23:12:50.688636
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    # testing for type datetime.date
    test_date = datetime.date(2019, 5, 1)
    expected_date = "2019-05-01"
    assert encoder.default(test_date) == expected_date
    # testing for type datetime.datetime
    test_datetime = datetime.datetime(2019, 5, 1, 18, 27, 59)
    expected_datetime = "2019-05-01T18:27:59"
    assert encoder.default(test_datetime) == expected_datetime



# Generated at 2022-06-12 23:12:52.869594
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    assert ansible_json_encoder.default(1) == 1

# Generated at 2022-06-12 23:12:55.294145
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.dumps(dict(foo='bar', bar='baz'), cls=AnsibleJSONEncoder) == '{"foo": "bar", "bar": "baz"}'

# Generated at 2022-06-12 23:12:59.871081
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    expected = json.dumps({"__ansible_unsafe": "unsafe"}, ensure_ascii=True)
    assert encoder.default({'__ansible_unsafe': "unsafe"}) == expected
    assert encoder.default({"__ansible_unsafe": "unsafe"}) == expected

if __name__ == '__main__':
    test_AnsibleJSONEncoder_default()

# Generated at 2022-06-12 23:13:10.146002
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Test the method default of AnsibleJSONEncoder.
    """
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import binary_type

    data = {'test_data': u'12345',
            'test_binary_data': binary_type(b'binary_data'),
            'test_dict': {'key1': u'value1', 'key2': u'value2'}}

    # Keys are sorted to make comparison easier.
    expected_data = json.dumps(data, sort_keys=True)

    # Test JSON encoding with default settings.
    actual_data = json.dumps(data, sort_keys=True, cls=AnsibleJSONEncoder)
    assert expected_data

# Generated at 2022-06-12 23:13:21.520875
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_json = AnsibleJSONEncoder()
    assert test_json.default("A string") == "A string"

    import ansible.constants
    assert test_json.default(ansible.constants.AnsibleUnsafe("An AnsibleUnsafe object")) == "{'__ansible_unsafe': u'An AnsibleUnsafe object'}"

    import ansible.parsing.vault
    vault_item = ansible.parsing.vault.VaultLib("Some encrypted text")
    assert test_json.default(vault_item) == "{'__ansible_vault': u'$ANSIBLE_VAULT;1.1;AES256'}"

# Generated at 2022-06-12 23:13:31.663671
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test that AnsibleUnsafe objects are not encoded as JSON
    assert json.dumps({"data": AnsibleUnsafe("")}, cls=AnsibleJSONEncoder).count("AnsibleUnsafe") == 0

    # test that AnsibleVault objects are not encoded as JSON
    assert json.dumps({"data": AnsibleVault("")}, cls=AnsibleJSONEncoder).count("ansibleVault") == 0

    # test that AnsibleVaultEncryptedUnicode objects are not encoded as JSON
    assert json.dumps({"data": AnsibleVaultEncryptedUnicode("")}, cls=AnsibleJSONEncoder).count("ansibleVault") == 0

    # test that AnsibleVaultEncryptedUnicode objects are not encoded as JSON

# Generated at 2022-06-12 23:13:37.630599
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_encoder = AnsibleJSONEncoder()
    vault = VaultLib([], None)
    vault_data = vault.encrypt(b'123')
    vault_obj = AnsibleVaultEncryptedUnicode(vault_data)

    result_default = vault_encoder.default(vault_obj)
    result_vault_to_text = vault_encoder.default(vault_obj)
    print(result_default)
    print(result_vault_to_text)


# Generated at 2022-06-12 23:13:45.554356
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # set datetime
    time = datetime.datetime(2018, 1, 1, 12, 34, 56)
    assert encoder.default(time) == '2018-01-01T12:34:56'

    # set hostvars
    hostvars = {'key': 'value'}
    assert encoder.default(hostvars) == hostvars

    # set unsafeobject
    unsafeobject = {'__ansible_unsafe': "<80>"}
    assert encoder.default(unsafeobject) == unsafeobject

# Generated at 2022-06-12 23:13:55.886140
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Vault(str):
        __ENCRYPTED__ = True

    class Unsafe(str):
        __UNSAFE__ = True

    class HostVars(dict):
        pass

    assert AnsibleJSONEncoder().default(Vault('foo')) == {'__ansible_vault': 'foo'}
    assert AnsibleJSONEncoder(vault_to_text=True).default(Vault('foo')) == 'foo'
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(Unsafe('foo')) == 'foo'
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(Unsafe('foo')) == {'__ansible_unsafe': 'foo'}

# Generated at 2022-06-12 23:14:03.738579
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type

    def test_for_encryption(v):
        # Check if the value is encrypted
        try:
            VaultLib.decrypt(v, 'secret')
            return True
        except (ValueError, TypeError):
            return False

    data = [
        {'k_int': 10, 'k_str': '20'},
        'foo',
        10,
        [10, '20'],
        {'k1': [{'k2': 10}] },
        u'bar',
        datetime.datetime.utcnow()
    ]

    # Check if the default method return the dict representation of the object

# Generated at 2022-06-12 23:14:14.353492
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    test method default of class AnsibleJSONEncoder
    """
    # test case 1: o is a mapping(dict), return value
    o = {'test':'test'}
    assert AnsibleJSONEncoder().default(o) == o
    assert AnsibleJSONEncoder(vault_to_text=True).default(o) == o

    # test case 2: o is a datetime.datetime, return value.isoformat
    o = datetime.datetime(2015, 1, 1, 20, 0, 0, 0)
    assert AnsibleJSONEncoder().default(o) == '2015-01-01T20:00:00'
    assert AnsibleJSONEncoder(vault_to_text=True).default(o) == '2015-01-01T20:00:00'

    # test case 3:

# Generated at 2022-06-12 23:14:19.323577
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils._text import to_bytes
    import datetime
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor

    # AnsibleUnsafe
    unsafe_object = to_bytes('unsafe object')
    unsafe_object.__UNSAFE__ = True
    unsafe_object.__ENCRYPTED__ = False
    assert '__ansible_unsafe' in AnsibleJSONEncoder(preprocess_unsafe=False).default(unsafe_object)

    # AnsibleVault

# Generated at 2022-06-12 23:14:29.362355
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    #This is a unit test for the default method of the AnsibleJSONEncoder class
    #This will be needed to verify that any non-serializable python object can
    #be serialized.
    import datetime
    test_serializer = AnsibleJSONEncoder()
    test_unsafe_string = u'This is an unsafe string'
    test_unsafe_object = dict()
    test_unsafe_object['value'] = test_unsafe_string
    test_unsafe_object['__UNSAFE__'] = True
    test_unsafe_object['__ENCRYPTED__'] = False
    test_datetime_object = datetime.date(2020, 3, 26)
    test_unsafe_string_serialized = test_serializer.default(test_unsafe_string)
    test_unsafe_object_

# Generated at 2022-06-12 23:14:32.183587
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    date = datetime.date(2016, 3, 30)
    jsonstring = json.dumps(date, cls=AnsibleJSONEncoder)
    assert jsonstring == "\"2016-03-30\""

# Generated at 2022-06-12 23:14:49.846450
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    with VaultLib() as vault_lib:
        enc = vault_lib.encode('test')
        unsafe_encoder = AnsibleJSONEncoder()
        result = json.loads(json.dumps(enc, cls=unsafe_encoder))

# Generated at 2022-06-12 23:14:51.946568
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    data = dict(foo='bar')
    json.loads(json.dumps(data, cls=AnsibleJSONEncoder))

# Generated at 2022-06-12 23:15:02.022741
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    try:
        import __builtin__
    except ImportError:
        import builtins as __builtin__

    from ansible.parsing.vault import VaultLib

    # Test for string type
    val_str = 'test'
    assert(val_str == __builtin__.str(json.dumps(val_str, cls=AnsibleJSONEncoder)))

    # Test for datetime type
    val_date = datetime.datetime.now()
    assert(val_date.isoformat() == __builtin__.str(json.dumps(val_date, cls=AnsibleJSONEncoder)))

    # Test for sequence type
    val_list = [val_str, val_date, val_str]

# Generated at 2022-06-12 23:15:10.841486
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import os
    os.environ['ANSIBLE_JINJA2_NATIVE'] = "False"
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import range
    from ansible.module_utils.six import string_types
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import binary_type

    def _expected(o, expected):
        if type(o) == binary_type:
            o = to_unicode(o, errors='surrogate_or_strict')

        if is_sequence(expected):
            assert o in expected
        else:
            assert o == expected

    json

# Generated at 2022-06-12 23:15:19.115104
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    encoder = AnsibleJSONEncoder()
    assert encoder.default(AnsibleUnsafeText(u"mytext")) == u"mytext"
    assert encoder.default(u"mytext") == u"mytext"
    assert encoder.default(dict(key=u"value")) == dict(key=u"value")
    assert encoder.default(dict(key=AnsibleUnsafeText(u"value"))) == dict(key=u"value")
    assert encoder.default([1, 2, 3, u"mytext", AnsibleUnsafeText(u"mytext")]) == [1, 2, 3, u"mytext", u"mytext"]

# Generated at 2022-06-12 23:15:29.348180
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Test if AnsibleUnsafe object is encoded to dict
    class MyAnsibleUnsafe(str):
        __UNSAFE__ = True

    ansible_unsafe_obj = MyAnsibleUnsafe('MyAnsibleUnsafe')
    my_json_encoder = AnsibleJSONEncoder()
    assert '{"__ansible_unsafe": "MyAnsibleUnsafe"}' == my_json_encoder.encode(ansible_unsafe_obj)

    # Test if AnsibleVault object is encoded to dict
    class MyAnsibleVault(str):
        __ENCRYPTED__ = True

    ansible_unsafe_obj = MyAnsibleVault('MyAnsibleVault')
    my_json_encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:15:37.866946
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()

    class AnsibleSafe:
        __SAFE__ = True

    class AnsibleUnsafe:
        __UNSAFE__ = True

    class AnsibleVault:
        __ENCRYPTED__ = True

    my_date = datetime.date(2020, 10, 1)
    test_list = [
        'Test string',
        AnsibleSafe(),
        AnsibleUnsafe(),
        AnsibleVault(),
        {'test': 'dict'},
        my_date
    ]

    for test in test_list:
        ansible_json_encoder.default(test)

# Generated at 2022-06-12 23:15:40.666900
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    o = [1, {'a': u'€'}]
    assert json.loads(j.encode(o)) == o



# Generated at 2022-06-12 23:15:48.233564
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    enc = AnsibleJSONEncoder()

    assert enc.default("Hello World") == "Hello World"
    assert enc.default("") == ""
    assert enc.default(" ") == " "
    assert enc.default("\t") == "\t"
    assert enc.default("\n") == "\n"

    assert enc.default(u"Hello World") == "Hello World"
    assert enc.default(u"") == ""
    assert enc.default(u" ") == " "
    assert enc.default(u"\t") == "\t"
    assert enc.default(u"\n") == "\n"

    assert enc.default(True) == True
    assert enc.default(False) == False
    assert enc.default(None) == None


# Generated at 2022-06-12 23:15:58.304451
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test for dict
    class MyDict(dict):
        pass
    myDict = MyDict()
    myDict['key_0'] = 0
    myDict['key_1'] = 'one'
    assert AnsibleJSONEncoder(sort_keys=True).encode(myDict) == \
           '{"key_0": 0, "key_1": "one"}'

    # Test for json.JSONEncoder
    class TestObject(object):
        """ Test object to test default method of AnsibleJSONEncoder class
        """
        def __init__(self, x, y):
            self.x = x
            self.y = y

    testObj = TestObject(1, 2)
    result = AnsibleJSONEncoder(sort_keys=True).default(testObj)

# Generated at 2022-06-12 23:16:15.889431
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('key') == "key"


# Generated at 2022-06-12 23:16:23.436623
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.vault import VaultLib

    from datetime import datetime
    from datetime import date

    from ansible.module_utils.common.text.converters import to_text

    class MyJSONEncoder(json.JSONEncoder):
        def default(self, o):
            return super(MyJSONEncoder, self).default(o)

    # Test Class AnsibleJSONEncoder
    encoder = AnsibleJSONEncoder()
    ansible_json_obj = AnsibleJSONEncoder()
    assert encoder.encode(ansible_json_obj) != json.JSONEncoder().encode(ansible_json_obj)

    # Test Class AnsibleUnsafeText
    ansible_text = to_text

# Generated at 2022-06-12 23:16:32.509928
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # This is a test script for AnsibleJSONEncoder.default

    # import standard libraries
    import unittest
    import json

    # import modules for unit test
    import ansible.module_utils.json_utils as json_utils

    # create class instance of AnsibleJSONEncoder
    class MyAnsibleJSONEncoder(json_utils.AnsibleJSONEncoder):
        def default(self, o):
            return {"MyAnsibleJSONEncoder": "called"}

    my_encoder = MyAnsibleJSONEncoder()

    # prepare for input value
    class DummyClass(dict):
        pass
    dummy = DummyClass()
    dummy['a'] = 1
    dummy['b'] = 2

    # test for AnsibleJSONEncoder.default

# Generated at 2022-06-12 23:16:39.044620
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(u'string') == u'string'
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(42) == 42
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(3.1415926535) == 3.1415926535
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(True) is True
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(False) is False
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(None) is None
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(u'\u1234') == u'\u1234'