

# Generated at 2022-06-13 07:38:38.786073
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('test')
    assert loader

    # Test the default values of 'file_name' and 'vault_secrets'
    assert loader.file_name == '<string>'
    assert loader.vault_secrets is None

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:38:45.795909
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # This doesn't test loading of a file, unfortunately, since the dumper
    # doesn't support all the same features as the constructor
    data = AnsibleLoader("""
        ---
        - hosts: all
          gather_facts: no
          tasks:
            - action: command /bin/foo
              register: result
            - action: command /usr/bin/bar
              when: result.rc == 5
              register: result2
              changed_when: result2.rc > 0
            - action: command /bin/baz
              register: result3
              failed_when: result3.rc != 0
        """).get_single_data()
    print(data)

# Generated at 2022-06-13 07:38:55.297895
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader
    import ansible.parsing.yaml.objects
    import yaml
    l = AnsibleLoader("hello: world")
    assert isinstance(l, yaml.resolver.Resolver)
    assert isinstance(l, ansible.parsing.yaml.constructor.AnsibleConstructor)
    assert isinstance(l, yaml.composer.Composer)
    assert isinstance(l, yaml.parser.Parser)
    assert isinstance(l, yaml.reader.Reader)
    assert isinstance(l, yaml.scanner.Scanner)
    assert isinstance(l, ansible.parsing.yaml.objects.AnsibleBaseYAMLObject)

# Generated at 2022-06-13 07:39:01.749698
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:39:03.082113
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    if HAS_LIBYAML:
        assert AnsibleLoader(None)
    else:
        assert AnsibleLoader(None)

# Generated at 2022-06-13 07:39:11.701998
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    text = '''
    - hosts: localhost
      connection: local
      tasks:
        - name: test
          tags: test
          action:
            module: shell
            args: ls
    '''
    loader = AnsibleLoader(text)
    obj = loader.get_single_data()

    assert obj['tasks'][0]['name'] == 'test'
    assert obj['tasks'][0]['tags'] == ['test']
    assert obj['tasks'][0]['action']['module'] == 'shell'
    assert obj['tasks'][0]['action']['args'] == 'ls'

# Generated at 2022-06-13 07:39:15.218105
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Make test
    yaml_obj = '''{
      "A": "B",
      "C": "D",
      "E": "F"
    }'''
    stream = AnsibleLoader(yaml_obj)
    assert isinstance(stream, AnsibleLoader)

# Generated at 2022-06-13 07:39:26.453094
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile


# Generated at 2022-06-13 07:39:39.251589
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml

    yaml_str = """
    - hosts: all
      tasks:
      - include: no_such_file.yml
      - name: do something
        command: /bin/true
    """

    # TODO: validate that file name is recorded in list of errors

    def my_constructor(loader, node):
        return loader.construct_yaml_null(node)

    def my_multi_constructor(loader, tag_prefix, node):
        return loader.construct_yaml_null(node)

    class MyLoader(AnsibleLoader):
        add_constructor(u'!null', my_constructor)
        add_multi_constructor(u'!', my_multi_constructor)

    MyLoader.add

# Generated at 2022-06-13 07:39:43.591069
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=too-many-function-args
    loader = AnsibleLoader('[1,2,3]', file_name='./test.txt', vault_secrets=[])
    data = loader.get_single_data()
    assert data == [1, 2, 3]

# Generated at 2022-06-13 07:39:48.207160
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class Test:
        def __init__(self):
            pass

    class Test2(object):
        def __init__(self):
            pass

    assert(Test is not Test2)

# Generated at 2022-06-13 07:39:55.455972
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=missing-docstring
    loader = AnsibleLoader(None, None, None)
    assert loader._filename == None
    assert loader._vault_secrets == None
    loader = AnsibleLoader(None, "foo", None)
    assert loader._filename == "foo"
    assert loader._vault_secrets == None
    loader = AnsibleLoader(None, "foo", "bar")
    assert loader._filename == "foo"
    assert loader._vault_secrets == "bar"

