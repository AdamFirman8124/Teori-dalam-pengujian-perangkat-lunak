

# Generated at 2022-06-22 11:29:48.632987
# Unit test for function represent_binary
def test_represent_binary():
    data = b'\x92\xe2\xc5\xf0\xff'
    assert yaml.safe_dump(data, Dumper=AnsibleDumper) == '!!binary |\n  8mmeJjd/\n'

# Generated at 2022-06-22 11:29:54.811953
# Unit test for function represent_unicode
def test_represent_unicode():
    def check(value, expected):
        dumper = AnsibleDumper
        actual = dumper.represent_unicode(dumper, value)
        assert actual == expected

    check(
        AnsibleUnicode(u'foo'),
        'foo\n...\n'
    )

    check(
        AnsibleUnicode(u'foo\nbar'),
        '|-\n  foo\n  bar\n'
    )

# Generated at 2022-06-22 11:29:58.205151
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert yaml.dump(AnsibleVaultEncryptedUnicode("test"), Dumper=yaml.dump) == '!vault |\n  $ANSIBLE_VAULT;1.1;AES256\ntest'

# Generated at 2022-06-22 11:30:10.280299
# Unit test for function represent_unicode
def test_represent_unicode():
    import datetime

    def r(d):
        return yaml.dump(d, Dumper=AnsibleDumper)

    assert r(u'asdf') == u'asdf\n...\n'
    assert r(AnsibleUnsafeText(u'asdf')) == u'asdf\n...\n'
    assert r(AnsibleUnsafeBytes(u'asdf')) == u'asdf\n...\n'
    assert r(AnsibleUnicode(u'asdf')) == u'asdf\n...\n'
    assert r(datetime.datetime(2014, 1, 2, 3, 4, 5)) == u'2014-01-02 03:04:05\n...\n'
    assert r(obj()) == u'obj()\n...\n'



# Generated at 2022-06-22 11:30:20.710338
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.template.vars import AnsibleJ2Vars

    dumper = AnsibleDumper()
    templar = Templar(loader=None, variables=AnsibleJ2Vars(basedir=None, extra_vars=[], context=dict(),
                                                           templar=None, vars_cache=dict()),
                      shared_loader_obj=None, environment=None, fail_on_undefined=False)

    play = Play().load(dict(hosts='localhost', gather_facts=False, tasks=[dict(
        action=dict(module='debug', args=dict(msg=AnsibleUndefined)))]), loader=None, templar=templar)

    play

# Generated at 2022-06-22 11:30:28.114724
# Unit test for function represent_hostvars
def test_represent_hostvars():
    dumper = AnsibleDumper()
    hostVars = HostVars()
    hostVars.add_host_vars(
        host=dict(
            ansible_host='foo',
        ),
        hostvars=dict(
            x=1,
            y=2,
        ))
    hostVars.add_host_vars(
        host=dict(
            ansible_host='bar',
        ),
        hostvars=dict(
            z=3,
            w=4,
        ))

    print(dumper.represent_data(hostVars))



# Generated at 2022-06-22 11:30:32.778881
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert represent_unicode(AnsibleDumper, AnsibleUnicode('hello')) == 'hello'
    assert represent_unicode(AnsibleDumper, 'hello') == 'hello'
    assert represent_unicode(AnsibleDumper, '\u00e7') == u'\u00e7'.encode('utf-8')
    assert represent_unicode(AnsibleDumper, u'\u00e7') == u'\u00e7'.encode('utf-8')

# Generated at 2022-06-22 11:30:44.676001
# Unit test for function represent_unicode
def test_represent_unicode():
    # unicode has support both in python2 and python3.
    # so it can use the method of AnsibleDumper directly
    u = u'{"key1": "value", "key2": ["value1", "value2"]}'
    yaml.load(u)

    a = u'{"key1": "value", "key2": ["value1", "value2"], "_ansible_verbose_override": true, "omit_ansible_version": true, "omit_ansible_tags": true, "ansible_loop_var": "item"}'
    yaml.load(a)

    # AnsibleUnsafeText
    unsafe_unicode = AnsibleUnsafeText(text_type(u), encoding=None, errors='strict')
    unsafe_unicode.__repr__()

    # AnsibleUn

