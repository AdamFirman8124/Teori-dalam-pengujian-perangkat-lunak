

# Generated at 2022-06-13 07:28:06.895261
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    yaml_data = ''' ---
    a:
        b: 1
        c: 2
    d: 3
    '''

    node = yaml.compose(yaml_data)
    yaml.construct_mapping(node)

# Generated at 2022-06-13 07:28:18.177553
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import os
    import __main__ as main
    import unittest
    import yaml # FIXME: use module loading to allow for testing without libyaml support

    # Save original module, for cleanup at end
    orig_sys_modules_main = sys.modules['__main__']

    # Create a dummy '__main__' module, to be used by AnsibleConstructor
    class DummyMainModule(object):
        pass
    sys.modules['__main__'] = DummyMainModule()

    # Create a dummy '__file__' variable, to be used by AnsibleConstructor
    current_dir = os.path.dirname(__file__)
    test_file = os.path.join(current_dir, 'tests', 'test_yaml_constructor.py')

# Generated at 2022-06-13 07:28:28.723890
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml import from_yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    secret_msg = to_native(b'hello world')

# Generated at 2022-06-13 07:28:31.649111
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import ansible.parsing.yaml

    # Prepare arguments
    node = 'node'

    # Execute the script
    ansible.parsing.yaml.AnsibleConstructor.construct_mapping(node)

# Generated at 2022-06-13 07:28:33.916540
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    src = """
foo: bar
bar: 1
"""
    data = yaml.load(src, Loader=AnsibleConstructor)
    assert data == dict(foo='bar', bar=1)



# Generated at 2022-06-13 07:28:41.441098
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:28:45.476547
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['test_vault_secret']
    a = AnsibleConstructor(vault_secrets=vault_secrets)
    assert a.vault_secrets == ['test_vault_secret']

# Generated at 2022-06-13 07:28:58.312989
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_passwords = ['vault_password']
    constructor = AnsibleConstructor(vault_secrets=vault_passwords)
    node = constructor.construct_yaml_str('$ANSIBLE_VAULT;1.1;AES256;myuser\n333737356233666263326561643937303765356661303231393132613862373364363865653232373\n36376466396564663730626466353838643663346138346533313961643236616336653462623365\n39646636366466316137643964613337626134316632646437636266653530363163356366643630\n37613534373938333662383537\n')

# Generated at 2022-06-13 07:29:12.204879
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml

    yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                         ansible_construct_mapping)


# Generated at 2022-06-13 07:29:18.436533
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ansible_constructor = AnsibleConstructor()
    mapping_node = MappingNode(tag='tag:yaml.org,2002:map', value=[])
    mapping_node.start_mark = object()
    actual = ansible_constructor.construct_mapping(mapping_node)
    assert type(actual) is AnsibleMapping
    assert actual.ansible_pos is mapping_node.start_mark

# Generated at 2022-06-13 07:29:27.055014
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    data = yaml.load("""
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
    """, Loader=AnsibleConstructor)

    assert isinstance(data, list)
    assert data == [1,2,3,4,5,6,7,8,9,10,11,12,13]


# Generated at 2022-06-13 07:29:36.581042
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    constructor = AnsibleConstructor()

    # default is to return unicode
    assert isinstance(constructor.construct_yaml_str(None), AnsibleUnicode)

    # empty string is unicode
    node = type('EmptyStringNode', (object,), dict(start_mark=None))
    assert isinstance(constructor.construct_yaml_str(node), AnsibleUnicode)

    # non-empty string is unicode
    node = type('NonEmptyStringNode', (object,), dict(start_mark=None))
    assert isinstance(constructor.construct_yaml_str(node), AnsibleUnicode)

