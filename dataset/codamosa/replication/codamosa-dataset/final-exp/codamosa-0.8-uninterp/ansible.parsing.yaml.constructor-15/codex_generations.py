

# Generated at 2022-06-13 07:28:07.962327
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    ansibleConstructor = AnsibleConstructor()
    mapping_node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[])
    actual = ansibleConstructor.construct_yaml_map(mapping_node)
    expected = AnsibleMapping()
    assert actual.ansible_pos == expected.ansible_pos

# Generated at 2022-06-13 07:28:08.572299
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:28:19.482609
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
  from io import StringIO
  from ansible.parsing.vault import VaultLib

  def get_one():
    if count >= len(secrets):
      raise StopIteration
    secret = secrets[count]
    count += 1
    return secret

  count = 0
  secrets = ['1', '2', '3']
  vault_secrets = VaultLib(secrets=iter(get_one, None))
  input = '''
    test:
      - a: 1
      - b: 2
      - c: 3
  '''
  yaml = YAMLDumper()
  output = yaml.load(YAMLLoader(input, vault_secrets=vault_secrets).get_single_data())
  assert isinstance(output, AnsibleMapping)

# Generated at 2022-06-13 07:28:29.987756
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    from ansible.parsing.yaml.loader import AnsibleLoader
    vault_secrets = ['TestVaultSecret']

# Generated at 2022-06-13 07:28:35.627043
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleSequence
    c = AnsibleConstructor()
    node = AnsibleBaseYAMLObject()
    node.start_mark = ''
    node.end_mark = ''
    node.value = [
        AnsibleBaseYAMLObject(), AnsibleBaseYAMLObject(), AnsibleBaseYAMLObject()
    ]
    data = c.construct_yaml_seq(node)
    assert isinstance(data, AnsibleSequence)
    assert len(data) == 3


# Generated at 2022-06-13 07:28:40.666179
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    x = b'hello world\n'
    y = AnsibleConstructor.construct_yaml_str(AnsibleConstructor(), x)
    assert isinstance(y, AnsibleUnicode)
    assert y == u'hello world\n'

    x = b'hello_world'
    z = AnsibleConstructor.construct_yaml_str(AnsibleConstructor(), x)
    assert isinstance(z, AnsibleUnicode)
    assert z == u'hello_world'

    assert y != z

# Generated at 2022-06-13 07:28:44.185991
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = """
foo:
  - a
  - b
bar:
  - 2
  - 4
"""
    yaml.load(data, Loader=AnsibleConstructor)

# Generated at 2022-06-13 07:28:52.288986
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml import objects
    import yaml
    # Construct a string that can execute arbitrary Python code with the !unsafe tag
    value = "!unsafe |\n{0}\n|".format(repr(objects))
    # Use the safe_load method of the yaml module to prevent unsafe Python objects
    # from being deserialized
    data = yaml.safe_load(value)
    assert data is objects


# Generated at 2022-06-13 07:29:02.454699
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.module_utils._text import to_bytes

    from ansible.parsing.yaml import objects

    nodes = [
        u"{A: foo, B: {C: bar, D: baz}, E: [one, two, three]}"
    ]
    for s in nodes:
        data = yaml.load(to_bytes(s), Loader=AnsibleConstructor)
        assert isinstance(data, objects.AnsibleMapping)
        assert data['A'] == 'foo'
        assert data['B']['C'] == 'bar'
        assert data['B']['D'] == 'baz'
        assert data['E'][0] == 'one'
        assert data['E'][1] == 'two'
        assert data['E'][2] == 'three'



# Generated at 2022-06-13 07:29:15.925799
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    import tempfile
    import os

    vault_secrets_path = '/tmp/ansible/construct'
    if not os.path.exists(vault_secrets_path):
        os.makedirs(vault_secrets_path)

    vault_secrets_file = os.path.join(vault_secrets_path, 'ansible.txt')
    if not os.path.exists(vault_secrets_file):
        with open(vault_secrets_file, 'w') as fh:
            fh.write('test_vault_password_file\n')

    tmp_fh, tmp_path = tempfile.mkstemp()

