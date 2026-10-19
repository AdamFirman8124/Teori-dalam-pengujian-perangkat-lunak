

# Generated at 2022-06-13 07:28:16.795485
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Init a vault secret
    vault_secret = 'mysecret'
    # Calculate the encrypted data using the vault secret
    vault_data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          62333839633832393537393464623665373736356366343639656539633765363631663033616237\n          34343633343565346639623365666533343930653165343635363530383936346135313339626661\n          646638323965623635333964363565306264373364303535326566383364\n          '

# Generated at 2022-06-13 07:28:27.876538
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import os
    import sys
    import unittest
    mydir = os.path.dirname(__file__)
    # We need to find a file which is in the tests directory so we can get the filename from the full path
    testfile = os.path.join(mydir, 'testYAMLObject_test.yaml')


# Generated at 2022-06-13 07:28:32.467607
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Tests if the constructor correctly returns an unsafe version of the loaded object
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    c = AnsibleConstructor()
    object = AnsibleUnsafeText(u'test')
    unsafe = c.construct_yaml_unsafe(object)
    assert(isinstance(unsafe, AnsibleUnsafeText))
    assert(unsafe._unsafe is True)

# Generated at 2022-06-13 07:28:34.604745
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    assert(AnsibleConstructor.construct_yaml_str.__doc__ == AnsibleConstructor.construct_yaml_str.__doc__)


# Generated at 2022-06-13 07:28:41.858599
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # Test normal execution of similar to the example from yaml.constructor.SafeConstructor

# Generated at 2022-06-13 07:28:54.286402
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.module_utils.yaml_loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    if hasattr(loader, 'set_vault_secrets'):
        loader.set_vault_secrets([])
    if hasattr(loader, 'set_vault_password'):
        loader.set_vault_password(None)

    #
    # Test we store the line number for AnsibleUnicode.
    #

    line_number_data = loader.load(b"--- |\n    hello world\n")
    assert hasattr(line_number_data[0], "ansible_pos")
    assert line_number_data[0].ansible_pos == ("<unicode string>", 2, 1)

    #


# Generated at 2022-06-13 07:29:01.167516
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Given
    data = {
        'firstname': 'Joe',
        'lastname': 'Doe'
    }
    node = yaml.nodes.MappingNode(u'foo', [])
    node.value = [
        (yaml.nodes.ScalarNode(u'firstname', u'foo', 1, 1), yaml.nodes.ScalarNode(u'Joe', u'bar', 2, 2)),
        (yaml.nodes.ScalarNode(u'lastname', u'foo', 3, 3), yaml.nodes.ScalarNode(u'Doe', u'bar', 4, 4)),
    ]
    ac = AnsibleConstructor()
    # When
    d = ac.construct_yaml_map(node)
    # Then
    assert d.value

# Generated at 2022-06-13 07:29:15.053982
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Create a mapping node with a deep key referencing a sequence
    node = MappingNode(
        tag=u'tag:yaml.org,2002:map',
        value=[
            [
                ScalarNode(u'tag:yaml.org,2002:str', u'foo'),
                SequenceNode(
                    tag=u'tag:yaml.org,2002:seq',
                    value=[
                        ScalarNode(u'tag:yaml.org,2002:str', u'foo'),
                        ScalarNode(u'tag:yaml.org,2002:str', u'bar')
                    ]
                )
            ]
        ]
    )

    # Expected output:
    expected = {
        'foo': ['foo', 'bar']
    }

    # Instantiate the AnsibleConstructor and construct output from the node
   

# Generated at 2022-06-13 07:29:22.594526
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    obj = AnsibleConstructor()
    a = [obj.construct_yaml_seq, [None], None]
    assert ['1', '2'] == obj.construct_yaml_seq([None, ['1', '2']])
    assert ['1', ['2', '3']] == obj.construct_yaml_seq([None, ['1', ['2', '3']]])
    assert ['1', '2', '3'] == obj.construct_yaml_seq([None, ['1', '2', '3']])

# Generated at 2022-06-13 07:29:24.850682
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()
    node = MappingNode(None, None, None)
    data = constructor.construct_yaml_map(node)
    assert isinstance(data, AnsibleMapping)



