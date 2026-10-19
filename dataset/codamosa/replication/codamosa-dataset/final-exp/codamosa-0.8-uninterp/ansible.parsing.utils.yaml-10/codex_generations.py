

# Generated at 2022-06-13 07:17:39.789737
# Unit test for function from_yaml
def test_from_yaml():
    # Test from_json()
    input_json = '[{"item": "a"}, {"item": "b"}]'
    assert from_yaml(input_json, json_only=True) == [{u'item': u'a'}, {u'item': u'b'}]

    # Test from_yaml()
    input_yaml = '''
      - item: a
      - item: b
    '''
    assert from_yaml(input_yaml) == [{u'item': u'a'}, {u'item': u'b'}]

    # Test from_yaml() with vault
    input_yaml_vault = '''
      - item: a
      - item: b
    '''
    # FIXME: vault_secrets should be accepted as arg but currently vault plugin is not initialized

# Generated at 2022-06-13 07:17:46.888027
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Tests to ensure the behavior of the from_yaml() function when given
    valid and invalid data.
    '''

    # Valid YAML
    data = "{ foo: bar }"
    result = from_yaml(data)
    assert result == dict(foo='bar')

    # Should return None when JSON is empty
    data = "{}"
    result = from_yaml(data)
    assert result == {}

    # Invalid YAML
    # data = "{ foo: "
    # result = from_yaml(data)
    # print(result)
    # assert result == dict(foo='bar')

# Generated at 2022-06-13 07:17:57.441452
# Unit test for function from_yaml
def test_from_yaml():
    obj = {
        'foo': 'bar',
        'baz': ['one', 'two'],
        'qux': {
            'quux': 'quuz'
        }
    }

    # If obj is serialized as JSON and parsed as JSON, results should match
    json_str = json.dumps(obj)
    jres = json.loads(json_str, cls=AnsibleJSONDecoder)
    assert obj == jres

    # If obj is serialized as JSON and parsed as YAML, results should match
    yres = from_yaml(json_str)
    assert obj == yres, 'Failed to load data as YAML when it was valid JSON'

    # If obj is serialized as YAML and parsed as JSON, results should match

# Generated at 2022-06-13 07:18:03.637311
# Unit test for function from_yaml
def test_from_yaml():
    # TODO: use unittest.TestCase or mock for this.
    import pytest

    def _assert_success(content, expected):
        actual = from_yaml(content, file_name='<string>', show_content=False, vault_secrets=None, json_only=False)
        assert actual == expected

    _assert_success('{ "a": 1, "b": "2" }', {u'a': 1, u'b': u'2'})

    _assert_success('{ "a": 1, "b": "2" }', {u'a': 1, u'b': u'2'})


# Generated at 2022-06-13 07:18:13.754465
# Unit test for function from_yaml
def test_from_yaml():
    # Test for simple int
    assert from_yaml("123") == 123

    # Test for simple string
    assert from_yaml("test") == "test"

    # Test for empty string
    assert from_yaml("") == ''

    # Test for empty array
    assert from_yaml("[]") == []

    # Test for empty dictionary
    assert from_yaml("{}") == {}

    # Test for empty dictionary with space
    assert from_yaml("\n{}") == {}

    # Test for empty list with space
    assert from_yaml("\n[]") == []

    # Test for dictionary
    assert from_yaml("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}

    # Test for list

# Generated at 2022-06-13 07:18:24.037120
# Unit test for function from_yaml
def test_from_yaml():
    # YAML
    assert from_yaml("a: 1") == {'a': 1}
    assert from_yaml("a: 1", show_content=False) == {'a': 1}

    # JSON
    assert from_yaml("{\"a\": 1}", show_content=False) == {'a': 1}

    # JSON parsing error
    with pytest.raises(AnsibleParserError) as excinfo:
        from_yaml("{\"a\": 1")
    assert str(excinfo.value).startswith("{")
    assert excinfo.value.show_content is True
    assert excinfo.value.obj is None
    assert "Expecting property name" in str(excinfo.value)

    # JSON parsing error through YAML

# Generated at 2022-06-13 07:18:31.503675
# Unit test for function from_yaml
def test_from_yaml():
    '''Test whether from_yaml correctly parses an example'''
    example = '''
--- # Example
- hosts: all
  remote_user: root
  tasks:
    - shell: echo hello world
'''

    try:
        from_yaml(example)
    except AnsibleParserError as e:
        assert False, 'Failed to parse YAML:\n{0}'.format(e)

# Generated at 2022-06-13 07:18:39.520905
# Unit test for function from_yaml
def test_from_yaml():
    import tempfile
    import os
    import sys
    import ansible.constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.parsing.yaml.loader import AnsibleLoader

    utf8_data = b'a: I\xc3\xb1t\xc3\xabrn\xc3\xa2ti\xc3\xb4n\xc3\xa0liz\xc3\xa6ti\xc3\xb8n'

    # Fix issue with VaultLib's supports_encrypting_strings() not
    # working for Python < 2.

# Generated at 2022-06-13 07:18:49.880245
# Unit test for function from_yaml
def test_from_yaml():

    # Get the path to the fixture_file
    import os
    test_dir = os.path.dirname(os.path.realpath(__file__))
    fixture_file = os.path.join(test_dir, "fixtures", "from_yaml.yml")

    with open(fixture_file, "r") as f:
        text = f.read()

    import sys
    import stat
    import ansible.module_utils.common
    # If the fixture is a symlink, it may not be executable
    # and since Ansible treats it as such, we need to chmod it
    # Otherwise Windows will complain on Ansible 2.9+.

# Generated at 2022-06-13 07:18:52.625525
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"boom": {"bad": "good"}}'
    result = from_yaml(data)
    assert result == {'boom': {'bad': 'good'}}

# Generated at 2022-06-13 07:19:05.354815
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.display import Display

    display = Display()
    test_str = """
    - test1:
        key: value
    - test2:
        '{"key": "value"}'
    """

    data = from_yaml(test_str, show_content=False)
    display.display(data)
    assert isinstance(data, list)
    assert len(data) == 2
    assert isinstance(data[0], dict)
    assert isinstance(data[1], dict)
    assert 'key' not in data[1]['test2']

    test_dict = {
        'test1': 'value1',
        'test2': 'value2',
        'test3': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'},
    }

   

# Generated at 2022-06-13 07:19:16.349505
# Unit test for function from_yaml
def test_from_yaml():
    input_dict1 = {'key1': 'value1', 'key2': 'value2'}
    input_dict2 = {'key1': 'value1', 'key2': 'value2'}

    # Test for yaml
    yaml_dict = from_yaml(yaml.dump(input_dict1))
    assert input_dict1 == yaml_dict

    # Test for json
    json_dict = from_yaml(json.dumps(input_dict2))
    assert input_dict2 == json_dict

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:24.498806
# Unit test for function from_yaml
def test_from_yaml():
    data_yaml = """
    - hosts: all
      roles:
        - azure_role
    """
    data_json = '''
    [
      {
        "hosts": "all",
        "roles": [
          {
            "role": "azure_role"
          }
        ]
      }
    ]
    '''
    new_data = from_yaml(data_yaml)
    assert(new_data[0]['hosts'] == 'all')
    assert(new_data[0]['roles'][0]['role'] == 'azure_role')

    new_data = from_yaml(data_json)
    assert(new_data[0]['hosts'] == 'all')

# Generated at 2022-06-13 07:19:32.396425
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    import os
    import tempfile
    import shutil

    if shutil.which('ansible-vault') is None:
        # no vault command availble, just bail out
        return

    dir_path = os.path.dirname(os.path.realpath(__file__))
    vault_id = os.path.join(dir_path, 'from_yaml_vaultid')
    vault_password_file = os.path.join(dir_path, 'from_yaml_vaultpassword')

    # use temp directory as vault cache dir to speed up and simplify test
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 07:19:42.389639
# Unit test for function from_yaml
def test_from_yaml():
    data = """
---
- hosts: all
  tasks:
    - debug: msg="hello world"
    - debug:
        msg: "hello world"
    - debug: |
        msg="hello world"
      tags:
        - always
    - debug:
        msg="fancy newlines handling
            with lot of spacing
          "
"""
    result = from_yaml(data)
    assert result['tasks'][0]['debug']['msg'] == 'hello world'
    assert result['tasks'][2]['debug'] == 'msg="hello world"'
    assert result['tasks'][3]['debug'] == 'msg="fancy newlines handling\nwith lot of spacing\n"'



# Generated at 2022-06-13 07:19:52.100866
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"a": false}'
    output = from_yaml(data)
    assert output.get('a') == False
    data = '{"a": false}'
    output = from_yaml(data, json_only=True)
    assert output.get('a') == False
    data = '{"a": false}'
    output = from_yaml(data, json_only=False)
    assert output.get('a') == False

    data = 'a: false'
    output = from_yaml(data)
    assert output.get('a') == False
    data = 'a: false'
    output = from_yaml(data, json_only=True)
    assert output is None
    data = 'a: false'
    output = from_yaml(data, json_only=False)

# Generated at 2022-06-13 07:19:59.849511
# Unit test for function from_yaml
def test_from_yaml():
    assert(from_yaml("foo") == "foo")
    assert(from_yaml("foo\n") == "foo\n")
    assert(from_yaml("foo\n", json_only=True) == "foo\n")
    assert(from_yaml("{\"foo\": \"bar\"}") == {u"foo": u"bar"})
    assert(from_yaml("\"foo\"") == "foo")
    assert(from_yaml("\"foo\"\n") == "foo")

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:20:07.536011
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import string_to_bytes

    print("Testing from_yaml()")

    print("... simple json string")
    json_string = u'{"test": "1", "test2": "test3"}'
    py_struct = from_yaml(json_string)
    assert py_struct == {"test": "1", "test2": "test3"}

    print("... simple yaml string")
    yaml_string = u"---\n- test: 1\n  test2: test3"
    py_struct = from_yaml(yaml_string)
    assert py_struct == [{"test": "1", "test2": "test3"}]

    print("... generate yaml from py struct")

# Generated at 2022-06-13 07:20:18.082865
# Unit test for function from_yaml
def test_from_yaml():
    try:
         data = 'true'
         val_temp = from_yaml(data, file_name = '<string>', show_content=True, vault_secrets=None, json_only=True)
         if val_temp == True:
             print('Unit test 1 is passed')
         else:
             print('Unit test 1 is NOT passed')
    except Exception as e:
        print ('Unit test 1 is NOT passed since', e)


# Generated at 2022-06-13 07:20:25.562825
# Unit test for function from_yaml
def test_from_yaml():

    # success cases
    assert isinstance(from_yaml("{}"), dict)
    assert isinstance(from_yaml("[]"), list)
    assert isinstance(from_yaml("1"), int)
    assert isinstance(from_yaml("1.1"), float)
    assert from_yaml("true") is True
    assert from_yaml("false") is False
    assert from_yaml("null") is None
    assert from_yaml("foo") == 'foo'
    assert from_yaml('"foo"') == 'foo'
    assert from_yaml("'foo'") == 'foo'
    assert from_yaml("---\nfoo") == 'foo'
    assert from_yaml('{"foo":"bar"}') == {'foo': 'bar'}

# Generated at 2022-06-13 07:20:37.907483
# Unit test for function from_yaml
def test_from_yaml():

    # Test loading yaml
    yaml = '''
        foo: 1
        bar: 2
    '''

    data = from_yaml(yaml)
    assert data == {u'foo': 1, u'bar': 2}

    # Test that we also load json
    json_data = '''
        {
          "foo": 1,
          "bar": 2
        }
    '''

    data = from_yaml(json_data)
    assert data == {u'foo': 1, u'bar': 2}

    # Test that we raise a AnsibleParserError on invalid data.
    # Ensure it happens on both invalid YAML and JSON
    bad_yaml = from_yaml.__doc__
    bad_json = '{foo}: 1'


# Generated at 2022-06-13 07:20:48.415277
# Unit test for function from_yaml
def test_from_yaml():
    ''' this is used in conjunction with a unit test script to ensure that the
    from_yaml() function returns the correct datastructures for given YAML input
    '''

    import os
    import sys
    import unittest

    if not hasattr(unittest, 'skipIf'):
        unittest.skipIf = lambda x, y: lambda func: func

    skip_msg = 'skipping yaml tests due to import failure'

    try:
        import yaml
        import json
    except ImportError:
        if os.environ.get('ANSIBLE_YAML_TEST'):
            raise
        else:
            unittest.skipIf(True, skip_msg)


# Generated at 2022-06-13 07:20:58.619520
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.playbook.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleUnicode

    from_yaml(u'[]')
    from_yaml(u'{}')
    from_yaml(u'string')
    from_yaml(u'1')
    from_yaml(u'1.0')
    from_yaml(u'true')
    from_yaml(u'false')
    from_yaml(u'null')
    from_yaml(u'string', json_only=True)
    from_yaml(u'{"a": "a"}', json_only=True)

    # example file using ini vault

# Generated at 2022-06-13 07:21:04.388977
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"foo": {"bar": "baz", "zoo": 2}}'
    assert from_yaml(data) == json.loads(data)

    data = '''
    foo:
      bar: baz
      zoo: 2
    '''
    assert from_yaml(data) == json.loads(data, object_pairs_hook=dict)

# Generated at 2022-06-13 07:21:13.174064
# Unit test for function from_yaml
def test_from_yaml():

    assert from_yaml("{}") == {}
    assert from_yaml("[]") == []
    assert from_yaml("42") == 42

    # FIXME: those are illegal (but still parsed)
    assert from_yaml("{}, []") == {}
    assert from_yaml("[], {}") == []

    # FIXME: those are illegal (but still parsed)
    assert from_yaml("1, 2") == 1
    assert from_yaml("2, 1") == 2

# Generated at 2022-06-13 07:21:17.011314
# Unit test for function from_yaml
def test_from_yaml():
    test_data = dict(
            a = dict(
                b = dict(
                    c = 1
                ),
                d = dict(
                    e = 2
                )
            )
        )

    data_to_be_tested = from_yaml(json.dumps(test_data))
    assert data_to_be_tested == test_data

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:18.437561
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml("roles: [common, webservers]")

# Generated at 2022-06-13 07:21:32.637292
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    testvals = {}
    testvals['int'] = 123
    testvals['float'] = 123.456
    testvals['str'] = 'str'
    testvals['unicode'] = u'unicode'
    testvals['list'] = [123, 123.456, 'str', u'unicode', []]
    testvals['dict'] = {'int': 123, 'float': 123.456, 'str': 'str', 'unicode': u'unicode', 'list': [], 'dict': {}}
    testvals['complex'] = {'int': 123, 'float': 123.456, 'str': 'str', 'unicode': u'unicode', 'list': [testvals['dict']],
                           'dict': testvals['dict']}

# Generated at 2022-06-13 07:21:37.042030
# Unit test for function from_yaml
def test_from_yaml():
    # Create a simple YAML file with a single key:value pair
    assert(from_yaml('hello: world') == {'hello': 'world'})
    # Make sure we can handle YAML lists
    assert(from_yaml('hello: [world, world]') == {'hello': ['world', 'world']})

# Generated at 2022-06-13 07:21:44.411526
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict

    examples = [
        (b'{', '{'),
        (b'[', '['),
    ]

    for data, expect in examples:
        result = from_yaml(data)
        assert result == expect, "%s != %s" % (result, expect)

    # test with vault secrets and vaulted item
    secret_vars = ImmutableDict(foo='hunter2')
    vault_secrets = ImmutableDict(
        vault_pass='pass',
        vault_identity_list=['~/.vault-id-1.txt'],
        vault_version=None,
        vault_secrets=secret_vars,
    )


# Generated at 2022-06-13 07:21:55.604573
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common._collections_compat import OrderedDict

    yaml_data = '''
