

# Generated at 2022-06-13 07:17:36.284949
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(b'''
- name: test
  hosts: localhost
  user: localhost
  vars:
    foo: bar
  tasks:
    - debug: msg={{ foo }}
''') == [{'tasks': [{'debug': {'msg': '{{ foo }}'}}], 'vars': {'foo': 'bar'}, 'hosts': 'localhost', 'user': 'localhost', 'name': 'test'}]

    from ansible.module_utils.common.text.converters import to_bytes

# Generated at 2022-06-13 07:17:45.788261
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This function performs a basic unit test of the Ansible from_yaml function
    to ensure it works as expected. The test is run by loading the data from
    the section of ansible/test/units/parsing/yaml.yaml.

    This function currently does not test the vault encryption capabilities
    but that is a minor issue as the vault functions are well tested.
    '''

    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import StringIO as StringIO_m

    import sys
    import yaml
    if PY3:
        import io
        StringIO = io.StringIO

    # some yaml

# Generated at 2022-06-13 07:17:48.368734
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"user": "xxxx"}'
    assert from_yaml(data) == {u'user': u'xxxx'}

# Generated at 2022-06-13 07:17:58.716240
# Unit test for function from_yaml
def test_from_yaml():

    # Test basic json and yaml parsing
    assert from_yaml('[{"sample_key": "sample_value"}]') == [{u'sample_key': u'sample_value'}]
    assert from_yaml('{"sample_key": "sample_value"}') == {u'sample_key': u'sample_value'}

    # Test yaml parsing with ansible specific syntax
    assert from_yaml('[{{ "sample_key": "sample_value" }}]') == [{u'sample_key': u'sample_value'}]
    assert from_yaml('[{{ sample_key }}]') == [{u'sample_key': u''}]

    # Test that we fail when we try yo parse an invalid json

# Generated at 2022-06-13 07:17:59.588053
# Unit test for function from_yaml
def test_from_yaml():
    # data = '{"version": 2}'
    pass

# Generated at 2022-06-13 07:18:09.322868
# Unit test for function from_yaml
def test_from_yaml():
    # 1. Basic AJSON syntax check
    assert from_yaml('{"foo": "bar"}', json_only=True) == {u'foo': u'bar'}
    assert from_yaml('[]', json_only=True) == []
    assert from_yaml('[1,2,3,4]', json_only=True) == [1, 2, 3, 4]
    assert from_yaml('"string"', json_only=True) == u'string'
    assert from_yaml('true', json_only=True) is True
    assert from_yaml('false', json_only=True) is False
    assert from_yaml('null', json_only=True) is None

# Generated at 2022-06-13 07:18:13.233644
# Unit test for function from_yaml
def test_from_yaml():
    output = from_yaml('''{
    "hello": "world",
    "foo": "bar",
    "is_it_true": true,
    "float_number": 42.0,
    "number": 42,
    "other_number": 43,
    "some_json": "\\"{}\\""
}''')

    assert output == {
        'hello': 'world',
        'foo': 'bar',
        'is_it_true': True,
        'float_number': 42.0,
        'number': 42,
        'other_number': 43,
        'some_json': '"{}"'
    }

# Generated at 2022-06-13 07:18:17.980987
# Unit test for function from_yaml
def test_from_yaml():
    file = open('./role_yaml.yml', 'r')
    yml = file.read()
    # print(yml)
    d = from_yaml(yml)
    # print(type(d))
    print(d)


# Generated at 2022-06-13 07:18:26.372195
# Unit test for function from_yaml
def test_from_yaml():
    # json test
    json_data = '{"a": 1, "b": 2, "c": 3, "e": [1,2,3,4], "f": {"g": "hi"}, "h": true, "i": null}'
    json_dict = {"a": 1, "b": 2, "c": 3, "e": [1,2,3,4], "f": {"g": "hi"}, "h": True, "i": None}
    assert json_dict == from_yaml(json_data)

    # yaml test
    yaml_data = '''a: 1
b: 2
c: 3
e:
  - 1
  - 2
  - 3
  - 4
f:
  g: hi