# Generated at 2022-06-13 07:40:04.869688
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from tests.test_utils import AnsibleLoaderTestCase, dict_equal

    (result, errors) = AnsibleLoaderTestCase.loadYaml('')
    assert dict_equal(result, {})

    (result, errors) = AnsibleLoaderTestCase.loadYaml('a: b')
    assert dict_equal(result, {'a': 'b'})

    (result, errors) = AnsibleLoaderTestCase.loadYaml('a: b\nd: e')
    assert dict_equal(result, {'a': 'b', 'd': 'e'})

    (result, errors) = AnsibleLoaderTestCase.loadYaml('a: b\n  d: e')
    assert dict_equal(result, {'a': 'b', 'd': 'e'})

    (result, errors) = AnsibleLoaderTest

# Generated at 2022-06-13 07:40:10.391621
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import sys

    from ansible.parsing.yaml.constructor import AnsibleConstructor

    class AnsibleLoader(Reader, Scanner, Parser, Composer, AnsibleConstructor, Resolver):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Reader.__init__(self, stream)
            Scanner.__init__(self)
            Parser.__init__(self)  # pylint: disable=non-parent-init-called
            Composer.__init__(self)
            AnsibleConstructor.__init__(self, file_name=file_name, vault_secrets=vault_secrets)
            Resolver.__init__(self)


# Generated at 2022-06-13 07:40:22.568226
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import binary_type, text_type

    loader = AnsibleLoader({})

    # Test AnsibleMapping
    data = {'key1': 'value1', 'key2': 'value2'}
    ansible_data = loader.construct_yaml_map(data)
    assert isinstance(ansible_data, AnsibleMapping)
    if PY3:
        assert isinstance(ansible_data.get('key1'), AnsibleUnsafeText)
        assert isinstance(ansible_data.get('key2'), AnsibleUnsafeText)

# Generated at 2022-06-13 07:40:27.466200
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    data = loader.load("""
    ---
    foo: this is a string
    bar: 12345
    bam:
      - 1st item
      - 2nd item
      - 3rd item
    """)

    assert isinstance(data['foo'], AnsibleUnicode)
    assert isinstance(data['bar'], int)
    assert isinstance(data['bam'][0], AnsibleUnicode)
    assert isinstance(data['bam'][1], AnsibleUnicode)
    assert isinstance(data['bam'][2], AnsibleUnicode)

