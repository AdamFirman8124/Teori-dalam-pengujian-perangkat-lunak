

# Generated at 2022-06-13 07:38:43.417857
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''Test the loader for AnsibleLoader'''
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:38:46.454483
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """Unit test for constructor of class AnsibleLoader."""
    stream = open('test/unit/parsing/yaml/data/load.yaml')
    file_name = stream.name
    vault_secrets = None
    loader = AnsibleLoader(stream, file_name, vault_secrets)
    assert loader is not None

# Generated at 2022-06-13 07:38:55.975565
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import unittest

    class TestAnsibleLoader(unittest.TestCase):

        def setUp(self):
            self.loader = AnsibleLoader(None)

        def tearDown(self):
            self.loader = None

        def test_init(self):
            self.assertIsInstance(self.loader, AnsibleLoader)
            self.assertIsInstance(self.loader, Reader)
            self.assertIsInstance(self.loader, Scanner)
            self.assertIsInstance(self.loader, Parser)
            self.assertIsInstance(self.loader, Composer)
            self.assertIsInstance(self.loader, AnsibleConstructor)
            self.assertIsInstance(self.loader, Resolver)

    test_suite = unittest.TestSuite()
    test_

# Generated at 2022-06-13 07:39:02.146932
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def check(data, expected):
        loader = AnsibleLoader(data, vault_secrets=[])
        actual = loader.get_single_data()
        assert expected == actual

    data = '{key: {subkey: value}}'
    check(data, {'key': {'subkey': 'value'}})


# Generated at 2022-06-13 07:39:12.878711
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.scanner import ScannerError
    from yaml.parser import ParserError
    from ansible.parsing.yaml.constructor import AnsibleConstructorError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    class VaultSecret(object):
        def __init__(self, password, filename=None):
            self.password = password
            self.filename = filename

    def _test_loader(data, loader_class=AnsibleLoader, expected=None, expected_error=None):
        """
        Runs a test in a deterministic way to have exact same test outputs
        """
        import os
        import sys



# Generated at 2022-06-13 07:39:21.048381
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # import sys
    # from io import StringIO
    # from yaml import load
    # from yaml.dumper import SafeDumper
    #
    # # fake stdin
    # sys.stdin = StringIO(u'\n'.join(sys.argv[1:]))
    #
    # al = AnsibleLoader(sys.stdin)
    #
    # # Ensure AnsibleVaultEncryptedUnicode is treated as a scalar
    # safe_dumper = SafeDumper
    # safe_dumper.ignore_aliases = lambda self, data: isinstance(data, AnsibleVaultEncryptedUnicode)
    #
    # sys.stdout.write(safe_dumper.dump(al.

# Generated at 2022-06-13 07:39:26.912419
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    contents = """
    ---
    - hosts: all
      gather_facts: False
      tasks:
        - debug:
            msg: hello world
    """
    import io
    stream = io.BytesIO(contents)
    a = AnsibleLoader(stream)
    st = a.get_single_data()
    assert st[0]['hosts'] == 'all'
    assert st[0]['tasks'][0]['debug']['msg'] == 'hello world'

# Generated at 2022-06-13 07:39:34.381274
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data =  '''
        - hosts: localhost
          tasks:
          - name: test
            command: /bin/false
    '''
    yaml_data = AnsibleLoader(data)
    assert(yaml_data[0]['hosts'] == 'localhost')
    assert(yaml_data[0]['tasks'][0]['name'] == 'test')

# Generated at 2022-06-13 07:39:36.522790
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert hasattr(loader, '_ansible_get_constructor')

# Generated at 2022-06-13 07:39:41.648672
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys, os

    loader = AnsibleLoader(open(sys.argv[1], 'r'))
    data = loader.get_single_data()

    if HAS_LIBYAML:
        from yaml import dump
        print(dump(data, explicit_start=True, indent=2, default_flow_style=False))
    else:
        import pprint
        pprint.pprint(data)

# Generated at 2022-06-13 07:39:50.465407
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class DummyVaultSecret:
        def __init__(self, password):
            self.password = password
        def decode(self, text):
            return text

    class DummyLoader:
        pass

    # Case 1:
    # file_name is None, vault_secrets is None
    try:
        AnsibleLoader(DummyLoader())
        assert False
    except AttributeError:
        assert True

    # Case 2:
    # file_name is not None, vault_secrets is None
    try:
        AnsibleLoader(DummyLoader(), 'test.yml')
        assert False
    except AttributeError:
        assert True

    # Case 3:
    # file_name is None, vault_secrets is not None

# Generated at 2022-06-13 07:40:01.569046
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class Test_AnsibleLoader(AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            AnsibleLoader.__init__(self, stream, file_name=file_name, vault_secrets=vault_secrets)

    class Test_Reader(Reader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Reader.__init__(self, stream)

    class Test_Scanner(Scanner):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Scanner.__init__(self)

    class Test_Parser(Parser):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Parser

# Generated at 2022-06-13 07:40:12.126719
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleMapping
    from io import StringIO
    import os

    p = VaultLib(password_file=os.path.join(os.path.dirname(__file__), "./test_vault.pwd"))

    # Test AnsibleConstructor

# Generated at 2022-06-13 07:40:24.043842
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io
    import os
    import tempfile

    filename = None
    a = u'\u1234'
    b = u'\u5678'

    string = '''\
