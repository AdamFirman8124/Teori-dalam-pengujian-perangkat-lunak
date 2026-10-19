

# Generated at 2022-06-13 07:38:33.972803
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = """
    - hosts: localhost
      tasks:
      - name: print hello
        debug: msg="hello world"
    """

    y = AnsibleLoader(yaml_str)
    doc = y.get_single_data()
    assert doc[0]['hosts'] == 'localhost'
    assert doc[0]['tasks'][0]['name'] == 'print hello'
    assert doc[0]['tasks'][0]['debug'] == {'msg': 'hello world'}

# Generated at 2022-06-13 07:38:37.511541
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    >>> stream = 'hello: world'
    >>> loader = AnsibleLoader(stream)
    >>> data = loader.get_single_data()
    >>> data == {'hello': 'world'}
    True
    '''
    pass

# Generated at 2022-06-13 07:38:39.000349
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader([])
    assert loader is not None

# Generated at 2022-06-13 07:38:41.179845
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(file_name=None, vault_secrets=None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:38:49.909586
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.utils import AnsibleVaultSecret

    my_vault_secret = AnsibleVaultSecret('secret')

# Generated at 2022-06-13 07:38:51.081567
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True

# Generated at 2022-06-13 07:38:53.949168
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class FakeStream:
        def read(self):
            return 'YAML'

    assert AnsibleLoader(FakeStream()).get_single_data() == 'YAML'

# Generated at 2022-06-13 07:39:01.071624
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.serializer import AnsibleSerializer

    # Created the YAML class objects

# Generated at 2022-06-13 07:39:12.372583
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import AnsibleLoader

    data = """
---
- hosts: node-1
  gather_facts: false
  tasks:
    - name: Get ansible facts
      setup:
    - debug: 'msg={{ ansible_os_family }}'
"""

    loader = AnsibleLoader(data)
    data = loader.get_single_data()
    for obj in data:
        for key, value in obj.items():
            if key == 'hosts':
                assert value == 'node-1'
            elif key == 'gather_facts':
                assert value == False
            elif key == 'tasks':
                tasks_list = []
                tasks_name_dict = {}
                tasks_setup_dict = {}
                tasks_debug_dict = {}
                tasks_

# Generated at 2022-06-13 07:39:19.174061
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import doctest

    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
    os.environ['ANSIBLE_RETRY_FILES_ENABLED'] = 'False'
    os.environ['ANSIBLE_DEPRECATION_WARNINGS'] = 'False'
    os.environ['PYTHONPATH'] = ':'.join(sys.path)
    return doctest.testmod(sys.modules['ansible.parsing.yaml.loader'])

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:39:27.923538
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret


# Generated at 2022-06-13 07:39:31.266698
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=too-few-public-methods
    '''
    AnsibleLoader()
    '''
    pass

# Generated at 2022-06-13 07:39:42.498280
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleSequence
    from ansible.module_utils.six import PY2

    if PY2:
        from yaml.constructor import ConstructorError
    else:
        from yaml.constructor import ConstructorError as ConstructorError
    try:
        AnsibleLoader(0)
    except ConstructorError as err:
        assert str(err) == "expected a character buffer object"
    assert isinstance(AnsibleLoader('').get_single_data(), AnsibleBaseYAMLObject)
    assert isinstance(AnsibleLoader('---').get_single_data(), AnsibleBaseYAMLObject)

# Generated at 2022-06-13 07:39:50.548401
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:39:51.105811
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader()

# Generated at 2022-06-13 07:40:02.132595
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Acquire string object representing the YAML file
    # Write up a YAML file
    yaml_string='\n'.join([
        "# Test YAML file",
        "",
        "---",
        "",
        "test_scalar: hello world",
        "test_list:",
        "  - test",
        "  - list",
        "test_mapping:",
        "    name: test mapping",
        "other_test_mapping:",
        "    name: other test mapping",
        "yet_another_mapping:",
        "    name: yet another mapping",
    ])

    # Convert string object to file-like object
    from StringIO import StringIO
    stream = StringIO(yaml_string)

    # Instantiate AnsibleLoader object
    loader = Ansible

# Generated at 2022-06-13 07:40:05.618282
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert len(AnsibleLoader.yaml_constructors) == len(_yaml_constructors)
    assert len(AnsibleLoader.yaml_multi_constructors) == len(_yaml_multi_constructors)


# Generated at 2022-06-13 07:40:08.692239
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    if HAS_LIBYAML:
        raise AssertionError("Test doesn't work with libyaml")
    assert isinstance(AnsibleLoader('foo'), AnsibleLoader)

# Generated at 2022-06-13 07:40:11.624245
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader(None)
    assert loader.construct_yaml_str(None) == AnsibleUnicode('')

# Generated at 2022-06-13 07:40:17.771625
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    string_in = """
---
test:
 - abc
---
test:
 - def
"""
    stream = yaml.compat.StringIO(string_in)
    ansible_loader = yaml.AnsibleLoader(stream)
    ansible_loader.get_single_data()
    ansible_loader.get_single_data()

# Generated at 2022-06-13 07:40:26.523927
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, "construct_yaml_map")
    assert hasattr(AnsibleLoader, "add_constructor")
    assert hasattr(AnsibleLoader, "add_multi_constructor")
    assert not hasattr(AnsibleLoader, "resolver_base")


# Generated at 2022-06-13 07:40:34.512350
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import io
    import yaml
    # Test AnsibleConstructor
    ansible_const = AnsibleLoader(None)
    assert hasattr(ansible_const, '_vault'), 'Failed to set AnsibleConstructor._vault'
    # Test AnsibleConstructor.add_constructor
    ansible_const.add_constructor(None, None)
    assert len(ansible_const.yaml_constructors) == 2, 'Failed to add to AnsibleConstructor.yaml_constructors'
    # Test AnsibleConstructor.add_multi_constructor
    ansible_const.add_multi_constructor(None, None)

# Generated at 2022-06-13 07:40:35.639725
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:40:36.663032
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:40:37.267547
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:40:46.347308
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    import os
    import base64
    import sys
    import tempfile
    import shutil

    vault_secret = 'verysecretvalue'
    vault_password = VaultLib.create_vault_password_file(vault_secret)

# Generated at 2022-06-13 07:40:50.768516
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test the class AnsibleLoader exists
    from ansible.parsing.yaml import objects
    loader = objects.AnsibleLoader("foobar")
    assert loader.__class__.__name__ == 'AnsibleLoader'


# Generated at 2022-06-13 07:40:59.426990
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from io import StringIO


# Generated at 2022-06-13 07:41:10.562723
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, 'add_constructor')
    assert hasattr(AnsibleLoader, 'add_multi_constructor')
    assert hasattr(AnsibleLoader, 'add_path_resolver')
    assert hasattr(AnsibleLoader, 'add_implicit_resolver')
    assert hasattr(AnsibleLoader, 'get_single_data')
    assert hasattr(AnsibleLoader, 'construct_document')
    assert hasattr(AnsibleLoader, 'construct_scalar')
    assert hasattr(AnsibleLoader, 'construct_yaml_map')
    assert hasattr(AnsibleLoader, 'construct_yaml_seq')
    assert hasattr(AnsibleLoader, 'construct_yaml_set')

# Generated at 2022-06-13 07:41:18.779168
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader

    data = """
      # example
      - hosts:
        - localhost
        remote_user: root
        gather_facts: no
        tasks:
          - name: test
            setup:
              filter: ansible_distribution
            register: os_facts
          - debug: var=os_facts
    """
    loader = AnsibleLoader(data)
    assert loader is not None
    print(loader)

# Generated at 2022-06-13 07:41:34.822410
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:41:42.898627
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestAnsibleLoader(unittest.TestCase):

        def test_read(self):

            # test empty
            loader = AnsibleLoader('')
            self.assertEqual(loader.get_data(), None)
            self.assertEqual(loader.construct_object(None, None), None)

            # test simple
            loader = AnsibleLoader('{}')
            self.assertEqual(loader.get_data(), {})
            self.assertEqual(loader.construct_object(None, None), {})


# Generated at 2022-06-13 07:41:51.110723
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """This is a fake unit test for AnsibleLoader

    This is a fake unit test for AnsibleLoader.  It tests the __init__
    method of the class.  Since the AnsibleLoader loads plugins that
    the real unit tests may not have, this is a simple test to make
    sure the constructor is sane.  It is here to silence the pylint
    warning about too many public methods on AnsibleLoader.
    """
    data = '---\n- hosts: localhost\n'
    loader = AnsibleLoader(data)
    assert loader.get_single_data() == [{'hosts': 'localhost'}]

# Generated at 2022-06-13 07:42:01.994916
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    # AnsibleLoader is only available if PyYAML is installed
    try:
        from ansible.parsing.yaml.loader import AnsibleLoader
    except ImportError:
        return
    # AnsibleLoader is only available on Python 2.7+
    if sys.version_info < (2, 7):
        return
    # Reader is not available if Ansible is run with Python 3.5+
    if sys.version_info >= (3, 5):
        return
    # AnsibleLoader is only available if PyYAML was installed with libYAML
    if not getattr(AnsibleLoader, 'add_constructor', False):
        return
    # AnsibleLoader is only available if libYAML is available

# Generated at 2022-06-13 07:42:09.059231
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    from ansible.module_utils.common.yaml import AnsibleLoader

    # We prefer to use libyaml, but it is not available on all platforms
    if sys.version_info >= (2, 7):
        yaml = AnsibleLoader('[foo, bar, baz]')
        assert yaml.get_single_data() == ['foo', 'bar', 'baz']
        assert yaml.get_single_data() is None

        yaml = AnsibleLoader('foo: bar\nbaz: 42')
        assert yaml.get_single_data() == {'foo': 'bar', 'baz': 42}
        assert yaml.get_single_data() is None

        yaml = AnsibleLoader('')

        yaml = AnsibleLoader('[foo, bar, baz]')

# Generated at 2022-06-13 07:42:13.176803
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys, yaml
    yaml.load('---', AnsibleLoader)
    yaml.load('---', AnsibleLoader(sys.stdin))
    yaml.load('---', AnsibleLoader(sys.stdin, 'foo.yaml'))

# Generated at 2022-06-13 07:42:19.945052
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io

# Generated at 2022-06-13 07:42:23.720579
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io, sys
    stream = io.StringIO( u"--- {'a': 'b', 'c': {'d' : 'e'}}")
    AnsibleLoader(stream)

# Generated at 2022-06-13 07:42:26.564408
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestAnsibleLoader(AnsibleLoader):
        pass
    TestAnsibleLoader()

# Generated at 2022-06-13 07:42:40.280773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test using default constructor
    loader = AnsibleLoader("")
    assert loader.file_name is None
    assert loader.vault_secrets is None
    assert loader.get_single_data() is None

    # Test using both parameters
    loader = AnsibleLoader("", "TestFile", ["TestSecret1", "TestSecret2"])
    assert loader.file_name == "TestFile"
    assert loader.vault_secrets == ["TestSecret1", "TestSecret2"]
    assert loader.get_single_data() is None

    # Test using only file_name
    loader = AnsibleLoader("", "TestFile")
    assert loader.file_name == "TestFile"
    assert loader.vault_secrets is None
    assert loader.get_single_data() is None

    # Test using only vault_secrets


# Generated at 2022-06-13 07:43:00.933393
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader._yaml_version is None
    assert loader._implicit_resolvers == {}
    assert loader._path_resolvers == []
    assert loader._base_loader == None

# Generated at 2022-06-13 07:43:10.315317
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.inventory.host import Host


# Generated at 2022-06-13 07:43:11.847817
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader('')

# Generated at 2022-06-13 07:43:26.661365
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('')
    assert hasattr(loader, 'construct_yaml_map')
    assert hasattr(loader, 'construct_yaml_seq')
    assert hasattr(loader, 'construct_mapping')
    assert hasattr(loader, 'construct_python_name')
    assert hasattr(loader, 'construct_undefined')
    assert hasattr(loader, 'construct_yaml_str')
    assert hasattr(loader, 'construct_yaml_int')
    assert hasattr(loader, 'construct_yaml_bool')
    assert hasattr(loader, 'construct_yaml_float')
    assert hasattr(loader, 'construct_yaml_omap')
    assert hasattr(loader, 'construct_yaml_pair')
    assert hasattr(loader, 'construct_yaml_timestamp')


# Generated at 2022-06-13 07:43:32.429053
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert(AnsibleLoader.yaml_constructors.get('!include') is not None)
    assert(AnsibleLoader.yaml_constructors.get('!include_vars') is not None)
    assert(AnsibleLoader.yaml_constructors.get('!include_role') is not None)
    assert(AnsibleLoader.yaml_constructors.get('!import_playbook') is not None)

# Generated at 2022-06-13 07:43:41.548218
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    print("TESTING AnsibleLoader")

    data = '''
    - host: localhost
      gather_facts: no
      tasks:
         - name: test
           ping:
'''

    try:
        al = AnsibleLoader(data)
        al.get_single_data()
        print("Test 1: Success")
    except:
        print("Test 1: Failed")

    try:
        al = AnsibleLoader(data, '/tmp/test_AnsibleLoader')
        al.get_single_data()
        print("Test 2: Success")
    except:
        print("Test 2: Failed")

    vault_secrets = {'decryption_keys': ['~/ansible/vault_password']}

# Generated at 2022-06-13 07:43:54.518628
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    struct = AnsibleLoader(None, vault_secrets=[1, 2, 3]).get_single_data()
    assert struct == {}

    struct = AnsibleLoader("---", vault_secrets=[1, 2, 3]).get_single_data()
    assert struct == {}

    struct = AnsibleLoader("{}", vault_secrets=[1, 2, 3]).get_single_data()
    assert struct == {}

    struct = AnsibleLoader("{a: b}", vault_secrets=[1, 2, 3]).get_single_data()
    assert struct == {'a': 'b'}


# Generated at 2022-06-13 07:44:06.309940
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import sys
    if sys.version_info[0] < 3:
        from io import BytesIO as StringIO
    else:
        from io import StringIO
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    # Constructor and destructor
    stream = StringIO(u"a: 1")
    data = AnsibleLoader(stream)
    assert data is not None
    del data

    # Exceptions
    loader = AnsibleLoader(stream)
    with pytest.raises(TypeError) as excinfo:
        loader.construct_yaml_map(None)
    assert 'expected' in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        loader.construct_yaml_map(u'aaa')
   

# Generated at 2022-06-13 07:44:16.111977
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestAnsibleLoader(AnsibleLoader):
        def __init__(self):
            self.yaml_data = None
            self.file_name = None
            self.vault_secrets = None

        def compose_node(self, parent, index):
            pass

        def compose_document(self):
            pass

        def construct_object(self, node, deep=False):
            pass

        def construct_scalar(self, node):
            pass

        def construct_sequence(self, node, deep=False):
            pass

        def construct_mapping(self, node, deep=False):
            pass

        def construct_yaml_null(self, node):
            pass

        def construct_yaml_bool(self, node):
            pass


# Generated at 2022-06-13 07:44:18.893444
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Since the loaders are not implemented as iterators,
    # something with a length of 1 is enough to test for
    yaml = '---\nfoo: bar'
    assert len(list(AnsibleLoader(yaml))) == 1

# Generated at 2022-06-13 07:44:52.747775
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:44:56.567317
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''This test works around the fact that the class AnsibleLoader has no direct unit tests yet.'''
    # This test is to cover the case where the class AnsibleLoader has no direct unit tests yet.
    ansible_loader = AnsibleLoader(None)
    assert ansible_loader is not None

