

# Generated at 2022-06-22 11:29:52.937513
# Unit test for function represent_undefined
def test_represent_undefined():
    def _assert_equal(data):
        return AnsibleDumper.represent_undefined(data)

    class A:
        def __nonzero__(self):
            # This is only called when calling bool(A) in Python 2.
            # Python 3 does not have __nonzero__
            return True

    assert _assert_equal(None)
    assert _assert_equal(undefined_from_yaml(None))
    assert not _assert_equal(A())



# Generated at 2022-06-22 11:29:55.478537
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = yaml.SafeDumper
    assert dumper.represent_undefined(dumper, AnsibleUndefined()) is False

# Generated at 2022-06-22 11:29:57.682243
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_undefined(AnsibleUndefined) is False


# Generated at 2022-06-22 11:30:00.543011
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert(represent_hostvars(AnsibleDumper, HostVars()) == yaml.representer.SafeRepresenter.represent_dict(AnsibleDumper, {'foo': 'bar'}))



# Generated at 2022-06-22 11:30:08.096382
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    assert dumper.represent_vault_encrypted_unicode(AnsibleVaultEncryptedUnicode("test")) == "!vault |\n          VjJUSg==\n"
    assert dumper.represent_vault_encrypted_unicode(u"test") == dumper.represent_vault_encrypted_unicode(AnsibleVaultEncryptedUnicode("test"))

# Generated at 2022-06-22 11:30:18.997339
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper

    # Test the represent_binary function with a byte string
    encoded_byte_string = b'\x00\x01\x02\x03'
    expected = '!!binary "\x00\x01\x02\x03"'
    ansible_byte_string = AnsibleUnsafeBytes(encoded_byte_string)
    actual = dumper.represent_binary(dumper, ansible_byte_string)

    # Here we check if the actual result is the same as the expected result
    assert actual == expected

    # Test the represent_binary function with a unicode string
    unicode_string = u'\xff\xfe\xfd\xfc'
    expected = '!!binary "\xff\xfe\xfd\xfc"'
    ansible_unicode_string = AnsibleUnsafeText

# Generated at 2022-06-22 11:30:24.065983
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('foo')
    repo = AnsibleDumper(width=1000)
    result = repo.represent_scalar(u'!vault', data, style='|')
    assert result == '!vault |\n          %s\n' % data._ciphertext.decode()

# Generated at 2022-06-22 11:30:27.492002
# Unit test for function represent_hostvars
def test_represent_hostvars():
    representer = AnsibleDumper()
    assert representer.represent_hostvars({
        'hostvars': 'foo',
        'playbook_dir': 'bar',
    }) == '{hostvars: foo, playbook_dir: bar}'


# Generated at 2022-06-22 11:30:29.227426
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper.represent_undefined(AnsibleDumper, AnsibleUndefined()) == True



# Generated at 2022-06-22 11:30:34.397539
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(yaml.ByteString(b'12345'), Dumper=AnsibleDumper) == b"!binary |\n  MTIzNDU=\n"

# Generated at 2022-06-22 11:30:41.476894
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dump = yaml.dump({'key': 'value'}, Dumper=AnsibleDumper)
    test_data = {'key': 'value'}
    dumper = AnsibleDumper
    # call the function to be tested
    result = represent_hostvars(dumper, test_data)
    assert result == dump

# Generated at 2022-06-22 11:30:42.862950
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(None, b'hello') == u'hello'

# Generated at 2022-06-22 11:30:46.931579
# Unit test for function represent_undefined
def test_represent_undefined():
    output = yaml.dump({'foo': AnsibleUndefined}, Dumper=AnsibleDumper)
    assert output == 'foo: null\n'



# Generated at 2022-06-22 11:30:49.183277
# Unit test for function represent_binary
def test_represent_binary():
    expected = "!!binary \"/w==\"\n"
    actual = yaml.dump(b'\x00', Dumper=AnsibleDumper)
    assert actual == expected

# Generated at 2022-06-22 11:30:51.773955
# Unit test for function represent_hostvars
def test_represent_hostvars():
    result = represent_hostvars(None, HostVars(dict(foo='bar')))
    assert result == {'foo': 'bar'}

