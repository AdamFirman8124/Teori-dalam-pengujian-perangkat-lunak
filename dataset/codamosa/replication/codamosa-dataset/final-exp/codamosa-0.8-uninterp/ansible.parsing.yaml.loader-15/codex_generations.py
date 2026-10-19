

# Generated at 2022-06-13 07:38:30.528723
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import yaml

    yaml_text = '''
    - shell: echo "hello world"
    '''

    yaml_data = yaml.load(yaml_text, AnsibleLoader)

# Generated at 2022-06-13 07:38:31.405745
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, '__init__')

# Generated at 2022-06-13 07:38:37.023539
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    # ABC: Abstract Base Class
    class AnswerABC:
        def __init__(self, answer):
            self.answer = answer

    # No implementation for AnswerABC.represent()
    # so AnsibleLoader.represent_abc() will be used
    def AbstractBaseClassTest():
        """Check that AnsibleLoader uses
        AnsibleLoader.represent_abc()
        """
        class MyConstructor(AnsibleLoader):
            def construct_yaml_map(self, node):
                data = AnsibleMapping()
                yield data
                value = self.construct_mapping(node)
                data.update(value)

# Generated at 2022-06-13 07:38:41.776166
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    yaml_text = u"""
---
- name: test
  hosts: localhost
  tasks:
   - local_action: >
       copy dest=/tmp/test
         content='hello'
       """
    loader = AnsibleLoader(io.StringIO(yaml_text))
    assert u'name' in loader.get_single_data()

# Generated at 2022-06-13 07:38:48.625622
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
# sample
name:
  - host
hosts: all
remote_user: root
tasks:
  - name: task
    debug: msg="{{item}}"
    with_items: name
  - name: task
    debug: msg="{{item}}"
    with_items: host
"""
    stream = AnsibleLoader(data)
    datastructure = stream.get_single_data()
#   print datastructure
    assert datastructure['hosts'] == 'all'
    assert datastructure['tasks'][0]['with_items'] == 'name'
    assert datastructure['tasks'][1]['with_items'] == 'host'

# Generated at 2022-06-13 07:38:59.047587
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.module_utils.common.yaml import Parser
    from ansible.parsing.vault import VaultLib

    # make sure AnsibleLoader is subclass of Parser, AnsibleConstructor, Resolver
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

    # generate vault_secrets
    vault_secrets = [VaultLib(password="password")]

    # test with normal value of parameter
    loader = AnsibleLoader(stream="---\n- - yaml\n  - ansible\n", vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:39:10.482077
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import logging
    import tempfile
    import yaml

    TEST_FILE = """
    ---
    hello: world
    world: hello
    int: 1234567890
    float: 3.1415
    """

    # set up logging to file - see previous section for more details
    log_file = os.path.join(tempfile.gettempdir(), 'ansible-vault-test.log')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file,
                        filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stder

# Generated at 2022-06-13 07:39:11.944435
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # TODO: implement test
    pass

# Generated at 2022-06-13 07:39:18.846100
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode

    stream = '''---
- !include include.yaml
- !include include_2.yaml
...
'''
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data[0]._filename == "include.yaml"
    assert data[0]._anchor == None

    assert data[1]._filename == "include_2.yaml"
    assert data[1]._anchor == None


# Generated at 2022-06-13 07:39:25.905955
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info[0] == 3:
        pytest.skip("Doesn't work on py3")
    import yaml

    yaml.add_constructor(u'!include', AnsibleConstructor._load_yaml_include)
    yaml.add_constructor(u'!include_vars', AnsibleConstructor._load_yaml_include_vars)

    data = """\
---
- include: included_file.yaml
- hosts: all
  roles:
    - some_role
- !include_vars
  file: included_vars.yaml
  name: some_var
