

# Generated at 2022-06-13 07:38:41.338688
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

# Generated at 2022-06-13 07:38:43.762951
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    assert(issubclass(AnsibleLoader, AnsibleConstructor))
    assert(issubclass(AnsibleLoader, Resolver))
    assert(issubclass(AnsibleLoader, Parser))

# Generated at 2022-06-13 07:38:50.545884
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    if __name__ == '__main__':
        sys.path.append(os.path.dirname(__file__) + "/../")
        from ansible.parsing.yaml.constructor import AnsibleConstructor
        from ansible.parsing.mod_args import ModuleArgsParser
        from ansible.parsing.dataloader import DataLoader
        from ansible.parsing.yaml.objects import AnsibleUnicode
        from ansible.parsing.yaml.objects import AnsibleSequence
        from ansible.parsing.yaml.objects import AnsibleMapping
        from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
        from ansible.parsing.yaml.objects import AnsibleVaultEncrypted

# Generated at 2022-06-13 07:38:56.715871
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    import yaml

    class Loader(AnsibleConstructor, Resolver):

        # Unit test for method scan_once
        def test_scan_once(self):
            INPUT = "text:\n- item1\n- item2\n"
            stream = yaml.Stream(INPUT)
            stream.check_plain()

        # Unit test for method set_state
        def test_set_state(self):
            self.anchors = dict()
            self.tagged_values = dict()
            self.file_name = ''
            self.cur_value = None
            self.cur_key = None
            self.cur_val_is_map = False
            self.state_stack = list()

        # Unit test for method process

# Generated at 2022-06-13 07:39:08.594427
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultEditor
    import filecmp
    import os
    import tempfile
    # create an input file in current dir
    (tmp_fd, tmp_file) = tempfile.mkstemp(prefix='ansible-test-')
    with os.fdopen(tmp_fd, 'w') as tmp:
        tmp.write(u"vault_password_file: secrets.txt\n")
        tmp.write(u"foo: !vault |\n")
        tmp.write(u"          $ANSIBLE_VAULT;1.1;AES256\n")

# Generated at 2022-06-13 07:39:22.402649
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Initialize a loader using a file
    loader = AnsibleLoader(None, '/my/template.j2')

    assert loader.file_name == "/my/template.j2"
    assert loader.construct_python_list == AnsibleConstructor.construct_python_list
    assert loader.construct_python_unicode == AnsibleConstructor.construct_python_unicode
    assert loader.construct_python_str == AnsibleConstructor.construct_python_str
    assert loader.construct_python_dict == AnsibleConstructor.construct_python_dict
    assert loader.add_implicit_resolver == Resolver.add_implicit_resolver

    # Initialize a loader using a string
    loader = AnsibleLoader(None, file_name='<string>')

    assert loader.file_name == "<string>"
    assert loader.construct

# Generated at 2022-06-13 07:39:27.985715
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from sys import stdin
    from io import StringIO

    l = AnsibleLoader(StringIO(''))
    assert isinstance(l, (Scanner, Reader))
    assert isinstance(l, (Parser, Composer))
    assert isinstance(l, AnsibleConstructor)
    assert isinstance(l, Resolver)

    l = AnsibleLoader(stdin)
    assert isinstance(l, (Scanner, Reader))
    assert isinstance(l, (Parser, Composer))
    assert isinstance(l, AnsibleConstructor)
    assert isinstance(l, Resolver)

# Generated at 2022-06-13 07:39:37.496073
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test __init__ for class AnsibleLoader
    stream = Parser(stream)
    file_name = 'test.yaml'
    vault_secrets = dict()

    ansible_loader = AnsibleLoader(stream, file_name, vault_secrets)

    assert ansible_loader._reader == stream
    assert ansible_loader._scanner == stream
    assert ansible_loader._parser == stream
    assert ansible_loader._composer == stream
    assert ansible_loader._constructor == stream
    assert ansible_loader._resolver == stream

# Generated at 2022-06-13 07:39:47.380625
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import yaml

    try:
        file_name = os.path.expanduser(os.path.join('~', 'test.yaml'))
        with open(file_name, 'w') as yaml_file:
            yaml_file.write('---\n')
            yaml_file.write('hosts: all\n')
            yaml_file.write('user: root\n')
            yaml_file.write('tasks:\n')
            yaml_file.write('  - shell: echo "ok"\n')
    except IOError as e:
        print(e)
        sys.exit(1)


