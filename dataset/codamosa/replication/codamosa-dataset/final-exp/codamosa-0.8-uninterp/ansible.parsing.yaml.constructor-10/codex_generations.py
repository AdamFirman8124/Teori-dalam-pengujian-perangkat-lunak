

# Generated at 2022-06-13 07:28:13.479524
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import sys
    import yaml

    if sys.version_info < (2, 7):
        # dict() is not guaranteed to preserve insertion order before Python 2.7
        raise SkipTest()

    yaml_str = u'''
    key1: val1
    key2: val2
    '''
    ansible_constructor = AnsibleConstructor()
    data = yaml.load(yaml_str, Loader=yaml.loader.BaseLoader)
    assert isinstance(data, AnsibleMapping)
    assert list(data.keys()) == [u'key1', u'key2']
    # Check we get back the right type of objects
    data[u'key1'] = u'one'
    data[u'key2'] = u'two'

# Generated at 2022-06-13 07:28:16.582066
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    result = AnsibleConstructor().construct_mapping(MappingNode(None, None, block=True), deep=False)

    # Check number of results
    assert len(result) == 0


# Generated at 2022-06-13 07:28:26.870920
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    data = """
name: Gump
species: dog
owner: Forrest
"""

    data2 = """
name: Gump
species: dog
owner: Forrest
"""
    yaml_data = yaml.load(data, Loader=AnsibleLoader)
    yaml_data2 = yaml.load(data2, Loader=AnsibleLoader)
    assert(data == data2)
    assert(yaml_data == yaml_data2)
    assert(yaml_data['name'] == yaml_data2['name'])
    assert(yaml_data['species'] == yaml_data2['species'])
    assert(yaml_data['owner'] == yaml_data2['owner'])


# Generated at 2022-06-13 07:28:34.247797
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Empty yaml seq
    test_input = '[]'
    data = yaml.load(test_input, Loader=AnsibleConstructor)
    assert data == []

    # Test yaml seq with elements
    test_input = '[1, 2]'
    data = yaml.load(test_input, Loader=AnsibleConstructor)
    assert data == [1, 2]

    # Test yaml seq of maps
    test_input = '- host: localhost\n  name: test_foo'
    data = yaml.load(test_input, Loader=AnsibleConstructor)
    assert data == [{'host': 'localhost', 'name': 'test_foo'}]

# Generated at 2022-06-13 07:28:41.668755
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_dict = """
a: 1
b:
  c: 3
  d: 4
"""
    # test for duplicate key
    yaml_dict_dup = """
a: 1
b: 1
a: 2
"""
    # test for duplicate key 'error'
    yaml_dict_dup_error = """
a: 1
a: 2
"""
    yaml_unicode = """
a: 1
b:
  c: 3
  d: 4
"""
    yaml_nodict = """
"a": 1
"b:
  c: 3
  d: 4
"""
    yaml_nodict_sub = """
- a: 1
- b: 2
- c:
  - 3
  - 4
  - 5
  - 6
"""
    yaml_

# Generated at 2022-06-13 07:28:42.980800
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass


# Generated at 2022-06-13 07:28:56.766804
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    # Mock class for node
    class MockNode():
        """A mocked class to use in place of yaml.nodes.Node"""
        def __init__(self):
            self.value = [(1), (2), (3)]
            self.id = 'seq'
            self.start_mark = None

    # Mock class for sequence
    class MockSequence():
        """A mocked class to use in place of yaml.sequence.Sequence"""
        def __init__(self):
            self.extend = [1, 2, 3]

    # construct_yaml_seq() is a generator; call list() on it so that we can
    # make assertions against it
    rval = list(AnsibleConstructor.construct_yaml_seq(MockNode()))

# Generated at 2022-06-13 07:29:05.431886
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    test_data = """
a: "{{x}}"
b: "{{ y}}"
c: "{{z}}"
"""
    node = yaml.load(test_data, Loader=AnsibleConstructor)

    assert node.get('a') == wrap_var("{{x}}")
    assert node.get('b') == wrap_var("{{ y}}")
    assert node.get('c') == wrap_var("{{z}}")