# Generated at 2022-06-22 11:30:55.029088
# Unit test for function represent_hostvars
def test_represent_hostvars():
    h = HostVars({'foo': 'bar'})
    dumped = yaml.dump({'_hostvars': h}, Dumper=AnsibleDumper)
    assert dumped == '{_hostvars: {foo: bar}}\n...\n'



# Generated at 2022-06-22 11:31:00.702948
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    res = represent_vault_encrypted_unicode(AnsibleDumper, AnsibleVaultEncryptedUnicode('ciphertext'))
    assert isinstance(res, yaml.ScalarNode)
    assert res.tag == u'!vault'
    assert res.value == u'ciphertext'
    assert res.style == u'|'

# Generated at 2022-06-22 11:31:07.007747
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.load(yaml.dump(AnsibleUnicode('test'), Dumper=AnsibleDumper)) == 'test'
    assert yaml.load(yaml.dump(AnsibleUnsafeText('test'), Dumper=AnsibleDumper)) == 'test'
    assert yaml.load(yaml.dump(AnsibleUnsafeText(b'test'), Dumper=AnsibleDumper)) == 'test'

# Generated at 2022-06-22 11:31:10.471397
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    b = b'abc'
    bson = 'abc'
    assert (dumper.represent_binary(dumper, b) ==
            yaml.representer.SafeRepresenter.represent_binary(dumper, bson))

# Generated at 2022-06-22 11:31:15.585488
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(AnsibleUnicode('')) == '""\n...\n'
    assert yaml.dump(AnsibleUnicode(''), default_style=None) == '""\n...\n'
    assert yaml.dump(AnsibleUnicode('', style='|')) == '|\n...\n'



# Generated at 2022-06-22 11:31:21.656550
# Unit test for function represent_undefined
def test_represent_undefined():
    try:
        yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)
    except Exception as e:
        raise AssertionError('AnsibleDumper failed to represent AnsibleUndefined: %s' % e)

# Generated at 2022-06-22 11:31:30.604694
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    dloader = DataLoader()

# Generated at 2022-06-22 11:31:34.843715
# Unit test for function represent_hostvars
def test_represent_hostvars():
    hv = HostVars({"data": "SomeData"}, per_host_var_type='extra_var')
    assert yaml.dump(hv, Dumper=AnsibleDumper, default_flow_style=False) == \
        "data: SomeData\n"

# Generated at 2022-06-22 11:31:42.618990
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    # Create vault secret
    secret_string = 'ThisIsASecret'

    # Create vault object
    vault = VaultLib([])

    # Encrypt secret using vault object
    encrypted_secret = vault.encrypt(secret_string)

    # Create AnsibleVaultEncryptedUnicode object from secret
    encrypted_obj = AnsibleVaultEncryptedUnicode(encrypted_secret.encode())

    # Create yaml file for unit test
    yaml_file = '/tmp/testvault.yml'

    # Create variable manager for unit test
    variable_manager = VariableManager()

    # Register variable manager
    variable_manager.register_vault(vault)

    # Add variable to variable manager
    variable

# Generated at 2022-06-22 11:31:54.237223
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper
    # when data is a sequence of AnsibleUnicode
    data = [
        AnsibleUnicode('a'),
        AnsibleUnicode('b'),
    ]
    actual = dumper.represent_data(data)
    expected = u'\n- a\n- b'
    assert actual == expected

    # when data is a mapping of AnsibleUnicode
    data = [{
        AnsibleUnicode('a'): AnsibleUnicode('b'),
        AnsibleUnicode('c'): AnsibleUnicode('d'),
    }]
    actual = dumper.represent_data(data)
    expected = u'\n- a: b\n  c: d'
    assert actual == expected

    # when data is a mapping of AnsibleUnicode including

# Generated at 2022-06-22 11:32:05.578956
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # pylint: disable=unused-variable
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultSecret

    secret = VaultSecret('secret')
    dumper = AnsibleDumper
    vault = VaultLib(secret)
    password_input = 'foobar'
    # pylint: disable=bad-option-value,unexpected-keyword-arg
    ciphertext = vault.encrypt('foobar', password_input, True)
    encrypted_data = AnsibleVaultEncryptedUnicode(ciphertext)

