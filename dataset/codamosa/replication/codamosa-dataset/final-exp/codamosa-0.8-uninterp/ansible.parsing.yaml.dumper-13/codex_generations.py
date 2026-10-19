

# Generated at 2022-06-22 11:29:48.728393
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    binary_str = b'\x12\x13\x14\x15'
    data = dumper.represent_binary(dumper, binary_str)
    assert data == "!binary |-\n  EyQxMxExNQ==\n"



# Generated at 2022-06-22 11:29:55.050004
# Unit test for function represent_undefined
def test_represent_undefined():
    undefined = AnsibleUndefined(var_name='undefined', obj=None)
    # In Python 2 dumper.represent_data() returns utf-8 encoded string
    # So we have to decode it to unicode
    # In Python 3 the return value is always unicode
    # In Python 2 dumper.represent_data() will crash
    # if there is Undefined in the data dict
    assert yaml.safe_load(yaml.dump(undefined, Dumper=AnsibleDumper)) is not None

    # Now test with a dict
    data = {
        'my_var': 'my_value',
        'my_undefined_var': undefined,
    }

# Generated at 2022-06-22 11:29:57.659490
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    bin_data = '\x01\x02\x03\x04'
    # The result should be b64 encoded
    assert dumper.represent_binary(dumper, bin_data) == 'AAEAAQ=='

# Generated at 2022-06-22 11:30:09.879670
# Unit test for function represent_undefined
def test_represent_undefined():

    string1 = u"This is a regular ansible string"

    if not isinstance(string1, AnsibleUndefined):
        assert False

    output = AnsibleDumper.represent_scalar(
        u'tag:yaml.org,2002:str', string1, style='"'
    )
    assert (output == u'"This is a regular ansible string"\n')

    string3 = u"This is தமிழ்"

    if not isinstance(string3, AnsibleUndefined):
        assert False

    output = AnsibleDumper.represent_scalar(
        u'tag:yaml.org,2002:str', string3, style='"'
    )

# Generated at 2022-06-22 11:30:16.389087
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvar = dict(
        a=1,
        b=2,
        c=dict(
            d=3,
            e=4,
        ),
        f=5,
    )

    hvs = HostVars(host=None, variables=hostvar)
    assert yaml.dump(hvs, Dumper=AnsibleDumper) == yaml.dump(hostvar, Dumper=AnsibleDumper)  # noqa