h: true
i: null
'''

# Generated at 2022-06-13 07:18:36.785001
# Unit test for function from_yaml
def test_from_yaml():
    # Test valid JSON
    valids = [
        "{}",
        "{\"foo\":\"bar\"}",
        "[1,2,3]",
        "\"hello\"",
        1234
    ]
    for data in valids:
        res = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
        assert type(res) is type(json.loads(data)), "Expected to get %s from %s" % (type(json.loads(data)), data)

    # Test valid YAML
    valids = [
        "{}",
        "{foo: bar}",
        "[1,2,3]",
        "hello",
        1234
    ]
    for data in valids:
        res = from_

# Generated at 2022-06-13 07:18:43.254953
# Unit test for function from_yaml
def test_from_yaml():
	DATA_JSON = """
	{
		"a": "b",
		"c": "d",
		"e": { "f": "g", "h": "i" },
		"j": [ "k", "l", { "m": "n" } ]
	}
	"""

	DATA_YAML = """
	---
	a: b
	c: d
	e:
	  f: g
	  h: i
	j:
	- k
	- l
	- {m: "n"}
	"""

	assert from_yaml(DATA_JSON) == from_yaml(DATA_YAML)


# Generated at 2022-06-13 07:18:51.100285
# Unit test for function from_yaml
def test_from_yaml():
    v = { 'a': 'a' }
    assert from_yaml(json.dumps(v), json_only=True) == v
    assert from_yaml(json.dumps(v)) == v
    assert from_yaml("a: b") == {'a': 'b'}
    error = False
    try:
        from_yaml("a: b\n c: d")
    except AnsibleParserError:
        error = True
    assert error is True

# Generated at 2022-06-13 07:18:59.514932
# Unit test for function from_yaml
def test_from_yaml():

    def assert_from_yaml(data, expected):
        assert expected == from_yaml(data)

    # --- common gotchas ---

    # items should be separated by newlines
    assert_from_yaml("{'foo': 'bar'}", {"foo": "bar"})
    assert_from_yaml("{'foo': 'bar'}\n", {"foo": "bar"})
    assert_from_yaml("{'foo': 'bar'}\n\n", {"foo": "bar"})
    assert_from_yaml("{'foo': 'bar'}\n{'foo': 'bar'}", {"foo": "bar"})

    # quotes can be omitted for strings
    assert_from_yaml("{foo: bar}", {"foo": "bar"})

# Generated at 2022-06-13 07:19:06.772585
# Unit test for function from_yaml
def test_from_yaml():
    test_data = '''
    - hosts:
        - localhost
    tasks:
    - name: Ansible_Skeleton_Plugin_Test
      community.general.ansible_skeleton:
        key: "value"
    '''

    # Load and validate YAML
    data = from_yaml(test_data, vault_secrets=None, json_only=False)
    assert data == [{"hosts": ["localhost"],
                     "tasks": [{"name": "Ansible_Skeleton_Plugin_Test",
                                "community.general.ansible_skeleton": {"key": "value"}}]}]

# Generated at 2022-06-13 07:19:13.153771
# Unit test for function from_yaml
def test_from_yaml():
    data = '{ "a" : 1 }'
    file_name = "abc"
    show_content = True
    vault_secrets = None
    assert from_yaml(data, file_name, show_content, vault_secrets, json_only = False) == json.loads(data, cls = AnsibleJSONDecoder)

# Generated at 2022-06-13 07:19:21.695584
# Unit test for function from_yaml
def test_from_yaml():

    import os
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.yaml import from_yaml

    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'unit', 'parsing', 'yaml', 'data')

    assert from_yaml(u'test: [ 1, 2, 3]', '<string>') == {'test': [1, 2, 3]}

    assert from_yaml(open(os.path.join(file_path, 'good.yaml')).read(), 'good.yaml') == {u'foo': u'bar'}

# Generated at 2022-06-13 07:19:26.956888
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    {
    "object": "whatever",
    "value": 5,
    "array": [ 1 ]
    }
    '''

    new_data = from_yaml(data)

    # assertions
    assert new_data['object'] == 'whatever'
    assert new_data['value'] == 5
    assert new_data['array'] == [1]

# Generated at 2022-06-13 07:19:30.181608
# Unit test for function from_yaml
def test_from_yaml():
    data = """
    {
        'test': [
            {
                'user': 'test',
                'pass': 'test'
            }
        ]
    }
    """

    new_data = from_yaml(data)
    assert(new_data['test'][0]['user'] == 'test')

# Generated at 2022-06-13 07:19:36.160864
# Unit test for function from_yaml
def test_from_yaml():
    valid_json_string = "{\"hello\": \"world\"}"
    valid_yaml_string = "hello: world"
    invalid_string = "hellow wourld"

    # Test valid JSON
    result = from_yaml(valid_json_string)
    assert len(result) == 1
    assert result['hello'] == "world"

    # Test valid YAML
    result = from_yaml(valid_yaml_string)
    assert len(result) == 1
    assert result['hello'] == "world"

    # Test invalid string
    try:
        from_yaml(invalid_string)
        assert False
    except AnsibleParserError:
        assert True

    # Test invalid json_only

