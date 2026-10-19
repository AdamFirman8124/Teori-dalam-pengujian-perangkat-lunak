

# Generated at 2022-06-13 07:28:12.524907
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    expected_result = ['normal list element']
    observed_result = None

    yaml.add_representer(unicode, lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:str', value))

    yaml_str = """
    - !unsafe "normal list element"
    """

    observed_result = yaml.load(yaml_str, Loader=yaml.Loader)

    assert(observed_result == expected_result)
    assert(observed_result[0] == expected_result[0])
    assert(isinstance(observed_result[0], AnsibleUnsafeText))



# Generated at 2022-06-13 07:28:24.189071
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml
    yaml_str = '''
a: 1
b: 2
c:
  - 9
  - 10
d:
  - a: 1
    b: 2
    c: 3
  - d: 4
    e: 5
'''
    data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert data['a'] == 1
    assert data['b'] == 2
    assert data['c'][0] == 9
    assert data['c'][1] == 10
    assert data['d'][0]['a'] == 1
    assert data['d'][0]['b'] == 2
    assert data['d'][0]['c'] == 3

# Generated at 2022-06-13 07:28:32.428908
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Set up test data
    data_good_key = {'one': 1, 'two': 2, 'three': 3}
    data_bad_key = {1: 1, 2: 2, 3: 3}

    # Set up the AnsibleConstructor
    con = AnsibleConstructor()

    # Test for a good, hashable key
    constructed = con.construct_mapping(None, deep=True)
    constructed.update(data_good_key)
    assert constructed == data_good_key

    # Test for a bad key
    try:
        constructed = con.construct_mapping(None, deep=True)
        constructed.update(data_bad_key)
        assert True, 'Expected exception'
    except TypeError:
        pass

# Generated at 2022-06-13 07:28:40.864412
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor

# Generated at 2022-06-13 07:28:47.608268
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    data = dict(a=1, b=2)

    yaml = AnsibleDumper().dump(data, Dumper=AnsibleDumper)
    new_data = yaml.load(yaml.dump(data, Dumper=AnsibleDumper))

    assert new_data == data

# Generated at 2022-06-13 07:28:48.874353
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass


# Generated at 2022-06-13 07:28:56.771106
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.vault import VaultLib
    vault_string = VaultLib(secrets=['test']).encrypt("test_string")
    data = yaml.load(vault_string, Loader=AnsibleConstructor)
    assert data == 'test_string'

AnsibleConstructor.add_constructor(
    u'tag:yaml.org,2002:python/str',
    AnsibleConstructor.construct_yaml_str)

AnsibleConstructor.add_constructor(
    u'tag:yaml.org,2002:python/name:ansible.builtin.vars',
    AnsibleConstructor.construct_yaml_str)

# Generated at 2022-06-13 07:29:05.431590
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    testmen = AnsibleConstructor()
    root_node = MappingNode(None, None, True, False)
    root_node.update([
        (StrNode('a'), StrNode('b')),
        (StrNode('c'), StrNode('d'))
    ])
    mapping = testmen.construct_yaml_map(root_node)
    assert isinstance(mapping, AnsibleMapping)
    assert isinstance(mapping, dict)



# Generated at 2022-06-13 07:29:17.223305
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.unsafe_proxy import wrap_var
    from yaml.nodes import ScalarNode

    loader = DataLoader()

    data_str = '''
        a: !unsafe b
        c: !unsafe [1, 2, 3]
        d: !unsafe
            e: 1
            f: 2
    '''
    data = loader.load(data_str)
    assert data == dict(a=wrap_var('b'), c=wrap_var([1, 2, 3]), d=wrap_var(dict(e=1, f=2)))



# Generated at 2022-06-13 07:29:23.763603
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    """
    Test AnsibleConstructor.construct_yaml_unsafe
    """
    class Data:
        pass

    data = Data()
    data.value = set([1, 2, 3])

    constructor = AnsibleConstructor()

    ansible_unsafe = constructor.construct_yaml_unsafe(data)

    assert isinstance(ansible_unsafe, AnsibleUnsafeText)

    ansible_unsafe.value.add(4)

    assert set([1, 2, 3, 4]) == data.value



# Generated at 2022-06-13 07:29:43.057371
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    class MockVault(object):
        def __init__(self):
            self.secrets = None
            self.password = 'secret'
            self.secrets = [self.password]

    vault = MockVault()


# Generated at 2022-06-13 07:29:50.872403
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import os
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var

    cwd = os.path.dirname(__file__)

    vault_secrets = ['ansible']

    data = {
        'foo': 'bar',
        'vault_str': VaultLib(secrets=vault_secrets).encrypt('secret'),
        'nested': {
            'vault_nested': VaultLib(secrets=vault_secrets).encrypt('secret'),
        }
    }

    fd = open(os.path.join(cwd, 'vault-unittest.yml'), 'rb')

# Generated at 2022-06-13 07:29:53.418365
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    mapping = AnsibleConstructor.construct_mapping(MappingNode(None, None, True, FlowStyle.FLOW))
    assert isinstance(mapping, AnsibleMapping)
    assert len(mapping) == 0



# Generated at 2022-06-13 07:30:04.711803
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """We test that AnsibleConstructor.construct_yaml_map stores the line number in the constructed object.

    For example,

        - hosts: all
          tasks:
            - debug:
                msg: hello world
    """
    import yaml
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    results = yaml.load("""
    - hosts: all
      tasks:
        - debug:
            msg: hello world
    """, Loader=AnsibleConstructor)
    play = results[0]
    variable

# Generated at 2022-06-13 07:30:05.656480
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass


# Generated at 2022-06-13 07:30:14.670489
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:30:22.928153
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    doc = """
        - foo: bar
          bam: 123
    """

    obj = list(yaml.load_all(doc))[0]
    assert isinstance(obj, AnsibleSequence)
    assert obj[0]['foo'] == 'bar'
    assert obj[0]['bam'] == 123
    assert obj.ansible_pos[0] == '<unicode string>'
    assert obj.ansible_pos[1] == 2
    assert obj.ansible_pos[2] == 3
    assert obj.ansible_line == 2
    assert obj.ansible_column == 3


# Generated at 2022-06-13 07:30:26.761953
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Dummy string for testing
    node = "!unsafe 'I am not a function'\n"
    # Expected result:
    expected = wrap_var("I am not a function")
    ac = AnsibleConstructor(file_name=None)
    actual = ac.construct_yaml_unsafe(node)

    assert expected == actual

# Generated at 2022-06-13 07:30:37.670560
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys

    class MyAnsibleConstructor(AnsibleConstructor):

        def __init__(self, file_name=None, vault_secrets=None):
            super(MyAnsibleConstructor, self).__init__(file_name, vault_secrets)

        def construct_mapping(self, node, deep=False):
            return super(AnsibleConstructor, self).construct_mapping(node, deep)

    yaml_str = '''
foo:
  - 1
  - 2
bar: test
'''


# Generated at 2022-06-13 07:30:48.657770
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    d = '''
- ['a', 'b', 'c']
- [ 1 , 2 , 3 ]
- [1, 1, 2, 3, 5, 8, 13]
'''
    # Test ansible.parsing.yaml.objects.AnsibleSequence()
    data = yaml.load(d, Loader=AnsibleConstructor)
    assert len(data) == 3
    assert data[0][0] == 'a'
    assert data[0][1] == 'b'
    assert data[0][2] == 'c'

    assert data[1][0] == 1
    assert data[1][1] == 2
    assert data[1][2] == 3

    assert data[2][0] == 1
    assert data[2][1] == 1
    assert data

# Generated at 2022-06-13 07:31:05.851735
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    data = {'test': {'key1': 'string', 'key2': 42, 'key3': [0, 1, 2]}}
    try:
        from yaml import load, YAMLError
        from yaml.representer import SafeRepresenter
    except ImportError:
        print(
            'Error importing yaml module, please install pyyaml package to use this module')

    class Representer(SafeRepresenter):
        def represent_str(self, data):
            return self.represent_scalar('tag:yaml.org,2002:str', data)

    yaml = YAMLError()
    for key in data:
        for subkey in data[key]:
            representer = Representer()
            representer.add_representer(str, representer.represent_str)

# Generated at 2022-06-13 07:31:14.759913
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Provide a set of data to serve as the input
    yaml_input = u'g1: 1\ng2: 2\n'
    # Create a constructor object
    constructor = AnsibleConstructor()
    # Declare a dictionary to use to store the parsed results
    parsed_results = {}
    # Call the constructor to parse the data
    for key, value in constructor.construct_mapping(yaml_input):
        parsed_results[key] = value
    # Test that the results are as expected
    assert parsed_results == {'g1': 1, 'g2': 2}

# Generated at 2022-06-13 07:31:19.523944
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    import yaml

    ac = AnsibleConstructor()
    assert ac.construct_yaml_unsafe(yaml.nodes.ScalarNode(value='!nt', tag='!unsafe')) == AnsibleUnsafeText('!nt')

# Generated at 2022-06-13 07:31:24.037845
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ansible_constructor = AnsibleConstructor()
    dummy_str = "dummy"
    dummy_node = object()
    setattr(dummy_node, 'start_mark', object())
    setattr(dummy_node.start_mark, 'column', 1)
    setattr(dummy_node.start_mark, 'line', 1)
    setattr(dummy_node.start_mark, 'name', None)
    # invoke test method
    ansible_constructor.construct_yaml_str(dummy_node)
    assert dummy_str == u"dummy"

# Generated at 2022-06-13 07:31:31.207150
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    class MySafeConstructor(AnsibleConstructor):
        def construct_yaml_map(self, node):
            ret = AnsibleConstructor.construct_yaml_map(self, node)
            return next(ret)
    constructor = MySafeConstructor()
    ret = constructor.construct_yaml_map(constructor.construct_yaml_str(u'tag:yaml.org,2002:str'))
    assert isinstance(ret, AnsibleMapping)
    assert ret.ansible_pos is None


# Generated at 2022-06-13 07:31:37.783323
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Note: the first "line" is the file name
    node = MappingNode(None, [])
    node.start_mark = object()
    node.start_mark.name = "foobar"
    node.start_mark.column = 0
    node.start_mark.line = 0
    ansible = AnsibleConstructor('somefile')
    for data in ansible.construct_yaml_seq(node):
        assert data is not None
        data.extend(3)
        assert data[0] == 3
        assert data.ansible_pos == ('somefile', 1, 1)

# Generated at 2022-06-13 07:31:43.483040
# Unit test for method construct_yaml_map of class AnsibleConstructor

# Generated at 2022-06-13 07:31:51.873024
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import unittest
    import re
    import textwrap

    class Object(object):
        def __init__(self):
            self.foo = 1

    class ObjectLoader(AnsibleConstructor):
        def construct_object(self, node):
            return Object()

    class UnitTestAnsibleConstructor(unittest.TestCase):
        def test_construct_yaml_unsafe(self):
            yaml = AnsibleUnicode(textwrap.dedent(
                """\
                !unsafe |
                #!/bin/sh
                echo 'hello world'
                """))
            obj = ObjectLoader().get_single_data(yaml)
            self.assertTrue(hasattr(obj, 'foo'))
            self.assertTrue(obj.foo, 1)


# Generated at 2022-06-13 07:32:02.061378
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml.nodes import ScalarNode
    from yaml.events import ScalarEvent
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    vault_passwords = ['password']
    vault_secrets = ['password']
    vault_ids = ['default']
    vault_lib = VaultLib(vault_secrets)
    vault_id = 'default'

    # test the constructor
    data = '$ANSIBLE_VAULT;1.1;AES256'
    node = ScalarNode(u'tag:yaml.org,2002:python/unicode', data,
        (1,0,0), (1,59,0), "")

# Generated at 2022-06-13 07:32:02.432811
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    assert True

# Generated at 2022-06-13 07:32:30.525901
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    data = AnsibleMapping()
    data_in = {'a': 1, 'b': 2, 'c': 3}

    line = 1
    name = 'test_AnsibleConstructor_construct_yaml_map'
    column = 1

    for value in data:
        assert value == data_in

    for value in data_in:
        assert value in data

    for key in data_in:
        assert data_in[key] == data[key]

    datasource, line_out, column_out = data.ansible_pos
    assert line_out == line
    assert name == datasource
    assert column_out == column

    line2 = 3
    column2 = 10
    data.ansible_pos = name, line2, column2

    datasource, line_out, column_out = data.ans

# Generated at 2022-06-13 07:32:34.927699
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_str = """
foo: bar
baz:
    - one
    - two
    - three
"""

    data = AnsibleLoader(yaml_str, file_name='test').get_single_data()
    assert data['foo'] == 'bar'
    assert data['baz'] == ['one', 'two', 'three']



# Generated at 2022-06-13 07:32:46.510208
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # We construct a node of type unsafe
    node = dict()
    node["id"] = 'unsafe'
    # We construct a mock object of class AnsibleConstructor
    cons = AnsibleConstructor()
    # We verify the result of the call of the method construct_yaml_unsafe with class AnsibleConstructor as input
    assert AnsibleConstructor.construct_yaml_unsafe(cons, node)
    # We verify the result of the call of the method construct_yaml_unsafe with class AnsibleConstructor as input
    assert not AnsibleConstructor.construct_yaml_unsafe(cons, node)
    # We construct an object of type dict
    first_node = dict()
    # We construct an object of type dict
    second_node = dict()
    # We construct an object of type dict
    third_node = dict

# Generated at 2022-06-13 07:32:55.781169
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import os
    import sys
    import unittest

    # Save references to builtins
    builtin_str = str
    builtin_unicode = str

    # Create functions to return encoded or decoded str or unicode
    # based on whether the PY2 or PY3 bool is True or False
    def str(obj, *args, **kwargs):
        if PY2:
            return builtin_str(obj, *args, **kwargs)
        else:
            return builtin_unicode(obj, *args, **kwargs)

    def unicode(obj, *args, **kwargs):
        if PY2:
            return builtin_unicode(obj, *args, **kwargs)
        else:
            return builtin_str(obj, *args, **kwargs)


# Generated at 2022-06-13 07:32:59.470137
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    obj = yaml.load(
        u'--- !unsafe\n'
        u'"foo"\n'
        u'', Loader=AnsibleConstructor
    )
    assert obj == u'foo'
    assert isinstance(obj, AnsibleUnicode)
    assert isinstance(obj, str)



# Generated at 2022-06-13 07:33:08.826632
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:33:23.201265
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml.nodes import SequenceNode
    from yaml.parser import ParserError
    from ansible.parsing.yaml.objects import AnsibleSequence

    yaml_str = '''
- A
- B
- C
'''
    node = AnsibleConstructor().compose_document(AnsibleConstructor().compose_node(yaml_str,
                                                                                   Loader=AnsibleConstructor.yaml_loader))
    assert isinstance(node, SequenceNode)
    assert isinstance(AnsibleConstructor().construct_yaml_seq(node), AnsibleSequence)

    with pytest.raises(ConstructorError):
        AnsibleConstructor().construct_yaml_seq(AnsibleConstructor().construct_yaml_map(node))

# Generated at 2022-06-13 07:33:33.076172
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import vault_loader
    from ansible.plugins.cache import vault_cache
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vars.resolver import resolve_unsafe_strings
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.vars.manager import Loader
    import yaml


# Generated at 2022-06-13 07:33:38.960675
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    "AnsibleConstructor_construct_yaml_map"

    yaml_dict = '''
---
key1: value
key2: value2
...
'''
    yaml_dict_loader = yaml.loader.BaseLoader(yaml_dict)
    yaml_doc = yaml_dict_loader.get_single_node()
    func = getattr(AnsibleConstructor, 'construct_yaml_map')
    data = func(AnsibleConstructor, yaml_doc)

    assert len(data) == 2
    assert 'key1' in data
    assert 'key2' in data



# Generated at 2022-06-13 07:33:49.263924
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

        # Check for empty case
        data = '''{}'''
        y = yaml.load(data, Loader=AnsibleConstructor)
        assert type(y[0]) is AnsibleMapping
        assert y[0].ansible_pos == ('<string>', 1, 1)
        assert y[0]['a'] == 1

        # Check for simple case
        data = '''{'a':1, 'b':2}'''
        y = yaml.load(data, Loader=AnsibleConstructor)
        assert type(y[0]) is AnsibleMapping
        assert y[0].ansible_pos == ('<string>', 1, 1)
        assert y[0]['a'] == 1
        assert y[0]['b'] == 2

        # Check for complex case

# Generated at 2022-06-13 07:34:32.554543
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    va = VaultLib(secrets=['test'])
    va.update({'test': 'encrypted word'})
    test = AnsibleConstructor()
    test._vaults['default'] = va
    node = u'!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n316139316360653163363935666164346431626363393232356337626565326336613061323133393\n 6230373835313961306662616639636363323666316536346463633663663534643965666630616663\n613337353037653139643338316365633337\n'
    result = test.construct_vault_encrypted_unicode(node)
    assert result == 'encrypted word'

# Generated at 2022-06-13 07:34:39.986130
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    string_to_encrypt = "This is my secret string"
    ansible_constructor_object = AnsibleConstructor()
    ansible_constructor_object.vault_secrets.append('secret')
    result = ansible_constructor_object.construct_vault_encrypted_unicode(yaml.nodes.ScalarNode(tag=u'!vault', value=string_to_encrypt))
    assert result.decrypt() == string_to_encrypt
    x = AnsibleVaultEncryptedUnicode.new_encrypted(string_to_encrypt, 'secret')
    result = ansible_constructor_object.construct_vault_encrypted_unicode(yaml.nodes.ScalarNode(tag=u'!vault-encrypted', value=str(x)))
   

# Generated at 2022-06-13 07:34:48.525366
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml.add_constructor(u'tag:yaml.org,2002:map',
                         AnsibleConstructor.construct_yaml_map)
    yaml.add_constructor(u'tag:yaml.org,2002:python/dict',
                         AnsibleConstructor.construct_yaml_map)
    obj = yaml.load('''
mydict:
  key: value
  key2: value2
''')
    assert isinstance(obj, dict)
    assert isinstance(obj['mydict'], AnsibleMapping)
    assert obj['mydict']['key'] == 'value'
    assert obj['mydict']['key2'] == 'value2'



# Generated at 2022-06-13 07:34:49.774129
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:34:58.759896
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Create an instance of class AnsibleConstructor
    ans_constructor = AnsibleConstructor()
    # Create a node with an impossible start_mark and add an id to represent the value '!vault'.
    node = MappingNode({}, start_mark='impossible_start_mark')
    node.id = 'vault'
    # Create a Mapping Node with a certain scalar value and then pass it to the constructed_scalar method.
    data = MappingNode({'GA': '7f6gahj', 'GB': '0bicl3f'}, start_mark='value_mark')
    data_value = AnsibleConstructor.construct_scalar(ans_constructor, data)
    # Pass the data value to the construct_vault_encrypted_unicode method and get the instance of class AnsibleVaultEncrypted

# Generated at 2022-06-13 07:35:09.881457
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import yaml
    import sys

    # Create an AnsibleConstructor
    _constructor = AnsibleConstructor()

    # Create a map that will be converted to a AnsibleMapping
    dict_obj = {'a': 'b'}

    # Create a AnsibleMapping and serialize it back to a map
    ansible_dict = AnsibleMapping(dict_obj)

    # Validate the test case

# Generated at 2022-06-13 07:35:17.584789
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Create secret to encrypt and decrypt
    secret = AnsibleUnicode('my secret')
    # Init AnsibleConstructor
    ansible_constructor = AnsibleConstructor()
    # Create node to pass to method construct_vault_encrypted_unicode
    node = None

    # Encrypt secret using method construct_vault_encrypted_unicode
    node = ansible_constructor.construct_vault_encrypted_unicode(node)
    # Decrypt secret using method construct_vault_encrypted_unicode
    vault_encrypted_unicode = ansible_constructor.construct_vault_encrypted_unicode(node)

    # Check if secret is equal to decrypted secret
    assert secret == vault_encrypted_unicode



# Generated at 2022-06-13 07:35:32.334795
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    # test for safe_eval
    ac = AnsibleConstructor()
    
    # test for ast.literal_eval
    mydict = {"key1" : "value1"}
    assert(ac.construct_yaml_unsafe(mydict) == wrap_var(mydict))

    mylist = ["value1", "value2"]
    assert(ac.construct_yaml_unsafe(mylist) == wrap_var(mylist))

    myset = { "value1", "value2"}
    assert(ac.construct_yaml_unsafe(myset) == wrap_var(myset))

    mytuple = ( "value1", "value2")
    assert(ac.construct_yaml_unsafe(mytuple) == wrap_var(mytuple))


# Generated at 2022-06-13 07:35:39.758589
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    '''
    In order to test AnsibleConstructor.construct_yaml_seq()
    we need to load an YAML string and convert it back to
    an YAML string. The test succeeds if the resulting
    string is identical to the original string.
    We use a valid YAML string as the test variable
    and an invalid YAML string as the control variable
    The test succeeds if the resulting string of the
    test variable and the resulting string of the control
    variable are different, as expected.
    '''

    from yaml import load
    from yaml import dump
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_str = '''\
foo:
-   one
-   two'''


# Generated at 2022-06-13 07:35:50.925746
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    yaml_constructor = AnsibleConstructor()
    testcase_yaml = """---
- item1
- item2
- item3
"""
    testcase_python = ['item1', 'item2', 'item3']

    testcase_result = yaml.load(testcase_yaml, Loader=yaml.Loader)
    assert(testcase_result == testcase_python)
    print("Passed test 1")

    testcase_result = yaml.safe_load(testcase_yaml)
    assert(testcase_result == testcase_python)
    print("Passed test 2")

    testcase_result = yaml.load(testcase_yaml, Loader=AnsibleConstructor)
    assert(testcase_result == testcase_python)

# Generated at 2022-06-13 07:37:25.013356
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    constructor = AnsibleConstructor()
    node = object()
    value = object()
    constructor.construct_object = lambda node: value
    result = constructor.construct_yaml_unsafe(node)
    assert result == wrap_var(value)

# Generated at 2022-06-13 07:37:35.529841
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import io
    import sys

    if sys.version_info > (3,):
        string_types = str,
    else:
        string_types = basestring,  # noqa

    def construct_vault_encrypted_unicode(ciphertext, method='sha256', vault_id=None):
        '''Construct a AnsibleVaultEncryptedUnicode object by passing in
        ciphertext data and using the default vault (VaultLib), and the
        default vault password. Similar to how an encrypted value is
        constructed in AnsibleConstructor.'''
        ciphertext = to_bytes(ciphertext)
        vault = AnsibleConstructor._vaults['default']

# Generated at 2022-06-13 07:37:35.934176
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    AnsibleConstructor()

# Generated at 2022-06-13 07:37:42.408583
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    import json

    with open("test/unit/parsing/fixtures/test_vault_encrypted_data.yml", 'r') as stream:
        try:
            data_map = yaml.load(stream, Loader=AnsibleConstructor)
            assert data_map['encrypted_text'] == "decrypted text"
            assert data_map['encrypted_text'] == json.loads(json.dumps(data_map))['encrypted_text']
        except yaml.YAMLError as exc:
            print(exc)



# Generated at 2022-06-13 07:37:46.792228
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    y_obj = yaml.load('''
key1:
- foo
key2: bar
''', Loader=AnsibleConstructor)

    print(y_obj)
    print(type(y_obj))
    print(y_obj.ansible_pos)


# Generated at 2022-06-13 07:37:54.452866
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    """
    Test that AnsibleConstructor.construct_yaml_seq() is behaving
    as expected.
    """
    import yaml

    yaml_data = u'[{}, 1, foo]'
    yaml_ansible_data = yaml.load(yaml_data, Loader=AnsibleConstructor)

    # The following is a bit of a hack.  This is not the preferred way to
    # construct an AnsibleSequence object, but it works for testing.
    ansible_data = AnsibleSequence([{}, 1, u'foo'])

    assert isinstance(yaml_ansible_data[0], dict)
    assert isinstance(yaml_ansible_data[1], int)
    assert isinstance(yaml_ansible_data[2], AnsibleUnicode)


# Generated at 2022-06-13 07:38:01.458390
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    import base64
    from ansible.parsing.yaml.objects import AnsibleUnicode

    secret_text = AnsibleUnicode(u'text')
    print("secret_text: ")
    print(secret_text)
    
    vault_passwd = 'b'

    alg = 'AES256'
    vault_secrets = [vault_passwd]
    ac = AnsibleConstructor(vault_secrets=vault_secrets)
    
    vault_encrypted_secret_text = ac.construct_vault_encrypted_unicode(secret_text)
    print("vault_encrypted_secret_text: ")
    print(vault_encrypted_secret_text)
