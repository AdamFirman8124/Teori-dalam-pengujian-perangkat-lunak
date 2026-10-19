

# Generated at 2022-06-13 07:28:13.838202
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    # test a python class
    class Toto: pass
    data = yaml.safe_load(yaml.dump({ 'a': Toto() }))
    assert data.get('a', None) is not None

    # test an object
    data = yaml.safe_load(yaml.dump({ 'a': { 'b': 'c' } }))
    assert data.get('a', None) is not None

    # test a list
    data = yaml.safe_load(yaml.dump({ 'a': [ 1, 2, 3 ] }))
    assert data.get('a', None) is not None

    # test a string
    data = yaml.safe_load(yaml.dump({ 'a': 'b' }))
    assert type(data.get('a', None)) == str

# Generated at 2022-06-13 07:28:25.258241
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Test ansible constructor with correct value
    correct_data_str = '''--- a_string'''
    correct_data_str_expected = AnsibleUnicode('a_string')
    _, data_str = yaml.load(correct_data_str, AnsibleConstructor)
    assert data_str == correct_data_str_expected

    # Test ansible constructor with incorrect value
    incorrect_data_str = '''--- children'''
    incorrect_data_str_expected = AnsibleUnicode()
    _, data_str = yaml.load(incorrect_data_str, AnsibleConstructor)
    assert data_str == incorrect_data_str_expected

    # Test ansible constructor with correct value

# Generated at 2022-06-13 07:28:28.343133
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    c = AnsibleConstructor()
    node = c.construct_yaml_map({'name': 'John Doe'})
    assert len(node) == 1
    assert 'name' in node
    assert node.name == 'John Doe'



# Generated at 2022-06-13 07:28:30.666871
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    test = AnsibleConstructor()

    node = None
    data = test.construct_yaml_map(node)
    assert data is not None


# Generated at 2022-06-13 07:28:34.904724
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml import datatype
    import yaml

    input_data = """
    key1: value
    key2: value
    key1: value
    """

    safe_constructor = datatype.AnsibleConstructor.construct_mapping
    safe_loader = yaml.SafeLoader(input_data)

    assert safe_constructor(safe_loader)['key1'] == 'value'

# Generated at 2022-06-13 07:28:40.578549
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    string = u"""
---
- 1
- 2
- 3
"""
    result = AnsibleConstructor(file_name='/tmp/test').construct_yaml_seq(yaml.nodes.MappingNode('', [yaml.nodes.SequenceNode('', [yaml.nodes.ScalarNode('', '1'), yaml.nodes.ScalarNode('', '2'), yaml.nodes.ScalarNode('', '3')])], []))
    assert next(result) == AnsibleSequence([1, 2, 3])



# Generated at 2022-06-13 07:28:54.701824
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader
    constructor = AnsibleConstructor()
    yaml_str = u'a: b\nc: d'
    data = AnsibleLoader(yaml_str, constructor).get_single_data()
    assert data == {u'a': u'b', u'c': u'd'}
    yaml_str = u'a: b\nc: d\na: f\n'

# Generated at 2022-06-13 07:29:01.462758
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing import vault
    yaml_map_text = b"""
foo: bar
baz:
   - qux
   - corge
""".strip()

    vault_secret = vault.VaultSecret('sekrit', b'sekrit')
    vault_secrets = [vault_secret]
    vault_mock = mock.MagicMock(VaultLib)


# Generated at 2022-06-13 07:29:06.483105
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    node = MappingNode(anchor=None, tag=u'!vault', value=[], start_mark=1, end_mark=2)
    value = AnsibleConstructor.construct_vault_encrypted_unicode(node)
    assert value



# Generated at 2022-06-13 07:29:09.484596
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    assert isinstance(AnsibleConstructor().construct_mapping(None), AnsibleMapping)

# Generated at 2022-06-13 07:29:21.396885
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    test_string = "Ansible Constructor"

    # Create a node object
    node_obj = {'tag': 'tag:yaml.org,2002:python/unicode', 'value': test_string}

    # Create a object of class AnsibleConstructor
    construct_obj = AnsibleConstructor()

    # Call the method construct_yaml_str
    construct_method = construct_obj.construct_yaml_str(node_obj)

    assert test_string == construct_method

