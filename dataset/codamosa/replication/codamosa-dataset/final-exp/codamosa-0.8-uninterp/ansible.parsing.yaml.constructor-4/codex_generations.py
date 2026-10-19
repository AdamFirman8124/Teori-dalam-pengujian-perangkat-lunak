

# Generated at 2022-06-13 07:28:12.214536
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    yaml.constructor.SafeConstructor.add_constructor(u'tag:yaml.org,2002:seq', AnsibleConstructor.construct_yaml_seq)

    parser = yaml.Loader(u"")
    obj = parser.get_single_node()
    # obj.start_mark.index
    # obj.end_mark.index
    # obj.start_mark.line
    # obj.end_mark.line

    assert(yaml.dump(AnsibleConstructor.construct_yaml_seq(obj)) == '[\n]\n')
    return

# Generated at 2022-06-13 07:28:23.608292
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    test_key_secret = ['1234']
    test_value_secret = ['$ANSIBLE_DH_GROUP1_SIZE']

# Generated at 2022-06-13 07:28:32.731448
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # test data
    yaml_data = '''\
        a: 1
        b: 2
        c:
          - 3
          - 4
          - 5
        d: foo
        e: 10
        f: !unsafe "test"
        g: !vault "test"
        h: !vault-encrypted "test"
        '''
    # initialize
    v = VaultLib()
    v.secrets = ['test']
    ac = AnsibleConstructor(vault_secrets=v.secrets)
    # process
    m = ac.construct_yaml_map(yaml.load(yaml_data))
    # test
    assert m['a'] == 1
    assert m['b'] == 2
    assert m['c'] == [3, 4, 5]

# Generated at 2022-06-13 07:28:40.636750
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Tests that unicode objects are not wrapped.
    # FIXME: probably should move this to test_utils_vars
    my_unicode = u'unicode\x00string'
    ac = AnsibleConstructor()
    my_unicode2 = ac.construct_yaml_unsafe(my_unicode)
    assert my_unicode is my_unicode2

    # Tests that bytes objects are wrapped
    my_bytes = b'bytes\x00string'
    my_bytes2 = ac.construct_yaml_unsafe(my_bytes)
    assert type(my_bytes2) is not bytes
    assert my_bytes2.__class__.__name__ == 'unsafe_bytes'
    assert my_bytes2.__bytes__() == my_bytes

    # Tests that str objects are wrapped

# Generated at 2022-06-13 07:28:54.766610
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys
    import unittest

    class TestAnsibleConstructor(unittest.TestCase):
        def test_vault_constructor(self):

            # test the vault object
            vault = AnsibleConstructor()
            try:
                vault._vaults['default'].load_ciphertext('test/test_vault_ascii')
            except IOError as e:
                print(e)
                sys.exit(1)

            # set the vault secret
            vault = AnsibleConstructor(vault_secrets=['test'])
            try:
                vault._vaults['default'].load_ciphertext('test/test_vault_ascii')
            except IOError as e:
                print(e)
                sys.exit(1)

            # vault check
            vault.construct_v

# Generated at 2022-06-13 07:29:01.507965
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():

    from ansible.module_utils._text import to_native, to_text

    # Create a mock node for testing purposes:
    class MappingNode(object):
        def __init__(self, value, start_mark=None, end_mark=None):
            self.value = value
            self.start_mark = start_mark
            self.end_mark = end_mark
    class Mark:
        def __init__(self, name, line, column):
            self.name = name
            self.line = line
            self.column = column
    class ScalarNode(object):
        def __init__(self, tag, value, start_mark=None, end_mark=None):
            self.tag = to_text(tag)
            self.value = to_text(value)
            self.start_mark = start_

# Generated at 2022-06-13 07:29:10.891995
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node_a = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], start_mark=None, end_mark=None)
    node_a.value.append((
        ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'a', start_mark=None, end_mark=None),
        ScalarNode(tag=u'tag:yaml.org,2002:int', value=1, start_mark=None, end_mark=None)))

