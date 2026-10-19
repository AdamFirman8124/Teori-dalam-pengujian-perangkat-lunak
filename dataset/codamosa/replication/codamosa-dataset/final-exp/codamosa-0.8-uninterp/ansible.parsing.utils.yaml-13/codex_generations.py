

# Generated at 2022-06-13 07:17:36.454776
# Unit test for function from_yaml
def test_from_yaml():
    # Test JSON data
    data = '{"test": "json"}'
    expected_output = {u'test': u'json'}
    result = from_yaml(data)
    assert result == expected_output

    # Test YAML data
    data = 'test: yaml'
    expected_output = {u'test': u'yaml'}
    result = from_yaml(data)

    # Test invalid JSON data
    data = '{"test": json'
    expected_output = u'We were unable to read either as JSON nor YAML, these are the errors we got from each:\n' \
                      'JSON: Unterminated string starting at: line 1 column 14 (char 13)'
    try:
        from_yaml(data)
    except Exception as e:
        assert str(e) == expected_output

# Generated at 2022-06-13 07:17:37.977175
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": "b"}') == {'a': 'b'}

# Generated at 2022-06-13 07:17:40.671139
# Unit test for function from_yaml
def test_from_yaml():
    data = """
    ---
    foo: bar
    """

    d = from_yaml(data)
    assert d == {'foo': 'bar'}

# Generated at 2022-06-13 07:17:49.141219
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible import module_utils


# Generated at 2022-06-13 07:17:53.107900
# Unit test for function from_yaml
def test_from_yaml():
    # In here we can test it and assert whether we get the correct output.
    print("Testing from_yaml function")
    from_yaml('{"testvar":"testvar"}')
    print("Test OK")


# Test
#test_from_yaml()

# Generated at 2022-06-13 07:18:02.409359
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("") == {}
    assert from_yaml("foo") == "foo"
    assert from_yaml("1") == 1
    assert from_yaml("[1,2,3]") == [1,2,3]
    assert from_yaml("{}") == {}
    assert from_yaml("a: 1") == {"a": 1}
    assert from_yaml(u"a: 1") == {"a": 1}
    assert from_yaml("a: 1\nb: 2") == {"a": 1, "b": 2}
    assert from_yaml("# foo") == None
    assert from_yaml("---\n# foo") == None
    assert from_yaml("---\nfoo") == "foo"
    assert from_yaml("--- foo") == "foo"

# Generated at 2022-06-13 07:18:12.580703
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    # insert this directory into the module import path
    mydir = os.path.dirname(__file__)
    if not mydir in sys.path:
        sys.path.insert(0, mydir)
    # now import our library
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedOpaque
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.errors.yaml_strings import YAML_SYNTAX_ERROR

    mydata = "---\n"
    mydata += "string: 'this is a string'\n"

# Generated at 2022-06-13 07:18:23.921870
# Unit test for function from_yaml
def test_from_yaml():
    fields = {}
    fields['arg'] = {'type': 'dict', 'default': {}}
    fields['arg']['default']['foo'] = 'bar'
    fields['arg']['default']['bar'] = True
    fields['arg']['default']['baz'] = '123'
    fields['arg']['default']['none'] = None
    fields['arg']['default']['nested'] = {'n1': 'v1'}
    fields['arg']['default']['nested']['n2'] = {'nn1': 'vv1'}
    fields['arg']['default']['list'] = [1, 2, 3]
    fields['arg']['default']['list'].append({'li1': 'lv1'})
   

# Generated at 2022-06-13 07:18:33.615005
# Unit test for function from_yaml
def test_from_yaml():
    ''' Does the from_yaml function work? '''

    from ansible.parsing.vault import VaultLib

    # Some basic YAML
    from_yaml.ansible_test_data = """
    - [ "item1", "item2" ]
    - { key1: value1, key2: value2 }
    """

    assert isinstance(from_yaml(from_yaml.ansible_test_data), list)

    # Some basic JSON
    from_yaml.ansible_test_json = '''{"ansible": "2.2"}'''

    assert isinstance(from_yaml(from_yaml.ansible_test_json), dict)

    # Test vault functionality