# Generated at 2022-06-13 07:29:45.544739
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml import load
    from yaml.nodes import SequenceNode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_snippet = """
    - "value1"
    - "value2"
    """
    yaml_results = load(yaml_snippet, Loader=AnsibleLoader)
    a = AnsibleConstructor()
    b = SequenceNode(tag=u'tag:yaml.org,2002:seq')
    c = a.construct_yaml_seq(b)

    assert(isinstance(yaml_results, AnsibleSequence))
    assert(isinstance(c, AnsibleSequence))

# Generated at 2022-06-13 07:29:51.421813
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # instance attributes
    yaml_file = 'test_file.yml'
    vault_secrets_1 = 'secret1'
    vault_secrets_2 = 'secret2'
    vault_secrets = [vault_secrets_1, vault_secrets_2]

    # test case
    # expect pass
    ansible_constuctor = AnsibleConstructor(yaml_file, vault_secrets)
    assert ansible_constuctor._ansible_file_name == yaml_file
    assert ansible_constuctor.vault_secrets == vault_secrets
    assert ansible_constuctor._vaults['default'] is not None

# Generated at 2022-06-13 07:29:55.862108
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # given
    node = MappingNode(tag=u'tag:yaml.org,2002:python/dict', value=[], start_mark=None, end_mark=None)
    ac = AnsibleConstructor()

    # when
    ret = ac.construct_yaml_seq(node)

    # then
    assert isinstance(ret, AnsibleSequence)



# Generated at 2022-06-13 07:30:01.317762
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    yaml_code = """
---
- TEST SEQ1
- TEST SEQ2
"""

    yaml_result = yaml.load(yaml_code, Loader=AnsibleConstructor)

    assert yaml_result == ['TEST SEQ1', 'TEST SEQ2']


# Generated at 2022-06-13 07:30:05.746772
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    yaml_data = """
    foo: first
    foo: last
    """

    original_setting = C.DUPLICATE_YAML_DICT_KEY
    C.DUPLICATE_YAML_DICT_KEY = 'ignore'  # Don't care what the setting is

# Generated at 2022-06-13 07:30:14.751983
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # test default behavior
    yaml_str = '''
    a: 1
    b: 2
    '''
    yaml_data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(yaml_data, AnsibleMapping)
    assert yaml_data['a'] == 1
    assert not hasattr(yaml_data['a'], 'ansible_pos')
    assert yaml_data['b'] == 2
    assert not hasattr(yaml_data['b'], 'ansible_pos')

    # test to make sure attributes are set
    yaml_str = '''
    a: 1
    b: 2
    '''
    yaml_data = yaml.load(yaml_str, Loader=AnsibleConstructor)

    assert has

# Generated at 2022-06-13 07:30:24.700322
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    """
    This is a little convoluted but we want to test the following conditions in this unit test:
    - vault secrets provided
    - vault ciphertext, but no vault secrets
    - "decrypt" function actually returns plaintext, not ciphertext
    """

    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))

    import ansible.constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml import AnsibleConstructor, AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # case 1:
    vault_secrets = ["secret1", "secret2", "secret3"]
    vault = VaultLib(secrets = vault_secrets)

# Generated at 2022-06-13 07:30:35.766743
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    constructor = yaml.constructor.Constructor(yaml.safe_load)
    constructor.add_constructor(
        u'tag:yaml.org,2002:map',
        constructor.construct_yaml_map)
    constructor.add_constructor(
        u'tag:yaml.org,2002:python/dict',
        constructor.construct_yaml_map)
    constructor.add_constructor(
        u'tag:yaml.org,2002:str',
        constructor.construct_yaml_str)
    constructor.add_constructor(
        u'tag:yaml.org,2002:python/unicode',
        constructor.construct_yaml_str)

# Generated at 2022-06-13 07:30:50.044028
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:31:01.072007
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import os
    import sys
    import tempfile
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Create temporary file and write yaml string to it
    tmp = tempfile.NamedTemporaryFile(mode='w+t')
    tmp.file.write('!!python/object/apply:os.system [\'echo "Hello, the time is now $(date +%T)"\']')
    tmp.file.seek(0)

    # Parse yaml string
    data = AnsibleLoader(tmp.file, file_name='test_file').get_single_data()

    # Evaluate the resulting data

