

# Generated at 2022-06-13 07:28:14.840010
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:28:26.009962
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from yaml import nodes
    from ansible.parsing.yaml.loader import AnsibleLoader
    """
    This function test the method construct_vault_encrypted_unicode of AnsibleConstructor class.
    It verifies the behavior of this method.
    """
    test_ansible_object = AnsibleConstructor()

# Generated at 2022-06-13 07:28:34.377360
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:28:40.201747
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    stream = u"""
- {foo: 1, bar: 2}
- [1, 2, 3]
- foo
- bar
"""
    result = list(yaml.load_all(stream, Loader=AnsibleConstructor))

    assert result[0]['foo'] == 1
    assert result[0]['bar'] == 2

    assert result[1] == [1, 2, 3]

    assert result[2] == 'foo'
    assert result[3] == 'bar'

# Unit tests for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:28:53.032626
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import ansible.parsing.yaml.loader as loader
    import ansible.parsing.yaml.objects as objects
    import ansible.parsing.yaml.dumper as dumper
    import ansible.parsing.vault as vault

    ansible_constructor = AnsibleConstructor(vault_secrets=['password'])
    ansible_constructor.vault_secrets
    # 'Hello!' is converted to a unicode string and added to a set
    node = objects.AnsibleVaultEncryptedUnicode(b'Hello!')
    node = ansible_constructor.construct_vault_encrypted_unicode(node)

    assert isinstance(node, objects.AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 07:29:00.499604
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    # to test _node_position_info

# Generated at 2022-06-13 07:29:14.430595
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Arrange
    class MockVaultLib(VaultLib):
        def __init__(self):
            pass

        def decrypt(self, ciphertext_data):
            return ciphertext_data

        def create_encrypted_text(self, b_plaintext_data):
            return b_plaintext_data


# Generated at 2022-06-13 07:29:23.063721
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    yaml_str = '''
    - shell: ls /usr/bin/python
      args:
        executable: !unsafe "/usr/bin/python3.5"
    - shell: ls /usr/bin/python
      args:
        executable: !unsafe "/usr/bin/python2.7"
    '''
    ret = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert ret[0]['args']['executable'] == '/usr/bin/python3.5'
    assert ret[1]['args']['executable'] == '/usr/bin/python2.7'

# Generated at 2022-06-13 07:29:28.839664
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    c = AnsibleConstructor()
    n = m = yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'foo')

    assert c.construct_yaml_str(n) == u'foo'
    assert yaml.load(u'foo') == 'foo'
    assert yaml.load(u'foo', Loader=AnsibleLoader) == u'foo'
    assert yaml.load(u'foo', Loader=AnsibleLoader).__class__ == AnsibleUnicode

    # FIXME: correct test for construct_yaml_unsafe and construct_vault_encrypted_unicode
    #assert yaml.load(u'!unsafe foo', Loader=AnsibleLoader) == u'foo'
    #assert yaml.load(

# Generated at 2022-06-13 07:29:38.758554
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():

    c = AnsibleConstructor()

    # test whether we get the original value back
    node = type('', (), {'tag': u'tag:yaml.org,2002:python/bytes', 'value': b'\x00\x01\x02\x03\x04'})
    assert id(node.value) == id(c.construct_yaml_unsafe(node))

    # test whether we get the original value back
    node = type('', (), {'tag': u'tag:yaml.org,2002:python/int', 'value': 42})
    assert id(node.value) == id(c.construct_yaml_unsafe(node))

# Generated at 2022-06-13 07:29:52.798300
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    test_string = u'foo'
    test_constructor = AnsibleConstructor()
    result = yaml.dump(test_string, Dumper=yaml.SafeDumper, default_style=None, default_flow_style=None, default_constructor=test_constructor.construct_yaml_str)
    expected_result = u'foo\n...\n'
    assert result == expected_result, 'Start and End Markers should be added for a string value'

