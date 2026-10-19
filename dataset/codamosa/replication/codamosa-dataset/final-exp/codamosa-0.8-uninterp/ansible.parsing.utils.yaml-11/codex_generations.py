

# Generated at 2022-06-13 07:17:45.639366
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.vars.unsafe_proxy import wrap_var

    data = dict(a=123, b=dict(c=456, d='789'))
    assert from_yaml(json.dumps(data)) == data
    assert from_yaml(json.dumps(data), json_only=True) == data
    assert from_yaml(json.dumps(data), json_only=True, show_content=False) == data

    data = dict(a='{{foo}}', b=dict(c='{{bar}}', d='789'))
    vault_secrets = dict(foo='{{vault_foo}}', bar='{{vault_bar}}')
    assert from_yaml(json.dumps(data)) == data

# Generated at 2022-06-13 07:17:52.153443
# Unit test for function from_yaml
def test_from_yaml():
    # Test YAML input with a JSON encoded string
    data = from_yaml(data='{"foo": ["bar", "baz"]}')
    assert data == {u'foo': [u'bar', u'baz']}

    # Test JSON input with a YAML encoded string
    data = from_yaml(data='foo: ["bar", "baz"]', json_only=True)
    assert data == {u'foo': [u'bar', u'baz']}

# Generated at 2022-06-13 07:18:01.808757
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    import yaml

    yaml.add_representer(
        AnsibleVaultEncryptedUnicode,
        lambda dumper, node: dumper.represent_str(node.data)
    )

    yaml.add_representer(
        AnsibleVaultEncryptedUnicode,
        lambda dumper, node: dumper.represent_str(node.data)
    )

    data_json = '{"a": "{{ vault_a }}", "b": "{{ vault_b }}"}'
    data_yaml = 'a: {{ vault_a }}\nb: {{ vault_b }}'

    # load both JSON and YAML as

# Generated at 2022-06-13 07:18:05.334549
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('''
---
foo:
- 1
- 2
bar:
- 3
- 4
''') == {'bar': [3, 4], 'foo': [1, 2]}

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:09.766787
# Unit test for function from_yaml
def test_from_yaml():
    assert 1 == from_yaml('1')   # json
    assert 1 == from_yaml('1.0')
    assert 'a' == from_yaml('"a"')
    assert 'a' == from_yaml('a')  # yaml
    assert {'a': 1} == from_yaml('a: 1')
    assert {'a': 1} == from_yaml('{"a": 1}')
    assert {'a': 1} == from_yaml('{\"a\": 1}')
    assert {'a': 1} == from_yaml('\n\t{ \n "a"  : 1 \n }\n\t')
    assert {'a': 1} == from_yaml('{"a": 1,}')  # trailing comma

# Generated at 2022-06-13 07:18:14.789096
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml_data = """
    ---
    a: b
    """
    data = AnsibleLoader(yaml_data, file_name='<string>').get_single_data()
    assert data['a'] == 'b', "yaml_str is not being converted to python object correctly"
    assert isinstance(data, dict), "yaml_str is not being converted to python object correctly"

# Generated at 2022-06-13 07:18:19.484057
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    sys.path.append('/tmp/ansible/bin')
    from ansible import constants

    with open('/tmp/ansible/lib/ansible/playbook/play_context.py', 'r') as f:
        print (f.read())

    print (constants.DEFAULT_MODULE_PATH)

# Generated at 2022-06-13 07:18:25.166695
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"name":"test"}'
    result = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert result == {'name': 'test'}

    data = 'name: test'
    result = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert result == {'name': 'test'}

# Generated at 2022-06-13 07:18:33.376734
# Unit test for function from_yaml
def test_from_yaml():
    data = "{\"a\": \"b\"}"
    result = from_yaml(data)
    assert result == {'a': 'b'}
    data = "{a: 'b'}"
    result = from_yaml(data)
    assert result == {'a': 'b'}
    data = "{'a': 'b'}"
    result = from_yaml(data)
    assert result == {'a': 'b'}
    data = "{a: b}"
    result = from_yaml(data)
    assert result == {'a': 'b'}
    data = "{a: \"b\"}"
    result = from_yaml(data)
    assert result == {'a': 'b'}

