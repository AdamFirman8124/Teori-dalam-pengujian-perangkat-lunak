

# Generated at 2022-06-13 07:28:14.545997
# Unit test for method construct_mapping of class AnsibleConstructor

# Generated at 2022-06-13 07:28:25.778972
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class TestVaultLib(object):
        secrets = None

    my_vault = TestVaultLib()

    class TestNode(object):
        def __init__(self, start_mark, id):
            self.start_mark = start_mark
            self.id = id

    class TestStartMark(object):
        def __init__(self, name='<string>', line=None, column=None):
            self.name = name
            self.line = line
            self.column = column

    class TestLoader(object):
        def __init__(self):
            self.construct_yaml_map = AnsibleConstructor.construct_yaml_map
            self.construct_vault_encrypted_unicode = AnsibleConstructor.construct_vault_encrypted_unicode

# Generated at 2022-06-13 07:28:31.287373
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_str = """
    foo: bar
    bar: baz"""
    yaml_map = AnsibleConstructor(file_name='dummy_file').construct_yaml_map(yaml.parser.Parser(yaml.scanner.Scanner(yaml_str)).get_single_node())
    assert isinstance(yaml_map, AnsibleMapping)
    assert yaml_map.ansible_pos == ('dummy_file', 1, 1)

# Generated at 2022-06-13 07:28:36.798353
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # yaml.parser.Parser.parse returns a list of only one mappings
    data = [
        (
            "{key: value}",
            'key'
        ),
        (
            "key: value",
            'key'
        ),
        (
            "? key : value\n: value",
            'key'
        ),
    ]

    for yaml_data, key in data:
        c = AnsibleConstructor()
        result = c.construct_yaml_map(yaml.parser.Parser(yaml_data).get_single_node())
        assert key in result


# Generated at 2022-06-13 07:28:41.858656
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    yaml_str = """
    data: 
     - 1
     - 2
     - 3
    """

    # parse YAML
    data = yaml.safe_load(yaml_str)

    # assert data["data"] is an instance of dict
    assert(isinstance(data["data"], dict))

    # assert data["data"] is an instance of AnsibleUnsafeText
    assert(isinstance(data["data"], list))

    # assert data["data"] is an instance of list
    assert(isinstance(data["data"], list))

# Generated at 2022-06-13 07:28:55.862766
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import types
    import ansible.parsing.yaml.loader

    # Create an AnsibleConstructor object
    obj_AnsibleConstructor = ansible.parsing.yaml.loader.AnsibleConstructor()

    # Create the data to pass to the AnsibleConstructor's method construct_yaml_unsafe
    # Create a mock of the class Node with attributes set to their required values.
    node = type('Node', (object,),
                {'id': None,
                 'start_mark': 'start_mark'})

    node.id = 'object'

    # Create an object of class object
    obj_object = object()

    # Create an object of class types.MethodType
    types.MethodType(
        # Create an object of class method
        object(),
        object(),
        object())

    # Call

# Generated at 2022-06-13 07:28:58.606673
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    text = "foo: !unsafe {'baz': 'BAZ!'}"
    data = AnsibleVaultLib.load(
        data=text,
        loader=AnsibleConstructor())

    assert data['foo']['baz'] == 'BAZ!'



# Generated at 2022-06-13 07:29:00.021789
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    ''' test_AnsibleConstructor_construct_yaml_map '''
    pass


# Generated at 2022-06-13 07:29:13.955193
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import collections

    from ansible.parsing.vault import VaultLib

    from ansible.parsing.yaml.constructor import AnsibleConstructor

    vault_secrets = [b'vault_secret1', b'vault_secret2']


# Generated at 2022-06-13 07:29:22.440578
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    a = [0, 1, 2, 3]
    yaml = u"""
- !unsafe 0
- !unsafe 1
- !unsafe 2
- !unsafe 3
"""
    import yaml
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.add_constructor(u'!unsafe', ansible_constructor.construct_yaml_unsafe)
    b = yaml.safe_load(yaml, Loader=yaml.SafeLoader)
    b = ansible_constructor.construct_yaml_seq(b)
    assert a == b

