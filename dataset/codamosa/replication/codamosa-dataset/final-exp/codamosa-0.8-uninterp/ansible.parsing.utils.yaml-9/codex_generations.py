

# Generated at 2022-06-13 07:17:37.601300
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.dataloader
    assert isinstance(ansible.parsing.dataloader.from_yaml("---\n- test"), list)
    assert isinstance(ansible.parsing.dataloader.from_yaml("{}"), dict)
    assert isinstance(ansible.parsing.dataloader.from_yaml("test"), str)
    assert isinstance(ansible.parsing.dataloader.from_yaml("100"), int)

# Generated at 2022-06-13 07:17:47.033333
# Unit test for function from_yaml
def test_from_yaml():
    from nose.plugins.skip import SkipTest
    from ansible.module_utils import basic
    import sys

    def test_json_only(data_type, data, json_only):
        try:
            if json_only:
                raise SkipTest

            data_rep = basic.jsonify(from_yaml(data, json_only=json_only))
        except AnsibleParserError as e:
            if not json_only:
                # JSON should cause a parser error, and should not be supported
                assert False

            raise
        except SkipTest:
            # YAML should cause a parsing error, and should not be supported
            assert False

        if json_only:
            assert data_rep == data
        else:
            assert data_rep != data


# Generated at 2022-06-13 07:17:57.605908
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import pytest
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.vars.manager import VariableManager
    from ansible.vars import VAULT_SECRETS_MATCH

    test_source = os.path.join(os.path.dirname(__file__), "from_yaml_test.yml")
    test_dest = os.path.join(os.path.dirname(__file__), "from_yaml_test_dest.json")

    with open(test_source) as f:
        source_data = from_yaml(f.read(), file_name=test_source, vault_secrets=None)
    source_data_str = json.d

# Generated at 2022-06-13 07:18:02.822673
# Unit test for function from_yaml
def test_from_yaml():
    yaml_data = """
        ---
        # We are ignoring the json value as it is not important right now.
        # yaml version is the only one we care about.
        ansible_variable:
          yaml:
            json: junk
            yaml: success
    """
    json_data = '{"ansible_variable": {"yaml": {"json": "junk", "yaml": "success"}}}'

    assert from_yaml(yaml_data) == from_yaml(json_data)

# Generated at 2022-06-13 07:18:13.030264
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import ansible.parsing.yaml.objects
    from ansible.parsing.yaml.loader import AnsibleLoader

    sys.modules['ansible.parsing.yaml.objects'] = ansible.parsing.yaml.objects
    sys.modules['ansible.parsing.yaml.loader'] = AnsibleLoader

    os_path = os.path.dirname(os.path.realpath(__file__))
    samples_path = os.path.join(os_path, '..', 'ansible', 'utils', 'sample_vars')

    for f in os.listdir(samples_path):
        path = os.path.join(samples_path, f)
        with open(path, 'rb') as f:
            data = f.read

# Generated at 2022-06-13 07:18:24.000818
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[1,2,3]') == [1,2,3]
    assert from_yaml('[1,2,3]', json_only=True) == [1,2,3]
    assert from_yaml('["foo", "bar"]') == ["foo", "bar"]
    assert from_yaml('{"foo":"bar"}') == {"foo":"bar"}
    assert from_yaml('{"foo":"bar"}', json_only=True) == {"foo":"bar"}
    assert from_yaml('{"foo":"bar"},["a","b"]', show_content=False) == {u'foo': u'bar'}
    assert from_yaml('"baz"') == "baz"
    assert from_yaml('"baz"', json_only=True) == "baz"

# Generated at 2022-06-13 07:18:35.908533
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "key": "value" }') == { "key": "value" }
    assert from_yaml('key: value') == { "key": "value" }
    assert from_yaml('test:\n- item1\n- item2') == { "test": ["item1", "item2"] }
    assert from_yaml('{ "key": "value", "key2": "value2" }') == { "key": "value", "key2": "value2" }
    assert from_yaml('{ "key": 1 }') == { "key": 1 }
    assert from_yaml('key: 1') == { "key": 1 }
    assert from_yaml('{ "key": 1, "key2": 2 }') == { "key": 1, "key2": 2 }
   