# Generated at 2022-06-13 07:30:03.977240
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml.parser import Parser
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:30:13.064422
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    """Test AnsibleConstructor.construct_yaml_map()"""
    from yaml.nodes import MappingNode
    from yaml.parser import ParserError
    from yaml.reader import Reader
    from yaml.scanner import ScannerError
    from yaml.error import YAMLError


# Generated at 2022-06-13 07:30:23.512953
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import tempfile
    import ruamel.yaml as yaml

    # ConstructorError is in yaml.constructor.ConstructorError
    # pylint: disable=no-member

    # Before we start, we read the expected error message from a temporary file.
    # This is necessary, because Python 3.2 on Windows prints an error message
    # using backslash as path separator in the error message, even if the
    # path separator is forward slash (probably a bug in Python).
    # We read the error message from the tempfile to avoid the inconsistency.
    expected_error = None
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("'While constructing a mapping from {1}, line {2}, column {3}'\n")
       

# Generated at 2022-06-13 07:30:27.891590
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import os
    myVar={'key1':'val1','key2':'val2','key3':'val3'}

    #Test code starts here for method construct_yaml_map

    yaml_test = AnsibleConstructor(file_name='my_file_name')
    d = yaml_test.construct_yaml_map('myVar')
    assert isinstance(d, AnsibleMapping)

# Generated at 2022-06-13 07:30:31.567924
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # since 'construct_yaml_seq' is a generator, we have to use 'next'
    # to actually execute it
    class FakeNode(object):
        def __init__(self):
            self.value = 'foobar'
    node = FakeNode()
    ac = AnsibleConstructor()
    seq = ac.construct_yaml_seq(node)
    data = next(seq)
    assert data == 'foobar'

# Generated at 2022-06-13 07:30:42.167457
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['f00b4r']
    ac = AnsibleConstructor(vault_secrets=vault_secrets)
    # This string is what we expect to be returned from a ansible-vault encrypted variable

# Generated at 2022-06-13 07:30:43.894649
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # TODO: write some tests
    pass

# Generated at 2022-06-13 07:30:51.591561
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Test the constructor with a regular string
    test_node_string = u'AnsibleConstructorTestString'

    ansible_constructor = AnsibleConstructor()
    ansible_string = ansible_constructor.construct_vault_encrypted_unicode(test_node_string)
    assert isinstance(ansible_string, AnsibleVaultEncryptedUnicode)
    assert ansible_string == u'AnsibleConstructorTestString'

    # Test the constructor with a unicode string
    test_node_string_unicode = u'AnsibleConstructorTest\u00FCString'

    ansible_string_unicode = ansible_constructor.construct_vault_encrypted_unicode(test_node_string_unicode)

# Generated at 2022-06-13 07:30:57.860883
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml
    construct_yaml_seq = AnsibleConstructor().construct_yaml_seq

    assert construct_yaml_seq(yaml.nodes.SequenceNode(
        u'tag:yaml.org,2002:seq',
        [yaml.nodes.ScalarNode(u'foo', u'foo')],
        None, None
    )) == [u'foo']

# Generated at 2022-06-13 07:31:10.178995
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ac = AnsibleConstructor(file_name='file/name', vault_secrets=['my_secret'])
    node = MappingNode(tag='vault', value=[(ScalarNode(
        tag='vault-encrypted', value='$ANSIBLE_VAULT;1.2;AES;something'), 'value'), ('key', ScalarNode(tag='vault-encrypted', value='$ANSIBLE_VAULT;1.2;AES;something'))],
                       start_mark=None, end_mark=None, flow_style=False)
    ansible_vault_encrypted_unicode = ac.construct_vault_encrypted_unicode(node)
    assert isinstance(ansible_vault_encrypted_unicode, AnsibleVaultEncryptedUnicode)
    assert ansible_vault_encrypted_unicode

