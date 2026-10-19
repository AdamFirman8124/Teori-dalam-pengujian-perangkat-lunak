

# Generated at 2022-06-12 23:06:45.842972
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default('str') == 'str'
    assert AnsibleJSONEncoder().default(u'unicode') == u'unicode'
    assert AnsibleJSONEncoder().default(1) == 1
    assert AnsibleJSONEncoder().default({}) == {}
    assert AnsibleJSONEncoder().default([1, 2]) == [1, 2]
    assert AnsibleJSONEncoder().default({'__ansible_vault': 'test'}) == {'__ansible_vault': 'test'}
    assert AnsibleJSONEncoder(vault_to_text=True).default({'__ansible_vault': 'test'}) == 'Vaulted'
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default({'__ansible_unsafe': 'test'}) == 'test'

# Generated at 2022-06-12 23:06:53.257832
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:07:02.986714
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    n1 = AnsibleJSONEncoder(preprocess_unsafe=True)
    n2 = AnsibleJSONEncoder(preprocess_unsafe=False)

    assert '__ansible_vault' in n1.default(dict(__ENCRYPTED__=True, _ciphertext=None))
    assert '__ansible_vault' in n2.default(dict(__ENCRYPTED__=True, _ciphertext=None))
    assert '__ansible_unsafe' in n1.default(dict(__UNSAFE__=True))
    assert '__ansible_unsafe' in n2.default(dict(__UNSAFE__=True))



# Generated at 2022-06-12 23:07:13.160186
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Temp(object):
        def __init__(self):
            pass

    class Temp2(object):
        def __init__(self):
            pass

    o1 = Temp()
    o2 = Temp2()
    s = {'a': o1, 'b': o2}
    o3 = AnsibleJSONEncoder()
    result = o3.default(s)
    assert result == s, 'dictionary default encode error'

    class Temp3(object):
        def __init__(self):
            pass

    o4 = Temp3()
    l = [o4, s]
    o5 = AnsibleJSONEncoder()
    result = o5.default(l)
    assert result == l, 'list default encode error'

    class Temp4(object):
        def __init__(self):
            pass

