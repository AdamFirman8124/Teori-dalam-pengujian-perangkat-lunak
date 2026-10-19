

# Generated at 2022-06-22 11:29:50.146284
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper

    assert represent_hostvars(dumper, {'foo': 'bar'}) == yaml.representer.SafeRepresenter.represent_dict(dumper, {'foo': 'bar'})



# Generated at 2022-06-22 11:29:52.621127
# Unit test for function represent_undefined
def test_represent_undefined():
    result = AnsibleDumper().represent_data({'test' : AnsibleUndefined})
    assert result == 'test: null\n'

# Generated at 2022-06-22 11:29:56.204546
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    data = AnsibleVaultEncryptedUnicode('!vault |', b'bar')
    output = dumper.represent_data(data)
    expected = '!vault |\n          bar\n          '
    assert output == expected

# Generated at 2022-06-22 11:29:58.497338
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(binary_type(b'\xc3\xa9'), Dumper=AnsibleDumper) == "'\\xc3\\xa9'"

# Generated at 2022-06-22 11:30:01.367678
# Unit test for function represent_binary
def test_represent_binary():
    representer = yaml.representer.SafeRepresenter()
    assert represent_binary(representer, b'\x00\x01\n') == ('|\n'
                                                           '    AAoA')

# Generated at 2022-06-22 11:30:13.887529
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars('testhostname')

    # The only way to set a HostVarsVars item is by calling its append
    # method.
    hvv = HostVarsVars(hv, 'test')
    hvv.append(AnsibleUnicode('test'))
    hv._hostvars_vars['test'] = hvv

    # The only way to set an item on a HostVars object itself is by doing the
    # following.
    hv._hostvars['test2'] = AnsibleUnicode('test2')

    hv2 = HostVars('testhostname2')
    hv2._hostvars['test3'] = AnsibleUnicode('test3')


# Generated at 2022-06-22 11:30:18.818703
# Unit test for function represent_hostvars
def test_represent_hostvars():

    x = HostVars({"test_key": "test_val", "test_key2": "test_val2"})
    output = yaml.dump(x, Dumper=AnsibleDumper, default_flow_style=False)

    assert output == 'test_key: test_val\ntest_key2: test_val2\n'



# Generated at 2022-06-22 11:30:25.745533
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    bytes = b'\x00\x01\x02\x03\x04\x05home/nesting'
    aveu = AnsibleVaultEncryptedUnicode(bytes, None)
    ad = AnsibleDumper()
    value = ad.represent_vault_encrypted_unicode(aveu)
    assert value == ("!vault |\n  "
                     "AQABAEABABAABABABAEBwQGtvbWUvbmVzdGluZw==\n")

# Generated at 2022-06-22 11:30:31.712915
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    g = AnsibleUndefined()
    a = set()
    assert dumper.visit_set(a) == {g}
    b = {}
    assert dumper.visit_dict(b) == {g}
    assert dumper.visit_set(b) == {g}
    c = []
    assert dumper.visit_list(c) == [g]
    d = {g: g}
    assert dumper.visit_dict(d) == {g: g}
    assert dumper.visit_set(d) == {g: g}

# Generated at 2022-06-22 11:30:35.295100
# Unit test for function represent_unicode
def test_represent_unicode():
    s = AnsibleUnicode(u"hello")
    assert represent_unicode(None, s) == "'hello'"

# Generated at 2022-06-22 11:30:40.117679
# Unit test for function represent_undefined
def test_represent_undefined():
    dump = yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper, default_flow_style=False)
    assert dump == "~"



# Generated at 2022-06-22 11:30:43.322794
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper.represent_undefined(AnsibleDumper, AnsibleUndefined) == True
    assert AnsibleDumper.represent_undefined(AnsibleDumper, '') == False

# Generated at 2022-06-22 11:30:50.523454
# Unit test for function represent_binary
def test_represent_binary():
    # Sort yaml.record_path_attribute to get a predictable order of the encoded
    # data.
    dumped = yaml.dump(str('mystring'), default_flow_style=False, Dumper=yaml.Dumper, allow_unicode=True)
    dump_lines = dumped.split('\n')
    assert dump_lines[0] == '!!python/bytes'
    assert dump_lines[1] == "    b'mystring'"

# Generated at 2022-06-22 11:30:55.205265
# Unit test for function represent_hostvars
def test_represent_hostvars():
    h = HostVars(None)
    h.host = 'host1'
    h.vars['a'] = 'b'
    h.vars['clear'] = AnsibleVaultEncryptedUnicode('1234')
    h.vars['c'] = 'd'
    assert AnsibleDumper(indent=2).represent_hostvars(h) == dict(h) is not h

