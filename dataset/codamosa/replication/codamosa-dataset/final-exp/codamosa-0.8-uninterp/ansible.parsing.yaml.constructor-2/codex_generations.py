

# Generated at 2022-06-13 07:28:11.808885
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml = '''
    - hosts: localhost
      tasks:
        - shell: !unsafe
          command: "{{ 'hello world' }}"
    '''
    data = AnsibleLoader(yaml, file_name='(none)').get_single_data()
    assert repr(data) == "[{'tasks': [{'shell': {'command': '{{ ansible_unsafe_proxy.mixed() }}'}}], 'hosts': 'localhost'}]"


# Generated at 2022-06-13 07:28:23.183574
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    class TestClass:

        def __init__(self):
            self.stdout = False

        def construct_mapping(self, node, deep=False):
            mapping = AnsibleMapping()
            mapping.ansible_pos = self.ansible_pos
            return mapping

        def test_construct_mapping(self):
            self.ansible_pos = ('test.yml', 1, 1)

            # Test a normal mapping
            yaml_mapping = AnsibleMapping()
            yaml_mapping['key1'] = 'value1'
            yaml_mapping['key2'] = 'value2'

            mapping = self.construct_mapping(yaml_mapping)

            # Test that the ansible_pos is equal
            assert mapping.ansible_pos == self.ansible_pos

            # Test that

# Generated at 2022-06-13 07:28:32.390840
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    '''Unit test for method construct_yaml_unsafe of class AnsibleConstructor'''
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleUnsafeText, _AnsibleUnsafeLoader

    # Fake token
    class FakeToken(object):
        def __init__(self):
            self.start_mark = FakeMark()
            self.value = 'FakeToken'
        def __repr__(self):
            return "FakeToken(%s)" % self.value

    # Fake mark
    class FakeMark(object):
        def __init__(self):
            self.line = 1
            self.column = 1
            self.name = 'FakeMark'

    #

# Generated at 2022-06-13 07:28:40.429083
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets = None
    ansible_constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    node = AnsibleMapping(value=((AnsibleUnicode("!vault-encrypted"), AnsibleUnicode("dummy")),))
    try:
        ansible_constructor.construct_vault_encrypted_unicode(node)
    except ConstructorError as exc:
        assert exc.problem == 'found !vault but no vault password provided'
    ansible_constructor.vault_secrets = ['VAULT_PASS']

# Generated at 2022-06-13 07:28:49.094576
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    dict_in = {u"a": u"b"}
    node = MappingNode(u'a', [
        (u"a", u"b"),
    ], dict_in, dict_in.start_mark, dict_in.end_mark)

    constructor = AnsibleConstructor()

    first = next(constructor.construct_yaml_seq(node))

    for idx, item in enumerate(first):
        assert item == dict_in[idx]

# Generated at 2022-06-13 07:28:57.795323
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    import sys
    import io

    test_yaml = """
    ---
    foo: bar
    bar: foo
    foobar:
    - 1
    - 2
    """
    sys.stdin = io.StringIO(test_yaml)

    test_parser = AnsibleConstructor(file_name='<stdin>')
    result = test_parser.get_single_data()
    assert result['foo'] == 'bar'
    assert result['bar'] == 'foo'
    assert result['foobar'] == [1, 2]

# Generated at 2022-06-13 07:29:11.674559
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():

    ac = AnsibleConstructor()

    from ansible.vars.unsafe_proxy import wrap_var
    from yaml.nodes import ScalarNode
    from yaml.nodes import MappingNode
    import yaml


# Generated at 2022-06-13 07:29:19.325719
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.vault import VaultSecret
    vault_secret = VaultSecret('vault_password', 'vault_password_file')
    constructor = AnsibleConstructor(vault_secrets=[vault_secret])
    text = "!unsafe 'test_value'"
    yaml_node = yaml.compose_all(text)
    node = yaml_node.value
    value = constructor.construct_yaml_unsafe(node)
    assert value == 'test_value'

# Generated at 2022-06-13 07:29:21.971138
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    inp = """
    - a
    - b
    - c
    """
    assert AnsibleConstructor.construct_yaml_seq(inp) == ["a", "b", "c"]

# Generated at 2022-06-13 07:29:28.175755
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    ansible_constructor = AnsibleConstructor()
    class YamlNode:
        pass
    node = YamlNode()
    node.start_mark = YamlNode()
    node.start_mark.column = 42
    node.start_mark.line = 18
    node.start_mark.name = "__my_file__"
    node.id = "scalar"

