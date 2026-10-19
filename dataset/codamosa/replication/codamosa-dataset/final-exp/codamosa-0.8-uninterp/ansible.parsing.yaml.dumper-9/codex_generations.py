

# Generated at 2022-06-22 11:29:51.007037
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test case for !ansible/unicode
    # FIXME: In future we can change this to a call of represent_scalar
    #        but it will require some custom logic at the TagLoader level.
    stream = yaml.StringIO()
    yaml.safe_dump(u'hello world', stream, default_flow_style=False, Dumper=AnsibleDumper)

    assert stream.getvalue() == u'!ansible/unicode \'hello world\'\n...\n'

# Generated at 2022-06-22 11:30:00.984850
# Unit test for function represent_unicode
def test_represent_unicode():

    data = AnsibleUnicode(u'ä')
    assert type(data) == AnsibleUnicode
    assert isinstance(data, text_type)
    assert not isinstance(data, binary_type)

    # On Python 2, the type of u"unicode" is unicode
    # On Python 3, the type of u"unicode" is str
    # On Python 2, the type of b"bytes" is str
    # On Python 3, the type of b"bytes" is bytes
    # We want to make sure that the data is encoded to bytes
    dumper = AnsibleDumper()
    yaml_str = dumper.represent_unicode(data)
    assert type(yaml_str) == str
    assert isinstance(yaml_str, binary_type)

    # Now make sure the round trip to Ansible

# Generated at 2022-06-22 11:30:06.418972
# Unit test for function represent_hostvars
def test_represent_hostvars():
    v = HostVars({"a": 1, "b": 2})
    d = yaml.dump({'v': v}, Dumper=AnsibleDumper)
    assert d == ("v:\n"
                 "  a: 1\n"
                 "  b: 2\n")


# Generated at 2022-06-22 11:30:17.717448
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    loader = yaml.SafeLoader

# Generated at 2022-06-22 11:30:18.685069
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_data(AnsibleUndefined) == dumper.represent_data(AnsibleUndefined)



# Generated at 2022-06-22 11:30:23.396029
# Unit test for function represent_hostvars
def test_represent_hostvars():
    d = yaml.dump(['hi', {'a' : 1, 'b' : 'seq'}, {'a': 1, 'b': 'seq'}], Dumper=AnsibleDumper)
    assert(d == '''- hi
- a: 1
  b: seq
- {a: 1, b: seq}\n''')



# Generated at 2022-06-22 11:30:32.233587
# Unit test for function represent_binary
def test_represent_binary():
    expected = [
        ('foo', b'foo'),
        ('bar', b'bar'),
        ('baz', b'baz'),
        ('qux', b'qux'),
        ('quux', b'quux'),
        ('corge', b'corge'),
        ('grault', b'grault'),
        ('garply', b'garply'),
        ('waldo', b'waldo'),
        ('fred', b'fred'),
        ('plugh', b'plugh'),
        ('xyzzy', b'xyzzy'),
        ('thud', b'thud'),
    ]
    stream = yaml.serialize(expected)
    data = yaml.deserialize(stream)
    assert expected == data

# Unit tests for function represent_unicode

# Generated at 2022-06-22 11:30:38.487500
# Unit test for function represent_binary
def test_represent_binary():
    """ represent_binary should work like represent_str,
    but be a bit more explicit (handles binary data). """
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, b'foo\nbar\nbaz\n') == 'foo\\nbar\\nbaz\\n'

# Generated at 2022-06-22 11:30:42.636870
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars_object = HostVars(dict(name1='value1', name2='value2'))
    assert represent_hostvars(None, hostvars_object) == {'name1': 'value1', 'name2': 'value2'}



# Generated at 2022-06-22 11:30:44.586316
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    assert dumper.representer.represent_undefined(dumper, None) is True