# Generated at 2022-06-13 07:18:41.764921
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    vault_password = '$ecretP@ssw0rd!'
    vault = VaultLib(vault_password)
    sample_yaml = """
vault_encrypted_data: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          34336437663332663566346462333936343866376430333464353733383562313731396234363964
          3964366531333164340a343865643361633861643934643033376435343163323661623862326130
          633835303664333165386361320a
"""

# Generated at 2022-06-13 07:18:51.509392
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": "b", "c": "d"}') == {u'a': u'b', u'c': u'd'}
    assert from_yaml("a: b\nc: d") == {u'a': u'b', u'c': u'd'}
    assert from_yaml("a: b\nc: d\n  e: f") == {u'a': u'b', u'c': {u'e': u'f'}}

# Generated at 2022-06-13 07:18:59.742633
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("test: test\n"
                     "name: example\n") == {"test": "test", "name": "example"}
    assert from_yaml("test: test\n"
                     "name: example\n",
                     vault_secrets=['12345678']) == {"test": "test", "name": "example"}
    assert from_yaml("[0, 1, 2, 3]") == [0, 1, 2, 3]
    assert from_yaml("{0: 0, 1: 1, 2: 2}") == {0: 0, 1: 1, 2: 2}
    assert from_yaml("name: example") == {"name": "example"}
    assert from_yaml("name: example\n"
                     "name: another example\n") == {"name": "another example"}

# Generated at 2022-06-13 07:19:06.295389
# Unit test for function from_yaml
def test_from_yaml():
    #from ansible.parsing import vars_from_file
    #from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible import context
    #from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    #v = vars_from_file('/etc/ansible/hosts')
    #print(v)
    #return

    #v2 = {'hosts':"static", 'roles':'v2', 'restore_files':'v2'}

    #print(to_yaml(v2))
    #return


    v = {'hosts':"static", 'roles':'v1', 'restore_files':'v1'}
    print(to_yaml(v))
    j

# Generated at 2022-06-13 07:19:13.153517
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('''
---
- hosts: localhost
  tasks:
    - debug: msg="Hi"
''') == [
    {
        'hosts': 'localhost',
        'tasks': [
            {
                'debug': {
                    'msg': 'Hi',
                }
            }
        ]
    }
]

# Generated at 2022-06-13 07:19:19.804524
# Unit test for function from_yaml
def test_from_yaml():
    iq = '''{
    "hosts": ["localhost","remote01","remote02"],
    "vars": {
        "example_var": "value"
    }
}'''
    assert from_yaml(iq, json_only=True) == {"hosts": ["localhost","remote01","remote02"], "vars": { "example_var": "value" } }

# Generated at 2022-06-13 07:19:22.909411
# Unit test for function from_yaml
def test_from_yaml():
    yaml_mydict = '''
a: 1
key:
  group: test
  hosts:
    host1:
      ansible_host: 10.10.10.10
    host2:
      ansible_host: 10.10.10.11
  vars:
    a: 1
    b: 2
    c: 3
'''
    from_yaml(yaml_mydict)


# Generated at 2022-06-13 07:19:30.746795
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test the from_yaml function, test that it can parse JSON and YAML
    correctly.
    '''

    import functools

    # These tests are in the format of a tuple, (success, data, expected output)
    # True indicates that the test expects a successful parse of data.
    # The data is what will be parsed, and the expected output is the expected
    # result of the parse.  Any errors will raise a ValueError exception with
    # the contents of error.

# Generated at 2022-06-13 07:19:41.974522
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.errors import AnsibleParserError
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import is_encrypted
    from ansible.parsing.vault import VaultSecret

    data = '''
foo:
  bar:
    baz:
    - "10"
    - "11"
    - "12"
'''

    data_json = '{"foo": {"bar": {"baz": ["10", "11", "12"]}}}'
    data_yaml = '''
foo:
  bar:
    baz:
      - "10"
      - "11"
      - "12"