# Generated at 2022-06-13 07:29:19.140902
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import unittest
    import sys

    class TestAnsibleConstructor_construct_yaml_seq(unittest.TestCase):
        """
        Tests for AnsibleConstructor._node_position_info
        """
        def setUp(self):
            self.const = AnsibleConstructor()
            self.doc  = '''
- 1
- 2
- 3
'''
            self.node = yaml.parser.Parser().parse(self.doc)

        def test_construct_yaml_seq(self):
            for value in self.const.construct_yaml_seq(self.node):
                self.assertEqual(type(value), AnsibleSequence)

    test = TestAnsibleConstructor_construct_yaml_seq()

# Generated at 2022-06-13 07:29:26.475214
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault = VaultLib(secrets=[])
    node = AnsibleConstructor.construct_yaml_str("$ANSIBLE_VAULT;1.1;AES256;darwin\n383464346133376466353634633463663664303965643432366664336538646632623564663863\n346130366632316330633163636539336332623862613631333166633231306631323739663437")
    assert isinstance(node, AnsibleVaultEncryptedUnicode)
    assert node.vault == vault

# Generated at 2022-06-13 07:29:37.864073
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_text = '''
connection: local
hosts:
  - localhost
  - otherhost
'''

    data = AnsibleLoader(yaml_text).get_single_data()
    assert data == {'connection': 'local', 'hosts': ['localhost', 'otherhost']}
    assert data.ansible_pos == ('<string>', 2, 0)
    foo = data['hosts'].pop()
    assert foo == 'otherhost'
    assert foo.ansible_pos == ('<string>', 5, 2)

    new_data = AnsibleDumper.from_representer(data)
    assert new_data == yaml_text

# Generated at 2022-06-13 07:29:50.248736
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Create an instance of AnsibleConstructor
    a = AnsibleConstructor()

    # Create a node from a string
    node = a.compose_node('test', 'value')

    # Create an instance of AnsibleSequence
    data = AnsibleSequence()
    data.extend(a.construct_sequence(node))

    result = a.construct_yaml_seq(node)

    # Unit test for method construct_yaml_seq of class AnsibleConstructor
    assert type(result) == type(data)

# Generated at 2022-06-13 07:29:55.398013
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml import YAMLError
    from yaml import CLoader as Loader
    from yaml import dump
    import ansible.parsing.yaml.objects

    # Test Sequences
    test_sequence = ['first', 'second']
    test_yaml = dump(test_sequence, default_flow_style=False)
    try:
        test_output = ansible.parsing.yaml.objects.AnsibleSequence(Loader.get_single_data(test_yaml))
    except YAMLError as e:
        print(e)
    assert test_output == AnsibleConstructor.construct_yaml_seq(Loader.get_single_node(test_yaml))

# Generated at 2022-06-13 07:30:06.480985
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.module_utils._text import to_text
    ad = AnsibleDumper(Dumper=AnsibleDumper)
    fname = 'test.yml'
    data = [1,2,3]
    stream = ad.dump(data)
    stream = to_text(stream)
    stream = stream.replace('\n- 1', '\nlist:\n- 1')
    stream = stream.replace('\n- 2', '- 2')
    stream = stream.replace('\n- 3', '- 3')
    stream = stream.replace('- {', '- z:{')

# Generated at 2022-06-13 07:30:11.988477
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    obj = AnsibleConstructor()
    node = {'ansible': {'version': {'full': '2.5.5', 'major': 2, 'minor': 5, 'revision': 5}}}
    res = obj.construct_yaml_map(node)
    assert res == {'ansible': {'version': {'full': '2.5.5', 'major': 2, 'minor': 5, 'revision': 5}}}



# Generated at 2022-06-13 07:30:15.276694
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    c = AnsibleConstructor()
    assert isinstance(c, AnsibleConstructor)
    ansible_mapping = c.construct_yaml_map(MappingNode(None, None, True, None, None))
    assert isinstance(ansible_mapping, AnsibleMapping)

# Generated at 2022-06-13 07:30:25.068101
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from collections import OrderedDict
    data = """
    - when: 1
      name: query_all
      type: string
      workspace: PUBLIC
      value: SELECT * FROM all_tables
    - when: 1
      name: query_all_objects
      type: string
      workspace: PUBLIC
      value: SELECT * FROM all_objects
    - when: 1
      name: query_all_objects_empty
      type: string
      workspace: PUBLIC
      value: SELECT * FROM all_objects where 1=0
    """
    yamlobj = AnsibleLoader(data, None, AnsibleConstructor).get_single_data()
    assert isinstance(yamlobj, list)
    assert len(yamlobj) == 3