# Generated at 2022-06-13 07:40:28.754383
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:40:33.076296
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
---
# A load of YAML - passed to the constructor
"""
    stream = yaml.load(data, AnsibleLoader)
    assert stream['file_name'] == None
    assert stream['vault_secrets'] == None


# Generated at 2022-06-13 07:40:34.606834
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, '__init__')

# Generated at 2022-06-13 07:40:39.965715
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def check(data, expected):
        loader = AnsibleLoader(data)
        got = loader.get_single_data()
        assert got == expected

    # boolean
    check(b'---\ntrue\n', True)
    check(b'---\nfalse\n', False)
    # integer
    check(b'---\n10\n', 10)
    # float
    check(b'---\n10.0\n', 10.0)
    # list
    check(b'---\n- foo\n- bar\n', ['foo', 'bar'])
    # dict
    check(b'---\nfoo: bar\n', {'foo': 'bar'})
    # list of dict

# Generated at 2022-06-13 07:40:47.974484
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    l = AnsibleLoader(file_name='filename')
    assert 'filename' == l.file_name

# Generated at 2022-06-13 07:40:58.119629
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    # Read from stdin
    # TODO: the vault password is compared with the one from constructor, but
    #       we don't send the vault password in constructor.
    #       It's not a problem for now, but we may want to clean up the code.
    stream = open('test/unit/fragments/test_loader.yml', 'r')
    loader = AnsibleLoader(stream, vault_secrets=[{'secret': 'foo'}, {'secret': 'bar'}])

    # Read from a file
    vault_file = open('test/unit/fragments/test_loader.vault', 'r')
    vault_pass = VaultLib('foo')

# Generated at 2022-06-13 07:41:06.171089
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    loader = AnsibleLoader(
        stream='---\n'
               '- hosts: localhost\n'
               '  connection: local\n'
               '  tasks:\n'
               '    - debug:\n'
               '        msg: \'test\'\n'
    )
    data = loader.get_single_data()
    assert data == [{'hosts': 'localhost', 'connection': 'local', 'tasks': [{'debug': {'msg': 'test'}}]}]

# Generated at 2022-06-13 07:41:19.211076
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    from yaml.error import YAMLError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

# Generated at 2022-06-13 07:41:29.375730
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys

    stream = '''
    - hosts: localhost
      tasks:
      - name: print the message once
        debug: msg="hello"
        when: 1 == 1
    '''
    if sys.version_info[:2] == (2, 6):
        from ansible.parsing.yaml.constructor import AnsibleLoader26 as AnsibleLoader
        loader = AnsibleLoader(stream)
    else:
        loader = AnsibleLoader(stream)
    data = yaml.load(stream, AnsibleLoader)
    assert data[0]['hosts'] == 'localhost'
    assert data[0]['tasks'][0]['name'] == 'print the message once'
    assert data[0]['tasks'][0]['debug']['msg'] == 'hello'

# Generated at 2022-06-13 07:41:32.981348
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    class fpr(object):
        def read(self):
            return "gid: 10000\n"
    res = yaml.load(fpr(), Loader=AnsibleLoader)
    assert res['gid'] == '10000'

# Generated at 2022-06-13 07:41:35.269281
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, file_name="file.yml")
    assert loader.file_name == "file.yml"

# Generated at 2022-06-13 07:41:43.116419
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import os
    from ansible.parsing.vault import VaultLib

    assert AnsibleLoader

# Generated at 2022-06-13 07:41:52.563017
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.module_utils.six import PY3, text_type
    import sys

    if not PY3:
        if sys.version_info < (2, 7):
            assert issubclass(AnsibleLoader, AnsibleConstructor)
            assert issubclass(AnsibleLoader, Parser)
            assert issubclass(AnsibleLoader, Resolver)
        else:
            assert issubclass(AnsibleLoader, AnsibleConstructor)
            assert issubclass(AnsibleLoader, Reader)
            assert issubclass(AnsibleLoader, Scanner)
            assert issubclass(AnsibleLoader, Parser)
            assert issubclass(AnsibleLoader, Composer)

# Generated at 2022-06-13 07:41:56.794635
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    sample = u"""
    foo: 1
    bar:
      - 1
      - 2
    """
    loader = AnsibleLoader(io.StringIO(sample))
    data = loader.get_single_data()
    assert data == { 'foo': 1, 'bar': [ 1, 2 ] }

# Generated at 2022-06-13 07:42:06.338163
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test = AnsibleLoader(None)

# Generated at 2022-06-13 07:42:12.192359
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import tempfile

    # Create a temporary file
    (fd, tmp_f) = tempfile.mkstemp()
    test_vars = {
        'var': {
            'a': 'b',
            'c': 'd',
        },
    }

    # Write the test_vars to the temporary file
    try:
        with os.fdopen(fd, 'w') as f:
            f.write("---\n%s\n" % test_vars)
    except:
        # Wasn't able to create the file
        os.remove(tmp_f)
        raise

    # Load the contents of the file into a dictionary

# Generated at 2022-06-13 07:42:19.230635
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    filename = 'tests/constructors_test_file'
    stream = open(filename, 'r')
    loader = AnsibleLoader(stream)
    assert loader.file_name is not None
    assert loader.file_name == filename
    assert loader.stream is not None
    assert loader.vault_secrets is None

    vault_secrets = [{'password1': 'password1'}, {'password2': 'password2'}]
    loader = AnsibleLoader(stream, file_name=filename, vault_secrets=vault_secrets)

    assert loader.stream is not None
    assert loader.file_name is not None
    assert loader.file_name == filename
    assert loader.vault_secrets is not None
    assert len(loader.vault_secrets) == 2

# Generated at 2022-06-13 07:42:20.204890
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Parser)

# Generated at 2022-06-13 07:42:23.002250
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert HAS_LIBYAML in [True, False]
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:42:38.195897
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Loads nothing
    empty = AnsibleLoader('', None, None)
    assert empty.get_single_data() is None

    # Loads something
    something = AnsibleLoader('key: value\n', None, None)
    assert something.get_single_data() == {'key': 'value'}

    # Loads integer
    integer = AnsibleLoader('key: 42\n', None, None)
    assert integer.get_single_data() == {'key': 42}

    # Loads float
    _float = AnsibleLoader('key: 42.5\n', None, None)
    assert _float.get_single_data() == {'key': 42.5}

    # Loads boolean
    boolean = AnsibleLoader('key: yes\n', None, None)
    assert boolean.get_single_data

# Generated at 2022-06-13 07:42:41.435095
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import _AnsibleVaultEncryptedUnicode, \
        _AnsibleVaultEncryptedUnicodeString

    assert isinstance(_AnsibleVaultEncryptedUnicode(), _AnsibleVaultEncryptedUnicodeString)



# Generated at 2022-06-13 07:42:49.158574
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml = u'''---
        food:
            - pie
            - apple
        fruit:
            - orange
            - bananna
        protein:
            - meat
            - eggs
        ...
    '''
    loader = AnsibleLoader(None, file_name=None)
    coerced_data = loader.construct_yaml_map(yaml)
    assert(coerced_data == {'food': ['pie', 'apple'], 'fruit': ['orange', 'bananna'], 'protein': ['meat', 'eggs']})



# Generated at 2022-06-13 07:42:51.524434
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, 'add_constructor')
    assert hasattr(AnsibleLoader, 'add_multi_constructor')

# Generated at 2022-06-13 07:42:53.576716
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Ensure class AnsibleLoader instantiation succeeds
    '''
    module = AnsibleLoader(stream='')
    assert module

# Generated at 2022-06-13 07:43:19.942032
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib

    stream = '''
---
a: 1
b: 2
c: 0x3
d:
- 1
- 2
- 0x3
e:
- foo
- bar
'''

    loader = AnsibleLoader(stream, vault_secrets=dict(vault_password='secret'))
    vault = VaultLib([('default', dict(vault_password='secret'))])

    vault.load(loader.get_single_data())

# Generated at 2022-06-13 07:43:23.362851
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # import pdb; pdb.set_trace()
    assert __name__ == '__main__'


if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:43:33.938705
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from yaml.reader import Reader
        from yaml.scanner import Scanner
        from yaml.parser import Parser
        from yaml.composer import Composer
    except ImportError:
        # Libyaml is not installed, so we can't test this
        pass
    else:
        from io import StringIO
        from ansible.module_utils.common.yaml import HAS_LIBYAML
        has_equivalents = [Reader, Scanner, Parser, Composer]

        if not HAS_LIBYAML:
            has_equivalents.append(Parser)

        stream = StringIO('---')
        loader = AnsibleLoader(stream)
        assert isinstance(loader, tuple(has_equivalents + [AnsibleConstructor, Resolver]))

# Generated at 2022-06-13 07:43:36.469334
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    assert isinstance(dataloader._loader, AnsibleLoader)

# Generated at 2022-06-13 07:43:44.351417
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import yaml

    class AnsibleLoaderWrapper(AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            AnsibleLoader.__init__(self, stream, file_name=file_name, vault_secrets=vault_secrets)
            self.seen_imports = []

        def check_data(self, data):
            if isinstance(data, list):
                for item in data:
                    self.check_data(item)
            elif isinstance(data, dict):
                #import pdb; pdb.set_trace()
                if '!include' in data and '!vault' not in data:
                    self.seen_imports.append(data['!include'])

# Generated at 2022-06-13 07:43:54.780440
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
    ---
    1: one
    2: two
    '''

    # Test creation
    loader = AnsibleLoader(stream)
    assert isinstance(loader, AnsibleLoader)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)
    if HAS_LIBYAML:
        assert isinstance(loader, Parser)
    else:
        assert isinstance(loader, Reader)
        assert isinstance(loader, Scanner)
        assert isinstance(loader, Parser)
        assert isinstance(loader, Composer)

    assert loader.load() == {'1': 'one', '2': 'two'}

# Generated at 2022-06-13 07:43:57.656383
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, None)
    empty_node = loader.construct_object(None, None)
    assert empty_node == "null"

# Generated at 2022-06-13 07:43:59.318438
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(file_name="foo", vault_secrets="yay")

# Generated at 2022-06-13 07:44:09.457478
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # test string, no vault secret
    raw_data = """
    ---
    one:
      two: three
    a: easy as
    b:
      c: 1
      d: 2
    """
    my_loader = AnsibleLoader(raw_data)
    my_list = my_loader.get_single_data()
    assert my_list.get('a') == 'easy as'
    assert my_list.get('b')['d'] == 2

    # test file, no vault secret
    my_loader = AnsibleLoader('/etc/hosts', file_name='/etc/hosts')
    my_list = my_loader.get_single_data()
    assert my_list.get('localhost') == ['localhost']

    # test string with vault secret

# Generated at 2022-06-13 07:44:14.475731
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '---\nhost: 1.2.3.4\nuri:\n - http://www.google.com\n'
    loader = AnsibleLoader(stream)
    result = loader.get_single_data()
    assert result == {'host': '1.2.3.4', 'uri': ['http://www.google.com']}

# Generated at 2022-06-13 07:44:59.954170
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    import tempfile
    import shutil
    import textwrap
    import json

    def setUp():
        # create a temp dir
        temp_dir = tempfile.mkdtemp(prefix='ansible-test-')
        temp_file = tempfile.mktemp(prefix='ansible-test-', dir=temp_dir)

        return temp_dir, temp_file


    def tearDown(temp_dir, temp_file):
        # clean up temp dir
        temp_dir = os.path.relpath(temp_dir)
        shutil.rmtree(temp_dir)

        return temp_dir, temp_file


    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    my_v

# Generated at 2022-06-13 07:45:05.033736
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, Reader)
    assert isinstance(loader, Scanner)
    assert isinstance(loader, Parser)
    assert isinstance(loader, Composer)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)

# Generated at 2022-06-13 07:45:06.128456
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:45:13.123853
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io

    # This is a simple YAML file that contains a basic list.
    data = '''
    - banana
    - apple
    - orange
    '''

    # Write the above string to a temporary file.
    f = io.StringIO()
    f.write(data)

    # Now, we can read the file with AnsibleLoader...
    f.seek(0)
    loader = AnsibleLoader(f)

    # The loader should provide a generator for each entry in the YAML file.
    for entry in loader:
        sys.stdout.write(entry)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:45:14.396865
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.constructor

    AnsibleLoader('test stream', 'test_file')

# Generated at 2022-06-13 07:45:22.003636
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from ansible.parsing.yaml.constructor import AnsibleConstructor  # pylint: disable=unused-variable
        from ansible.parsing.yaml.loader import AnsibleLoader  # pylint: disable=unused-variable
    except ImportError:
        print('Ansible codebase not found!')
        sys.exit(1)


if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:45:23.319074
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # TODO:
    print("AnsibleLoader")


# Generated at 2022-06-13 07:45:24.699066
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:45:26.329561
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = AnsibleLoader(None).get_single_data()
    assert data is None

# Generated at 2022-06-13 07:45:37.456921
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import __main__
    __main__.file_name = 'test_AnsibleLoader_file_name'
    __main__.yaml_vault = dict(
        vault_secrets='test_AnsibleLoader_vault_secrets',
        vault_password_file='test_AnsibleLoader_vault_password_file',
        vault_password='test_AnsibleLoader_vault_password',
        vault_identity='test_AnsibleLoader_vault_identity',
    )

    loader = AnsibleLoader(sys.stdin)
    assert loader.file_name == 'test_AnsibleLoader_file_name'
    assert loader.vault_secrets == 'test_AnsibleLoader_vault_secrets'

# Generated at 2022-06-13 07:47:01.505022
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Only if libyaml is available
    if HAS_LIBYAML:
        test_loader = AnsibleLoader(stream=None)

        # Assert object type
        assert isinstance(test_loader, Parser)
        assert isinstance(test_loader, AnsibleConstructor)
        assert isinstance(test_loader, Resolver)
    else:
        test_loader = AnsibleLoader(stream=None)

        # Assert object type
        assert isinstance(test_loader, Reader)
        assert isinstance(test_loader, Scanner)
        assert isinstance(test_loader, Parser)
        assert isinstance(test_loader, Composer)
        assert isinstance(test_loader, AnsibleConstructor)
        assert isinstance(test_loader, Resolver)

# Generated at 2022-06-13 07:47:06.716595
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.objects
    stream = "---\n- 1\n- 2\n- 3\n"
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert isinstance(data, ansible.parsing.yaml.objects.AnsibleSequence)
    assert len(data) == 3
    assert data[0] == 1
    assert data[1] == 2
    assert data[2] == 3

# Generated at 2022-06-13 07:47:07.888595
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # TODO: Actually test this
    AnsibleLoader(None)

# Generated at 2022-06-13 07:47:11.062126
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.objects

    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)
    assert isinstance(loader, ansible.parsing.yaml.objects.AnsibleBaseYAMLObject)

# Generated at 2022-06-13 07:47:12.424332
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader,'__init__')

# Generated at 2022-06-13 07:47:19.303394
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=redefined-outer-name
    data = """
    - hosts: localhost
      pre_tasks:
        - name: write into file
          copy:
            dest: /tmp/foo
            content: testing

    - hosts: localhost
      tasks:
      - name: read from file
        copy:
          src: /tmp/foo
          dest: /tmp/bar
          remote_src: yes

    - hosts: localhost
      tasks:
      - include: other.yml
    """

    loader = AnsibleLoader(data, file_name='test_file.yml')
    ansible_data = loader.get_single_data()
    assert 'pre_tasks' in ansible_data[0]
    assert 'hosts' in ansible_data[0]

# Generated at 2022-06-13 07:47:22.366381
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    module = AnsibleLoader("---")
    assert not hasattr(module,"construct_yaml_str")
    assert hasattr(module,"construct_undefined")
    assert hasattr(module,"construct_mapping")

# Generated at 2022-06-13 07:47:28.785651
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    from collections import Mapping
    from io import StringIO
    try:
        from yaml import FullLoader
    except ImportError:
        FullLoader = None

    simple_yaml = '''
    - 1
    - 2
    - 3
    '''

    data = list(AnsibleLoader(StringIO(simple_yaml), vault_secrets=None))
    assert len(data) == 3
    assert data == [1, 2, 3]

    dict_yaml = '''
    a: 1
    b: 2
    c: 3
    '''
    data = Mapping(AnsibleLoader(StringIO(dict_yaml), vault_secrets=None))
    assert len(data) == 3
    assert data['a'] == 1
    assert data['b'] == 2
    assert data

# Generated at 2022-06-13 07:47:34.519760
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from StringIO import StringIO
    stream = StringIO(u"---\n"
        " - host: example.org\n"
        "   connection: local\n"
        "   tasks:\n"
        "    - debug:\n"
        "        msg: System {{ inventory_hostname }} has uuid {{ ansible_product_uuid }}\n")

    assert(AnsibleLoader(stream) is not None)

# Generated at 2022-06-13 07:47:35.878542
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader
