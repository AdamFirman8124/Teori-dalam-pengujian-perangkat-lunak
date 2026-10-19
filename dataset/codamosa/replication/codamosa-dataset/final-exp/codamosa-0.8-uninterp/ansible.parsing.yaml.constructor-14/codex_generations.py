

# Generated at 2022-06-13 07:28:11.039617
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.utils.unsafe_proxy import wrap_var
    decode_method = AnsibleConstructor.construct_yaml_unsafe
    code_test_values = [
        ("!unsafe '{ \"test\": 42 }'", wrap_var('{ "test": 42 }')),
    ]
    for value, expected in code_test_values:
        assert decode_method(value) == expected

# Generated at 2022-06-13 07:28:22.322510
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from yaml.representer import SafeRepresenter

# Generated at 2022-06-13 07:28:29.358633
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    code = '''
- a:
    - b
- c:
    - d
    - e
    '''
    # use load() instead of load_all() to get a single python object
    # (we don't want to use load_all() since that would return a generator)
    test_object = yaml.load(code, Loader=AnsibleConstructor)

    assert isinstance(test_object, list)
    assert test_object == [{'a': ['b']}, {'c': ['d', 'e']}]

# Generated at 2022-06-13 07:28:36.896599
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # create a test node
    node = MappingNode('tag:yaml.org,2002:map', [], [], [False])
    map_value = {'a': 1, 'b': 1, 'c': 1}
    map_value_pair = [(k, v) for k, v in map_value.items()]

    # add mappings to the node
    # we add each key:value pair as a separate element,
    # and then we add a duplicated key:value pair
    for key, value in map_value_pair:
        key_node = AnsibleConstructor.construct_yaml_str(key)
        value_node = AnsibleConstructor.construct_yaml_str(value)
        node.value.append((key_node, value_node))

    # add last key:value pair twice
    node

# Generated at 2022-06-13 07:28:43.367551
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from io import StringIO
    document = """
    a:
      - 1
      - 2
    """
    s = StringIO(document)
    # create an object of class OrderedDict from the document using
    doc = yaml.load(s, Loader=AnsibleLoader)
    # check if all the keys are loaded as unicode objects
    assert isinstance(doc.keys()[0], str)

# Generated at 2022-06-13 07:28:51.915711
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml.nodes import ScalarNode

    class FakeMark:
        def __init__(self):
            self.line = 1
            self.column = 1
            self.name = ''

    fake_mark = FakeMark()
    node = ScalarNode('tag:yaml.org,2002:str', 'Hello World', fake_mark, fake_mark, "")

    assert AnsibleConstructor().construct_yaml_str(node) == 'Hello World'

# Generated at 2022-06-13 07:28:59.726169
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    #
    # Create a VaultLib object with a correct vault password
    #
    vault_secrets = [ u'secret' ]
    vault = VaultLib(secrets=vault_secrets)
    #
    # Create a AnsibleConstructor instance with the VaultLib object.
    # Use the file name as None
    #
    constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    #
    # Create a AnsibleVaultEncryptedUnicode instance.
    #

# Generated at 2022-06-13 07:29:00.349389
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:29:14.281213
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import re
    import sys
    import unittest
    import warnings

    class AnsibleConstructorTest(unittest.TestCase):

        def test___init__(self):
            self.assertEqual(AnsibleConstructor().vault_secrets, [])
            self.assertEqual(AnsibleConstructor(
                file_name='foobar', vault_secrets=['secret1', 'secret2']).vault_secrets,
                ['secret1', 'secret2'])

        def test_construct_mapping(self):
            a = AnsibleConstructor()
            a.add_constructor(u'!vault', a.construct_vault_encrypted_unicode)
            # expected behavior, normal
            from yaml.nodes import MappingNode
            from yaml.nodes import ScalarNode


# Generated at 2022-06-13 07:29:21.062687
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    test_string = '''name: test_obj
key: a_string
key2: "0"
'''
    ansible_constructor = AnsibleConstructor()
    ret = ansible_constructor.construct_yaml_map(test_string)
    assert ret['name'] == 'test_obj'
    assert ret['key'] == 'a_string'
    assert ret['key2'] == '0'


# Generated at 2022-06-13 07:29:42.835397
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    mapping_nodes = []
    for _ in range (3):
        mapping_node = MappingNode(tag=u'!foo', value=[], flow_style=False)
        mapping_nodes.append(mapping_node)

    # Test: 3 dicts with duplicate keys
    for node in mapping_nodes:
        for key, value in zip(range(3), range(3)):
            key_node = ScalarNode(tag=u'!foo', value=key, style='', start_mark=None, end_mark=None)
            value_node = ScalarNode(tag=u'!foo', value=value, style='', start_mark=None, end_mark=None)
            node.value.append((key_node, value_node))

# Generated at 2022-06-13 07:29:45.545262
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import ansible.parsing.yaml.objects
    if not isinstance(ansible.parsing.yaml.objects.AnsibleSequence, type):
        raise AssertionError

# Generated at 2022-06-13 07:29:47.878171
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Constructing string
    ans_str = AnsibleConstructor()
    node = 'abcd'
    result = ans_str.construct_yaml_str(node)
    assert result == node

# Generated at 2022-06-13 07:29:53.162149
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    type_str = u"str"
    node = type(type_str)
    ac = AnsibleConstructor()
    result = ac.construct_yaml_str(node)
    assert isinstance(result, AnsibleUnicode), "construct_yaml_str should return AnsibleUnicode"
    assert result == type_str, "construct_yaml_str should return the same as type_str"


# Generated at 2022-06-13 07:30:04.377183
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class _AnsibleConstructor(AnsibleConstructor):
        def _node_position_info(self, node):
            return (None, None, None)

    import yaml
    data = yaml.load(u"""
a: b
c: d
e:
- f
- g
h:
  i: j
  k: l
    """, Loader=_AnsibleConstructor)

    # Map the data to a dictionary that is easier to traverse
    data = dict([(k, v) for k, v in data.items()])

    # Verify the keys are as expected
    assert 'a' in data
    assert 'c' in data
    assert 'e' in data
    assert 'h' in data

    # Verify the values are as expected
    assert data['a'] == 'b'
    assert data

# Generated at 2022-06-13 07:30:13.449769
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    # Test for construct_vault_encrypted_unicode() with ciphertext not loaded from file

    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib

    yaml_constructor = AnsibleConstructor()

    vault_secret = VaultSecret("bobo")
    vault_secret.token = b'$ANSIBLE_VAULT;1.1;AES256;test'
    vault_secret.ciphertext = b'asETdz0iGjDvCCzfDys8+X0XkLMMG1QifycZ+oar0Qc='

    vault = VaultLib([vault_secret])

    node = yaml_constructor.construct_yaml_map({u'!vault': vault_secret.ciphertext})

    vault_encrypted

# Generated at 2022-06-13 07:30:21.786719
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml_data = """
    foo: bar
    name: "John Smith"
    age: 22
    """

    ans_constructor = AnsibleConstructor
    data = AnsibleLoader(yaml_data, ans_constructor).get_single_data()

    assert data['foo'] == 'bar'
    assert data['name'] == "John Smith"
    assert data['age'] == 22
    assert type(data['name']) == AnsibleUnicode
    assert type(data['age']) == AnsibleUnicode

# Generated at 2022-06-13 07:30:29.723558
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    yaml_src = """
---
a: [1, 2, 3]
b:
  - 4
  - 5
  - 6
c: {'d': 7, 'e': 8}
d:
  f: 9
  g: 10
"""
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils._text import to_bytes, to_text
    vals = AnsibleLoader(yaml_src, file_name='<string>').get_single_data()
    assert isinstance(vals, dict)
    assert isinstance(vals['a'], list)
    assert isinstance(vals['a'][0], AnsibleUnsafe)
    assert vals['a'][0] == 1
    assert isinstance(vals['b'], list)

# Generated at 2022-06-13 07:30:40.349849
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml

    # Given a yaml map
    yaml_map = yaml.load('''
a: b
c:
  d: e
''', Loader=yaml.Loader)

    # When we call construct_yaml_map
    ansible_constructor = AnsibleConstructor()
    ansible_map = ansible_constructor.construct_yaml_map(yaml_map)

    # Then we get an ansible map
    assert type(yaml_map) == dict
    assert type(ansible_map) == AnsibleMapping

    # And when we convert it back to yaml
    yaml_map2 = yaml.dump(ansible_map, default_flow_style=False, Dumper=yaml.Dumper, width=1000)

    # Then we get the original yaml
   