# Generated at 2022-06-13 07:44:57.087332
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True

# Generated at 2022-06-13 07:45:08.695733
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping, AnsibleUnicode
    import io
    import sys

    class MyDumper(AnsibleLoader):
        def construct_yaml_map(self, node):
            data = AnsibleMapping()
            yield data
            value = self.construct_mapping(node)
            data.update(value)

        def construct_yaml_seq(self, node):
            data = AnsibleSequence()
            yield data
            value = self.construct_sequence(node)
            data.extend(value)

        def construct_yaml_str(self, node):
            # Override the default string handling function
            # to always return unicode objects
            return AnsibleUnicode(self.construct_scalar(node))

       

# Generated at 2022-06-13 07:45:09.924353
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    print(AnsibleLoader(file_name = "abc"))

# Generated at 2022-06-13 07:45:13.312474
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create an object for testing
    loader_test_obj = AnsibleLoader(None)
    assert(isinstance(loader_test_obj, AnsibleLoader))

# Generated at 2022-06-13 07:45:24.986332
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    def check_content(loader):
        '''checks that the loader content is as the following yaml doc'''
        data = loader.get_single_data()
        assert data == {'A list': [1, 2, 3, 4, 'a string', u'a unicode string', {'a': 'complex', 'dictionary': [1, 2, 3, {'another': 'dict'}]}]}

    def load_yaml(yaml_text, loader_class):
        '''loads yaml doc using the given loader'''
        stream = yaml_text.encode('utf-8')
        loader = loader_class(stream)
        check_content(loader)

    # Test with one of the Ansible loader in case we have LibYAML support