# Generated at 2022-06-13 07:31:16.474972
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[], anchor=None, index=None, head=True)
    ansibleConstructor = AnsibleConstructor()
    assert ansibleConstructor.construct_mapping(node) == AnsibleMapping()
    ansibleConstructor = AnsibleConstructor(C.DEFAULT_VAULT_PASSWORD_FILE)
    assert ansibleConstructor.construct_mapping(node) == AnsibleMapping()

# Generated at 2022-06-13 07:31:23.500072
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    class Loader(yaml.constructor.SafeConstructor):
        def construct_yaml_map(self, node):
            data = AnsibleMapping()
            yield data
            value = self.construct_mapping(node)
            data.update(value)
            data.ansible_pos = (node.start_mark.name, node.start_mark.line + 1, node.start_mark.column + 1)

    def check(s, expected):
        assert yaml.load(s, Loader) == expected

    check("{a: 1, b: 2, c: 3}", AnsibleMapping(a=1, b=2, c=3))

# Generated at 2022-06-13 07:31:33.709635
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader(None, {'file_name': 'test'})
    test_object = AnsibleBaseYAMLObject()
    test_object.ansible_pos = ('test', 1, 1)
    test_object2 = AnsibleBaseYAMLObject()
    test_object2.ansible_pos = ('test2', 1, 1)
    yaml_map = AnsibleMapping()
    yaml_map['test_object'] = test_object
    yaml_map['test_object2'] = test_object2
    result = loader.construct_yaml

# Generated at 2022-06-13 07:31:34.291615
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    pass

# Generated at 2022-06-13 07:31:38.671827
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

    yaml_data = '''
    foo:
        bar: 1
        bar: 2
    '''

    yaml_obj = AnsibleConstructor(file_name=None)
    data = yaml.load(yaml_data, Loader=yaml_obj)
    assert data.has_key('foo')
    assert data['foo'].has_key('bar')
    assert data['foo']['bar'] == 2

# Generated at 2022-06-13 07:31:48.813641
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

    from ansible.parsing.yaml.objects import AnsibleMapping

    tests = {
        "{'a': 1, 'c': 2, 'b': 2}": AnsibleMapping({'a': 1, 'c': 2, 'b': 2}, 0, 3),
        "{'a': 1, 'b': 2, 'c': 2}": AnsibleMapping({'a': 1, 'b': 2, 'c': 2}, 0, 3),
        "{'a': 1, 'b': 2}": AnsibleMapping({'a': 1, 'b': 2}, 0, 2),
        "{'a': 1, 'a': 2}": AnsibleMapping({'a': 2}, 0, 2),
    }

    for input, expected in tests.items():
        yaml_constructed = yaml

# Generated at 2022-06-13 07:32:03.864217
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from yaml import load, dump
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    vault = VaultLib(password_file=False)
    loader.set_vault_secrets([vault])


# Generated at 2022-06-13 07:32:10.008006
# Unit test for method construct_yaml_seq of class AnsibleConstructor

# Generated at 2022-06-13 07:32:16.286310
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    result = AnsibleLoader(stream="!unsafe ''").get_single_data()
    assert isinstance(result, AnsibleUnsafeText)

    # testing with the default "construct_" method
    result = AnsibleLoader(stream="!!python/unicode ''").get_single_data()
    assert not isinstance(result, AnsibleUnsafeText)

# Generated at 2022-06-13 07:32:34.245898
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from yaml import SafeLoader
    from yaml.nodes import MappingNode
    from yaml.composer import Composer
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    # Setup YAML mapping
    mapping = {
        "mav": "may",
        "mav1": wrap_var("may1"),
        "mav2": wrap_var("may2"),
        "mav3": wrap_var("may3")
    }
    node = MappingNode(u'tag:yaml.org,2002:map', mapping, None, None, True)

    # Call AnsibleConstructor.construct_yaml_map(self, node):
    constructor = AnsibleConstructor()
   