# Generated at 2022-06-22 11:30:21.248821
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    Tests the function represent_undefined returns an empty dict
    when an AnsibleUndefined object is passed.
    '''
    data = AnsibleUndefined()
    assert represent_undefined(AnsibleDumper, data) == {}



# Generated at 2022-06-22 11:30:26.509352
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(dict(a=AnsibleUnicode(u'foo'))) == 'a: foo\n'
    assert yaml.dump(dict(a=AnsibleUnsafeText(u'foo'))) == 'a: foo\n'
    assert yaml.dump(dict(a=AnsibleUnsafeText(u'foo'))) == 'a: foo\n'


# Generated at 2022-06-22 11:30:30.374162
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    data = HostVars({"ansible_all_ipv4_addressess": ["192.168.1.1"]})
    assert dumper.represent_hostvars(dumper, data) == dumper.represent_dict(dumper, dict(data))



# Generated at 2022-06-22 11:30:43.677134
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper

# Generated at 2022-06-22 11:30:54.848597
# Unit test for function represent_binary
def test_represent_binary():
    y = yaml.YAML(typ='unsafe')
    y.default_flow_style = False
    rp = y.representer
    rp.add_representer(
        AnsibleUnsafeBytes,
        yaml.representer.SafeRepresenter.represent_binary,
    )

# Generated at 2022-06-22 11:31:05.690781
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    value = AnsibleVaultEncryptedUnicode(u"hello")
    assert represent_vault_encrypted_unicode(AnsibleDumper, value) == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30363464366538663734623235653734643066623662323562653538333463633264616264366364\n          39376432373365386432643939376633383263616239306266353338653264656531613362303261\n          3465\n          "



# Generated at 2022-06-22 11:31:12.304403
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert represent_unicode(dumper, u'foo') == 'foo'
    assert represent_unicode(dumper, u'\x1b') == '\\e'
    assert represent_unicode(dumper, u'\U0001F4A9') == '\\U0001F4A9'
    assert represent_unicode(dumper, u'\n') == '\\n'
    assert represent_unicode(dumper, u'\u1234') == '\\u1234'
    assert represent_unicode(dumper, '\x1b') == '\\e'

# Generated at 2022-06-22 11:31:17.900722
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    str_utf8 = u'\u2260'
    str_unicode = u'\u2260'
    assert yaml.representer.SafeRepresenter.represent_str(dumper, str_utf8) == yaml.representer.SafeRepresenter.represent_str(dumper, str_unicode)



# Generated at 2022-06-22 11:31:21.547068
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert not dumper.represent_undefined(AnsibleUndefined(error_msg='fail'))

# TODO: add test for represent_hostvars

# Generated at 2022-06-22 11:31:23.947046
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    output = yaml.representer.SafeRepresenter.represent_binary(dumper, binary_type('\x00\x00\x00\x00'))
    assert output == u'!!binary |\n  AAAAAA==\n'

# Generated at 2022-06-22 11:31:28.941164
# Unit test for function represent_binary
def test_represent_binary():
    t_data = b'hello'
    a_data = AnsibleUnsafeBytes(t_data)
    dumper = AnsibleDumper
    rep_data = dumper.represent_binary(dumper, a_data)
    assert rep_data == "!!binary |-\n  aGVsbG8=\n"

# Generated at 2022-06-22 11:31:31.582578
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    f = represent_vault_encrypted_unicode
    assert f(f, AnsibleVaultEncryptedUnicode('foo')) == f(f, 'foo')



# Generated at 2022-06-22 11:31:40.122318
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars('test')
    hv.add_host_var('host1', 'foo', 'bar')
    hv.add_host_var('host1', 'baz', 'qux')
    hv.add_host_var('host2', 'foo', 'abc')
    hv.add_host_var('host2', 'baz', 'xyz')

    assert yaml.dump(hv, Dumper=AnsibleDumper) == \
        "host1:\n" \
        "  baz: qux\n" \
        "  foo: bar\n" \
        "host2:\n" \
        "  baz: xyz\n" \
        "  foo: abc\n"

# Generated at 2022-06-22 11:31:50.960152
# Unit test for function represent_hostvars
def test_represent_hostvars():
    import copy
    import six
    data = {'var1': 'value1', 'var2': {'var1.1': 'value1.1'}, 'var3': ['value1.2', 'value1.3']}
    if six.PY2:
        data = copy.copy(data)
    else:
        data = copy.deepcopy(data)
    hostvars = HostVars(data)
    # For python 2, AnsibleDumper would cause deepcopy
    representer = AnsibleDumper(None, None, None)
    hostvars_repr = representer.represent_hostvars(hostvars)

# Generated at 2022-06-22 11:31:54.813898
# Unit test for function represent_binary
def test_represent_binary():
    representer = AnsibleDumper()
    value = representer.represent_binary(b'\x00\x01')
    assert value == '!!binary |\n  AA=='




# Generated at 2022-06-22 11:32:06.092844
# Unit test for function represent_binary
def test_represent_binary():
    import sys
    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO

    # Python 3 writes out the bytes with u'\u00ff' escapes, while Python 2
    # writes out the raw bytes.
    result = StringIO()
    yd = AnsibleDumper(result, allow_unicode=True)
    yd.represent_binary(b'\xff')
    if sys.version_info[0] == 2:
        assert result.getvalue() == '- "\xff"\n'
    else:
        assert result.getvalue() == '- "\\u00ff"\n'

# Generated at 2022-06-22 11:32:13.919422
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''Ensure represent_vault_encrypted_unicode returns expected output.'''
    yaml.add_representer(
        AnsibleVaultEncryptedUnicode,
        represent_vault_encrypted_unicode,
        Dumper=AnsibleDumper,
    )
    obj = AnsibleVaultEncryptedUnicode('foo')
    output = yaml.dump(obj)

