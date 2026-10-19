

# Generated at 2022-06-13 07:38:43.147203
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 07:38:44.538384
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:38:50.817618
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import from_yaml

    yaml_str = '''
    debug:
    - msg: 1
    - msg: 2
    - msg: 3
    - msg: 4
    '''
    data = from_yaml(yaml_str)
    assert isinstance(data, dict)
    assert isinstance(data['debug'], list)
    assert data['debug'] == [{'msg': '1'}, {'msg': '2'}, {'msg': '3'}, {'msg': '4'}]

# Generated at 2022-06-13 07:38:52.518135
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, None, None)
    assert loader is not None


# Generated at 2022-06-13 07:38:54.265546
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert AnsibleUnicode('foo') == AnsibleLoader('foo').get_single_data()


# Generated at 2022-06-13 07:39:01.254602
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import PY3, text_type

    class FakeConstructor(AnsibleConstructor):

        def construct_python_unicode(self, node):
            raise ValueError(node)

    class FakeScanner(object):

        def check_token(self, *args, **kwargs):
            pass

    class FakeParser(FakeScanner):

        def get_token(self):
            pass

    class FakeComposer(object):

        def get_single_node(self):
            pass

    class FakeReader(object):

        def read(self, *args, **kwargs):
            pass

    class FakeResolver(object):
        pass


# Generated at 2022-06-13 07:39:04.680794
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:39:13.001558
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = '''
    d0: 1
    d1:
        a: 2
        b: 3
    d2:
        d3:
            c: 4
            d: 5
    '''

    # Test
    result = AnsibleLoader(data).get_single_data()
    assert(result['d0'] == 1)
    assert(result['d1']['a'] == 2)
    assert(result['d1']['b'] == 3)
    assert(result['d2']['d3']['c'] == 4)
    assert(result['d2']['d3']['d'] == 5)

# Generated at 2022-06-13 07:39:21.147695
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # pylint: disable=protected-access
    AnsibleLoader._yaml_base_loader = AnsibleLoader
    AnsibleLoader._yaml_errors      = []
    AnsibleLoader._yaml_ext_tags    = []
    AnsibleLoader._yaml_supported_extensions = []
    AnsibleLoader._yaml_supported_tags = []

    assert not hasattr(AnsibleLoader, '_yaml_add_constructor')
    assert not hasattr(AnsibleLoader, '_yaml_add_multi_constructor')
    assert not hasattr(AnsibleLoader, '_yaml_add_implicit_resolver')
    assert not hasattr(AnsibleLoader, '_yaml_add_path_resolver')

    assert hasattr(AnsibleLoader, 'add_multi_constructor')


# Generated at 2022-06-13 07:39:28.990820
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import BytesIO

    SOME_YAML = b"""---
a: 1
b:
  - c
  - d
  - e
"""

    # load data
    l = AnsibleLoader(BytesIO(SOME_YAML), 'test')
    data = l.get_single_data()

    assert isinstance(data, dict)
    assert data == dict(a=1, b=['c', 'd', 'e'])
    assert isinstance(data, AnsibleBaseYAMLObject)

    # dump data
    b = BytesIO()
    d = AnsibleDumper(b)