# Generated at 2022-06-22 11:30:55.668067
# Unit test for function represent_unicode
def test_represent_unicode():
    a = AnsibleUnicode('string with unicode chars like ' + text_type('\xe9'))

    if not isinstance(text_type(a), text_type):
        raise AssertionError("a.__str__() is not text_type")
    if not isinstance(str(a), str):
        raise AssertionError("a.__unicode__() is not unicode")
    if not isinstance(binary_type(a), binary_type):
        raise AssertionError("a.__bytes__() is not bytes")
    if not isinstance(yaml.dump(a), str):
        raise AssertionError("yaml.dump(a) is not str")



# Generated at 2022-06-22 11:31:06.757539
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = yaml.SafeDumper(width=50)
    dumper.add_representer(
        AnsibleVaultEncryptedUnicode,
        represent_vault_encrypted_unicode,
    )
    ciphertext = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n" \
                 "          363038306138346161623563616138393437626663336536646338356538616562366430376266663235623\n" \
                 "          30a383335306664323563376436383137656264376261623236623339396630316430333365393364613936\n" \
                 "          66393533653037323966366164\n"
    assert dumper.represent

# Generated at 2022-06-22 11:31:14.283246
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    key = 'ansible-test'
    vault = VaultLib([key])
    text = 'test'
    encrypted_text = vault.encrypt(text)
    rep = yaml.representer.SafeRepresenter().represent_scalar(
        u'!vault', encrypted_text.decode(), style='|')
    assert rep == '!vault |\n          %s\n' % encrypted_text.decode()
    # When using the same function for dumping, it will raise TypeError
    # because data is unicode

# Generated at 2022-06-22 11:31:18.318028
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    hostvars['a'] = 1
    assert represent_hostvars(AnsibleDumper([{'x': hostvars}]), [{'x': hostvars}]) == '[{a: 1}]'


# Generated at 2022-06-22 11:31:26.866820
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Create test data
    data = HostVars()
    data['var1'] = 'a'
    data['var2'] = 'b'

    # Dump test data
    dumped = yaml.dump(data, Dumper=AnsibleDumper)
    assert dumped == '{var1: a, var2: b}\n'

    # Load dumped data
    loaded = yaml.load(dumped)
    assert isinstance(loaded, dict)
    assert loaded == {'var1': 'a', 'var2': 'b'}



# Generated at 2022-06-22 11:31:32.023501
# Unit test for function represent_unicode
def test_represent_unicode():
    # Create a dummy dumper and the data to represent
    dumper = AnsibleDumper()
    data = AnsibleUnicode(u'\u2713')
    # Make sure that data is of the correct type
    assert isinstance(data, AnsibleUnicode)
    # Make sure that it doesn't raise an exception
    assert dumper.represent_unicode(data) is not None

# Generated at 2022-06-22 11:31:38.981011
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(AnsibleDumper, AnsibleUnsafeText(u"test_{{ foo.bar }}")) == "test_{{ foo.bar }}"
    assert represent_unicode(AnsibleDumper, AnsibleUnsafeText(u"test_{{ foo.bar }}", unsafe=False)) == "test_{{ foo.bar }}"
    assert represent_unicode(AnsibleDumper, AnsibleUnsafeText(b"test_{{ foo.bar }}", unsafe=False).encode('ascii')) == "test_{{ foo.bar }}"

# Generated at 2022-06-22 11:31:40.327207
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml.safe_dump(AnsibleUndefined(''), default_flow_style=False)

# Generated at 2022-06-22 11:31:42.934842
# Unit test for function represent_hostvars
def test_represent_hostvars():
    host = HostVars(dict(name='jdoe'))
    assert represent_hostvars(None, host) == {'name': 'jdoe'}



# Generated at 2022-06-22 11:31:46.877851
# Unit test for function represent_unicode
def test_represent_unicode():
    ansible_dumper = AnsibleDumper()
    ansible_unicode = AnsibleUnicode(u'TestString')
    result = ansible_dumper.represent_unicode(ansible_unicode)
    assert result == u'TestString'