# Generated at 2022-06-22 11:30:47.548463
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(r'\t\r\n', default_flow_style=False) == "!ansible_safe '\\\\t\\\\r\\\\n'\n"



# Generated at 2022-06-22 11:30:50.727769
# Unit test for function represent_binary
def test_represent_binary():
    for dumper in (AnsibleDumper, yaml.SafeDumper):
        represent_binary(dumper, '\0borat') == "!!binary |\n  AGJvcgF0"

# Generated at 2022-06-22 11:30:58.180845
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    # Create the data
    data = AnsibleVaultEncryptedUnicode(text_type('foo'))

    # Create the AnsibleDumper
    ad = AnsibleDumper()

    # Dump the data
    dumped = ad.represent_vault_encrypted_unicode(data)

    # Verify the dumped data
    assert dumped == '!vault |\n          Zm9v\n'

# Generated at 2022-06-22 11:31:01.684837
# Unit test for function represent_undefined
def test_represent_undefined():
    try:
        AnsibleDumper.represent_undefined(AnsibleUndefined())
        assert False, "Representing undefined did not fail"
    except yaml.representer.RepresenterError:
        pass

# Generated at 2022-06-22 11:31:08.598344
# Unit test for function represent_binary
def test_represent_binary():
    # test dumping a binary string with 'splitlines=True' set
    dumper = yaml.dumper.SafeDumper
    dumper.ignore_aliases = lambda self, data: True
    dumper.represent_str = represent_binary
    # test dumping a string with embedded newlines
    assert (yaml.dump(b"12\n3", Dumper=dumper, allow_unicode=True, default_flow_style=False) == "|-\n    12\n    3\n")


