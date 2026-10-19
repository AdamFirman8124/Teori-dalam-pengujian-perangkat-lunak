

# Generated at 2022-06-22 11:29:56.440969
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    result = yaml.dump(AnsibleVaultEncryptedUnicode(text_type('foo'), version=1), Dumper=AnsibleDumper, indent=0, default_flow_style=False)

# Generated at 2022-06-22 11:30:01.890399
# Unit test for function represent_unicode
def test_represent_unicode():
    representer = AnsibleDumper()
    assert represent_unicode(representer, text_type('foo')) == \
        yaml.representer.SafeRepresenter.represent_str(representer, text_type('foo'))
    assert represent_unicode(representer, text_type('foo')).value ==  \
        yaml.representer.SafeRepresenter.represent_str(representer, text_type('foo')).value



# Generated at 2022-06-22 11:30:07.284904
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    binstr = b'\x00\x01foo'
    assert dumper.represent_binary(binstr) == {'!' : '<ansible-internal-bin>', '#' : ' <ansible-internal-bin>\n'}

# Generated at 2022-06-22 11:30:15.582332
# Unit test for function represent_binary
def test_represent_binary():
    # test_empty_binary
    assert yaml.dump(binary_type(), Dumper=AnsibleDumper) == "!!binary ''\n"
    # test_simple_binary
    assert yaml.dump(binary_type(b'foo'), Dumper=AnsibleDumper) == "!!binary 'Zm9v'\n"
    # test_binary_with_spaces
    assert yaml.dump(binary_type(b'foo bar'), Dumper=AnsibleDumper) == "!!binary 'Zm9vIGJhcg=='\n"

# Generated at 2022-06-22 11:30:22.192349
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])

    enc = vault.encrypts('test_pass', 'test_data')
    eu = AnsibleVaultEncryptedUnicode(enc)

    dumper = AnsibleDumper()
    dumper.represent_vault_encrypted_unicode(eu)
    return

# Generated at 2022-06-22 11:30:31.631175
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:30:36.562131
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('abc')
    dumper = AnsibleDumper
    assert dumper.represent_data(data) == u'abc\n...\n'

# Generated at 2022-06-22 11:30:46.899467
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(AnsibleDumper, "a") == represent_unicode(yaml.representer.SafeRepresenter, "a")
    assert represent_unicode(AnsibleDumper, u'c') == represent_unicode(yaml.representer.SafeRepresenter, u'c')
    assert represent_unicode(AnsibleDumper, 'd') == represent_unicode(yaml.representer.SafeRepresenter, 'd')
    assert represent_unicode(AnsibleDumper, AnsibleUnicode(u'dd')) == represent_unicode(yaml.representer.SafeRepresenter, 'dd')
    #assert represent_unicode(AnsibleDumper, u'd') == represent_unicode(yaml.representer.SafeRepresenter, u'd')



# Generated at 2022-06-22 11:30:48.821930
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper(None, None, None).represent_undefined(AnsibleUndefined) == True




# Generated at 2022-06-22 11:30:59.272923
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Setup
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256\n3437303732306138613932326539623831346663366383163636162393239303237646232343533\n39363262373564656638643366356437653664326362333134613762323633356132326238363361\n356634\n'.encode()
    plaintext = 'hello world'
    aveu = AnsibleVaultEncryptedUnicode(ciphertext)

    # Exercise
    result = represent_vault_encrypted_unicode(AnsibleDumper, aveu)

    # Verify
    assert type(result) is tuple
    assert result[0] is aveu

# Generated at 2022-06-22 11:31:08.551401
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(object, 'test') == yaml.representer.SafeRepresenter.represent_str(object, 'test'.encode())
    assert represent_unicode(object, '你好') == yaml.representer.SafeRepresenter.represent_str(object, '你好'.encode())
    assert represent_unicode(object, '你好'.encode()) == yaml.representer.SafeRepresenter.represent_str(object, '你好'.encode())


