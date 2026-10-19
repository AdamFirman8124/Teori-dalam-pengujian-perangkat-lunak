

# Generated at 2022-06-13 07:38:43.223733
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib, VaultSecret
    from ansible.module_utils.six import text_type

    vault_password_file = u'foo'
    vault_secrets = VaultLib([VaultSecret(vault_password_file)])
    stream = b'foo: {{bar}}\n'
    loader = DataLoader()
    data = loader.load(stream, file_name=u'foo', vault_secrets=vault_secrets)
    assert isinstance(data, dict)
    assert list(data.keys()) == [u'foo']

# Generated at 2022-06-13 07:38:52.377298
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.data import AnsibleMapping
    import sys


# Generated at 2022-06-13 07:38:57.563016
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestAnsibleLoader(unittest.TestCase):

        def test_constructor(self):
            self.assertTrue(hasattr(AnsibleLoader, "__init__"))

    unittest.main()

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:38:58.320760
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert False, "Unit tests must be implemented"

# Generated at 2022-06-13 07:38:59.079470
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    obj = AnsibleLoader('')
    assert obj

# Generated at 2022-06-13 07:39:10.481366
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils._text import to_bytes

    kwargs = {
        'vault_secrets': {},
        'file_name': '/etc/test/test.yml'
    }

    # Test with default AnsibleUnsafeText object
    output = AnsibleLoader.to_safe_data({'x': 'foo'}, **kwargs)
    assert(isinstance(output, dict))
    assert(isinstance(output['x'], AnsibleUnsafeText))


# Generated at 2022-06-13 07:39:15.470568
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    def mock_get_vault_secrets():
        return {'secret_key': 'secret_value'}

    # TODO: Write unit tests
    # loader = AnsibleLoader()
    # loader.get_vault_secrets = mock_get_vault_secrets
    pass

# Generated at 2022-06-13 07:39:17.373111
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader is not None


# Generated at 2022-06-13 07:39:27.451343
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    stream = '''
    foo:
        - { name: this runs a command, cmd: /usr/bin/foo, args: bar }
        - { name: this copies a file to a remote host, copy: src=foo dest={{ inventory_hostname }} }
        - name: this fetches a file, fetch: src=http://foo dest=/etc/foo flat=yes
    '''
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data['foo'][0]['args'] == 'bar'
    assert data['foo'][1]['copy']['src'] == 'foo'
    assert data['foo'][2]['fetch']['flat'] == 'yes'

# Generated at 2022-06-13 07:39:39.989833
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:39:50.701978
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class TestLoader(AnsibleLoader):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            super(TestLoader, self).__init__(stream, file_name=file_name, vault_secrets=vault_secrets)

    # test no file name is used
    test_loader_no_file_name = TestLoader(None)
    assert test_loader_no_file_name.file_name is None

    # test file name is used
    test_loader_with_file_name = TestLoader(None, file_name="/test/file/name")
    assert test_loader_with_file_name.file_name == "/test/file/name"

    # test vault_secrets is loaded

# Generated at 2022-06-13 07:40:01.777671
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    import sys
    import codecs
    # AnsibleUnicode is needed to get unicode strings on Python 2 and 3
    utf8_reader = codecs.getreader('utf-8')
    utf8_writer = codecs.getwriter('utf-8')
    # unicode strings on Python 3 need to be encoded in 'utf-8' while they can be directly written
    # to sys.stdout on Python 2
    if sys.version_info >= (3, 0):
        sys.stdin = utf8_reader(sys.stdin)
        sys.stdout = utf8_writer(sys.stdout)
    # Test AnsibleLoader:
    #

# Generated at 2022-06-13 07:40:08.203494
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    fp = open("test_AnsibleConstructor.yml", "w")
    fp.write("""
    ---
    !t
    """)
    fp.close()

    fp = open("test_AnsibleConstructor.yml", "r")
    loader = AnsibleLoader(fp)
    fp.close()

    output = loader.get_single_data()
    assert output == 't'

# Generated at 2022-06-13 07:40:09.600028
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True == HAS_LIBYAML or True

# Generated at 2022-06-13 07:40:21.787130
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    import datetime
    ansible_loader = AnsibleLoader(file_name='/foo')
    assert ansible_loader.file_name == '/foo'
    assert ansible_loader.vault_secrets is None

    yaml_unicode = ansible_loader.construct_yaml_unicode('foo')
    assert yaml_unicode == 'foo'
    assert isinstance(yaml_unicode, AnsibleUnicode)

    yaml_timestamp = ansible_loader.construct_yaml_timestamp('2013-12-19 12:15:01')