# Generated at 2022-06-12 23:07:20.328851
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Unit test for the method `default` of class `AnsibleJSONEncoder`"""
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.module_utils.common.collections import ImmutableDict

    # Test default encoder
    assert b'"foo"' == AnsibleJSONEncoder().encode('foo')

    # Test unsafe
    unsafe = AnsibleJSONEncoder().encode(u'foo')
    assert b"{'__ansible_unsafe': 'foo'}" == unsafe

    # Test vault_to_text
    vault_to_text_encoder = AnsibleJSONEncoder(vault_to_text=True)
    o = VaultLib(b'password')
    vault = o.encrypt('foo')

# Generated at 2022-06-12 23:07:31.922882
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    import datetime
    vault = VaultLib([(u'$ANSIBLE_VAULT;1.1;AES256', u'$ANSIBLE_VAR1=pwd1\n$ANSIBLE_VAR2=pwd2\n')])
    vault.read_data('')
    vault.check_password('_n0_Pas5w0rd_')
    vault_dict = vault.dump(obj=vault._obfuscated_data)
    vault_data = vault.decrypt(vault_dict['__ansible_vault'])


# Generated at 2022-06-12 23:07:39.427178
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.constants
    import ansible.module_utils.parsing.vault
    import ansible.module_utils.six
    import ansible.parsing.vault

    assert isinstance(json.JSONEncoder().encode(ansible.module_utils.six.binary_type(b'binary')), ansible.module_utils.six.text_type)
    assert isinstance(json.JSONEncoder().encode(ansible.module_utils.six.text_type(u'text')), ansible.module_utils.six.text_type)

    # ansible.constants.UnsafeText
    unsafe = ansible.constants.UnsafeText(b'\x80')

# Generated at 2022-06-12 23:07:50.471285
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Testing the default behaviour
    input_data = {'allura': [u'Люба'], 'yaml': [u'Любая'], 'user': 'root', 'dict': {'test': '1234'}, 'int': 1}
    output_data = {'allura': [u'Люба'], 'yaml': [u'Любая'], 'user': 'root', 'dict': {'test': '1234'}, 'int': 1}
    # Convert input_data to JSON
    result = json.dumps(input_data, cls=AnsibleJSONEncoder, sort_keys=True, ensure_ascii=False)

# Generated at 2022-06-12 23:07:53.607761
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) is None
    assert AnsibleJSONEncoder().default(True) is True
    assert AnsibleJSONEncoder().default(False) is False



# Generated at 2022-06-12 23:08:02.990274
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafeObject(object):
        pass

    class AnsibleVaultObject(object):
        __ENCRYPTED__ = True

    class AnsibleUnsafeVaultObject(AnsibleUnsafeObject, AnsibleVaultObject):
        pass

    ANSIBLE_UNSAFE_EXPECT = {'__ansible_unsafe': u'~/\u2665'}
    ANSIBLE_VAULT_EXPECT = {'__ansible_vault': u'~/\u2665'}
    ANSIBLE_UNSAFE_VAULT_EXPECT = {'__ansible_unsafe': u'~/\u2665'}


# Generated at 2022-06-12 23:08:17.038672
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.errors import AnsibleError
    import tempfile

    test_s = "hello"
    test_datetime = datetime.datetime.now()
    test_dict = {"hello": "world"}

    # class VaultLib
    test_vault_password_1 = "ansible"
    test_encrypted_text_1 = VaultLib(test_vault_password_1).encrypt(test_s)

    test_vault_password_2 = "world"
    test_encrypted_text_2 = VaultLib(test_vault_password_2).encrypt(test_s)

    # class AnsibleUnsafeText
    test_unsafe_text = AnsibleUnsafe

# Generated at 2022-06-12 23:08:26.142315
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class TestAnsibleUnsafe(unicode):
        def __unicode__(self):
            return u'test'
        def __str__(self):
            return self.__unicode__()
        __UNSAFE__ = True
        __ENCRYPTED__ = False

    class TestAnsibleUnsafeSubclass(TestAnsibleUnsafe):
        pass

    class TestAnsibleVault(str):
        def __str__(self):
            # The vault object has an attribute "vault_id" which would not be returned from the json.dumps() call when
            # using the default encoder, we must therefore not call the super's __str__() function here to ensure we
            # keep the vault's original string representation
            return self
        __ENCRYPTED__ = True

# Generated at 2022-06-12 23:08:31.224934
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class TestAnsible(object):
        def __init__(self, value):
            self.value = value

    class TestAnsibleUnsafe(str):
        __UNSAFE__ = True

    class TestAnsibleVault(str):
        __ENCRYPTED__ = True
        _ciphertext = 'encrypted'

    encoder = AnsibleJSONEncoder()
    assert encoder.default(TestAnsible('test')) == 'test'
    assert encoder.default(TestAnsibleUnsafe('test')) == {'__ansible_unsafe': 'test'}
    assert encoder.default(TestAnsibleVault('test')) == {'__ansible_vault': 'encrypted'}

# Generated at 2022-06-12 23:08:32.888813
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    Data = dict(AnsibleUnsafe = 'AnsibleUnsafe')
    AnsibleJSONEncoder().default(Data)
    assert Data['AnsibleUnsafe'] == 'AnsibleUnsafe'

# Generated at 2022-06-12 23:08:39.091275
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default('somestring') == 'somestring'
    assert encoder.default(set([1, 2, 3])) == [1, 2, 3]
    assert encoder.default(datetime.datetime(2019, 9, 3, 14, 51, 26, 691746)) == '2019-09-03T14:51:26.691746'
    assert encoder.default(datetime.date(2019, 9, 3)) == '2019-09-03'


# Generated at 2022-06-12 23:08:49.330619
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_unsafe = 'ansible_unsafe'
    ansible_vault = 'ansible_vault'
    ansible_mapping = {'key1': 'value1', 'key2': 'value2'}
    ansible_date = datetime.date.today()

    assert AnsibleJSONEncoder().default('ansible') == 'ansible'
    assert AnsibleJSONEncoder(vault_to_text=True).default(ansible_vault) == ansible_vault
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(ansible_vault) == {'__ansible_vault': 'ansible_vault'}

# Generated at 2022-06-12 23:08:53.140256
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_encoder = AnsibleJSONEncoder()
    class TestClass(object):
        def __init__(self, some_required_param, optional_param=None):
            self.some_required_param = some_required_param
            self.optional_param = optional_param

        def __repr__(self):
            return 'TestClass(some_required_param=%r, optional_param=%r)' % (self.some_required_param,
                                                                             self.optional_param)

    assert ansible_encoder.default(TestClass('foo')) == {"optional_param": None, "some_required_param": "foo"}

# Generated at 2022-06-12 23:09:00.956386
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    This test written to test the default method of class AnsibleJSONEncoder().
    For each test case, we are expecting the correct JSON encoding of the object.
    """

    # import here because this module is imported globally in utils/json_encoder.py and would otherwise fail
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY2

    vault_secret = 'dakljflkjdsaf'
    vault_password = 'password'
    unsafe_object = 'foo'
    host_vars = {'foo': 'bar', 'baz': 'qux'}
    date_object = datetime.date(2016, 1, 1)
    default_object = 100

    # create vault object
    vault = VaultLib(vault_password)
    vault_