# Generated at 2022-06-22 11:32:00.890339
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    Verify that we can represent unicode objects with YAML
    '''

    string = u'test'
    assert string == yaml.dump(string, Dumper=AnsibleDumper)

    # We need to convert the string to an object because that is what
    # yaml.dump() would have done
    string_obj = AnsibleUnicode(string)
    assert string == yaml.dump(string_obj, Dumper=AnsibleDumper)

    # Test the case where we do not explicitly create an AnsibleUnicode
    # and the object is created on the fly when we use the yaml.dump()
    string = AnsibleUnicode(string)
    assert string == yaml.dump(string, Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:32:10.452011
# Unit test for function represent_hostvars

# Generated at 2022-06-22 11:32:13.646259
# Unit test for function represent_undefined
def test_represent_undefined():
    result = AnsibleDumper.represent_undefined(AnsibleDumper(None), AnsibleUndefined())
    assert not result

# Generated at 2022-06-22 11:32:24.552049
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    # unicode with width equals to 1
    u = u"\u4e00"
    assert yaml.representer.SafeRepresenter.represent_unicode(dumper, u) == yaml.representer.SafeRepresenter.represent_unicode(dumper, text_type(u))
    # unicode with width equals to 2
    u = u"\u4e42"
    assert yaml.representer.SafeRepresenter.represent_unicode(dumper, u) == yaml.representer.SafeRepresenter.represent_unicode(dumper, text_type(u))
    # unicode with width equals to 3
    u = u"\u1f620"
    assert yaml.representer.SafeRepresenter.represent_unicode(dumper, u) == yaml.represent

# Generated at 2022-06-22 11:32:32.381747
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.SafeDumper
    dumper.add_representer(binary_type, yaml.representer.SafeRepresenter.represent_binary)
    value = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    expected_output = b'!!binary |-\n  AAEBAQIDBAUGBw==\n'
    actual_output = yaml.dump(value, Dumper=dumper, encoding=None)
    assert(actual_output == expected_output)

# Generated at 2022-06-22 11:32:35.059598
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hvars = HostVars({"foo": "bar"})
    expected_output = {'foo': 'bar'}
    assert represent_hostvars(yaml.representer.SafeRepresenter(), hvars) == expected_output

# Generated at 2022-06-22 11:32:46.576672
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_txt = '$ANSIBLE_VAULT;1.2;AES256;testhost\n33373435353264323662353635373935336636643239396139616331333962643730333934383264313\n366362653639333464316466646531326131363034633733386130336162366435626366613034\n'
    vault = VaultLib(b'testpassword')
    ciphertext = vault.decrypt(vault_txt).encode('utf-8')
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:32:50.160707
# Unit test for function represent_binary
def test_represent_binary():
    bin_data = b'abc'
    repr_data = AnsibleDumper.represent_binary(bin_data)
    assert repr_data == b"!binary |-\n  YWJj\n"


# Generated at 2022-06-22 11:32:53.246971
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'\x00\xFF', Dumper=AnsibleDumper) == u'!!binary |\n  AAY+\n'

# Generated at 2022-06-22 11:33:03.204514
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n313233343536373839303132333435363738393031323334353637383930313233343536373839303132333435363738393035322d32\n343536373839303132333435363738393031323334353637383930313233343536373839303132333435363738393031323334\n")
    result = represent_vault_encrypted_unicode(None, data)

# Generated at 2022-06-22 11:33:12.342797
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test for python-2
    is_python2 = True

    # Check if this is python-2
    if not isinstance(u"", type(b"")):
        is_python2 = False

    if is_python2:
        if AnsibleUnicode(u"\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9").tag is not u'tag:yaml.org,2002:str':
            assert False, "Representer did not work"


# Generated at 2022-06-22 11:33:23.921404
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Basic test
    assert '{foo: bar, baz: 123}' == repr(yaml.safe_dump(dict(foo='bar', baz=123), Dumper=AnsibleDumper))

    # Test for HostVars object
    assert '{foo: bar, baz: 123}' == repr(yaml.safe_dump(dict(foo=HostVars({'foo': 'bar'}), baz=HostVars({'baz': 123})), Dumper=AnsibleDumper))

    # Test for HostVarsVars object
    hvv = HostVarsVars()
    hvv.vars = {'foo': 'bar'}
    hvv.vars_cache = {'foo': 'bar'}

# Generated at 2022-06-22 11:33:28.651321
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(AnsibleDumper,
                                             AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\nblahblahblahblah')) == '!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  blahblahblahblah\n'

# Generated at 2022-06-22 11:33:30.540246
# Unit test for function represent_undefined
def test_represent_undefined():
    _ = AnsibleDumper.represent_undefined(AnsibleDumper(), AnsibleUndefined('fail_with_undefined_error'))


# Generated at 2022-06-22 11:33:32.553449
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:33:43.399025
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    v = VariableManager()
    v.set_host_variable(
        host='localhost',
        varname='foo',
        value=dict(bar=[{'bam': 'baz'}])
    )
    hv = HostVars(v.data, v.vars)

    assert yaml.dump(hv, Dumper=AnsibleDumper) == '---\nlocalhost: {}\n'
    assert yaml.dump(hv['localhost'], Dumper=AnsibleDumper) == '---\nfoo: {bar: [{bam: baz}]}\n'
    assert yaml.dump

# Generated at 2022-06-22 11:33:54.449776
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
   dumper = AnsibleDumper()

# Generated at 2022-06-22 11:33:57.642024
# Unit test for function represent_undefined
def test_represent_undefined():
    def object_hook(obj):
        del obj['__bool__']
        return obj

    yaml.add_constructor(u'!undefined', object_hook)

# Generated at 2022-06-22 11:34:01.402084
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.SafeDumper
    # Note:  here the test string is converted to bytes so it may be
    #        properly tested.
    data = binary_type('!binary \'test\'\n')
    assert dumper.represent_binary(dumper, data) == data



# Generated at 2022-06-22 11:34:08.241148
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert yaml.dump(AnsibleVaultEncryptedUnicode(u'asdf'), Dumper=AnsibleDumper) == '!vault |\n  $ANSIBLE_VAULT;1.2;AES256;ansible\n  35306466316334613339383061636238313338316430393638653731323536353536376538303237\n  3366393930343765333033360a\n'

# Generated at 2022-06-22 11:34:15.236890
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes('foo')
    dumper = yaml.representer.SafeRepresenter(allow_unicode=True)
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, data) == u'!binary |\n  Zm9v\n'

# Generated at 2022-06-22 11:34:17.643015
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode(text_type('foo'))) == "foo\n..."



# Generated at 2022-06-22 11:34:22.095839
# Unit test for function represent_unicode
def test_represent_unicode():
    u = u"\u043f\u0440\u0438\u0432\u0435\u0442"
    serialized = yaml.dump(u, Dumper=AnsibleDumper, allow_unicode=True)
    assert serialized == u"{0}\n".format(u)

# Generated at 2022-06-22 11:34:32.852750
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.compat import StringIO
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleUnicode

    s = StringIO()
    dumper = AnsibleDumper(s)

    # create a HostVars object to dump
    data = HostVars()
    data['ansible_connection'] = AnsibleUnicode(u'local')
    data['ansible_user'] = AnsibleUnicode(u'root')
    data['ansible_ssh_pass'] = AnsibleUnicode(u'Vault(Vu_aL7)'
                                              u'jk==)')

    # dump the data to the StringIO
    dumper.represent_data(data)

    # read the data as a string

# Generated at 2022-06-22 11:34:35.677340
# Unit test for function represent_hostvars
def test_represent_hostvars():
    reps = yaml.representer.Representer()
    test_data = HostVars()._data
    assert represent_hostvars(reps, test_data) == reps.represent_dict(dict(test_data))



# Generated at 2022-06-22 11:34:43.018344
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import ansible.parsing.vault
    uni = 'string'
    non_encrypted_vault = ansible.parsing.vault.VaultLib([])
    non_encrypted_vault.decrypt(uni)
    ciphertext = non_encrypted_vault.encrypt(uni)
    encrypted_unicode = ansible.parsing.vault.VaultLib.deserialize(ciphertext)
    encrypted_unicode._ciphertext = ciphertext
    representation = AnsibleDumper.represent_data(encrypted_unicode)

# Generated at 2022-06-22 11:34:45.805910
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars(dict(foo='bar'))
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == 'foo: bar\n'



# Generated at 2022-06-22 11:34:55.736371
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars(dict())
    x = yaml.dump(hv, default_flow_style=False)
    assert x == '--- {}\n'

    hv.update([('a', 'b'), ('c', 'd')])
    x = yaml.dump(hv, default_flow_style=False)
    assert x == '---\n  a: b\n  c: d\n'

    hv.update({'e': 'f'})
    x = yaml.dump(hv, default_flow_style=False)
    assert x == '---\n  a: b\n  c: d\n  e: f\n'

    hv2 = HostVarsVars(dict())

# Generated at 2022-06-22 11:35:07.951070
# Unit test for function represent_undefined
def test_represent_undefined():
    # The function assert_raises takes a callable and arguments,
    # so we need to define a function which always calls represent_undefined
    # with the given data. The behavior we're testing is when represent_undefined
    # returns a boolean, which happens when the data is not an instance of
    # AnsibleUndefined.
    data = 'foo'
    call_represent_undefined = lambda: represent_undefined(None, data)

    # Test that when the data is not an instance of AnsibleUndefined,
    # represent_undefined returns a boolean value.
    assert isinstance(represent_undefined(None, data), bool)

    # Test that when the data is an instance of AnsibleUndefined,
    # represent_undefined raises an error.
    from ansible.template import StrictUndefined
    data = StrictUndefined()

# Generated at 2022-06-22 11:35:14.627986
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper(indent=0)
    hostvars = HostVars()
    hostvars['key1'] = 'value1'
    hostvars['key2'] = 'value2'

    fake_dict = dict()
    fake_dict['key1'] = 'value1'
    fake_dict['key2'] = 'value2'

    assert dumper.represent_hostvars(hostvars) == dumper.represent_dict(fake_dict)



# Generated at 2022-06-22 11:35:25.776754
# Unit test for function represent_binary
def test_represent_binary():
    import sys

    # False for py2
    assert yaml.representer.SafeRepresenter.use_binary is False
    bytes_string = b'testing for bytes'
    if sys.version_info[0] == 2:
        yaml_string = yaml.dump(bytes_string, Dumper=AnsibleDumper)
    else:
        yaml_string = yaml.dump(bytes_string, Dumper=AnsibleDumper)
        # True for py3
        assert yaml.representer.SafeRepresenter.use_binary is True

    assert yaml_string == u'!!binary |\n  dGVzdGluZyBmb3IgYnl0ZXNcbiA=\n'

    # reset use_binary to False

# Generated at 2022-06-22 11:35:30.162875
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    class DummyClass(object):
        _ciphertext = 'ciphertext'

    dumper = AnsibleDumper()
    dumper.represent_vault_encrypted_unicode(DummyClass())

if __name__ == '__main__':
    test_represent_vault_encrypted_unicode()

# Generated at 2022-06-22 11:35:41.641003
# Unit test for function represent_unicode
def test_represent_unicode():
    d = AnsibleDumper()
    # The default SafeRepresenter.represent_str uses ANSI escapes.
    # We want this to be a simple string, so we're overriding
    assert d.represent_unicode(u'\x1b[1mBold\x1b[0m') == u'Bold'
    assert d.represent_unicode(u'\x1b[1mBold') == u'\x1b[1mBold'
    assert d.represent_unicode(u'\x1b[') == u'\x1b['
    assert d.represent_unicode(u'\\x1b') == u'\\x1b'
    assert d.represent_unicode(b'\x1b[1m') == u'\x1b[1m'
    assert d.represent

# Generated at 2022-06-22 11:35:44.613721
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(None, b'\x00\x01') == "'\\x00\\x01'"



# Generated at 2022-06-22 11:35:51.816353
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml = AnsibleDumper()

    # Test with unicode string
    ansible_unicode = AnsibleUnicode(u'This is a unicode string')
    expected_output = u'this is a unicode string\n...\n'
    assert expected_output == yaml.represent_unicode(ansible_unicode)

    # Test with non-unicode string
    ansible_unicode = AnsibleUnicode(b'This is a non-unicode string')
    expected_output = u'this is a non-unicode string\n...\n'
    assert expected_output == yaml.represent_unicode(ansible_unicode)

# Generated at 2022-06-22 11:35:57.615230
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''Unsafe text can be dumped to yaml format safely'''
    hostvars = {
        'var1': 'value',
        'var2': AnsibleUnsafeText('unsafe value'),
        'var3': {
            'key1': 'value',
            'key2': AnsibleUnsafeText('unsafe value'),
        },
        'var4': [
            'value',
            AnsibleUnsafeText('unsafe value'),
        ]
    }

    result = yaml.dump(HostVars(hostvars), default_flow_style=False, Dumper=AnsibleDumper)
    # Remove the last newline
    result = result.rstrip()

