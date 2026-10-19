

# Generated at 2022-06-13 07:17:37.779705
# Unit test for function from_yaml
def test_from_yaml():
    # Tests that function from_yaml successfully converts YAML string to a python dictionary
    assert from_yaml('{test:test}') == {'test':'test'}, "Function from_yaml failed to convert YAML string to python dictionary."


# Replaces function from_yaml
from_yaml = from_yaml

# Generated at 2022-06-13 07:17:47.208713
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = """{
    "foo": "test",
    "bar": [ "test1", "test2" ],
    "bam": {
        "baz": "test3"
    }
}"""

    result = from_yaml(data)
    assert(result['foo'] == 'test')
    assert(result['bam']['baz'] == 'test3')
    assert(result['bar'][1] == 'test2')

    data = """
- foo: test
- bar:
    - test1
    - test2
- bam:
    baz: test3
"""

    result = from_yaml(data)
    assert(result[0]['foo'] == 'test')

# Generated at 2022-06-13 07:17:57.723573
# Unit test for function from_yaml
def test_from_yaml():
    data = "['one', 'two', 'three']"


# Generated at 2022-06-13 07:18:03.896731
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"omg\": [1,2,3]}") == {u'omg': [1, 2, 3]}
    assert from_yaml("{\"omg\": [1,2,3]}", show_content=False) == {u'omg': [1, 2, 3]}
    assert from_yaml("{\"omg\": [1,2,3]}", show_content=True) == {u'omg': [1, 2, 3]}
    assert from_yaml("{\"omg\": [1,2,3]}", show_content=False) == {u'omg': [1, 2, 3]}

# Generated at 2022-06-13 07:18:14.005098
# Unit test for function from_yaml
def test_from_yaml():
    pytest.importorskip('yaml')
    import sys
    import io
    import os
    import tempfile
    import shutil
    import ansible.constants as C
    from ansible.parsing.yaml.dumper import AnsibleDumper

    curdir = os.path.dirname(__file__)
    data_path = curdir + '/../../lib/ansible/module_utils/splitter.py'

    yaml_data = open(data_path).read()
    json_data = json.dumps(yaml.load(yaml_data), cls=AnsibleJSONEncoder, sort_keys=True)
    json_data1 = json.dumps(yaml.load(yaml_data, Loader=AnsibleUnsafeLoader), sort_keys=True)
    json

# Generated at 2022-06-13 07:18:24.107496
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Test normal YAML
    yaml_data = """
    foo: bar
    baz: 42
    """
    assert loader.load(yaml_data) == {"foo": "bar", "baz": 42}

    # Test if YAML returns an error when we expect JSON
    yaml_data = """
    foo: bar
    baz: 42
    """
    try:
        loader.load(yaml_data, json_only=True)
    except AnsibleParserError:
        pass
    else:
        pytest.fail("DataLoader should return an AnsibleParserError when JSON is expected")

    # Test if JSON returns an error when we expect YAML

# Generated at 2022-06-13 07:18:29.459187
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    data = u"%YAML 1.2\n---\n" + u'{"test":"asdf"}'
    assert loader.load(data) == {'test': 'asdf'}

# Generated at 2022-06-13 07:18:37.344970
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars import combine_vars

    # The YAML parser handles many types of data.  We need to test each
    # type of data to verify that the parser is handling them correctly.

    # Test YAML parse of list
    data = [ 1, 2, 3, 4, 5 ]
    test_data = from_yaml(AnsibleDumper(default_flow_style=False).dump(data))
    assert test_data == [1, 2, 3, 4, 5]

    # Test YAML parse of string
    data = 'This is a test'

# Generated at 2022-06-13 07:18:44.628244
# Unit test for function from_yaml
def test_from_yaml():

    class AnsibleFailJson(Exception):
        ''' a custom exception class that represents failure in a Ansible module '''

    assert(from_yaml('{ "basic": true }') == { 'basic': True })

    # when report_errors is False, no exception is raised
    try:
        from_yaml('{ basic": true }')
        assert(True)
    except Exception as e:
        assert(False)

    try:
        from_yaml('{ basic": true }', show_content=False)
        assert(True)
    except Exception as e:
        assert(False)

    # when report_errors is True, exception is raised
    try:
        from_yaml('{ basic": true }', show_content=True)
        assert(False)
    except Exception as e:
        assert(True)


