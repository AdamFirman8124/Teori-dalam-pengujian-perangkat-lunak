

# Generated at 2022-06-13 07:17:37.137250
# Unit test for function from_yaml

# Generated at 2022-06-13 07:17:46.738834
# Unit test for function from_yaml
def test_from_yaml():

    #Example data
    json_string = '[{"name":"test1", "test": {"name": "test2"}},{"test": "test1"}]'
    json_string2 = '[{"test": "test1"},{"test": "test2"}]'
    json_string3 = '[{"test": "test1",}]'
    yaml_string = 'name: test1\ntest: {name: test2}\n- test: test1\n- test: test2\n- test: test3'
    yaml_string2= 'name: test1\ntest: test2\n- test: test1\n- test: test2\n- test: test3'
    yaml_string3 = '''name: test1
    test:
      - name: test2
        test: test3'''

# Generated at 2022-06-13 07:17:57.351244
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper

    test_data = dict(one=1, two=2)
    test_data_yaml = b'---\none: 1\ntwo: 2\n'

    test_data_json = b'{ "one": 1, "two": 2 }'

    # Test loading from YAML
    result_data_load = from_yaml(test_data_yaml)
    assert result_data_load == test_data

    # Test loading from JSON
    result_data_load = from_yaml(test_data_json)
    assert result_data_load == test_data

    # Test dumping to YAML
    result_data_dump = AnsibleDumper(sort_keys=True).dump(test_data)
    assert result_

# Generated at 2022-06-13 07:18:06.406691
# Unit test for function from_yaml

# Generated at 2022-06-13 07:18:14.755756
# Unit test for function from_yaml
def test_from_yaml():
    one = {'one': 1}
    one_json = json.dumps(one)
    one_yaml = 'one: 1'

    # json
    assert from_yaml(one_json) == one
    assert from_yaml(one_json) == one
    assert from_yaml(one_json) == one
    assert from_yaml(one_json) == one

    # yaml
    assert from_yaml(one_yaml) == one
    assert from_yaml(one_yaml) == one
    assert from_yaml(one_yaml) == one
    assert from_yaml(one_yaml) == one

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:18:24.474321
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    vl = VaultLib([])
    vault_secret = vl.secrets.get('vault_password_1', VaultSecret('vault_password_1', 'vault_password_1'))

    data = {'foo': 'bar', 'list': ['one', 'two', 'three']}
    json_data = json.dumps(data)

# Generated at 2022-06-13 07:18:33.793336
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"test": "pass"}') == {'test': 'pass'}
    assert from_yaml('test: pass') == {'test': 'pass'}
    assert from_yaml('test: pass', json_only=True) == 'test: pass'
    assert from_yaml(['test', 'pass']) == {'test': 'pass'}
    assert from_yaml('[test, pass]') == {'test': 'pass'}
    assert from_yaml('{"test": "pass",}') == {'test': 'pass'}
    assert from_yaml('test: pass,', json_only=True) == 'test: pass,'
    assert from_yaml('test: pass,', json_only=False) == {'test': 'pass'}
    assert from_y

# Generated at 2022-06-13 07:18:40.142815
# Unit test for function from_yaml
def test_from_yaml():

    def test_input(yaml_data, expected_output):
        actual_output = from_yaml(yaml_data)
        assert actual_output == expected_output

    test_input("{test:test}", {u'test': u'test'})
    test_input("[test,test]", [u'test', u'test'])
    test_input("test", u'test')
    test_input("- test\n- test2", [u'test', u'test2'])

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:41.438333
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('not a real yaml file') == None


# Generated at 2022-06-13 07:18:45.628805
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{ "name" : "ctb902" }'))

