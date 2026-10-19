

# Generated at 2022-06-22 11:29:49.320783
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(width=1000)
    assert dumper.represent_undefined(AnsibleUndefined())



# Generated at 2022-06-22 11:29:55.322129
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = yaml.dumper.SafeDumper
    dumper.add_representer(
        AnsibleVaultEncryptedUnicode,
        represent_vault_encrypted_unicode,
    )
    assert represent_vault_encrypted_unicode(dumper, AnsibleVaultEncryptedUnicode('test')) == '!vault |\n          dGVzdA==\n'


# Generated at 2022-06-22 11:29:57.335475
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    data = u'test'
    res = represent_unicode(dumper, data)
    assert res == u'test\n...\n'



# Generated at 2022-06-22 11:29:58.470156
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    value = AnsibleUndefined()
    assert dumper.represent_undefined(value) is False



# Generated at 2022-06-22 11:30:10.615200
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:30:17.004484
# Unit test for function represent_unicode
def test_represent_unicode():
    class DumperWithString(yaml.Dumper):
        def represent_str(self, data):
            return self.represent_scalar('tag:yaml.org,2002:str', data, style='"')

    dumper = DumperWithString()
    a = AnsibleUnicode(u'abc')
    assert dumper.represent_data(a) == u'!!python/unicode "abc"\n'



# Generated at 2022-06-22 11:30:28.319888
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml.safe_dump(AnsibleUnicode('foo'), sys.stdout, default_flow_style=False, Dumper=AnsibleDumper)
    yaml.safe_dump(AnsibleUnsafeText('foo'), sys.stdout, default_flow_style=False, Dumper=AnsibleDumper)
    yaml.safe_dump(AnsibleUnsafeBytes('foo'), sys.stdout, default_flow_style=False, Dumper=AnsibleDumper)
    yaml.safe_dump(HostVars({'foo': 'bar'}), sys.stdout, default_flow_style=False, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:30.114100
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test unicode string
    ustr = u'foo'
    assert represent_unicode(None, ustr) == "foo"



# Generated at 2022-06-22 11:30:37.207257
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'a': 'A'}

    dumper = AnsibleDumper
    # make a fake class to return from the representation function
    class FakeClass:
        tag = data
    dumper.represent_dict = lambda x: FakeClass
    assert dumper.represent_hostvars(data) == FakeClass



# Generated at 2022-06-22 11:30:41.820514
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(u'unicode_value') == u"!ansible-unicode 'unicode_value'"
    assert dumper.represent_unicode(b'bytes_value') == u"!ansible-unicode 'bytes_value'"

# Generated at 2022-06-22 11:30:49.811584
# Unit test for function represent_unicode
def test_represent_unicode():
    import string
    test_str = u''.join(c for c in string.printable if c not in string.whitespace)
    test_input = AnsibleUnicode(test_str)
    assert test_str == test_input
    output = yaml.dump(test_input, Dumper=AnsibleDumper)
    assert test_str == output.strip()

# Generated at 2022-06-22 11:30:52.431312
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import validate_filters

    validate_filters()
    yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:56.058048
# Unit test for function represent_binary
def test_represent_binary():
    d = yaml.Dumper()
    r = AnsibleDumper.represent_binary(d, b'foo\nbar')
    assert r == "!!binary |\n  Zm9vCmJhcg==\n"

# Generated at 2022-06-22 11:31:07.008101
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.compat.tests import mock
    from ansible.parsing.yaml.objects import AnsibleUnicode

    test_data = dict(
        test=AnsibleUnicode("12345"),
    )
    mock_dumper = mock.MagicMock()
    mock_dumper.represent_str.return_value = "str rep"
    mock_dumper.represent_unicode.return_value = "uni rep"

    # Test representation of regular unicode string (in python 2)
    represent_unicode(mock_dumper, "12345")
    mock_dumper.represent_str.assert_called_once()
    mock_dumper.represent_unicode.assert_not_called()

    # Test representation of an AnsibleUnicode object