# Generated at 2022-06-22 11:31:14.301204
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:31:24.056388
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    hostvars_data = {'k1': 'v1', 'k2': AnsibleUnsafeText('v2'), 'k3': AnsibleMapping({'k4': 'v4'})}
    hostvars = HostVars(hostvars_data)
    rep_hostvars = yaml.dump(hostvars, Dumper=AnsibleDumper)
    assert rep_hostvars == "k1: v1\nk2: 'v2'\nk3:\n  k4: v4\n"

# Generated at 2022-06-22 11:31:26.679040
# Unit test for function represent_unicode
def test_represent_unicode():
    data = {'value':123}
    rep_data = represent_unicode(AnsibleDumper, data)
    assert rep_data == '{value: 123}'

# Generated at 2022-06-22 11:31:30.274285
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    obj = AnsibleUnicode(u"unit test")
    yaml.dump(obj, Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:31:31.079663
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, "foo") == yaml.representer.SafeRepresenter.represent_str(None, "foo")



# Generated at 2022-06-22 11:31:39.560312
# Unit test for function represent_hostvars
def test_represent_hostvars():

    # Fill dictionary
    data = HostVarsVars()
    data['hostname'] = 'hostname'
    data['groups'] = ['group1', 'group2']
    data['vars'] = dict()
    data['vars']['foo'] = 'bar'

    # Create dumper with ansible custom representer
    dumper = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)

    # Assert on dumper output

# Generated at 2022-06-22 11:31:45.788343
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.yaml.dumper import VaultLib
    import os

    VAULT_PASSWORD_FILE = os.path.join(os.path.dirname(__file__), 'test_vault_password')
    with open(VAULT_PASSWORD_FILE, 'rb') as f:
        vault_password = f.read().strip()

    ve = VaultEditor(vault_password)
    vl = VaultLib('filename.yml')
    vl.password = vault_password

    # Test a scalar
    val = 'test-string'
    ev = ve.encrypt(val)
    et = vl.dump({'a': val})
    assert ev == et

    # Test a list

# Generated at 2022-06-22 11:31:51.021732
# Unit test for function represent_hostvars
def test_represent_hostvars():
    class TestHostvars(object):
        def __getitem__(self, key):
            return HostVars({'_hostvars': {'test': True}})

    ansible_dumper = AnsibleDumper()
    output = ansible_dumper.represent_hostvars(TestHostvars())
    assert output == "{'_hostvars': {'test': True}}"

# Generated at 2022-06-22 11:31:56.313297
# Unit test for function represent_undefined
def test_represent_undefined():
    dumped = yaml.dump([(1, AnsibleUndefined)])
    assert dumped == ('- - 1\n'
                      '  - !!python/object:ansible.template.AnsibleUndefined "{\'strict\': False, \'failed_when_result\': False}"\n')

# Generated at 2022-06-22 11:32:07.401876
# Unit test for function represent_binary
def test_represent_binary():
    '''
    AnsibleDumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )
    '''
    # We have to have a dummy class to use with the yaml.safe_dump
    class Dummy():
        def __init__(self, b):
            self.b = b

    data = b"abc"
    d = Dummy(data)

    # expected result
    res = yaml.safe_dump(d)

    # actual result
    rep = represent_binary(AnsibleDumper, data)
    ans = AnsibleDumper.represent_data(rep)

    assert res == ans



# Generated at 2022-06-22 11:32:15.443625
# Unit test for function represent_undefined
def test_represent_undefined():

    # Create ansible_undefined with no arguments
    ansible_undefined_1 = AnsibleUndefined()

    # Create ansible_undefined with _obj argument
    ansible_undefined_2 = AnsibleUndefined(obj="some_object")

    # Create ansible_undefined with _obj and _trace argument
    ansible_undefined_3 = AnsibleUndefined(obj="some_object", trace="some_trace")

    # Create a dict
    test_dict = dict()

    # Add ansible_undefined_1 to the dictionary
    test_dict['ansible_undefined_1'] = ansible_undefined_1

    # Add ansible_undefined_1 to the dictionary
    test_dict['ansible_undefined_2'] = ansible_undefined_2

    # Add ansible_undefined_

# Generated at 2022-06-22 11:32:21.106682
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    actual = yaml.dump(AnsibleVaultEncryptedUnicode(text_type('foo')), Dumper=AnsibleDumper)
    expected = text_type('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          666f6f00\n')
    assert actual == expected

