

# Generated at 2022-06-22 11:29:50.399133
# Unit test for function represent_unicode
def test_represent_unicode():
    assert yaml.dump(u'some \x99 unicode', Dumper=AnsibleDumper) == u'some \xa9 unicode\n...\n'


import unittest

from ansible.module_utils import six



# Generated at 2022-06-22 11:29:52.789178
# Unit test for function represent_binary
def test_represent_binary():
    dumper = AnsibleDumper()
    assert dumper.represent_binary(b'hello') == u'!binary |-\n  aGVsbG8=\n'

# Generated at 2022-06-22 11:30:02.107828
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert yaml.dump(AnsibleVaultEncryptedUnicode('foo'), Dumper=AnsibleDumper) == "!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  31383032333333633039353662316663633236636433333561623432666337613231393133633563\n  65643332333739336534303532353533393165626266613961350a30383139353633393864366537\n  31343635333730343332626161396562336361316135316531353265323631646336376665646362\n  62633861373165653932000a"


# Generated at 2022-06-22 11:30:14.344577
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper

    # Test undefined object
    assert dumper.represent_undefined(dumper, AnsibleUndefined)

    # Test undefined key in dictionary
    empty_dictionary = AnsibleMapping(None)
    empty_dictionary['foo'] = AnsibleUndefined
    assert dumper.represent_undefined(dumper, empty_dictionary)

    # Test undefined key in list
    empty_list = AnsibleSequence()
    empty_list.append(AnsibleUndefined)
    assert dumper.represent_undefined(dumper, empty_list)

    # Test undefined key in mixed list/dict
    mixed_list = AnsibleSequence()
    mixed_list.append(empty_dictionary)
    mixed_list.append(empty_list)

# Generated at 2022-06-22 11:30:21.375824
# Unit test for function represent_unicode
def test_represent_unicode():
    # Note, the only way to get a "true" unicode in Python2 is to
    # create a class and set __unicode__
    class UnicodeClass(object):
        def __unicode__(self):
            return u"foobaz"

    uc = UnicodeClass()
    assert yaml.dump(uc) == "foobaz\n...\n", \
           "Unexpected yaml dump for unicode class"



# Generated at 2022-06-22 11:30:25.706507
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.vars.unsafe_proxy import wrap_var

    test_data = AnsibleUnsafeText('foo')
    item = wrap_var(test_data)
    assert AnsibleDumper.represent_data(item) == u'!vault |2-\n  foo\n'



# Generated at 2022-06-22 11:30:28.006844
# Unit test for function represent_undefined
def test_represent_undefined():
    d = AnsibleDumper()
    assert d.represent_undefined(None) is None
    assert d.represent_undefined(AnsibleUndefined()) is False

# Generated at 2022-06-22 11:30:31.139798
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    assert represent_vault_encrypted_unicode(None, AnsibleVaultEncryptedUnicode('my_cipher_text')) == u'!vault |\n  bXlfY2lwaGVyX3RleHQ=\n'

# Generated at 2022-06-22 11:30:44.157457
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    data = {
        "vaulted": AnsibleVaultEncryptedUnicode(u"mydata")
    }
    actual = yaml.dump(data, Dumper=AnsibleDumper)

# Generated at 2022-06-22 11:30:55.010180
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    represent_vault_encrypted = represent_vault_encrypted_unicode()

    # Here the VaultEncrypted is encrypted and is safe
    vault_encrypted = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n332a3034316239633238323431626366616334636336133383364343331323262633863303061\n3365643063623434336636346536313165396638636361343562326166326230306332343536\n393835626634383038663163323539396230633636356232346530\n')

    dumper = yaml.dumper.SafeDumper()
    # Here we are testing the representation of the encrypted value

# Generated at 2022-06-22 11:31:00.210451
# Unit test for function represent_unicode
def test_represent_unicode():
    data = AnsibleUnicode('test')
    dumped = yaml.dump(data, Dumper=AnsibleDumper)
    assert dumped == "test\n...\n"


# Generated at 2022-06-22 11:31:05.744477
# Unit test for function represent_binary
def test_represent_binary():
    yaml_str = yaml.dump(
        {'test_bin': '\x00\x01\x02\x03\x04'},
        Dumper=AnsibleDumper,
        default_flow_style=False
    )
    assert yaml_str == '''
test_bin: !!binary |
  AAECAQQ=
'''