# Generated at 2022-06-22 11:31:02.727605
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # This is the data format to represent.
    input_data = AnsibleVaultEncryptedUnicode(u'foo', u'bar')

    # This is the expected output
    expected_output = u'!vault |\n          bar'

    # This is the actual output from the AnsibleDumper
    actual_output = yaml.dump(input_data, Dumper=AnsibleDumper)

    # If the expected and actual outputs match, then the test passes.
    assert actual_output == expected_output

# Generated at 2022-06-22 11:31:12.039005
# Unit test for function represent_undefined
def test_represent_undefined():
    # Verify that the output of represent_undefined is never used.
    # For this to work, it is necessary that the returned value is
    # consumed by parent code. If the value is not consumed, that
    # is a bug.

    # First make sure _fail_with_undefined_error is called.
    # This should be true if represent_undefined returns True.
    # If represent_undefined returns False, then _fail_with_undefined_error
    # will not be called.

    unset_var = AnsibleUndefined
    dump_out = yaml.dump(unset_var, Dumper=AnsibleDumper, default_flow_style=False)
    # This should not raise an exception
    assert dump_out is not None

    # Now a test case where the value is consumed


# Generated at 2022-06-22 11:31:20.694362
# Unit test for function represent_undefined
def test_represent_undefined():
    def check(value):
        rep = AnsibleDumper.represent_undefined(None, value)
        assert rep is True

    def check_exception(value):
        try:
            AnsibleDumper.represent_undefined(None, value)
        except:
            return
        raise Exception("expected exception for: %s" % value)

    check(AnsibleUndefined(strict=False))
    check(AnsibleUndefined(strict=True))

    check_exception({})
    check_exception([])
    check_exception(10)

# Generated at 2022-06-22 11:31:22.843585
# Unit test for function represent_undefined
def test_represent_undefined():
    new_dumper = AnsibleDumper(None)
    assert new_dumper.represent_undefined(None) is False

# Generated at 2022-06-22 11:31:32.749628
# Unit test for function represent_unicode

# Generated at 2022-06-22 11:31:41.504907
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

    vault_key = 'test'
    vault_password_file = None
    vault = VaultLib(vault_key, vault_password_file)

    encrypted_string = vault.encrypt('test')
    encrypted_unicode = AnsibleVaultEncryptedUnicode(encrypted_string)
    out = yaml.dump([encrypted_unicode], Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:31:48.477082
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {
        "ansible_all_ipv4_addresses": [u'192.168.0.130'],
        "ansible_architecture": u'x86_64',
    }

    representer = represent_hostvars
    dumper = AnsibleDumper
    result = representer(dumper, data)

# Generated at 2022-06-22 11:32:00.146843
# Unit test for function represent_undefined
def test_represent_undefined():
    class Faketemplate(object):
        def __init__(self, x=None):
            self.x = x

    class FakeUndefined(object):
        def __init__(self, x):
            self.x = x

    for x in (False, 0, '', '0', b'', b'0', (), {}, None, set()):
        a = Faketemplate(x)
        fake_undefined = represent_undefined(a, FakeUndefined(x))
        assert (fake_undefined == x)

    # This should raise an exception
    a = Faketemplate()
    fake_undefined = represent_undefined(a, 'x')
    assert (fake_undefined is False)

# Generated at 2022-06-22 11:32:06.093251
# Unit test for function represent_undefined
def test_represent_undefined():
    # True if Undefined value is present in the data
    # Here the bool will be True
    val1 = {
        'name': 'foo',
        'state': 'present',
        'unknown_variable': AnsibleUndefined,
    }
    val2 = yaml.dump(val1, Dumper=AnsibleDumper)
    assert val2.startswith('Traceback (most recent call last):')



# Generated at 2022-06-22 11:32:09.219109
# Unit test for function represent_binary
def test_represent_binary():
    assert(yaml.dump(binary_type(b"foo"), Dumper=AnsibleDumper, encoding='utf-8') == "!!binary |\n  Zm9v\n")


# Generated at 2022-06-22 11:32:14.113214
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert not dumper.represent_undefined(None)
    assert not dumper.represent_undefined(AnsibleUndefined)
    assert dumper.represent_undefined(AnsibleUndefined(var_name='foo'))

# Generated at 2022-06-22 11:32:17.936270
# Unit test for function represent_binary
def test_represent_binary():
    x = AnsibleUnsafeBytes(b'abc\x99')
    y = yaml.dump(x, Dumper=AnsibleDumper)
    assert y == '!unsafe/bin abwEJg==\n'

# Generated at 2022-06-22 11:32:21.104661
# Unit test for function represent_hostvars
def test_represent_hostvars():
    input = HostVars({"foo": "bar"})
    output = yaml.dump(input, Dumper=AnsibleDumper)
    assert output == 'foo: bar\n'



# Generated at 2022-06-22 11:32:31.200730
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert dumper.represent_unicode(dumper, "some str") == dumper.represent_scalar(u'tag:yaml.org,2002:str', u'some str', style='"')
    assert dumper.represent_unicode(dumper, u"some str") == dumper.represent_scalar(u'tag:yaml.org,2002:str', u'some str', style='"')
    assert dumper.represent_unicode(dumper, u"some: str") == dumper.represent_scalar(u'tag:yaml.org,2002:str', u'some: str', style='"')

# Generated at 2022-06-22 11:32:34.935519
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'a': 1, 'b': 2, 'c': 3}
    dumper = AnsibleDumper()
    yaml_data = dumper.represent_dict(dict(data))
    assert data == yaml.load(yaml_data)