# Generated at 2022-06-13 07:39:42.573289
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    This tests if the AnsibleLoader class throws an exception
    """

    yaml_str = '''
- hosts: all
  gather_facts: no
  vars:
    package: ' vsftpd'
  tasks:
    - name: install vsftpd package
      yum:
        name: "{{ package | trim }}"
        state: latest
      when: ansible_os_family == 'RedHat'
    - name: install vsftpd package
      apt:
        name: "{{ package | trim }}"
        state: latest
      when: ansible_os_family == 'Debian'
    - name: start service
      service: name=vsftpd state=started
'''

# Generated at 2022-06-13 07:39:48.293215
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class MockStream(object):
        def __init__(self):
            self.data = []
            self.longest_line = 10

        def read(self, length):
            return self.data.pop(0)

    def test(data):
        stream = MockStream()
        stream.data = data
        loader = AnsibleLoader(stream)
        return loader.get_single_data()

    assert test([]) is None
    assert test(['---', 'abc', '...']) == 'abc'

# Generated at 2022-06-13 07:39:59.582711
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

# Generated at 2022-06-13 07:40:06.046843
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    my_data = '''
    a: 1
    b:
        c: 3
        d: 4
    '''
    my_constructor = AnsibleLoader(my_data.split('\n'))
    my_constructor.get_single_data()
    assert set(my_constructor.data.keys()) == set(['a', 'b'])
    assert set(my_constructor.data['b'].keys()) == set(['c', 'd'])
    assert my_constructor.data['b']['c'] == 3
    assert my_constructor.data['b']['d'] == 4

# Generated at 2022-06-13 07:40:15.231846
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import json
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault = VaultLib([])
    encrypted_data = vault.encrypt(u'secret')

# Generated at 2022-06-13 07:40:27.288261
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib

    class FakeVaultSecret:
        password = "password"

    class FakeVaultSecretList:
        secrets = [FakeVaultSecret()]

    class FakeVaultSecretFile:
        def __init__(self, data):
            self.data = data

        def load(self, secret_file=None, password=None):
            return FakeVaultSecretList()

    class FakeVault:
        def __init__(self):
            self._Vault__secrets_files_cache = dict()

        def get_secrets(self, secret_file=None):
            if secret_file not in self._Vault__secrets_files_cache:
                self._Vault__secrets_files_cache[secret_file]

# Generated at 2022-06-13 07:40:38.991252
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import tempfile
    import random
    import string
    import os

    def random_string(length):
        return ''.join([random.choice(string.ascii_lowercase) for _ in range(length)])

    ansible_loader = AnsibleLoader(None)

    # test adding to searched_paths
    path_to_add = random_string(10)
    ansible_loader.add_path(path_to_add)
    assert path_to_add in ansible_loader.searched_paths

    # test get_file_name from a path that does not exist
    path = os.path.join(random_string(10), random_string(10))
    assert ansible_loader.get_file_name(path) is None

    # test get_file_name from a path that does exist


# Generated at 2022-06-13 07:40:47.451185
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=unused-variable
    import os

    # Read Stream
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base, 'test_loader.yml')) as f:
        yml_text = f.read()
    # yml_stream = StringIO(yml_text)

    # Instantiate Loader
    loader = AnsibleLoader(yml_text)

    # Step 1: Load obj in memory
    _ = loader.get_single_data()

    # Step 2: Set file name
    loader.set_file_name('test_loader.yml')

    # Step 3: Construct data
    data = loader.get_single_data()

    assert data is not None  # pylint: disable=expression

# Generated at 2022-06-13 07:40:53.195805
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
    a: 1
    b:
      c:
        - 1
        - 2
        - 3
    '''
    loader = AnsibleLoader(stream)
    import json
    print(json.dumps(loader.get_single_data(), indent=2))

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:40:55.734042
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    res = AnsibleLoader(stream='{ hello: world }', file_name='foo.yml')
    assert res.file_name == 'foo.yml'

# Generated at 2022-06-13 07:41:11.055092
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:41:15.592905
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    # Assert that the base class that eventually constructs the object is AnsibleConstructor
    assert issubclass(AnsibleLoader, AnsibleConstructor)

    # Assert that AnsibleLoader has the following properties:
    #   - add_constructor, add_multi_constructor, add_implicit_resolver
    assert hasattr(AnsibleLoader, 'add_constructor')
    assert hasattr(AnsibleLoader, 'add_multi_constructor')
    assert hasattr(AnsibleLoader, 'add_implicit_resolver')

    # Assert that AnsibleLoader has the following method:
    #   - add_path_resolver
    assert hasattr(AnsibleLoader, 'add_path_resolver')



# Generated at 2022-06-13 07:41:26.876271
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' Unit test of AnsibleLoader'''
    from yaml import load
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list=['dummy']))

    stream = open("../../../test/sanity/playbook/test.yml", "r")
    inventory_my_hosts = load(stream, Loader=AnsibleLoader)
    playbook = Play().load(inventory_my_hosts, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 07:41:32.288773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    import yaml
    yaml.AnsibleLoader = AnsibleLoader

    # Test inject AnsibleLoader class
    data = yaml.load('''
    foo: !str 2013-08-19
    ''')
    assert isinstance(data['foo'], datetime.datetime)

    # Test Loader (AnsibleLoader) class search path
    data = yaml.load('''
    bar: !date 2013-08-19
    ''')
    assert isinstance(data['bar'], datetime.datetime)

# Generated at 2022-06-13 07:41:41.236964
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

    yaml_str = """