# Generated at 2022-06-13 07:31:07.807824
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Input data
    input_data = {"a": 1, "b": 1, "c": 2}
    input_data_with_duplicates = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 2}
    # Expected output data
    expected_output_data = {"a": 1, "b": 1, "c": 2}
    expected_output_data_with_duplicates_ignore = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 2}
    expected_output_data_with_duplicates_warn = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 2}

# Generated at 2022-06-13 07:31:19.037146
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:31:29.718338
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    testcases = {
        "test_duplicate_yaml_dict_key" : {
            'yaml' : "foo: bar\nfoo: baz",
            'expected_lines' : [
                "foo: bar",
                "foo: baz"
            ],
            'expected_columns': [
                1,
                6
            ],
            'expected_msg' : u'While constructing a mapping from <string>, line 1, column 1, found a duplicate dict key (foo). Using last defined value only.'
        }
    }


# Generated at 2022-06-13 07:31:38.113499
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import _fixture

    # test for Node that represents a scalar text value
    #   * constructor = u'!vault'
    #   * value = b'$ANSIBLE_VAULT;1.2;AES256;ansible\r\n'
    #   * start_mark = Mark(u'', 0, 1, 1, None, None)
    #   * end_mark = Mark(u'', 11, 1, 12, None, None)
    #   * style = u'?'
    arg_node = _fixture.construct_yaml_scalar_node_unformatted_vault_encrypted_string()
    arg_secrets = ['Vv0C6ElZVqlKdNxFifD9q4v4nGcf/7zier6aW2V8MJw=', ]


# Generated at 2022-06-13 07:31:43.974094
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode()
    node.value = None
    ac = AnsibleConstructor()
    assert ac.construct_mapping(node) == {}

    node.value = []
    assert ac.construct_mapping(node) == {}

    node.value = [(1, 2), (1, 3)]
    assert ac.construct_mapping(node) == {1: 3}



# Generated at 2022-06-13 07:31:47.333120
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    def _mock_construct_scalar(node):
        return "testPassword"

    ac = AnsibleConstructor()
    ac.construct_scalar = _mock_construct_scalar
    ac.construct_vault_encrypted_unicode(None)

# Generated at 2022-06-13 07:31:54.353805
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    obj = AnsibleConstructor()
    mapping = AnsibleMapping()
    mapping['foo'] = 'bar'
    mapping['baz'] = 'quux'
    assert obj.construct_mapping(mapping) == mapping
    mapping['foo'] = 'override'
    assert obj.construct_mapping(mapping) == mapping

# Generated at 2022-06-13 07:32:01.863914
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    node_1 = AnsibleConstructor.construct_yaml_map({'a': 1, 'b': 2})
    assert( isinstance(node_1,AnsibleMapping) )
    assert( len(node_1) == 2 )
    assert( node_1['a'] == 1 )
    assert( node_1['b'] == 2 )


# Generated at 2022-06-13 07:32:15.248097
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml import nodes

    test = 'string'
    expected = 'string'

    m = nodes.ScalarNode('tag:yaml.org,2002:str', test)

    ac = AnsibleConstructor()
    actual = ac.construct_yaml_str(m)

    assert (actual) == (expected)

# Generated at 2022-06-13 07:32:18.010637
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml.nodes import ScalarNode

    data = u'AnsibleConstructor_construct_yaml_str'
    mock_node = ScalarNode( u'tag:yaml.org,2002:str', data )

    ac = AnsibleConstructor()

    # Method is callable
    ac.construct_yaml_str(mock_node)
    assert(data, ac.construct_yaml_str(mock_node))