- a: %s
- b: %s
''' % (a, b)

    if sys.version_info.major == 2:
        fd, filename = tempfile.mkstemp()
        f = os.fdopen(fd, 'w')
    else:
        f = io.StringIO()

    f.write(string)
    f.flush()
    f.seek(0)

    l = AnsibleLoader(f, file_name=filename)
    l.dispose()

    if sys.version_info.major == 2:
        f.close()
        os.remove(filename)

   

# Generated at 2022-06-13 07:40:32.204717
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    import StringIO

    vault_pass = '$argon2i$v=19$m=102400,t=10,p=6$5UOfjFz+0XRxZDW0ygDhWA$LJ8YwYOyaOQ2GHA+cWJ9XqO3qFbWM7Iz1G4FVyJwA4E'
    sio = StringIO.StringIO()
    sio.write('$ANSIBLE_VAULT;1.1;AES256\n')

# Generated at 2022-06-13 07:40:35.066784
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    code = """
    - "test"
    """

    result = AnsibleLoader(code).get_single_data()
    assert result == ["test"]

# Generated at 2022-06-13 07:40:44.759036
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import HAS_LIBYAML
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from io import StringIO
    import yaml

# Generated at 2022-06-13 07:40:47.222965
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:40:48.863961
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    bytes = AnsibleLoader(None)
    assert bytes is not None

# Generated at 2022-06-13 07:40:54.442076
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Parser)
    assert AnsibleLoader.yaml_constructors == AnsibleConstructor.yaml_constructors
    assert AnsibleLoader.yaml_multi_constructors == AnsibleConstructor.yaml_multi_constructors


if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-13 07:41:10.628613
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile

    # Testing vault decryption, see ansible.parsing.yaml.objects
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:41:13.034218
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('')
    assert isinstance(loader, AnsibleConstructor)

# Generated at 2022-06-13 07:41:23.602748
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test with a generic YAML file w/o a script tag
    test_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_file_nopl_norst.yaml')
    with open(test_file_path, 'r') as f:
        result = yaml.load(f, Loader=AnsibleLoader)
        assert result == {'plaintext': 'Hello World', 'ciphertext': 'VjJUSU5ERVJcQlRydWVUcnVlXEJUcnVlVHJ1ZVxCVHJ1ZVRydWVcQlRydWVUcnVl'}

    # Test with a generic YAML file w/ a script tag
    test_file_path = os

# Generated at 2022-06-13 07:41:25.106616
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:41:33.626254
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.nodes import AnsibleMappingNode, AnsibleSequenceNode
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping, AnsibleSequence, \
        AnsibleUnicode, AnsibleUnicodeColon
    from ansible.parsing.yaml.representer import AnsibleRepresenter
    from ansible.parsing.yaml.serializer import AnsibleSerializer
    assert(issubclass(AnsibleLoader, Reader))

# Generated at 2022-06-13 07:41:42.151710
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    #import json
    #from ansible.module_utils._text import to_bytes

    ansible_yaml_snippet = """
a: 1
b:
  c: 3
  d: 4
"""
    ansible_yaml_snippet_bytes = to_bytes(ansible_yaml_snippet)
    ansible_yaml_snippet_unicode = to_unicode(ansible_yaml_snippet, errors='surrogate_then_replace')
    ansible_json_snippet = """
{
"a": 1,
"b": {
"c": 3,
"d": 4
}
}
"""
    class TestLoader(AnsibleLoader):  # test loading from string
        def __init__(self, stream):
            Ansible

# Generated at 2022-06-13 07:41:52.125276
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO
    from yaml import load, dump
    from ansible.module_utils.common.yaml import HAS_LIBYAML

    # Tests for class AnsibleLoader

    # Testing with IO stream
    input_str = StringIO("test_str: Ansible")
    assert load(input_str, Loader=AnsibleLoader) == {'test_str': 'Ansible'}

    # Testing with StringIO
    input_str = StringIO("test_str: Ansible")
    assert load(input_str, Loader=AnsibleLoader) == {'test_str': 'Ansible'}

    # Testing with BytesIO
    input_bytes = b'{"test_str": "Ansible"}'

# Generated at 2022-06-13 07:41:57.208814
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = """
    foo: [ a, &anchor b, *alias ]
    bar:
        <<: *alias
    """

    loader = AnsibleLoader(data)
    contents = loader.get_single_data()
    assert contents == {
        'foo': [ 'a', 'b', 'b' ],
        'bar': 'b',
    }

# Generated at 2022-06-13 07:42:02.581456
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import json

    import ansible.constants as C

    loader = AnsibleLoader(None)

    # assert that the strings are being used as a regex and not at exact
    # values (arbitrary test here, but we should always have bin/python[2] or
    # python[2] in our path)
    loader.set_cached_data('/bin/python2', 'some_key', 'some_value')
    assert loader.get_cached_data('/usr/bin/python2', 'some_key') == 'some_value'
    assert loader.get_cached_data('/usr/bin/python3', 'some_key') is None

    # assert that setting data without a key works
    loader.set_cached_data('/bin/python2', None, 'some_value')


# Generated at 2022-06-13 07:42:05.972118
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """Test that AnsibleLoader"""

    s = "{extends: parent.yml, other: stuff} {foo: true}"
    assert isinstance(AnsibleLoader(s).get_single_data(), AnsibleLoader)

# Generated at 2022-06-13 07:42:25.482618
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 07:42:34.505981
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansibleloader = AnsibleLoader(None, None, None)

    assert ansibleloader.file_name is None
    assert ansibleloader.vault_secrets is None
    # assert ansibleloader.stream is None

    ansibleloader = AnsibleLoader(None, 'test')
    assert ansibleloader.file_name == 'test'

    ansibleloader = AnsibleLoader(None, file_name='test')
    assert ansibleloader.file_name == 'test'

# Generated at 2022-06-13 07:42:40.880236
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io
    import unittest

    class TestAnsibleLoader(unittest.TestCase):

        def test_yaml_load(self):
            data = '''
