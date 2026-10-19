

# Generated at 2022-06-22 11:29:55.480078
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    if not yaml.__with_libyaml__:
        raise SkipTest('libyaml is not installed')

    # Encoding test
    s = b'foo'
    data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          3534333664303764663531666466353062333265373934356663633165656538626236312d636565\n          12383964323062643734633366643933316330363236656438363330613031333161353\n          361303330326438666166343565333064653438326261623339636436363366663065356638\n          63313330666366\n          '

# Generated at 2022-06-22 11:29:59.540902
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    hostvars.update({'my_var': 'my_value'})
    hostvars_dict = dict(hostvars)
    assert type(hostvars_dict) is dict
    assert hostvars_dict == {'my_var': 'my_value'}

# Generated at 2022-06-22 11:30:03.911076
# Unit test for function represent_unicode
def test_represent_unicode():
    data = {u'foo': u'bar'}
    yaml_data = yaml.dump(data, Dumper=AnsibleDumper)
    assert yaml_data == 'foo: bar\n'



# Generated at 2022-06-22 11:30:07.578663
# Unit test for function represent_binary
def test_represent_binary():

    d = AnsibleDumper()
    result = d.represent_binary(b'\xe5\x9b\xba')
    assert result == u':binary |-\n  5L2g5aW9\n'

# Generated at 2022-06-22 11:30:10.471455
# Unit test for function represent_hostvars
def test_represent_hostvars():
    """
    Checks if items in a dictionary are sorted
    """
    data = {'b': 2, 'a': 1}
    new_data = yaml.load(yaml.dump(data, Dumper=AnsibleDumper))
    assert new_data == {'a': 1, 'b': 2}



# Generated at 2022-06-22 11:30:20.842828
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:30:23.083754
# Unit test for function represent_undefined
def test_represent_undefined():
    undefined_value = AnsibleUndefined
    dumper = AnsibleDumper()
    assert bool(represent_undefined(dumper, undefined_value))

# Generated at 2022-06-22 11:30:31.535397
# Unit test for function represent_binary
def test_represent_binary():
    # This creates the basic output structure that ansible uses
    # to store data. It has a string named 'key' with a base64 encoded
    # value.
    assert yaml.dump(dict(key=binary_type(b'foo')), Dumper=AnsibleDumper, default_flow_style=False) == '{key: !!binary "Zm9v"}\n'
    # The assertion below would fail because the string was not
    # encoded as base64. It does not match Zm9v
    #  assert yaml.dump( dict(key='foo') ) == '{key: !!binary "Zm9v"}\n'
    # The assertion below tests that the representation of binary is not
    # in quotes. This would fail because the value of key would be
    # "!!binary \"Zm9v\"" as a string

# Generated at 2022-06-22 11:30:37.880797
# Unit test for function represent_hostvars
def test_represent_hostvars():
    import json

    hostvars = HostVars({"test": "test"})

    result = yaml.dump(hostvars, Dumper=AnsibleDumper)
    assert "!hostvars" not in result
    assert json.loads(result) == {"test": "test"}

# Generated at 2022-06-22 11:30:41.960794
# Unit test for function represent_hostvars
def test_represent_hostvars():

    d = yaml.dump({'_ansible_no_log': True}, Dumper=AnsibleDumper)
    assert d == '{_ansible_no_log: true}\n...\n'


# Unit tests for class AnsibleDumper

# Generated at 2022-06-22 11:30:53.393125
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(AnsibleDumper, HostVars({"foo1": "bar1"})) == "!!python/object/apply:ansible.vars.hostvars.HostVars []\n"
    assert represent_hostvars(AnsibleDumper, HostVarsVars({"foo2": "bar2"})) == "!!python/object/apply:ansible.vars.hostvars.HostVarsVars []\n"
    assert represent_hostvars(AnsibleDumper, VarsWithSources({"foo3": "bar3"})) == "!!python/object/apply:ansible.vars.manager.VarsWithSources []\n"