# Generated at 2022-06-13 07:29:35.553085
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    d = {}
    def fake_load_file(self, path):
        return(d)

    vault = VaultLib(vault_password_file='password')
    vault.load_file = fake_load_file
    ac = AnsibleConstructor(vault_secrets=[vault])
    ac._vaults['default'] = vault
    c = ac.construct_vault_encrypted_unicode
    assert c(None) == b'\x04\x00\x00\x00'



# Generated at 2022-06-13 07:29:44.560751
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.module_utils import basic

    # Test for basic object
    m = basic.AnsibleModule(argument_spec={})
    assert AnsibleConstructor().construct_yaml_unsafe(m) == wrap_var(m)

    # Test for list
    l = [1, '2', b'3']
    assert AnsibleConstructor().construct_yaml_unsafe(l) == wrap_var(l)

    # Test for tuple
    t = (1, '2', b'3')
    assert AnsibleConstructor().construct_yaml_unsafe(t) == wrap_var(t)

    # Test for dictionary
    d = {'1': 1, '2': '2', '3': b'3'}
    assert AnsibleConstructor().construct_yaml_unsafe(d) == wrap_

# Generated at 2022-06-13 07:29:49.351025
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    testFileName = 'ansible_constructor_test.yml'
    testYaml = u'[1, 2, 3]\n'
    loader = AnsibleLoader(testYaml, testFileName)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleSequence)
    print(data)
    assert len(data) == 3


# Generated at 2022-06-13 07:30:00.161325
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Test array
    node_in = dict(value=[
        ('key1', u'test1'),
        ('key2', u'test2'),
        ('key3', u'test3'),
        ('key1', u'test4')])
    ansible_const = AnsibleConstructor()
    node_out = ansible_const.construct_mapping(node_in)
    assert node_out == dict(key3=u'test3', key2=u'test2', key1=u'test4')
    # Test unicode array
    node_in = dict(value=[
        ('key1', u'\u4f60\u597d'),
        ('key2', u'\u4eca\u5929'),
        ('key3', u'\u5475\u5475')])
    ansible_

# Generated at 2022-06-13 07:30:09.808420
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    if not HAS_YAML:
        raise SkipTest("not yaml installed")

    class AnsibleConstructorTest(AnsibleConstructor):
        pass

    yaml_str = """
    first:
      key1: one
    second:
      key1: two
    """

    x = AnsibleConstructorTest()
    x = yaml.load(yaml_str, Loader=yaml.Loader)

    assert x['first']['key1'] == 'one'
    assert x['second']['key1'] == 'two'

    assert x.ansible_pos == ('<string>', 1, 0)

    assert x['first'].ansible_pos == ('<string>', 2, 2)
    assert x['second'].ansible_pos == ('<string>', 5, 2)

    #

# Generated at 2022-06-13 07:30:17.869316
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    import yaml

    # Create our vault lib's instance
    vault_secrets = ['A_SECRET_PASSWORD']
    vault_lib = VaultLib(vault_secrets)

    # Create the string that we want to test
    key_id = 'default'
    version = 1
    ciphertext = 'AES128'
    data = 'VALUE_TO_ENCRYPT'
    b_data_to_encrypt = to_bytes(data)
    b_ciphertext_data = vault_lib.encrypt(key_id, b_data_to_encrypt)
    string_to_test = '!vault |\n  %s\n' % b_ciphertext_data

    # Replicate the correct behavior of AnsibleConstructor
    ansible_constructor = Ansible

# Generated at 2022-06-13 07:30:26.957655
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from io import StringIO
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.utils.display import Display

    display = Display()
    input_file = StringIO(u"{ key: value }\n")
    vault = VaultLib(secrets=["vaultpassword"])
    vault_encrypted_data = vault.encrypt("vault-encrypted-data")
    vault_encrypted_data_encoded = vault_encrypted_data.encode("utf-8")