# Generated at 2022-06-13 07:29:15.863500
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    """
    Unit test for method construct_yaml_seq of class AnsibleConstructor
    """
    import sys
    import yaml
    import os

    data = '''
- a:
  - b:
      name: "xx"
'''
    file_name = os.path.dirname(sys.argv[0])
    ac = AnsibleConstructor()
    content = yaml.load(data, Loader=AnsibleConstructor)
    assert type(content) == list
    assert content[0]['a'][0]['b']['name'] == u"xx"

# Generated at 2022-06-13 07:29:22.207437
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = u'''\
a: 1
b: 2
c: 3
'''
    node = yaml.compose(data)
    ac = AnsibleConstructor()
    mapping = ac.construct_mapping(node)
    assert isinstance(mapping, dict)
    assert mapping['a'] == 1
    assert mapping['b'] == 2
    assert mapping['c'] == 3



# Generated at 2022-06-13 07:29:33.959330
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml_str= '''
    - foo: some_new_string
    '''
    data = AnsibleLoader(yaml_str).get_single_data()

    assert isinstance(data[0].get('foo',None), AnsibleUnicode) is True
    assert data[0].get('foo',None) == u'some_new_string'

# Generated at 2022-06-13 07:29:37.325289
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode(None, None, [123, 456])
    ac = AnsibleConstructor()
    result = ac.construct_mapping(node)
    assert result == {123: 456}



# Generated at 2022-06-13 07:29:43.020784
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml

    expected = AnsibleMapping()
    expected.ansible_pos = ('<string>', 1, 1)

    test_data = """
---
first_item: value1
second_item: value2
"""

    yaml_object = yaml.load(test_data, Loader=AnsibleConstructor)

    assert isinstance(yaml_object, AnsibleMapping)
    assert yaml_object == expected


__all__ = ['AnsibleConstructor']

# Generated at 2022-06-13 07:29:50.873183
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    import yaml

    # no password on the vault
    vault_secret = []
    vault = VaultLib(secrets=vault_secret)
    encoded_data = vault.encrypt(b"test")
    # this is the string that would be loaded from YAML

# Generated at 2022-06-13 07:29:53.640881
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Get an instance of the class
    c = AnsibleConstructor()
    # Construct the mapping
    m = c.construct_mapping({'a': 1, 'b': 2, 'c': 3})
    # Check that a is 1 and that c is 3
    assert m['a'] == 1
    assert m['c'] == 3

# Generated at 2022-06-13 07:29:58.256487
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secret1 = '$ANSIBLE_VAULT;1.1;AES256'
    vault_secret2 = '39dD8gvRndtT1TtX9On+kA=='
    node = MappingNode(None, None, None, True, None)
    node.start_mark.line = 1
    node.start_mark.column = 3
    node.start_mark.name = 'data1.yml'
    x = AnsibleConstructor(vault_secrets=[vault_secret1, vault_secret2]).construct_vault_encrypted_unicode(node)
    assert isinstance(x, AnsibleVaultEncryptedUnicode)
    assert not x.vault.secrets
    x.vault.secrets = [vault_secret1, vault_secret2]
   

# Generated at 2022-06-13 07:30:08.256111
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.resolver import Resolver
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    yaml = '''
    !unsafe "a string"
    !unsafe [1, 2]
    !unsafe {a: b}
    '''

    parser = Parser(yaml)
    composer = Composer(parser, Resolver())

    aconstructor = AnsibleConstructor()
    assert isinstance(aconstructor.construct_document(composer.get_node()), AnsibleUnsafeText)
    assert isinstance(aconstructor.construct_document(composer.get_node()), AnsibleUnsafeText)