# Generated at 2022-06-13 07:18:56.369003
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.collections import ImmutableDict
    data = from_yaml('{"test": "data"}')
    assert (data == {'test': 'data'})
    data = from_yaml('{"test": !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          34356637386163363961663836306336626361393534616539313339376233323236326265626161\n          36363\n          65346565663139636435313739383538306462323832626334623636666433616462663638396462\n          646332\n          3136363265623163666238\n          }')

# Generated at 2022-06-13 07:19:07.157502
# Unit test for function from_yaml
def test_from_yaml():
    # Test empty object
    obj = from_yaml('{}')
    assert obj == {}

    # Test empty string
    obj = from_yaml('""')
    assert obj == ''

    # Test null
    obj = from_yaml('null')
    assert obj is None

    # Test empty array
    obj = from_yaml('[]')
    assert obj == []

    # Test simple array
    obj = from_yaml('["a","b","c"]')
    assert obj == ['a', 'b', 'c']

    # Test simple array with json
    obj = from_yaml('["a","b","c"]', json_only=True)
    assert obj == ['a', 'b', 'c']

    # Test simple object

# Generated at 2022-06-13 07:19:12.769146
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    name: "test"
    age: 1
    '''
    expected = {
        "name": "test",
        "age": 1
    }
    assert from_yaml(data) == expected

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:19:18.025051
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "my_var": "value" }', json_only=True) == { "my_var": "value" }
    assert from_yaml('{ "my_var": "value" }') == { "my_var": "value" }
    assert from_yaml('my_var: value') == { "my_var": "value" }

# Generated at 2022-06-13 07:19:28.049468
# Unit test for function from_yaml
def test_from_yaml():
    # Testing with valid yaml
    yaml_data = ''
    yaml_data += '---\n'
    yaml_data += '- hosts:\n'
    yaml_data += '    - all\n'
    yaml_data += '  become:\n'
    yaml_data += '    - yes\n'
    yaml_data += '  gather_facts:\n'
    yaml_data += '    - no\n'
    yaml_data += '  tasks:\n'
    yaml_data += '    - name: This is a test module\n'
    yaml_data += '      testmodule:\n'
    yaml_data += '        test_string: "{{ string_var }}"\n\n'

    from ansible.parsing.ajson import AnsibleJSONDec

# Generated at 2022-06-13 07:19:33.395030
# Unit test for function from_yaml
def test_from_yaml():
    ''' validates if from_yaml() parses valid json and yaml '''
    def assert_equal(file_name, data, vars):
        assert from_yaml(data, file_name=file_name) == vars

    assert_equal('json.json', '{"a": "b"}', {'a': 'b'})
    assert_equal('json.yml', '{"a": "b"}', {'a': 'b'})
    assert_equal('yaml.yml', 'a: b', {'a': 'b'})


# Generated at 2022-06-13 07:19:45.020952
# Unit test for function from_yaml
def test_from_yaml():
    # Demonstrates that from_yaml() can successfully parse JSON as well as YAML
    assert from_yaml(json.dumps({'a': 1, 'b': 2, 'c': 3})) == {'a': 1, 'b': 2, 'c': 3}
    assert from_yaml('a: 1\nb: 2\nc: 3\n') == {'a': 1, 'b': 2, 'c': 3}

    # Demonstrates that from_yaml() can successfully parse JSON with comments
    assert from_yaml('// this is a comment\n// and this is\n{\n"a": 1\n}') == {'a': 1}
    assert from_yaml('/* this is a comment\n * and this is */\n{"a": 1}') == {'a': 1}

   

# Generated at 2022-06-13 07:19:50.270892
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    ---
    i: 3
    j:
        - [1, 2, 3]
    k:
    '''
    assert from_yaml(data, file_name='<string>') == {
        'i' : 3,
        'j' : [
            [1, 2, 3]
        ],
        'k' : None
    }


# Generated at 2022-06-13 07:19:55.460939
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml('{"foo": "bar"}')
    from_yaml('{"foo": "bar"}', json_only=True)
    from_yaml('foo: bar')
    from_yaml('foo: bar', json_only=False)

    # TODO: add more unit tests