# Generated at 2022-06-13 07:40:28.820265
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # construct a dict
    test_dict = dict(a=1, b='foo')
    # convert the dict to a yaml string
    test_yaml_dict = '\n'.join((
        'a: 1',
        'b: foo',
    ))
    # create AnsibleLoader
    stream = AnsibleLoader(test_yaml_dict)
    # load the yaml string
    data = stream.get_single_data()
    # test the dict object
    assert isinstance(data, dict)
    assert data == test_dict


# Generated at 2022-06-13 07:40:39.884464
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # import the module
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # create a AnsibleVaultEncryptedUnicode object
    o = AnsibleVaultEncryptedUnicode('$ANSIBLE_VAULT;1.1;AES256\n33343533313838663039396562623733356238633033663232376264343538663835626663376333\n34306633306336326132323164303464636361316533303462626334313965616230343431613261\n636664316435396566313165323863356135363539643731356661623935313031641369a')

    # create a AnsibleLoader object

# Generated at 2022-06-13 07:40:42.453897
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml.add_constructor("!include", AnsibleConstructor.include)
    yaml.add_constructor("!vault", AnsibleConstructor.vault)

# Generated at 2022-06-13 07:40:55.556573
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    loader = DataLoader()

    # load some non-encrypted text
    data = '''
    foo: hi there
    bar:
      baz:
        - 1
        - 2
        - 3
    '''

    # check that the round-trip works
    assert data == loader.load(
        loader.dump(loader.load(data))
    )

    # now load an encrypted string and make sure it stays encrypted
    vault_pass = 'ansible'

# Generated at 2022-06-13 07:41:02.990209
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Create a stream
    stream = "key1: value1"

    # Testing init
    AnsibleLoader(stream)

    # Testing is_text
    obj = AnsibleLoader(stream)
    result = obj.is_text("hello")
    assert result == True
    result = obj.is_text("")
    assert result == True
    result = obj.is_text("  ")
    assert result == True

# Generated at 2022-06-13 07:41:12.469170
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    ansible_loader = AnsibleLoader(True)
    assert isinstance(ansible_loader, Resolver)

# Generated at 2022-06-13 07:41:23.666666
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_data = '''
---
-
  hosts: localhost
  tasks:
  - name: test
    debug:
        msg: testing
    when: true
  vars:
  -
     var1: "var1"
  vars_prompt:
  -
     var2: "var2_prompt"
    '''
    loader = AnsibleLoader(test_data)
    for data in loader:
        assert data == [{
            'hosts': 'localhost',
            'tasks': [{'debug': {'msg': 'testing'}, 'name': 'test', 'when': True}],
            'vars': [{'var1': 'var1'}],
            'vars_prompt': [{'var2': 'var2_prompt'}],
        }]

# Generated at 2022-06-13 07:41:26.487469
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.reader
    r = ansible.parsing.yaml.reader.AnsibleReader('foo')
    assert isinstance(r, AnsibleLoader)

# Generated at 2022-06-13 07:41:27.469350
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None, None, None)

# Generated at 2022-06-13 07:41:35.714106
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys

    class fake_file(object):
        def __init__(self,name):
            self.file_name = name
            self.data = '''
# test comment

- hosts: localhost
  remote_user: root
  gather_facts: False
  tasks:
    - name: test
      shell: "echo ok"
'''

        def read(self):
            return self.data

    file_name = "/path/to/test.yml"
    stream = fake_file(file_name)
    loader = AnsibleLoader(stream, file_name=file_name)
    for d in loader.get_single_data():
        assert d
        print(d)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:36.646086
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    t = AnsibleLoader(None, None)

# Generated at 2022-06-13 07:41:41.416709
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Verify that file_name is stored in __init__
    file_name = "hello"
    al = AnsibleLoader(file_name)
    assert al.file_name == file_name

    # Verify that vault_secrets is stored in __init__
    vault_secrets = {'password': 'hello'}
    al = AnsibleLoader(vault_secrets=vault_secrets)
    assert al.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:41:46.639600
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=too-many-locals,too-many-statements
    ''' Tests whether yaml.AnsibleLoader can load data into AnsibleData '''
    loader = AnsibleLoader(stream=None)
    assert loader is not None
    assert loader.file_name is None
    assert loader.vault_secrets is None

    # test construct_yaml_map for AnsibleData:
    #
    #  - name: Dummy
    #    values:
    #      color: blue
    #      size: large
    #      list:
    #        - one
    #        - two
    #      key:
    #        subkey: value
    #
    #  - name: Dummy2
    #    values:
    #      number: 1.5
    #      list:
    #

