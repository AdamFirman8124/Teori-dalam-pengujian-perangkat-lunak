

# Generated at 2022-06-22 11:29:51.277642
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(host=dict(hostvars=dict(a=1)))

    if data != {'a': 1}:
        raise AssertionError('test_represent_hostvars: represent_hostvars test failed. Expected {\'a\': 1}, got %s' % data)



# Generated at 2022-06-22 11:29:55.322058
# Unit test for function represent_unicode
def test_represent_unicode():
    string = 'foo'
    assert represent_unicode(AnsibleDumper(on_unset_format='strict'), string) == \
        yaml.representer.SafeRepresenter.represent_str(AnsibleDumper(on_unset_format='strict'), text_type(string))



# Generated at 2022-06-22 11:30:00.346809
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    result = dumper.represent_unicode(u'foo')
    assert result == 'foo'
    result = dumper.represent_unicode(u'foo\nbar')
    assert result == "|-\n  foo\n  bar"
    result = dumper.represent_unicode(u'foo\nbar\n')
    assert result == "|-\n  foo\n  bar"
    result = dumper.represent_unicode(u'')
    assert result == ''
    result = dumper.represent_unicode(u'\n')
    assert result == "|-\n  \n  "
    result = dumper.represent_unicode(u'\n\n')
    assert result == "|-\n  \n  \n  "

# Generated at 2022-06-22 11:30:11.438553
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from base64 import b64encode

    vault = VaultLib([])
    ciphertext = b64encode(vault.encrypt(b'A' * 16))

    aveu = AnsibleVaultEncryptedUnicode(ciphertext)
    value = aveu._ciphertext.decode()

    dump = yaml.dump(aveu, default_flow_style=False, Dumper=AnsibleDumper)

    assert dump == '!vault |\n          %s\n' % value


# Generated at 2022-06-22 11:30:21.724297
# Unit test for function represent_unicode
def test_represent_unicode():
    """
    AnsibleDumper.represent_unicode()
    """
    from ansible.parsing.yaml.loader import AnsibleLoader
    from sys import version_info

    data = {'a': {'b': {'c': 'hello'}}}
    yaml_data = yaml.dump(data, default_flow_style=False)

    ansible_data = yaml.load(yaml_data, Loader=AnsibleLoader)

    # Python3 returns a different object type
    # depending on how the data is loaded.
    if version_info < (3,):
        assert isinstance(ansible_data['a']['b']['c'], AnsibleUnicode)

# Generated at 2022-06-22 11:30:30.152717
# Unit test for function represent_binary
def test_represent_binary():
    try:
        import yaml
        yaml.__with_libyaml__ = True
    except ImportError:
        yaml = None
    if yaml is None:
        return

    dumper = yaml.SafeDumper
    assert yaml.dump(binary_type(b'hello world'), Dumper=dumper, encoding=None) == 'hello world\n...\n'
    assert yaml.dump(binary_type(b'hello world'), Dumper=AnsibleDumper, encoding=None) == '!!binary |\n  aGVsbG8gd29ybGQK\n'


if __name__ == '__main__':
    test_represent_binary()

# Generated at 2022-06-22 11:30:35.419905
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined, Dumper=AnsibleDumper) == ''
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper) == ''
    assert yaml.dump(AnsibleUndefined, default_flow_style=True, Dumper=AnsibleDumper) == ''
    assert yaml.dump(AnsibleUndefined(), default_flow_style=True, Dumper=AnsibleDumper) == ''



# Generated at 2022-06-22 11:30:46.220517
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    if yaml.__with_libyaml__:
        # This is a regression test for the issue #18021
        # AnsibleVaultEncryptedUnicode has different __len__
        # when native vs pure python loader is used
        # see https://bitbucket.org/xi/libyaml/issues/4/
        enc_data = AnsibleVaultEncryptedUnicode("test")

# Generated at 2022-06-22 11:30:56.910154
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    ansible_dumper = AnsibleDumper
    yaml_formatter = yaml.representer.SafeRepresenter()

# Generated at 2022-06-22 11:31:07.038263
# Unit test for function represent_binary
def test_represent_binary():

    # yaml.representer.SafeRepresenter.add_representer(bytes, represent_binary)
    yaml.add_representer(bytes, represent_binary)
    yaml.add_representer(str, represent_unicode)

    #print(yaml.dump("aabb")) # --- aabb
    #print(yaml.dump(b"aabb"))  # Traceback (most recent call last):
    #print(yaml.dump("aabb", Dumper=yaml.Dumper))
    print(yaml.dump("aabb", Dumper=yaml.Dumper, default_style='"'))
    print(yaml.dump(b"aabb", Dumper=yaml.Dumper, default_style='"'))