# Generated at 2022-06-22 11:30:56.555019
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''Test represent_hostvars'''
    d = AnsibleDumper()
    hv = HostVars('foo')
    hv['a'] = 1
    hv['b'] = 2
    assert d.represent_hostvars(hv) == {'a': 1, 'b': 2}



# Generated at 2022-06-22 11:30:59.614463
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, u'foo') == "foo"
    assert represent_unicode(None, u'foo \x01 bar') == u"foo \\x01 bar"



# Generated at 2022-06-22 11:31:09.820887
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars(
        hostname='somehost',
        variables=dict(
            var1='value1',
            var2='value2',
        ),
        variables_file='/path/to/vars/file',
        defaults=dict(
            var3='value3',
            var4='value4',
        ),
        defaults_file='/path/to/defaults/file',
    )
    yaml_snippet = yaml.dump(hv, Dumper=AnsibleDumper, default_flow_style=False)
    assert isinstance(yaml_snippet, text_type)

# Generated at 2022-06-22 11:31:19.916424
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import base64

# Generated at 2022-06-22 11:31:24.044467
# Unit test for function represent_binary
def test_represent_binary():
    data = b'123'
    dumper = yaml.SafeDumper(width=1)

    result = yaml.representer.SafeRepresenter.represent_binary(dumper, data)
    assert result == "!binary |\n  MTIz\n", result
    # Same as above but different way of calling
    result = represent_binary(dumper, data)
    assert result == "!binary |\n  MTIz\n", result


# Generated at 2022-06-22 11:31:27.330862
# Unit test for function represent_unicode
def test_represent_unicode():
    x = AnsibleUnicode(u"foo")
    output = yaml.dump(x, Dumper=AnsibleDumper)
    assert output == u'foo\n...\n'



# Generated at 2022-06-22 11:31:37.358692
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    testData = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.2;AES256;foobar\n3031323334353637383930313233343536373839'
                                            '\n3031323334353637383930313233343536373839')
    testData._ciphertext = b'00012345678901234567890123456789'
    output = represent_vault_encrypted_unicode(None, testData)
    # lines are expected to be output as binary.
    # compare them with b'...' literal
    assert output == b'!vault |\n  00012345678901234567890123456789'

# Generated at 2022-06-22 11:31:44.288606
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''Test representation of AnsibleVaultEncryptedUnicode objects'''
    from ansible.parsing.vault import VaultLib

    # AnsibleVaultEncryptedUnicode(original_bytes)
    secret = AnsibleVaultEncryptedUnicode(VaultLib().encrypt(b'foobar'))

    # Representation
    rep = yaml.safe_dump({'secret': secret}, Dumper=AnsibleDumper)

    # Check result

# Generated at 2022-06-22 11:31:53.831428
# Unit test for function represent_unicode
def test_represent_unicode():
    s = AnsibleUnicode('foo')
    r = represent_unicode(None, s)
    if not isinstance(r, yaml.ScalarNode):
        raise AssertionError("expected ScalarNode, got %s" % repr(r))
    if r.tag != 'tag:yaml.org,2002:str':
        raise AssertionError("expected tag:yaml.org,2002:str, got %s" % repr(r.tag))
    if r.value != 'foo':
        raise AssertionError("expected 'foo', got %s" % repr(r.value))



# Generated at 2022-06-22 11:32:01.760568
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template.templar import Templar

    template_str = '{{ foo }}'
    templar = Templar()
    template_data = templar.template(template_str)
    output = yaml.safe_dump(template_data, Dumper=AnsibleDumper)
    assert isinstance(output, text_type), "Failed to convert output to text"

# Generated at 2022-06-22 11:32:07.837947
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper(width=1024)
    plain = HostVars({'x': 'y'})
    assert represent_hostvars(dumper, plain) == u'{x: y}'
    assert hasattr(plain, '_ansible_vars_cache')
    hvv = HostVarsVars(plain)
    assert represent_hostvars(dumper, hvv) == u'{x: y}'
    assert hasattr(hvv, '_ansible_vars_cache')

# Generated at 2022-06-22 11:32:12.486302
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml_data = yaml.dump(dict(a=dict(a=text_type('Hello World'))), Dumper=AnsibleDumper)
    assert yaml_data == "a:\n  a: Hello World\n"

# Generated at 2022-06-22 11:32:22.756741
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper()
    hostvars = HostVars()
    hostvars.add_host("host1")
    hostvars.add_host("host2")
    hostvars["host1"]["var1"] = "value1"
    hostvars["host1"]["var2"] = "value2"

    expected = u"\n".join([
        '{',
        '    "host1": {',
        '        "var1": "value1",',
        '        "var2": "value2"',
        '    },',
        '    "host2": {}',
        '}',
    ])

    assert dumper.represent_data(hostvars) == expected

# Generated at 2022-06-22 11:32:26.962339
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode("hello"), Dumper=AnsibleDumper) == 'hello\n...\n'
    assert yaml.dump(AnsibleUnicode("hello world"), Dumper=AnsibleDumper) == 'hello world\n...\n'



# Generated at 2022-06-22 11:32:34.142671
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    hostvars.add_host('127.0.0.1')
    hostvars.set('127.0.0.1', 'var1', 'value1')
    hostvars.set('127.0.0.1', 'var2', 'value2')
    dumped = yaml.dump(hostvars, Dumper=AnsibleDumper, default_flow_style=False)
    assert dumped == '''\
127.0.0.1:
  var1: value1
  var2: value2
'''

# Generated at 2022-06-22 11:32:44.227065
# Unit test for function represent_hostvars
def test_represent_hostvars():
    output = AnsibleDumper().represent_hostvars({"foo": 1, "bar": 2})
    assert output is not None, "output for represent_hostvars is None"
    assert isinstance(output, yaml.nodes.MappingNode), "output is not a MappingNode instance"
    assert len(output.value) == 2, "output %s" % output.value
    assert (output.value[0][0].value == 'foo') and (output.value[0][1].value == 1), "output %s" % output.value
    assert (output.value[1][0].value == 'bar') and (output.value[1][1].value == 2), "output %s" % output.value

# Generated at 2022-06-22 11:32:47.881946
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(dict(a=1, b=2))
    d = AnsibleDumper()
    d.represent_hostvars(data) == d.represent_dict(dict(a=1, b=2))



# Generated at 2022-06-22 11:32:52.013871
# Unit test for function represent_unicode
def test_represent_unicode():
    ''' represent_unicode should represent AnsibleUnicode as a yaml string '''
    ansible_unicode = AnsibleUnicode(u'test_string')
    dumps = yaml.dump(ansible_unicode, Dumper=AnsibleDumper, default_flow_style=False)
    assert dumps == 'test_string\n...\n'

# Generated at 2022-06-22 11:32:57.633171
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_data("foo") == "foo\n"
    assert dumper.represent_data("훈민정음") == "훈민정음\n"
    assert dumper.represent_data("𠜎") == "𠜎\n"



# Generated at 2022-06-22 11:33:09.296964
# Unit test for function represent_binary
def test_represent_binary():
    '''Test that our represent_binary works the same as SafeRepresenter.represent_binary.'''
    # Generate a string of 255 bytes.
    # Then append byte 0 to the end to test that code path in represent_binary().
    data = b'\x00' * 255 + b'\x00'
    # SafeRepresenter.represent_binary()
    safe_representer_result = yaml.representer.SafeRepresenter.represent_binary(None, data)
    # Our represent_binary()
    ansible_dumper_represent_binary_result = AnsibleDumper.represent_binary(None, data)
    assert safe_representer_result == ansible_dumper_represent_binary_result

# Generated at 2022-06-22 11:33:17.162032
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'1': '2'}
    v = HostVars(data)
    assert yaml.dump(v, Dumper=AnsibleDumper) == "1: 2\n"

    v = HostVarsVars(data)
    assert yaml.dump(v, Dumper=AnsibleDumper) == "vars:\n  1: 2\n"

    v = VarsWithSources(data)
    assert yaml.dump(v, Dumper=AnsibleDumper) == "vars:\n  1: 2\n"



# Generated at 2022-06-22 11:33:18.845950
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'bytes', Dumper=AnsibleDumper) == "!!binary \"Ynl0ZXM=\"\n"

# Generated at 2022-06-22 11:33:27.769424
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper

    # Test bytes
    test_bytes = b'foo'
    assert yaml.representer.SafeRepresenter.represent_unicode(dumper, test_bytes) == \
        yaml.representer.SafeRepresenter.represent_unicode(dumper, AnsibleUnsafeBytes(test_bytes))

    # Test unicode
    test_unicode = u'foo'
    assert yaml.representer.SafeRepresenter.represent_unicode(dumper, test_unicode) == \
        yaml.representer.SafeRepresenter.represent_unicode(dumper, AnsibleUnsafeText(test_unicode))

# Generated at 2022-06-22 11:33:29.824579
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(None, HostVars({'q': 'r'})) == {'q': 'r'}



# Generated at 2022-06-22 11:33:37.158358
# Unit test for function represent_binary
def test_represent_binary():
    data = '\0'

    # Force the data to be an AnsibleUnsafeBytes
    if isinstance(data, binary_type):
        data = AnsibleUnsafeBytes(data)

    # Create a dumper object
    dumper = AnsibleDumper()

    # Represent AnsibleUnsafeBytes
    data_out = dumper.represent_data(data)
    assert data_out == '!!binary |\n  ' + data.encode('base64').strip()

# Generated at 2022-06-22 11:33:44.648489
# Unit test for function represent_binary
def test_represent_binary():
    res_true = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, b'\x00\x01\x02\x03')
    assert res_true == u'!!binary |\n  AAECAQ==\n'
    res_false = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, b'\x00\x01\x02\x03', style='|')
    assert res_false == u'!!binary |\n  AAECAQ==\n'



# Generated at 2022-06-22 11:33:50.730091
# Unit test for function represent_unicode
def test_represent_unicode():
    class Dumper(AnsibleDumper):
        def represent_scalar(self, tag, value, style=None):
            return value

    rep = Dumper().represent_unicode
    assert rep(u'unicode_str') == u'unicode_str'

    rep = Dumper().represent_unicode
    assert rep(u'unicode_str_?+&') == u'unicode_str_?+&'



# Generated at 2022-06-22 11:33:57.148401
# Unit test for function represent_unicode
def test_represent_unicode():
    """make sure we can represent unicode data"""
    # 1. Verify we can represent unicode by passing in unicode data
    result = yaml.dump({'unicode_test': u'unicode_value'}, Dumper=AnsibleDumper)

    # We must use the safe loader to emulate the behaviour of the serializer
    assert yaml.load(result, yaml.SafeLoader) == {'unicode_test': 'unicode_value'}



# Generated at 2022-06-22 11:34:02.561996
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    hostvars.variable = "testvalue"

    hostvars_from_dict = HostVars({"variable": "testvalue"})

    assert represent_hostvars(None, hostvars) == represent_hostvars(None, hostvars_from_dict)

    assert represent_hostvars(None, hostvars) == "variable: testvalue\n"



# Generated at 2022-06-22 11:34:15.845845
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_undefined(AnsibleUndefined()) is False
    assert dumper.represent_undefined(True) is True
    assert dumper.represent_undefined(1) is True
    assert dumper.represent_undefined("") is True
    assert dumper.represent_undefined("foo") is True

# Generated at 2022-06-22 11:34:25.228607
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:34:27.645277
# Unit test for function represent_undefined
def test_represent_undefined():
    AnsibleDumper().represent_data(AnsibleUndefined())



# Generated at 2022-06-22 11:34:33.606328
# Unit test for function represent_unicode
def test_represent_unicode():
    """Simple test for represent_unicode function."""

    class TestAnsibleDumper(object):
        """Simple stub class for testing represent_unicode function."""

        @staticmethod
        def represent_str(dumper, data):
            return data

    text = u'B\xe9po is an input method'
    dumper = TestAnsibleDumper()
    rep = represent_unicode(dumper, text)
    assert rep == text

# Generated at 2022-06-22 11:34:35.603719
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert not dumper.represent_undefined(AnsibleUndefined(var_name='foo'))

# Generated at 2022-06-22 11:34:38.528278
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    data = dict(
        a=1,
        b=2
    )
    assert dumper.represent_dict(data) == dumper.represent_hostvars(data)



# Generated at 2022-06-22 11:34:42.566702
# Unit test for function represent_hostvars
def test_represent_hostvars():
    d = AnsibleDumper(indent=2)
    hostvars = HostVars({'foo': 'bar'})
    data = d.represent_data(hostvars)
    data = yaml.load(data)
    assert data['foo'] == 'bar'

# Generated at 2022-06-22 11:34:45.456229
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars(hostname='localhost')
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == '{}\n'



# Generated at 2022-06-22 11:34:49.155164
# Unit test for function represent_unicode
def test_represent_unicode():
    s = AnsibleUnicode('unicode_str_data')
    yaml_data = yaml.dump({'testdata': s}, Dumper=AnsibleDumper, default_flow_style=False)
    print(yaml_data)

    assert yaml_data == "testdata: unicode_str_data\n"



# Generated at 2022-06-22 11:35:00.693772
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault_password = 'myvaultpassword'
    plaintext = 'secret message'
    vault = VaultLib(vault_password)
    ciphertext = vault.encrypt(plaintext)
    vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    output = yaml.dump(vault_obj, default_flow_style=False, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:35:19.112382
# Unit test for function represent_binary
def test_represent_binary():
    """
    Test if blob of binary data is properly serialized.
    """
    d = AnsibleDumper()
    s = d.represent_binary(b'\x00\x01\x02')
    assert s == '!!binary |\n  AAEC\n'



# Generated at 2022-06-22 11:35:21.626572
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('Test')) == u'- Test\n'