# Generated at 2022-06-13 07:30:33.275245
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import datetime
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    yaml_str = '!unsafe "datetime.datetime(1970, 1, 1, 0, 0)"'
    unsafe = yaml.load(yaml_str, Loader=vars_loader.VarsLoader)
    assert isinstance(unsafe, datetime.datetime)
    assert unsafe == datetime.datetime(1970, 1, 1, 0, 0)

    yaml_str = '!unsafe datetime.datetime(1970, 1, 1, 0, 0)'
    unsafe = yaml.load(yaml_str, Loader=vars_loader.VarsLoader)
    assert isinstance(unsafe, AnsibleUnsafeText)
   

# Generated at 2022-06-13 07:30:43.943444
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml.nodes import ScalarNode
    value = u"$ANSIBLE_VAULT;7.yml;AES256\n353130363931346533386538386261353236613135333162323832333939363835\n353130363931346533386538386261353236613135333162323832333939363835"
    node = ScalarNode(tag=u'!vault', value=value, start_mark=None, end_mark=None, style=None)
    value = AnsibleConstructor().construct_vault_encrypted_unicode(node)
    assert (value.vault == AnsibleConstructor()._vaults['default'])

# Generated at 2022-06-13 07:30:51.614438
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    class MockMappingNode:
        pass
    class MockVaultLib:
        def __init__(self, secrets=None):
            self.secrets = secrets
        def decrypt(self, str_value):
            return {'value': str_value}
    class MockAnsibleConstructor:
        def __init__(self, f, s=None):
            self._vaults = {'default': MockVaultLib(secrets=s)}
            self._ansible_file_name = f
        def construct_mapping(self, node):
            pass
        def construct_vault_encrypted_unicode(self, node):
            pass

    # TODO: figure out a way to test error conditions
    # (I couldn't get a node with id != mapping)
    # TODO: test the code that raises Construct

# Generated at 2022-06-13 07:31:05.507548
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.exceptions import InvalidTag
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes
    import os
    import string
    import random
    from base64 import b64encode, b64decode

    # Generate random password
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    vault_pass = ''.join(random.choice(chars) for i in range(32))

    # Encrypt vault_pass using AES256-GCM

# Generated at 2022-06-13 07:31:14.284565
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_data = '''meta_var:
  key_a:
    key_a_a: a
    key_a_b: b
  key_b:
    key_b_a: a
    key_b_b: b
'''
    # ansible_pos = ('<string>', 1, 1)
    data = AnsibleConstructor().construct_yaml_map(yaml_data)
    print(data)
    for key, value in data.items():
        print(key, value)


# Generated at 2022-06-13 07:31:22.173863
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import os
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes, to_text

    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    here = os.path.dirname(os.path.abspath(__file__))

    # Test 1: test that duplicate dict keys are not allowed unless setting
    # is set to 'ignore'
    yaml_string = '''
vault_password_files:
  - 'a.txt'
  - 'b.txt'
  - 'c.txt'
vault_password_files:
  - 'd.txt'
  - 'e.txt'
'''

    # make sure our test file is never included in

# Generated at 2022-06-13 07:31:32.712312
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    # test the entire method
    node_start_mark = [254, 1, 0, u'<unicode string>', u'test_construct_mapping']  # type: List[Union[int, str]]
    data_start_mark = [254, 1, 0, u'<unicode string>', u'test_construct_mapping'] # type: List[Union[int, str]]

# Generated at 2022-06-13 07:31:40.257380
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import os
    import sys
    import stat
    import unittest
    import yaml
    import tempfile
    import shutil

    class TestAnsibleConstructor_construct_yaml_map(unittest.TestCase):

        def setUp(self):
            ''' Create temp directory, and write vault password file '''
            self.temp_dir = tempfile.mkdtemp()
            self.password_file = os.path.join(self.temp_dir, 'vault_password')
            f = open(self.password_file, 'wb')
            f.write(b'ansible')
            f.close()

            # make the temp directory world readable/searchable
            read_perm = (stat.S_IROTH | stat.S_IRGRP | stat.S_IRUSR)
            search_perm