# Generated at 2022-06-22 11:31:14.424174
# Unit test for function represent_binary
def test_represent_binary():
    a = b'bytes'
    b = 'unicode'
    c = yaml.YAML()
    d = AnsibleDumper()
    a1 = c.representer.represent_binary(c, a)
    a2 = d.represent_binary(a)
    assert b'!!binary' in a1, "represent_binary_test: Binary data is not preserved"
    assert b'!!binary' in a2, "represent_binary_test: Binary data is not preserved"
    assert b'\n' not in a1, "represent_binary_test: Binary data is not preserved"
    assert b'\n' not in a2, "represent_binary_test: Binary data is not preserved"
    assert b' ' not in a1, "represent_binary_test: Binary data is not preserved"

# Generated at 2022-06-22 11:31:25.960052
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-22 11:31:36.095712
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:31:37.860440
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper().represent_undefined(None) is True
    assert AnsibleDumper().represent_undefined(AnsibleUndefined) is True
    assert AnsibleDumper().represent_undefined(AnsibleUndefined('foo')) is True

# Generated at 2022-06-22 11:31:44.479280
# Unit test for function represent_undefined
def test_represent_undefined():
    # Create class with __bool__ to mimic StrictUndefined
    class TestUndefined:
        def __bool__(self):
            raise Exception('Custom exception from __bool__')

    dumper = AnsibleDumper()

    try:
        dumper.represent_data(TestUndefined())
    except Exception as ex:
        assert str(ex) == 'Custom exception from __bool__'
    else:
        assert False, 'Exception was not raised'

# Generated at 2022-06-22 11:31:46.354458
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert not dumper.represent_undefined(AnsibleUndefined())

# Generated at 2022-06-22 11:31:56.482509
# Unit test for function represent_binary
def test_represent_binary():
    # Testing a single byte to ensure that leading zero bytes are not stripped.
    # See https://github.com/ansible/ansible/pull/51646 for more details.
    b = b'\x00'
    dumper = AnsibleDumper
    result = dumper.represent_scalar(yaml.resolver.BaseResolver.DEFAULT_SCALAR_TAG, b, style='|')
    assert result == u'|-\n  !!binary |-\n    AA==\n'

# Generated at 2022-06-22 11:32:03.568636
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    class _Representer(AnsibleDumper):
        pass
    _representer = _Representer()
    result = _Representer.represent_vault_encrypted_unicode(_representer, AnsibleVaultEncryptedUnicode('dummy'))
    assert isinstance(result, yaml.representer.ScalarNode)
    assert result.value == '!vault'
    # The actual encrypted value is lost, hence the comparison below
    assert result.style == '|'

# Generated at 2022-06-22 11:32:07.208977
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(AnsibleUnsafeText(b'abc'), Dumper=AnsibleDumper, default_flow_style=True) == "!!binary \"YWJj\"\n"



# Generated at 2022-06-22 11:32:09.254826
# Unit test for function represent_undefined
def test_represent_undefined():
    a = AnsibleUndefined()
    d = AnsibleDumper()
    assert represent_undefined(d, a) is False

# Generated at 2022-06-22 11:32:12.355207
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    yaml.load(dumper.represent_undefined(AnsibleUndefined('hello')))



# Generated at 2022-06-22 11:32:16.417954
# Unit test for function represent_unicode
def test_represent_unicode():
    data = u'some_unicode_\x75\x74\x66\x38'
    r = yaml.representer.SafeRepresenter
    assert r.represent_str(AnsibleDumper, data) == represent_unicode(AnsibleDumper, data)

# Generated at 2022-06-22 11:32:22.109848
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    # Use repr for the tuple, since it
    # can't be constructed literally with (A, B).
    assert dumper.represent_undefined(AnsibleUndefined('A', 'B')) == "(AnsibleUndefined('A', 'B'),)"