# Generated at 2022-06-13 07:39:58.422475
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    import tempfile

    curdir = os.path.dirname(__file__)
    datadir = os.path.join(curdir, "data")
    hostvarsfile = os.path.join(datadir, "host_vars_file.yaml")
    stream = open(hostvarsfile, 'r')
    yamlloader = AnsibleLoader(stream)
    result = yamlloader.get_single_data()
    assert result['a'] == 'foo'
    stream.close()

    # test load of vault_yaml_file
    filename = tempfile.NamedTemporaryFile(delete=False).name
    os.chmod(filename, 0o700)

# Generated at 2022-06-13 07:40:00.917073
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader("")

# Generated at 2022-06-13 07:40:11.839004
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.errors import AnsibleError, AnsibleAssertionError
    from ansible.utils.vars import load_extra_vars, load_options_vars, load_options_vars_defaults
    from ansible.utils.vars import merge_hash
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_hash
    from ansible.utils.vars import jsonify
    from ansible.utils.unicode import to_unicode, from_unicode
    from ansible.vars.clean import module_response

# Generated at 2022-06-13 07:40:12.909424
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader(None)

# Generated at 2022-06-13 07:40:14.492913
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Parser)

# Generated at 2022-06-13 07:40:20.192896
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create a new AnsibleLoader object
    result = AnsibleLoader(None)

    # Create a new AnsibleLoader object with vault_secrets
    vault_secrets = {'ansible_vault_password': 'password'}
    result = AnsibleLoader(None, vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:40:20.802967
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:40:22.309897
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert(loader is not None)

# Generated at 2022-06-13 07:40:24.883686
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    ret = AnsibleLoader(None)

# Generated at 2022-06-13 07:40:31.647886
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # import yaml
    loader = AnsibleLoader(None)
    assert loader.yaml_constructors == {'!include': loader.construct_include}
    loader.vault_secrets = ['foo']
    assert loader.vault_secrets == ['foo']
    assert not loader.file_name
    loader = AnsibleLoader(None, 'hosts')
    assert loader.file_name == 'hosts'

# Generated at 2022-06-13 07:40:42.098829
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.utils.vars import combine_vars

    # set up the basics for our test
    loader = AnsibleLoader(None, 'non-existent-file')
    loader.construct_mapping = lambda node: combine_vars(loader.construct_yaml_map(node), dict())

    # test with a scalar value
    data = loader.get_single_data('42')
    assert data == 42

    # test with existing file name
    data = loader.get_single_data('yaml_loader_tests.yml')
    assert data == dict(a='b')

    # test with non-existent file name
    data = loader.get_single_data('yaml_loader_tests_non_existent.yml')
    assert data == dict(a=dict(b='c'))

    # test with multi

# Generated at 2022-06-13 07:40:53.195785
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader
    from yaml.resolver import Resolver
    from ansible.module_utils.common.yaml import Parser

    with open('t.yml', 'r') as f:
        AnsibleLoader(f)


if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:05.751012
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import shutil
    from six import StringIO
    from ansible.parsing.yaml.objects import AnsibleMapping
    import yaml

    yaml_file = StringIO("""
---
- name: test
  when: "{{test}}"
""")
    _old_stdin = sys.stdin
    sys.stdin = yaml_file
    _loader = yaml.Loader
    _dumper = yaml.Dumper
    yaml.Loader = AnsibleLoader
    yaml.Dumper = AnsibleLoader
    try:
        data = yaml.load(yaml_file)
        assert isinstance(data[0], AnsibleMapping)
        assert data[0]['name'] == 'test'
    finally:
        yaml.Loader = _loader
       

# Generated at 2022-06-13 07:41:09.402765
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    global HAS_LIBYAML
    HAS_LIBYAML = True
    AnsibleLoader(None)

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:18.020161
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
---
a:
  b:
    - 1
    - 2
    - {a: 1, b: 2}
    - {a: 3, b: 4}
'''
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert 3 == len(data['a']['b'])
    assert data['a']['b'][2]['a'] == 1

# Generated at 2022-06-13 07:41:21.492726
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
     assert hasattr(AnsibleLoader, 'add_constructor')

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:29.968643
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_string = """
---
- name: '{{role_name}}'
  shell: /bin/false
    """
    file_name = 'file_name_to_be_provided_in_class_AnsibleConstructor.yml'
    vault_secrets = ['/path/to/encrypted_file_name_to_be_provided_in_class_AnsibleConstructor.yml']
    from io import StringIO
    loader = AnsibleLoader(StringIO(yaml_string),
                           file_name=file_name,
                           vault_secrets=vault_secrets)
    assert loader.file_name == file_name
    assert loader.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:41:31.910474
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO

    loader = AnsibleLoader(StringIO.StringIO('['))
    loader.get_single_data()

# Generated at 2022-06-13 07:41:33.783472
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert HAS_LIBYAML == True, 'test_AnsibleLoader needs libyaml installed.'

# Generated at 2022-06-13 07:41:42.290751
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Exercise a few ways of calling the class
    loader = AnsibleLoader(None)
    assert loader

    import StringIO
    stream = StringIO.StringIO()
    loader = AnsibleLoader(stream)
    assert loader

    # A simple test of the construct_yaml_map method
    class Test:
        def __init__(self):
            self.data = {'a': 'b'}

    yaml_data = """
    foo:
      bar: 1
      bam: [ 2, 3 ]
      baz:
          - one
          - two
          - three
    """

    loader = AnsibleLoader(stream)
    loader.data = Test()
    data = loader.get_single_data()
    assert data == loader.data.data

    # Exercise the load method

# Generated at 2022-06-13 07:41:52.238069
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    loader = AnsibleLoader(None)

    data = """
    foo:
        bar: baz
    """
    ans_obj = loader.get_single_data(data)
    assert isinstance(ans_obj, AnsibleMapping)
    assert ans_obj['foo']['bar'] == "baz"

    data = """
    - foo: bar
      bam: [baz, zam]
    - pam: spam
    """
    ans_obj = loader.get_single_data(data)
    assert isinstance(ans_obj, AnsibleSequence)
    assert ans_obj[0] == {"foo": "bar", "bam": ["baz", "zam"]}
    assert ans_obj

# Generated at 2022-06-13 07:42:05.431475
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''Unit test for constructor of class AnsibleLoader'''
    stream = '{}'
    file_name = 'hosts'
    vault_secrets = {}
    ansible_loader = AnsibleLoader(stream, file_name, vault_secrets)
    # Check if the attributes are set after creation
    assert ansible_loader.stream == stream
    assert ansible_loader.file_name == file_name
    assert ansible_loader.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:42:06.650758
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    loader = AnsibleLoader(dict)
    assert loader.get_single_data() == dict()

# Generated at 2022-06-13 07:42:12.284065
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream='')
    assert isinstance(loader, AnsibleLoader)
    assert isinstance(loader, Reader)
    assert isinstance(loader, Scanner)
    assert isinstance(loader, Parser)
    assert isinstance(loader, Composer)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)


