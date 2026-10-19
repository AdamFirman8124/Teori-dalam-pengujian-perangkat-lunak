

# Generated at 2022-06-13 07:28:12.038821
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    mock_node = object()

    # Test with invalid scenarios
    secrets = None
    cons = AnsibleConstructor(vault_secrets=secrets)
    with pytest.raises(ConstructorError) as excinfo:
        cons.construct_vault_encrypted_unicode(mock_node)
    assert 'found !vault but no vault password provided' in to_native(excinfo.value)
    assert mock_node.start_mark == excinfo.value.problem_mark

    # Test with valid scenario
    secrets = ['test']
    cons = AnsibleConstructor(vault_secrets=secrets)
    cons.construct_vault_encrypted_unicode(mock_node)


# Generated at 2022-06-13 07:28:23.429583
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    import yaml

    test_data = \
        '''
        a: 1
        b: 2
        c: 3
        '''

    mapping = yaml.load(test_data, Loader=AnsibleConstructor)

    assert isinstance(mapping, AnsibleMapping)
    assert 'a' in mapping and mapping['a'] == 1
    assert 'b' in mapping and mapping['b'] == 2
    assert 'c' in mapping and mapping['c'] == 3

    test_data = \
        '''
        a: 1
        b: 2
        c: 3
        d: 4
        e: 5
        '''

    mapping = yaml.load(test_data, Loader=AnsibleConstructor)

    assert isinstance(mapping, AnsibleMapping)
    assert 'a' in mapping

# Generated at 2022-06-13 07:28:31.690373
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from yaml import Loader, SafeLoader
    from nose.tools import assert_is_instance

    data = '''
- value1
- value2
'''

    assert_is_instance(Loader(data).get_single_data(), AnsibleSequence)
    assert_is_instance(AnsibleConstructor(data).get_single_data(), AnsibleSequence)
    assert_is_instance(SafeLoader(data).get_single_data(), AnsibleSequence)



# Generated at 2022-06-13 07:28:36.338536
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Arrange
    input={"foo": "bar", "utf8": "こんにちは"}
    yaml_node = yaml.nodes.MappingNode.from_yaml(input, loader)
    ansible_constructor = AnsibleConstructor()

    # Act
    result = ansible_constructor.construct_yaml_map(yaml_node)

    # Assert
    assert isinstance(result, list)
    assert result[0] == input


# Generated at 2022-06-13 07:28:39.382015
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    data = """
        - one
        - two
        - three
    """
    loader = AnsibleLoader(data)
    doc = loader.get_single_data()
    assert len(doc) == 3

# Generated at 2022-06-13 07:28:44.186318
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Exercise
    node = u"test_string"
    instance = AnsibleConstructor()
    ans_dict = instance.construct_yaml_str(node)
    assert ans_dict == u"test_string"


# Generated at 2022-06-13 07:28:50.616512
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    safeConstructor = SafeConstructor()
    ansibleConstructor = AnsibleConstructor()
    assert safeConstructor.construct_yaml_str(None).__class__.__name__ == 'str'
    assert ansibleConstructor.construct_yaml_str(None).__class__.__name__ == 'AnsibleUnicode'



# Generated at 2022-06-13 07:28:58.852447
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Create an instance of BasicTest
    yaml_loader = AnsibleConstructor()
    yaml_loader.add_multi_constructor('!map', yaml_loader.construct_yaml_map)

    yaml_str = """
---
- { test_var1: test_value1, test_var2: test_value2, test_var3: test_value3 }
- { test_var1: test_value1, test_var2: test_value2, test_var3: test_value3 }
- { test_var1: test_value1, test_var2: test_value2, test_var3: test_value3 }
- { test_var1: test_value1, test_var2: test_value2, test_var3: test_value3 }
"""

    # Load YAM

# Generated at 2022-06-13 07:29:01.167462
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    assert type(AnsibleConstructor().construct_yaml_str(None)) is AnsibleUnicode

# Generated at 2022-06-13 07:29:07.481789
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    c = AnsibleConstructor()

    # Test for case when deep=False