# Generated at 2022-06-13 07:29:26.891253
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    f = tempfile.NamedTemporaryFile(delete=False)
    try:
        f.write(b'test_key: test_value')
        f.close()

        constructor = AnsibleConstructor(file_name=f.name)

        with open(f.name) as yaml_file:
            data = yaml_file.read()

        node = yaml.compose(data, f.name)
        yaml.construct_document(node, constructor)
        result = constructor.get_single_data()
        assert isinstance(result, AnsibleMapping)
    finally:
        if f:
            os.unlink(f.name)

# Generated at 2022-06-13 07:29:38.301052
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    vault = VaultLib()

# Generated at 2022-06-13 07:29:43.937548
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode(tag='tag:yaml.org,2002:map',
                       value=[],
                       start_mark=None, end_mark=None, flow_style=False)
    a = AnsibleConstructor()
    m = a.construct_mapping(node)
    assert isinstance(m, AnsibleMapping)
    assert m.__class__.__name__ == 'AnsibleMapping'
    assert m.ansible_pos == ('<unicode str>', 1, 0)

# Generated at 2022-06-13 07:29:51.517485
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():

    ansible_constructor = AnsibleConstructor()
    assert ansible_constructor != None

    yaml_str = '''
        ---
        first_item:
          key1: value1
          key2: value2

        second_item:
          key1: value1
          key2: value2
        '''

    yaml_obj = yaml.load(yaml_str, Loader=AnsibleConstructor)

    assert yaml_obj['first_item']['key1'] == 'value1'
    assert yaml_obj['first_item']['key2'] == 'value2'
    assert yaml_obj['second_item']['key1'] == 'value1'
    assert yaml_obj['second_item']['key2'] == 'value2'


# Generated at 2022-06-13 07:29:58.393686
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    data = '1234567890'
    node = {}
    a = AnsibleConstructor()

    v = a.construct_yaml_str(node)
    assert len(v) == len(data)
    assert list(v) == list(data)
    assert len(v.ansible_pos) == 3
    assert v.ansible_pos[2] == 0
    assert v.ansible_pos[1] == 0
    assert v.ansible_pos[0] is None



# Generated at 2022-06-13 07:29:59.514810
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # This test makes sure that the module is importable.
    # Tests for the method are in test_unsafe_proxy.
    pass



# Generated at 2022-06-13 07:30:09.209294
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Test with yaml.nodes.MappingNode
    mappingnode_test = MappingNode('testtag', [], [], True)
    # Test without yaml.nodes.MappingNode
    notmappingnode_test = "I'm not a MappingNode"
    # Test with duplicate dictionary keys
    duplicated_mappingnode_test = MappingNode('testtag', [], [], True)
    # Test with dictionary containing illegal keys
    illegal_key_mappingnode_test = MappingNode('testtag', [], [], True)
    # Test with an AnsibleMapping object
    ansible_mapping_test = AnsibleMapping()
    # Test with a empty AnsibleMapping
    empty_ansible_mapping_test = AnsibleMapping()

    ac = AnsibleConstructor()
    # Test with

# Generated at 2022-06-13 07:30:17.465861
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import io
    # ConstructorError is in the global namespace only in pyyaml <= 4.1b1, then it was moved to yaml.constructor
    if sys.version_info[0] == 2 and sys.version_info[1] == 7:
        ConstructorError = 'ConstructorError'
    else:
        from yaml.constructor import ConstructorError
    constructed_vault_obj = None
    # Create the VaultLib object to pass to the constructor and
    # the vault_secret_data.
    syspass = sys.stdin.readline().splitlines()
    vault_password_file = io.StringIO(u"%s\n" % syspass[0])
    vault = VaultLib(vault_password_file)
    # Test for successful construction of vault-encrypted unicode
   

# Generated at 2022-06-13 07:30:20.066768
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    secret = VaultLib()
    secret.secrets = ["test"]

    yaml_str = secret.encode("test")

    ansible_constructor = AnsibleConstructor()
    ansible_constructor.vault_secrets = ["test"]
    ret = ansible_constructor.construct_vault_encrypted_unicode(yaml_str)

    assert ret == b"test"