# Generated at 2022-06-22 11:31:18.887252
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # should match regex
    # {
    #   "host_ipv6_address": "[0:0:0::1]",
    #   "host_ipv4_address": "127.0.0.1",
    #   "hoisted_var": "bar"
    # }
    hvars = HostVars({
        'host_ipv6_address': '2a00:1450:400c:c07::53',
        'host_ipv4_address': '127.0.0.1',
        'hoisted_var': 'bar'
    })
    output = yaml.dump({'foo': hvars}, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:31:27.079989
# Unit test for function represent_undefined
def test_represent_undefined():

    class AnsibleUndefined(object):
        def __init__(self, msg):
            self.msg = msg

        def __bool__(self):
            raise Exception("__bool__ called")

        def __nonzero__(self):
            raise Exception("__nonzero__ called")

    undef = AnsibleUndefined("invalid")
    dumper = AnsibleDumper()
    try:
        dumper.represent_undefined(undef)
    except Exception:
        assert False, "represent_undefined didn't call __bool__"

# Generated at 2022-06-22 11:31:36.965540
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    test_encryption_key = b'\xbfF\xbb\xa3\xea\x8b\x14\x17\xf6m\x1a\xc8\x04\xbd/\x14g\xdd\x96\xd6\x92\x98\xd2\x9e\xe5\x86\xf5\xad\x8b\xd5\x94\xb5\xd0\xc8\x97\xd7\xe7\x16\x0e\xf0\xac\xb1\xef\xe9\x00\x10\x00\x10\x00'
    vault = Vault

# Generated at 2022-06-22 11:31:41.669977
# Unit test for function represent_binary
def test_represent_binary():
    representer = AnsibleDumper.represent_binary
    assert representer(None, b"foo") == yaml.representer.SafeRepresenter.represent_binary(None, b"foo")
    assert representer(None, AnsibleUnsafeBytes("foo")) == yaml.representer.SafeRepresenter.represent_binary(None, b"foo")

# Generated at 2022-06-22 11:31:43.535395
# Unit test for function represent_binary
def test_represent_binary():
    yaml_string = yaml.dump(binary_type(b'\xc3'), Dumper=AnsibleDumper)
    assert yaml_string == u"!binary |\n  w6k=\n"

# Generated at 2022-06-22 11:31:45.853057
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(ansible_payload, Dumper=AnsibleDumper).startswith('- !vault |')


# Generated at 2022-06-22 11:31:51.770860
# Unit test for function represent_binary
def test_represent_binary():
    # Represent binary object as Base64
    assert yaml.dump(binary_type(b'abcd'), Dumper=AnsibleDumper) == '!!binary "YWJjZA=="\n'
    # Represent it as str when allow_unicode is True
    assert yaml.dump(binary_type(b'abcd'), Dumper=AnsibleDumper, allow_unicode=True) == '!<!binary "YWJjZA==">\n'

# Generated at 2022-06-22 11:31:59.654157
# Unit test for function represent_unicode
def test_represent_unicode():
    '''
    Test for function represent_unicode

    Test:
    test function represent_unicode of yaml_loader.py

    TODO:
        - write a more complete unit test
    '''
    test_str = 'this is a test'
    out = AnsibleDumper.represent_unicode(None, test_str)
    assert out == 'this is a test'

# Generated at 2022-06-22 11:32:04.847511
# Unit test for function represent_hostvars
def test_represent_hostvars():

    test_obj = {'key1': 'value1', 'key2': 'value2'}
    test_hostvars = HostVars(test_obj)

    new_obj = yaml.dump(test_hostvars, Dumper=AnsibleDumper, default_flow_style=False)
    assert new_obj == '---\nkey1: value1\nkey2: value2\n'


# test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:32:07.651454
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(
        AnsibleUnicode("some text"), Dumper=AnsibleDumper
    ) == u'some text\n'



# Generated at 2022-06-22 11:32:10.623740
# Unit test for function represent_undefined
def test_represent_undefined():
    test = AnsibleUndefined('test')
    assert represent_undefined(test, test) == yaml.representer.SafeRepresenter.represent_undefined(test, test)

# Generated at 2022-06-22 11:32:19.633311
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = u'p$ea|lkajsdflkj'
    ciphertext = AnsibleVaultEncryptedUnicode(data)
    # simple check for a known, hardcoded value
    output = AnsibleDumper.represent_vault_encrypted_unicode(None, ciphertext)
    assert (output == '!vault |\n          iBYngL4J4hpmFJfRgwvJ1EQW8+9a3qFBg1fvYnY+d75AXpKVZoJWFwOR+zzTbT/T\n')

# Generated at 2022-06-22 11:32:23.152689
# Unit test for function represent_unicode
def test_represent_unicode():
    yaml_data = AnsibleUnicode('foo')
    y = yaml.dump(yaml_data, Dumper=AnsibleDumper)
    assert y == 'foo\n...\n'

# Generated at 2022-06-22 11:32:28.511825
# Unit test for function represent_binary
def test_represent_binary():

    data = b'test_represent_binary'
    data_len = len(data)
    result = yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, data)
    assert result.startswith('!!binary |-'), "return value should start with '!!binary |-'"
    assert len(result) == data_len + 10, 'len of return value should be len of data plus 10'

# Generated at 2022-06-22 11:32:35.211943
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = AnsibleVaultEncryptedUnicode(u'value')
    assert represent_vault_encrypted_unicode(None, data) == u'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          34336338373035393963376166636135643435353166633735376631633963643562366430383765\n          35616237316665356231633532613035663634653131666438356133373362\n          \n'



# Generated at 2022-06-22 11:32:41.928018
# Unit test for function represent_unicode
def test_represent_unicode():
    from ansible.module_utils._text import to_text
    test_obj = AnsibleUnicode('test_string')
    # ansible_unicode add unicode marker (u) before string
    test_obj_yaml = to_text(yaml.dump(test_obj, Dumper=AnsibleDumper, default_flow_style=False))
    assert test_obj_yaml == "u'test_string'"