# Generated at 2022-06-13 07:30:36.362749
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from hvac import Client
    client = Client(url='http://localhost:8200', token='root')
    root_token = client.create_token(lease='1h', renewable=True, ttl='1h')
    client.token = root_token['auth']['client_token']
    secret_path = 'secret/hello'
    client.secrets.kv.v1.create_or_update_secret(path=secret_path, secret='world')
    secret_engine_path = 'secret'
    client.sys.enable_secret_engine(backend_type='kv', path=secret_engine_path)
    client.secrets.kv.v1.create_or_update_secret(path=secret_path, secret='world')
    resp = client.secrets.kv.v2.read

# Generated at 2022-06-13 07:30:47.125689
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml.representer import Representer
    from yaml.dumper import Dumper
    from ansible.parsing.yaml.objects import AnsibleUnicode
    rep = Representer()
    yaml = Dumper(representer=rep)
    # create a yaml scalar with specified style
    yaml.representer.add_representer(AnsibleUnicode, rep.represent_str)
    node = yaml.represent_str(u'foo')
    # not really testing the formatting of the class here
    # as that is tested elsewhere
    val = AnsibleConstructor.construct_yaml_str(node)
    assert val == u'foo'
    assert isinstance(val, AnsibleUnicode)
    assert val.ansible_pos[0] is None

# Generated at 2022-06-13 07:30:51.363464
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    yaml_str = """
  - 1
  - 2
  - 3
  - 4
"""
    data = yaml.load(yaml_str, Loader=yaml.Loader)
    s = AnsibleConstructor()
    seq = s.construct_yaml_seq(data)
    assert isinstance(seq, AnsibleConstructor.construct_yaml_seq)
    assert list(seq) == [1, 2, 3, 4]



# Generated at 2022-06-13 07:31:02.202000
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():

    def _create_node(value):
        # Create a YAML node of type str
        return SafeConstructor.construct_yaml_str(SafeConstructor(), value)

    # Test for non-unicode values
    for nonunicode in (b'', b'String with\x00null byte', b'String with\x7Fcontrol char'):
        ansible_unicode = AnsibleConstructor.construct_yaml_str(SafeConstructor(), _create_node(nonunicode))
        assert isinstance(ansible_unicode, AnsibleUnicode)
        assert to_bytes(ansible_unicode) == nonunicode

    # Test for unicode values
    for unicode_char in (u'', u'\u20ac', u'\ud83d\ude02'):
        ansible_unicode = Ans

# Generated at 2022-06-13 07:31:20.328141
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils._text import to_bytes
    from collections import namedtuple

    FakeNode = namedtuple('FakeNode', 'start_mark')
    data = b'[1,2,3]'
    data = to_native(data)
    yaml_data = AnsibleLoader(data).get_single_data()

    constructor = AnsibleConstructor()

    yaml_seq = constructor.construct_yaml_seq(FakeNode(start_mark=1))
    assert yaml_seq.__class__.__name__ == 'AnsibleSequence'
    assert yaml_seq.ansible_pos == (None, 1, 0)
    yaml_seq.extend(yaml_data)

# Generated at 2022-06-13 07:31:30.910350
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.module_utils.six import PY3
    from ansible.parsing.vault import VaultLib

    vault_secrets = ['test']
    vault_passwords = dict(default='test')
    ac = AnsibleConstructor(vault_secrets=vault_secrets)

    if PY3:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

    # test the construct_yaml_unsafe method
    # test if the ansible construct_yaml_unsafe method can successfully parse the

# Generated at 2022-06-13 07:31:39.171568
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import datetime
    import sys
    from ansible.module_utils._text import to_text

    # The test function
    def run_test(obj):
        display.display(obj)
        s = to_text(obj)
        data = yaml.load(s, Loader=AnsibleConstructor)
        display.display(data.__class__.__name__)
        display.display(data)
        assert data.__class__ == obj.__class__
        assert data == obj

        data = yaml.load(s, Loader=AnsibleLoader)
        display.display(data.__class__.__name__)
        display.display(data)
        assert data.__class__ == obj.__class__
        assert data == obj

    # The unit test

