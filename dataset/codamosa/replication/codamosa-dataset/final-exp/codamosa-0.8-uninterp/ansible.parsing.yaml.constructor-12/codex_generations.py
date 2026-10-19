

# Generated at 2022-06-13 07:28:16.367905
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    import yaml
    from ansible.module_utils._text import to_bytes, to_native

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader, AnsibleConstructor, load_from_text

    # Test the constructor to make sure it works
    # for the different types of input it might get.

    data = u'{ "a":"1", "b":"2" }'
    expected_data = {u'a': u'1', u'b': u'2'}

    loader = AnsibleConstructor(file_name=u'<string>')
    obj = yaml.load(data, Loader=loader)
    assert isinstance(obj, AnsibleMapping)
    assert obj == expected_data

    obj = y

# Generated at 2022-06-13 07:28:27.341199
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault = VaultLib(secrets=['secret'])
    cleartext = u'foo'
    ciphertext = to_bytes(vault.encrypt(cleartext))

    expected = AnsibleVaultEncryptedUnicode(ciphertext)
    expected.vault = vault
    expected.ansible_pos = ('<string>', 1, 7)

    node = yaml.nodes.ScalarNode('tag:yaml.org,2002:str', ciphertext)
    node.start_mark.line = node.end_mark.line = 0
    node.start_mark.column = node.end_mark.column = 6

    actual = AnsibleConstructor(vault_secrets=['secret']).construct_vault_encrypted_unicode(node)

    assert expected.ciphertext == actual.ciphertext


# Generated at 2022-06-13 07:28:30.454098
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    ansible_constructor = AnsibleConstructor()
    ansible_mapping = ansible_constructor.construct_yaml_map(None)
    assert isinstance(ansible_mapping, AnsibleMapping)


# Generated at 2022-06-13 07:28:37.461690
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()
    mapping_node = MappingNode(None, None)
    mapping_node.value = [('key1', 'value1'), ('key2', 'value2')]

    mapping = constructor.construct_yaml_map(mapping_node)
    assert mapping is not None
    for key, value in mapping_node.value:
        assert key in mapping
        assert mapping[key] == value

    # Test duplicate keys
    mapping_node = MappingNode(None, None)
    mapping_node.value = [('key1', 'value1'), ('key1', 'value2')]
    mapping = constructor.construct_yaml_map(mapping_node)
    assert mapping is not None
    assert mapping['key1'] == 'value2'



# Generated at 2022-06-13 07:28:51.129276
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import unittest
    from yaml.nodes import MappingNode
    from yaml.nodes import ScalarNode
    from yaml import nodes
    import ansible.parsing.yaml
    ansible.parsing.yaml.yaml.add_constructor("!unsafe", AnsibleConstructor.construct_yaml_unsafe)


    class TestAnsibleConstructor(unittest.TestCase):

        def setUp(self):
            self.constructor = AnsibleConstructor()

        def test_construct_mapping_not_mapping_node_raises_constructor_error(self):
            node = ScalarNode("tag:yaml.org,2002:str", "test")
            with self.assertRaises(ConstructorError) as error:
                self.constructor.construct_mapping

# Generated at 2022-06-13 07:28:55.567792
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    
    some_list = ['1', '2', '3'] 

    data = AnsibleLoader(some_list).get_single_data()

    assert isinstance(data, AnsibleSequence)
    assert all(isinstance(x, AnsibleUnicode) for x in data)


# Generated at 2022-06-13 07:29:01.851506
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Given: a = 1 and b = {c: 2}
    # When:
    #   - I create a dictionary with dictionary b as its value
    #   - and I create a dictionary with dictionary b as its value
    # Then:
    #   - a dictionary with dictionary b as its value is created
    a = 1
    b = {'c': 2}
    c = AnsibleConstructor.construct_yaml_unsafe(
        {'c': AnsibleConstructor.construct_yaml_unsafe(b)})
    d = AnsibleConstructor.construct_yaml_unsafe({AnsibleConstructor.construct_yaml_unsafe(a): AnsibleConstructor.construct_yaml_unsafe(b)})

    # Expect: b is a value of c
    assert c == {'c': b}
    #