# Generated at 2022-06-13 07:18:41.506054
# Unit test for function from_yaml
def test_from_yaml():
    json_data_str = '{"one": "two", "three": [1,2,3], "four": {"five": 5, "six": "six"}}'
    assert from_yaml(json_data_str) == json.loads(json_data_str)

    json_data_str = '{"one": "two", "three": [1,2,3], "four": {"five": 5, "six": "six"}}'
    yaml_data_str = 'one: two\nthree: [1, 2, 3]\nfour:\n    five: 5\n    six: six\n'
    assert from_yaml(json_data_str) == from_yaml(yaml_data_str)


# Generated at 2022-06-13 07:18:55.299864
# Unit test for function from_yaml
def test_from_yaml():
    # Test JSON input, without vault content
    try:
        json_str = r'{"a": 1, "b": ["x", "y"]}'
        json_dict = json.loads(json_str)
        assert(json_dict == from_yaml(json_str))
    except Exception as e:
        raise AssertionError("invalid json string '%s' with error '%s'" % (json_str, e))

    # Test JSON input, with vault content

# Generated at 2022-06-13 07:19:03.154588
# Unit test for function from_yaml
def test_from_yaml():
    data = """---
- hosts: all
  gather_facts: False
  tasks:
    - name: test
      debug:
        msg: "hello world"

- hosts: other
  gather_facts: False
  tasks:
    - name: test
      command: "/bin/true"
"""
    new_data = from_yaml(data)
    print(json.dumps(new_data, indent=4))

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:19:09.718762
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    import json

    # Test valid YAML
    yaml_data = 'a: b'
    expected = {'a': 'b'}
    actual = from_yaml(yaml_data)
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

    # Test invalid JSON
    yaml_data = '''
abc
abc
'''
    try:
        actual = from_yaml(yaml_data, json_only=True)
    except AnsibleParserError:
        pass
    else:
        assert False, 'AnsibleParserError not raised for invalid JSON'

    # Test invalid YAML
    yaml_data = '''
a: b
'''

# Generated at 2022-06-13 07:19:22.717077
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml import objects

    vault_password = '$ANSIBLE_VAULT;1.1;AES256\n35393465643638363533653363326465333262613431366339613661393164666463653263383761\n61353235346338326439613262653136613961366139316466646365326338376100000000000000000000\n00000000000000000000'

    vault = VaultLib(None)
    vault_secrets = vault.secrets
    vault_secrets['_vault_password'] = vault_password

    # test if ansible yaml can be loaded

# Generated at 2022-06-13 07:19:30.538200
# Unit test for function from_yaml
def test_from_yaml():
    data = '---\n- 1\n- 2\n'
    data2 = '---\n- 1\n- 2\n\n'
    data3 = '---\n- 1\n- 2\n\n\n'
    data4 = '---\n- 1\n- 2\n\n\n\n'
    data5 = '---\n- 1\n- 2\n  \n'
    data6 = '---\n- 1\n- 2\n\n...\n'
    data7 = '---\n- 1\n- 2\n\n...\n---\n- 3\n- 4\n\n'
    assert from_yaml(data) == [1, 2]
    assert from_yaml(data2) == [1, 2]

# Generated at 2022-06-13 07:19:32.592510
# Unit test for function from_yaml
def test_from_yaml():
    data = "{ {'json': 'value'} }"
    assert from_yaml(data) == {'json': 'value'}

# Generated at 2022-06-13 07:19:36.486051
# Unit test for function from_yaml
def test_from_yaml():
    assert {'foo': 'bar'} == from_yaml("{'foo': 'bar'}")
    assert {'foo': 'bar'} == from_yaml("{\"foo\": \"bar\"}")
    assert {'foo': 'bar'} == from_yaml("foo: bar")