# Generated at 2022-06-13 07:41:52.356764
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class_name = "AnsibleLoader"
    class_types = [Parser, AnsibleConstructor, Resolver]
    for class_type in class_types:
        if not isinstance(object.__new__(AnsibleLoader), class_type):
            raise AssertionError("%s should be a subclass of %s" % (class_name, class_type.__name__))
    # Instance of class AnsibleLoader
    ansibleloader = AnsibleLoader(stream="")
    # Now accessing a class member
    ansibleloader.contruct_yaml_str("")

# Generated at 2022-06-13 07:41:53.834301
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# vim: set expandtab shiftwidth=4: #

# Generated at 2022-06-13 07:42:14.429609
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import shutil

    filename = 'test_AnsibleLoader/example.yaml'
    module_path = 'library/'
    test_vault_password = 'pass'
    encrypted_dir = 'vault'
    vault_id = 'vault.yml'
    decrypted_dir = 'decrypted'
    test_file_path = 'example.decrypted'

    # Create test directory
    shutil.rmtree(filename, True)
    if not os.path.exists(test_file_path):
        os.makedirs(test_file_path)

    # Create test vault file
    vault_path = os.path.join(filename, vault_id)
    if os.path.exists(vault_path):
        os.remove(vault_path)


# Generated at 2022-06-13 07:42:22.245447
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import load
    string = """
    foo: 1
    bar:
        - 2
            - 3
                - 4
    bam: {a: 2, b: 3}
    """

    obj = load(string, Loader=AnsibleLoader)
    assert obj['bar'] == [[[4]]]

    string = """
    foo: [1]
    bar: [2]
    bam: {a: 2, b: 3}
    """

    obj = load(string, Loader=AnsibleLoader)
    assert obj['bar'] == [2]
    assert obj['foo'] == [1]

# Generated at 2022-06-13 07:42:27.864915
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    obj = AnsibleLoader(None)
    assert isinstance(obj._file_name, type(None))
    assert isinstance(obj._vault_secrets, type(None))

# Generated at 2022-06-13 07:42:35.886880
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = """
---
# A trivial example to test AnsibleLoader constructor
- hosts: localhost
  tasks:
    - debug:
        msg: 'Hello world'
"""

    loader = AnsibleLoader(data)
    res = loader.get_single_data()
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0]['tasks'][0]['debug']

# Generated at 2022-06-13 07:42:40.447771
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Constructor should accept a list of valid file paths
    AnsibleLoader([__file__])

    # And should raise a TypeError exception for any other input
    try:
        AnsibleLoader(dict())
    except TypeError:
        pass
    else:
        raise AssertionError('unexpected test success')

# Generated at 2022-06-13 07:42:42.819606
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(None, None)
    assert not ansible_loader.file_name
    assert not ansible_loader.vault_secrets

# Generated at 2022-06-13 07:42:47.750288
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert hasattr(loader, '_yaml_extensions')
    assert isinstance(loader, AnsibleConstructor)
    assert hasattr(loader, 'state_machine')
    assert hasattr(loader, 'yaml_reader')
    assert isinstance(loader, Resolver)

# Generated at 2022-06-13 07:42:50.597590
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream='{}', file_name='file.yml', vault_secrets={})
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:42:58.749213
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def roundtrip(data, expected=None):
        if expected is None:
            expected = data
        loader = AnsibleLoader(data)
        result = loader.get_single_data()
        assert result == expected
    roundtrip("bi-token-scalar: bi-scalar")
    roundtrip("quoted-string: 'quoted-string'")
    roundtrip("complicated-key: !!str 'complicated-value'")
    roundtrip("list: [a, b, c]")
    roundtrip("plus-at-end: value+", "plus-at-end: value")
    roundtrip("plus-at-beginning: +value", "plus-at-beginning: value")
    roundtrip("plus-at-both-ends: +value+", "plus-at-both-ends: value")
   

# Generated at 2022-06-13 07:43:09.214043
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io
    import re
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_secret = None


# Generated at 2022-06-13 07:43:33.152502
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert 'AnsibleConstructor' in str(loader)

