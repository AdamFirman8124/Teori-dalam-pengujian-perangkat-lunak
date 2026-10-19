

# Generated at 2022-06-13 07:38:43.648886
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    options = dict(file_name='item1', vault_secrets=None)
    l = AnsibleLoader('', **options)
    assert isinstance(l.file_name, AnsibleUnicode)

if __name__ == "__main__":
    import sys
    import doctest
    import unittest
    suite = doctest.DocTestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_AnsibleLoader))
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)

# Generated at 2022-06-13 07:38:44.859433
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml.load('''
foo: !include bar
''', Loader=AnsibleLoader)

# Generated at 2022-06-13 07:38:54.438368
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultLib, UnsafeLoader

    vault_secrets = VaultLib(load_methods=[UnsafeLoader])


# Generated at 2022-06-13 07:38:55.661631
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleConstructor)

# Generated at 2022-06-13 07:38:57.096513
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    print(AnsibleLoader)

# Generated at 2022-06-13 07:39:00.293177
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansibleloader = AnsibleLoader('')
    assert isinstance(ansibleloader.construct_yaml_map, AnsibleConstructor.construct_yaml_map.__func__)

# Generated at 2022-06-13 07:39:03.451717
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def check_AnsibleLoader_instantiation():
        AnsibleLoader(None)
    check_AnsibleLoader_instantiation()

# Generated at 2022-06-13 07:39:08.028812
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    file_name = 'filename'
    vault_secrets = ['foo', 'bar']
    test_ansible_loader = AnsibleLoader(file_name, vault_secrets)
    assert test_ansible_loader.file_name == file_name
    assert test_ansible_loader.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:39:21.138685
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''
- hosts: localhost
  tasks:
  - shell: echo "This is a test"
    register: shell_out
    changed_when: shell_out.stdout != "This is a test"
  - debug: var=shell_out.stdout
    debug:
      msg: "This is also a test"
    debug:
      msg: "This is {{ shell_out.stdout }} a test"
'''

    data = AnsibleLoader(yaml_str).get_single_data()
    assert data is not None
    assert len(data) == 2
    hosts = data[0]
    tasks = data[1]
    assert hosts['hosts'] == 'localhost'
    assert tasks[0]['shell'] == 'echo "This is a test"'

# Generated at 2022-06-13 07:39:26.211501
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(None)
    assert not hasattr(ansible_loader, '_AnsibleLoader__settings')
    assert not hasattr(ansible_loader, '_AnsibleLoader__file_name')
    assert not hasattr(ansible_loader, '_AnsibleLoader__vault_secrets')
    del ansible_loader

# Generated at 2022-06-13 07:39:32.858867
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:39:38.262775
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    loader = AnsibleLoader(io.StringIO(u"""
    {% raw %}{{ val }}{% endraw %}:
      name: foo
      new: "{{ val }}"
      baz: "{{ myvar }}"
      dict:
           key: val
    """))

    assert loader



# Generated at 2022-06-13 07:39:40.671794
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import doctest
    failed, tried = doctest.testmod()
    if failed == 0:
        print('All Tests for AnsibleLoader passed.')

# Generated at 2022-06-13 07:39:49.497011
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    # pylint: disable=too-many-function-args
    a = AnsibleLoader("---\nfoo: !vault |\n  $ANSIBLE_VAULT;1.1;AES256\n  34616261393266323962653861613633346532623263633065346163383962336635333439336364\n  61653430376362316664333631303262393262303864616133323431346331626366633462366231\n  363734\n", vault_secrets={"_ansible_vault_password": "foo"})
    # pyl

# Generated at 2022-06-13 07:39:50.472676
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None, None, None)

# Generated at 2022-06-13 07:40:00.521712
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = """
    - hosts: all
      gather_facts: no
    - hosts: unix
      tasks:
      - shell: echo "Hello world!"
      - shell: echo "The meaning of life is 42"
    - hosts: windows
      tasks:
      - debug:
          msg: Hello world!
      - debug:
          msg: The meaning of life is 42
    """

    parsed_data = AnsibleLoader(data, vault_secrets=[], file_name='cli').get_single_data()
    print(parsed_data)


if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:40:08.737263
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import unittest

    class TestAnsibleLoader(unittest.TestCase):
        def test_AnsibleLoader(self):
            stream = io.StringIO("{ 'a':1, 'b':2 }")

            loader = AnsibleLoader(stream, file_name='myfile')
            self.assertIsInstance(loader, AnsibleLoader)

            data = loader.get_single_data()
            self.assertIsInstance(data, dict)

    # Run tests if module run directly
    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 07:40:09.410936
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:40:10.764477
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:40:12.991974
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    stream = file('/etc/ansible/hosts')
    stream = AnsibleLoader(stream)
    data = yaml.load(stream)

# Generated at 2022-06-13 07:40:18.689779
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
- one
- two
- three
"""
    result = list(AnsibleLoader(data))
    assert result == ['one', 'two', 'three']

# Generated at 2022-06-13 07:40:27.918141
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    AnsibleLoader.__init__
    '''
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence

    stream = "a_string:\n  - item1\n  - item2"
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert isinstance(data, dict), data
    assert isinstance(data['a_string'], AnsibleSequence)
    assert isinstance(data['a_string'][0], AnsibleUnicode)

    data = loader.get_single_data()
    assert data is None

