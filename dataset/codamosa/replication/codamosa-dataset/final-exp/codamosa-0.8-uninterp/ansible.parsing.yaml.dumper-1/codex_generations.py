

# Generated at 2022-06-22 11:29:47.790761
# Unit test for function represent_undefined
def test_represent_undefined():
    d = AnsibleDumper()
    undef = AnsibleUndefined()
    # _fail_with_undefined_error will be called if the representation of
    # undef is False
    assert d.represent(undef) is True



# Generated at 2022-06-22 11:29:54.461822
# Unit test for function represent_hostvars
def test_represent_hostvars():

    from ansible.template import Templar

    templar = Templar(loader=None)
    dumper = AnsibleDumper()
    dump_data = dumper.represent_data(dict(var1="value1"))

    hv = HostVars(hostname="hostname", inventory="inventory")
    hv.load_vars = load_vars = {'_ansible_verbose_always': True}
    load_vars['some_var'] = templar.template("{{ value }}", dict(value="{{ some_other_var }}"), fail_on_undefined=False)
    load_vars['some_var']._finalized = True
    load_vars['some_other_var'] = templar.template("value", {}, fail_on_undefined=False)

# Generated at 2022-06-22 11:29:59.944235
# Unit test for function represent_binary
def test_represent_binary():
    safe_dumper = yaml.representer.SafeRepresenter()
    string_b = "some string\nwith\nmulti-line\n"
    string_unicode = u"some unicode\nwith\nmulti-line\n"
    string_ascii_b = b"some ascii\nwith\nmulti-line\n"

    # Test using ascii
    ascii_b = yaml.compat.binary_type("some ascii\nwith\nmulti-line\n")
    dump = yaml.dump(ascii_b, allow_unicode=False, default_flow_style=False)

# Generated at 2022-06-22 11:30:03.618238
# Unit test for function represent_hostvars
def test_represent_hostvars():

    test_hostvars = HostVars(host_name='testhost', host_vars=dict(x=5))
    output = yaml.dump(test_hostvars, Dumper=AnsibleDumper)
    assert b'testhost:' in output
    assert b'x: 5' in output