# Generated at 2022-06-22 11:32:24.798382
# Unit test for function represent_unicode
def test_represent_unicode():
    import sys

    # These unicode strings can be decoded by sys.getdefaultencoding
    u1 = AnsibleUnicode('\u3042')
    u2 = AnsibleUnicode('\u3044')
    u3 = AnsibleUnicode('\u3046')
    u4 = AnsibleUnicode('\u3048')

    # These unicode strings can not be decoded by sys.getdefaultencoding
    u5 = AnsibleUnicode('\u3042')
    u6 = AnsibleUnicode('\u3044')
    u7 = AnsibleUnicode('\u3046')
    u8 = AnsibleUnicode('\u3048')


# Generated at 2022-06-22 11:32:33.246063
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    actual = yaml.dump(AnsibleVaultEncryptedUnicode(u'foo'), Dumper=AnsibleDumper)
    expected = u'!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  666f6f\n  39303664336561646435346564333630643533376439383762326631376162373339663131346\n  626164383536653633613063646565313236396437656336623131650a\n'
    assert actual == expected

# Generated at 2022-06-22 11:32:38.729906
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, b'hello world') == u"!binary |\n  aGVsbG8gd29ybGQ=\n"
    assert dumper.represent_binary(dumper, b'\x00\x01\x02') == u"!binary |\n  AAAECAw==\n"
    assert dumper.represent_binary(dumper, b'!@#$%^&*()_') == u"!binary |\n  ISFAIyVeJionXw==\n"



# Generated at 2022-06-22 11:32:47.347461
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.compat.tests.mock import patch, MagicMock

    # Ensure that yaml.representer.SafeRepresenter.represent_binary() is called.
    # This test used to fail with a KeyError because the python yaml package used for testing did
    # not have a representer for bytes objects.

    b = b'foo'
    with patch.object(yaml.representer.SafeRepresenter, 'represent_binary', return_value='foo') as mock_method:
        represent_binary(MagicMock(), b)
        mock_method.assert_called_once_with('foo')



# Generated at 2022-06-22 11:32:58.371708
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.vars.encrypted_lookup import VaultLib
    from ansible.vars.encrypted_lookup.vault import VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-22 11:33:03.941488
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(AnsibleDumper, HostVars({"a": "b"})) == represent_hostvars(AnsibleDumper, {"a": "b"})
    assert represent_hostvars(AnsibleDumper, HostVarsVars({"a": "b"})) == represent_hostvars(AnsibleDumper, {"a": "b"})

# Generated at 2022-06-22 11:33:15.194446
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # hostvars object
    hostvars = HostVars(variables=dict(a=1, b=2))
    expected_yaml = '{"a": 1, "b": 2}'
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == expected_yaml
    # hostvarsvars object
    hostvarsvars = HostVarsVars(hostvars=hostvars, variables=dict(c=3))
    expected_yaml = '{"a": 1, "b": 2, "c": 3}'
    assert yaml.dump(hostvarsvars, Dumper=AnsibleDumper) == expected_yaml
    # varswithsources object

# Generated at 2022-06-22 11:33:18.414087
# Unit test for function represent_unicode
def test_represent_unicode():
    representer = AnsibleDumper()
    assert representer.represent_unicode('foo') == u"'foo'"
    assert representer.represent_unicode(u'\xe9') == u"'\xe9'"



# Generated at 2022-06-22 11:33:30.341808
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import unit.utils.vault as vault_util
    test_val = 'test'
    representation = b'!vault |\n          $ANSIBLE_VAULT;1.2;AES256;ansible\n          393032396661353764373433663937343433313363666235313531353238363231626262383137\n          323637353039653836353830353661343562353634303432393633646130306438303562663431\n          346565353961346431343639393331303437323864313835653964653035616230313065353165\n          313236\n          '

    key = vault_util.make_key('ansible')