# Generated at 2022-06-13 07:32:27.980351
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    import yaml
    data = AnsibleUnicode("This is a test")
    string_val = yaml.dump(data, default_flow_style=True)
    print("ANSIBLE_UNICODE: %s" % string_val)
    assert string_val == u'!ansible/unicode |\n  This is a test\n'
    data = AnsibleUnicode("")
    string_val = yaml.dump(data, default_flow_style=True)
    print("ANSIBLE_UNICODE: %s" % string_val)
    assert string_val == u'!ansible/unicode |\n  \n'

# Generated at 2022-06-13 07:32:33.606382
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    for C.DUPLICATE_YAML_DICT_KEY in ['error', 'warn', 'ignore']:
        yaml_data = '''\
        foo: bar
        foo: baz
        '''
        loaded_data = yaml.load(yaml_data, AnsibleConstructor)
        if C.DUPLICATE_YAML_DICT_KEY == 'error':
            assert loaded_data is None
        else:
            assert loaded_data['foo'] == 'baz'

# Generated at 2022-06-13 07:32:41.936627
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    myAnsibleConstructor = AnsibleConstructor()

    sample_dict = {'key1': 'value1', 'key2': 'value2'}
    yaml_node = myAnsibleConstructor.construct_yaml_map(MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=False))

    assert isinstance(yaml_node, AnsibleMapping)
    assert yaml_node.ansible_pos == (None, 0, 0)  # default values for ansible_pos in AnsibleMapping



# Generated at 2022-06-13 07:32:51.328762
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Test with AnsibleSequence
    yaml_text = """
stuff:
- one
- two
- three
    """
    # Note: The import in this particular file can't be replaced by a
    # from ansible.parsing.yaml.loader import AnsibleLoader because the
    # AnsibleLoader class is defined after the AnsibleConstructor class
    from ansible.parsing.yaml.loader import AnsibleLoader
    data = AnsibleLoader(yaml_text).get_single_data()
    assert isinstance(data['stuff'], AnsibleSequence)
    assert data['stuff'] == ['one', 'two', 'three']

    # Test without AnsibleSequence
    yaml_text = """
stuff: [ one, two, three ]
    """
    data = AnsibleLoader(yaml_text).get

# Generated at 2022-06-13 07:32:57.014467
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    def test(vault_password):
        secret_string = u'Hello, world!'
        vault_lib = VaultLib(secrets=[vault_password])
        encoded = vault_lib.encrypt(secret_string)
        node = yaml.nodes.ScalarNode(tag=u'!vault', value=encoded)
        v = AnsibleConstructor().construct_vault_encrypted_unicode(node)
        assert v == secret_string

    # test without vault password
    try:
        test(None)
    except ConstructorError:
        pass
    else:
        assert False

    # test with vault password
    test(u'foobar')

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 07:33:00.647383
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Create an instance of AnsibleConstructor
    ansible_constructor = AnsibleConstructor()

    data = u'Hello!'
    # Create a node
    node = None
    # Test the method
    assert ansible_constructor.construct_yaml_str(node) == data



# Generated at 2022-06-13 07:33:01.121575
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:33:10.427698
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import find_vault_secrets_class

    vault_secrets_cls = find_vault_secrets_class()

    # Test: It will return the crypto key and its id
    vault_secrets_obj = vault_secrets_cls()
    crypto_key, vault_id = vault_secrets_obj.get_vault_secrets()[0]

    # Test: It will return a new instance of AnsibleConstructor
    # which verifies that the vault_secrets is a list


# Generated at 2022-06-13 07:33:25.494903
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import StringIO
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    data = StringIO.StringIO(u'\xEF\xBB\xBF- !unsafe "{\'a\': 1}\"\n')

    c = AnsibleConstructor(file_name=u'<it>')
    c.vault_secrets = [u'it']
    # call the yaml.load() method from the yaml library
    output = c.get_single_data(data)

    assert isinstance(output, AnsibleUnsafeText)
    assert output == u'{\'a\': 1}'