AnsibleConstructor.add_multi_constructor(u'!vault-encrypted', AnsibleConstructor.construct_vault_encrypted_unicode)

# Generated at 2022-06-13 07:30:28.599930
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.reader import Reader
    from ansible.parsing.yaml.loader import AnsibleLoader

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text

    from six import StringIO

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()


# Generated at 2022-06-13 07:30:42.702268
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    class MyDict(AnsibleBaseYAMLObject):
        def __init__(self, d=None):
            super(MyDict, self).__init__()
            self.value = d or {}

        def __getitem__(self, key):
            return self.value[key]

        def __setitem__(self, key, value):
            self.value[key] = value

        def __getattr__(self, name):
            return getattr(self.value, name)

    from yaml.parser import Parser
    from yaml.scanner import Scanner
    from io import StringIO


# Generated at 2022-06-13 07:30:48.875453
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    key = 'foo'
    vault_id = None
    vault_secrets = [key]
    constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    value = '$ANSIBLE_VAULT;1.1;AES256\n66616233653564386333306439333762633038306434393764333565343361336337313461323666\n6138623262646337623063306339383138653037663435363437623761646165303833323735653661\n6131393433656163393965616462633337663533323539396533313435633062653038653435653633\n3765\n'

# Generated at 2022-06-13 07:30:52.219220
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    stream = '{a: 1, b: 2, c: 3}'
    stream = yaml.load(stream, Loader=AnsibleConstructor)
    assert stream['a'] == 1
    assert stream['b'] == 2
    assert stream['c'] == 3


# Generated at 2022-06-13 07:31:03.029863
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # pylint: disable=too-few-public-methods
    class MockAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            self.vault_secrets = ['password']
            super(MockAnsibleConstructor, self).__init__(vault_secrets=self.vault_secrets)

    ac = MockAnsibleConstructor()
    import yaml

# Generated at 2022-06-13 07:31:05.162976
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    node = u'tag:yaml.org,2002:str'
    datum = AnsibleConstructor.construct_yaml_str(node)
    assert datum == node


# Generated at 2022-06-13 07:31:08.359083
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    dup_yaml = '''---
- hosts: all
  vars:
    foo: hello
    foo: world
  tasks:
    - debug: var=foo
'''
    yaml_obj = AnsibleConstructor().get_single_data(dup_yaml)
    assert isinstance(yaml_obj, list) and yaml_obj[0]['vars']['foo'] == 'hello'



# Generated at 2022-06-13 07:31:19.252084
# Unit test for method construct_mapping of class AnsibleConstructor

# Generated at 2022-06-13 07:31:29.934050
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys
    import yaml
    if sys.version_info[0] >= 3:
        unicode = str

    data = yaml.load("""
    - foo:
        name: "a"
      bar:
        name: "b"
    - foo:
        name: "c"
      bar:
        name: "d"
    """, Loader=AnsibleConstructor)

    assert type(data) == list
    assert len(data) == 2
    assert type(data[0]) == dict
    assert type(data[1]) == dict
    assert "foo" in data[0]
    assert "bar" in data[0]
    assert type(data[0]["foo"]) == dict
    assert type(data[0]["bar"]) == dict

# Generated at 2022-06-13 07:31:30.457235
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:31:34.517669
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()
    node = object()
    result = constructor.construct_yaml_seq(node)
    # Result should be a generator
    assert isinstance(result, types.GeneratorType)
    result = next(result)
    # Result should be an instance of AnsibleSequence
    assert isinstance(result, AnsibleSequence)

# Generated at 2022-06-13 07:31:43.094217
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    from ansible.module_utils._text import to_text
    constructor = AnsibleConstructor()
    loader = yaml.Loader(constructor)
    data = loader.get_single_data()
    assert data == 'default'


# vim: set expandtab shiftwidth=4 softtabstop=4:

# Generated at 2022-06-13 07:31:51.710223
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # initialize a test input
    test_input = {'b': 2, 'd': 3, 'a': 1, 'e': 4, 'c': 2}
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], flow_style=False)
    for key, value in test_input.items():
        key_node = AnsibleUnicode(key)
        key_node.ansible_pos = ('file', 1, 1, 0)
        value_node = AnsibleUnicode(value)
        value_node.ansible_pos = ('file', 1, 1, 0)
        node.value.append((key_node, value_node))
    ansible_constructor = AnsibleConstructor()

    # run the test and check results

# Generated at 2022-06-13 07:31:57.303022
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    ac = AnsibleConstructor()

    # test with a string
    node = ac.construct_yaml_str('hello')
    assert isinstance(node, AnsibleUnsafeText)



# Generated at 2022-06-13 07:32:09.171431
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ac = AnsibleConstructor()
    c = C

    # Testing different duplicate dict key outcomes
    # we use a list comprehension to create a dict with duplicate keys, which
    # should be overwritten, triggering the 'warn' by default.
    d1 = AnsibleMapping({x: x for x in range(3)})
    display.verbosity = 0  # turn off verbose output
    # default warn
    c.DUPLICATE_YAML_DICT_KEY = 'warn'
    ac.construct_mapping(d1)
    # error
    c.DUPLICATE_YAML_DICT_KEY = 'error'
    ac.construct_mapping(d1)
    # ignore
    c.DUPLICATE_YAML_DICT_KEY = 'ignore'
    ac.construct_mapping

# Generated at 2022-06-13 07:32:18.799461
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os, sys
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    current_directory = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(current_directory)

    test_loader = yaml.Loader('')
    test_loader.add_constructor(u'!vault', AnsibleConstructor.construct_vault_encrypted_unicode)
    test_loader.add_constructor(u'!vault-encrypted', AnsibleConstructor.construct_vault_encrypted_unicode)
    vault_password = 'secret'

# Generated at 2022-06-13 07:32:23.422455
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # AnsibleMapping should be used instead of dict
    obj = {'key': 'value'}
    node = 'tag:yaml.org,2002:map'
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_yaml_map(node)
    assert(isinstance(obj, AnsibleMapping))


# Generated at 2022-06-13 07:32:33.493689
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    import yaml

    yaml_str = """
one:
    key1: val1
    key2: val2

two:
    key3: val3
    key4: val4
"""

    data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(data, dict)
    assert data == {"one": {"key1": "val1", "key2": "val2"}, "two": {"key3": "val3", "key4": "val4"}}

    # Test duplicate keys
    yaml_str = """
one:
    key1: val1
    key1: val2
"""

    try:
        data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    except ConstructorError:
        pass

# Generated at 2022-06-13 07:32:37.273351
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    mapping_node = MappingNode(u'tag:yaml.org,2002:map', [])
    data = AnsibleMapping()
    data.ansible_pos = None
    mapping_node.value = []
    assert AnsibleConstructor().construct_mapping(mapping_node) == data



# Generated at 2022-06-13 07:32:48.341590
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 07:32:53.096453
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from yaml.resolver import Resolver
    from io import StringIO

    # yaml_str is contains the equivalent of:
    # 'a: b'
    yaml_str = u"a: b"

    # utf8_yaml_str is contains the equivalent of:
    # 'utf8: "some utf8 text"'
    utf8_yaml_str = u"utf8: 'some utf8 text'"

    # dbl_utf8_yaml_str is contains the equivalent of:
    # 'utf8: "some utf8 text"'
    # 'utf8_2: "some utf8 text 2"'
   

# Generated at 2022-06-13 07:33:09.867799
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml_text = '''\
foo: 1
bar: 2
'''
    ansible_constructor = AnsibleConstructor()
    loaded_yaml = yaml.load(yaml_text, Loader=AnsibleConstructor)
    # Check that the loaded yaml is a dict class AnsibleMapping
    assert isinstance(loaded_yaml, dict)
    assert isinstance(loaded_yaml, AnsibleMapping)
    # Check that the loaded yaml is of the expected format
    assert loaded_yaml == {u'foo':1, u'bar':2}
    # Check that the dict contains a variable ansible_pos
    assert loaded_yaml.ansible_pos == (None, 1, 0)


# Generated at 2022-06-13 07:33:24.344912
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleUnicode

    test_data = '''
value:
  - text
  - 12345
  - !vault |
        $ANSIBLE_VAULT;1.1;AES256
        35313563633039323632363465356665623166613638353437373635613762393736363765643935
        63336566313165663430633739623033313231366534353932643061646232396366663566623365
        663630

'''
    secrets = ['hunter2']
    vault = VaultLib(secrets=secrets)

# Generated at 2022-06-13 07:33:29.533333
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleSequence

    yaml_str = '''
    - 1
    - 2
    - 3
        '''

    data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(data, AnsibleSequence)
    assert data == [1, 2, 3]

# Generated at 2022-06-13 07:33:41.053328
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys

    yaml_str = u'hèllo'
    node = yaml.nodes.ScalarNode(u'tag:yaml.org,2002:str', yaml_str)
    constructor = AnsibleConstructor()

    # Check that we get a unicode string back
    ansible_str = constructor.construct_yaml_str(node)
    assert type(ansible_str) == AnsibleUnicode
    assert ansible_str == yaml_str

    # I'm not entirely sure why we have this test
    # It looks a bit hackish, but I don't want to remove it
    # until we are sure it is not needed.
    #
    # It looks like the way the data is passed in to the constructor
    # might depend on the python version
    #
    # The first two checks are not

# Generated at 2022-06-13 07:33:46.278036
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml import load, FullLoader
    data = load(u'--- "61f3a7b17c6d1e7f59022f2b7e754a26"', Loader=FullLoader)
    assert data == u'61f3a7b17c6d1e7f59022f2b7e754a26'
    assert type(data) == AnsibleUnicode

# Generated at 2022-06-13 07:33:54.461495
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secret = 'test123'
    vault_password_file = '/tmp/test123'
    with open(vault_password_file, 'w') as f:
        f.write(vault_secret)
    ac = AnsibleConstructor(vault_secrets=[vault_password_file])
    ac._vaults['default'].secrets.append(vault_secret)

# Generated at 2022-06-13 07:34:02.361853
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var, unwrap_var

    unsafe_str = u"unsafe_text"
    yaml_str = u"!unsafe {0}".format(unsafe_str)
    data = AnsibleLoader(yaml_str).get_single_data()
    assert data == unsafe_str
    assert isinstance(data, AnsibleUnsafeText)
    assert unwrap_var(data) == unsafe_str

    unsafe_unicode = u"\u7d22\u5c3c\u514b"

# Generated at 2022-06-13 07:34:15.504424
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import sys
    import io
    from ansible.parsing.yaml.objects import AnsibleUnicode

    yaml_str = u'''
test_dict:
  test_key: test_value
  test_key2: test_value2
'''
    yaml_stream = io.StringIO(yaml_str)

    # Monkey patch StreamReader in order to get access to attributes
    # start_mark and end_mark. We need to do this because PyYAML fake
    # a StreamReader object. We need to assign the original value to
    # original_StreamReader before in order to restore initial state
    # after test.
    original_StreamReader = SafeConstructor.StreamReader
    SafeConstructor.StreamReader = io.StringIO

    ans_constructor = AnsibleConstructor()

# Generated at 2022-06-13 07:34:24.998549
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    # idempotency test
    sample_yaml_list = '''
- !unsafe 1
- !unsafe yes
- !unsafe
  - 1
  - 2
- !unsafe [1,2]
- !unsafe {a: 1, b: 2}
'''

# Generated at 2022-06-13 07:34:34.071663
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = '''
        foo:
          bar: hi
          bar: hello
        baz:
          bar: world
        foo:
          bar: hello2
    '''
    from ansible import constants as C

    for yaml_dict_key in ['ignore', 'warn', 'error']:
        C.DUPLICATE_YAML_DICT_KEY = yaml_dict_key
        node = yaml.compose(data)
        mapping = AnsibleConstructor().construct_mapping(node)
        assert mapping == {u'foo': {u'bar': u'hello2'}, u'baz': {u'bar': u'world'}}
        C.DUPLICATE_YAML_DICT_KEY = 'error'

# Generated at 2022-06-13 07:34:58.566530
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import sys
    import StringIO
    from io import BytesIO
    from ansible.parsing.yaml.loader import AnsibleLoader
    import ansible.constants as C
    import yaml

    test_data = '''
---
a: b
c:
  - d
  - e
'''

    del sys.argv[1:]
    sys.argv = [sys.argv[0], '--syntax-check']
    C.DEFAULT_MODULE_LANG = 'en_US.UTF-8'
    if sys.version_info >= (3, 0):
        fh_in = BytesIO(to_bytes(test_data))
    else:
        fh_in = StringIO(test_data)


# Generated at 2022-06-13 07:35:09.804870
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # A simple test to check that the vault file can be parsed (in case of change in pyyaml)
    from yaml import load


# Generated at 2022-06-13 07:35:16.994472
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml

    test_input = u"""
    test_key:
        key1: 'value1'
        key2: 'value2'
    """

    loader_constructor = AnsibleConstructor()
    loader_constructor.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, AnsibleConstructor.construct_yaml_map)
    test_output_data = yaml.load(test_input, Loader=yaml.Loader, constructor=loader_constructor)

    assert isinstance(test_output_data, dict)
    assert test_output_data.get('test_key')


# Generated at 2022-06-13 07:35:31.684616
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml import load, dump

    yaml_string = '''
    value: !!str
      abcdef
    '''

    yaml_string2 = '''
    value: |
      abcdef
    '''

    yaml_string3 = '''
    value: abcdef
    '''

    yaml_string4 = '''
    value: 'abcdef'
    '''

    yaml_string5 = '''
    value: "abcdef"
    '''

    yaml_string6 = '''
    value: 123
    '''

    yaml_string7 = '''
    value: |-
      abc\
      def
    '''

    yaml_object = load(yaml_string, Loader=AnsibleConstructor)

# Generated at 2022-06-13 07:35:39.307766
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from mock import patch
    from copy import copy
    from ansible.parsing.yaml.objects import AnsibleMapping

    test_dup_key = [
        "---\n",
        "foo: bar\n",
        "foo: bar2\n"
    ]

    test_dup_key_content = ''.join(test_dup_key)
    test_dup_key_dup_key_ctor = copy(AnsibleConstructor)
    test_dup_key_dup_key_ctor.duplicate_key_allowed = True
    assert isinstance(test_dup_key_dup_key_ctor.get_single_data(test_dup_key_content), AnsibleMapping)

    test_dup_key_no_dup_key_ctor = copy

# Generated at 2022-06-13 07:35:50.777658
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os


# Generated at 2022-06-13 07:35:59.541637
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Read yaml string with !vault syntax
    yaml_string = '''
    ---
    hash: !unsafe |
      $1$MnFSJvgy$W1Ax8dFt2nPtFwyLn0V7X/
    '''
    # Convert to Python data structure
    result = yaml.load(yaml_string, Loader=AnsibleConstructor)
    # Assert result is a dict
    assert isinstance(result, dict)
    # Assert result is not a string

# Generated at 2022-06-13 07:36:11.685111
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    test_AnsibleConstructor_construct_yaml_unsafe.ac = AnsibleConstructor()
    test_AnsibleConstructor_construct_yaml_unsafe.ac.Constructor.construct_yaml_unsafe = AnsibleConstructor.construct_yaml_unsafe

    class FakeNode:
        def __init__(self, id):
            self.id = id
    # FIXME: Mock in the necessary code to use assertEqual
    def assertEqual(a, b):
        if a != b:
            raise Exception("Values do not match: {0} != {1}".format(a, b))

    assertEqual(test_AnsibleConstructor_construct_yaml_unsafe.ac.construct_yaml_unsafe(FakeNode('yaml')), None)

# Generated at 2022-06-13 07:36:20.563497
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # test method construct_mapping of class AnsibleConstructor
    # AnsibleConstructor.construct_mapping
    # construct_mapping
    # public
    #
    # tests AnsibleConstructor.construct_mapping

    # test cases

    import yaml

    data = """
    key1: aaa
    key2: true
    key3:
      key4: bbb
      key5: false
    key6:
      key7: ccc
    key8:
    - 10
    - 11
    - 12
    """

    data = yaml.load(data, Loader=AnsibleConstructor)
    assert data['key1'] == u'aaa'
    assert data['key2'] is True
    assert data['key3']['key4'] == u'bbb'

# Generated at 2022-06-13 07:36:24.000429
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    yaml_str = "test1: 1\ntest2: 2\ntest2: 3\n"
    data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert len(data) == 2
    assert data['test2'] == 3

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 07:37:04.992351
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    v = VaultLib()
    vault_pass = 'this is a secret'
    # this is our plaintext string
    plain = u'This is something to be encrypted'
    # here we encrypt the plaintext
    ciphertext = v.encrypt(to_bytes(plain), vault_pass)
    # our call to be tested:
    ret = AnsibleConstructor('/tmp/nonexisting_file', [vault_pass]).construct_vault_encrypted_unicode(None)
    assert ret.vault == v
    assert ret == ciphertext

# Generated at 2022-06-13 07:37:13.440251
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # generate an AnsibleConstructor object
    constructor = AnsibleConstructor()
    # test the construct_yaml_map function with a non-MappingNode node
    non_mapping_node = 'node'
    try:
        constructor.construct_yaml_map(non_mapping_node)
    except ConstructorError as e:
        if e.problem:
            assert e.problem == 'expected a mapping node, but found %s' % non_mapping_node.id
        else:
            raise AssertionError(e.problem)

    # test with a mapping node
    mapping_node_id = 'tag:yaml.org,2002:map'

# Generated at 2022-06-13 07:37:19.970919
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = '''
      a: b
      c: d
      b: e
    '''

    ansible_constructor = AnsibleConstructor()

    try:
        ansible_constructor.construct_mapping(data, deep=False)
    except ConstructorError as e:
        assert e.problem == u'While constructing a mapping from <unknown>, line 4, column 7, found a duplicate dict key (b). Using last defined value only.'

    try:
        ansible_constructor.construct_mapping(data, deep=False)
        assert False
    except ConstructorError as e:
        assert e.problem == u'While constructing a mapping from <unknown>, line 4, column 7, found a duplicate dict key (b). Using last defined value only.'

# Generated at 2022-06-13 07:37:31.938422
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.unsafe_proxy import wrap_var

    # When parsing a mapping, yaml.constructor.SafeConstructor.construct_mapping
    # does a recursive call to the construct_object method of the same class,
    # which explains the need for the fake AnsibleConstructor class.
    class FakeAnsibleConstructor(AnsibleConstructor):
        def construct_object(self, node, deep=False):
            return wrap_var('test1')  # Fake return, as we just want to test construct_mapping here

    loader = AnsibleLoader(FakeAnsibleConstructor())

# Generated at 2022-06-13 07:37:39.484944
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_dict = {u'key': u'value'}
    test_dict_duplicate_dict_keys = {u'key': 'value1', u'key': 'value2'}
    yaml_node = AnsibleConstructor.yaml_to_node(test_dict)
    test_dict_constructed = AnsibleConstructor.construct_mapping(yaml_node)
    assert isinstance(test_dict_constructed, AnsibleMapping)
    assert test_dict_constructed == test_dict
    yaml_node_duplicate_keys = AnsibleConstructor.yaml_to_node(test_dict_duplicate_dict_keys)
    test_dict_duplicate_keys_constructed = AnsibleConstructor.construct_mapping(yaml_node_duplicate_keys)


# Generated at 2022-06-13 07:37:43.424040
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    ac = AnsibleConstructor()
    m = ac.construct_yaml_map({'value': []})
    assert list(m) == [{}]


# Generated at 2022-06-13 07:37:57.759595
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Define test variables
    vault_secrets = ['secret1', 'secret2']
    constructor = AnsibleConstructor(file_name='<string>', vault_secrets=vault_secrets)
    class TestNode:
        pass
    test_node = TestNode()
    test_node.start_mark = TestNode()
    test_node.start_mark.column = 0
    test_node.start_mark.line = 0
    test_node.start_mark.name = '<string>'