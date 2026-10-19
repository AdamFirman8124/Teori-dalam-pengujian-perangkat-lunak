

# Generated at 2022-06-22 11:29:51.733256
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(u'bytestring') == u"bytestring\n"
    assert dumper.represent_unicode('bytestring') == u"bytestring\n"
    assert dumper.represent_unicode(u'\u0123') == u"\u0123\n"


# Generated at 2022-06-22 11:29:56.845219
# Unit test for function represent_binary
def test_represent_binary():
    text = b"foo\x01\x02\x03bar"
    data = [text]
    AnsibleDumper.add_representer(type(text), represent_binary)
    out = yaml.dump(data, Dumper=AnsibleDumper)
    assert out == b"[!!binary |\n  Zm9vADEyM2Jhcg==\n]\n"

# Generated at 2022-06-22 11:29:59.160908
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.safe_dump(AnsibleUnicode('hello')) == u'- hello\n'



# Generated at 2022-06-22 11:30:01.682041
# Unit test for function represent_binary
def test_represent_binary():
    assert represent_binary(AnsibleDumper, '\xff\x00') == '!!binary |\n  /wAA'



# Generated at 2022-06-22 11:30:04.517974
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'foo', Dumper=AnsibleDumper).strip() == "!!binary \"Zm9v\""

# Generated at 2022-06-22 11:30:08.313657
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    data = AnsibleUndefined
    ansible_undefined = dumper.representers[AnsibleUndefined](dumper, data)
    assert ansible_undefined is False

# Generated at 2022-06-22 11:30:18.080869
# Unit test for function represent_binary
def test_represent_binary():

    dumper = AnsibleDumper

    def assert_represent_binary(input_value, expected_output):
        actual_output = dumper.represent_binary(dumper, input_value)
        assert actual_output == expected_output

    def assert_represent_binary_error(input_value):
        try:
            dumper.represent_binary(dumper, input_value)
        except TypeError:
            pass
        else:
            raise AssertionError("Unexpected success")

    # Test basic functionality
    assert_represent_binary(b'12345', 'MTIzNDU=\n')

    # Test invalid type - should thrown an exception
    assert_represent_binary_error(u'12345')

# Generated at 2022-06-22 11:30:27.650920
# Unit test for function represent_binary
def test_represent_binary():
    # Example string with null bytes
    a = 'Foo\0Bar'
    # Example string with non-ascii chars
    b = 'F\xe9vrier'

    # Test: binary should have !binary and use the Base64-encoded representation
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, a) == (
        "!binary |-\n"
        "  Rm9vAGJhcg==\n"
    )
    assert dumper.represent_binary(dumper, b) == (
        "!binary |-\n"
        "  RuiD4mVyaWVy\n"
    )



# Generated at 2022-06-22 11:30:32.154921
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.utils.unsafe_proxy import wrap_var
    dumper = AnsibleDumper()
    binary_data = wrap_var(b'\x80\x81\x82')
    assert dumper.represent_data(binary_data) == u'!binary |\n  gICAg\n'

    binary_data = wrap_var(b'', encoding='base64')
    assert dumper.represent_data(binary_data) == u'!binary |\n  \n'



# Generated at 2022-06-22 11:30:40.481964
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # this test is pretty useless, we need to stub out the VaultLib or
    # use a real vault file. For now, just make sure we get the right
    # string back
    foo = AnsibleVaultEncryptedUnicode(u'hello there')
    assert foo._ciphertext == b'hello there'
    assert represent_vault_encrypted_unicode(AnsibleDumper, foo) == u"!vault |\n  hello there\n"



# Generated at 2022-06-22 11:30:48.175665
# Unit test for function represent_unicode
def test_represent_unicode():

    # Ensure that nothing is changed when string is passed
    assert yaml.dump(text_type('Hello World!'), Dumper=AnsibleDumper, encoding=None) == 'Hello World!\n...\n'

    # Ensure that SafeUnicode is encoded to utf-8
    safeunicode = AnsibleUnicode('Hello World!')
    assert yaml.dump(safeunicode, Dumper=AnsibleDumper, encoding=None) == 'Hello World!\n...\n'



# Generated at 2022-06-22 11:30:50.928763
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(None, AnsibleVaultEncryptedUnicode(b'foo')) == u'!vault |\n  foo\n'