'''

    results = from_yaml(data_yaml)
    assert results == json.loads(data_json)
    results = from_

# Generated at 2022-06-13 07:19:49.159393
# Unit test for function from_yaml
def test_from_yaml():
    data = "* test string "
    file_name = '/file/name'
    show_content = True
    vault_secrets = 'test_vault_secrets'
    json_only = False
    new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert isinstance(new_data, list)
    assert new_data[0] == 'test string'

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:50.625068
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("foobar", json_only=True), str)
    assert from_yaml("foobar") == "foobar"

# Generated at 2022-06-13 07:20:02.492823
# Unit test for function from_yaml
def test_from_yaml():
    ''' Test the from_yaml function '''

    data1 = '''
    foo: This is the first line
      - This is the second
      - This is the third
    '''

    data2 = '''
    foo: "This is the first line
      - This is the second
      - This is the third
    '''

    data3 = '''
    foo: "This is the first line
      - This is the second
      - This is the third"
    '''

    data4 = '''
    foo: This is the first line
      - "This is the second"
      - This is the third
    '''

    data5 = '''
    foo: This is the first line
      - {'This is the second': "This is the third"}
      - This is the fourth
    '''

    data

# Generated at 2022-06-13 07:20:06.909062
# Unit test for function from_yaml
def test_from_yaml():
    assert json.loads(from_yaml('{"example": "value 1"}')) == {"example": "value 1"}
    assert json.loads(from_yaml('{"example": "value 2"}', json_only=True)) == {"example": "value 2"}
    assert json.loads(from_yaml("example: value 3")) == {"example": "value 3"}
    assert json.loads(from_yaml("example: value 4", json_only=True)) == {"example": "value 4"}

# Generated at 2022-06-13 07:20:17.649690
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import BytesIO
    from ansible.parsing.yaml.dumper import AnsibleDumper

    output = 'foo: bar'

    data = from_yaml(BytesIO(output), '<string>', show_content=True)
    assert data == {u'foo': u'bar'}

    data = from_yaml(BytesIO(output), '<string>', json_only=True)
    assert data is None

    o = {u'foo': u'bar'}

    assert json.loads(json.dumps(o, cls=AnsibleJSONDecoder)) == o

    data = json.loads(json.dumps(o, cls=AnsibleJSONDecoder))
    assert data == o


# Generated at 2022-06-13 07:20:19.885158
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 07:20:27.952459
# Unit test for function from_yaml
def test_from_yaml():
    dict = from_yaml("var: 1")
    assert dict == {u'var': 1, '__ansible_vault': None}
    dict = from_yaml("var: 1", json_only=True)
    assert dict == {'var': 1}
    dict = from_yaml("var: 1", vault_secrets=[{"token": "sometoken", "vault_id": "vault1"}])
    assert dict == {u'var': 1, '__ansible_vault': {'vault1': None}}
    dict = from_yaml("var: 1", vault_secrets=[{"token": "sometoken", "vault_id": "vault1"}], json_only=True)
    assert dict == {'var': 1}

# Generated at 2022-06-13 07:20:36.759998
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.ajson import AnsibleJSONEncoder

    good_json_str = json.dumps({'name': 'John'}, cls=AnsibleJSONEncoder)
    good_yaml_str = 'name: John\n'
    good_json_str_with_comments = json.dumps({'#name': 'John', 'name': 'John'}, cls=AnsibleJSONEncoder)

    for s in (good_json_str,
              good_yaml_str,
              good_json_str_with_comments):
        assert from_yaml(s) == {'name': 'John'}

# Generated at 2022-06-13 07:20:47.242244
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml(""), dict)
    assert isinstance(from_yaml("{}"), dict)
    assert isinstance(from_yaml("[]"), list)
    assert isinstance(from_yaml('{"h": "a", "b": {"s": "p"}, "q": [3, 4, 5]}'), dict)
    assert isinstance(from_yaml('{"h": "a", "b": "test"}', json_only=True), dict)
    assert from_yaml('{"h": "a", "b": "test"}', json_only=True) == {'h': 'a', 'b': 'test'}
    assert from_yaml('h: "a"\nb: "test"') == {'h': 'a', 'b': 'test'}
    assert from_yaml

# Generated at 2022-06-13 07:20:51.111177
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml(data=data, file_name=file_name, show_content=show_content, vault_secrets=vault_secrets, json_only=json_only)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:20:53.242130
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"hello": "world"}') == {'hello': 'world'}

# Generated at 2022-06-13 07:21:03.107508
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import datetime

    fy = from_yaml

    # dict
    assert isinstance(fy('{}'), dict)
    assert isinstance(fy('{}')[0], AnsibleMapping)
    assert isinstance(fy('foo: bar'), dict)
    assert isinstance(fy('foo: bar')[0], AnsibleMapping)

    # list
    assert isinstance(fy('[]'), list)
    assert isinstance(fy('[]')[0], AnsibleSequence)

# Generated at 2022-06-13 07:21:12.429423
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    # json to dict
    data = '{"name": "foo"}'
    assert isinstance(dl.load_from_file(data=data), dict)
    # yaml to dict
    data = '---\nname: "foo"'
    assert isinstance(dl.load_from_file(data=data), dict)

# Generated at 2022-06-13 07:21:14.682967
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("[1, 2]") == [1, 2]
    assert from_yaml("{a: b}") == {'a': 'b'}
    assert from_yaml("'''[1, 2]'''") == '[1, 2]'
    assert from_yaml("'''{a: b}'''") == '''{a: b}'''

# Generated at 2022-06-13 07:21:23.481670
# Unit test for function from_yaml
def test_from_yaml():

    # Test 'Simple' JSON
    ret = from_yaml('{"a": "b"}')
    assert isinstance(ret, dict), 'JSON obj missing'
    assert ret['a'] == 'b', 'JSON missing val'

    # Test 'Simple' YAML
    ret = from_yaml('a: b')
    assert isinstance(ret, dict), 'YAML obj missing'
    assert ret['a'] == 'b', 'YAML missing val'

    # Test 'Simple' JSON/YAML
    ret = from_yaml('{"a": "b"}', json_only=True)
    assert isinstance(ret, dict), 'JSON obj missing'
    assert ret['a'] == 'b', 'JSON missing val'

    # Test 'Simple' JSON/YAML

# Generated at 2022-06-13 07:21:30.888806
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.vars import combine_vars
    from ansible.utils.vault import VaultLib
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.vault import VaultSecret, VaultAES256
    import sys

    input_yaml = '''