# Generated at 2022-06-13 07:29:35.998949
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    input = """
        a: 1
        b: 2
        c: 3
    """

    construct = AnsibleConstructor()
    data = yaml.load(input, Loader=AnsibleLoader)
    expected_data = {'a': 1, 'c': 3, 'b': 2}
    import pdb; pdb.set_trace()
    assert data == expected_data


# Generated at 2022-06-13 07:29:45.036793
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    from collections import OrderedDict
    node = yaml.MappingNode(tag=u'tag:yaml.org,2002:map', value=[],
                            flow_style=None)
    data = OrderedDict()
    data.ansible_pos = (__file__, 1, 1)
    node.value.append((yaml.ScalarNode(tag=u'tag:yaml.org,2002:str',
                                       value=u'example1'), yaml.ScalarNode(
                                           tag='tag:yaml.org,2002:str',
                                           value=u'example2')))

# Generated at 2022-06-13 07:29:52.214327
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import crypt
    import yaml
    vault_secrets = ['test_password']

# Generated at 2022-06-13 07:30:03.170067
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml

    def construct_vault_encrypted_unicode(node):
        return AnsibleConstructor().construct_vault_encrypted_unicode(node)
    yaml.add_constructor(u'!vault-encrypted', construct_vault_encrypted_unicode)

    # encrypt data
    vault = VaultLib(
        vault_secrets=['dummy', 'secret'],
        vault_password_file=None,
        new_vault_password='secret'
    )
    ciphertext = vault.encrypt('mystring')

    # create yaml file
    ciphertext_yaml = '!vault-encrypted |\n  {}'.format(ciphertext)

# Generated at 2022-06-13 07:30:12.277895
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret


# Generated at 2022-06-13 07:30:19.672996
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:30:23.513560
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_str = '''---
                "test"
                '''
    p = AnsibleLoader(yaml_str)
    assert p.get_single_data().ansible_pos == ("<unicode>", 1, 0)

# Generated at 2022-06-13 07:30:34.800602
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import re
    import string
    import pytest
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    import ansible.parsing.vault as vault

# Generated at 2022-06-13 07:30:45.492733
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import ansible.parsing.yaml
    constructor = AnsibleConstructor()
    node = ansible.parsing.yaml.objects.AnsibleSequenceNode(['a', 'b'])
    seq = list(constructor.construct_yaml_seq(node))[0]
    assert seq == ['a', 'b']
    assert seq.start_mark == node.start_mark
    assert seq.end_mark == node.end_mark
    assert seq.ansible_pos == ('<string>', 1, 0)
    node2 = ansible.parsing.yaml.objects.AnsibleSequenceNode(['c', 'd'])
    node2.start_mark.line = 3
    node2.start_mark.column = 1

# Generated at 2022-06-13 07:30:50.840595
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    d = {
        'list': [1, 2],
        'dict': {'1': 1},
        'int': 1,
        'str': 'str',
        'unicode_str': u'str',
        'empty': None,
        'float': 1.1,
        'bool': False,
    }
    for key in d:
        input = '!unsafe %s' % key
        c = AnsibleConstructor()
        assert type(c.construct_yaml_unsafe(input)) == type(d[key])

# Generated at 2022-06-13 07:31:04.844362
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    instance = AnsibleConstructor()
    data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n' \
           '          32396637643566346430386265366534366666376233353235313161386232366532653162393639\n' \
           '          63393136653031353666633330393432663466\n'
    node = '!vault'
    ret = instance.construct_vault_encrypted_unicode(data, node)

# Generated at 2022-06-13 07:31:09.390062
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    test_string1 = '''\
    - a: A
      b: 1
    - c: C
      d: 2
    - e: E
      f: 3
    '''
    y = yaml.load(test_string1, Loader=yaml.BaseLoader)
    assert y[0].ansible_pos == (u'<unicode string>', 1, 5)
    assert y[1].ansible_pos == (u'<unicode string>', 4, 5)
    assert y[2].ansible_pos == (u'<unicode string>', 7, 5)
    assert y[0]['a'] == 'A'
    assert y[0]['b'] == 1
    assert y[1]['c'] == 'C'
    assert y[1]['d']