# Generated at 2022-06-12 23:09:11.940254
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    from ansible.module_utils._text import to_text
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.parsing.vault import VaultLib

    # AnsibleUnsafe
    unsafe_encoder = AnsibleJSONEncoder()
    assert unsafe_encoder.default(to_text('my password', errors='surrogate_or_strict')) == {'__ansible_unsafe': u'my password'}

    # AnsibleVault
    vault = VaultLib([])
    vault.password = 'test'
    ciphertext = vault.encrypt(to_text('test', errors='surrogate_or_strict'))

# Generated at 2022-06-12 23:09:21.804944
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    json_encoder = AnsibleJSONEncoder()

    assert json_encoder.default("a string") == "a string"

    # JSONEncoder.default() can't encode datetime.date()
    dt = datetime.datetime(2013, 11, 13, 12, 45)
    assert json_encoder.default(dt) == dt.isoformat()

    # JSONEncoder.default() can't encode datetime.datetime()
    dt = datetime.date(2013, 11, 13)
    assert json_encoder.default(dt) == dt.isoformat()

    # JSONEncoder.default() can't encode dictionary
    dic = {1: "One", 2: "Two", 3: "Three"}
    assert json_encoder.default(dic) == dic

    # JSONEncoder.default()

# Generated at 2022-06-12 23:09:35.243291
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import json

    # test if default function of parent class is used if object is not of type AnisbleJSONEncoder
    test_dict = {'name': 'test'}
    test_list = ['test']
    test_int = 1
    test_float = 1.11
    json_test_dict = json.dumps(test_dict, cls=AnsibleJSONEncoder)
    json_test_list = json.dumps(test_list, cls=AnsibleJSONEncoder)
    json_test_int = json.dumps(test_int, cls=AnsibleJSONEncoder)
    json_test_float = json.dumps(test_float, cls=AnsibleJSONEncoder)
    assert json_test_dict == '{"name": "test"}'
    assert json_test_list

# Generated at 2022-06-12 23:09:45.626955
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys
    if sys.version_info[0] < 3:
        assert '{0}<type \'ansible.parsing.yaml.objects.AnsibleUnsafeText\'>'.format(u'\x1b[1m\x1b[33m') \
               in AnsibleJSONEncoder(indent=8).default(AnsibleJSONEncoder(indent=8).default(u'\x1b[1m\x1b[33m'))