---
test_var:
  - var1
  - var2
  - var3
'''
    secrets = VaultSecret(VaultAES256())
    v = VaultLib([(secrets, 'password')])
    vars_manager = combine_vars(loader=None, variables=dict(), include_vars=None)
    input_var = vars_manager._add_host_vars_from_inventory(host=None, hostvars=dict())

# Generated at 2022-06-13 07:21:35.968895
# Unit test for function from_yaml
def test_from_yaml():
    '''
    AnsibleParserError should be raised when specified file is not
    readable.
    '''
    try:
        from_yaml(__file__)
    except AnsibleParserError as e:
        print('%s: %s' % (e.__class__.__name__, e))
        print('test_from_yaml succeeded')

# Generated at 2022-06-13 07:21:42.109291
# Unit test for function from_yaml
def test_from_yaml():


    data = '''
    {
    'key1': 'value'
    }
    '''

    new_data = from_yaml(data)
    assert new_data == {'key1': 'value'}


    data = '''
    {
    key: 'value'
    }
    '''

    new_data = from_yaml(data)
    assert new_data == {'key': 'value'}


    data = '''
    key: 'value'
    '''

    new_data = from_yaml(data)
    assert new_data == {'key': 'value'}


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:43.758187
# Unit test for function from_yaml
def test_from_yaml():
    data = ""
    with open("test.yaml") as f:
        data = f.read()
    from_yaml(data)

# Generated at 2022-06-13 07:21:53.404750
# Unit test for function from_yaml
def test_from_yaml():
    test_yaml_1 = '''
    ---
    - hosts: localhost
      tasks:
      - name: test task 1
        ping:
      - name: test task 2
        debug:
            msg: "hello world!"
    '''

    test_json_1 = '''
    {"hosts": "localhost", "tasks": [{"name": "test task 1", "ping": ""}, {"name": "test task 2", "debug": {"msg": "hello world!"}}]}
    '''

    test_yaml_2 = '''
    ---
    - hosts: localhost
      tasks:
      - name: test task 1
        ping:
      - name: test task 2
        debug:
            msg: "hello world!"