# Generated at 2022-06-13 07:30:16.674408
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    """Test construct_mapping of class AnsibleConstructor"""
    # If keys are different, just construct a AnsibleMapping object
    mapping_node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[(
        AnsibleConstructor.construct_yaml_str('test1'), AnsibleConstructor.construct_yaml_str('test2'))])
    ac = AnsibleConstructor()
    mapping = ac.construct_mapping(mapping_node)
    assert isinstance(mapping, AnsibleMapping)

    # If keys are same, construct a AnsibleMapping object, take only the first one
    mapping_node

# Generated at 2022-06-13 07:30:20.510608
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    fixture = '''
- 1
- 2
- 3
- 4
'''

    import yaml
    imp_yaml = yaml.load(fixture)

    # get instance of AnsibleConstructor
    obj = AnsibleConstructor()

    # get nodes data
    nodes = yaml.compose(fixture)

    # call the method we want to test.
    data = obj.construct_yaml_seq(nodes)

    assert next(data) == imp_yaml

# Generated at 2022-06-13 07:30:24.945577
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from yaml.nodes import MappingNode
    instance = AnsibleConstructor(file_name='test_file_name', vault_secrets=['test_vault_secret'])
    assert isinstance(instance, AnsibleConstructor)
    assert isinstance(instance.construct_mapping(MappingNode('tag:yaml.org,2002:map', 'value')), AnsibleMapping)

# Generated at 2022-06-13 07:30:48.576857
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    f = open('./test/ansible_constructor.yaml')
    data = AnsibleConstructor.construct_yaml_map(AnsibleConstructor, f)
    print(data)

# Generated at 2022-06-13 07:30:58.779732
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_data = u' - a\n - b\n - c'
    ansible_constructor = AnsibleConstructor()
    ansible_loader = AnsibleLoader(yaml_data, None, None, None, None, ansible_constructor)
    list_data = list(ansible_loader.get_single_data())
    data_1 = AnsibleUnicode(u'a')
    data_2 = AnsibleUnicode(u'b')
    data_3 = AnsibleUnicode(u'c')
    assert list_data == [data_1, data_2, data_3]
    assert data_1.ansible_pos == (None, 1, 2)

# Generated at 2022-06-13 07:31:06.793315
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import ansible.parsing.yaml.loader
    import yaml

    data = b"---\n!unsafe foo\nbar\n"

    ac = AnsibleConstructor()
    yaml.Reader.NON_PRINTABLE = yaml.reader.Reader.NON_PRINTABLE = set(i for i in range(256) if chr(i) not in yaml.reader.Reader.PRINTABLE)

    # Call the private _create_composer method of the AnsibleYamlFile constructor
    # to create an '_AnsibleComposer' object. Calling this method is necessary
    # to prevent the AnsibleYamlFile constructor from attempting to read the
    # file from disk.
    pyyaml_loader = ansible.parsing.yaml.loader.AnsibleYamlFile(None)

# Generated at 2022-06-13 07:31:18.422395
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # This test uses a (deprecated) ciphertext from test_vault.py, which uses the same code to encrypt and decrypt data
    vault_secrets = [u'vault_secret1']
    vault = VaultLib(secrets=vault_secrets)
    encrypted_string = u'$ANSIBLE_VAULT;1.1;AES256;test_key;test_iv;test_hmac;539ef0b2575be7d3d3a24c7a2066b72c;7a8d067c0f735e88a6f1cf6b9bcb727ee'
    constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    ansible_vault_encrypted_unicode = constructor.construct_vault_encrypted_unicode(encrypted_string)


# Generated at 2022-06-13 07:31:23.271174
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    """This is not a real unit test because it requires pyyaml to be installed.
    It is meant to be run manually to check unicode handling of AnsibleConstructor.construct_yaml_str"""
    import yaml
    a_str = u"\u00E9"
    data = yaml.load(a_str, Loader=AnsibleConstructor)
    assert type(data) is AnsibleUnicode
    # Check that it is really a unicode object
    assert data == a_str
    # Check that we can convert it to ascii without error
    ascii_str = str(data)