# Generated at 2022-06-13 07:30:49.925083
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import textwrap
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_code = textwrap.dedent(u"""\
        - foo: bar
          duplicate_key: value
          duplicate_key: "second value for duplicate_key"
          duplicate_key: "third value for duplicate_key"
          duplicate_key: |
            |
            |- value
            |- for duplicate_key
            |
            |- spans
            |- multiple lines
    """)

    result = AnsibleLoader(None, yaml_code).get_single_data()

    assert result[0]['foo'] == "bar"

# Generated at 2022-06-13 07:31:02.773458
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Given
    test_data = b'{"key_1": "value_1"}'
    yaml_object = AnsibleMapping(**dict(key_1='value_1'))
    yaml_object.ansible_pos = (None, None, None)
    test_constructor = AnsibleConstructor()

    # When
    actual = test_constructor.construct_yaml_map(yaml_object, test_data)

    # Then
    assert actual == yaml_object

# Generated at 2022-06-13 07:31:07.113526
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    safe_no_str = AnsibleConstructor().construct_yaml_unsafe(yaml.nodes.MappingNode([], start_mark=None, end_mark=None))
    safe_str = AnsibleConstructor().construct_yaml_unsafe(yaml.nodes.ScalarNode('tag:yaml.org,2002:str', 'test', start_mark=None, end_mark=None))
    assert safe_no_str == {}
    assert safe_str == 'test'


# Generated at 2022-06-13 07:31:09.677535
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    assert AnsibleConstructor.construct_yaml_str(None, None) == None

# Generated at 2022-06-13 07:31:14.661918
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()

    # Initialize a node
    from yaml.nodes import ScalarNode
    node = ScalarNode(None, None, None)

    # Test the method
    result = ac.construct_yaml_str(node)
    assert isinstance(result, AnsibleUnicode) is True


# Generated at 2022-06-13 07:31:22.393742
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # test construct_yaml_map with error
    c = AnsibleConstructor()
    with pytest.raises(ConstructorError):
        list(c.construct_yaml_map(None))

    # test construct_yaml_map with normal value
    node = MappingNode(tag="tag:yaml.org,2002:map", value=[],
                       start_mark=(None, 1, 1), end_mark=(None, 3, 3), flow_style=False)
    ansible_map = c.construct_yaml_map(node)
    assert isinstance(ansible_map, AnsibleMapping)
    assert ansible_map.ansible_pos == (None, 1, 1)

    # test construct_yaml_map with C.DUPLICATE_YAML_DICT_KEY = 'warn'
   

# Generated at 2022-06-13 07:31:30.465611
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode, AnsibleVaultEncryptedUnicode
    import yaml

    valid_yaml = '''
- 1
- 2
- 3
- 4
- 5
'''

    expected_value = AnsibleSequence([1, 2, 3, 4, 5])
    actual_value = AnsibleConstructor().construct_yaml_seq(yaml.nodes.SequenceNode('tag:yaml.org,2002:seq'))
    assert expected_value == actual_value

# Generated at 2022-06-13 07:31:35.878604
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    test_construct_mapping = {'a': 1, 'b': 2, 'c': 3}
    constructor = AnsibleConstructor()
    node = MappingNode(None, test_construct_mapping.items(), flow_style=False)
    # Test to see if the returned mapping is the same as the input mapping
    final_mapping = constructor.construct_yaml_map(node).__next__()
    assert test_construct_mapping == final_mapping

# Generated at 2022-06-13 07:31:39.452129
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Given:
    yaml_str = u'foo'
    ac = AnsibleConstructor()
    # When:
    ret = ac.construct_yaml_str(yaml_str)
    # Then:
    expected_output = AnsibleUnicode(u'foo')
    assert ret.__dict__ == expected_output.__dict__
    assert ret == expected_output

# Generated at 2022-06-13 07:31:49.286360
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    if sys.version_info[0] > 2:
        import io
        StringIO = io.StringIO
    else:
        import StringIO
        StringIO = StringIO.StringIO

    node = '''
        something:
          - a
          - b
    '''
    data = StringIO(node)
    node = yaml.load(data, Loader=AnsibleConstructor)
    assert dict(node).keys() == ['something']
    assert node['something'].ansible_pos == ('<unicode string>', 2, 3)

    node = '''
        something:
          - a
          - b
        something:
          - c
          - d
    '''
    data = StringIO(node)