# Generated at 2022-06-22 11:33:33.999717
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.dump(HostVars({'key': 'value'}), Dumper=AnsibleDumper) == '{key: value}\n...\n'



# Generated at 2022-06-22 11:33:36.289502
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'\x00\t') == '!!binary |-\n  AAAB\n'

# Generated at 2022-06-22 11:33:43.740470
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''
    Ensure that this function operates as expected
    '''

# Generated at 2022-06-22 11:33:52.250185
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    AnsibleUndefined does not implement __bool__ but
    ansible.template.AnsibleUndefined does.
    '''
    try:
        from ansible.template import AnsibleUndefined
    except ImportError:
        from ansible.template import StrictUndefined as AnsibleUndefined

    dumper = AnsibleDumper()
    assert dumper.represent_undefined(AnsibleUndefined())
    assert not dumper.represent_undefined(None)


if __name__ == '__main__':
    test_represent_undefined()
    print("No problems detected, exiting")

# Generated at 2022-06-22 11:33:53.941678
# Unit test for function represent_unicode
def test_represent_unicode():
    """
    >>> represent_unicode(AnsibleDumper, 'foo')
    "foo"
    """



# Generated at 2022-06-22 11:34:05.502845
# Unit test for function represent_binary
def test_represent_binary():
    if not hasattr(yaml.representer, 'SafeRepresenter'):
        return

    # Making a string unicode should return a scalar instead of a bytes.
    dumper = yaml.representer.SafeRepresenter()
    represent_binary(dumper, b'hello') == yaml.representer.SafeRepresenter.represent_str(dumper, u'hello')

    # Making a bytearray unicode should return a scalar instead of a bytes.
    dumper = yaml.representer.SafeRepresenter()
    represent_binary(dumper, bytearray(b'hello')) == yaml.representer.SafeRepresenter.represent_str(dumper, u'hello')

    # Making a bytes with a non ascii byte should return a bytes instead of a scalar.
    dumper = yaml.representer

# Generated at 2022-06-22 11:34:13.634481
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined()) == ''
    assert yaml.dump({'foo': AnsibleUndefined()}, default_flow_style=False) == 'foo: {}\n'
    assert yaml.dump({'foo': [AnsibleUndefined()]}, default_flow_style=False) == 'foo:\n- {}\n'


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-22 11:34:18.255927
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'a': 1, 'b': 2, 'c': 3}
    dumper = AnsibleDumper()
    output = dumper.represent_hostvars(data)
    assert output is not None
    assert output.tag == u'tag:yaml.org,2002:map'



# Generated at 2022-06-22 11:34:22.700400
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Setup
    data = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n3137656638333239346234323338323261316132316433643462303166623335323361356466353265\n3962333433653237613137386565353839653730663635353235376534663338653961373833363163\n3735373161396136623563366237383666303534663734356630363964656566333637366666323565\n32366336353033\n')

    # Execute
    out = represent_vault_encrypted_unicode(None, data)

    # Assert

# Generated at 2022-06-22 11:34:33.024364
# Unit test for function represent_hostvars
def test_represent_hostvars():
    ''' Unit test for function represent_hostvars
    '''
    hosts = {
        'foo': {
            'bar': 'baz'
        }
    }
    expected_result = '{foo: {bar: baz}}'
    result = yaml.dump(hosts, Dumper=AnsibleDumper, default_flow_style=False)

    assert result == expected_result

# Generated at 2022-06-22 11:34:39.422816
# Unit test for function represent_hostvars
def test_represent_hostvars():
    d = AnsibleDumper()
    hostvars = HostVars()
    hostvars.add_host_var('host1', 'var1', 'value')
    hostvars.add_host_var('host1', 'var2', 'value')
    hostvars.add_host_var('host2', 'var1', 'value')
    d.represent_hostvars(hostvars) == {'host1': {'var1': 'value', 'var2': 'value'},
                                       'host2': {'var1': 'value'}}

