

# Generated at 2022-06-13 07:17:45.804294
# Unit test for function from_yaml

# Generated at 2022-06-13 07:17:56.443187
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from test.units.parsing.yaml.loader import load_fixture, assert_results

    # test the successful loading of a yaml file
    example_yaml = load_fixture('test_from_yaml.yaml')
    assert_results('test_from_yaml.yaml', example_yaml)

    # test that the yaml parser errors out for a json file
    with pytest.raises(AnsibleParserError):
        example_json = load_fixture('test_from_yaml.json')
        from_yaml(example_json)

    # test that the yaml parser errors out for a yaml file with a syntax error

# Generated at 2022-06-13 07:18:03.706393
# Unit test for function from_yaml
def test_from_yaml():
    data = """
        { "good": true, "broken": "json", "fixed": ["json", "array"] }
    """
    assert from_yaml(data) == {
        u'good': True,
        u'broken': u'json',
        u'fixed': [u'json', u'array']
    }

    data = """
        good: True
        broken: "json"
        fixed:
            - "json"
            - "array"
    """
    assert from_yaml(data) == {
        u'good': True,
        u'broken': u'json',
        u'fixed': [u'json', u'array']
    }

# Generated at 2022-06-13 07:18:10.899639
# Unit test for function from_yaml
def test_from_yaml():
    json_data = r'{"a":{"b":{"c":"d"}}}'
    yaml_data = r'a:{"b":{"c":"d"}}'
    data = from_yaml(json_data)
    assert(data == {"a":{"b":{"c":"d"}}})
    data = from_yaml(yaml_data)
    assert(data == {"a":{"b":{"c":"d"}}})

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:17.381781
# Unit test for function from_yaml
def test_from_yaml():
    import json
    import os
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    src = os.path.dirname(__file__)
    src = os.path.join(src, 'data', 'yaml.yml')
    with open(src, 'rb') as f:
        data = f.read()

    res = from_yaml(data)
    assert isinstance(res, dict)
    assert res['foo'] == 'bar'
    assert res['a']['b']['c']['d']['e']['f']['g'] == 'h'
    assert res['one'][0] == 'two'
    assert res['one'][1]

# Generated at 2022-06-13 07:18:31.223450
# Unit test for function from_yaml
def test_from_yaml():
    # Testing for error cases
    try:
        from_yaml("{}", json_only=True)
        assert False, "Should not get here!"
    except Exception as e:
        assert isinstance(e, AnsibleParserError)
    try:
        from_yaml("{ }")
        assert False, "Should not get here!"
    except Exception as e:
        assert isinstance(e, AnsibleParserError)
    try:
        from_yaml("{ }", json_only=False)
        assert False, "Should not get here!"
    except Exception as e:
        assert isinstance(e, AnsibleParserError)

    # Testing for happy path.
    data = from_yaml("{}", json_only=True)
    assert data == {}, "Should be equal"

    data = from_yaml

# Generated at 2022-06-13 07:18:36.304005
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo') is None
    assert from_yaml('{}') == {}
    assert from_yaml('[1,2,3]') == [1,2,3]
    assert from_yaml('{"foo": "bar"}') == {'foo': 'bar'}

    assert from_yaml('---\nfoo: bar') == {'foo': 'bar'}
    assert from_yaml('---\n- foo\n- bar') == ['foo', 'bar']

    assert from_yaml('# Test') is None
    assert from_yaml('---\n# Test') == '# Test'
    assert from_yaml('---\n# Test\nfoo: bar') == {'# Test': None, 'foo': 'bar'}


# Generated at 2022-06-13 07:18:44.005821
# Unit test for function from_yaml
def test_from_yaml():
    # Test good json
    assert from_yaml('{"hello": "world"}') == {u'hello': 'world'}
    # Test good json-list
    assert from_yaml('[{"hello": "world"}, {"bye": "world"}]') == [{u'hello': 'world'}, {u'bye': 'world'}]
    # Test good yaml
    assert from_yaml('hello: world') == {u'hello': 'world'}
    # Test good yaml-list
    assert from_yaml('- hello: world\n- bye: world') == [{u'hello': 'world'}, {u'bye': 'world'}]
    # Test good yaml-list

# Generated at 2022-06-13 07:18:56.007986
# Unit test for function from_yaml
def test_from_yaml():
    # Some examples from yaml.org
    """
    This is a JSON string (YAML is a superset of JSON):
    {
        "a": ["b", "c"],
        "d": {"e": "f"}
    }
    """
    assert from_yaml('{ "a": ["b", "c"], "d": {"e": "f"} }') == {'a': ['b', 'c'], 'd': {'e': 'f'}}

    """
    This is a YAML document:
    ---
    a: ["b", "c"]
    d: {e: f}
    """

# Generated at 2022-06-13 07:19:03.360722
# Unit test for function from_yaml
def test_from_yaml():
    json_string = '{"name": "Ben Scott"}'
    yaml_string = "name: Ben Scott"
    data = from_yaml(json_string)
    assert data['name'] == 'Ben Scott'
    #data = from_yaml(json_string, json_only=True)
    #assert data['name'] == 'Ben Scott'
    data = from_yaml(yaml_string)
    assert data['name'] == 'Ben Scott'

# Generated at 2022-06-13 07:19:19.428446
# Unit test for function from_yaml
def test_from_yaml():
    d1 = from_yaml("""
- 1
- 2
- 3
- 4
- 5
    """)
    assert d1 == [1, 2, 3, 4, 5], d1

    d2 = from_yaml("""
{a: 1}
    """)
    assert d2 == {'a': 1}, d2

    d3 = from_yaml("""
a: 1
    """)
    assert d3 == {'a': 1}, d3

    d4 = from_yaml("""
a:
  - 1
  - 2
  - 3
    """)
    assert d4 == {'a': [1, 2, 3]}, d4

    d5 = from_yaml("""
a: 1
b: 2
    """)

# Generated at 2022-06-13 07:19:22.869068
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(b'{"foo": "bar"}', file_name='my_file.yaml') == {"foo": "bar"}


# unit test for class AnsibleJSONDecoder

# Generated at 2022-06-13 07:19:31.292430
# Unit test for function from_yaml
def test_from_yaml():
    test_var = dict(
        yaml_str = "this is yaml",
        json_str = "this is json",
        yaml_dict = dict(name="this is yaml dict"),
        json_dict = dict(name="this is json dict")
    )

    # a dict
    yaml_dict = dict(
        name = "YAML",
        test_yaml_str = test_var["yaml_str"],
        test_json_str = test_var["json_str"],
        test_yaml_dict = test_var["yaml_dict"],
        test_json_dict = test_var["json_dict"]
    )

    # json string

# Generated at 2022-06-13 07:19:36.834129
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.vault import VaultLib
    try:
        from yaml import CSafeLoader as SafeLoader, CSafeDumper as SafeDumper
    except ImportError:
        from yaml import SafeLoader, SafeDumper

    vault_password = '$ANSIBLE_VAULT;1.1;AES256'
    vault = VaultLib([])
    vault_secret = vault.encrypt(vault_password, 'foobar')

# Generated at 2022-06-13 07:19:47.661114
# Unit test for function from_yaml
def test_from_yaml():
    # Test for JSON support
    data = '{"foo": "bar"}'
    new_data = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert new_data == json.loads(data, cls=AnsibleJSONDecoder)

    # Test for YAML support
    data = '{foo: bar}'
    new_data = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert new_data == _safe_load(data, file_name='<string>', vault_secrets=None)

# Generated at 2022-06-13 07:19:57.679080
# Unit test for function from_yaml