# Generated at 2022-06-13 07:32:45.861280
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import os
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)
    from yaml import safe_dump
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    dataloader = DataLoader()
    assert isinstance(dataloader.load("!unsafe {'unsafe key': 'unsafe value'}"), dict)

# Generated at 2022-06-13 07:32:51.000137
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    ansible_constructor = AnsibleConstructor()
    class Node:
        id = None

    assert ansible_constructor.construct_yaml_unsafe(
        Node()) == wrap_var(None)

    assert ansible_constructor.construct_yaml_unsafe(
        Node()) == wrap_var(None)

    assert ansible_constructor.construct_yaml_unsafe(
        Node()) == wrap_var(None)



# Generated at 2022-06-13 07:32:55.001353
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    data = b'Hello World!'
    yaml_data = yaml.load(data)
    if not isinstance(yaml_data, AnsibleUnicode):
        raise AssertionError('%s is not an AnsibleUnicode' % (yaml_data,))


# Generated at 2022-06-13 07:32:56.112541
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # TODO: add a test
    assert True



# Generated at 2022-06-13 07:33:03.046926
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:33:11.693333
# Unit test for method construct_yaml_map of class AnsibleConstructor

# Generated at 2022-06-13 07:33:18.837227
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['random', 'string']
    a = AnsibleConstructor(vault_secrets=vault_secrets)
    ret = a.construct_vault_encrypted_unicode('')
    assert ret.decrypt == a._vaults['default'].decrypt
    assert ret.vault == a._vaults['default']

# Generated at 2022-06-13 07:33:26.148128
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    text = '''
a:
- 1
- 2
- 3
- 4
b:
- a
- b
- c
c:
- 1
- 2
- 3
d:
- 1
- 2
- 3
'''
    yaml.load(text, Loader=AnsibleConstructor)
    try:
        yaml.load(text, Loader=AnsibleConstructor)
    except ConstructorError as e:
        print(e.problem)


if __name__ == '__main__':
    import yaml

    test_AnsibleConstructor_construct_mapping()

# Generated at 2022-06-13 07:33:34.796215
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    from collections import OrderedDict
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class TestAnsibleConstructor(AnsibleConstructor):
        def __init__(self, file_name=None, vault_secrets=None):
            self._ansible_file_name = file_name
            super(TestAnsibleConstructor, self).__init__()
            self._vaults = {}
            self.vault_secrets = vault_secrets or []
            self._vaults['default'] = VaultLib(secrets=self.vault_secrets)

        def _node_position_info(self, node):
            return ("test_filename", 1, 1)

    class TestVaultLib(VaultLib):
        def __init__(self, secrets=None):
            super

# Generated at 2022-06-13 07:33:54.543423
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    import sys
    vault_password = u"test"
    file_name = u"testyaml"
    # We should be able to decrypt this using the default vault
    # encryption key

# Generated at 2022-06-13 07:33:58.934423
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    yaml_snippet = "!unsafe 'password'"
    # Create a node for the !unsafe tag and call the constructor
    y = yaml.compose(yaml_snippet)
    yaml_node = y.get_node()
    ac = AnsibleConstructor()
    ret = ac.construct_yaml_unsafe(yaml_node)
    assert ret == 'password'

# Generated at 2022-06-13 07:34:14.306238
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    node = yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', [])

    # Case 1.1 - Construct Mapping Node with a duplicate key - in this case we should raise an exception
    # Case 1.2 - Construct Mapping Node with a non duplicate key - in this case we should not raise an exception

    # Case 1.1

# Generated at 2022-06-13 07:34:23.640881
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import time
    import os

    # Generate a temporary vault password file
    vault_secrets = []
    secrets_1 = b'test_vault_secret_1'
    secrets_2 = b'test_vault_secret_2'
    secrets_3 = b'test_vault_secret_3'
    vault_secrets.append(secrets_1)
    vault_secrets.append(secrets_2)
    vault_secrets.append(secrets_3)

    vault = VaultLib(secrets=vault_secrets)