# Generated at 2022-06-13 07:19:48.660187
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''

    def _test_string(stream, expected):
        # TODO: test vault_secrets
        assert from_yaml(stream) == expected

    _test_string("{{ foo }}", {u'{{ foo }}': None})
    _test_string("{{ foo }}\nbar", {u'{{ foo }}\nbar': None})
    _test_string("foo: {{ foo }}", {u'foo': u'{{ foo }}'})
    _test_string("foo: {{ foo }}\nbar: baz", {u'foo': u'{{ foo }}', u'bar': u'baz'})
    _test_string("foo: bar\n- baz", {u'foo': u'bar', u'baz': None})
    _test

# Generated at 2022-06-13 07:19:58.613252
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""
---
this_looks_awfully_like_yaml:
- but
- its
- really
- json
    """) == {u'this_looks_awfully_like_yaml': [u'but', u'its', u'really', u'json']}

    assert from_yaml("""
---
its:
- a
- yaml
    """) == {u'its': [u'a', u'yaml']}

    assert from_yaml("""{
    this_looks_awfully_like_json: but its really yaml
}""") == {u'this_looks_awfully_like_json': u'but its really yaml'}


# Generated at 2022-06-13 07:20:11.256250
# Unit test for function from_yaml
def test_from_yaml():
    import random as rand
    import tempfile

    assert isinstance(from_yaml("", json_only=True), dict)
    assert isinstance(from_yaml("{}", json_only=True), dict)
    assert isinstance(from_yaml("[]", json_only=True), list)

    try:
        from_yaml("{]", json_only=True)
    except AnsibleParserError as e:
        assert "JSON" in to_native(e)

    assert isinstance(from_yaml("", json_only=False), dict)
    assert isinstance(from_yaml("{}", json_only=False), dict)
    assert isinstance(from_yaml("[]", json_only=False), list)

    # from the docs

# Generated at 2022-06-13 07:20:24.053175
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.ajson import AnsibleJSONDecoder

    def json_verifier(data, file_name=None, show_content=True, vault_secrets=None):
        return json.loads(data, cls=AnsibleJSONDecoder)

    def yaml_verifier(data, file_name=None, show_content=True, vault_secrets=None):
        loader = AnsibleLoader(data, file_name=file_name)
        try:
            return loader.get_single_data()
        finally:
            try:
                loader.dispose()
            except AttributeError:
                pass  # older versions of yaml don't have dispose

# Generated at 2022-06-13 07:20:24.624142
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:20:30.418752
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"foo": "bar"}'
    new_data = from_yaml(data)
    assert new_data.get('foo') == 'bar'

    data = '{"foo": "bar"}{}'
    try:
        new_data = from_yaml(data)
    except Exception as e:
        assert type(e) == AnsibleParserError

# Generated at 2022-06-13 07:20:36.296520
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '{"name": "foo"}'
    json_data = from_yaml(json_str, json_only=True)
    assert json_data['name'] == 'foo'

    yaml_str = '---\nname: foo'
    yaml_data = from_yaml(yaml_str)
    assert yaml_data['name'] == 'foo'

# Generated at 2022-06-13 07:20:47.202013
# Unit test for function from_yaml
def test_from_yaml():
    # Test for simple YAML usage
    yaml_data = """---
- name: test
  hosts: localhost
  tasks:
  - shell: echo "Hello World"