# Generated at 2022-06-22 11:34:49.721498
# Unit test for function represent_binary
def test_represent_binary():
    # Note, just the base64-encoded version of "some text"
    binary_data = (b'c29tZSB0ZXh0')

    # Test basic functionality
    yaml_data = yaml.dump(binary_data, Dumper=AnsibleDumper)
    assert yaml_data == '!!binary |\n  c29tZSB0ZXh0\n'

    # Test when input is str()
    yaml_data = yaml.dump(str(binary_data), Dumper=AnsibleDumper)
    assert yaml_data == '!!binary |\n  c29tZSB0ZXh0\n'

    # Test when input is unicode()
    yaml_data = yaml.dump(unicode(binary_data), Dumper=AnsibleDumper)
    assert y

# Generated at 2022-06-22 11:34:56.571496
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleMapping
    test_data = {'HostVars': HostVars(HostVarsVars())}
    x = yaml.safe_dump(test_data)
    assert isinstance(x, text_type)
    y = yaml.load(x)
    assert test_data == y



# Generated at 2022-06-22 11:35:07.392919
# Unit test for function represent_binary
def test_represent_binary():
    d = AnsibleDumper()
    # Test that it doesn't escape the BOM if present
    b = u'\ufefffoo'.encode('utf-8-sig')
    assert yaml.representer.SafeRepresenter.represent_binary(d, b, style='') == b
    assert yaml.representer.SafeRepresenter.represent_binary(d, b, style='|') == b
    assert yaml.representer.SafeRepresenter.represent_binary(d, b, style='>') == b
    assert yaml.representer.SafeRepresenter.represent_binary(d, b, style='|>') == b

if __name__ == '__main__':
    test_represent_binary()

# Generated at 2022-06-22 11:35:17.229045
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import logging
    # These are temporary logger settings to get rid of warnings that would flood the output
    # Without it the output is too long and is a distraction to the actual error.
    # We are only interested in the actual error anyway so no need to see the long list of repr
    log_handlers = list(logging.getLogger().handlers)
    logging.getLogger().handlers = []
    expected = {"ansible_variable": "some_value"}
    data = {"ansible_variable": AnsibleUnicode("some_value")}
    dumped = yaml.dump(data, Dumper=AnsibleDumper)
    loaded = yaml.load(dumped, Loader=AnsibleLoader)
    assert loaded == expected
    # Turn the logger