# Generated at 2022-06-13 07:34:24.469532
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    pass



# Generated at 2022-06-13 07:34:34.029697
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    import yaml
    password = '12345'
    secret = [password]
    vault = VaultLib(secrets=secret)
    string = "Hello world"
    encrypted_string = vault.encrypt(string)
    yaml_string = '!vault |\n          %s' % encrypted_string.decode('utf8')
    yaml_node = yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value=yaml_string)
    string_decrypted = AnsibleConstructor(vault_secrets=secret).construct_vault_encrypted_unicode(yaml_node)
    assert string == string_decrypted.decrypt()

# Generated at 2022-06-13 07:34:45.299337
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:34:48.292029
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml = b'{ "variable": "value" }'
    yaml_obj = AnsibleConstructor().get_single_data(yaml)
    assert isinstance(yaml_obj, dict)
    assert yaml_obj['variable'] == 'value'


# Generated at 2022-06-13 07:34:58.193771
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    class MockNode:
        def __init__(self, cont):
            self.start_mark = self
            self.end_mark = self
            self.value = cont
            self.tag = u'tag:yaml.org,2002:str'

        def __repr__(self):
            return repr(self.value)

        def __add__(self, other):
            return repr(self.value) + repr(other.value)

        def __eq__(self, other):
            return repr(self.value) == repr(other.value)

    class MockVault:
        def __init__(self, secrets=None):
            self.secrets = secrets

    vault = MockVault()
    construct_vault_encrypted_unicode = AnsibleConstructor(vault_secrets=[u'test']).construct_

# Generated at 2022-06-13 07:35:05.899717
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.plugins.vars.vault import VaultLib
    ciphertext = VaultLib().encrypt('secret')
    data = '!vault |\n          ' + ciphertext
    loader = AnsibleLoader(data, variable_start_string='{{', variable_end_string='}}')
    data = loader.get_single_data()
    assert data == 'secret'


# Generated at 2022-06-13 07:35:37.160555
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import ansible.parsing.yaml.loader as yaml_loader
    import ansible.errors as errors
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode, AnsibleSequence

    vault_secrets = [b'secret1', b'secret2']
    yaml_1 = """\
        a: 1
        b: 2
        c: 3
    """
    loader = yaml_loader.AnsibleLoader(yaml_1, 'memory', vault_secrets=vault_secrets)
    # Test AnsibleConstructor.__init__()
    assert isinstance(loader.constructor._vaults['default'], VaultLib)

# Generated at 2022-06-13 07:35:49.464674
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import BytesIO
    import yaml
    safe_constructor = AnsibleConstructor(file_name="test")
    safe_constructor.vault_secrets = [b"abc"]

# Generated at 2022-06-13 07:35:53.968544
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import yaml
    from io import BytesIO

    # Don't pollute the real sys.stderr
    fake_stderr = BytesIO()
    real_stderr = sys.stderr

# Generated at 2022-06-13 07:36:04.807239
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    v = VaultLib()

    vault_password = VaultLib.create_vault_password('test', 1)
    plaintext_data = "dummy"
    ciphertext_data = v.encrypt(vault_password, plaintext_data)
    ac = AnsibleConstructor(file_name='/dev/null', vault_secrets=[vault_password])
    node = SafeConstructor.construct_yaml_str(node=None, value=ciphertext_data)
    ciphertext_data_as_AnsibleVaultEncryptedUnicode = ac.construct_vault_encrypted_unicode(node)
    assert ciphertext_data_as_AnsibleVaultEncryptedUnicode.vault.secrets[0] == vault_password