# Generated at 2022-06-13 07:29:28.114844
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()
    seq_test_data = """
- one
- two
- three
-
  - one
  - two
  - three
"""
    actual_result = constructor.construct_yaml_seq(seq_test_data)
    expected_result = [u'one', u'two', u'three', [u'one', u'two', u'three']]
    assert expected_result == actual_result

# Generated at 2022-06-13 07:29:28.499798
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    pass

# Generated at 2022-06-13 07:29:30.523993
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    c = AnsibleConstructor()
    assert c.construct_yaml_seq() == c.construct_yaml_seq()

# Generated at 2022-06-13 07:29:36.958398
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_object = AnsibleConstructor()
    result = test_object.construct_mapping(MappingNode(node='node', tag=u'tag:yaml.org,2002:map', value=[(u'tag:yaml.org,2002:str', u'a')], start_mark=None, end_mark=None, flow_style=None))
    assert result == {u'a': None}

# Generated at 2022-06-13 07:29:45.880619
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    collect_all = True  # collect all the values into a list
    collect_single = False  # collect only the first value from YAML mapping
    collect_concat = False  # collect only the concatenated values from YAML mapping
    collect_non_dict = True  # collect only non-dict values from YAML mapping
    collect_none = False  # collect all the values from YAML mapping and remove None from the list
    collect_replace_dict = False  # collect all the values into a list and replace the dict with its values
    display.verbosity = 3
    node, deep = None, False

    # Testing examples with duplicate_yaml_dict_key=error
    C.DUPLICATE_YAML_DICT_KEY = 'error'

    # Testing with collect_all=True
    data = AnsibleConstructor

# Generated at 2022-06-13 07:29:52.262640
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnicode

    secret = 'Hello World'
    vault_secrets = {'default': secret}

# Generated at 2022-06-13 07:29:55.286941
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    test_object = AnsibleConstructor()
    # setup test args
    node = None
    # invoke method under test
    test_return = test_object.construct_vault_encrypted_unicode(node)
    # verify results



# Generated at 2022-06-13 07:30:06.394585
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    class TestAnsibleConstructor_construct_vault_encrypted_unicode(unittest.TestCase):
        def setUp(self):
            self.vault = VaultLib([b'123'])

# Generated at 2022-06-13 07:30:15.277215
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:30:21.742968
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    node = MappingNode(tag='tag:yaml.org,2002:map', value=['key', 'value'], flow_style=True)
    ac = AnsibleConstructor()
    ret = ac.construct_yaml_map(node)
    assert isinstance(ret, AnsibleMapping)

# Generated at 2022-06-13 07:30:29.693191
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # Create an encrypted data
    vault = VaultLib(vault_secrets=['abc'])
    ciphertext_data= vault.encrypt('A dummy string')

    # Create an Ansible Constructor with the same vault secret and construct a vault-encrypted string
    ansible_constructor = AnsibleConstructor(file_name='/file/name', vault_secrets=['abc'])

    # Create a YAML node. Note that it is a "scalar node", which doesn't contain chilren
    node = to_bytes(yaml.nodes.ScalarNode(tag='!vault-encrypted', value=ciphertext_data))

    # Call the function and verify the result
    result = ansible_constructor.construct_vault_encrypted_unicode(node)

    # Verify the type of the result

# Generated at 2022-06-13 07:30:35.954205
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    try:
        from yaml import CSafeLoader as Loader
    except ImportError:
        # in case libyaml is not installed
        from yaml import SafeLoader as Loader

    data = b"""
- foo: bar
"""

    loader = Loader(data)
    loadeddata = loader.get_single_data()

    assert loadeddata[0].foo == AnsibleUnicode('bar')

# Generated at 2022-06-13 07:30:40.336700
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    vault_secrets = ['mysecret1', 'mysecret2', 'mysecret3']

    c = AnsibleConstructor(vault_secrets=vault_secrets)

# Generated at 2022-06-13 07:30:48.255795
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    sequence = """
    - item: 1
    - item: 2
    - item: 3
    """
    yaml = YAML(typ='safe')
    data = yaml.load(sequence)
    assert isinstance(data, AnsibleSequence)
    assert isinstance(data[0], AnsibleMapping)
    assert isinstance(data[1], AnsibleMapping)
    assert isinstance(data[2], AnsibleMapping)
    assert data[0]['item'] == '1'
    assert data[1]['item'] == '2'
    assert data[2]['item'] == '3'