# Generated at 2022-06-22 11:31:15.336605
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    host_vars = HostVars(
        inventory=None,
        loader=None,
        hostname='host',
        variables=dict(a='foo', b='bar', c=dict(d='baz'), e=['f', 'g', 'h'])
    )
    host_vars_dict = dict(host_vars)
    yaml_string = yaml.dump(host_vars_dict, Dumper=AnsibleDumper, default_flow_style=False, allow_unicode=True)

# Generated at 2022-06-22 11:31:25.074711
# Unit test for function represent_unicode
def test_represent_unicode():
    assert AnsibleDumper.represent_scalar('tag:yaml.org,2002:str', 'foo') == ('foo', False)
    assert AnsibleDumper.represent_scalar('tag:yaml.org,2002:str', u'foo') == ('foo', False)
    try:
        assert AnsibleDumper.represent_scalar('tag:yaml.org,2002:str', AnsibleUnicode('foo')) == ('foo', False)
    except AssertionError:
        assert AnsibleDumper.represent_scalar('tag:yaml.org,2002:str', AnsibleUnicode('foo')) == (u'foo', False)

# Generated at 2022-06-22 11:31:27.881980
# Unit test for function represent_undefined
def test_represent_undefined():
    representer = AnsibleDumper.yaml_representers[AnsibleUndefined]
    assert representer(AnsibleDumper, AnsibleUndefined())



# Generated at 2022-06-22 11:31:30.174414
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('test'), Dumper=AnsibleDumper) == "test\n..."



# Generated at 2022-06-22 11:31:38.871020
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(
        HostVarsVars({
            'a': '1',
            'b': '2',
            'c': '3',
        })
    )
    assert(yaml.dump(data, Dumper=AnsibleDumper) == 'a: 1\nb: 2\nc: 3\n')

    data = VarsWithSources(
        HostVarsVars({
            'a': '1',
            'b': '2',
            'c': '3',
        })
    )
    assert(yaml.dump(data, Dumper=AnsibleDumper) == 'a: 1\nb: 2\nc: 3\n')



# Generated at 2022-06-22 11:31:41.639713
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    assert isinstance(AnsibleDumper.represent_binary(AnsibleDumper, b'bab\x00ab\x00a'), yaml.ScalarNode)


# Generated at 2022-06-22 11:31:45.904023
# Unit test for function represent_binary
def test_represent_binary():
    # function tested by TestYaml.test_yaml_unsafe_strings

    # Test that represent_binary does not raise exception on a unicode string
    try:
        represent_binary(AnsibleDumper, u'unicode')
    except:
        raise Exception("Unexpected exception")