- hosts: test_host
  vars:
    a: 1
  tasks:
    - name: test
      debug:
        var: a
"""

    # _yaml.AnsibleLoader.__init__(self, file_name=None, vault_secrets=None)
    # _yaml.AnsibleLoader.__init__(self, stream, file_name=None, vault_secrets=None)
    data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert data

    # _yaml.AnsibleLoader.__init__(self, file_name='test', vault_secrets=None)
    # _yaml.AnsibleLoader.__init__(self, stream, file_name='test', vault_

# Generated at 2022-06-13 07:41:51.553484
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():   # pylint: disable=too-many-public-methods
    assert hasattr(AnsibleLoader, 'add_implicit_resolver')
    assert hasattr(AnsibleLoader, 'add_path_resolver')
    assert hasattr(AnsibleLoader, 'add_constructor')
    assert hasattr(AnsibleLoader, 'dispose')
    assert hasattr(AnsibleLoader, 'get_data')
    assert hasattr(AnsibleLoader, 'get_single_data')
    assert hasattr(AnsibleLoader, 'check_data')
    assert hasattr(AnsibleLoader, 'compose_node')
    assert hasattr(AnsibleLoader, 'construct_document')
    assert hasattr(AnsibleLoader, 'construct_sequence')

# Generated at 2022-06-13 07:42:02.083137
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test: no vault string provided
    ansible_loader = AnsibleLoader('{encrypted_key: !vault |\n\n          $ANSIBLE_VAULT;1.1;AES256\n\n6131633237383036343964336633333037663133353533386232396462393239\n\n3536333531656161303762663366396265653935343332383130646535303165\n\n3330343630623536633735633732333065313466393365\n}\n', vault_secrets='secret')
    assert ansible_loader.get_single_data() == {'encrypted_key': ''}

    # Test: vault string provided

# Generated at 2022-06-13 07:42:07.466066
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.path import path_dwim
    from ansible.vars.unsafe_proxy import wrap_var

    loader = AnsibleLoader(open(path_dwim(u'test/sanity/vault/test2.yml')))

    print(loader.get_single_data())

# Generated at 2022-06-13 07:42:10.266267
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('', file_name='/tmp/test.yml')
    assert loader._filename == '/tmp/test.yml'
    assert loader.vault_secrets == None

# Generated at 2022-06-13 07:42:14.939204
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    content = """
- shell: /bin/false
  register: result
  no_log: true
- shell: /bin/false
  register: result
  no_log: true