# Generated at 2022-06-22 11:31:13.721257
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    s = AnsibleVaultEncryptedUnicode('encrypted text')
    result = represent_vault_encrypted_unicode(None, s)

# Generated at 2022-06-22 11:31:20.193477
# Unit test for function represent_binary
def test_represent_binary():
    # two representers were defined, but only the latter should be kept
    assert len(AnsibleDumper.yaml_representers[binary_type]) == 1

    assert b'foo' == yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, b'foo')
    assert b'foo' == yaml.representer.SafeRepresenter.represent_binary(AnsibleDumper, AnsibleUnsafeBytes(b'foo'))

# Generated at 2022-06-22 11:31:31.288139
# Unit test for function represent_hostvars
def test_represent_hostvars():
    assert represent_hostvars(None, dict()) == dict()
    assert represent_hostvars(None, dict(a=1)) == dict(a=1)
    assert represent_hostvars(None, dict(a=dict(b=1))) == dict(a=dict(b=1))
    assert represent_hostvars(None, dict(a=dict(b=dict()))) == dict(a=dict(b=dict()))

    hostvars = HostVars(dict(a=1))
    assert represent_hostvars(None, hostvars) == dict(a=1)

    hostvars_vars = HostVarsVars(hostvars)
    assert represent_hostvars(None, hostvars_vars) == dict(a=1)

    vars_with_sources = Vars

# Generated at 2022-06-22 11:31:39.671795
# Unit test for function represent_hostvars
def test_represent_hostvars():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import AnsibleUndefined
    from ansible.vars.hostvars import HostVars

    a = AnsibleSequence()
    a.append(1)
    a.append('foo')
    a.append(AnsibleUndefined('bar'))

    b = AnsibleMapping()
    b['a'] = '1'
    b['c'] = AnsibleUndefined('foo')

    hv = HostVars()
    hv['a'] = a
    hv['b'] = b


# Generated at 2022-06-22 11:31:50.792370
# Unit test for function represent_hostvars
def test_represent_hostvars():
    import sys
    import io
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    import yaml

    my_hostvars = HostVars(Vars=HostVarsVars(
        ansible_ssh_host='192.168.1.1',
        ansible_ssh_port=22
    ))

# Generated at 2022-06-22 11:31:55.526686
# Unit test for function represent_binary
def test_represent_binary():
    da = {'a':'\x01\x02\x03\x04'}
    assert yaml.dump(da, Dumper=AnsibleDumper, default_flow_style=True) == "a: !!binary |\n  AQIDBA==\n"

# Generated at 2022-06-22 11:32:01.492896
# Unit test for function represent_unicode
def test_represent_unicode():
    '''Test that the AnsibleDumper correctly represents unicode strings'''
    yaml_doc = b"\xef\xbb\xbfunicode: \xe2\x99\xa5"
    assert yaml_doc == yaml.dump(dict(unicode=u"\u2665"), Dumper=AnsibleDumper)



# Generated at 2022-06-22 11:32:06.045390
# Unit test for function represent_unicode
def test_represent_unicode():
    represent = AnsibleDumper().represent_unicode

    # bytestring
    value = b'foo'
    result = 'foo\n...\n'
    assert represent(value) == result

    # unicode
    value = u'foo'
    result = 'foo\n...\n'
    assert represent(value) == result



# Generated at 2022-06-22 11:32:11.404838
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper
    representer = dumper.represent_undefined
    assert representer(dumper, AnsibleUndefined('test')) == True



# Generated at 2022-06-22 11:32:17.830720
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    vault = VaultLib([])
    raw = vault.encrypt('test')
    encrypted_data = AnsibleVaultEncryptedUnicode(raw)
    output = yaml.dump(encrypted_data, Dumper=AnsibleDumper)
    assert output == "!vault |\n  $ANSIBLE_VAULT;" + raw + '\n'

# Generated at 2022-06-22 11:32:29.395470
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():

    # We must call this method in order to add the vault representer
    # to the dumper
    AnsibleDumper.yaml_representers = AnsibleDumper.yaml_representers.copy()

    # Sample ciphertext

# Generated at 2022-06-22 11:32:31.550919
# Unit test for function represent_unicode
def test_represent_unicode():
    print(yaml.dump(AnsibleUnicode('test_string_xyz'), Dumper=AnsibleDumper, default_flow_style=False))


if __name__ == '__main__':
    test_represent_unicode()