'''


# Generated at 2022-06-13 07:21:55.892268
# Unit test for function from_yaml
def test_from_yaml():
    expected_result = {'foo': 'bar'}
    new_data = from_yaml("foo: bar", file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert new_data == expected_result

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:22:01.828594
# Unit test for function from_yaml
def test_from_yaml():
    yaml.register_class(TestingYamlObject)
    assert from_yaml("test_var: !testing_yaml_object 'test_value'\n", file_name='file', show_content=True) == dict(test_var=TestingYamlObject('test_value'))
    yaml.unregister_class(TestingYamlObject)


# Generated at 2022-06-13 07:22:12.558385
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    data = '{ "test_json" : 1 }'
    data_parsed = from_yaml(data)
    assert data_parsed == json.loads(data)

    data = 'test_yaml: 1'
    data_parsed = from_yaml(data)
    assert data_parsed == {'test_yaml': 1}

    data = '{ json: 1 }'
    try:
        data_parsed = from_yaml(data)
    except AnsibleParserError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 07:22:19.982597
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml_json = from_yaml('{"foo": "bar"}')
    assert from_yaml_json == {"foo": "bar"}

    from_yaml_yaml = from_yaml('foo: bar')
    assert from_yaml_yaml == {'foo': 'bar'}

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:22:23.546046
# Unit test for function from_yaml
def test_from_yaml():
    test_input = "{'key': 'value'}"
    assert from_yaml(test_input)['key'] == 'value'
    assert from_yaml(test_input, json_only=True) is None

# Generated at 2022-06-13 07:22:29.294095
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.collections import ImmutableDict
    file_name = '<string>'
    show_content = True
    vault_secrets = None
    json_only = False
    yml_str = '''
- hosts: localhost
  tasks:
  - debug:
      msg: "Hello World!"
  - name: "Print the supplied variable"
    debug:
      msg: "The variable X contains {{ x }}"
    vars:
      x: "Goodbye World!"
'''
    try: 
        result = from_yaml(yml_str)
    except Exception as err:
        assert(False)


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:39.807000
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"foo":"bar"}'
    assert from_yaml(data, show_content=False) == {"foo":"bar"}
    
    data = '{"foo": bar}'
    assert from_yaml(data, show_content=False) == {"foo":"bar"}
    
    data = '{"foo": "bar"}'
    assert from_yaml(data, show_content=False) == {"foo":"bar"}
    
    data = {"foo": "bar"}
    assert from_yaml(data, show_content=False) == {"foo":"bar"}
    
if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:46.422968
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('{foo: bar}') == {'foo': 'bar'}
    assert from_yaml('{foo: 3}') == {'foo': 3}
    assert from_yaml('{foo: 3.14}') == {'foo': 3.14}
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 07:22:54.178034
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"key" : "value"}') == json.loads('{"key" : "value"}')
    assert from_yaml('{"key" : "value"}') != json.loads('{"key" : "VALUE"}')
    assert from_yaml('{"key" : "value"}') != json.loads('{"key" : "value","key2" : "value"}')
    assert from_yaml('{"key" : "value"}') != json.loads('{"key" : "value","key2" : "value"}')



# Generated at 2022-06-13 07:23:04.572445
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Runs the test suite for the from_yaml function
    '''

    import unittest
    from ansible.parsing.ajson import AnsibleJSONDecoder

    class TestFromYaml(unittest.TestCase):
        def setUp(self):
            AnsibleJSONDecoder.set_secrets(None)

        def test_from_json(self):

            # Test valid json
            json_input = b'{"test_key":"test_value"}'
            json_output = from_yaml(json_input, json_only=True)
            self.assertEqual(json_output, {"test_key": "test_value"})

            # Test invalid json
            # When parsing from yaml, we first attempt parsing from json, and
            # if that fails we fallback to yaml.  This