# Generated at 2022-06-22 11:35:25.796751
# Unit test for function represent_hostvars
def test_represent_hostvars():
    """
    Unit test for function represent_hostvars.
    """
    data = {'foo': 'bar'}
    hostvars = HostVars(vars=data)
    yaml.dump(hostvars, default_flow_style=False, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:35:34.942177
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper
    data = AnsibleVaultEncryptedUnicode('AES256', b'$ANSIBLE_VAULT;1.1;AES256\n333835363533326139366433666537623562393734366138613239633534613534646666336364\n373466353436323362643762316532376135613162623662333236643365623732626535666338\n666534363836636163313137663133333266626235616265343461343038666231626263363563\n3636393362333466653362666234613736646565\n')
    s = dumper.represent_vault_encrypted_unicode(dumper, data)

# Generated at 2022-06-22 11:35:37.480752
# Unit test for function represent_binary
def test_represent_binary():

    assert b'{foo: "\x00"}' == yaml.dump({'foo': b'\x00'}, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:35:42.139168
# Unit test for function represent_unicode
def test_represent_unicode():
    sut = AnsibleDumper()
    assert sut.represent_unicode(u'test') == u'test'



# Generated at 2022-06-22 11:35:51.410079
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    data = AnsibleVaultEncryptedUnicode(u'foobar')
    data._ciphertext = '$ANSIBLE_VAULT;1.1;AES256;ansible\n6162326436356562306237616332653135313531376332326566643330663864623663653630\n3762313337373764636331306265643365393639313434666633646366643739623335396262\n6163313231316630616863623064366233626461633862316432333736316466373534663565\n3638653835'
    assert dumper.represent_scalar(u'!vault', text_type(data), style='|') is not None

# Generated at 2022-06-22 11:36:03.410638
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:36:06.229726
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.dump(
        HostVars(dict(a=1)),
        Dumper=AnsibleDumper
    ) == "a: 1\n"


# Generated at 2022-06-22 11:36:08.576723
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'foo') == "!!binary |-\n  Zm9v\n"

# Generated at 2022-06-22 11:36:58.649290
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-22 11:37:03.947254
# Unit test for function represent_unicode
def test_represent_unicode():
    unicode_text = AnsibleUnicode(u'unicode!')
    assert text_type(unicode_text) == u'unicode!'
    result = yaml.dump(unicode_text, Dumper=AnsibleDumper)
    assert text_type(result) == u'unicode!\n...\n'



# Generated at 2022-06-22 11:37:15.528824
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    plaintext = '$ANSIBLE_VAULT;1.1;AES256\n53616c7465645f5fc0d0e9814be939b689905d82820f5d5f5cff7d2bfb5d5c5a\n'
    ciphertext = b'$ANSIBLE_VAULT;1.1;AES256\n4e4d4f4b4a4b414d4b4a4b414d4b4a4b414d4b4a4b414d4b4a4b414d4b4a4b41\n'
    ex_vault = AnsibleVaultEncryptedUnicode(ciphertext.decode())
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:37:27.906030
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()

    string = 'Ansible Vault Encrypted String'
    ciphertext = '$ANSIBLE_VAULT;1.1;AES256;ansible\n64303435643866656430663833373638313534373537613036653265653730653566633733653730\n66643039656438353130316633356434363134636561316632666534643361646637633463376438\n353130306264633132313961346135626230343035643033366366360414141414141404141414141\n414141410041414141414141414141414141'

# Generated at 2022-06-22 11:37:30.289167
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('test\ntest')) == yaml.dump('test\ntest')

# Generated at 2022-06-22 11:37:35.249704
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper

    data = AnsibleUnsafeBytes('test')
    # With this, the output is binary
    dumper.represent_binary(dumper, data)
    # With this, the output is unicode
    dumper.represent_unicode(dumper, data)

# Generated at 2022-06-22 11:37:38.888350
# Unit test for function represent_binary
def test_represent_binary():
    a = AnsibleDumper()
    # bytes are not converted to base64
    result = a.represent_binary(b'\x00\x01')
    assert result == "!binary |\n  AAECA\n"



# Generated at 2022-06-22 11:37:42.546893
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(AnsibleDumper, u'blah') == u'blah'
    assert represent_unicode(AnsibleDumper, 'blah') == u'blah'
    assert represent_unicode(AnsibleDumper, 1) == u'1'



# Generated at 2022-06-22 11:37:50.225311
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()

    val = b'b\xE5\xBB\xAB'
    ansible_unicode = AnsibleUnicode(val)
    assert dumper.represent_unicode(ansible_unicode) == yaml.representer.SafeRepresenter.represent_str(dumper, val)
    assert dumper.represent_unicode(val) == yaml.representer.SafeRepresenter.represent_str(dumper, val)

# Generated at 2022-06-22 11:37:55.508847
# Unit test for function represent_unicode
def test_represent_unicode():
    # Setup
    data = AnsibleUnicode(u'This is a unicode string.')

    # Test
    result = yaml.representer.SafeRepresenter.represent_str(AnsibleDumper, data)

    # Verify
    assert isinstance(result, list)
    assert result == [u'this is a unicode string\n']

    # Teardown, cleanup
    assert True