# Generated at 2022-06-13 07:31:49.037570
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import os
    import tempfile
    import unittest
    vault_id = 'default'

# Generated at 2022-06-13 07:32:02.223257
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    class FakeNode:
        def __init__(self):
            self.start_mark = FakeMark()

    class FakeMark:
        def __init__(self):
            self.line = 3
            self.column = 4
            self.name = 'foo'

    yaml_str = u'bar'
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_scalar = lambda x: yaml_str
    ret = ansible_constructor.construct_yaml_str(FakeNode())
    assert ret == yaml_str
    assert ret.ansible_pos == ('foo', 3, 5), "Should return the right line and column"



# Generated at 2022-06-13 07:32:12.553061
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    Ansible_Constructor = AnsibleConstructor()
    # Create a sequence and a node that contains the sequence.
    test_sequence = [1,2,3]
    test_seq_node = yaml.nodes.SequenceNode(u'tag:yaml.org,2002:seq','!!python/tuple',test_sequence,None,None)
    # we don't care about the first value returned, so ignore it.
    Ansible_Constructor.construct_yaml_seq(test_seq_node)
    # The second value returned is the constructed sequence.
    test_seq_constructed = Ansible_Constructor.construct_yaml_seq(test_seq_node).next()

# Generated at 2022-06-13 07:32:21.931281
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    import copy
    import sys
    import os
    import re
    import unittest

    # Python 3.2 backwards compat
    # http://bugs.python.org/issue7980
    if sys.version_info >= (3, 3):
        if ',' not in repr(range(0)):
            raise unittest.SkipTest("This test requires that Python 3.2+ style repr() works for 'range(0)'")

    # Python 3.3
    # http://bugs.python.org/issue16454
    # Python 3.4 (and higher) is not affected.

# Generated at 2022-06-13 07:32:29.969392
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # setup
    yaml_map = MappingNode(tag=u'tag:yaml.org,2002:map',
                           value=[],
                           start_mark=None,
                           end_mark=None,
                           flow_style=None)
    ansible_constructor = AnsibleConstructor()

    # test
    assert id(ansible_constructor.construct_yaml_map(yaml_map).__next__()) == id(ansible_constructor.construct_yaml_map(yaml_map).__next__())


# Generated at 2022-06-13 07:32:35.261102
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    class TestAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            self._ansible_file_name = None
            self._vaults = {}
            self.vault_secrets = ['test']
            self._vaults['default'] = VaultLib(secrets=self.vault_secrets)

    test_vault_data = TestAnsibleConstructor()
    res = test_vault_data.construct_vault_encrypted_unicode(node=u'!vault')
    return res

# Generated at 2022-06-13 07:32:41.479844
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import textwrap
    import yaml

    obj = yaml.load(textwrap.dedent("""
    - !unsafe {a: true}
    - !unsafe '[1,2,3]'
    """))

    assert obj
    assert not isinstance(obj[0], dict)
    assert not isinstance(obj[1], list)

# Generated at 2022-06-13 07:33:04.202374
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64
    import yaml

    class FakeAnsibleConstructor(AnsibleConstructor):
        def __init__(self, file_name=None, vault_secrets=[]):
            pass
        def _node_position_info(self, node):
            return ('some file', 1, 2)

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    fake_constructor = FakeAnsibleConstructor()

    class MapNode(object):
        def __init__(self, value):
            self.value = value
            self.start_mark = ''

    class ScalarNode(object):
        def __init__(self, value):
            self.value = value
            self.start_mark = ''

    # Empty string

# Generated at 2022-06-13 07:33:12.340338
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # test no duplicate dict keys (good)
    data = '''
    a: 1
    b: 2
    '''
    x = AnsibleConstructor(file_name='/tmp/testfile')
    res = x.construct_yaml_map(yaml.nodes.MappingNode(tag=u'tag:yaml.org,2002:map', value=[], flow_style=False))
    for event in yaml.compose(yaml.parse(data, Loader=AnsibleConstructor), Loader=AnsibleConstructor):
        res.send(event)
    assert next(res) == {'a': 1, 'b': 2}

    # test duplicate dict keys (bad, only last key is used)