# Generated at 2022-06-13 07:40:39.317035
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
- hosts: all
  gather_facts: false
  tasks:
  - shell: echo "hello world"
'''
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert sorted(data[0]) == ['gather_facts', 'hosts', 'tasks']
    assert data[0]['gather_facts'] == False
    assert data[0]['hosts'] == 'all'
    assert len(data[0]['tasks']) == 1
    assert data[0]['tasks'][0]['shell'] == 'echo "hello world"'
    assert sorted(data[0]['tasks'][0]) == ['shell', 'when']
    assert data[0]['tasks'][0]['when'] == 'True'

# Generated at 2022-06-13 07:40:47.639609
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import YAMLError
    sample_yaml_string = '''
        - hosts: localhost
          gather_facts: false
          tasks:
            - name: Just a debug task to display the ec2_facts
              debug:
                  var: ec2_facts
    '''

    rval = []
    try:
        rval = AnsibleLoader(sample_yaml_string, 'hosts', None).get_single_data()
    except YAMLError:
        pass
    assert type(rval) == list
    assert len(rval) == 1
    assert type(rval[0]) == dict
    assert 'hosts' in rval[0]
    assert rval[0]['hosts'] == 'localhost'
    assert 'gather_facts' in rval[0]
   

# Generated at 2022-06-13 07:40:48.869686
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    fake_secret = u'$ANSIBLE_VAULT;1.1;AES256;'
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:40:56.315617
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=invalid-name
    valid_yaml = b'''
        ---
        scope: local
        hosts:
            - green
            - blue
            - red
        tasks:
            - name: test localhost
              ping:
        ...
    '''

    from io import BytesIO
    from ansible.parsing.yaml.objects import AnsibleVaultSecret

    loader = AnsibleLoader(BytesIO(valid_yaml))
    data = loader.get_single_data()
    assert isinstance(data, dict)
    assert 'scope' in data
    assert data['scope'] == 'local'
    assert 'hosts' in data
    assert isinstance(data['hosts'], list)
    assert data['hosts'][0] == 'green'

# Generated at 2022-06-13 07:41:04.696695
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Make sure we don't instantiate AnsibleLoader class as we need to
    # instantiate specific loader class based on libyaml available
    try:
        AnsibleLoader('')
        raise AssertionError('Expected to throw ImportError when initializing AnsibleLoader')
    except ImportError as e:
        if str(e) != 'No module named libyaml':
            raise AssertionError('ImportError exception has unexpected message: %s' % str(e))

# Generated at 2022-06-13 07:41:17.742376
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from yaml import CLoader, CDumper
    except ImportError:
        from yaml import Loader, Dumper
    input_data = u"""{
    AnsibleUnicodeType: "Hello World!"
}
"""
    input_stream = input_data.encode('utf-8')
    from io import BytesIO
    stream = BytesIO(input_stream)
    import sys
    if sys.version_info > (3, 0):
        loader = AnsibleLoader(stream)  # pylint: disable=no-value-for-parameter
    else:
        loader = AnsibleLoader(stream)
    datamap = loader.get_single_data()
    assert 'AnsibleUnicodeType' in datamap

# Generated at 2022-06-13 07:41:28.351113
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    s = '!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          34643066396438313161393538623564396139313363383131303065646637326435323634623965\n          65653537363937313162382d33373465323061623762306130623033656636626266636339623839\n          373363313236\n'

    loader = AnsibleLoader(s)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 07:41:34.201150
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import StringIO
    s = StringIO.StringIO()
    print('---', file=s)
    print('foo: bar', file=s)
    print('baz:', file=s)
    print('  - qux', file=s)
    s.seek(0)
    assert AnsibleLoader(s).get_single_data() == {'foo': 'bar', 'baz': ['qux']}

# Generated at 2022-06-13 07:41:48.124704
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert HAS_LIBYAML
    data = dict(
        test=dict(
            value=dict(
                str="abc",
                bool=True,
                date="2001-01-01",
                time="12:00:00",
                datetime="2001-01-01 12:00:00",
                ansible_date="2001-01-01T12:00:00Z",
            )
        )
    )
    yaml_data = __import__('yaml').dump(data)
    loader = AnsibleLoader(yaml_data)
    assert loader.get_single_data() == data

# Generated at 2022-06-13 07:41:50.992319
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """ Test if AnsibleLoader class is instantiable """
    loader = AnsibleLoader(None)
    assert hasattr(loader, 'construct_yaml_map')

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:52.551272
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Ensure that the loaders are in place
    '''

    # Place holder test case
    assert True