---
- name: test
  hosts: localhost
  tasks:
  - debug:
      msg: "Hello World!"
'''
            loader = AnsibleLoader(io.StringIO(data))
            results = loader.get_single_data()
            assert type(results) is list
            for result in results:
                assert result['hosts'] == "localhost"
                assert result['name'] == "test"
        
            # This requires pyyaml to be installed
            # with open("playbook.yml","w") as myfile:
            #     data = loader.get_single_data()
            #     myfile.write

# Generated at 2022-06-13 07:42:51.895444
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.vault import VaultLib

    class TestYAMLObject(AnsibleBaseYAMLObject):

        def __init__(self, *args, **kwargs):
            AnsibleBaseYAMLObject.__init__(self)
            self.comments = []
            self.__obj_init__(*args, **kwargs)

    vault = VaultLib('secret')
    loader = AnsibleLoader(stream='foo')
    assert loader.file_name is None
    assert not hasattr(loader, '_match')

# Generated at 2022-06-13 07:42:54.907290
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    with open('../../../test/units/data/test_yaml.yml') as yaml_file:
        loaded = AnsibleLoader(yaml_file).get_single_data()
        assert (isinstance(loaded, list))

# Generated at 2022-06-13 07:43:00.932375
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
    ---
    foo: bar

    # a comment
    baz:
      - quux
      - zot
    '''
    loader = AnsibleLoader(stream)
    doc = loader.get_single_data()
    assert doc == {'foo': 'bar', 'baz': ['quux', 'zot']}

# Generated at 2022-06-13 07:43:02.931556
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(stream=None)
    assert isinstance(ansible_loader, AnsibleLoader)