# Generated at 2022-06-22 11:30:11.417177
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''
    This is a simple test to ensure we are taking the correct data
    and rendering it
    '''

# Generated at 2022-06-22 11:30:21.725877
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault_secret = VaultLib([])
    vault_value = vault_secret.encrypt('test')
    assert vault_value == '$ANSIBLE_VAULT;1.1;AES256\n30643739353633353038333363633376364313438373466653633663613365303232376666386536\n396462643537343632373165636437333662616466636366620a3735343536313939373037323035\n38393166623431636332633966343364663632316530653137383565343930353063656333633663\n6463303332633665613731350a'

# Generated at 2022-06-22 11:30:31.237190
# Unit test for function represent_hostvars
def test_represent_hostvars():
    ''' ansible.parsing.yaml.dumper.represent_hostvars '''

    from ansible.parsing.yaml.objects import AnsibleMapping

    source = 'foo.yml'
    debug = 'test'
    hv = HostVars({'test': 'ing'}, sources=set([source]))

    d = AnsibleDumper()
    assert d.represent_dict(hv) == d.represent_dict(dict(hv))
    assert d.represent_dict(hv) == d.represent_dict({'test': 'ing'})

    assert type(d.represent_dict(hv)) is AnsibleMapping
    assert d.represent_dict(hv) == dict({'test': 'ing'})


# Generated at 2022-06-22 11:30:44.230814
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml_data = """
    foo: bar
    baz:
        - qux
    undefined: '{{ foo }}'
    """
    data = yaml.full_load(yaml_data)
    yaml.dump(data, None, Dumper=AnsibleDumper)
    yaml.dump(data, None, Dumper=AnsibleDumper, default_flow_style=True)

    yaml_data = """
    foo: bar
    baz:
        - qux
    undefined: 
        - '{{ foo }}'
        - '{{ baz }}'
    """
    data = yaml.full_load(yaml_data)
    yaml.dump(data, None, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:47.089871
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    results = dumper.represent_binary(dumper, u'\u0085'.encode('utf-8'))
    assert results == "'\\x85'"



# Generated at 2022-06-22 11:30:57.635390
# Unit test for function represent_unicode
def test_represent_unicode():

    from ansible.vars.unsafe_proxy import wrap_var

    # Test the represent_unicode function with a regular string
    s = AnsibleUnicode('this is a string')
    ystr = yaml.dump(s, Dumper=AnsibleDumper)
    assert ystr == u'this is a string\n...\n'

    # Test the represent_unicode function with a unicode string
    unicode_string = u'\u20ac'
    uni = AnsibleUnicode(unicode_string)
    ystr = yaml.dump(uni, Dumper=AnsibleDumper)
    assert ystr == u'\u20ac\n...\n'

    # Test the represent_unicode function with a variable

# Generated at 2022-06-22 11:31:09.179188
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    result = yaml.dump({'foo': AnsibleVaultEncryptedUnicode(b'asdf')}, default_flow_style=False, Dumper=AnsibleDumper)
    assert result == "foo: !vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  34393635306431636434363631366166646566343364666565343538656436356163626539396538\n  62613831376135613663306466633562633262376364356366653339306463653539623532666232\n  346536626639623330386334383963650a\n"

# Generated at 2022-06-22 11:31:18.211901
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper(width=0)
    encrypted = AnsibleVaultEncryptedUnicode('test')
    assert dumper.represent_vault_encrypted_unicode(encrypted) == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          64726362343261376461316663376235633766666132653434636564646235386231623435643033\n          32343638646635613239663536383230633163653534666333643737306334393663306266623137\n          66353834653434623232627D\n"

# Generated at 2022-06-22 11:31:29.719931
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    ciphertext = binary_type('$ANSIBLE_VAULT;1.1;AES256;'
                             'foo\n33646432393539366239363537626162383634316265343938313734333933323765326664'
                             '63653938323031316262383731613363396133393437346336\n')

    vault = AnsibleVaultEncryptedUnicode(ciphertext)

    dumper = AnsibleDumper()

    yaml_data = dumper.represent_vault_encrypted_unicode(vault)


# Generated at 2022-06-22 11:31:35.542760
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    from collections import namedtuple
    variables = namedtuple('hostvars', ['vars'])
    hostvars = HostVars(variables(vars={'foo': 'bar'}))
    assert dumper.represent_hostvars(dumper, hostvars) == dumper.represent_dict(dict(hostvars))



# Generated at 2022-06-22 11:31:37.775628
# Unit test for function represent_undefined
def test_represent_undefined():
    testInput = AnsibleUndefined('inputresult')
    testInputBool = bool(testInput)
    expectedOutput = True
    assert testInputBool == expectedOutput

# Generated at 2022-06-22 11:31:39.803018
# Unit test for function represent_undefined
def test_represent_undefined():
    # Test not wrapped in a with statement because we want the failure
    # to make the unit test fail
    represent_undefined(AnsibleDumper, AnsibleUndefined())



# Generated at 2022-06-22 11:31:43.800023
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, u'\u0100') == yaml.representer.SafeRepresenter.represent_unicode(dumper, u'\u0100')
    assert dumper.represent_binary(dumper, b'\x80') == yaml.representer.SafeRepresenter.represent_bytes(dumper, b'\x80')

# Generated at 2022-06-22 11:31:47.302560
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode(b'vaulted_value')

    output = yaml.dump(data, Dumper=AnsibleDumper)

    assert output == '!vault |\n  vaulted_value\n'

# Generated at 2022-06-22 11:31:50.146069
# Unit test for function represent_unicode
def test_represent_unicode():
    obj = AnsibleUnicode(u'unicode')
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(obj) == 'unicode'

# Generated at 2022-06-22 11:31:54.080841
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Data should be represented as dictionary
    assert yaml.dump(HostVars({'foo': 'bar'}), Dumper=AnsibleDumper) == '{foo: bar}\n...\n'

# Generated at 2022-06-22 11:32:03.225099
# Unit test for function represent_hostvars
def test_represent_hostvars():
    obj = HostVars(
        {'foo': 'bar'},
        vault_files=['/opt/vault'],
        vault_passwords=['/opt/vault_pass']
    )
    assert yaml.safe_dump(obj, default_flow_style=True).rstrip() == "- foo: bar\n  vault_files: ['/opt/vault']\n  vault_passwords: ['/opt/vault_pass']"


# Generated at 2022-06-22 11:32:12.252133
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, b'1') == '!!binary |\n  MQ==\n'
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, b'1234567890') == '!!binary |\n  MTIzNDU2Nzg5MA==\n'
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, '1') == '!!binary |\n  MQ==\n'
    assert yaml.representer.SafeRepresenter.represent_binary(dumper, '1234567890') == '!!binary |\n  MTIzNDU2Nzg5MA==\n'

# Generated at 2022-06-22 11:32:16.569550
# Unit test for function represent_binary
def test_represent_binary():
    binary_data = b"Hello World"
    data = AnsibleUnsafeBytes(binary_data)
    result =  AnsibleDumper.represent_binary(None, data)
    assert result == u'!binary |\n  SGVsbG8gV29ybGQ=\n'


# Generated at 2022-06-22 11:32:27.067618
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    ctext = '$ANSIBLE_VAULT;1.1;AES256\n' \
            '3061623663643139633132313363643333323263653465363661356236356665323932626261610a' \
            '30643936396437626135313739623161623963383365633162626463323832643935363639610a' \
            '653739666163656639373466653331383963343834626539383037373633643462623364363732\n'

# Generated at 2022-06-22 11:32:30.250601
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    input_byte_string = '\xff'
    assert dumper.represent_binary(input_byte_string) == yaml.representer.SafeRepresenter.represent_binary(dumper, input_byte_string)

# Generated at 2022-06-22 11:32:32.788340
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = AnsibleMapping({'key_1': AnsibleUnicode('value_1')})
    assert yaml.dump({'key_1': 'value_1'}, Dumper=AnsibleDumper) == yaml.dump(data, Dumper=AnsibleDumper)


# Generated at 2022-06-22 11:32:35.706911
# Unit test for function represent_binary
def test_represent_binary():
    yaml_dump = yaml.dump("\x00\xff\xfe\xfd\n\\\u1234", Dumper=AnsibleDumper)
    assert yaml_dump == "!!binary |\n  AA/9/w4=\n", yaml_dump

# Generated at 2022-06-22 11:32:38.916702
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml_data = yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)
    if yaml_data != '':
        raise AssertionError('Unexpected value for represent_undefined.')

# Generated at 2022-06-22 11:32:47.833615
# Unit test for function represent_binary
def test_represent_binary():
    assert(yaml.dump(u'ansible', Dumper=AnsibleDumper) == 'ansible\n...\n')
    assert(yaml.dump(u'ansible', AnsibleDumper)).encode('utf-8') == 'ansible\n...\n'.encode('utf-8')
    assert(yaml.dump(b'ansible', Dumper=AnsibleDumper) == 'ansible\n...\n')
    assert(yaml.dump(b'ansible', AnsibleDumper)).encode('utf-8') == 'ansible\n...\n'.encode('utf-8')

# Generated at 2022-06-22 11:32:54.859025
# Unit test for function represent_hostvars
def test_represent_hostvars():

    representer = AnsibleDumper.represent_hostvars

    # Dict
    assert representer(AnsibleDumper, {'foo': 'bar'}) == yaml.representer.SafeRepresenter.represent_dict(AnsibleDumper, {'foo': 'bar'})
    # Sequence
    assert representer(AnsibleDumper, ['foo', 'bar']) == yaml.representer.SafeRepresenter.represent_dict(AnsibleDumper, {'0': 'foo', '1': 'bar'})
    # String
    assert representer(AnsibleDumper, 'foo') == yaml.representer.SafeRepresenter.represent_dict(AnsibleDumper, {'0': 'foo'})
    # None

# Generated at 2022-06-22 11:32:58.546286
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper(default_style='|').represent_binary(b'foo') == "|\n  foo\n"



# Generated at 2022-06-22 11:33:02.992305
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'a': 'b'}
    hostvars_data = HostVars(data)
    assert yaml.dump(hostvars_data, Dumper=AnsibleDumper) == yaml.dump(data, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:33:09.741186
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # the class HostVars is defined in the module ansible.vars.hostvars
    assert isinstance(HostVars(), dict)
    # the class HostVarsVars is defined in the module ansible.vars.hostvars
    assert isinstance(HostVarsVars(), dict)
    # the class VarsWithSources is defined in the module ansible.vars.manager
    assert isinstance(VarsWithSources(), dict)

# Generated at 2022-06-22 11:33:13.636620
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    result = dumper.represent_vault_encrypted_unicode(b"sample password")
    assert result == "!vault |\n          c2FtcGxlIHBhc3N3b3Jk\n"

# Generated at 2022-06-22 11:33:20.371314
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()

    data = AnsibleUnicode(value=u"hello world")
    assert dumper.represent_unicode(data) == u"hello world"

    data = AnsibleUnicode(value=True)
    assert dumper.represent_unicode(data) == u"True"

    data = AnsibleUnicode(value=False)
    assert dumper.represent_unicode(data) == u"False"



# Generated at 2022-06-22 11:33:23.348377
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(u'dummy') == u'"dummy"\n'

# Generated at 2022-06-22 11:33:27.509715
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars('localhost')
    hv.add_host_var(HostVarsVars('localhost', dict({"a": 1})))
    result = yaml.dump(hv, Dumper=AnsibleDumper)
    assert result == 'a: 1\n'

# Generated at 2022-06-22 11:33:34.686269
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''
    Validate the behaviour of represent_hostvars by making sure
    that we can dump HostVars to yaml.

    We expect that ansible.vars.hostvars.HostVars will be serialized
    to a yaml object mapping hostname to a yaml object mapping
    key to value.
    '''
    v = HostVars(vars={"a": "hello", "b": {"c": "world"}})
    assert yaml.dump(v, Dumper=AnsibleDumper) == "one:\n  a: hello\n  b:\n    c: world\n"