# Generated at 2022-06-13 07:33:21.075933
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os, sys
    sys.modules['__builtin__'].open = open
    sys.modules['yaml'] = __import__('yaml')
    import ansible.parsing.yaml.constructor as constructor

    # Load the password from vault.yml file
    vault_password = ''
    vault_yaml_path = os.path.dirname(__file__) + '/../../lib/ansible/parsing/vault/vault.yml'
    try:
        with open(vault_yaml_path, 'r') as f:
            import yaml
            vault_dict = yaml.load(f)
            vault_password = vault_dict['vault_password']
    except: pass


# Generated at 2022-06-13 07:33:28.052575
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    yaml_data = '''\
a_key: another value
a_dict:
    a: 1
    b: 2
    c: 3
'''
    yaml_data_dict = dict(a_key=u'another value',
                          a_dict=dict(a=1, b=2, c=3))
    import yaml
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    AnsibleConstructor.add_constructor(
        u'tag:yaml.org,2002:map',
        AnsibleConstructor.construct_yaml_map)

    # Test yaml without duplicate dict keys
    yaml_data_loaded = yaml.load(yaml_data, Loader=AnsibleConstructor)
    assert yaml_data_loaded == yaml_data_

# Generated at 2022-06-13 07:33:36.237370
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import sys, os
    # append module path
    my_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(my_path, '..', 'library'))
    from ansible_vault import VaultLib, VaultEditor
    import textwrap
    plaintext = u"foo\nbar\n"
    b_plaintext = plaintext.encode('utf-8')
    vault = VaultLib(password='ansible')
    b_ciphertext = vault.encrypt(b_plaintext)
    b_ciphertext = b_ciphertext.encode('utf-8')
    node_value = "!vault |\n"

# Generated at 2022-06-13 07:33:42.516792
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping

    # Test case consisting of a normal dictionary
    test_dict = dict(a=1, b=2)

    # Create a node with the given dictionary
    node = MappingNode(u'tag:yaml.org,2002:python/dict', test_dict)

    # Create an instance of AnsibleConstructor
    constructor = AnsibleConstructor()

    # Construct map from the node
    result = constructor.construct_yaml_map(node)

    # Check that we have an instance of AnsibleMapping
    assert isinstance(result, AnsibleMapping)

    # Check that we have the expected dictionary
    assert result == test_dict

    # Test case consisting of a normal dictionary with duplicate keys

# Generated at 2022-06-13 07:33:46.178277
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    yaml_str = "{a: 1, b: 2}"
    ansible_constructor = AnsibleConstructor()
    yaml_data = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert isinstance(yaml_data, AnsibleMapping)
    assert len(yaml_data) == 2
    assert yaml_data['a'] == 1
    assert yaml_data['b'] == 2

# Generated at 2022-06-13 07:33:54.405478
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys

    # Constructor for the unit test
    def construct_test(self, node):
        value = self.construct_scalar(node)
        return value

    # Add test constructor to class AnsibleConstructor
    AnsibleConstructor.add_constructor(
        u'!test',
        construct_test)

    # We must add the unit test constructor to the class AnsibleConstructor
    ansible_constructor = AnsibleConstructor()

    # Value of the node to be used on the method construct_yaml_unsafe of class AnsibleConstructor
    value = '!test abc'

    # Node to be used on the method construct_yaml_unsafe of class AnsibleConstructor

# Generated at 2022-06-13 07:34:01.539204
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml.nodes import MappingNode, ScalarNode

    vault = VaultLib()
    vault.secrets = ['1234']
    ansible_constructor = AnsibleConstructor(vault_secrets=['1234'])
    ansible_constructor._vaults['default'] = vault

    ciphertext = vault.encrypt(b'foo')
    my_unencrypted_value = ansible_constructor.construct_vault_encrypted_unicode(ScalarNode(tag=u"tag:yaml.org,2002:str", value=ciphertext, start_mark=None, end_mark=None,
                                                                                              style=None))
    assert my_unencrypted_value == b'foo'

# Generated at 2022-06-13 07:34:10.117320
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], start_mark=None, end_mark=None)
    constructor = AnsibleConstructor(file_name=None, vault_secrets=None)
    generator = constructor.construct_yaml_map(node)
    result = next(generator)
    assert isinstance(result, AnsibleMapping)