# Generated at 2022-06-13 07:45:36.308086
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (2, 7):
        # Python >=2.7
        from ansible.parsing.yaml.loader import AnsibleLoader
        from ansible.parsing.dataloader import DataLoader
        from ansible.utils.vars import combine_vars

        my_loader = DataLoader()

        class DummyVarsModule(object):
            def get_vars(self, loader, path, entities, cache=True):
                if isinstance(entities, list):
                    entity_vars = {}
                    for entity in entities:
                        #somehow load vars, using loader, path and entity
                        entity_vars = combine_vars(entity_vars, {'a': 'b'})
                    return entity_vars

# Generated at 2022-06-13 07:45:46.207221
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    mock_vault_secret = VaultLib('dummy_password')
    test_loader = AnsibleLoader(None, file_name='/dummy/file', vault_secrets=mock_vault_secret)

    assert test_loader.construct_yaml_str is not None
    assert test_loader.construct_yaml_seq is not None
    assert test_loader.construct_yaml_map is not None
    assert hasattr(test_loader, '_construct_yaml_seq')
    assert hasattr(test_loader, 'construct_yaml_map')
    assert hasattr(test_loader, 'file_name')

# Generated at 2022-06-13 07:45:49.098111
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from yaml import CSafeLoader as SafeLoader
    except ImportError:
        from yaml import SafeLoader
    if not issubclass(AnsibleLoader, SafeLoader):
        raise AssertionError("The loader should subclass the SafeLoader class.")