# Generated at 2022-06-13 07:30:58.368808
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml.loader import AnsibleLoader

    SAMPLE_YAML = '''
    a: 1
    b: 2
    a: 3
    '''
    SAMPLE_YAML_DICT_KEY_ERROR = '''
    a: 1
    b: 2
    a: 3
    d: 1
    e: 2
    f: 3
    a: 4
    '''

    if C.DUPLICATE_YAML_DICT_KEY == 'error':
        expected_dict = {u'a': 3, u'b': 2}
    else:
        expected_dict = {u'a': 4, u'b': 2, u'd': 1, u'e': 2, u'f': 3}


# Generated at 2022-06-13 07:31:06.536784
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    yaml_src = '''
- foo: 1
- bar: 2
- baz: 3
'''.lstrip()
    ansible_constructor = AnsibleConstructor()

    # Check return type of construct_yaml_str()
    node = yaml.compose(yaml_src, Loader=yaml.SafeLoader)
    ret = ansible_constructor.construct_yaml_str(node.value[0].value[0])
    assert(isinstance(ret, AnsibleUnicode))

    # Check return type of construct_yaml_str()
    node = yaml.compose(yaml_src, Loader=yaml.SafeLoader)
    ret = ansible_constructor.construct_yaml_str(node.value[0].value[1])

# Generated at 2022-06-13 07:31:18.125080
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    yaml_data = """
    ok:
      - name: '{{ name }}'
        test: '{{ test }}'
    """
    data = yaml.load(yaml_data, AnsibleConstructor)
    assert str(data.keys()[0]) == "ok"
    assert str(data["ok"].__class__) == "<class 'ansible.parsing.yaml.objects.AnsibleSequence'>"
    assert str(data["ok"][0].__class__) == "<class 'ansible.parsing.yaml.objects.AnsibleMapping'>"

# Generated at 2022-06-13 07:31:24.523289
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    """
    _test_AnsibleConstructor_construct_mapping unit tests the construct_mapping()
    of the AnsibleConstructor class.
    """
    from yaml.composer import Composer
    from yaml.parser import Parser
    from yaml.scanner import Scanner

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.vault import VaultSecret

    prompt = 'test'
    vault_password = 'secret'
    password = VaultSecret(vault_password).data

    # Note, these values must be escaped for YAML.
    # We want the key names to contain all special characters because those
    # were the original motivation for creating this custom constructor function.

# Generated at 2022-06-13 07:31:33.915263
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_data = '''
    foo: bar
    baz:
      - item1
      - item2
      - item3
    meh:
      - name: alpha
        value: beta
      - name: gamma
        value: delta
    '''

    yaml_obj = yaml.load(test_data, Loader=AnsibleConstructor)
    print(yaml_obj)
    # prints:
    # {'foo': 'bar', 'baz': ['item1', 'item2', 'item3'],
    # 'meh': [{'value': 'beta', 'name': 'alpha'},
    #         {'value': 'delta', 'name': 'gamma'}]}


import unittest


# Generated at 2022-06-13 07:31:43.289029
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    pass



# Generated at 2022-06-13 07:31:51.793348
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import StringIO, BytesIO
    import sys

    assert sys.version_info >= (2, 7)

    yamldata_in = '''
- 1
- 2
- 3
'''

    yamldata_out = '''\
- 1
- 2
- 3
'''

    results = AnsibleLoader(BytesIO(yamldata_in.encode('utf-8')), 'test_file_name').get_single_data()
    assert isinstance(results, AnsibleSequence)
    assert len(results) == 3

# Generated at 2022-06-13 07:32:06.173605
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest

    class TestPlugin(unittest.TestCase):
        def setUp(self):
            self.secret = '$ANSIBLE_VAULT;1.1;AES256\n363063326637333862333163386636616633306132323230653533663763626261623463616266\n306566373738653365353331333236336133653738363330393930346536623861653734643639\n353261366131646232383864623865346663326262393638653266653630666430656564343066\n35396500\n'

        def test_decrypt(self):
            vault = VaultLib(secrets=[self.secret])

# Generated at 2022-06-13 07:32:07.108869
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    assert "hello" == AnsibleConstructor().construct_yaml_str('')

# Generated at 2022-06-13 07:32:13.049969
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import ansible.parsing.yaml.loader as yaml_loader
    helper_msg = "Test helper"