# Generated at 2022-06-13 07:29:21.632342
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Run the method under test with yaml.nodes.ScalarNode
    yaml_str = "hi"
    scalar_node = yaml.nodes.ScalarNode('tag:yaml.org,2002:str', yaml_str)
    obj = AnsibleConstructor(file_name="test_construct_yaml_str").construct_yaml_str(
        scalar_node
    )
    assert isinstance(obj, AnsibleUnicode)
    assert obj.ansible_pos == ("test_construct_yaml_str", 1, 1)



# Generated at 2022-06-13 07:29:27.986199
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    # This is the string to be parsed, which contains a list
    doc = '''
# ##################################################
# This is a list of items in the inventory file
# ##################################################

[webservers]
foo.example.org
bar.example.org

[dbservers]
one.example.org
two.example.org
three.example.org
'''

    # Parse the string using the ANSIBLE_VAULT_PASSWORD_FILE as a vault password
    ac = AnsibleConstructor(file_name='none')
    parsed_doc = ac.construct_yaml_seq(doc)

    # Manually check that we parsed it correctly
    assert parsed_doc[2] == '[webservers]', 'The string was not parsed correctly'

# Generated at 2022-06-13 07:29:36.622421
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from yaml.parser import Parser

    parser = Parser()
    ast = parser.parse("""
        foo:
          key1: value1
          key2: value2
          key3: value3
      """)

    yaml_constructor = AnsibleConstructor()
    data = yaml_constructor.construct_yaml_map(ast)[0]
    assert data == {u"foo": {u"key1": u"value1", u"key2": u"value2", u"key3": u"value3"}}



# Generated at 2022-06-13 07:29:40.583470
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping
    mapping = AnsibleMapping([('key', 'value')])
    mapping.ansible_pos = ('test_file_name', 1, 1)
    assert AnsibleConstructor().construct_yaml_map(mapping) == mapping

# Generated at 2022-06-13 07:29:51.038563
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from yaml.nodes import MappingNode
    from yaml.constructor import ConstructorError

    test_data = {1: 'one', 2: 'two', 3: 'three'}
    test_data_duplicate_keys = {'root_key': 'root_value', 'environment': 'local'}

    # Test data must be a MappingNode object.
    test_data_invalid = [1, 2, 3]

    # Allowed duplicate keys 'warn', 'error', 'ignore'
    allowed_duplicate_dict_keys = ['warn', 'error', 'ignore']

    # Allowed error message prefixes when duplicate keys are not allowed
    allowed_error_message_prefixes = ['Using last defined value only.', 'Using first defined value only.']


# Generated at 2022-06-13 07:29:51.522674
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:30:02.384802
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

    yaml_test_string_1 = '''\
test_dict_1:
    foo: &foo 42
    bar: *foo
    baz: 63
'''
    test_dict_1_loaded = yaml.load(yaml_test_string_1, Loader=AnsibleConstructor)
    test_dict_1_dict_type = type(test_dict_1_loaded)
    assert test_dict_1_dict_type is dict
    assert test_dict_1_loaded.keys() == ['test_dict_1']
    assert test_dict_1_loaded['test_dict_1'].keys() == ['foo', 'bar', 'baz']
    assert test_dict_1_loaded['test_dict_1']['foo'] == 42
    assert test_dict_1

# Generated at 2022-06-13 07:30:11.531032
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    class YAMLObject(AnsibleConstructor):
        __slots__ = ()

    yaml_object = YAMLObject()
    # Test for a mapping node
    class TestMappingNode(object):
        __slots__ = ('start_mark', 'end_mark', 'line', 'column', 'value', 'id')
        def __init__(self):
            self.start_mark = self
            self.end_mark   = self
            self.line       = 1
            self.column     = 1
            self.id         = "map"
            self.value      = [("a", "b"), ("c", "d")]

        # method required for constructing a mapping node
        def __getitem__(self, key):
            return self.value[key]

    test_mapping_node = TestMappingNode

# Generated at 2022-06-13 07:30:12.078438
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:30:15.877139
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    yaml_data = '''
foo: bar
a: b
c: d
'''
    y = yaml.load(yaml_data, Loader=AnsibleConstructor)
    assert y['foo'] == u'bar'
    assert y['a'] == u'b'
    assert y['c'] == u'd'