# Generated at 2022-06-22 11:31:54.416343
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''
    hostvars is associated with the HostVarsVars class and is initialized into
    an empty dictionary, as such, we use the data and logic from our previous
    unit test to validate that the hostvars representation looks as expected.
    '''
    h = HostVars(loader=None)
    hv = HostVarsVars(host=h, variables={'key': 'value'}, loader=None)
    h.vars = hv

    output = yaml.dump(h, Dumper=AnsibleDumper, default_flow_style=False)
    assert output == "vars:\n  key: value\n"



# Generated at 2022-06-22 11:32:01.331084
# Unit test for function represent_undefined
def test_represent_undefined():
    data = {'foo': AnsibleUndefined}
    # Here we expect that exception should be raised
    # so pytest can check it
    expected_result = """Failed to compile Jinja template: expected token
'my_string', got 'undefined'"""

    with pytest.raises(AnsibleError, match=expected_result):
        yaml.dump(data, Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:32:10.905735
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Setup
    test_obj = HostVarsVars(
        name = u'sample_host',
        variables = {
            u'var1': {
                u'value': u'value1',
                u'state': u'present',
                u'variable': u'var1',
                u'key': u'var1',
                u'host': u'sample_host'
                },
            u'var2': {
                u'value': u'value2',
                u'state': u'present',
                u'variable': u'var2',
                u'key': u'var2',
                u'host': u'sample_host'
                },
            }
        )

    # Test 1: Make sure that the representer is picking up the right type
    # and returning the right thing.
   

# Generated at 2022-06-22 11:32:16.464069
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'n\x07\x1e\x1c') == 'n\\x07\\x1e\\x1c'

# Generated at 2022-06-22 11:32:25.765952
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.manager import VarsWithSources
    from ansible.vars.hostvars import HostVars, HostVarsVars
    a = AnsibleMapping(
        {'a': 'b'},
        hostvars=HostVars({'host1': {'a': 'b'}}),
        vars_with_sources=VarsWithSources(vars={'a': 'b'})
    )

    b = AnsibleMapping({'a': 'b'})

    assert yaml.dump(a, Dumper=AnsibleDumper) == yaml.dump(b)



# Generated at 2022-06-22 11:32:34.638575
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    rep = AnsibleDumper.represent_vault_encrypted_unicode
    result = rep(None, AnsibleVaultEncryptedUnicode('This is a secret'))
    assert(result == '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          343866653163383661623533386166313663616332633566663530653639653733363466373431\n          30663538376632636536616132626139343431660a363332653737363466313036373461616161\n          373834653534653530336466666565393530663539323662646539396433363638666337613662\n          3364383538650a')


# Unit

# Generated at 2022-06-22 11:32:39.188676
# Unit test for function represent_binary
def test_represent_binary():
    e = {u'b': b'hello world'}
    data = yaml.dump(e, Dumper=AnsibleDumper)
    assert data == "b: !!binary |-\n  aGVsbG8gd29ybGQ=\n"



# Generated at 2022-06-22 11:32:41.778330
# Unit test for function represent_binary
def test_represent_binary():
    yaml_rep = AnsibleDumper.represent_binary(None, b'foo ')
    assert yaml_rep == 'foo%20'

# Generated at 2022-06-22 11:32:51.350193
# Unit test for function represent_binary
def test_represent_binary():
    from io import BytesIO
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    class TestDumper(object):
        def represent_binary(self, binary):
            return BytesIO(binary)
    dumper = TestDumper()

    data = b'123'
    expected = BytesIO(data)

    mock_binary_type = MagicMock()
    mock_binary_type.return_value = data
    with patch('ansible.utils.yaml.dumper.binary_type', mock_binary_type):
        result = represent_binary(dumper, data)
        mock_binary_type.assert_called_with(data)

    assert result == expected

# Generated at 2022-06-22 11:33:02.039993
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:33:05.866048
# Unit test for function represent_undefined
def test_represent_undefined():
    # Here bool will ensure _fail_with_undefined_error happens
    # if the value is Undefined.
    # This happens because Jinja sets __bool__ on StrictUndefined
    assert bool(represent_undefined(yaml.Dumper, object())) is False

# Generated at 2022-06-22 11:33:11.760334
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml.representer.SafeRepresenter.add_representer(
        AnsibleUnicode,
        represent_unicode,
    )
    data = AnsibleUnicode(u'some unicode data')
    s = yaml.safe_dump(data, default_flow_style=False)
    assert s == 'some unicode data\n'



# Generated at 2022-06-22 11:33:19.112622
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    undefined = AnsibleUndefined('some_undefined_value')
    assert bool(undefined) == True
    # Here we need to provide some value so that represent_undefined
    # will be used, otherwise the default yaml.representer.SafeRepresenter
    # would be used, which always returns the actual value.
    # This is a good thing, because we want the final output to be
    # ``some_undefined_value``
    # To do this, we need to make sure that _fail_with_undefined_error
    # happens, because only _fail_with_undefined_error will cause
    # represent_undefined to return undefined value.
    data = dumper.represent_data(undefined)
    assert data is undefined

# Generated at 2022-06-22 11:33:25.637012
# Unit test for function represent_undefined
def test_represent_undefined():
    try:
        AnsibleDumper.default_flow_style = True
        yaml.dump({'test': AnsibleUndefined(fail_on_undefined=True)}, AnsibleDumper)
    except Exception as e:
        if e.args[0] == '> test: foo':
            pass
        else:
            raise e

# Generated at 2022-06-22 11:33:32.105014
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:33:38.430512
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    templar = Templar(loader=None, variables={})
    assert yaml.dump([templar._fail_with_undefined_error(AnsibleUnsafeText('{{ foo }}'))], Dumper=AnsibleDumper) == "['{{foo}}': 'VARIABLE IS NOT DEFINED!']\n"

# Generated at 2022-06-22 11:33:46.716169
# Unit test for function represent_undefined
def test_represent_undefined():
    ansible_dumper = AnsibleDumper(None, None, None)
    ansible_undefined = AnsibleUndefined()

    class FakeClass():
        pass

    assert bool(ansible_dumper.represent_undefined(ansible_undefined)) is False
    assert ansible_dumper.represent_undefined(FakeClass()) == yaml.representer.SafeRepresenter.represent_undefined(ansible_dumper, FakeClass())
    assert ansible_dumper.represent_undefined(FakeClass()) == yaml.representer.SafeRepresenter.represent_undefined(ansible_dumper, FakeClass())

# Generated at 2022-06-22 11:33:54.741696
# Unit test for function represent_unicode
def test_represent_unicode():
    """Make sure that AnsibleUnicode objects are properly dumped."""
    my_unicode = AnsibleUnicode(u"Foo Bar Baz")
    dumped = yaml.dump([my_unicode], Dumper=AnsibleDumper)
    assert dumped == "- Foo Bar Baz\n"

    # Also test with a normal Unicode object.
    my_unicode = text_type(u"Foo Bar Baz")
    dumped = yaml.dump([my_unicode], Dumper=AnsibleDumper)
    assert dumped == "- Foo Bar Baz\n"



# Generated at 2022-06-22 11:34:02.543014
# Unit test for function represent_unicode
def test_represent_unicode():
    d = AnsibleDumper()
    data = 'foo'
    result = d.represent_unicode(data)
    # Verify that the output is of type str
    assert isinstance(result, str)
    # Verify that the output is an inline scalar
    assert result.startswith('!python/unicode \'') and result.endswith('\'')
    # Verify that no newlines or other escape characters are present
    assert '\\' not in result



# Generated at 2022-06-22 11:34:09.762724
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('hello'), Dumper=AnsibleDumper) == 'hello\n...\n'
    assert yaml.dump(AnsibleUnicode(u'hola'), Dumper=AnsibleDumper) == 'hola\n...\n'
    assert yaml.dump(AnsibleUnicode(u'hello\nworld'), Dumper=AnsibleDumper) == "hello\nworld\n...\n"

# Generated at 2022-06-22 11:34:19.496842
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    ansible_yaml_dumper = AnsibleDumper
    data = AnsibleVaultEncryptedUnicode(u'this is vault encrypted data')
    result = ansible_yaml_dumper.represent_vault_encrypted_unicode(ansible_yaml_dumper, data)
    assert result == '!vault |\n  AQAAAM5UAAAAAwAAAADIG0cB5gchAE2QCiH0ZAyx6xaVTH6WXUZcV63nSj\n  /7mW8/ybV7f4n4vxVlPW8AvdtY/PlP/oDw==\n'



# Generated at 2022-06-22 11:34:26.458758
# Unit test for function represent_unicode
def test_represent_unicode():

    # Basic test
    test_data = 'string'
    test_obj = AnsibleUnicode(test_data)
    assert represent_unicode(yaml.representer.SafeRepresenter(), test_obj) == yaml.representer.SafeRepresenter.represent_str(yaml.representer.SafeRepresenter(), test_data)

    # Test with unsafe proxy object
    test_data = 'string'
    test_obj = AnsibleUnsafeText(test_data)
    assert represent_unicode(yaml.representer.SafeRepresenter(), test_obj) == yaml.representer.SafeRepresenter.represent_str(yaml.representer.SafeRepresenter(), test_data)

    # Test with bytes
    test_data = b'string'
    test_obj = AnsibleUnicode(test_data)
   

# Generated at 2022-06-22 11:34:33.212722
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    data = AnsibleUnicode(u'foo')

    # This should not happen as there is a representer for AnsibleUnicode
    assert dumper.represent_data(data) == u'? foo\n'

    # This should happen as we defined a new representer for AnsibleUnicode
    assert dumper.represent_data(data) == u"'foo'\n"



# Generated at 2022-06-22 11:34:43.011983
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    v = AnsibleVaultEncryptedUnicode('mysecret')
    # All of the following should be valid:
    assert represent_vault_encrypted_unicode(AnsibleDumper(), v) == '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          62386235386435663562346361346035373430653739383766356262336238343630626236326533\n          63346365656461303036663534646634366465353364663830646530343663383935646461363364\n          323432376130613062326564623236\n'
    assert represent_vault_encrypted_unicode(AnsibleDumper(default_flow_style=True), v)

# Generated at 2022-06-22 11:34:45.806510
# Unit test for function represent_unicode
def test_represent_unicode():
    data = u'Hello World'
    dumper = AnsibleDumper
    result = dumper.represent_unicode(dumper, data)
    assert result == u'Hello World\n'

# Generated at 2022-06-22 11:34:50.117424
# Unit test for function represent_hostvars
def test_represent_hostvars():
    h = HostVars({"foo": "bar"})
    assert AnsibleDumper().represent_hostvars(h) == '''{foo: bar}'''

    h = HostVarsVars({"foo": "bar"})
    assert AnsibleDumper().represent_hostvars(h) == '''{foo: bar}'''

# Generated at 2022-06-22 11:34:55.640583
# Unit test for function represent_unicode
def test_represent_unicode():
    value = AnsibleUnicode(u'SAS')

    # Unit test for function yaml_dumps
    def yaml_dumps():
        yaml.dump(value, Dumper=AnsibleDumper, default_flow_style=False)

    assert yaml_dumps() == u'"SAS"'



# Generated at 2022-06-22 11:35:05.168872
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Create AnsibleUnicode object
    mystr = AnsibleUnicode('this is a test')
    mydict = dict()
    mydict['mystr'] = mystr
    myhostvar = HostVars(mydict)
    # Call function represent_hostvars with myhostvar object
    ansible_dumper_obj = AnsibleDumper()
    result = ansible_dumper_obj.represent_hostvars(myhostvar)
    # Compare result with expected result
    expected_result = ansible_dumper_obj.represent_dict(mydict)
    assert (result == expected_result)

# Generated at 2022-06-22 11:35:09.808528
# Unit test for function represent_unicode
def test_represent_unicode():
    input_value = "\u1234"
    expected = "!ansible_unicode '\\u1234'"
    ansible_dumper = AnsibleDumper
    actual = ansible_dumper.represent_unicode(ansible_dumper, input_value)
    assert actual == expected


# Generated at 2022-06-22 11:35:18.346973
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.loader import AnsibleLoader

    dumper = AnsibleDumper
    dumper.ignore_aliases = lambda *args: True

    hostvars = HostVars(hostvars=dict(foo="bar", baz=42))
    data = yaml.dump(hostvars, Dumper=dumper)
    data2 = yaml.dump(dict(hostvars), Dumper=dumper)
    assert data == data2

    data = yaml.dump(dict(foo="bar", baz=42), Dumper=dumper)

    # Ensure we did not modify the default yaml.loader
    assert isinstance(yaml.loader.Loader, yaml.loader.SafeLoader)

    # Ensure we can restore the original dumper and still dump ansible objects

# Generated at 2022-06-22 11:35:23.258929
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(explicit_start=True, explicit_end=True)
    dumped = dumper.represent_data(AnsibleUndefined)
    assert dumped == '!!python/object/apply:ansible.template.AnsibleUndefined []\n'

# Generated at 2022-06-22 11:35:29.954249
# Unit test for function represent_binary
def test_represent_binary():
    import sys

    class mystr(str):
        def __init__(self, data):
            self.data = data

    if sys.version_info < (3,):
        assert "!binary |-\n  Zg==" == yaml.dump(mystr(u'f'), Dumper=AnsibleDumper)
    else:
        assert "!binary |-\n  Zg==" == yaml.dump(mystr('f'), Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:35:32.472874
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'123', Dumper=AnsibleDumper) == b"'123'\n"



# Generated at 2022-06-22 11:35:39.537010
# Unit test for function represent_hostvars
def test_represent_hostvars():
    """
    :param self:
    :param data:
    :return:
    >>> represent_hostvars(SafeDumper, HostVars())
    '{}\\n'
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-22 11:35:45.169031
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    result = dumper.represent_binary(dumper, b"\xEF\xBB\xBF")
    assert (result == u'!!binary "\\xEF\\xBB\\xBF"')



# Generated at 2022-06-22 11:35:48.621029
# Unit test for function represent_binary
def test_represent_binary():
    d = AnsibleDumper(None)
    assert d.represent_binary(b"0xFAFBFC") == "!!binary |-\n  MHgxRkFCRkND\n\n"

# Generated at 2022-06-22 11:35:50.848924
# Unit test for function represent_binary
def test_represent_binary():
    assert represent_binary(AnsibleDumper, 'hello\n') == u"!binary |-\n  aGVsbG8K"

# Generated at 2022-06-22 11:35:58.290243
# Unit test for function represent_hostvars
def test_represent_hostvars():
    datastruct = {"key1": "value1"}
    expected_result = "!!python/object/apply:ansible.vars.manager.VarsWithSources [0, [['hostvars', '/home/user/filename.yml']], {'key1': 'value1'}]\n"
    hostvars = HostVars(datastruct)
    result = yaml.dump(hostvars, Dumper=AnsibleDumper, default_flow_style=False)
    assert result == expected_result

# Generated at 2022-06-22 11:36:01.755448
# Unit test for function represent_binary
def test_represent_binary():
    data = b'ABC123'
    assert AnsibleDumper(None, None, None).represent_binary(data) == u'!!binary |\n  QUJDMTIz\n'



# Generated at 2022-06-22 11:36:11.684396
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.module_utils.common.yaml import AnsibleDumper
    hv = HostVars(
        source='/a/b',
        data={'a': 1, 'b': 2}
    )
    assert 'source: /a/b' in yaml.dump(hv, Dumper=AnsibleDumper)

    vws = VarsWithSources(
        sources=[
            '/a/b',
            '/c/d',
        ],
        data={
            'e': 5,
            'f': 6
        }
    )
    assert 'sources: [/a/b, /c/d]' in yaml.dump(vws, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:36:13.592775
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(u'foo') == u'foo\n...\n'



# Generated at 2022-06-22 11:36:19.632546
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    text = u'foo'
    data = AnsibleVaultEncryptedUnicode(text, 'dummy')
    output = yaml.dump(data, Dumper=AnsibleDumper)
    assert output == '!vault |\n          Zm9v\n'
    assert output.count('\n') == 2
    assert output[:-1].count('\n') == 1

# Generated at 2022-06-22 11:36:24.722916
# Unit test for function represent_unicode
def test_represent_unicode():

    def round_trip(dumper, data):
        """ Make sure that the object survives a round trip """
        dumped = yaml.dump(data, Dumper=dumper)
        loaded = yaml.load(dumped)
        assert data == loaded

    obj = AnsibleUnicode(u'foo')
    round_trip(AnsibleDumper, obj)



# Generated at 2022-06-22 11:36:34.850333
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''represent_hostvars'''
    def check(input_data, expected_output):
        output = yaml.dump(input_data, Dumper=AnsibleDumper)
        assert output == expected_output

    test_data = {'secret_key': 's3cr3t'}
    check(HostVars(ansible_vars=test_data), 'secret_key: s3cr3t\n')

    # TODO: how to test for HostVarsVars?