"""
    l = AnsibleLoader(content, file_name='(string)')
    assert(None == l.get_single_data())
    data = l.get_many_data()
    assert(2 == len(data))

# Generated at 2022-06-13 07:42:30.365086
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # create a test instance of AnsibleLoader
    ansible_loader = AnsibleLoader("""
        ---
        - name: test_node
          connection: ssh
          gather_facts: no
          hosts: 127.0.0.1
        """)
    assert ansible_loader is not None

# Generated at 2022-06-13 07:42:41.902481
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:42:45.752166
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    _AnsibleLoader = AnsibleLoader(None, None, None)
    assert isinstance(_AnsibleLoader, Resolver)
    assert isinstance(_AnsibleLoader, Parser)
    assert isinstance(_AnsibleLoader, AnsibleConstructor)

# Generated at 2022-06-13 07:42:46.813530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert False


# Generated at 2022-06-13 07:42:56.294342
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''
    - hosts:
        - localhost
      user: root
      tasks:
        - name: install net-tools on centos7
          yum: name=net-tools state=present
          when: ansible_os_family == 'RedHat' and ansible_distribution_version == '7'
        - name: install net-tools on ubuntu 14.04
          apt: name=net-tools state=present
          when: ansible_os_family == 'Debian' and ansible_lsb.codename == 'trusty'
        - name: install net-tools on ubuntu 16.04
          apt: name=net-tools state=present
          when: ansible_os_family == 'Debian' and ansible_lsb.codename == 'xenial'
    '''
   

# Generated at 2022-06-13 07:42:58.094477
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=unused-argument
    assert True

# Generated at 2022-06-13 07:43:08.890192
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile
    import shutil

    dirpath = tempfile.mkdtemp()
    create_temp_yaml = lambda vars: open(os.path.join(dirpath, "test.yaml"), "w").write(vars)
    create_temp_yaml("---\nabc:\n  123: true")
    l = AnsibleLoader(open(os.path.join(dirpath, "test.yaml")), file_name=os.path.join(dirpath, "test.yaml"))
    results = l.get_single_data()
    assert results == {"abc": {"123": True}}

    create_temp_yaml("---\nabc:\n  123: true\ndef: [234, 345]")

# Generated at 2022-06-13 07:43:14.283227
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """Test ansible loader constructor."""
    sl = AnsibleLoader(stream='test_stream',file_name='test_file',vault_secrets='test_vault_secrets')
    assert sl.loader.stream.stream == 'test_stream'
    assert sl.constructor.file_name == 'test_file'
    assert sl.constructor.vault_secrets == 'test_vault_secrets'

# Generated at 2022-06-13 07:43:20.413540
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_text = """
a:
  - 1
  - 2
  - 3
b:
  - 1
  - 2
  - 3
c:
  - 1
  - 2
  - 3