# Generated at 2022-06-13 07:32:21.757404
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class TestAnsibleConstructor(AnsibleConstructor):
        def __init__(self):
            super(TestAnsibleConstructor, self).__init__()
            self.value = None

        def construct_object(self, node, deep=False):
            self.value = node.value

    node = MappingNode(tag='tag:yaml.org,2002:map', value=[('key', 'value')],
                       start_mark=None, end_mark=None)
    test_constructor = TestAnsibleConstructor()
    test_constructor.construct_mapping(node)

    assert 'key' == test_constructor.value
    assert 'value' == test_constructor.construct_object(node)

# Generated at 2022-06-13 07:32:32.101261
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = ['123']
    vault_file_name = "/dev/null"
    v = VaultLib(vault_secret=vault_secrets)

# Generated at 2022-06-13 07:32:37.656339
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml
    yaml_unsafe = '''\
reserved: !unsafe "{{ lookup('template', './template.j2') }}"
null: !unsafe "null"
true: !unsafe "true"
false: !unsafe "false"
empty: !unsafe ""
'''
    obj = yaml.load(yaml_unsafe, Loader=AnsibleConstructor)
    assert obj == {
        'reserved': wrap_var('{{ lookup(\'template\', \'./template.j2\') }}'),
        'null': wrap_var('null'),
        'true': wrap_var('true'),
        'false': wrap_var('false'),
        'empty': wrap_var(''),
    }

# Generated at 2022-06-13 07:32:48.588082
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    data = AnsibleConstructor().construct_yaml_seq(yaml.nodes.SequenceNode(tag=u'tag:yaml.org,2002:seq', value=[
        yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'item1'),
        yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'item2'),
        yaml.nodes.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'item3'),
    ]))

    assert data.ansible_pos == (None, 1, 1)
    assert data == [u'item1', u'item2', u'item3']

# Unit test

# Generated at 2022-06-13 07:32:53.891350
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:33:24.535997
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import sys
    from io import StringIO
    from yaml import load
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    in_str = StringIO("""\
        a: abc
        b: 45
        c: 123
        d: !str def
        e: [abc]
        """)

    in_str.name = '<string>'
    setattr(in_str, 'name', '<string>')

    yaml_data = load(in_str, Loader=AnsibleLoader)

    assert isinstance(yaml_data['a'], AnsibleUnicode)
    assert isinstance(yaml_data['b'], AnsibleUnicode)

# Generated at 2022-06-13 07:33:29.653389
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    data = '''
- keya: valuea
- keyb: valueb
- keyc: valuec
'''
    map_obj = yaml.load(data, Loader=AnsibleConstructor)

    assert isinstance(map_obj, AnsibleSequence), 'Expect an AnsibleSequence'
    assert len(map_obj) == 3, "Expect three items"

# Generated at 2022-06-13 07:33:41.053406
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    AnsibleConstructor.add_constructor(
        u'tag:yaml.org,2002:float',
        AnsibleConstructor.construct_yaml_str)

    node = AnsibleDumper.represent_data({
        'name': 'bob',
        'age': 22.2,
        'nested': {
            'data': 22.2
        }
    })

    cons = AnsibleConstructor()

    # make sure it works
    data = cons.construct_yaml_map(node)

    # check that the ansible_pos attribute was added
    assert hasattr(data, 'ansible_pos')

    # check the value of ansible_pos

# Generated at 2022-06-13 07:33:51.022212
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor

# Generated at 2022-06-13 07:34:01.129185
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import sys, os, tempfile

    (fd, test_file_name) = tempfile.mkstemp(suffix='.yml', prefix='AnsibleConstructor_construct_yaml_seq_test')
    test_file = os.fdopen(fd, 'w')

    test_file.write('["a","a"]\n')
    test_file.close()

    ac = AnsibleConstructor()

    from yaml.nodes import SequenceNode
    import yaml

    eg = yaml.load(open(test_file_name, 'r'))
    ne = ac.construct_yaml_seq(SequenceNode('tag:yaml.org,2002:seq', [], None))
    for v in eg:
        ne.next()
    ne.next()
    assert eg == list(ne)

   

# Generated at 2022-06-13 07:34:03.873864
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    ansible_constructor = AnsibleConstructor()
    ansible_constructor.construct_yaml_str()

