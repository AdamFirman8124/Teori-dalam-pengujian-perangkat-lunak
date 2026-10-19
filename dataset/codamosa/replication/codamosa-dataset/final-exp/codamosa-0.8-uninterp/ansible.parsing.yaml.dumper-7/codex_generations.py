

# Generated at 2022-06-22 11:29:50.542125
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = yaml.dumper.SafeDumper
    representer = represent_hostvars
    data = {'foo': 'bar'}
    result = representer(dumper, data)
    assert result == dumper.represent_dict(dict(data))



# Generated at 2022-06-22 11:29:54.662098
# Unit test for function represent_binary
def test_represent_binary():
    a_bytes = b'\xc3\x80'
    expected_value = u'!binary |-\n  w6k=\n'
    actual_value = yaml.dump(a_bytes, Dumper=AnsibleDumper)
    assert expected_value == actual_value



# Generated at 2022-06-22 11:29:57.716376
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dict_vars = dict(a=1, b=2)
    hostvars = HostVars(hostname='hostname', vars=dict_vars)
    assert represent_hostvars(AnsibleDumper, hostvars) == represent_hostvars(AnsibleDumper, dict_vars)



# Generated at 2022-06-22 11:30:04.630730
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.SafeDumper
    represent = AnsibleDumper.represent_binary
    result = represent(dumper, 'abc')
    assert result == yaml.representer.SafeRepresenter.represent_binary(dumper, b'abc')
    result = represent(dumper, b'abc')
    assert result == yaml.representer.SafeRepresenter.represent_binary(dumper, b'abc')



# Generated at 2022-06-22 11:30:16.439057
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    # Just need an instance of VaultEncryptedUnicode for testing
    from ansible.parsing.vault import VaultLib
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile() as tf:
        vault = VaultLib([])
        ciphertext = vault.encrypt(tf.name, 'some string')
        data = AnsibleVaultEncryptedUnicode(ciphertext)
        assert False is data._is_binary, 'Expected AnsibleVaultEncryptedUnicode to be text'

        # Test successful path
        with tf.open('r') as f:
            key = vault._get_vault_secret(f)

        data._secret_id = key.salt + key.hmac_key + key.cipher_type

# Generated at 2022-06-22 11:30:27.969084
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    to_represent = AnsibleUnicode('asdf')

# Generated at 2022-06-22 11:30:30.686744
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(binary_type('foo'), Dumper=AnsibleDumper, allow_unicode=True) == u": !!binary |\n  Zm9v\n"


# Generated at 2022-06-22 11:30:32.842581
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    undefined = AnsibleUndefined('{"test": "value"}')
    assert dumper.represent_data(undefined) is None

# Generated at 2022-06-22 11:30:39.550414
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml.add_representer(text_type, represent_unicode)
    data = b'\xc3\xbc'.decode('utf-8')
    dumped_data = yaml.dump(data)
    expected_data = '# ASCII unicode (U+00FC)\n"\\u00fc"\n'
    assert dumped_data == expected_data

# Generated at 2022-06-22 11:30:42.384935
# Unit test for function represent_undefined
def test_represent_undefined():
    class FakeData:
        def __bool__(self):
            return True
    assert represent_undefined(AnsibleDumper, FakeData())



# Generated at 2022-06-22 11:30:47.981486
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert yaml.dump(AnsibleVaultEncryptedUnicode('foo', ciphertext=b'AES256'), Dumper=AnsibleDumper) == '!vault |\n  AES256'

# Generated at 2022-06-22 11:30:51.909961
# Unit test for function represent_unicode
def test_represent_unicode():
    test_output = 'foo: bar'
    test_dump = AnsibleUnicode(u'{"foo": "bar"}')
    test_result = yaml.dump(test_dump, Dumper=AnsibleDumper)
    assert test_result == test_output



# Generated at 2022-06-22 11:30:54.593892
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    assert dumper.represent_hostvars(dumper, HostVars(dict())) == dumper.represent_dict(dumper, dict())



# Generated at 2022-06-22 11:30:58.277825
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()

    try:
        dumper.represent_undefined(AnsibleUndefined)
    except AttributeError:
        return
    assert False, "The representer should have raised an AttributeError exception"