"""
    result = from_yaml(yaml_data)
    assert result[0]['name'] == 'test'

    # Test for simple JSON usage
    json_data = """[{"name": "test", "hosts": "localhost", "tasks": [{"shell": "echo \"Hello World\""}]}]"""
    result = from_yaml(json_data)
    assert result[0]['name'] == 'test'

    # Test for JSON usage with vaults

# Generated at 2022-06-13 07:20:56.096293
# Unit test for function from_yaml
def test_from_yaml():
    """
    Validate graceful functionality when parsing yaml or json
    """
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.ajson import AnsibleJSONDecoder

    # Valid JSON, Valid YAML
    valid_json_yaml = AnsibleLoader(u"""
        ---
        json:
            nested_json: 1
        yaml:
            nested_yaml: 1
        """).get_single_data()
    assert valid_json_yaml['json']['nested_json'] == 1
    assert valid_json_yaml['yaml']['nested_yaml'] == 1

    # Invalid JSON, Valid YAML

# Generated at 2022-06-13 07:21:07.720389
# Unit test for function from_yaml
def test_from_yaml():
    # Simple test to make sure that from_yaml is working as expected
    yaml_str = '''{
      "str_key": "str_val",
      "int_key": 10,
      "bool_key": true,
      "list_key": [ 5, 10, 20 ],
      "dict_key": {
        "sub_dict_key": "sub_dict_val"
       }
    }'''

    data = from_yaml(yaml_str)
    assert data['dict_key']['sub_dict_key'] == 'sub_dict_val'
    assert data['list_key'][1] == 10


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:19.912921
# Unit test for function from_yaml
def test_from_yaml():
  test_dict = { "abcd": "1234", "xyz": "5678" }
  test_yaml = '{"abcd":"1234","xyz":"5678"}'
  test_json = json.dumps(test_dict)
  print("YAML: " + test_yaml)
  print("JSON: " + test_json)
  print("DICT: " + str(test_dict))

  output1 = from_yaml(test_yaml)
  output2 = from_yaml(test_json)
  print("YAML from_yaml output: " + str(output1))
  print("JSON from_yaml output: " + str(output2))
  assert(output1 == output2)

# Uncomment to run unit test for from_yaml, above
#test_

# Generated at 2022-06-13 07:21:34.118900
# Unit test for function from_yaml
def test_from_yaml():
    # ensure we can parse JSON strings
    assert from_yaml('{"a": [1, "1", true]}') == {"a": [1, "1", True]}

    # ensure we can parse YAML strings
    assert from_yaml('# this is a comment\na: [1, "1", true]\n') == {"a": [1, "1", True]}
    assert from_yaml('# this is a comment\n\na: [1, "1", true]\n') == {"a": [1, "1", True]}

    # ensure we can parse YAML strings with a leading newline
    assert from_yaml('\na: [1, "1", true]\n') == {"a": [1, "1", True]}

    # ensure we can parse YAML strings with a trailing newline
   

# Generated at 2022-06-13 07:21:41.951413
# Unit test for function from_yaml
def test_from_yaml():
    # Verify a valid JSON String
    json_str = '{"name":"John", "age":30, "city":"New York"}'
    assert json_str == json.dumps(from_yaml(json_str))

    # Verify an empty string
    json_str = ''
    assert json_str == json.dumps(from_yaml(json_str))

    # Verify an empty string
    json_str = '{}'
    assert json_str == json.dumps(from_yaml(json_str))

    # Verify an empty string
    json_str = 'true'
    assert json_str == json.dumps(from_yaml(json_str))

    # Verify an empty string
    json_str = 'null'
    assert json_str == json.dumps(from_yaml(json_str))

# Generated at 2022-06-13 07:21:50.021832
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("1") == 1
    assert from_yaml("1.1") == 1.1
    assert from_yaml("a") == u'a'
    assert from_yaml("true")
    assert not from_yaml("false")
    assert from_yaml("[1, 2, 3]") == [1, 2, 3]
    assert from_yaml("{a: 1}") == {u'a': 1}

# Generated at 2022-06-13 07:21:57.738713
# Unit test for function from_yaml
def test_from_yaml():

    import ansible.parsing.dataloader  # noqa

    # test out the from_yaml function
    assert from_yaml('{ "foo": "bar" }') == dict(foo="bar")
    assert from_yaml('{ foo: bar }') == dict(foo="bar")
    assert from_yaml('{ foo: bar }', json_only=True, show_content=False) == dict(foo="bar")

    # test out the from_yaml function, with a value error

# Generated at 2022-06-13 07:22:08.596137
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('hello_world') == {'hello_world': None}
    assert from_yaml('hello_world: 123') == {'hello_world': 123}
    assert from_yaml('hello_world: 123\n') == {'hello_world': 123}
    assert from_yaml('hello_world:\n  - "123"') == {'hello_world': ['123']}
    assert from_yaml('hello_world:\n  - "123"\n') == {'hello_world': ['123']}
    assert from_yaml('hello_world: \'123\'') == {'hello_world': '123'}
    assert from_yaml('hello_world: \'123\'') == {'hello_world': '123'}

# Generated at 2022-06-13 07:22:23.160506
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("a: 1") == {"a": 1}
    assert from_yaml("{\"a\": 1}") == {"a": 1}
    assert from_yaml("a: 1\nb: 2") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\n\nb: 2") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\nb: 2\n") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\n\nb: 2\n") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\n\n") == {"a": 1}

# Generated at 2022-06-13 07:22:27.778244
# Unit test for function from_yaml
def test_from_yaml():
    # Test for function from_yaml
    data = '''
        ---
        child:
         - key3: val3
         - key4: val4
        key1:
         - val1
         - val2'''
    import json
    assert json.dumps(from_yaml(data)) == json.dumps({'child': [{'key3': 'val3'}, {'key4': 'val4'}], 'key1': ['val1', 'val2']})

# Generated at 2022-06-13 07:22:39.712752
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This test just tests the from_yaml() function to ensure that it works as
    expected with a variety of inputs.
    '''

    import os

    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_YAML_PATH = os.path.join(TEST_DIR, 'parsing/yaml/test.yml')
    TEST_JSON_PATH = os.path.join(TEST_DIR, 'parsing/yaml/test.json')
    TEST_BAD_YAML_PATH = os.path.join(TEST_DIR, 'parsing/yaml/test.bad.yml')

    with open(TEST_YAML_PATH) as f:
        test_yaml_data = f.read()



# Generated at 2022-06-13 07:22:47.904989
# Unit test for function from_yaml
def test_from_yaml():
    data = u"{'foo': 'bar', 'blah': [1, 2, 3]}".encode('utf-8')
    file_name = "/tmp/fakehost_1353636363.53"
    show_content = True
    vault_secrets = None
    json_only = False
    try:
        new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
        print(new_data)
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:22:52.728967
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert from_yaml('foo: bar') == {u'foo': u'bar'}
    assert type(from_yaml('foo: bar')['foo']) == AnsibleUnicode


# Generated at 2022-06-13 07:23:03.477353
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    name: test
    test: pass
    '''
    ret = from_yaml(data)
    assert ret['name'] == 'test'
    assert ret['test'] == 'pass'

    data = '''
    - 1
    - 2
    '''
    ret = from_yaml(data)
    assert isinstance(ret, list)
    assert ret[0] == 1
    assert ret[1] == 2

    data = '''
    - name: test
      test: pass
    - name: test2
      test2: pass2
    '''
    ret = from_yaml(data)
    assert isinstance(ret, list)
    assert ret[0]['name'] == 'test'
    assert ret[1]['test2'] == 'pass2'


# Generated at 2022-06-13 07:23:09.928005
# Unit test for function from_yaml
def test_from_yaml():

    fail_msg = "from_yaml() failed to load JSON data"
    json_data = '{"foo": "bar"}'
    data = from_yaml(json_data)
    assert data == {"foo": "bar"}, fail_msg

    fail_msg = "from_yaml() failed to load YAML data"
    yaml_data = 'foo: bar'
    data = from_yaml(yaml_data)
    assert data == {"foo": "bar"}, fail_msg

    fail_msg = "from_yaml() failed to load JSON data with a JSON string"
    yaml_data = 'foo: \'{"foo": "bar"}\''
    data = from_yaml(yaml_data)
    assert data == {"foo": {"foo": "bar"}}, fail_msg


# Generated at 2022-06-13 07:23:20.907410
# Unit test for function from_yaml
def test_from_yaml():
    val = from_yaml("{'key': 'value'}")
    assert val == {'key': 'value'}
    val = from_yaml("{'key': 'value'}", json_only=True)
    assert val == {'key': 'value'}

# Generated at 2022-06-13 07:23:29.205568
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    yaml = "---\n- some_tasks:\n- name: setup_app\n  tags:\n    - setup_app\n    - app\n    - cache\n  vars:\n    - app_name: Test\n    - app_user: app\n"
    vault_secrets = {'key': 'test_secret'}
    result = from_yaml(yaml, vault_secrets=vault_secrets)
    assert isinstance(result[0], dict)
    assert isinstance(result[0]['some_tasks'][0]['vars'][0]['app_name'], AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 07:23:43.570236
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.objects
    ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode.VAULT_VERSION = 1
    assert json.loads(from_yaml("a: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          36353436383339343335656161383034363935656631383136623961666434393337383437623761\n          6435346082630200076333537663263366662336335643339346437333762333738396434373630\n          653265300a\n          b: hello\n")) == {"a": "bar", "b": "hello"}

# Generated at 2022-06-13 07:23:55.223554
# Unit test for function from_yaml
def test_from_yaml():
    """
    from_yaml: returns from_jason if it works
    """
    import json
    # Our main test value is for a list
    test_val = json.loads('[{"a": 1, "b":2}]')
    # This is our JSON list
    json_list = "[{\"a\": 1, \"b\":2}]"

    # In the main function, if it is json data, it will
    # just return whatever the json.loads returns
    # This should be the same as test_val
    assert test_val == from_yaml(json_list)

    # If it is yaml, it will try to load it as json, and if
    # it fails, it will load it as yaml.
    # This should be the same as test_val

# Generated at 2022-06-13 07:24:05.484362
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleUnicode

    source = """