# Generated at 2022-06-13 07:30:30.365306
# Unit test for method construct_mapping of class AnsibleConstructor

# Generated at 2022-06-13 07:30:37.810038
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import os
    import pytest
    with open(os.path.join(os.path.dirname(__file__), 'test_yaml_constructor_unsafe_constructor.yml'), 'r') as f:
        data = AnsibleLoader(f).get_single_data()
        assert isinstance(data['value'], AnsibleUnsafeText)
        assert data['value'] == '!!python/unicode $EVN_VAR'

# Generated at 2022-06-13 07:30:46.693745
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    
    # Create constructor to test
    cst = AnsibleConstructor()
    data = AnsibleMapping()
    node = MappingNode()
    value = cst.construct_mapping(node)
    data.update(value)
    datasource, line, column = cst._node_position_info(node)
    data.ansible_pos = (datasource, line, column)
    yaml_map = cst.construct_yaml_map(node)

    assert "dict" in type(next(yaml_map))
    yaml_map.close()


# Generated at 2022-06-13 07:30:48.657675
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    construct_yaml_seq_obj = AnsibleConstructor()
    assert construct_yaml_seq_obj.construct_yaml_seq('') == ''

# Generated at 2022-06-13 07:30:57.025962
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Testing a value with an utf-8 character
    expected = u'abc\u20ac'
    node = AnsibleConstructor.construct_yaml_str(None, expected)
    assert isinstance(node, AnsibleUnicode)
    assert to_native(node) == expected

    # Testing a value with an utf-8 character encoded in a different encoding
    expected = u'abc\u20ac'
    node = AnsibleConstructor.construct_yaml_str(None, to_bytes(expected, 'latin1'))
    assert isinstance(node, AnsibleUnicode)
    assert to_native(node) == expected

# Generated at 2022-06-13 07:31:01.028225
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    a = AnsibleConstructor()
    result = a.construct_yaml_map(None)
    assert result is not None
    correct_result = AnsibleMapping()
    assert result == correct_result
    result.update(correct_result)
    assert result == correct_result


# Generated at 2022-06-13 07:31:05.071501
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    file_name = "/etc/ansible/hosts"
    vault_secrets = None
    ansible_constructor = AnsibleConstructor(file_name=file_name, vault_secrets= vault_secrets)
    node = AnsibleSequence()
    assert_obj = ansible_constructor.construct_yaml_seq(node)
    assert(assert_obj is not None)


# Generated at 2022-06-13 07:31:08.983748
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import BytesIO
    import yaml
    stream = BytesIO(b'[1, 2, 3]')
    data = yaml.load(stream, Loader=AnsibleConstructor)
    data[1] = 4
    assert data[1] == 4
    output = yaml.dump(data, Dumper=AnsibleDumper, encoding='utf-8', allow_unicode=True)
    assert output == b'[1, 4, 3]\n'

# Generated at 2022-06-13 07:31:19.357166
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml import AnsibleLoader
    from ansible.module_utils._text import to_text
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import yaml

# Generated at 2022-06-13 07:31:27.612484
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """
    Test of the method construct_mapping from class AnsibleConstructor.
    """
    from io import StringIO
    from yaml import dump, load

    # We need to construct a node
    data = dump({'key1': 'value1', 'key2': 'value2'})
    data_stream = StringIO(data)
    document = load(data_stream)
    mapping_node = document.value[0]

    # We can then test the method.
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_mapping(mapping_node)

# Generated at 2022-06-13 07:31:39.906127
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    testdata = u"""[1,2,3,[4,5,6],{'k': 'v'}, 'something', 'something else', !unsafe 'I am unsafe']"""
    result = yaml.load(testdata, Loader=AnsibleLoader)
    assert isinstance(result, AnsibleSequence)
    assert len(result) == 8
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3

# Generated at 2022-06-13 07:31:41.227852
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    a = AnsibleConstructor()
    print(a.construct_yaml_seq)