# Generated at 2022-06-13 07:29:11.358722
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    class Args(object):
        _ansible_file_name = 'filename'

    a = AnsibleConstructor(Args)
    yaml_loader = yaml.Loader
    yaml_dumper = yaml.Dumper
    yaml.add_constructor(u'tag:yaml.org,2002:seq', a.construct_yaml_seq, Loader=yaml_loader, Dumper=yaml_dumper)

    # test with an empty list
    data = yaml.load('''
-
''')
    assert data[0]._ansible_file_name == 'filename'
    assert data[0]._ansible_line_number == 2
    assert data[0]._ansible_column_number == 1

    # test with a list with one element

# Generated at 2022-06-13 07:29:19.299108
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping

    class TestConstructor(AnsibleConstructor):
        """
        Mock constructor to control behavior of AnsibleConstructor.construct_mapping method.
        Mocks are used to control the behavior of the flatten_mapping and construct_object
        methods.

        """
        def __init__(self, *args, **kwargs):
            super(TestConstructor, self).__init__(*args, **kwargs)

            # Create dummy MappingNode
            mapping_node = MappingNode(tag=True, value=[], flow_style=False)

            # Create dummy ScalarNode
            scalar_node = None

            # Create dummy mapping node to represent a dictionary
            # within a dictionary and an empty list for the value attribute.
            self.nested_mapping

# Generated at 2022-06-13 07:29:26.559468
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    st = "key1: value1\nkey2: value2\nkey1: value3"
    stream = yaml.parse(st, Loader=yaml.SafeLoader)

    # test duplicate yaml dict keys are not allowed
    # - this should not raise errors and should warn
    ac = AnsibleConstructor()
    ansible_data = ac.construct_yaml_map(stream)
    assert isinstance(ansible_data, AnsibleMapping)
    assert 'key1' in ansible_data and ansible_data['key1'] == 'value3'

    # test that duplicate yaml dict keys are not allowed
    # - this should not raise errors and should ignore
    C.DUPLICATE_YAML_DICT_KEY = 'ignore'
    ac = AnsibleConstructor()
   

# Generated at 2022-06-13 07:29:35.451709
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_vault_encrypted_unicode(MappingNode(u'tag:yaml.org,2002:map', []))

# Generated at 2022-06-13 07:29:44.485447
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import os
    import sys
    from io import open

    from yaml import round_trip_load

    this_dir, this_filename = os.path.split(__file__)
    data_path = os.path.join(this_dir, "../lib/ansible/parsing/yaml/tests/constructor_data.yml")
    data_path = os.path.normpath(data_path)

    with open(data_path, 'r', encoding='utf-8') as f:
        data = f.read()

    if sys.version_info[0] == 3:
        assert isinstance(data, str)

    result = round_trip_load(data, AnsibleConstructor)

    assert result[0] == [1, 2, 3, 4]

# Generated at 2022-06-13 07:29:51.641779
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():

    def test(node, expected_value):
        c = AnsibleConstructor()
        ret = c.construct_yaml_str(node)
        assert isinstance(ret,AnsibleUnicode),"return value not AnsibleUnicode"
        assert ret == expected_value, "return value is not expected value"

    import yaml
    from yaml.nodes import ScalarNode
    test_data = [
        ("foo",u'foo'),
        (u"foo",u'foo'),
        (u"fä",u'fä'),
    ]
    for i, (nodevalue, expected_value) in enumerate(test_data):
        test(ScalarNode(tag='tag:yaml.org,2002:str',value=nodevalue), expected_value)