# Generated at 2022-06-22 11:32:24.561454
# Unit test for function represent_binary
def test_represent_binary():
    test_string = b"abc\xff"
    result = yaml.dump(test_string, Dumper=AnsibleDumper)
    assert result == b"!binary |-\n  YWJj/w==\n"

# Generated at 2022-06-22 11:32:27.022285
# Unit test for function represent_undefined
def test_represent_undefined():
    # It's a black box, so just try it
    assert AnsibleDumper().represent_undefined(None)

# Generated at 2022-06-22 11:32:32.233422
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml.representer.BaseRepresenter.add_representer(
        type(u'dummy'),
        represent_unicode,
    )
    assert yaml.dump(u'dummy', Dumper=AnsibleDumper), '"dummy"\n...'


if __name__ == '__main__':
    import sys
    import unittest
    sys.exit(unittest.main())

# Generated at 2022-06-22 11:32:35.245661
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.parsing.yaml import load_yaml_undefined
    from ansible.template.jinja2 import AnsibleUndefined
    assert (load_yaml_undefined(AnsibleUndefined('foo')) == 'foo')



# Generated at 2022-06-22 11:32:44.513010
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.module_utils.six import BytesIO

    a = HostVars()
    a['foo'] = 1
    a['bar'] = 2

    b = VarsWithSources()
    b['foo'] = 1
    b['bar'] = 2

    c = HostVarsVars()
    c['foo'] = 1
    c['bar'] = 2

    data = {
        'a': a,
        'b': b,
        'c': c,
    }

    buf = BytesIO()
    AnsibleDumper(buf, encoding='utf-8').dump(data)
    assert b'a: {foo: 1, bar: 2}' in buf.getvalue()
    assert b'b: {foo: 1, bar: 2}' in buf.getvalue()

# Generated at 2022-06-22 11:32:48.190226
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    string = b'\xfa\xf2\xf1\x00'
    encoded = dumper.represent_binary(string)
    assert encoded == b'!!binary |\n  +H4='

# Generated at 2022-06-22 11:32:56.033825
# Unit test for function represent_binary
def test_represent_binary():
    # Test bytes
    data = b'hello'
    assert AnsibleDumper.represent_binary(AnsibleDumper, data) == "!!binary 'aGVsbG8='\n"

    # Test unicode
    data = u'hello'
    assert AnsibleDumper.represent_binary(AnsibleDumper, data) == u"!!binary 'aGVsbG8='\n"
    assert isinstance(AnsibleDumper.represent_binary(AnsibleDumper, data), text_type)



# Generated at 2022-06-22 11:33:00.261861
# Unit test for function represent_undefined
def test_represent_undefined():
    value = AnsibleUndefined("Value")
    assert AnsibleDumper().represent_data(value) == True

# Generated at 2022-06-22 11:33:05.885344
# Unit test for function represent_binary
def test_represent_binary():
    from io import StringIO
    stream = StringIO()
    serializer = yaml.serializer.Serializer(stream, Dumper=AnsibleDumper)
    # pylint: disable=protected-access
    serializer.open()
    serializer.represent(AnsibleUnsafeBytes(b'Hello World'))
    serializer.close()
    assert stream.getvalue() == "Hello World\n"

# Generated at 2022-06-22 11:33:10.429026
# Unit test for function represent_binary
def test_represent_binary():
    # Check that binary is dumped properly as str
    ansible_dumper = AnsibleDumper()
    binary = ansible_dumper.represent_data('binary')

    assert binary == "? binary\n"

    # Check that binary_type is dumped properly as str
    ansible_dumper = AnsibleDumper()
    binary = ansible_dumper.represent_data(binary_type(u'binary'))

    assert binary == "? binary\n"

# Generated at 2022-06-22 11:33:13.034529
# Unit test for function represent_undefined
def test_represent_undefined():
    """
    Unit test for function represent_undefined
    """
    dumper = AnsibleDumper(default_flow_style=False)
    undefined_object = AnsibleUndefined("Test Value")
    assert bool(undefined_object)
    assert dumper.represent_data(undefined_object)