# Generated at 2022-06-13 07:31:59.446848
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import os
    import tempfile
    import yaml
    import unittest

    class TestAnsibleConstructor(unittest.TestCase):
        def test_construct_mapping(self):
            # Verify type of returned object
            result = AnsibleConstructor().construct_mapping(None)
            self.assertIsInstance(result, AnsibleMapping)

        def test_duplicate_dict_keys(self):
            """
            Verify that value for 'duplicate_dict_keys' settings of
            'ignore', 'warn', and 'error' are handled as expected.
            """
            # set invalid value for duplicate_dict_keys settings
            invalid_settings = [
                'ignore',
                'warn',
                'error',
            ]


# Generated at 2022-06-13 07:32:17.060658
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    data = {'k1': 'v1', 'k2': 'v2', 'k1': 'v3'}
    yaml_str = '---\nk1: v1\nk2: v2\nk1: v3\n'
    # yaml.load doesn't call __setitem__, so we need to use AnsibleLoader
    data2 = AnsibleLoader(yaml_str).get_single_data()
    assert isinstance(data2, AnsibleMapping) and data == data2

# Generated at 2022-06-13 07:32:23.075740
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys,os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
    import yaml
    node = yaml.compose_all(yaml.parse('[test]'))
    d = {}
    d['test'] = {'valu': [1,2,3]}
    result = yaml.constructor.SafeConstructor.construct_yaml_seq(node)
    assert result

# Generated at 2022-06-13 07:32:33.300084
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ansible_constructor = AnsibleConstructor()
    map1 = (MappingNode('tag:yaml.org,2002:map', [],
                        flow_style=True),
            [])

    expected_key = 'foo'
    expected_value = 'bar'

    map1[1].append((MappingNode('tag:yaml.org,2002:str', [],
                                flow_style=True),
                    expected_key))

    map1[1].append((MappingNode('tag:yaml.org,2002:str', [],
                                flow_style=True),
                    expected_value))

    ansible_map = ansible_constructor.construct_mapping(map1[0],
                                                        deep=False)

    assert expected_key in ansible_map
    assert expected_value == ansible_

# Generated at 2022-06-13 07:32:44.289831
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # preparation
    vault = VaultLib(secrets=[b'foo'])
    constructor = AnsibleConstructor(file_name=None)

# Generated at 2022-06-13 07:32:53.933639
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import datetime

    # to_unicode is being tested here, so let's force it to return bytestrings
    # to ensure we don't get a False-positive in the test case.
    # This function should never be called in normal use, because yaml.load()
    # will presumably be called with a TextLoader which will call the
    # construct_unicode() method instead of the construct_yaml_str() method.
    orig_to_unicode = AnsibleConstructor.to_unicode
    # NOTE: We are replacing the global to_unicode method with one that
    # always returns a bytestring.
    AnsibleConstructor.to_unicode = lambda self, x: to_bytes(x, nonstring='passthru', errors='strict')


# Generated at 2022-06-13 07:33:01.579698
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64

    # Create a node object to mock the object passed to construct_vault_encrypted_unicode() from YAML
    class Node:
        pass

    node = Node()
    node.start_mark = Node()
    node.start_mark.column = 1
    node.start_mark.line = 2
    node.start_mark.name = u"test"

    # Create an AnsibleConstrutor object and add a secret to its vault
    import sys
    ac = AnsibleConstructor(vault_secrets=['test'])
    ac._vaults['default'].secrets = ['test']
    ac._vaults['default']._create_unlocked_vault()

    # Encrypt the string 'test'
    ciphertext_bytes = ac._vaults['default'].encrypt(b'test')

# Generated at 2022-06-13 07:33:10.865392
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['test_secret']

# Generated at 2022-06-13 07:33:24.993286
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    node = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          39306534313365316532393839316536633461353861356537383862316239656439616662313731350a\n          343537363732666565376262373137376534323039303766373938663830653365356563353465656235\n          0a'
    vault_secrets = ['secret_password']
    ac = AnsibleConstructor(None, vault_secrets)