# Generated at 2022-06-13 07:18:58.075593
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('test') == 'test'
    assert from_yaml(1) == 1
    assert from_yaml(["test", "test2"]) == ["test", "test2"]
    assert from_yaml({'test': 'test'}) == {'test': 'test'}
    assert from_yaml(1, file_name="test") == 1
    assert from_yaml(["test", "test2"], file_name="test") == ["test", "test2"]
    assert from_yaml({'test': 'test'}, file_name="test") == {'test': 'test'}
    assert from_yaml(1, show_content=False) == 1
    assert from_yaml(["test", "test2"], show_content=False) == ["test", "test2"]
   

# Generated at 2022-06-13 07:19:07.249436
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.ajson import AnsibleJSONEncoder

    assert from_yaml("true") == True
    assert from_yaml("false") == False
    assert from_yaml("foobar") == u'foobar'
    assert from_yaml("3.14159") == 3.14159
    assert from_yaml("null") == None
    assert from_yaml("[1, 2, 3, 4]") == [1, 2, 3, 4]
    assert from_yaml("{ 'foo': 'bar' }") == {u'foo': u'bar'}

# Generated at 2022-06-13 07:19:11.973271
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{}') == {}

    with pytest.raises(AnsibleParserError):
        from_yaml('{a')

    assert from_yaml('{a:', json_only=True) == {'a': None}

# Generated at 2022-06-13 07:19:16.546008
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "test" : "test_json" }') == {'test': 'test_json'}

    assert from_yaml('test: test_yaml', json_only=True) is None  # Invalid JSON

# Generated at 2022-06-13 07:19:24.554531
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml.__globals__['from_yaml'] = from_yaml  # for recursive calls
    assert from_yaml(u'{ "rubbish": 1 }') == {u'rubbish': 1}
    assert from_yaml(u'["rubbish", 1]') == [u'rubbish', 1]
    assert from_yaml(u'{"a": ["b", "c"]}') == {u'a': [u'b', u'c']}
    assert from_yaml(u'{"a": {"c": "d"}}') == {u'a': {u'c': u'd'}}
    assert from_yaml(u'{"a": "b"}') == {u'a': u'b'}

# Generated at 2022-06-13 07:19:32.436682
# Unit test for function from_yaml
def test_from_yaml():
    # Load a yaml file
    data = from_yaml(open('/testPath').read())

    # Load a json file
    data2 = from_yaml(open('/testPath').read())

    # Load a non yaml or json file
    try:
        data3 = from_yaml(open('/testPath').read())
    except:
        pass

    # Load a json file with only json option
    data4 = from_yaml(open('/testPath').read(), json_only=True)

    # Load a non json file with only json option
    try:
        data5 = from_yaml(open('/testPath').read(), json_only=True)
    except:
        pass

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:35.886642
# Unit test for function from_yaml
def test_from_yaml():
    yaml_test = '''---
a: 1
b:
  c: 3
  d: 4
'''
    print(from_yaml(yaml_test))

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:44.393138
# Unit test for function from_yaml
def test_from_yaml():
    print('============From YAML test============')
    from ansible.parsing.yaml.loader import AnsibleLoader
    ansible_loader = AnsibleLoader(b'foo (bar):', file_name='<string>')
    print(ansible_loader.check_data())
    ansible_loader.get_chunk()
    ansible_loader.dispose()
    print(ansible_loader.get_single_data())
if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:49.415570
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("foo", show_content=False).get('foo') == 'bar'
    assert from_yaml("{\"foo\": \"bar\"}", show_content=False).get('foo') == 'bar'
    assert from_yaml("{\"foo\":\"bar\"}", show_content=False, json_only=True).get('foo') == 'bar'

# Generated at 2022-06-13 07:19:59.888220
# Unit test for function from_yaml
def test_from_yaml():

    # Test if JSON input correctly is correctly detected
    json_str = '{"some_key": "some_value"}'
    json_ans = {'some_key': 'some_value'}
    assert from_yaml(json_str) == json_ans
    assert not isinstance(from_yaml(json_str), AnsibleBaseYAMLObject)

    # Test if YAML input correctly is correctly detected
    yaml_str = '---\nsome_key: some_value\n'
    yaml_ans = {'some_key': 'some_value'}
    assert from_yaml(yaml_str) == yaml_ans
    assert not isinstance(from_yaml(yaml_str), AnsibleBaseYAMLObject)

