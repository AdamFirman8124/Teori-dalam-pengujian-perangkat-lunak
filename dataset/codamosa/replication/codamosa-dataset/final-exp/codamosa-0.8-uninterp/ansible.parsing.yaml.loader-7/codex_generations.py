

# Generated at 2022-06-13 07:38:33.212976
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:38:43.030370
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:38:52.116047
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.objects

    class MyDict(dict):
        pass

    class MyAnsibleLoader(AnsibleLoader):
        pass

    data = MyAnsibleLoader(stream=None, file_name=None, vault_secrets=None)

    data.add_constructor('!foo', lambda data: 'FOO!')
    assert data.construct_yaml_map() == {'!foo': 'FOO!'}
    assert data.construct_yaml_map() == MyDict({'!foo': 'FOO!'})
    assert isinstance(data.construct_yaml_map(), MyDict)

    data.add_multi_constructor('!bar', lambda data: data.__class__(data))

# Generated at 2022-06-13 07:38:57.600870
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('24')
    assert loader.construct_yaml_int('24') == 24
    assert loader.construct_yaml_int(24) == 24
    assert loader.construct_yaml_int('0x24') == 36
    assert loader.construct_yaml_float('24') == 24.0
    assert loader.construct_yaml_float('inf') == float('inf')
    assert loader.construct_yaml_float('+inf') == float('inf')
    assert loader.construct_yaml_float('-inf') == float('-inf')
    assert loader.construct_yaml_float('0.05') == 0.05
    assert loader.construct_yaml_float('.05') == 0.05
    assert loader.construct_yaml_float('24.24') == 24.24

# Generated at 2022-06-13 07:39:00.402320
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        AnsibleLoader
    except NameError:
        raise AssertionError("Failed to construct AnsibleLoader class")

# Generated at 2022-06-13 07:39:05.390444
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    source = '''
foo:
  - bar
  - bam
'''

    loader = AnsibleLoader(source, file_name='test_file')
    result = loader.get_single_data()

    assert result == dict(foo=['bar', 'bam'])

# Generated at 2022-06-13 07:39:20.071627
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Loader instance
    loader = AnsibleLoader('{test: 123}')

    # Check AnsibleConstructor.__init__
    assert loader.construct_mapping == AnsibleConstructor.construct_mapping
    assert loader.construct_sequence == AnsibleConstructor.construct_sequence
    assert loader.construct_object == AnsibleConstructor.construct_object
    assert loader.construct_yaml_str == AnsibleConstructor.construct_yaml_str
    assert loader.construct_yaml_seq == AnsibleConstructor.construct_yaml_seq
    assert loader.file_name == AnsibleConstructor.file_name
    assert loader.vault_secrets == AnsibleConstructor.vault_secrets

    # Check Resolver.__init__
    assert loader.yaml_implicit_resolvers == Resolver.yaml_

# Generated at 2022-06-13 07:39:24.604051
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    data = AnsibleLoader(u'name: "John Doe"', u'valid_file').get_single_data()
    assert data["name"] == AnsibleUnicode("John Doe")

# Generated at 2022-06-13 07:39:26.901646
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream=None)
    assert loader


# Generated at 2022-06-13 07:39:34.785389
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = """\
    normal
    ---
    double-dash
    """
    loader = AnsibleLoader(stream)
    assert loader.get_single_data() == u'normal'
    assert loader.get_single_data() == u'double-dash'
    try:
        loader.get_single_data()
    except StopIteration:
        pass
    else:
        raise AssertionError('StopIteration not raised')

# Generated at 2022-06-13 07:39:39.978060
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Basic test that validates the constructor of class AnsibleLoader is
    # working properly
    ansible_loader = AnsibleLoader(None)
    assert ansible_loader is not None

# Generated at 2022-06-13 07:39:41.168697
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert (AnsibleLoader(None) is not None)