# Generated at 2022-06-13 07:42:00.965839
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    
    if sys.version_info[0] == 3:
        # Python 3 syntax, with 'myvar' as the data source
        myvar = b"!!!python/object:ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode aGVsbG8gd29ybGQ="
    
        # Create a yaml parser object, using AnsibleLoader as the constructor
        ansible_loader = AnsibleLoader(myvar)
        ansible_loader.get_single_node()
    
        # Get the parsed output
        print(ansible_loader.get_data())


# Generated at 2022-06-13 07:42:01.869737
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:42:05.779804
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = "{ foo: bar }"
    loader = AnsibleLoader(data)
    assert isinstance(loader.get_single_data(), dict)
    assert isinstance(list(loader.get_single_data().keys())[0], AnsibleUnicode)



# Generated at 2022-06-13 07:42:14.975839
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os,sys,json
    #sys.argv = ['','/Users/mac/dev/ansible/lib/ansible/parsing/yaml/loader.py']
    #sys.argv = os.path.abspath(sys.argv[1])
    #print(sys.argv)
    config_file = '/Users/mac/dev/ansible/playbooks/example.yml'
    with open(config_file, 'r') as f:
        #print(f)
        data = AnsibleLoader(f).get_single_data()
        print(data)
        f.close()
    #print(json.dumps(datas,indent=4,sort_keys=True))

# Generated at 2022-06-13 07:42:16.684623
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, (Parser, AnsibleConstructor, Resolver))

# Generated at 2022-06-13 07:42:23.645960
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    try:
        from ansible.parsing.yaml.loader import AnsibleLoader
    except ImportError:
        from ansible.parsing.yaml.loader import AnsibleLoader

    data = '''
        a: 1
        b:
            c: 3
            d: 4
        e:
            f: 5
        '''
    loader = AnsibleLoader(data)
    target = '''{'a': 1, 'b': {'c': 3, 'd': 4}, 'e': {'f': 5}}'''
    result = str(loader.get_single_data())
    assert result == target

# Generated at 2022-06-13 07:42:38.822386
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import TelnetConstructor
    from ansible.parsing.yaml.loader import TelnetPattern
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.dumper import AnsibleSafeDumper
    import os
    import pkg_resources

    resource_package = __name__

    resource_path = '/'.join(('data', 'base.yml'))
    filename = pkg_resources.resource_filename(resource_package, resource_path)

    # Load yaml with Telnet as a tag
    with open(filename, 'r') as f:
        data = AnsibleLoader(f).get_single_data()

    # Check if TelnetPattern is used