# Generated at 2022-06-22 11:32:10.198654
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()
    v = AnsibleVaultEncryptedUnicode('fake-ciphertext')
    assert dumper.represent_vault_encrypted_unicode(v) == yaml.representer.SafeRepresenter.represent_scalar(dumper, u'!vault', v._ciphertext.decode(), style='|')


# Generated at 2022-06-22 11:32:13.837839
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.dump({'ansible_inventory_sources': []}, Dumper=AnsibleDumper) == 'ansible_inventory_sources: []\n'

# Generated at 2022-06-22 11:32:18.541474
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert dumper.represent_undefined(AnsibleUndefined()) == True
    assert dumper.represent_undefined(list()) == False
    assert dumper.represent_undefined({}) == False
    assert dumper.represent_undefined(object()) == False

# Generated at 2022-06-22 11:32:28.072885
# Unit test for function represent_undefined
def test_represent_undefined():
    data = [[AnsibleUndefined(strict=True)]]
    dumper = AnsibleDumper()
    result = dumper.represent_data(data)
    # displaying the error would be verbose in test case
    dumper.default_flow_style = None
    assert result == "\n- - !error 'This value is undefined.'\n" + \
        "  - 'The error was converted to a string for YAML output - see below for '\n" + \
        "    'the original exception.'\n" + \
        "  - |-\n" + \
        "    __ansible_module_stderr__:\n" + \
        "      failed to parse: This value is undefined."



# Generated at 2022-06-22 11:32:34.954182
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleDumper.represent_binary(data=None, value=u'\x80')
    assert data == b'!binary |\n  IQ==\n'

# Generated at 2022-06-22 11:32:38.073616
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    assert dumper.represent_data(b'\xff\xfe') == {'!!binary': '//8='}



# Generated at 2022-06-22 11:32:44.806643
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    dumper = AnsibleDumper
    data = AnsibleMapping({
        "var1": "val1",
        "var2": "val2",
    })
    result = dumper.represent_hostvars(dumper, data)
    assert result == dumper.represent_dict({
        "var1": "val1",
        "var2": "val2",
    })

# Generated at 2022-06-22 11:32:53.625766
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    yaml_str = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          633262396330666234353531666563613961326263643133656566363664633664653066353062\n          3362346131383463396236373163316132303666653163662333036356634656566366330333032\n          33316133313166326236616563363233633636393037663162626332323335386239\n'
    yaml.add_representer(AnsibleVaultEncryptedUnicode, represent_vault_encrypted_unicode, SafeDumper)

# Generated at 2022-06-22 11:33:03.470281
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars import hostvars
    from ansible.vars.manager import VarsWithSources
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import wrap_var

    templar = Templar(loader=None)

    inventory = dict(
        one=dict(
            hostvars=dict(
                k1='v1',
                nested=dict(
                    another='one',
                ),
            ),
        ),
    )

    result = yaml.dump(inventory, Dumper=AnsibleDumper, default_flow_style=False)
    assert result == """\
one:
  hostvars:
    nested:
      another: one
    k1: v1
"""

# Generated at 2022-06-22 11:33:07.720927
# Unit test for function represent_undefined
def test_represent_undefined():
    yaml_dumper = AnsibleDumper
    yaml_dumper.add_representer(
        AnsibleUndefined,
        represent_undefined,
    )

    yaml_data = yaml.dump(AnsibleUndefined, Dumper=yaml_dumper)
    assert yaml_data is not None

# Generated at 2022-06-22 11:33:11.761038
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    str_value = 'hello world \x00'
    assert dumper.represent_binary(str_value) == dumper.represent_str(str_value)

# Generated at 2022-06-22 11:33:14.630647
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b"\x00", Dumper=AnsibleDumper) == "!!binary \"\\x00\"\n"


# Generated at 2022-06-22 11:33:19.438166
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    # Note: "vault" is not a valid identifier in YAML spec,
    # but it's used as a tag in ansible
    assert yaml.dump(AnsibleVaultEncryptedUnicode('test', 'vault'),
                     Dumper=AnsibleDumper) == '!vault |\n  vault(test)\n'

# Generated at 2022-06-22 11:33:24.563001
# Unit test for function represent_undefined
def test_represent_undefined():
    try:
        yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)
    except Exception as e:
        assert 'The error was: ' in str(e)
        assert AnsibleUndefined.ERROR_MSG in str(e)
    else:
        raise Exception("Expected exception")