# Generated at 2022-06-13 07:31:45.299283
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest

    class TestCase(unittest.TestCase):
        def test_construct_vault_encrypted_unicode(self):
            # Make a vault
            vault_secrets = ['d41d8cd98f00b204e9800998ecf8427e']
            vl = AnsibleConstructor(vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:31:52.444389
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # in this case, we should be able to construct
    data = AnsibleMapping()
    assert not data
    data.update({'a': 1, 'b': 2})
    assert data == {'a': 1, 'b': 2}

    data = AnsibleMapping()
    assert not data
    data.update({'a': 1, 'b': 2})
    assert data == {'a': 1, 'b': 2}


# Generated at 2022-06-13 07:31:58.798375
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # Some test data
    foo_bar = dict(foo=[1, 2], bar=dict(buz=u'foobar'))
    # The test
    yaml = AnsibleConstructor(None).construct_yaml_map(foo_bar)
    # The assertion
    assert foo_bar == yaml

# Generated at 2022-06-13 07:32:01.111711
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    a = AnsibleConstructor()
    value = a.construct_yaml_unsafe({
        "id": "test",
        })
    assert isinstance(value, wrap_var)

# Generated at 2022-06-13 07:32:04.191606
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()
    value = list()
    ansible_seq = constructor.construct_yaml_seq(value)
    assert not isinstance(ansible_seq, list)
    assert isinstance(ansible_seq, AnsibleSequence)


# Generated at 2022-06-13 07:32:18.124485
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping
    yaml_in = u'1 \n2\n 3\n  4'

    c = AnsibleConstructor()
    c.add_constructor(u'tag:yaml.org,2002:int', lambda x, y: x[0])
    c.add_constructor(u'tag:yaml.org,2002:str', lambda x, y: x)

    data = yaml.load(yaml_in, Loader=c)

    assert isinstance(data, AnsibleMapping)
    assert sorted(data.keys()) == [u'1', u'2', u'3']
    assert sorted(data[u'3'].keys()) == [u'4']

# Generated at 2022-06-13 07:32:26.163846
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    c = AnsibleConstructor()
    n = yaml.nodes.ScalarNode("tag:yaml.org,2002:str", '$ANSIBLE_VAULT;1.1;AES256\n313232626332343733613237316338633530366333326164373132393365633037343032623963626\n')
    v = c.construct_vault_encrypted_unicode(n)
    assert v.vault.decrypt(v) == "123456"

# Generated at 2022-06-13 07:32:30.214284
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    class TestAnsibleConstructor_construct_vault_encrypted_unicode(unittest.TestCase):
        def setUp(self):
            pass
        def tearDown(self):
            pass
        def test___call__(self):
            pass
    unittest.main()

# Generated at 2022-06-13 07:32:36.087243
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    input_yaml = '''
- 1
- 2
- 3
'''
    ansible_constructor = AnsibleConstructor()
    output = yaml.load(input_yaml, Loader=yaml.Loader, constructor=ansible_constructor)
    assert output == [1, 2, 3]
    assert type(output) == AnsibleSequence
    assert len(output.ansible_pos) == 3
    assert output.ansible_pos[0] == '<unicode string>'
    assert output.ansible_pos[1] == 1
    assert output.ansible_pos[2] == 0


# Generated at 2022-06-13 07:32:47.463777
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader

    yamlContent = b'foo: !unsafe "bar"'
    mockLocation = (u'<string>', 0, 1)

    mockArgs = {
        'file_name': u'<string>',
        'vault_secrets': [],
    }

    # Create mock AnsibleConstructor
    mockAnsibleConstructor = AnsibleConstructor(**mockArgs)
    mockAnsibleConstructor.construct_yaml_str = AnsibleConstructor.construct_yaml_str

    # Create mock AnsibleLoader
    mockAnsibleLoader = AnsibleLoader(yamlContent, mockAnsibleConstructor)

    mockAnsibleLoader.get_single_node = lambda: None

# Generated at 2022-06-13 07:32:56.877828
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from collections import namedtuple
    from ansible.parsing.yaml.objects import AnsibleMapping

    # Each test data represents a list of YAML nodes and expected result
    # from AnsibleConstructor.construct_yaml_seq call.

# Generated at 2022-06-13 07:33:00.144284
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    a = AnsibleConstructor()
    node = {'a': 1, 'b':2, 'c':3}
    l = a.construct_yaml_map(node)
    assert l['a'] == 1
    assert l['b'] == 2
    assert l['c'] == 3

# Generated at 2022-06-13 07:33:07.332088
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Given
    input_string = "string"
    input_node = type(u'Node', (), {"id": "tag:yaml.org,2002:str"})
    input_node.start_mark = type(u'Mark', (), {"column": 1, "line": 2, "name": "name"})

    # When
    actual_output = AnsibleConstructor.construct_yaml_str(input_node)

    # Then
    assert actual_output == AnsibleUnicode(input_string)
    assert actual_output.ansible_pos == ("name", 2, 2)

# Generated at 2022-06-13 07:33:15.301245
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], start_mark=None, end_mark=None)
    sut = AnsibleConstructor(file_name=None)
    sut.construct_mapping(node)