# Generated at 2022-06-12 23:09:52.492304
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder(sort_keys=True).encode({'a':'b', 'c':'d'}) == '{"a": "b", "c": "d"}'

    assert AnsibleJSONEncoder(sort_keys=True).encode({'a':'b', 'c':'d', 'e': {'f': 'g'}}) == '{"a": "b", "c": "d", "e": {"f": "g"}}'

    from ansible.executor.task_queue_manager import TaskQueueItem
    from ansible.parsing.vault import VaultLib
    vault_password = 'foo'
    vault = VaultLib([(vault_password,)])
    encrypted_value = vault.encrypt('my_secret')

# Generated at 2022-06-12 23:10:01.253645
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class TestClass(object):
        def __json__(self):
            return 'TestClass'

    class TestClassWithoutJson(object):
        pass

    class TestClassDerived(TestClassWithoutJson):
        def __json__(self):
            return 'TestClassDerived'

    assert '"TestClass"' == json.dumps(TestClass(), cls=AnsibleJSONEncoder).strip('"')
    assert '"TestClassDerived"' == json.dumps(TestClassDerived(), cls=AnsibleJSONEncoder).strip('"')


# Generated at 2022-06-12 23:10:10.987951
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # We don't test every possible class here (ex. datetime.date), but
    # we do test some that Ansible uses.  These classes are not expected
    # to be converted to JSON, but rather returned as is.
    assert encoder.default(object) == object
    assert encoder.default(set) == set
    assert encoder.default(dict) == dict
    assert encoder.default(list) == list
    assert encoder.default(set) == set
    assert encoder.default(tuple) == tuple
    assert encoder.default(unicode) == unicode
    assert encoder.default(type(b'')) == type(b'')

    assert encoder.default(set()) == set()
    assert encoder.default(dict()) == dict()
    assert enc

# Generated at 2022-06-12 23:10:12.976693
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class my_class(object):
        def __repr__(self):
            return 'my_class'

    assert AnsibleJSONEncoder().encode(my_class()) == '"my_class"'

# Generated at 2022-06-12 23:10:14.453113
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    j = AnsibleJSONEncoder()
    assert j.default('a') == 'a'


# Generated at 2022-06-12 23:10:25.673895
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword

    vault = VaultLib([VaultSecret(VaultPassword('secret'))])

    # test vault-encrypted value
    assert {'__ansible_vault': vault.encrypt('secret string')} == \
        AnsibleJSONEncoder().default(vault.encrypt('secret string'))

    # test datetime
    dt_value = datetime.datetime.now()
    assert dt_value.isoformat() == AnsibleJSONEncoder().default(dt_value)

    # test date
    date_value = datetime.date.today()

# Generated at 2022-06-12 23:10:27.616076
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    assert encoder.default({'a': 'b'}) == {'a': 'b'}



# Generated at 2022-06-12 23:10:37.349985
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Testing with class AnsibleUnsafe
    s = 'Hello World'
    unsafe_s = AnsibleUnsafe(s)
    assert AnsibleJSONEncoder(preprocess_unsafe=False).default(unsafe_s) == {'__ansible_unsafe': s}
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(unsafe_s) == {'__ansible_unsafe': s}

    # Testing with class AnsibleVault
    ansiblevault_key_string = 'ansible-vault'
    ciphertext_string = 'encrypted data'
    vault_obj = AnsibleVault(ciphertext_string, ansiblevault_key_string)

# Generated at 2022-06-12 23:10:50.670276
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import b, binary_type
    import base64

    ansible_vault_password = 'my_ansible_vault'

    # create an instance of class AnsibleJSONEncoder
    my_encoder = AnsibleJSONEncoder()

    # the input value to be encoded

# Generated at 2022-06-12 23:10:56.034583
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert json.loads(json.dumps({1: 'one'}, cls=AnsibleJSONEncoder)) == {1: 'one'}
    assert json.loads(json.dumps({1: 'one'}, cls=AnsibleJSONEncoder, preprocess_unsafe=True)) == {1: 'one'}
    assert json.loads(json.dumps({1: 'one'}, cls=AnsibleJSONEncoder, preprocess_unsafe=True, vault_to_text=True)) == {1: 'one'}