# Generated at 2022-06-13 07:19:42.117556
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('nope', 'test_from_yaml') == None
    assert from_yaml('"test"', 'test_from_yaml') == 'test'
    assert from_yaml('{"test": "from_yaml"}', 'test_from_yaml') == {'test': 'from_yaml'}

# Generated at 2022-06-13 07:19:52.664225
# Unit test for function from_yaml
def test_from_yaml():
    # Test JSON input
    testjson = '{"key": "value"}'
    testval = from_yaml(testjson)
    assert testval == {"key": "value"}

    # Test YAML input
    testyaml = '''
    - hosts: localhost
      tasks:
      - debug:
          msg: 'Hello World'
    '''
    testval = from_yaml(testyaml)
    correct_value = [{'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'Hello World'}}]}]
    assert testval == correct_value

    # Test invalid input
    testyaml_invalid = '''
    - hosts: localhost
      tasks:
    '''
    # Ensure an exception occurs.

# Generated at 2022-06-13 07:20:02.565348
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    dl = DataLoader()

    # Test loading data as json, correctly returns with json
    data = '{"a": "1", "b": [1, 2, 3]}'
    expected = {'a': '1', 'b': [1, 2, 3]}
    data_json = from_yaml(data)
    assert data == data_json

    # Test loading data as yaml, correctly returns with json
    data = 'a: 1\nb:\n- 1\n- 2\n- 3'
    expected = {'a': '1', 'b': [1, 2, 3]}
    data_json = from_y

# Generated at 2022-06-13 07:20:09.264493
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib

    output = from_yaml("{'a':'b'}")
    assert output == {'a': 'b'}
    output = from_yaml("{{ 'a' : 'b' }}")
    assert output == {'a': 'b'}
    output = from_yaml("a: b")
    assert output == 'a: b'
    output = from_yaml("a: 'b'")
    assert output == {'a': 'b'}
    output = from_yaml("a: \"b\"")
    assert output == {'a': "b"}

    vault = VaultLib()

# Generated at 2022-06-13 07:20:20.076706
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "foo": [ "bar", "baz" ] }') == {"foo": ["bar", "baz"]}
    assert from_yaml('foo') == "foo"
    assert from_yaml(1) == 1
    assert from_yaml('') == ""
    assert from_yaml(None) == None
    assert from_yaml([]) == []
    assert from_yaml('{"a": { "b": { "c": { "d": 1 }}}}}') == {"a": {"b": {"c": {"d": 1}}}}
    assert from_yaml('{"foo": [ "bar", "baz" ] }') == {"foo": ["bar", "baz"]}
    assert from_yaml('foo') == "foo"
    assert from_yaml(1) == 1

# Generated at 2022-06-13 07:20:27.805950
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{ 'k1': 'v1' }", json_only=True) == { 'k1': 'v1' }
    assert from_yaml("{ 'k1': 'v1' }") == { 'k1': 'v1' }
    assert from_yaml("k1:\n  - v1\n  - v2") == { 'k1': ['v1', 'v2'] }
    assert from_yaml("k1: |\n  v1\n  v2") == { 'k1': "v1\nv2" }
    from_yaml("k1: v1", show_content=False)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:20:38.212547
# Unit test for function from_yaml
def test_from_yaml():
    import unittest
    from ansible.module_utils.six import PY3, binary_type, text_type

    class TestAnsibleYaml(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def do_test_from_yaml(self, data, expected, file_name='<string>'):
            # checking Python 3 JSON decoding
            new_data = from_yaml(data, file_name, True)
            if PY3 and isinstance(new_data, text_type):
                new_data = new_data.encode('utf-8')
            self.assertEqual(data, new_data)

            # checking Python 2 JSON decoding
            new_data = from_yaml(data, file_name, True)
           

# Generated at 2022-06-13 07:20:42.641251
# Unit test for function from_yaml
def test_from_yaml():
    data = u"{'foo': 'bar'}"
    expected = {u'foo': u'bar'}
    assert from_yaml(data) == expected
    assert from_yaml(data, json_only=True) == expected

# Generated at 2022-06-13 07:20:56.766113
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.loader import AnsibleUnicode
    from ansible.parsing.ajson import AnsibleJSONEncoder

    # Create a unicode string and a byte string
    unicode_string = u''.join(u'\u05d0')

    # The unicode string should encode as UTF-8
    assert unicode_string.encode('utf-8') == b'\xd7\x90'

    # A unicode string is the same as a byte string in Python 2
    if not PY3:
        assert unicode_string == b'\xd7\x90'

    # The unicode string should be equal to and encoded as JSON
    assert unicode_

# Generated at 2022-06-13 07:21:08.882845
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.unicode import to_unicode
    from ansible.parsing.yaml import objects as yaml_objects
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 07:21:12.853906
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('''
    {
        "json": "The key is in JSON",
        "yaml": "The key is in YAML"
    }
    '''))

# Generated at 2022-06-13 07:21:23.522718
# Unit test for function from_yaml
def test_from_yaml():
    import datetime
    test_yaml_str = """
---
int: 1
float: 23.0
float_with_exp: 2.3e1
string: test string
string_with_exp: ~
list: [1, 2, 3, 4]
dict:
  key1: val1
  key2: val2
datetime: 1984-05-13T13:20:00
bool_t: true
bool_f: false
null_none: null
null_empty:
"""
    test_yaml_data = from_yaml(test_yaml_str)
    assert test_yaml_data['int'] == 1
    assert test_yaml_data['float'] == 23.0
    assert test_yaml_data['float_with_exp'] == 23.0
    assert test_yaml_

# Generated at 2022-06-13 07:21:26.073868
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('stuff') == None
    assert from_yaml('[]') == []
    assert from_yaml('{}') == {}


# Generated at 2022-06-13 07:21:28.790944
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '{"name": "test"}'
    json_dict = {"name": "test"}
    yaml_str = 'name: test'
    yaml_dict = {"name": "test"}

    assert from_yaml(json_str) == json_dict
    assert from_yaml(yaml_str) == yaml_dict

# Generated at 2022-06-13 07:21:34.172970
# Unit test for function from_yaml
def test_from_yaml():
    # this should be a valid JSON
    json_str = '{"a": {"b": {"c": [1, 2, {"d": "e", "a": "b"}]}}}'

    # this should be a valid YAML
    yaml_str = '''a:
    b:
        c:
            - 1
            - 2
            - d: e
              a: b'''

    # both should be parsed and return the same dict
    res1 = from_yaml(json_str, json_only=True)
    res2 = from_yaml(yaml_str)

    assert res1 == res2

    try:
        from_yaml(json_str)
        assert False
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:21:38.476014
# Unit test for function from_yaml
def test_from_yaml():
    with open('test/test_ajson.json', 'r') as f:
        data_str = f.read()
    data = json.loads(data_str, cls=AnsibleJSONDecoder)
    new_data = from_yaml(data_str)
    assert data == new_data

# Generated at 2022-06-13 07:21:44.744559
# Unit test for function from_yaml
def test_from_yaml():
    # This could be a single string,
    data = '''
    key: value
    '''

    # or a file pointer,
    import io
    data_io = io.StringIO(data)

    # or a file pathname.
    import tempfile
    (data_fd, data_pathname) = tempfile.mkstemp()
    data_file = open(data_fd)
    data_file.write(data)
    data_file.close()

    # In all cases, from_yaml returns the same data structure.
    assert from_yaml(data) == from_yaml(data_io) == from_yaml(data_pathname)


# Generated at 2022-06-13 07:21:54.196516
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"awx": {"foo": "bar"}, "test": "success"}'
    new_data = from_yaml(data, json_only=True)
    assert new_data == {'awx': {'foo': 'bar'}, 'test': 'success'}
    new_data = from_yaml(data, json_only=False)
    assert new_data == {'awx': {'foo': 'bar'}, 'test': 'success'}

    data = 'a: 1\nb: 2'
    new_data = from_yaml(data, json_only=True)
    assert new_data == None

    data = 'awx:\n  foo: bar'
    new_data = from_yaml(data, json_only=True)
    assert new_data == None