# Generated at 2022-06-13 07:33:26.058314
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest2 as unittest
    from ansible.parsing.yaml import objects
    import ansible.parsing.vault as vault

    # Encrypt "test"
    vault.Vault.MIN_SECRETS = 1
    tokens = vault.VaultLib(
        secrets=['abcd']
    ).encrypt(b'test')
    # Inject a VaultEncryptedUnicode into our map
    yaml_map = {'ansible_password': objects.AnsibleVaultEncryptedUnicode(tokens['data'])}
    # Add the vault_secrets
    constructor = AnsibleConstructor(vault_secrets=['abcd'])
    # The map should be populated with a regular 'test' string

# Generated at 2022-06-13 07:33:35.493846
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor('')
    node1 = 'value'
    node2 = 1
    data = constructor.construct_yaml_seq(node1)
    constructor.construct_yaml_seq(node2)

    assert(data == 'value')
    assert(data == 1)
    assert(data == 'value')
    assert(data == 1)



# Generated at 2022-06-13 07:33:39.146466
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    data = AnsibleMapping()
    ret = AnsibleConstructor()
    ret_node = ansible_yaml = """
a: "one"
b: "two"
"""
    node_ret = yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', [])
    data = ret.construct_yaml_map(node_ret)
    assert data == "one"

# Generated at 2022-06-13 07:33:41.018321
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    result = AnsibleConstructor.construct_yaml_unsafe(None)
    assert result == None

    result = AnsibleConstructor.construct_yaml_unsafe("test")
    assert result == "test"

# Generated at 2022-06-13 07:33:46.844531
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import io
    import unittest
    import yaml


# Generated at 2022-06-13 07:33:54.622059
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    from ansible.errors import AnsibleError

    secrets = ['dummy_password']

# Generated at 2022-06-13 07:34:01.687847
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib

    # test case where vault secrets are not provided
    node = object()
    value = 'value'
    v = VaultLib()

    ciphertext_data = to_bytes(value)
    value_byte = b'!vault |\n          ' + ciphertext_data
    node.value = value_byte
    node.start_mark = object()
    node.start_mark.line = 0
    node.start_mark.column = 0
    node.start_mark.name = ''
    constructor = AnsibleConstructor()
    constructor._vaults['default'] = v
    assert value == constructor.construct_vault_encrypted_unicode(node).data