# Generated at 2022-06-13 07:20:06.357372
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test the from_yaml function to produce the correct output against sample test data
    '''
    sample_data = """
        ---
        - hosts: localhost
          tasks:
            - name: "Return hello world"
              debug:
                msg: "Hello world!"
                verbosity: 1
              when: false
    """

    assert {"hosts": "localhost",
            "tasks": [{"name": "Return hello world",
                       "debug": {"msg": "Hello world!", "verbosity": 1},
                       "when": False}]} == from_yaml(sample_data)

# Generated at 2022-06-13 07:20:17.426222
# Unit test for function from_yaml
def test_from_yaml():

    import sys
    import pytest
    if sys.version_info < (2, 7):
        pytest.skip("from_yaml() only required on Python 2.7 or later")
    elif sys.version_info >= (3, 0) and sys.version_info < (3, 4):
        pytest.skip("from_yaml() does not work on Python 3.0 - 3.3")

    from collections import MutableMapping
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

# Generated at 2022-06-13 07:20:22.201710
# Unit test for function from_yaml
def test_from_yaml():

    assert from_yaml("""
        - alpha
        - bravo
        - charlie
    """) == [u'alpha', u'bravo', u'charlie']

# Generated at 2022-06-13 07:20:29.955910
# Unit test for function from_yaml
def test_from_yaml():
    import string, random
    # Test non-JSON
    for repeated in range(0, 10):
        for i in range(0, 1000):
            if i % 100 == 0:
                print('i = ', i)
            s = ''.join(random.choice(string.ascii_letters) for _ in range(i))
            with open('test.txt', 'w') as f:
                f.write(s)
            j = from_yaml(s)
            s2 = json.dumps(j)
            j2 = json.loads(s2)
            assert j == j2

    # Test JSON
    for repeated in range(0, 10):
        for i in range(0, 1000):
            if i % 100 == 0:
                print('i = ', i)
            s = ''

# Generated at 2022-06-13 07:20:36.139075
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a":"b"}') == {"a":"b"}
    assert from_yaml('a: b') == {"a": "b"}
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]
    assert from_yaml('[1, 2, 3]') != [1, 2, 0]
    assert from_yaml('[1, 2, 3]') != [1, 2, 4]

# Generated at 2022-06-13 07:20:47.202948
# Unit test for function from_yaml
def test_from_yaml():
    # Test case 1
    # test the case of yaml and json data
    json_data = '{"abc": [{"def": "ghi"}]}'
    yaml_data = '---\n abc: [{ def: ghi }]\n'
    assert from_yaml(yaml_data) == from_yaml(json_data)

    # Test case 2
    # test the case of vars for parser
    yaml_data = '---\n abc: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          353936613661346337613665303738353336366465313963323663656661646664626565343963\n          30613739\n          '

# Generated at 2022-06-13 07:20:56.842256
# Unit test for function from_yaml
def test_from_yaml():
    datastructure = { 'first': 1, 'second': 2 }

    data = json.dumps(datastructure)
    assert from_yaml(data) == datastructure
    assert from_yaml(data) != None

    data = 'this is not json'
    try:
        from_yaml(data)
        assert False
    except AnsibleParserError:
        assert True

    data = 'key: value'
    assert from_yaml(data) != None
    assert from_yaml(data) != datastructure

# Generated at 2022-06-13 07:20:59.576245
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{ 'foo': 'bar' }") == {'foo': 'bar'}



# Generated at 2022-06-13 07:21:09.798351
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    yaml_text = '''
        ---
        testhost:
          key: string
          key2: 42
    '''
    yaml_from_string = from_yaml(yaml_text)
    assert isinstance(yaml_from_string, dict)
    assert len(yaml_from_string) == 1
    assert yaml_from_string['testhost'] is not None
    assert yaml_from_string['testhost']['key'] == u'string'
    assert yaml_from_string['testhost']['key2'] == 42
    assert isinstance(yaml_from_string['testhost'], AnsibleMapping)

# Generated at 2022-06-13 07:21:14.471258
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("{}"), dict)
    assert isinstance(from_yaml("[]"), list)
    assert isinstance(from_yaml("[1,2,3]"), list)
    assert isinstance(from_yaml("""---
a: 1
b: 2
c: 3
"""), dict)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:20.129394
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.ahjson import from_yaml
    from ansible.vars.manager import VariableManager

    import tempfile
    import os

    data_json = """
{
    "foo": true,
    "bar": false
}
"""

    data_yaml = """
---
foo: true
bar: false
"""

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(data_json)
        f.close()
        vars = from_yaml(data_json)
        assert(vars['foo'] and not vars['bar'])
        vars = from_yaml(open(f.name))
        assert(vars['foo'] and not vars['bar'])
        os.unlink(f.name)


# Generated at 2022-06-13 07:21:29.345476
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"hello": "world"}') == {u'hello': u'world'}
    assert from_yaml('hello: world') == {u'hello': u'world'}
    assert from_yaml('hello: world', json_only=True) == {u'hello': u'world'}
    assert from_yaml('1234') == 1234

    yaml_fail_tests = [
        '{ hello: world }',
        'hello: world\nbye: world',
        '',
        ' '
    ]

    for data in yaml_fail_tests:
        try:
            from_yaml(data, file_name='<string>', json_only=True)
        except AnsibleParserError:
            pass

# Generated at 2022-06-13 07:21:40.800388
# Unit test for function from_yaml
def test_from_yaml():
    "Run unit tests for AnsibleParserError and AnsibleBaseYAMLObject."
    import sys
    import unittest
    import ansible.module_utils.basic
    from ansible.module_utils.six import StringIO

    class TestAnsibleParserException(unittest.TestCase):
        """Test class for ansible_parser module."""

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_correct_error_msg(self):
            """Test if error msg is correct."""
            yaml_error = """
                found unknown escape character '\\%c'
                in "test.yml", line 1, column 6
                %s
                      ^
            """ % ('a', 'a')

# Generated at 2022-06-13 07:21:45.204398
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    assert isinstance(DataLoader().load_from_file("tests/test_from_yaml.yaml"), dict) is True

# Generated at 2022-06-13 07:21:50.464629
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""---
a: 1
b: 2
c: [ 3, 4, 5 ]""") == {"a": 1, "b": 2, "c": [3, 4, 5]}
    assert from_yaml("""
a: 1
b: 2
c: [ 3, 4, 5 ]
""") == {"a": 1, "b": 2, "c": [3, 4, 5]}

# Generated at 2022-06-13 07:21:55.844691
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

# Generated at 2022-06-13 07:22:03.053107
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml('{ "test": { "test": { "test": 4 } } }'), dict)
    assert isinstance(from_yaml('test: test: test: 4'), dict)
    assert from_yaml('{ "test": { "test": { "test": 4 } } }')['test']['test']['test'] == 4
    assert from_yaml('test: test: test: 4')['test']['test']['test'] == 4

# Generated at 2022-06-13 07:22:11.776070
# Unit test for function from_yaml
def test_from_yaml():

    from ansible.module_utils.common.collections import is_sequence, is_set
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types

    vault_secrets = [{'vault_secret': 'vault_test_secret'}]

# Generated at 2022-06-13 07:22:20.680352
# Unit test for function from_yaml
def test_from_yaml():
    datastructure = '{"a": "b"}'
    data = from_yaml(datastructure)
    assert data == {"a": "b"}

    datastructure = "{'a': 'b'}"
    data = from_yaml(datastructure)
    assert data == {"a": "b"}

    # The following should fail to parse
    datastructure = "{'a': 'b',"
    try:
        data = from_yaml(datastructure)
    except AnsibleParserError:
        pass



# Generated at 2022-06-13 07:22:27.062032
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3

    test_string_json = "{\"AllCaps\":\"test\"}"
    test_dict_json = {"AllCaps": "test"}

    if PY3:
        assert from_yaml(test_string_json, json_only=True) == test_dict_json
    else:
        assert from_yaml(test_string_json.decode('utf-8'), json_only=True) == test_dict_json

# Generated at 2022-06-13 07:22:39.139384
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # Simple test case
    data = {
        'a': 1,
        'b': 2,
        'c': 'd'
    }
    yaml_data = AnsibleDumper().dump(data, None)

    assert data == from_yaml(yaml_data)

    # Mark test case
    data = {
        'key1': AnsibleMapping(None, 'problem'),
        'key2': AnsibleMapping(None, 'problem'),
        'key3': AnsibleMapping(None, 'problem')
    }

# Generated at 2022-06-13 07:22:48.545526
# Unit test for function from_yaml

# Generated at 2022-06-13 07:22:57.990316
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"b":"hi", "a":{"b":{"c":"hi" }, "c":"hi"}}'
    json_expect = {u'b': u'hi', u'a': {u'b': {u'c': u'hi'}, u'c': u'hi'}}
    json_only = from_yaml(data, json_only=True)
    yaml = from_yaml(data)
    assert json_expect == json_only, 'json_only failed'
    assert json_expect == yaml, 'yaml failed to match json'

# Generated at 2022-06-13 07:23:03.239072
# Unit test for function from_yaml
def test_from_yaml():
    data = """
    ---
    - name: foo
      - name: bar
    - name: baz
    """

    assert from_yaml(data) == [
        {'name': ['foo', {'name': 'bar'}]},
        {'name': 'baz'}
    ]

    data = """
    ---
    - name: foo
    - name: baz
    """

    assert from_yaml(data) == [
        {'name': 'foo'},
        {'name': 'baz'}
    ]

# Generated at 2022-06-13 07:23:12.428261
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    - hosts: all
      gather_facts: False
      tasks:
        - name: test
          debug: var=hostvars[inventory_hostname]['ansible_all_ipv4_addresses']
          ignore_errors: yes
          tags:
            - always
    '''

    new_data = from_yaml(data)
    assert new_data
    assert new_data == [{'hosts': 'all', 'gather_facts': False, 'tasks': [{'debug': "var=hostvars[inventory_hostname]['ansible_all_ipv4_addresses']",
                                                                          'ignore_errors': 'yes', 'name': 'test',
                                                                          'tags': ['always']}]}]

    # If data is already a dict
   