# Generated at 2022-06-13 07:34:41.900792
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import ansible.parsing.yaml.objects
    assert issubclass(ansible.parsing.yaml.objects.AnsibleMapping, dict)
    assert issubclass(ansible.parsing.yaml.objects.AnsibleSequence, list)

# Generated at 2022-06-13 07:34:49.768360
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    # test using the default vault
    from ansible.parsing.vault import VaultLib, VaultSecret, VaultPassword

    password_file = '/tmp/passwordfile'
    password = 'secret'
    with open(password_file, 'w') as f:
        f.write(str(password))

    vault_secret = VaultSecret(VaultPassword(password_file))
    # Empty vault dictionary
    vault = VaultLib(secrets=[vault_secret])

    # Init vault
    cipher_text = vault.encrypt('test')
    # Create node
    node = '!vault %s' % cipher_text

    constructor = AnsibleConstructor()

    # create !vault-encrypted yaml node
    ret = constructor.construct_yaml_unsafe(node)

    # Check the value
    assert ret.decrypt()

# Generated at 2022-06-13 07:34:53.499534
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping

    constructor = AnsibleConstructor()
    assert isinstance(constructor.construct_yaml_map(None), AnsibleMapping)


# Generated at 2022-06-13 07:35:00.575247
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_yaml = """
first_run:
- name: 'New user'
  state: present
  name: new_user
  password: 'pwd'
- name: 'Enable User'
  state: present
  name: enable_user
  password: 'pwd'
"""
    # TODO: Find out more about the file name
    c = AnsibleConstructor()
    result = c.construct_yaml(test_yaml)["first_run"]
    print("First run:")
    print(result)
    print("\n")
    print("Second run:")

# Generated at 2022-06-13 07:35:10.963532
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    node = type('',(object,),{
        'start_mark': None,
        'construct_scalar': lambda self, node : 'ciphertet'
        })()
    vault = type('',(object,),{
        'decrypt': lambda x, y : 'plaintext'
        })()
    vault.secrets = ['password']
    constructor = type('',(object,),{
        '_vaults': {'default': vault}
        })()
    constructor.vault_secrets = ['password']
    pos = (1, 2, 3)
    constructor._node_position_info = lambda self, node : pos
    expect = AnsibleVaultEncryptedUnicode('plaintext')
    expect.vault = vault
    expect.ansible_pos = pos
    assert constructor.construct_vault_

# Generated at 2022-06-13 07:35:18.929899
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import datetime
    import os.path
    import yaml

    class MyAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            super(MyAnsibleConstructor, self).__init__()
            self.vault_secrets = ['password']

    ansible_constructor = MyAnsibleConstructor()


# Generated at 2022-06-13 07:35:32.648068
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    class Fake_construct_scalar:
        def __init__(self, ciphertext, version=1):
            self.ciphertext = ciphertext
            self.version = version

    class Fake_VaultLib:
        def __init__(self, secrets):
            self.secrets = secrets

    class Fake_AnsibleVaultEncryptedUnicode:
        def __init__(self, ciphertext, version=1):
            self.ciphertext = ciphertext
            self.version = version
            self.vault = None

    password_file_name = 'fakepass'
    fake_vault_secrets = ['fakesecret']

    class Fake_AnsibleConstructor:
        def __init__(self):
            self._vaults = {}
            self.vault_secrets = fake_vault_secrets

# Generated at 2022-06-13 07:35:35.396937
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ansible_constructor = AnsibleConstructor()
    yaml_str = ansible_constructor.construct_yaml_str('a string')
    assert isinstance(yaml_str, AnsibleUnicode), 'construct_yaml_str() should return AnsibleUnicode objects'

# Generated at 2022-06-13 07:35:38.590582
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    # test variables
    ansible_constructor = AnsibleConstructor()

    # test functions
    vault_node = AnsibleVaultEncryptedUnicode('123456')
    assert ansible_constructor.construct_vault_encrypted_unicode(vault_node) == '123456'

# Generated at 2022-06-13 07:35:43.450919
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    node = yaml.nodes.ScalarNode('test', 'test')
    constructor = AnsibleConstructor()
    res = constructor.construct_yaml_str(node)
    assert res == u'test'