# Generated at 2022-06-22 11:33:39.443764
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    x = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;TEST')
    y = represent_vault_encrypted_unicode(AnsibleDumper, x)
    assert y == '!vault |\n  $ANSIBLE_VAULT;1.1;TEST\n'


# Generated at 2022-06-22 11:33:45.248157
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from io import BytesIO

    data = HostVars({'foo': 'bar'})
    expected = u'{foo: bar}\n...\n'

    output = BytesIO()
    yaml.dump(data, output, Dumper=AnsibleDumper, default_flow_style=False)
    assert output.getvalue() == expected.encode('utf-8')



# Generated at 2022-06-22 11:33:53.728668
# Unit test for function represent_undefined
def test_represent_undefined():
    data = AnsibleUndefined
    dumper = AnsibleDumper
    dumper.add_representer(AnsibleUndefined, represent_undefined)
    result = dumper.represent_undefined(dumper, data)
    assert(result)



# Generated at 2022-06-22 11:33:58.196289
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(AnsibleDumper, AnsibleVaultEncryptedUnicode(b'aGVsbG8gd29ybGQ=\n')) == u'!vault |\n          aGVsbG8gd29ybGQ=\n'

# Generated at 2022-06-22 11:34:00.875850
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(None, b'test\x00') == AnsibleDumper.represent_scalar(u'tag:yaml.org,2002:binary', 'dGVzdAA=')