# Generated at 2022-06-13 07:30:02.520910
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.objects import AnsibleMapping

    t1 = AnsibleConstructor()
    node_t1_simple = t1.construct_scalar(value='ascii')
    assert isinstance(node_t1_simple, AnsibleUnicode)
    assert node_t1_simple == u'ascii'

    node_t1_with_tags = t1.construct_yaml_str(node_t1_simple)
    assert isinstance(node_t1_with_tags, AnsibleUnicode)
    assert node_t1_with_tags == u'ascii'
    assert node_t1_with_tags.ansible_pos[0] is None
    assert node_t1_with_tags.ansible_pos[1] == 0

# Generated at 2022-06-13 07:30:03.083770
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:30:12.197003
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """
    Unit test for method construct_mapping of class AnsibleConstructor
    """
    # Test bad node type
    node = object()
    ac = AnsibleConstructor()
    with pytest.raises(ConstructorError):
        ac.construct_mapping(node)

    # Test empty mapping node
    node = MappingNode(None, None, None)
    output = ac.construct_mapping(node)
    assert output == {}

    # Test node with single key-value pair
    key_node = 'key'
    value_node = 'value'
    node = MappingNode(None, [(key_node, value_node)], None)
    output = ac.construct_mapping(node)
    assert len(output) == 1
    assert list(output.keys())[0] == key_node

# Generated at 2022-06-13 07:30:16.468354
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.vars.unsafe_proxy import wrap_var

    assert AnsibleConstructor.construct_yaml_map({'a':1, 'b':2}) == {'a':1, 'b':2}

    assert AnsibleConstructor.construct_yaml_map({'a':1, 'b':wrap_var(2)}) == {'a':1, 'b':wrap_var(2)}

# Generated at 2022-06-13 07:30:22.429759
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    constructor = AnsibleConstructor()
    str_node = MappingNode(tag=u'tag:yaml.org,2002:str', value=[])
    map_node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[])
    assert isinstance(constructor.construct_mapping(str_node), dict)
    assert isinstance(constructor.construct_mapping(map_node), dict)



# Generated at 2022-06-13 07:30:30.186058
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:30:40.751327
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader

    ansible_constructor = AnsibleConstructor()

    seq_yaml_snippet = "- 1\n- 2\n- 3\n"
    node = (AnsibleLoader(seq_yaml_snippet).get_single_data())
    expected_data = AnsibleSequence([1, 2, 3])

    gen = ansible_constructor.construct_yaml_seq(node)
    data = next(gen)
    assert data == expected_data, 'Expected "{0}", got "{1}"'.format(
        expected_data, data
    )


# Generated at 2022-06-13 07:30:52.509443
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Test construct_yaml_str with node that don't have start_mark and end_mark attributes
    node = {}
    data = AnsibleConstructor().construct_yaml_str(node)
    assert data is None

    # Test construct_yaml_str with node that have start_mark and end_mark attributes
    loader = AnsibleLoader('hello world')
    node = loader.get_single_node()
    data = AnsibleConstructor().construct_yaml_str(node)
    assert isinstance(data, AnsibleUnicode)
    assert data == u'hello world'
    # Check position info
    datasource, line, column = data.ansible_pos
    assert datasource == u'<unicode string>'
    assert line == 1


# Generated at 2022-06-13 07:31:03.141270
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import string_types, binary_type, text_type

    ac = AnsibleConstructor()
    values = [
        binary_type(b'X'),
        text_type(u'Y'),
        123,
        456.7,
        False,
        [1, 2],
        (3, 4),
        {'a': 5, 'b': 6},
        None,
    ]

    for value in values:
        node = type('Node', (object,), {'id': 'object'})()
        # Ensure the value is returned unmodified
        assert ac.construct_yaml_unsafe(node) == value

    # Ensure an immutable type is preserved