# Generated at 2022-06-22 11:31:09.277555
# Unit test for function represent_unicode
def test_represent_unicode():
    data = {
        'test': ['value1', 'value2', 'value3'],
        'test2': {'value1': 'value2', 'value3': 'value4'},
        'test3': u'A unicode string',
        'test4': b'A byte string'
    }

    expected_output = '''{test: [value1, value2, value3],
 test2: {value1: value2, value3: value4},
 test3: A unicode string,
 test4: !!binary "QSBieXRlIHN0cmluZw==\\n"}'''

    yaml.dump(data, stream=None, Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:31:19.416046
# Unit test for function represent_undefined
def test_represent_undefined():
    instance = AnsibleUndefined('foo')
    dumper = AnsibleDumper()
    dumper.add_representer(
        AnsibleUndefined,
        represent_undefined,
    )
    with pytest.raises(yaml.representer.RepresenterError):
        dumper.represent_data({'test': instance})
    with pytest.raises(yaml.representer.RepresenterError):
        dumper.represent_sequence([instance])
    with pytest.raises(yaml.representer.RepresenterError):
        dumper.represent_data(instance)
    dumper.represent_data(dict(test=instance)) == '{test: !!python/object:ansible.utils.unsafe_proxy.Undefined}\n'

# Generated at 2022-06-22 11:31:21.466093
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode(u'foo'), Dumper=AnsibleDumper) == 'foo\n...\n'


# Generated at 2022-06-22 11:31:32.749090
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode(text_type('test'))
    value = represent_vault_encrypted_unicode(None, data)

# Generated at 2022-06-22 11:31:38.639991
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.module_utils.six import binary_type
    from ansible.parsing.yaml.objects import AnsibleUnsafeBytes
    d = AnsibleDumper()
    b = AnsibleUnsafeBytes(b'blah')
    result = d.represent_binary(b)
    assert isinstance(result, binary_type), 'Expected a binary string or bytes representation'
    assert result == b'!!binary |\n' + b'  YmxhaA==\n'

# Generated at 2022-06-22 11:31:43.944000
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    # if the value is Undefined

# Generated at 2022-06-22 11:31:58.799514
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars, HostVarsVars
    from ansible.vars.manager import VarsWithSources

    hh = HostVars()
    hh['host1'] = {'a': 'b'}
    hh['host2'] = {'b': 'c'}
    assert yaml.dump(hh, Dumper=AnsibleDumper) == '{host1: {a: b}, host2: {b: c}}\n'

    hh = HostVarsVars()
    hh['host1'] = {'a': 'b'}
    hh['host2'] = {'b': 'c'}

# Generated at 2022-06-22 11:32:02.185842
# Unit test for function represent_binary
def test_represent_binary():
    output = yaml.dump(b'\\xff', Dumper=AnsibleDumper)
    assert output.endswith(b': !!binary |-\n  \\xff\n')



# Generated at 2022-06-22 11:32:06.276262
# Unit test for function represent_binary
def test_represent_binary():
    representer = represent_binary
    dumper = AnsibleDumper([])
    representer(dumper, b'foo\x00')
    assert dumper.represent_data.call_count == 1
    dumper.represent_data.assert_called_with(b'foo\x00')



# Generated at 2022-06-22 11:32:08.469895
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode(u'test') == u'test'

# Generated at 2022-06-22 11:32:10.369788
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    assert represent_undefined(dumper, AnsibleUndefined())

# Generated at 2022-06-22 11:32:22.274115
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hostvars = HostVars()
    some_dict = dict(a=1, b=2)
    hostvars['this_is_a_dict'] = some_dict
    dumped = yaml.dump(hostvars, Dumper=AnsibleDumper)
    assert '!hostvars' not in dumped, "Representing HostVars as a dictionary should not include the !hostvars tag."
    assert '&' not in dumped, "Representing HostVars should not include '&' references."
    # Verify the contents of the dumped object
    # The first line should be the hostvars tag, and the second line should be a sequence
    # containing one element, the dictionary that we put in
    lines = [l.strip() for l in dumped.strip().splitlines()]