# Generated at 2022-06-13 07:34:15.296218
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    import sys
    import six
    import yaml

    class TestAnsibleConstructor(AnsibleConstructor):

        def _node_position_info(self, node):
            return ('<string>', 1, 1)

    test_obj = TestAnsibleConstructor()

    test_data_seq = ['a', 'b', 'c']
    test_data_str = '''
- a
- b
- c'''

    if six.PY2:
        if type(test_data_str) is unicode:
            test_data_str = test_data_str.encode('utf-8')

    test_data_seq_expected_output = [(u'<string>', 1, 1), u'a', u'b', u'c']

# Generated at 2022-06-13 07:34:19.944775
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()
    test_value = AnsibleSequence()
    test_value.ansible_pos = ("filename", "line", "column")
    test_value.append(True)
    test_value.append(False)
    assert constructor.construct_yaml_seq(node=None) == test_value

# Generated at 2022-06-13 07:34:22.167846
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    node = u'tag:yaml.org,2002:str'
    cls = AnsibleConstructor.construct_yaml_str(node)
    assert cls == u'tag:yaml.org,2002:str'


# Generated at 2022-06-13 07:34:32.179949
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # note that this is only testing the method itself, not the vault code
    # from ansible.parsing.vault

    from yaml.nodes import ScalarNode

    def _get_node(value):
        return ScalarNode(
            'tag:yaml.org,2002:str',
            to_bytes(value),
            None,
            None,
            None,
        )

    # test non-encrypted
    node = _get_node('foo')
    assert isinstance(AnsibleConstructor(vault_secrets=[])
                      .construct_vault_encrypted_unicode(node), str)

    # test encrypted
    node = _get_node(u'!vault |\n          $ANSIBLE_VAULT;1.2;AES256;foo\n          bar\n          ')
   

# Generated at 2022-06-13 07:34:46.784623
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = """
        foo:
            a: 1
            b: 2
            c: 3
        bar:
            foo: 1
            bar: 2
            baz: 3
    """
    data = yaml.load(data, Loader=AnsibleConstructor)
    assert isinstance(data, dict)
    assert isinstance(data, AnsibleMapping)
    assert data.foo.a == 1
    assert data.foo.b == 2
    assert data.foo.c == 3
    assert data.bar.foo == 1
    assert data.bar.bar == 2
    assert data.bar.baz == 3

# Generated at 2022-06-13 07:34:48.918645
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    result = AnsibleConstructor.construct_yaml_map(AnsibleConstructor, None)
    assert isinstance(result, AnsibleMapping)

# Generated at 2022-06-13 07:34:58.451064
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    class AnsibleConstructor_construct_yaml_map(AnsibleConstructor):
        def __init__(self, file_name=None, vault_secrets=None):
            self._ansible_file_name = file_name
            super(AnsibleConstructor, self).__init__()
            self._vaults = {}
            self.vault_secrets = vault_secrets or []
            self._vaults['default'] = VaultLib(secrets=self.vault_secrets)

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.nodes import AnsibleMappingNode
    ac = AnsibleConstructor_construct_yaml_map()

# Generated at 2022-06-13 07:35:09.724727
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    yaml_str = '''
    roles:
      - role: httpd
        t:
          a: 1
          b: 2
        c: 3
    '''

    yaml_data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(yaml_data, AnsibleMapping)
    assert len(yaml_data) == 1
    assert 'roles' in yaml_data
    assert len(yaml_data['roles']) == 1
    role = yaml_data['roles'][0]
    assert isinstance(role, AnsibleMapping)
    assert len(role) == 3
    assert 'role' in role
    assert role['role'] == 'httpd'
    assert 't' in role
    t = role

# Generated at 2022-06-13 07:35:13.501014
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test = AnsibleConstructor()
    node = MappingNode(u'tag:yaml.org,2002:map', [], None, None, False)
    mapping = test.construct_mapping(node=node)
    assert isinstance(mapping, AnsibleMapping)
    assert [] == mapping


