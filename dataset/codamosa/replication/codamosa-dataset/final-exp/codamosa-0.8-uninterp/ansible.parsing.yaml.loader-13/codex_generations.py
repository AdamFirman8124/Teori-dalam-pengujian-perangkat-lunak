

# Generated at 2022-06-13 07:38:36.661404
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # Loader for an encrypted variable

# Generated at 2022-06-13 07:38:43.609266
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    context = {}
    yaml_list = [
        '---',
        '- hosts: all',
        '  vars:',
        '    foo: 1',
        '  tasks:',
        '  - debug:',
        '      msg: hello world',
    ]
    data = '\n'.join(yaml_list)
    loader = AnsibleLoader(data)
    loader.construct_mapping(context)
    assert context == {'hosts': 'all',
                       'vars': {'foo': 1},
                       'tasks': [{'debug': {'msg': 'hello world'}}]}

# Generated at 2022-06-13 07:38:52.643767
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Constructor test
    '''
    file = "../../lib/ansible/parsing/yaml/constructor.py"
    text = """
    ---
    - hosts: all
      vars:
        version: 1.7
        mode: '0644'
        owner: root
        group: wheel
      tasks:
        - name: create the foobar configuration file
          template: src=templates/foobar.j2 dest={{ files }}/foobar.conf owner={{ owner }} group={{ group }} mode={{ mode }}
          with_fileglob:
            - ../files/*
    """
    #stream = open(file, "r")
    vault_secrets = {'ansible_vault_password': ['yamjv2']}

# Generated at 2022-06-13 07:38:58.028881
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    # read sample test data
    test_file = os.path.join(os.path.dirname(__file__), 'data', 'simple_variable.yml')
    with open(test_file, 'r') as f:
        test_data = f.read()

    # create temp file, write test data to it, and read it with AnsibleLoader
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.yml')
    f.write(test_data)
    f.flush()
    with open(f.name, 'r') as yf:
        al = AnsibleLoader

# Generated at 2022-06-13 07:39:05.650843
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # AnsibleLoader is a pure abstract class and does not implement
    # __init__ functions, thus it cannot be instantiated for testing.
    # nsibleLoader is a subclass of Parser which has __init__ function.
    # Thus it is used here for testing purposes

    ansible_loader_parser = Parser()
    assert hasattr(ansible_loader_parser, 'get_event')

    ansible_loader_parser.dispose()
    assert True

# Generated at 2022-06-13 07:39:07.742563
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader
    assert AnsibleLoader(None)

# Generated at 2022-06-13 07:39:21.526343
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    loader = AnsibleLoader("---\nfoo: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          33613631346135613261313837383064396636623862393464333130613333396333616234356461\n          61386334320a64396566653839336434306536306462393835383635336230653762613366303438\n          62376339640a36313163623266303536343631613230303535623531653164306639633538316462\n          3035333736\n")
    vault_secrets = dict(vault_password='foo')

# Generated at 2022-06-13 07:39:22.086996
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:29.292520
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common.yaml import HAS_LIBYAML
    from ansible.vars.manager import VariableManager
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'hacking'))
    from test_yaml_load import _TestYamlLoad

    class _TestAnsibleLoader(_TestYamlLoad):
        """
        This class inherites from _TestYamlLoad, which is a test base class
        for yaml/__init__.py.
        In order to use AnsibleLoader in _TestYamlLoad,
        _load_yaml function was overridden in this child class.
        """

# Generated at 2022-06-13 07:39:41.527571
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, \
        AnsibleVaultEncryptedString

    loader = AnsibleLoader(None, file_name='test_file')
    assert loader.file_name == 'test_file'
    loader = AnsibleLoader(None)
    assert loader.file_name is None
    loader = AnsibleLoader(None, vault_secrets=['secret'])
    assert loader.vault_secrets == ['secret']
    # test _construct_yaml_str
    assert loader._construct_yaml_str('hello') == 'hello'
    assert loader._construct_yaml_str(123) == '123'
    assert loader._construct_yaml_str('{{hello}}') == '{{hello}}'

# Generated at 2022-06-13 07:39:49.035905
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    d = yaml.load("""
        ---
        - &common one
        - &common two
        - &common three
        - &common four
        - *common
        - *common
        - *common
        - *common
        - *common
        - *common
        - *common
        - *common
        - *common
    """, Loader=AnsibleLoader)
    assert d == [['one', 'two', 'three', 'four']] * 10

# Generated at 2022-06-13 07:39:50.413139
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' unit test for class AnsibleLoader '''
    loader = AnsibleLoader("")