# vim: set expandtab shiftwidth=4 softtabstop=4 ft=python :

# Generated at 2022-06-13 07:42:19.511784
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    string_to_load = '''
    - !YAML_OBJECT_0
    '''

    string_to_dump = '''
    - !YAML_OBJECT_0 {}
    '''

    class YAML_OBJECT_0():
        pass

    class YAML_OBJECT_1(YAML_OBJECT_0):
        pass

    class YAML_OBJECT_2(YAML_OBJECT_0):
        pass

    class YAML_OBJECT_3(YAML_OBJECT_0):
        pass


# Generated at 2022-06-13 07:42:24.082809
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = 'foo'
    file_name = 'bar'
    vault_secrets = {}
    the_loader = AnsibleLoader(stream, file_name, vault_secrets)
    assert the_loader != None
    assert the_loader.stream == stream
    assert the_loader.file_name == file_name
    assert the_loader.vault_secrets == vault_secrets


# Generated at 2022-06-13 07:42:27.503005
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)

# Generated at 2022-06-13 07:42:36.365053
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # test if AnsibleUnsafeText is correctly constructed
    data = AnsibleLoader("{ansible_unsafe} foo").get_single_data()
    assert isinstance(data, AnsibleUnsafeText)
    assert data == "foo"

    data = AnsibleLoader("!!unsafe foo").get_single_data()
    assert isinstance(data, AnsibleUnsafeText)
    assert data == "foo"

    # test if AnsibleMapping is correctly constructed
    data = AnsibleLoader("{foo: bar}").get_single_data()
    assert isinstance(data, AnsibleMapping)
    assert data['foo'] == 'bar'

    # test if the resolver