# Generated at 2022-06-13 07:35:20.499948
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    test_data = """
    This string:
    is a string
    """

    import yaml

    # Resetting the file name to None because otherwise you get
    # `no implicit conversion of NoneType into string`
    file_name=None
    test_yaml = yaml.load(test_data, Loader=AnsibleConstructor)

    import sys
    from ansible.module_utils._text import to_bytes, to_text
    from yaml.constructor import ConstructorError
    from yaml.nodes import MappingNode

    assert test_yaml is not None
    assert test_yaml.ansible_pos[0] == file_name
    assert test_yaml.ansible_pos[1] == 2
    assert test_yaml.ansible_pos[2] == 1

    # TODO:

# Generated at 2022-06-13 07:35:34.154491
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.module_utils._text import to_text

    # Test data for a yaml node containing a single element
    node_1_element = {
        'value': [('a', 'b')],
        'id': 'seq',
        'start_mark': {'column': 3, 'line': 0, 'buffer': '', 'pointer': 0},
        'end_mark': {'column': 5, 'line': 0, 'buffer': 0, 'pointer': 0}
    }

    # Test data for a yaml node containing two elements

# Generated at 2022-06-13 07:35:38.458733
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from unit.parsing.yaml.test_yaml_constructors import test_AnsibleConstructor_construct_mapping
    test_AnsibleConstructor_construct_mapping(AnsibleConstructor)

# Generated at 2022-06-13 07:35:50.658483
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from collections import OrderedDict

    '''
    Doctest for AnsibleConstructor.construct_yaml_map method
    >>> obj = AnsibleConstructor()
    >>> # Test for construction of a map from a YAML map node
    >>> yaml_map_data = b'''

# Generated at 2022-06-13 07:36:02.142810
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    import os, tempfile
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Create a temporary file, and load the yaml string to be tested
    fd, fname = tempfile.mkstemp(text=True)

# Generated at 2022-06-13 07:36:18.561998
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    data = u"foo: bar\n"
    data += u"bar: [ foo, bar, baz ]\n"
    data += u"baz:\n"
    data += u"  - foo\n"
    data += u"  - bar\n"
    data += u"  - baz\n"
    node = yaml.compose(data)
    mapping = AnsibleConstructor.construct_yaml_map(
        None, node)
    assert type(mapping) == AnsibleMapping
    assert type(mapping.ansible_pos) == tuple
    assert mapping[u'foo'] == u'bar'
    assert type(mapping[u'bar']) == AnsibleSequence
    assert mapping[u'bar'][0] == u'foo'

# Generated at 2022-06-13 07:36:26.759239
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_data = """
- name: test
  foo: bar
- name: another test
  foo: baz
"""
    expected = [{
        u"name": u"test",
        u"foo": u"bar",
        u"ansible_pos": (u'<unicode string>', 1, 1)
    }, {
        u"name": u"another test",
        u"foo": u"baz",
        u"ansible_pos": (u'<unicode string>', 4, 1)
    }]
    x = AnsibleConstructor(file_name=None)
    actual = x.construct_yaml_seq(yaml.compose(yaml_data)).pop()
    assert actual == expected

# Generated at 2022-06-13 07:36:28.157086
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()
    constructor.construct_yaml_seq(None)

# Generated at 2022-06-13 07:36:37.311579
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    # Test input data
    data = b'''
    # comment
    - name: "#'"
    - name: "'"
    - name: '"'
    - name: '"#'"
    - name: '"\''
    - name: '"\\'"
    - name: '"\\\\'"
    - name: '"\\\\\\'"
    - name: '"\\\\\\\'"'
    '''

    # Create an object of class AnsibleConstructor
    constructor = AnsibleConstructor()

    # Use the load method of class AnsibleConstructor to create an Ansible sequence type object to be tested
    ansible_seq = list(constructor.load_all(data))
    assert isinstance(ansible_seq, AnsibleSequence)

    # Add expected values to test against

