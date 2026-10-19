

# Generated at 2022-06-13 07:38:41.994946
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)
    stream = 'test'
    file_name = 'testFileName'
    vault_secrets = ['secret']
    ansible_loader = AnsibleLoader(stream, file_name, vault_secrets)
    assert isinstance(ansible_loader.construct_yaml_str(stream), AnsibleUnicode)
    assert isinstance(ansible_loader.construct_yaml_seq(stream), AnsibleSequence)

# Generated at 2022-06-13 07:38:50.738456
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Test AnsibleLoader class
    '''
    data = '''
        - hosts: icedtea
          gather_facts: False
          tasks:
            - debug:
                var: hostvars'''
    l = AnsibleLoader(data)
    first_item = l.get_single_data()
    assert isinstance(first_item, dict)
    assert list(first_item.keys()) == ['hosts', 'gather_facts', 'tasks']
    assert first_item['hosts'] == 'icedtea'
    assert first_item['gather_facts'] is False
    assert isinstance(first_item['tasks'], list)
    second_item = first_item['tasks'][0]
    assert isinstance(second_item, dict)

# Generated at 2022-06-13 07:38:59.452211
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    vault_pass = 'secret'
    vault_id = '734da9b5-5b99-48fb-b93c-22a1dcb513dd'
    vault = VaultLib(vault_pass)

# Generated at 2022-06-13 07:39:00.191530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:08.435345
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = AnsibleLoader('')
    assert data
    data = AnsibleLoader('{ test: pass }')
    assert data
    data = AnsibleLoader('{ test: { nested: pass } }')
    assert data
    data = AnsibleLoader('---')
    assert data
    data = AnsibleLoader('{ test: &test_reference pass }')
    assert data
    data = AnsibleLoader('{ test2: *test_reference }')
    assert data
    data = AnsibleLoader('{ test: !!str pass }')
    assert data


# Generated at 2022-06-13 07:39:09.755434
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test constructor
    assert AnsibleLoader

# Generated at 2022-06-13 07:39:21.393582
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
        - include: foo.yml
        - include: test.yml
        - name: test1
          include: foo.yml
        - include: foo.yml
          when: foo
        - include: foo.yml
          when: bar
        - debug: msg="hello world"
        - include_tasks: foo.yml
        - import_playbook: foo.yml
        - import_tasks: foo.yml
    '''

    # test with file name
    file_name = "foo.yml"

    loader = AnsibleLoader(stream, file_name=file_name)
    foo = loader.get_single_data()

# Generated at 2022-06-13 07:39:29.108940
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io

    yaml = io.StringIO("""
---
# this is a comment
- hosts:
    host1:
      ansible_host: 1.2.3.4
    host2:
      ansible_host: 5.6.7.8
nop: [cmd1, cmd2]
- name: test
  action:
    module: ping
""")

    loader = AnsibleLoader(yaml, file_name='file_name')
    result = list(loader)

    assert result[0]['hosts']['host1']['ansible_host'] == '1.2.3.4'
    assert result[0]['nop'][0] == 'cmd1'
    assert result[1]['name'] == 'test'

# Generated at 2022-06-13 07:39:32.669403
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' test AnsibleLoader class constructor '''
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:39:33.832797
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None, None)

# Generated at 2022-06-13 07:39:43.802525
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # test datatypes
    stream = 'key: str'
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert type(data['key']) == str

    stream = 'key: []'
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert type(data['key']) == list

    stream = 'key: {}'
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert type(data['key']) == dict

    # test scalar value of None
    stream = 'key: '
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert type(data['key']) == type(None)

    # 1012: check if vaulted

# Generated at 2022-06-13 07:39:51.198602
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # create a vault data
    vault_password = 'dummy_password'
    vault_secrets = {}
    vault_secrets['_ansible_vault'] = vault_password
    vault_secrets['_ansible_vault_secret_id'] = '0000'

    # create an unsafe test data
    unsafe_text = 'this is some unsafe text'

    # create the loader and dump the vault data
    loader = AnsibleLoader('', vault_secrets=vault_secrets, file_name='test')
    vault_test = AnsibleVaultEnc

# Generated at 2022-06-13 07:39:56.107973
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils._text import to_text
    stream = """
---
a: 1
b:
  - {c: 3, d: 4}
  - {c: 5}
"""
    print(to_text(AnsibleLoader(stream).get_single_data()))

# Generated at 2022-06-13 07:39:58.674120
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    "This does not test the entire class, just a sanity check for the constructor"
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:40:04.900606
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Verify that AnsibleLoader is a subclass of all its bases.
    '''
    if HAS_LIBYAML:
        assert issubclass(AnsibleLoader, Parser)
    else:
        assert issubclass(AnsibleLoader, Reader)
        assert issubclass(AnsibleLoader, Scanner)
        assert issubclass(AnsibleLoader, Parser)
        assert issubclass(AnsibleLoader, Composer)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:40:10.812722
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(b"TESTING ANSIBLE LOADER")
    assert loader.stream == b"TESTING ANSIBLE LOADER"  # or: assert loader.get_stream() == b"TESTING ANSIBLE LOADER"
    # assert loader.
    # assert loader.
    assert loader.file_name is None
    assert loader.vault_secrets is None



# Generated at 2022-06-13 07:40:23.076292
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import os

    # Test is only for libyaml case, for C-based libyaml the YAML files
    # generate by python-yaml library are not readable by Ansible.
    if HAS_LIBYAML:
        from ansible.errors import AnsibleError
        from ansible.parsing.yaml.objects import AnsibleUnicode
        from ansible.parsing.yaml.dumper import AnsibleDumper

        # Test __init__()
        loader = AnsibleLoader(None)

        # Test read_data()
        settings = AnsibleLoader(None).read_data(os.path.join('test', 'yaml', 'fail_ini_type.yaml'))
        assert not settings

        # Test load_from_file()

# Generated at 2022-06-13 07:40:28.261848
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader(u'test_string_here')
    assert isinstance(loader.construct_object(None, None), AnsibleUnicode)

# Generated at 2022-06-13 07:40:30.860134
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:40:32.254768
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:40:41.596684
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    # Test with a built-in Python type
    test_dict_str = '{"key":"value"}'
    test_dict = {"key":"value"}
    assert test_dict == AnsibleLoader(io.StringIO(test_dict_str)).get_single_data()
    assert test_dict == AnsibleLoader(test_dict_str).get_single_data()
    # Test with a custom Python type
    test_ansible_str = 'key=value'
    test_ansible = {'key': ['=', 'value']}
    assert test_ansible == AnsibleLoader(io.StringIO(test_ansible_str)).get_single_data()
    assert test_ansible == AnsibleLoader(test_ansible_str).get_single_data()

# Generated at 2022-06-13 07:40:48.674754
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
---
# This is a YAML comment
name: TestUser
# Another comment
home_dir: /home/testuser # This is also a comment
# One more comment
'''
    load = AnsibleLoader(data)
    assert(load.get_single_data() == {'name': 'TestUser', 'home_dir': '/home/testuser'})

# Generated at 2022-06-13 07:40:55.823085
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.loader
    ansible.parsing.yaml.loader.AnsibleLoader

# The following is a list of variables that are expected to be set by
# various methods in the YAML parsing code, at least on the ansible
# namespace. This list is used to test that we do not get duplicate
# variable names being set in the namespace.

# FIXME: this test is really only for parser.py. Need to move into the
# appropriate location.


# Generated at 2022-06-13 07:41:08.444739
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def check(data, expected):
        class MyDumper(AnsibleConstructor):
            def __init__(self, file_name):
                AnsibleConstructor.__init__(self, file_name=file_name)
        loader = MyDumper("testing_file")
        assert loader.construct_python_dict(data) == expected

    # bool
    check([True, False], [True, False])
    # int
    check([0, 10, -5], [0, 10, -5])
    # float
    check([0.5, 9e-3, 4.3], [0.5, 9e-3, 4.3])
    # string
    check(["hello", "blah"], ["hello", "blah"])
    # list

# Generated at 2022-06-13 07:41:14.314663
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader('foo')
    assert loader.get_single_data() == 'foo'
    loader.dispose()


# Generated at 2022-06-13 07:41:20.492070
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()
    loader = AnsibleLoader(None, file_name=None, vault_secrets=[context])
    assert hasattr(loader, '_construct_mapping')
    assert hasattr(loader, '_construct_sequence')

# Generated at 2022-06-13 07:41:24.641122
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    loader = AnsibleLoader(stream='')

    assert isinstance(loader, Parser), 'loader is not instance of Parser'
    assert isinstance(loader, AnsibleConstructor), 'loader is not instance of AnsibleConstructor'
    assert isinstance(loader, Resolver), 'loader is not instance of Resolver'

# Generated at 2022-06-13 07:41:28.284292
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    old_stdout = sys.stdout

    ansible_loader = AnsibleLoader(os.path.abspath("test.yml"))

    sys.stdout = old_stdout

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:38.262738
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleSequence
    vault_pass = 'foobar'
    vault_secrets = [('default', VaultLib([vault_pass]))]
    loader = AnsibleLoader(None, vault_secrets=vault_secrets)
    aseq1 = AnsibleSequence()
    aseq1.append('{{ foo }}')
    aseq2 = AnsibleSequence()
    aseq2.append('{{ bar }}')
    loader.constructed_objects['!vault'] = {'pass': vault_pass, 'vault_secrets': vault_secrets}
    loader.constructed_objects['!seq'] = [aseq1, aseq2]

# Generated at 2022-06-13 07:41:39.096987
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:41:49.001933
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream=None)
    assert loader is not None


# Generated at 2022-06-13 07:41:52.739997
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.vault import VaultLib
    ansible_loader = AnsibleLoader(vault_secrets=VaultLib())
    assert isinstance(ansible_loader, AnsibleConstructor)

# Generated at 2022-06-13 07:41:55.487205
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    stream = '''
    something:
        - else
    '''

    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data is not None

# Generated at 2022-06-13 07:41:57.154985
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader('')

# Generated at 2022-06-13 07:41:58.823078
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    # import pdb; pdb.set_trace()

# Generated at 2022-06-13 07:42:00.061483
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 07:42:01.523424
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:42:06.297816
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestLoader(AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            super(TestLoader, self).__init__(stream, file_name, vault_secrets)

    try:
        loader = TestLoader(stream='unicode:')
    except TypeError:
        assert False, "AnsibleLoader constructor failed to accept unicode"

    assert True, "AnsibleLoader constructor does not accept unicode"

# Generated at 2022-06-13 07:42:15.272037
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader

# Generated at 2022-06-13 07:42:22.566321
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import AnsibleLoader

    stream = '''
---
# This is a comment for the complete document
- hosts:
    - best-web-1
    - best-web-2
  remote_user: root
  tasks:
    - name: test
      command: echo 'hello'
'''

    loader = AnsibleLoader(stream, '/dev/null', None)
    data = loader.get_single_data()
    assert data['hosts'] == ['best-web-1', 'best-web-2']



# Generated at 2022-06-13 07:42:42.019411
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, (Reader, Scanner, Parser, Composer, AnsibleConstructor, Resolver)) or issubclass(AnsibleLoader, (Parser, AnsibleConstructor, Resolver))

# Generated at 2022-06-13 07:42:45.039466
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        # parser warns on empty strings
        AnsibleLoader('', 'fakeyaml')
    except Exception:
        assert True
    else:
        assert False

# Generated at 2022-06-13 07:42:46.122278
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # no need to test anything
    assert True

# Generated at 2022-06-13 07:42:49.827367
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io

    yaml_file = io.StringIO(u'---\ntest: test\n')
    loader = AnsibleLoader(yaml_file)
    data = loader.get_single_data()
    assert data['test'] == 'test'

# Generated at 2022-06-13 07:42:58.306853
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.constants import DEFAULT_VAULT_ID_MATCH

    vault_secrets = dict(identity='test', password='test')

# Generated at 2022-06-13 07:43:08.962042
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:43:18.308170
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    r'''
    class AnsibleLoader(Reader, Scanner, Parser, Composer, AnsibleConstructor, Resolver):
    |  def __init__(self, stream, file_name=None, vault_secrets=None):
    |      Reader.__init__(self, stream)
    |      Scanner.__init__(self)
    |      Parser.__init__(self)  # pylint: disable=non-parent-init-called
    |      Composer.__init__(self)
    |      AnsibleConstructor.__init__(self, file_name=file_name, vault_secrets=vault_secrets)
    |      Resolver.__init__(self)
    '''

    # Mock modules
    import sys


# Generated at 2022-06-13 07:43:20.757219
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(stream=None)

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:43:31.212637
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # No Exception raised
    AnsibleLoader(stream=None, file_name=None, vault_secrets=None)

    # Exception raised, check the type and the message
    try:
        AnsibleLoader(None,'abc')
    except TypeError as e:
        assert isinstance(e, TypeError)
        assert e.args[0] == "__init__() missing 1 required positional argument: 'vault_secrets'"

    # Exception raised, check the type and the message
    try:
        AnsibleLoader(None, 'def', 'ghi')
    except TypeError as e:
        assert isinstance(e, TypeError)
        assert e.args[0] == "__init__() takes 1 positional argument but 3 were given"

# Generated at 2022-06-13 07:43:32.628769
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:44:06.735718
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:44:11.972005
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("hello")
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)
    if HAS_LIBYAML:
        assert isinstance(loader, Parser)
    else:
        assert isinstance(loader, Parser)
        assert isinstance(loader, Composer)
        assert isinstance(loader, Reader)
        assert isinstance(loader, Scanner)

# Generated at 2022-06-13 07:44:16.019114
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Only if libyaml is installed
    if HAS_LIBYAML:
        # Test empty string
        AnsibleLoader("")
        # Test contains string
        AnsibleLoader("test")

if __name__ == "__main__":
    # Unit test for class AnsibleLoader
    test_AnsibleLoader()