if __name__ == "__main__":
    import doctest

# Generated at 2022-06-13 07:20:15.292497
# Unit test for function from_yaml
def test_from_yaml():
    """Test the _from_yaml function"""

    def _assert_failed_load(data, json_only=False):
        """Helper function to test _from_yaml with a given input string."""

        try:
            from_yaml(data, json_only=json_only)
            assert False, '_from_yaml did not throw an exception'
        except AnsibleParserError as e:
            # verification is the fact that we got here, with an exception
            pass
        except Exception as e:
            assert False, '_from_yaml did not throw AnsibleParserError'

    # test various strings we know will fail to load
    _assert_failed_load('[]')  # empty list
    _assert_failed_load('{"ntp": "ntp.example.com"}')  # JSON hash with string
    _assert

# Generated at 2022-06-13 07:20:25.423087
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.play_context import PlayContext

    test_block = '''
    ---
        hosts: all
        gather_facts: True
        vars:
            a:
                b:
                    c: "{{lookup('env', 'HOME')}}"
        tasks:
            - name: "Test Task"
              debug:
                  msg: "{{a['b']['c']}}"
    '''
    data = from_yaml(test_block)
    assert data['hosts'] == 'all'
    assert data['vars']['a']['b']['c'] == "{{lookup('env', 'HOME')}}"

    # test serialization
    to_yaml = ''
    to_

# Generated at 2022-06-13 07:20:36.572994
# Unit test for function from_yaml
def test_from_yaml():
    # Test all try cases
    import pytest

    with pytest.raises(AnsibleParserError):
        from_yaml(data='{}', show_content=False, file_name='defaults/main.yml')

    with pytest.raises(AnsibleParserError):
        from_yaml(data='{}', show_content=True, file_name='test.yml')

    with pytest.raises(AnsibleParserError):
        from_yaml(data='{', show_content=True, file_name='test.yml')

    with pytest.raises(AnsibleParserError):
        from_yaml(data='{}', show_content=True, file_name='test.yml', json_only=True)

    # Useful to test safe_load

# Generated at 2022-06-13 07:20:47.239915
# Unit test for function from_yaml
def test_from_yaml():
    test_data_json_string = '''{
  "a": "b"
}'''
    test_data = json.loads(test_data_json_string)
    assert test_data == from_yaml(test_data_json_string)
    test_data_json_string = '''{
  "a": "b",
  "c": "d"
}'''
    test_data = json.loads(test_data_json_string)
    assert test_data == from_yaml(test_data_json_string)
    test_data_json_string = '''{
  "a": "b",
  "c": "d",
  "e": "f"
}'''
    test_data = json.loads(test_data_json_string)