# Generated at 2022-06-22 11:36:41.361561
# Unit test for function represent_hostvars

# Generated at 2022-06-22 11:36:51.946366
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.vars import Variable

    variable_manager = VariableManager()
    variable_manager.set_inventory(None)
    variable_manager.set_loader(None)

    variable_manager._fact_cache = HostVars(
        variable_manager,
        variable_manager._fact_cache._host_cache,
        variable_manager._fact_cache._host,
    )
    variable_manager._fact_cache._variable_manager = variable_manager

    variable_manager._vars_cache = HostVars(
        variable_manager,
        variable_manager._vars_cache._host_cache,
        variable_manager._vars_cache._host,
    )
    variable_manager._v

# Generated at 2022-06-22 11:36:53.707241
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump("hello") == yaml.dump(AnsibleUnicode("hello"))

# Generated at 2022-06-22 11:37:02.271328
# Unit test for function represent_hostvars
def test_represent_hostvars():

    class FakeHostVars(HostVars):
        def __init__(self, inner):
            self.inner = inner

        def __iter__(self):
            return iter(self.inner)

        def __getitem__(self, key):
            return self.inner[key]

    class FakeVarsWithSources(VarsWithSources):
        def __init__(self, inner):
            self._raw = inner

    hv = FakeHostVars({"a": "b"})
    vws = FakeVarsWithSources({"c": "d"})

    dumper = AnsibleDumper
    dumper.ignore_aliases = lambda *args: True