# Generated at 2022-06-13 07:20:10.899573
# Unit test for function from_yaml
def test_from_yaml():

    # Test the original case of a non-JSON string.
    valid_yaml = '''
    foo:
      - 1
      - two
      - 0x3
    '''

    assert from_yaml(valid_yaml) == {'foo': [1, u'two', 3]}

    # Test the JSON string case.
    valid_json = '{"foo": [1, "two", 3]}'

    assert from_yaml(valid_json) == {'foo': [1, u'two', 3]}

    # Test the broken YAML case.
    in_valid_yaml = '''
    "foo": [1, "two", 3]}}
    '''

    try:
        from_yaml(in_valid_yaml)
        assert False
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 07:20:21.892777
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.utils.objects as utils
    import ansible.parsing.vault as vault
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import ansible.parsing.yaml.loader as yaml_loader
    import ansible.vars.manager as var_manager
    import ansible.utils.vars as vars_utils

    # Test that AnsibleVaultEncryptedUnicode is parsed as JSON.
    # Note: AnsibleVaultEncryptedUnicode is a subclass of unicode
    # Note: Test this to get 100% coverage

    # Create test string

# Generated at 2022-06-13 07:20:32.829531
# Unit test for function from_yaml
def test_from_yaml():
    try:
        # This malformed yaml is expected to fail
        from_yaml('''
        -
        - "a": b
        - "c": d
        ''')
    except AnsibleParserError:
        pass
    else:
        raise AssertionError("Test failed")
    # All following yaml are expected to succeed
    assert from_yaml('') is None
    assert from_yaml('''
    foo:
      - bar: baz
    ''') == {u'foo': [{u'bar': u'baz'}]}
    assert from_yaml('''
    foo:
      - baz
    ''') == {u'foo': [u'baz']}
    assert from_yaml('''
    foo: "bar"
    ''')

# Generated at 2022-06-13 07:20:42.355772
# Unit test for function from_yaml
def test_from_yaml():
    class DummyTransformer():
        def __init__(self):
            self.data = None
        def transform_data(self, secret_data):
            return self.data
    from_yaml('''---
---
- { host: testhost1, flags: revision, dest: /tmp/testhost1 }
- { host: testhost2, flags: revision, dest: /tmp/testhost2 }
''')
    from_yaml('''---
- { host: testhost1, flags: revision, dest: /tmp/testhost1 }
- { host: testhost2, flags: revision, dest: /tmp/testhost2 }
''')
    transformer = DummyTransformer()
    transformer.data = {}

# Generated at 2022-06-13 07:20:50.417567
# Unit test for function from_yaml
def test_from_yaml():

    # Loading JSON: should return an object
    data = '{"foo":"bar"}'
    assert isinstance(from_yaml(data), dict)

    # Loading YAML: should return an object
    data = b'foo: bar\n'
    assert isinstance(from_yaml(data, file_name='<string>'), dict)

# Generated at 2022-06-13 07:21:01.281916
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import get_file_vault_secret
    data1 = """ a_dict: {foo: bar}"""
    data2 = """a_dict: {foo: bar}"""
    data3 = """a_dict: {foo: bar}"""
    d1 = from_yaml(data1, json_only=True)
    d2 = from_yaml(data2)
    d3 = from_yaml(data3)
    assert d1 == d2 == d3
    data4 = """
    ---
    foo: bar
    """
    config = {}
    config['vault_password_file'] = '/etc/ansible/vault_password'
   

# Generated at 2022-06-13 07:21:07.200596
# Unit test for function from_yaml
def test_from_yaml():
    string = '[1, 2, 3]'
    assert from_yaml(string) == json.loads(string)

    string = '[1, 2, 3'
    try:
        from_yaml(string)
        assert False
    except AnsibleParserError:
        assert True
    except:
        assert False