# Generated at 2022-06-13 07:31:50.763208
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml import load, dumper

    a = load(u"foo: 42\nbar: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          66373339313542343564373730323161353537663839623561353764366139386362386233396137\n          646263643832363166633466610a3036613831653965653163363837623233336265353430616330\n          626539663435376633613066322b6330336530343834613733653062613037303438333137353966\n          336537\n", AnsibleConstructor)

# Generated at 2022-06-13 07:32:05.726834
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars, Variable

    loader = AnsibleLoader(None, None, variable_manager=VariableManager())
    vault_password_file = os.path.join(os.path.dirname(__file__), 'vault_password')
    vault_password = [vault_password_file]
    loader._constructor = AnsibleConstructor(vault_secrets=vault_password)

# Generated at 2022-06-13 07:32:08.633377
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    # Test dict object
    data = dict()
    data['a'] = 1
    data['b'] = 2
    data['c'] = 3

    parser = AnsibleConstructor()
    data = parser.construct_yaml_unsafe(None, data)

    assert data.a == 1
    assert data.b == 2
    assert data.c == 3

# Generated at 2022-06-13 07:32:18.493331
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import logging
    import copy

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestAnsibleConstructor_construct_mapping(unittest.TestCase):
        def setUp(self):
            # disable loggers
            logging.disable(logging.CRITICAL)


# Generated at 2022-06-13 07:32:29.122121
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    value = '$ANSIBLE_VAULT;1.2;AES256;ansible\n35326234616637663837336631643164373735666132303836643663313664353166343636375\nEOF'
    b_ciphertext_data = to_bytes(value)
    # could pass in a key id here to choose the vault to associate with
    # TODO/FIXME: plugin vault selector
    vault = VaultLib(secrets=['ansible'])
    ret = AnsibleVaultEncryptedUnicode(b_ciphertext_data)
    ret.vault = vault
    ret.ansible_pos = ('/home/david.p/ansible/test/test-vault.yml', 1, 0)
    assert ret._ansible_vault_encrypted_

# Generated at 2022-06-13 07:32:33.901102
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    ac = AnsibleConstructor()
    test_node = [u'test', u'node']
    expected_result = {u'ansible_pos': (u'<unicode string>', 1, 0)}
    result = ac.construct_yaml_seq(test_node).next()
    assert result == [u'test', u'node']
    assert result.ansible_pos == expected_result[u'ansible_pos']

# Generated at 2022-06-13 07:32:42.826566
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    sample_encoded_data = u"vault-encrypted-data"
    sample_data = b"this will be the decrypted sample data"
    expected_data = u"this will be the decrypted sample data"
    mock_vault = VaultLib(secrets=[b'secret'])
    mock_vault.decrypt = MagicMock(return_value=sample_data)
    results = AnsibleConstructor._construct_vault_encrypted_unicode(mock_vault, sample_encoded_data)
    assert isinstance(results, VaultEncryptedUnicode)
    assert results.data == expected_data

# Generated at 2022-06-13 07:32:52.338648
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import os
    import tempfile
    import shutil
    import textwrap
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    # Create temporary directory to work in
    tmp_dir = tempfile.mkdtemp()
    # This is the YAML we'll load
    data_str = textwrap.dedent(u"""
    ---
    foo: !unsafe !test_class
      bar: baz
    """)

    # Create the file
    (fd, path) = tempfile.mkstemp(dir=tmp_dir, prefix=u'test_', suffix=u'.yml')
    os.close(fd)
    with open(path, u'w') as stream:
        stream.write(data_str)

    # Define a class that has a '

# Generated at 2022-06-13 07:33:12.574017
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    data = '''a: 1
b: 2
'''
    yaml_data = yaml.load(data, Loader=AnsibleConstructor)

    retval = {'a': 1, 'b': 2}
    assert yaml_data == retval


# Generated at 2022-06-13 07:33:14.915069
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    item = '!vault'
    node = AnsibleConstructor.construct_yaml_str(item)
    assert str(item) == str(node)