# Generated at 2022-06-13 07:20:57.350199
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "not": "a real file" }') == {'not': 'a real file'}
    try:
        from_yaml('file not found!')
        assert False, "YAML file not found should have raised an exception"
    except AnsibleParserError:
        assert True
    try:
        from_yaml('---\n{ bad yaml \n')
        assert False, "Invalid YAML should have raised an exception"
    except AnsibleParserError:
        assert True
    try:
        from_yaml('---\n[ "list", "of", "strings" ]\n')
        assert False, "YAML list should have raised an exception"
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 07:21:09.167801
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('1234') == 1234
    assert from_yaml('---\n- 1\n- 2\n- 3') == [1, 2, 3]
    assert from_yaml('{"a": 1}') == {"a": 1}
    assert from_yaml('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    assert from_yaml('{a: b}') == {"a": "b"}
    assert from_yaml('a: b\n') == {"a": "b"}
    assert from_yaml('-\n - foo\n - bar') == [["foo", "bar"]]
    assert from_yaml('foo: {bar: baz}') == {"foo": {"bar": "baz"}}

# Generated at 2022-06-13 07:21:17.093137
# Unit test for function from_yaml
def test_from_yaml():
    print("Testing from_yaml")
    data = """
    - name: this is a task
      action: command echo hello world
    - name: this is another task
      action: command echo hello world
    """
    parsed_data = from_yaml(data)
    assert parsed_data[0]['name'] == 'this is a task'
    assert parsed_data[0]['action']['command'] == 'echo hello world'
    assert parsed_data[1]['name'] == 'this is another task'
    assert parsed_data[1]['action']['command'] == 'echo hello world'


# Generated at 2022-06-13 07:21:24.838684
# Unit test for function from_yaml
def test_from_yaml():
    valid_yaml = """
    - name: some_module
      action: some_action
    """
    valid_json = valid_yaml.replace('- ', '{ "name": "some_module", "action": "some_action" }')

    assert from_yaml(valid_yaml) == [{'action': u'some_action', 'name': u'some_module'}]
    assert from_yaml(valid_json) == [{u'action': u'some_action', u'name': u'some_module'}]



# Generated at 2022-06-13 07:21:30.622241
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from test.units.parsing.utils import _to_yaml
    from ansible.module_utils.common.collections import AnsibleMapping, AnsibleSequence
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import is_encrypted_data
    from ansible.parsing.vault import is_encrypted_file
    from ansible.parsing.dataloader import DataLoader
    vault_secret = VaultSecret()
    vault = Vault

# Generated at 2022-06-13 07:21:40.129567
# Unit test for function from_yaml
def test_from_yaml():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # test a standard string
    data = '{ "one": "two" }'
    new_data = from_yaml(data)
    assert(type(new_data) == dict)
    assert(type(new_data.get('one')) == str)
    assert(new_data.get('one') == 'two')

    # test a unicode string
    data = u'{ "one": "two" }'
    new_data = from_yaml(data)
    assert(type(new_data) == dict)
    assert(type(new_data.get('one')) == str)

# Generated at 2022-06-13 07:21:54.000423
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import stat
    import tempfile
    from ansible.parsing.yaml.loader import AnsibleLoader

    tmp_dir = tempfile.gettempdir()
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_filename = tmp_file.name
    tmp_file.close()

    data_to_dump = {
        "key": {
            "subkey": [1, 2, 3, 4, 5]
        }
    }

    # Load data to the file
    with open(tmp_filename, 'w') as tmp_file:
        yaml.dump(data_to_dump, tmp_file)

    # Change permissions
    os.chmod(tmp_filename, stat.S_IWRITE)

    data = from_yaml(tmp_filename)


# Generated at 2022-06-13 07:22:04.949776
# Unit test for function from_yaml
def test_from_yaml():
    (b, v) = from_yaml("---\nfoo: bar\n")
    assert b == {'foo': 'bar'}
    assert v == {'ANSIBLE_VAULT': 'AES256', 'ANSIBLE_VAULT_IDENTITY': '4f4eaeb5-5b5c-4421-a2a4-f4748b05fa9f'}


# Generated at 2022-06-13 07:22:12.846450
# Unit test for function from_yaml
def test_from_yaml():
    # These are some tests to ensure bug #22129 doesn't regress:
    # https://github.com/ansible/ansible/issues/22129
    assert from_yaml('{}') == {}
    assert from_yaml('[]') == []
    assert from_yaml('["a","b","c"]') == ["a","b","c"]
    assert from_yaml('["a", "b", "c"]') == ["a","b","c"]
    assert from_yaml('["a",  "b",  "c"]') == ["a","b","c"]
    assert from_yaml('A') == 'A'
    assert from_yaml('"A"') == 'A'
    assert from_yaml('A"') is None
    assert from_yaml('"A') is None
    assert from_

# Generated at 2022-06-13 07:22:25.665673
# Unit test for function from_yaml
def test_from_yaml():
    import collections

    d = dict(a=1,b=2,c=3,d=4,e=5,f=6)

# Generated at 2022-06-13 07:22:40.055313
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"foo": "bar"}'
    assert from_yaml(data) == {"foo": "bar"}

    data = '{"foo": "bar" "baz": "qux"}'
    try:
        assert from_yaml(data)
    except AnsibleParserError:
        pass

    data = "{'foo': 'bar'}"
    assert from_yaml(data) == {'foo': 'bar'}

    data = "{'unquoted_string': foo}"
    assert from_yaml(data) == {'unquoted_string': 'foo'}

    data = '''{
        "unquoted_key_string": "value1",
        "dictionary": {
            "key1": "val1",
            "key2": "val2"
        }
    }'''


