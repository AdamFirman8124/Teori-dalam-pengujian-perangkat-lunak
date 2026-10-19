

# Generated at 2022-06-22 11:29:52.269936
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    secret = VaultLib().encrypt('bacon')
    vault_text = AnsibleVaultEncryptedUnicode(secret)
    loaded = yaml.load(yaml.dump(vault_text, Dumper=AnsibleDumper))
    assert loaded == vault_text

# Generated at 2022-06-22 11:30:02.423549
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import AnsibleUndefined
    from ansible.parsing.yaml.dumper import AnsibleDumper

    for data in ('string', b'bytes', AnsibleUnsafeText('ansible-unsafe'), AnsibleUnsafeBytes(b'ansible-unsafe'), AnsibleUnicode('ansible-unicode')):
        assert AnsibleDumper().represent_data(data) == data

    # Undefined value not converted to bool
    undefined = AnsibleUndefined('AnsibleUndefined')
    assert AnsibleDumper().represent_data(undefined)



# Generated at 2022-06-22 11:30:08.205654
# Unit test for function represent_undefined
def test_represent_undefined():
    # Construct a Dumper to test the representer
    dumper = AnsibleDumper()

    # Verify representer returns the correct truthy value
    assert dumper.represent_undefined(AnsibleUndefined("test", obj='something')) is False
    assert dumper.represent_undefined(AnsibleUndefined("test", sv='something')) is True

# Generated at 2022-06-22 11:30:11.922858
# Unit test for function represent_unicode
def test_represent_unicode():
    # Given
    dumper = AnsibleDumper
    s = u"Test"

    # When
    ret = dumper.represent_unicode(dumper, s)

    # Then
    assert ret == "Test"