# Generated at 2022-06-13 07:23:19.918795
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-13 07:23:28.686559
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('"This is a JSON String"'))
    print(from_yaml('["This","is","a","JSON","Array"]'))
    print(from_yaml('"This is a JSON String"', json_only=True))
    try:
        from_yaml('["This","is","a","YAML","Array"]', json_only=True)
    except AnsibleParserError as e:
        print(e)
    try:
        from_yaml('["This","is","a","YAML","Array"]')
    except AnsibleParserError as e:
        print(e)
    print(from_yaml('[This,"is","a","YAML","Array"]'))
    print(from_yaml('[This,"is",a,"YAML","Array"]'))
   

# Generated at 2022-06-13 07:23:34.652466
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": 1}') == {"a": 1}
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

    assert from_yaml('a: 1\nb: 2\n') == {"a": 1, "b": 2}

    assert from_yaml('a: 1\nb: 2\n', json_only=True)

# Generated at 2022-06-13 07:23:48.648814
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import ansible.constants as C
    import ansible.utils.template as template

    data = b'{ "foo": "{{ lookup("pipe", "echo bar") }}" }'
    template.jinja2.filters.update(C.DEFAULT_JINJA2_FILTERS)
    res = from_yaml(data)
    assert res == dict(foo='bar')

    data = '{ "foo": "{{ lookup("pipe", "echo bar") }}" }'
    res = from_yaml(data)
    assert res == dict(foo='bar')

    # Test for environment vars
    os.environ['ANSIBLE_TEST_FOO'] = 'bar'
    data = b'{ "foo": "{{ lookup("env","ANSIBLE_TEST_FOO") }}" }'