# Generated at 2022-06-22 11:36:09.396506
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    orig_data = {b'a': u'b', u'a': b'b'}
    hostvars = HostVars(orig_data)
    # Test representing a HostVars object
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == yaml.dump(dict(orig_data), Dumper=AnsibleDumper)

    # Test representing the dict inside a HostVarsVars object
    hostvars = HostVars({'h': b'ost'})
    hostvarsvars = HostVarsVars(hostvars)

# Generated at 2022-06-22 11:36:12.342406
# Unit test for function represent_unicode
def test_represent_unicode():
    data = {'a': u'unicode_value'}
    assert yaml.dump(data, Dumper=AnsibleDumper) == u"{a: unicode_value}\n"



# Generated at 2022-06-22 11:36:20.854547
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:36:21.306022
# Unit test for function represent_undefined
def test_represent_undefined():
    assert(True)

# Generated at 2022-06-22 11:36:28.248971
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = yaml.SafeDumper
    data = HostVars({"a": "b"})
    assert yaml.safe_dump(data, Dumper=dumper) == '{a: b}\n'



# Generated at 2022-06-22 11:36:31.005591
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('foo')
    yaml.dump(data, Dumper=AnsibleDumper)


# Generated at 2022-06-22 11:36:38.477035
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import Templar

    templar = Templar(loader=None)
    for in_val in (None, '', '0', 0, {}, {'foo': 'bar'}, ['foo', 'bar']):
        out_val = yaml.safe_dump(in_val, Dumper=AnsibleDumper, default_flow_style=False)
        assert out_val == yaml.safe_dump(in_val, default_flow_style=False)
        assert templar.template(out_val, convert_bare=False) == templar.template(yaml.safe_dump(in_val, default_flow_style=False), convert_bare=False)