# Generated at 2022-06-22 11:30:22.086676
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''Test represent_hostvars function'''
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml import YAMLObject

    vault_password = VaultLib()._password

    hostvars_test_obj = HostVars()
    hostvars_test_obj.add_host("test_host", {"vaulted_value": AnsibleVaultEncryptedUnicode("vaulted_value", vault_password, None)})
    hostvars_str = yaml.dump(hostvars_test_obj, Dumper=AnsibleDumper)

    # Test if Vaulted value is not in clear text
    assert "vaulted_value" not in hostvars_str

    # Test if an object of type YAMLObject is present in the yaml file
   

# Generated at 2022-06-22 11:30:31.231958
# Unit test for function represent_undefined
def test_represent_undefined():
    # None is private, hence not a public interface, so no need for backwards compatibility
    dumper = AnsibleDumper
    try:
        dumper.represent_undefined(dumper, None)
    except:
        from warnings import warn
        warn("Representer function represent_undefined is not unit tested! Please test it manually", DeprecationWarning)
        raise

# This will ensure the right dumper is used in yaml.dump
yaml.add_representer(
    AnsibleSequence,
    yaml.representer.SafeRepresenter.represent_list,
    Dumper=AnsibleDumper)

yaml.add_representer(
    AnsibleMapping,
    yaml.representer.SafeRepresenter.represent_dict,
    Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:36.288886
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    undefined = AnsibleUndefined('unittest_placeholder')
    assert not dumper.represent_undefined(dumper, undefined)


# Generated at 2022-06-22 11:30:39.970782
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    repr = represent_vault_encrypted_unicode(AnsibleDumper, AnsibleVaultEncryptedUnicode(text_type(''), text_type('')))
    assert repr == '!vault |\n          '

# Generated at 2022-06-22 11:30:46.340243
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = yaml.YAML(Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:52.003163
# Unit test for function represent_binary
def test_represent_binary():
    """
    Test that represent_binary will successfully convert all
    printable ASCII characters. PyYAML will not
    represent characters whose ordinal value is above 0x7E.
    """
    test_string = ''
    for i in range(0, 0x100):
        test_string += chr(i)
    assert yaml.dump(test_string, Dumper=AnsibleDumper, encoding=None) == test_string



# Generated at 2022-06-22 11:30:59.090936
# Unit test for function represent_undefined
def test_represent_undefined():
    # with_traceback will raise an exception
    # In the unit test, expect to see the following
    # TypeError: super(type, obj): obj must be an instance or subtype of type
    # This is due to the fact that the function represent_undefined is
    # not being called in the context of a yaml dump.
    # The with_traceback is for developer convenience and therefore
    # is not exceptioned in the unit test
    try:
        AnsibleDumper.add_representer(
            AnsibleUndefined,
            represent_undefined,
        )
    except TypeError as e:
        pass

# Generated at 2022-06-22 11:31:04.850106
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Test with a real HostVars object
    vars = HostVars(name="test")
    vars.set_variable("a", "b")
    vars.set_variable("c", "d")
    assert yaml.dump(vars, Dumper=AnsibleDumper) == '{a: b, c: d}\n'



# Generated at 2022-06-22 11:31:07.298996
# Unit test for function represent_unicode
def test_represent_unicode():
    dump = yaml.dump(["Test"], Dumper=AnsibleDumper)
    assert dump == "[Test]\n"



# Generated at 2022-06-22 11:31:13.301481
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    hostvars._data['ansible_all_ipv4_addresses'] = [u'192.168.1.10', u'192.168.1.11']
    hostvars._data['ansible_default_ipv4']['address'] = u'192.168.1.10'
    expected_result = u"[{1!: 192.168.1.10, 2: [192.168.1.10, 192.168.1.11]}]"
    result = AnsibleDumper.represent_data(hostvars)
    assert result == expected_result

# Generated at 2022-06-22 11:31:14.998384
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml.dump(dict(a=5, b=6), Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:31:26.604753
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper(None)
    value = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;userid\n63633535383330363164396235323537336134383135366335636232333136656265336437396139340a66343765303933666237636239326534383536353266633362353564383931356437393638336164623236623963363433633035626230363632616333')
    output = dumper.represent_data(value)

# Generated at 2022-06-22 11:31:36.596550
# Unit test for function represent_binary
def test_represent_binary():
    '''
    Unit test for function represent_binary
    '''
    import sys
    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO
    import yaml

    # Note: assertRaisesRegex is Python >= 3.2
    class StreamWrapper(StringIO):
        def __init__(self, stream):
            StringIO.__init__(self)
            self.stream = stream

        def close(self):
            pass

        def getvalue(self):
            return self.stream.getvalue()

    class StreamWrapperError(StringIO):
        def __init__(self, stream):
            StringIO.__init__(self)
            self.stream = stream

        def close(self):
            pass


# Generated at 2022-06-22 11:31:42.884389
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper
    x = AnsibleVaultEncryptedUnicode('abc')
    result = dumper.represent_data(x)
    assert result == u'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          61626300663738396565356532653938663330613038353634663233366534356566373033663635\n          61323531343230303637643339623239373731633539656664343139316465386538316139623338\n          3838363030626232613036\n'

# Generated at 2022-06-22 11:31:45.281155
# Unit test for function represent_binary
def test_represent_binary():
    # represent_binary should return a byte string
    dumper = AnsibleDumper()
    result = dumper.represent_binary(b'foo')
    assert isinstance(result, binary_type)



# Generated at 2022-06-22 11:31:54.927700
# Unit test for function represent_hostvars
def test_represent_hostvars():

    hostvars = HostVars(dict())
    hostvars['nested'] = HostVars(dict())
    hostvars['nested']['nested_var'] = "bar"
    hostvars['nested']['literal'] = '{{ literal }}'
    hostvars['nested']['with_space'] = 'foo bar'
    hostvars['nested']['with_quotes'] = "foo 'bar'"
    hostvars['nested']['nested'] = HostVars(dict())
    hostvars['nested']['nested']['var'] = "foo"
    hostvars['nested']['list'] = ["foo", "bar"]
    hostvars['nested']['unicode'] = u"\u0080"
    hostvars

# Generated at 2022-06-22 11:32:06.802018
# Unit test for function represent_unicode
def test_represent_unicode():
    ''' Tests that python2 and python3 unicode strings are treated the same '''
    data = {
        'as_text': AnsibleUnicode(u'my text'),
        'as_utf8': AnsibleUnicode('my text'),
        'as_native_str': AnsibleUnicode(u'my text'),
    }
    expected = {
        'as_text': 'my text',
        'as_utf8': 'my text',
        'as_native_str': 'my text',
    }
    assert yaml.safe_load(yaml.dump(data, Dumper=AnsibleDumper)) == expected



# Generated at 2022-06-22 11:32:09.534342
# Unit test for function represent_unicode
def test_represent_unicode():
    result = yaml.dump(dict(foo='bar'), Dumper=AnsibleDumper)
    assert result.endswith('foo: bar\n'), result
    assert isinstance(result, text_type)

# Generated at 2022-06-22 11:32:17.213960
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test string without any non-ascii character
    value = '{"hello": "world"}'
    dumper = yaml.dumper.SafeDumper

    # unicode value is returned as it is
    assert represent_unicode(dumper, "foo") == "foo"
    # Non-ascii values are returned as quoted strings
    assert represent_unicode(dumper, value) == "\"{\\\"hello\\\": \\\"world\\\"}\""

# Generated at 2022-06-22 11:32:22.898645
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'hostvars': {'hostname': 'hostname',
                         'inventory_hostname_short': 'inventory_hostname_short',
                         'group_names': ['group_names']}}

    hostvars = HostVars(data=data)
    yaml.safe_dump(hostvars, sys.stdout, default_flow_style=False, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:32:26.059251
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode(u"This is a string\nwith a newline")
    assert represent_unicode(None, data) == "This is a string\nwith a newline\n"

# Generated at 2022-06-22 11:32:34.291794
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    Run a unit test against the function represent_unicode
    '''

    # Create a AnsibleDumper object with default values
    # and the custom representers we added earlier
    dumper = AnsibleDumper()

    # Create a test string object to test the function
    ansible_unicode = AnsibleUnicode(u'This is a test of AnsibleUnicode')

    # Try dumping the test string with our dumper
    try:
        result = dumper.represent_data(ansible_unicode)
    except:
        raise

    # Ensure everything worked as expected
    assert result == 'This is a test of AnsibleUnicode'