# Generated at 2022-06-13 07:31:07.276356
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    import sys
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    class MyConstructor(AnsibleConstructor):
        def construct_vault_encrypted_unicode(self, node):
            value = self.construct_scalar(node)
            b_ciphertext_data = to_bytes(value)
            ret = AnsibleVaultEncryptedUnicode(b_ciphertext_data)
            ret.vault = self._vaults['default']
            ret.ansible_pos = self._node_position_info(node)
            return ret

    yaml_str = '!vault |\n'

# Generated at 2022-06-13 07:31:12.211339
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class MockNode(object):
        def __init__(self, id):
            self.id = id
    safe = AnsibleConstructor()
    deep = True
    node = MockNode('some_node')
    safe.construct_mapping(node,deep)

# Generated at 2022-06-13 07:31:21.090290
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """
    Test that yaml_map method of the AnsibleConstructor returns an AnsibleMap object
    with the ansible_pos attribute correctly set.
    """
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.scanner import Scanner
    from yaml.reader import Reader

    yaml_str = u"test_variable: value"
    parser = Parser(Reader(yaml_str))
    composer = Composer(parser)
    document = composer.get_single_node()

    constructor = AnsibleConstructor()
    ansible_map = constructor.construct_yaml_map(node=document)
    assert isinstance(ansible_map, AnsibleMapping)
    assert ansible_map.ansible_pos == ('<string>', 1, 0)



# Generated at 2022-06-13 07:31:31.697886
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    import ast
    yaml_str = '!unsafe 123'
    construct = AnsibleConstructor()
    data = yaml.load(yaml_str, Loader=yaml.Loader)
    assert isinstance(data, ast.Num)

    yaml_str = '!unsafe "123"'
    construct = AnsibleConstructor()
    data = yaml.load(yaml_str, Loader=yaml.Loader)
    assert isinstance(data, ast.Num)

    yaml_str = '!unsafe \'123\''
    construct = AnsibleConstructor()
    data = yaml.load(yaml_str, Loader=yaml.Loader)
    assert isinstance(data, ast.Num)

    yaml_str = '!unsafe [123]'
    construct = Ansible

# Generated at 2022-06-13 07:31:39.791528
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Testing 'tag:yaml.org,2002:map'
    fname = 'construct_yaml_map.yml'
    s = '''
    key1: val1
    key2: val2
    '''
    data = yaml.load(s, Loader=AnsibleConstructor)
    assert isinstance(data, AnsibleMapping)
    assert len(data) == 2
    assert 'key1' in data
    assert 'key2' in data
    assert data['key1'].ansible_pos == (fname, 1, 0)
    assert data['key2'].ansible_pos == (fname, 2, 0)

    # Testing 'tag:yaml.org,2002:python/dict'
    fname = 'construct_python_dict.yml'

# Generated at 2022-06-13 07:31:49.642929
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    import sys

    if sys.version_info[0] < 3:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins

    # Test the case where construct_mapping works properly
    test_string = "{a: b, c: d}"
    test_mapping = yaml.load(test_string, Loader=AnsibleConstructor)
    assert(isinstance(test_mapping, dict))
    assert(len(test_mapping) == 2)
    assert(test_mapping == {'a': 'b', 'c': 'd'})

    # Test the case where construct_mapping works properly with duplicate keys
    # and the user has set DUPLICATE_YAML_DICT_KEY to 'warn'
    C

# Generated at 2022-06-13 07:32:04.737298
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    ansible_constructor = AnsibleConstructor()
    ansible_loader = AnsibleLoader(constructor=ansible_constructor)

    # Test for correct output for correct input

# Generated at 2022-06-13 07:32:10.858446
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from io import StringIO
    from yaml import dump, load
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    secret = 'test'

# Generated at 2022-06-13 07:32:26.379767
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml_str = '''
- a
- b
- c
'''
    data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert isinstance(data, list)