# Generated at 2022-06-13 07:18:40.384941
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
{
    "foo": "bar",
    "list": [
        {
            "key": "value"
        }
    ]
}
'''
    new_data = from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert new_data['foo'] == 'bar'

# Generated at 2022-06-13 07:18:51.248534
# Unit test for function from_yaml
def test_from_yaml():
    # Test json input
    json_data = '{"name":"John Doe","age":25,"city":"New York","no_ansible_vars": {"test_var": $TEST_VAR}}'
    contents = from_json(json_data)
    assert contents is not None
    assert contents['name'] == 'John Doe'
    assert contents['age'] == 25
    assert contents['city'] == 'New York'
    assert contents['no_ansible_vars']['test_var'] == '$TEST_VAR'

    # Test yaml input
    yaml_data = '---\nname: John Doe\nage: 25\ncity: New York\nno_ansible_vars: {test_var: $TEST_VAR}\n'
    contents = from_yaml(yaml_data)

# Generated at 2022-06-13 07:18:58.905487
# Unit test for function from_yaml
def test_from_yaml():
    # Test json
    json_string = '''
    [
        {
            "name": "test",
            "colour": "test"
        }
    ]
    '''
    test_dict = from_yaml(json_string)
    assert test_dict[0]['name'] == 'test'
    assert test_dict[0]['colour'] == 'test'


    # Test yaml
    yaml_string = '''
    - name: test
      colour: test
    '''
    test_dict = from_yaml(yaml_string)
    assert test_dict[0]['name'] == 'test'
    assert test_dict[0]['colour'] == 'test'

# Generated at 2022-06-13 07:19:05.193341
# Unit test for function from_yaml
def test_from_yaml():

    test_data = '{"one": 1, "two": [2, 2], "three": {"four": 4}}'
    test_file_name = 'some_file'

    json_data = json.loads(test_data)
    yaml_data = from_yaml(test_data, test_file_name, False)
    assert yaml_data == json_data

# Generated at 2022-06-13 07:19:17.335312
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    # Make sure the current directory is in PYTHON_PATH,
    # so that
    # (1) ansible.parsing.yaml.loader can be imported
    # (2) ansible.__init__.py is executed to set __version__
    sys.path.append(os.getcwd())

    import ansible.parsing.dataloader

    ds = {'testing': 'data'}
    yds = ansible.parsing.dataloader.serialize(ds)

    try:
        ansible.parsing.dataloader.from_yaml(yds)
    except:
        raise AssertionError('Failed to parse yaml')

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:20.236732
# Unit test for function from_yaml
def test_from_yaml():

    with open("test_files/test_from_yaml.yml", 'r') as stream:
        print(from_yaml(stream.read()))



# Generated at 2022-06-13 07:19:27.155692
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    ---
    - hosts: localhost
      gather_facts: False
      tasks:
      - name: test command
        command: /bin/banana
    '''
    file_name = "test_file"
    show_content = True
    vault_secrets = None
    json_only = False

    new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert new_data['tasks'][0]['name'] == 'test command'

# Generated at 2022-06-13 07:19:30.354996
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("false") is False
    assert from_yaml("{}") == {}
    assert from_yaml("{\"a\":1}") == {"a": 1}

    with pytest.raises(AnsibleParserError):
        from_yaml("{\"a\"")

# Generated at 2022-06-13 07:19:32.813340
# Unit test for function from_yaml
def test_from_yaml():
    json_string = '{"name": "bob"}'
    assert from_yaml(json_string) == {"name": "bob"}
    yaml_string = 'name: bob'
    assert from_yaml(yaml_string) == {"name": "bob"}

# Generated at 2022-06-13 07:19:40.902058
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class FromYamlTest(unittest.TestCase):

        def test_from_yaml(self):
            test_input = '{ "test": "input" }'

            test_output = from_yaml(test_input)
            self.assertEqual(test_output, {'test': 'input'})

    # Run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(FromYamlTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 07:19:46.761448
# Unit test for function from_yaml
def test_from_yaml():
    text = "first_name: John\nlast_name: Doe\nage: 23\nweight: 65.2"
    assert isinstance(from_yaml(text), dict)
    text = "{\"first_name\": \"John\", \"last_name\": \"Doe\", \"age\": \"23\", \"weight\": \"65.2\"}"
    assert isinstance(from_yaml(text), dict)