# Generated at 2022-06-13 07:33:21.230071
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_config = """---
    - 1.0
    - 1
    - test
    -
      - 1
      - 2
      - 3
      - 4
      - 5
    -
      - ansible
      - ansible
    - False
    - null
    """
    res = yaml.load(yaml_config, Loader=yaml.Loader)
    assert len(res) == 8
    assert res[0] == 1.0
    assert res[1] == 1
    assert res[2] == 'test'
    assert len(res[3]) == 5
    assert len(res[4]) == 2
    assert res[4][0] == 'ansible'
    assert res[4][1] == 'ansible'
    assert res[5] == False
    assert res[6] == None

# Generated at 2022-06-13 07:33:32.273521
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_password = 'this is a vault password'
    vault_secrets = [vault_password]
    yaml_data = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          3438393864303537623534366236630a333665666233326632623765336666343965326133313336\n          3265333465653835346663613633626563616561386334610a303835393437656262633631373636\n          39353633353466383463653038333339373331336135613134383263363936373564633662396165\n          3966363339326264\n          '

# Generated at 2022-06-13 07:33:44.136965
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Create an instance of AnsibleConstructor
    ansible_constructor = AnsibleConstructor()

    string_key_dict = {'key': 'value'}

    # Construct mapping
    mapping = ansible_constructor.construct_mapping(string_key_dict)

    # Assert that the mapping is an instance of AnsibleMapping
    assert isinstance(mapping, AnsibleMapping)

    # Assert that the mapping size is equal to 1
    assert len(mapping) == 1

    # Assert that the mapping contains {'key': 'value'}
    assert mapping['key'] == 'value'

    # Assert that both keys (which are 'key') are mapped to the same value (which is 'value')
    assert mapping.get('key') == mapping.get('key')

    # Assert that the first key ('key

# Generated at 2022-06-13 07:33:49.549959
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ansible_constructor = AnsibleConstructor(file_name=None, vault_secrets=None)
    value = 'Hello'
    mock_node = MagicMock()
    mock_node.id = 'scalar'
    mock_node.start_mark = 'mark'
    mock_node.tag = 'tag:yaml.org,2002:str'
    mock_node.value = 'Hello'
    mock_node.end_mark = 'mark'
    mock_node.anchor = None
    mock_node.__repr__ = MagicMock(return_value='repr')
    mock_node.__deepcopy__ = MagicMock(return_value='deepcopy')
    mock_node.__dict__ = {}
    result = ansible_constructor.construct_yaml_str(mock_node)

# Generated at 2022-06-13 07:34:00.038304
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Test if a AnsibleMapping object is returned
    assert isinstance(AnsibleConstructor.construct_yaml_map(AnsibleConstructor()), AnsibleMapping)
    assert isinstance(AnsibleConstructor.construct_yaml_map(AnsibleConstructor()), AnsibleMapping)

    # Test if an ConstructorError is raised when something different from a MappingNode is passed
    import yaml
    from yaml.nodes import ScalarNode
    mynode = ScalarNode(tag='tag:yaml.org,2002:str', value='hello')
    try:
        AnsibleConstructor.construct_yaml_map(AnsibleConstructor(), mynode)
    except yaml.constructor.ConstructorError as e:
        assert e

# Generated at 2022-06-13 07:34:14.733195
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml

    data = """encrypted: !vault $ANSIBLE_VAULT;1.1;AES256
    616263313233343536373839303132333435363738393031323334353637383930
    313233343536373839303132333435363738393031323334353637383930313233
    3435363738393031323334353637383930
    """

# Generated at 2022-06-13 07:34:24.120777
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """Ensure that duplicate keys always result in a warning"""
    # data without duplicate keys
    data = AnsibleConstructor(file_name='test_file').construct_mapping(
        yaml.nodes.MappingNode(u'tag:yaml.org,2002:map',
                               [yaml.nodes.Node(u'tag:yaml.org,2002:str', 'a', (0,0), (0,0), None ),
                                yaml.nodes.Node(u'tag:yaml.org,2002:int', '1', (0,0), (0,0), None)]
                               )
    )
    assert 'a' in data and data['a'] == 1, \
        "The data without duplicate keys should be a dictionary in which key 'a' is mapped to int 1"

    # data with