# Generated at 2022-06-12 23:11:04.113180
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import binary_type
    try:
        from ansible.module_utils.six.moves import __builtin__ as builtins
    except ImportError:
        import __builtin__ as builtins

    # do not print vault passwords in the output
    builtins.__ansible_show_all_vault_output = False


# Generated at 2022-06-12 23:11:13.921631
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import text_type
    from ansible.module_utils.six.moves import cStringIO

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.compat import skippable
    from ansible.errors import AnsibleError
    import os
    import sys

    # This test will pass if your environment use USERPROFILE env variable
    # as your home directory under Windows

    # We do this outside of the function because we want to setup the file
    # if it doesn't exist and we only want to do it once.
    # We also need to use the same

# Generated at 2022-06-12 23:11:18.338367
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    class TestClass:

        def __init__(self):
            self.tes_attr = "Test"

    test_class = TestClass()
    assert ansible_json_encoder.default(test_class) == {"tes_attr": "Test"}

# Generated at 2022-06-12 23:11:28.978822
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.collections import AnsibleMapping
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE, BOOLEANS_TRUE
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafe

    import datetime

    # AnsibleVaultEncryptedUnicode
    ciphertext = "this is a ciphertext"
    vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    vault_default = AnsibleJSONEncoder().default(vault_obj)
    assert(vault_default == {'__ansible_vault': ciphertext})

    # AnsibleUnsafe
    unsafe_obj = AnsibleUnsafe

# Generated at 2022-06-12 23:11:38.455728
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.basic import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib

    vault_password = 'p@ssw0rd'
    data_to_encrypt = 'hello world'