# Generated at 2022-06-13 07:46:58.758210
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader('test_data')

# Generated at 2022-06-13 07:47:07.926448
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys

    if sys.version_info < (2, 7):
        print('Test only works on python 2.7 or higher')
        return

    def assertRoundTrip(value):
        # Create a loader, load a string, and make sure the load result
        # matches the original string
        assert isinstance(value, str), '%r is not a string' % value

        loader = AnsibleLoader(value)
        result = list(loader.get_single_data())

        # Create a dumper, dump the result, and make sure the dump result
        # matches the original string
        dumper = AnsibleDumper(None)
        result = dumper.represent_list(result)

# Generated at 2022-06-13 07:47:17.324640
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    yaml_content = r'''
- hosts: all
  gather_facts: yes
  tasks:
    - name: test
      ping:
      register: ansible_loader_test
    - debug:
        msg: "{{ ansible_loader_test.ping }}"
'''
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = AnsibleLoader(StringIO(yaml_content)).get_single_data()
    for task in data:
        assert isinstance(task, dict)
        for entry in task:
            assert isinstance(entry, AnsibleUnicode)

    from ansible.parsing.yaml.dumper import AnsibleDumper
    temp_content = StringIO()

# Generated at 2022-06-13 07:47:26.876861
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # dict
    yaml = 'a: b'
    loader = AnsibleLoader(yaml)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleMapping)

    # list
    yaml = '''
    - foo
    - bar
    - baz'''
    loader = AnsibleLoader(yaml)
    data = loader.get_single_data()
    assert isinstance(data, list)
    assert data == ['foo', 'bar', 'baz']

    # string
    yaml = 'foo'
    loader = AnsibleLoader(yaml)
    data = loader.get_single_data()
   

# Generated at 2022-06-13 07:47:31.747062
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    yaml_stream = io.StringIO(u"\n- name: Hello\n  action: yum\n  args: name=world\n")
    loader = AnsibleLoader(yaml_stream)
    loader.get_single_data()

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:36.514305
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io
    stream = io.BytesIO(b"hello world")
    val_loader = AnsibleLoader(stream, file_name="<foo>", vault_secrets=[])
    assert hasattr(val_loader, "use_extended_loader")

# Generated at 2022-06-13 07:47:38.960202
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ANSIBLE_LOADER = AnsibleLoader('test', file_name='test_file')
    assert ANSIBLE_LOADER.file_name == 'test_file'

# Generated at 2022-06-13 07:47:50.075681
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    data = '''
    - hosts: all
      gather_facts: no
      tasks:
      - name: ping
        ping:
    '''

    loader = AnsibleLoader(data)
    obj = loader.get_single_data()

    assert isinstance(obj[0].get('hosts'), AnsibleUnicode)
    assert obj[0].get('gather_facts') is False
    assert isinstance(obj[0].get('tasks')[0].get('name'), AnsibleUnicode)
    assert isinstance(obj[0].get('tasks')[0].get('ping'), AnsibleUnicode)


# Generated at 2022-06-13 07:47:51.443243
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # following should not throw:
    AnsibleLoader(None)

# Generated at 2022-06-13 07:48:01.482470
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=missing-docstring
    from ansible.parsing.yaml import objects as yaml_objects
    assert(hasattr(AnsibleLoader, '__init__'))
    assert(hasattr(AnsibleLoader, 'construct_python_dict'))
    assert(hasattr(AnsibleLoader, 'construct_mapping'))
    assert(hasattr(AnsibleLoader, 'construct_sequence'))
    assert(hasattr(AnsibleLoader, 'import_yaml'))
    assert(hasattr(AnsibleLoader, 'build_mapping'))
    assert(hasattr(AnsibleLoader, 'construct_yaml_map'))
    assert(hasattr(AnsibleLoader, 'tag_object'))