# Generated at 2022-06-13 07:34:10.472883
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    assert isinstance(AnsibleConstructor.construct_yaml_str(None), AnsibleUnicode)

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 07:34:15.269025
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    yaml_key_values = """
a: 1
b: 2
c: 3
"""
    node = MappingNode(tag=u'tag:yaml.org,2002:map', value=yaml_key_values)
    deep = False
    asc = AnsibleConstructor('a')
    asc.construct_mapping(node, deep)

# Generated at 2022-06-13 07:34:24.625713
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils import context_objects as co

    # Use specified file name and line number values
    test_filename = 'testfile'
    line_number = 100
    node_start_mark = co.Mark(test_filename, None, line_number, None, None, None)
    test_node = co.Node(None, None, [(None, None)], None, None, None, node_start_mark, None, None)

    # Create an instance of AnsibleConstructor
    a = AnsibleConstructor()

    # Test expected execution path
    # Expected value is a subclass of unicode
    actual = a.construct_yaml_str(test_node)
    assert isinstance(actual, AnsibleUnicode)

# Generated at 2022-06-13 07:34:29.253505
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    text = '''
- aaa
- bbb
'''

    data = yaml.load(text, Loader=AnsibleConstructor)

    assert isinstance(data, list)
    assert data[0] == 'aaa'
    assert data[1] == 'bbb'



# Generated at 2022-06-13 07:35:08.662708
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from yaml import load
    from ansible.parsing.yaml.objects import AnsibleMapping

    data = '''
    - a
    - b
    - c
    '''

    constructor = AnsibleConstructor()
    seq = constructor.construct_yaml_seq(load(data))

    assert len(seq) == 3
    assert seq == ['a', 'b', 'c']
    assert type(seq) == AnsibleSequence
    assert seq.ansible_pos == ('<unicode string>', 1, 0)


# Generated at 2022-06-13 07:35:16.079329
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import yaml
    vault_password = "foo"
    vault_id = "default"
    vault_secrets = [ { "id": vault_id, "password": vault_password } ]
    constructor = AnsibleConstructor(vault_secrets=vault_secrets)

    vault = VaultLib(vault_password)
    ciphertext_data = vault.encrypt("bar")
    vault_yaml = "!vault |\n{0}".format(ciphertext_data.decode('utf-8'))
    data = yaml.load(vault_yaml, Loader=constructor)
    assert data.vault == vault
    assert data == "bar"

# Generated at 2022-06-13 07:35:27.811584
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
  import yaml
  import ansible.parsing.yaml.objects

  real_vault_secrets = [ b'$ANSIBLE_VAULT;1.1;AES256', b'653137616536613262633163393362313462316230646631636364333832643835653038373463' ]
  vault = ansible.parsing.vault.VaultLib(vault_secrets=real_vault_secrets)

# Generated at 2022-06-13 07:35:35.683006
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import collections
    import datetime
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.utils.unsafe_proxy import wrap_var
    dl = DataLoader()

    data = dl.load_from_file('test/utils/yaml/data/construct_yaml_unsafe.yaml')

    # Tests to see that the data is actually a Proxy object
    assert type(data) is dict
    assert type(data['boolean_constant']) is wrap_var.Proxy
    assert type(data['datetime_object']) is wrap_var.Proxy

    # Tests to see that the value matches the original
    assert data['boolean_constant'].value is True

    # Tests to see that the value matches the

# Generated at 2022-06-13 07:35:41.569970
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Tests with dictionaries containing duplicate keys will not raise an exception.
    # The exception is caught in AnsibleConstructor._node_position_info and a warning
    # is added if DUPLICATE_YAML_DICT_KEY is set to 'warn' in constants.py
    yaml_str = "--- \nhello: world\nhello: ansible"
    AnsibleConstructor().construct_yaml(yaml_str)
    yaml_str = "---\n{hello: world, hello: ansible}"
    AnsibleConstructor().construct_yaml(yaml_str)
    yaml_str = "---\n{hello: world, hello: ansible, hello: world}"
    AnsibleConstructor().construct_yaml(yaml_str)