# Generated at 2022-06-13 07:23:58.665184
# Unit test for function from_yaml
def test_from_yaml():
    test_data = b'''
    # This is just a comment
    hello:
      # This is just another comment
      world: #Nope not a comment here
        # But this is one
        - 1
        - 2
        - 3
    '''
    output = from_yaml(test_data)
    assert output == {'hello': {'world': [1, 2, 3]}}

    test_data = b'''
    foo:
      bar: 1
      baz:
      - 1
      - 2
      - 3
    '''
    output = from_yaml(test_data)
    assert output == {'foo': {'bar': 1, 'baz': [1, 2, 3]}}



# Generated at 2022-06-13 07:24:08.035411
# Unit test for function from_yaml
def test_from_yaml():

    expected_data = {
        'status': 'success',
        'error': {
            'code': '200'
        },
        'data': [
            '0',
            '1'
        ]
    }
    sample_json_data = '{"status": "success", "error": {"code": "200"}, "data": ["0", "1"]}'
    sample_yaml_data = """
status: success
error:
    code: 200
data:
    - 0
    - 1
"""

    assert from_yaml(sample_json_data) == expected_data
    assert from_yaml(sample_yaml_data) == expected_data


# Generated at 2022-06-13 07:24:18.106444
# Unit test for function from_yaml
def test_from_yaml():
    # Test JSON decode
    json_data = '{"foo": "bar", "bam": ["this", "is", "json"]}'
    assert from_yaml(json_data, json_only=True) == {"foo": "bar", "bam": ["this", "is", "json"]}

    # Test YAML decode
    yaml_data = '''
    foo: "bar"
    bam:
      - "this"
      - "is"
      - "yaml"
    '''
    assert from_yaml(yaml_data) == {"foo": "bar", "bam": ["this", "is", "yaml"]}