# Generated at 2022-06-13 07:43:48.187917
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    raw_text = """
    ---
    vars:
      var1: value1
    tasks:
    - name: task1
      debug: msg='Debug task1'
      assert:
        that:
          - foo == bar
    - name: task2
      debug: msg='Debug task2'
      assert:
        that:
          - foo == bar
          - 1 == 2
    - name: task3
      debug: msg='Debug task3'
      assert:
        that:
          - foo == bar
          - 1 == 1
    """
    loader = AnsibleLoader(raw_text)
    data = loader.get_single_data()
    assert len(data['assert']) == 3
    assert data['assert'][0]['that'][0] == 'foo == bar'

# Generated at 2022-06-13 07:43:58.030492
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    class TestConstructor(AnsibleLoader):
        def construct_yaml_str(self, node):
            # Override the default string handling function
            # to always return unicode objects
            return self.construct_scalar(node)

        def construct_scalar(self, node):
            return AnsibleUnicode(self.construct_yaml_str(node))

        def construct_yaml_seq(self, node):
            # Override the default list handling function
            # to always return list objects
            return self.construct_sequence(node)

        def construct_yaml_map(self, node):
            # Override the default dict handling function
            # to always return dict objects
            return self.construct_mapping(node)

       

# Generated at 2022-06-13 07:44:03.042349
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Positive test for AnsibleLoader.
    """
    stream = """
    this is some yaml
    """
    file_name = 'my_file_name'
    vault_secrets = 'my_vault_secrets'
    assert AnsibleLoader(stream, file_name, vault_secrets)

# Generated at 2022-06-13 07:44:12.489454
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultEditor

    vault_password = 'dummypass'
    vault = VaultEditor(vault_password)
    res = AnsibleLoader(None, vault_secrets=vault).construct_yaml_map(None, None)
    assert res == dict(), "Constructing empty map should return empty dict"
    res = AnsibleLoader(None, vault_secrets=vault).construct_yaml_seq(None, None)
    assert res == [], "Constructing empty sequence should return empty list"
    res = AnsibleLoader(None, vault_secrets=vault).construct_yaml_str(None)
    assert res == '', "Constructing empty string should return empty string"
   

# Generated at 2022-06-13 07:44:20.892012
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """This is a first level test to ensure that AnsibleLoader class
    is working properly.

    This test is only executed if we have PyYAML with LibYAML bindings
    installed.

     TODO: add more tests
    """
    import os
    TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'loader_unittest_data')
    TEST_VARS_FILE = os.path.join(TEST_DATA_DIR, 'vars.yml')

    anl = AnsibleLoader(open(TEST_VARS_FILE, 'r'))

    # First let's test AnsibleConstructor's __init__() method
    assert anl.stream is not None
    assert anl.file_name == TEST_VARS_FILE
    assert anl.vault_sec

# Generated at 2022-06-13 07:44:22.493231
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=too-few-public-methods
    """Unit test for constructor of class AnsibleLoader"""
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:44:28.365159
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    fake_yaml_string='''
---
foo:
  - [ 1, 2, 3 ]
'''
    yaml_data = AnsibleLoader(fake_yaml_string).get_single_data()

    assert yaml_data['foo'] == [ [ 1, 2, 3 ] ]

# Generated at 2022-06-13 07:44:29.684224
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    constructor = AnsibleLoader(None)
    assert constructor is not None

# Generated at 2022-06-13 07:44:31.285657
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None, file_name='/etc/ansible/hosts', vault_secrets=[])

# Generated at 2022-06-13 07:45:18.598690
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml.AnsibleLoader = AnsibleLoader

# Generated at 2022-06-13 07:45:27.652631
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=too-many-branches,too-many-statements
    import sys
    import os
    import yaml
    from ansible.parsing.yaml import objects

    fake_loader = AnsibleLoader(None, file_name='/fake/file')
    tmp_yaml = None

    if sys.version_info[0] > 2:
        assert isinstance(fake_loader.construct_python_unicode(None), str)
    else:
        assert isinstance(fake_loader.construct_python_unicode(None), unicode)  # pylint: disable=undefined-variable

    assert isinstance(fake_loader, AnsibleLoader)
    assert isinstance(fake_loader, yaml.Loader)
    assert not fake_loader.vault_secrets

# Generated at 2022-06-13 07:45:34.646279
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import tempfile
    fd, fn = tempfile.mkstemp()
    f = open(fn, 'w')
    f.write("""
- hosts: localhost
  vars:
    varname: hi
  tasks:
    - shell: echo {{ varname }}")
