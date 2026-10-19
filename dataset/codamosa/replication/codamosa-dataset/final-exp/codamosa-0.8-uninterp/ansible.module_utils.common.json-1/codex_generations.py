

# Generated at 2022-06-12 23:06:47.358507
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    vault_text = to_text(b'$ANSIBLE_VAULT;1.1;AES256\n36336166633539366631313666626032383165383433616533363265353332616562656537613230\n6230663739396361346539623238616333633530313863323863323333376331666630383231633\n373265626461623763343134343631633462626164363035616663656632386662663839666130\n39346566\n')

    import ansible.constants

# Generated at 2022-06-12 23:06:58.112126
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault

    ans = AnsibleJSONEncoder()

    o = {'foo': 'bar'}
    assert json.loads(json.dumps(o, cls=ans)) == o

    o = {'foo': vault.VaultLib('dummy')}
    assert json.loads(json.dumps(o, cls=ans, vault_to_text=True)) == {'foo': '$ANSIBLE_VAULT;1.1;AES256;dummy'}

    from ansible.parsing.vault import VaultSecret
    o = {'foo': VaultSecret('bar')}
    assert json.loads(json.dumps(o, cls=ans, vault_to_text=True)) == {'foo': 'bar'}


# Generated at 2022-06-12 23:07:04.574471
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    assert AnsibleJSONEncoder().default(b'string') == 'string'
    assert AnsibleJSONEncoder().default(42) == 42
    assert AnsibleJSONEncoder().default(42.0) == 42.0
    assert AnsibleJSONEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert AnsibleJSONEncoder().default({'one': 1, 'two': 2}) == {'one': 1, 'two': 2}
    assert AnsibleJSONEncoder().default({'__ansible_unsafe': 'unsafe', '__ansible_vault': 'vault'}) == \
        {'__ansible_unsafe': 'unsafe', '__ansible_vault': 'vault'}