# Generated at 2022-06-13 07:42:56.693193
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import os
    import getpass

    if getpass.getuser() == 'jenkins':
        sys.path.append('/usr/lib/python2.7/site-packages')
    else:
        sys.path.append('/usr/local/lib/python2.7/dist-packages')

    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleSequence
    from ansible.module_utils.common.collections import ImmutableDict

    loader = AnsibleLoader(None, 'dummy.txt', None)
    dumper = AnsibleDumper()

# Generated at 2022-06-13 07:43:08.154885
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def test_variable_padding(self):
        self.assertEqual(self.get_single_data('{{foo}}'), '{{foo}}')
        self.assertEqual(self.get_single_data('{{ foo }}'), '{{ foo }}')
        self.assertEqual(self.get_single_data('{{  foo  }}'), '{{  foo  }}')
        self.assertEqual(self.get_single_data('{{ foo  }}'), '{{ foo  }}')
        self.assertEqual(self.get_single_data('{{ foo}}'), '{{ foo}}')

    def test_nested_variable_padding(self):
        self.assertEqual(self.get_single_data('{{ foo{{nested}} }}'), '{{ foo{{nested}} }}')

# Generated at 2022-06-13 07:43:17.936355
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # The data to be loaded
    data = u'''
a: 1
b:
  c: 2
d: "{{foobar}}"
e: "{{ fa la  }}"
f: "{{'fa' 'la'}}"
g: |
  {{ 'fa'
  'la'}}
h: "{{nospaces}}"
i: "{{foo|upper}}"

j:
  - k: "{{bar|upper}}"
  - k: "{{bar|upper}}"
l:
  foo: "{{ 'bar' }}"
'''

    # The variables

# Generated at 2022-06-13 07:43:19.330264
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleConstructor)

# Generated at 2022-06-13 07:43:23.363315
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = "foo: !var a"
    loader = AnsibleLoader(stream)
    assert loader.stream == stream

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:43:24.384814
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    instance = AnsibleLoader(None)

# Generated at 2022-06-13 07:43:25.967117
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    class AnsibleLoader
    '''
    pass

# Generated at 2022-06-13 07:43:27.245181
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader(None, None, None)

# Generated at 2022-06-13 07:43:37.225115
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping

    # https://github.com/ansible/ansible/issues/26463
    # Sequences (lists) within mappings (dicts) were not being recognized as
    # AnsibleSequences by AnsibleConstructor's construct_yaml_map() method.
    # Instead, they were being recognized as YAML Lists, which have __slots__,
    # and thus don't get returned to AnsibleAnsibleLoader functions as
    # proper Python Lists.  The end result was that the caller would see a
    # YAML List instead of a Python List in certain cases.
    #
    # This unit test ensures that the AnsibleLoader correctly returns a Python
    # List when a YAML List is expected.
    data

# Generated at 2022-06-13 07:43:40.489107
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader('')
    unicode_object = loader.construct_yaml_str(None)
    assert isinstance(unicode_object, AnsibleUnicode)

# Generated at 2022-06-13 07:43:58.680397
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True

# Generated at 2022-06-13 07:44:00.491413
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:44:01.944104
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    x = AnsibleLoader("test")
    assert type(x) == AnsibleLoader

# Generated at 2022-06-13 07:44:04.508575
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("{test: test}")
    assert loader.get_single_data() == {'test': 'test'}

# Generated at 2022-06-13 07:44:11.839466
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultEditor
    text = '$ANSIBLE_VAULT;1.1;AES256'
    secrets = VaultSecret('foobar')
    vault = VaultLib(secrets)
    vault_password = 'foobar'
    vault_password_file = None
    editor = VaultEditor(vault, vault_password, vault_password_file)
    vault_data = VaultEditor.decrypt(editor, text)
    assert type(vault_data) == AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:44:20.375332
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import os
    import tempfile

    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader

    vault_id = '7b70d2c5-7d5a-4876-a7a8-3c3ae7b943ec'
    vault_password = '$6$8O3E1lZw$KvHfW23O8X9f0cg.6UzL6U0p6Z0AMdT'
    vault_secrets = {'_ansible_vault_password': vault_password,
                     '_ansible_vault_id': vault_id}
    fd, tmpfile = tempfile.mkstemp()

    stream = open(tmpfile, 'w+')

# Generated at 2022-06-13 07:44:21.222974
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:44:28.811068
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
    !!python/object/apply:ansible.parsing.yaml.objects.AnsibleUnicode
    args: ['string with a {{ lookup(\'pipe\', \'echo test1\') }}']
    '''
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data == 'string with a test1'