# Generated at 2022-06-13 07:24:34.657847
# Unit test for function from_yaml
def test_from_yaml():
    # Test loading a single string (YAML or JSON)
    d = "str"
    assert from_yaml(d) == "str"

    # Test loading a single integer (YAML or JSON)
    d = "42"
    assert from_yaml(d) == 42

    # Test loading a naked list (YAML)
    d = "- a\n- b"
    assert from_yaml(d) == ['a', 'b']

    # Test loading a list (JSON)
    d = '["foo", "bar"]'
    assert from_yaml(d) == ['foo', 'bar']

    # Test loading a dict (YAML)
    d = '''
test:
  - foo
  - bar
'''

# Generated at 2022-06-13 07:24:44.338354
# Unit test for function from_yaml
def test_from_yaml():
    # FIXME: not a true unit test ... should be converted to real unit test
    #  assert from_yaml(dict(a=1)) == dict(a=1)
    #  assert from_yaml(dict(a='foo')) == dict(a='foo')
    #  assert from_yaml(dict(a='{{ foo }}')) == dict(a='{{ foo }}')
    assert from_yaml('{ "a": 1 }') == dict(a=1)
    assert from_yaml('{ "a": "{{ foo }}" }') == dict(a=u'{{ foo }}')
    assert from_yaml('{ "a": "foo" }') == dict(a=u'foo')

# Generated at 2022-06-13 07:24:49.816000
# Unit test for function from_yaml
def test_from_yaml():
    test_data = [
        ('hello world', 'hello world'),
        ('{ "a": 1 }', {'a': 1}),
        ('[ 1, 2, 3 ]', [1, 2, 3]),
        ('{"a":"1"}', {'a': '1'})
    ]
    for test_string, expected_value in test_data:
        assert expected_value == from_yaml(test_string)
    return True

# Generated at 2022-06-13 07:24:58.664001
# Unit test for function from_yaml
def test_from_yaml():
    try:
        # Unit test for function from_yaml
        data = '''
        ---
        - name: this is a list
          hosts: all
          gather_facts: no
          tasks:
            - name: command test
              command: /usr/bin/foo
              register: output
        
          vars:
            some_var: "{{ lookup('env','HOME') }}"
    
        '''
        new_data = from_yaml(data)
    except Exception as e:
        raise
    else:
        assert isinstance(new_data, list)
        assert isinstance(new_data[0], dict)

# Generated at 2022-06-13 07:25:05.210194
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "this": "is", "a": "dictionary" }') == {"this": "is", "a": "dictionary"}
    assert from_yaml('[ "this", "is", "a", "list" ]') == ["this", "is", "a", "list"]
    assert from_yaml('"this is a string"') == "this is a string"
    assert from_yaml('foo') is None
    assert from_yaml('"foo"') == "foo"
    assert from_yaml('null') is None
    assert from_yaml('{}') == {}

# Generated at 2022-06-13 07:25:06.154297
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    import sys
    import os

# Generated at 2022-06-13 07:25:13.201540
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"hello": "world"}') == {"hello": "world"}
    assert from_yaml('---\nhello: world') == {"hello": "world"}
    assert from_yaml('{"hello": "world"}', json_only=True) == {"hello": "world"}
    try:
        from_yaml('---\nhello: world', json_only=True)
        assert False, "from_yaml(json_only=True) with a yaml string should fail"
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:25:16.340879
# Unit test for function from_yaml
def test_from_yaml():
    data = """
            foo: bar
        """
    new_data = from_yaml(data)
    assert {'foo': 'bar'} == new_data


