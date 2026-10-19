

# Generated at 2022-06-22 11:29:52.389186
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(None)
    undefined = AnsibleUndefined()
    # the parent class should not throw an exception for represent scalar so we will not here
    output = dumper.represent_scalar('tag:yaml.org,2002:str', undefined)
    assert output == None
    # but our bool() override should cause it to throw an exception
    output = dumper.represent_data(undefined)
    assert output == None

# Generated at 2022-06-22 11:30:02.072430
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:30:11.814790
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Creating a HostVars object to test function represent_hostvars
    obj = HostVars()
    # Adding a value to test
    obj['ansible_ssh_host'] = '10.1.1.1'
    # Creating a custom yaml dumper
    dumper = AnsibleDumper
    # Calling the function with the custom dumper
    result = yaml.representer.Representer.represent_dict(dumper, dict(obj))
    # Asserting that the function returned the required value
    assert result.value == '{ansible_ssh_host: 10.1.1.1,}'



# Generated at 2022-06-22 11:30:21.659480
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper(None)

    assert dumper.represent_dict(dict(a=None)) == \
           dumper.represent_dict(HostVars(dict(a=None)))

    assert dumper.represent_dict(dict(a=1, b=2)) == \
           dumper.represent_dict(HostVars(dict(a=1, b=2)))

    assert dumper.represent_dict(dict(a=1, b=2)) != \
           dumper.represent_dict(HostVars(dict(a=1)))

    assert dumper.represent_dict(dict(a=1, b=2)) != \
           dumper.represent_dict(HostVars(dict(a=1, b=3)))



# Generated at 2022-06-22 11:30:31.195722
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = yaml.dump(AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;7.2;AES256;ansible\n'
                                                  '3430373933353733346635343635333865633832323535316665656634306132616335616437\n'
                                                  '36383666303737353233313661316230663433613063333764\n'), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:37.159200
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.module_utils.parsing.convert_bool import boolean
    assert boolean(yaml.dump(AnsibleUnicode('foo', 'utf-8'), Dumper=AnsibleDumper))



# Generated at 2022-06-22 11:30:45.758731
# Unit test for function represent_binary
def test_represent_binary():
    def check(data, expected):
        assert yaml.serialize(data, Dumper=AnsibleDumper) == expected

    check(b'123\n456\n789\n', "!!binary |\n  MTIzCjQ1Ngo3ODkK\n")
    check(b'1', "!!binary |\n  MQ==\n")
    check(b'12', "!!binary |\n  MTI=\n")
    check(b'123', "!!binary |\n  MTIz\n")
    check(b'1234', "!!binary |\n  MTIzNA==\n")

# Generated at 2022-06-22 11:30:51.568574
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars

    d = {u'foo': u'bar'}

    hostvars = HostVars(ansible_inventory_sources='/tmp/s')
    hostvars.update(d)

    dm = ansible_dump(hostvars)
    assert dm == u'foo: bar\n'



# Generated at 2022-06-22 11:30:53.496944
# Unit test for function represent_binary
def test_represent_binary():
    b = AnsibleDumper().represent_binary('foo')
    assert b is not None and isinstance(b, text_type)



# Generated at 2022-06-22 11:30:59.653796
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:31:06.221494
# Unit test for function represent_binary
def test_represent_binary():
    data = b'AAA\x00\xffBBB'
    result = yaml.representer.SafeRepresenter().represent_binary(data)
    assert result == u'!!binary |\n  QUFB/9CQkJC\n'


# Generated at 2022-06-22 11:31:14.005479
# Unit test for function represent_binary
def test_represent_binary():
    import sys

# Generated at 2022-06-22 11:31:25.017449
# Unit test for function represent_binary
def test_represent_binary():
    # Helper function to test represent_binary
    def _test_represent_binary(val):
        # Create an instance of AnsibleDumper
        dumper = AnsibleDumper()
        # Call the actual method under test
        return dumper.represent_binary(val)

    # Test representing bytes
    b = b'foo'
    assert _test_represent_binary(b) == b'!!binary |\n  Zm9v\n'

    # Test representing unicode
    s = u'a string after encoding'
    b = s.encode()
    assert _test_represent_binary(b) == b'!!binary |\n  YSBzdHJpbmcgYWZ0ZXIgZW5jb2Rpbmc=\n'

# Generated at 2022-06-22 11:31:29.516424
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.SafeDumper
    data = b"test\x00test"
    expected = "!!binary |\n  dGVzdAB0ZXN0"

    result = list(yaml.representer.SafeRepresenter.represent_binary(dumper, data))
    assert result == [expected]

# Generated at 2022-06-22 11:31:36.882579
# Unit test for function represent_binary
def test_represent_binary():
    import base64

    dumper = yaml.SafeDumper

    class Bytes(object):
        def __init__(self):
            self.value = b'\x00\x01\x02\x03\x04'

        def __bytes__(self):
            return self.value

    # Test 0
    representer = AnsibleDumper(dumper)
    result = representer.represent_binary(Bytes())

    assert result == '!!binary |-\n  {binary_value}'.format(
        binary_value=base64.b64encode(Bytes().value).decode()
    )

# Generated at 2022-06-22 11:31:47.156102
# Unit test for function represent_binary
def test_represent_binary():
    myDumper = AnsibleDumper()
    myDumper.indent = 4
    myDumper.width = 40
    myDumper.allow_unicode = True