# Generated at 2022-06-13 07:35:52.979552
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import unittest
    import yaml

    class mock_Display(object):
        def __init__(self):
            self.warn = self.info = self.debug = lambda x: None
        def display(self, msg, color=None, stderr=False, screen_only=False):
            print(msg)

    # test without vault secret
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 07:36:04.086951
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    import yaml

    data = (
        u'#Value example 1\n'
        u'{#Value example 1\n'
        u'1: one\n'
        u'2: two\n'
        u'}#Value example 1\n'
        u'#Value example 2\n'
        u'{#Value example 2\n'
        u'1: test1\n'
        u'2: test2\n'
        u'}#Value example 2\n'
    )

    constructor = AnsibleConstructor(file_name='source file context')
    yaml_stream = yaml.load_all(data, Loader=yaml.Loader)
    for mapping in yaml_stream:
        # Construct yaml_seq from mapping
        mapping_obj = constructor.construct_yaml_seq

# Generated at 2022-06-13 07:36:16.216795
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import os

    if not os.path.exists("/usr/lib/python2.7/site-packages/pyYAML-3.11-py2.7-linux-x86_64.egg/ansible/parsing/vault"):
        print("Skipping test_AnsibleConstructor_construct_vault_encrypted_unicode, not implemented yet")
        return 0
    else:
        print("Testing test_AnsibleConstructor_construct_vault_encrypted_unicode")

    vault_password_file = os.path.join(os.path.dirname(__file__), 'vault_test_file')

# Generated at 2022-06-13 07:36:19.616212
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    yaml = """
foo:
  bar: baz
"""
    data = yaml_loads(yaml)
    assert isinstance(data, AnsibleMapping)
    data.ansible_pos = ('doc.yaml', 1, 2)
    assert data == {'foo': {'bar': 'baz'}}

# Generated at 2022-06-13 07:36:24.333569
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    data = {'a': 1, 'b': 2}
    data_dupe_key = {'a': 1, 'a': 2}
    map_obj = AnsibleConstructor.construct_mapping(data)
    map_dupe_key_obj = AnsibleConstructor.construct_mapping(data_dupe_key)

    assert isinstance(map_obj, AnsibleMapping)
    assert isinstance(map_dupe_key_obj, AnsibleMapping)
    assert len(map_dupe_key_obj) == 1
    assert len(map_obj) == 2

# Generated at 2022-06-13 07:37:37.872923
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    import os
    import unittest
    import yaml
    import tempfile

    class AnsibleConstructor_Test(unittest.TestCase):

        def setUp(self):
            self.vault_secrets = ['1kQkydhr6UwVJUzJe6ZNWA7ZuNllFxVlCg9RfGu/14I=']

        def test_construct_vault_encrypted_unicode_1(self):
            """Test that an AnsibleVaultEncryptedUnicode is returned when constructing an encrypted string"""

            # Generate an encrypted string for testing
            test_string = 'test string 1'
            test_file_1, test_file_name_1 = tempfile.mkstemp(suffix='.yml')

# Generated at 2022-06-13 07:37:47.939923
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class Foo(object):
        pass
    import sys
    from io import StringIO
    from yaml import SafeLoader, nodes

    class TestError(Exception):
        pass

    class Constructor(SafeConstructor):
        def construct_yaml_map(self, node):
            data = Foo()
            yield data
            value = self.construct_mapping(node)
            setattr(data, 'foo', value)

        def construct_mapping(self, node, deep=False):
            if isinstance(node, nodes.MappingNode):
                self.flatten_mapping(node)
            else:
                raise TestError('not a MappingNode')
            mapping = {}

            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                value

# Generated at 2022-06-13 07:37:54.364396
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Test scalar usage
    node = AnsibleConstructor.construct_yaml_seq('>-\nsome scalar value')
    assert next(node) == []
    assert next(node) == ['some scalar value']

    # Test with a sequence
    node = AnsibleConstructor.construct_yaml_seq('>-\na: b\nc: d')
    assert next(node) == []
    assert next(node) == ['a: b', 'c: d']

    # Test with an empty sequence
    node = AnsibleConstructor.construct_yaml_seq('>-\n')
    assert next(node) == []
    assert next(node) == []

# Generated at 2022-06-13 07:38:01.412240
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    print('Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor')
    vault_pwd = 'my_secret'
    if isinstance(vault_pwd, str):
        vault_pwd = vault_pwd.encode('utf-8')

    # Decrypt using AnsibleConstructor.construct_vault_encrypted_unicode()
    ac = AnsibleConstructor()
    ac.vault_secrets = [vault_pwd]