# Generated at 2022-06-22 11:30:52.334738
# Unit test for function represent_undefined
def test_represent_undefined():
    represent_undefined(None, AnsibleUndefined("Hello"))

# Generated at 2022-06-22 11:31:03.303703
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import string
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    assert string.printable in set(string.printable).difference(set(u'\n\r\t')), "printable is used in a regex and must not contain any newlines, tabs, or carriage returns"
    test_value = u'vaulted value'
    vault = VaultLib([])
    encrypted_value = vault.encrypt(u'$ANSIBLE_VAULT;1.1;AES256\n6364303633306165633864303939363166333862393266353964633739326236636133313562343463\n' + text_type(test_value), u'secret')
   

# Generated at 2022-06-22 11:31:08.022821
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    data = text_type(u'\x0a\x0b\x0c', 'utf-8')
    result = dumper.represent_binary(data)
    assert '!!binary' in result
    assert '\\n\\v\\f' in result



# Generated at 2022-06-22 11:31:12.060960
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib('foo')
    secret = "string to encrypt"
    data = AnsibleVaultEncryptedUnicode(vault.encrypt(secret).decode())
    assert data._ciphertext.decode() == AnsibleDumper.represent_vault_encrypted_unicode(None, data)

# Generated at 2022-06-22 11:31:15.747572
# Unit test for function represent_undefined
def test_represent_undefined():
    class UndefinedLike:
        def __bool__(self):
            return False

    assert yaml.dump(UndefinedLike(), default_flow_style=True, Dumper=AnsibleDumper) == ''

# Generated at 2022-06-22 11:31:25.905229
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml.loader import AnsibleLoader

    def test_unicode_to_binary(u):
        assert text_type(u) == (u'\u00AA')
        b = binary_type(u)
        assert binary_type(u) == ('\xc2\xaa')

        dumper = AnsibleDumper
        d = dumper.represent_binary(dumper, b)
        assert d == ("!!binary |-\n  wqQ=\n")

        l = AnsibleLoader(d)
        b2 = l.get_single_data()
        assert b2 == b

    test_unicode_to_binary(u'\u00AA')

# Generated at 2022-06-22 11:31:36.053105
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:31:42.014177
# Unit test for function represent_unicode
def test_represent_unicode():
    ans_unicode = AnsibleUnicode("unicode")
    ans_binary = AnsibleUnicode(b"binary")
    ans_unsafe_text = AnsibleUnsafeText("unsafe_text")
    ans_unsafe_bytes = AnsibleUnsafeBytes(b"unsafe_bytes")

    res = yaml.dump([
        ans_unicode,
        ans_binary,
        ans_unsafe_text,
        ans_unsafe_bytes,
    ])

    assert res == text_type("""- unicode
- binary
- unsafe_text
- unsafe_bytes
""")

# Generated at 2022-06-22 11:31:51.596523
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('My secret value')
    expected = u'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          31323334626533356437613064343332366334623465363837623463393137613938636233316579\n          860a0d0a'
    repr_dumper = AnsibleDumper()
    actual = repr_dumper.represent_vault_encrypted_unicode(data)
    assert  expected == actual

# Generated at 2022-06-22 11:32:02.927583
# Unit test for function represent_unicode
def test_represent_unicode():
    test1 = AnsibleUnicode("This is a unit test")
    test2 = AnsibleUnsafeText("This is a unit test")
    test3 = AnsibleUnsafeBytes("This is a unit test")

    rep1 = yaml.representer.SafeRepresenter.represent_str(AnsibleDumper, test1)
    rep2 = yaml.representer.SafeRepresenter.represent_str(AnsibleDumper, test2)
    rep3 = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, test3)

    if isinstance(rep1, text_type) and isinstance(rep2, text_type) and isinstance(rep3, text_type):
        return rep1, rep2, rep3

# Generated at 2022-06-22 11:32:12.171770
# Unit test for function represent_binary
def test_represent_binary():
    # AnsibleUnsafeBytes, should be returned as binary
    assert yaml.dump(AnsibleUnsafeBytes("\x06\xa9\xab\xae"), Dumper=AnsibleDumper) == '!!binary "Fqg="\n'
    # Other bytes, must be returned as str
    assert yaml.dump(b"\x06\xa9\xab\xae", Dumper=AnsibleDumper) == '"\\x06\\xa9\\xab\\xae"'
    # Special case for octal escaping
    assert yaml.dump(b"\007", Dumper=AnsibleDumper) == "'\\a'"
    # Special case for utf-8 encoding