# Generated at 2022-06-13 07:29:43.679203
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secrets_safe = [u'$1$pBDEkDZj$pdHuuY12hEUjWpX8oA7Gd/', u'$5$xMZ8wvZQnjYtIXs7$uRX8Dv7yhTRjKHj7L3qT8wvTZ0pekYiL/7zW8PvM0R3', u'$6$i3T8TvA3$cOiWMfHj1Cp9XvFsoaHHoAO4j4fc0xl1gO2Qr6eqYH6U5i6zcBKQJxEzKO0nfI.pYRiJwZ.YpYnB6Ezq3jKem.']
   

# Generated at 2022-06-13 07:29:49.983825
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    ''' test construct_yaml_seq method of class AnsibleConstructor '''

    ans_constr = AnsibleConstructor()
    ans_node = '''
    - foo
    - bar
    '''
    seq = ans_constr.yaml_parse(ans_node)
    # FIXME: this isn't actually testing anything because ans_node is never
    # loaded properly (yaml.constructor.BaseConstructor.__init__() fails and
    # yaml.composer.Composer.get_node() is never called, which is needed to
    # actually invoke AnsibleConstructor.construct_yaml_seq()



# Generated at 2022-06-13 07:30:00.261032
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import yaml

    yaml_src = '''
foo: !unsafe !!python/object/apply:os.stat ["/etc/passwd"]
bar: !unsafe !!python/object/apply:os.stat [!!python/tuple ["/etc/passwd"]]
baz: !unsafe !!python/object/apply:os.stat [/etc/passwd]
'''
    # ConstructorError: while constructing a mapping
    # found duplicate dict key (foo)
    # in "./test.yml", line 3, column 1

    with open('/tmp/test.yml', 'w') as f:
        f.write(yaml_src)


# Generated at 2022-06-13 07:30:08.462968
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Generate a dict, key1 in dict is unique
    dict_1 = AnsibleConstructor.construct_mapping(MappingNode(None, [], []))
    # Generate a dict, key1 in dict is duplicate
    dict_2 = AnsibleConstructor.construct_mapping(MappingNode(None, [], [[u'key1', u'value1'], [u'key1', u'value2']]))
    # assert key1: value1 in dict_1
    assert dict_1[u'key1'] == u'value1'
    # assert key1: value2 in dict_2
    assert dict_2[u'key1'] == u'value2'

# Generated at 2022-06-13 07:30:16.502023
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    class Node():
        def __init__(self, start_mark, end_mark):
            self.start_mark = start_mark
            self.end_mark = end_mark

    start_mark = type('', (object,), {'column': 0, 'line': 0})()
    end_mark = type('', (object,), {'column': 8, 'line': 1})()

    node = Node(start_mark, end_mark)
    node.tag = u'tag:yaml.org,2002:str'
    node.value = 'abcdefgh'
    ret = AnsibleConstructor.construct_yaml_str(node)

    assert isinstance(ret, AnsibleUnicode)
    assert ret.ansible_pos == ('<unicode>', 1, 1)

# Generated at 2022-06-13 07:30:21.743518
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from collections import MutableMapping
    from random import randint
    from ..units.mock.loader import DictDataLoader

    size = randint(100, 1000)
    data = DictDataLoader({
        'key{0}'.format(i): randint(0, 0xFFFFFFFF) for i in range(size)
    })
    data.ansible_pos = ('/dev/null', 1, 1)

    assert isinstance(data, MutableMapping)
    assert len(data) == size
    for i in range(size):
        assert 'key{0}'.format(i) in data
        assert isinstance(data['key{0}'.format(i)], int)



# Generated at 2022-06-13 07:30:26.189497
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # Test 1: load data with 'variable_1' using constructor
    yaml_data = '''
variable_1:
- name: first_value
- name: second_value
variable_2:
- name: another_value
 '''
    yaml_data = yaml.load(yaml_data, Loader=AnsibleConstructor)
    assert yaml_data['variable_1'][1].value == 'second_value'
    assert yaml_data['variable_2'][0].value == 'another_value'

    # Test 2: load data with 'variable_1' using custom loader class
    yaml_data = '''
variable_1: !unsafe
- name: first_value
- name: second_value
variable_2:
- name: another_value
 '''