# Generated at 2022-06-13 07:31:26.645802
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    constructor = AnsibleConstructor()

    # Normal dict
    data = constructor.construct_mapping(MappingNode(u'tag:yaml.org,2002:python/dict', []))
    assert data == {}

    # Duplicate dict key (for test)
    data = constructor.construct_mapping(MappingNode(u'tag:yaml.org,2002:python/dict', [(u'key', u'value'),(u'key', u'value2')]))
    assert data == {u'key': u'value2'}



# Generated at 2022-06-13 07:31:36.032816
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    from ansible.module_utils._text import to_native
    from ansible.module_utils import basic
    from six import StringIO
    from ansible.parsing.vault import VaultLib

    basic._ANSIBLE_ARGS = None

    # generate some data that would have unicode in it
    data = {u'f\xf6\xf6': u'bar'}

    # dump the data to a string
    dump = yaml.safe_dump(data, encoding='utf-8', allow_unicode=True)

    # load using our custom Loader
    class TestLoader(yaml.SafeLoader):
        def __init__(self, stream):
            super(TestLoader, self).__init__(stream)

# Generated at 2022-06-13 07:31:46.354838
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import six

    class DummyConstructor(object):

        def construct_scalar(self, node):
            return node.tag.split('!')[1]

    # Create a dummy constructor
    dummy_constructor = DummyConstructor()

    # Create a fake node object
    class DummyNode(object):
        tag = u'!vault_encrypted'

    # Create a fake yaml file which contains encrypted contents
    class DummyYamlFile(object):
        def __init__(self, contents):
            self.contents = contents
            self.pointer = 0

        def read(self, bytes=-1):
            if self.pointer == len(self.contents):
                return ''
            self.pointer += 1
            return self.contents[self.pointer - 1]

    # Create a fake object

# Generated at 2022-06-13 07:31:50.991211
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    con = AnsibleConstructor()
    assert con.construct_yaml_map({u'a': 1, u'b': 2}) == {u'a': 1, u'b': 2}


# Generated at 2022-06-13 07:32:05.849480
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secret = "my_vault_secret"
    vault_password_file = "/tmp/vault_password_file"
    import os
    open(vault_password_file, 'w').close()
    os.system("echo %s > %s" %(vault_secret, vault_password_file))
    vault_secrets = [vault_password_file]
    c = AnsibleConstructor(vault_secrets=vault_secrets)
    c._vaults['default'] = VaultLib(secrets=vault_secrets)

# Generated at 2022-06-13 07:32:32.276751
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    seq_value = ['hello', 'world', '!']
    yaml_seq = u'tag:yaml.org,2002:seq'
    yaml_node = MappingNode(yaml_seq, seq_value)
    ansible_constructor = AnsibleConstructor()
    constructed_yaml_node_iterator = ansible_constructor.construct_yaml_seq(yaml_node)
    assert constructed_yaml_node_iterator is not None
    constructed_yaml_node = next(constructed_yaml_node_iterator)

    assert(constructed_yaml_node == seq_value)


# Generated at 2022-06-13 07:32:42.294734
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/vault/vault.yml')
    secrets = [ 'secret' ]
    constructor = AnsibleConstructor(file_name=filename, vault_secrets=secrets)
    # Add the vault_secret to the vault_secrets of the constructor
    # Use yaml.load to use AnsibleConstructor.construct_vault_encrypted_unicode()
    # and return an AnsibleVaultEncryptedUnicode object.

# Generated at 2022-06-13 07:32:48.752265
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    abc = b'abc'
    data = b'\x00\x01\x02'
    yaml_str = u'{abc: \x00\x01\x02}'
    yaml_str = to_bytes(yaml_str, encoding='utf-8')
    result = AnsibleConstructor().construct_mapping(yaml.compose(yaml_str), deep=True)
    result = dict(result)
    abc_from_result = result[abc]
    assert abc_from_result == data

# Generated at 2022-06-13 07:32:53.961455
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    v = VaultLib()
    v.secrets = ['vault1']
    v.secrets_filename = 'test/vault1.secrets'
    v.encrypt_string('testcontent')