# Generated at 2022-06-13 07:42:44.240856
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test with libyaml
    if HAS_LIBYAML:
        raw = """
---
- hosts: localhost
  gather_facts: no
  connection: local
- hosts: localhost
  connection: local
  tasks:
    - set_fact:
        foo: bar
...
"""
        stream = raw.encode()
        loader = AnsibleLoader(stream)
        data = loader.get_single_data()
        assert data[0]['hosts'] == 'localhost'

    # Test without libyaml
    else:
        raw = """
---
- hosts: localhost
  gather_facts: no
  connection: local
- hosts: localhost
  connection: local
  tasks:
    - set_fact:
        foo: bar
...
"""
        stream = raw.encode()
        loader

# Generated at 2022-06-13 07:42:45.161515
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True

# Generated at 2022-06-13 07:42:55.231492
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    loader = AnsibleLoader(None)
    text = '$VAULT;1.1;AES256\n34464143646232333463386434363564313038643938633362316338383766363435356334336566\n31323538393032323465656239343663643463383964663231666433626263343237616566316130\n38616234326334623331666432666565363534386533326262653366373965383038353939643433\n396665643732323162343066\n'

   

# Generated at 2022-06-13 07:43:25.214422
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Don't test for HAS_LIBYAML, ugh.
    # if not HAS_LIBYAML:
    #     return

    import sys

    # Make sure basic AnsibleLoader works
    stream = '''\
---
a: 1
'''
    debug = False
    output = '''\
<ansible_loader.AnsibleLoader object at 0x%x>
  tag: a
    - 1
...
''' % id(AnsibleLoader(stream))
    if debug:
        print('Input stream:', file=sys.stderr)
        print(stream, file=sys.stderr)
        print('Output:', file=sys.stderr)
        print(repr(AnsibleLoader(stream)), file=sys.stderr)

# Generated at 2022-06-13 07:43:29.825476
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO
    fake_yaml = StringIO("{'abc':123}")

    loader = AnsibleLoader(fake_yaml)
    parsed_yaml = loader.get_single_data()

    assert parsed_yaml == {'abc': 123}

# Generated at 2022-06-13 07:43:33.492243
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.loader as test_loader
    import sys
    reload(test_loader)
    l = test_loader.AnsibleLoader(sys.stdin)
    assert isinstance(l, test_loader.AnsibleLoader)

# Generated at 2022-06-13 07:43:42.066980
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    file_name = 'test_data.yaml'

# Generated at 2022-06-13 07:43:48.147103
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, 'construct_yaml_map')
    assert hasattr(AnsibleLoader, 'construct_mapping')
    assert hasattr(AnsibleLoader, 'construct_scalar')
    assert hasattr(AnsibleLoader, 'construct_yaml_bool')

# Generated at 2022-06-13 07:43:57.998921
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.errors import AnsibleParserError
    import ansible.constants as C
    import os

    yaml_data = """
    - hosts: all
      gather_facts: no

      tasks:
        - debug:
            msg: '{{ ansible_system }} on {{ inventory_hostname }}'
      vars:
        testvar: success
    """

    # change ANSIBLE_LIBRARY path to load our mocked module 'test_module'
    path = os.path.join(os.getcwd(), 'test/units/module_utils/test_module.py')
    os.environ["ANSIBLE_LIBRARY"] = os.path.dirname(path)

    # initialize AnsibleLoader and load yaml data
   

# Generated at 2022-06-13 07:44:08.368770
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    company = """
    name: Company
    employees:
      - { name: Michael DeHaan, position: founder }
      - { name: John Anderson, position: CEO }
      - { name: Greg DeKoenigsberg, position: VP Community }
    """
    data = AnsibleLoader(None).construct_yaml(company)
    assert isinstance(data, dict)
    assert data['name'] == 'Company'
    assert isinstance(data['employees'], list)
    assert len(data['employees']) == 3
    assert data['employees'][0]['name'] == 'Michael DeHaan'
    assert data['employees'][1]['position'] == 'CEO'
    assert data['employees'][2]['name'] == 'Greg DeKoenigsberg'