"""
    ansible_loader = AnsibleLoader(test_text)
    parser_object = ansible_loader.get_single_data()
    assert parser_object is not None
    assert isinstance(parser_object, dict)
    assert isinstance(parser_object.get('a'), list)
    assert isinstance(parser_object.get('b'), list)
    assert isinstance(parser_object.get('c'), list)

# Generated at 2022-06-13 07:43:22.120806
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # TODO: this unit test does not test AnsibleLoader
    pass

# Generated at 2022-06-13 07:43:50.976334
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import BytesIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:43:56.062377
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.dict import AnsibleDict
    ansible_loader_factory = AnsibleLoader
    stream = 'test: {{ var1 }}'
    loader = ansible_loader_factory(stream, file_name='fake', vault_secrets='test')
    assert isinstance(loader.get_single_data(), AnsibleDict)

# Generated at 2022-06-13 07:44:07.417127
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def check(data, expected):
        loader = AnsibleLoader(data, vault_secrets=dict(foo="bar"))
        assert loader.construct_object(None, None) == expected

    # dict
    check("{foo: bar}", dict(foo='bar'))
    check("{foo: bar, baz: qux}", dict(foo='bar', baz='qux'))

    # list
    check("[foo, bar]", ['foo', 'bar'])
    check("[foo, {bar: baz}]", ['foo', dict(bar='baz')])

    # string
    check("foo", 'foo')
    check('"foo"', 'foo')

    # number
    check("42", 42)
    check("42.0", 42.0)

# Generated at 2022-06-13 07:44:09.645969
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """Test AnsibleLoader constructor by instantiating it"""
    ansible_loader = AnsibleLoader('')
    assert ansible_loader

# Generated at 2022-06-13 07:44:15.968828
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml
    # Basic test
    assert yaml.load('''
- hosts: localhost
  tasks:
  - include_tasks: "{{ foo }}"
''', Loader=AnsibleLoader) == [
        {
            u'hosts': u'localhost',
            u'tasks': [
                {
                    u'include_tasks': '{{ foo }}'
                }
            ]
        }
    ]

# Generated at 2022-06-13 07:44:18.436867
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '{"a": "b"}'
    loader = AnsibleLoader(stream=stream)
    data = loader.get_single_data()
    assert data == {'a': 'b'}

# Generated at 2022-06-13 07:44:33.215166
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping, AnsibleUnicode
    al = AnsibleLoader("[1,2,3]")
    ao = al.get_single_data()
    assert isinstance(ao, AnsibleSequence)
    assert ao.value == [1, 2, 3]
    al = AnsibleLoader("foo: bar")
    ao = al.get_single_data()
    assert isinstance(ao, AnsibleMapping)
    assert isinstance(list(ao.value.values())[0], AnsibleUnicode)
    assert list(ao.value.values())[0].value == 'bar'
    al = AnsibleLoader("foo: 123")
    ao = al.get_single_data()

# Generated at 2022-06-13 07:44:43.720890
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    data = """
    - key1: value1
      key2: value2
    - key3: value3
    - key4:
        subkey1: subvalue1
        subkey2: subvalue2
    """

    loader = AnsibleLoader(data)
    data = loader.get_single_data()

    assert isinstance(data, AnsibleSequence)
    assert len(data) == 3

    elem1 = data[0]
    assert isinstance(elem1, AnsibleMapping)

    elem2 = data[1]
    assert isinstance(elem2, AnsibleMapping)

    elem3 = data[2]
    assert isinstance(elem3, AnsibleMapping)

   

# Generated at 2022-06-13 07:44:49.101926
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    sys.path.append("/Users/jason/projects/ansible/lib/ansible")
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE
    from ansible.parsing.vault import VaultLib
    loader = AnsibleLoader(vault_secrets=[(DEFAULT_VAULT_PASSWORD_FILE, VaultLib())])
    loader.construct_yaml_str("value: !!str 5")

# Generated at 2022-06-13 07:44:59.921103
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.composer import Composer
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from yaml.parser import Parser
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from yaml.resolver import Resolver

    class AnsibleLoader(Reader, Scanner, Parser, Composer, AnsibleConstructor, Resolver):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Reader.__init__(self, stream)
            Scanner.__init__(self)
            Parser.__init__(self)  # pylint: disable=non-parent-init-called
            Composer.__init__(self)

# Generated at 2022-06-13 07:45:49.059006
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    This is a test for validate constructor of class AnsibleLoader,
    it is only valid for libyaml=True.
    """
    if HAS_LIBYAML:
        loader = AnsibleLoader("---\nhosts:\n- localhost")
        assert loader.constructor.vault_secrets == None
        assert loader.constructor.file_name == None
    else:
        loader = AnsibleLoader("---\nhosts:\n- localhost")
        assert loader.constructor.vault_secrets == None
        assert loader.constructor.file_name == None


# Generated at 2022-06-13 07:45:56.752315
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def _assert_AnsibleLoader_loaded_types(res):
        assert isinstance(res, dict)
        for v in res.values():
            assert isinstance(v, dict)
            for v_key, v_val in v.items():
                assert isinstance(v_val, str)
                assert v_key in ('default', 'vault')

    loader = AnsibleLoader(None)

    res = loader._yaml_get_default_values()
    _assert_AnsibleLoader_loaded_types(res)

    res = loader._yaml_get_vault_values()
    _assert_AnsibleLoader_loaded_types(res)