"""

    fh = open('test_AnsibleLoader.yaml', 'w')
    fh.write(data)
    fh.close()

    fh = open

# Generated at 2022-06-13 07:39:40.249597
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import from_yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class FakeVaultSecret(object):
        def __init__(self, password):
            self.password = password

    vault_secrets = [FakeVaultSecret('secret')]


# Generated at 2022-06-13 07:39:43.764741
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ANSIBLE_LOADER_DATA = '''
---
list:
- one
- two
- three
'''

    assert (list(AnsibleLoader(ANSIBLE_LOADER_DATA).get_single_data()) == ['list',
                                                                           ['one', 'two', 'three']])

# Generated at 2022-06-13 07:39:45.215542
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass


# Generated at 2022-06-13 07:39:48.618566
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import pytest
    from ansible.module_utils.common.yaml.fixtures import AnsibleLoaderFixture
    loader = AnsibleLoaderFixture.append_line.append_block.yaml_dict
    assert type(loader) == AnsibleLoader

# Generated at 2022-06-13 07:39:59.915504
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword


# Generated at 2022-06-13 07:40:07.377399
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import load
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultSecret

    vault_secrets = [VaultSecret('1111'), VaultSecret('2222')]

# Generated at 2022-06-13 07:40:08.827056
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml.AnsibleLoader = AnsibleLoader

# Generated at 2022-06-13 07:40:09.889688
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Placeholder for a unit test
    assert True

# Generated at 2022-06-13 07:40:17.872706
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    vault_secrets = [
        dict(secret='secret'),
        dict(files='files'),
        dict(env='env'),
    ]
    loader = AnsibleLoader(None, vault_secrets=vault_secrets)
    assert loader.vault_secrets == vault_secrets

    loader = AnsibleLoader(None, file_name='foo.yaml', vault_secrets=vault_secrets)
    assert loader.file_name == 'foo.yaml'
    assert loader.basename == 'foo'
    assert loader.vault_secrets == vault_secrets

    loader = AnsibleLoader(None, file_name='bar.yml', vault_secrets=vault_secrets)
    assert loader.file_name == 'bar.yml'
    assert loader.basename == 'bar'
   

# Generated at 2022-06-13 07:40:24.236579
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    result = dataloader.load_from_file('test/units/parsing/yaml/ansible_loader_test.yaml')
    assert result == {'foo': 'bar', 'baz': [1, 2, 3]}

# Generated at 2022-06-13 07:40:36.508441
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from ansible.parsing.yaml.objects import AnsibleUnicode
        # Test to see if AnsibleLoader properly constructs a dict in the non-libyaml case
        stream = "foo: bar\nspam: baz\n"
        ansible_loader = AnsibleLoader(stream, vault_secrets=None)
        loaded_dict = ansible_loader.get_single_data()
        assert 'foo' in loaded_dict and isinstance(loaded_dict['foo'], AnsibleUnicode)
    except ImportError:
        pass

# Generated at 2022-06-13 07:40:45.816411
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test 1
    yaml_str = """
---
- name: test host
  serial: 0
  tags:
    - { role: common, when: 'ansible_os_family == "RedHat"' }
    - { role: common, when: '"/data/media" in ansible_mounts.mount' }
    - { role: common, when: 1 }
    - { role: common, when: 0 }
    - { role: common, when: 'ansible_os_family != "RedHat"' }
  vars:
    - { var1: 0 }
    - { var2: 1 }
    - { var3: { var31: 31, var32: 32 } }