# Generated at 2022-06-13 07:22:50.400877
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils import basic

    def _test(data, expected, file_name='<string>', show_content=True, vault_secrets=None, json_only=False):
        results = from_yaml(data, file_name, show_content, vault_secrets, json_only)
        basic._assertEqual(results, expected)

    _test('  hello: world', {'hello': 'world'})
    _test('{ hello: world }', {'hello': 'world'})
    _test('{  hello: world }', {'hello': 'world'})
    _test('{  hello:   world }', {'hello': 'world'})
    _test('{  hello:   world }', {'hello': 'world'})

# Generated at 2022-06-13 07:22:55.187766
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    res = from_yaml("""
        foo:
          bar: 1
          qux: True
    """)
    assert res == {'foo': {'bar': 1, 'qux': True}}

# Generated at 2022-06-13 07:23:05.341010
# Unit test for function from_yaml
def test_from_yaml():
    module_name = 'ansible.compat.tests.test_from_yaml'
    import pytest
    import platform
    import sys
    if sys.version_info[:2] == (2, 6):
        pytest.skip("Skip this test on Python2.6 because of python-yaml/ansible/issue/22102")

    if platform.python_implementation() == 'PyPy':
        pytest.skip("Skipped on pypy because it is too slow")

    test_data = [
        ('''---
foo: [ a, b, c, d ]
''', {'foo': ['a', 'b', 'c', 'd']}),
    ]
    for data, expected_results in test_data:
        assert expected_results == from_yaml(data, module_name)

    #

# Generated at 2022-06-13 07:23:13.955274
# Unit test for function from_yaml
def test_from_yaml():
    import unittest


# Generated at 2022-06-13 07:23:17.525364
# Unit test for function from_yaml
def test_from_yaml():
    # setup
    input = """
---
a:
    b: 1
    c:
        - true
        - false
"""
    expected = {"a": {"b": 1, "c": [True, False]}}
    # run tests
    assert from_yaml(input) == expected
    assert from_yaml(json.dumps(expected)) == expected

# Generated at 2022-06-13 07:23:30.142928
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'a':10, 'b':20}"
    ds = from_yaml(data)
    assert ds == {"a":10, "b":20}

    data = "['a',10, 'b', 20]"
    ds = from_yaml(data)
    assert ds == ['a',10, 'b', 20]

    data = "[{'a':10, 'b':20}, {'a':11, 'b':21}]"
    ds = from_yaml(data)
    assert ds == [{'a':10, 'b':20}, {'a':11, 'b':21}]

    data = "['a',10, ['b', 20], 'c', 30]"
    ds = from_yaml(data)

# Generated at 2022-06-13 07:23:37.881330
# Unit test for function from_yaml
def test_from_yaml():
    sample = """{"msg": "Good job!"}"""
    assert from_yaml(sample) == json.loads(sample)

    # Make sure yaml strings that are valid json throw an error
    sample = """{{ 'msg': 'Bad job!' }}"""
    try:
        from_yaml(sample)
        assert not True
    except AnsibleParserError:
        assert True



# Generated at 2022-06-13 07:23:42.408271
# Unit test for function from_yaml
def test_from_yaml():
    with open("test.yml","rb") as f:
        yaml_file = f.read()
        data = from_yaml(yaml_file)
        print("data:", data)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:23:49.784545
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.module_utils.six import string_types
    data = {
        'foo': 'bar',
        'baz': 2,
        'l': {},
        'v': [1, 2, 3],
        'b': True,
        'n': None,
        's': "foo\n  bar",
    }
    new_data = from_yaml(AnsibleDumper(Dumper=AnsibleDumper).dump(data))
    # Make sure the types are the same
    assert type(new_data) == type(data)
    assert type

# Generated at 2022-06-13 07:24:00.805913
# Unit test for function from_yaml
def test_from_yaml():
    """
    Test YAML parsing.
    """
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText, AnsibleSequence, AnsibleMapping
    from ansible.parsing.vault import VaultLib, VaultSecret
    import os

    # Create a Vault secret for testing
    vault_file = os.path.join(os.path.dirname(__file__), 'vault_password.txt')
    vault_password = open(vault_file).read().rstrip('\n')
    vault = VaultLib([VaultSecret(vault_password)])

    # parse yaml

# Generated at 2022-06-13 07:24:09.652149
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[1,2,3]') == [1, 2, 3]
    assert from_yaml('["eggs","spam"]') == ["eggs", "spam"]
    assert from_yaml('{"key":"value"}') == {"key": "value"}
    assert from_yaml('---') == None
    assert from_yaml('---\n') == None
    assert from_yaml('---', json_only=True) == None
    assert from_yaml('---\n', json_only=True) == None
    assert from_yaml('["eggs","spam"]', json_only=True) == ["eggs", "spam"]
    assert from_yaml('{"key":"value"}', json_only=True) == {"key": "value"}

# Generated at 2022-06-13 07:24:19.764391
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = "1"
    result = from_yaml(data)
    # assert isinstance(result, int)
    assert result == 1

    data = '{ "test": 1 }'
    result = from_yaml(data)
    assert isinstance(result, dict)
    assert result['test'] == 1

    data = '{ "test": 1'
    loader = AnsibleLoader(data)
    try:
        result = loader.get_single_data()
    except YAMLError as err:
        assert to_native(err.problem_mark) == 'line 1, column 10'
    finally:
        loader.dispose()

# Generated at 2022-06-13 07:24:32.227998
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'foo': 'bar'}") == {b'foo': b'bar'}
    assert from_yaml(b"{'foo': 'bar'}") == {b'foo': b'bar'}
    assert from_yaml("{'foo': 'bar'}", json_only=True) == {b'foo': b'bar'}

    # Unsupported file extension
    try:
        from_yaml("{'foo': 'bar'}", file_name='test.md')
        assert False
    except AnsibleParserError as e:
        assert 'We were unable to read either as JSON nor YAML' in to_native(e)

# Generated at 2022-06-13 07:24:38.238673
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Run unit tests for from_yaml

    This is not a proper unit test, it just prints out the results from from_yaml
    '''
    def _test_from_yaml(in_data, file_name='<string>', show_content=False, vault_secrets=None):
        '''
        return string containing result of calling from_yaml on in_data
        '''

# Generated at 2022-06-13 07:24:46.704347
# Unit test for function from_yaml
def test_from_yaml():
    # Test a normal string which is parsed as yaml
    yaml_string = '    name: string'
    assert from_yaml(yaml_string) == {'name': 'string'}

    # Test a json like string which is parsed as json
    json_string = '{"name": "string"}'
    assert from_yaml(json_string) == {'name': 'string'}

    # Test a json like string with json_only=True
    json_string = '{"name": "string"}'
    assert from_yaml(json_string, json_only=True) == {'name': 'string'}

# Generated at 2022-06-13 07:25:01.612775
# Unit test for function from_yaml
def test_from_yaml():
    # Load yaml string as JSON
    data_json = '{"key": "value"}'
    result_json = from_yaml(data_json)
    assert result_json == {u'key': u'value'}

    # Load yaml string as YAML
    data_yaml = '{key: value}'
    result_yaml = from_yaml(data_yaml)
    assert result_yaml == {u'key': u'value'}

    # Test error handling
    data_yaml_error = '{key: {key2: value2}'
    try:
        from_yaml(data_yaml_error)
        assert True
    except Exception as exc:
        assert type(exc) is AnsibleParserError


# Generated at 2022-06-13 07:25:10.331893
# Unit test for function from_yaml
def test_from_yaml():

    # test simple json string
    data = '{"a": 1}'
    new_data = from_yaml(data)
    assert new_data == {"a": 1}

    # test simple yaml string (json is subset of yaml)
    data = '{a: 1}'
    new_data = from_yaml(data)
    assert new_data == {"a": 1}

    # test invalid json string
    data = '{"a": 1'
    try:
        from_yaml(data)
        raise Exception('ValueErrors should be raised when data is invalid.')
    except ValueError as e:
        assert "No JSON object could be decoded" in to_native(e)

    # test invalid yaml string
    data = "{a: 1"

# Generated at 2022-06-13 07:25:15.162663
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    data_dict = {"test": "value"}
    data_json = json.dumps(data_dict, cls=AnsibleJSONDecoder)
    data_yaml = yaml.dump(data_dict, Dumper=AnsibleDumper)
    # Convert to Json
    data_from_json = from_yaml(data_json)
    data_from_json = json.dumps(data_from_json, cls=AnsibleJSONDecoder)
    assert data_from_json == data_json
    # Convert to yaml
    data_from_yaml = from_yaml(data_yaml)

# Generated at 2022-06-13 07:25:18.824891
# Unit test for function from_yaml
def test_from_yaml():
    vars_str = """
    ---
    foo: bar
    """
    data = from_yaml(vars_str)
    assert 'foo' in data
    assert data['foo'] == 'bar'

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:30.471954
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('---\n{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('{foo: {bar: baz} }') == {'foo': {'bar': 'baz'}}
    assert from_yaml('foo: {bar: baz}') == {'foo': {'bar': 'baz'}}
    assert from_yaml('foo: [ {bar: baz} ]') == {'foo': [{'bar': 'baz'}]}
    assert from_yaml('foo: [ bar, baz ]') == {'foo': ['bar', 'baz']}

# Generated at 2022-06-13 07:25:37.052629
# Unit test for function from_yaml
def test_from_yaml():
    data="""
        {
            "name": "test_host",
            "groups": ["ungrouped"],
            "vars": {
                "ansible_connection": "local"
            }
            "hostname": "test_host",
            "port": 22
        }
    """

    new_data = from_yaml(data)
    assert new_data["name"] == "test_host"

test_from_yaml()

# Generated at 2022-06-13 07:25:51.476976
# Unit test for function from_yaml

# Generated at 2022-06-13 07:25:59.780678
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'[1,2,3]') == [1,2,3]
    assert from_yaml(u'{a: 1, b: 2}') == {u'a': 1, u'b': 2}
    assert from_yaml(u'---\n- 1\n- 2\n- 3') == [1,2,3]
    assert from_yaml(u'---\na: 1\nb: 2') == {u'a': 1, u'b': 2}
    assert from_yaml(u'---\n0: [1, 2]\n1: [3, 4]') == {0: [1,2], 1: [3,4]}
    # Python's str type is unicode, ansible.parsing.yaml likes normal strings
    assert from_

# Generated at 2022-06-13 07:26:13.420433
# Unit test for function from_yaml
def test_from_yaml():
    filename = './unittest_data/tst_from_yaml_data'
    print(from_yaml(open(filename).read()))


# Generated at 2022-06-13 07:26:18.460737
# Unit test for function from_yaml
def test_from_yaml():
    data = "name: foo"
    foo = from_yaml(data)
    assert foo == {'name': 'foo'}, 'Unexpected object returned.'

    data = "{'name': 'foo'}"
    foo = from_yaml(data)
    assert foo == {'name': 'foo'}, 'Unexpected object returned.'

# Generated at 2022-06-13 07:26:31.701090
# Unit test for function from_yaml

# Generated at 2022-06-13 07:26:42.402051
# Unit test for function from_yaml
def test_from_yaml():
    # Test valid YAML 1.1
    yaml_source = '''
        - key: value
          key2:
            - {key3: value, key4: value}
            - key5: value
    '''
    assert from_yaml(yaml_source) == [{'key': 'value', 'key2': [{'key3': 'value', 'key4': 'value'}, {'key5': 'value'}]}]

    # Test error
    yaml_source = '---\n{key3: value, key4: value}\n...'
    try:
        from_yaml(yaml_source)
        raise AssertionError("The following YAML should not be parsable: %s" % yaml_source)
    except AnsibleParserError:
        pass
    # Test non

# Generated at 2022-06-13 07:26:51.116266
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('{"foo": "bar"}', json_only=True) == {"foo": "bar"}
    assert from_yaml('{"foo": "bar"', json_only=True) == {"foo": "bar"}

    try:
        from_yaml('{"foo": "bar"')
        assert False, "This line should not be reached"
    except AnsibleParserError as e:
        assert e.message.startswith('We were unable to read either as JSON nor YAML, these are the errors we got from each:')
        assert "Unexpected end of JSON input" in e.message
        assert "could not find expected ':' while scanning a simple key" in e.message


# Generated at 2022-06-13 07:27:00.879133
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.module_utils._text import to_text

    yaml_s = to_text('''