# Generated at 2022-06-13 07:39:48.405126
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.composer import Composer
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from yaml.parser import Parser
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from yaml.resolver import Resolver

    a = AnsibleLoader(None)
    assert isinstance(a, Reader)
    assert isinstance(a, Scanner)
    assert isinstance(a, Parser)
    assert isinstance(a, Composer)
    assert isinstance(a, AnsibleConstructor)
    assert isinstance(a, Resolver)


# Generated at 2022-06-13 07:39:57.631218
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO
    from ansible.parsing.vault import VaultLib

    yaml_str = '''---
        foo: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          xxxx==
    '''

    vault_pass = 'secret'
    vault = VaultLib([(vault_pass,)])
    loader = AnsibleLoader(StringIO(yaml_str), vault_secrets=vault.secrets)
    data = loader.get_single_data()
    assert data == {'foo': vault_pass}

# Generated at 2022-06-13 07:39:58.734543
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    print(AnsibleLoader(None).__class__)

# Generated at 2022-06-13 07:40:04.666512
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    if not HAS_LIBYAML:
        import warnings
        warnings.warn(
            "PyYAML is not installed, skipping AnsibleLoader tests.")
        return

    loader = AnsibleLoader(
        '''
        ---
        foo:
            bar: hello world!
            baz: [1, 2, 3]
        '''
    )

    data = loader.get_single_data()

    assert data == {'foo': {'bar': 'hello world!', 'baz': [1, 2, 3]}}

# Generated at 2022-06-13 07:40:10.905038
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_yaml = """
    ---
    - hosts: somehost
      gather_facts: no
      tasks: []
    """
    loader = AnsibleLoader(stream=test_yaml, file_name="/tmp/test.yaml")
    data = loader.get_single_data()
    assert data['hosts'] == 'somehost'
    assert data['gather_facts'] == 'no'
    assert data['tasks'] == []

# Generated at 2022-06-13 07:40:12.792280
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=unused-variable
    # trying to construct an AnsibleLoader directly.
    loader = AnsibleLoader('dummy')