"""

    # Test 2

# Generated at 2022-06-13 07:40:46.955040
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:40:52.235743
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    from ansible.vars import VariableManager

    if HAS_LIBYAML:
        load_ansible_yaml = lambda loader: loader.get_single_data()
    else:
        load_ansible_yaml = lambda loader: CompositeYamlObject(loader.get_single_data())

    test_loader = AnsibleLoader(file_name=os.path.join(os.path.dirname(__file__), 'data/loader_test.yml'))
    unsafe_proxy = UnsafeProxy()
    variable_manager = VariableManager()

    # test presence of private _vault_secrets after initialization
    assert '_vault_secrets' in test_loader.__dict__

# Generated at 2022-06-13 07:41:00.144676
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.compose import AnsibleComposer
    from ansible.parsing.yaml.serializer import AnsibleSerializer
    from ansible.parsing.yaml.representer import AnsibleRepresenter

    loader = AnsibleLoader({})

    assert isinstance(loader, Reader)
    assert isinstance(loader, Scanner)
    assert isinstance(loader, Parser)
    assert isinstance(loader, Composer)
    assert isinstance(loader, AnsibleComposer)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)
    assert isinstance(loader, AnsibleRepresenter)
    assert isinstance(loader, AnsibleSerializer)

# Generated at 2022-06-13 07:41:07.274543
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''\
---

# All tasks in this play
- hosts: all
  user: root
  tasks:

  - name: print date
    command: date

  - name: print uptime
    command: uptime
'''

    loader = AnsibleLoader(stream, file_name='test_AnsibleLoader.yml')
    data = loader.get_single_data()

    assert 1 < len(data['tasks'])

# Generated at 2022-06-13 07:41:08.491217
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)

# Generated at 2022-06-13 07:41:16.345687
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    content = '''
---
- name: test1
  value: "{{ test_variable }}"
  state: present
  comment: test variable
...

---
- name: test2
  value: "{{ test_variable }}"
  state: present
  comment: test variable
...
'''
    file_name = 'hello.yml'
    stream = io.BytesIO(content.encode('utf-8'))
    vault_secrets = [{'name': 'hello', 'password': 'secret'}]
    loader = AnsibleLoader(stream, file_name, vault_secrets)
    # read/scan
    loader.peek()
    loader.check_token()
    loader.get_token()
    # parser
    loader.compose_document()
    loader.get_event

# Generated at 2022-06-13 07:41:25.986869
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import time
    import datetime
    s = "time_test: 2013-01-20 15:43:08.431134\n"
    loader = AnsibleLoader(s)
    data = loader.get_data()
    if hasattr(data['time_test'], '__int__'):
        assert False, "time was not parsed"
    if data['time_test'] != datetime.datetime(2013, 1, 20, 15, 43, 8, 431134):
        assert False, "time was parsed incorrectly: %s" % data['time_test']
    s = "time_test: 2013-01-20 15:43:08.431134\ndict_test: {a: 2013-01-20 15:43:08.431134}"
    loader = AnsibleLoader(s)
    data = loader

# Generated at 2022-06-13 07:41:28.243868
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
    a:
    - b
    - c
    - d
    '''
    stream = AnsibleLoader(data)
    assert stream.get_single_data() == {'a': ['b', 'c', 'd']}

# Generated at 2022-06-13 07:41:46.972974
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys
    if sys.version_info[0] > 2:
        unicode = str
        long = int
    example_yaml_unicode = AnsibleUnicode('foo: â')
    example_yaml_long = long(42)
    example_yaml_text = unicode('foo: â')
    example_data = {'example_yaml_unicode': example_yaml_unicode,
                    'example_yaml_long': example_yaml_long,
                    'example_yaml_text': example_yaml_text}
    data = AnsibleLoader(None).construct_mapping(None, example_data)


# Generated at 2022-06-13 07:41:54.948005
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import unittest

    from ansible.parsing.yaml.constructor import AnsibleConstructor

    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'constructor_test_data.yaml')
    with open(TEST_DATA_PATH) as test_file:
        source = test_file.read()
    loader = AnsibleLoader(source)
    data = loader.get_single_data()
    assert 'scalar' in data and data['scalar'] == 'example'
    assert 'sequence' in data and data['sequence'] == ['example', 'example2']
    assert 'mapping' in data and data['mapping'] == {'v1': 'example', 'v2': 'example2'}

# Generated at 2022-06-13 07:42:04.565400
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    import  io
    # make sure we're using a version of yaml that supports
    # versions/tags, as well as libyaml bindings
    yaml.__with_libyaml__ = True

    # test the default AnsibleLoader constructor with a file
    fd = io.BytesIO("test: 1\n")
    AnsibleLoader(fd)

    # test the default AnsibleLoader constructor with a file path
    fd.close()
    fd = open("/dev/null", "rb")
    AnsibleLoader(fd)

    # test the default AnsibleLoader constructor with a file name
    fd.close()
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    AnsibleLoader("yaml/constructor.py")

   

# Generated at 2022-06-13 07:42:11.337787
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:42:18.827509
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.module_utils.common.text.converters import to_bytes

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/test_datasets/inventory/test_inventory.yaml')

# Generated at 2022-06-13 07:42:26.677885
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=too-few-public-methods
    class Stream():
        def __init__(self):
            pass
    import copy
    import os

    # Create an instance of AnsibleLoader
    x = AnsibleLoader(Stream())

    # Create a deepcopy of the instance
    y = copy.deepcopy(x)

    # Ensure setting the attributes of the deepcopy does not mutate the original class
    y.file_name = 'test'
    y.path_hash = 'test'
    y.vault_secrets = {'vault': 'secret'}
    assert x.file_name is None
    assert x.path_hash is None
    assert x.vault_secrets is None

    # Try to set an attribute that does not exist on the class

# Generated at 2022-06-13 07:42:31.096107
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(b'{"foo": "bar"}', file_name='/path/to/filename')
    assert loader.stream is not None
    assert loader.constructor.vault_secrets is None
    assert loader.constructor.file_name == '/path/to/filename'

# Generated at 2022-06-13 07:42:38.027210
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml import load

    yaml_str = u"---\n" \
               u"proxy: '//foo:bar@baz.com:8080'\n" \
               u"proxy_port: 8080\n" \
               u"proxy_user: foo\n" \
               u"proxy_password: bar\n" \
               u"..."

    data = load(yaml_str)

    assert data.get('proxy') == "//foo:bar@baz.com:8080"
    assert data.get('proxy_port') == 8080
    assert data.get('proxy_user') == "foo"
    assert data.get('proxy_password') == "bar"

# Generated at 2022-06-13 07:42:47.646204
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Test basic AnsibleLoader class instantiation.
    '''
    import io
    # Note: Using io.StringIO() io.BytesIO() objects is not a test of AnsibleLoader
    #       as methods of the io module invoke different i/o code paths.
    #
    #       The object returned by StringIO() expects unicode text, the object
    #       returned by BytesIO() expects bytes.
    #
    #       For a true test of constraints imposed by AnsibleLoader, we must use
    #       mock objects.
    import mock_io
    import sys

    # Test for file-like types which invoke the legacy i/o path
    mock_stream = mock_io.StringIO()
    assert isinstance(mock_stream, io.TextIOBase)

    loader = AnsibleLoader(mock_stream)


# Generated at 2022-06-13 07:42:50.965366
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    source = u'[1, 2, 3]'
    loader = AnsibleLoader(io.StringIO(source), '<string>')
    assert list(loader) == [1, 2, 3]

# Generated at 2022-06-13 07:43:08.507258
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Test to verify that the AnsibleLoader class can be instanciated by
    the test suite.
    """
    # AnsibleLoader does not have a constructor
    AnsibleLoader(None)