# Generated at 2022-06-13 07:40:01.531247
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import json

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader

    for data in ['', '[]', '{}', 'foo', '1', 1, 1.0]:
        s = json.dumps(data)
        l = AnsibleLoader(s)
        assert data == l.get_single_data()
        assert l.file_name is None, l.file_name

    for data in ['', '{}', '[]']:
        s = json.dumps(data)
        l = AnsibleUnicode(s)
       

# Generated at 2022-06-13 07:40:03.714505
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '---\nkey1: 1\nkey2: 2'
    loader = AnsibleLoader(stream)
    loader.get_single_data()

# Generated at 2022-06-13 07:40:07.208600
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class TestAnsibleLoader(AnsibleLoader):
        pass

    loader = TestAnsibleLoader('foo: 1')
    data = loader.get_single_data()
    assert data == {'foo': 1}

# Generated at 2022-06-13 07:40:10.611148
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    sett = { 'file_name': 'test', 'vault_secrets': None }
    a = AnsibleLoader(stream='', **sett)
    assert a.file_name == sett['file_name']
    assert a.vault_secrets == sett['vault_secrets']

# Generated at 2022-06-13 07:40:12.210029
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:40:24.097951
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    test_data = """\
a: 1
b:
  - 2
  - 3
"""

    stream = open('test', 'rb')
    stream.write(test_data)
    stream.seek(0)

    loader = AnsibleLoader(stream)
    data = loader.get_single_data()

    assert len(data) == 2
    assert isinstance(data, AnsibleMapping)

    assert data['a'] == 1
    assert isinstance(data['a'], int)

    assert len(data['b']) == 2
    assert isinstance(data['b'], AnsibleSequence)

    assert data['b'][0]

# Generated at 2022-06-13 07:40:24.728904
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:40:30.172410
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class_inst = AnsibleLoader(stream='', file_name='', vault_secrets='')
    assert isinstance(class_inst, Resolver)
    assert isinstance(class_inst, AnsibleConstructor)
    if HAS_LIBYAML:
        assert isinstance(class_inst, Parser)
    else:
        assert isinstance(class_inst, Reader)
        assert isinstance(class_inst, Scanner)
        assert isinstance(class_inst, Parser)
        assert isinstance(class_inst, Composer)

# Generated at 2022-06-13 07:40:35.179543
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:40:40.695838
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''---
- name: test
  foo: bar