# Generated at 2022-06-22 11:34:12.159725
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    plaintext = "s3cr3t"
    ciphertext = vault.encrypt(plaintext)
    encrypted = AnsibleVaultEncryptedUnicode(ciphertext)
    output = yaml.dump(encrypted, Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:34:23.175685
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:34:25.939894
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars(dict(foo='bar'))
    output = yaml.dump(hostvars, Dumper=AnsibleDumper)
    assert output == "foo: bar\n"

# Generated at 2022-06-22 11:34:32.837349
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Input data
    data = AnsibleVaultEncryptedUnicode('a_key', 'a_secret')

    # Expected output
    expected_output = u'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          61315f6b65790a0a61305f736563726574\n          '

    assert represent_vault_encrypted_unicode(data) == expected_output


# Generated at 2022-06-22 11:34:37.826667
# Unit test for function represent_unicode
def test_represent_unicode():
    # Negative test case
    input = dict(data="value")
    assert yaml.dump(input) == yaml.dump(input, Dumper=AnsibleDumper)

    # Positive test case
    input = dict(data=AnsibleUnicode(u"value"))
    assert yaml.dump(input) != yaml.dump(input, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:34:42.473315
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    vault_text = AnsibleVaultEncryptedUnicode('test', b'testvault')
    output = yaml.dump(vault_text, Dumper=AnsibleDumper)
    assert output == '!vault |\n  testvault\n'


# Generated at 2022-06-22 11:34:45.739464
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template.safe_eval import Undefined
    dumper = AnsibleDumper(width=1000000)
    result = dumper.represent_undefined(Undefined)
    assert result is False