# Generated at 2022-06-22 11:32:50.596851
# Unit test for function represent_unicode
def test_represent_unicode():
    # legacy:
    #   test if ansibleunicode is an unicode object in python2
    #   test if ansibleunicode is a str (unicode) object in python3
    assert type(AnsibleUnicode('foo')) == text_type

    # legacy:
    #   test if ansibleunicode is represented as unicode in python2
    #   test if ansibleunicode is represented as str (unicode) in python3
    assert yaml.dump(AnsibleUnicode('bar'), Dumper=AnsibleDumper, default_flow_style=False) == u'bar\n...\n'



# Generated at 2022-06-22 11:33:00.452149
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n343539663734613361386263326461313435623463643330333861616637333262666164616466\n62316365303366343536653633613461323934303839643530376637353462653939\n'
    ansible_dumper = AnsibleDumper()
    result = ansible_dumper.represent_vault_encrypted_unicode(data)
    assert(result == data)

# Generated at 2022-06-22 11:33:03.200149
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    result = dumper.represent_binary(dumper, b"\x00")
    assert result == "!!binary |\n  AA=="

# Generated at 2022-06-22 11:33:05.632501
# Unit test for function represent_undefined
def test_represent_undefined():

    output = yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper)
    assert output == '{}\n'

# Generated at 2022-06-22 11:33:16.927085
# Unit test for function represent_undefined
def test_represent_undefined():
    # Create a new dumper for this test as the AnsibleDumper is
    # modified during loading and it will fail in the first call
    # to represent_undefined
    dumper = AnsibleDumper(None)
    from jinja2.runtime import StrictUndefined, Undefined
    from ansible.template import Jinja2Undefined
    from ansible.template.safe_eval import UndefinedError
    assert dumper.represent_undefined(Undefined('test'))
    assert dumper.represent_undefined(Jinja2Undefined('test'))
    try:
        dumper.represent_undefined(StrictUndefined('test'))
    except UndefinedError as exc:
        assert 'test' in str(exc)
    else:
        raise AssertionError('UndefinedError not raised')

# Generated at 2022-06-22 11:33:18.160096
# Unit test for function represent_undefined
def test_represent_undefined():
    my_var = AnsibleUndefined('test')
    assert not my_var

# Generated at 2022-06-22 11:33:25.813057
# Unit test for function represent_binary
def test_represent_binary():
    from ansible.template.safe_eval import unsafe_proxy, ANSIBLE_KEEP_REMOTE_FILES
    text = "test"

    for proxy in [unsafe_proxy, unsafe_proxy(keep_remote_files=ANSIBLE_KEEP_REMOTE_FILES)]:
        assert represent_binary(AnsibleDumper, proxy(text)) == \
            yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, binary_type(text))



# Generated at 2022-06-22 11:33:34.842570
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    result = dumper.represent_binary(dumper, b'8\x06\x06\x06\x06\x06\x06\x06\x06}')
    assert result == u'!!binary |\n  OCAvXGAvXGAvXGAvXGAvXGAvXGAvXGAvXGAvfQ==\n', \
        "Result is: %r, expected: '!!binary |\n  OCAvXGAvXGAvXGAvXGAvXGAvXGAvXGAvXGAvfQ==\n'" % result

if __name__ == '__main__':
    print(yaml.dump([1, 2, 3], Dumper=AnsibleDumper, default_flow_style=False))

# Generated at 2022-06-22 11:33:41.252951
# Unit test for function represent_hostvars
def test_represent_hostvars():
    value = yaml.dump(HostVars(dict({"a": "b"}), sources=[]),
                      Dumper=AnsibleDumper)
    ref = "a: b\n"
    try:
        assert value == ref
    except AssertionError:
        raise AssertionError(
            "Test failed: actual output does not match expected output:%s"
            " !=%s" % (value, ref)
        )