# Generated at 2022-06-13 07:21:19.059140
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    TEST_DATA = [
        (
            "{'a': 'b'}",
            {u'a': u'b'},
        ),
    ]

    class TestYaml(unittest.TestCase):

        def test(self):
            for yaml_data_in, dict_data_out in TEST_DATA:
                try:
                    data = from_yaml(yaml_data_in)
                except:
                    self.assertFail('Failed to load yaml data: {0}'.format(yaml_data_in))
                else:
                    self.assertEqual(data, dict_data_out)

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 07:21:33.286776
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test YAML string to python object conversion
    '''

    # Test data

# Generated at 2022-06-13 07:21:41.491023
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes

    test_data = """
        {
            "a": 1,
            "b": 2,
            "c": [
                "d",
                "e",
                {
                    "f": "g",
                    "h": "i"
                }
            ]
        }
        """

    result = from_yaml(to_bytes(test_data))
    assert result
    assert isinstance(result, Mapping)
    assert len(result) == 3
    assert 'a' in result
    assert result['a'] == 1
    assert 'b' in result
    assert result['b'] == 2
    assert 'c' in result

# Generated at 2022-06-13 07:21:47.848779
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestFromYaml(unittest.TestCase):
        def test_from_yaml(self):
            import ansible.parsing.yaml

            # Very simple test just to make sure that the test_from_yaml function
            # is not broken:

            # This is a valid YAML file that should be decoded correctly:
            data1 = r'''---
a: 10
'''
            self.assertEqual(ansible.parsing.yaml.from_yaml(data1), {u'a': 10})
            # This is a valid JSON file that should be decoded correctly:
            data2 = r'''{"a": 10}
'''

# Generated at 2022-06-13 07:21:51.957178
# Unit test for function from_yaml
def test_from_yaml():

    data = {
        'foo': [
            1, 2, 3
        ]
    }

    data_str = json.dumps(data)

    new_data = from_yaml(data_str)

    assert data == new_data

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:57.301376
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("1234"), int)
    assert isinstance(from_yaml("true"), bool)
    assert isinstance(from_yaml("false"), bool)
    assert isinstance(from_yaml("{\"a\": 1}"), dict)
    assert isinstance(from_yaml("[1, 2, 3]"), list)
    assert isinstance(from_yaml("\"abc\""), str)

    assert from_yaml("1234") == 1234
    assert from_yaml("true") == True
    assert from_yaml("false") == False
    assert from_yaml("{\"a\": 1}") == {"a": 1}
    assert from_yaml("[1, 2, 3]") == [1, 2, 3]

# Generated at 2022-06-13 07:22:08.366600
# Unit test for function from_yaml
def test_from_yaml():
    # Test that json can be parsed
    text = '{"a":{"b":"c","d":{"e":"f","g":{"h":"i","j":{"k":"l"}}}}}'
    data = from_yaml(text)
    assert data['a']['b'] == 'c'
    assert data['a']['d']['e'] == 'f'
    assert data['a']['d']['g']['h'] == 'i'
    assert data['a']['d']['g']['j']['k'] == 'l'

    # Test that yaml can be parsed
    text = '''
        a:
          b: c
          d:
            e: f
            g:
              h: i
              j:
                k: l'''

# Generated at 2022-06-13 07:22:25.592126
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    import unittest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    script_dir = os.path.dirname(os.path.realpath(__file__))
    vault_pass = script_dir + "/../../../.vault_pass"

    class TestFromYaml(unittest.TestCase):
        def setUp(self):
            self.vault_secrets = ['vault']

        def test_from_json(self):
            json_string = b'{"hello": "world"}'
            result = from_yaml(json_string)
            self.assertEqual(result, {u'hello': u'world'})


# Generated at 2022-06-13 07:22:39.986128
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo') == 'foo'
    assert from_yaml('{foo:bar}') == dict(foo='bar')
    assert from_yaml('[foo:bar]') == [dict(foo='bar')]
    assert from_yaml('{"foo":bar}') == dict(foo='bar')
    assert from_yaml('{"foo":bar}', json_only=True) == dict(foo='bar')
    assert from_yaml('[foo, bar]') == ['foo', 'bar']
    assert from_yaml('foo: bar') == dict(foo='bar')
    assert from_yaml('foo: null') == dict(foo=None)
    assert from_yaml('foo: None') == dict(foo=None)
    assert from_yaml('foo: "null"') == dict

# Generated at 2022-06-13 07:22:49.575534
# Unit test for function from_yaml
def test_from_yaml():

    # Test with valid JSON data
    json_data = """
{
    "foo": {
        "bar": {
            "baz": "qux"
        }
    }
}
"""
    # Convert to dict
    py_data = from_yaml(json_data)
    assert type(py_data) is dict

    # Test with valid YAML data
    yaml_data = """
foos:
    - foo:
        - bar:
            - baz:
                - qux
            - qux:
                - qux
    - baz:
        - qux
    - baz:
        - qux
"""
    # Convert to dict
    py_data = from_yaml(yaml_data)
    assert type(py_data) is dict

# Generated at 2022-06-13 07:23:00.757304
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys

    def test_assert(condition, original, expected, actual, message):
        if not condition:
            print("Test failed!")
            print("Original input:")
            print(original)
            print("Expected result:")
            print(expected)
            print("Actual result:")
            print(actual)
            print("Message:")
            print(message)
            print()

            assert condition

    def test_yaml(input, expected, message):
        input = input.encode('utf-8')
        actual = from_yaml(input)
        test_assert(actual == expected, input, expected, actual, message)


# Generated at 2022-06-13 07:23:05.930415
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    - name: test_yaml
      data:
        a: b
    '''
    expect_data = [
        {
            'name': 'test_yaml',
            'data': {
                'a': 'b'
            }
        }
    ]
    got_data = from_yaml(data)
    assert isinstance(got_data, list)
    assert got_data == expect_data

# Generated at 2022-06-13 07:23:11.619467
# Unit test for function from_yaml
def test_from_yaml():
    yaml_text = """
    --- 
    # example
    name:
        # details
        family: Smith       # very common
        given: Alice        # one of the siblings
 
    children:
      - name: Alice
        age: 8
      - name: Bob
        age: 10
    """
    data = from_yaml(yaml_text)
    assert(data["children"][0]["age"] == 8)
    assert(data["children"][1]["age"] == 10)


# Generated at 2022-06-13 07:23:21.700373
# Unit test for function from_yaml
def test_from_yaml():
    # Testing basic yml
    yml_string = '''
    a: 1
    b: 2
    c: string
    d:
      e: 1
      f: 2
    '''

    assert from_yaml(yml_string) == {'a': 1, 'b': 2, 'c': 'string', 'd': {'e': 1, 'f': 2}}

    # Testing basic json
    json_string = '''
    {
        "a": 1,
        "b": 2,
        "c": "string",
        "d": {
            "e": 1,
            "f": 2
        }
    }
    '''


# Generated at 2022-06-13 07:23:26.082960
# Unit test for function from_yaml
def test_from_yaml():
    test_str = """
        - hosts: all
          become: true
          roles:
            - { role: role_one, tags: [one] }
            - { role: role_two, tags: [two] }
            - { role: role_three, tags: [three] }
    """
    from_yaml(test_str)

# Generated at 2022-06-13 07:23:30.817341
# Unit test for function from_yaml
def test_from_yaml():
    test_str = "key: 'value'"
    assert {u'key': u'value'} == from_yaml(test_str)
    test_str = "{'key': 'value'}"
    assert {u'key': u'value'} == from_yaml(test_str)



# Generated at 2022-06-13 07:23:39.022785
# Unit test for function from_yaml
def test_from_yaml():
    # valid yaml
    yaml_dict = {
        'foo': {
            'bar': 'baz',
            'boo': 10,
            'bam': [
                1, 2, 3
            ]
        }
    }

    yaml_str = r'''
        foo:
            bar: baz
            boo: 10
            bam:
                - 1
                - 2
                - 3
        '''

    # should return the same dict no matter what
    assert from_yaml(yaml_str, file_name='<string>') == yaml_dict
    assert from_yaml(yaml_dict, file_name='<dict>') == yaml_dict
    assert from_yaml(json.dumps(yaml_dict), file_name='<json>') == yaml_dict

# Generated at 2022-06-13 07:23:46.349497
# Unit test for function from_yaml
def test_from_yaml():
    yaml_blob = "---\n" \
    "- hosts: all\n" \
    "  become: true\n"
    test_data = from_yaml(yaml_blob)
    assert test_data[0]['hosts'] == 'all'
    assert test_data[0]['become'] is True

# Generated at 2022-06-13 07:23:50.110339
# Unit test for function from_yaml
def test_from_yaml():
    data = {'foo': {'bar': 'baz'}}
    assert data == from_yaml(json.dumps(data))
    assert data == from_yaml(json.dumps(data), json_only=True)
    assert data == from_yaml(yaml.dump(data))
    assert data == from_yaml(yaml.dump(data), json_only=True)



# Generated at 2022-06-13 07:24:01.293357
# Unit test for function from_yaml
def test_from_yaml():
    #valid YAML
    test_string = '''
---
- name: this is a simple test
  hosts: localhost
'''
    try:
        res = from_yaml(test_string)
    except AnsibleParserError as e:
        e.show_content=False
        raise
    #valid JSON
    test_string = '''
{
  "hosts": "localhost",
  "name": "this is a simple test"
}
'''
    try:
        res = from_yaml(test_string)
    except AnsibleParserError as e:
        e.show_content=False
        raise
    #invalid JSON
    test_string = '''
{
  "hosts": "localhost",
  "name": "this is a simple test",
'''

# Generated at 2022-06-13 07:24:01.923286
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:24:10.222834
# Unit test for function from_yaml
def test_from_yaml():
    t1 = ("""\
---
- hosts: all
  tasks:
    - name: test
      debug:
        msg: OK
""")
    t = from_yaml(t1)
    assert len(t) == 1
    assert t[0]['hosts'] == 'all'
    assert len(t[0]['tasks']) == 1
    assert t[0]['tasks'][0]['name'] == 'test'
    assert t[0]['tasks'][0]['debug']['msg'] == 'OK'

    t1 = ("""\
---

- hosts: all
  tasks:
    - name: test
      debug:
        msg: OK
""")
    t = from_yaml(t1)
    assert len(t) == 1

# Generated at 2022-06-13 07:24:18.784469
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('''
---
- hosts: localhost
  connection: local
  gather_facts: False
  tasks:
  - name: ping
    ping:
''') == [{'hosts': 'localhost', 'connection': 'local',
          'gather_facts': False, 'tasks': [{'name': 'ping', 'ping': {}}]}]
    assert from_yaml('{ "hello": "world", "is": "JSON"}') == {'hello': 'world', 'is': 'JSON'}



# Generated at 2022-06-13 07:24:30.312093
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    results = from_yaml(loader=loader, variable_manager=variable_manager, data=u"""
a: 1
b:
    - 2
    - 3
    - 4
    - 5
    -
       a: 6
""")
    assert results == { u"a": 1, u"b":[2,3,4,5, {u"a": 6}] }

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:24:42.057684
# Unit test for function from_yaml
def test_from_yaml():

    yaml_str = '''{
       "foo": [
         "a",
         "b",
         "c"
       ],
       "bar": {
         "a": "A",
         "b": "B",
         "c": "C"
       },
       "baz": "example"
     }'''
    assert from_yaml(yaml_str) == {'bar': {'a': 'A', 'b': 'B', 'c': 'C'}, 'baz': 'example', 'foo': ['a', 'b', 'c']}


# Generated at 2022-06-13 07:24:51.550980
# Unit test for function from_yaml
def test_from_yaml():
    test_data_dir = "./test/unit/parsing/yaml/"
    bad_data = open(test_data_dir + "bad.yml").read()
    good_data = open(test_data_dir + "good.yml").read()
    jinja_data = open(test_data_dir + "jinja_bad.j2").read()
    empty_data = open(test_data_dir + "empty.yml").read()


# Generated at 2022-06-13 07:24:54.669000
# Unit test for function from_yaml
def test_from_yaml():
    # Just make sure we can load a string
    assert from_yaml('{ "a": "b" }') == {'a': 'b'}

# Generated at 2022-06-13 07:25:07.944612
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"a\": [ 'x', \"y\" ], \"b\": {\"c\": 12, \"d\": false }}") == dict(a=['x', 'y'], b=dict(c=12, d=False))
    assert from_yaml("a: 1") == dict(a=1)
    assert from_yaml("a: - 1") == dict(a=[-1])
    assert from_yaml("{\"a\":\"{{ b }}\"}") == dict(a="{{ b }}")
    assert from_yaml("{\"a\":\"{{ b.c.d.e }}\"}") == dict(a="{{ b.c.d.e }}")

# Generated at 2022-06-13 07:25:10.724880
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    assert isinstance(from_yaml("{'a': '5', 'b': 6, 'c': ['1', '2', '3']}"), AnsibleMapping)

# Generated at 2022-06-13 07:25:16.860942
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("test: ok") == {"test": "ok"}
    assert from_yaml("{test: ok}") == {"test": "ok"}
    assert from_yaml("{\"test\": ok}") == {"test": "ok"}
    assert from_yaml("{\"test\": \"ok\"}") == {"test": "ok"}
    try:
        from_yaml("{test: ok")
        assert False
    except AnsibleParserError:
        pass
    try:
        from_yaml("{\"test\": ok")
        assert False
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:25:20.359926
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('a: [ 1, 2, 3 ]') == {'a': [1, 2, 3]}
    assert from_yaml('a: 1') == {'a': 1}
    assert from_yaml('a: "1"') == {'a': '1'}

# Generated at 2022-06-13 07:25:27.012360
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestAnsibleModuleLoad(unittest.TestCase):

        def test_json_loads(self):
            data = dict(json_only=True,
                        show_content=True,
                        data=u'{"foo": "bar", "baz": [1, 2]}',
                        file_name=u'hello',
                        vault_secrets=None)

            result = from_yaml(**data)

            self.assertEqual(result, dict(foo=u'bar', baz=[1, 2]))


# Generated at 2022-06-13 07:25:31.118047
# Unit test for function from_yaml
def test_from_yaml():
    test_string = '{"foo": "bar" }'
    assert from_yaml(test_string) == {"foo": "bar" }
    test_string = "{foo: bar }"
    try:
        new_data = from_yaml(test_string)
        assert False
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 07:25:40.836781
# Unit test for function from_yaml
def test_from_yaml():
    string_valid_json = '{"one": 1, "two": 2, "three": 3}'
    string_valid_yaml = '{"one": 1, "two": 2, "three": 3}'
    string_invalid_json = '{"one": 1, "two": 2, "three": 3'
    string_invalid_yaml = '{"one": 1, "two": 2, "three": 3'
    assert from_yaml(string_valid_yaml, json_only=True) == {"one": 1, "two": 2, "three": 3}
    assert from_yaml(string_valid_json) == {"one": 1, "two": 2, "three": 3}

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:55.301301
# Unit test for function from_yaml
def test_from_yaml():
    try:
        result = from_yaml("string")
    except AnsibleParserError as e:
        assert False, "This string shoud not be invalid YAML."

    result = from_yaml("--- [1,2]")
    assert result == [1,2]

    try:
        result = from_yaml("string", json_only=True)
    except AnsibleParserError as e:
        assert False, "This string should not be invalid JSON."

    result = from_yaml("[1, 2]", json_only=True)
    assert result == [1,2]

    try:
        result = from_yaml("{'str':'str'}")
    except AnsibleParserError as e:
        assert False, "This string shoud not be invalid YAML."

# Generated at 2022-06-13 07:25:58.265132
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml('{"a": 123, "b": "hello"}')
    from_yaml('a: 123\nb: hello')



# Generated at 2022-06-13 07:26:03.368958
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import from_yaml
    file_content = "{\"foo\": 42, \"bar\": \"asdf\"}"
    res = from_yaml(file_content)
    assert res.get('foo') == 42 and res.get('bar') == "asdf"



# Generated at 2022-06-13 07:26:23.102650
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"a": "b", "c": "d"}'
    new_data = from_yaml(data)
    assert new_data == {u'a': u'b', u'c': u'd'}

    data = '{a: b, c: d}'
    new_data = from_yaml(data)
    assert new_data == {u'a': u'b', u'c': u'd'}

    data = '''
            foo: [
              {
                bar1: cool
                bar2: neat
              },
              {
                bar1: value
                bar3: stuff
              }
            ]'''
    new_data = from_yaml(data)

# Generated at 2022-06-13 07:26:29.638218
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    from ansible.parsing.vault import VaultLib
    vault = VaultLib("abcd")
    load = from_yaml("""{
        "a": "b",
        "c": {
            "d": "{{myvault|password}}",
            "e": "f"
        },
        "g": {
            "h": "i"
        }
    }""", vault_secrets=vault)

    assert load['c']['d'] == "password"


# Generated at 2022-06-13 07:26:36.152954
# Unit test for function from_yaml
def test_from_yaml():
    data1 = '{ "a" : 1 }'
    data2 = 'a : 1'
    data3 = '---\n- json_only: true\n'
    assert from_yaml(data1) == json.loads(data1)
    assert from_yaml(data2) == json.loads(json.dumps(data2))
    assert from_yaml(data3) == {'json_only': True}
    assert from_yaml(data3, json_only=True) == None

# Generated at 2022-06-13 07:26:47.831934
# Unit test for function from_yaml
def test_from_yaml():
    ''' Validate that our from_yaml implementation matches yaml.load '''

    import os
    import sys
    import tempfile
    import traceback
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    from ansible.parsing.yaml.dumper import AnsibleDumper

    from ansible.module_utils.basic import AnsibleModule

    def run_module():
        # argument specification
        fields = {
            "arg_spec": {
                "arg1": {"required": True, "type": "str"},
                "arg2": {"required": True, "type": "bool"},
                "arg3": {"required": True, "type": "list"},
            },
            "supports_check_mode": True
        }


# Generated at 2022-06-13 07:26:53.360227
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "test": "obj" }', json_only=True) == {"test": "obj"}
    assert from_yaml('test: obj') == {"test": "obj"}
    assert from_yaml('- test') == ["test"]

# Generated at 2022-06-13 07:27:03.900075
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing import vault

    # Test valid JSON
    json_string = u'{"the": "test"}'
    assert from_yaml(json_string) == {"the": "test"}

    # Test valid YAML
    yaml_string = u"---\n" \
                  u"the: test\n"
    assert from_yaml(yaml_string) == {"the": "test"}

    # Invalid JSON
    json_string = u'{"the": test}'
    try:
        from_yaml(json_string)
    except AnsibleParserError:
        pass
    else:
        assert False

    # Invalid YAML
    yaml_string = u"---\n" \
                  u"the: : test\n"

# Generated at 2022-06-13 07:27:13.915084
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

# Generated at 2022-06-13 07:27:18.728400
# Unit test for function from_yaml
def test_from_yaml():
    # This is not a unit test, merely a convenient way to call from_yaml from the
    # command line. The unit test should be run from the unit test directory.
    import sys
    if len(sys.argv) > 2:
        print(from_yaml(sys.argv[1], file_name=sys.argv[2]))
    elif len(sys.argv) > 1:
        print(from_yaml(sys.argv[1]))
    else:
        print(from_yaml(''))

# Generated at 2022-06-13 07:27:20.691351
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("---\nfoo: bar"), dict)
    assert isinstance(from_yaml("foo: bar"), dict)

# vim: set fileencoding=utf-8 sts=4 sw=4 et :

# Generated at 2022-06-13 07:27:28.984817
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml("1.2.3")
    from_yaml("---")
    from_yaml("---\n- 1.2.3")
    from_yaml("---\n- 1.2.3\n- 4.5.6")
    from_yaml("---\n- 1.2.3\n- 4.5.6\n- 7.8.9")