if __name__ == '__main__':
    import pytest
    pytest.main(__file__)

# Generated at 2022-06-22 11:32:26.277281
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = yaml.SafeDumper
    dumper.add_representer(
        AnsibleUndefined,
        represent_undefined,
    )
    assert yaml.dump({'test': AnsibleUndefined('foo')}, Dumper=dumper) == '{test: !error "foo"}\n'

# Generated at 2022-06-22 11:32:32.272850
# Unit test for function represent_hostvars
def test_represent_hostvars():
    v = AnsibleDumper().represent_hostvars(HostVars(
        groups=['group1', 'group2'],
        hostvars=dict(
            host1=dict(
                var1=5
            ),
            host2=dict(
                var2=6
            )
        )
    ))

    assert v == """{groups: [group1, group2], hostvars: {host1: {var1: 5}, host2: {var2: 6}}}"""

# Generated at 2022-06-22 11:32:33.615573
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined('obj'), Dumper=AnsibleDumper) == ''



# Generated at 2022-06-22 11:32:40.488490
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_data(AnsibleUndefined()) == yaml.representer.SafeRepresenter.represent_none(dumper, None)

# Generated at 2022-06-22 11:32:42.720414
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(None, b'test') == (u"!binary |\n  dGVzdA==\n")

# Generated at 2022-06-22 11:32:51.117233
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Generate a random string to encrypt, decrypt and test
    from ansible.parsing.vault import VaultLib
    import os
    import base64

    vault_password = u'secret'
    vault = VaultLib(password=vault_password)
    secret = os.urandom(32)
    ciphertext = vault.encrypt(secret)
    data = AnsibleVaultEncryptedUnicode(ciphertext)
    assert u'!vault |\n          ' + base64.b64encode(ciphertext).decode() == yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:32:54.935282
# Unit test for function represent_hostvars
def test_represent_hostvars():
    for data, expected in (
        (({}, '{}'),
         ({'val1': 1}, "{'val1': 1}")),
    ):
        assert represent_hostvars(None, data) == expected

# Generated at 2022-06-22 11:32:58.516974
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    aveu = AnsibleVaultEncryptedUnicode()
    aveu._ciphertext = 'foo'
    assert represent_vault_encrypted_unicode(None, aveu) == '!vault |\n          foo\n'

# Generated at 2022-06-22 11:33:06.935239
# Unit test for function represent_binary
def test_represent_binary():
    # Represent a binary string
    result = yaml.dump(b'This is a binary string', Dumper=AnsibleDumper)
    assert result == "!!binary \"VGhpcyBpcyBhIGJpbmFyeSBzdHJpbmc=\\n\"\n"

    # Represent a binary string with non-ascii characters
    result = yaml.dump(b'\xc4\x8d\xc4\x8f\xc4\x9b', Dumper=AnsibleDumper)
    assert result == "!!binary \"x0Jce0Jfx0Js\\n\"\n"

# Generated at 2022-06-22 11:33:08.901143
# Unit test for function represent_binary
def test_represent_binary():
    binary_data = b'a\x01b'
    assert AnsibleDumper.represent_binary(binary_data) == u"!!binary |\n  YQBi\n"

# Generated at 2022-06-22 11:33:19.656362
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    yaml_out = dumper.represent_unicode('foo')
    assert yaml_out.startswith('|')
    yaml_out = dumper.represent_unicode('foo\n')
    assert yaml_out.startswith('>')
    yaml_out = dumper.represent_unicode('foo\nbar\nbaz\n')
    assert yaml_out.startswith('|')
    yaml_out = dumper.represent_unicode(u'foo\xbbbar')
    assert yaml_out.startswith('|')

    yaml_out = dumper.represent_unicode('foo')
    assert yaml_out.startswith('|')



# Generated at 2022-06-22 11:33:29.985070
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    def _check(dumper):
        data = AnsibleVaultEncryptedUnicode('foo')