# Generated at 2022-06-13 07:40:22.035508
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestAnsibleLoader(AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            AnsibleLoader.__init__(self, stream, file_name=None, vault_secrets=None)
            self.test = 1

    stream = 'test_string'
    file_name = None
    vault_secrets = None
    obj = TestAnsibleLoader(stream, file_name, vault_secrets)
    assert obj.test == 1

# Generated at 2022-06-13 07:40:25.046103
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def test_construction(stream, file_name):
        loader = AnsibleLoader(stream, file_name)
        return loader

    # TODO
    assert False

# Generated at 2022-06-13 07:40:32.632962
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create class
    A = AnsibleLoader(None)

    # Add an attribute
    A.foo = "bar"
    assert A.foo == "bar"

# Generated at 2022-06-13 07:40:33.450995
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader("")

# Generated at 2022-06-13 07:40:35.789107
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_obj = AnsibleLoader(stream = open('test.yaml','r'))
    print(yaml_obj)


# Generated at 2022-06-13 07:40:37.215395
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:40:44.876133
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    print(HAS_LIBYAML)
    if HAS_LIBYAML:
        loader = AnsibleLoader(stream = '1')
        assert(loader.state == 1)
        assert('file_name' in loader.__dict__.keys())
        assert('vault_secrets' in loader.__dict__.keys())
    else:
        loader = AnsibleLoader(stream = '1', file_name='2', vault_secrets=['3', '4'])
        assert(loader.state == 1)
        assert(loader.file_name == '2')
        assert(loader.vault_secrets == ['3', '4'])

# Generated at 2022-06-13 07:40:51.248341
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader('')
    assert isinstance(loader.construct_yaml_str(''), AnsibleUnicode)
    assert isinstance(loader.construct_yaml_str(None), AnsibleUnicode)

# Generated at 2022-06-13 07:40:54.066353
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    annotation = yaml.load('[1, 2, 3]', Loader=AnsibleLoader)
    assert annotation == [1, 2, 3]

# Generated at 2022-06-13 07:40:58.490821
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Need to check that the vault secrets are properly passed through
    # when creating a new AnsibleLoader.
    vault_secrets = [{'vault_id': 'test_vault_id',
                      'vault_password': 'test_vault_password'}]

    loader = AnsibleLoader(None, vault_secrets=vault_secrets)
    assert loader.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:41:09.922205
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_bytes
    vault_secrets = [
        VaultLib.AES256,
        VaultLib.get_vault_secrets(filename='secrets/vault-pass.txt')[0][0]
    ]
    test_yaml = to_bytes("""---
a:
  b:
    c:
      vault:
        c: hello
""")
    ansible_loader = AnsibleLoader(test_yaml, vault_secrets=vault_secrets)
    result = ansible_loader.get_single_data()
    assert result == {'a': {'b': {'c': 'hello'}}}


# Generated at 2022-06-13 07:41:17.230422
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

    yaml_str = """
- hosts: all
  vars:
    var1: "{{ var1_value }}"
  tasks:
  - name: Test
    ping:
    tags:
    - test
"""
    stream = yaml.load(yaml_str, Loader=AnsibleLoader)
    print(stream)

# Generated at 2022-06-13 07:41:33.719786
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    stream = '''
- foobar: '2012-06-01'
- foobar: 2012-06-01
- foobar: !!str 2012-06-01
- foobar:
    - !!str 2012-06-01
    - 2012-06-01
    - 2012
'''
    expect = [
        {'foobar': datetime.date(2012, 6, 1)},
        {'foobar': '2012-06-01'},
        {'foobar': '2012-06-01'},
        {'foobar': ['2012-06-01', '2012-06-01', 2012]},
    ]
    assert list(AnsibleLoader(stream)) == expect

# Generated at 2022-06-13 07:41:34.809688
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:41:42.898057
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader("foo: bar\n")
    assert loader.get_single_data() == { b'foo': b'bar' }

    loader = AnsibleLoader(u"foo: bar\n")
    assert loader.get_single_data() == { u'foo': u'bar' }

    loader = AnsibleLoader(u"foo: bar\n")
    assert loader.get_single_data() == { u'foo': u'bar' }

    loader = AnsibleLoader(u"foo: bar\n", file_name=b"/tmp/foo")
    assert loader.get_single_data() == { u'foo': u'bar' }


# Generated at 2022-06-13 07:41:44.780320
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader
    assert AnsibleLoader.__doc__

# Generated at 2022-06-13 07:41:49.754734
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    with open("/home/yihan/yihan-workspace/my-ansible/library/read_yml.yml") as f:
        AnsibleLoader(f, file_name="/home/yihan/yihan-workspace/my-ansible/library/read_yml.yml", vault_secrets=None)

# Generated at 2022-06-13 07:41:50.288959
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:41:51.853406
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, (AnsibleLoader,))

# Generated at 2022-06-13 07:41:53.531378
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader), "AnsibleLoader() returns AnsibleLoader"

# Generated at 2022-06-13 07:41:55.433116
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, file_name='foo')
    assert loader.file_name == 'foo'

# Generated at 2022-06-13 07:41:58.181627
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    assert issubclass(AnsibleLoader, (Reader, Scanner, Parser, Composer,
                                      AnsibleConstructor, Resolver))

# Generated at 2022-06-13 07:42:17.679313
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader('stream','file_name','vault_secrets')

# Generated at 2022-06-13 07:42:18.260234
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:42:21.903938
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_dump = AnsibleLoader(open('./test/unit/parsing/yaml/constructor_test.yml'))
    print(yaml_dump)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:42:37.074660
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_data = b"""
- name: test
  hosts: localhost
  gather_facts: False
  tasks:
    - debug: var=omit
    - debug: var=no_log
    - debug: var=changed_when
- name: more test
  hosts: localhost
  gather_facts: False
  tasks:
    - debug: var=omit
    - debug: var=no_log
    - debug: var=changed_when
"""
    data = AnsibleLoader(test_data)