# Generated at 2022-06-13 07:23:14.090023
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing import vault
    from ansible.parsing.yaml import objects

    p = vault.VaultSecret('password')

    data = {
        'hello': 'world',
        'a': 1,
        'b': 2,
        'c': [1, 2, 3],
        'd': {'e': 'f'},
        'password': p.get_secret(),
    }
    d = {'a': 1, 'b': 2, 'c': [1, 2, 3], 'd': {'e': 'f'}, 'hello': 'world', 'password': u'asdf'}

    # test dumps of data_structure

# Generated at 2022-06-13 07:23:19.377086
# Unit test for function from_yaml
def test_from_yaml():
    test_yaml = '''
hosts:
  - group1:
      key1: value1
      key2: value2
  - group2:
      key1: value1
      key2: value2
'''
    test_json = '''{"hosts": [{"group1": {"key1": "value1", "key2": "value2"}}, {"group2": {"key1": "value1", "key2": "value2"}}]}'''
    assert from_yaml(test_yaml) == from_yaml(test_json)

# Generated at 2022-06-13 07:23:37.754472
# Unit test for function from_yaml
def test_from_yaml():
    json_1 = """{
    "ansible_facts": {
        "ansible_distribution": "debian",
        "ansible_distribution_major_version": "8",
        "ansible_distribution_release": "jessie",
        "ansible_distribution_version": "8.0"
    },
    "changed": false
}"""
    assert from_yaml(json_1) == json.loads(json_1)

    json_2 = """{"changed": false, "ansible_facts": {
    "ansible_distribution_version": "8.0",
    "ansible_distribution": "debian",
    "ansible_distribution_release": "jessie",
    "ansible_distribution_major_version": "8"
    }}"""
    assert from_yaml

# Generated at 2022-06-13 07:23:47.049399
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY2
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Test the "is JSON" case
    data = {'foo': 'bar'}

    # The resulting data should be the same
    result = from_yaml(json.dumps(data))
    assert result == data

    # Test the "is YAML" case
    data = 'foo: bar'

    # The resulting data should be the same
    result = from_yaml(data)
    assert result == {'foo': 'bar'}

    # Test the "is YAML" case with unicode value
    data = u'foo: \u20ac'

    # The resulting data should be the same
    result = from_yaml(data)
   

# Generated at 2022-06-13 07:23:49.016455
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"key": "value"}'
    func_data = from_yaml(data)
    assert func_data == {u'key': u'value'}

# Generated at 2022-06-13 07:23:59.969377
# Unit test for function from_yaml
def test_from_yaml():
  assert from_yaml("""{
    "username": "bob",
    "password": "123",
    "mfa_serial": "arn:aws:iam::123456:mfa/bob",
    "region": "us-east-1"
  }""") == {'password': '123', 'username': 'bob', 'region': 'us-east-1', 'mfa_serial': 'arn:aws:iam::123456:mfa/bob'}


# Generated at 2022-06-13 07:24:07.589597
# Unit test for function from_yaml
def test_from_yaml():
    x = from_yaml('{ "a": 1 }')
    assert (x['a'] == 1)
    # from_yaml should not load non-JSON strings as JSON
    x = from_yaml('foo')
    assert (x is None)
    # from_yaml should load proper JSON strings
    x = from_yaml('"foo"')
    assert (x == 'foo')
    # from_yaml should load proper JSON strings that can be loaded as JSON
    x = from_yaml('"true"')
    assert (x == 'true')

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:19.194488
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeVars

    res = from_yaml('{ "a": "b" }')
    assert res == {'a': 'b'}
    res = from_yaml('{ a: b }')
    assert res == {'a': 'b'}
    res = from_yaml('[ 1, 2, 3 ]')
    assert res == [1, 2, 3]
    res = from_yaml('---\n- 1\n- 2')
    assert res == [1, 2]