# Generated at 2022-06-13 07:30:32.313321
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    text = '''
    foo: [
      1,2
      , 3
      ,
      4,
      ]
    '''

    data = yaml.load(text, Loader=AnsibleConstructor)
    assert data == {'foo': [1,2,3,4]}, 'YAML sequence with newlines and empty items not parsed correctly'

    text = '''
    foo:
      - 1 # comment
      - 2 # comment
      - 3 # comment
      - 4 # comment
    '''

    data = yaml.load(text, Loader=AnsibleConstructor)
    assert data == {'foo': [1,2,3,4]}, 'YAML sequence with comments not parsed correctly'

# Generated at 2022-06-13 07:30:37.085869
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText

    constructor = AnsibleConstructor()

    unsafe_text = u'{"key": "value"}'
    result = constructor.construct_yaml_unsafe(unsafe_text)
    assert isinstance(result, AnsibleUnsafeText)
    assert unsafe_text == result.as_bytes()

# Generated at 2022-06-13 07:30:47.972977
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import sys

    class MockObject(object):
        pass

    yaml_parser = AnsibleConstructor
    testobj = MockObject()
    testobj.start_mark = MockObject()
    testobj.start_mark.column = 1
    testobj.start_mark.line = 1
    testobj.start_mark.buffer = '<unicode string>'
    testobj.start_mark.pointer = 0
    testobj.end_mark = MockObject()
    testobj.end_mark.column = 1
    testobj.end_mark.line = 1
    testobj.end_mark.buffer = '<unicode string>'
    testobj.end_mark.pointer = 3
    testobj.value = [('foo', 'bar')]
    testobj.tag = 'tag:yaml.org,2002:map'

# Generated at 2022-06-13 07:31:03.323219
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    from ansible.parsing.yaml.loader import AnsibleLoader

    vault_secrets = ['secret']
    vault_id = 'default'

# Generated at 2022-06-13 07:31:07.444230
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # testing:
    #       1. role_name: role_name_value
    #       2. role_name: role_name_value
    # expected:
    #       1. error message to occur
    #       2. last value should be stored, with no error
    yaml_1 = '''
    - role_name: role_name_value
    - role_name: role_name_value
    '''
    yaml_2 = '''
    - role_name: role_name_value
    - role_name: role_name_value
    '''
    yaml_3 = '''
    - role_name: role_name_value
    - role_name: role_name_value
    '''

# Generated at 2022-06-13 07:31:18.684391
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import yaml
    text_file = open("vars_example.yaml", "r")
    out = text_file.read()
    print(out)
    yaml_data = yaml.load(out, AnsibleConstructor)
    print(yaml_data)
    #print(yaml_data.ansible_pos)
    #print(yaml_data['vars'].ansible_pos)
    #print(yaml_data['vars']['var1'].ansible_pos)
    #print(yaml_data['vars']['dict1'].ansible_pos)
    #print(yaml_data['vars']['dict1']['inner'].ansible_pos)
    #print(yaml_data['vars']['dict1']['inner'

# Generated at 2022-06-13 07:31:29.633410
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    import copy
    import sys

    # Test for python 2 or python 3
    PY3 = sys.version_info[0] == 3

    # Test ansible constructors
    from ansible.parsing.yaml.loader import AnsibleLoader
    ansible_constructor = AnsibleConstructor(vault_secrets=['test_construct_vault_encrypted_unicode'])


