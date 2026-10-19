

# Generated at 2022-06-13 07:17:39.765318
# Unit test for function from_yaml
def test_from_yaml():
    # No error
    yaml_input = '''
---
abc:123
'''
    d = from_yaml(yaml_input)
    assert d == {'abc': 123}
    d = from_yaml(yaml_input, json_only=True)
    assert d == {'abc': 123}

    # Syntax error
    yaml_input = '''
---
abc:123
---
'''
    try:
        d = from_yaml(yaml_input)
        assert False
    except AnsibleParserError as e:
        assert 'invalid yaml' in e.message

    # JSON error
    yaml_input = '''
---
abc:123
'''

# Generated at 2022-06-13 07:17:48.443513
# Unit test for function from_yaml
def test_from_yaml():

    import sys
    import pytest

    # Default AnsibleJSONDecoder.set_secrets() call sets _secrets to None
    if sys.version_info < (3,):
        from ansible.parsing.ajson import AnsibleJSONDecoder
        AnsibleJSONDecoder.set_secrets(None)

    # test dumps of python objects into JSON and use from_yaml to
    # construct the same objects

# Generated at 2022-06-13 07:17:53.895482
# Unit test for function from_yaml
def test_from_yaml():
    if not bool(from_yaml('{}')) and not bool(from_yaml('{"foo": "bar"}')):
        raise Exception("from_yaml() cannot parse JSON.")
    if not bool(from_yaml('---\n')) and not bool(from_yaml('---\nfoo: bar\n')):
        raise Exception("from_yaml() cannot parse YAML.")

# Generated at 2022-06-13 07:18:02.935441
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{"hello": "world"}'))
    print(from_yaml('{"hello": "world"}', json_only=True))
    print(from_yaml('hello: world'))
    print(from_yaml('hello: world', json_only=True))
    print(from_yaml('{"hello": world'))
    print(from_yaml('{"hello": world', json_only=True))
    print(from_yaml('hello: "world"'))
    print(from_yaml('hello: "world"', json_only=True))
    print(from_yaml('hello: world', file_name='test.yml'))
    print(from_yaml('hello: world', file_name='test.yml', json_only=True))

# Generated at 2022-06-13 07:18:13.147162
# Unit test for function from_yaml

# Generated at 2022-06-13 07:18:23.999887
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils._text import to_bytes

    def _get_path(name):
        test_dir = os.path.dirname(sys.modules[__name__].__file__)
        return os.path.join(test_dir, '..', '..', 'unit', 'parsing', 'yaml', name)

    test_json_data = open(_get_path('data/json_array.json')).read()
    assert isinstance(from_yaml(to_bytes(test_json_data), vault_secrets=VaultSecret([])), list)

# Generated at 2022-06-13 07:18:33.642245
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test function from_yaml
    '''
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    test_data = {'some_unicode': u'\u2665', 'some_bytes': b'\xe2\x99\xa5'}
    test_json = json.dumps(test_data, ensure_ascii=False, cls=AnsibleJSONEncoder)
    test_yaml = _safe_load(test_json)

    assert test_yaml == test_data

    dumper = AnsibleDumper()

# Generated at 2022-06-13 07:18:41.798712
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # Test case 1
    array_yaml = u'''[{'key': ['value1', 'value2', "value3"]},
                    {'key1': 'value1',
                    'key2': 'value2'}]'''
    array = from_yaml(array_yaml)
    assert array[0]['key'][0] == 'value1'
    assert array[0]['key'][1] == 'value2'
    assert array[0]['key'][2] == 'value3'
    assert array[1]['key1'] == 'value1'
    assert array[1]['key2'] == 'value2'

    # Test case 2
    # Detect integer
    assert from_yaml('150') == 150

# Generated at 2022-06-13 07:18:52.914994
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys
    import os

    # We can't run this test in python2.6 because it doesn't have the ability to
    # override the 'import' builtin
    # https://docs.python.org/2.6/library/functions.html
    if sys.version_info < (2,7):
        return

    tmp_file = 'test_from_yaml.yml'
    with open('agol.yml', 'r') as f:
        yml_data = f.read()
    data = from_yaml(yml_data, tmp_file)
    # Test that normal data structure is returned
    assert isinstance(data, dict)

# Generated at 2022-06-13 07:19:00.440731
# Unit test for function from_yaml
def test_from_yaml():
    file = 'tests/test_docs_ansible_module_data.json'
    show_content = True
    data = open(file).read()
    ansible_module = from_yaml(data, file_name=file, show_content=show_content)

    assert ansible_module[0]['doc']['return'] == [{'type': 'bool',
                                                 'description':
                                                 'Ansible checks if changed is set to True when running a module.  If set to True, this will let Ansible know that your module had an effect on the system.  If no other tasks have modified the system, Ansible will get a changed result and will proceed to call the handlers of this module.',
                                                 'optional': True}]


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:09.139417
# Unit test for function from_yaml
def test_from_yaml():
    testdata1 = '''---