""")
    f.close()
    loader = AnsibleLoader(f)
    for d in list(loader):
      print(d)
    import os
    os.remove(fn)

# Generated at 2022-06-13 07:45:35.306517
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:45:37.895884
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:45:41.765008
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = "test"
    file_name = "file"
    vault_secrets = "vault_secrets"

    assert AnsibleLoader(stream, file_name=file_name, vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:45:49.825951
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class DummyVaultSecrets(object):

        key = 'this is a key, really'
        all_candidates = [key]

        @staticmethod
        def get_decryption_key(secret):
            if secret not in DummyVaultSecrets.all_candidates:
                raise ValueError('secret not found')
            return DummyVaultSecrets.key

    class DummyVaultSecrets2(DummyVaultSecrets):

        all_candidates = []

    def check(loader, yaml_data, expected_data):

        data = loader.get_single_data()

        assert data == expected_data, \
            '%s != %s' % (data, expected_data)


# Generated at 2022-06-13 07:45:56.455030
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
    ---
    a:
      - 1
      - 2
      - 3
      - "a=b"
      - "c={{ d }}"
    """
    al = AnsibleLoader(data, file_name='/tmp/file_name')
    assert al.get_single_data() == {'a': [1, 2, 3, "a=b", "c={{ d }}"]}
    assert str(al.file_name) == '/tmp/file_name'

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:45:57.742947
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:46:05.177898
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime

    data = """
    - 1
    - 2
    - 3
    """

    data = AnsibleLoader(data).get_single_data()
    assert isinstance(data, list) and data == [1, 2, 3]

    data = """
    _string: "0123456789"
    _int: 12345
    _float: 12345.6789
    _bool: True
    _binary: !!binary |
      0123456789ABCDEF
    _none: null
    _list:
      - 1
      - 2
    _dict:
      a: 1
      b: 2
    """
    data = AnsibleLoader(data).get_single_data()

    assert isinstance(data['_string'], str) and data['_string'] == "0123456789"


# Generated at 2022-06-13 07:47:46.006823
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    test_input = '''
- hosts: localhost
  tasks:
  - name: test
    ping:
'''

    loader = AnsibleLoader(test_input)
    obj = loader.get_single_data()
    assert obj

# Generated at 2022-06-13 07:47:46.597167
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:47:48.896346
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=no-self-use
    loader = AnsibleLoader('')
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:47:54.593241
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # This is not testing the instantiation of the class, but rather
    # the yaml constructor
    config = AnsibleLoader("---\n")
    assert config is not None
    config = AnsibleLoader('---\nfoo: [ 1, {{ bar }} ]')
    assert config is not None
    assert config.yaml_data == {u'foo': [1, u'{{ bar }}']}

# Generated at 2022-06-13 07:48:01.123324
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml_str = """
    - hosts: localhost
      tasks:
        - name: will be replaced
          shell: uname -a
          register: shell_out
        - debug: var=shell_out.stdout
    """
    my_loader = AnsibleLoader(yaml_str)
    data = my_loader.get_single_data()
    print(data)
    print(yaml.dump(data))

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:48:12.037007
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Basic unit test for AnsibleLoader class
    """

# Generated at 2022-06-13 07:48:19.397441
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=unused-variable
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping, AnsibleSequence

    # This test should fail if we have libyaml but not python2.7 and if we don't have libyaml we're testing on python2.7
    if HAS_LIBYAML:
        assert not (sys.version_info[0] == 2 and sys.version_info[1] < 7)
    else:
        assert sys.version_info[0] == 2 and sys.version_info[1] >= 7


# Generated at 2022-06-13 07:48:24.333306
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestLoader:
        def __init__(self, stream):
            pass
    try:
        TestLoader.__bases__ = (AnsibleLoader,)
    except TypeError:
        TestLoader.__bases__ = (AnsibleLoader,)
    finally:
        t = TestLoader(stream=None)

# Generated at 2022-06-13 07:48:35.921615
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys

    # Test of non-vault yaml file
    if HAS_LIBYAML:
        filename = sys.modules[__name__].__file__
        if filename.endswith(".pyc"):
            filename = filename[:-1]
        sample_file = open(filename.replace('/lib/ansible/parsing/yaml/objects.pyc', '/test/sanity/parsing/yaml/sample.yml'))
    else:
        sample_file = sys.modules[__name__].__file__
        sample_file = open(sample_file.replace('/ansible/parsing/yaml/objects.py', '/test/sanity/parsing/yaml/sample.yml'))

    loader = AnsibleLoader(sample_file)