# Generated at 2022-06-13 07:42:37.987091
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    string = 'example: "string"'
    loader = AnsibleLoader(string, None, None)
    loader.dispose()

# Generated at 2022-06-13 07:42:42.457829
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import io
    import sys

    if sys.version_info[0] == 2:
        # Workaround for Python 2 not having a io.StringIO
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO
        s = StringIO(u'{ "test": "success" }')
    else:
        s = io.StringIO(u'{ "test": "success" }')

    # Test without a file name
    loader = AnsibleLoader(s)
    data = loader.get_single_data()
    assert data == {u"test": u"success"}

    # Test with a file name
    loader = AnsibleLoader(s, file_name='/dev/null')
    data = loader.get_single_data()

# Generated at 2022-06-13 07:42:43.416393
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:42:49.779774
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml import objects

    loader = AnsibleLoader(None)
    assert isinstance(loader.construct_scalar(None), objects.AnsibleUnicode)
    assert isinstance(loader.construct_sequence(None), objects.AnsibleSequence)
    assert isinstance(loader.construct_mapping(None), AnsibleConstructor.AnsibleMapping)

# Generated at 2022-06-13 07:42:52.120635
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = ''
    file_name = ''
    vault_secrets = ''
    AnsibleLoader(stream, file_name, vault_secrets)

# Generated at 2022-06-13 07:42:54.405441
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Resolver)
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)

# Generated at 2022-06-13 07:43:33.228723
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert "AnsibleConstructor" in str(loader)

# Generated at 2022-06-13 07:43:35.831705
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert 'AnsibleConstructor' in str(type(loader))
    assert 'Resolver' in str(type(loader))

# Generated at 2022-06-13 07:43:43.396460
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    # Python 3 has no long type
    long_type = long if sys.version_info < (3, 0) else int

    assert isinstance(AnsibleLoader(None).construct_yaml_int('1234'), int)
    assert isinstance(AnsibleLoader(None).construct_yaml_int('-1234'), int)
    assert isinstance(AnsibleLoader(None).construct_yaml_int('0o644'), int)
    assert isinstance(AnsibleLoader(None).construct_yaml_int('0x3fa'), int)
    assert isinstance(AnsibleLoader(None).construct_yaml_int('0xffffffffffffff'), long_type)

# Generated at 2022-06-13 07:43:44.347627
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = """---
- hosts: all
  become: yes
"""
    loader = AnsibleLoader(stream)
    loader.get_single_data()

# Generated at 2022-06-13 07:43:54.780146
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    vault_secrets = DataLoader()._find_vault_secrets(
        vault_passwords=['test'],
        vault_password_files=['test'],
        vault_ids=['test'],
        force_vault_ids=['test'],
    )
    loader = AnsibleLoader(None, vault_secrets=vault_secrets)

    v = VaultLib(vault_secrets['test'])
    loader.set_vault_secrets(v)

    assert loader.vault_secrets == v

# Generated at 2022-06-13 07:43:57.279071
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, vault_secrets=None)
    assert loader is not None

# Generated at 2022-06-13 07:44:06.838234
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    input_data = """
        ---
        - hosts: localhost
          tasks:
          - name: hello world test
            debug:
              msg: "{{ 'Hello World! ' | repeat(3) }}"
    """
    loader = AnsibleLoader(input_data)
    result = loader.get_single_data()

    assert result['hosts'] == 'localhost'
    tasks = result['tasks']
    assert tasks[0]['name'] == 'hello world test'
    assert tasks[0]['debug']['msg'] == AnsibleUnsafeText('Hello World! Hello World! Hello World! ')

# Generated at 2022-06-13 07:44:10.370235
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = """
    -   one
    -   two
    """

    loader = AnsibleLoader(stream, vault_secrets=['foo'])
    data = loader.get_single_data()

    assert data == ['one', 'two']