foobar:
  baz:
    - item1
    - |
      item2
      with
      newlines and stuff
    - item3
    - item4
    - item5
    - item6
    - item7
"""
    expected = {
        'foobar': {
            'baz': [
                'item1',
                'item2\nwith\nnewlines and stuff\n',
                'item3',
                'item4',
                'item5',
                'item6',
                'item7',
            ],
        },
    }

    actual = from_yaml(to_bytes(source))



# Generated at 2022-06-13 07:24:09.480276
# Unit test for function from_yaml
def test_from_yaml():
    data = "foo: \"{{ 'hi' }}\""
    file_name = "<string>"
    show_content = False
    vault_secrets = {}
    json_only = False
    output = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert output == {"foo": "{{ 'hi' }}"}

# Generated at 2022-06-13 07:24:17.018433
# Unit test for function from_yaml
def test_from_yaml():
    # simplest possible yaml
    yaml_str = "foo: bar"
    yaml_data = from_yaml(yaml_str)
    assert yaml_data == {u'foo': u'bar'}

    # simplest possible json
    json_str = '{"foo": "bar"}'
    json_data = from_yaml(json_str)
    assert json_data == {u'foo': u'bar'}

# Generated at 2022-06-13 07:24:20.981473
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a":"b"}') == {"a": "b"}
    assert from_yaml('{"a":"b"}', json_only=True) == {"a": "b"}
    assert from_yaml('a: b\n') == {"a": "b"}
    json_data = {"a": "b"}
    assert from_yaml(json.dumps(json_data)) == json_data

# Generated at 2022-06-13 07:24:32.853372
# Unit test for function from_yaml
def test_from_yaml():
    def test_parse(v, expected):
        assert from_yaml(v) == expected

    # all scalars
    for v in [
        '1',
        '1.0',
        '""',
        '"str"',
        "true",


        # http://yaml.org/spec/1.2/spec.html#id2759572
        "'single quoted'",
        "''",
        "123.456",
        "1.23e-10",
        "0x1a",
        "-12",
        "0b10",
        "0o12",
        "0xff",
    ]:
        test_parse(v, eval(v))

    # all lists

# Generated at 2022-06-13 07:24:37.192337
# Unit test for function from_yaml
def test_from_yaml():

    TEST_DATA = {
        "one": 1,
        "two": 2,
        "three": True
    }

    test_j = json.dumps(TEST_DATA)
    test_y = """
    one: 1
    two: 2
    three: True
    """

    result = from_yaml(test_j)
    assert result == TEST_DATA

    result = from_yaml(test_y)
    assert result == TEST_DATA

# Generated at 2022-06-13 07:24:53.714614
# Unit test for function from_yaml
def test_from_yaml():
    """
    Unit test for function from_yaml
    """

    import ansible.constants as C
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    from_yaml.__globals__['__name__'] = 'from_yaml'

    # case 1: we have a json
    data = '{"a": 1, "b": "hello"}'
    result = from_yaml(data, json_only=True)
    assert(result == {"a": 1, "b": "hello"})
    assert(from_yaml.__globals__['json'].loads.call_count == 1)
    assert(from_yaml.__globals__['AnsibleJSONDecoder'].set_secrets.call_count == 1)

    # case 2:

# Generated at 2022-06-13 07:25:02.778241
# Unit test for function from_yaml
def test_from_yaml():
    import unittest
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 07:25:11.764924
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.vars.unsafe_proxy import UnsafeProxy

    data = '{"a": {"b": "c", "d": {"e": "f"}}, "b": "{{ c }}"}'
    assert from_yaml(data) == {"a": {"b": "c", "d": {"e": "f"}}, "b": "{{ c }}"}

    # older versions of pyyaml do not support the load() function on the
    # yaml decoder and older versions of yaml do not appear to load JSON
    # (and older versions of ansible were not reloading attributes like
    # selected_file on the vars inventory source)
    assert not hasattr(from_yaml(data), 'selected_file')

    # A vault-secrets argument was added to from_yaml(). We don't do any vault processing here,


# Generated at 2022-06-13 07:25:19.201965
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    v = VaultLib('a secret')
    s = v.encrypt('a secret')
    expected = {'secret': 'a secret'}
    real = from_yaml('!vault |\n%s' % s, show_content=False, vault_secrets=[v])
    assert real == expected
    real = from_yaml('!vault |\n%s' % s, show_content=False, vault_secrets=[v])
    assert real == expected
    real = from_yaml('!vault |\n%s' % s, show_content=False, vault_secrets=[v])
    assert real == expected

# Generated at 2022-06-13 07:25:30.574375
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO

    _from_yaml = from_yaml

    # Function from_yaml() calls function _safe_load() which calls class AnsibleLoader().
    # We need to mock both these functions.
    # Function _safe_load() and class AnsibleLoader() are defined in module
    # ansible/parsing/yaml/__init__.py
    # Therefore we patch this module here.

    # For Python 2.7 we patch the module by temporarily patching sys.modules.
    # For Python 3.5 and later we use the patching mechanism of the unittest module.

    if not PY3:
        import sys
        import mock
    else:
        from unittest.mock import patch



# Generated at 2022-06-13 07:25:37.122508
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.constructor
    result = from_yaml("""
        ---
        - hosts: all
          gather_facts: no
        """, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)

    assert len(result) == 2
    assert result[0] == '---'
    assert result[1]['hosts'] == 'all'

# Generated at 2022-06-13 07:25:39.098463
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}

# Generated at 2022-06-13 07:25:50.005689
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '{"test_key":"test_value"}'
    data = from_yaml(json_str)
    if data['test_key'] != "test_value":
        print('json test failed: %s' % data['test_key'])
    yaml_str = "test_key: test_value"
    data = from_yaml(yaml_str)
    if data['test_key'] != "test_value":
        print('yaml test failed: %s' % data['test_key'])

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:57.952653
# Unit test for function from_yaml
def test_from_yaml():
    try:
        json_string = "{\"foo\": {\"bar\": {\"baz\": 123}}}"
        data = from_yaml(json_string, json_only=True)
        if data["foo"]["bar"]["baz"] != 123:
            raise AssertionError('The value of data["foo"]["bar"]["baz"] is %s' % data["foo"]["bar"]["baz"])
    except AssertionError as e:
        print('This block should not have failed with exception {}'.format(e))
        return 1


# Generated at 2022-06-13 07:26:10.112897
# Unit test for function from_yaml
def test_from_yaml():
    test_data = {
        'data': [
            {'key': "value"},
            {'key': 'value with "quotes"'},
            {'key': {'foo': 'bar'}},
            {'key': ["foo", 'bar', 'baz']},
        ],
        'expected': [
            {'key': "value"},
            {'key': 'value with "quotes"'},
            {'key': {'foo': 'bar'}},
            {'key': ["foo", 'bar', 'baz']},
        ],
    }

    for entry in test_data['data']:
        json_data = json.dumps(entry)
        yaml_data = '---\n' + to_native(json_data)
        converted_data = from_yaml(yaml_data)

# Generated at 2022-06-13 07:26:35.513083
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # ---
    # Empty yaml string
    yaml_str = ''
    assert from_yaml(yaml_str) == None

    # ---
    # YAML string
    yaml_str = '''
    - hosts:
        - Lnx01
        - Lnx02
    roles:
        - web
        - database
    '''

    # function returns an AnsibleUnicode object if the string contains a unicode character
    # From ansible/config.py
    # ansible_python_interpreter: /usr/local/bin/python3.6
    # 
    # python3.6 is an unicode string
    ans_unico_obj = from_yaml(yaml_str)

# Generated at 2022-06-13 07:26:47.313485
# Unit test for function from_yaml
def test_from_yaml():

    import unittest
    import os
    import json

    # test load_from_file
    test_yaml_file = 'test_from_yaml.yml'
    test_data = '''
    {
        "name": "test",
        "key": "value",
        "array": [
            'a',
            {
                "name": "test"
            },
            "b"
        ],
        "dict": {
            "key": "value"
        }
    }
    '''

    with open(test_yaml_file, 'w') as f:
            f.write(test_data)

    test_yaml_data = from_yaml(test_data, file_name=test_yaml_file)
    test_yaml_data_from_file = from_y

# Generated at 2022-06-13 07:26:59.220931
# Unit test for function from_yaml
def test_from_yaml():
    # All good
    try:
        from_yaml("{\"a\":1}")
        assert True
    except ValueError:
        assert False
    try:
        from_yaml("a: 1\n")
        assert True
    except ValueError:
        assert False
    try:
        from_yaml("{\"a\":1}",json_only=True)
        assert True
    except ValueError:
        assert False

    # Errors
    try:
        from_yaml("a: 1\n", json_only=True)
        assert False
    except ValueError:
        assert True
    try:
        from_yaml("{a:1}")
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-13 07:27:10.801935
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3

    # test basic string
    data = from_yaml('This is a string', '<string>')
    assert data == 'This is a string'

    # test basic string with numeric
    data = from_yaml('This is a string 123', '<string>')
    assert data == 'This is a string 123'

    # test string containing regex pattern
    data = from_yaml('This is a string containing a .', '<string>')
    assert data == 'This is a string containing a .'

    # test string containing regex pattern using negation
    data = from_yaml('This is a string containing a [\D]', '<string>')
    assert data == 'This is a string containing a [\D]'

    # test string containing regex pattern using range
    data

# Generated at 2022-06-13 07:27:21.328895
# Unit test for function from_yaml
def test_from_yaml():
    # 1. Good JSON data
    data = '{"foo": "bar", "baz": "qux", "corge": null, "grault": 1, "waldo": false, "fred": [1.2, 3.4], "plugh": {"thud": true}}'
    ret = from_yaml(data)
    assert ret == json.loads(data)

    # 2. Invalid JSON data
    data = '{"foo": bar, "baz": "qux", "corge": null, "grault": 1, "waldo": false, "fred": [1.2, 3.4], "plugh": {"thud": true}}'
    try:
        from_yaml(data)
    except AnsibleParserError as e:
        pass

# Generated at 2022-06-13 07:27:35.354919
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    script_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir = os.path.realpath(os.path.curdir)
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
    from tests.unit.parsing.utils import assert_raises_ansible_parse_error

    # Empty YAML
    assert from_yaml('{}') == {}
    assert from_yaml('[]') == []
    assert from_yaml('') is None

    # Nested key/value
    assert from_yaml('key1: value1') == {'key1': 'value1'}