# Generated at 2022-06-13 07:24:33.426956
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultSecret

    vault1 = VaultSecret('$ANSIBLE_VAULT;1.1;AES256;foo\nbar\n')
    vault2 = VaultSecret('$ANSIBLE_VAULT;1.1;AES256;foo2\nbar2\n')

    vault_secrets = dict(foo=vault1, foo2=vault2)
    x = from_yaml('{ "test": "mytest" }', vault_secrets=vault_secrets)
    assert x == dict(test='mytest')

    x = from_yaml('{ "test": "{{ vault_secret }}" }', vault_secrets=vault_secrets)
   

# Generated at 2022-06-13 07:24:39.936337
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import from_yaml

    # Test a yaml file
    test_yaml = '''
- one
- two
- three
- four
- five
- six
- seven
- eight
- nine
- ten
'''

    new_yaml = from_yaml(test_yaml)

    assert type(new_yaml) == list
    assert new_yaml[0] == 'one'
    assert new_yaml[4] == 'five'

    # Test a json file
    test_json = '''
{
    "tool": "ansible",
    "lang": "python",
    "looks": "easy"
}
'''

    new_json = from_yaml(test_json)
    assert type(new_json) == dict
   

# Generated at 2022-06-13 07:24:50.187672
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    from lib.config import DATA_ROOT

    # JSON
    assert from_yaml('{}') == {}
    assert from_yaml('[]') == []
    assert from_yaml('false') is False
    assert from_yaml('null') is None
    assert from_yaml('1') == 1
    assert from_yaml('-10') == -10
    assert from_yaml('"foo"') == "foo"

    # JSON with whitespaces
    assert from_yaml('{\n}') == {}
    assert from_yaml('[\n1,\n2 ]') == [1, 2]
    assert from_yaml

# Generated at 2022-06-13 07:24:54.321337
# Unit test for function from_yaml
def test_from_yaml():
    yaml_data = '''
    eins: drei
    zwei: vier
    '''
    assert from_yaml(yaml_data) == {'zwei': 'vier', 'eins': 'drei'}

# Generated at 2022-06-13 07:25:15.037762
# Unit test for function from_yaml
def test_from_yaml():
    import pytest

    with pytest.raises(AnsibleParserError):
        from_yaml("1" * 3000)

    with pytest.raises(AnsibleParserError):
        from_yaml("---\n- 'foo'\nbar: 42")

# Generated at 2022-06-13 07:25:23.180397
# Unit test for function from_yaml
def test_from_yaml():

    # Parse JSON string
    json_string = '{"name": "Bob", "age": 43, "items": ["Sunscreen 200ml", "Hat"]}'
    data = from_yaml(json_string, file_name='<string>', show_content=False, vault_secrets=None, json_only=False)
    assert data == {u'age': 43, u'name': u'Bob', u'items': [u'Sunscreen 200ml', u'Hat']}

    # Parse YAML string
    yaml_string = '''
name: Bob
age: 43
items:
  - Sunscreen 200ml
  - Hat
'''
    data = from_yaml(yaml_string, file_name='<string>', show_content=False, vault_secrets=None, json_only=False)

# Generated at 2022-06-13 07:25:27.534522
# Unit test for function from_yaml
def test_from_yaml():
    yaml_string = "{a: 1, b: 2, c: 3, d: 4}"
    assert from_yaml(yaml_string) == {"a": 1, "b": 2, "c": 3, "d": 4}



# Generated at 2022-06-13 07:25:38.705476
# Unit test for function from_yaml
def test_from_yaml():
    data = """---
- {username: test, password: foo}
- {username: test2, password: foo2}
"""

    result = from_yaml(data)
    assert result == [{u'username': u'test', u'password': u'foo'}, {u'username': u'test2', u'password': u'foo2'}]

    data = """
- username: test
  password: foo

- username: test2
  password: foo2
"""

    result = from_yaml(data)
    assert result == [{u'username': u'test', u'password': u'foo'}, {u'username': u'test2', u'password': u'foo2'}]