# Generated at 2022-06-22 11:37:06.253905
# Unit test for function represent_unicode
def test_represent_unicode():
    AnsibleDumper.add_representer(
        AnsibleUnicode,
        represent_unicode,
    )

    data = AnsibleUnicode('test_string')
    actual = yaml.dump(data, Dumper=AnsibleDumper)
    expected = "test_string\n"
    assert actual == expected

# Generated at 2022-06-22 11:37:14.207434
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import DataLoader

    loader = DataLoader()

    v = HostVars(loader, 'localhost', {})
    hv = AnsibleDumper().represent_hostvars(v)
    assert hv == '{}'

    v.data['x'] = 'y'
    hv = AnsibleDumper().represent_hostvars(v)
    assert hv == '{\n    x: y\n}'


# Generated at 2022-06-22 11:37:23.408567
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # Create a fake vault secret to test with
    secret = "SuperSecret"

    # Create a fake vault password
    password = "SuperPassword"

    # Create a vault object
    vault_secret = VaultSecret(secret=secret, encrypt=True)

    # Create a vault object
    ciphertext = vault_secret.encrypt(password=password)

    # Create a vault encrypted unicode object
    vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(ciphertext)

    # Create a vault object
    vault_object = VaultLib(password=password)

    # Load the secret from the vault file
    vault_secret = vault_object.load(vault_encrypted_unicode)

    # Create a