# Generated at 2022-06-22 11:33:20.395954
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.six import text_type, binary_type

    # Create string with a special character, i.e. non-ASCII
    represent_binary_string = "X\xf0"
    # Convert to binary
    represent_binary_string_bin = binary_type(represent_binary_string)
    # Convert to text
    represent_binary_string_txt = text_type(represent_binary_string)

    # Create an instance of AnsibleDumper
    ad = AnsibleDumper()
    # Simulate the yaml.dumps() call on the AnsibleDumper instance
    represent_binary_string_yaml = ad.represent_binary(represent_binary_string_bin)
    # Convert the output to text

# Generated at 2022-06-22 11:33:30.305949
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    '''
    Test the AnsibleDumper.represent_binary function.
    Represent the byte string as a byte string in base64.

    :kwarg test_string: byte string to be dumped
    :kwarg expected_output: Expected string representation
    '''

    assert dumper.represent_binary(None, b'bytes') == '!!binary |\n  Ynl0ZXM='


# Generated at 2022-06-22 11:33:41.895535
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml import objects

    dumper = AnsibleDumper()

    # Test without style
    data = '0123456789abcdefABCDEF'
    assert type(data) == binary_type
    data = objects.AnsibleUnsafeBytes(data)
    output = dumper.represent_data(data)
    assert output == b'!unsafe "0123456789abcdefABCDEF"\n'

    # Test with style
    data = b'0123456789abcdefABCDEF'
    assert type(data) == binary_type
    data = objects.AnsibleUnsafeBytes(data)
    output = dumper.represent_data(data)
    assert output == b'!unsafe |\n  0123456789abcdefABCDEF\n'

    # Test with

# Generated at 2022-06-22 11:33:42.968234
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml.dump(AnsibleUndefined())

# Generated at 2022-06-22 11:33:45.438515
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(u'foo', Dumper=AnsibleDumper) == "foo\n...\n"



# Generated at 2022-06-22 11:33:55.036701
# Unit test for function represent_unicode
def test_represent_unicode():

    dumper = AnsibleDumper
    assert dumper.represent_unicode(dumper, u'hello') == u"'hello'"
    assert dumper.represent_unicode(dumper, 'hello') == u"'hello'"
    assert dumper.represent_unicode(dumper, u'\u2600') == u"'\u2600'"
    assert dumper.represent_unicode(dumper, '\u2600') == u"'\u2600'"
    assert dumper.represent_unicode(dumper, u'\xe9') == u"'\xe9'"
    assert dumper.represent_unicode(dumper, '\xe9') == u"'\xe9'"



# Generated at 2022-06-22 11:33:59.556149
# Unit test for function represent_binary
def test_represent_binary():
    n = AnsibleDumper.represent_binary(None, b'\x8e\xfe\xff')
    assert n == "!!binary |\n  /oexff"



# Generated at 2022-06-22 11:34:04.348450
# Unit test for function represent_binary
def test_represent_binary():
    obj = b'\xbc\xa0\xbc\xa0'
    result = AnsibleDumper().represent_binary(obj)
    expected = "!!binary |\n  wiL/wiL/"
    assert result == expected

# Generated at 2022-06-22 11:34:12.776697
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    ## Tests that the proper yaml output is generated for the encrypted data
    class AnsibleVaultFake:
        def __init__(self):
            self._ciphertext = 'AQAAAABAAAAAQAAAAEAAAABAA=='
            self._content = 'hello world'

    data = AnsibleVaultFake()
    assert represent_vault_encrypted_unicode(AnsibleDumper, data) == u'!vault |\n  AQAAAABAAAAAQAAAAEAAAABAA==\n'

# Generated at 2022-06-22 11:34:14.368158
# Unit test for function represent_undefined
def test_represent_undefined():
    dump = yaml.dump(AnsibleUndefined())

    assert dump == ''

# Generated at 2022-06-22 11:34:20.707766
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert yaml.representer.SafeRepresenter.represent_str(dumper, '') == yaml.representer.SafeRepresenter.represent_str(dumper, text_type(''))
    assert yaml.representer.SafeRepresenter.represent_str(dumper, 'foo') == yaml.representer.SafeRepresenter.represent_str(dumper, text_type('foo'))