# Generated at 2022-06-13 07:32:34.961450
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    # test for when secrets is None
    try:
        vault_constructor = AnsibleConstructor(vault_secrets=None)
        loader = AnsibleLoader(None, vault_constructor)
        value = loader.get_single_data()
        value = vault_constructor.construct_vault_encrypted_unicode(value)
    except ConstructorError as e:
        raise AssertionError('no exception should have been raised')

    # test for when secrets is not None
    vault_constructor = AnsibleConstructor(vault_secrets=['first secret', 'second secret'])
    loader = AnsibleLoader(None, vault_constructor)
    value = loader.get_single_data()
    value = vault_constructor.construct_vault

# Generated at 2022-06-13 07:32:46.551461
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import types
    import re
    import six
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    # This is the same test code from test_yaml_constructor of the module
    # python/Lib/yaml/constructor.py

    from yaml import Node, ScalarNode
    from yaml.nodes import MappingNode, SequenceNode
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.resolver import Resolver
    from yaml.scanner import Scanner

    class UnsafeLoader(AnsibleConstructor):
        def construct_python_str(self, node):
            return 'construct_python_str was executed'

# Generated at 2022-06-13 07:32:55.819570
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import StringIO
    import yaml

    s = u"foo:\n  - 1\n  - 2\n  - 3"
    fh = StringIO(s)
    stream = yaml.compose(fh, AnsibleLoader)
    ansible_mapping = AnsibleConstructor.construct_yaml_map(stream)
    assert isinstance(ansible_mapping, AnsibleMapping)
    foo = ansible_mapping.get('foo')
    assert isinstance(foo, AnsibleSequence)
    assert isinstance(foo[0], AnsibleUnicode)

# Generated at 2022-06-13 07:33:02.859886
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    doc = '''
    test:
        name: "{{ test }}"
    '''
    yaml_obj = yaml.load(doc, Loader=AnsibleConstructor)
    # Test that the object was constructed
    assert yaml_obj.__class__ is AnsibleMapping
    assert yaml_obj['test'].__class__ is AnsibleMapping
    assert yaml_obj['test']['name'].__class__ is AnsibleUnicode
    # Check that ansible_pos was added to the object
    assert (yaml_obj.ansible_pos == ('<unicode string>', 1, 1))
    assert (yaml_obj['test'].ansible_pos == ('<unicode string>', 2, 5))

# Generated at 2022-06-13 07:33:11.611706
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = '''
    {
        "foo": 1,
        "bar": 2,
        "foo": 3,
        "baz": 4
    }
    '''
    # ansible_pos is set to line and column position of dictionary
    ansible_pos = (__file__, 1, 1)
    # we need to make sure we have C._DUPLICATE_YAML_DICT_KEY in our environment
    # to make sure we have the correct warning/error
    import os
    import tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.file.write(to_bytes(node))
    temp.file.close()

# Generated at 2022-06-13 07:33:25.247323
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    constructor = AnsibleConstructor()

    def _check_construct_mapping(node, value):
        assert constructor.construct_mapping(node) == value

    # test different key types
    _check_construct_mapping({}, {})
    _check_construct_mapping({'boolean_key': True}, {'boolean_key': True})
    _check_construct_mapping({'key': 'value'}, {u'key': u'value'})
    _check_construct_mapping({1: 'value'}, {1: u'value'})
    _check_construct_mapping({1.1: 'value'}, {1.1: u'value'})

# Generated at 2022-06-13 07:33:34.106536
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    test_data = [
        dict(
            in_str="$ANSIBLE_VAULT;1.2;AES256;testuser\n0000000000",
            out_str="0000000000",
        ),
        dict(
            in_str="$ANSIBLE_VAULT;1.1;AES256;testuser\n0000000000",
            out_str="0000000000",
        ),
        dict(
            in_str="$ANSIBLE_VAULT;1.0;AES256;testuser\n0000000000",
            out_str="0000000000",
        ),
        dict(
            in_str="$ANSIBLE_VAULT;1.2;AES256;testuser\n0000000000",
            out_str="0000000000",
        ),
    ]

    c = AnsibleConstructor()