# Generated at 2022-06-13 07:31:33.318592
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # unit test the constructor map
    yaml = YAML(typ='safe')
    yaml.default_flow_style = None
    data = yaml.load("""
---
foo: bar
baz: qux
""")

    assert data == {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 07:31:40.623889
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    class FakeNode(object):
        def __init__(self, start_mark):
            self.start_mark = start_mark
        id = None

    class FakeMark(object):
        def __init__(self, line=0, column=0, name="<string>"):
            self.line = line
            self.column = column
            self.name = name

    # Construct a FakeNode to pass to AnsibleConstructor
    node = FakeNode(FakeMark())

    # Run construct_yaml_str
    ac = AnsibleConstructor()
    x = ac.construct_yaml_str(node)

    # Verify output is of type AnsibleUnicode
    assert isinstance(x, AnsibleUnicode)

    # Verify output is empty
    assert x == u''

    # Verify start_mark is properly copied to ans

# Generated at 2022-06-13 07:31:50.348079
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    import yaml
    try:
        import yaml.cyaml as cyaml
        use_libyaml = True
    except ImportError:
        use_libyaml = False

    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestAnsibleConstructor(unittest.TestCase):

        def setUp(self):
            self.constructor = AnsibleConstructor()

        def test_construct_mapping_duplicate_ok(self):
            yaml_data = u'{"key": "value", "key": "value2"}'

# Generated at 2022-06-13 07:32:05.968923
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():

    import pytest


# Generated at 2022-06-13 07:32:12.026406
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    constructor = AnsibleConstructor()

# Generated at 2022-06-13 07:32:16.971942
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.loader import AnsibleLoader

    contents = '''
test_key1: string
test_key2:
  - array entry 1
  - array entry 2
'''

    results = AnsibleLoader(contents).get_single_data()
    assert results['test_key1'] == 'string'
    assert results['test_key2'] == ['array entry 1', 'array entry 2']

# Generated at 2022-06-13 07:32:31.946007
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    test_list = [{'foo': {'bar': 'baz', 'bam': 'bop'}, 'bam': 10, 'bar': ['a', 'b', {'baz': 11}]}]
    my_dict = dict(ansible_facts=test_list)
    data = 'ansible_facts:\n- bar:\n  - a\n  - b\n  - baz: 11\n  bam: bop\n  foo: {bar: baz}\nbam: 10\n'
    my_list = AnsibleLoader(data, file_name='<string>').get_single_data()
    assert my_list == my_dict

# Generated at 2022-06-13 07:32:37.256073
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    try:
        import yaml
    except ImportError:
        print('Skipping since PyYAML is not installed.')
        return
    contents = """
- val_1
- val_2
- val_3
"""
    yaml_data = yaml.load(contents, Loader=AnsibleConstructor)
    assert isinstance(yaml_data, AnsibleSequence)
    for i in range(len(yaml_data)):
        assert isinstance(yaml_data[i], AnsibleUnicode)


# Verify that we can use AnsibleConstructor class to load a file with
# duplicate keys, using the default setting

# Generated at 2022-06-13 07:32:42.793159
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    class FakeConstructor:
        def construct_object(self, node):
            return node.value
    constructor = AnsibleConstructor()
    test_node = FakeConstructor()
    test_node.value = 3.14
    assert constructor.construct_yaml_unsafe(test_node) == 3.14

# Generated at 2022-06-13 07:32:51.379893
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    import ansible.parsing.yaml.loader
    yaml_data = '''{"key1": "value1", "key2": "value2"}'''
    ansible_constructor = ansible.parsing.yaml.loader.AnsibleConstructor()
    ansible_dict = ansible_constructor.construct_yaml_map(yaml_data)
    assert ansible_dict.__class__ == ansible.parsing.yaml.objects.AnsibleMapping
    assert ansible_dict == {'key1': 'value1', 'key2': 'value2'}
    assert ansible_dict.ansible_pos == (None, 1, 1)
    assert not ansible_dict.vault is None

# Generated at 2022-06-13 07:33:00.085820
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    # load a Unicore object which has been marked as !unsafe
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    constructor = AnsibleConstructor(file_name='master.yml')
    node = yaml.nodes.ScalarNode(tag='!unsafe', value='hello')

    result = constructor.construct_yaml_unsafe(node)

    # even though the original object was a unicode string, AnsibleUnicode is not an instance of basestring
    # (because it has extra attributes)
    # assert that the result is an instance of AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafeText)
    # assert that the result is an instance of both basestring and Unicode
    #

# Generated at 2022-06-13 07:33:04.102393
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    a = yaml.load(u'foo: hello world', Loader=AnsibleConstructor)
    assert isinstance(a, dict)
    assert a == {u'foo': u'hello world'}
    assert isinstance(a[u'foo'], AnsibleUnicode)


# Generated at 2022-06-13 07:33:08.485362
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    data = """
    w: 1
    x: 2
    y: 3
    z: 4
    """
    node = yaml.compose(data)
    ac = AnsibleConstructor()
    mapping = ac.construct_mapping(node)
    assert mapping['x'] == 2



# Generated at 2022-06-13 07:33:17.661676
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Need to specify file_name and vault secrets as AnsibleConstructor
    # constructor will fail without it
    file_name = 'test.yml'
    vault_secrets = ['VaultSecrets']
    c = AnsibleConstructor(file_name, vault_secrets)

    assert c.construct_yaml_seq({"value": [1, 2], "id": "test_id"}).next() == [1, 2]

# Generated at 2022-06-13 07:33:24.270208
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node1 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)
    node2 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)
    node3 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)
    node4 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)
    node5 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)
    node6 = MappingNode(tag='tag:yaml.org,2002:map', value=[], flow_style=None)