# Generated at 2022-06-22 11:33:32.601696
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_undefined(AnsibleUndefined) is False

# Generated at 2022-06-22 11:33:50.621111
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml_text = "---\n- {not_defined}\n- [{ok: definition}, {not_defined}]\n- {ok: definition}\n- {ok: {def: {not_defined: definition}}}\n"
    expected_result = "---\n- {}\n- [{ok: definition}, {}]\n- {ok: definition}\n- {ok: {def: {not_defined: definition}}}\n"

    # test case: list

# Generated at 2022-06-22 11:33:52.946442
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    dumper.represent_binary(b'bytes')
    dumper.represent_binary(bytearray(b'bytearray'))

# Generated at 2022-06-22 11:33:55.665041
# Unit test for function represent_hostvars
def test_represent_hostvars():
    obj = HostVars(vars={})
    assert obj == represent_hostvars(AnsibleDumper(), obj)
    assert obj == yaml.representer.SafeRepresenter.represent_dict(AnsibleDumper(), dict(obj))

# Generated at 2022-06-22 11:34:06.840162
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import os
    import sys
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    if 'ANSIBLE_VAULT' in os.environ:
        del os.environ['ANSIBLE_VAULT']

    test_text = 'This is a test'
    test_text_bytes = test_text.encode('utf-8')

    vault_password = 'password'
    vault_password_bytes = vault_password.encode('utf-16')

    ciphertext = VaultLib(vault_password).encrypt(test_text_bytes)

    if sys.version_info[0] >= 3:
        testcase = ciphertext.encode('utf-8')
    else:
        testcase = ciphertext

   

# Generated at 2022-06-22 11:34:18.871714
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    represent_unicode()
    '''
    def __check(data):
        # First let's test that our element actually is dumped.
        output = yaml.dump(data, Dumper=AnsibleDumper)
        assert isinstance(output, text_type)
        assert u"\n" not in output

        # Then let's test that it's dumped as a scalar (not as sequence or mapping)
        stream = yaml.Stream(output.encode('utf-8'), Loader=yaml.SafeLoader)
        type(next(stream))

    # Test represent_unicode with multiple datatypes
    for data in (
        AnsibleUnicode('foo'),
        AnsibleUnsafeText('foo'),
        AnsibleUnsafeBytes(b'foo'),
    ):
        yield __check, data

# Generated at 2022-06-22 11:34:22.715574
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key4': 'value4',
            'key5': 'value5'
        }
    }
    assert '!!python/object:ansible.vars.hostvars.HostVarsVars {\n    key1: value1,\n    key2: value2,\n    key3: !!python/object:ansible.vars.hostvars.HostVarsVars {\n        key4: value4,\n        key5: value5\n    }\n}' == yaml.dump(data, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:34:26.920677
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert yaml.representer.SafeRepresenter.represent_str(dumper, u"my string") == dumper.represent_str(u"my string")
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, b"my string") == dumper.represent_binary(b"my string")

# Generated at 2022-06-22 11:34:29.409210
# Unit test for function represent_unicode
def test_represent_unicode():
    data = {u'foo': {u'bar': u'baz'}}
    assert yaml.dump(data) == '{foo: {bar: baz}}\n'



# Generated at 2022-06-22 11:34:38.921593
# Unit test for function represent_unicode
def test_represent_unicode():
    # Normal python unicode
    yaml_data = """
        key_with_normal_unicode: "a"
    """
    # Read into python structure
    yaml_data_structure = yaml.safe_load(yaml_data)
    # Dump back into YAML
    yaml_data_dump = yaml.dump(yaml_data_structure, Dumper=AnsibleDumper)
    # Should not be changed
    assert yaml_data_dump == yaml_data

    # Ansible unicode that is converted to normal python unicode
    yaml_data = """
        key_with_ansible_unicode: !ansible_unicode u"a"
    """
    # Read into python structure
    yaml_data_structure = yaml.safe_load(yaml_data)

# Generated at 2022-06-22 11:34:46.204492
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'one': 1, 'two': '2', 'three': False, 'four': [1, 2, 3]}
    output = "!!python/object/apply:ansible.parsing.yaml.objects.AnsibleMapping\n- one: 1\n- two: 2\n- three: false\n- four: [1, 2, 3]\n"  # noqa
    result = yaml.dump(data, Dumper=AnsibleDumper)
    assert output == result



# Generated at 2022-06-22 11:35:08.722833
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, b'foo') == u"!binary |-\n  Zm9v\n"
    assert dumper.represent_binary(dumper, u'foo') == u"!binary |-\n  Zm9v\n"
    assert dumper.represent_binary(dumper, 'foo') == u"!binary |-\n  Zm9v\n"

# Generated at 2022-06-22 11:35:11.451302
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    Need this to be a test because of the intentional call to _fail_with_undefined_error().
    '''
    yaml.dump({'foo': AnsibleUndefined()}, AnsibleDumper)