# Generated at 2022-06-13 07:32:58.596922
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    dict_node = MappingNode(tag="tag:yaml.org,2002:map", value=[])
    dict_node.start_mark = 1
    dict_node.end_mark = 4

    ansible_constructor = AnsibleConstructor()

    ansible_map = ansible_constructor.construct_yaml_map(dict_node).next()

    assert ansible_map['ansible_pos'] == ('<string>', 1, 1)


# Generated at 2022-06-13 07:33:01.339165
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    b_data = b'{"test": "hello", "test": "world"}'
    data = yaml.load(b_data, Loader=AnsibleConstructor)
    assert data == {b'test': b'world'}



# Generated at 2022-06-13 07:33:10.649016
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys
    import io
    import yaml
    class fake_file_name(io.StringIO):
        def __init__(self):
            self.value = 'my_fake_file.yaml'
            self.pos = 0
            self.len = len(self.value)
        def read(self, n):
            self.pos += n
            return self.value[self.pos - n:self.pos]
        def seek(self, offset, whence=sys.stdin.seek.__defaults__[1]):
            if whence == 0:
                self.pos = offset
            elif whence == 1:
                self.pos += offset
            elif whence == 2:
                self.pos = self.len - offset
            else:
                raise Exception("Unexpected value of whence parameter")

# Generated at 2022-06-13 07:33:24.899080
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os

    text = '!vault |\n'\
           '          $ANSIBLE_VAULT;1.2;AES256;test_host\n'\
           '          63393737303633326536353365316230633263353431626138633531366239333765636130383230\n'\
           '          31383839333065643539613663340a66636237623763323932616337646530646336633939646630\n'\
           '          3964663263396339303864343730383034353763373334643038326561620a\n'
    filename = '/tmp/vault_test.yml'

    # Write the file

# Generated at 2022-06-13 07:33:33.850854
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import unittest
    import sys
    import yaml
    from ansible.module_utils.six import PY3
    class ConstructYamlUnsafeTestCase(unittest.TestCase):
        def setUp(self):
            self.constructor = AnsibleConstructor()
            self.yaml_seq = u'[1, 2, 3]'
            self.yaml_dict = u'{a: 1, b: 2}'
            self.yaml_int = u'3'

        def test_seq(self):
            yaml_str = yaml.dump(self.yaml_seq)
            result = yaml.load(yaml_str, Loader=yaml.Loader)
            self.assertEqual(type(result), AnsibleSequence)

        def test_dict(self):
            yaml

# Generated at 2022-06-13 07:33:40.676042
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    construct_yaml_str = AnsibleConstructor.construct_yaml_str
    AnsibleConstructor.construct_yaml_str = lambda self, node: self.construct_scalar(node)

    class AnsibleConstructor_test_construct_yaml_unsafe(AnsibleConstructor):
        def construct_python_str(self, node):
            return self.construct_scalar(node)

    original_construct_yaml_unsafe = AnsibleConstructor_test_construct_yaml_unsafe.construct_yaml_unsafe
    AnsibleConstructor_test_construct_yaml_unsafe.construct_yaml_unsafe = lambda self, node: original_construct_yaml_unsafe(node)

    acu = AnsibleConstructor_test_construct_yaml_unsafe()
    m = ac

# Generated at 2022-06-13 07:34:26.082978
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import pytest
    import os
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    auc = AnsibleConstructor()
    with tempfile.NamedTemporaryFile(delete=False, mode="w+") as fd:
        fd.write("\n".join([
            "---",
            "- hosts: localhost",
            "  tasks:",
            "  - name: Test",
            "    command: echo test",
        ]))
    test_path = fd.name
    with pytest.raises(ConstructorError) as exc:
        with open(test_path) as fd:
            auc.construct_mapping(fd.read())
    assert exc.value