- key1: value1
- key2: value2
- key3: value3
'''
    yaml_data_wo_dash = '''
key1: value1
key2: value2
key3: value3
'''
    yaml_data_dict = '''
key1: value1
key2: value2
key3: value3
'''
    yaml_data_wo_section = '''value'''
    yaml_data_wo_section2 = '''
- value1
- value2
- value3
'''

    yaml_data_dict = '''
key1: value1
key2: value2
key3: value3
'''
   

# Generated at 2022-06-13 07:22:01.877556
# Unit test for function from_yaml
def test_from_yaml():
    test_dict = dict(
        test_value=dict(
            test_sub_value=True
        )
    )

    json_data = json.dumps(test_dict)
    yaml_data = '---\n' + yaml.dump(test_dict)

    assert from_yaml(json_data) == test_dict
    assert from_yaml(yaml_data) == test_dict

# Generated at 2022-06-13 07:22:11.075972
# Unit test for function from_yaml

# Generated at 2022-06-13 07:22:25.472992
# Unit test for function from_yaml
def test_from_yaml():
    ''' test results of from_yaml function '''

    from ansible.parsing.yaml.dumper import AnsibleDumper
    data = AnsibleDumper(sort_keys=True).add_single_data(dict(str='str', true=True, false=False, int=10, float=3.14,
                                                              list=[1, 2, 3], dict={'a': 1, 'b': 2}))
    assert from_yaml(data) == dict(str='str', true=True, false=False, int=10, float=3.14, list=[1, 2, 3], dict={'a': 1, 'b': 2})

    bad_yaml = '''
I'm bad!
- [1,
- 2]
'''

# Generated at 2022-06-13 07:22:39.850589
# Unit test for function from_yaml
def test_from_yaml():
    """
    >>> assert from_yaml("{\"a\": 42}") == {'a': 42}
    >>> assert from_yaml("a: 42") == {'a': 42}
    >>> assert from_yaml("{\"a\": \"  42\"}") == {'a': '  42'}
    >>> assert from_yaml("a: \"  42\"") == {'a': '  42'}
    >>> assert from_yaml("a: 42") == {'a': 42}
    >>> assert from_yaml("a: 42\\n") == {'a': 42}
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 07:22:49.863044
# Unit test for function from_yaml
def test_from_yaml():
    json_string = '{"key": "value"}'

    # Verify that JSON is handled correctly
    assert from_yaml(json_string) == {u'key': u'value'}

    # Verify that YAML is handled correctly
    yaml_string = '''
        key: value
        key2: value2
    '''
    assert from_yaml(yaml_string) == {u'key': u'value', u'key2': u'value2'}

    # Verify that JSON_only works correctly
    json_only_string = '''
        key: value
        key2: value2
    '''
    with pytest.raises(AnsibleParserError):
        output = from_yaml(json_only_string, json_only=True)

# Generated at 2022-06-13 07:23:01.022198
# Unit test for function from_yaml
def test_from_yaml():
    result = from_yaml("""
- plugin: aws_ec2
  region: us-east-1
  image_name: "{{ image_name }}"
  instance_size: "{{ instance_size }}"
  count: 1
  wait: yes
  wait_timeout: 300
  state: running
  instance_tags:
    name: "{{ instance_prefix }}-{{ instance_name }}"
    environment: "{{ environment }}"
    role: "{{ role }}"
    role_group: "{{ role_group }}"
""")

# Generated at 2022-06-13 07:23:08.739766
# Unit test for function from_yaml
def test_from_yaml():
    test_string = '''
    {
        "key": "value",
        "key_array": ["value1", "value2"],
        "key_dict": {
            "key": {
                "key": "value",
                "key_array": ["value1", "value2"],
                "key_dict": {
                    "key": "value"
                }
            }
        }
    }
    '''
    result = from_yaml(test_string)
    assert result["key_array"][1] == "value2"
    assert result["key_dict"]["key"]["key_dict"]["key"] == "value"

    test_string = '''
    {
        key: value,
        key_array: [value1, value2]
    }
    '''
    result

# Generated at 2022-06-13 07:23:17.589615
# Unit test for function from_yaml
def test_from_yaml():
    # a couple of test cases
    yaml_test_cases = (
        (u'{}', u'', u'empty string test'),
        (u'[]', u'', u'no playbook test'),
        (u'[{"hosts": "all", "vars": {}, "tasks": []}]', u'all', u'empty task test'),
        (u'{"foo": "bar"}', u'bar', u'simple json test'),
        (u'{ foo : bar }', u'', u'simple yaml test'),
    )

    for test_yaml, test_hosts, test_desc in yaml_test_cases:
        test_data = from_yaml(test_yaml)

# Generated at 2022-06-13 07:23:21.855763
# Unit test for function from_yaml
def test_from_yaml():
    new_data = from_yaml('{"name": "test"}')
    assert new_data == {u'name': u'test'}

    new_data = from_yaml('{"test": "ok", "test2": 1}')
    assert new_data == {u'test': u'ok', u'test2': 1}

# Generated at 2022-06-13 07:23:31.064745
# Unit test for function from_yaml
def test_from_yaml():
    # test, that simple yaml file is loaded ok
    yaml_data = "---\na: 1\nb: 2"
    data = from_yaml(yaml_data)
    assert 'a' in data
    assert data['a'] == 1
    assert 'b' in data
    assert data['b'] == 2

    # test, that simple JSON file is loaded ok
    json_data = "{ \"a\": 1, \"b\": 2 }"
    data = from_yaml(json_data)
    assert 'a' in data
    assert data['a'] == 1
    assert 'b' in data
    assert data['b'] == 2

    # test, that vault file is loaded ok

# Generated at 2022-06-13 07:23:35.007156
# Unit test for function from_yaml
def test_from_yaml():
    json_test = "foo: bar\n"
    assert from_yaml(json_test, file_name='<string>', show_content=True, vault_secrets=None, json_only=False) == {'foo': 'bar'}


# Generated at 2022-06-13 07:23:48.830090
# Unit test for function from_yaml
def test_from_yaml():

    yamlstr = """
    key1: value1
    key2:
      - value2
      - value3
      - value4
    """

    jsonstr = """
    {
      "key1": "value1",
      "key2": [
        "value2",
        "value3",
        "value4"
      ]
    }
    """

    def assert_data(data, expected):
        for key, value in expected.items():
            if key in data:
                assert data[key] == value
            else:
                assert False, "Key '%s' is missing from datastructure '%s'" % (key, expected)

    for data in [yamlstr, jsonstr]:
        new_data = from_yaml(data, json_only=True)

# Generated at 2022-06-13 07:23:50.033455
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{ "foo": "bar" }'))


# Generated at 2022-06-13 07:23:57.119200
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml('{"a":1}')
    from_yaml('a: 1')
    try:
        from_yaml('{a:1}')
        assert False
    except AnsibleParserError:
        assert True
    try:
        from_yaml('a:1', json_only=True)
        assert False
    except AnsibleParserError:
        assert True

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:24:06.977807
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('', json_only=True) == None
    assert from_yaml('invalid', json_only=True) == None
    assert from_yaml('{"valid": "json"}', json_only=True) == {"valid": "json"}
    assert from_yaml('{"valid": "json"}' ) == {"valid": "json"}
    assert from_yaml('valid: "yaml"') == {"valid": "yaml"}
    assert from_yaml('{"valid": "json"}', json_only=True) == {"valid": "json"}
    assert from_yaml('{"valid": "json"}', json_only=False) == {"valid": "json"}
    assert from_yaml('valid: "yaml"', json_only=True) == None

# Generated at 2022-06-13 07:24:18.432564
# Unit test for function from_yaml
def test_from_yaml():
    # Verify that we can generate the proper json error even if the yaml is not valid
    # and that this happens even though the proper key was in the data.
    # Also, the json.loads() call above should have already removed the vault secrets from the string
    # before it is passed to the yaml parser.

    my_vault_secret = dict(test_test='test_test')
    my_vault_secrets = [my_vault_secret]

    # try to process an invalid yaml string with a vault secret in it

# Generated at 2022-06-13 07:24:32.546714
# Unit test for function from_yaml
def test_from_yaml():
    import os
    class MockVaultSecret:
        def __init__(self, *args, **kwargs):
            pass
        def decrypt(self, vault_data):
            return vault_data

    test_data = os.path.join(os.path.dirname(__file__), "data", "parser_json_yaml.yml")
    val = from_yaml(open(test_data, "r").read(), file_name=test_data, vault_secrets=MockVaultSecret)
    if 'dict_with_json_and_vault_before' not in val:
        raise AssertionError("dict_with_json_and_vault_before not found")
    if val['dict_with_json_and_vault_before']['key1'] != 'red':
        raise Assert

# Generated at 2022-06-13 07:24:44.074187
# Unit test for function from_yaml
def test_from_yaml():
    ansible_yaml = '''---