# Generated at 2022-06-13 07:31:11.829616
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    node1 = u'tag:yaml.org,2002:str'
    node2 = 'foo'
    ansibleConstructor = AnsibleConstructor()
    ansibleConstructor.construct_scalar = lambda node: node2
    result1 = ansibleConstructor.construct_yaml_str(node1)
    assert result1 == 'foo'
    assert type(result1) == AnsibleUnicode


# Generated at 2022-06-13 07:31:16.648625
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    line = '''
# comment
- hosts: myhosts
  vars:
    a: 1
    a: 2
    b: 3
'''
    md = yaml.load(line, Loader=AnsibleConstructor)
    assert md == {'a': 2, 'b': 3}
    return True


# Generated at 2022-06-13 07:31:21.028831
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    file_name = 'ansible.cfg'
    vault_secrets = ['ansible']
    node = None

    test = AnsibleConstructor(file_name, vault_secrets)
    assert isinstance(test.construct_yaml_seq(node), type(AnsibleSequence())), 'Expected AnsibleSequence'

# Generated at 2022-06-13 07:31:28.519929
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Test for basic constructor
    values = {b'a': (1, 2, 3), b'b': 4.0, b'c': u'unicode',
              b'd': b'str', b'e': ['sequence', b'bytes']}

    for k, v in values.items():
        const = AnsibleConstructor()
        node = const.construct_yaml_unsafe(k)
        assert v == node, 'Failed to convert {0}: {1}'.format(v, node)



# Generated at 2022-06-13 07:31:37.284376
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Simple test
    data = """
- 1
- 2
- 3
    """
    obj = yaml.load(data, Loader=AnsibleConstructor)
    assert obj.ansible_pos == ('<string>', 1, 1)
    assert obj[0].ansible_pos == ('<string>', 2, 2)
    assert obj[1].ansible_pos == ('<string>', 3, 2)
    assert obj[2].ansible_pos == ('<string>', 4, 2)

    # Test multiline data
    data = """
- 1

- 2
- 3
(some other string)
    """
    obj = yaml.load(data, Loader=AnsibleConstructor)
    assert obj.ansible_pos == ('<string>', 1, 1)

# Generated at 2022-06-13 07:31:39.649653
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    constructor = AnsibleConstructor()
    # Test a single file path with prefix
    value = 'file|/etc/test.conf'
    result = constructor.construct_yaml_unsafe(value)
    assert result == wrap_var(value)

# Generated at 2022-06-13 07:31:49.489117
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from io import StringIO
    from yaml import load

    # test AnsibleConstructor.construct_yaml_seq
    # we create a anonymous file-like object and pass it to load()
    fake = StringIO(u'[ "test1", "test2", "test3" ]')
    obj = load(fake, Loader=AnsibleConstructor)
    assert len(obj) == 3
    assert obj[0] == 'test1'
    assert obj[1] == 'test2'
    assert obj[2] == 'test3'

    # test AnsibleConstructor.construct_yaml_seq with empty list
    fake = StringIO(u'[]')
    obj = load(fake, Loader=AnsibleConstructor)
    assert len(obj) == 0



# Generated at 2022-06-13 07:32:04.593748
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:32:21.931115
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.loader import AnsibleLoader
    doc = """
    foo: bar
    bam: {'key': 'value'}
    """
    AnsibleConstructor.add_constructor(u'tag:yaml.org,2002:str', AnsibleConstructor.construct_yaml_str)
    AnsibleConstructor.add_constructor(u'tag:yaml.org,2002:python/unicode', AnsibleConstructor.construct_yaml_str)
    data = AnsibleLoader(doc, file_name=__file__).get_single_data()
    assert data == {u'foo': u'bar', u'bam': {u'key': u'value'}}



# Generated at 2022-06-13 07:32:26.060296
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml
    from ansible.config.data import ConfigData

    draft = ConfigData.instance()
    draft.DUPLICATE_YAML_DICT_KEY = 'error'
    data = '''\
- one
- {quot: -2, key: value}
- [three, four]
'''
    exp = [u'one', {u'quot': -2, u'key': u'value'}, [b'three', b'four']]
    # exp = [u'one', {u'quot': u'-2', u'key': u'value'}, [b'three', b'four']]
    res = yaml.load(data, Loader=AnsibleLoader)