# Generated at 2022-06-22 11:33:36.698135
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    encrypted_data = b'$ANSIBLE_VAULT;1.1;AES256\n3561646232633264653934306638646566373639353337323235343833313863396336633337343166\n3937643334366136366535373936303261333238363363353235316333656565373262376233356231\n3336303334613261336134333861653939356534376466306461626537396466\n'
    dumper = AnsibleDumper
    # assert that the vault data is properly represented in plain text
    # and that the ciphertext is not represented

# Generated at 2022-06-22 11:33:38.957540
# Unit test for function represent_binary
def test_represent_binary():
    data = dict(var=b'foo')
    expected = b'var: !!binary |\r\n  Zm9v\r\n'
    assert yaml.dump(data, Dumper=AnsibleDumper) == expected

# Generated at 2022-06-22 11:33:42.042746
# Unit test for function represent_binary
def test_represent_binary():
    '''
    Test to ensure that binary data can be represented.
    '''
    assert(yaml.dump(b'foo', Dumper=AnsibleDumper).strip() == 'foo')



# Generated at 2022-06-22 11:33:53.056498
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    au = AnsibleVaultEncryptedUnicode("vaultpassword", "somedata")
    actual = repr(yaml.dump({'test': au}, Dumper=AnsibleDumper))

# Generated at 2022-06-22 11:33:54.546862
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper) == ''


# Generated at 2022-06-22 11:34:05.765095
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.module_utils.six import StringIO
    from ansible.template import StrictUndefined
    from ansible.parsing.yaml.loader import AnsibleLoader

    test_data = StrictUndefined()
    test_stream = StringIO()
    test_loader = AnsibleLoader(test_data, file_name='<test_stream>')
    test_dumper = AnsibleDumper(test_loader)

    test_dumper.represent_undefined(test_data)
    test_dumper.serialize(test_data, test_stream=test_stream)

    # Serialize returns None and writes to stream
    assert test_dumper.serialize(test_data, test_stream=test_stream) is None
    assert test_stream.getvalue() == ""

# Generated at 2022-06-22 11:34:18.177928
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    v = VaultLib([])
    ciphertext = v.encrypt(to_bytes('test', encoding='utf-8'))

    data = AnsibleVaultEncryptedUnicode(ciphertext)
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:34:22.057583
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib({})
    value = vault.encrypt('foo')

    result = yaml.dump(value, Dumper=AnsibleDumper)
    assert result == "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          623239643063366633376266396262623135643130336466326234363435613962616362363130\n          6431633138383262666631623661620a6665373763386232636537643736336135633738643234\n          36\n"

# Generated at 2022-06-22 11:34:25.125392
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(None, None) is None
    assert represent_vault_encrypted_unicode(None, AnsibleVaultEncryptedUnicode('foo')) is not None


# Generated at 2022-06-22 11:34:32.700218
# Unit test for function represent_hostvars
def test_represent_hostvars():
    representer = AnsibleDumper()
    # test empty HostVars
    hostvars = HostVars()
    assert representer.represent_hostvars(hostvars) == '{}'
    # test non-empty HostVars
    hostvars.update({'lorem': 'ipsum'})
    assert representer.represent_hostvars(hostvars) == '{\n    lorem: \'ipsum\'\n}'


# Generated at 2022-06-22 11:34:43.121000
# Unit test for function represent_binary
def test_represent_binary():
    class TextIOWrapper:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    dumper = AnsibleDumper(None, default_style=None, default_flow_style=None, canonical=None, indent=None, width=None,
                           allow_unicode=None, line_break=None, encoding=None, explicit_start=None, explicit_end=None,
                           version=None, tags=None)

    dumper.open = lambda filename: TextIOWrapper(filename, "wb")

    represent_binary(dumper, "binary-data")
    output = dumper.open.call_args[0][0]
    assert isinstance(output, TextIOWrapper)

# Generated at 2022-06-22 11:34:44.906515
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.load(yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper))