# Generated at 2022-06-22 11:32:17.726441
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    actual = yaml.dump(AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256;dummy_id\ndummy_value'), Dumper=AnsibleDumper)
    expected = '!vault |\n  $ANSIBLE_VAULT;1.1;AES256;dummy_id\n  dummy_value\n'
    assert actual == expected

# Generated at 2022-06-22 11:32:24.347901
# Unit test for function represent_binary
def test_represent_binary():
    from .. import tree

    # Note: literal block style will not work because of current limitations
    # in PyYAML.  A future improvement would be to detect if "|" works, and
    # fall back to a plain scalar if it does not.

    for value in (u'', u'abcd', u'!'):
        assert tree.to_yaml(value) == u"%s\n" % value



# Generated at 2022-06-22 11:32:32.519322
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Create a unicode object with simple string
    data = AnsibleVaultEncryptedUnicode('cipherext')
    # Create an AnsibleDumper object and use it to represent the data
    # Note: Need to pass a stream object to AnsibleDumper
    stream = open('/dev/null', 'w')
    dumper = AnsibleDumper(stream)
    output = dumper.represent_vault_encrypted_unicode(data)
    # Test result based on YAML format
    assert output == "!vault |\n          cipherext\n          "

# Generated at 2022-06-22 11:32:39.461695
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    expected = u"test_represent_unicode"
    to_dump = AnsibleUnicode(u"test_represent_unicode")
    actual = dumper.represent_data(to_dump)
    assert actual == expected
    to_dump = AnsibleUnicode(u"test_represent_unicode")
    actual = dumper.represent_data(to_dump)
    assert actual == expected
    input_dict = {u"test": AnsibleUnicode(u"test_represent_unicode")}
    expected = u"{test: test_represent_unicode}"
    actual = dumper.represent_data(input_dict)
    assert actual == expected



# Generated at 2022-06-22 11:32:50.628972
# Unit test for function represent_binary

# Generated at 2022-06-22 11:32:58.127564
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('test')
    assert represent_vault_encrypted_unicode(Dumper(), data) == '!vault |\n          AAAAAAEEAgAAAAAAEQAAABQAAAAAeAAAABN/agCP/cEtq3/tYX68go16hH2\n          I/O8RVyaNlJh1rVd0T0TUmQVX9m17li/10VzsWf/FA7Vm1U=\n'

# Generated at 2022-06-22 11:33:08.201409
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    encrypted_text = binary_type(b'U2FsdGVkX1/c6QNe0S0SMMX9SdFyfjzD4me4kywU6lk=\n')
    encrypted_str = AnsibleVaultEncryptedUnicode(ciphertext=encrypted_text)
    plaintext_text = binary_type(b'This is the plaintext\n')
    plaintext_str = AnsibleUnicode(plaintext_text)

    plaintext_file = open('plaintext.yml', 'w')
    plaintext_file.write(yaml.dump(plaintext_str, Dumper=AnsibleDumper))
    plaintext_file.close()

    # If the plaintext file is the same as the encrypted text, then the
    # safe loader will correctly decode the literal style

# Generated at 2022-06-22 11:33:13.314558
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes  # pylint: disable=import-outside-toplevel
    dumper = AnsibleDumper
    bytes = b'\xff'
    assert '!!binary |\n  //8=' == dumper.represent_binary(dumper, AnsibleUnsafeBytes(bytes))



# Generated at 2022-06-22 11:33:24.859285
# Unit test for function represent_unicode
def test_represent_unicode():
    assert(represent_unicode(AnsibleDumper, 'foo') == represent_unicode(AnsibleDumper, AnsibleUnicode('foo')))
    assert(represent_unicode(AnsibleDumper, 'foo') == represent_unicode(AnsibleDumper, AnsibleUnsafeText('foo')))
    assert(represent_unicode(AnsibleDumper, 'foo'.encode('utf-8')) == represent_unicode(AnsibleDumper, AnsibleUnsafeBytes('foo')))

    assert(yaml.representer.SafeRepresenter.represent_str(AnsibleDumper, 'foo') == represent_unicode(AnsibleDumper, AnsibleUnicode('foo')))

# Generated at 2022-06-22 11:33:33.737464
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:33:44.371001
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:33:50.234103
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import StringIO

    text = 'Test ÄÖÜ!'
    data = b(text).decode('utf-8')

    stream = StringIO()
    AnsibleDumper(stream=stream, default_flow_style=False).represent_data(data)
    assert stream.getvalue() == "!!binary \"%s\"\n" % text

# Generated at 2022-06-22 11:34:00.415461
# Unit test for function represent_undefined
def test_represent_undefined():

    def test_fn():
        pass

    # To test represent_undefined requires a StrictUndefined object,
    # which isn't directly available in Ansible
    # But it is available in jinja2.runtime
    # To use this, need to patch up import errors as jinja is
    # not a dependency of ansible
    try:
        import jinja2.runtime
        strict_undefined = jinja2.runtime.StrictUndefined
    except Exception:
        strict_undefined = None

    # If we have StrictUndefined, then test represent_undefined,
    # otherwise just pass (it isn't used)
    if strict_undefined:
        Dumper = AnsibleDumper

        dumper = Dumper()

# Generated at 2022-06-22 11:34:05.636262
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    text = 'swordfish'
    value = AnsibleVaultEncryptedUnicode(text)
    expected = "!vault |\n          %s\n" % text
    result = dumper.represent_vault_encrypted_unicode(value)
    assert result == expected

# Generated at 2022-06-22 11:34:09.332532
# Unit test for function represent_unicode
def test_represent_unicode():
    # Test unsafe value
    plain_value = '\nabc \ndef\r\n'
    assert yaml.dump(plain_value, Dumper=AnsibleDumper) == "\"\\nabc \\ndef\\r\\n\"\n"

    # Test safe value
    safe_value = AnsibleUnsafeText(plain_value)
    assert yaml.dump(safe_value, Dumper=AnsibleDumper) == "\"\\nabc \\ndef\\r\\n\"\n"



# Generated at 2022-06-22 11:34:13.744550
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper(None)
    yaml_data = u'foo'
    assert yaml.representer.SafeRepresenter.represent_str(dumper, yaml_data) == dumper.represent_unicode(AnsibleUnicode(yaml_data))

# Generated at 2022-06-22 11:34:17.911004
# Unit test for function represent_undefined
def test_represent_undefined():
    obj = AnsibleUndefined(name="test")
    expected_output = yaml.representer.SafeRepresenter.represent_str(AnsibleDumper, text_type("test"))

    output = AnsibleDumper.represent_undefined(obj)

    assert output == expected_output

# Generated at 2022-06-22 11:34:32.241833
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:34:33.965601
# Unit test for function represent_binary
def test_represent_binary():
    r = represent_binary(None, b'passed')
    assert(r == 'passed')



# Generated at 2022-06-22 11:34:37.031022
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes(b'\x00\x01\x02')
    d = AnsibleDumper()
    assert d.represent_binary(data) == u'!!binary |\n  AAEC\n'

# Generated at 2022-06-22 11:34:42.190315
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars(is_unsafe=False)
    hv['ansible_ssh_host'] = "some_host"
    hv['ansible_host'] = "some_host:7999"
    hv['ansible_user'] = "test_user"
    hv['ansible_connection'] = "local"
    assert yaml.dump(hv, Dumper=AnsibleDumper) == "{ansible_connection: local, ansible_host: 'some_host:7999', ansible_ssh_host: some_host, ansible_user: test_user}\n"

# Generated at 2022-06-22 11:34:48.759200
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    dumper.dispose()
    undefined = AnsibleUndefined('no value for defined object foo.bar')
    dumper.add_representer(
        AnsibleUndefined,
        represent_undefined,
    )
    assert True is bool(undefined)
    assert bool(False) is False
    out = yaml.dump(undefined, Dumper=dumper)
    assert out == 'no value for defined object foo.bar\n...\n'

# Generated at 2022-06-22 11:34:55.145331
# Unit test for function represent_undefined
def test_represent_undefined():
    import pytest
    a_str = "not_none"
    dummy = AnsibleUndefined
    def _fail_with_undefined_error(msg):
        raise AssertionError("UndefinedError should not be raised")
    dumper = AnsibleDumper()
    dumper._fail_with_undefined_error = _fail_with_undefined_error
    try:
        represent_undefined(dumper, a_str)
    except AssertionError as e:
        pytest.fail("AssertionError should not be raised")
    try:
        represent_undefined(dumper, dummy)
    except AssertionError as e:
        pytest.fail("AssertionError should not be raised")

# Generated at 2022-06-22 11:34:59.795230
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.module_utils._text import to_bytes

    test_password = 'test_password'
    test_data = ['some', 'test', 'data', {'to': 'test'}]
    vault = VaultLib([to_bytes(test_password)])
    vault_text = VaultEditor.dump_yaml(vault, test_data)

    assert isinstance(vault_text, AnsibleVaultEncryptedUnicode)

    represented = yaml.safe_dump([vault_text], default_flow_style=False, Dumper=AnsibleDumper)


# Generated at 2022-06-22 11:35:11.582768
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode(value='hello', version=2)

# Generated at 2022-06-22 11:35:19.389043
# Unit test for function represent_hostvars
def test_represent_hostvars():

    dumper = yaml.dumper.SafeDumper()
    dumper.add_representer(
        HostVars,
        represent_hostvars,
    )

    data = HostVars()
    data["var"] = "value"
    data.add_source("file1")
    data["extra_var"] = "extra_value"
    data.add_source("file2")

    expected = u"file2: {extra_var: extra_value}\nfile1: {var: value}"

    result = yaml.dump(data, Dumper=dumper, default_flow_style=False)

    assert result == expected

# Generated at 2022-06-22 11:35:21.728527
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper) == ''