# Generated at 2022-06-22 11:34:26.772675
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # use a dict as that is the data type to render
    dumper = AnsibleDumper()
    hostvars = HostVars(dict(test=dict(test=dict(test='test'))))
    hostvars_data = dumper.represent_dict(dict(hostvars))
    expected_data = '{hostvars: {test: {test: {test: test}}}}'
    assert hostvars_data == expected_data

# Generated at 2022-06-22 11:34:37.920473
# Unit test for function represent_hostvars

# Generated at 2022-06-22 11:34:49.054051
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:34:51.754301
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'asdf', Dumper=AnsibleDumper, default_flow_style=False) == u'!!binary |\n  YXNkZg==\n'


# Generated at 2022-06-22 11:34:59.019523
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils._text import to_bytes
    dumper = AnsibleDumper
    dumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )
    value = to_bytes('\x00foo\xFF')
    output = yaml.dump([value], default_flow_style=True, Dumper=AnsibleDumper).split('\n')
    assert output == ['- !!binary |', '  AQZmb28/', '']

# Generated at 2022-06-22 11:35:14.162845
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    text = u'secret'

# Generated at 2022-06-22 11:35:17.847767
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper()
    assert dumper.represent_hostvars(HostVars(dict(a=1, b=2), sources=[])) == dumper.represent_dict(dict(a=1, b=2))

# Generated at 2022-06-22 11:35:23.695747
# Unit test for function represent_hostvars
def test_represent_hostvars():

    h = HostVarsVars(vars=dict(a='123', b='456'))
    host = HostVars(name='test', hostvars=h)
    assert yaml.dump(host, Dumper=AnsibleDumper) == 'test:\n  a: 123\n  b: 456\n'

# Generated at 2022-06-22 11:35:35.012511
# Unit test for function represent_binary
def test_represent_binary():
    # Test for data equals ASCII characters
    data = '\n'.join(['a', 'b', 'c'])
    assert binary_type(data) == b'\n'.join([b'a', b'b', b'c'])
    result = yaml.dump(data, encoding='ascii', allow_unicode=False, Dumper=AnsibleDumper)
    assert result == 'a\nb\nc\n'
    # Test for data equals non-ASCII characters
    data = '\n'.join(['a', 'b', 'c\xe0'])
    assert binary_type(data) == b'\n'.join([b'a', b'b', b'c\xe0'])

# Generated at 2022-06-22 11:35:38.066321
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('test'), Dumper=AnsibleDumper) == "test\n...\n"



# Generated at 2022-06-22 11:35:45.531904
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    test_data = b'\x07\x03\x00test_represent_binary'
    result = dumper.represent_binary(dumper, test_data)
    assert result == u"!!binary |\n  CwAzAAB0ZXN0X3JlcHJlc2VudF9iaW5hcnk=\n"



# Generated at 2022-06-22 11:35:48.325765
# Unit test for function represent_undefined
def test_represent_undefined():
    foo = AnsibleUndefined('bar')
    assert yaml.safe_dump(foo, Dumper=AnsibleDumper) == ''

# Generated at 2022-06-22 11:35:53.154203
# Unit test for function represent_unicode
def test_represent_unicode():
    expected = "- u'unicode string'"
    rep_uni = represent_unicode(None, 'unicode string')
    assert rep_uni == expected
    # TODO: add more test cases for string with not printable characters
    #       or string with complex unicode symbols like emoji, dingbats, etc