# Generated at 2022-06-13 07:34:33.982280
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.unsafe_proxy import wrap_var

    input_yaml = u"- test1: test2\n- test3: test4"
    loaded_data = AnsibleLoader(input_yaml).get_single_data()
    assert len(loaded_data) == 2
    assert loaded_data[0].ansible_pos == (u'<unicode string>', 1, 0)
    assert loaded_data[1].ansible_pos == (u'<unicode string>', 2, 0)
    assert loaded_data[0][u"test1"] == u"test2"
    assert loaded_data[1][u"test3"] == u"test4"


# Generated at 2022-06-13 07:34:56.537421
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnicode
    AnsibleConstructor.add_constructor(u'tag:yaml.org,2002:str', AnsibleConstructor.construct_yaml_str)
    yaml_str = yaml.load(to_bytes('foo: bar', nonstring='simplerepr'))
    assert yaml_str['foo'] == AnsibleUnicode('bar')

# Generated at 2022-06-13 07:35:02.377340
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    class Runner:
        pass

    runner = Runner()
    runner.vault_ids = []
    runner.vault_password = None
    runner.ask_vault_pass = lambda x: u'vault_pass'
    runner.load_vault_file= lambda x: None
    runner.unlock_vault = lambda x: None
    runner.setup_vault = lambda x: None
    runner.no_log = lambda x: None

    class Base:
        pass

    from ansible.parsing.dataloader import DataLoader

    class Play:
        def __init__(self):
            self.basedir = '.'
            self.vars = {}
            self.tags = {}
            self.vars_prompt = {}
            self.password_prompts = {}
            self.basedir

# Generated at 2022-06-13 07:35:10.922700
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from io import StringIO
    # Test case 1: duplicate dict key
    stream = StringIO(u"foo:\n  bar: 1\n  bar: 2")
    yaml = YAML(typ='safe')
    yaml.constructor = AnsibleConstructor
    data = yaml.load(stream)
    assert data == {'foo': {'bar': 2}}

    # Test case 2: !unsafe
    stream = StringIO(u"!unsafe {'x':1}")
    yaml = YAML(typ='safe')
    yaml.constructor = AnsibleConstructor
    data = yaml.load(stream)
    assert isinstance(data, wrap_var)


# Generated at 2022-06-13 07:35:18.900953
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os

    def fake_vault_get_unseal_data(self, vault_secrets):
        return True

    vault_secrets = [u'foo', u'bar']
    vault_secrets_1 = [u'baz', u'qux']

    vault_lib = VaultLib()
    vault_lib.get_unseal_data = fake_vault_get_unseal_data

# Generated at 2022-06-13 07:35:23.157936
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    mapping = AnsibleConstructor.construct_mapping(None)
    assert isinstance(mapping, AnsibleMapping)
    assert mapping.ansible_pos == (None, None, None)

# Generated at 2022-06-13 07:35:24.990256
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor("/path/to/file")
    node = MappingNode()
    node.tag = b"!vault-encrypted"
    ret = ansible_constructor.construct_vault_encrypted_unicode(node)
    assert ret == ""

# Generated at 2022-06-13 07:35:32.405200
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader

    vault_lib = VaultLib(secrets=["password"])

# Generated at 2022-06-13 07:35:39.784415
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    ansible_constructor = AnsibleConstructor()

    # Load a vault encrypted string

# Generated at 2022-06-13 07:35:50.925975
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    from ansible.module_utils.six import PY3

    # On Python3, gettext.find() returns a function that requires a positional
    # argument.  On Python2, it returns a string.
    if PY3:
        expected_gettext_output = "<function gettext at 0x{:x}>(arg)".format(hash(gettext))
    else:
        expected_gettext_output = "gettext(arg)"

    # Test that !unsafe tag returns a AnsibleUnsafeText object

# Generated at 2022-06-13 07:35:55.433602
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    '''
    This is a unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor.
    '''
    ac = AnsibleConstructor()
    v = VaultLib(secrets=['secret1', 'secret2'])
    test_data = '$ANSIBLE_VAULT;1.1;AES256\n313364343361346139613236633635326564306235326531636432353233696431633762313166\n623561376131623337623831343162653135666438633863373865633230653666386362666361\n6664303162323730343132623563386166323331636535643466363365\n'
    node = v.decrypt(test_data)