# Generated at 2022-06-22 11:35:28.452570
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    A = AnsibleVaultEncryptedUnicode(u'somestring')
    assert A._ciphertext == u'somestring'
    representer = AnsibleDumper()
    assert representer.represent_unicode(A) == u'!vault |\n          c29tZXN0cmluZw==\n'

# Generated at 2022-06-22 11:35:33.267345
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(width=1000)
    d = b'\x00\x01\x02'
    d_quoted = dumper.represent_binary(d)

    assert d_quoted == '!!binary |\n  AAEC', "Should quote binary string"

# Generated at 2022-06-22 11:35:42.901780
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_vault_encrypted_unicode(
        'some_encryption_string'
    ) == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          35306339643965333733663610a663934383964333835623432616235393235326532643864346164\n          64633934353366393965663363383561320a3237383065663665623231383037366432616437643534\n          376564373832326537306364323162363738303364343331623330656236"



# Generated at 2022-06-22 11:35:44.944373
# Unit test for function represent_undefined
def test_represent_undefined():
    data = yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)
    assert data == '{}'



# Generated at 2022-06-22 11:35:53.289191
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(AnsibleDumper, AnsibleVaultEncryptedUnicode('This is a test!')) == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          34353736373664633031336132333563353735646635386436626637643466653261643834633363\n          6133613130663835386634336265663935333932386362662d3d0a\n"