# Generated at 2022-06-13 07:34:35.610511
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml import objects
    import sys
    import types
    import yaml

    class MyConstructor(AnsibleConstructor, yaml.SafeLoader):
        pass

    with open(sys.modules[objects.__module__].__file__) as fh:
        objects_yaml = fh.read()

    loader = MyConstructor(file_name=sys.modules[objects.__module__].__file__)
    loader.vault_secrets = ['foo']
    objects_python = loader.get_single_data(objects_yaml)

    for name, obj in objects_python.items():
        assert(isinstance(obj, type(getattr(objects, name, None))))

# Generated at 2022-06-13 07:34:41.730686
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """
    Test that AnsibleConstructor.construct_yaml_map warns users of
    duplicated keys. By default, the value of DUPLICATE_YAML_DICT_KEY
    is set to 'ignore'. This test ensures that the default behavior is
    preserved.

    """
    from yaml.nodes import MappingNode
    from yaml.parser import ParserError
    from yaml import load

    # Create a
    # key: value
    # key: value
    # mapping node

# Generated at 2022-06-13 07:34:49.745404
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault = VaultLib()
    vault.secrets = ['password']

    # test variable that is not vault encrypted
    node_value = 'this is the value of node'
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.vault_secrets = ['password']
    ansible_constructor._vaults['default'] = vault

    ansible_constructor._ansible_file_name = 'test/name'
    result = ansible_constructor.construct_vault_encrypted_unicode(node_value)
    assert result == 'this is the value of node'

    # test variable that is vault encrypted

# Generated at 2022-06-13 07:34:58.259788
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    # Test case 1
    node = u'\r\n    !unsafe\r\n    123\r\n'
    ac = AnsibleConstructor()
    value = ac.construct_yaml_unsafe(node)
    assert isinstance(value, AnsibleUnsafeText)
    assert value == u'123\r\n'
    # Test case 2
    node = u'\r\n    !unsafe\r\n    123'
    ac = AnsibleConstructor()
    value = ac.construct_yaml_unsafe(node)
    assert isinstance(value, AnsibleUnsafeText)
    assert value == u'123'

# Generated at 2022-06-13 07:35:03.436385
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    """
    Test to verify that when !unsafe is encountered, we wrap the following string as a variable

    >>> s = AnsibleConstructor('').construct_yaml_unsafe(None)
    >>> print(s)
    AnsibleUnsafeText(u'')
    """

# Generated at 2022-06-13 07:35:04.067895
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    pass

# Generated at 2022-06-13 07:35:11.221301
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Create AnsibleConstructor object
    ac = AnsibleConstructor(file_name=None, vault_secrets=None)
    # Get a node object
    node_obj = ac.construct_yaml_str('test')
    # Test actual functionality
    output = ac.construct_vault_encrypted_unicode(node_obj)
    assert isinstance(output, AnsibleVaultEncryptedUnicode)
    assert output.ansible_pos == ('<unicode>', 1, 1)
    assert output.vault == ac._vaults['default']
    assert output.b_ciphertext_data == b'test'

# Generated at 2022-06-13 07:35:23.477681
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    class TestConstructor(AnsibleConstructor):
        def __init__(self, file_name=None, vault_secrets=None):
            super(TestConstructor, self).__init__(file_name=file_name, vault_secrets=vault_secrets)
            self.data = None

        def construct_yaml_map(self, node):
            data = super(TestConstructor, self).construct_yaml_map(node)
            self.data = data
            return data # return the generator to be iterated for test

    # test simple map (dict)
    yaml_str = '''\
key: value
'''
    doc = yaml.load(yaml_str, Loader=TestConstructor)
    assert isinstance(doc, AnsibleMapping)
    assert doc.ansible_pos

# Generated at 2022-06-13 07:35:27.990885
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    constructor = AnsibleConstructor()
    node = None
    value = constructor.construct_yaml_str(node)
    assert isinstance(value, AnsibleUnicode), "Returned value is not of type AnsibleUnicode"