# Generated at 2022-06-13 07:25:53.549089
# Unit test for function from_yaml
def test_from_yaml():
    data1 = '''
foo: 1
bar: 2
'''

    ydata = from_yaml(data1, file_name='<string>')
    assert ydata == {'bar': 2, 'foo': 1}

    data2 = '''
["foo", "bar"]
'''

    ydata = from_yaml(data2, file_name='<string>')
    assert ydata == ['foo', 'bar']


# Generated at 2022-06-13 07:26:00.812475
# Unit test for function from_yaml
def test_from_yaml():

    import StringIO

    # Test for valid JSON, this should just return
    assert from_yaml('{"valid_json": true}') == {"valid_json": True}

    # Test for valid YAML, this should just return
    assert from_yaml('valid_yaml: OK') == {"valid_yaml": "OK"}

    # Test for JSON containing an error, this should throw

# Generated at 2022-06-13 07:26:13.759616
# Unit test for function from_yaml
def test_from_yaml():
    import os
    from ansible.parsing.yaml import from_yaml, objects
    from ansible.parsing.vault import VaultLib
    from ansible.errors import AnsibleParserError
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_data1 = """
        ---
        name: 'Joe'
        age: 40
    """
    yaml_data2 = """
        ---
        name: 'Joe'
        age: 40
        fav_color: '{{ my_color }}'
    """

# Generated at 2022-06-13 07:26:24.685296
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'[1,2,3]') == [1,2,3]
    assert from_yaml(u'[1.1,2.2,3.3]') == [1.1,2.2,3.3]
    assert from_yaml(u'{"a1":1.1,"a2":2.2,"a3":3.3}') == {"a1":1.1,"a2":2.2,"a3":3.3}
    assert from_yaml(u'{"a1":1.1,"a2":2.2,"a3":"a3"}') == {"a1":1.1,"a2":2.2,"a3":"a3"}

# Generated at 2022-06-13 07:26:33.174198
# Unit test for function from_yaml
def test_from_yaml():
    '''
    test_from_yaml tests function from_yaml
    '''
    import os
    import os.path
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib

    try:
        import yaml
    except ImportError as e:
        yaml_found = False
    else:
        yaml_found = True

    # Unit test for function from_yaml

    yamlfile = """
        ---
        name:
        - file1
        - file2
        - file3
        """

    # from_yaml should return a list
    yaml_data = from_yaml(yamlfile)
    assert isinstance(yaml_data, list)

# Generated at 2022-06-13 07:26:44.330877
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
'''
    a = from_yaml(data)
    assert(a == [1,2,3,4,5,6,7,8,9])

    data = '''
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
'''
    a = from_yaml(data, json_only=True)
    assert(a == [1,2,3,4,5,6,7,8,9])

    data = '''
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
'''

# Generated at 2022-06-13 07:27:16.922402
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    # Test valid YAML
    assert from_yaml("a: value") == dict(a="value")
    assert from_yaml("a:\n  - b") == dict(a=["b"])
    assert from_yaml("{a: value}") == dict(a="value")
    assert from_yaml("[a, value]") == ["a", "value"]
    # Test invalid YAML
    with pytest.raises(AnsibleParserError):
        from_yaml("a: value\nc: value")
    with pytest.raises(AnsibleParserError):
        from_yaml("[a: value")
    with pytest.raises(AnsibleParserError):
        from_yaml("[a, value}")
    # Test valid JSON

# Generated at 2022-06-13 07:27:18.764182
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""
[foo, bar]
- baz
""") == [['foo', 'bar'], 'baz']



# Generated at 2022-06-13 07:27:30.015788
# Unit test for function from_yaml
def test_from_yaml():

    assert from_yaml('{ "foo": "bar" }') == {'foo': 'bar'}
    assert from_yaml('{ "foo": "bar" }', json_only=True) == {'foo': 'bar'}
    assert from_yaml('{ "foo": "bar" }', json_only=False) == {'foo': 'bar'}
    assert from_yaml('{ "foo": "bar" }', json_only=True) == {'foo': 'bar'}
    assert from_yaml('{ "foo": "bar" }', json_only=False) == {'foo': 'bar'}

    assert from_yaml('[ "foo", "bar" ]') == ['foo', 'bar']