# Generated at 2022-06-13 07:33:33.508124
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml import objects
    import yaml

    obj = {'a': 3, 'b': 4, 'c': 5}
    data = """
a: 3
b: 4
c: 5
"""
    data_samevalue = """
a: 3
b: 4
c: 3
"""

    yaml_obj = yaml.load(data, Loader=yaml.Loader)
    assert isinstance(yaml_obj, objects.AnsibleMapping)

    ac = AnsibleConstructor()
    ac_obj = ac.construct_mapping(yaml.load(data, Loader=yaml.Loader))
    assert isinstance(ac_obj, objects.AnsibleMapping)

    assert obj == ac_obj


# Generated at 2022-06-13 07:33:49.901354
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    from ansible.parsing.yaml import objects

    # test parameters
    node = {'type': 'map', 'start_mark': '<mark>', 'value': [('key', 'value')]}
    node_class = {'type': 'map', 'start_mark': '<mark>', 'value': [('key', 'value')]}

    # mock
    class MockDisplay(object):
        def __init__(self):
            self._warned = False
        def warning(self, message):
            if 'dict key' in message:
                self._warned = True
    display = MockDisplay()

    # test
    def construct_mapping_func(self, node, deep=False):
        return 'mapping_value'

    ansible_constructor = AnsibleConstructor()

# Generated at 2022-06-13 07:34:00.573492
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    """ Test the AnsibleConstructor._node_position_info method with a a vary of text types """
    import yaml
    import six

    class TestVault:
        def __init__(self, secrets=[]):
            self.secrets = secrets

        def decrypt(self, ciphertext_data):
            return ciphertext_data


# Generated at 2022-06-13 07:34:14.936848
# Unit test for method construct_yaml_map of class AnsibleConstructor

# Generated at 2022-06-13 07:34:24.315639
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    import yaml
    # test that tags are preserved when scalars are loaded as strings
    s = u'{foo}'
    yaml_str = yaml.dump(s)
    assert yaml.load(yaml_str) == u'{foo}'
    assert type(yaml.load(yaml_str)) == str
    assert yaml.load(yaml_str, Loader=AnsibleLoader) == u'{foo}'
    assert type(yaml.load(yaml_str, Loader=AnsibleLoader)) == AnsibleUnicode

    # test that tags aren't preserved when not loading as strings
    s = u'{foo}'
    yaml_str = yaml.dump(s)

# Generated at 2022-06-13 07:34:27.564138
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    node = AnsibleConstructor.construct_yaml_str(None, None)

    assert str(type(node)) == "<class 'ansible.parsing.yaml.objects.AnsibleUnicode'>"

# Generated at 2022-06-13 07:34:36.898057
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import types
    class Foo(object):
        def __init__(self, x):
            self.x = x
        def __str__(self):
            return "Foo(x=%s)" % self.x
        def __repr__(self):
            return "Foo(x=%s)" % self.x
    dummy_data = {
        'text': "whatever",
        'foo': Foo("hello"),
        'nested': {
            "foo": Foo("world"),
            "bar": Foo("!")
            }
        }

# Generated at 2022-06-13 07:34:37.699956
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    # TODO: write unit test
    pass

# Generated at 2022-06-13 07:34:40.679886
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    doc = """
    foo: bar
    baz:
      - one
      - two
      - three
    """
    expected = {'foo': 'bar', 'baz': ['one', 'two', 'three']}
    c = AnsibleConstructor(file_name="foo.yml")
    # xxx: need to determine how to test a Generator method?


# Generated at 2022-06-13 07:34:44.978594
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    constructor = AnsibleConstructor()
    test_node = MappingNode(u'tag', u'key', u'value')
    assert type(constructor.construct_yaml_map(test_node)) == AnsibleMapping


# Generated at 2022-06-13 07:34:54.802270
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    # Test case for setting ansible_pos
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import StringIO
    data1 = u'---\n[one, two]'

    constructor = AnsibleConstructor()
    loader = AnsibleLoader(StringIO(data1), constructor)
    sequence = list(loader.get_single_data())
    assert sequence[0].ansible_pos == (None, 1, 1)
    assert sequence[1] == 'one'
    assert sequence[2] == 'two'
    assert sequence[3].ansible_pos == (None, 1, 11)

    # Test case for ansible_pos in different line
    data2 = u'---\n[\n one,\n two\n]'

    loader = AnsibleLoader(StringIO(data2), constructor)