# Generated at 2022-06-22 11:37:31.940194
# Unit test for function represent_hostvars
def test_represent_hostvars():

    from ansible.vars.manager import VariableManager

    fake_host = 'fake_host'
    vm = VariableManager()

    # set a basic var
    vm.set_host_variable(fake_host, 'myvar', dict(myvar_key='myvar_value'))

    test_hostvars = HostVars(vm, fake_host)
    test_hostvars_representation = yaml.dump(test_hostvars, Dumper=AnsibleDumper, default_flow_style=False)
    assert test_hostvars_representation == """myvar:
  myvar_key: myvar_value
"""

    # set a hostvars variable
    vm.set_host_variable(fake_host, 'myhostvarsvar', dict(my_key='my_value'))

    test_

# Generated at 2022-06-22 11:37:35.248525
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # in theory, this is all we need to do to make the tests pass
    # but it's not working for some reason
    assert False

# Generated at 2022-06-22 11:37:48.392040
# Unit test for function represent_unicode
def test_represent_unicode():
    import ansible.constants as C
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnicode

    assert C.DEFAULT_VAULT_ID_MATCH == '^Vault.*$'
    assert C.DEFAULT_VAULT_ID_MATCH_ORDERED == False
    assert C.DEFAULT_YAML_VERSION == (1, 2)

    unicode_object = u'unicode str: \u2713'
    assert unicode_object == u'unicode str: \u2713'

    unicode_object = AnsibleUnicode(unicode_object)
    assert unicode_object == u'unicode str: \u2713'