# Generated at 2022-06-22 11:36:04.038680
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    # Set up a simple vault object
    obj = AnsibleVaultEncryptedUnicode(text_type("$ANSIBLE_VAULT;1.1;AES256"))
    obj._ciphertext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Set up a dumper
    from StringIO import StringIO
    sf = StringIO()
    dumper = yaml.SafeDumper(sf)

    # Play the representer
    represent_vault_encrypted_unicode(dumper, obj)

    # Verify the vault object was encoded properly
    assert sf.getvalue() == '!vault |\n  AgAAAAA'

# Generated at 2022-06-22 11:36:13.033398
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # test ansible_facts
    d = {'1': 1, '2': '2'}
    dumper = AnsibleDumper
    result = dumper.represent_hostvars(dumper, d)
    assert isinstance(result, yaml.nodes.MappingNode)
    assert len(result.value) == len(d)
    # test ansible_vars
    d = {'name': 'Alice'}
    result = dumper.represent_hostvars(dumper, d)
    assert isinstance(result, yaml.nodes.MappingNode)
    assert len(result.value) == len(d)


# Generated at 2022-06-22 11:36:16.122819
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    dumper.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )
    res = dumper.represent_binary(dumper, b'foo\n')
    assert res == u'!binary |\n  Zm9vCg==\n'