# Generated at 2022-06-13 07:43:10.672062
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    globals()['__loader__'] = globals().get('__loader__', None)

    try:
        stream = open("../../lib/ansible/parsing/yaml/tests/data/with_nulls.yaml")
        data = Parser(stream=stream).get_single_data()
        assert data == {u'first': u'one', u'second': None, u'third': 3, u'fourth': [1, None, None, 4], u'fifth': {u'a': 1, u'b': None, u'c': 3}, u'sixth': [u'one', None, None, u'four']}
    finally:
        stream.close()

# Generated at 2022-06-13 07:43:25.643679
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test private method _get_implicit_resolvers
    loader = AnsibleLoader('')
    loader._get_implicit_resolvers()

    # Test private method _construct_yaml_str
    data = loader._construct_yaml_str('test_data')
    assert data == 'test_data'

    # Test private method _construct_yaml_seq
    data = loader._construct_yaml_seq([])
    assert data == []

    # Test private method _construct_mapping
    data = loader._construct_mapping()
    assert data == {}

    # Test private method _construct_mapping_from_yaml
    data = loader._construct_mapping_from_yaml()
    assert data == {}

    # Test private method _construct_flow_style
    data = loader._construct_flow_style

# Generated at 2022-06-13 07:43:35.936388
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import sys
    from ansible.module_utils.common.yaml.constructor import AnsibleConstructor

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    from ansible.inventory.host import Host

    class TestAnsibleLoader(unittest.TestCase):

        def test_AnsibleLoader_hostvars(self):
            fake_loader = dict({u'hostvars': dict({u'foo': dict()})})
            fake_loader[u'hostvars'][u'foo'][u'a'] = u'foo.a'
            fake_loader[u'hostvars'][u'foo'][u'b'] = u'foo.b'

# Generated at 2022-06-13 07:44:01.786372
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    d = AnsibleLoader(stream=None, file_name=None)
    assert isinstance(d, AnsibleConstructor)
    assert isinstance(d, Resolver)
    assert isinstance(d, Parser)

# Generated at 2022-06-13 07:44:11.457953
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import yaml
    from ansible.parsing.vault import VaultLib

    # test reloader
    def test_constructor(loader, node):
        return loader.construct_yaml_reload(node)

    yaml.add_constructor(u'!reload', test_constructor)

    class TestVaultLib(VaultLib):
        def decrypt(self, data):
            return data

    vault_secrets = [TestVaultLib().decrypt, {}]
    setattr(yaml, 'vault_secrets', vault_secrets)


# Generated at 2022-06-13 07:44:12.705112
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:44:14.974920
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, '__init__')
    assert callable(AnsibleLoader.__init__)



# Generated at 2022-06-13 07:44:17.921882
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create a test ansibleLoader
    ansibleLoader = AnsibleLoader()
    assert isinstance(ansibleLoader, Parser)
    assert isinstance(ansibleLoader, AnsibleConstructor)
    assert isinstance(ansibleLoader, Resolver)

# Generated at 2022-06-13 07:44:18.710227
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=unused-argument
    pass

# Generated at 2022-06-13 07:44:21.510050
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader  # substitute pylint error "used when a class is defined but not used"

# Generated at 2022-06-13 07:44:35.991241
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test 1: Check success on empty file
    empty = '{}'
    loader = AnsibleLoader(empty)
    try:
        loader.get_single_data()
    except KeyError:
        assert False
    assert True

    # Test 2: Check that vault_secrets is set correctly
    empty2 = '{}'
    loader2 = AnsibleLoader(empty2, vault_secrets={'test_id': 'test_pw'})
    try:
        loader2.get_single_data()
    except KeyError:
        assert False
    assert True
    assert loader2.vault_secrets['test_id'] == 'test_pw'

    # Test 3: Check that file_name is set correctly
    empty3 = '{}'

# Generated at 2022-06-13 07:44:40.393362
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' unit tests for AnsibleLoader '''

    import sys
    import unittest

    if sys.version_info < (2, 7):
        import unittest2 as unittest

    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping

    class TestAnsibleLoader(unittest.TestCase):

        def setUp(self):
            self.loader = AnsibleConstructor()

        def tearDown(self):
            pass

        def test_construct_yaml_str(self):
            # loader should construct unicode strings from yaml scalar nodes.
            yaml_scalar = u'foo'

# Generated at 2022-06-13 07:44:45.295974
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import io

    class FakeVaultSecret():
        def get_decrypted_secret(self, vault_secret):
            return 'sauce'