# Generated at 2022-06-13 07:22:06.011682
# Unit test for function from_yaml
def test_from_yaml():
    # Passing valid YAML string
    assert from_yaml("---\nhosts: all\nbecome: true") == {'hosts': 'all', 'become': True}

    # Passing valid JSON string
    assert from_yaml('{\"hosts\": \"all\", \"become\": true}') == {'hosts': 'all', 'become': True}

    # Valid YAML/JSON string with a vaulted value

# Generated at 2022-06-13 07:22:13.262667
# Unit test for function from_yaml
def test_from_yaml():
    '''
    from_yaml - test for yml
    '''

# Generated at 2022-06-13 07:22:17.586759
# Unit test for function from_yaml
def test_from_yaml():
    ansible_from_yaml = from_yaml('[1,2,3,4,5]')
    assert ansible_from_yaml == [1,2,3,4,5]

# Generated at 2022-06-13 07:22:23.822233
# Unit test for function from_yaml
def test_from_yaml():
    json_data = '{"player": "johndoe", "points": 10}'
    data = from_yaml(json_data)
    assert( data['player'] == 'johndoe' )


# Generated at 2022-06-13 07:22:29.376279
# Unit test for function from_yaml
def test_from_yaml():
    # If this test fails, it is likely you have installed a different version of PyYAML
    # than is used in this class.
    # The safest way to resolve the error is to reinstall PyYAML via the distro package or pip.
    # If that is not an option for some reason, you can change the test to not expect the
    # custom error class.
    yaml_data = \