# Generated at 2022-06-13 07:33:33.924351
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq(): # pylint: disable=invalid-name
    '''AnsibleConstructor.construct_yaml_seq()'''

    # Testing short Sequence
    node = [1, 2, 3]
    yaml_data = u"---\n- 1\n- 2\n- 3\n---\n"

    yaml_node = yaml.compose(yaml_data)
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_yaml_seq(yaml_node)
    test_seq = next(yaml_node.value)
    assert test_seq == node

    # Testing long Sequence
    node = [x for x in range(200)]

# Generated at 2022-06-13 07:33:37.744096
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    class FakeUnsafeStrConstructor:
        def construct_object(self, node):
            return "fake"

    fake_constructor = FakeUnsafeStrConstructor()
    fake_constructor.construct_yaml_unsafe = AnsibleConstructor.construct_yaml_unsafe

    result = fake_constructor.construct_yaml_unsafe(None)

    assert(result == u"fake")

# Generated at 2022-06-13 07:34:03.230399
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    mio_yaml_test = """
- [ 1, 2, 3 ]
- { one: 1, two: 2 }
"""

    constructor = AnsibleConstructor()
    data = load(mio_yaml_test, constructor)
    expected = [[1, 2, 3], {'one': 1, 'two': 2}]
    assert data == expected

# Generated at 2022-06-13 07:34:09.324901
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    u = AnsibleConstructor.construct_yaml_str(AnsibleConstructor(), 'yaml')
    assert isinstance(u, AnsibleUnicode)
    assert u == u'yaml'
    assert isinstance(u.ansible_pos, tuple)


# Generated at 2022-06-13 07:34:20.313378
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_node = MappingNode('mapping', False, [], None, None)
    ac = AnsibleConstructor()

    # Test Node with an empty list
    assert ac.construct_mapping(test_node) == {}

    # Test Node with a list of one 3-tuple
    test_node.value = [
        (ScalarNode('id', False, 'foo', None, None), ScalarNode('id', False, 'bar', None, None)),
    ]
    assert ac.construct_mapping(test_node) == {'foo': 'bar'}

    # Test Node with a list of 2 three-tuples (same keys)
    test_node.value.append((ScalarNode('id', False, 'foo', None, None), ScalarNode('id', False, 'baz', None, None)))
   

# Generated at 2022-06-13 07:34:22.411381
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ansible_constructor = AnsibleConstructor()
    node = MappingNode(u'tag:yaml.org,2002:map', [], [], None, None)
    ansible_constructor.construct_mapping(node)

# Generated at 2022-06-13 07:34:32.474382
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.vault import VaultLib
    constructor = AnsibleConstructor()
    test_string = ''
    with open("test/unit/parsing/yaml/constructor_input.yml", "r") as f:
        test_string = f.read()
    input_node = yaml.eval(test_string, Loader=yaml.BaseLoader)
    vault = VaultLib('', vault_secrets=['test/unit/parsing/vault/test_vault.key'])
    input_node.value[0].value[1].value = vault.decrypt(yaml.load(input_node.value[0].value[1].value))
    results = constructor.construct_yaml_seq(input_node)
    test_dict = {}

# Generated at 2022-06-13 07:34:36.641891
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    constructor = AnsibleConstructor()
    for directive in ['warn', 'error', 'ignore']:
        C.DUPLICATE_YAML_DICT_KEY = directive
        data = constructor.construct_mapping(load('{a: 1, a: 2}'))
        assert data == {'a': 2}, "Failed to produce correct results for %s" % directive

# Generated at 2022-06-13 07:34:42.268121
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    from io import StringIO

    import sys
    import types

    # Save stdout because we're going to set it to a StringIO
    orig_stdout = sys.stdout

    # Define a fake class and function
    class FakeClass(object):
        def __init__(self):
            pass

    def fake_function():
        pass


# Generated at 2022-06-13 07:34:46.267357
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    node = MappingNode(u'tag:yaml.org,2002:map', [], [], None, None)
    ac = AnsibleConstructor()
    result = ac.construct_yaml_map(node)
    assert AnsibleMapping == type(next(result))


# Generated at 2022-06-13 07:34:47.740517
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    a = AnsibleConstructor()
    assert isinstance(a.construct_mapping(None), dict)