# Generated at 2022-06-22 11:34:52.034608
# Unit test for function represent_binary
def test_represent_binary():
    """ Successfully represent binary data
    """
    from ansible.module_utils.six.moves import StringIO
    from ansible.utils.unsafe_proxy import wrap_var
    my_binary = wrap_var(b"\x01\x02\x03")

    stream = StringIO()
    dumper = AnsibleDumper(stream, default_flow_style=False, default_style=None, canonical=True)
    dumper.represent(my_binary)
    output = stream.getvalue()

    assert output == "!!binary 'AQID'\n"



# Generated at 2022-06-22 11:34:55.432765
# Unit test for function represent_hostvars
def test_represent_hostvars():

    data = {'key1': 'value1', 'key2': 'value2'}
    hostvars = HostVars(data)
    # For HostVars object, we want to dump {"key1": "value1", "key2": "value2"}
    # as plain dict.
    assert yaml.dump(hostvars, Dumper=AnsibleDumper) == u'{key1: value1, key2: value2}\n'

# Generated at 2022-06-22 11:34:58.469980
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    result = dumper.represent_data(AnsibleUndefined())
    # Should now raise error instead of return False
    assert result == 'false'

# Generated at 2022-06-22 11:35:07.016228
# Unit test for function represent_binary
def test_represent_binary():
    representer = yaml.representer.SafeRepresenter()
    representer.add_representer(
        AnsibleUnsafeBytes,
        represent_binary,
    )
    result = yaml.dump(AnsibleUnsafeBytes(b"$ANSIBLE_VAULT;1.1;AES256\n1234567890"), Dumper=representer)
    assert result == "!unsafe_bytes |\n  $ANSIBLE_VAULT;1.1;AES256\n  1234567890\n"


# Generated at 2022-06-22 11:35:11.486038
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = 'this is a test'
    data = AnsibleVaultEncryptedUnicode(data)
    ad = AnsibleDumper()
    # get string representation of data
    data_repr = ad.represent_data(data)
    # covert string to python obj
    yaml.load(data_repr)

# Generated at 2022-06-22 11:35:14.767774
# Unit test for function represent_undefined
def test_represent_undefined():
    false_data = True
    assert AnsibleDumper.represent_undefined(None, false_data) == False

    true_data = AnsibleUndefined
    assert AnsibleDumper.represent_undefined(None, true_data) == True