# Generated at 2022-06-22 11:37:53.091834
# Unit test for function represent_undefined
def test_represent_undefined():
    test_value = AnsibleUndefined
    # We don't care much about the string value
    # we are getting, this tests that it doesn't
    # throw an exception
    yaml.safe_dump(test_value, default_flow_style=False)

# Generated at 2022-06-22 11:37:59.044374
# Unit test for function represent_unicode
def test_represent_unicode():
    d = yaml.YAML()
    d.Representer = AnsibleDumper

    yaml.dump(AnsibleUnicode('foo'), d)
    yaml.dump(AnsibleUnicode({'foo': 'bar'}), d)
    yaml.dump(AnsibleUnicode(['foo', 'bar']), d)



# Generated at 2022-06-22 11:38:04.035300
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test represent_unicode
    assert unicode == type(represent_unicode(None, 1))
    assert unicode == type(represent_unicode(None, u'test'))
    assert unicode == type(represent_unicode(None, u'\u1234'))
    assert unicode == type(represent_unicode(None, AnsibleUnicode(u'\u1234')))



# Generated at 2022-06-22 11:38:06.615097
# Unit test for function represent_hostvars
def test_represent_hostvars():
    stream = AnsibleDumper.represent_hostvars({'a': 1, 'b': 2, 'c': 3})
    assert stream is not None



# Generated at 2022-06-22 11:38:11.945306
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars(hostvars=dict(a=1, b=2))
    data = dict(hv=hv)
    dumper = AnsibleDumper
    output = yaml.dump(data, Dumper=dumper)
    assert output == 'hv: {a: 1, b: 2}\n'



# Generated at 2022-06-22 11:38:15.374593
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes(b"\x00\x01\x02\x03\x04\x05\x06\x07")
    result = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, data)
    assert result == b"!!binary |\n  AAECAwQFBgc=\n"



# Generated at 2022-06-22 11:38:19.900816
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Given
    data = AnsibleVaultEncryptedUnicode('foo')

    # When
    result = AnsibleDumper.represent_vault_encrypted_unicode(data)

    # Then
    assert result == u"!vault |\n          " + data._ciphertext.decode()