# Generated at 2022-06-22 11:35:13.599456
# Unit test for function represent_unicode
def test_represent_unicode():
    test_val = AnsibleUnicode(u'foo')
    yaml.representer.SafeRepresenter.represent_str(test_val)



# Generated at 2022-06-22 11:35:19.422121
# Unit test for function represent_hostvars
def test_represent_hostvars():
    host_vars = HostVars('/path/to/file')
    host_vars._vars = {'key1': 'value1', 'key2': 'value2'}

    dump = yaml.dump({'hostvars': host_vars}, Dumper=AnsibleDumper)

    expected = '{hostvars: {key1: value1, key2: value2}}\n'

    assert dump == expected

# Generated at 2022-06-22 11:35:21.305945
# Unit test for function represent_undefined
def test_represent_undefined():
    dump = yaml.dump(AnsibleUndefined())
    assert dump == ''

# Generated at 2022-06-22 11:35:27.019583
# Unit test for function represent_undefined
def test_represent_undefined():
  from ansible.template import AnsibleUndefined
  class TestClass(object):
    def __nonzero__(self):
      raise AssertionError('The yaml dumper should not try to call nonzero on '
                           'AnsibleUndefined objects')
    __bool__ = __nonzero__
  # yaml.dump should not call nonzero on TestClass
  yaml.dump(TestClass(), Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:35:30.208507
# Unit test for function represent_binary
def test_represent_binary():
    data = b'hello world'
    assert yaml.dump(data, Dumper=AnsibleDumper) == '!!binary "aGVsbG8gd29ybGQ="\n'

# Generated at 2022-06-22 11:35:34.450941
# Unit test for function represent_undefined
def test_represent_undefined():
    # Here we need to make sure that the AnsibleUndefined object is never
    # passed directly to the SafeDumper.with_undefined_representer
    try:
        yaml.dump(AnsibleUndefined(), Dumper=yaml.SafeDumper)
    except Exception as e:
        assert 'expected base10 number' in text_type(e)
    else:
        assert False, "Expected to catch an exception"

# Generated at 2022-06-22 11:35:42.156690
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('vault(9.9.9)$SOMEENCRYPTEDSTRING')
    dumper = AnsibleDumper(None)
    assert dumper.represent_scalar('!vault', data._ciphertext.decode(), style='|') == u'!vault |\n  vault(9.9.9)$SOMEENCRYPTEDSTRING\n'
    assert repr(data) == repr(u'vault(9.9.9)$SOMEENCRYPTEDSTRING')



# Generated at 2022-06-22 11:35:51.439590
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.config.data import ConfigData
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    config_data = ConfigData()
    config_data.parse()
    variable_manager = InventoryManager(loader=None, sources=['/dev/null'], variable_manager=None, all_hosts=None)
    play = Play().load({
        'name': 'test',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'action': {'module': 'debug', 'args': {'msg': b"\xfe\xff\x00\xc0"}}}
        ]
    }, variable_manager=variable_manager, loader=None)
    play._variable_manager = variable_manager
    play.post