# Generated at 2022-06-13 07:35:13.654528
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    # Note: This test has been in the codebase for years, so even though it
    # doesn't show up in coverage, it is being tested.
    ans_con = AnsibleConstructor()
    test_node = MappingNode(tag="dict", start_mark="", end_mark="")
    test_node.value = [("key1", "value1"), ("key2", "value2")]

    ans_con.construct_mapping(test_node)

    assert ans_con.construct_mapping(test_node) == {"key1": "value1", "key2": "value2"}

# Generated at 2022-06-13 07:35:20.139853
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    import yaml

    if sys.version_info < (2, 7):
        encrypt = "!!python/str 'c29tZXRoaW5nCg==\n'"
    else:
        encrypt = "!!python/unicode 'c29tZXRoaW5nCg==\n'"
    yamlinput = """
a: !unsafe
  b: %s
""" % encrypt
    yamloutput = yaml.load(yamlinput, Loader=yaml.Loader)
    assert isinstance(yamloutput['a'], dict)
    assert isinstance(yamloutput['a']['b'], AnsibleUnicode)
    assert yamloutput['a']['b'] == 'something\n'

# Generated at 2022-06-13 07:35:32.914967
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.dumper import AnsibleDumper

    if not PY3:
        # There is a bug in PyYaml 3.11, 3.12 that doesn't allow
        # empty strings to be dumped in non-PY3 mode.
        # This test will only be valid in PY3 and when the bug is
        # fixed in PyYaml.
        return

    seq = [1, 2, 3, 4, 5]
    orig_seq = seq[:]

    node = AnsibleDumper().represent_sequence(u'tag:yaml.org,2002:seq', seq)
    node.start_mark.name = "Test"
    node.start_mark.line = 1
    node.start_mark.column = 0
   

# Generated at 2022-06-13 07:35:45.000024
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    file_name = None
    vault_secrets = None
    yaml_str = '''      
- name: Create a temp file    
  tempfile:    
    state: directory    
  register: temp_dir_result

- name: Copy ssh keys to the temp dir
  copy:
    src: "{{ lookup('env','HOME') }}/.ssh"
    dest: "{{ temp_dir_result.path }}/backup"
'''
    data = list(yaml.load_all(yaml_str, Loader=AnsibleConstructor))
    assert len(data) == 2
    for x in data:
        assert isinstance(x, AnsibleMapping)
        for field, value in x.items():
            assert isinstance(field, AnsibleUnicode)

# Generated at 2022-06-13 07:35:46.253072
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    assert AnsibleConstructor.construct_vault_encrypted_unicode is not None

# Generated at 2022-06-13 07:35:58.116367
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.error import AnsibleParserError

    # create dict as string, and load it to AnsibleConstructor
    testdata = '''
one: 1
two: 2
three: 3
four:
  - 1
  - 2
  - 3
'''

    data = AnsibleLoader(testdata)

    # the dict constructed by AnsibleConstructor should contains
    # a list of AnsibleUnicode, not only python built-in string

# Generated at 2022-06-13 07:36:03.320926
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    class MyAnsibleConstructor(AnsibleConstructor):
        def construct_yaml_str(self, node):
            return AnsibleUnicode('construct_yaml_str called')
    node = MyAnsibleConstructor().construct_yaml_str('')
    assert node.__class__ is AnsibleUnicode
    assert node == 'construct_yaml_str called'

# Generated at 2022-06-13 07:36:15.262640
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 07:36:18.449565
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    ac = AnsibleConstructor()
    node = {
        'a': 1,
        'b': 2,
    }
    d = ac.construct_yaml_map(node)
    assert type(d) == AnsibleMapping



# Generated at 2022-06-13 07:36:20.327246
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    test_node = SafeConstructor.construct_mapping(AnsibleConstructor, None)
    assert isinstance(test_node, AnsibleMapping)


# Generated at 2022-06-13 07:36:33.764300
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    obj = AnsibleConstructor()
    node = MappingNode(u"1", [], [], [], True)
    output = AnsibleMapping()
    output.ansible_pos = (u'<unicode string>', 1, 1)
    assert obj.construct_yaml_map(node).next().ansible_pos == output.ansible_pos