# Generated at 2022-06-13 07:25:22.616148
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("{'foo': 'bar'}"), dict)
    assert from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    assert from_yaml("{'foo': [1,2,3,{'hello':'world', 'nested':{'foo':'bar'}}]}") == {'foo': [1,2,3,{'hello':'world', 'nested':{'foo':'bar'}}]}
    assert from_yaml("[1,2,3]") == [1,2,3]
    assert from_yaml("[1,2,3]", json_only=True) == [1,2,3]

# Generated at 2022-06-13 07:25:31.340845
# Unit test for function from_yaml
def test_from_yaml():
    res = from_yaml('{"this": "is json"}')
    assert res == {"this": "is json"}

    res = from_yaml("{'this': 'is json'}")
    assert res == {"this": "is json"}

    res = from_yaml("this: 'is yaml'")
    assert res == {"this": "is yaml"}

    res = from_yaml("{this: 'is text'}")
    assert res == "{this: 'is text'}"

    try:
        from_yaml("this: is text")
        assert False
    except AnsibleParserError:
        pass


# Generated at 2022-06-13 07:25:43.480199
# Unit test for function from_yaml
def test_from_yaml():
    '''
    basic test function to run to make sure our test data files can be loaded by ansible
    '''
    import unittest
    import os
    import yaml

    yaml_loader = yaml.FullLoader
    yaml_loader.add_constructor(u'tag:yaml.org,2002:timestamp', yaml_loader.construct_yaml_timestamp)

    class TestYamlFromAnsible(unittest.TestCase):
        '''
        run base tests on data from ansible repo, to make sure it's loading
        '''


# Generated at 2022-06-13 07:25:48.114321
# Unit test for function from_yaml
def test_from_yaml():
    """
    Creates a python datastructure from the given data, which can be either
    a JSON or YAML string.
    """
    try:
        from yaml import CSafeLoader as SafeLoader
    except ImportError:
        from yaml import SafeLoader

    import os
    import unittest

    from ansible.module_utils.common.network.config.base import BaseNetworkConfig

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    test_file_name = os.path.join(cur_dir, "test_config.txt")
    test_file_name2 = os.path.join(cur_dir, "test_config2.txt")
    test_file_name3 = os.path.join(cur_dir, "test_config3.txt")
   

# Generated at 2022-06-13 07:25:58.368382
# Unit test for function from_yaml
def test_from_yaml():
    print('Testing from_yaml function')

    a = '''
    {
    "A": "foo"
    }
    '''

    # Load a json document (no exceptions should be raised)
    test_json = from_yaml(a)
    assert test_json == {'A': 'foo'}

    b = '''
    {
    "A": "foo",
    "B": "life"
    }
    '''

    # Load a json document with a comma (no exceptions should be raised)
    test_json = from_yaml(b)
    assert test_json == {'A': 'foo', 'B': 'life'}

    c = '''
    {
    "A": 'foo'
    }
    '''

    # Load a json document with single quotes wrapped around the single word value

# Generated at 2022-06-13 07:26:10.489296
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleSequence

    a_dict = {'a': '123', 'b': [1, 2, 3]}
    a_yaml = u'a: 123\nb:\n- 1\n- 2\n- 3\n'

    a_dict_as_yaml = from_yaml(a_yaml)
    assert a_dict_as_yaml == a_dict

    a_dict_to_yaml = from_yaml(a_yaml, json_only=True)
    assert a_dict_to_yaml == a_dict

    a_dict_to_yaml = from_yaml(a_dict, json_only=True)
    assert a_dict_to_yaml == a_dict


# Generated at 2022-06-13 07:26:15.717120
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import pytest
    from ansible.parsing.ansible_yaml import from_yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    this_dir, this_filename = os.path.split(__file__)

    fake_vault_secrets = [{'partition': '0123456789ABCDEF0123', 'salt': 'salt'}]

    # Not encrypted YAML
    ds = from_yaml(open(os.path.join(this_dir, 'parse_data/not_encrypted.yaml'), 'r').read(), vault_secrets=fake_vault_secrets)
    assert ds == {'a': 'b', 'c': 'd'}

    # Encrypted YAML
   

# Generated at 2022-06-13 07:26:17.662875
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"foo\": 1}", "file_name")