# Generated at 2022-06-22 11:31:50.629224
# Unit test for function represent_binary
def test_represent_binary():
    unsafe_bytes = b'some bytes'
    repr_unsafe_bytes = AnsibleDumper().represent_binary(unsafe_bytes)
    assert repr_unsafe_bytes == 'some bytes'

# Generated at 2022-06-22 11:31:53.567328
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(None, b"\x00\x01\x02") == u"!binary |\n  AAEC"

# Generated at 2022-06-22 11:31:59.493140
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    assert dumper.represent_binary(binary_type(b'123')) == yaml.representer.SafeRepresenter.represent_binary(dumper, b'123')
    assert dumper.represent_binary('123') == yaml.representer.SafeRepresenter.represent_binary(dumper, '123')



# Generated at 2022-06-22 11:32:08.630272
# Unit test for function represent_binary
def test_represent_binary():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, Mock
    from ansible.template import Templar
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VarsManager

    with patch.object(Templar, 'template') as mock_template:
        mock_template.side_effect = [
            ('a', 'b'),
            ('c', 'd'),
            ('e', 'f'),
        ]

        vm = VarsManager()
        vm.add_host_vars('host1', HostVars(hostname='host1', vars=dict(x=b'y')))

# Generated at 2022-06-22 11:32:17.103170
# Unit test for function represent_binary
def test_represent_binary():
    stream = object()
    node = object()

    dumper = AnsibleDumper(stream)

    styled_node = dumper.represent_binary(node)

    style = styled_node[1]
    tag = styled_node[0]
    val = styled_node[2]

    assert style == '|'
    assert tag == 'tag:yaml.org,2002:binary'
    assert val == node



# Generated at 2022-06-22 11:32:20.764864
# Unit test for function represent_binary
def test_represent_binary():
    dump = AnsibleDumper()
    try:
        dump.represent_binary(b'abc')
    except UnicodeDecodeError:
        assert False, "UnicodeDecodeError exception should not be raised"


# Generated at 2022-06-22 11:32:22.886820
# Unit test for function represent_binary
def test_represent_binary():
    my_unrepresentable_str = '\xFF'
    represent_binary(None, my_unrepresentable_str)

# Generated at 2022-06-22 11:32:29.392792
# Unit test for function represent_binary
def test_represent_binary():
    # need to make sure we return byte strings and not unicode, for
    # use in e.g. the template module.
    assert yaml.dump(b'foo', Dumper=AnsibleDumper) == "!!binary \"Zm9v\"\n"
    # this should roundtrip with yaml properly
    data = yaml.load(yaml.dump(b'foo', Dumper=AnsibleDumper), Loader=yaml.SafeLoader)
    assert data == b'foo'

# Generated at 2022-06-22 11:32:31.384687
# Unit test for function represent_binary
def test_represent_binary():
    retval = represent_binary(AnsibleDumper, b'foo')
    assert retval == yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, b'foo')

# Generated at 2022-06-22 11:32:37.482159
# Unit test for function represent_binary
def test_represent_binary():
    class TestAnsibleDumper(AnsibleDumper):
        pass

    TestAnsibleDumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )

    test_str = AnsibleUnsafeBytes(six.b('\x82\x85\x88\x8a\x8d'))

    output = yaml.dump([test_str,], Dumper=TestAnsibleDumper)
    assert output == '---\n- !!binary |\n  --/u/8fQ==\n'

# Generated at 2022-06-22 11:32:48.240873
# Unit test for function represent_binary
def test_represent_binary():

    dumper = AnsibleDumper(width=256)

    # Test of short strings
    short_string_1 = b'\xDE\xAD\xBE\xEF'
    short_string_2 = b'foo'

    expected_short_string_1 = b'!binary |-\n  3q2+7w=='
    expected_short_string_2 = b'!binary |-\n  Zm9v'

    represent_binary_1 = yaml.dump([short_string_1], Dumper=dumper).splitlines()[1]
    represent_binary_2 = yaml.dump([short_string_2], Dumper=dumper).splitlines()[1]
    assert represent_binary_1 == expected_short_string_1
    assert represent_binary_2 == expected_short_string_

# Generated at 2022-06-22 11:32:53.074155
# Unit test for function represent_binary
def test_represent_binary():
    """
    Data contains ansible.module_utils.six.binary_type,
    we want to convert it to text_type
    """
    data = {'foo': 'bar', 'baz': ansible_b('qux')}
    dump_data = yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)
    new_data = yaml.safe_load(dump_data)

    assert new_data == data



# Generated at 2022-06-22 11:32:58.516149
# Unit test for function represent_binary
def test_represent_binary():
    ansible_dumper = AnsibleDumper
    ansible_dumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )

    result = yaml.dump([u'foo'], Dumper=ansible_dumper)
    assert result == u'- !!binary |\n  %s\n' % u'foo'.encode('base64')

# Generated at 2022-06-22 11:33:06.055710
# Unit test for function represent_binary
def test_represent_binary():
    datalist = [b'abc\x00\x01\x02\x03', b'abc\x00\x01\x02\x03', u'abc\x00\x01\x02\x03', u'abc\x00\x01\x02\x03']
    for data in datalist:
        result = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, binary_type(data))
        assert result == "!!binary |\n  YWJjACAwMTIz"