# Generated at 2022-06-13 07:44:19.274879
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
    content = b'''---
a_string: 'Ansible Unicode string'
a_number: 42
another_number: 9.5
a_bool: yes
a_list:
  - 1st list value
  - 2nd list value
  - 3rd list value
a_dict:
  key1: value1
  key2: value2
  key3: value3
'''
    stream = content.decode('utf-8')
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert(type(data) is AnsibleMapping)
    assert(len(data) == 6)
    assert(type(data['a_string']) is AnsibleUnicode)

# Generated at 2022-06-13 07:44:20.117472
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
  pass

# Generated at 2022-06-13 07:45:36.043986
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(0)
    assert loader is not None

# Generated at 2022-06-13 07:45:38.106640
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    __import__('pytest').test.test_AnsibleConstructor(loader.construct_python_json)

# Generated at 2022-06-13 07:45:47.706116
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml import AnsibleLoader
    from ansible.module_utils.common.yaml import ParserError
    from ansible.plugins.loader import vault_loader


# Generated at 2022-06-13 07:45:56.826180
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Construct loader
    with open(__file__) as fp:
        loader = AnsibleLoader(fp)
    # assert it has properties we expect
    assert loader.stream is not None
    assert loader.composer is not None
    assert loader.resolver is not None
    assert loader.constructor is not None
    assert loader.constructor is not None
    assert loader.representer is not None
    assert loader.constructor.vault_secrets == loader.representer.vault_secrets
    # assert it has functions we expect
    assert callable(loader.check_data)
    assert callable(loader.construct_document)
    assert callable(loader.construct_object)
    assert callable(loader.construct_mapping)
    assert callable(loader.prepare_file_vault_secrets)

# Generated at 2022-06-13 07:46:03.229634
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = '''
    ---
    - {
        "Hello": "1",
        "World": "2"
      }
    - {
        "Hello": "3",
        "World": "4"
      }
    '''

    stream = Parser(data)

    ansible_loader = AnsibleLoader(stream)

    assert isinstance(ansible_loader, AnsibleLoader)

# Generated at 2022-06-13 07:46:10.676446
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_string = """
        ---
        foo: bar
        vars:
            baz: boo
        tzatziki:
            type: dip
            ingredients:
              - cucumbers
              - yogurt
        """

    test_string_array = """
        ---
        foo:
          - bar
          - baz
          - boo
        vars:
            baz:
              - boo
              - boz
              - bop
            foo:
              - bar
              - baz
              - boo
        tzatziki:
            type: dip
            ingredients:
              - cucumbers
              - yogurt
        """

# Generated at 2022-06-13 07:46:20.010783
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib  # pylint: disable=no-name-in-module
    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    vault_secrets = [{'vault_id': DEFAULT_VAULT_ID_MATCH, 'vault_password': 'password'}]
    vault = VaultLib(vault_secrets)
    loader = AnsibleLoader(b'x', vault_secrets=vault)

# Generated at 2022-06-13 07:46:25.106759
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader

    try:
        yaml.load(stream=u'{ a: b }', Loader=AnsibleLoader)
    except:
        assert False, "YAML Loader class could not be instantiated"

# Generated at 2022-06-13 07:46:30.708015
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='localhost,')

    host = inventory.get_host('localhost')
    variable_manager.set_host_variable(host, 'foo', 'bar')
    stream = loader.load_from_file("test_AnsibleLoader_data.yml")
    data = AnsibleLoader(stream, 'test_AnsibleLoader_data.yml').get_single_data()


# Generated at 2022-06-13 07:46:40.914394
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    sample_data = """
    - image:
        name: foo
        state: present
        docker_host: localhost
        force: yes
        api_version: 1.21
    - image:
        name: bar
        state: absent
    - image:
        name: '{{ lookup("file", "/tmp/foo.txt") }}'
        state: absent
    - image:
        name: '{{ lookup("env", "HOME") }}'
        state: absent
    """
    for data in sample_data.split('\n'):
        AnsibleLoader(data)