# Generated at 2022-06-22 11:36:48.154487
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.module_utils.common.yaml import AnsibleDumper
    from ansible.module_utils.six import u

    outstr = u('a string')
    outstr_out = yaml.dump(outstr, Dumper=AnsibleDumper)
    assert outstr_out == "a string\n...\n", outstr_out

    outstr2 = u('a string with a "quote"')
    outstr2_out = yaml.dump(outstr2, Dumper=AnsibleDumper)
    assert outstr2_out == "\"a string with a \\\"quote\\\"\"\n...\n", outstr2_out



# Generated at 2022-06-22 11:36:49.731803
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars({"foo": "bar"})
    assert represent_hostvars(AnsibleDumper, hv) == "foo: bar"

# Generated at 2022-06-22 11:37:00.494174
# Unit test for function represent_undefined
def test_represent_undefined():
    """Test the behaviour of AnsibleUndefined when used with AnsibleDumper."""

    from unittest import TestCase

    class TestAnsibleDumper(TestCase):
        def test_continue(self):

            self.assertTrue(yaml.dump({'foo': True}, default_flow_style=False, Dumper=AnsibleDumper))

        def test_fail(self):

            with self.assertRaises(yaml.YAMLError):
                yaml.dump({'foo': AnsibleUndefined('foo')}, default_flow_style=False, Dumper=AnsibleDumper)

    TestAnsibleDumper().test_continue()
    TestAnsibleDumper().test_fail()