# Generated at 2022-06-13 07:44:38.780883
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys

    class TestAnsibleLoader(AnsibleLoader):
        def construct_yaml_null(self, node):
            return None

    data1 = "foo"
    yaml_str = AnsibleDumper(default_flow_style=False).dump(data1)
    data2 = TestAnsibleLoader(yaml_str).get_single_data()

    assert isinstance(data2, AnsibleUnicode)
    assert data2 == data1

    data3 = {'a': 1, 'b': 2, 'c': 'foo'}

# Generated at 2022-06-13 07:44:41.875773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    obj = AnsibleLoader('[ datetime.datetime(2013, 12, 29, 15, 20, 21) ]').get_single_data()
    assert obj == datetime.datetime(2013, 12, 29, 15, 20, 21)

# Generated at 2022-06-13 07:45:26.687562
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.resolver import Resolver
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    if HAS_LIBYAML:
        from ansible.module_utils.common.yaml import Parser
        from ansible.module_utils.common.yaml import HAS_LIBYAML
        from __main__ import AnsibleLoader

        def test_AnsibleLoader():
            from yaml.resolver import Resolver
            from ansible.parsing.yaml.constructor import AnsibleConstructor
            from ansible.module_utils.common.yaml import Parser
            from ansible.module_utils.common.yaml import HAS_LIBYAML
            from __main__ import AnsibleLoader
            assert issubclass(AnsibleLoader, Parser)

# Generated at 2022-06-13 07:45:37.851942
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import time, copy
    import yaml
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var

    test_constructors = {
        "!fail": lambda x: 1/0,
        "!hail": lambda x: (2, 3)
    }
    vault_secrets = {'vault_password_file': 'foobar'}
    test_types = {
        "!fail": int,
        "!hail": list
    }
    file_name="test_file"
    al = AnsibleLoader(None, file_name=file_name, vault_secrets=vault_secrets)
    assert al.file_name == file_name

# Generated at 2022-06-13 07:45:43.514295
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert(loader.construct_yaml_map == AnsibleConstructor.construct_yaml_map)
    assert(loader.construct_yaml_str == AnsibleConstructor.construct_yaml_str)
    assert(loader.construct_yaml_seq == AnsibleConstructor.construct_yaml_seq)
    assert(loader.resolve == Resolver.resolve)

# Generated at 2022-06-13 07:45:50.916423
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if not hasattr(sys, 'gettotalrefcount'):
        # gettotalrefcount() is only available with python debug builds
        return

    import os
    import re
    import traceback

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    def load_yaml_text(text):
        # load yaml and return the number of nodes created (total_nodes) and the number of AnsibleBaseYAMLObject instances (ansible_nodes)
        sl = AnsibleLoader(text)
        try:
            data = sl.get_single_data()
        except:
            raise
        total_nodes = sl.composer.node_count()
        ansible_nodes = 0

# Generated at 2022-06-13 07:45:52.520176
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None)

# Generated at 2022-06-13 07:46:00.017242
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.scalarstring import AnsibleScalarString

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Tests below are adapted from the 'YAML Cookbook' by
    # Shawn M Moore, and 'YAML Ain't Markup Language' by
    # Clark Evans, Ingy döt Net, and Brian Ingerson

    # All scalar strings are prefaced by the 'tag:yaml.org,2002:str' tag
    # http://pyyaml.org/wiki/PyYAMLDocument