# Generated at 2022-06-22 11:32:37.658802
# Unit test for function represent_undefined
def test_represent_undefined():
    data = AnsibleUndefined()
    stream = AnsibleDumper.represent_undefined(None, data)
    assert stream is False

# Generated at 2022-06-22 11:32:47.688795
# Unit test for function represent_unicode
def test_represent_unicode():

    value = AnsibleUnicode("some text")
    yaml_wrapper = AnsibleDumper()
    result = yaml_wrapper.represent_unicode(value)
    assert result == "some text"

    value = AnsibleUnsafeText("some text")
    result = yaml_wrapper.represent_unicode(value)
    assert result == "some text"

    value = AnsibleUnsafeBytes(b"some text")
    result = yaml_wrapper.represent_unicode(value)
    assert result == "some text"



# Generated at 2022-06-22 11:32:54.620961
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    dumper = AnsibleDumper
    templar = Templar(loader=None)
    data = "test"
    yaml_data = dumper.represent_unicode(dumper, templar.do_string_replacement_safe(data))
    yaml_data = yaml.load(yaml_data)
    assert yaml_data == "test"
    data = "test"
    yaml_data = dumper.represent_unicode(dumper, templar.do_string_replacement_safe(data))
    yaml_data = yaml.load(yaml_data)
    assert yaml_data == "test"

# Generated at 2022-06-22 11:32:57.836679
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(None)
    r_string = dumper.represent_binary(b"\x01")
    assert r_string == u"!binary |\n  AQ==\n"

# Generated at 2022-06-22 11:33:00.357182
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    ret = dumper.represent_unicode(dumper, 'some_string')
    assert ret == "'some_string'\n"

# Generated at 2022-06-22 11:33:03.109091
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    dump = text_type(dumper.represent_unicode(dumper, u'foo'))
    assert dump == u'foo'



# Generated at 2022-06-22 11:33:07.034699
# Unit test for function represent_unicode
def test_represent_unicode():

    class Dumper(AnsibleDumper):
        pass

    dumper = Dumper()
    string = u'123'
    assertion_message = 'Test failed'
    assert isinstance(dumper.represent_unicode(dumper, string), str), assertion_message

# Generated at 2022-06-22 11:33:18.601392
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml.loader import AnsibleLoader
    dumper = yaml.SafeDumper
    dumper.ignore_aliases = lambda self, data: True
    # The loader is used to round-trip the data so we can compare it later
    # The load parameter is a short-hand for AnsibleLoader that takes
    # the data as an argument.
    load = lambda x: yaml.load(x, Loader=AnsibleLoader)
    # Using this method we can check that the representation of the data
    # is what we expect.
    assert load(yaml.dump(b'test', Dumper=dumper)) == b'test'
    assert load(yaml.dump(b'123', Dumper=dumper)) == b'123'

# Generated at 2022-06-22 11:33:29.370815
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.utils.unsafe_proxy import wrap_var
    mystr = wrap_var(AnsibleUnsafeText(u'hello world'))
    assert yaml.dump(mystr, Dumper=AnsibleDumper) == u"!!python/unicode 'hello world'\n"

    mystr = wrap_var(AnsibleUnsafeText(u'hello world'))
    assert yaml.dump(mystr, default_flow_style=True, Dumper=AnsibleDumper) == u"!!python/unicode 'hello world'\n"

    mystr = wrap_var(u'hello world')
    assert yaml.dump(mystr, Dumper=AnsibleDumper) == u"!!python/unicode 'hello world'\n"


# Generated at 2022-06-22 11:33:31.746697
# Unit test for function represent_binary
def test_represent_binary():
    yaml_str = yaml.dump(dict(b'A', b'B'), Dumper=AnsibleDumper)
    assert yaml_str == '!!python/bytes A\n!!python/bytes B\n'

# Generated at 2022-06-22 11:33:42.916764
# Unit test for function represent_binary

# Generated at 2022-06-22 11:33:54.192812
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(SafeDumper, b'123\n456\n') == u'!!binary |\n  MTIzCgo0NTYK\n'
    assert AnsibleDumper.represent_binary(SafeDumper, b'123456') == u'!!binary |\n  MTIzNDU2\n'
    assert AnsibleDumper.represent_binary(SafeDumper, b'\x01\x02\x03') == u'!!binary |\n  AQID\n'
    assert AnsibleDumper.represent_binary(SafeDumper, b'\xff\xfe\xfd') == u'!!binary |\n  /v8A\n'


# Generated at 2022-06-22 11:33:58.897689
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('value')
    # DATA -> Python object
    # dumper -> Python object -> YAML
    # YAML -> yaml.nodes.ScalarNode
    yaml_data = yaml.dump(data, Dumper=AnsibleDumper)
    assert yaml_data == "value\n...\n"



# Generated at 2022-06-22 11:34:05.018914
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    data = b"\x00\xFF"
    binary = yaml.representer.SafeRepresenter.represent_binary(dumper, data)
    if not isinstance(binary, text_type):
        assert False, "represent_binary returns a text_type object"
    elif not binary == '!!binary |-\n  AA8K\n':
        assert False, "represent_binary does not work as expected"
    else:
        assert True, "represent_binary works as expected"



# Generated at 2022-06-22 11:34:10.285191
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    dumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )

    value = AnsibleUnsafeBytes(b'\n')
    assert dumper.represent_data(value) == "!!binary '\\n'"

# Generated at 2022-06-22 11:34:13.404481
# Unit test for function represent_unicode
def test_represent_unicode():
    value = 'test'
    assert represent_unicode(AnsibleDumper, value) == \
        text_type(yaml.dump(text_type(value)))



# Generated at 2022-06-22 11:34:24.029902
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert dumper.represent_unicode(dumper, 'string') == yaml.representer.SafeRepresenter.represent_str(dumper, 'string')
    assert dumper.represent_unicode(dumper, b'string') == yaml.representer.SafeRepresenter.represent_str(dumper, 'string')
    assert dumper.represent_unicode(dumper, u'string') == yaml.representer.SafeRepresenter.represent_str(dumper, 'string')
    assert dumper.represent_unicode(dumper, u'\N{SNOWMAN}') == yaml.representer.SafeRepresenter.represent_str(dumper, '\N{SNOWMAN}')
    assert dumper.represent_unicode(dumper, u'\u00b0')

# Generated at 2022-06-22 11:34:32.701059
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml_str = u'''foo: !u 'bar'\n'''
    data = yaml.load(yaml_str, Loader=yaml.SafeLoader)
    yaml_out = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    yaml_out = yaml_out.replace('\n', '')
    assert yaml_out == u'''foo: 'bar'\n'''
    data = yaml.load(yaml_out, Loader=yaml.SafeLoader)
    assert data[u'foo'] == u'bar'



# Generated at 2022-06-22 11:34:36.050346
# Unit test for function represent_unicode
def test_represent_unicode():
    data = yaml.dump({'a': 1, u'unicode_key\u1234': 2}, Dumper=AnsibleDumper)
    assert data == b'{a: 1, "unicode_key\\u1234": 2}\n'



# Generated at 2022-06-22 11:34:42.530226
# Unit test for function represent_binary
def test_represent_binary():
    # Test data
    # Raw binary data
    data = b'\xA1'
    # What the rendered output should be
    ref_output = '!binary |\n  qUE='

    # Create a safe dumper
    yaml_sd = yaml.SafeDumper
    # Create a representer for binary
    yaml.add_representer(binary_type, yaml.representer.SafeRepresenter.represent_binary, Dumper=yaml_sd)

    # Render the test data
    result = yaml.dump(data, Dumper=yaml_sd)
    # Check result matches expected
    assert result == ref_output

    # Cleanup
    delattr(yaml, 'representer')

# Generated at 2022-06-22 11:34:48.312323
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump({u'foo': u'bar'}, Dumper=AnsibleDumper) == u'{foo: bar}\n...\n'
    assert yaml.dump({u'foo': u'bar', u'foos': u'bars'}, Dumper=AnsibleDumper) == u'{foo: bar, foos: bars}\n...\n'


# Generated at 2022-06-22 11:34:54.340991
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.common.yaml import AnsibleDumper

    assert AnsibleDumper.represent_binary(u'\u2318') == AnsibleDumper.represent_scalar(u'!binary', u'\u2318')

# Generated at 2022-06-22 11:35:00.397002
# Unit test for function represent_binary
def test_represent_binary():

    b = b'\x80'
    expected = "!!binary 'gAAAAA='"

    # With
    dumper = AnsibleDumper(stream=None)
    result = dumper.represent_binary(b)
    assert result == expected

    # Without
    dumper = yaml.Dumper(stream=None)
    result = dumper.represent_binary(b)
    assert result != expected



# Generated at 2022-06-22 11:35:03.459287
# Unit test for function represent_unicode
def test_represent_unicode():
    ipaddress = 'ipaddress'
    x = AnsibleUnicode(ipaddress)
    assert represent_unicode(AnsibleDumper, x) == u"'ipaddress'"
    assert type(represent_unicode(AnsibleDumper, x)) == text_type

# Generated at 2022-06-22 11:35:12.321142
# Unit test for function represent_binary
def test_represent_binary():
    def decode(string):
        return string

    ansible_dumper = AnsibleDumper(default_style='|', default_flow_style=False)

    src = b'test'
    result = ansible_dumper.represent_binary(src)
    assert result == '|-\n    test\n'

    # Note that this will change in Ansible 2.7 when we start using
    # an ordered dict
    src = {b'test': b'value'}
    result = ansible_dumper.represent_dict(src)
    assert result == '!<tag:yaml.org,2002:map>\n- test: value\n'

# Generated at 2022-06-22 11:35:19.333548
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = dict(
        key=AnsibleUnicode('foo'),
    )

    buf = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    assert buf == 'key: foo\n'

    buf = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=True)
    assert buf == '{key: foo}\n'

    loaded_data = yaml.load(buf, Loader=AnsibleLoader)
    assert loaded_data == data

    loaded_data = yaml.load(buf)
    assert loaded_data != data



# Generated at 2022-06-22 11:35:24.086767
# Unit test for function represent_unicode
def test_represent_unicode():
    pre_yaml = u'foo: bar\na: b'
    expected_yaml = b'foo: bar\na: b\n'

    yaml_output = yaml.dump(pre_yaml, Dumper=AnsibleDumper)

    assert yaml_output == expected_yaml



# Generated at 2022-06-22 11:35:31.624558
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    AnsibleDumper.represent_unicode() should return the correct YAML representation
    of the given AnsibleUnicode, making sure to prefix it with ``u``.
    '''

    ansible_unicode = AnsibleUnicode('test')
    output = yaml.dump(ansible_unicode, Dumper=AnsibleDumper, default_flow_style=False)

    # Need to strip trailing newline for this test to pass.
    assert output.endswith('\n')
    output = output.strip()

    assert output == "u'test'"

# Generated at 2022-06-22 11:35:39.586316
# Unit test for function represent_binary
def test_represent_binary():
    data = b'#!\n---\n- 1\n- 2.0\n- three\n'

    yaml.add_representer(binary_type, represent_binary, Dumper=AnsibleDumper)
    assert yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False) == '!!binary |-\n  IyEKLS0KLSAxCi0gMi4wCi0gdGhyZWUK'



# Generated at 2022-06-22 11:35:51.104613
# Unit test for function represent_binary
def test_represent_binary():
    def dump_represent_binary(data):
        import io
        out = io.StringIO()
        AnsibleDumper(None, None, None, None).represent_binary(data)
        return out.getvalue()

    assert dump_represent_binary(None) == """\
!binary |-
""".encode('utf-8')

    assert dump_represent_binary(b'') == """\
!binary |-
""".encode('utf-8')

    assert dump_represent_binary(b' ') == """\
!binary |
 IGU=
""".encode('utf-8')

    assert dump_represent_binary(b'a') == """\
!binary |
 YQ==
""".encode('utf-8')


# Generated at 2022-06-22 11:35:59.441295
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(b'{"a": u"b"}', Dumper=AnsibleDumper) == "\"{'a': u'b'}\"\n"
    assert yaml.dump(b'u"test"', Dumper=AnsibleDumper) == "u'test'\n"
    assert yaml.dump(u'"test"', Dumper=AnsibleDumper) == "u'test'\n"
    assert yaml.dump(u'test', Dumper=AnsibleDumper) == "u'test'\n"

# Generated at 2022-06-22 11:36:12.808261
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(width=1024, default_flow_style=True)
    result = dumper.represent_binary(b'aabbcc')
    assert result == "!!binary \"YWFhYmJjYw==\"\n"

    result = dumper.represent_binary(b'')
    assert result == "!!binary \"\"\n"

    result = dumper.represent_binary(bytearray(range(256)))


# Generated at 2022-06-22 11:36:19.365550
# Unit test for function represent_binary
def test_represent_binary():
    if yaml.__with_libyaml__:
        out = yaml.dump(b'foo', Dumper=AnsibleDumper)
        assert out == b"!binary |-\n  Zm9v\n"
    else:
        out = yaml.dump(b'foo', Dumper=AnsibleDumper)
        assert out == b"!binary |\n  Zm9v\n"



# Generated at 2022-06-22 11:36:23.181983
# Unit test for function represent_unicode
def test_represent_unicode():
    # Given
    data = AnsibleUnicode("Foo")

    # When
    output = yaml.safe_dump(data, default_flow_style=False, Dumper=AnsibleDumper)

    # Then
    assert("Foo" in output)


# Generated at 2022-06-22 11:36:34.759071
# Unit test for function represent_binary
def test_represent_binary():

    dumper = AnsibleDumper(preserve_quotes=True)

    assert dumper.represent_binary(b"\x00\x01\x02\x03") == "!!binary \"\\u0000\\u0001\\u0002\\u0003\"\n"
    assert dumper.represent_binary(b"\xc3\x28") == "!!binary \"\\u00c3(\"\n"
    assert dumper.represent_binary(b"\xe6\x97\xa5\xd1\x88") == "!!binary \"\\u65e5\\u0428\"\n"

# Generated at 2022-06-22 11:36:37.423758
# Unit test for function represent_unicode
def test_represent_unicode():
    rep = AnsibleDumper().represent_unicode
    if not PY3:
        assert rep('unicode') == u'"unicode"'
    else:
        assert rep('unicode') == u'"unicode"'

# Generated at 2022-06-22 11:36:41.467410
# Unit test for function represent_binary
def test_represent_binary():
    result = repr(AnsibleDumper.represent_binary(None, b'123'))
    assert result == "'123'", result
    result = repr(AnsibleDumper.represent_binary(None, b'123\n'))
    assert result == "'123\\n'", result

# Generated at 2022-06-22 11:36:49.749468
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump('foo') == yaml.dump(AnsibleUnicode('foo'))
    assert yaml.dump('foo') == yaml.dump(AnsibleUnsafeText('foo'))
    assert yaml.dump('foo') == yaml.dump(AnsibleUnsafeBytes('foo'))
    # test handling of unicode
    assert yaml.dump('\u2028') == yaml.dump(AnsibleUnsafeText('\u2028'))
    assert yaml.dump('\u2029') == yaml.dump(AnsibleUnsafeText('\u2029'))

# Generated at 2022-06-22 11:36:51.766077
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    text = u'hello world'
    result = dumper.represent_unicode(text)
    assert result == u"'hello world'"

# Generated at 2022-06-22 11:36:53.896301
# Unit test for function represent_binary
def test_represent_binary():
    assert represent_binary(AnsibleDumper, b'\x1e') == u'!!binary |\n  FSg='



# Generated at 2022-06-22 11:36:57.467738
# Unit test for function represent_binary
def test_represent_binary():
    ansible_dumper = AnsibleDumper()

    data = b'\x01\x02\x03'
    result = ansible_dumper.represent_binary(data)
    assert result == "!!binary |\n  AQID"


# Generated at 2022-06-22 11:37:08.330586
# Unit test for function represent_unicode
def test_represent_unicode():

    BLOCK_STYLE = u"""
foo:
  - Hello World: |
      This is some information
      That spans multiple lines
      And includes a colon, but there's no need to worry
      because we can handle it.
  - Other thing: this is some other : key with a value
"""
    FLOW_STYLE = u"""
foo:
- {key: Hello World, value: |-
    This is some information
    That spans multiple lines
    And includes a colon, but there's no need to worry
    because we can handle it.}
- {key: Other thing, value: 'this is some other : key with a value'}
"""


# Generated at 2022-06-22 11:37:13.315359
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, b'\x01\x02\x03\x04') == b"!!binary 'AQIDBA=='"
    assert dumper.represent_binary(dumper, b'') == b"!!binary ''"



# Generated at 2022-06-22 11:37:22.891948
# Unit test for function represent_unicode
def test_represent_unicode():

    # Test1: ansible unicode object is dumped as ansible string
    ansible_unicode = AnsibleUnicode('test')
    assert yaml.dump(ansible_unicode, Dumper=AnsibleDumper) == 'test\n...\n'

    # Test2: ansible unsafe text object is dumped as ansible string
    ansible_unsafe_text = AnsibleUnsafeText('test')
    assert yaml.dump(ansible_unsafe_text, Dumper=AnsibleDumper) == 'test\n...\n'

    # Test3: ansible unsafe bytes object is dumped as ansible binary
    ansible_unsafe_bytes = AnsibleUnsafeBytes('test')

# Generated at 2022-06-22 11:37:27.944266
# Unit test for function represent_binary
def test_represent_binary():

    test_case = AnsibleUnsafeBytes(b"\x01\x02\x03\x04")
    output = yaml.safe_dump(test_case, default_flow_style=True, Dumper=AnsibleDumper)

    assert output == "!!binary |\n  AQIDBA==\n"

# Generated at 2022-06-22 11:37:38.412969
# Unit test for function represent_binary
def test_represent_binary():

    # Empty binary should be empty string
    assert yaml.dump(binary_type(b''), Dumper=AnsibleDumper) == '""\n'

    # Binary data will be encoded as a string literal
    assert yaml.dump(binary_type(b'blah'), Dumper=AnsibleDumper) == "'blah'\n"

    # A byte string with control characters will get encoded with
    # double quotes and backslash escapes.
    result = yaml.dump(binary_type(b'\x00\x01\x02abcd'), Dumper=AnsibleDumper)
    assert result.startswith('"')
    assert result.endswith('"\n')



# Generated at 2022-06-22 11:37:49.797858
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import yaml

    # This is a regression test for https://github.com/ansible/ansible/issues/22415

    # python2 accepts both str and unicode types, so if we want test to be
    # meaningful, we need to make sure that we are not getting the default
    # behavior from the parent class
    sample_str = u'yaml_unicode_test'
    assert isinstance(sample_str, text_type)
    sample_unicode = u"""sample_unicode: yaml_unicode_test"""
    sample_data = yaml.load(sample_unicode, AnsibleLoader)

# Generated at 2022-06-22 11:37:58.810859
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.representer.Representer()
    dumper.represent_binary = represent_binary
    dumper.encoding = 'utf-8'

    if yaml.__with_libyaml__:
        input_ = b'\x01\x02\x03'
        expected = '!!binary |\n  AQID\n'
    else:
        input_ = b'\x01\x02\x03'
        expected = '!!binary |\n  AAAAAQID\n'

    # Test with bytes as input
    output = yaml.dump(input_, Dumper=dumper)
    assert output == expected

    # Test with str as input,
    output = yaml.dump(input_.decode(), Dumper=dumper)
    assert output == expected

# Generated at 2022-06-22 11:38:00.903145
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b"bar") == yaml.representer.SafeRepresenter.represent_binary(b"bar")

# Generated at 2022-06-22 11:38:03.338694
# Unit test for function represent_unicode
def test_represent_unicode():
    d = yaml.dump(AnsibleUnicode('Hello World'), Dumper=AnsibleDumper)
    assert d == 'Hello World\n...\n'



# Generated at 2022-06-22 11:38:06.191092
# Unit test for function represent_unicode
def test_represent_unicode():
    d = AnsibleDumper()
    assert d.represent_unicode(u'string') == u"'string'\n"
    assert d.represent_unicode(u"Y'all") == u"'Y\\'all'\n"



# Generated at 2022-06-22 11:38:11.117892
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes(b"a \n b")
    assert AnsibleDumper.represent_data(data) == u"!binary |\n  YSAgCiBi\n"

# Generated at 2022-06-22 11:38:14.014987
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes("blah")
    dumper = AnsibleDumper()
    yaml.representer.SafeRepresenter.represent_binary(dumper, data)
    assert dumper.stream.getvalue() == '!binary |\n  YmxhaA==\n'

# Generated at 2022-06-22 11:38:24.561510
# Unit test for function represent_binary
def test_represent_binary():
    # x means b'x'
    assert yaml.safe_dump(b'x', default_flow_style=False) == '"x"\n'

    # 'x' means 'x'
    assert yaml.safe_dump('x', default_flow_style=False) == "'x'\n"

    # b'x' means b'x'
    assert yaml.safe_dump(b'x', default_flow_style=False) == '"x"\n'

    # b'' means ''
    assert yaml.safe_dump(b'', default_flow_style=False) == "''\n"

    # '' means ''
    assert yaml.safe_dump('', default_flow_style=False) == "''\n"

    # 'x' with AnsibleUnsafeText means 'x'


# Generated at 2022-06-22 11:38:35.280340
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml.add_constructor(u'tag:yaml.org,2002:str', lambda loader, node: node.value, AnsibleLoader)

    # This test data contains UTF-8 characters
    utf8_data = {'a': 'b\xe9\xe9\xe9\xe9\xe9'}

    # The YAML returned from yaml.safe_dump is going to be Unicode.
    # yaml.safe_dump returns a Unicode string if passed a Unicode string
    # or a character mapping.
    yaml_data = yaml.safe_dump(utf8_data, allow_unicode=True, default_flow_style=False, Dumper=AnsibleDumper)

    # This test will fail if the Unicode characters are not properly

# Generated at 2022-06-22 11:38:39.235465
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes(b'binary')
    assert yaml.dump(data, Dumper=AnsibleDumper) == '!!binary "YmluYXJ5"\n'

# Generated at 2022-06-22 11:38:42.073900
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    representer = yaml.representer.SafeRepresenter.represent_binary
    test_data = binary_type('some binary data')
    assert repr(representer(dumper, test_data)) == repr(representer(dumper, binary_type(test_data)))


# Generated at 2022-06-22 11:38:53.889320
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleUnsafeBytes(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f ') == b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f '

# Generated at 2022-06-22 11:38:56.162614
# Unit test for function represent_unicode
def test_represent_unicode():
    represent_unicode(AnsibleDumper, "")


# Generated at 2022-06-22 11:39:00.028658
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper([], None, None)
    assert dumper.represent_binary("\x00\x01\x02\x03\x05") == "!!binary |\n  AAAECAw==\n"



# Generated at 2022-06-22 11:39:03.886271
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(u"example") == u'example'
    assert dumper.represent_unicode(u'example \"quoted\" string') == u'example \"quoted\" string'


# Generated at 2022-06-22 11:39:10.455758
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    data = u'\x00\x01\r\n'

    expected_result = "'\\x00\\x01\\r\\n'"

    result = dumper.represent_binary(dumper.represent_unicode, data)

    assert expected_result == result

# Generated at 2022-06-22 11:39:22.140301
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper

    test_data = b'\xed\xa1\xbc\xed\xb0\x8d'
    assert dumper.represent_unicode(dumper, test_data) == '"\\ud7a4\\ud7b0\\ubcd"'

    test_data = b'\xe4\xbb\xac'
    assert dumper.represent_unicode(dumper, test_data) == '"\\u4f60"'

    test_data = b'\xe2\x99\xaa'
    assert dumper.represent_unicode(dumper, test_data) == '"\\u262a"'

    test_data = b'\xe3\x80\x81'

# Generated at 2022-06-22 11:39:25.159977
# Unit test for function represent_unicode
def test_represent_unicode():
    dumped = yaml.dump({'unicode': AnsibleUnicode('unicode string')}, default_flow_style=True, Dumper=AnsibleDumper)
    assert dumped == '{unicode: unicode string}\n'



# Generated at 2022-06-22 11:39:31.237777
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, text_type(u'unicode')) == yaml.representer.SafeRepresenter.represent_str(None, text_type(u'unicode'))
    assert represent_unicode(None, AnsibleUnsafeText(u'unicode')) == yaml.representer.SafeRepresenter.represent_str(None, text_type(u'unicode'))


# Generated at 2022-06-22 11:39:34.439608
# Unit test for function represent_binary
def test_represent_binary():
    representer = AnsibleDumper()
    from io import BytesIO
    data = b"\x00\x01\x02\x03"
    result = yaml.representer.SafeRepresenter.represent_binary(representer, data)
    assert yaml.serializer.Serializer.emit(result) == b'{!!binary}\\x000102\\x03'

# Generated at 2022-06-22 11:39:38.664882
# Unit test for function represent_binary
def test_represent_binary():
    b1 = b'example'
    assert u'!!binary |\n  ' + b1.decode('utf-8') == yaml.dump(b1, Dumper=AnsibleDumper)


if __name__ == '__main__':
    test_represent_binary()

# Generated at 2022-06-22 11:39:40.890604
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, u"foo") == "foo"

# Generated at 2022-06-22 11:39:43.998577
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('abc')
    data_out = yaml.dump(data, Dumper=AnsibleDumper)
    assert data_out == 'abc\n...\n'