'''---
- hosts: server
  tasks:
    - name: Run ls
      shell: ls
'''

    test_data = from_yaml(yaml_data)
    assert test_data[0]['hosts'] == 'server'
    assert test_data[0]['tasks'][0]['name'] == 'Run ls'

# Generated at 2022-06-13 07:22:43.566558
# Unit test for function from_yaml
def test_from_yaml():

    assert from_yaml('this is a string') == 'this is a string'
    assert from_yaml('this is a string\n') == 'this is a string'
    assert from_yaml('this is a string\n\n') == 'this is a string'
    assert from_yaml('this is a string\n\n\n') == 'this is a string'

    # very simple list
    list_input = '''- one
- two'''
    expected_output = ['one', 'two']
    assert from_yaml(list_input) == expected_output

    # very simple dict
    dict_input = '''one: two'''
    expected_output = {'one': 'two'}
    assert from_yaml(dict_input) == expected_output

    # list of dicts
    list

# Generated at 2022-06-13 07:22:54.784668
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """

# Generated at 2022-06-13 07:23:05.039718
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test YAML functionality
    '''
    a_data = '''
---
a_string:
  name: timmy
'''
    try:
        from_yaml(a_data, json_only=True)
        assert False, "Expected Exception"
    except AnsibleParserError:
        pass
    json_like = from_yaml(a_data)
    assert 'a_string' in json_like
    assert json_like['a_string']['name'] == 'timmy'
    assert 'a_string' in from_yaml(a_data, json_only=False)
    assert 'a_string' in from_yaml(a_data, json_only=True)


# vim: filetype=python ts=4 sw=4 expandtab

# Generated at 2022-06-13 07:23:14.355419
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    import datetime, sys

    class TestAnsibleBaseYAMLObject(AnsibleBaseYAMLObject):
        yaml_loader = AnsibleLoader
        yaml_dumper = AnsibleDumper
        yaml_tag = u'!bar'
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __repr__(self):
            return "%s(a=%r, b=%r)" % (self.__class__.__name__, self.a, self.b)

    yaml.add_representer(TestAnsibleBaseYAMLObject, TestAnsibleBaseYAMLObject.to_yaml)
    yaml.add_

# Generated at 2022-06-13 07:23:20.987901
# Unit test for function from_yaml
def test_from_yaml():
    '''
    from_yaml - function test
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import pytest
    import os

    TESTFILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data')
    SIMPLE_JSON = os.path.join(TESTFILE_DIR, 'simple.json')
    SIMPLE_YAML = os.path.join(TESTFILE_DIR, 'simple.yml')


# Generated at 2022-06-13 07:23:29.512640
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.objects

    data = 'foo: 1\nbar: !vault |\n          $ANSIBLE_VAULT;1.2;AES256;testvault\n          38306136316233653539393566336164633262636663633030666464383134653339343530346538\n          32333466613761643236636265396664343136636634623430353938333261633762343137333962\n          333434336638393934363361666231640a353034313064353335303531383464363131656433356233\n'
    datastruct = from_yaml(data, vault_secrets=['testvault'])
    assert dat

# Generated at 2022-06-13 07:23:40.017181
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("42") == 42
    assert from_yaml("[ 42, 43, 44]") == [42, 43, 44]
    assert from_yaml('{"foo": "bar", "baz": 42}') == {"foo": "bar", "baz": 42}

    assert from_yaml("foo: bar") == {"foo": "bar"}
    assert from_yaml("foo: {bar: baz}") == {"foo": {"bar": "baz"}}

    assert from_yaml("foo: bar", json_only=True)

# Generated at 2022-06-13 07:23:43.859305
# Unit test for function from_yaml
def test_from_yaml():
    ''' testing from_yaml '''
    from ansible.parsing.yaml import objects

    data = u"""