# Generated at 2022-06-22 11:35:19.320301
# Unit test for function represent_binary
def test_represent_binary():
    data = {'binary': b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'}
    dump = yaml.dump(data, Dumper=AnsibleDumper)
    assert dump == 'binary: !!binary |\n  AAABAQIDBAUGBwg=\n'

# Generated at 2022-06-22 11:35:22.890027
# Unit test for function represent_binary
def test_represent_binary():
    assert len(yaml.dump(binary_type('123'))) > 0
    assert len(yaml.dump(binary_type('123'), Dumper=AnsibleDumper)) > 0



# Generated at 2022-06-22 11:35:35.354038
# Unit test for function represent_hostvars
def test_represent_hostvars():
    '''
    represent_hostvars is a function, which takes a yaml.dumper object and
    AnsibleHostVars object holding data and writes the correct yaml
    representation to the dumper stream.
    '''
    dummy_vars = HostVars("dummyhost")
    dummy_vars.update({
        'my_var': 'test',
        'complex_var': {
            'complex_var_item': 'test',
        }
    })
    dump = yaml.dump(dummy_vars, default_flow_style=False, Dumper=AnsibleDumper)
    assert dump == '''\
complex_var:
  complex_var_item: test
my_var: test
'''


# Generated at 2022-06-22 11:35:37.480568
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    assert not dumper.represent_undefined(AnsibleUndefined('foo'))

# Generated at 2022-06-22 11:35:49.497816
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # Test data :
    # - hostvars = HostVars(data = { 'key1' : 'value_str', 'key2' : list_contents })
    # - list_contents = AnsibleUnicode(['item1', 'item2'])
    # - unicode_str = AnsibleUnicode(u'unicode string')

    list_contents = AnsibleUnicode([u'item1', u'item2'])
    unicode_str = AnsibleUnicode(u'unicode string')

    hostvars = HostVars(data = { u'key1' : unicode_str, u'key2' : list_contents })

# Generated at 2022-06-22 11:35:55.289274
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play

    v = VariableManager()
    p = Play()

    v.set_host_variable(host="foo.example.com", varname="myvar", value={"foo": "bar"})
    v.set_host_variable(host="foo.example.com", varname="myvar", value="test")

    myvar = v.get_vars(play=p, host="foo.example.com", task=None)['myvar']
    myvar_dict = dict(myvar)

    # Test a dict with a single child
    assert myvar_dict == {'foo.example.com': 'test'}

    # Test that a mapping whose key

# Generated at 2022-06-22 11:35:59.165059
# Unit test for function represent_binary
def test_represent_binary():
    data1 = b'\x00\x01\x02\x03'
    data2 = b'\x00\x01\x02\x03\x04'

    dumper = AnsibleDumper(indent=2, default_flow_style=False)

    rep1 = dumper.represent_binary(data1)
    rep2 = dumper.represent_binary(data2)

    assert rep1 == b'!!binary |-\n  AAEDAw\n'
    assert rep2 == b'!!binary |-\n  AAEDAwQ=\n'



# Generated at 2022-06-22 11:36:08.784458
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    text = 'This is some super secret text'
    encrypted_text = vault.encrypt(text)
    evu = AnsibleVaultEncryptedUnicode(encrypted_text)
    assert evu._ciphertext == encrypted_text
    assert represent_vault_encrypted_unicode(AnsibleDumper, evu) == u'!vault |\n          ' + encrypted_text
    assert represent_vault_encrypted_unicode(AnsibleDumper, evu) == u'!vault |\n          ' + encrypted_text

# Generated at 2022-06-22 11:36:11.770531
# Unit test for function represent_hostvars
def test_represent_hostvars():
    d = {'a': 1, 'b': 2}
    assert(represent_hostvars(AnsibleDumper, d) == AnsibleDumper.represent_dict(d))



# Generated at 2022-06-22 11:36:20.658911
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # create hostvars object
    hostvars = HostVars()
    hostvars.add_host_vars('test_host',
                           {'var1': 'value1',
                            'var2': 'value2',
                            'var3': 'value3'})
    # create safe dumper instance
    yaml_dumper = yaml.SafeDumper
    yaml_dumper.ignore_aliases = lambda self, data: True
    # test
    ret = AnsibleDumper.represent_hostvars(yaml_dumper, hostvars)
    # verify

# Generated at 2022-06-22 11:36:28.760578
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    class TestVaultEncryptedUnicode:
        def __init__(self, ciphertext):
            self._ciphertext = ciphertext

    v3 = TestVaultEncryptedUnicode(b'\x01\x02\x03\x04')
    data = {'foo': v3}
    expected = '''\
foo: !vault |
          AAEAAQ==
'''
    actual = yaml.dump(data, Dumper=AnsibleDumper, explicit_start=True, explicit_end=True)
    assert expected == actual



# Generated at 2022-06-22 11:36:38.144280
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.hostvars import HostVars

    # Creates a dictionary with the following structure:
    # {'foo': 'bar', 'baz': '3', 'apple': 'boy', 'b0': 'b1', 'blist': 'bleh'}
    class MyDict(dict):
        pass

    # Creates a dictionary with the following structure:
    # {'foo': 'bar', 'baz': '3', 'apple': 'boy', 'b0': 'b1', 'blist': 'bleh'}

# Generated at 2022-06-22 11:36:46.920076
# Unit test for function represent_binary
def test_represent_binary():
    data = binary_type(b'bytes')
    assert yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, data) == "!!binary |\n  Ynl0ZXM=\n"



# Generated at 2022-06-22 11:36:49.903248
# Unit test for function represent_binary
def test_represent_binary():
    out = yaml.dump(b'foo', Dumper=AnsibleDumper, allow_unicode=True)
    assert out == u"!!binary |\n  Zm9v\n\n"

# Generated at 2022-06-22 11:37:00.344657
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('test')
    assert yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True) == '!vault |\n          V2Jhc2ljIEFQSTQgdmVyc2lvbgECbXRmMnRjNzM0\n          CWJhc2U2NCB2ZXJzaW9uAQAhc2hha2VkIG91dCB0by\n          AxYzYWYwNjYwYzY1Mjg4MWVlMzcxYjA4Y2I4Y2Vh\n          NDJhYjU3MzU3ZDQ2ZTRjNzQw\n'