# Generated at 2022-06-13 07:26:27.607115
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils._text import to_bytes
    import pkgutil

    test_yaml_data = pkgutil.get_data('ansible', 'test/lib/units/modules/test_from_yaml.yml')
    assert test_yaml_data is not None

    test_json_data = pkgutil.get_data('ansible', 'test/lib/units/modules/test_from_yaml.json')
    assert test_json_data is not None

    test_json_as_yaml_data = pkgutil.get_data('ansible', 'test/lib/units/modules/test_from_yaml_json_as_yaml.yml')
    assert test_json_as_yaml_data is not None

    # test YAML

# Generated at 2022-06-13 07:26:30.577551
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.collections import is_sequence
    result = []
    result = from_yaml('''
    - name: test_host
    ''')
    assert result != None
    assert is_sequence(result)

# Generated at 2022-06-13 07:26:34.549676
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "name": "example", "value": 42 }') == {u'name': u'example', u'value': 42}
    assert from_yaml('name: example\nvalue: 42\n') == {u'name': u'example', u'value': 42}

# Generated at 2022-06-13 07:26:46.398418
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Validate Ansible built-in type
    '''
    from ansible.parsing.yaml.objects import AnsibleUnicode
    data = u'foobar'
    new_data = from_yaml(data)
    assert isinstance(new_data, AnsibleUnicode)
    assert new_data == u"foobar"

    '''
    Validate Python bool type
    '''
    data = 'True'
    new_data = from_yaml(data)
    assert isinstance(new_data, bool)
    assert new_data is True

    data = 'true'
    new_data = from_yaml(data)
    assert isinstance(new_data, bool)
    assert new_data is True

    data = 'False'
    new_data = from_yaml

# Generated at 2022-06-13 07:26:56.781944
# Unit test for function from_yaml
def test_from_yaml():
    data = ('[{"name": "John", "age": 45}, {"name": "Jane", "age": 25}]')
    assert (from_yaml(data, file_name='<string>', show_content=True, json_only=True)
            == [{'name': 'John', 'age': 45}, {'name': 'Jane', 'age': 25}])

# Generated at 2022-06-13 07:27:00.968157
# Unit test for function from_yaml
def test_from_yaml():
    # Test the most straight-forward case
    data = '{"key": "value"}'
    assert from_yaml(data) == {"key": "value"}

    # Test to ensure that yaml can be loaded from a YAML file
    # and validates against the resulting dict
    data = '''
    ---
    key: value
    '''
    assert from_yaml(data) == {"key": "value"}

# Generated at 2022-06-13 07:27:06.319811
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('') is None, 'Empty string -> None'
    assert from_yaml('\n') is None, 'Empty line -> None'
    assert from_yaml('1') == 1, 'Integer -> integer'
    assert from_yaml('-1'), 'Negative integer -> integer'
    assert from_yaml('+1'), 'Positive integer -> integer'
    assert from_yaml('1.1') == 1.1, 'Decimal -> decimal'
    assert from_yaml('-1.1'), 'Negative decimal -> decimal'
    assert from_yaml('+1.1'), 'Positive decimal -> decimal'
    assert from_yaml('6.02e23') == 6.02e23, 'Scientific decimal -> decimal'

# Generated at 2022-06-13 07:27:19.432945
# Unit test for function from_yaml
def test_from_yaml():
    test_cases = [
                   """{
                   "tasks": [
                     {
                       "name": "Use assert to debug",
                       "local_action": {
                         "module": "lineinfile",
                         "dest": "/tmp/test.txt",
                         "state": "present",
                         "regexp": "^log_level=.*",
                         "line": "log_level=debug"
                       }
                     }
                   ]
                 }""",
            """
            ---
            - hosts: local
              user: root
              become: True
              tasks:
              - name: test basic ansible json file
                script: /tmp/test
              """,
            """
            ---
            - name: test basic ansible json file
              script: /tmp/test
            """,
    ]


# Generated at 2022-06-13 07:27:30.800246
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml('{"foo": 42}')
    except Exception as e:
        assert False, "json is accepted by from_yaml"

    try:
        from_yaml('foo: 42')
    except Exception as e:
        assert False, "yaml is accepted by from_yaml"

    try:
        from_yaml('foo: 42', json_only=True)
        assert False, "yaml is rejected by from_yaml with json_only=True"
    except Exception as e:
        assert True, "yaml is rejected by from_yaml with json_only=True"