# Notes on the following code:
#
# We have to override the default scalar string formatter to handle


# Generated at 2022-06-22 11:37:09.239654
# Unit test for function represent_unicode
def test_represent_unicode():

    from ansible.module_utils.six import PY3
    from ansible.vars.manager import VariableManager

    dumper = yaml.Dumper()
    ansible_dumper = AnsibleDumper(dumper)
    dumper.represent_unicode = represent_unicode

    data = {'foo': 'bar'}
    loaded_data = yaml.safe_load(yaml.dump(data, Dumper=ansible_dumper))

    # py3 has unicode strings by default
    if PY3:
        assert isinstance(loaded_data['foo'], text_type)
    else:
        assert isinstance(loaded_data['foo'], str)

    # test a VariableManager
    vm = VariableManager()
    vm._variables = {'foo': [{'bar': 'Text'}]}


# Generated at 2022-06-22 11:37:10.532634
# Unit test for function represent_undefined
def test_represent_undefined():
    # No assertRaises on Python 3
    yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:37:20.575777
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''represent_vault_encrypted_unicode'''
    # Make an AnsibleVaultEncryptedUnicode object

# Generated at 2022-06-22 11:37:24.921898
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(None, None)
    assert dumper.represent_undefined(None) is None
    assert not dumper.represent_undefined(AnsibleUndefined())


# Generated at 2022-06-22 11:37:38.236574
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    representer = dumper.represent_binary

    # Ensure that represent_binary encodes the string
    actual = representer(dumper, 'hi')
    assert actual == yaml.representer.SafeRepresenter.represent_binary(dumper, 'hi')
    assert isinstance(actual, yaml.representer.ScalarNode)
    assert actual.style == '|'

    # Ensure that the string is encoded using latin-1 and then base64 encoded
    assert actual.value == str.encode('hi').encode('base64').decode('latin-1')

# Generated at 2022-06-22 11:37:49.446037
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''
    This is a stub function to unit test the above representer
    '''
    rep = yaml.representer
    dumper = AnsibleDumper