# Generated at 2022-06-22 11:36:12.807830
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'data': HostVars(host_data={'myvar': 'mydata'})}
    # Load in and out to ensure there are no issues with hostvars
    assert yaml.load(yaml.dump(data, Dumper=AnsibleDumper)) == data



# Generated at 2022-06-22 11:36:20.514212
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    test_hostvars = HostVars(
        vault_password='V4ULT_PASSWORD',
    )

    test_hostvars._set('vault_password', 'V4ULT_PASSWORD')

    # Test actual HostVars
    assert '!vault |' in yaml.dump(dict(test_hostvars), default_flow_style=False, Dumper=AnsibleDumper)

    # Test HostVarsVars
    assert '!vault |' in yaml.dump(dict(test_hostvars['vault_password']), default_flow_style=False, Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:36:24.513935
# Unit test for function represent_hostvars
def test_represent_hostvars():
    h = {'a': 2, 'b': {'c': 3}}
    hostvars = HostVars(h)
    expected = yaml.dump(dict(hostvars))
    assert expected == yaml.dump(h, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:36:32.847029
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = yaml.dumper.SafeDumper
    dumper.add_representer(
        HostVars,
        represent_hostvars,
    )
    hostvars_data = {u'var1': u'foo', u'var2': [1, 2, 3]}
    hostvars_obj = HostVars(hostvars_data)
    output = yaml.dump(hostvars_obj, Dumper=dumper)

    assert b'&id001\nvar1: foo\nvar2:\n- 1\n- 2\n- 3\n' == output



# Generated at 2022-06-22 11:36:38.769709
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'hostvars': {'host1': {'ansible_python_interpreter': '/usr/bin/python'}}}
    output = '''hostvars: {host1: {ansible_python_interpreter: /usr/bin/python}}'''

    ansible_dumper = AnsibleDumper()
    output_from_ansible_dumper = ansible_dumper.dump(data, Dumper=AnsibleDumper)
    assert output_from_ansible_dumper == output

# Generated at 2022-06-22 11:36:44.788092
# Unit test for function represent_hostvars
def test_represent_hostvars():

    data = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    class FakeRepresenter(object):
        representers = {}

    representer = FakeRepresenter()

    assert yaml.representer.SafeRepresenter.represent_dict(representer, data) == represent_hostvars(representer, data)


# Generated at 2022-06-22 11:36:50.389945
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from io import StringIO

    test_dict = {'key1': 'value1', 'key2': 'value2'}
    output = StringIO()
    dumper = AnsibleDumper(output, default_flow_style=False)
    dumper.represent(HostVars(test_dict))
    result = output.getvalue()
    assert result == 'key1: value1\nkey2: value2\n'

# Generated at 2022-06-22 11:36:54.112415
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars()
    hv['foo'] = 'bar'
    hv._data = {'foo': 'bar'}
    assert represent_hostvars(None, hv) == represent_hostvars(None, {'foo': 'bar'})

# Generated at 2022-06-22 11:36:56.417930
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars(sources=(
        'awx',
    ))
    print(yaml.dump(hostvars, Dumper=AnsibleDumper))

# Generated at 2022-06-22 11:37:02.891575
# Unit test for function represent_hostvars
def test_represent_hostvars():

    # Setup a data structure with a simple, string key and a string value
    data = dict()
    data['hostvars'] = dict()
    data['hostvars']['localhost'] = dict()
    data['hostvars']['localhost']['ansible_connection'] = 'local'

    # Dump it using our AnsibleDumper
    output = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)

    # Assert we have the expected output
    assert output == 'hostvars:\n  localhost:\n    ansible_connection: local\n'