# Generated at 2022-06-13 07:44:19.478509
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib

    loader = AnsibleLoader(file_name='memory_vault', vault_secrets=[('default', VaultLib('password'))])
    loader.get_single_data()
    loader.construct_document(None)
    loader.get_data()

# Generated at 2022-06-13 07:44:25.432211
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    stream = open("tests/constructor_test.yml")
    loader = AnsibleLoader(stream, vault_secrets=VaultLib())
    loader.get_single_data()

# Generated at 2022-06-13 07:44:36.767300
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

# Generated at 2022-06-13 07:44:46.153135
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml import load
    from ansible.module_utils.common.yaml import HAS_LIBYAML, Parser

    assert HAS_LIBYAML or issubclass(AnsibleLoader, Reader)
    assert HAS_LIBYAML or issubclass(AnsibleLoader, Scanner)
    assert issubclass(AnsibleLoader, Parser)
    assert HAS_LIBYAML or issubclass(AnsibleLoader, Composer)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

    # test load()
    load("---\nhello world")
    load("hello world")  # no exception

# Generated at 2022-06-13 07:44:48.860030
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = u'QWxhZGRpbjpvcGVuIHNlc2FtZQ==\n'
    loader = AnsibleLoader(data)
    loader.get_single_data()

# Generated at 2022-06-13 07:44:59.738919
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleUnicode


# Generated at 2022-06-13 07:45:10.511907
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import shutil
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleUnicode

    (fd, tempfile_path) = tempfile.mkstemp()
    stream = open(tempfile_path, mode='r+b')

    AnsibleLoader(stream)

    content = """
    - foo: bar
    - baz: 123
    """
    stream.write(content)
    stream.seek(0)

    data = list(AnsibleLoader(stream))
    assert data[0]['foo'] == AnsibleUnicode('bar')
    assert data[1]['baz'] == 123

    stream.close()
    os.close(fd)
    os.remove(tempfile_path)

# Generated at 2022-06-13 07:46:29.814191
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
        - hosts: localhost
          tasks:
          - name: data1
            debug:
                msg: "data1"
        - hosts: localhost
          tasks:
          - name: data2
            debug:
                msg: "data2"
    """
    ansible_loader = AnsibleLoader(data, file_name='/tmp/test_AnsibleLoader.yaml')
    for i, _data in enumerate(ansible_loader):
        assert _data == {u'hosts': u'localhost', u'tasks': [{u'name': u'data%d' % (i+1), u'debug': {u'msg': u'data%d' % (i+1)}}]}

# Generated at 2022-06-13 07:46:37.265267
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    sample = '''---
key1: value1
key2:
- "{{ inventory_hostname }}"
'''
    loader = AnsibleLoader(stream=sample, vault_secrets=None)
    result = loader.get_single_data()
    assert result is not None
    assert result['key2'][0] == '{{ inventory_hostname }}'
    assert result['key1'] == 'value1'

# Generated at 2022-06-13 07:46:47.551969
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import ansible.parsing.yaml.loader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnicode

    test_file = os.path.join(os.path.dirname(sys.modules[ansible.parsing.yaml.loader.__name__].__file__), 'constructor_data_files', 'loader_test_file.yml')
    with open(test_file, 'r') as f:
        data = AnsibleLoader(f).get_single_data()

    assert data['a_string'] is None
    assert data['a_unicode'] == AnsibleUnicode(u'hello')

# Generated at 2022-06-13 07:46:51.853809
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    stream = "'foo': 'bar'\n"
    yaml = AnsibleLoader(stream)
    loader_data = yaml.get_single_data()
    assert loader_data['foo'] == 'bar'

# Generated at 2022-06-13 07:46:54.067773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(stream="")

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:46:58.341485
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test the AnsibleLoader class
    stream = "!foo 123"
    loader = AnsibleLoader(stream)
    print(loader.get_single_data())

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:07.637368
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret


# Generated at 2022-06-13 07:47:08.958223
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(b'')
    assert loader is not None

# Generated at 2022-06-13 07:47:18.635334
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=missing-docstring
    from ansible.parsing.dataloader import DataLoader

    data = """
---
# comments
- hosts: localhost
  gather_facts: no
  tasks:
  - shell: echo 1234
    register: result
  - fail: msg="{{ result.stdout }}"

- hosts: localhost
  gather_facts: no
  tasks:
  - name: test the idempotent task
    shell: echo 1234
    register: result
  - fail: msg="{{ result.stdout }}"
  - name: make sure it failed
    assert:
      that:
        - result.stdout != result.stdout
"""

    loader = DataLoader()
    inventory = loader.load(data)

    assert inventory.get_hosts('localhost')

# Generated at 2022-06-13 07:47:27.454328
# Unit test for constructor of class AnsibleLoader