# Generated at 2022-06-13 07:44:17.767511
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:44:24.603320
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible import constants
    from ansible.parsing.vault import VaultSecret

    def test_with_non_string_vault_secrets(non_string_vault_secrets):
        stream = ['---', 'foo: bar', '...', '']
        constructor = AnsibleLoader(stream, vault_secrets=non_string_vault_secrets)
        vault_secret = constructor.vault_secrets
        assert vault_secret is None or \
            (isinstance(vault_secret, VaultSecret) and \
             (vault_secret.is_encrypted() or vault_secret.is_binary()))
    test_with_non_string_vault_secrets(constants.DEFAULT_VAULT_ID)
    test_with_non_string_vault_secrets('')

# Generated at 2022-06-13 07:44:26.732735
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = "!!python/object/apply:os.system\n- ls"
    try:
        loader = AnsibleLoader(stream)
        loader.get_single_data()
    except Exception:
        pass
    else:
        assert False, 'AnsibleLoader raises exception'

# Generated at 2022-06-13 07:45:09.716916
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class TestAnsibleLoader(AnsibleLoader):
        def compose_node(self, parent, index):
            # this is super ugly but its a shortcut to test the compose_node() method
            # which would otherwise be very hard to do without loading data
            self.compose_document(None)
            node = self.get_node()
            return node

    loader = TestAnsibleLoader(None)
    assert loader
    assert loader.dumper
    assert loader.constructor
    assert loader.constructor._loader

    # 'loader' doesn't have a stream of yaml data to parse but that's not needed
    # to test the compose_node() method.  This is a valid test of AnsibleLoader

    # test a very simple list
    data = loader.compose_node(None, None)
    assert type(data) is list

# Generated at 2022-06-13 07:45:17.420719
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import pprint
    import yaml

    yaml_str = u"""
        - hosts: localhost
          tasks:
            - debug:
                msg: Hello
                verbosity: 4
    """
    stream = io.StringIO(yaml_str)
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert(data == yaml.load(stream))

# Generated at 2022-06-13 07:45:21.581503
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # import module snippets
    from ansible.utils.unicode import to_bytes

    # Setup loader for testing
    assert HAS_LIBYAML, "This test needs LibYAML"
    test_file = 'test/loader_test.yml'
    test_obj = "!my_test_obj"
    test_stream = open(test_file, 'rb')
    test_loader = AnsibleLoader(test_stream)

    # Read yaml_loader
    test_loader.dispose()
    test_loader.check_node()
    test_loader.get_token()
    test_loader.compose_document()
    test_loader.compose_node(None, None)
    test_loader.compose_mapping_node(None, None)

# Generated at 2022-06-13 07:45:28.837442
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Unit tests for constructor of class AnsibleLoader
    """
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    secret_text = '$ANSIBLE_VAULT;1.1;AES256\n35623261623531393139613361323937346564383734643765666465336630343835623263613036\n33613331336562643537376539316566363530316439363364626436356262646236313231333236\n326439396162613031346635\n'
    loader = AnsibleLoader(secret_text)
    vault = VaultLib(['vault.key'])
    vault_

# Generated at 2022-06-13 07:45:32.222054
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Run a quick check to make sure our ansible loader constructed
    properly
    """
    l = AnsibleLoader('')

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:45:43.253708
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    yaml_str = '''---
- hosts: localhost
  connection: local
  remote_user: root
  gather_facts: no
  tasks:
    - bzr:
        repo: lp:~ansible-test/ansible/test-module-runner
        dest: /tmp/test-module-runner
    - file:
        dest: /tmp/test-module-runner/test-module
        state: link
        src: /usr/local/bin/ansible-test-module
    - command: /tmp/test-module-runner/test-module
      register: test_module_result
    - fail: msg="test-module failed"
      when: test_module_result.rc > 0
'''


# Generated at 2022-06-13 07:45:49.396549
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test AnsibleLoader with a yaml file
    from ansible.module_utils.common.yaml import AnsibleLoader
    loader = AnsibleLoader(open('../../../../examples/ansible.cfg', 'r'))
    loader.get_single_data()

    # Test AnsibleLoader with a string
    string1 = """
    ---
    - hosts: localhost
      user: root
      tasks:
        - name: Test AnsibleLoader with a string
          debug:
            msg: Hello world!
    """
    loader = AnsibleLoader(string1)
    loader.get_single_data()