# Generated at 2022-06-13 07:36:20.494417
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # test_AnsibleConstructor_construct_yaml_unsafe: Test the construct_yaml_unsafe method of the AnsibleConstructor class

    constructor = AnsibleConstructor()
    node = type("Node", (object,), {
        "id": None,
        "start_mark": type("node_mark", (object,), {
            "line": 0,
            "column": 0
        })()
    })
    constructor.construct_object = lambda node: "Hello"
    actual = constructor.construct_yaml_unsafe(node)

    assert actual == "Hello"

# Generated at 2022-06-13 07:36:21.733971
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    assert AnsibleConstructor().construct_yaml_unsafe({'id': 'list'}) == wrap_var([])

# Generated at 2022-06-13 07:36:28.439166
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    import base64
    vault_secrets = ["hello"]
    ac = AnsibleConstructor(file_name="ansible.yml", vault_secrets=vault_secrets)
    vault_data = VaultLib(secrets=vault_secrets)
    # re-used in a later test
    b_plaintext_data = b"plaintext"
    b_ciphertext_data = vault_data.encrypt(b_plaintext_data)
    s_ciphertext_data = base64.b64encode(b_ciphertext_data)

# Generated at 2022-06-13 07:36:37.237724
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(b'hello')
    constructor = AnsibleConstructor(vault_secrets=['secret'])
    vault = constructor._vaults["default"]
    node = loader.get_single_node()

    ret = constructor.construct_vault_encrypted_unicode(node)

    assert ret.vault == vault, 'constructor.construct_vault_encrypted_unicode: vault != vault'
    assert ret == 'hello', 'constructor.construct_vault_encrypted_unicode: ret != hello'
    assert ret.ansible_pos == ('', 1, 1), 'constructor.construct_vault_encrypted_unicode: ret.ansible_pos != ("", 1, 1)'

# Generated at 2022-06-13 07:36:48.302080
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    constructor = AnsibleConstructor()
    node = "1"
    expected_result = u'1'
    actual_result = constructor.construct_yaml_str(node)
    assert isinstance(actual_result, AnsibleUnicode), \
        'Expected AnsibleUnicode but found {0}'.format(type(actual_result))
    assert actual_result == expected_result, 'Expected {0} but found {1}'.format(expected_result, actual_result)

    node = u"1"
    expected_result = u'1'
    actual_result = constructor.construct_yaml_str(node)
    assert isinstance(actual_result, AnsibleUnicode), \
        'Expected AnsibleUnicode but found {0}'.format(type(actual_result))

# Generated at 2022-06-13 07:36:52.947558
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import os
    import sys
    import yaml
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    password = 'supersecret'
    vault = VaultLib(password)
    vault_data = 'supersecretvaultsecret'
    data = vault.encrypt(vault_data)
    myyaml = u'!vault |\n  %s' % to_unicode(data)
    ansible_constructor

# Generated at 2022-06-13 07:37:07.752968
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor(None)
    ansible_constructor.vault_secrets = ['password']
    vault = VaultLib(secrets=ansible_constructor.vault_secrets)

# Generated at 2022-06-13 07:37:17.477034
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # assert that testing is enabled
    vault_secrets = ['secret1']
    ac = AnsibleConstructor(vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:37:29.170111
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # the question of whether or not this test is valid is complex.
    # In general, the return value of construct_vault_encrypted_unicode
    # is supposed to be an AnsibleVaultEncryptedUnicode object, which it
    # isn't in this test.  The reason for this is that AnsibleVaultEncryptedUnicode
    # doesn't exist when this test is run.  I would say that the test is probably
    # valid because the object returned is at least of the right class.  A better test
    # is probably something like test_vault_crypto, which tests the decryption algorithm.

# Generated at 2022-06-13 07:37:37.966542
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml.nodes import SequenceNode, ScalarNode
    from yaml.composer import Composer
    from yaml.resolver import Resolver
    node = SequenceNode(tag="tag:yaml.org,2002:seq",
                        value=[ScalarNode(tag="tag:yaml.org,2002:int",
                                          value="1")],
                        start_mark=None,
                        end_mark=None,
                        flow_style=None)
    ac = AnsibleConstructor(None)
    r = Resolver(Resolver.DEFAULT_MAPPING_TAG)
    c = Composer(node, r)
    seq = ac.construct_yaml_seq(node).next()
    seq = c.construct_sequence(node)
    print(seq)
    assert len(seq) is 1
   