foo: bar
# comment
baz:
  - test
  - 123
  - true
  - null
'''

    result = from_yaml(testdata1)
    assert result == {'foo': 'bar', 'baz': ['test', 123, True, None]}

    testdata2 = '''---
foo: bar
# comment
baz:
  - test
  - 123
  - true
  - null
'''

    result = from_yaml(testdata2)
    assert result == {'foo': 'bar', 'baz': ['test', 123, True, None]}

    assert from_yaml(testdata2, '<string>', True) == {'foo': 'bar', 'baz': ['test', 123, True, None]}


# Generated at 2022-06-13 07:19:22.550112
# Unit test for function from_yaml
def test_from_yaml():
    # This test only covers the try/except logic, not the parsing logic
    data = '{"a": [1, 2, 3]}'
    new_data = from_yaml(data)
    assert new_data['a'][0] == 1

    data = '{"a": 1\n "b": 2}'  # invalid JSON
    try:
        from_yaml(data)
        assert False  # should never get here
    except AnsibleParserError:
        pass

    data = '---\n"a": [1, 2, 3]'  # valid YAML but not JSON
    new_data = from_yaml(data)
    assert new_data['a'][0] == 1

    data = '---\n"a": [1, 2, 3}\n'  # invalid YAML

# Generated at 2022-06-13 07:19:30.538113
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()

# Generated at 2022-06-13 07:19:41.543613
# Unit test for function from_yaml
def test_from_yaml():

    # FIXME: Those should be real unit tests, not doctest tests
    import doctest
    import sys

    if sys.version_info[0] > 2:  # Python 3
        import io
        import sys
        import yaml

        class TestAnsibleJSONDecoder(json.JSONDecoder):
            def decode(self, data):
                return super(TestAnsibleJSONDecoder, self).decode(data)

        def test_from_json(data, file_name='<string>', show_content=True):
            '''
            Creates a python datastructure from the given data, which must be a JSON string.
            '''
            new_data = None
            new_data = json.load(io.StringIO(data), cls=TestAnsibleJSONDecoder)
            return new_data

       

# Generated at 2022-06-13 07:19:43.187089
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This tests the function from_yaml.
    '''
    pass

# Generated at 2022-06-13 07:19:46.279638
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    input = '''
{
  "name": "World",
  "hello": 3
}
'''
    data = from_yaml(input)
    assert data["hello"] == 3

# Generated at 2022-06-13 07:19:49.989365
# Unit test for function from_yaml
def test_from_yaml():
    test_yaml = """
    test_yaml:
      - test_yaml_list_item
    """
    assert from_yaml(test_yaml) == {'test_yaml': ['test_yaml_list_item']}



# Generated at 2022-06-13 07:19:57.908513
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test function for function from_yaml
    '''
    assert from_yaml("") is None
    assert from_yaml(" ") is None
    assert from_yaml("{}") == {}
    assert from_yaml("[]") == []
    assert from_yaml("text") == "text"
    assert from_yaml("1") == 1
    assert from_yaml("1.1") == 1.1

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:20:01.334926
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    assert from_yaml("[ 1, 2, 3 ]") == [1, 2, 3]
    assert from_yaml("foo: bar") == {'foo': 'bar'}

# Generated at 2022-06-13 07:20:08.515880
# Unit test for function from_yaml
def test_from_yaml():
    test_data = [
        {
            'json': "{'a': 42}",
            'expected': {'a': 42}
        },
        {
            'json': "{\"a\": 42}",
            'expected': {'a': 42}
        }
    ]

    for data in test_data:
        actual = from_yaml(data.get('json'))
        assert actual == data.get('expected')


# Load 'ansible' import path after test_from_yaml has been defined, to avoid a circular import
# (utils.py imports from_yaml, which imports the Loader class, which imports the PluginLoader class,
# which imports the utils module).
from ansible.plugins.loader import become_loader, callback_loader, connection_loader, filter_loader, lookup_loader

# Generated at 2022-06-13 07:20:14.121127
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo') == 'foo'
    assert from_yaml('{ "foo": "bar" }') == { "foo": "bar" }
    assert from_yaml('---\n- foo\n- bar') == ['foo', 'bar']

# Generated at 2022-06-13 07:20:17.802216
# Unit test for function from_yaml
def test_from_yaml():
    # This unit test is just a stub for now
    # TODO: add more tests
    assert from_yaml('hi') == 'hi'
    assert from_yaml('{"hi": 1}') == {'hi': 1}

# Generated at 2022-06-13 07:20:27.140232
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"testTrue": true, "testFalse": false, "testList": [ "item1", "item2" ], "testDict": { "item1": "value1", "item2": "value2" }, "testInt": 1, "testFloat": 99.99}'
    new_data = from_yaml(data)
    assert new_data is not None
    assert new_data['testTrue'] is True
    assert new_data['testFalse'] is False
    assert new_data['testList'] == [ 'item1', 'item2' ]
    assert new_data['testDict'] == { 'item1': 'value1', 'item2': 'value2' }
    assert new_data['testInt'] == 1
    assert new_data['testFloat'] == 99.99


# Generated at 2022-06-13 07:20:37.771415
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.errors import AnsibleParserError

    assert from_yaml(b'{{ foo }}') is None

    try:
        from_yaml(b'{{ foo }}', show_content=False)
    except AnsibleParserError as e:
        msg = str(e)
        print('msg:', msg)
        assert 'We were unable to parse your inventory' in msg
        assert '{{ foo }}' not in msg
    else:
        pytest.fail('AnsibleParserError should have been raised')

    try:
        from_yaml(b'{{ foo }}', show_content=True)
    except AnsibleParserError as e:
        msg = str(e)
        print('msg:', msg)
        assert 'We were unable to parse your inventory' in msg

# Generated at 2022-06-13 07:20:41.742168
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": 1}') == {u'a': 1}
    assert from_yaml('a: 1') == {u'a': 1}

# Generated at 2022-06-13 07:20:55.822650
# Unit test for function from_yaml
def test_from_yaml():
    """ test_from_yaml: Tests to ensure from_yaml returns the same data as loaded from a YAML file. """
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils._text import to_bytes

    original = {'key1': 'value1', 'key2': {'key3': 'value3'}, 'key4': [1, 2, 3]}
    data = AnsibleDumper(original).get_data()
    assert original == from_yaml(data)

    vaulted_data = AnsibleVaultEncryptedUnicode.from_plaintext(to_bytes('secret'))


# Generated at 2022-06-13 07:21:01.700313
# Unit test for function from_yaml
def test_from_yaml():
    data = b"test: True"
    assert from_yaml(data) == {'test': True}

    data = b'"foo"'
    assert from_yaml(data) == 'foo'

    data = b'1'
    assert from_yaml(data) == 1

    data = b'# test\n1'
    assert from_yaml(data) == 1


# Generated at 2022-06-13 07:21:15.770024
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml(data="{}")
        from_yaml(data="[]", show_content="False")
        from_yaml(data="[]", vault_secrets="")
        from_yaml(data="[]", vault_secrets="[]")
        from_yaml(data="[]", json_only="")
        from_yaml(data="[]", json_only="True")
    except AnsibleParserError as exception:
        assert exception.msg == 'We were unable to read either as JSON nor YAML, these are the errors we got from each:\n' \
                'JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)\n\n' \
                'The error appears to have been in \'%s\': line 1, column 1, but may\n' \
               

# Generated at 2022-06-13 07:21:23.274255
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "foo": [ "bar", "baz" ] }') == {'foo': ['bar', 'baz']}
    assert from_yaml('- foo\n- bar') == ['foo', 'bar']
    assert from_yaml('{ "foo": "bar" }') == {'foo': 'bar'}
    assert from_yaml('{ "include": "*.yml" }') == {'include': '*.yml'}
    assert from_yaml('{ foo: bar }') == {'foo': 'bar'}
    assert from_yaml('[ foo, bar ]') == ['foo', 'bar']


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 07:21:37.321945
# Unit test for function from_yaml
def test_from_yaml():

    # Borrowed from ansible.hacking.pylint.reporter.get_parser_opts()
    OPTIONS = {
        'file': '<string>',
        'vault_password_files': [],
        'new_plugins': True,
        'plugins': None,
        'group_names': set(['ANSIBLE']),
        'ignore_plugins': set(),
    }

    JSON_STRING = '{"a": 1, "b": 2}'
    assert from_yaml(JSON_STRING, **OPTIONS) == {u'a': 1, u'b': 2}

    YAML_STRING = "a: 1\nb: 2"
    assert from_yaml(YAML_STRING, **OPTIONS) == {u'a': 1, u'b': 2}

# Generated at 2022-06-13 07:21:43.983377
# Unit test for function from_yaml
def test_from_yaml():
    test_data = '{"foo":"bar","baz":[1,2,3]}'
    result = from_yaml(test_data, file_name='test_file', show_content=False)

    assert result == json.loads(test_data)

# Generated at 2022-06-13 07:21:53.608070
# Unit test for function from_yaml
def test_from_yaml():
    data_examples = [
        ({"a": 1, "b": 2}, "{\"a\": 1, \"b\": 2}"),
        ("1a", "\"1a\""),
        (b"1a", "\"1a\""),
        (1, "1"),
        ("null", "null"),
        (False, "false"),
        (True, "true"),
    ]

    for expected, data in data_examples:
        result = from_yaml(data)
        assert( result == expected )

    data_examples_json_only = [
        ({"a": 1, "b": 2}, "{\"a\": 1, \"b\": 2}"),
        ("1a", "\"1a\""),
        (b"1a", "\"1a\""),
        (1, "1"),
    ]



# Generated at 2022-06-13 07:21:58.008564
# Unit test for function from_yaml
def test_from_yaml():
    x = from_yaml('1')
    assert x == 1

    x = from_yaml('[1, 2, 3]')
    assert x == [1, 2, 3]

    x = from_yaml('{ "a": 1, "b": 2 }')
    assert x == { 'a': 1, 'b': 2 }

    x = from_yaml('a: 1\nb: 2\nc: 3')
    assert x == { 'a': 1, 'b': 2, 'c': 3 }

# Generated at 2022-06-13 07:22:08.862766
# Unit test for function from_yaml
def test_from_yaml():
    # Test with empty string
    data = ""

    assert from_yaml(data) == None

    # Test with string
    data = "string"

    assert from_yaml(data) == "string"

    # Test with simple JSON
    data = json.dumps({'key': 'value'})

    assert from_yaml(data) == {"key":"value"}

    # Test with simple JSON
    data = json.dumps(['key', 'value'])

    assert from_yaml(data) == ["key", "value"]

    # Test with simple YAML
    data = "key: value"

    assert from_yaml(data) == {"key":"value"}

    # Test with simple YAML
    data = "- key\n- value"


# Generated at 2022-06-13 07:22:23.459017
# Unit test for function from_yaml
def test_from_yaml():
    #from ansible.inventory import Inventory
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    def _test_yaml(yaml_str, expected_data):
        data = from_yaml(yaml_str, file_name='<string>', show_content=True)
        assert data == expected_data
        assert type(data) == type(expected_data)


# Generated at 2022-06-13 07:22:25.505771
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml('{"foo": "bar"}')
        assert True
    except:
        assert False

# Generated at 2022-06-13 07:22:39.915235
# Unit test for function from_yaml
def test_from_yaml():
    # Test with a valid YAML string
    str_yaml = "a: 1\nb: 2"
    assert from_yaml(str_yaml) == {'a': 1, 'b': 2}

    # Test with a valid JSON string
    str_json = "{\"a\": 1, \"b\": 2}"
    assert from_yaml(str_json) == {'a': 1, 'b': 2}

    # Test with invalid JSON string
    str_json = "{\"a\": 1, \"b\": 2"
    try:
        from_yaml(str_json)
    except Exception as err:
        assert isinstance(err, AnsibleParserError)

    # Test with invalid YAML string
    str_yaml = "a: 1\nb: 2"

# Generated at 2022-06-13 07:22:40.792228
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:22:50.802818
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import inspect
    from ansible.utils.vars import combine_vars

    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe())))) + os.path.sep + 'lib' + os.path.sep + 'ansible' + os.path.sep

    vars_files = [
        'test/units/parsing/vars/main.yml',
        'test/units/parsing/vars/extend.yml',
        'test/units/parsing/vars/combine.yml'
    ]

    # combine vars files into one data structure
    vars_data = {}

# Generated at 2022-06-13 07:22:54.378474
# Unit test for function from_yaml
def test_from_yaml():
    data = '{ "name": "john doe" }'
    new_data = from_yaml(data)
    assert new_data['name'] == 'john doe'



# Generated at 2022-06-13 07:23:07.283938
# Unit test for function from_yaml
def test_from_yaml():

    import os
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import ansible.parsing.yaml.loader
    from ansible.parsing.utils.yaml_loader import AnsibleLoader

    ANSIBLE_VAULT_PASSWORD_FILE = os.environ.get('ANSIBLE_VAULT_PASSWORD_FILE', None)
    ANSIBLE_VAULT_PASSWORD = os.environ.get('ANSIBLE_VAULT_PASSWORD', None)


# Generated at 2022-06-13 07:23:10.534023
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'test': 123}"
    data2 = '{"test": 123}'

    assert from_yaml(data) == json.loads(data2)
    assert from_yaml(data2) == json.loads(data2)

# Generated at 2022-06-13 07:23:15.117329
# Unit test for function from_yaml
def test_from_yaml():
    test_data = '''
---
- hosts: localhost
  tasks:
    - debug:
        msg: vmware_guest exists
    - debug:
        msg: vmware_guest
'''
    print(from_yaml(test_data))
    assert True

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:23:25.467625
# Unit test for function from_yaml
def test_from_yaml():
    """Test the from_yaml function"""

    # Test JSON
    data = '{"hello": "world"}'
    new_data = from_yaml(data)
    assert new_data == {"hello": "world"}

    # Test YAML
    data = '''
        foo:
          - bar
          - baz
    '''
    new_data = from_yaml(data)
    assert new_data == {"foo": ["bar", "baz"]}

    # Test invalid JSON
    data = '{"hello": "world"}'
    try:
        new_data = from_yaml(data, json_only=True)
    except Exception:
        assert True
    else:
        assert False

    # Test invalid syntax
    data = '{"hello": "world": "boo"}'

# Generated at 2022-06-13 07:23:29.072123
# Unit test for function from_yaml
def test_from_yaml():

    data = "[{ \"key\": \"value\" }]"
    assert "[{u'key': u'value'}]" == str(from_yaml(data))

    data = { "key": "value" }
    assert "{u'key': u'value'}" == str(from_yaml(data))

    data = "{ \"key\": \"value\" }"
    assert "{u'key': u'value'}" == str(from_yaml(data))

    data = "[{ \"key\": \"value\", \"key\": \"value\" }]"
    try:
        from_yaml(data)
    except AnsibleParserError as e:
        assert 'line 1, column 17' in str(e)

    data = "[{ \"key\": \"value\", \"key\": \"value\", \"key\": \"value\" }]"

# Generated at 2022-06-13 07:23:43.431734
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    original = dict(
        a=dict(
            b=dict(
                c=dict(
                    d=1,
                ),
                e=[
                    1,
                    2,
                    3,
                ],
            ),
        ),
        f=[
            dict(
                g=1,
            ),
            dict(
                h=1,
            ),
        ],
        i="{{ lookup('env','HOME') }}",
        j="{{ lookup('env','PATH') }}",
    )
    yaml_text = yaml.dump(original, Dumper=AnsibleDumper, default_flow_style=False)

    parsed = from_yaml(yaml_text)
    assert parsed == original

    assert parsed['i'] != original

# Generated at 2022-06-13 07:23:55.174962
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'test': {'test': 'test'}}"
    assert from_yaml(data, show_content=False) == {'test': {'test': 'test'}}
    assert from_yaml(data, json_only=True, show_content=False) == {'test': {'test': 'test'}}

    data = "{'test': 'test'} 1"
    assert from_yaml(data, show_content=False).get('test') == 'test'

    data = '{"test": {"test": "test"}}'
    assert from_yaml(data, show_content=False) == {'test': {'test': 'test'}}
    assert from_yaml(data, json_only=True, show_content=False) == {'test': {'test': 'test'}}



# Generated at 2022-06-13 07:23:58.763858
# Unit test for function from_yaml
def test_from_yaml():
    try:
         from_yaml('{"foo": "bar"}')
         assert True
    except:
        assert False
    try:
         from_yaml('{"foo": "bar",')
         assert False
    except:
        assert True

# Generated at 2022-06-13 07:24:06.271394
# Unit test for function from_yaml
def test_from_yaml():
    data = dict(a=1, b=2)
    assert from_yaml('{"a": 1, "b": 2}') == data
    assert from_yaml('{"a": 1, "b": 2}', json_only=True) == data
    assert from_yaml('{"a": 1, "b": 2', json_only=True) == data
    assert from_yaml('{"a": 1, "b": 2', json_only=True, file_name='test_from_yaml') == data

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:12.805118
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{  "foo": true, "bar": false }') == {"foo": True, "bar": False}
    assert from_yaml('- {  "foo": true, "bar": false }') == [{'foo': True, 'bar': False}]
    assert from_yaml('- {  "foo": true, "bar": false }\n- {  "foo": true, "bar": false }') == [{'foo': True, 'bar': False}, {'foo': True, 'bar': False}]
    assert from_yaml('{  "foo": true, "bar": false }\n- {  "foo": true, "bar": false }') == {'foo': True, 'bar': False}

    assert from_yaml('---\nfoo: 1') == {'foo': 1}

# Generated at 2022-06-13 07:24:29.652313
# Unit test for function from_yaml
def test_from_yaml():
    # Test for issue #18754
    jdata = '{"foo": "bar"}'
    jdata2 = from_yaml(jdata)
    assert jdata2['foo'] == "bar"

    # Test for issue #42892
    jdata = '{"foo": "bar"}'
    jdata2 = from_yaml(jdata, json_only=True)
    assert jdata2['foo'] == "bar"

# Generated at 2022-06-13 07:24:37.516797
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.parsing.convert_bool import boolean

    true_tests = [
        'True',
        'On',
        'true',
        'yes',
        'Yes',
        'y',
        'Y',
        'ON'
    ]

    for test in true_tests:
        print(test, boolean(from_yaml(test), strict=False))

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:47.841584
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "test": "ok" }') == {u'test': u'ok'}
    assert from_yaml('test: ok') == {u'test': u'ok'}
    assert from_yaml("""
- a: 1
- b:
    - 2
    - 3
- c: 4
""") == [u'a', {u'b': [2, 3]}, {u'c': 4}]
    assert (from_yaml("""
- [ a, b ]
- { c: d }
""") == [[u'a', u'b'], {u'c': u'd'}])


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 07:24:51.141515
# Unit test for function from_yaml
def test_from_yaml():
    data = {}
    from_yaml(data, file_name='test', show_content=True, vault_secrets=None, json_only=False)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:24:56.807526
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    ---
    a: 1
    b: 2
    '''
    try:
        from_yaml(data)
    except AnsibleParserError:
        raise AssertionError('from_yaml failed.')

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:02.106808
# Unit test for function from_yaml
def test_from_yaml():
    ''' basic unit test to check json, then yaml, then bad data '''

    raw_result = from_yaml("test")
    assert raw_result == "test"

    raw_result = from_yaml("{\"test\":\"test\"}")
    assert raw_result == {"test": "test"}

    try:
        raw_result = from_yaml("test: test")
    except Exception:
        raw_result = None
    assert raw_result is None



# Generated at 2022-06-13 07:25:10.941141
# Unit test for function from_yaml
def test_from_yaml():
    ''' Unit test for function `from_yaml` '''
    assert from_yaml('foo') == 'foo'
    assert from_yaml("{ 'foo': 'bar'}") == {'foo': 'bar'}
    assert from_yaml("[ 'foo', 'bar']") == ['foo', 'bar']
    assert from_yaml("[ 'foo', 'bar']", json_only=True) == ['foo', 'bar']
    assert from_yaml("{ 'foo': 'bar'}", json_only=True) == {'foo': 'bar'}
    with pytest.raises(AnsibleParserError):
        from_yaml("{ 'foo': 'bar'}", json_only=True, show_content=False)

# Generated at 2022-06-13 07:25:12.828438
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{}') == {}
    assert from_yaml('key1: value1') == {'key1': 'value1'}

# Generated at 2022-06-13 07:25:22.177402
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This is a unit test for the from_yaml function.
    '''

    # Load valid json data
    valid_json_data = '{"key": "value", "answer": 42}'

    # Load valid yaml data
    valid_yaml_data = '---\nkey: value\nanswer: 42\n'

    # Load json data with YAML comments
    yaml_comments_data = '''
        {
            "key": "value",
            "answer": 42,
            "data": [1, 2, 3],
        }  # this is only JSON
    '''

    # Load json data with block chomping indicator (|)
    block_chomping_data = '''
---
{ key: value}
'''

    # Load bad JSON data
    bad_json_data

# Generated at 2022-06-13 07:25:29.450791
# Unit test for function from_yaml
def test_from_yaml():
    # Test the parsing of yaml
    y = '''
    ---
    a: b
    c: 1
    '''
    data = from_yaml(y)
    assert data['a'] == 'b'
    assert data['c'] == 1

    # Test the parsing of json
    j = '{"a":"b", "c": 1}'
    data = from_yaml(j)
    assert data['a'] == 'b'
    assert data['c'] == 1

# Generated at 2022-06-13 07:25:55.936770
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {u'foo': u'bar'}
    assert from_yaml('[foo, bar]') == [u'foo', u'bar']
    assert from_yaml('{"foo": {"bar": "baz"}}') == {u'foo': {u'bar': u'baz'}}
    assert from_yaml('{"foo": [bar, baz]}') == {u'foo': [u'bar', u'baz']}


# Generated at 2022-06-13 07:26:07.291583
# Unit test for function from_yaml
def test_from_yaml():
    # Test with a YAML string
    yaml_string = '''
    foo: bar
    baz:
        - qux
        - quux
    '''
    data = from_yaml(yaml_string)

    assert data['foo'] == 'bar'
    assert data['baz'] == ['qux', 'quux']

    # Test with a non-YAML string
    non_yaml_string = '''
    foo bar
    baz
        - qux
        - quux
    '''

    try:
        data = from_yaml(non_yaml_string)
    except AnsibleParserError as e:
        assert e.orig_exc
        assert str(e.orig_exc)

# Generated at 2022-06-13 07:26:11.744173
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml('{ "a": "b" }'), dict)
    assert isinstance(from_yaml('{ "a": "b" }', json_only=True), dict)

    try:
        assert isinstance(from_yaml('{ a: b }', json_only=True), dict)
    except AnsibleParserError:
        pass
    else:
        assert False, 'Failed to raise error when given a YAML string'

# Generated at 2022-06-13 07:26:14.216733
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('---\na'))
    print(from_yaml('{a}'))
    print(from_yaml('a'))

test_from_yaml()

# Generated at 2022-06-13 07:26:20.810955
# Unit test for function from_yaml
def test_from_yaml():
    # Positive testcase
    test_data = "---\n- name: foo\n  key: value"
    assert isinstance(from_yaml(test_data), list)

    # Negative testcase, error should be thrown
    try:
        test_data = "---\nname: foo\nkey: value"
        from_yaml(test_data)
    except AnsibleParserError:
        pass
    else:
        assert False

# Generated at 2022-06-13 07:26:30.109414
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.parsing.dataloader import DataLoader

    f = 'tests/units/parsing/yaml/yaml_multiline.yml'
    data = DataLoader().load_from_file(f)

    assert data['a'] == 'b'
    assert data['c'] == 'd'
    assert data['e'] == [
        {'g': 'h'},
        {'i': 'j'}
    ]
    assert data['k'] == 'l'

    # Test with a bad YAML file
    with pytest.raises(AnsibleParserError):
        f = 'tests/units/parsing/yaml/yaml_badsyntax.yml'
        DataLoader().load_from_file(f)

    # Test with a bad

# Generated at 2022-06-13 07:26:40.638341
# Unit test for function from_yaml
def test_from_yaml():

    import ansible.parsing.yaml.objects as ya_obj

# Generated at 2022-06-13 07:26:50.376478
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from io import StringIO

    assert from_yaml("{}") == {}
    assert from_yaml("---{}") == {}
    assert from_yaml("{}", json_only=True) == {}
    assert from_yaml("---{}", json_only=True) == {}

    # expected error cases
    try:
        assert from_yaml("[") == {}
        pytest.fail("Did not raise AnsibleParserError")
    except AnsibleParserError:
        pass


# Generated at 2022-06-13 07:27:00.187037
# Unit test for function from_yaml
def test_from_yaml():
    ''' Test function from_yaml '''

    # Test function return
    data = '{"foo": "bar"}'
    assert from_yaml(data) == {'foo': 'bar'}
    data = 'foo: bar'
    assert from_yaml(data) == {'foo': 'bar'}

    # Test exceptions (JSON)
    data = '{"foo": "bar"'
    try:
        from_yaml(data)
    except AnsibleParserError:
        pass
    else:
        assert False

    # Test exceptions (YAML)
    data = 'foo: bar'
    try:
        from_yaml(data, json_only=True)
    except AnsibleParserError:
        pass
    else:
        assert False

# Generated at 2022-06-13 07:27:11.343416
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": 1, "bar": "something"}') == {"foo": 1, "bar": "something"}
    assert from_yaml('foo: 1\nbar: something') == {"foo": 1, "bar": "something"}
    assert from_yaml('"invalid yaml":') == '"invalid yaml":'
    assert from_yaml('"a":') == '"a":'
    assert from_yaml('"b":') == '"b":'
    assert from_yaml('"c":') == '"c":'
    assert from_yaml('"d":') == '"d":'
    assert from_yaml('"e":') == '"e":'
    assert from_yaml('"f":') == '"f":'
    assert from_yaml