# Generated at 2022-06-13 07:34:57.748473
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class MockNode:
        def __init__(self, identifier, start_mark=None):
            self.id = identifier
            self.value = []
            self.start_mark = start_mark
    class MockPosition:
        def __init__(self, line, column):
            self.line = line
            self.column = column
        def __str__(self):
            return 'line %s column %s' % (self.line, self.column)

    # Set of 3 nodes representing a list of 2 dicts with duplicate key
    # Each dict should be parsed and then merged
    node1 = MockNode('map', MockPosition(0, 0))
    node2 = MockNode('scalar', MockPosition(0, 2))
    node3 = MockNode('scalar', MockPosition(0, 3))
    node4 = Mock

# Generated at 2022-06-13 07:35:41.816824
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test AnsibleConstructor.construct_yaml_str for correctness.

    # Arrange
    # Note: this test assumes knowledge of the code being tested.
    # Specifically that the AnsibleConstructor class contains an attribute
    # named _node_position_info and a method named construct_yaml_str
    # which takes a node as an argument.

    # Create a node where line=1, col=1, name='dummy', and value='value'
    node = make_node(1, 1, 'dummy', 'value')

    # Act
    obj = AnsibleConstructor.construct_yaml_str(node)

    # Assert
    assert isinstance(obj, AnsibleUnicode)
    assert obj == 'value'
    assert obj.ansible_pos == ('dummy', 1, 1)



# Generated at 2022-06-13 07:35:53.211930
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class AnsiCon(AnsibleConstructor):
        def _node_position_info(self, node):
            return (1, 2, 3)

    test_data = ["a: b", "b: c", "a: d"]

    if C.DUPLICATE_YAML_DICT_KEY == 'warn':
        with display.override_verbosity(display.Verbosity.QUIET):
            ansicon = AnsiCon()
            ansicon.construct_yaml_map(yaml.compose_all(test_data))
        assert display._display.deprecated_messages == \
            ['1:2:3: While constructing a mapping from 1, line 2, column 3, found a duplicate dict key (a). Using last defined value only.']

# Generated at 2022-06-13 07:36:04.394723
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from io import StringIO
    from yaml.parser import ParserError
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_str = r'''
    - foo:
        - bar: baz
        - qux: quux
    - foo2:
        - bar2: baz2
        - qux2: quux2
    '''

    # a AnsibleConstructor object
    ac = AnsibleConstructor()
    loader = AnsibleLoader(StringIO(yaml_str), AnsibleConstructor)
    try:
        data = loader.get_single_data()
    except ParserError:
        assert False, "Failed, Please fix the code"

# Generated at 2022-06-13 07:36:16.470309
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import StringIO


# Generated at 2022-06-13 07:36:17.001176
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:36:24.060429
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test with bytes in the input
    input_bytes = b'foo: bar\n'
    constructor = AnsibleConstructor()
    ret = constructor.construct_object(input_bytes, deep=True)
    assert isinstance(ret, AnsibleMapping)
    assert isinstance(ret['foo'], AnsibleUnicode)

    # Test with bytes in the input and unicode_str set to True
    input_bytes = b'foo: bar\n'
    constructor = AnsibleConstructor()
    ret = constructor.construct_object(input_bytes, deep=True)
    assert isinstance(ret, AnsibleMapping)
    assert isinstance(ret['foo'], AnsibleUnicode)

    # Test with a string in the input
    input_string = u'foo: bar\n'
    constructor = AnsibleConstructor

# Generated at 2022-06-13 07:36:32.727238
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    mapdata = """
        over-write-on-duplicate-keys:
            a: b
            a: c
            b: 1
            c: 2
            d: 3
        preserve-on-duplicate-keys:
            a: b
            a: c
            b: 1
            c: 2
            d: 3
        """

    from ansible.parsing.yaml.dumper import AnsibleDumper
    import yaml
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 07:36:34.703122
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # pylint: disable=invalid-name
    assert True



# Generated at 2022-06-13 07:36:48.263129
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:36:54.278203
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import copy
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    data_dupe_key_warn_dict = """
    firstkey: val1
    secondkey: val2
    thirdkey: val3
    firstkey: val_overwritten
    """

    data_dupe_key_error_dict = """
    firstkey: val1
    secondkey: val2
    thirdkey: val3
    firstkey: val_overwritten
    """

    data_dupe_multiline_key_error_dict = """
    firstkey: val1
    secondkey: val2
    thirdkey: val3
    firstkey: val_overwritten
    """

    data_dupe_key_