# Generated at 2022-06-13 07:19:56.790039
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import unittest
    import shlex
    import test.utils.module_runner as module_runner

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'yaml_data')

    def _get_yaml_data(filename):
        file_path = os.path.join(data_dir, filename)
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            print("ERROR: Failed to read test data: %s" % file_path)
            raise e

    class TestYAMLParsing(unittest.TestCase):
        def test_empty(self):
            ''' Test parsing an empty file '''
            yaml_data = ""
            self.assertIs

# Generated at 2022-06-13 07:20:06.726734
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
---
- hosts: localhost
  connection: local
  vars:
    test_key: test_value
  tasks:
  - action: ping
'''
    try:
        d = from_yaml(data)
        assert d is not None
        assert d['vars']['test_key'] == 'test_value'
    except Exception as e:
        assert None, 'Unable to parse test data: {0}'.format(e)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:20:15.762831
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    yaml_dumper = AnsibleDumper()
    test_data = {'key1': 'value1', 'key2': 'value2', 'key3': {'key4': [1, 2, 3]}}
    yaml_data = yaml_dumper.dump(test_data, default_flow_style=False)
    return_data = from_yaml(yaml_data)
    assert test_data == return_data

# Generated at 2022-06-13 07:20:25.061476
# Unit test for function from_yaml
def test_from_yaml():
    try:
        test_data = [
            '',
            '[1,2,3]',
            '{"kd": "dv"}',
            'invalid json',
            'invalid: yaml'
        ]

        for data in test_data:
            data_passed = data
            try:
                data = from_yaml(data, json_only=True)
                data = json.dumps(data)
            except Exception as e:
                data = e.__class__.__name__

            assert data == data_passed, "%s != %s" % (data, data_passed)

    except:
        raise
    else:
        pass
    finally:
        pass


# Generated at 2022-06-13 07:20:36.296287
# Unit test for function from_yaml
def test_from_yaml():
    # smoke test - make sure our yaml loading works
    example_yaml = '''
    flow:
      - name: "Hello World"
        type: "say_hello"
        target: "console"
    '''
    data = from_yaml(example_yaml)
    assert data['flow'][0]['name'] == 'Hello World'

    # Make sure we can handle vaulted data

# Generated at 2022-06-13 07:20:47.204857
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import tempfile

    sample = '''
    ---
    - name: test 1
      tags:
       - always
    '''

    # create a YAML file to work with
    temp = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    temp.write(sample)
    temp.close()

    # parse the YAML file
    with open(temp.name, 'rb') as f:
        data = from_yaml(f.read(), file_name=temp.name)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data == [{'tags': ['always'], 'name': 'test 1'}]

    # clean up the file
    if sys.version_info < (3, 0):
        import os
       

# Generated at 2022-06-13 07:20:51.504477
# Unit test for function from_yaml
def test_from_yaml():
    # simple test
    assert 'ok' == from_yaml('ok')
    # tests around 'yes' value and booleans
    assert True is from_yaml('true')
    assert False is from_yaml('false')
    assert True is from_yaml('yes')
    assert False is from_yaml('no')

# Generated at 2022-06-13 07:20:58.544095
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml("{\"foo\": \"bar\"}")
        assert True
    except Exception:
        assert False

    try:
        from_yaml("foo: \"bar\"")
        assert True
    except Exception:
        assert False

    try:
        from_yaml("{\"foo\": \"bar\"}", json_only=True)
    except AnsibleParserError:
        assert True
    except Exception:
        assert False


# Generated at 2022-06-13 07:21:09.760095
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    import ansible.parsing.yaml.objects
    import os
    import pytest

    vault_secrets = [u'vault_passwd_1', u'vault_passwd_2']
    file_name = os.path.join(os.path.dirname(__file__), './yaml_test1.yaml')

    with open(file_name, 'r') as f:
        data = f.read()
    data_dict = from_yaml(data, file_name, show_content=True, vault_secrets=vault_secrets)
    assert isinstance(data_dict, AnsibleMapping)

# Generated at 2022-06-13 07:21:17.415972
# Unit test for function from_yaml
def test_from_yaml():
    # Create some yaml files and see if we can load them as dictionaries
    import os
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import pytest

    # Test a good file
    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tf:
        tf.write('{}\n')
        tf.close()
        assert AnsibleBaseYAMLObject.from_yaml(filename=tf.name) == {}
    os.unlink(tf.name)

    # Test a bad file
    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tf:
        tf.write('{')
        tf.close()

# Generated at 2022-06-13 07:21:23.868642
# Unit test for function from_yaml
def test_from_yaml():
    str = '{"cat": {"ascii": "Cat", "html": "&lt;div&gt;Cat&lt;/div&gt;"}}'
    out = from_yaml(str)
    assert(out["cat"]["ascii"] == "Cat")
    assert(out["cat"]["html"] == "&lt;div&gt;Cat&lt;/div&gt;")

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:21:31.022903
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common._collections_compat import MutableMapping
    import ansible.parsing.yaml as yaml
    import ansible.parsing.json as json

    buf = "{'a': 'b', 'c': 'd'}"
    obj = from_yaml(buf)
    assert isinstance(obj, MutableMapping)
    assert obj == json.loads(buf)

    buf = "{a: 'b', c: 'd'}"
    obj = from_yaml(buf)
    assert isinstance(obj, MutableMapping)
    assert obj == json.loads(buf)

    buf = '{"a": "b", "c": "d"}'
    obj = from_yaml(buf)
    assert isinstance(obj, MutableMapping)
    assert obj

# Generated at 2022-06-13 07:21:42.348779
# Unit test for function from_yaml
def test_from_yaml():
    # test good yaml
    yaml_str = '---\nfoo: bar'
    assert from_yaml(yaml_str) == {u'foo': u'bar'}

    # test good json
    json_str = '{ "foo": "bar" }'
    assert from_yaml(json_str) == {u'foo': u'bar'}

    # test bad yaml
    yaml_str = '---\nfoo: :'

# Generated at 2022-06-13 07:21:49.363754
# Unit test for function from_yaml
def test_from_yaml():
    import yaml
    file_name = 'test'
    data = (
        'test_dict:\n'
        '  host: localhost\n')

    try:
        yaml.load(data)
    except Exception as yaml_exc:
        _handle_error(None, yaml_exc, file_name)

    new_data = from_yaml(data)
    assert new_data['test_dict']['host'] == 'localhost'

# Generated at 2022-06-13 07:21:53.115621
# Unit test for function from_yaml
def test_from_yaml():
    data = "---\n"
    file_name = 'file'
    show_content = True
    vault_secrets = None
    json_only = True
    new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
    assert new_data == None

# Generated at 2022-06-13 07:21:58.109133
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo') == 'foo'
    assert from_yaml(
        "{ 'foo': 'bar' }"
    ) == {'foo': 'bar'}
    assert from_yaml(
        "{ 'foo': 'bar' }", json_only=True
    ) == {'foo': 'bar'}
    assert from_yaml(
        '''
        ---
        foo: bar
        '''
    ) == {'foo': 'bar'}


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:04.817642
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"foo\": \"bar\"}", json_only=True) == {"foo": "bar"}
    assert from_yaml("[1,2,3]", json_only=True) == [1, 2, 3]
    assert from_yaml("{\"foo\": \"bar\"}") == {"foo": "bar"}
    assert from_yaml("[1,2,3]") == [1, 2, 3]

# Generated at 2022-06-13 07:22:12.797123
# Unit test for function from_yaml
def test_from_yaml():
    null = None
    assert from_yaml('') == null
    assert from_yaml(None) == null
    assert from_yaml('{}') == {}
    assert from_yaml('{ "foo": "bar" }') == {'foo': 'bar'}
    assert from_yaml('{ foo: bar }') == {'foo': 'bar'}
    assert from_yaml('{ "foo": [ "bar"] }') == {'foo': ['bar']}
    assert from_yaml('{ "foo": [ "bar", "baz"] }') == {'foo': ['bar', 'baz']}
    assert from_yaml('{ "foo": [] }') == {'foo': []}
    assert from_yaml('{ "foo": [], }') == {'foo': []}
   

# Generated at 2022-06-13 07:22:16.525152
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml("---\ntest"), dict)
    assert isinstance(from_yaml("--- 1\n"), int)

# Generated at 2022-06-13 07:22:25.176950
# Unit test for function from_yaml
def test_from_yaml():
    j = '{"pets": ["cats", "dogs"]}'
    y = '''
---
pets:
  - cats
  - dogs
    '''
    assert from_yaml(j) == { 'pets': [ 'cats', 'dogs' ] }
    assert from_yaml(y) == { 'pets': [ 'cats', 'dogs' ] }

    with pytest.raises(AnsibleParserError):
        from_yaml('nope')

    # This was a bug
    assert from_yaml("[] and []") == [ [] ]

# Generated at 2022-06-13 07:22:27.906194
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import from_yaml
    data = b"{'a':1, 'b':2}"
    new_data = from_yaml(data)
    assert new_data['a'] == 1

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:39.807670
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    test_data = {'name': 'bob', 'age': 5, 'skills': ['foo', 'bar', 'baz'], 'place': {'city': 'XYZ', 'country': 'TD'}}
    ansible_obj = AnsibleBaseYAMLObject()
    ansible_obj.ansible_pos = ('test_file.yml', 3, 2)
    try:
        from_yaml('')
    except AnsibleParserError as e:
        print(e.message)
        print('+++ ' + str(e.obj))

# Generated at 2022-06-13 07:22:48.340495
# Unit test for function from_yaml
def test_from_yaml():
    print("test_from_yaml")
    result = {"mode": "push",
              "name": "test_webhook",
              "push_events": True,
              "url": "http://test.com/webhook"}
    assert result == from_yaml('{"mode":"push","name":"test_webhook","push_events":true,"url":"http://test.com/webhook"}')

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:22:59.730536
# Unit test for function from_yaml
def test_from_yaml():
    test_data = {
        'fruits': ['apple', 'banana', 'pear'],
        'vegetables': ['carrot', 'potato'],
        'fish': ['sardine'],
        'empty': [],
        'str': 'Hello World',
        'int': 1234,
        'float': 123.4,
        'bool': True,
        'none': None,
        'dict': {'key': 'value'},
    }

    # test_data can be represented as JSON or YAML
    json_text = json.dumps(test_data)
    yaml_text = from_yaml(json_text)
    assert test_data == yaml_text

    # But we need to use from_yaml to parse YAML

# Generated at 2022-06-13 07:23:07.522786
# Unit test for function from_yaml
def test_from_yaml():
    yaml_snippet = '''
-  name: create database user
   mysql_user:
      name: acd
      password: "{{ mysql_root_password }}"
      priv: '{{ item.name }}.*:ALL'
      state: present
     with_items: "{{ mysql_databases }}"
     '''

    data = from_yaml(yaml_snippet)
    assert isinstance(data, list), "Failed to parse YAML snippet: list expected"
    assert data[0].get('name') == 'create database user', "Failed to parse YAML snippet: data[0]['name'] should be 'create database user'"

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:23:15.717382
# Unit test for function from_yaml
def test_from_yaml():
    """
    Run tests for from_yaml function

    Arguments:
        None

    Returns:
        None
    """

    from ansible.parsing.vault import VaultLib


    vault = VaultLib([])
    string_vars = ["'''Hello '''''World'''",
                   "'''Hello'' World'''",
                   "'''Hello '' World'''"]

    for string in string_vars:
        yaml_string = from_yaml(string, vault_secrets=vault.secrets)
        assert yaml_string == "Hello 'World"

    string_vars = ["'''Hello '''''World'",
                   "'''Hello'' World'",
                   "'''Hello '' World'"]


# Generated at 2022-06-13 07:23:25.998091
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.collections import ImmutableList
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    def _assert_equal_data_structures(one, two):
        assert type(one) == type(two)
        if isinstance(one, (dict, AnsibleMapping)):
            assert one.keys() == two.keys()
            for key in one:
                _assert_equal_data_structures(one[key], two[key])
        elif isinstance(one, (list, tuple, AnsibleSequence)):
            assert len(one) == len(two)
            for one_item, two_item in zip(one, two):
                _assert_

# Generated at 2022-06-13 07:23:30.255420
# Unit test for function from_yaml
def test_from_yaml():
    data = """---
a: 1
b:
  - 2
  - 3
"""
    expected = {'a': 1, 'b': [2, 3]}
    actual = from_yaml(data)
    assert expected == actual
    data = "{'a': 1, 'b': [2, 3]}"
    expected = {u'a': 1, u'b': [2, 3]}
    actual = from_yaml(data)
    assert expected == actual

# Generated at 2022-06-13 07:23:44.834551
# Unit test for function from_yaml
def test_from_yaml():
    # NOTE: To run this test, you will need a pyyaml package installed in your
    # virtualenv.

    # Try the simplest case.
    data = "One: 1\nTwo: 2"
    obj = from_yaml(data)
    assert obj == dict(One=1, Two=2)

    # Try a more complex case that also includes JSON.
    data = "{\"One\": 1, \"Two\": 2}\n\nOne: 1\nTwo: 2"
    obj = from_yaml(data)
    assert obj == dict(One=1, Two=2)

    # Try a case where we have a syntax error.
    data = "{\"One\" 1, \"Two\": 2}\n\nOne: 1\nTwo: 2"

# Generated at 2022-06-13 07:23:56.067768
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    # string empty
    data = ''
    new_data = from_yaml(data)
    assert new_data == AnsibleLoader(stream=data, file_name='<string>').get_single_data()
    # string not empty
    data = 'test'
    new_data = from_yaml(data)
    assert new_data == AnsibleLoader(stream=data, file_name='<string>').get_single_data()
    # unknown type
    data = object()
    try:
        from_yaml(data)
        assert False
    except Exception as e:
        assert True
    # list
    data = []

# Generated at 2022-06-13 07:24:06.231067
# Unit test for function from_yaml

# Generated at 2022-06-13 07:24:11.729350
# Unit test for function from_yaml
def test_from_yaml():
    fake_vaults = { "foo" : "bar" }
    data = """
    {
        "foo": "bar",
        "baz": {
            "lorem": "ipsum"
        }
    }
    """
    ret = from_yaml(data, vault_secrets=fake_vaults)
    assert isinstance(ret, dict)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:19.157633
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("foo: bar") == {"foo": "bar"}
    assert from_yaml(u"foo: bar") == {"foo": "bar"}
    assert from_yaml(b"foo: bar") == {"foo": "bar"}

    try:
        from_yaml("foo bar")
    except AnsibleParserError:
        pass
    else:
        assert False, "Should raise AnsibleParserError"

# Generated at 2022-06-13 07:24:26.433794
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys

    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_dir = os.path.join(script_dir, "yaml")

    # Error and exit if any exceptions encountered
    sys.exit(__name__)

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:24:35.791194
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
        ---
        a_string: this is a string 
        another_string: "a quoted string"
        true_value: yes
        false_value: no
        int_value: 42
        float_value: 3.14159
        list_value:
            - item1
            - item2
            - item3
        dict_value:
            key1: value1
            key2: value2
            key3: value3
        '''

    test_data = from_yaml(data, file_name='test.yml', show_content=True)

    assert(test_data['a_string'] == 'this is a string')
    assert(test_data['another_string'] == 'a quoted string')
    assert(test_data['true_value'] == True)

# Generated at 2022-06-13 07:24:42.232135
# Unit test for function from_yaml
def test_from_yaml():
    print('Testing from_yaml')
    try:
        data = from_yaml('{ "mydict": { "mykey": 42, "mykey2": 43 } }')
        assert data['mydict']['mykey'] == 42
    except Exception as e:
        print('from_yaml test failed: %s' % e)
        raise e

    print('from_yaml test success.')

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:24:51.183692
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    data = {
        'a': "foo",
        'b': [1, 2, 3],
        'c': {
            'k': "v"
        },
        'd': True,
        'e': False,
        'f': None,
    }

    # We use the legacy yaml loader and dumper because the default
    # yaml dumper only works in python >= 3.7 and the default loader
    # only works in python >= 3.6, making it difficult to test it in
    # older python versions.
    assert from_yaml(yaml.dump(data, Dumper=AnsibleDumper, default_flow_style=False)) == data

# Generated at 2022-06-13 07:25:01.686523
# Unit test for function from_yaml
def test_from_yaml():
    """
    This is not a real unit test, but a simple test of the from_yaml() function.
    """
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    import os
    import tempfile

    # setup
    test_dir = os.path.dirname(os.path.dirname(__file__))
    test_env = os.environ.copy()
    test_env['ANSIBLE_CONFIG'] = os.path.join(test_dir, 'ansible.cfg')
    test_loader = DataLoader()
    test_vars = VariableManager()

    # test the function
    yaml_string = 'string: this is a test'

# Generated at 2022-06-13 07:25:10.404006
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    def check_safe_load(data, expected_result, expected_vault_secrets=None, filename='<string>'):
        assert from_yaml(data, filename) == expected_result
        assert from_yaml(data + "\n", filename) == expected_result
        assert from_yaml("---\n" + data, filename) == expected_result
        assert from_yaml("---\n" + data + "\n", filename) == expected_result

        # see https://github.com/ansible/ansible/issues/9480
        # ansible-vault 2.2.x cannot decrypt this but 2.3.x can
        assert from_yaml

# Generated at 2022-06-13 07:25:10.981465
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:25:15.368871
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestFromYaml(unittest.TestCase):
        def test_multiple_docs(self):
            yaml_strng = '---\nfoo: bar\n---\nfoo: bar'
            yaml_object = from_yaml(yaml_strng)
            assert yaml_object is None

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-13 07:25:16.942282
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo: bar') == {'foo': 'bar'}


# Generated at 2022-06-13 07:25:30.613198
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    - include_vars:
        file: foo.yml
    '''
    actual = from_yaml(data)
    expected = [
        {'include_vars': {'file': 'foo.yml'}}
    ]
    assert actual == expected

    data = "{'foo': 42}"
    actual = from_yaml(data)
    expected = {'foo': 42}
    assert actual == expected

    data = "{'foo': 'bar'}"
    actual = from_yaml(data)
    expected = {'foo': 'bar'}
    assert actual == expected

    data = "{'foo': {'bar': {'baz': 'blur'}}}"
    actual = from_yaml(data)

# Generated at 2022-06-13 07:25:37.457817
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import re
    import random

    # Create a random dict and write it out as a yaml string
    test_dict = {}
    for _ in range(0,random.randint(1,1000)):
        test_dict[str(random.randint(0,10000))] = random.random()
    plain_yaml_str = AnsibleDumper().dump(test_dict, default_flow_style=False)
    assert str(type(plain_yaml_str)) == "<class 'str'>"

    # Ensure that the string we created can be loaded as yaml
    plain_yaml_obj = from_yaml(plain_yaml_str)
    assert dict(plain_yaml_obj) == test_dict

    # Now, scrub

# Generated at 2022-06-13 07:25:42.873073
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test module for function from_yaml.
    '''

    result = from_yaml('[1,2,3]', '<string>', False, None, True)

    if result is None:
        return True
    else:
        return False


# Generated at 2022-06-13 07:25:56.150139
# Unit test for function from_yaml
def test_from_yaml():
    # test with a string
    assert from_yaml('some string') == 'some string'

    # test a list
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

    # test a dict
    assert from_yaml('{"a": "b", "c": "d"}') == {'a': 'b', 'c': 'd'}

    # test a nested datastructure
    assert from_yaml('{"a": ["b", "c", {"d": "e"}]}') == {'a': ['b', 'c', {'d': 'e'}]}

    # test with yaml (note: unicode characters are valid yaml)

# Generated at 2022-06-13 07:26:01.769381
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    {
        "foo": "bar",
        "bam": [1, 2, 3],
        "baz": {
            "quux": 1,
            "spam": "eggs"
        }
    }
    '''
    assert from_yaml(data) == json.loads(data)

# Generated at 2022-06-13 07:26:14.016650
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""
---
- hosts: all
  gather_facts: no
""") == [{'hosts': 'all', 'gather_facts': 'no'}]

    assert from_yaml("""
- hosts: all
  gather_facts: no
""") == [{'hosts': 'all', 'gather_facts': 'no'}]

    assert from_yaml("""
- name: "{{thing}}"
""") == [{'name': '{{thing}}'}]

    assert from_yaml("""
---
- name: "{{thing}}"
""") == [{'name': '{{thing}}'}]

    assert from_yaml("""
not_yaml
""") is None


# Generated at 2022-06-13 07:26:24.947632
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAES256

    dec_data = None
    vault = VaultAES256()
    password = "mysecrete"
    vault.load_decryption_key(password)
    vault.load_password(password)
    secret = VaultSecret('$ANSIBLE_VAULT;1.1;AES256\n'
                         '3063313161313837343833383163393262643163356231636536306433623966316535633064\n'
                         '375a7a656430636164613437616666323137373262383266693131633d0a')
    data = vault.decrypt(secret)

    assert data == 'mypass'

# Generated at 2022-06-13 07:26:33.380331
# Unit test for function from_yaml
def test_from_yaml():
    from .basic import test_data

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Encrypted unicode object

# Generated at 2022-06-13 07:26:44.379120
# Unit test for function from_yaml
def test_from_yaml():
    import json
    import yaml


# Generated at 2022-06-13 07:26:51.768145
# Unit test for function from_yaml
def test_from_yaml():
    # Test a valid Json string
    str1 = '{"name": "foo", "state": "present"}'
    assert json.loads(str1) == from_yaml(str1)

    # Test a valid Yaml string
    str2 = '''
    foo:
        state: present
        name: foo
    '''
    assert {'foo': {'state': 'present', 'name': 'foo'}} == from_yaml(str2)

    # Test a valid Json string with stringified Json
    str3 = '{"name": "bar", "state": "present", "extra": "{\\"fizz\\": {\\"buzz\\": true}}"}'
    assert json.loads(str3) == from_yaml(str3)

    # Test a valid Json string with stringified Json inside Yaml

# Generated at 2022-06-13 07:27:04.579532
# Unit test for function from_yaml
def test_from_yaml():
    # Testing with a correctly encoded JSON file
    json_file = '''{"key1": "value1", "key2": ["value2", "value3"]}'''
    json_file_output = {"key1": "value1", "key2": ["value2", "value3"]}

    assert json_file_output == from_yaml(json_file, json_only=True)

    # Testing with a correctly encoded JSON file with a string containing '{}'
    json_file_containing_brackets = '''{"key1": "value1 { with_brackets }", "key2": ["value2", "value3"]}'''
    json_file_containing_brackets_output = {"key1": "value1 { with_brackets }", "key2": ["value2", "value3"]}

    assert json_file

# Generated at 2022-06-13 07:27:05.858035
# Unit test for function from_yaml
def test_from_yaml():
    '''
    How to test json vs yaml conversion?
    '''
    pass

# Generated at 2022-06-13 07:27:18.928382
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.vault import VaultLib

    secrets = {'vault_password_file': 'passwordfile', 'vault_ids': []}
    vault_secret = VaultLib(secrets)

    data = from_yaml("{'hello': 'world'}")
    assert isinstance(data, dict), 'Non dict value returned'
    assert data['hello'] == 'world', 'Non matching value returned'

    data = from_yaml("- name: test")
    assert isinstance(data, list), 'Non list value returned'
    assert data[0]['name'] == 'test', 'Non matching value returned'


# Generated at 2022-06-13 07:27:24.218461
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.dataloader
    data = "foo: 1"
    new_data = ansible.parsing.dataloader.from_yaml(data)
    assert isinstance(new_data, dict)
    assert len(new_data) == 1
    assert isinstance(new_data['foo'], int)
    assert new_data['foo'] == 1


# Generated at 2022-06-13 07:27:29.111541
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('') == None
    assert from_yaml('{}') == {}
    assert from_yaml('{"a": 1}') == {"a": 1}
    assert from_yaml('{a: 1}') == {"a": 1}

# Generated at 2022-06-13 07:27:39.181725
# Unit test for function from_yaml
def test_from_yaml():
    from tempfile import NamedTemporaryFile
    from ansible.parsing.vault import VaultLib

    tmp_file = NamedTemporaryFile()
    tmp_file.write("""
       {
          "some": ["list", "of", "strings"],
          "a": "simple string",
          "nested": {
            "hash": "dictionary",
            "with": "more stuff"
          }
       }
    """)
    tmp_file.seek(0)

    with open(tmp_file.name, 'r') as f:
        data = f.read()
        json_data = from_yaml(data, 'JSON file', show_content=True, json_only=True)
        yaml_data = from_yaml(data, 'YAML file', show_content=True)

    assert json