ansible: dict
test:
- dict
test2:
- dict2
test3:
  dict: dict
'''
    ansible_yaml2 = '''---
ansible: dict
test:
- dict
test2:
- dict2
test3:
  dict: dict
'''

    check = '''
    ---
    ansible: dict
    test:
      - dict
    test2:
      - dict2
    test3:
      dict: dict
    '''

    res = from_yaml(ansible_yaml)
    assert res == from_yaml(ansible_yaml2)
    res2 = from_yaml(ansible_yaml2)
    assert res2 == from_yaml(check)


# Generated at 2022-06-13 07:24:52.526610
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    import os
    from ansible.module_utils.common._collections_compat import MutableSequence

    s = u'{"a": "value"}'
    r = from_yaml(data=s)
    assert (r == {u'a': u'value'})

    s = u'{"a": "value"}'
    r = from_yaml(data=s)
    assert (r == {u'a': u'value'})

    s = u'{"a": "value"}'
    r = from_yaml(data=s)
    assert (r == {u'a': u'value'})

    vault_secrets = [u'vaultsecret']

# Generated at 2022-06-13 07:25:04.601008
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"some_key\": null}") == {u'some_key': None}
    assert from_yaml("{'some_key': 'some_value'}") == {u'some_key': u'some_value'}
    assert from_yaml("{'some_key': 'some_value'}", json_only=True) == {u'some_key': u'some_value'}
    assert from_yaml("{'some_key': 'some_value'}", json_only=False) == {u'some_key': u'some_value'}
    assert from_yaml("{key: 'value'}", json_only=False) == {u'key': u'value'}
    assert from_yaml("key: 'value'", json_only=False)

# Generated at 2022-06-13 07:25:07.242528
# Unit test for function from_yaml
def test_from_yaml():
    test_str = "[1, 2, 3]"
    assert from_yaml(test_str, file_name='<string>') == [1, 2, 3]

# Generated at 2022-06-13 07:25:11.309358
# Unit test for function from_yaml
def test_from_yaml():
    """
    Test ability to read a yaml file and convert it to a python dictionary.
    """
    yaml_str = '''
    ---
    - hosts: all
      tasks:
        - shell: echo "Hello, world!"
    '''
    dict_data = from_yaml(yaml_str)
    assert dict_data is not None

# Generated at 2022-06-13 07:25:16.826312
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml_test = from_yaml('''{
    "comments": {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
}
''')

    assert(from_yaml_test['comments']['key1'] == 'value1')
    assert(from_yaml_test['comments']['key2'] == 'value2')
    assert(from_yaml_test['comments']['key3'] == 'value3')


# Generated at 2022-06-13 07:25:18.108453
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": 1}') == {"a": 1}

# Generated at 2022-06-13 07:25:25.321837
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text

    # Encoding tests
    if PY3:
        # Python3 unicode string
        assert from_yaml(to_text(u'hello')) == [to_text(u'hello')]

        # Python3 byte string encoded in ASCII
        assert from_yaml(to_bytes(u'hello')) == [to_text(u'hello')]

        # Python3 byte string encoded in UTF-8
        assert from_yaml(to_bytes(u'h\xe9')) == [to_text(u'h\xe9')]

        # Python3 byte string encoded in ISO-8859-1

# Generated at 2022-06-13 07:25:33.526643
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '{"a": {"a1": 1, "a2": 2}, "b": 3}'
    json_data = json.loads(json_str)
    yaml_data = from_yaml(json_str)
    assert yaml_data == json_data
    assert yaml_data == {"a": {"a1": 1, "a2": 2}, "b": 3}

    yaml_str = 'a:\n  a1: 1\n  a2: 2\nb: 3'
    json_data = json.loads(json_str)
    yaml_data = from_yaml(yaml_str)
    assert yaml_data == json_data
    assert yaml_data == {"a": {"a1": 1, "a2": 2}, "b": 3}

    yaml_

# Generated at 2022-06-13 07:25:42.567062
# Unit test for function from_yaml
def test_from_yaml():
    print('Testing from_yaml ...')
    from ansible import constants as C
    C.HOST_KEY_CHECKING = False
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import cStringIO
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    result = loader.load_from_file('unittest/test_data/test_vault.yml')
    assert len(result) == 3
    assert result[0].get('test') == 'secret'
    module = AnsibleModule(
        argument_spec={},
    )
    fixed_result = from_yaml(b(module.jsonify(result, pretty=True)))

# Generated at 2022-06-13 07:25:56.038229
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("---\n- hosts: localhost\n  tasks:\n  - debug: var=ansible_os_family") == [{'hosts': 'localhost', 'tasks': [{'debug': {'var': 'ansible_os_family'}}]}]
    # test the yaml object
    assert from_yaml(AnsibleBaseYAMLObject("---\nyourtext")) == "yourtext"
    assert from_yaml("---\n" + "yourtext") == "yourtext"
    # test number parsing
    assert from_yaml("---\n- 1024") == [1024]
    assert from_yaml("---\n- 3.14") == [3.14]

# Generated at 2022-06-13 07:26:08.441922
# Unit test for function from_yaml
def test_from_yaml():

    # Test 1 - ensure this method returns the proper object type
    #          for all of our supported data types
    types = dict(
        string = "string",
        list   = [ "list" ],
        dict   = dict( foo = "dict" ),
        number = 42,
        null   = None,
        bool   = True,
    )
    for t in types:
        data = from_yaml(json.dumps(types[t]), file_name='<string>')
        assert type(data) is type(types[t])

    # Test 2 - check that from_yaml() is not just a wrapper for json.loads() or yaml.safe_load()
    #          (i.e. ensure that the file name is being added to the yaml object)
    filename = "/tmp/foo"
    data = from_

# Generated at 2022-06-13 07:26:24.728054
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'{}') == {}
    assert from_yaml(u'[]') == []
    assert from_yaml(u'["foo", "bar"]') == ["foo", "bar"]
    assert from_yaml(u'["foo", "bar"]', json_only=True) == ["foo", "bar"]
    assert from_yaml(u'foo: bar') == {u'foo': u'bar'}
    assert from_yaml(u'foo: bar', json_only=True) == u'foo: bar'

# Generated at 2022-06-13 07:26:33.200478
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_native
    import pytest
    display = Display()
    yaml_path = './test/integration/ansible_module_meta_yaml_list.yml'
    display.vvvv("Testing yaml in file " + yaml_path)
    yaml_content = AnsibleBaseYAMLObject(filename=yaml_path)
    assert yaml_content.data[0].keys() == {'name', 'documentation', 'version_added', 'short_description'}
    assert "The Ansible modules" == yaml_content.data[0]['short_description']
    # test error handling

# Generated at 2022-06-13 07:26:44.330471
# Unit test for function from_yaml
def test_from_yaml():

    class TestAnsibleVaultSecret(object):
        def __init__(self, vault_password):
            self.password = vault_password

    test_vault_secret = TestAnsibleVaultSecret('my_secret_key')

    # Various valid YAMLs
    from_yaml('{}')
    from_yaml('foo: bar', vault_secrets=[test_vault_secret])
    from_yaml('foo:\n- bar')
    from_yaml('foo: !!str 42')

# Generated at 2022-06-13 07:26:50.608062
# Unit test for function from_yaml
def test_from_yaml():
    try:
        new_data = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
        assert new_data == {'foo': 'bar', 'bam': {'hello': 'world'}}
    except Exception as error:
        assert False

# Generated at 2022-06-13 07:27:02.906552
# Unit test for function from_yaml
def test_from_yaml():
    json_only = False
    data = '{\n  "foo": "bar"\n}'
    file_name = "test/file/name"
    show_content = True
    vault_secrets = None
    new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert new_data == {"foo": "bar"}

    # Test if from_yaml throws exception for invalid JSON
    data = '{\n  "foo": "bar"\n'
    file_name = "test/file/name"
    show_content = True
    vault_secrets = None
    json_only = True

# Generated at 2022-06-13 07:27:16.922095
# Unit test for function from_yaml
def test_from_yaml():
    # Test single data
    assert from_yaml('foo') == 'foo'
    assert from_yaml('1') == 1

    # Test multiple data
    assert from_yaml('foo\n---\nbar') == ['foo', 'bar']

    # Test JSON
    assert from_yaml('{"foo": "bar"}') == {'foo': 'bar'}

    # Test YAML
    # FIXME: this test should fail but tests/core/inventory/test_group_vars.py depends on this output
    assert from_yaml('foo: bar\n') == {'foo': 'bar'}

    # Test empty data

# Generated at 2022-06-13 07:27:26.889874
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    # Test that the custom error handling logic works
    class FakeYAMLException(YAMLError):
        problem_mark = 'foo'

    class FakeJSONException(Exception):
        pass

    invalid_yaml = """{ foo: "bar" """
    try:
        from_yaml(invalid_yaml, 'myfile', vault_secrets=['foo'])
        assert False
    except AnsibleParserError as e:
        file, line, col = e.obj.ansible_pos
        assert file == 'myfile'
        assert line == 1
        assert col == 8
        assert isinstance(e.obj, AnsibleBaseYAMLObject)

    # Test that we can load a valid YAML file
   

# Generated at 2022-06-13 07:27:35.936449
# Unit test for function from_yaml
def test_from_yaml():
    # This test will be executed only if invoked as standalone
    # Unit test for function from_yaml
    json_input = '["foo", "bar"]'
    result = from_yaml(json_input)