a: a
b: b
''')
    assert from_yaml(yaml_s) == {'a': 'a', 'b': 'b'}

    with pytest.raises(AnsibleParserError):
        from_yaml(to_text('{a: a\nb: b}'))

    with pytest.raises(AnsibleParserError):
        from_yaml(to_text('{a: a\n b: b\n }'))


# Generated at 2022-06-13 07:27:10.403867
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import yaml

    text1 = """
    - hosts:
        - host1
        - host2

    - hosts:
        - host3
        - host4

    tasks:
      - name: task1
      - name: task2

    - name: dump hostvars
      debug:
        var: hostvars[inventory_hostname]
        verbosity: 2
    """

    json1 = json.dumps(yaml.load(text1, Loader=AnsibleLoader), cls=AnsibleJSONDecoder)
    assert from_yaml(json1) == yaml.load(text1, Loader=AnsibleLoader)
    assert from_

# Generated at 2022-06-13 07:27:18.430300
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import tempfile

    # Create a small file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write('dummy: data\n')
    dummy_file = tmp.name

    # Attempt to load the file
    from_yaml(dummy_file)
    from_yaml(dummy_file, json_only=True)

    # Attempt to raise an error
    try:
        from_yaml('foo: bar')
    except AnsibleParserError as e:
        assert isinstance(e.orig_exc, YAMLError)
    except Exception as e:
        assert False, "Invalid exception raised: %s" % str(e)

    # Clean up our file
    os.remove(dummy_file)

# Generated at 2022-06-13 07:27:29.078903
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from .test_from_yaml import from_yaml_data
    except ImportError:
        from .test_from_yaml import from_yaml_data

    for (desc, data, file_name, expected) in from_yaml_data:
        result = from_yaml(data, file_name)
        assert result == expected, "%s: expected %r != %r" % (desc, expected, result)

if __name__ == '__main__':
    import sys
    import traceback
    try:
        test_from_yaml()
    except AssertionError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(traceback.format_exc())
        sys.exit(1)