# Generated at 2022-06-22 11:38:26.770557
# Unit test for function represent_binary
def test_represent_binary():
    """
    basic test to ensure that the binary representation
    works and doesn't throw a misleading error indicating
    that v2_represent_binary was called
    """
    data = '\x00\x01\x02\x03\x04\x05\x06\x07'  # 8 zero bytes
    expected = u'!!binary |\n  AAECAwQFBgc=\n'
    dumper = AnsibleDumper
    got = dumper.represent_binary(dumper, data)
    assert got == expected

# Generated at 2022-06-22 11:38:37.395374
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    Ensure that Unicode objects can be properly dumped as YAML.

    This test is used to check that the code added to the
    ansible.parsing.yaml.objects.AnsibleUnicode class still works.

    :param AnsibleDumper dumper: Dumper instance
    :param AnsibleUnicode data: Unicode data to be dumped
    :param str result: Expected YAML representation
    :rtype: bool
    :returns: whether the test passed or not
    '''

    dumper = AnsibleDumper
    data = AnsibleUnicode('unicøde')
    result = 'unicøde\n...\n'

    # Test the represent_unicode function
    return dumper.represent_unicode(dumper, data) == result

# Generated at 2022-06-22 11:38:50.015412
# Unit test for function represent_binary
def test_represent_binary():
    # Create a dummy AnsibleDumper.
    dumper = AnsibleDumper

    # Create a AnsibleUnsafeBytes object
    data = AnsibleUnsafeBytes(b'\x84\x00\x81\x00')

    # Assert that represent_binary was called on the object.
    assert dumper.represent_data(data) == dumper.represent_binary(data)

# Generated at 2022-06-22 11:39:01.687200
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_password = 'ansible'
    v = VaultLib(vault_password)

# Generated at 2022-06-22 11:39:04.222903
# Unit test for function represent_binary
def test_represent_binary():
    assert type(yaml.representer.SafeRepresenter.represent_binary(None, b'foo')) == yaml.representer.ScalarNode



# Generated at 2022-06-22 11:39:14.007066
# Unit test for function represent_unicode
def test_represent_unicode():
    import os
    import sys

    if sys.version_info[0] < 3:
        try:
            unicode = unicode
        # pylint: disable=undefined-variable
        except:
            pass

    # unicode test
    if sys.version_info[0] < 3:
        text = unicode('Ψ')
    else:
        text = 'Ψ'

    out = yaml.dump(text, Dumper=AnsibleDumper)
    assert out == 'Ψ\n...\n'

    # byte test
    byte = os.urandom(10)
    out = yaml.dump(byte, Dumper=AnsibleDumper)
    assert out == ('{0}\n...\n'.format(byte))



# Generated at 2022-06-22 11:39:22.039711
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars()
    hv.add_host_var('host1', 'var1', 'val1')
    hv.add_host_var('host1', 'var2', 'val2')
    hv.add_host_var('host2', 'var1', 'val3')
    hv_str = '{host1: {var1: val1, var2: val2}, host2: {var1: val3}}'

    assert represent_hostvars(AnsibleDumper.add_representer, hv) == hv_str

# Generated at 2022-06-22 11:39:33.258663
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.utils.unsafe_proxy import wrap_var
    import re
    for i in [ {u'a': u'b'},
               wrap_var(u'a'),
               wrap_var(u'a'),
               {u'b': u'a', u'c': [1,2,3]} ]:
        myvar = HostVars(i)
        result = yaml.safe_dump(myvar,  default_flow_style=True, default_style=False, Dumper=AnsibleDumper)
        print (result)
        assert isinstance(result, text_type)
        assert not re.search(r'---\s*', result.strip())
        assert result.strip().startswith(u'{')
        assert result.strip().endswith(u'}')

# Generated at 2022-06-22 11:39:40.092875
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(VarsWithSources())
    data.add({"k": 12}, "some/file")
    data.add({"k2": 13}, "some/file")
    data.add({"k": 10}, "other/file")
    data.add({"k3": 11}, "other/file")
    data.add({"k4": 11}, "other/file")

    expected = """k2: 13
k: 10
k3: 11
k4: 11
"""

    assert str(expected) == yaml.dump(data, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:39:47.653206
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = yaml.load("""
---
foo:
  - bar: 123
""")
    assert isinstance(hv, dict)
    assert 'foo' in hv
    hv_obj = hv['foo']
    assert isinstance(hv_obj, list)
    assert isinstance(hv_obj[0], dict)
    assert 'bar' in hv_obj[0]
    assert hv_obj[0]['bar'] == 123
    assert yaml.dump(hv) == '---\nfoo:\n  - bar: 123\n'