# Generated at 2022-06-13 07:36:39.244243
# Unit test for method construct_mapping of class AnsibleConstructor
def test_AnsibleConstructor_construct_mapping():
    node_value = [
        ('key', 'value'),
        ('key', 'overwrite'),
        ('new', 'value'),
        ('new', 'overwrite'),
        ('new', 'overwrite_again'),
        ('key', 'overwrite_again'),
    ]
    node = MappingNode(node_value, False, None, None, None)
    mapping = AnsibleConstructor.construct_mapping(node=node)
    expected_mapping = AnsibleMapping(
        key='overwrite_again',
        new='overwrite_again',
    )
    assert mapping == expected_mapping

# Generated at 2022-06-13 07:36:49.439852
# Unit test for method construct_yaml_unsafe of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_unsafe():
    import sys
    if sys.version_info[0] < 3:
        from cStringIO import StringIO
    else:
        from io import StringIO

    from ansible.parsing.yaml.loader import AnsibleLoader

    data1 = '''
    key: !unsafe
        Not a SafeConstructor
    key2: !unsafe "Not a SafeConstructor"
    '''
    stream1 = StringIO(data1)
    loader1 = AnsibleLoader(stream1, file_name='<string>')
    loader1.get_single_data()
    assert 'Not a SafeConstructor' == loader1.get_single_data()['key']
    assert isinstance(loader1.get_single_data()['key'], type(''))
    assert 'Not a SafeConstructor' == loader1.get_

# Generated at 2022-06-13 07:36:55.120960
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    # arrange
    vault_id = 'test'
    vault_password = 'test'
    vault_secrets = [u'{0}:{1}'.format(vault_id, vault_password)]


# Generated at 2022-06-13 07:37:03.390176
# Unit test for method construct_yaml_seq of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_seq():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import yaml
    loader = AnsibleLoader(yaml.load, file_name='test_file')

# Generated at 2022-06-13 07:37:12.758117
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    vault_secret = None
    # We don't have a vault secret
    ac = AnsibleConstructor(file_name=None, vault_secrets=vault_secret)

# Generated at 2022-06-13 07:37:19.969714
# Unit test for method construct_vault_encrypted_unicode of class AnsibleConstructor
def test_AnsibleConstructor_construct_vault_encrypted_unicode():
    constructor = AnsibleConstructor()
    constructor.vault_secrets = [b'hunter']
    node = MappingNode(tag=u'tag:yaml.org,2002:str', value=[],
                       flow_style=False, anchor=None,
                       tag_directives=[], start_mark=None, end_mark=None)
    node.value = ['', '']
    node.value[0] = '!vault |\n'

# Generated at 2022-06-13 07:37:31.901631
# Unit test for method construct_yaml_str of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_str():
    # Float numbers should be retrieved as string

    try:
        import yaml
    except ImportError:
        raise SkipTest()

    input_data = {'test': 'yaml'}

    src = yaml.dump(input_data).replace('\n- ', '- ')
    src += '\n'
    src += '   - 1.0\n'
    src += '   - 1.5\n'
    src += '   - 3.14159265359\n'

    data = yaml.load(src, Loader=yaml.Loader)
    for item in data:
        assert isinstance(item, AnsibleUnicode)
        if isinstance(data[item], AnsibleUnicode):
            assert isinstance(data[item], AnsibleUnicode)

    # Test default values
    input

# Generated at 2022-06-13 07:37:38.992741
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from collections import OrderedDict
    yaml_str = "foo: bar\nbaz: tar"
    constructor = AnsibleConstructor()
    node = yaml.compose(yaml_str)
    node.tag = u'tag:yaml.org,2002:map'
    #convert to OrderedDict
    result = OrderedDict(constructor.construct_yaml_map(node))
    assert isinstance(result, OrderedDict)
    assert result == OrderedDict([(u'foo', u'bar'), (u'baz', u'tar')])

test_AnsibleConstructor_construct_yaml_map.unittest = ['.yamlconstructor']


# Generated at 2022-06-13 07:37:42.220498
# Unit test for method construct_yaml_map of class AnsibleConstructor
def test_AnsibleConstructor_construct_yaml_map():
    from ansible.parsing.yaml.objects import AnsibleMapping
    empty_dict = {}
    assert isinstance(AnsibleConstructor(file_name="test").construct_yaml_map(empty_dict), AnsibleMapping)