# Generated at 2022-06-13 07:36:16.751923
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    # set up the test
    example_data = 'AES256d:UUl6eW4KU1VMRUExAWIQSxV7zDQS5YBkLfQKauw5AOEbBOMdzV7Kj' \
        'MQyMtrts/5oBEif5K/0/7ZR5JZp49amN1KkJ99DP3qPJl9Kj6Y+UdOsiM6VF4Z4kLCijVuO' \
        'VbHXz334gcFvy+gYvcwBKjWZ+QEJlTkTgcbjKkTl+rnnpfMNVJn3Ew=='
    example_expected_ciphertext = 'password'



# Generated at 2022-06-13 07:36:23.851589
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml

    from io import BytesIO

    # Simple mapping
    yaml_str = b'{ w: ww\n, x: xx\n, y: yy\n, z: zz\n }'
    yaml_obj = yaml.load(yaml_str, Loader=AnsibleConstructor)
    assert yaml_obj == {'w': 'ww', 'x': 'xx', 'y': 'yy', 'z': 'zz'}

    # Mapping with duplicate keys
    yaml_str = b'{ w: ww\n, x: xx\n, y: yy\n, x: xx\n }'
    yaml_obj = yaml.load(yaml_str, Loader=AnsibleConstructor)

# Generated at 2022-06-13 07:36:29.788144
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    # Save current version_info
    vi = sys.version_info
    # Constructor tests
    c = AnsibleConstructor()
    # Test case : Python 3.x
    if sys.version_info.major >= 3:
        # Test !unsafe
        result = c.construct_yaml_unsafe(node=False)
        assert isinstance(result, bool)
        # Test !python/bool
        result = c.construct_yaml_unsafe(node=True)
        assert isinstance(result, bool)
        # Test !python/int
        result = c.construct_yaml_unsafe(node=1)
        assert isinstance(result, int)
        # Test !python/long

# Generated at 2022-06-13 07:36:37.892383
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Initialize
    test_yaml_str = '''
        a: 1
        b: 2
        c: 3
        c: 4  # Will be discarded
        a: 5  # Will be discarded
    '''
    test_yaml_data = ruamel.yaml.load(test_yaml_str, Loader=ruamel.yaml.Loader)
    # Default: No warning/error
    ac = AnsibleConstructor()
    test_mapping = ac.construct_mapping(test_yaml_data)
    assert isinstance(test_mapping, ruamel.yaml.comments.CommentedMap)
    assert test_mapping['a'] == 5
    assert test_mapping['b'] == 2
    assert test_mapping['c'] == 4
    # Warn
    ac = AnsibleConstructor

# Generated at 2022-06-13 07:36:48.553955
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing import vault

    # two unequal dictionaries, for equality testing
    test_dict_1 = dict(foo=dict(bar='some_value'), numbers=list(range(10)))
    test_dict_2 = dict(foo=dict(bar='some_other_value'),
                       numbers=list(range(9)) + [10])

    # two unequal lists, for equality testing
    test_list_1 = list(range(10))
    test_list_2 = list(range(10))

    # test the constructor
    ac = AnsibleConstructor()
    wrapped_dict_1 = ac.construct_yaml_unsafe(test_dict_1)
    wrapped_dict_2 = ac.construct_yaml_unsafe(test_dict_2)
    wrapped_list_1 = ac.construct_y

# Generated at 2022-06-13 07:36:58.762574
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from pytest import raises


# Generated at 2022-06-13 07:37:58.224586
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from yaml.nodes import MappingNode
    from yaml.constructor import ConstructorError

    # test assert that mapping node is passed
    with pytest.raises(ConstructorError):
        AnsibleConstructor().construct_yaml_map("foobar")

    # test that _node_position_info() is called
    node = MappingNode(None, None, flow_style=False)
    ac = AnsibleConstructor()
    ac._node_position_info = MagicMock(return_value='foobar')
    ac.construct_yaml_map(node)
    ac._node_position_info.assert_called_once_with(node)

    # test that the value attribute of mapping is not changed
    expected = {'a': 'b'}
    data = AnsibleMapping({'a': 'z'})