# Generated at 2022-06-22 11:36:21.601979
# Unit test for function represent_undefined
def test_represent_undefined():
    x = AnsibleDumper.represent_undefined(None, AnsibleUndefined)
    assert isinstance(x, bool), "represent_undefined should return bool"
    assert x is False, "represent_undefined should return bool False"
    x = AnsibleDumper.represent_undefined(None, AnsibleUndefined('foo'))
    assert x is False, "represent_undefined should return bool False"

# Generated at 2022-06-22 11:36:32.978921
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    This test ensures that AnsibleUndefined objects are not dumped to YAML.

    AnsibleUndefined is a subclass of Jinja2 StrictUndefined. Jinja 2
    implements a __bool__ method that always returns False. To test this
    AnsibleDumper uses the bool() call to ensure the AnsibleUndefined object
    is not dumped to YAML.

    For this test, the bool() method is temporarily replaced by a mock that
    raises an exception. If the code is working correctly and we are not
    trying to dump AnsibleUndefined to YAML, the exception will not be
    raised and a True will be returned from the test.

    :return: True if the test passes.
    :rtype: bool
    '''
    import mock

    test_bool = mock.Mock(name='test_bool')
    test

# Generated at 2022-06-22 11:36:41.156985
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:36:42.686992
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.dump(HostVars({}), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:36:51.613849
# Unit test for function represent_undefined
def test_represent_undefined():
    # If a variable contains a dict with a variable that is undefined
    # then the variable will be rendered as an empty dict instead of
    # as None. Hence, we need to add an extra test in the function
    # represent_undefined to ensure we render the variable as None.
    # The test below checks that.
    from ansible.template import AnsibleUndefined
    from yaml.representer import RepresenterError

    dumper = AnsibleDumper(allow_unicode=True)
    try:
        dumper.represent_data({'key': AnsibleUndefined()})
    except RepresenterError:
        pass
    else:
        assert False, 'A RepresenterError should have been raised'

# Generated at 2022-06-22 11:36:58.423285
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    test_hostvars = HostVars(host=dict(host_specified_var='host_specified_value'))
    result = yaml.safe_dump(test_hostvars, default_flow_style=False, Dumper=AnsibleDumper, encoding='utf-8', allow_unicode=True)

    # When converting to yaml and back, the HostVars object should be serialized as a simple dictionary
    assert result == u'{host: {host_specified_var: host_specified_value}}\n'

# Generated at 2022-06-22 11:37:03.397588
# Unit test for function represent_binary
def test_represent_binary():
    ''' Test represent_binary function '''
    from ansible.module_utils.six import BytesIO

    buf = BytesIO()
    dumper = AnsibleDumper(buf)
    dumper.represent_binary(b'testdata')

    assert buf.getvalue() == "testdata\n"

# Generated at 2022-06-22 11:37:10.220980
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.hostvars import HostVars
    hv = HostVars('foo')
    hv.update({'a': 'b'})
    assert hv == {'a': 'b'}

    m = AnsibleMapping()
    m.add_field('hv', hv)
    actual = AnsibleDumper().represent_mapping(None, m)
    expected = ('{hv: {a: b}}')
    assert actual == expected

    # Test empty dict with HostVars instance
    hv_empty = HostVars('foo')
    assert hv_empty == {}
    m = AnsibleMapping()
    m.add_field('hv', hv_empty)
    actual = Ansible

# Generated at 2022-06-22 11:37:12.837440
# Unit test for function represent_binary
def test_represent_binary():
    obj = AnsibleUnsafeBytes(u"\xff")
    rep = represent_binary(None, obj)
    expected = "!!binary |\n  /w==\n"
    assert rep == yaml.load(expected)



# Generated at 2022-06-22 11:37:13.954157
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'foo') == ("!!binary |-\n  Zm9v\n")

# Generated at 2022-06-22 11:37:23.187586
# Unit test for function represent_binary
def test_represent_binary():
    binary_value = b'\xc3\xa9'
    dump_value = yaml.dump(binary_value, Dumper=AnsibleDumper, default_flow_style=False)
    assert dump_value == '!!binary |-\n  w6k=\n'

    binary_value = b'\xc3\xa9'
    dump_value = yaml.dump(binary_value, Dumper=AnsibleDumper, default_style='"', default_flow_style=False)
    assert dump_value == '!!binary "|-\n  w6k=\n"'

    binary_value = b'\xc3\xa9'
    dump_value = yaml.dump(binary_value, Dumper=AnsibleDumper, default_style='\'', default_flow_style=False)
   

# Generated at 2022-06-22 11:37:25.947511
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(AnsibleDumper(None), HostVars(None)) == {'_ansible_no_log': False}

# Generated at 2022-06-22 11:37:31.137755
# Unit test for function represent_binary
def test_represent_binary():
    a = AnsibleDumper()
    out = a.represent_binary('\x00\x01\x02\x03\x04')
    assert out == '!!binary |\n  AAECABA==\n'

# Generated at 2022-06-22 11:37:41.150448
# Unit test for function represent_binary
def test_represent_binary():
    yaml.representer.SafeRepresenter.add_representer(
        AnsibleUnsafeBytes, represent_binary
    )

    value = AnsibleUnsafeBytes(b'\xFF\x00\xFF')
    expected = b'!!binary |-\n  //8=\n'
    actual = yaml.dump(value, Dumper=yaml.representer.SafeRepresenter, default_flow_style=False)

    assert actual == expected

    yaml.representer.SafeRepresenter.remove_representer(
        AnsibleUnsafeBytes
    )


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-22 11:37:48.909539
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(default_style='|')
    data = '\xab\xed\xde\xad\xf0\x0d\xbe\xef\xfe\xed'
    result = dumper.represent_binary(data)
    assert result == "{'|': '\\xab\\xed\\xde\\xad\\xf0\\r\\xbe\\xef\\xfe\\xed'}"



# Generated at 2022-06-22 11:37:54.556425
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.safe_dump({u'x': b'\x00\x01'}, default_flow_style=True) == u'{x: !!binary |\n  AAECA\n}'
    assert yaml.safe_dump({u'x': u'\x00\x01'}, default_flow_style=True) == u'{x: AAECA}\n'

# Generated at 2022-06-22 11:38:04.728418
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    output = yaml.dump(
        AnsibleVaultEncryptedUnicode(
            '$ANSIBLE_VAULT;1.2;AES256;ansible\n386343363362303837623334613961343133316238373163303437623330396631623563636637\n393536643662656536353339623364363464353430303166396664356566653963656638353830\n38356365366130396563303634653035646266316236616237630a'),
        Dumper=yaml.dumper.SafeDumper,
        default_flow_style=False
    )

# Generated at 2022-06-22 11:38:06.258814
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(None, HostVars('test')) == "{}"



# Generated at 2022-06-22 11:38:11.628738
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars(vars={'x': 1}, facts={'y': 2}, groups={'z': 3}, happens={'w': 4})
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == '{x: 1, y: 2, z: 3, w: 4}'

# Generated at 2022-06-22 11:38:16.515955
# Unit test for function represent_binary
def test_represent_binary():
    # test for python 2
    if yaml.representer.Binary.yaml_impl.preserve_quotes:
        assert AnsibleDumper.represent_binary(
            None, b'A\x00B\x00C'
        ) == '!!binary |\n  QQBC\n'
    else:
        assert AnsibleDumper.represent_binary(
            None, b'A\x00B\x00C'
        ) == '!!binary "A\\x00B\\x00C"\n'



# Generated at 2022-06-22 11:38:22.186172
# Unit test for function represent_hostvars
def test_represent_hostvars():

    yaml_obj = dict()
    yaml_obj['key1'] = 'a'
    yaml_obj['key2'] = 'b'

    yaml_string = yaml.dump(HostVars(yaml_obj), Dumper=AnsibleDumper)

    assert yaml_string == '{key1: a, key2: b}\n'



# Generated at 2022-06-22 11:38:32.940983
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    ciphertext = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\r\n'
                                              '306234336433312d643232392d616630652d613561392d656332\r\n'
                                              '323163383264333166633033370a\r\n')
    assert(yaml.dump(ciphertext, Dumper=AnsibleDumper) == '!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  306234336433312d643232392d616630652d613561392d656332\n  323163383264333166633033370a\n\n')



# Generated at 2022-06-22 11:38:41.242018
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    class FakeData:
        _ciphertext = b'Pi5v+'
    assert represent_vault_encrypted_unicode(None, FakeData()) == u'!vault |\n  Pi5v+'

# Generated at 2022-06-22 11:38:43.439037
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper(default_flow_style=False)
    assert yaml.representer.SafeRepresenter.represent_str(dumper, b'foo') == \
        yaml.representer.SafeRepresenter.represent_binary(dumper, b'foo')

# Generated at 2022-06-22 11:38:54.927894
# Unit test for function represent_hostvars
def test_represent_hostvars():
    ansible_dumper = yaml.Dumper(AnsibleDumper)
    assert ansible_dumper.represent_dict({"a": "b"}) == u'{a: b}\n...\n', "Dictionary not represented correctly."
    assert ansible_dumper.represent_dict(HostVars({"a": "b"})) == u'{a: b}\n...\n', "Hostvars not represented correctly."
    assert ansible_dumper.represent_dict(HostVarsVars({"a": "b"})) == u'{a: b}\n...\n', "HostvarsVars not represented correctly."

# Generated at 2022-06-22 11:39:05.290793
# Unit test for function represent_binary
def test_represent_binary():
    from distutils import version

    if version.LooseVersion(yaml.__version__) < version.LooseVersion('5.1'):
        # If PyYAML is less then 5.1, binary representation style is not set which
        #  cause the following failure:
        #  TypeError: u'\u2713' is invalid base64
        # If PyYAML is greater or equal to 5.1, binary representation style is set
        # to '|' which without any encoding.
        # is not producing any error.

        data = '\u2713'
        dumper = AnsibleDumper
        dumper.allow_unicode = True

        # The following should not produce any error:
        dumper.represent_binary(data)



# Generated at 2022-06-22 11:39:07.754601
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'\x80\xFF') == '!!binary |\n  gIC8/w==\n'

# Generated at 2022-06-22 11:39:15.631164
# Unit test for function represent_hostvars
def test_represent_hostvars():

    from units.mock.loader import DictDataLoader

    hv = HostVars(loader=DictDataLoader({'add_host': {"hostname": "testhost"}}))

    class FakeVarsModule(object):
        params = dict(test1="test1", test2="test2")

    hv.set_variable("add_host", "testhost", FakeVarsModule())

    result = yaml.safe_dump({'add_host': hv}, default_flow_style=False, Dumper=AnsibleDumper)
    assert result == """add_host:
  '{{ ansible_managed }}': This file is managed by the Ansible 'Ansible'
  testhost:
    params:
      test1: test1
      test2: test2
"""

# Generated at 2022-06-22 11:39:19.284504
# Unit test for function represent_hostvars
def test_represent_hostvars():
    s = AnsibleDumper({'foo': 'bar'}).represent_hostvars({'foo': 'bar'})
    assert s == '{foo: bar}\n...\n'


# Generated at 2022-06-22 11:39:24.405491
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    string_to_dump = AnsibleVaultEncryptedUnicode('Vault data to be dumped')
    # No need to specify _get_yaml_loader() because the representation
    # of data is all we need in this case
    string_representation = yaml.dump(string_to_dump)
    assert string_representation == "!vault |\n  Vault data to be dumped"

# Generated at 2022-06-22 11:39:29.795165
# Unit test for function represent_hostvars
def test_represent_hostvars():
    represent_hostvars_obj = AnsibleDumper.dispatch[HostVars.__repr__]
    isinstance(represent_hostvars_obj, (type(yaml.representer.SafeRepresenter.represent_dict)))

default_flow_style = ansible_yaml = yaml.dump

# Generated at 2022-06-22 11:39:35.667857
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Base class HostVars
    test_hostvars = HostVars()
    assert test_hostvars.vars == {}

    # Subclass HostVarsVars
    test_hostvarsvars = HostVarsVars()
    assert test_hostvarsvars.vars == {}

    # Subclass VarsWithSources
    test_varswithsources = VarsWithSources()
    assert test_varswithsources.vars == {}
    assert test_varswithsources.source == 'unknown'