# Generated at 2022-06-13 07:32:34.476432
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    with open(u'../test/test_constructor.yml','r') as test_constructor:
        yaml_data = yaml.load(test_constructor, Loader=AnsibleConstructor)

    assert u"value" in yaml_data[u"first_level_key"]
    assert yaml_data[u"first_level_key"][u"value"] == 3

    assert u"second_level_key" in yaml_data[u"first_level_key"]
    assert u"value" in yaml_data[u"first_level_key"][u"second_level_key"]

    assert yaml_data[u"first_level_key"][u"second_level_key"][u"value"] == u"second level value"

# Generated at 2022-06-13 07:32:42.470252
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    for value in [
            b'1', 1, 0xFF, 1.0,
            1j, 1+1j,
            True, False, None,
            [], (), {},
            set(), frozenset(),
            object(), object
    ]:
        constructor = AnsibleConstructor()
        node = object()
        wrapper = constructor.construct_yaml_unsafe(node)
        assert isinstance(wrapper, wrap_var)
        assert wrapper._obj == value
        assert wrapper._node == node

# Generated at 2022-06-13 07:32:44.573122
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    constructor = AnsibleConstructor()
    assert type(constructor.construct_yaml_str('foo')) == AnsibleUnicode



# Generated at 2022-06-13 07:32:47.095176
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    node = None
    construct = AnsibleConstructor()
    construct.vault_secrets = []
    construct.construct_yaml_seq(node)


# Generated at 2022-06-13 07:32:56.288624
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    try:
        import ansible
        from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
        from ansible.parsing.vault import VaultLib
    except ImportError:
        # Ansible not present, won't run the test
        return

    import yaml

    # Store vault password in environment variable, the test will remove it when done
    import os
    password='secret'
    os.environ['ANSIBLE_VAULT'] = 'secret'


# Generated at 2022-06-13 07:33:00.185970
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    obj = AnsibleConstructor()
    mapping = AnsibleMapping()
    mapping.ansible_pos = ('datasource', 1, 1)
    data = obj.construct_yaml_map(mapping)
    assert isinstance(data, AnsibleMapping)
    assert data.ansible_pos == ('datasource', 1, 1)



# Generated at 2022-06-13 07:33:03.569431
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    sample_str = 'somesample'
    value = yaml.load(sample_str, Loader=AnsibleConstructor)
    assert isinstance(value, AnsibleUnicode)
    assert value == sample_str


# Generated at 2022-06-13 07:33:11.959751
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import ansible
    from ansible.parsing.vault import VaultLib
    vault_pass = 'asdfasdf'
    vault_id = '11111111-1111-1111-1111-111111111111'
    vault_secrets = [{'vault_id': vault_id, 'password': vault_pass}]

    yaml_string = '''
---
name: test_var_in_value
candidate: test_var
interfaces:
  GigabitEthernet3:
    description: "{{description}}"
    unit:
        number: {{interface_unit}}
        family:
          inet:
            address:
              - {{ip}}/{{netmask}}
          inet6:
            address:
              - {{ip_6cidr}}
'''
    import ansible

# Generated at 2022-06-13 07:33:27.104999
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    a_constructor = AnsibleConstructor('filename')
    raw_dict = {'key1': 'val1', 'key2': 'val2'}
    # Test normal dict
    data = a_constructor.construct_mapping(raw_dict)
    assert type(data) == AnsibleMapping
    assert data['key1'] == 'val1'
    assert data['key2'] == 'val2'
    # Test dict with duplicate key
    data = a_constructor.construct_mapping({'key1': 'val1', 'key1': 'val2'})
    assert type(data) == AnsibleMapping
    assert data['key1'] == 'val2'
    # Test dict with non-string key