# Generated at 2022-06-22 11:32:38.143219
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    fake_key = u'AES256'
    fake_vaulttext = u'$ANSIBLE_VAULT;1.1;' + fake_key + u'\n'
    eufake = AnsibleVaultEncryptedUnicode(u'Test!', fake_key)
    eufake._ciphertext = eufake._encrypt(u'Test!', fake_key)
    assert represent_vault_encrypted_unicode(AnsibleDumper, eufake) == fake_vaulttext + eufake._ciphertext.decode()
    assert eufake.decrypt(fake_key) == u'Test!'

# Generated at 2022-06-22 11:32:39.417550
# Unit test for function represent_undefined
def test_represent_undefined():
    value = AnsibleUndefined()
    assert yaml.dump(value, Dumper=AnsibleDumper, default_flow_style=False)

# Generated at 2022-06-22 11:32:43.084030
# Unit test for function represent_undefined
def test_represent_undefined():
    d = yaml.Dumper()
    d.represent_undefined = represent_undefined
    assert d.represent_data(True) == d.represent_data(AnsibleUndefined)



# Generated at 2022-06-22 11:32:46.767302
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.parsing.yaml.objects import AnsibleMapping
    assert text_type(AnsibleDumper.represent_undefined(None, AnsibleUndefined(scope=AnsibleMapping()))) == 'null'



# Generated at 2022-06-22 11:32:49.319425
# Unit test for function represent_undefined
def test_represent_undefined():
    from ansible.template import Templar
    templar = Templar()
    assert templar.template("{{ foo }}", dict(foo=AnsibleUndefined)) is None

# Generated at 2022-06-22 11:32:55.144775
# Unit test for function represent_undefined
def test_represent_undefined():
    # Representer will return False if value is Undefined
    assert yaml.safe_dump({'undef': False}, Dumper=AnsibleDumper) == 'undef: false\n'
    # Else the value is returned
    assert yaml.safe_dump({'undef': True}, Dumper=AnsibleDumper) == 'undef: true\n'



# Generated at 2022-06-22 11:33:06.897870
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    dumper = AnsibleDumper(default_flow_style=False)
    dumper.add_representer(
        AnsibleVaultEncryptedUnicode,
        represent_vault_encrypted_unicode,
    )
    ciphertext = b'AES256$p4$4$7IwWmZWTk7BjK2S0rxEgIw==$GTc0YTQ3ODUzZjU3ZjU1MGM0MGZkNzNhNDkwZmMzYzY='
    encrypted_str = AnsibleVaultEncryptedUnicode(ciphertext)
    result = dumper.represent_data(encrypted_str)
    actual = yaml.load(result)

# Generated at 2022-06-22 11:33:10.576510
# Unit test for function represent_vault_encrypted_unicode
def test_represent_vault_encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(ciphertext='myciphertext', context='mycontext')
    expected = "!vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  myciphertext\n"
    assert yaml.dump(obj, Dumper=AnsibleDumper) == expected


# Generated at 2022-06-22 11:33:18.235174
# Unit test for function represent_unicode
def test_represent_unicode():
    assert represent_unicode(AnsibleDumper, "hello") == "hello"
    assert represent_unicode(AnsibleDumper, "汉字") == "汉字"
    assert represent_unicode(AnsibleDumper, "日本語") == "日本語"
    assert represent_unicode(AnsibleDumper, "Ελληνικά") == "Ελληνικά"
    assert represent_unicode(AnsibleDumper, "עִבְרִית") == "עִבְרִית"

# Generated at 2022-06-22 11:33:29.193704
# Unit test for function represent_vault_encrypted_unicode

# Generated at 2022-06-22 11:33:32.910910
# Unit test for function represent_binary
def test_represent_binary():
    assert yaml.dump(b'bytes', Dumper=AnsibleDumper) == '!binary |\n  bytes\n'
    assert yaml.dump(b'a\x00b', Dumper=AnsibleDumper) == '!binary |\n  YQBi\n'

# Generated at 2022-06-22 11:33:35.174299
# Unit test for function represent_unicode
def test_represent_unicode():
    s = 'hello'
    result = represent_unicode(SafeDumper, s)

    assert result == u'hello'

# Generated at 2022-06-22 11:33:37.251594
# Unit test for function represent_undefined
def test_represent_undefined():
    representer = AnsibleDumper.yaml_representers[AnsibleUndefined]
    assert representer(represent_undefined, AnsibleUndefined()), 'AnsibleUndefined not represented'