# Generated at 2022-06-22 11:33:46.496731
# Unit test for function represent_hostvars
def test_represent_hostvars():
    d = AnsibleDumper()
    assert d.represent_hostvars({'some_variable': 'some_value'}) == d.represent_dict({'some_variable': 'some_value'})
    assert d.represent_hostvars({}) == d.represent_dict({})
    assert d.represent_hostvars(None) == d.represent_dict({})

# Generated at 2022-06-22 11:33:57.120010
# Unit test for function represent_hostvars
def test_represent_hostvars():

    # Test 1
    # Expected result:
    # {"key1": 1, "key2": 2, "key3": 3}
    data_dict = {u'key1': 1, u'key2': 2, u'key3': 3}
    data_hostvars = HostVars(data_dict)
    output = yaml.dump(data_hostvars, Dumper=AnsibleDumper)
    expected_output = '{key1: 1, key2: 2, key3: 3}\n'
    assert(output == expected_output)

    # Test 2
    # Expected result:
    # {"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}

# Generated at 2022-06-22 11:34:01.881580
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(AnsibleDumper,
        AnsibleVaultEncryptedUnicode(b'1234')) == '!vault |\n  MTIzNA==\n'

# Generated at 2022-06-22 11:34:04.840187
# Unit test for function represent_binary
def test_represent_binary():
    d = yaml.Dumper()
    yaml_dump = yaml.dump(binary_type(b'\x00\xFF'), Dumper=AnsibleDumper)
    assert yaml_dump == '!!binary "AP8="\n'

# Generated at 2022-06-22 11:34:12.378214
# Unit test for function represent_unicode
def test_represent_unicode():

    value = AnsibleUnicode('test')
    expected = 'test'
    result = represent_unicode(None, value)
    assert result == yaml.representer.SafeRepresenter.represent_str(None, expected)

    value = AnsibleUnsafeText('test')
    result = represent_unicode(None, value)
    assert result == yaml.representer.SafeRepresenter.represent_str(None, expected)



# Generated at 2022-06-22 11:34:14.536961
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert yaml.safe_load(yaml.dump(dict(HostVars()))) == dict()



# Generated at 2022-06-22 11:34:22.423219
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper
    assert dumper.represent_binary(dumper, binary_type('foo')) == dumper.represent_str(dumper, text_type('foo'))
    assert dumper.represent_binary(dumper, binary_type('\xff')) == u"!binary |-\n  /+MA==\n"
    assert dumper.represent_binary(dumper, binary_type('\xff\xfe\xf0\x0f')) == u"!binary |-\n  /+gA//5A=\n"


# Generated at 2022-06-22 11:34:28.811826
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault = VaultLib([])
    ciphertext = vault.encrypt(b'foobar')
    value = AnsibleVaultEncryptedUnicode(ciphertext)
    dumped = yaml.dump([value], Dumper=AnsibleDumper)
    loaded = yaml.safe_load(dumped)
    assert value == loaded[0]



# Generated at 2022-06-22 11:34:36.858568
# Unit test for function represent_unicode
def test_represent_unicode():
    dumper = AnsibleDumper

    # Make a list of data so that it works for both
    # python 3 and python 2
    encoded_data = [u"hello", b"hello"]

    # For each encoded data
    for encoded in encoded_data:
        # Encode to yaml
        yaml_data = dumper.represent_unicode(dumper, encoded)

        # Convert to python dict
        python_data = yaml.load(yaml_data)

        # Decode unicode
        decoded = text_type(python_data)

        assert decoded == "hello", "Unicode representation is incorrect"



# Generated at 2022-06-22 11:34:46.324160
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    unencrypted_dict = {'foo': 'bar'}
    ciphertext_dict = {'foo': AnsibleVaultEncryptedUnicode('u8fNLxg7VwrPsHfY', '$ANSIBLE_VAULT;1.1;AES256', '16628003310f3c3a24363b4f4b2d4a3b')}
    # ciphertext_dict is expected to be "{'foo': !vault |\n$ANSIBLE_VAULT;1.1;AES256\n383338303138623235656434303265663737353332326263346231666136646164366433623463313\n6336338343865383338303536653134326663396266623166613638313463333261316265