# Generated at 2022-06-13 07:33:35.494793
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    doc_str = """
- !seq [
    - !seq [
        - 1
        - 2
        - 3
    ]
    - !seq [
        - 4
        - 5
        - 6
    ]
    - !seq [
        - 7
        - 8
        - 9
    ]
]
    """
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.unsafe_proxy import wrap_var
    import pprint
    data = yaml.load(doc_str, Loader=AnsibleLoader)
    assert isinstance(data, AnsibleSequence)

# Generated at 2022-06-13 07:33:35.963324
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:33:38.296337
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    c = AnsibleConstructor()
    data = u'test'
    node = AnsibleConstructor.construct_yaml_str(c, data)
    assert type(node) == AnsibleUnicode
    assert node[:] == data


# Generated at 2022-06-13 07:33:41.138067
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    a = AnsibleConstructor()
    node = {'tag:yaml.org,2002:seq': [1, 2, 3, 4]}

    ansible_seq = a.construct_yaml_seq(node)
    for i in ansible_seq:
        for j in i:
            assert isinstance(j, int)

# Generated at 2022-06-13 07:33:45.395466
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    yaml_input = '''
- one
- two
- three
'''
    obj = yaml.load(yaml_input, AnsibleConstructor)
    print(obj)
    pass

if __name__ == "__main__":
    test_AnsibleConstructor_construct_yaml_seq()

# Generated at 2022-06-13 07:33:54.049119
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """
    Tests for AnsibleConstructor class method construct_mapping
    """
    from ansible import errors
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleMapping
    import yaml
    from yaml.nodes import ScalarNode, MappingNode, SequenceNode

# Generated at 2022-06-13 07:34:02.090950
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    # Setup
    loader = DataLoader()
    vault_password_str = 'vault_secret_password'
    vault_password = to_bytes(vault_password_str)
    vault = VaultLib(vault_password)
    encrypted_string = base64.b64encode(vault.encrypt(to_bytes('value')))
    node = AnsibleVaultEncryptedUnicode(encrypted_string)

    # Without a vault password
    ansible_constructor = AnsibleConstructor(loader=loader, file_name=None)

# Generated at 2022-06-13 07:34:15.403519
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

    vault_string = VaultLib.encrypt('secret',secrets=['secret'])
    vault_string = "%s\n" % vault_string
    class FakeAnsibleConstructor(AnsibleConstructor):
        def construct_scalar(self, node):
            return "%s\n" % vault_string

    # test when vault class is not initialized
    fail_msg = "found !vault but no vault password provided"
    fake_node = type('Node', (object,), {'start_mark': None})()
    constructor = FakeAnsibleConstructor(vault_secrets=None)
    try:
        constructor.construct_vault_encrypted_unicode(fake_node)
    except ConstructorError as e:
        assert fail_msg in str

# Generated at 2022-06-13 07:34:21.695615
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    #construct node for dict with duplicate keys
    node = MappingNode('tag:yaml.org,2002:map', [(u'k1', u'v1'), (u'k1', u'v2')],
                       start_mark=None, end_mark=None, flow_style=False)

    # construct dict with duplicate keys
    ansible_constructor = AnsibleConstructor()
    try:
        ansible_constructor.construct_mapping(node)
        assert False
    except ConstructorError:
        assert True

# Generated at 2022-06-13 07:34:38.378027
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    #check input type
    ac = AnsibleConstructor
    test_string = """
---
data:
  - { this:
      what: is
      can: be
      list:
        - keys:
            - entries:
            - or:
            - lists:
              - whatever
            - right:
              - the: order
              - doesnt: matter
              - its: a dict
              - why: would it
    }
  - { this:
      is:
      another:
      key: value
    }
    """

    from yaml import load
    from ansible.parsing.yaml.objects import AnsibleMapping
    yaml_data = load(test_string)
    assert isinstance(yaml_data, AnsibleMapping)

# Generated at 2022-06-13 07:34:48.382793
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import re
    import types

    def get_ref(obj, name):
        if hasattr(obj, name):
            return getattr(obj, name)
        return None

    def get_func_defaults(obj):
        sub_obj = get_ref(obj, 'func_defaults')
        if sub_obj:
            return sub_obj
        sub_obj = get_ref(obj, '__defaults__')
        if sub_obj:
            return sub_obj
        return None

    def test_func(func, expected_globals, expected_defaults):
        assert type(func) in (types.FunctionType, types.MethodType)
        assert func.__name__ == 'test_func'
        assert func.__module__ == '__main__'