# Generated at 2022-06-13 07:36:43.050221
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.module_utils.parsing.yaml.objects import AnsibleUnsafeText

    unsafe_value = '!unsafe this is a string'
    constructor = AnsibleConstructor()
    ret = constructor.construct_yaml_unsafe(unsafe_value)
    assert isinstance(ret, AnsibleUnsafeText)



# Generated at 2022-06-13 07:36:51.284336
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.data import DataLoader
    from ansible.vars import merge_hash

    # Load our test data
    data = DataLoader()
    datas = data.load_from_file('test/units/parsing/yaml/constructor_data.yml')

    # Create an instance of our constructor
    constructor = AnsibleConstructor()

    # Test the construct_mapping method with the data
    for test in datas:
        result = constructor.construct_mapping(test['datas'][0], deep=True)
        assert test['result'] == result

        # merge_hash needs native strings and we don't want to use 'unicode' because we want to test
        # the fallback within merge_hash, which is only available when using Python 2
        # That's why we are using str(x

# Generated at 2022-06-13 07:37:06.035988
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml import _load_yaml_without_tags
    from ansible.parsing.yaml.objects import AnsibleMapping
    import textwrap
    from io import StringIO
    from ansible.module_utils._text import to_bytes
    import sys

    data = u'{foo: bar}\n'

    expected_data = AnsibleMapping({u'foo': u'bar'})

    ds = 'file.yml'
    lnum = 1
    col = 1
    expected_pos = (ds, lnum, col)

    expected_data.ansible_pos = expected_pos

    yaml_data = _load_yaml_without_tags(StringIO(data))

    assert type(yaml_data) is AnsibleMapping

# Generated at 2022-06-13 07:37:14.093376
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """
    The method construct_mapping of class AnsibleConstructor should return a
    dict object containing the key-value pairs of the given Yaml mapping node,
    and it should validate that the key is hashable.

    :param node: The Yaml mapping node to be converted to a dict.

    :return: A dict containing the key-value pairs of the given Yaml mapping
             node.
    """

    # Test valid data
    valid_node = dict()
    valid_node['start_mark'] = 'start_mark'
    valid_node['value'] = list(('one', 'two'))
    valid_node['id'] = 'id'
    valid_mapping = dict()
    valid_mapping['one'] = 'one'
    valid_mapping['two'] = 'two'
    constructor = AnsibleConstructor()


# Generated at 2022-06-13 07:37:18.216143
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml.nodes import ScalarNode

    class MockScalarNode(ScalarNode):
        def __init__(self, tag, value, pos=False):
            ScalarNode.__init__(self, tag, value)
            if pos:
                self.start_mark = pos
                self.end_mark = pos

    assert AnsibleConstructor.construct_yaml_str(MockScalarNode(None, '')) == AnsibleUnicode('')
    assert AnsibleConstructor.construct_yaml_str(MockScalarNode(None, 'a')) == AnsibleUnicode('a')



# Generated at 2022-06-13 07:37:29.791553
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 07:37:44.995087
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    sample_yaml_mapping_node = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'subkey1': 'subkey1_value',
            'subkey2': 'subkey2_value',
            'subkey3': {
                'subsubkey1': 'subsubkey1_value1',
                'subsubkey2': 'subsubkey2_value2',
                'subsubkey3': 'subsubkey3_value3',
            },
        },
    }
    ac = AnsibleConstructor()
    assert ac.construct_mapping(sample_yaml_mapping_node) == sample_yaml_mapping_node


# Generated at 2022-06-13 07:37:58.447639
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    import os
    file_name_test = os.path.join(os.path.dirname(__file__), "yaml_test.yml")

    data = {
        'name': 'test_AnsibleConstructor_construct_yaml_map',
        'dict_key1': 'value1',
        'dict_key2': 'value2',
        'duplicate_dict_key': 'value1',
        'list': [
            'list_elem1',
            'list_elem2',
            'list_elem3',
            {
                'dict_key3': 'value3',
                'dict_key4': 'value4',
            }
        ]
    }

    constructor = AnsibleConstructor(file_name=file_name_test)
    result = constructor.construct_y