# Generated at 2022-06-22 11:34:48.870882
# Unit test for function represent_binary
def test_represent_binary():

    s = 'some binary string'

    result = yaml.dump(s, Dumper=AnsibleDumper)

    assert(result == '"some binary string"\n')



# Generated at 2022-06-22 11:34:55.750348
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    ctx = PlayContext()
    ctx.network_os = 'ios'
    ctx._ansible_vars = HostVars(loader=loader, context=ctx)
    ctx._ansible_vars['inventory_hostname'] = "foobar"
    ctx._ansible_vars['foo'] = "bar"

    yaml_res = yaml.dump(dict(ctx._ansible_vars), Dumper=AnsibleDumper, default_flow_style=False, allow_unicode=True)
    assert (yaml_res == """foo: bar
inventory_hostname: foobar\n""")



# Generated at 2022-06-22 11:35:01.028310
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(None, None)
    assert represent_undefined(dumper, AnsibleUndefined(str_type='unicode')) is False

# Generated at 2022-06-22 11:35:04.313455
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper(None)
    undefined = AnsibleUndefined()
    assert dumper.represent_data(undefined) is False

# Generated at 2022-06-22 11:35:07.170106
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    assert dumper.represent_binary(b'some data') == '!!binary |-\n  c29tZSBkYXRh\n'

# Generated at 2022-06-22 11:35:10.785102
# Unit test for function represent_hostvars
def test_represent_hostvars():
    result = represent_hostvars(yaml, HostVars({'hostvars': 1}))
    assert result.startswith('{hostvars: 1')
    assert result.endswith('}')



# Generated at 2022-06-22 11:35:12.380882
# Unit test for function represent_binary
def test_represent_binary():
    assert AnsibleDumper.represent_binary(b'\x00\x01') == AnsibleDumper.represent_binary(u'\x00\x01')

# Generated at 2022-06-22 11:35:21.763540
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    '''
    Test to ensure strings encrypted with AnsibleVaultEncryptedUnicode
    are represented as vault encrypted strings.
    '''
    text = 'test string'

# Generated at 2022-06-22 11:35:32.339499
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()

    dumper.represent_binary(b'1234')

# Generated at 2022-06-22 11:35:41.174027
# Unit test for function represent_hostvars
def test_represent_hostvars():
    # We use dict(data) because AnsibleVars.get_vars()
    # returns a special HostVarsVars object. That will be
    # converted to a dict by dict(data)
    data = dict(HostVars({"foo": 1, "bar": 2}).get_vars())
    result = yaml.safe_dump(data, Dumper=AnsibleDumper)

    # If a value is a dict, the dict will be converted to
    # a list of dicts of size 1.
    assert result == '{bar: 2, foo: 1}\n'



# Generated at 2022-06-22 11:35:46.781785
# Unit test for function represent_unicode
def test_represent_unicode():
    text = u'\u043f\u0440\u0438\u0432\u0435\u0442'
    assert text == yaml.dump(text, Dumper=AnsibleDumper, default_flow_style=True, encoding='utf-8').strip(), \
        "Non-ascii characters were not dumped correctly"



# Generated at 2022-06-22 11:35:54.306727
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import AnsibleUndefined

    class FakeDumper(object):
        pass

    fake_dumper = FakeDumper()
    fake_dumper._fail_with_undefined_error = False

    # _fail_with_undefined_error is true and AnsibleUndefined._fail_on_undefined_errors is set
    AnsibleUndefined._fail_on_undefined_errors = True
    assert represent_undefined(fake_dumper, AnsibleUndefined()) is True

    # _fail_with_undefined_error is false and AnsibleUndefined._fail_on_undefined_errors is set
    AnsibleUndefined._fail_on_undefined_errors = True
    assert represent_undefined(fake_dumper, AnsibleUndefined()) is False

    # AnsibleUndefined._fail_on_undefined