# Generated at 2022-06-13 07:33:41.239087
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Verify that the value returned is an instance of AnsibleUnicode, not just a regular string.
    ansible_constructor = AnsibleConstructor()
    string_node = ansible_constructor.construct_yaml_str('a_yaml_str_node')
    assert isinstance(string_node, AnsibleUnicode)
    assert string_node == 'a_yaml_str_node'

# Generated at 2022-06-13 07:33:50.300057
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    import copy
    import types
    data_str = '''
- 1
- 2
- 3
'''
    yaml_obj = yaml.load(data_str, AnsibleConstructor)
    assert isinstance(yaml_obj, list)
    assert isinstance(yaml_obj, AnsibleSequence)
    for i in yaml_obj:
        assert isinstance(i, int)
    assert copy.deepcopy(yaml_obj) == yaml_obj
    assert copy.copy(yaml_obj) == yaml_obj
    assert yaml.dump(yaml_obj) == '''- 1
- 2
- 3
'''


# Generated at 2022-06-13 07:34:12.792706
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    yaml = """
    test: "abc"
    """
    data = yaml_load(yaml)
    assert isinstance(data['test'], AnsibleUnicode)
    assert data['test'] == u'abc'


# Generated at 2022-06-13 07:34:13.389425
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:34:22.442500
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

# Generated at 2022-06-13 07:34:32.515085
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    from ansible.parsing.yaml import objects

    # Dummy object for '!unsafe' tag
    class DummyPYamlObject(object):
            pass

    # Dummy object for '!anotherobject' tag
    class DummyPYamlAnotherObject(object):
            pass

    dummy_pyaml_object = DummyPYamlObject()
    dummy_pyaml_another_object = DummyPYamlAnotherObject()

    # Dummy ConstructorError exception
    class DummyConstructorError(Exception):
            pass

    # Create a safe constructor that returns the expected value when calling
    # the method construct_object with the given tag
    class DummySafeConstructor(AnsibleConstructor):
        def construct_object(self, node):
            if node.tag == u'!unsafe':
                return dummy

# Generated at 2022-06-13 07:34:39.064173
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from itertools import islice

    # Test sequences
    data = ['foo', 'bar', 'baz', 'qux']
    yaml_text = '''\
- foo
- bar
- baz
- qux
'''
    assert yaml_text == AnsibleDumper(width=float("inf")).dump(data)
    res = AnsibleLoader(yaml_text).get_single_data()
    assert type(res) == AnsibleSequence
    assert res == data



# Generated at 2022-06-13 07:34:44.465923
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # When constructed with a yaml.nodes.SequenceNode argument,
    # the AnsibleConstructor.construct_yaml_seq method will yield
    # an AnsibleSequence and extend it with the result of the
    # AnsibleConstructor.construct_sequence method.
    pass

# Generated at 2022-06-13 07:34:54.059469
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    """
    Test AnsibleConstructor.construct_yaml_unsafe method.

    :return:
    """

    data = """
    b: 2
    a: 1
    c: !unsafe "{{x}}"
    """

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # Test construct_yaml_unsafe with a proxy object !unsafe "{{x}}"
    constructor = AnsibleConstructor(file_name=None, vault_secrets=[])
    result = list(constructor.construct_documents(data))

    assert isinstance(result[0]['c'], wrap_var)
    assert result[0]['c']._obj == "{{x}}"

# Generated at 2022-06-13 07:35:00.882565
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # tests both default VaultLib, and passing in a per-file vault secret
    class TestSecret(object):
        pass
    TestSecret.vault_secret = ['test_vault_secret']
    test_secret = TestSecret()


# Generated at 2022-06-13 07:35:04.842525
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test with a unicode string
    node = 'node'
    ret = AnsibleConstructor().construct_yaml_str(node)
    assert isinstance(ret, AnsibleUnicode)
    assert ret == 'node'