# Generated at 2022-06-13 07:46:09.025158
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestLoader(AnsibleLoader):
        def ansible_find_all_include_paths(self):
            return ['.']

    # test ansible_find_all_include_paths being used when it's defined
    try:
        from ansible.parsing.yaml.loader import find_all_include_paths
    except ImportError:
        # ansible 2.4
        from ansible.parsing.yaml.objects import AnsibleMapping
        class TestLoader(AnsibleLoader):
            def ansible_find_all_include_paths(self):
                return ['.']

        TestLoader.add_constructor(
            u'tag:yaml.org,2002:map',
            TestLoader.construct_yaml_map)

# Generated at 2022-06-13 07:46:20.149217
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.objects

    filename = None
    loader = AnsibleLoader(None, filename)
    assert(loader)

    # Can't test this code path without libyaml
    # Though given it's also not used on any Python 2 platform,
    # likely ok
    if HAS_LIBYAML:
        # ensure AnsibleLoader adds the ansible namespace to the tag registry
        registry = loader.yaml_impl.resolver.yaml_impl.registry
        assert(ansible.parsing.yaml.objects in registry.values())



# Generated at 2022-06-13 07:46:29.047731
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.yaml import HAS_LIBYAML, Parser
    import pytest
    if HAS_LIBYAML:
        from ansible.parsing.yaml.loader import AnsibleLoader

    test_up_front_error = '''
        #!/bin/sh
        echo "hello world"
        '''
    loader = AnsibleLoader(None, file_name=None, vault_secrets=None)

if __name__ == '__main__':
    pytest.main([__file__])

# Generated at 2022-06-13 07:46:36.614443
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    test_stream = '''
        ---
        - "{{ a }}"
        - "{{ b }}"
        - "{{ c }}"
        - "{{ d }}"
        - "{{ e }}"
        - "{{ f }}"
    '''
    obj = AnsibleLoader(test_stream)
    print(obj)
    yaml_obj = obj.get_single_data()
    print(yaml_obj)
    obj1 = AnsibleConstructor(file_name=None, vault_secrets=None)
    print(obj1)

# Unit tests for class Reader

# Generated at 2022-06-13 07:47:52.449777
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass



# Generated at 2022-06-13 07:47:57.955313
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test parsing empty stream.
    assert AnsibleLoader('').get_single_data() == None

    # Test parsing stream containing just a comment.
    assert AnsibleLoader('#just a comment').get_single_data() == None

    # Test parsing stream containing just a document.
    assert AnsibleLoader('key: value').get_single_data() == dict(key='value')

    # Test parsing str

# Generated at 2022-06-13 07:48:00.384482
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    text = '''{ ansible_facts: { test_fact: "test_value" } }'''
    loader = AnsibleLoader(text)
    loader.get_data()

# Generated at 2022-06-13 07:48:05.780160
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader(None, 'a_file_name')
    assert isinstance(loader.file_name, AnsibleUnicode)
    assert loader.file_name == u'a_file_name'

# Generated at 2022-06-13 07:48:15.291255
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedFile
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    from ansible.inventory.host import Host


# Generated at 2022-06-13 07:48:20.212738
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # init empty AnsibleLoader
    AnsibleLoader('')

    # init AnsibleLoader with some stream
    AnsibleLoader('---\n')

    # init AnsibleLoader with file name
    AnsibleLoader('', file_name='dummy_file_name')

# Generated at 2022-06-13 07:48:22.272281
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(None)
    assert ansible_loader is not None

# Generated at 2022-06-13 07:48:24.570359
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    y = AnsibleLoader('hello: world')
    assert 'hello' in y.get_data()


# Generated at 2022-06-13 07:48:29.436594
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    ansible.parsing.yaml.dumper.AnsibleLoader
    """
    print('TEST','ansible.parsing.yaml.dumper.AnsibleLoader')
    al = AnsibleLoader(None)
    assert al
    # cleanup
    del al

# Generated at 2022-06-13 07:48:38.462367
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # non 2.6 yaml
    if not hasattr('yaml.BaseLoader.check_data'):
        return

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