# Generated at 2022-06-22 11:35:56.703820
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {
        'foo': 'bar',
        'baz': {
            'one': 1,
            'two': '2',
            'three': [3],
            'four': {'outers': {'inners': 4}}
        }
    }
    assert yaml.dump(HostVars(data), Dumper=AnsibleDumper) == yaml.dump(data, Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:36:08.627163
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.utils.unsafe_proxy import wrap_var
    dumper = AnsibleDumper(width=80, indent=2, default_style=False, default_flow_style=False)

# Generated at 2022-06-22 11:36:15.345043
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.load("'\u20ac'") == u"\u20ac"

# Generated at 2022-06-22 11:36:25.839320
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:36:36.249073
# Unit test for function represent_undefined
def test_represent_undefined():
    # The simplest case to test is when the value is a StrictUndefined.
    # We do this by creating a class that mimics the behaviour of the
    # StrictUndefined in the template.
    class StrictUndefinedForTesting:
        def __bool__(self):
            raise RuntimeError('value is undefined')

        def __nonzero__(self):
            # This must also be defined, because the jinja2.runtime.StrictUndefined
            # also defines it, and in python2, __bool__ is always called first.
            # If __nonzero__ is not defined, we will get a TypeError instead of
            # the RuntimeError that __bool__ normally raises.
            raise RuntimeError('value is undefined')

    strict_undefined = StrictUndefinedForTesting()

# Generated at 2022-06-22 11:36:42.006225
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.six import StringIO, b

    assert yaml.dump(b("foo"), Dumper=AnsibleDumper) == "!!binary |-\n  Zm9v\n\n"
    assert yaml.dump([b("foo")], Dumper=AnsibleDumper) == "[!!binary |-\n  Zm9v\n]\n"
    assert yaml.dump({b("foo"): b("bar")}, Dumper=AnsibleDumper) == "{!!binary |-\n  Zm9v\n: !!binary |-\n  YmFy\n}\n"

    a = {}
    a[b("foo")] = {}
    a[b("foo")][b("bar")] = b("baz")

# Generated at 2022-06-22 11:36:52.558403
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper(width=1000, indent=2)

    data = AnsibleUnicode(u'\ubcf4\uc784')
    yaml_data = dumper.represent_unicode(data)
    expected_yaml_data = yaml.representer.SafeRepresenter.represent_str(dumper, u'\ubcf4\uc784')
    assert yaml_data == expected_yaml_data

    data = AnsibleUnsafeText(u'\ubcf4\uc784')
    yaml_data = dumper.represent_unicode(data)
    expected_yaml_data = yaml.representer.SafeRepresenter.represent_str(dumper, u'\ubcf4\uc784')
    assert yaml_data == expected_yaml_data

    data = AnsibleUnsafe

# Generated at 2022-06-22 11:36:56.230973
# Unit test for function represent_hostvars
def test_represent_hostvars():
    block = HostVars(host=dict(a='b'))
    result = yaml.dump(block, Dumper=AnsibleDumper)
    # The block should be dumped as a dict
    assert(result == '{a: b}\n...\n')


# Generated at 2022-06-22 11:37:03.907023
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = HostVars()
    data["key"] = AnsibleUnicode("value")
    res = yaml.safe_dump(data, default_flow_style=False, Dumper=AnsibleDumper)
    assert res == 'key: "value"\n'

# Generated at 2022-06-22 11:37:08.416143
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('example')
    dumper = AnsibleDumper()
    expected_result = dumper.represent_str('example')

    result = dumper.represent_unicode(data)

    assert expected_result == result



# Generated at 2022-06-22 11:37:19.142684
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.decrypt import VaultLib
    from ansible.parsing.vault import VaultSecret

    ansible_dumper = AnsibleDumper()
    secret = VaultSecret(password=b'ansible')
    vault = VaultLib(secret)
    encrypted = vault.encrypt(b'Any text here')
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(encrypted)
    output = ansible_dumper.represent_vault_encrypted_unicode(ansible_vault_encrypted_unicode)

# Generated at 2022-06-22 11:37:23.402846
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = dict(
        foo=dict(a=1),
        bar=True
    )
    print(yaml.dump(HostVars(data), Dumper=AnsibleDumper))

# Generated at 2022-06-22 11:37:33.520166
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('foo bar')) == "'foo bar'\n"


# Generated at 2022-06-22 11:37:41.276543
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    hostvars = HostVars()
    hostvars.add_host("myhost", {'foo': 'bar'})
    hostvars.add_host("yourhost", {'foo': 'baz'})
    assert dumper.represent_hostvars(dumper, hostvars) == [
        {'key': 'myhost'},
        {'foo': 'bar'},
        {'key': 'yourhost'},
        {'foo': 'baz'}
    ]