# Generated at 2022-06-13 07:35:14.257028
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = '''
    a: 1
    b: 2
    c: 3
    '''
    for duplicate_key_handling in ['ignore', 'warn', 'error']:
        with set_env_var(C.DUPLICATE_YAML_DICT_KEY, duplicate_key_handling):
            ansible_constructor = AnsibleConstructor()
            ansible_constructor.construct_yaml_map(yaml.compose(yaml.load(data)))
            value = ansible_constructor.construct_mapping(yaml.compose(yaml.load(data)))
            assert value == {u'a': 1, u'b': 2, u'c': 3}

    data = '''
    a: 1
    a: 2
    a: 3
    '''

# Generated at 2022-06-13 07:35:39.136399
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml import objects
    import sys

    # Create a list with a very simple value. E.g. a list with the string "test"
    test_list = u'---\n- test\n'

    # Create a AnsibleConstructor object and load it using the test_list variable.
    ac = AnsibleConstructor()
    loading_result = AnsibleLoader(test_list, ac).get_single_data()

    # Check if the loading_result is a AnsibleSequence-object.
    if not isinstance(loading_result, objects.AnsibleSequence):
        print("The loading_result is not a AnsibleSequence-object. Exiting with exit code 1.\n")
        sys.exit(1)

# Generated at 2022-06-13 07:35:50.739038
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():  # noqa
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping

    # AnsibleConstructor(yaml.SafeLoader) hooks
    # _construct_yaml_seq into yaml.SafeLoader.construct_yaml_seq
    class TestYaml(AnsibleBaseYAMLObject):
        pass

    # AnsibleConstructor.construct_yaml_seq uses self.construct_sequence()
    # to convert the node value into a python sequence object.
    # construct_sequence() casts the value through construct_object()
    # and construct_object() calls type.__call__ to create an instance
    # of the constructor.  To get the correct constructor, construct_object()
    # needs to be overridden.

# Generated at 2022-06-13 07:35:58.774154
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ascii_string = u'ascii'
    unicode_string = u'unicode'
    str1 = AnsibleConstructor.construct_yaml_str(ascii_string)
    str2 = AnsibleConstructor.construct_yaml_str(unicode_string)
    assert isinstance(str1, AnsibleUnicode)
    assert isinstance(str2, AnsibleUnicode)
    assert str1 == ascii_string
    assert str2 == unicode_string

# Generated at 2022-06-13 07:36:04.935670
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # mocking node
    class MockNode(object):
        start_mark = ''

    # mocking constructor node
    class MockConstructorNode(object):
        def __init__(self):
            self.value = None
            self.start_mark = ''

        id = 'constructor'

    node = MockNode()
    constructor_node = MockConstructorNode()
    ansible = AnsibleConstructor()
    assert ansible.construct_mapping(node) == {}

# Generated at 2022-06-13 07:36:16.216763
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault = VaultLib(secrets=[])
    vault_data = vault.encrypt(b'password')
    vault_encrypted_data = vault.encrypt(vault_data.encode('utf-8'))
    # Test if the construct_vault_encrypted_unicode method returns an instance of AnsibleVaultEncryptedUnicode
    # and that the returned data is exactly the same as the encrypted vault data
    constructor = AnsibleConstructor()
    vault_encrypted_unicode = constructor.construct_vault_encrypted_unicode(vault_encrypted_data)
    assert isinstance(vault_encrypted_unicode, AnsibleVaultEncryptedUnicode)
    assert vault_encrypted_unicode.unvault_text() == vault_data

# Generated at 2022-06-13 07:36:24.861961
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # default ansible.cfg
    ansible_cfg = 'tests/ansible.cfg'
    # A mock AnsibleConstructor
    test_constructor = AnsibleConstructor('tests/fixtures/unittest_constructor/no_secret.yml', vault_secrets=['test'])
    # construct_yaml_map with a node