foo:
  - {host: localhost, port: 6379, state: present}
  - {host: test, port: 6379, state: present, slave_priority: 10, slave_repl_offset: 1}
  - {host: example, port: 8000, state: absent}
  - {host: example2, state: absent}
  - {host: example, port: 8000, state: absent, slaveof: example2 6379}
  """

    ds = from_yaml(data)
    assert isinstance(ds['foo'][0], dict)
    assert isinstance(ds['foo'][1], objects.AnsibleMapping)

# Generated at 2022-06-13 07:23:48.723060
# Unit test for function from_yaml
def test_from_yaml():

    # Example from_yaml call from modules/utilities/logic/async_wrapper.py
    assert from_yaml("{'foo': 'bar'}", '/file/path', False) == {'foo': 'bar'}

# Generated at 2022-06-13 07:23:59.589335
# Unit test for function from_yaml
def test_from_yaml():
    test_yaml_content = '''
    - hosts: localhost
      tasks:
      - name: fail
        fail:
          msg: "This task is supposed to fail"
      - debug:
          var: ignored_var
      - fail:
          msg: "This task is supposed to fail if ran on a host which is not localhost"
        when: not (inventory_hostname == 'localhost')
      rescue:
      - debug:
          var: failed_hosts
        when: "'127.0.0.1' in failed_hosts"
      - debug:
          var: "failed_hosts|length == 0"
      always:
      - debug:
          var: "failed_hosts|length == 0"
    '''


# Generated at 2022-06-13 07:24:08.751427
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Run basic tests on the from_yaml function.
    '''
    import os
    import tempfile
    import shutil

    # Setup a temporary directory to test with
    cwd = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    #os.chdir(tmpdir)

    # Setup data to use for tests
    data = {
        'a': 'b',
        'b': '1',
        'c': '2',
        'd': {
            'e': 'f',
            'g': 'h'
        }
    }
    data2 = '''
a: b
b: 1
c: 2
d:
    e: f
    g: h
'''


# Generated at 2022-06-13 07:24:19.922345
# Unit test for function from_yaml
def test_from_yaml():
    data = " I am not YAML or JSON"
    file_name = '<string>'
    show_content = True
    vault_secrets = None
    json_only = False
    new_data = from_yaml(data, file_name = file_name, show_content = show_content, vault_secrets = vault_secrets, json_only = json_only)
    assert new_data == " I am not YAML or JSON"
    data2 = "I am not YAML or JSON"
    new_data2 = from_yaml(data2, file_name = file_name, show_content = show_content, vault_secrets = vault_secrets, json_only = json_only)
    assert new_data2 == "I am not YAML or JSON"

# Generated at 2022-06-13 07:24:30.781342
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.dataloader

    test_yaml = '''{
        "foo": "bar",
        "baz": "quux",
    }'''

    assert ansible.parsing.dataloader.from_yaml('{}') == {}
    assert ansible.parsing.dataloader.from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert ansible.parsing.dataloader.from_yaml(test_yaml) == {"foo": "bar", "baz": "quux"}

# Generated at 2022-06-13 07:24:38.286701
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    {
        'foo': 'bar',
        'baz': {
            'foo': 'bar'
        }
    }
    '''
    data_no_fail = '''
    {
        'foo': 'bar',
        'baz': {
            'foo': 'bar'
        }
    }
    '''
    data_bad = '''
    {
        foo: bar,
        'baz': {
            'foo': 'bar'
        }
    }
    '''
    bad_data = from_yaml(data, json_only=True)
    assert bad_data is None
    data_no_fail = from_yaml(data_no_fail, json_only=True)
    assert data_no_fail is not None

# Generated at 2022-06-13 07:24:45.362128
# Unit test for function from_yaml
def test_from_yaml():
    yaml_data = {'foo': 'bar', 'blip': 'blop'}
    assert yaml_data == from_yaml(json.dumps(yaml_data), json_only=True)

    yaml_data = '''
        foo: bar
        blip: blop
    '''
    assert from_yaml(json.dumps(yaml_data)) == from_yaml(yaml_data)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:53.308203
# Unit test for function from_yaml
def test_from_yaml():
    # test for a standalone object
    yaml_text = (
        "---\n"
        "st_mode: 0600\n"
        "owner: user\n"
        "group: group\n"
        "type: file\n"
    )
    expected_dict = {u'st_mode': 600, u'owner': u'user', u'group': u'group', u'type': u'file'}
    assert(from_yaml(yaml_text) == expected_dict)

    # test for an object within a list
    yaml_text = (
        "---\n"
        "- st_mode: 0600\n"
        "  owner: user\n"
        "  group: group\n"
        "  type: file\n"
    )

# Generated at 2022-06-13 07:25:02.535971
# Unit test for function from_yaml
def test_from_yaml():

    # Test 1
    data = '{"name": "user", "state": "present", "comment": "Cannot run as root"}'
    file_name = 'test.json'
    show_content = True
    vault_secrets = None
    json_only = True

    new_data_test1 = from_yaml(data, file_name, show_content, vault_secrets, json_only)

    if isinstance(new_data_test1, dict) and 'name' in new_data_test1:
        test_1 = True
    else:
        test_1 = False
        print("Test 1 failed")

    # Test 2
    data = '{"name": "user", "state": "present", "comment": "Cannot run as root"}'
    file_name = 'test.json'
    show_

# Generated at 2022-06-13 07:25:11.382567
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    # Check if from_yaml can handle empty data
    assert from_yaml('', loader.load_from_file, file_name='', show_content=True, vault_secrets=None, json_only=False) == {}, "from_yaml should handle empty data"

    # Check if from_yaml can handle JSON data
    assert from_yaml('{"a": 1}', loader.load_from_file, file_name='', show_content=True, vault_secrets=None, json_only=False) == {u'a': 1}, "from_yaml should handle JSON data"

    # Check if from_yaml can handle YAML data

# Generated at 2022-06-13 07:25:17.993840
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('a: 1') == {'a': 1}

if __name__ == "__main__":
    assert from_yaml('a: 1') == {'a': 1}

# Generated at 2022-06-13 07:25:21.400338
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{"tasks": [{"shell": "echo hello"}]}'))
    try:
        from_yaml('{"tasks": [{"shell": "echo hello"}]}', json_only=True)
    except AnsibleParserError as e:
        print(e)
    try:
        from_yaml('shell: echo hello')
    except AnsibleParserError as e:
        print(e)

# Generated at 2022-06-13 07:25:26.201727
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    vault_secrets = VaultLib([])

    # test valid json
    test_json_str = '{"key_1": "value", "key_2": "value"}'
    assert from_yaml(test_json_str, vault_secrets=vault_secrets) == {'key_1': 'value', 'key_2': 'value'}

    # test valid yaml
    test_yaml_str = """
    key_1: value
    key_2: value
    """
    assert from_yaml(test_yaml_str, vault_secrets=vault_secrets) == {'key_1': 'value', 'key_2': 'value'}

    # test invalid json

# Generated at 2022-06-13 07:25:33.813891
# Unit test for function from_yaml
def test_from_yaml():
    print("from_yaml")
    # Test just JSON
    data = '''{
    "a": 1,
    "b": 2,
    "c": 3
    }'''

    result = from_yaml(data, json_only=True)
    assert result == {"a": 1, "b": 2, "c": 3}, result

    # Test just YAML
    data = '''a: 1
b: 2
c: 3
'''

    result = from_yaml(data)
    assert result == {"a": 1, "b": 2, "c": 3}, result

    # Test JSON and YAML
    data = '''{
    "a": 1,
    "b": 2,
    "c": 3
    }'''

    result = from_yaml(data)

# Generated at 2022-06-13 07:25:43.452501
# Unit test for function from_yaml
def test_from_yaml():
    # Case 1: Yaml file is loaded as a list
    yaml_data = '''
- name: Lovelace, Ada
- name: Lovelace, Annabella
- name: Turing, Alan
- name: Lovelace, Byron
'''
    data = from_yaml(yaml_data)
    assert [['name', 'Lovelace, Ada'], ['name', 'Lovelace, Annabella'], ['name', 'Turing, Alan'], ['name', 'Lovelace, Byron']] == data

    # Case 2: Yaml file is loaded as a dict
    yaml_data = '''
    attributes:
    - name: Lovelace, Ada
    - name: Lovelace, Annabella
    - name: Turing, Alan
    - name: Lovelace, Byron
'''
    data = from_

# Generated at 2022-06-13 07:25:47.352955
# Unit test for function from_yaml
def test_from_yaml():
    import tempfile
    import textwrap

    tmp_fd, tmp_path = tempfile.mkstemp()
    try:
        with open(tmp_path, 'w') as tmp:
            tmp.write(textwrap.dedent('''
                ---
                foo: 10
                bar:
                  baz: 20
            '''))

        data = from_yaml(tmp_path)
        assert isinstance(data, dict)
        assert data['foo'] == 10
        assert isinstance(data['bar'], dict)
        assert data['bar']['baz'] == 20

    finally:
        os.unlink(tmp_path)

# Generated at 2022-06-13 07:25:57.944696
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    # The dir that contains this file
    org_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(org_dir, '../../test/unit/parsing/yaml/')
    # print(test_dir)
    os.chdir(test_dir)
    # print(os.getcwd())
    for file_name in os.listdir(test_dir):
        if file_name == '__init__.py' or file_name[-3:] != '.py':
            continue
        mod_name = file_name[:-3]
        # print(mod_name)
        mod = __import__(mod_name)
        # print(mod)

# Generated at 2022-06-13 07:26:12.067277
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.module_utils._text import to_text
    with pytest.raises(AnsibleParserError):
        assert from_yaml("a", "test")

    assert from_yaml("", "test") == ""
    assert from_yaml("test", "test") == "test"
    assert from_yaml("[test]", "test") == ["test"]
    assert from_yaml(to_text("[test]"), "test") == ["test"]
    assert from_yaml("{test: test}", "test") == {"test":"test"}
    assert from_yaml("[{test: test}]", "test") == [{"test":"test"}]

# Generated at 2022-06-13 07:26:19.409056
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'k1': 'v1', 'k2': 'v2'}"
    file_name = 'test'
    show_content = True
    vault_secrets = None
    json_only = False
    expected = {'k1': 'v1', 'k2': 'v2'}
    actual = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert expected == actual

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:26:26.229544
# Unit test for function from_yaml
def test_from_yaml():
    str1 = """
        {
            "name": "test",
            "foo": [
                "bar",
                "baz"
            ]
        }
        """

    import ansible.parsing.dataloader
    dl = ansible.parsing.dataloader.DataLoader()
    ret = from_yaml(str1)
    assert ret['name'] == "test"
    assert ret['foo'][0] == "bar"
    assert ret['foo'][1] == "baz"

# Generated at 2022-06-13 07:26:41.590788
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit tests for parser.json.from_yaml
    '''
    from ansible.parsing.dataloader import DataLoader

    test_loader = DataLoader()

    def _assert_valid_yaml(yaml_str, expected_data, file_name='<data>'):
        res_data = from_yaml(yaml_str, file_name=file_name)
        assert expected_data == res_data


# Generated at 2022-06-13 07:26:50.706074
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError

    data_loader = DataLoader()

    # JSON
    input_json = data_loader.load_from_file('./test/units/parsing/data/json_string.json')
    output_json = json.loads(input_json)
    assert from_yaml(input_json, json_only=True) == output_json

    # YAML
    input_yaml = data_loader.load_from_file('./test/units/parsing/data/yaml_string.yaml')
    output_yaml = data_loader.load('./test/units/parsing/data/yaml_string.yaml')

# Generated at 2022-06-13 07:27:00.630494
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml('[1,2,3]')
    except AnsibleParserError as e:
        assert False, 'We were unable to parse a json list'

    try:
        from_yaml('key: value')
    except AnsibleParserError as e:
        assert False, 'We were unable to parse a simple key value'

    try:
        from_yaml('''
        key: value
        another: value
        ''')
    except AnsibleParserError as e:
        assert False, 'We were unable to parse a simple key value as yaml'

    try:
        from_yaml('{ "key": "value" }')
    except AnsibleParserError as e:
        assert False, 'We were unable to parse a simple key value as yaml'


# Generated at 2022-06-13 07:27:09.961420
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import stat
    import tempfile
    import logging
    import shutil
    import subprocess
    import unittest

    try:
        import unittest.mock as mock
    except Exception:
        import mock

    from ansible import constants as C

    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar

    from ansible.module_utils.six import string_types


# Generated at 2022-06-13 07:27:15.696622
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "some": "json"}') == {"some": "json"}
    assert from_yaml('some: yaml') == {"some": "yaml"}
    assert from_yaml('invalid', json_only=True) == None
    assert from_yaml('{ "some": "json",') == None
    assert from_yaml('some: "yaml"') == {"some": "yaml"}


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:27:21.818765
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.yaml.dumper import AnsibleDumper

    c1 = to_native("""
---
a: 'b'
""")

    data, errors = from_yaml(c1)
    assert data['a'] == 'b'
    assert errors is None

    c2 = to_native("""!a 'b'""")

    data, errors = from_yaml(c2)
    assert data == 'b'
    assert errors is None

    # github issue #20792
    d = {"str_with_null": "A\x00B"}
    c = to_native(json.dumps(d))


# Generated at 2022-06-13 07:27:35.533210
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    import os
    import sys

    file_name = os.path.join(os.path.dirname(__file__), 'test_from_yaml.yml')
    try:
        with open(file_name, 'r') as f:
            data = f.read().encode('utf-8')
    except IOError as e:
        print('ERROR: could not open file %s: %s' % (file_name, e))
        sys.exit(1)

    vault_secrets = {}