# Generated at 2022-06-13 07:45:32.586380
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class TestAnsibleLoader(AnsibleLoader):
        pass

    TestAnsibleLoader(stream=None)

# Generated at 2022-06-13 07:45:36.307621
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    with open('/etc/hosts', 'r') as stream:
        loader = AnsibleLoader(stream, '/etc/hosts')
        loader.get_single_data()
        assert loader.check_data() is None

# Generated at 2022-06-13 07:45:39.863801
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml.AnsibleLoader = AnsibleLoader


# pylint: disable=unused-import
# Load the preferred implementation of AnsibleLoader
from ansible.module_utils.common.yaml import AnsibleLoader

# Generated at 2022-06-13 07:45:40.769173
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:45:46.631822
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    fixtures = [
        u'---\n- hosts: localhost\n  tasks:\n    - debug:\n        msg: Hello\n',
        u'---\n- hosts: localhost\n  tasks:\n    - debug:\n        msg: Hello\n---\n- hosts: localhost\n  tasks:\n    - debug:\n        msg: Hello\n'
    ]
    for fixture in fixtures:
        loader = AnsibleLoader(fixture)
        assert "tasks" in loader.get_single_data()

# Generated at 2022-06-13 07:45:55.853651
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    vault_secrets = [
        VaultLib.VaultSecret('sha1', VaultLib.VaultAES256('password'))
    ]


# Generated at 2022-06-13 07:46:07.631278
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO

    yaml_str = '''
example:
  -
    - name: test1
      value: 123
  -
    - name: test2
      value: 321
'''
    loader = AnsibleLoader(StringIO(yaml_str))
    data = loader.get_single_data()
    assert data['example'][0][0]['name'] == 'test1'
    assert data['example'][0][0]['value'] == 123
    assert data['example'][1][0]['name'] == 'test2'
    assert data['example'][1][0]['value'] == 321

    # test that a dict with a string key containing a colon does not

# Generated at 2022-06-13 07:46:15.599149
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
        {
            "hello": "world",
            "foo": [1, 2, 3]
        }
    '''
    from StringIO import StringIO
    loader = AnsibleLoader(StringIO(data))
    assert loader.get_single_data() == {
        'foo': [1, 2, 3],
        'hello': 'world'
    }

# Generated at 2022-06-13 07:46:18.475514
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, 'yaml_constructor')
    assert hasattr(AnsibleLoader, 'yaml_multi_constructor')

# Generated at 2022-06-13 07:46:24.026148
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_yaml = """
    key1: OK
    key2: "{{foobar}}"
    key3:
      - OK
      - "{{foobar}}"
      - "OK"
    """
    ansible_loader = AnsibleLoader(test_yaml)
    for yaml_data in ansible_loader:
        assert yaml_data == {'key1': 'OK', 'key2': '{{foobar}}', 'key3': ['OK', '{{foobar}}', 'OK']}

# Generated at 2022-06-13 07:48:11.071360
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    # load dictionary data (document)
    data = u"---\nkey: value"
    data = AnsibleLoader(data).get_single_data()
    assert isinstance(data, dict)
    assert len(data) == 1
    assert data[u'key'] == u'value'

    # load sequence data (document)
    data = u"---\n- item1\n- item2"
    data = AnsibleLoader(data).get_single_data()
    assert isinstance(data, list)
    assert len(data) == 2

# Generated at 2022-06-13 07:48:18.870212
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=unused-variable
    obj = AnsibleLoader(None)
    assert obj
    import yaml

# Generated at 2022-06-13 07:48:22.957568
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=invalid-name
    import yaml
    test_dict = yaml.load(open(__file__))
    assert test_dict != None
    assert type(test_dict) == type({})

# Generated at 2022-06-13 07:48:27.100710
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    data = '''
a: 1
b:
  c: 3
  d: 4
'''
    loader = AnsibleLoader(data)
    assert loader.get_single_data() == eval(data)

# Generated at 2022-06-13 07:48:29.154213
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:48:33.704590
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml = """
---
- hosts: localhost
  tasks:
    - debug:
        msg: 'Hello World!'
"""
    loader = AnsibleLoader(yaml)
    code = loader.get_single_data()
    assert type(code) == list and len(code) == 1, 'Something wrong with AnsibleLoader.get_single_data()'