# Generated at 2022-06-13 07:36:18.598509
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    if sys.version_info[0] >= 3:
        if sys.version_info[1] >= 2:
            assert '_io.TextIOWrapper' in str(AnsibleConstructor.construct_yaml_unsafe("!unsafe '_io.TextIOWrapper'"))
        else:
            assert '_io.BytesIO' in str(AnsibleConstructor.construct_yaml_unsafe("!unsafe '_io.BytesIO'"))

# Generated at 2022-06-13 07:36:26.784984
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_data_str = '''\
key1: value1
key2: value2
'''
    yaml_data = yaml.load(yaml_data_str, Loader=AnsibleConstructor)
    assert yaml_data == {'key1': 'value1', 'key2': 'value2'}
    #  Check if a different type is returned
    assert type(yaml_data) == AnsibleMapping
    # Now test the duplicate key detection
    yaml_data_str = '''\
key1: value1
key2: value2
key2: value3
'''

# Generated at 2022-06-13 07:36:32.609056
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Running this module as a script for testing purposes
    # Test the constructor of class AnsibleConstructor
    yaml_str = '--- \n- "{{ ansible_all_ipv4_addresses }}"\n'
    ans_construct = AnsibleConstructor()
    data = ans_construct.construct_yaml_str(yaml_str)
    assert data == AnsibleUnicode('{{ ansible_all_ipv4_addresses }}')

# Generated at 2022-06-13 07:36:35.897143
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

    data = u'{"key1": 1, "key2": 2, "key1": 3}'
    conf = yaml.load(data, Loader=AnsibleConstructor)
    assert conf == {u'key1': 3, u'key2': 2}

# Generated at 2022-06-13 07:36:46.907063
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    assert AnsibleConstructor(file_name=None).construct_yaml_str(yaml.nodes.ScalarNode(u'tag:yaml.org,2002:str', to_bytes('te\u00adst'))).encode() == 'test'
    assert AnsibleConstructor(file_name=None).construct_yaml_str(yaml.nodes.ScalarNode(u'tag:yaml.org,2002:str', to_bytes('te\xadst'))).encode() == 'te\xadst'

# Generated at 2022-06-13 07:36:49.685875
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    result = AnsibleConstructor().construct_mapping(MappingNode(tag=u'tag:yaml.org,2002:map',
                                                                value=[(u'a', 1), (u'b', 2)],
                                                                flow_style=False))
    assert result == {u'a': 1, u'b': 2}
    assert result.ansible_pos == (u'<string>', 1, 1)

# Generated at 2022-06-13 07:36:59.567755
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None)  # file_name=None, vault_secrets=None
    constructor = loader.constructor


# Generated at 2022-06-13 07:37:11.332026
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import os
    import yaml

    output = ''
    try:
        output = yaml.load(os.linesep.join(["---",
                                            "a:",
                                            "  b:",
                                            "    c: >",
                                            "      Ansible is a radically simple IT automation",
                                            "      engine that automates cloud provisioning, ",
                                            "      configuration management, application ",
                                            "      deployment, intra-service orchestration, ",
                                            "      and many other IT needs."]),
                           Loader=AnsibleConstructor)
    except yaml.YAMLError as exc:
        print(exc)
    

# Generated at 2022-06-13 07:37:19.164557
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    from yaml.composer import Composer
    from yaml.constructor import Constructor
    from yaml.parser import Parser
    from yaml.reader import Reader
    from yaml.resolver import Resolver
    from io import BytesIO

    class MyConstructor(Constructor):
        def construct_yaml_map(self, node):
            return {'custom': 'value'}

    stream = BytesIO(b'--- {}\n---\n{}\n')

    Reader.NON_PRINTABLE = ''.join(chr(x) for x in range(0x0, 0x20))

    resolver = Resolver()
    reader = Reader(stream, None, None, None, resolver)

# Generated at 2022-06-13 07:37:23.307449
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ansible_constructor = AnsibleConstructor()
    yaml_node = None
    assert isinstance(ansible_constructor.construct_yaml_str(yaml_node), AnsibleUnicode)