# Generated at 2022-06-22 11:37:52.566540
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars()
    data['logs_dir'] = '/var/log/'
    data['config_dir'] = '/etc/'
    assert yaml.safe_dump(data, default_flow_style=False, Dumper=AnsibleDumper) == 'logs_dir: /var/log/\nconfig_dir: /etc/\n'

# Generated at 2022-06-22 11:37:56.905931
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(None)
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, binary_type(b'foo')) == u"!binary |\n  Zm9v\n"



# Generated at 2022-06-22 11:38:04.210615
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''
    Test the representation of HostVars data.

    The `represent_hostvars` function should represent the
    HostVars data structure as a dict to match how the
    module's return values are represented.
    '''
    test_data = {'test_key': 'test_value'}
    hv = HostVars(test_data)
    hv_data = {'test': hv}
    res = represent_hostvars(AnsibleDumper, hv_data)

    assert res == {'test': {'test_key': 'test_value'}}

# Generated at 2022-06-22 11:38:14.215289
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars(dict(a=1, b=2))

    assert yaml.safe_dump(hv, default_flow_style=False, Dumper=AnsibleDumper) == \
        "a: 1\nb: 2\n"

    # all the following should dump the same
    assert yaml.safe_dump(dict(a=1, b=2), default_flow_style=False, Dumper=AnsibleDumper) == \
        "a: 1\nb: 2\n"

    assert yaml.safe_dump(HostVarsVars(dict(a=1, b=2)), default_flow_style=False, Dumper=AnsibleDumper) == \
        "a: 1\nb: 2\n"


# Generated at 2022-06-22 11:38:24.587032
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-22 11:38:31.753298
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import AnsibleUndefined
    from ansible.vars.manager import VarsManager
    vm = VarsManager()
    in_dict = dict(a=1)
    vm.set_host_variable(host='example.com', variable='my_dict', value={'a': 1})
    hostvars = HostVars(host_name='example.com', # pylint: disable=redefined-outer-name
                        vars_manager=vm)
    hostvars['my_dict'] = in_dict
    hostvars['my_undef'] = AnsibleUndefined('my_undef')
    assert 'example.com' == hostvars['inventory_hostname']

# Generated at 2022-06-22 11:38:34.692125
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(width=1)
    rendered = yaml.dump(AnsibleUndefined(), Dumper=dumper)
    assert rendered == 'False\n...\n'

# Generated at 2022-06-22 11:38:39.939987
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.module_utils.common.yaml import AnsibleDumper
    data = {'foo': 'bar'}
    hostvars = HostVars(data, hostvars=data)

    # TODO: how to test this?
    # serialized = yaml.dump(hostvars, Dumper=AnsibleDumper)
    # assert serialized == "{'foo': 'bar'}\n"

# Generated at 2022-06-22 11:38:54.440492
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = SafeDumper

    hostvars = HostVars(
        inventory=None,
        ansible_vars={
            'var1': 'value1',
            'var2': 'value2',
        }
    )
    dumper.add_representer(HostVars, represent_hostvars)
    assert dumper.represent_hostvars(hostvars) == dumper.represent_dict({'var1': 'value1', 'var2': 'value2'})



# Generated at 2022-06-22 11:38:58.788887
# Unit test for function represent_undefined
def test_represent_undefined():
    representer = AnsibleDumper()
    assert representer.represent_undefined(AnsibleUndefined) == False
    assert representer.represent_undefined(AnsibleUndefined) == True

# Generated at 2022-06-22 11:39:02.727326
# Unit test for function represent_unicode
def test_represent_unicode():
    instance = yaml.dumper.SafeDumper.represent_unicode
    data = dict(a=dict(b='foo'))
    assert instance(None, data) == yaml.representer.SafeRepresenter.represent_unicode(None, text_type(data))



# Generated at 2022-06-22 11:39:11.061385
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    vault = AnsibleVaultEncryptedUnicode(text_type(u"test"), 1)
    result = represent_vault_encrypted_unicode(None, vault)
    assert result == (u'"!vault"\n   "test"')
    # Note: this checks that we will have a string even if the input is bytes.
    # This is because the ouput is checked as yaml in several places (i.e. runner/lookup_plugins/vault.py)
    vault = AnsibleVaultEncryptedUnicode(binary_type(b"test"), 1)
    result = represent_vault_encrypted_unicode(None, vault)
    assert result == (u'"!vault"\n   "test"')



# Generated at 2022-06-22 11:39:22.920912
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:39:26.739744
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    data = 'some string'
    assert dumper.represent_unicode(data) == dumper.represent_unicode(text_type(data))


# Generated at 2022-06-22 11:39:28.650125
# Unit test for function represent_undefined
def test_represent_undefined():
    assert not AnsibleDumper.represent_undefined(None, AnsibleUndefined)

# Generated at 2022-06-22 11:39:31.237964
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVarsVars()
    data['foo'] = 'bar'
    assert represent_hostvars(AnsibleDumper, data) == "{'foo': 'bar'}"

# Generated at 2022-06-22 11:39:36.974755
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.manager import HostVarsVars

    assert yaml.dump(
        dict(HostVarsVars(dict(a=dict(c=3), b=42), 42)._get_value()),
        Dumper=AnsibleDumper,
        default_flow_style=False
    ) == '''a:
  c: 3
b: 42
'''
    assert yaml.dump(
        dict(HostVars(dict(a=dict(c=3), b=42))._get_value()),
        Dumper=AnsibleDumper,
        default_flow_style=False
    ) == '''a:
  c: 3
b: 42
'''

# Generated at 2022-06-22 11:39:40.978671
# Unit test for function represent_unicode
def test_represent_unicode():
    dump_data = AnsibleDumper(indent=4, default_flow_style=False).represent_unicode(b'')
    assert dump_data == 'null\n'