# Generated at 2022-06-13 07:45:53.516849
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.common.yaml import HAS_LIBYAML
    if HAS_LIBYAML:
        for cls in [AnsibleLoader]:
            x = cls()
            assert x is not None

# Generated at 2022-06-13 07:46:00.828188
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():   # pylint: disable=too-many-locals,too-many-return-statements,too-many-branches
    from ansible.parsing.yaml.constructor import AnsibleConstructorError

    class TestParser(AnsibleLoader):
        def get_single_data(self):
            self.get_event()
            return self.compose_document()

    import sys
    import os
    import json
    import shutil

    basedir = os.path.dirname(__file__)
    datadir = os.path.join(basedir, 'yaml_data')
    # noinspection PyShadowingNames
    def test_data(filename):
        return os.path.join(datadir, filename)


# Generated at 2022-06-13 07:46:08.333592
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import StringIO

    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__

    output = '\n'.join([
        "---",
        "foo: '{{bar}}'",
        "baz: [u'Boom', u'Bam', u'Bam', u'Ka-pow']",
        "bar: Bat",
        "vars:",
        "  bat: '{{bar}}'",
        "  baz: '{{bat}}'",
        "vault:",
        "  var1: \"{{ vault_var1 }}\"",
        "  var2: \"{{ vault_var2 }}\"",
    ])
    output += "\n"

# Generated at 2022-06-13 07:47:24.768231
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from io import BytesIO
    import os

    # Test default vault id

# Generated at 2022-06-13 07:47:26.008501
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert not HAS_LIBYAML, "test_AnsibleLoader() does not need to run with LibYAML"

# Generated at 2022-06-13 07:47:28.031128
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:30.477347
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, file_name='file_name')
    assert loader.file_name == 'file_name'

# Generated at 2022-06-13 07:47:31.354327
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(None)

# Generated at 2022-06-13 07:47:36.568949
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    AnsibleLoader:
        - AnsibleConstructor
        - Resolver
    '''

    class MyAnsibleLoader(AnsibleLoader):
        pass

    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:47:47.060484
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    loader = DataLoader()

    # we don't use the play datastructure in the parser and this allows us to
    # define test strings for the PlaybookInclude and HostPatternInclude
    # syntax and verify the results of parsing them as if they were tasks.
    def _construct_yaml_obj(self, node):
        # Override the default string handling function
        # to always return class str (as opposed to class unicode in PyYAML).
        return self.construct_scalar(node)


# Generated at 2022-06-13 07:47:52.192283
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("")
    assert hasattr(loader, "construct_yaml_map"), "construct_yaml_map not found"
    assert hasattr(loader, "construct_mapping"), "construct_mapping not found"
    assert hasattr(loader, "get_single_data"), "get_single_data not found"

# Generated at 2022-06-13 07:48:01.905417
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    correct_date = '2014-04-26'
    correct_time = '14:14:14+02:00'

    # Test valid ISO 8601 in YAML file
    yaml_str = "date: %s\ntime: %s" % (correct_date, correct_time)
    data = AnsibleLoader(yaml_str).get_single_data()

    assert data['date'] == correct_date
    assert data['time'] == correct_time

    # Test invalid strings in YAML file
    yaml_str = "date: %s\nbad1: 2014-04-26 14:14:14\nbad2: 14:14:14+02:00" % correct_date
    data = AnsibleLoader(yaml_str).get_single_data()


# Generated at 2022-06-13 07:48:12.598110
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
---
- hosts: localhost
  connection: local
  vars:
    var1: val1
    var2: val2
  tasks:
  - shell: /bin/false
    register: result1
    when: ansible_os_family != "RedHat"
  - set_fact:
      result2: "ansible_os_family != RedHat"
  - shell: /bin/false
    register: result3
    when: result2
  - shell: /bin/echo {{ hostvars[inventory_hostname].result1.rc }}
    register: result4
    when: result2
  - if result4:
      debug: msg={{ hostvars.result2.rc }}
    else:
      debug: msg="unexpected result"
...
     '''
    loader = Ans