# Generated at 2022-06-22 11:32:32.233264
# Unit test for function represent_unicode
def test_represent_unicode():
    # Convenience function used by assert statements.
    def check(expected, given):
        assert expected == given

    check(u'null', yaml.dump(yaml.RoundTripLoader(None).get_single_data(), Dumper=AnsibleDumper))

    # String is the only scalar type that doesn't dump as a string (that I know of)
    # so we need to test that.
    check(u'false', yaml.dump(False, Dumper=AnsibleDumper))
    check(u'true', yaml.dump(True, Dumper=AnsibleDumper))

    # List
    check(u'[false]', yaml.dump([False], Dumper=AnsibleDumper))

    # Tuple

# Generated at 2022-06-22 11:32:34.401694
# Unit test for function represent_binary
def test_represent_binary():
    d = AnsibleDumper()
    assert d.represent_binary(b'foo') == u"!binary |\n  Zm9v\n"



# Generated at 2022-06-22 11:32:36.802075
# Unit test for function represent_unicode
def test_represent_unicode():
    d = AnsibleDumper()
    assert d.represent_unicode(u'foo') == u'"foo"'

# Generated at 2022-06-22 11:32:42.375313
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('my_password', '$ANSIBLE_VAULT;1.1;AES256;my_password')
    result = represent_vault_encrypted_unicode(None, data)
    assert result == "!vault |\n  $ANSIBLE_VAULT;1.1;AES256;my_password\n"

# Generated at 2022-06-22 11:32:48.422383
# Unit test for function represent_unicode
def test_represent_unicode():
    result = yaml.dump({u'1': u'2'}, Dumper=AnsibleDumper)
    # Test exact content, for some reason this is not required by the standard
    assert result == '{1: 2}\n'



# Generated at 2022-06-22 11:32:52.719047
# Unit test for function represent_hostvars
def test_represent_hostvars():
    loader = yaml.loader.SafeLoader

    # Check that we get an object back with the right type
    data = yaml.load("!hostvars false", Loader=loader)
    assert isinstance(data, HostVars)

    # Make sure it contains the correct data
    assert "false" in data

    # Make sure the data is correct
    assert data["false"] is False



# Generated at 2022-06-22 11:33:02.863316
# Unit test for function represent_binary
def test_represent_binary():
    # prepare the data to be dumped
    original_data = b'\x96\x9a\x81\x8d\x8e\x99\x90\xad\x8d\x96\x9a'
    data = AnsibleUnsafeBytes(original_data)

    # dump the data and compare the result
    dumped_data = yaml.dump(data, Dumper=AnsibleDumper)
    assert dumped_data == b'!!binary |\n  nzVnXzlmXzk3XzknXzk3XzlmXzk3Xzk3Xzk3Xzk1Xzlm\n'

    # make sure when we load it back we get the original data
    loaded_data = yaml.load(dumped_data, Loader=yaml.Loader)


# Generated at 2022-06-22 11:33:06.005424
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template.template import AnsibleUndefined

    dumper = AnsibleDumper
    s = dumper.represent_undefined(dumper, AnsibleUndefined())



# Generated at 2022-06-22 11:33:07.721845
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, AnsibleUnicode('foo')) == represent_unicode(None, u'foo')

# Generated at 2022-06-22 11:33:12.185872
# Unit test for function represent_unicode
def test_represent_unicode():
    data = 'test_data_string'
    rep = yaml.representer.SafeRepresenter()
    represent_unicode(rep, data)
    assert type(represent_unicode(rep, data)) == str



# Generated at 2022-06-22 11:33:16.644968
# Unit test for function represent_hostvars
def test_represent_hostvars():
    ''' test_represent_hostvars - verify that the hostvars representation works as expected
    '''
    data = {'foo': 'bar'}
    rep = yaml.dump(HostVars(data), Dumper=AnsibleDumper)
    assert rep == "{foo: bar}\n"


