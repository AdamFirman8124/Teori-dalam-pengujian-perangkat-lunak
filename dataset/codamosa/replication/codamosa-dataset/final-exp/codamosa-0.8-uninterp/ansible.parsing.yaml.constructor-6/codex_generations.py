

# Generated at 2022-06-13 07:28:15.038930
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import io
    import unittest
    import ruamel.yaml

    class Test_construct_yaml_str(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None


# Generated at 2022-06-13 07:28:26.180623
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import UNSAFE_PROXY_MARKER

    text = '''
- 12345
- !unsafe "abcde"
- '!unsafe'
- !unsafe 12345
- !unsafe '!unsafe'
'''
    loader = AnsibleLoader(text, None)
    # Test that all unsafe unsafe objects are correctly constructed
    assert len(loader.get_single_data()) == 5
    assert loader.get_single_data()[0] == 12345
    assert isinstance(loader.get_single_data()[1], AnsibleUnsafeText)

# Generated at 2022-06-13 07:28:34.504013
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    yaml_src = '''
    roger:
        - first_name: "Roger"
          last_name: "Smith"
        - first_name: "Roger"
          last_name: "Smith"
    steve:
        - first_name: "Steve"
          last_name: "Rogers"
    '''
    settings = AnsibleMapping()
    settings.ansible_pos = ('/path/to/settings.yaml', 3, 2)

    roger = AnsibleMapping()
    roger.ansible_pos = ('/path/to/settings.yaml', 4, 4)
    roger['first_name'] = u'Roger'
    roger.ansible_pos = ('/path/to/settings.yaml', 4, 16)

# Generated at 2022-06-13 07:28:41.789025
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    class MyConstructor(AnsibleConstructor):
        def __init__(self, file_name=None, vault_secrets=None):
            super(MyConstructor, self).__init__(file_name=None, vault_secrets=None)
            self._implicit = {}

    loader = yaml.Loader
    loader.add_implicit_resolver('!class-a', re.compile("^class-a$"), None)
    loader.add_constructor('!class-a', MyConstructor.construct_yaml_unsafe)

    class_a = yaml.load("!class-a class-a", Loader=loader)
    assert class_a.value == "class-a"


# Generated at 2022-06-13 07:28:55.799612
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml import objects
    import sys
    import io

    vault_pass = 'dummy_vault_pass'
    plaintext_data = 'plaintext_data'
    vault_id = 'dummy_vault_id'

    #Mock the load method of VaultLib to return plaintext_data
    vault_proxy = VaultLib(secrets=[vault_pass])
    vault_proxy.load = mock.Mock(return_value=plaintext_data)

    #Mock the load method of AnsibleConstructor to return vault_encrypted_data
    vault_encrypted_data = vault_proxy.encrypt(plaintext_data, vault_id=vault_id)

# Generated at 2022-06-13 07:29:00.901255
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    text = u'["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]'
    text_bytes = to_bytes(text)
    constructor = AnsibleConstructor()
    data = list(constructor.construct_yaml_seq(constructor.construct_yaml_str(text_bytes)))
    assert len(data) == 10
    assert data[0] == u'one'
    assert data[1] == u'two'
    assert data[2] == u'three'
    assert data[9] == u'ten'



# Generated at 2022-06-13 07:29:10.184643
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Simple test, yaml file is empty
    # Compute expected value
    expected_value = "vault_encrypted_unicode"
    # Create instance of AnsibleConstructor and call method construct_vault_encrypted_unicode
    actual_value = AnsibleConstructor().construct_vault_encrypted_unicode("vault_encrypted_unicode")
    # Check
    assert isinstance(actual_value.__class__, AnsibleUnicode.__class__)
    assert actual_value == expected_value

# Generated at 2022-06-13 07:29:18.828383
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import base64

# Generated at 2022-06-13 07:29:22.129740
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys
    if sys.version_info[0] < 3:
        return py2_test_AnsibleConstructor_construct_yaml_seq()
    else:
        return py3_test_AnsibleConstructor_construct_yaml_seq()


# Generated at 2022-06-13 07:29:26.413654
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    instance = AnsibleConstructor("test_AnsibleConstructor_construct_yaml_map.yml")
    node = MappingNode(u'tag:yaml.org,2002:map', [], [])
    data = instance.construct_yaml_map(node)
    assert(isinstance(data, AnsibleMapping))
    assert(data.ansible_pos == ('test_AnsibleConstructor_construct_yaml_map.yml', 1, 1))


# Generated at 2022-06-13 07:29:42.041767
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml


# Generated at 2022-06-13 07:29:50.018733
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class MyConstructor(AnsibleConstructor):
        def __init__(self):
            super(MyConstructor, self).__init__()
            self.construct_mapping = AnsibleConstructor.construct_mapping.__get__(self)

    import yaml
    yaml_data = """
a: foo
b:
  c: bar
  d: baz
  e:
    f:
      g: 1
      h:
      - one
      - two
      - three
      i: { j: 4, k: 5 }
"""
    obj = yaml.load(yaml_data, Loader=yaml.Loader)
    new_constructor = MyConstructor()
    new_obj = new_constructor.construct_mapping(obj)


# Generated at 2022-06-13 07:29:55.733738
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from collections import OrderedDict
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = {
        "key1": "value1",
        "key2": "value2",
        "key1": "value3",
        "key4": {
            "key4_1": "value4_1",
            "key4_2": "value4_2"
        }
    }
    error_key_keys = ['key1']

    # Generate some yaml data
    dumper = AnsibleDumper()
    data_yaml = dumper.dump(data)

    # Test if data remains unchanged for ANSIBLE_DUPLICATE_DICT_KEY = 'warn'
    C.DU

# Generated at 2022-06-13 07:30:06.650595
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import os
    import types
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    source_file = tmp_dir + os.sep + 'vault_test.yml'
    expected_file = tmp_dir + os.sep + 'vault_test_expected.py'
    destination_file = tmp_dir + os.sep + 'vault_test_actual.py'
    vault_password = 'test'
    open(destination_file, 'w').close()
    # Test if construct_yaml_map method returns an object of type AnsibleMapping (indirectly tested)
    assert type(AnsibleConstructor().construct_yaml_map(MappingNode())) == types.GeneratorType

test_AnsibleConstructor_construct_yaml

# Generated at 2022-06-13 07:30:15.518014
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ac = AnsibleConstructor()
    b_ciphertext_data = b"$ANSIBLE_VAULT;1.1;AES256;ansible\n31323332323230646166653732"
    b_plaintext_data = b'this is plaintext'
    vault = VaultLib(
        secrets='test/test_utils.test_vault/vaultpassword',
        context=dict(cipher='AES256')
    )
    # Test vault data with cipher identifier
    try:
        vault.decrypt(b_ciphertext_data)
    except ValueError:
        assert False

    #

# Generated at 2022-06-13 07:30:25.300293
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.vault import VaultLib

    from io import StringIO
    test_vaultlib = VaultLib(secrets=['vault_password'])

# Generated at 2022-06-13 07:30:30.305238
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test for Unicode value
    test_node = u'Test Unicode'
    node = AnsibleConstructor.construct_yaml_str(test_node)
    assert isinstance(test_node, unicode)
    assert isinstance(node, AnsibleUnicode)

    # Test for normal string value
    test_node = 'Test normal string'
    node = AnsibleConstructor.construct_yaml_str(test_node)
    assert isinstance(test_node, str)
    assert isinstance(node, AnsibleUnicode)

# Generated at 2022-06-13 07:30:35.851343
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import os

    import pytest

    from operator import attrgetter

    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode

    testcases = {
        'media_type': [
            AnsibleUnicode('application/x-redhat-package-manager'),
            AnsibleUnicode('application/x-rpm')
        ],
    }

    for key, value in testcases.items():
        node = yaml.compose(yaml.round_trip_load(yaml.round_trip_dump({key: value})))
        c = AnsibleConstructor()
        observed = c.construct_yaml_seq(next(node.value)).pop()

        assert isinstance(observed, AnsibleSequence)
        assert len(observed) == len

# Generated at 2022-06-13 07:30:45.580288
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # 1. create an instance of AnsibleConstructor
    ansible_constructor = AnsibleConstructor()
    # 2. create a node with a name of "test_node" and a value of "hello world"
    test_node = yaml.nodes.ScalarNode('test_node', 'hello world')
    # 3. call construct_yaml_str, passing test_node as a parameter
    result = ansible_constructor.construct_yaml_str(test_node)
    # 4. the result should be a string of "hello world"
    assert result == 'hello world'
    # 5. the result should be an instance of unicode, not str
    assert isinstance(result, unicode)

# Generated at 2022-06-13 07:30:50.446794
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import ansible.parsing.yaml.objects

    seq = ansible.parsing.yaml.objects.AnsibleSequence()
    yaml_str = "['item1', 'item2', 'item3']"
    node = yaml.constructor.Constructor(yaml_str).get_single_node()
    seq = AnsibleConstructor.constrtuct_yaml_seq(node)

    assert seq == ['item1', 'item2', 'item3']

# Generated at 2022-06-13 07:31:04.402403
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.objects import AnsibleMapping
    yaml_constructor = AnsibleConstructor()
    data = AnsibleMapping()
    data['testkey1'] = 42
    data['testkey2'] = 'abc'
    data['testkey3'] = [1]
    data['testkey4'] = [1,2]
    assert data == yaml_constructor.construct_mapping(None, True)

# Generated at 2022-06-13 07:31:08.941519
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from io import BytesIO
    from yaml import load
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    if not hasattr(AnsibleConstructor, 'construct_vault_encrypted_unicode'):
        raise SkipTest("construct_vault_encrypted_unicode() not implemented in AnsibleConstructor")
    vault_secrets = [ "12345" ]
    ac = AnsibleConstructor("", vault_secrets)

# Generated at 2022-06-13 07:31:19.366330
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    import yaml

    if sys.version_info[0] >= 3:
        # in python3, yaml returns unicode strings
        yaml_str = 'test'
        python_str = 'test'
    else:
        # in python2, yaml returns byte strings
        yaml_str = b'test'
        python_str = u'test'

    # Test default behavior
    yaml.BaseLoader.add_constructor(
        u'tag:yaml.org,2002:str',
        yaml.Loader.construct_yaml_str)
    default_result = yaml.load(yaml_str, Loader=yaml.BaseLoader)
    print("default_result = %s" % type(default_result))
    assert type(default_result) is str
    assert default_result

# Generated at 2022-06-13 07:31:30.010474
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    fake_args = {}
    fake_args["vault_pass"] = "ANSIBLE_VAULT_PASS_ENV_VAR"
    fake_args["vault_password_file"] = "ANSIBLE_VAULT_PASSWORD_FILE_ENV_VAR"
    vault = VaultLib(secrets=[ "ANSIBLE_VAULT_PASS_ENV_VAR", "ANSIBLE_VAULT_PASSWORD_FILE_ENV_VAR" ])
    ciphertext = vault.encrypt("this is plain text")
    encrypted_text = "!vault |\n          " + ciphertext
    yaml_text = u'''tests:
  - !unsafe \'!vault |\n          {encrypted_text}\'
'''.format(encrypted_text=encrypted_text)

# Generated at 2022-06-13 07:31:33.059097
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    a_string = 'This is a string'
    yaml_node = AnsibleConstructor.construct_yaml_str(None, a_string)
    assert isinstance(yaml_node, AnsibleUnicode)



# Generated at 2022-06-13 07:31:33.628384
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    pass

# Generated at 2022-06-13 07:31:40.389509
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml.nodes import SequenceNode
    from yaml.nodes import ScalarNode

    ansibleconstructor = AnsibleConstructor()

    seqNode = SequenceNode(u'tag:yaml.org,2002:seq', [ScalarNode(u'tag:yaml.org,2002:str', u'item1'), ScalarNode(u'tag:yaml.org,2002:str', u'item2')], start_mark=Mark(u'', 0, 0, None, None, None), end_mark=Mark(u'', 0, 0, None, None, None))
    result = list(ansibleconstructor.construct_yaml_seq(seqNode))
    assert result == [u'item1', u'item2']

# Generated at 2022-06-13 07:31:43.790320
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Run unittest
    filename = None
    constructor = AnsibleConstructor(filename)
    node = None
    ret = constructor.construct_yaml_str(node)
    assert ret == None

# Generated at 2022-06-13 07:31:52.021775
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    try:
       from yaml import load, dump
    except ImportError:
        print('Warning: yaml python library not installed')
        return

    # These are the string literals we are testing with:
    # |    Python        |     YAML     |

# Generated at 2022-06-13 07:31:57.851493
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    constructor = AnsibleConstructor()

    a = constructor.construct_mapping({
        u'a': 'abc',
        u'b': 'bcd',
        u'c': 'cde'
    })

    assert a == {
        'a': 'abc',
        'b': 'bcd',
        'c': 'cde'
    }



# Generated at 2022-06-13 07:32:22.221330
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    test_obj = AnsibleConstructor()

    data = """\
foo:
  bar: -1
  baz: 2
spam:
  - one
  - two
  - three
eggs:
  - one: uno
  - two: dos
  - three: tres
"""
    test_yaml = yaml.load(data)

    expected_dict = dict(
        foo=dict(
            bar=-1,
            baz=2,
        ),
        spam=["one", "two", "three"],
        eggs=[
                dict(one="uno"),
                dict(two="dos"),
                dict(three="tres"),
        ]
    )
    assert test_yaml == expected_dict, 'Expected AnsibleConstructor to correctly construct a yaml map'



# Generated at 2022-06-13 07:32:32.553732
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import yaml
    ansible_constructor = AnsibleConstructor()
    ansible_yaml_str1 = u'foo: 1\nbar: 1\nbaz: 3\n'
    ansible_yaml_str2 = u'foo: 1\nbar: 2\nbaz: 3\n'
    ansible_yaml_str3 = u'foo: 1\nbar: 2\nbar: 3\nbaz: 3\n'
    ansible_yaml_str4 = u'foo: 1\nbar: 2\nbar: 3\nbaz:\n  - 4\n  - 5\n'
    data1 = yaml.load(ansible_yaml_str1, Loader=yaml.BaseLoader)

# Generated at 2022-06-13 07:32:32.974414
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass

# Generated at 2022-06-13 07:32:39.515216
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import sys
    if not sys.version.startswith('3'):
        import __builtin__
        builtins = __builtin__
    else:
        import builtins
    file_name = 'foo'
    vault_secrets = None
    obj = AnsibleConstructor(file_name, vault_secrets)
    data = obj.construct_yaml_map(node='')
    for i in data:
        assert i == {}
    assert i.ansible_pos == (file_name, 1, 1)



# Generated at 2022-06-13 07:32:49.922288
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    class MyAnsibleConstructor(AnsibleConstructor):
        # since the vault object is created without a single vault password
        # this method is required to test the !unsafe tag
        def construct_vault_encrypted_unicode(self, node):
            return None

    result = MyAnsibleConstructor().construct_yaml_unsafe(MappingNode(anchor=None))
    assert result.__class__.__name__ == 'AnsibleUnsafeDict'

    result = MyAnsibleConstructor().construct_yaml_unsafe(MappingNode(anchor='foo'))
    assert result.__class__.__name__ == 'AnsibleUnsafeDict'

    result = MyAnsibleConstructor().construct_yaml_unsafe(MappingNode(anchor=u'foo'))

# Generated at 2022-06-13 07:32:53.923025
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    tag = u'!yaml/map'
    node = MappingNode(tag, None, None, True)
    ansible_constructor = AnsibleConstructor()
    assert (ansible_constructor.construct_yaml_map(node) is not None)


# Generated at 2022-06-13 07:33:01.705724
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys
    import ansible.parsing.yaml.loader

    import unittest
    from ansible.parsing.yaml.objects import AnsibleSequence

    class TestConstructYamlSeq(unittest.TestCase):
        def setUp(self):
            self.constructor = AnsibleConstructor()

        def tearDown(self):
            pass

        def test_output_type(self):
            yaml_text = '''
            - a
            - b
            - c
            '''
            data = ansible.parsing.yaml.loader.load(yaml_text)

            seq = self.constructor.construct_yaml_seq(data)


# Generated at 2022-06-13 07:33:10.983001
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_doc = '''
    test_dict:
        foo: bar
        bar: baz
        lst:
            - a
            - b
        dct:
            foo: bar
            bar: baz
    '''

    from ansible.parsing.yaml.loader import AnsibleLoader
    data = AnsibleLoader(test_doc).get_single_data()

    assert data.ansible_pos[0] == '<unicode string>'
    assert data.ansible_pos[1] == 1
    assert data.ansible_pos[2] == 0

    assert data['test_dict'] is not None
    assert data['test_dict'].ansible_pos[0] == '<unicode string>'
    assert data['test_dict'].ansible_pos[1] == 2
   

# Generated at 2022-06-13 07:33:25.041041
# Unit test for method construct_mapping of class AnsibleConstructor

# Generated at 2022-06-13 07:33:32.962198
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import os
    import sys
    import pytest
    sys.path.append(os.path.dirname(__file__))
    from fixtures.yaml_map import yaml_dict, ansible_dict

    constructor = AnsibleConstructor()
    ansible_dict_output = AnsibleMapping(constructor.construct_yaml_map(yaml_dict))
    assert ansible_dict == ansible_dict_output
    ansible_dict_output.ansible_pos = ('test.yaml', 3, 1)
    ansible_dict.ansible_pos = ('test.yaml', 3, 1)
    assert ansible_dict == ansible_dict_output


# Generated at 2022-06-13 07:34:18.619903
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node = MappingNode(tag=u'tag:yaml.org,2002:map',
                       value=[
                           ([u'uniq-1', u'uniq-2'], [u'value-1', u'value-2']),
                           ([u'uniq-1', u'uniq-3'], [u'value-3', u'value-4'])],
                       start_mark=None, end_mark=None)
    ret = AnsibleConstructor.construct_mapping(node, deep=False)
    assert isinstance(ret, AnsibleMapping)
    assert ret == dict(uniq_1='value-3', uniq_2='value-2', uniq_3='value-4')

# Generated at 2022-06-13 07:34:27.866727
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    ##
    ## Test that we raise a ConstructorError when we encounter a duplicate dict
    ##

    import io
    import yaml

    # define a yaml dump for the source data for testing the method construct_mapping
    source_data = '''
    key1: value1
    key2: value2
    key1: value3
    '''
    stream = io.StringIO(source_data)

    # instantiate an object of class AnsibleConstructor
    constructor = AnsibleConstructor()
    loader = yaml.Loader(stream)
    loader.constructor = constructor

    # PyYAML silently allows overwriting keys, but we don't want to.
    # With the below call, we make sure that when a user enters a duplicate
    # dict key, the constructor will raise an exception.

# Generated at 2022-06-13 07:34:37.069689
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # let's test that AnsibleConstructor.construct_mapping raises the right exceptions
    def _construct_mapping(node):
        ac = AnsibleConstructor()
        ac.construct_mapping(node)

    # let's test that we raise the right exception when the node is None
    import pytest
    with pytest.raises(Exception) as excinfo:
        _construct_mapping(None)
    assert 'while constructing a mapping' in str(excinfo.value)

    # let's test that we raise the right exception when the node is not a MappingNode
    with pytest.raises(Exception) as excinfo:
        _construct_mapping('not a MappingNode')
    assert 'expected a mapping node' in str(excinfo.value)

    # let's test that we raise the right exception when the node key is not

# Generated at 2022-06-13 07:34:47.608820
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultAES256CBC

    vault_secrets = [VaultSecret('password')]
    vault_lib = VaultLib(secrets=vault_secrets)
    vault_str = '!' + '!vault-encrypted' + ' |' + '\n' + \
                vault_lib.encrypt('This is a test.') + '\n'
    ac = AnsibleConstructor(vault_secrets=[vault_secrets])
    ansible_vault_encrypted_unicode = ac.construct_yaml_unsafe(vault_str)

# Generated at 2022-06-13 07:34:57.567863
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from os import path
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.unsafe_proxy import wrap_var
    import yaml


# Generated at 2022-06-13 07:35:02.842479
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Testing with ASCII string
    value = u'123'
    node = u'tag:yaml.org,2002:str'
    ret = AnsibleConstructor().construct_yaml_str(value, node)
    assert ret.ansible_pos[0] == '<unicode string>'
    assert ret.ansible_pos[1] == 1
    assert ret.ansible_pos[2] == 1
    assert ret.ansible_type == u'AnsibleUnicode'

    # Testing with empty string
    value = u''
    node = u'tag:yaml.org,2002:str'
    ret = AnsibleConstructor().construct_yaml_str(value, node)
    assert ret.ansible_pos[0] == '<unicode string>'

# Generated at 2022-06-13 07:35:10.628092
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    display.display = mock.Mock()
    ac = AnsibleConstructor()
    node = mock.Mock()
    node.start_mark.column = 1
    node.start_mark.line = 2
    node.start_mark.name = 'test'
    node.start_mark.buffer = None
    node.start_mark.pointer = None
    assert ac.construct_yaml_str(node) == 'test'
    assert ac.construct_yaml_str(node).ansible_pos == ('test', 2, 1)
    assert ac.construct_yaml_str(node).ansible_pos == ('test', 2, 1)
    node.start_mark.column = 1
    node.start_mark.line = 2
    node.start_mark.name = 'test2'

# Generated at 2022-06-13 07:35:18.662775
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    """
    Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
    :return:
    """
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    import os


# Generated at 2022-06-13 07:35:29.315137
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from yaml import nodes
    from yaml.parser import Parser
    from yaml import scanner

    node_class_name = 'ScalarNode'
    value = 'value'
    tag = u'tag:yaml.org,2002:str'
    mock_node = nodes.ScalarNode(tag, value)

    yaml_constructor = AnsibleConstructor()

    result = yaml_constructor.construct_yaml_str(mock_node)
    assert isinstance(result, AnsibleUnicode)
    assert result == value



# Generated at 2022-06-13 07:35:37.537232
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = [ 'test' ]
    constructor = AnsibleConstructor(file_name='test_filename', vault_secrets=vault_secrets)
    # 0. No node
    parsed = constructor.construct_vault_encrypted_unicode(None)
    assert parsed is None
    # 1. Node without value
    node = MockNode(None)
    parsed = constructor.construct_vault_encrypted_unicode(node)
    assert parsed.vault.secrets == vault_secrets
    assert parsed.encrypted_text is None
    # 2. Node with value
    value = "bla"
    node = MockNode(value)
    parsed = constructor.construct_vault_encrypted_unicode(node)
    assert parsed.vault.secrets == vault_secrets
    assert parsed.encrypted_text == value


# Generated at 2022-06-13 07:36:46.436859
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    import os
    import tempfile
    import shutil
    import textwrap
    from ansible.parsing.yaml import objects
    import sys
    import os
    import stat
    import getpass
    import tempfile
    import textwrap
    import yaml
    import hashlib
    import binascii
    import base64
    import pprint
    import json
    import tempfile
    import stat
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml import objects
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultEditor
    from ansible.parsing.yaml import AnsibleLoader

# Generated at 2022-06-13 07:36:53.001779
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import os
    import unittest
    import tempfile

    # Initialize vault
    vault_pass_file = tempfile.NamedTemporaryFile()
    vault_pass_file.write(to_bytes("test_password"))
    vault_pass_file.flush()
    vault = VaultLib(vault_pass_file.name, 'sha256')
    vault_pass_file.close()
    vault_pass_file = None

    # Create encrypted_content
    encrypted_content = vault.encrypt(b"plaintext")

    # Initialize AnsibleConstructor
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.vault_secrets = [vault_pass_file]

    # Test if decrypt works


# Generated at 2022-06-13 07:36:57.886924
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.utils.unsafe_proxy import unwrap_var

    import types

    # use the vault password 'ansible'
    # Note: this test case will fail if the vault password is changed
    import os
    my_path = os.path.abspath(os.path.dirname(__file__))

# Generated at 2022-06-13 07:37:10.691124
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    """
    Test the method 'construct_yaml_seq' of the class'AnsibleConstructor'
    """

    try:
        from yaml import Loader
    except ImportError:
        from yaml import Loader
    from yaml.nodes import Node

    # create an object to load construct and return it
    ans_construct = AnsibleConstructor()
    ans_construct.construct_yaml_seq(None)

    # ans_construct.construct_yaml_seq(None)
    # a_seq = AnsibleSequence()
    # a_seq.extend(ans_construct.construct_sequence(None))
    # a_seq.ansible_pos = ans_construct._node_position_info(None)
    # ans_construct.construct_yaml_seq(None) == a_seq
    # ans_

# Generated at 2022-06-13 07:37:14.986743
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    node = object()
    safe_constructor = AnsibleConstructor()
    safe_constructor.construct_object = lambda node: node.data
    with wrap_var(node, 'shiny'):
        data = safe_constructor.construct_yaml_unsafe(node)

    assert data == 'shiny'

# Generated at 2022-06-13 07:37:18.529943
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
  y = '''
a:
  b: test
  c: 3
'''
  yaml_data = yaml.load(y, Loader=AnsibleConstructor)
  assert yaml_data['a']['b'] == u'test'
  assert yaml_data['a']['c'] == 3


# Generated at 2022-06-13 07:37:30.065332
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Setup
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=[], flow_style=None)
    ansible_constructor = AnsibleConstructor()
    deep = False

    # Exercise
    mapping = ansible_constructor.construct_mapping(node, deep)
    # Verify
    assert isinstance(mapping, dict)

    # Initialize a mapping node with some value

# Generated at 2022-06-13 07:37:34.285340
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    nodes_list = [{1:2, 3:4}, {1:2, 3:4, 5:6}, {1:2, 3:4, 1:5}]
    for nodes in nodes_list:
        for key in nodes.keys():
            if key == 1:
                assert False
        assert True

# Generated at 2022-06-13 07:37:43.692449
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = '''
---
str:
  a: foo
  b: bar
  c:
    - 1
    - 2
    - 3
    - 4
  d: |
      this is
      a block
      string
    '''

    loader = AnsibleLoader(data, None)
    for k, v in loader.get_single_data().items():
        assert isinstance(k, AnsibleUnicode)
        assert isinstance(v, AnsibleMapping)
        for k2, v2 in v.items():
            assert isinstance(k2, AnsibleUnicode)
            if k2 == 'd':
                assert isinstance(v2, AnsibleUnicode)

# Generated at 2022-06-13 07:37:57.956652
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    import yaml
    import sys
    import os