# Generated at 2022-06-22 11:37:03.397311
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(None)
    test = AnsibleUndefined('test_represent_undefined')
    assert not dumper.represent(test)

# Generated at 2022-06-22 11:37:05.173051
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    test_dump = AnsibleDumper().represent_vault_encrypted_unicode("1234")
    assert isinstance(test_dump, str)

# Generated at 2022-06-22 11:37:07.356651
# Unit test for function represent_undefined
def test_represent_undefined():
    assert not yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:37:17.466280
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    vault_obj = AnsibleVaultEncryptedUnicode('test')
    result = represent_vault_encrypted_unicode(None, vault_obj)
    assert result == ("!vault |\n" "          $ANSIBLE_VAULT;1.1;AES256\n"
                      "          343361356130633165313462626239353731616433306534333137313237626666313932376539\n"
                      "          396634316166376339623466383737393330346637643537366330353733396165616438356130\n"
                      "          326134313236626232306665346433333035343361356666\n")

# Generated at 2022-06-22 11:37:29.332619
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    # initialize vault object as in module_utils/basic.py
    vault = VaultLib(['/dev/null'])
    # encrypt data
    plaintext = u'baredata'
    ciphertext = vault.encrypt(plaintext)
    # create vault encrypted unicode object
    data = AnsibleVaultEncryptedUnicode(ciphertext)
    # create dumper
    dumper = AnsibleDumper()
    # run test
    result = dumper.represent_data(data)
    # check result
    expected = u"!!python/object/apply:ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode\n- !vault |\n  $ANSIBLE_VAULT;" + ciphertext + "\n"
   

# Generated at 2022-06-22 11:37:40.923595
# Unit test for function represent_binary
def test_represent_binary():
    dumper = yaml.Dumper
    representer = AnsibleDumper.represent_binary
    o = u'\x00\x01\x02\x03\x04\x05\x06\x07'
    assert(representer(dumper, o) == yaml.representer.SafeRepresenter.represent_binary(dumper, o))
    o = u'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10'
    assert(representer(dumper, o) == yaml.representer.SafeRepresenter.represent_binary(dumper, o))
    o = u'\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A'

# Generated at 2022-06-22 11:37:43.239135
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = {'foo': 'bar'}
    stream = yaml.dump(HostVars(data))
    assert stream == '{foo: bar}\n'

# Generated at 2022-06-22 11:37:51.721626
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleDumper.represent_binary(AnsibleDumper, AnsibleUnsafeBytes(b'\xc3\xa9'))
    assert data == "!!binary |\n  w5LDqQ==\n"



# Generated at 2022-06-22 11:38:00.480741
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper()

# Generated at 2022-06-22 11:38:03.683366
# Unit test for function represent_binary
def test_represent_binary():
    data = AnsibleUnsafeBytes(b'foo')
    rep = AnsibleDumper.represent_binary(data)
    assert rep == '!!binary "Zm9v"'

# Generated at 2022-06-22 11:38:09.327176
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = yaml.dumper.SafeDumper
    hostvars = HostVars()
    hostvars['test_a'] = 'test_a'
    hostvars['test_b'] = 'test_b'
    hostvars._sources = 'test'
    data = {'test': hostvars}
    output = yaml.dump(data, Dumper=dumper)
    assert output == b'test:\n  test_a: test_a\n  test_b: test_b\n'



# Generated at 2022-06-22 11:38:17.030080
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    test_data = AnsibleVaultEncryptedUnicode("encrypted_data")
    expected = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          63616139373464393538336665356534353631366163343234633263333335633462353562333838\n          33396433663730313333383963633031333537316662636534303530620a32316338303839383364\n          3238373562643736303531383935303364343463643032373964383331333535366134636438376d\n          "
    result = yaml.dump(test_data, Dumper=AnsibleDumper, default_flow_style=False)
    assert result

# Generated at 2022-06-22 11:38:20.362598
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper([])
    assert dumper.represent_binary(b'\xe4') == u'!!binary |-\n  w5Q=\n'