# Generated at 2022-06-12 23:11:46.704556
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # test all the various dict-like roots
    assert encoder.default({'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}
    assert encoder.default(dict(a='b', c='d')) == {'a': 'b', 'c': 'd'}
    assert encoder.default(dict([('a', 'b'), ('c', 'd')])) == {'a': 'b', 'c': 'd'}
    assert encoder.default(dict((('a', 'b'), ('c', 'd')))) == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-12 23:11:54.959560
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Unit test for default method of class AnsibleJSONEncoder
    """
    import ansible.constants as C
    encoder = AnsibleJSONEncoder()
    assert isinstance(encoder.default(1), int)
    assert isinstance(encoder.default("1"), (str, unicode))
    assert isinstance(encoder.default("test"), (str, unicode))
    assert encoder.default("test") == "test"
    assert isinstance(encoder.default(C.IncludeVars("test")), dict)
    assert encoder.default(C.IncludeVars("test")) == {"__ansible_vault": "test"}



# Generated at 2022-06-12 23:12:02.760281
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    value = object()
    v = VaultLib(b'password')
    v_enc = v.encrypt(value)


# Generated at 2022-06-12 23:12:14.893288
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    from ansible.parsing.vault import VaultLib
    from datetime import datetime

    ansible_json_encoder = AnsibleJSONEncoder(preprocess_unsafe=False)

    ansible_unsafe_proxy_instance = AnsibleUnsafe('unsafe text')
    vault_lib_instance = VaultLib(password='password')
    date_instance = datetime(2013, 12, 19, 20, 27, 33, 123456)

    assert ansible_json_encoder.default(ansible_unsafe_proxy_instance) == ansible_unsafe_proxy_instance

# Generated at 2022-06-12 23:12:17.513227
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """
    Unit tests for method default of class AnsibleJSONEncoder

    """

    from ansible.module_utils.basic import AnsibleUnsafe

    obj = AnsibleUnsafe(b'abc')
    encoder = AnsibleJSONEncoder()
    expected_result = {'__ansible_unsafe': 'abc'}
    actual_result = encoder.default(obj)
    assert actual_result == expected_result



# Generated at 2022-06-12 23:12:18.196250
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(None) == None


# Generated at 2022-06-12 23:12:22.307618
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test host variables
    o = {'x':'one', 'y':2}
    value = json.dumps(o, cls=AnsibleJSONEncoder)
    assert value == '{"x": "one", "y": 2}'

    # Test date variable
    o = datetime.date(2019, 2, 3)
    value = json.dumps(o, cls=AnsibleJSONEncoder)
    assert value == '"2019-02-03"'

    # Test Time variable
    o = datetime.time(10, 30, 35, 500)
    value = json.dumps(o, cls=AnsibleJSONEncoder)
    assert value == '"10:30:35.000500"'

    # Test datetime variable

# Generated at 2022-06-12 23:12:28.464194
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import re
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    data = {'result': AnsibleUnsafe("{'key':'value'}")}
    expected = {"result": {"__ansible_unsafe": "{'key':'value'}"}}
    a = AnsibleJSONEncoder()
    assert re.match('^{}$'.format(json.dumps(expected)), a.encode(data))

# Generated at 2022-06-12 23:12:39.030193
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class Test:
        def __init__(self, value, encrypted=False, unsafe=False):
            self._ciphertext = value
            self.__ENCRYPTED__ = encrypted
            self.__UNSAFE__ = unsafe

        def __repr__(self):
            return '%s(%r, %s, %s)' % (self.__class__.__name__, self._ciphertext, self.__ENCRYPTED__, self.__UNSAFE__)

    # type=basestring
    assert json.loads(json.dumps(u'this is a string')) == u'this is a string'
    assert json.loads(json.dumps(u'this is a string', cls=AnsibleJSONEncoder)) == u'this is a string'

    # type=int
   

# Generated at 2022-06-12 23:12:47.084343
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    e = AnsibleJSONEncoder()

    # Class
    assert (e.default(None) == None)
    assert (e.default(1) == 1)
    assert (e.default(True) == True)
    assert (e.default('') == '')

    # List
    d = [1, 2, 3]
    assert (e.default(d) == [1, 2, 3])

    # Dictionary
    d = {'a': 1}
    assert (e.default(d) == {'a': 1})

    # Class
    class Test:
        pass

    t = Test()
    assert (e.default(t) == {})

    # Instance of class
    class Test():
        pass
    t = Test()
    t.a = 1
    t.b = 2

# Generated at 2022-06-12 23:12:56.984450
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # NOTE: vault_to_text is not supported in the new _text module
    # so this test is only testing default behaviors, not vault_to_text = True
    # The vault_to_text = True case more closely mirrors what the deprecation
    # is trying to accomplish.
    from ansible.parsing import vault
    from ansible.module_utils.basic import AnsibleUnsafe


# Generated at 2022-06-12 23:13:03.725432
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    # Initialize test data
    ansible_vault = VaultLib([])

# Generated at 2022-06-12 23:13:08.569697
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Arrange
    encoder = AnsibleJSONEncoder()
    o = datetime.datetime(1970, 1, 1, 0, 0, 0)
    expected = "1970-01-01T00:00:00"

    # Act
    actual = encoder.default(o)

    # Assert
    assert actual == expected

# Generated at 2022-06-12 23:13:21.480016
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.plugins.loader import vault_manager

    enc = AnsibleJSONEncoder()

    # AnsibleUnsafeText
    unsafe = AnsibleUnsafeText(b"unsafe")
    result = enc.default(unsafe)
    assert result == {'__ansible_unsafe': 'unsafe'}

    # vault object
    vault_pass = '$ANSIBLE_VAULT;1.1;AES256\nJooFj27QH1L9X+jRgfRdNQ==\n'
    unsafe = AnsibleUnsafeText(vault_pass)
    result = enc.default(unsafe)

# Generated at 2022-06-12 23:13:23.396404
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(dict(key='value'))['key'] == 'value'


# Generated at 2022-06-12 23:13:33.912009
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    sample_datetime = datetime.datetime(2018, 1, 1, 1, 1)
    v = VaultLib('sample_password')
    sample_text = v.encrypt('sample')
    sample_unsafe = AnsibleUnsafeText('sample')

    assert AnsibleJSONEncoder().default(sample_dict) == sample_dict
    assert AnsibleJSONEncoder().default(sample_datetime) == '2018-01-01T01:01:00'
    assert AnsibleJSONEncoder(vault_to_text=True).default(sample_text) == to_text(sample_text, errors='surrogate_or_strict', nonstring='strict')
   

# Generated at 2022-06-12 23:13:40.037212
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    result = AnsibleJSONEncoder().default("")
    assert result == ""

    result = AnsibleJSONEncoder().default(None)
    assert result == "null"

    # test unwrapped vault

# Generated at 2022-06-12 23:13:52.505252
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_unicode, to_bytes
    import datetime

    def str_class(s):
        class Str(unicode):
            pass
        return Str(s)

    def dict_class(d):
        class Dict(dict):
            pass
        return Dict(d)

    def datetime_class(d):
        class Datetime(datetime.datetime):
            pass
        return Datetime(d)

    # Custom encoder when str_class is given as input
    encoder = AnsibleJSONEncoder()
    assert encoder.default(str_class('simple string')) == 'simple string'

    # Custom encoder when dict_class is given as input
    encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:01.254450
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.urls import AnsibleUnsafe
    # Passing non-dict object
    aje = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert aje.default(AnsibleUnsafe('1')) == {'__ansible_unsafe': '1'}
    # Passing dict object
    aje = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    assert aje.default({AnsibleUnsafe('k'): 1}) == {'k': 1}

    # Passing datetime object
    aje = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    dt = datetime.datetime(2017,3,4)
    assert aje.default

# Generated at 2022-06-12 23:14:10.463437
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Arrange
    # create instance of AnsibleJsonEncoder
    ansible_json_encoder = AnsibleJSONEncoder()

# Generated at 2022-06-12 23:14:14.353795
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # TODO: Add more test cases
    o = {'test_str': 'str'}
    encoder = AnsibleJSONEncoder()
    result = encoder.default(o)
    assert result == o


# Generated at 2022-06-12 23:14:22.865048
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.vault import VaultLib
    import datetime
    # Test AnsibleUnsafe
    ansible_unsafe = AnsibleJSONEncoder().default(to_bytes('asdf'))
    assert ansible_unsafe == {'__ansible_unsafe': u'asdf'}
    # Test hostvars
    hostvars = AnsibleJSONEncoder().default({'test_hostvars': 'test_hostvars'})
    assert hostvars == {'test_hostvars': 'test_hostvars'}
    # Test datetime object
    current_date = datetime.datetime.now()
    json_encoded_current_date = AnsibleJSONEncoder().default(current_date)

# Generated at 2022-06-12 23:14:33.524237
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    import ansible.parsing.unsafe_proxy

    def test_str(str):
        safe_str = ansible.parsing.unsafe_proxy.AnsibleUnsafeText(str)
        vault_str = ansible.parsing.vault.VaultSecret(safe_str)

        assert AnsibleJSONEncoder(vault_to_text=False).encode(safe_str) == json.dumps(safe_str, ensure_ascii=False)
        assert AnsibleJSONEncoder(vault_to_text=False).encode(vault_str) == json.dumps({'__ansible_vault': safe_str}, ensure_ascii=False)
        assert AnsibleJSONEncoder(vault_to_text=True).en

# Generated at 2022-06-12 23:14:56.353119
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # case for __ENCRYPTED__ = True
    encoder = AnsibleJSONEncoder()
    encrypted = vault.AnsibleVaultEncryptedUnicode('something')
    assert encoder.default(encrypted) == "{'__ansible_vault': u'something'}"

    # case for __UNSAFE__ = True
    encoder = AnsibleJSONEncoder()
    unsafe = vault.AnsibleUnsafeText('something')
    assert encoder.default(unsafe) == "{'__ansible_unsafe': u'something'}"

    # case for datetime.date
    encoder = AnsibleJSONEncoder()
    date = datetime

# Generated at 2022-06-12 23:15:05.489746
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test of method default of class AnsibleJSONEncoder
    # Test of case 1, if getattr(o, '__ENCRYPTED__', False) is True, return the value
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True)
    assert "123" == encoder.default(to_text('123'))

    # Test of case 2, if getattr(o, '__UNSAFE__', False) is True, return the value
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True)
    assert {'__ansible_unsafe': '123'} == encoder.default(to_text('123'))

    # Test of case 3, if isinstance(o, Mapping) is True, return the value


# Generated at 2022-06-12 23:15:09.134300
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_unix_epoch = datetime.datetime(1970, 1, 1, 0, 0, 0)
    assert json.loads(json.dumps(ansible_unix_epoch, cls=AnsibleJSONEncoder)) == '1970-01-01T00:00:00'



# Generated at 2022-06-12 23:15:17.444190
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class AnsibleUnsafe:
        __UNSAFE__ = True

    class VaultUnsafe:
        __ENCRYPTED__ = True

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    class CustomObject:
        def __init__(self, cmd):
            self.cmd = cmd

        def __repr__(self):
            return repr(self.cmd)

    ansible_unsafe = AnsibleUnsafe()
    ansible_uns

# Generated at 2022-06-12 23:15:26.483764
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    test_data = [  # Input, Expected output
        (dict(), dict()),
        ([], []),
        (dict(foo='bar'), dict(foo='bar')),
        (dict(foo='bar', baz=dict(boo=['list1', 'list2', 'list3'])), dict(foo='bar', baz=dict(boo=['list1', 'list2', 'list3']))),
        (dict(foo='bar', baz=dict(boo='list2')), dict(foo='bar', baz=dict(boo='list2'))),
    ]
    for item in test_data:
        encoder = AnsibleJSONEncoder()
        result = encoder.default(item[0])
        assert result == item[1]

# Generated at 2022-06-12 23:15:37.115697
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test function for method default of class AnsibleJSONEncoder"""
    import sys
    import datetime

    def test_data_item(item, expected_result, func_name):
        # apply the test only if the item is not of type AnsibleJSONEncoder
        if not isinstance(item, AnsibleJSONEncoder):
            # get the result
            result = func_name(item)
            # display the test result
            print("Item=%s, Type=%s, Expected=%s, Result=%s, Test %s" % (
            item, type(item), expected_result, result, ("PASSED" if result == expected_result else "FAILED")))
        # end of if

    # end of def test_data_item()

    # define the class to test
    test_class = AnsibleJSONEncoder

# Generated at 2022-06-12 23:15:46.020136
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    plaintext = u"test"
    ciphertext = vault.encrypt(plaintext)
    ansible_unsafe = "AnsibleUnsafe"
    ansible_unsafe_text = AnsibleUnsafeText(ansible_unsafe)
    ansible_unsafe_binary = AnsibleUnsafe(ansible_unsafe.encode('utf-8'), convert_to=bytes)
    ansible_unsafe_bytes = AnsibleUnsafe(ansible_unsafe_binary)

# Generated at 2022-06-12 23:15:56.173826
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unanswered import Unanswered
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    class Unsafe(str):
        __UNSAFE__ = True

    class Safe(str):
        pass

    def _assert_encoding(obj, expect):
        ansible_json = AnsibleJSONEncoder().encode(obj)
        assert ansible_json == expect, '%s encoding failed. Should be %s, instead it is %s' % (obj.__class__.__name__, expect, ansible_json,)

    _assert_encoding({'1':'a','2':'b'}, '{"1": "a", "2": "b"}')

# Generated at 2022-06-12 23:16:05.132595
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    json_encoder = AnsibleJSONEncoder()


# Generated at 2022-06-12 23:16:08.517176
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert(json.loads(
        json.dumps(
            {'my_date': datetime.datetime(2019, 1, 1, 0, 0)},
            cls=AnsibleJSONEncoder
        )
    )['my_date'] == '2019-01-01T00:00:00')