# Generated at 2022-06-12 23:07:14.697004
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Test method default of class AnsibleJSONEncoder"""
    # NOTE: always inform AWS/Tower when new items get added
    class FakeHost(object):
        def __init__(self, hostvars):
            self.hostvars = hostvars

    class FakeHostvars(object):
        def __init__(self, hostname):
            self.hostname = 'host1.example.com'
            self.ansible_python_interpreter = '/usr/bin/python'

    class FakeVault(object):
        __ENCRYPTED__ = True
        _ciphertext = b'{"key": "value"}'

    class FakeUnsafe(object):
        __UNSAFE__ = True

    obj = AnsibleJSONEncoder()
    assert obj.default(1) == 1
    assert obj.default

# Generated at 2022-06-12 23:07:21.401242
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # default behavior
    assert '{"key": "val"}' == json.dumps({'key': 'val'}, cls=AnsibleJSONEncoder)

    # unsafe
    unsafe = AnsibleUnsafeText(to_text(u'unsafe'))
    assert '{"__ansible_unsafe": "unsafe"}' == json.dumps(unsafe, cls=AnsibleJSONEncoder)

    # vault
    vault = AnsibleVaultEncryptedUnicode(to_text(u'vault'))
    assert '{"__ansible_vault": "vault"}' == json.dumps(vault, cls=AnsibleJSONEncoder)

    # date
    now = datetime.datetime.now()

# Generated at 2022-06-12 23:07:32.683071
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    # use vault lib to create an encrypted object
    v = VaultLib([])
    enc = v.dump('mypassword', 'mysecret')

    # instantiate an AnsibleJSONEncoder
    e = AnsibleJSONEncoder()
    # assert result for encrypted object is of the form {'__ansible_vault': '<mysecret>'}

# Generated at 2022-06-12 23:07:39.391323
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test for Vault object
    from ansible.parsing.vault import VaultLib
    vault_content = b'Vault test: AnsibleJSONEncoder_default'
    encrypter = VaultLib([b'secret'])
    ciphertext = encrypter.encrypt(vault_content)
    aje = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False, sort_keys=False, indent=None)
    _result = aje.default(ciphertext)
    assert _result['__ansible_vault'] == to_text(ciphertext._ciphertext)

    # test for SafeText object
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    safe_text = AnsibleUnsafeText(vault_content)
    _result = a

# Generated at 2022-06-12 23:07:45.789823
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    x = AnsibleJSONEncoder()
    # test vault object
    o = {"__ENCRYPTED__": True, "__ANSIBLE_VAULT": "42"}
    assert x.default(o) == {'__ansible_vault': 'NDI='}
    # test unsafe object
    o = {"__UNSAFE__": True, "__ANSIBLE_VAULT": "unsafe_string"}
    assert x.default(o) == {'__ansible_unsafe': 'unsafe_string'}
    # test normal object
    o = {"key1": "value1", "key2": "value2"}
    assert x.default(o) == {"key1": "value1", "key2": "value2"}
    # test date object

# Generated at 2022-06-12 23:07:53.207018
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault

    encoder = AnsibleJSONEncoder()
    print(encoder.encode(dict(
        date=datetime.date(2001, 2, 3),
        datetime=datetime.datetime(2001, 2, 3, 4, 5, 6, 7),
        unsafe=vault.AnsibleUnsafeText(b'foo'),
        vault=vault.VaultLib(['mypassword']).encode('bar'))))



# Generated at 2022-06-12 23:08:02.740582
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def assert_expected_result(o, expected_result):
        ansible_json_encoder = AnsibleJSONEncoder()
        result = ansible_json_encoder.default(o)
        assert result == expected_result

    # DateTime objects handled by AnsibleJSONEncoder
    # 2019-01-01T00:00:00
    assert_expected_result(datetime.datetime(2019, 1, 1), '2019-01-01T00:00:00')
    # 2019-01-01
    assert_expected_result(datetime.date(2019, 1, 1), '2019-01-01')

    # Other objects handled by AnsibleJSONEncoder
    # {'key1':'value1'}

# Generated at 2022-06-12 23:08:19.225673
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils import basic

    plaintext = b'plaintext'
    password = b'password'
    ciphertext = VaultLib(password).encrypt(plaintext)
    unsafe = basic.AnsibleUnsafe(b'unsafe')

    vault_obj = basic.AnsibleVaultEncryptedUnicode(ciphertext)
    unsafe_obj = basic.AnsibleUnsafeText(plaintext)

    # check that AnsibleVaultEncryptedUnicode is converted to dict
    assert b'"__ansible_vault":' in AnsibleJSONEncoder().encode(vault_obj)
    assert b'"__ansible_unsafe":' in AnsibleJSONEncoder().encode(unsafe_obj)
    assert AnsibleJSONEncoder

# Generated at 2022-06-12 23:08:25.089439
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    v = AnsibleJSONEncoder()
    assert v.default("Hello") == "Hello"
    assert v.default("Hello") != "there"
    class SampleClass():
        def __init__(self):
            self.__UNSAFE__ = True
    sample_object = SampleClass()
    assert v.default(sample_object) == {'__ansible_unsafe': 'Hello'}
    assert v.default(sample_object) != {'__ansible_unsafe': 'there'}



# Generated at 2022-06-12 23:08:34.860569
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    unsafe = ansible.module_utils.basic._AnsibleUnsafe('unsafe')
    assert AnsibleJSONEncoder().default(unsafe) == 'unsafe'
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(unsafe) == {'__ansible_unsafe': 'unsafe'}

    vault = ansible.parsing.vault.VaultLib('myvault')
    assert AnsibleJSONEncoder().default(vault) == {'__ansible_vault': ''}
    assert AnsibleJSONEncoder(preprocess_unsafe=True).default(vault) == {'__ansible_vault': ''}
    assert AnsibleJSONEncoder().default(vault) == {'__ansible_vault': ''}

# Generated at 2022-06-12 23:08:44.626251
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Note: for vaulted strings, __ansible_vault should be consistent with the
    # "rekey" command of ansible-vault
    # Note: for unsafe strings, __ansible_unsafe should be consistent with the
    # "rekey" command of ansible-vault

    import os
    import tempfile

    from ansible.module_utils.common.collections import AnsibleVaultError

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 4

    # Prepare a temporary file for testing.
    tmp_file_fd, tmp_file_path = tempfile.mkstem

# Generated at 2022-06-12 23:08:55.097480
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultEditor
    from ansible.module_utils.six import u, b

    vault_pass = 'secret'
    plain_text = u'plain_text', 'utf-8'
    vault_text = u'vault_text', 'utf-8'
    encoded_text = b'encoded_text', 'utf-8'
    json_unsafe_string = VaultEditor.encrypt(vault_pass, plain_text[0]).encode('utf-8'), 'utf-8'
    json_safe_string = VaultEditor.encrypt(vault_pass, vault_text[0]).encode('utf-8'), 'utf-8'
    json_safe_bytes = VaultEditor.encrypt(vault_pass, encoded_text[0]), 'utf-8'

    json

# Generated at 2022-06-12 23:09:03.553448
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    # Dummy classes for unit testing
    class DummyObj(object):
        def __init__(self, val):
            self.val = val

    class DummyObj2(object):
        def __init__(self, val):
            self.val = val

    # Dummy hostvars
    dummy_hostvars = {
        'host1': {
            'var1': 'value1',
            'var2': 'value2'
        },
        'host2': {
            'var1': 'value1',
            'var2': 'value2'
        }
    }

    # Date data
    dummy_date = datetime.datetime(year=2020, month=12, day=1)

    # Test data structure

# Generated at 2022-06-12 23:09:06.985747
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder = AnsibleJSONEncoder()
    o = {'a': 'b'}
    assert ansible_json_encoder.default(o) == o


# Generated at 2022-06-12 23:09:17.764028
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    from ansible.module_utils.six import BytesIO
    import sys

    from ansible.parsing.vault import VaultLib

    key = u'1234567890123456789012345678901234567890123456789012345678901234'
    vault = VaultLib([])
    vault.PROTOCOL_VERSION = 1
    secret = vault.encrypt(key, u'foo')
    value = AnsibleJSONEncoder().default(secret)
    assert isinstance(value, dict)
    assert u'__ansible_vault' in value

    secret = vault.encrypt(key, u'bar')
    value = AnsibleJSONEncoder(vault_to_text=True).default(secret)
    assert isinstance(value, unicode)
    assert value == u

# Generated at 2022-06-12 23:09:24.774364
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test __ENCRYPTED__
    from ansible.parsing.vault import VaultEditor
    ve = VaultEditor('password')
    value = ve.encrypt('string')
    assert isinstance(value, str)
    assert getattr(value, '__ENCRYPTED__', False)

# Generated at 2022-06-12 23:09:34.772345
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import sys

    # create an instance of the JSONEncoder class
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=True)

    # test data: dictionary
    input_dict = {'site': 'xyz.com', 'user': 'admin', 'pass': 'redhat'}

    # create a string containing the JSON representation of the dict
    json_string = encoder.encode(input_dict)
    print("Encoded dict: " + json_string)

    # create a dict from JSON string
    output_dict = json.loads(json_string)
    print("Decoded dict: " + str(output_dict))

    # print dict
    print("Dictionary is: " + str(output_dict))

    # test data: date object

# Generated at 2022-06-12 23:09:49.266750
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # Test with vault object
    vault_str = "@EANSIBLE_VAULT;1.1;AES256;test\n376531613361343132343331393432313233316333373564613063323334323236303366643430\n636331383330396430653864396539316238623935653835333066326565386432663466626434\n3933366630616338616630633635363262356636626633616134353034353061\n"
    vault_str = '\n'.join(vault_str.split('\n')[2:])
    vault_obj = {'__ansible_vault': vault_str}
    ansible_json_encoder = AnsibleJSONEncoder()
    val

# Generated at 2022-06-12 23:09:53.149019
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    result = AnsibleJSONEncoder().default({})
    assert result == {}

    from ansible.module_utils.six import text_type
    result = AnsibleJSONEncoder().default({'a': text_type('My string'), })
    assert result == {'a': 'My string'}


# Generated at 2022-06-12 23:10:01.986773
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    a_jenc = AnsibleJSONEncoder()
    assert a_jenc.default(None) == 'null'
    assert a_jenc.default(1) == 1
    assert a_jenc.default('test') == 'test'
    assert a_jenc.default(True) == True
    assert a_jenc.default(False) == False

    a_jenc = AnsibleJSONEncoder(vault_to_text=True)
    vault_text = VaultLib([[VaultSecret('test')]])
    assert a_

# Generated at 2022-06-12 23:10:11.609619
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common.encoding import to_text
    from ansible.module_utils.common.collections import to_unicode
    from ansible.parsing.vault import VaultLib

    # json.JSONEncoder.default
    def default(o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super(AnsibleJSONEncoder, default).default(o)

    # json.JSONEncoder.encode
    def encode(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return '"%s"' % o.isoformat()
        return super(AnsibleJSONEncoder, self).encode(o)

    # json.JSONEncoder.it

# Generated at 2022-06-12 23:10:22.029242
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import unittest
    import datetime
    from itertools import imap

    class dummy(object):
        def __init__(self, value):
            self.value = value

    class dummy2(unicode):
        pass

    class DummyEncoder(json.JSONEncoder):
        """A custom json.JSONEncoder that knows how to encode dummy objects."""

        def encode(self, o):
            return list(self.iterencode(o))

        def iterencode(self, o, _one_shot=False):
            if isinstance(o, dummy):
                yield '<dummy>'
            else:
                for chunk in super(DummyEncoder, self).iterencode(o, _one_shot=_one_shot):
                    yield chunk

    encoder = DummyEncoder()


# Generated at 2022-06-12 23:10:30.576528
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    d = AnsibleJSONEncoder()

    from ansible.parsing.vault import VaultLib
    vault_password = 'mypassword'
    v = VaultLib(vault_password)
    encrypted_text = v.encrypt('test string to encrypt')
    li_unsafe = u'test list \u2019\u2018'
    li_safe = u'does not contain \u2019\u2018'
    li_enc = u'list contains an encrypted item'

    # Test the default case
    assert d.default(None) is None
    assert d.default(False) is False
    assert d.default(True) is True
    assert d.default(1) == 1

    # Test with an encrypted item

# Generated at 2022-06-12 23:10:39.849697
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    def test_unsafe_class(value):
        value = to_text(value, errors='surrogate_or_strict', nonstring='strict')
        return type(value.encode('utf-8'), (value.encode('utf-8'),), dict(__UNSAFE__=True))

    # Check handling of AnsibleUnsafe objects
    unsafe_object_value = "unsafe_object_value"
    unsafe_object = test_unsafe_class(unsafe_object_value)
    assert isinstance(unsafe_object, type(unsafe_object_value))

    json_obj = json.loads(json.dumps(unsafe_object, cls=AnsibleJSONEncoder))
    assert json_obj == {'__ansible_unsafe': unsafe_object_value}

    # Check handling of non

# Generated at 2022-06-12 23:10:49.183267
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY3
    vault_secret = 'Abc1234'
    vault_data = 'ansible'
    vault_pw_path = '/tmp/vault_pw'
    vault = VaultLib(vault_secret)
    encrypted_data = vault.encrypt(vault_data)
    if PY3:
        encrypted_data = encrypted_data.encode('utf-8')

    encoder = AnsibleJSONEncoder()
    encoded_data = encoder.default(encrypted_data)
    dict_data = dict(__ansible_vault=encrypted_data)
    assert encoded_data == dict_data

# Generated at 2022-06-12 23:10:56.631553
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib

    pass_text = u"p@ssw0rd"
    vault_text = VaultLib().encrypt(pass_text)

    # Test vault object
    encoder = AnsibleJSONEncoder()
    res1 = encoder.default(vault_text)
    assert res1 == {'__ansible_vault': to_text(vault_text._ciphertext, nonstring='strict')}
    res2 = encoder.default(vault_text)
    assert res2 == {'__ansible_vault': to_text(vault_text._ciphertext, nonstring='strict')}

    # Test unsafe object
    encoder = AnsibleJSONEncoder()
    res1 = encoder.default(pass_text)

# Generated at 2022-06-12 23:11:04.540413
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    #test default handling of AnsibleVaultEncryptedUnicode
    test_json_vault_string_object = '{"__ansible_vault": "blah"}'

# Generated at 2022-06-12 23:11:19.769887
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    aje = AnsibleJSONEncoder()

    # test for vault object
    ciphertext = VaultSecret(VaultLib.encrypt('test', 'test'))._ciphertext
    assert aje.default(VaultSecret(ciphertext=ciphertext)) == {'__ansible_vault': ciphertext}

    # test for vault object with vault_to_text=True
    ciphertext = VaultSecret(VaultLib.encrypt('test', 'test'))._ciphertext
    assert aje.default(VaultSecret(ciphertext=ciphertext, vault_to_text=True)) == ciphertext

    # test for unsafe_text

# Generated at 2022-06-12 23:11:24.813407
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    d = {
        'a': AnsibleUnsafe("<Markdown>"),
        'b': AnsibleVaultEncryptedUnicode("hello"),
        }
    if AnsibleJSONEncoder().default(d['a']) == {'__ansible_unsafe': '<Markdown>'}:
        return True


# Generated at 2022-06-12 23:11:35.158861
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping, OrderedDict
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.parsing.vault import VaultLib

    key = 'ansible'
    plaintext = 'ansible'

# Generated at 2022-06-12 23:11:42.952209
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault as vault
    ansible_obj = vault.VaultLib(b"vaultpassword")
    ansible_obj.decrypt(b'$ANSIBLE_VAULT;1.1;AES256\n39306563366231643266313138643662376564356632653431653336623661363562666339323738\n30333734373639343863306563616236306439353334386665653766396439653033656632313861\n3430363163323531653264383231396431343361306637643134353638326437353861\n')

# Generated at 2022-06-12 23:11:49.680675
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence, Sequence
    from ansible.module_utils.six import StringIO
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes, to_text, to_native
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.module_utils.common.text.converters import to_bytes as to_text_to_bytes

    def __AnsibleUnsafe(obj):
        if isinstance(obj, str):
            obj = to_unicode(obj)

# Generated at 2022-06-12 23:11:59.431117
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class TestClass:
        pass

    # test case when o is an object
    o = TestClass()
    assert AnsibleJSONEncoder().default(o) == TestClass.__dict__

    # test case when o is a string
    o = "foo"
    assert AnsibleJSONEncoder().default(o) == "foo"

    # test case when o is a list
    o = ["foo", "bar"]
    assert AnsibleJSONEncoder().default(o) == ["foo", "bar"]

    # test case when o is a dict
    o = {"name", "foo", "age", 18}
    assert AnsibleJSONEncoder().default(o) == {"name", "foo", "age", 18}

    # test case when o is a date
    from datetime import date
    o = date(2018, 8, 8)


# Generated at 2022-06-12 23:12:04.063606
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    obj = AnsibleJSONEncoder()
    assert obj.default(datetime.datetime.now()) is not None
    assert obj.default(None) is None
    assert obj.default('test') == 'test'


# Generated at 2022-06-12 23:12:11.877819
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    def compare(a, b):
        if isinstance(a, list) and isinstance(b, list):
            assert len(a) == len(b)
            for x, y in zip(a, b):
                compare(x, y)
        elif isinstance(a, dict) and isinstance(b, dict):
            assert len(a) == len(b)
            for x, y in a.items():
                equate(y, b[x])
        else:
            assert a == b

    def equate(a,b):
        if isinstance(a, list) and isinstance(b, list):
            assert len(a) == len(b)
            for x, y in zip(a, b):
                equate(x, y)

# Generated at 2022-06-12 23:12:20.396550
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # test with o.__ENCRYPTED__ = False
    o = 'Nothing to see here'
    assert o == AnsibleJSONEncoder().default(o)

    # test with o.__ENCRYPTED__ = True and vault_to_text = True
    o = 'Nothing to see here'
    o.__ENCRYPTED__ = True
    assert 'Nothing to see here' == AnsibleJSONEncoder(vault_to_text=True).default(o)

    # test with o.__ENCRYPTED__ = True and vault_to_text = False
    o = 'Nothing to see here'
    o.__ENCRYPTED__ = True

# Generated at 2022-06-12 23:12:30.815851
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import base64
    from ansible.module_utils.six import binary_type

    class NotCustom(object):
        def __repr__(self):
            return 'NotCustom'
    not_custom = NotCustom()

    class Custom(object):
        def __repr__(self):
            return 'Custom'
    custom = Custom()
    custom.__ENCRYPTED__ = True
    custom._ciphertext = binary_type(base64.b64encode('This is not a real encrypted value!'))

    assert json.dumps(not_custom) == AnsibleJSONEncoder().default(not_custom)
    assert json.dumps(custom) == AnsibleJSONEncoder().default(custom)

# Generated at 2022-06-12 23:12:52.457010
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    enc = AnsibleJSONEncoder()
    assert enc.default(mock_class_unsafe()) == 'test_ansible_unsafe'
    assert enc.default(mock_class_encrypted()) == {'__ansible_vault': 'ansible_encrypted_data'}
    assert enc.default(datetime.datetime(2000, 1, 1, 1, 1, 1)) == '2000-01-01T01:01:01'
    assert enc.default(datetime.date(2000, 1, 1)) == '2000-01-01'
    assert enc.default(mock_class_normal()) == 'class_normal_text'
    assert enc.default(mock_class_dict()) == {'dict_key': 'dict_value'}


# Generated at 2022-06-12 23:13:00.723468
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import datetime
    test_dict = {"foo": "bar", "baz": "boz"}
    result = AnsibleJSONEncoder().encode(test_dict)
    assert result == json.dumps(test_dict)

    # test the datetime
    test_dict = {"foo": "bar", "baz": "boz", "time": datetime.datetime.now()}
    result = AnsibleJSONEncoder().encode(test_dict)
    assert result == json.dumps(test_dict)

    # test the date
    test_dict = {"foo": "bar", "baz": "boz", "time": datetime.date.today()}
    result = AnsibleJSONEncoder().encode(test_dict)
    assert result == json.dumps(test_dict)

    # test the dict

# Generated at 2022-06-12 23:13:10.347126
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    r'''
    >>> import json
    >>> from ansible.parsing.ajson import AnsibleJSONEncoder
    >>> class Encrypt(str):
    ...     __ENCRYPTED__ = True
    >>> class Unsafe(str):
    ...     __UNSAFE__ = True
    >>> json.dumps({'vault': Encrypt('hello'), 'unsafe': Unsafe('world'), 'date': datetime.date(2019, 10, 7)}, cls=AnsibleJSONEncoder)
    '{"date": "2019-10-07", "unsafe": "world", "vault": {"__ansible_vault": "AQEBAQFoaGVsbG8="}}'
    '''
    pass


# Generated at 2022-06-12 23:13:12.420699
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """This method is the unit test for default method of class AnsibleJSONEncoder"""
    assert AnsibleJSONEncoder().default('a') == 'a'

# Generated at 2022-06-12 23:13:18.772176
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class SimpleClass(object):
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return 'SimpleClass(value={0.value!r})'.format(self)

    encoder = AnsibleJSONEncoder()
    assert encoder.default(SimpleClass(42)) == 'SimpleClass(value=42)'
    assert encoder.default(SimpleClass('a')) == 'SimpleClass(value=\'a\')'
    assert encoder.default(['a', SimpleClass('b'), 1]) == ['a', 'SimpleClass(value=\'b\')', 1]


# Generated at 2022-06-12 23:13:28.284545
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    e = AnsibleJSONEncoder(preprocess_unsafe=False, vault_to_text=False)
    ansible_unsafe = "{'a': 'b'}"
    assert e.default(ansible_unsafe) == "{'a': 'b'}"
    ansible_vault = "{'a': 'b'}"
    assert e.default(ansible_vault) == "{'__ansible_vault': '{'a': 'b'}'}"
    ansible_vault_text = "{'a': 'b'}"
    assert e.default(ansible_vault_text) == "{'a': 'b'}"



# Generated at 2022-06-12 23:13:35.770693
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import ansible.parsing.vault
    the_vault_password = 'ansible'
    vault = ansible.parsing.vault.VaultLib(the_vault_password)
    ciphertext = vault.encrypt('the_secret')
    data = [
        'a',
        ['b', 'c'],
        {'d': 'e', 'f': {'g': 'h'}},
        ciphertext,
        to_text(ciphertext),
    ]
    actual = json.dumps(data, cls=AnsibleJSONEncoder, preprocess_unsafe=True, vault_to_text=True)

# Generated at 2022-06-12 23:13:43.627546
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # 'o' is a dictionary
    o = {'foo': 'bar'}
    # Test should pass even if parameter 'o' is altered
    d = AnsibleJSONEncoder().default(o)
    assert d == o
    assert d['foo'] == 'bar'
    assert id(d) != id(o)

    # 'o' is an instance of AnsibleUnsafe class
    from ansible.parsing.vault import VaultLib
    vault_secret = 'MySecret'
    vault_password = 'MyPassword'
    vault_secret_obj = VaultLib.encrypt(vault_secret, vault_password)
    assert isinstance(vault_secret_obj, VaultLib)
    o = vault_secret_obj
    d = AnsibleJSONEncoder().default(o)
    assert isinstance(d, dict)

# Generated at 2022-06-12 23:13:53.869011
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    ansible_json_encoder_instance = AnsibleJSONEncoder(
        sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=True)
    assert ansible_json_encoder_instance.default(None) is None
    assert ansible_json_encoder_instance.default(False) is False
    assert ansible_json_encoder_instance.default(True) is True
    assert ansible_json_encoder_instance.default(0) == 0
    assert ansible_json_encoder_instance.default(1) == 1
    assert ansible_json_encoder_instance.default(datetime.datetime.now()) == datetime.datetime.now().isoformat()



# Generated at 2022-06-12 23:13:57.382667
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    class TestClass:
        pass

    my_dict = {
        'hostname': 'host1',
        'ip': '192.168.0.1',
        'object': TestClass,
    }

    json_data = AnsibleJSONEncoder().encode(my_dict)
    assert '192.168.0.1' in json_data
    assert 'object' in json_data
    assert 'TestClass' in json_data
    assert '__ansible_vault' not in json_data
    assert '__ansible_unsafe' not in json_data

# Generated at 2022-06-12 23:14:31.353660
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    # Test encrypted object
    ansible_vault_obj = type('AnsibleVault', (object, ), dict(__ENCRYPTED__=True, _ciphertext=u'$ANSIBLE_VAULT;1234;AES256;jdoe;ansible_vault_test'))
    ansible_vault_o = ansible_vault_obj()
    assert encoder.default(ansible_vault_o) == {'__ansible_vault': u'$ANSIBLE_VAULT;1234;AES256;jdoe;ansible_vault_test'}

    ansible_vault_o = ansible_vault_obj()
    assert encoder._preprocess_unsafe

# Generated at 2022-06-12 23:14:38.860097
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():

    class Test:
        def __init__(self):
            self.a = 'test'
            self.b = 'test'

    class Test2:
        def __init__(self):
            self.a = 'test2'

    class Test3:
        def __init__(self):
            self.a = 'test3'

        def __eq__(self, other):
            return True

    class Test4(object):
        def __init__(self):
            self.a = 'test4'
            self.__UNSAFE__ = True

    class Test5(object):
        def __init__(self):
            self.a = 'test5'
            self.__UNSAFE__ = True
            self.__ENCRYPTED__ = True


# Generated at 2022-06-12 23:14:48.722689
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    # 1. Test the case when o has __ENCRYPTED__ attribute
    class Vault:
        def __init__(self, _ciphertext):
            self._ciphertext = _ciphertext
            self.__ENCRYPTED__ = True
    v = Vault('zLNhfDsyNzozLzI3NjM0MzE2OjQ0MzI4OmQ4YzY4NjMxNzA4YWZhNGU5NmU5YzdkMzQ2MmJjNjE5YjI5MzdlMjEz')
    # the case that _vault_to_text is True
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    value = encoder.default(v)


# Generated at 2022-06-12 23:14:55.674615
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    myclass = AnsibleJSONEncoder()
    assert myclass.default(None) == 'null'
    assert myclass.default(0) == '0'
    assert myclass.default(1) == '1'
    assert myclass.default('') == ''
    assert myclass.default('test') == 'test'
    assert myclass.default(True) == 'true'
    assert myclass.default(False) == 'false'
    assert myclass.default([]) == '[]'
    assert myclass.default({}) == '{}'

# Generated at 2022-06-12 23:15:00.325286
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()

    assert encoder.default({'foo': 'bar'}) == {'foo': 'bar'}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default([{'foo': 'bar'}]) == [{'foo': 'bar'}]

# Generated at 2022-06-12 23:15:08.122438
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    """Checks that the modified AnsibleJSONEncoder works as intended."""
    import base64
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_text

    # Check if unmodified value works correctly
    test_value = "test_value"
    json_result = json.dumps(test_value, cls=AnsibleJSONEncoder)
    assert test_value == json_result

    # Check if date object works correctly
    date_object = datetime.date(2014, 12, 19)
    json_result = json.dumps(date_object, cls=AnsibleJSONEncoder)
    assert date_object.isoformat() == json_result

    # Check if vault object works correctly
    vault_password_file = None

# Generated at 2022-06-12 23:15:13.269352
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    import uuid


# Generated at 2022-06-12 23:15:21.007003
# Unit test for method default of class AnsibleJSONEncoder

# Generated at 2022-06-12 23:15:25.074455
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    encoder = AnsibleJSONEncoder()
    assert encoder.default(o=datetime.datetime(2011, 1, 1, 10, 11, 12, 131415)) == "2011-01-01T10:11:12.131415"


# Generated at 2022-06-12 23:15:35.796927
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
    from ansible.utils.unsafe_proxy import AnsibleVaultEncryptedUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleVaultEncryptedUnsafeBytes

    # ansible unsafe object
    unsafe_text_obj = AnsibleUnsafeText(u'foo')
    unsafe_bytestr = AnsibleUnsafeBytes(b'foo')

    unsafe_encoder = AnsibleJSONEncoder(preprocess_unsafe=True)

    # vault object
    vault_encoder = AnsibleJSONEncoder(vault_to_text=True)
    vault_obj1 = VaultLib([])
    vault

# Generated at 2022-06-12 23:16:33.487225
# Unit test for method default of class AnsibleJSONEncoder
def test_AnsibleJSONEncoder_default():
    '''
    Unit test for method default of class AnsibleJSONEncoder
    '''
    import sys
    import os
    import re

    ansible_lib_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
    ansible_lib_dir = re.sub(r'^\/.*', '', ansible_lib_dir)
    ansible_lib_dir = re.sub(r'^\\.*', '', ansible_lib_dir)
    ansible_lib_dir = re.sub(r'^.*\/', '', ansible_lib_dir)