# Generated at 2022-06-22 11:32:38.607716
# Unit test for function represent_hostvars
def test_represent_hostvars():
    datastruct = {'ansible_host': '1.2.3.4', 'ansible_connection': 'local'}
    assert represent_hostvars(AnsibleDumper, HostVars({'ansible_one': 'one'}, datastruct, datastruct)) == {'ansible_one': 'one', 'ansible_host': '1.2.3.4', 'ansible_connection': 'local'}

# Generated at 2022-06-22 11:32:49.501615
# Unit test for function represent_hostvars
def test_represent_hostvars():

    hv = HostVars({"foo": "bar"})
    assert AnsibleDumper.represent_hostvars(None, hv) == "!!python/object/apply:ansible.parsing.yaml.objects.AnsibleMapping {'foo': 'bar'}"

    hvv = HostVarsVars({"foo": "bar"})
    assert AnsibleDumper.represent_hostvars(None, hvv) == "!!python/object/apply:ansible.parsing.yaml.objects.AnsibleMapping {'foo': 'bar'}"

    hvvars = VarsWithSources({"foo": "bar"})

# Generated at 2022-06-22 11:33:00.540650
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test string
    ansible_string = AnsibleUnicode('foo\nbar')
    assert yaml.dump(ansible_string, Dumper=AnsibleDumper) == 'foo\\nbar\n'
    # Test bytes string
    ansible_bytes = AnsibleUnicode(b'foo\nbar')
    assert yaml.dump(ansible_bytes, Dumper=AnsibleDumper) == 'foo\\nbar\n'
    # Test None
    ansible_none = AnsibleUnicode(None)
    assert yaml.dump(ansible_none, Dumper=AnsibleDumper) == 'null\n'
    # Test bool
    ansible_true = AnsibleUnicode(True)

# Generated at 2022-06-22 11:33:04.589103
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = yaml.SafeDumper
    assert represent_hostvars(dumper, {'a': 'b', 'c': 'd'}) == \
        yaml.representer.SafeRepresenter.represent_dict(dumper, {'a': 'b', 'c': 'd'})

# Generated at 2022-06-22 11:33:11.406596
# Unit test for function represent_binary
def test_represent_binary():
    b = AnsibleDumper.represent_binary( bytearray([1,2,10]) )
    assert b =="!!binary SGkh\n"