# Generated at 2022-06-22 11:37:53.788606
# Unit test for function represent_binary

# Generated at 2022-06-22 11:38:03.115458
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    Unit test function to ensure that the represent_undefined function will not
    cause an exception when called with an Undefined object. This can happen
    when jinja2 filters are used on objects which are not AnsibleUndefined and
    have a __bool__ defined that can raise an exception.
    '''
    dumper = yaml.dumper.SafeDumper
    dumper.add_representer(
        AnsibleUndefined,
        represent_undefined,
    )
    data = dict(undefined=AnsibleUndefined())
    dumped = yaml.dump(data, Dumper=dumper, default_flow_style=False)
    assert dumped == 'undefined: {}\n'

# Generated at 2022-06-22 11:38:06.218295
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(AnsibleDumper, AnsibleUnicode(u'foo')) == u'foo'
    assert represent_unicode(AnsibleDumper, AnsibleUnicode('foo')) == u'foo'

# Generated at 2022-06-22 11:38:13.750841
# Unit test for function represent_undefined
def test_represent_undefined():
    class TestRepresentUndefined:
        def __init__(self):
            self._undefined_ = True

        def __bool__(self):
            return not self._undefined_

    class TestRepresentNotUndefined:
        pass

    undefined_obj = TestRepresentUndefined()
    not_undefined_obj = TestRepresentNotUndefined()

    for obj in [undefined_obj, not_undefined_obj]:
        try:
            represent_undefined(None, obj)
        except Exception as e:
            assert isinstance(e, TypeError), \
                "Object %s raised unexpected exception: %s" % (obj, e.__class__)
        else:
           assert isinstance(obj, TestRepresentNotUndefined), \
               "Object %s was incorrectly represented as undefined" % obj

# Generated at 2022-06-22 11:38:23.951589
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    valid_values = [b'test123', b'\xff\x00\x7f', b'\x00\x7f\xff']
    for value in valid_values:
        assert dumper.represent_binary(dumper, value) == yaml.representer.SafeRepresenter.represent_binary(dumper, value)
    invalid_values = [[b'test123'], {b'test123': b'test456'}, 42, 42.0, None, True, False]
    for value in invalid_values:
        try:
            dumper.represent_binary(dumper, value)
            assert False
        except yaml.representer.RepresenterError:
            pass
        except Exception:
            assert False



# Generated at 2022-06-22 11:38:33.032693
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(
        dict(
            test_key_1='test_value_1',
            test_key_2='test_value_2'
        )
    )
    stream = yaml.dump(data, Dumper=AnsibleDumper)
    # Note: .load() is required to make sure the stream is present.
    # Otherwise the object cannot be used.
    assert isinstance(yaml.load(stream), dict)
    print(stream)
    assert stream == 'test_key_1: test_value_1\ntest_key_2: test_value_2\n'



# Generated at 2022-06-22 11:38:41.751628
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:38:47.414427
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert dumper.represent_unicode(dumper, AnsibleUnicode(u'foo')) == dumper.represent_unicode(dumper, AnsibleUnsafeText(u'foo')) == dumper.represent_unicode(dumper, u'foo')

# Generated at 2022-06-22 11:39:15.854937
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:39:18.682133
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.safe_dump(binary_type('a'.encode()), default_flow_style=True) == "!binary |-\na"

# Generated at 2022-06-22 11:39:20.469838
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper) == ''



# Generated at 2022-06-22 11:39:31.982165
# Unit test for function represent_undefined

# Generated at 2022-06-22 11:39:36.098076
# Unit test for function represent_binary
def test_represent_binary():
    output = represent_binary(None, b'hello\x00\xff')
    assert output == "!!binary |\n  aGVsbG8AKgA=\n"



# Generated at 2022-06-22 11:39:37.659873
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper.represent_undefined('Not Used') == True



# Generated at 2022-06-22 11:39:43.910634
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(None, b'foo\x00bar') == u'!!binary |\n  Zm9vAGJhcg==\n'
    assert AnsibleDumper.represent_binary(None, b'foo\x00bar\x80') == u'!!binary |\n  Zm9vAGJhcgD4\n'