# Generated at 2022-06-22 11:35:28.451897
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:35:38.212897
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''
    Test representer HostVars.
    '''
    hostvars = HostVars()
    hostvars['host1'] = {'var1': 'val1'}

    # Without dumper
    assert yaml.dump({'hostvars': hostvars}) == "{'hostvars': {'host1': {'var1': 'val1'}}}\n"

    # With dumper
    assert yaml.dump({'hostvars': hostvars}, Dumper=AnsibleDumper) == "{'hostvars': {'host1': {'var1': 'val1'}}}\n"

# Generated at 2022-06-22 11:35:41.672025
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    assert dumper.represent_undefined(dumper, None) is False



# Generated at 2022-06-22 11:35:46.464640
# Unit test for function represent_binary
def test_represent_binary():
    obj = dict(foo=u'bar', baz=u'blah')
    obj['unicode_key'] = u'unicode_value'
    obj[u'unicode_key'] = u'unicode_value'
    yaml.dump(obj, Dumper=AnsibleDumper, allow_unicode=True, encoding='utf-8')

# Generated at 2022-06-22 11:35:55.757873
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml.dump(AnsibleUndefined(), AnsibleDumper)

# Generated at 2022-06-22 11:36:07.568271
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

    vault_secret = VaultLib([])
    ciphertext = vault_secret.encrypt('foo')
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(ciphertext)

    yaml_string = yaml.dump(ansible_vault_encrypted_unicode, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:36:15.280012
# Unit test for function represent_unicode
def test_represent_unicode():
    original = {
        'plain': b'foo',
        'unicode': u'\u2713',
        'mixed': '\u2713',
        'vault': AnsibleVaultEncryptedUnicode('f00'),
    }

# Generated at 2022-06-22 11:36:22.107597
# Unit test for function represent_hostvars
def test_represent_hostvars():

    # Setup
    data = {'var1': 'foo'}
    hostvars = HostVars()
    hostvars['testhost'] = data
    hostvars_vars = HostVarsVars(hostvars)

    # Actual test
    assert 'var1: foo' in yaml.dump(hostvars_vars, Dumper=AnsibleDumper, default_flow_style=False)


# Test the dumping of AnsibleVaultEncryptedUnicode as well as the literal block scalar

# Generated at 2022-06-22 11:36:32.619571
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    dumper = AnsibleDumper

    class Test(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    # Test a simple object
    test = Test('foo', 'bar')
    assert dumper.represent_hostvars(test) == dumper.represent_dict(dict(test))

    # Test a complex object
    test = Test(Test('foo', 'bar'), Test('baz', 'qux'))
    assert dumper.represent_hostvars(test) == dumper.represent_dict(dict(test))

    # Test a simple dict
    test = dict(a='foo', b='bar')

# Generated at 2022-06-22 11:36:40.017951
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    text = """
    foo: "\x00"
    """

    data = yaml.load(text, Loader=AnsibleLoader)

    # Python 2: \x00 will decode to \x00
    # Python 3: \x00 will decode to \u0000
    assert text_type(data['foo']) == '\x00'

    # In both Python 2 and Python 3, str.encode('latin-1') will encode
    # \x00 to b"\x00"
    assert data['foo'].encode('latin-1') == b"\x00"

    # Now, dump the data and see what YAML dumps

# Generated at 2022-06-22 11:36:43.661418
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    binary = b'\x01'
    assert dumper.represent_data(binary) == '!!binary |\n  AQ==\n'

# Generated at 2022-06-22 11:36:45.451830
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml.dump(AnsibleUndefined, default_style="|", Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:36:55.611828
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = u'$ANSIBLE_VAULT;1.1;AES256\n'
    data += u'39636464663734306633313262373166313139363135363933643533656438386238633961363839\n'
    data += u'3431633764306537366462653637313433666262396337310a396466356133383261626137313235\n'
    data += u'34656430316531363066396130313962663364616264313236393934633665643530383664636265\n'

# Generated at 2022-06-22 11:37:00.383510
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.module_utils.six import StringIO
    output = StringIO()
    dumper = yaml.SafeDumper(output)
    represent_unicode(dumper, u'unicode')
    assert output.getvalue() == "unicode\n"

# Generated at 2022-06-22 11:37:29.127638
# Unit test for function represent_hostvars
def test_represent_hostvars():

    from ansible.vars.reserved import Reserved

    test_value = dict(key="value")

    # Create an instance of hostvars
    hr = Reserved()
    hv = HostVars([hr], a=test_value)

    # Dump the hostvars instance
    result = yaml.dump(hv.to_dict())

    # Check the result is what we expect
    assert result == "a:\n    key: value\n"

    test_value = dict(key="value")

    # Create an instance of varswithsources
    hr = Reserved()
    hv = VarsWithSources([hr], a=test_value)

    # Dump the varswithsources instance
    result = yaml.dump(hv.to_dict())

    # Check the result is what we expect
    assert result

# Generated at 2022-06-22 11:37:31.336292
# Unit test for function represent_unicode
def test_represent_unicode():

    result = represent_unicode(AnsibleDumper, "test")

    # check result is correct
    assert result == u"'test'"



# Generated at 2022-06-22 11:37:42.408680
# Unit test for function represent_unicode
def test_represent_unicode():
    # Check that it returns a unicode string
    # and the returned string is correctly encoded
    unicode_string = "こんにちは"
    assert isinstance(represent_unicode(None, unicode_string), text_type)
    assert yaml.dump(unicode_string, Dumper=AnsibleDumper) == "- こんにちは\n"

    # Check that it returns a unicode string
    # and the returned string is correctly encoded even
    # if input is str
    ascii_string = "Hello"
    assert isinstance(represent_unicode(None, ascii_string), text_type)
    assert yaml.dump(ascii_string, Dumper=AnsibleDumper) == "- Hello\n"



# Generated at 2022-06-22 11:37:50.223727
# Unit test for function represent_unicode
def test_represent_unicode():

    # Test using a string literal
    data = AnsibleUnicode('string literal')
    expected_result = "string literal"

    dumper = AnsibleDumper(None, default_flow_style=False)
    result = dumper.represent_unicode(data)

    assert result == expected_result, \
        "The result should be identical to the expected result. Result: %s, Expected: %s" \
        % (result, expected_result)



# Generated at 2022-06-22 11:37:59.320695
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''
    Tests that the function represent_vault_encrypted_unicode
    returns a correct string representation of a Vault object
    '''

    data = b'$ANSIBLE_VAULT;1.1;AES256\n33326666653466356361643338613365653638363264613231326537333163376531393262386266636\n393930383962323433353430666134613862356632626639666130356665363661316164356530306361\n65636566626565313132313166366437623531353530376632313530663533393837613336643530\n'