'''
    ansibleloader = AnsibleLoader(yaml_str)
    ansibleloader.get_data()
    try:
        ansibleloader.check_data()
    except:
        # FIXME: convert this to an actual unit test
        assert False, 'an actual unit test would have been run here'


# Generated at 2022-06-13 07:40:42.409946
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    if HAS_LIBYAML:
        assert AnsibleLoader
    else:
        assert AnsibleLoader

# Generated at 2022-06-13 07:40:48.509769
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml_str = '''\
    - name: test
      yaml: test
    '''
    data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert data[0]['name'] == 'test'

# Generated at 2022-06-13 07:40:58.452344
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    import ansible.parsing.yaml.loader
    file_name = os.path.join(os.path.dirname(__file__), "test_datetime.yml")
    fh = open(file_name)
    file_name = os.path.abspath(file_name)
    contents = fh.read()
    fh.close()
    data = ansible.parsing.yaml.loader.load(contents, file_name=file_name)
    assert isinstance(data, AnsibleMapping)

# Generated at 2022-06-13 07:41:01.627083
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    obj = AnsibleLoader(None)
    assert obj is not None

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:15.656236
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import StringIO
    s = StringIO.StringIO("""
        - hosts: localhost
          tasks:
            - yum:
                name: ntpdate
                state: latest
    """)
    AnsibleLoader(s)
    s = StringIO.StringIO("""
        - hosts: localhost
          tasks:
            - yum:
                name: ntpdate
                state: latest
    """)
    AnsibleLoader(s, vault_secrets={1: 44})
    s = StringIO.StringIO("""
        - hosts: localhost
          tasks:
            - yum:
                name: ntpdate
                state: latest
    """)
    AnsibleLoader(s, file_name='ansible.yml')

# Generated at 2022-06-13 07:41:17.545802
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:41:28.999661
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    loader = DataLoader()
    vault_pass = '$ANSIBLE_VAULT;1.1;AES256\n61626364656631323334353637383930393031323334353637383930393031323334353637383930393031323334353637383930393031323334353637383930393061\n'
    loader.set_vault_secrets(['vault_pass'], [vault_pass])

# Generated at 2022-06-13 07:41:35.491821
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
    key1: value1
    key2: value2

    key3:
      key4: value4
      key5: value5

    key6:
      key7: value7
      key8:
        key9: value9
        key10: value10
    """
    loader = AnsibleLoader(data)
    root = loader.get_single_data()

    assert root.get('key1') == 'value1'
    assert root.get('key2') == 'value2'
    assert root.get('key3').get('key4') == 'value4'
    assert root.get('key3').get('key5') == 'value5'
    assert root.get('key6').get('key7') == 'value7'
    assert root.get('key6').get('key8').get

# Generated at 2022-06-13 07:41:53.082445
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os

    # We need a file so AnsibleLoader can read the server_name
    with open(os.path.join(sys.path[0], "loader_data/hosts_file.yaml"), 'rt') as f:
        data = f.read()

    # Test file reading from disk
    loader = AnsibleLoader(data)
    loader.get_single_data()
    assert(loader.server_name == 'host1')

    # Test file reading from memory
    loader2 = AnsibleLoader(data)
    loader2.get_single_data()
    assert(loader2.server_name == 'host1')

    # Test data reading from memory
    d = yaml.dump(data)
    loader3 = AnsibleLoader(d)
    loader3.get_single_data()

# Generated at 2022-06-13 07:42:03.073850
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)
    ansible_loader = AnsibleLoader(file_name='test.yml', vault_secrets=[VaultLib('test')])
    assert isinstance(ansible_loader, AnsibleLoader)
    ansible_loader.dispose()

    ansible_loader = AnsibleLoader(vault_secrets=[VaultLib('test')])
    assert isinstance(ansible_loader, AnsibleLoader)
    ansible_loader.dispose()

    ansible_loader = Ans

# Generated at 2022-06-13 07:42:07.061280
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Load a complex datastructure on purpose
    data = AnsibleLoader(open(__file__), file_name=__file__, vault_secrets=None).get_single_data()
    assert type(data) is dict
    assert '__file__' in data
    assert data['__file__'] == __file__
    assert '__line__' in data
    assert type(data['__line__']) is int

# Generated at 2022-06-13 07:42:15.764500
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = """
    - hosts: all
      gather_facts: false
      tasks:
        - name: test
          ping:
    """

    loader = AnsibleLoader(data, "my_filename", ["my_vault_secret"])

    nodes = list(loader.get_single_data())
    assert len(nodes) == 1
    assert isinstance(nodes[0], dict)
    assert 'hosts' in nodes[0].keys()
    assert 'gather_facts' in nodes[0].keys()
    assert 'tasks' in nodes[0].keys()
    assert isinstance(nodes[0]['hosts'], AnsibleUnicode)

# Generated at 2022-06-13 07:42:24.250820
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    stream = '''
    - a: 1
      z: 6
      b: 2
      c: 
          - d
          - e
          - f
    - a2: 3
    - a3: 4
    '''
    loader = DataLoader()
    data = loader.load(stream)
    assert data[0]['a'] == 1
    assert data[0]['z'] == 6
    assert data[0]['b'] == 2
    assert data[0]['c'] == ['d', 'e', 'f']
    assert data[1]['a2'] == 3
    assert data[2]['a3'] == 4

# Generated at 2022-06-13 07:42:25.357508
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:42:27.937174
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:42:34.073780
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml.objects import AnsibleMapping

    ansible_map = AnsibleMapping
    ansible_loader = AnsibleLoader(None)
    assert isinstance(ansible_loader.construct_yaml_map(None, None), ansible_map)

# Generated at 2022-06-13 07:42:36.779063
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import doctest
    doctest.testmod(AnsibleConstructor)



# Generated at 2022-06-13 07:42:40.966509
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = '''
            ---
            - hosts: localhost
              gather_facts: false
              tasks:
                - name: test
                  yum:
                    name: vim
                    state: latest
              variables:
                var1: "{{ lookup('file', '/tmp/foo') }}"
                var2: "{{ lookup('template', '/tmp/bar') }}"
              when: var1 is defined and var2 == 'ASSIGNEE'
              register: result
              ...
            '''

    stream = AnsibleLoader(data)
    res = stream.get_single_data()
    assert res[0]['when'] == 'var1 is defined and var2 == \'ASSIGNEE\''
    assert res[0]['tasks'][0]['yum']['name'] == 'vim'

# Generated at 2022-06-13 07:43:00.382859
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    instance = AnsibleLoader(None, None, None)
    assert instance is not None

# Generated at 2022-06-13 07:43:10.062379
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:43:24.995666
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class TestLoader(AnsibleLoader):
        def __init__(self, stream):
            super(TestLoader, self).__init__(stream)

    def test_construct_mapping(loader, node):
        data = AnsibleLoader.construct_mapping(loader, node)
        return {'foo': data}

    ansible_loader = TestLoader(stream=None)
    ansible_loader.add_constructor('!include', test_construct_mapping)

    # Using pyaml to dump the results of the AnsibleLoader.load method as
    # ansible.parsing.yaml.dumper.AnsibleDumper (which is what the YAML
    # dumper would be if we had

# Generated at 2022-06-13 07:43:33.898387
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Test data for successful creation of object
    class FakeStream:
        pass
    fake_stream = FakeStream()
    fake_file_name = 'ansible'
    fake_vault_secrets = dict()
    fake_vault_secrets['fake_secret'] = 'fake_value'
    ansible_loader = AnsibleLoader(fake_stream, fake_file_name, fake_vault_secrets)
    assert ansible_loader._reader == fake_stream
    assert ansible_loader.stream == fake_stream
    assert ansible_loader.file_name == fake_file_name
    assert ansible_loader.vault_secrets == fake_vault_secrets

# Generated at 2022-06-13 07:43:39.698369
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils.common.yaml import load_yaml
    data = load_yaml('foo: bar')
    assert isinstance(data['foo'], AnsibleUnicode)

# Generated at 2022-06-13 07:43:53.340582
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys
    import tempfile
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedFile
    from ansible.parsing.vault import VaultLib

    #
    # Create a Vault password file
    #
    tmp_dir = tempfile.mkdtemp()
    vault_passfile = os.path.join(tmp_dir, "vault_pass")
    with open(vault_passfile, "w") as f:
        f.write("12345\n")

    #
    # Create a Vaulted file
    #
    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 07:44:00.637053
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:44:03.042385
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader

    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:44:05.057693
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:44:12.383915
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = """
        foo: 1
        bar:
            baz: 2
            short_circuit: 1 && 0
        foobar: [ 1, 2 ]
    """

    # an arbitrary class to assign to test the "instance" in the constructor
    class arbitrary_class(object):
        pass

    loader = AnsibleLoader(data, '', None)
    new_data = loader.get_single_data()
    assert isinstance(new_data['bar'], arbitrary_class)
    assert isinstance(new_data['foobar'], arbitrary_class)
    assert new_data['bar'].baz == 2
    assert new_data['bar']['short_circuit'] == 1 and 0
    assert new_data['foobar']['0'] == 1

# Generated at 2022-06-13 07:44:59.153181
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    import yaml

    yaml_str = '''