# Generated at 2022-06-22 11:33:25.200997
# Unit test for function represent_binary
def test_represent_binary():
    # Base64-encoded data
    data = b'SGVsbG8sIFdvcmxkIQ==\n'
    # Ensure it is rendered properly
    rendered = AnsibleDumper.represent_binary(None, data)
    assert isinstance(rendered, text_type)
    assert rendered == u"SGVsbG8sIFdvcmxkIQ==\n"
    # When rendered, data is properly base64-encoded
    result = yaml.safe_load(rendered)
    assert isinstance(result, binary_type)
    assert result == data

# Generated at 2022-06-22 11:33:28.743442
# Unit test for function represent_binary
def test_represent_binary():
    data = b'\xc3\xa9'
    dumper = AnsibleDumper(width=40)
    output = dumper.represent_binary(data)
    assert output == "!!binary |\n  w6k=\n"



# Generated at 2022-06-22 11:33:34.717397
# Unit test for function represent_unicode
def test_represent_unicode():
    # Note: using this function
    # Note: not using .encode('unicode-escape')
    # Note: test unicode
    assert represent_unicode(None, u'hello') == u'hello'
    # Note: test str
    assert represent_unicode(None, 'hello') == u'hello'
    # Note: test obj.__str__
    class A:
        def __str__(self):
            return u'hello'

    assert represent_unicode(None, A()) == u'hello'



# Generated at 2022-06-22 11:33:41.252360
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    any_data = { u'a': u'1' }
    hostvars = HostVars(any_data)
    assert dumper.represent_data(hostvars) == dumper.represent_dict(any_data)


# Generated at 2022-06-22 11:33:51.830858
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import ansible.parsing.vault
    from io import StringIO
    from ansible.parsing.yaml import objects

    test_data = 'The quick brown fox jumped over the lazy red dog'
    vault = ansible.parsing.vault.VaultLib('VaultMeBabyOneMoreTime')
    ciphertext = vault.encrypt(text_type(test_data))

    dump = yaml.dump([objects.AnsibleVaultEncryptedUnicode(ciphertext)], Dumper=AnsibleDumper)
    # print("Dump: %s" % dump)

    load = yaml.load(StringIO(dump))
    # print("Load: %s" % load)

    assert load[0].decrypt(vault) == test_data

# Generated at 2022-06-22 11:33:58.629337
# Unit test for function represent_binary
def test_represent_binary():
    my_binary_data = b'20:12:01:0a:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00'
    assert yaml.safe_dump(my_binary_data, default_flow_style=True, Dumper=AnsibleDumper).strip() == my_binary_data.decode('utf-8')

# Generated at 2022-06-22 11:34:01.666535
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    data = HostVars({"foo": "bar"})

    assert dumper.represent_hostvars(dumper, data) == dumper.represent_dict(dumper, dict(data))



# Generated at 2022-06-22 11:34:05.324770
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'hello', Dumper=AnsibleDumper, default_flow_style=False) == '!!binary |\n  aGVsbG8=\n'



# Generated at 2022-06-22 11:34:17.749623
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    result = represent_vault_encrypted_unicode(
        AnsibleDumper,
        AnsibleVaultEncryptedUnicode("password123", "AES256",
                                     "myencryptedpassword")
    )

# Generated at 2022-06-22 11:34:23.310592
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    data = AnsibleUndefined("testing")
    assert dumper.represent_undefined(dumper, data)


# Loader is only used if loading the data structure, i.e. parsing YAML
AnsibleDumper.add_multi_representer(
    type(None),
    yaml.representer.SafeRepresenter.represent_none,
)

# Generated at 2022-06-22 11:34:32.560144
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    test_string = 'test string'
    ciphertext = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          6333636538613039303432356332346337636366383936646335323531373063373430326661613833\n          3330623162323732626137663539333636376133353533613032626236633836383031303834636333\n          37\n"
    assert represent_vault_encrypted_unicode(AnsibleDumper(), AnsibleVaultEncryptedUnicode(test_string)) == ciphertext

# Generated at 2022-06-22 11:34:37.503667
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    Tests whether yaml parser is able to parse unicode strings or not.
    '''
    output_data = dict(test_unicode_key=unicode("test_unicode_value"))
    assert yaml.dump(output_data, Dumper=AnsibleDumper) == 'test_unicode_key: test_unicode_value\n'

# Generated at 2022-06-22 11:34:39.187687
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(dict(foo=AnsibleUnicode(u'bar'))) == u'foo: bar\n'



# Generated at 2022-06-22 11:34:43.846433
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    assert dumper.represent_unicode(dumper, u'foo') == "foo"

# Generated at 2022-06-22 11:34:53.161983
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:34:55.447083
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    result = dumper.represent_undefined(dumper, AnsibleUndefined())
    assert result is False

# Generated at 2022-06-22 11:35:00.096101
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.parsing.yaml.data import AnsibleVaultEncryptedText
    from ansible.vars import hostvars

    hv = hostvars({
        'a': u'foo',
        'b': AnsibleVaultEncryptedText('bar', 'baz')
    })
    binary_data = AnsibleUnsafeBytes(u'\x00\x01\x02')
    result = AnsibleDumper(default_flow_style=False).represent_data(dict(
        a=u'foo',
        b=hv,
        c=binary_data
    ))

# Generated at 2022-06-22 11:35:04.652278
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    output = dumper.represent_binary(b"Hello World\n")
    assert output == u"!!binary |\n  SGVsbG8gV29ybGQK\n"

# Generated at 2022-06-22 11:35:09.244346
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert bool(dumper.represent_undefined(AnsibleUndefined()))
    assert bool(dumper.represent_undefined(AnsibleUndefined(strict=True)))


# Unit tests for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:35:12.368149
# Unit test for function represent_hostvars
def test_represent_hostvars():
    result = yaml.dump(HostVars({"a": "foo"}), Dumper=AnsibleDumper, default_flow_style=False)
    assert result == 'a: foo\n'

# Generated at 2022-06-22 11:35:16.389550
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml_output = yaml.dump(u'unicode \u2603 abc', Dumper=AnsibleDumper)
    assert yaml_output == "u'unicode \\u2603 abc'\n"



# Generated at 2022-06-22 11:35:18.353366
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    data = AnsibleUndefined()
    ret = dumper.represent_data(data)
    assert ret is True

# Generated at 2022-06-22 11:35:23.653448
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    test_string = AnsibleVaultEncryptedUnicode(b'vaultencryptedtext')
    expected_string = "!vault |\n          vaultencryptedtext"
    dump = AnsibleDumper().represent_vault_encrypted_unicode(test_string)
    assert dump == expected_string

# Generated at 2022-06-22 11:35:33.501110
# Unit test for function represent_binary
def test_represent_binary():
    r = yaml.representer.SafeRepresenter()
    # We don't want to test the full yaml spec here so we only do basic tests
    # on the bytes we can safely handle
    assert r.represent_binary(b'foobar') == "'foobar'"
    assert r.represent_binary(b'\x7f') == "||\n  7A==\n"
    assert r.represent_binary(b'\xff') == "||\n  /w==\n"
    assert r.represent_binary(b'"\\') == "||\n  /8J\n"

# Generated at 2022-06-22 11:35:35.379767
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.dump(HostVars(dict(a=1)), default_flow_style=False, Dumper=AnsibleDumper) == (
        'a: 1\n'
    )



# Generated at 2022-06-22 11:35:45.175143
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    representer = AnsibleDumper.represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:35:56.425419
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_unicode("") == dumper.represent_unicode(AnsibleUnsafeText(""))
    assert dumper.represent_unicode("") == dumper.represent_unicode(AnsibleUnsafeText(""))
    assert dumper.represent_unicode("") == dumper.represent_unicode(AnsibleUnsafeBytes(""))
    assert dumper.represent_unicode("") == dumper.represent_unicode(AnsibleUnicode(""))
    assert dumper.represent_unicode("{{ foo }}") == dumper.represent_unicode(AnsibleUnicode("{{ foo }}"))
    assert dumper.represent_unicode("{{ foo }}") == dumper.represent_unicode(AnsibleUnsafeText("{{ foo }}"))
    assert d

# Generated at 2022-06-22 11:35:59.823410
# Unit test for function represent_binary
def test_represent_binary():
    '''
    AnsibleDumper: test represent_binary
    '''
    assert AnsibleDumper.represent_binary(None, b'foo') == b"!binary |\n  Zm9v"

# Generated at 2022-06-22 11:36:04.306161
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    test_data = AnsibleVaultEncryptedUnicode('test_plain_text')
    assert(test_data.__repr__() == "VaultEncryptedUnicode('test_plain_text')")



# Generated at 2022-06-22 11:36:12.890313
# Unit test for function represent_unicode
def test_represent_unicode():
    # The following is based on
    # https://github.com/yaml/pyyaml/blob/master/lib/yaml/representer.py#L54
    #
    # Python 2 supports str, unicode and bytestrings, so we need to clear
    # the yaml.representer.BaseRepresenter.represent_str attribute before
    # creating the yaml.representer.BaseRepresenter instance
    yaml.representer.BaseRepresenter.represent_str = None
    dumper = yaml.representer.BaseRepresenter()
    represent_unicode(dumper, AnsibleUnicode('foo'))



# Generated at 2022-06-22 11:36:14.667852
# Unit test for function represent_undefined
def test_represent_undefined():
    undefined = AnsibleUndefined('')
    d = AnsibleDumper()
    assert d.represent_data(undefined) is True



# Generated at 2022-06-22 11:36:21.401424
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert yaml.dump(AnsibleVaultEncryptedUnicode('foo'), default_flow_style=False) == u"!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  63656430383438663563386165653864396633323463323063393438376162313761393234323064\n  61343762333962333864663339646661\n"

# Generated at 2022-06-22 11:36:26.453638
# Unit test for function represent_undefined
def test_represent_undefined():
    AnsibleUndefined.strict = False
    u = AnsibleUndefined()
    d = AnsibleDumper()
    assert d.represent_data(u) is d.represent_undefined(u)
    AnsibleUndefined.strict = True

# Generated at 2022-06-22 11:36:33.420459
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert AnsibleDumper.represent_hostvars

# Generated at 2022-06-22 11:36:38.274266
# Unit test for function represent_unicode
def test_represent_unicode():
    # test for regular unicode
    assert represent_unicode(AnsibleDumper, u'H\xe9llo') == 'H\xe9llo'
    # test for unicode surrogate pairs
    assert represent_unicode(AnsibleDumper, u'H\ud83c\udf4d') == 'H\ud83c\udf4d'



# Generated at 2022-06-22 11:36:39.858757
# Unit test for function represent_binary
def test_represent_binary():
    representer = AnsibleDumper()
    represent_binary(representer, text_type('\x03\x02'))

# Generated at 2022-06-22 11:36:43.511880
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, 'foo') == u'foo'
    assert represent_unicode(None, u'foo') == u'foo'



# Generated at 2022-06-22 11:36:47.545264
# Unit test for function represent_binary
def test_represent_binary():
    # This could be any bytes,
    # the goal is just to test that it doesn't raise an exception
    data = b'\x00\x01'
    AnsibleDumper().represent_binary(data) == u'!!binary |\n  AAECA'



# Generated at 2022-06-22 11:36:57.348201
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-22 11:37:03.523583
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    assert dumper.represent_binary('%%%foo') == "!!binary |\n  wr8=\n"
    assert dumper.represent_binary('%%%foo'.encode('utf-16')) == "!!binary |\n  //8KMGxsbG\n"


# Generated at 2022-06-22 11:37:07.356914
# Unit test for function represent_hostvars
def test_represent_hostvars():
    output = yaml.dump(HostVars({'k': 'v'}), Dumper=AnsibleDumper)
    assert output == "k: v\n"

# Generated at 2022-06-22 11:37:10.611267
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.module_utils.common.yaml import YAML
    yaml_object = YAML(typ='unsafe')
    yaml_string = yaml_object.dump(HostVars({'a': 'b'}))
    assert "a: b" in yaml_string, ("HostVars not dumped correctly\n"
                                   "Output: %s" % yaml_string)



# Generated at 2022-06-22 11:37:14.550345
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = yaml.Dumper()
    yaml.add_representer(AnsibleUndefined, represent_undefined)
    repr_undefined = yaml.dump(AnsibleUndefined(), dumper)
    assert repr_undefined == "None"

# Generated at 2022-06-22 11:37:26.181124
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = HostVars(test=2)
    assert represent_hostvars(None, data) == {'test': 2}
    assert represent_hostvars(None, data).__class__ == dict


if __name__ == '__main__':
    import pytest
    pytest.main(['--boxed', '-v', '-s'])

# Generated at 2022-06-22 11:37:28.775377
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('unicode data')
    assert data == 'unicode data'
    assert data == u'unicode data'


# Generated at 2022-06-22 11:37:30.999121
# Unit test for function represent_unicode
def test_represent_unicode():
    o = AnsibleUnicode(u'å')
    r = represent_unicode(SafeDumper(), o)
    assert r.value == 'å'

# Generated at 2022-06-22 11:37:41.414721
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dh = AnsibleDumper({})
    # Create a HostVars object
    hv = HostVars(host_name='foo')
    # Create two variables
    hv['foo'] = 'bar'
    hv['blah'] = 'blahblah'
    # Create a dict using hv
    dict_hv = dict(hv)
    # Dump the dict using AnsibleDumper
    dumped_hv = dh.represent_dict(dict_hv)
    # Assert that it matched what we expected
    assert dumped_hv == "!hostvars 'foo'\nblah: blahblah\nfoo: bar"

# Unit tests for class AnsibleDumper

# Generated at 2022-06-22 11:37:45.861992
# Unit test for function represent_unicode
def test_represent_unicode():
    data = u'hello world'
    doc = yaml.dump(data, Dumper=AnsibleDumper)
    assert "hello world" in doc
    assert "!!python/unicode" not in doc



# Generated at 2022-06-22 11:37:55.801132
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper()
    # Test string value
    value = dumper.represent_unicode("some string")
    assert isinstance(value, yaml.representer.SafeRepresenter.represent_str)
    assert value.value == "some string"

    # Test bytes value
    value = dumper.represent_unicode(b'\xFF')
    assert isinstance(value, yaml.representer.SafeRepresenter.represent_str)
    assert value.value == "\xFF"

    # Test int value
    value = dumper.represent_unicode(42)
    assert isinstance(value, yaml.representer.SafeRepresenter.represent_str)
    assert value.value == "42"

# Generated at 2022-06-22 11:37:58.028447
# Unit test for function represent_unicode
def test_represent_unicode():
    d = AnsibleDumper()
    txt = 'abc'
    assert d.represent_unicode(txt) == d.represent_unicode(u'abc')

# Generated at 2022-06-22 11:38:07.055817
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper
    # The real HostVars object will not have the "hostvars" key
    # we have to add it like this for the test
    # The format for the test is a list of tuples where the first element
    # of the tuple is a dictionary and the second element is the expected
    # output from represent_hostvars
    # This test is not enough, other tests must be added in the code
    # using represent_hostvars
    test_data = [
        ({'hostvars': {'host1': {'key1': 'value1'}}},
         'hostvars:\n  host1:\n    key1: value1\n'),
    ]

    for data_to_test in test_data:
        (data, expected_output) = data_to_test
        output = d

# Generated at 2022-06-22 11:38:15.264617
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    result = yaml.dump(AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n333233623336623337393230656437353136633862656632633361373034396366323861653861\n38393163643337656161310a"), Dumper=AnsibleDumper)
    correct = "!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  333233623336623337393230656437353136633862656632633361373034396366323861653861\n  38393163643337656161310a\n"
    assert result == correct

# Generated at 2022-06-22 11:38:20.445971
# Unit test for function represent_unicode
def test_represent_unicode():

    def verify_unicode(unistr):
        d = AnsibleDumper()
        result = d.represent_unicode(unistr)
        expected = yaml.representer.SafeRepresenter.represent_unicode(d, unistr)
        assert result == expected

    verify_unicode(u'Hello World!')
    verify_unicode(u'\u2603')

# Generated at 2022-06-22 11:38:36.995988
# Unit test for function represent_hostvars
def test_represent_hostvars():
    this_host = HostVars({"ansible_ssh_user":"bender", "ansible_ssh_host":"12.34.567.890"})
    test_data = {
        "ansible_ssh_user": "bender",
        "ansible_ssh_host": "12.34.567.890",
    }
    dumper = AnsibleDumper()
    dumper.represent_hostvars(this_host)
    assert test_data == yaml.load(dumper.represent_hostvars(this_host))


# Generated at 2022-06-22 11:38:45.018817
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    import base64
    value = AnsibleVaultEncryptedUnicode(b'TGlhY3VzIEJlZSBpbiBodW1hbmllcyBhbmQgZnJpc2hlcyB3YXMgaW1wcm92ZWQgdmlhIHRoZSBjb21wbGV4aXR5IG9mIHNvZnR3YXJlLg==')

# Generated at 2022-06-22 11:38:55.553390
# Unit test for function represent_binary
def test_represent_binary():

    assert yaml.dump(u'{{ foo }}') == yaml.dump(AnsibleUnsafeBytes(u'{{ foo }}'))
    assert yaml.dump(u'{{ foo }}') == yaml.dump(AnsibleUnsafeText(u'{{ foo }}'))
    assert yaml.dump(u'{{ foo }}') == yaml.dump(AnsibleUnicode(u'{{ foo }}'))

    assert yaml.dump(u'{{ foo }}') == yaml.dump(AnsibleDumper().represent_unicode(u'{{ foo }}'))
    assert yaml.dump(b'{{ foo }}') == yaml.dump(AnsibleDumper().represent_binary(u'{{ foo }}'))

# Generated at 2022-06-22 11:39:06.537045
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.manager import VariableManager

    input_tests = [
        {
            "plain": {"a": 1},
            "complex": AnsibleMapping({"a": 1}),
        },
        {
            "plain": [1, 2, 3],
            "complex": [1, 2, 3],
        },
    ]

    for test in input_tests:
        # Use a yaml parser to ensure that it works with lists and dicts too
        yaml.dump(test['plain'], stream=None,
                  Dumper=AnsibleDumper, explicit_start=True)

        yaml.dump(test['complex'], stream=None,
                  Dumper=AnsibleDumper, explicit_start=True)

       

# Generated at 2022-06-22 11:39:10.417996
# Unit test for function represent_hostvars
def test_represent_hostvars():

    assert yaml.dump(dict(HostVars({"x": "y"})), Dumper=AnsibleDumper) == \
        "!!python/object/apply:ansible.vars.hostvars.HostVars {x: y}\n"

# Generated at 2022-06-22 11:39:22.089279
# Unit test for function represent_hostvars
def test_represent_hostvars():
    import collections
    hostvars = HostVars()
    hostvars.update(collections.OrderedDict((
        ("v1", "val1"),
        ("v2", "val2")
    )))
    assert yaml.dump({"hv": hostvars}, Dumper=AnsibleDumper).count('hv:') == 2
    assert yaml.dump({"hv": hostvars}, Dumper=AnsibleDumper).count('v1:') == 2
    assert yaml.dump({"hv": hostvars}, Dumper=AnsibleDumper).count('v2:') == 2
    assert yaml.dump({"hv": hostvars}, Dumper=AnsibleDumper).count('val1') == 1

# Generated at 2022-06-22 11:39:33.336943
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode("$ANSIBLE_VAULT;1.1;AES256\n3132333435363738396162636465663738653936636365632d326537626537352d343733362d386535\n332d633733626263633434306663343031\n")
    assert yaml.dump(data, Dumper=AnsibleDumper) == "!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  3132333435363738396162636465663738653936636365632d326537626537352d343733362d386535\n  332d633733626263633434306663343031\n"



# Generated at 2022-06-22 11:39:37.964951
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode(u'foo')
    assert represent_unicode(AnsibleDumper(), data) == u"!ansible-unicode 'foo'"
    assert represent_unicode(AnsibleUnsafeDumper(), data) == u'foo'

# Generated at 2022-06-22 11:39:41.660567
# Unit test for function represent_unicode
def test_represent_unicode():
    dump = AnsibleDumper(width=1, default_flow_style=False)
    assert dump.represent_unicode('Test') == '- Test'

# Generated at 2022-06-22 11:39:42.960346
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(None, "text") == "text"