# Generated at 2022-06-13 07:36:30.797866
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml

    file_name = 'tests/unit/parsing/yaml/artifacts/ansible4054.yml'
    with open(file_name) as f:
        yaml_string = f.read()
    yaml_string = yaml_string.replace('!vars', '!unsafe')

    obj = yaml.load(yaml_string, Loader=AnsibleConstructor)
    assert(obj['name'] == "{{ inventory_hostname }}")

# Generated at 2022-06-13 07:36:38.642671
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import os
    import yaml

    # This test assumes that the environment
    # variable TDD_VAULT_PASSWORD is defined
    # and has a value (not None or empty string)
    vault_password = os.environ.get('TDD_VAULT_PASSWORD')
    if not vault_password:
        print('TDD_VAULT_PASSWORD environment variable not defined')
        sys.exit(1)

    # This test assumes that the environment
    # variable TDD_VAULT_PASSWORD has a valid vault
    # password.  It checks that a password supplied
    # by TDD_VAULT_PASSWORD can decrypt the string
    # below

# Generated at 2022-06-13 07:36:46.605330
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    loader = AnsibleConstructor()

    mapping = loader.construct_mapping({"a": 1, "b": 2, "c": 3}, deep=True)
    assert mapping == {"a": 1, "b": 2, "c": 3}, \
            "failed to parse mapping without duplicated keys"

    mapping = loader.construct_mapping({"a": 1, "b": 2, "a": 3}, deep=True)
    assert mapping == {"a": 3, "b": 2}, \
            "failed to parse mapping with duplicated keys"



# Generated at 2022-06-13 07:36:55.153184
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible import constants as C
    # Test with default dunder_slots value
    c = AnsibleConstructor()
    result = c.construct_yaml_str(None)
    assert isinstance(result, AnsibleUnicode)
    assert not result._data.__slots__

    # Test with dunder_slots set to True
    C.DEFAULT_UNICODE_SLOTS = True
    c = AnsibleConstructor()
    result = c.construct_yaml_str(None)
    assert isinstance(result, AnsibleUnicode)
    assert result._data.__slots__

# Generated at 2022-06-13 07:37:31.721995
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # TODO: complete unit test for construct_mapping method
    assert 1 == 1

# Generated at 2022-06-13 07:37:39.344968
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    AnsibleConstructor_1 = AnsibleConstructor()

# Generated at 2022-06-13 07:37:45.854489
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import ansible.parsing.yaml.objects

    data = ansible.parsing.yaml.objects.AnsibleUnicode(u'foo')
    node = object()
    myAnsConst = AnsibleConstructor()

    class foo:
        start_mark = ''
        id = 'foo'
        value = 'bar'

    assert myAnsConst.construct_yaml_str(foo) == 'bar'


# vim: set expandtab ts=4 sw=4:

# Generated at 2022-06-13 07:37:53.932066
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_str = """
k1:
  k11: v11
  k12: v12
  k13: v13
k2:
  k21: v21
  k22: v22
  k23: v23
k3:
  k31: v31
  k32: v32
  k33: v33
"""
    data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert data['k1']
    assert data['k2']
    assert data['k3']
    assert data['k1']['k11'] == 'v11'
    assert data['k1']['k12'] == 'v12'
    assert data['k1']['k13'] == 'v13'

# Generated at 2022-06-13 07:38:01.332762
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    cstr = AnsibleConstructor(file_name='foobar')
    assert cstr
    s = ''
    # non-existent key
    s += '!!!python/dict "dict key"\n'
    s += ': !!!python/object/new:module.class\n'
    s += '   "dict key": !!!python/object/new:module.class.__init__\n'
    s += '   "dict value": !!!python/object/new:module.class.__init__\n'
    # non-existent value
    s += '   "dict value": !!!python/object/new:module.class.__init__\n'
    # existing key
    s += '   "dict key": !!!python/object/new:module.class.__init__\n'