# Generated at 2022-06-13 07:43:13.658339
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))
    import ansible.parsing.yaml
    ansible.parsing.yaml.AnsibleLoader(open('../module_utils/basic.py', 'r'))

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:43:21.204028
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from collections import Mapping
    import os
    import tempfile
    import datetime

    # Test vault decryption
    vault_password = 'ansible'

# Generated at 2022-06-13 07:43:25.320090
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader

    class TestAnsibleLoader(AnsibleLoader):
        pass

    test_instance = TestAnsibleLoader(None)

    assert test_instance is not None

# Generated at 2022-06-13 07:43:29.175265
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = u"""
        ---
        # some yaml
    """
    import io
    stream = io.StringIO(data)
    loader = AnsibleLoader(stream)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:43:36.742552
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Test AnsibleLoader class
    '''

    # test empty string
    test_string = ''
    data = AnsibleLoader(test_string).get_single_data()
    assert data is None

    # test string with illegal construct
    test_string = '{ a: 1 }'
    try:
        data = AnsibleLoader(test_string).get_single_data()
    except AnsibleParserError as e:
        # verify error message contains offending line
        assert 'line 1, column 1' in e.message
        assert 'mapping values are not allowed here' in e.message

# Generated at 2022-06-13 07:43:37.965324
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:43:48.647232
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=unused-variable
    # pylint: disable=redefined-outer-name
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    loader = AnsibleLoader(u"1234")
    assert loader is not None

    # Without the cast to AnsibleUnsafeText, the following loader
    # construction would fail with a 'value is not a string' error with
    # PyYAML 3.10 or earlier.
    loader = AnsibleLoader(AnsibleUnsafeText(u"1234"))
    assert loader is not None

# Generated at 2022-06-13 07:43:55.166124
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=no-self-use, protected-access
    obj = AnsibleLoader.from_string('{}')
    assert obj._constructor is AnsibleConstructor._construct_mapping
    assert obj._constructor_args == ((), {})
    obj = AnsibleLoader.from_string('- one')
    assert obj._constructor is AnsibleConstructor._construct_sequence
    assert obj._constructor_args == ((), {})

# Generated at 2022-06-13 07:44:05.201749
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping

    data = '''
    hello: world
    foo: bar
    list:
    - foo
    - bar
    '''
    loader = AnsibleLoader(data)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleMapping)
    assert data['hello'].value == 'world'
    assert data['foo'].value == 'bar'
    assert isinstance(data['list'], AnsibleMapping)
    assert data['list'].value[0].value == 'foo'
    assert data['list'].value[1].value == 'bar'

# Generated at 2022-06-13 07:44:45.463399
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleVaultEncryptedUnicode
    # It should be able to be called
    AnsibleLoader({'foo': 'bar'})
    # It should be able to initialize an AnsibleUnicode
    AnsibleLoader(u'foo')
    # It should be able to initialize an AnsibleVaultEncryptedUnicode
    AnsibleLoader(u'$ANSIBLE_VAULT;1.1;AES256;root\n63623464632623463623462346332323232353564396365373930393163326434613034333137636263\ntar')

# vim: filetype=python et ts=4 sw=4

# Generated at 2022-06-13 07:44:50.282144
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import yaml

    result = None
    data = None

    stream = io.StringIO("---\n- hosts: localhost")
    loader = AnsibleLoader(stream)
    try:
        data = yaml.load(stream, loader)
    except yaml.YAMLError as exc:
        print(exc)

    print(data)
    assert data == {'hosts': 'localhost'}

# Generated at 2022-06-13 07:44:59.627903
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.collections import ImmutableDict

    data = u'''
    foo:
      bar: 1
      baz: two
      dict:
        nested: 3
        dict:
          - value1
          - value2
    '''

    loader = AnsibleLoader(data)
    loader.get_single_data()

    assert isinstance(loader.data, ImmutableDict)
    assert loader.data == {
        u'foo': {
            u'bar': 1,
            u'baz': u'two',
            u'dict': {
                u'nested': 3,
                u'dict': [u'value1', u'value2']
            }
        }
    }

# Generated at 2022-06-13 07:45:00.351484
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    return True

# Generated at 2022-06-13 07:45:09.296038
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    yaml_str = 'foo: bar'
    yaml_data = AnsibleLoader(yaml_str).get_single_data(allow_includes=False)

    assert isinstance(yaml_data['foo'], AnsibleUnicode)
    assert yaml_data['foo'].data == 'bar'

    assert yaml_str == AnsibleDumper(yaml_data).get_str()

# Generated at 2022-06-13 07:45:11.625550
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    l = AnsibleLoader("---{}")
    l.get_single_data() == '---{}'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:45:17.897906
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import inspect
    import os
    import unittest

    class TestAnsibleLoader(unittest.TestCase):
        def setUp(self):
            self.loader = AnsibleLoader(None, os.path.join(os.path.dirname(__file__), '../data/ansible_loader.yml'))
            self.loader_vault = AnsibleLoader(None, os.path.join(os.path.dirname(__file__), '../data/ansible_loader_vault.yml'), vault_secrets={'vault_secret_1': 'secret_1', 'vault_secret_2': 'secret_2'})

        def tearDown(self):
            pass


# Generated at 2022-06-13 07:45:27.257482
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys, getopt, __builtin__
    import ansible.parsing.vault
    # AnsibleLoader(stream, file_name=None, vault_secrets=None)
    argv = sys.argv
    stream = argv[1]
    opts, args = getopt.getopt(argv[2:], "", "vault-password-file")
    opts = dict(opts)
    vault_password = None
    vault_filename = opts.get('--vault-password-file', None)
    if vault_filename:
        try:
            vault_password = open(vault_filename, 'rb').read().strip()
        except IOError:
            __builtin__.file = open(vault_filename, 'rb')

# Generated at 2022-06-13 07:45:28.741808
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert isinstance(AnsibleLoader(None), AnsibleLoader)

# Generated at 2022-06-13 07:45:31.271707
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:46:47.722429
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.objects as yaml_objects

    # Test the loading of !include

# Generated at 2022-06-13 07:46:54.822649
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestAnsibleLoader(AnsibleLoader):
        def get_single_data(self):
            return self.get_single_data()

    contenido = """
    - 1
    - 2
    - 3
    """
    loader = TestAnsibleLoader(contenido)
    data = loader.get_single_data()
    assert data == [1, 2, 3]

# Generated at 2022-06-13 07:47:05.226531
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:47:12.609287
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import yaml

    def test_AnsibleLoader_called_with_stream(test_yaml_file, stream):
        """
        :type test_yaml_file: yaml.YAML
        :type stream: io.StringIO
        """
        stream.write('---\n')
        stream.seek(0)
        assert test_yaml_file.load(stream) is not None

    test_yaml_file = yaml.YAML()
    test_yaml_file.Loader = AnsibleLoader
    stream = io.StringIO()
    test_AnsibleLoader_called_with_stream(test_yaml_file, stream)

# Generated at 2022-06-13 07:47:23.203115
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime as dt
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:47:24.941445
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # include empty yaml
    yaml_data = {}
    result = AnsibleLoader(yaml_data)
    assert result


# Generated at 2022-06-13 07:47:29.547092
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import inspect

    module_info = inspect.getmembers(AnsibleLoader, predicate=inspect.ismethod)
    for function, _ in module_info:
        if function.startswith('_'):
            continue
        assert(hasattr(AnsibleConstructor, function))

# Generated at 2022-06-13 07:47:30.134915
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:47:35.355080
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' unit test for ansible loader class '''

    yaml_string = '''
      foo:
      - 1
      - 2
      - 3
      -
        bar: hello
        zip: zap
        zap: zip
    '''

    loader = AnsibleLoader(yaml_string)
    loader.get_single_data()

# Generated at 2022-06-13 07:47:36.566011
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Resolver)