# Generated at 2022-06-22 11:38:26.865014
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import HostVars, HostVarsVars


    # gen data
    hvars = HostVars()
    hvars["a"] = 1
    hvars["b"] = 2

    # use it
    result = yaml.dump(hvars, Dumper=AnsibleDumper)

    # check result
    assert "a: 1" in result
    assert "b: 2" in result



# Generated at 2022-06-22 11:38:30.910427
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('12345abcde')
    assert represent_vault_encrypted_unicode(None, data) == '!vault |\n          MTIzNDVhYmNkZQ==\n'

# Generated at 2022-06-22 11:38:33.177623
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(AnsibleDumper, HostVars({'first': 'one'})) == {'first': 'one'}

# Generated at 2022-06-22 11:38:41.816313
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    ciphertext = b'$ANSIBLE_VAULT;1.2;AES256;testhost\n'
    ciphertext += b'35313663356133626535333936356339653234626465616266393430333836633861373566\n'
    ciphertext += b'3966356164353063306238316235323464376263653137630a373262356637353033343965\n'
    ciphertext += b'39353737386538373862393161386138313431326534373338363533633234393537393363\n'

# Generated at 2022-06-22 11:38:58.789408
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    # Note: only want to represent the encrypted data
    rep_data = represent_vault_encrypted_unicode(AnsibleDumper, AnsibleVaultEncryptedUnicode('vaultvalue', 2))

    # the actual YAML text is not important, just ensure it is a scalar and it starts with |
    assert rep_data[0:2] == '|-'
    assert rep_data[-1] == '\n'
    assert type(rep_data) is str

# Generated at 2022-06-22 11:39:03.142828
# Unit test for function represent_hostvars
def test_represent_hostvars():
    data = dict(one=1, two=2, three=3)
    dumper = AnsibleDumper(width=1)
    output = yaml.dump(data, Dumper=dumper)
    assert output == '{one: 1, two: 2, three: 3}\n'



# Generated at 2022-06-22 11:39:06.802033
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode('vaulted_text_value')
    assert represent_vault_encrypted_unicode(AnsibleDumper, data) == u'!vault |\n  vaulted_text_value'



# Generated at 2022-06-22 11:39:11.140144
# Unit test for function represent_binary
def test_represent_binary():
    # TODO: This doesn't actually test anything, but it's not clear what it should test.
    #       It's been here untouched since it was added, when the function was added.
    #       Should we just remove it, or update it to actually test something?
    represent_binary(None, b'1234')

# Generated at 2022-06-22 11:39:15.469351
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    data = u'asdf\u0633'
    result = dumper.represent_binary(dumper, data)

    assert(result == b'!!binary |\n  YXNkZow2z\n')

# Generated at 2022-06-22 11:39:19.584655
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    data = b'\x21'
    repr = dumper.represent_binary(dumper, data)
    assert repr == u'!binary |\n  !binary |\n    IQ==\n'

# Generated at 2022-06-22 11:39:23.066501
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = yaml.dumper.Dumper
    dumper.represent_scalar = lambda a, b, c: "foo"
    assert represent_vault_encrypted_unicode(dumper, "") == "foo"

# Generated at 2022-06-22 11:39:26.838006
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    dumper = AnsibleDumper()
    assert dumper.represent_hostvars(HostVars()) == dumper.represent_dict({})

# Generated at 2022-06-22 11:39:33.877736
# Unit test for function represent_hostvars
def test_represent_hostvars():
    """
    Unit test for function represent_hostvars.
    """
    representer = AnsibleDumper()
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_hostvars = HostVars(group_names=['group1', 'group2'], vault_password='myVault', host_vars_vars=my_dict)
    representer.represent_hostvars(my_hostvars)
    assert representer.represent_hostvars(my_hostvars)

# Generated at 2022-06-22 11:39:41.086207
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.vars.hostvars import HostVars
    import io
    import sys

    # ansible_hostvars will be dumped as hostvars in a dict
    hv = HostVars()
    hv.set_variable('test1', 'test1')
    hv.set_variable('test2', 'test2')

    c = AnsibleDumper()
    c.indent = 4
    c.default_flow_style = False
    c.allow_unicode = True

    output = io.StringIO()
    sys.stdout = output
    sys.stderr = output

    c.represent(hv)

    output_content = output.getvalue()
    output.close()