# Generated at 2022-06-22 11:33:20.153491
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.common.yaml import dumps
    from ansible.module_utils.six import PY2
    if PY2:
        # PY2 does not have the default base64 encoder for bytes so
        # we need to explicitly define it here
        from base64 import b64encode
    foo = b'\x12\x34\x56'
    result = dumps(foo)
    if PY2:
        expect = "!!binary |\n  " + b64encode(foo)
    else:
        expect = "!!binary |\n  " + foo.decode()
    assert result == expect

# Generated at 2022-06-22 11:33:24.015480
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(
        None, binary_type(b'\x01\x02\n')
    ) == ('|\n  AQAD\n', (4, 4))

# Generated at 2022-06-22 11:33:29.905457
# Unit test for function represent_binary
def test_represent_binary():
    def generate_tests(self):
        for test_val in (u'abcd', b'abcd'):
            yield test_val

    for val in generate_tests(None):
        assert yaml.dump(val, Dumper=AnsibleDumper) == '!!binary |\n  ' + u'YWJjZA=='
        assert yaml.dump(val, Dumper=AnsibleDumper, encoding='utf-8') == '!!binary |\n  ' + u'YWJjZA=='

# Generated at 2022-06-22 11:33:37.254514
# Unit test for function represent_binary
def test_represent_binary():
    class TestStruct:
        def __init__(self, datavalue):
            self.datavalue = datavalue

        def __bytes__(self):
            return binary_type(self.datavalue)

    dp = AnsibleDumper
    a = TestStruct('Testing')
    d = yaml.dump(a, Dumper=dp)
    assert d == "!!binary |-\n  VGVzdGluZw==\n", "b64encode failed"

# Generated at 2022-06-22 11:33:47.930975
# Unit test for function represent_binary
def test_represent_binary():
    data = 'hello ansible'
    expected = u'|\n  aGVsbG8gYW5zaWJsZQ==\n'

    a = yaml.representer.SafeRepresenter()
    a.represent_binary = represent_binary
    p = yaml.representer.Representer()

    assert a.represent_data(None) == p.represent_data(None)
    assert a.represent_data(42) == p.represent_data(42)
    assert a.represent_data(42.0) == p.represent_data(42.0)
    assert a.represent_data([3, 4]) == p.represent_data([3, 4])
    assert a.represent_data({1: 2}) == p.represent_data({1: 2})

# Generated at 2022-06-22 11:33:51.232240
# Unit test for function represent_binary
def test_represent_binary():
    binary_data = AnsibleUnsafeBytes(b'\x00\x01')
    dumper = yaml.SafeDumper()
    AnsibleDumper.add_representer(AnsibleUnsafeBytes, represent_binary)
    assert dumper.represent_data(binary_data) == dumper.represent_binary(binary_data)

# Generated at 2022-06-22 11:33:56.224519
# Unit test for function represent_binary
def test_represent_binary():
    '''
    Test represent_binary function
    '''

    dumper = yaml.Dumper(width=4096)
    data = AnsibleUnsafeBytes(b'asdf\x00zxcv')
    result = yaml.representer.SafeRepresenter.represent_binary(dumper, data)
    assert result == "!!binary |\n  YXNkZoA8enhjdg=="



# Generated at 2022-06-22 11:34:07.139445
# Unit test for function represent_binary
def test_represent_binary():

    dumper = AnsibleDumper(indent=4, width=700)

    # Simple byte string
    assert u'!binary |\n    aGVsbG8=\n' == dumper.represent_binary(b'hello').decode('utf-8')

    # Byte string with newlines
    assert u'!binary |-\n    aGVs\n    bG8=\n' == dumper.represent_binary(b'hel\nb\no').decode('utf-8')

    # Byte string with unicode
    try:
        # This fails because it uses binary_type
        assert u'!binary |\n    aGVsbG8=\n' == dumper.represent_binary("hello").decode('utf-8')
    except UnicodeDecodeError:
        assert True

    # Pretty simple unic

# Generated at 2022-06-22 11:34:09.537102
# Unit test for function represent_binary
def test_represent_binary():
    yaml.dump(b"aaa", sys.stdout, Dumper=AnsibleDumper, default_flow_style=False)


if __name__ == "__main__":
    import sys
    sys.modules['__main__'].__dict__.update(globals())
    import doctest
    doctest.testmod()