# Generated at 2022-06-13 07:36:48.816413
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    yaml_str = u"\n- !include include_test.yml"
    # ERROR:
    # Traceback (most recent call last):
    #   ...
    #   File "/usr/local/Cellar/python/2.7.6/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ansible/parsing/yaml/loader.py", line 44, in __init__
    #     SafeConstructor.__init__(self)
    #   File "/usr/local/Cellar/python/2.7.6/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/yaml/constructor.py", line 71, in __init__
    #     yaml.constructor.BaseConstructor.__

# Generated at 2022-06-13 07:36:50.315234
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    a = AnsibleConstructor()
    print(a.construct_sequence('hello world'))

# Generated at 2022-06-13 07:37:04.995939
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafe
    from ansible.utils.unsafe_proxy import wrap_var
    from file_diffs import assert_pyyaml_roundtrip
    from ansible.parsing.yaml.loader import AnsibleLoader

    c = AnsibleConstructor(file_name='/foo/bar')
    node = c.construct_yaml_unsafe('foo')
    assert isinstance(node, AnsibleUnsafe)
    assert_pyyaml_roundtrip(wrap_var(node))

    # yaml.safe_load / yaml.safe_dump calls the full_load / full_dump
    # methods of the constructor / representer to handle custom types,
    # and the full_load method of the constructor is construct_object
    # which is construct_yaml_uns

# Generated at 2022-06-13 07:37:05.631945
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:37:13.937638
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Test case 1:
    # [in] node.value = [key_node, value_node]
    # [in] node.key_node.value = 'key1'
    # [in] node.value_node.value = 'value1'
    # [out] ret = {'key1': 'value1'}
    key_node = MappingNode('', 'tag:yaml.org,2002:str', 'key1', 'key1')
    value_node = MappingNode('', 'tag:yaml.org,2002:str', 'value1', 'value1')
    node = MappingNode(value=[key_node, value_node])
    ret = AnsibleConstructor.construct_mapping(AnsibleConstructor, node)
    assert ret == {'key1': 'value1'}

    #

# Generated at 2022-06-13 07:37:20.635574
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = '''
a: b
c: d
c: e
'''
    try:
        yaml.load(data, Loader=AnsibleConstructor)
        assert False, "Expected a ConstructorError exception to be raised but was not."
    except ConstructorError as e:
        assert isinstance(e, ConstructorError), "Expected a ConstructorError exception to be raised but encountered %s instead." % type(e)
        assert str(e) == 'while constructing a mapping', 'Expected a ConstructorError to be raised with problem "while constructing a mapping" but encountered problem: "' + str(e) + '"'
        assert e.problem == 'while constructing a mapping', 'Expected a ConstructorError to be raised with problem "while constructing a mapping" but encountered problem: "' + e.problem + '"'


# Generated at 2022-06-13 07:37:26.459689
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    value = '42'
    node = object()
    assert value == AnsibleConstructor.construct_yaml_unsafe(None, node)
    assert isinstance(value, AnsibleUnsafeText)



# Generated at 2022-06-13 07:37:32.253696
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test variations of literal style
    data = [
        u'',
        u'a pretty string',
        u'another pretty string',
    ]
    for value in data:
        ac = AnsibleConstructor()
        ansible_str = ac.construct_yaml_str(value)
        assert isinstance(ansible_str, AnsibleUnicode)
        assert ansible_str == value

# Generated at 2022-06-13 07:37:39.649015
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import tempfile

    class UnitTestAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            super(UnitTestAnsibleConstructor, self).__init__()
            self.secret = 'mysecret'
            self._vaults['default'] = VaultLib(secrets=[self.secret])

        def construct_scalar(self, node):
            return node.value

        def construct_string(self, node):
            return node.value

    vault_secret = 'mysecret'
    cleartext_data = "hello world"

    # encrypt cleartext_data using vault_secret
    vault = VaultLib(secrets=[vault_secret])
    ciphertext = vault.encrypt(cleartext_data)

    # write ciphertext to temporary file
    ciphertext_file

# Generated at 2022-06-13 07:37:40.525320
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    return