foo:
 - name: chris
   age: 123
   hobbies:
     - skiing
     - snowboarding
   friends:
     - name: bob
       age: 456
       hobbies:
         - hiking
         - jumping
     - name: frank
       age: 789
       hobbies:
         - hacking
         - golf
'''

    yaml_data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert isinstance(yaml_data, AnsibleMapping)

    foo = y

# Generated at 2022-06-13 07:45:05.963108
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io

    data = u"""
        ---
        - hosts: all
          gather_facts: False
    """

    stream = io.BytesIO(data.encode('utf-8'))
    loader = AnsibleLoader(stream)
    data = loader.get_data()

    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    assert data[0].get('hosts') == 'all'

# Generated at 2022-06-13 07:45:11.561123
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:45:15.669702
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    test_AnsibleLoader:

    This function creates a AnsibleLoader instance and provides
    sample data for parsing. It can be used to test whether
    AnsibleLoader is a proper subclass of Parser.
    '''
    sample_data = '''
    - hosts: localhost
      gather_facts: False
      tasks:
      - shell: echo 1
    '''

    loader = AnsibleLoader(sample_data)
    assert isinstance(loader, Parser)

# Generated at 2022-06-13 07:45:17.366838
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=missing-docstring
    assert True

# Generated at 2022-06-13 07:45:26.964816
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Test the constructor of class AnsibleLoader
    """
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader('')
    assert isinstance(loader, Parser)
    assert isinstance(loader, AnsibleConstructor)

    loader = AnsibleLoader('', vault_secrets={})
    assert isinstance(loader.vault_secrets, dict)

    loader = AnsibleLoader('', vault_secrets={'a': 'A'})
    assert isinstance(loader.vault_secrets, dict)

# Generated at 2022-06-13 07:45:28.487318
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader(None, file_name=None, vault_secrets=None)

# Generated at 2022-06-13 07:45:29.505565
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:45:33.587737
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data1 = '''
%YAML 1.1
---
#anchor:
- &id001 hi
- &id002 there
- *id001
'''
    assert AnsibleLoader(data1).get_single_data() == ['hi', 'there', 'hi']



# Generated at 2022-06-13 07:45:44.530008
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import textwrap
    # Take block of text and strip whitespace (including newline characters)
    # so that we can use triple quotes in a multi-line string.
    yamlstring = textwrap.dedent("""
    ---
    foo:
      - name: 1
        b: 1
      - name: 2
        b: 2
    """).strip()
    # Now load the yaml with the AnsibleLoader
    mydict = AnsibleLoader(yamlstring).get_single_data()
    # Should be a dict
    import collections
    assert isinstance(mydict, collections.Mapping)
    # Should have key 'foo'
    assert 'foo' in mydict
    # Value of 'foo' should be a list
    assert isinstance(mydict['foo'], list)
    # Each member of the list should be a dict

# Generated at 2022-06-13 07:47:08.263760
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    vault_secret = [ 'secret' ]


# Generated at 2022-06-13 07:47:17.698035
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    import textwrap

# Generated at 2022-06-13 07:47:23.053113
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, Parser)

    if HAS_LIBYAML:
        assert isinstance(loader, AnsibleConstructor)
    else:
        assert isinstance(loader, Reader)
        assert isinstance(loader, Scanner)
        assert isinstance(loader, Composer)
        assert isinstance(loader, AnsibleConstructor)

# Generated at 2022-06-13 07:47:25.859210
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    with open('/usr/share/ansible/roles/test_role/vars/main.yaml', 'r') as f:
        AnsibleLoader(f)

# Test
if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:26.989681
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    obj = AnsibleLoader('')

# Generated at 2022-06-13 07:47:38.401650
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    import yaml

    # check that AnsibleLoader correctly calls AnsibleConstructor construct methods
    test_string = '''
        - unicode
        - 123
        -
          sequence:
            - 1
            - 2
            - 3
        -
          mapping:
            key1: val1
            key2: val2
            key3: val3
    '''

    # check that parse correctly calls AnsibleConstructor construct methods
    ansible_loader = AnsibleLoader(test_string)
    test_data = ansible_loader.get_single_data()

# Generated at 2022-06-13 07:47:41.631057
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = "Hello World!"
    a_loader = AnsibleLoader(stream)
    assert isinstance(a_loader, AnsibleLoader)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:43.021868
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:47:54.141964
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.common.yaml import HAS_LIBYAML
    from io import BytesIO

    vault_secrets = {'secret': {'password': 'vault_secret',
                                'password_file': '~/.vault_pass',
                                'rc_file': '~/.vault_pass',
                                'vault_id': 'vault_id',
                                'vault_identity': None,
                                'vault_version': 1}}


# Generated at 2022-06-13 07:48:03.143247
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import StringIO
    from ansible.parsing.yaml.objects import AnsibleUnicode

    if sys.version_info[0] < 3:
        from io import BytesIO
        from ansible.parsing.yaml.objects import AnsibleBase64
        from ansible.parsing.yaml.objects import AnsibleSequence

        class MyLoader(AnsibleLoader):
            def __init__(self, stream):
                AnsibleLoader.__init__(self, stream)