# Generated at 2022-06-22 11:33:38.872061
# Unit test for function represent_undefined
def test_represent_undefined():
    assert AnsibleDumper.represent_undefined(None, AnsibleUndefined()) == True

# Generated at 2022-06-22 11:33:41.202895
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump({'a': AnsibleUndefined()}, Dumper=AnsibleDumper) == 'a: null\n...\n'

# Generated at 2022-06-22 11:33:44.319690
# Unit test for function represent_binary
def test_represent_binary():
    res = yaml.safe_dump(u"t\x00est", default_flow_style=False, Dumper=AnsibleDumper)
    assert yaml.load(res) == u"t\x00est"

# Generated at 2022-06-22 11:33:53.120290
# Unit test for function represent_undefined
def test_represent_undefined():
    undefined = AnsibleUndefined()
    dumper = AnsibleDumper()
    try:
        dumper.represent_data(undefined)
    except AnsibleUndefined as ex:
        assert ex == undefined
    else:
        raise AssertionError('AnsibleUndefined not raised')

# Generated at 2022-06-22 11:33:58.675533
# Unit test for function represent_undefined
def test_represent_undefined():
    """Test function represent_undefined"""
    data = AnsibleUndefined
    yaml_obj = yaml.YAML()
    yaml_obj.indent(mapping=2, sequence=4, offset=2)
    yaml_obj.default_flow_style = False
    yaml_obj.representer = AnsibleDumper
    assert yaml_obj.represent(data) == 'undefined\n...\n'

# Generated at 2022-06-22 11:34:01.006955
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    data = AnsibleUndefined('foo')
    ret = dumper.represent_data(data)
    assert isinstance(ret, bool)


# Generated at 2022-06-22 11:34:04.334379
# Unit test for function represent_undefined
def test_represent_undefined():
    data = AnsibleUndefined
    loader = yaml.Loader(None)
    dumper = yaml.Dumper(None)
    dumper.represent_undefined(data)
    return loader.construct_object(dumper.represent_data(None), deep=True)


# Generated at 2022-06-22 11:34:09.493461
# Unit test for function represent_undefined
def test_represent_undefined():
    """
    Check that represent_undefined represent value as bool and
    not as str.
    """
    repr_undefined = AnsibleDumper.representers[AnsibleUndefined]
    assert repr_undefined(AnsibleDumper, AnsibleUndefined()) == False

# Generated at 2022-06-22 11:34:20.911526
# Unit test for function represent_undefined
def test_represent_undefined():
    # changes since last commit: None
    # https://github.com/ansible/ansible/commit/7e9055be5cd5b6179dcec8f0d2a73a7acb6e5b45
    # line: 46
    ResultDumper = AnsibleDumper
    undef_obj = AnsibleUndefined
    # changes since last commit: removed dict()
    # https://github.com/ansible/ansible/commit/7e9055be5cd5b6179dcec8f0d2a73a7acb6e5b45
    # line: 47
    # update: dict() added because it doesn't throw an error
    # since dict is iterable
    test_dict = {undef_obj: 'undefined'}

# Generated at 2022-06-22 11:34:24.742352
# Unit test for function represent_undefined
def test_represent_undefined():
    try:
        yaml.dump(AnsibleUndefined, Dumper=AnsibleDumper)
    except AnsibleUndefined as e:
        assert type(e) == AnsibleUndefined

# Generated at 2022-06-22 11:34:30.967091
# Unit test for function represent_undefined
def test_represent_undefined():
    '''
    ansible/ansible#49797 - Check if represent_undefined function returns a
    boolean value.
    '''
    # We are using a random boolean value to test the ansible
    # represent_undefined function.
    random_boolean = True
    assert (isinstance(represent_undefined(None, random_boolean), bool) is True)

# Generated at 2022-06-22 11:34:33.651771
# Unit test for function represent_undefined
def test_represent_undefined():
    dumper = AnsibleDumper()
    undef = AnsibleUndefined
    assert repr(dumper.represent_data(undef)) == repr(text_type(bool(undef)))

# Generated at 2022-06-22 11:34:35.296849
# Unit test for function represent_undefined
def test_represent_undefined():
    assert yaml.dump(AnsibleUndefined(), Dumper=AnsibleDumper) is True