# Generated at 2022-06-13 07:46:02.895920
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader( 'hello world' )
    assert loader.stream == 'hello world'
    assert isinstance( loader, Reader )
    assert isinstance( loader, Scanner )
    assert isinstance( loader, Parser )
    assert isinstance( loader, Composer )
    assert isinstance( loader, AnsibleConstructor )
    assert isinstance( loader, Resolver )

# Generated at 2022-06-13 07:46:09.570585
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    sys.path.append('..')
    import ansible.parsing.yaml.objects
    sys.modules['ansible.parsing.yaml.objects'] = ansible.parsing.yaml.objects
    sys.modules['ansible.parsing.yaml.loader'] = ansible.parsing.yaml.loader
    import ansible.parsing.yaml.loader
    from ansible.parsing.yaml.loader import AnsibleLoader
    f = open('./test.yml')
    test_loader=AnsibleLoader(f)
    test_loader.get_single_data()
    f.close()

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:46:22.199674
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

    data = '''
    a:
      - "1"
      - 1
    b:
      - "2"
      - 2.0
    '''

    loader = yaml.loader.BaseLoader
    if hasattr(loader, 'Loader'):
        loader = loader.Loader

    loader = loader(data)
    loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                           lambda loader, node: dict(loader.construct_pairs(node)))
    for datum in loader:
        print(datum)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:46:25.742343
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
    hello: world
    foo:
       - bar
    """
    loader = AnsibleLoader(data)
    assert loader.get_single_data() == {'hello': 'world', 'foo': ['bar']}

# Generated at 2022-06-13 07:46:27.526701
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, 'fake_file.yml')
    assert loader
    assert loader._loader is None

# Generated at 2022-06-13 07:46:31.982260
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class AnsibleLoader(AnsibleLoader):
        pass

    instance = AnsibleLoader(None)
    assert isinstance(instance, AnsibleConstructor)
    assert instance.get_data() == None

# Generated at 2022-06-13 07:46:32.647301
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("")
    assert loader is not None

# Generated at 2022-06-13 07:46:33.610530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:48:14.632365
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream=u'''
    name: TestPlay
    hosts: all
    gather_facts: no
    roles:
      - { role: testrole1, var1: testvar }
      - role: testrole2
    user: testuser
    '''
    loader = AnsibleLoader(stream)
    obj = loader.get_single_data()
    assert obj.get('name') == 'TestPlay'
    assert obj.get('hosts') == 'all'
    assert obj.get('gather_facts') == 'no'
    assert obj.get('user') == 'testuser'
    assert isinstance(obj.get('roles'),list)
    assert len(obj.get('roles')) == 2
    assert obj.get('roles')[0].get('role') == 'testrole1'
    assert obj

# Generated at 2022-06-13 07:48:27.384530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    source = """
    - hosts: localhost
      tasks:
        - action: copy src={{ src }} dest={{ dest }}
    """

    source = source.encode('utf-8')
    loader = AnsibleLoader(source, file_name="file.yml")
    parsed = loader.get_single_data()
    assert parsed[0]['hosts'] == 'localhost'
    assert parsed[0]['tasks'][0]['action']['module'] == 'copy'
    assert parsed[0]['tasks'][0]['action']['args']['src'] == '{{ src }}'
    assert parsed[0]['tasks'][0]['action']['args']['dest'] == '{{ dest }}'

    source2 = """
    include: {{ path }}
    """

    source

# Generated at 2022-06-13 07:48:28.579548
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    x = AnsibleLoader('')

# Generated at 2022-06-13 07:48:38.093199
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import json
    from ansible.parsing.yaml.objects import AnsibleUnicode
    tests = {
        'a': AnsibleUnicode("a"),
        'a#': AnsibleUnicode("a#"),
        "a#'": AnsibleUnicode("a#'"),
        "a 'b'": AnsibleUnicode("a 'b'"),
        'a\n#c': AnsibleUnicode("a#c"),
        'a\r\n#c': AnsibleUnicode("a#c"),
    }

    # encoding is hard to test without accessing private attributes,
    # so just skip the test when using libyaml (which is the default)