# Generated at 2022-06-13 07:33:34.397591
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import unittest
    from yaml.parser import Parser
    from yaml.scanner import Scanner
    import sys


# Generated at 2022-06-13 07:33:45.650811
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.module_utils._text import to_bytes

    # AnsibleConstructor.construct_mapping() converts duplicate dict keys in warnings and errors into a quietly
    # overwritten dict, as described in the ConfigParser module. We unit test that behavior here.

    ns = dict(warn=to_bytes('warn'), error=to_bytes('error'), ignore=to_bytes('ignore'))
    for duplicate_yaml_dict_key in (ns['warn'], ns['error'], ns['ignore']):
        builder = AnsibleConstructor()


# Generated at 2022-06-13 07:33:54.230877
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_data = b"""
---
- hosts: localhost
  tasks:
    - name: test
      shell: id
    - name: test2
      shell: id
"""
    import yaml
    from yaml.scanner import ScannerError
    from yaml.parser import ParserError
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    try:
        data = yaml.load(yaml_data, Loader=AnsibleLoader)
        assert isinstance(data, AnsibleSequence)
    except (ScannerError, ParserError) as e:
        print("test_AnsibleConstructor_construct_yaml_seq: %s" % e.message)
        assert False

# Generated at 2022-06-13 07:34:02.215011
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    import sys, os
    sys.path.append(os.path.dirname(__file__) + '/../../')

    import lib.tree as tree

    class FakeLoader:
        class FakeStream:
            class FakeNode:
                tag = u'tag:yaml.org,2002:seq'
                id   = u'seq'
                #Empty list
                value = []

            def __init__(self):
                self.node = FakeLoader.FakeStream.FakeNode()

            def __iter__(self):
                return self

            def __next__(self):
                return self.node

        def __init__(self):
            self.stream = FakeLoader.FakeStream()

        def get_single_data(self):
            return self.stream

    fake_loader = FakeLoader()
    fake_constructor = Ansible

# Generated at 2022-06-13 07:34:06.417700
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ac = AnsibleConstructor()
    assert ac.construct_yaml_str('test') == u'test'
    assert ac.construct_yaml_str('test') is not 'test'

# Generated at 2022-06-13 07:34:10.900574
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class ustr(str):
        def __eq__(self, other):
            return isinstance(other, self.__class__) and self is other

    class umap(AnsibleMapping):
        def __eq__(self, other):
            return isinstance(other, self.__class__) and self is other

    ac = AnsibleConstructor()
    # create a node that has the same encoding as u'\u2713'
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[(
        ustr(chr(0x2713)),
        ustr(u'\u2713'),
    )])
    # construct_mapping tries to compare the key with ASCII string
    # if it is ASCII string, it will not be converted to unicode,
    # and key comparison will fail

# Generated at 2022-06-13 07:34:14.837923
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Simple test to make sure it doesn't throw exception
    node = MappingNode(u'tag:yaml.org,2002:map', [], None, None, False)
    AnsibleConstructor().construct_yaml_map(node)



# Generated at 2022-06-13 07:34:21.513951
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing import vault

    yaml_data = """
        foo: !unsafe 'bar'
    """

    display = Display()
    vault_secrets = vault.lookup_vault_secrets(filename='dummmy', vault_password_files=None, passwords=None,
                                               prompt=display.input)

    c = AnsibleConstructor(vault_secrets=vault_secrets)
    c.construct_yaml_map(c.compose_document(yaml_data))

# Generated at 2022-06-13 07:34:26.341671
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secret = "1234"
    expected_value = u'$ANSIBLE_VAULT;1.2;AES256;test\n323232323232323232323232323232323232323232323231'

    # Test failure when no secret was provided
    with pytest.raises(ConstructorError) as execinfo:
        AnsibleConstructor(vault_secrets=[]).construct_vault_encrypted_unicode('!vault '+expected_value)
    assert "found !vault but no vault password provided" in str(execinfo.value)

    # Test successful construction of VaultEncryptedUnicode
    actual_value = AnsibleConstructor(vault_secrets=[vault_secret]).construct_vault_encrypted_unicode('!vault '+expected_value)