# Generated at 2022-06-13 07:34:54.515487
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()
    s = "test"
    node = ac.construct_yaml_str(s)
    assert(isinstance(node, AnsibleUnicode))
    assert(s == node)
    assert(s == node.ansible_value)
    assert(isinstance(node.ansible_pos, tuple))
    assert(isinstance(node.ansible_pos[0], str))

# Generated at 2022-06-13 07:34:59.849004
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    node = AnsibleVaultEncryptedUnicode(b'foo')
    vault = VaultLib(secrets=['ansible'])
    constructor = AnsibleConstructor(vault_secrets=['ansible'])
    value = constructor.construct_vault_encrypted_unicode(node)
    assert node.decrypt(vault) == value.decrypt(vault)



# Generated at 2022-06-13 07:35:10.881885
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml import load
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils import context_objects as co

    file_name = 'foobar'
    vault_secrets = ['secret']
    vault_secrets_str = ",".join(vault_secrets)
    content = """
    ---
    some_map:
      - key1: value1
      - key2: value2
      - key3: value3
    """


# Generated at 2022-06-13 07:35:15.331738
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_str = "{a: 1}"
    yaml.add_constructor(u'tag:yaml.org,2002:map', AnsibleConstructor.construct_yaml_map)
    data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(data, AnsibleMapping)



# Generated at 2022-06-13 07:35:23.146192
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()

    test_node = type('YAMLNode', (object,), {
        'start_mark': type('YAMLNodeMark', (object,), {
            'line': 1,
            'column': 1,
        }),
        'id': 'str',
    })()

    node_value = 'this is only a test'
    ret = ac.construct_yaml_str(test_node)
    assert ret.ansible_pos == ('<unicode>', 1, 2)

# Generated at 2022-06-13 07:35:31.941688
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()
    import yaml
    # the safe_load method automatically adds the default constructor
    # so we have to remove it here to use our own extended constructor
    del yaml.constructor.SafeConstructor.yaml_constructors[u'tag:yaml.org,2002:str']
    del yaml.constructor.SafeConstructor.yaml_constructors[u'tag:yaml.org,2002:python/unicode']
    del yaml.constructor.SafeConstructor.yaml_constructors[u'tag:yaml.org,2002:map']
    del yaml.constructor.SafeConstructor.yaml_constructors[u'tag:yaml.org,2002:seq']

    # Add our custom constructors

# Generated at 2022-06-13 07:35:39.470021
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import io
    import yaml


# Generated at 2022-06-13 07:35:50.776900
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import StringIO
    from yaml import load

    class AnsibleConstructor_construct_yaml_str(AnsibleConstructor):
        # make the private method public for unit testing
        public_construct_yaml_str = AnsibleConstructor.construct_yaml_str

    bc = AnsibleConstructor_construct_yaml_str()
    yaml_doc = '''\
    str1: 123
    str2: 123.456
    str3: "\"abcdef\""
    str4: '"abcdef"'
    str5: "abcdef"
    '''
    data = load(StringIO(yaml_doc), Loader=AnsibleLoader)
    assert isinstance(data['str1'], AnsibleUnicode)

# Generated at 2022-06-13 07:36:18.218399
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml.nodes import ScalarNode
    from binascii import unhexlify
    

# Generated at 2022-06-13 07:36:25.429899
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Case: Non-empty sequence.
    # Assert: construct_yaml_seq should return a non-empty AnsibleSequence object.
    seq_obj = []
    seq_node = { "value": seq_obj }
    assert len(AnsibleConstructor().construct_yaml_seq(seq_node)) > 0

    # Case: Empty sequence.
    # Assert: construct_yaml_seq should return an empty AnsibleSequence object.
    seq_obj = []
    seq_node = { "value": seq_obj }
    assert len(AnsibleConstructor().construct_yaml_seq(seq_node)) == 0


# Generated at 2022-06-13 07:36:29.884356
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constr = AnsibleConstructor()
    node = MappingNode(u'tag:yaml.org,2002:map', [], [], None, None, None)
    value = constr.construct_yaml_map(node)
    assert isinstance(value, AnsibleMapping)