# Generated at 2022-06-22 11:38:02.837275
# Unit test for function represent_binary
def test_represent_binary():
    data = b'\x00\x01'
    assert yaml.dump(data, Dumper=AnsibleDumper) == b"!binary |\n  AA==\n"



# Generated at 2022-06-22 11:38:12.986747
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import MultipleVariable
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars

    hostvars = HostVars()
    hostvars.add_host()
    # VariableManager.set_nonpersistent_facts will set the value of ansible_facts
    # to NonPersistentDict which is a subclass of HostVarsVars
    hostvars.set_nonpersistent_facts(MultipleVariable('ansible_facts', {}, True))
    hostvars.set_variable(MultipleVariable('ansible_connection', 'ssh', False))

    assert represent_hostvars(AnsibleDumper(), hostvars) == '{ansible_facts: {}, ansible_connection: ssh}'

# Generated at 2022-06-22 11:38:18.027030
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(None, AnsibleVaultEncryptedUnicode(b'hello')).value == '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          3536363732303537336430343764353365643035386434352d6466356364663036642d343764663037\n          362d3961363737356532322d6563336336336633632623463386330\n          '

# Generated at 2022-06-22 11:38:22.424742
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    aueo = AnsibleVaultEncryptedUnicode('foo', b'$ANSIBLE_VAULT;1.1;AES256', b'bar')
    yaml.dump(aueo, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:38:33.560503
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    representer = AnsibleDumper()
    # create a fake piece of vault text

# Generated at 2022-06-22 11:39:23.734883
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.module_utils.common.collections import ImmutableDict

    data = {}
    d = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    assert d == '{}\n'

    data = dict(a=1)
    d = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    assert d == 'a: 1\n'

    data = ImmutableDict()
    d = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    assert d == '{}\n'

    data = ImmutableDict(a=1)
    d = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:39:32.286492
# Unit test for function represent_unicode
def test_represent_unicode():
    assert repr(yaml.dump(AnsibleUnicode(u'foo'))) == "u'foo\\n'"
    assert repr(yaml.dump(AnsibleUnicode(u'foo'), default_flow_style=True)) == "u'foo'"
    assert repr(yaml.dump(AnsibleUnicode(u"foo\n"))) == "u'foo\\n'"
    assert repr(yaml.dump(AnsibleUnicode(u"foo\n"), default_flow_style=True)) == "u'foo\\n'"

# Generated at 2022-06-22 11:39:38.506283
# Unit test for function represent_unicode
def test_represent_unicode():
    u = u'hello_world'
    data = dict(
        ansible_var=AnsibleUnicode(u),
    )
    expected_representation = "ansible_var: hello_world\n"
    representation = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    assert representation == expected_representation



# Generated at 2022-06-22 11:39:43.657017
# Unit test for function represent_undefined
def test_represent_undefined():
    #yaml.dump(AnsibleUndefined(), AnsibleDumper)
    try:
        yaml.dump([AnsibleUndefined()], AnsibleDumper)
    except Exception:
        # We should get here
        pass
    else:
        # Should not get here
        assert False