# Generated at 2022-06-13 07:34:55.778052
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.utils.yaml import _ordered_attrdict as oad
    # We're testing an edge case, so we must construct the 'tag:yaml.org,2002:map' instance we send to
    # our constructor manually.
    class MockMappingNode(MappingNode):
        pass
    mock_node = MockMappingNode('tag:yaml.org,2002:map')
    mock_node.value = [(oad(value='foo'),oad(value='bar')), (oad(value='baz'),oad(value='qux'))]

    mock_constructor = AnsibleConstructor()
    mock_oid_constructor = AnsibleConstructor()
    mock_constructor.construct_mapping = lambda x,deep=False: {'foo': 'bar', 'baz': 'qux'}


# Generated at 2022-06-13 07:35:00.575096
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from yaml.nodes import ScalarNode

# Generated at 2022-06-13 07:35:10.963194
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['vault']

    display.current_screen = ['vault password: ', 'vault password: ']
    display.screen_output = []
    display.verbosity = 0

    constructor = AnsibleConstructor(vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:35:23.053775
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode, AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.add_constructor(u'tag:yaml.org,2002:map', AnsibleConstructor.construct_yaml_map)
    ansible_constructor.add_constructor(u'tag:yaml.org,2002:python/dict', AnsibleConstructor.construct_yaml_map)
    ansible_constructor.add_constructor(u'tag:yaml.org,2002:str', AnsibleConstructor.construct_yaml_str)

# Generated at 2022-06-13 07:35:27.861948
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_data = '''
- name: test1
- name: test2
'''
    yaml_data = yaml_data.strip()
    data = yaml.load(yaml_data, Loader=yaml.Loader)
    assert type(data) == AnsibleSequence

# Generated at 2022-06-13 07:35:35.121044
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    import sys
    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO

    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_str = '''
some_unsafe_lookup: "{{ some_variable }}"
some_safe_variable: "{{ safe_variable }}"
    '''
    yaml_file = StringIO(yaml_str)
    data = AnsibleLoader(yaml_file, file_name='<string>').get_single_data()
    assert '{{ some_variable }}' == data['some_unsafe_lookup']
    assert '{{ safe_variable }}' != data['some_safe_variable']

# Generated at 2022-06-13 07:35:41.617022
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.yaml.objects import AnsibleUnicode
    import sys
    import os
    import six

    content = "test"

    if not six.PY3:
        content = content.decode('utf-8')

    # Set the password temporarly
    if hasattr(sys, 'real_prefix'):
        vault_secrets = [VaultSecret(os.getenv('ANSIBLE_VAULT_PASSWORD_FILE'))]
    else:
        vault_secrets = [VaultSecret(os.getenv('HOME') + '/.ansible_vault_password')]

    # Create

# Generated at 2022-06-13 07:35:53.018701
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import ansible.parsing.yaml.objects
    ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode = object
    f = AnsibleConstructor()
    node = {'start_mark':{'line':0, 'column':0, 'name': None}, 'id': 'vault-encrypted', 'value': None}
    class Test:
        start_mark = None
        end_mark = None
        node = None
    value_node = Test()
    value_node.value = 'vaulted_value'
    value_node.start_mark = {'line':0, 'column':0, 'name': None}
    node['value'] = value_node
    ret = f.construct_vault_encrypted_unicode(node)

# Generated at 2022-06-13 07:36:04.164231
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    class MockObject:
        def __init__(self, **kw):
            for k,v in kw.items():
                setattr(self, k, v)

    #Test with mocked object
    #yaml_str = !unsafe "Class: 'ansible.parsing.yaml.objects.AnsibleMapping'"
    yaml_str = "!unsafe 'Class: '\"ansible.parsing.yaml.objects.AnsibleMapping\"''"
    construct_yaml_unsafe = AnsibleConstructor().construct_yaml_unsafe
    o = construct_yaml_unsafe(MockObject(tag=u'!unsafe', id=u'!unsafe', value=yaml_str))
    assert isinstance(o, AnsibleMapping)

# Generated at 2022-06-13 07:36:12.550667
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """
    This test method is for testing the AnsibleConstructor class method construct_yaml_map when the
    input value is of the data structure list. The expected value is string 'list'.
    """
    class_obj = AnsibleConstructor()
    node = "test"
    value = class_obj.construct_yaml_map(node)
    assert getattr(getattr(value, "__next__")(), "__class__").__name__ == 'dict'



# Generated at 2022-06-13 07:37:06.901842
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    vault_keys = [u'random']
    vault_file_contents = u'some secrets string'
    vault_key_id = u'random'
    vault_data = AnsibleVaultEncryptedUnicode.encrypt(
            vault_file_contents, vault_keys, vault_key_id)
    node = AnsibleUnicode(vault_data)
    ''' TODO: FIXME: For some reason, the node object is
    not getting set to AnsibleVaultEncryptedUnicode.
    The following tests the node object to ensure it is
    AnsibleVaultEncryptedUnicode.
    '''

# Generated at 2022-06-13 07:37:16.666680
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:37:28.552148
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    construct_yaml_map = AnsibleConstructor.construct_yaml_map

    with pytest.raises(ConstructorError):
        constructor = AnsibleConstructor()
        bad_node = object()
        construct_yaml_map(constructor, bad_node)

    with pytest.raises(ConstructedBadTypeException):
        node = MappingNode(u'tag:yaml.org,2002:map', [], start_mark=None, end_mark=None)
        node_dict = construct_yaml_map(AnsibleConstructor(), node)
        node_dict.test_bad_key

    with pytest.raises(ConstructedBadTypeException):
        node = MappingNode(u'tag:yaml.org,2002:map', [], start_mark=None, end_mark=None)
        node_

# Generated at 2022-06-13 07:37:37.490739
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import sys
    import types

    ansible_yaml = """
      - test1: {__unsafe__: !python/object:__builtin__.open ['file']}
      - test2: {__unsafe__: {__unsafe__: !python/object:__builtin__.open ['file']}}
    """
    ansible_result = [ {u'test1': open('file')}, {u'test2': {u'__unsafe__': open('file')}} ]

    # Test AnsibleLoader
    data = AnsibleLoader(ansible_yaml).get_single_data()
    assert data == ansible_result

    # Test AnsibleConstructor

# Generated at 2022-06-13 07:37:47.449241
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # pylint: disable=no-member
    # pylint: disable=unused-variable

    # test AnsibleConstructor.construct_yaml_str(node)
    # AnsibleConstructor.construct_yaml_str() returns
    # an instance of AnsibleUnicode, from which we can
    # only get an attribute:
    #   AnsibleUnicode.ansible_pos
    # which contains the position of the node in the YAML file

    # empty string
    yaml_str = ''
    node = yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=yaml_str)
    c = AnsibleConstructor()
    ans_obj = c.construct_yaml_str(node)

# Generated at 2022-06-13 07:37:54.807892
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_passwords = [b'VaultPassword1', b'VaultPassword2']
    vault_password_file = '/tmp/__ansible_vault1'
    with open(vault_password_file, 'wb') as fh:
        fh.write(b'VaultPassword1\n')


# Generated at 2022-06-13 07:37:58.301602
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    class AnsibleConstructor_construct_yaml_seq(AnsibleConstructor):
        def construct_sequence(self, node):
            return [1, 2]

    c = AnsibleConstructor_construct_yaml_seq()
    assert list(c.construct_yaml_seq(None)) == [2, 3]