# Generated at 2022-06-13 07:36:37.701844
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from yaml.nodes import ScalarNode
    from yaml.nodes import MappingNode
    from yaml.constructor import SafeConstructor
    ac = AnsibleConstructor()
    mapping = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
    }
    value_array = []
    for key in mapping:
        value_array.append((ScalarNode(key=None, value=key), ScalarNode(key=None, value=mapping[key])))
    node = MappingNode(tag=None, value=value_array, start_mark=None)
    result = ac.construct_mapping(node)
    expected_result = mapping
    assert result == expected_result

# Generated at 2022-06-13 07:36:48.140446
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys
    if sys.version_info[0] > 2:
        from io import StringIO
    else:
        from StringIO import StringIO
    seq_yaml = """\
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
    """
    seq_yaml_file = StringIO(seq_yaml)
    constructor = AnsibleConstructor()
    constructor._ansible_file_name = '/some/file.yaml'
    for data in constructor.construct_yaml_seq(seq_yaml_file):
        assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert data.ansible_pos == (constructor._ansible_file_name, 1, 1)

# Generated at 2022-06-13 07:36:54.197849
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    ##
    # test construct_yaml_unsafe()
    # through load() with a custom Constructor
    ##
    import sys
    if sys.version_info < (2, 7):
        # no assertRaisesRegexp in 2.6
        import re
        import unittest2 as unittest
    else:
        import unittest
        assertRaisesRegexp = unittest.TestCase.assertRaisesRegexp
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping


    class ConstructorTest(unittest.TestCase):
        def setUp(self):
            self.yaml = AnsibleLoader(stream=None, file_name=None, vault_secrets=None)


# Generated at 2022-06-13 07:37:08.997634
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    class TestAnsibleConstructor(AnsibleConstructor):
        def __init__(self, *args, **kwargs):
            self.data = []
            super(TestAnsibleConstructor, self).__init__(*args, **kwargs)

        def construct_yaml_seq(self, node):
            data = AnsibleSequence()
            yield data
            data.extend(self.construct_sequence(node))
            self.data.append(data)

    c = TestAnsibleConstructor()
    seq1 = c.get_single_data("""
    - 1
    - 2
    """)

    assert seq1 == [1, 2]

    # There should be only one element in c.data, which should be [1, 2]
    assert len(c) == 1

# Generated at 2022-06-13 07:37:14.640284
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    with open('test_constructor.yml') as f:
        data = AnsibleConstructor(file_name='test_constructor.yml').get_single_data(stream=f)

    assert (data == {
        u'one': u'hello',
        u'two': {
            u'k1': u'v1',
            u'k2': u'v2'
        }
    })

# Generated at 2022-06-13 07:37:21.120213
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # following dict should be read as it is
    input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # read the yaml file with yaml parser
    yaml_result = AnsibleConstructor.construct_yaml_map(input_dict)
    # read the yaml file with AnsibleConstructor
    ansible_result = AnsibleConstructor.construct_mapping(yaml_result[0])
    # check the result
    assert ansible_result == input_dict

    # following dict should be not read completely, because of duplicate key 'c'
    input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'c': 5}
    # read the yaml file with AnsibleConstructor
    ansible_result = AnsibleConstruct

# Generated at 2022-06-13 07:37:24.412416
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    data = AnsibleConstructor.construct_yaml_seq(None)
    assert isinstance(data, AnsibleSequence)



# Generated at 2022-06-13 07:38:03.427754
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys
    import yaml
    from ansible_collections.dev.tombuildsstuff.test_module import ansible_module

    class FakeNode(object):
        def __init__(self, value, id):
            self.value = value
            self.id = id

    class FakeConstructor(SafeConstructor):
        def construct_yaml_map(self, node):
            value = AnsibleMapping()
            yield value
            value.update(self.construct_mapping(node))

        def construct_yaml_seq(self, node):
            data = AnsibleSequence()
            yield data
            data.extend(self.construct_sequence(node))

    class FakeLoader(yaml.SafeLoader):
        pass

