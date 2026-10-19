

# Generated at 2022-06-13 07:17:39.864961
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{}') == {}, "Failed to load JSON empty dict"
    assert from_yaml('[]') == [], "Failed to load JSON empty list"
    assert from_yaml('""') == '', "Failed to load JSON empty string"
    assert from_yaml('''{ "test": "abc" }''') == {"test": "abc"}, "Failed to load JSON dict"
    assert from_yaml('''[ "test", "abc" ]''') == ["test", "abc"], "Failed to load JSON list"
    assert from_yaml('"abc"') == "abc", "Failed to load JSON string"
    assert from_yaml('1') == 1, "Failed to load JSON integer"

# Generated at 2022-06-13 07:17:48.530333
# Unit test for function from_yaml
def test_from_yaml():
    expected_data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key31': 'value31',
            'key32': 'value32',
            'key33': {
                'key331': 'value331',
                'key332': 'value332'
            }
        }
    }

    # Test case 1: Test valid yaml string
    test_yaml_string = "---\nkey1: value1\nkey2: value2\nkey3:\n  key31: value31\n  key32: value32\n  key33:\n    key331: value331\n    key332: value332\n"
    data = from_yaml(test_yaml_string)
    assert data == expected_data

    # Test case

# Generated at 2022-06-13 07:17:58.869046
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.config.data import ConfigData

    config = ConfigData()
    data = """
a: 1
b:
    b1: test_b1
    b2: test_b2
c:
    c1:
        c1a: test_c1a
        c1b: test_c1b
    c2: test_c2
    c3:
      - c3a: test_c3a
      - c3b: test_c3b
      - c3c: test_c3c

"""
    config.parse_config_file(data)
    print(config)
    assert config.get('a') == 1
    assert config.get_config_value('b', 'b1') == 'test_b1'

# Generated at 2022-06-13 07:18:08.273070
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test function from_yaml
    '''
    import unittest
    import sys
    import os
    # import shutil
    # import six

    #from ansible.parsing import yaml

    #from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    #from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    #from ansible.parsing.yaml.objects import AnsibleSequence
    #from ansible.parsing.yaml.objects import AnsibleMapping
    #from ansible.parsing.yaml.objects import AnsibleUnicode

    class TestFromYaml(unittest.TestCase):
        '''
        Test class for function from_yaml
        '''

       

# Generated at 2022-06-13 07:18:12.020990
# Unit test for function from_yaml
def test_from_yaml():
  print('Test from_yaml')
  data = '{"a": 1, "b": 2, "c": 3, "d": 4,  "e": 5}'
  print('data:{}'.format(data))
  print(from_yaml(data))

# Generated at 2022-06-13 07:18:17.425234
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'name': 'Jim'}"

    # First test that we can read in a json string
    try:
        from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    except Exception as e:
        raise Exception("Failed to read json string: " + to_native(e))

    # Next test that we throw an exception when we use a yaml string
    try:
        from_yaml("name: Jim", file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    except Exception as e:
        assert True
        return
    assert False


# Generated at 2022-06-13 07:18:23.540632
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "name": "John Doe" }') == { "name": "John Doe" }
    assert from_yaml('{ name: John Doe }') == { "name": "John Doe" }
    return True

if __name__ == "__main__":
    print(test_from_yaml())

# Generated at 2022-06-13 07:18:33.558949
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test that from_yaml correctly loads JSON or YAML
    '''
    assert from_yaml('["foo", "bar", "baz"]') == ['foo', 'bar', 'baz']
    assert from_yaml('{"foo": 1}') == {'foo': 1}

    assert from_yaml('[foo, bar, baz]') == ['foo', 'bar', 'baz']
    assert from_yaml('{foo: 1}') == {'foo': 1}

    # Test to make sure 'true'/'false' aren't being coerced to bools
    # in the JSON case by passing a decoder that checks that
    class CheckStringBools(json.JSONDecoder):
        def __init__(self, *args, **kwargs):
            super(CheckStringBools, self).__

# Generated at 2022-06-13 07:18:41.727138
# Unit test for function from_yaml
def test_from_yaml():

    # Test default behavior (show_content=True, json_only=False)
    try:
        from_yaml('{"foo": "bar", "empty": null}', '<string>')
    except AnsibleParserError as e:
        assert False, "No exception should happen here"
    try:
        from_yaml('{foo: "bar"}', '<string>')
    except AnsibleParserError as e:
        assert ':1:1:' in to_native(e), "AnsibleParserError should contain the error position"
        assert '{foo: "bar"}' in to_native(e), "AnsibleParserError should contain the content"

# Generated at 2022-06-13 07:18:43.509944
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'a': 1}") == {'a': 1}
    assert from_yaml('{"a": "b"}') == {'a': 'b'}

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:54.655305
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'{ "foo": "bar" }') == { "foo": "bar" }
    assert from_yaml(u'{ foo: bar }') == { "foo": "bar" }
    assert from_yaml(u'foo: bar') == { "foo": "bar" }
    assert from_yaml(u'[ "foo", "bar" ]') == [ "foo", "bar" ]
    assert from_yaml(u'''
    ---
    - 1
    - 2
    - 3
    ...
    ''') == [ 1, 2, 3 ]



# Generated at 2022-06-13 07:18:58.534439
# Unit test for function from_yaml
def test_from_yaml():
    # Given
    data = "this is yaml data"
    expected = data

    # When
    actual = from_yaml(data)

    # Then
    assert actual == expected

# Generated at 2022-06-13 07:19:07.454230
# Unit test for function from_yaml
def test_from_yaml():
    try:
        # test invalid json
        print("Testing invalid json...")
        from_yaml("{\"foo\" \"bar\"}")
        raise Exception("Invalid json string not causing error")
    except Exception as e:
        print("Caught error as expected: %s" % e)
    print("Testing invalid yaml...")
    try:
        from_yaml("foo: bar\n")
        raise Exception("Invalid yaml string not causing error")
    except Exception as e:
        print("Caught error as expected: %s" % e)
    # test valid json and yaml
    print("Valid JSON with single element...")
    print(from_yaml("{\"foo\": \"bar\"}"))
    print("Valid JSON with multiple elements...")

# Generated at 2022-06-13 07:19:18.614740
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six.moves import StringIO

    def assert_yml(data, expected):
        stream = StringIO(data)
        assert from_yaml(stream) == expected

    assert_yml('', None)
    assert_yml('{}', {})
    assert_yml('- 1\n- 2', [1, 2])
    assert_yml('1', 1)
    assert_yml('yes', True)
    assert_yml('no', False)
    assert_yml('null', None)
    assert_yml('[a,b,c,d]', ['a', 'b', 'c', 'd'])
    assert_yml('{a: null}', {'a': None})

# Generated at 2022-06-13 07:19:21.854746
# Unit test for function from_yaml
def test_from_yaml():
    assert (from_yaml('{"a": "b"}') == {"a": "b"})
    assert (from_yaml('{a: b}') == {"a": "b"})



# Generated at 2022-06-13 07:19:30.665319
# Unit test for function from_yaml
def test_from_yaml():
    # a default test case:
    #   from_yaml(data, file_name='<string>', show_content=True)
    data = '''
    - name: Test
      value: 1
    '''
    assert from_yaml(data) == [
        {
            'name': 'Test',
            'value': 1
        }
    ]

    # setting show_content to False
    assert from_yaml(data, show_content=False) == [
        {
            'name': 'Test',
            'value': 1
        }
    ]

    # with vault

# Generated at 2022-06-13 07:19:35.543934
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import BytesIO

    data_loader = DataLoader()
    yaml_str = """
---
test:
  - {host: www.example.com, port: 80}
  - {host: www.example.org, port: 80}
  - {host: www.example.net, port: 80}
"""
    yaml_data = data_loader.load(BytesIO(yaml_str))

# Generated at 2022-06-13 07:19:47.707816
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    import json
    import copy

    yaml_dir = "tests/yaml/"
    VERBOSITY = 1

    def display(msg, verbose, display_stderr=True):
        if not verbose:
            return

        if display_stderr:
            msg = "STDERR: %s" % msg

        print("\n%s\n" % msg)

    def test_file(full_path, base_name, display_failures=False):
        try:
            with open(full_path, 'rb') as f:
                data = from_yaml(f.read(), file_name=full_path)
        except AnsibleParserError as e:
            display("%s: %s" % (full_path, str(e)), display_failures)
           

# Generated at 2022-06-13 07:19:57.739905
# Unit test for function from_yaml
def test_from_yaml():
    # Happy path
    _from_yaml = from_yaml('''{
                             "foo": "bar",
                             "baz": null
                             }''')
    assert _from_yaml == {'foo': 'bar', 'baz': None}

    # Invalid yaml
    try:
        from_yaml('{')
    except AnsibleParserError:
        pass
    except Exception as e:
        assert False, "AnsibleParserError not raised, instead {}".format(e)

    # Invalid JSON
    try:
        from_yaml('{')
    except AnsibleParserError:
        pass
    except Exception as e:
        assert False, "AnsibleParserError not raised, instead {}".format(e)

from ansible.parsing.yaml.dumper import AnsibleD

# Generated at 2022-06-13 07:20:04.650508
# Unit test for function from_yaml
def test_from_yaml():
    assert not from_yaml('')
    assert not from_yaml('{"a": "b"}')
    assert not from_yaml('{a: b}')
    try:
        from_yaml('{a: b}', json_only=True)
    except AnsibleParserError:
        pass
    else:
        assert False, 'AnsibleParserError not raised'

# Generated at 2022-06-13 07:20:11.580061
# Unit test for function from_yaml
def test_from_yaml():
    # basic test
    data = """
    foo:Hello
    bar:World
    """
    result = {u'foo': u'Hello', u'bar': u'World'}
    assert result == from_yaml(data)

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:20:13.395953
# Unit test for function from_yaml
def test_from_yaml():
    data = '[{"abc": "xyz"}]'
    assert json.loads(data) == from_yaml(data)

# Generated at 2022-06-13 07:20:24.055194
# Unit test for function from_yaml
def test_from_yaml():
    print("Testing ansible.parsing.yaml.objects.from_yaml()")
    yaml = """
        ---
        {
          "array": [
            1,
            2,
            3
          ],
          "boolean": true,
          "color": "#82b92c",
          "null": null,
          "number": 123,
          "object": {
            "a": "b",
            "c": "d",
            "e": "f",
            "false": false,
            "true": true
          },
          "string": "Hello World"
        }
    """

# Generated at 2022-06-13 07:20:25.704344
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{}') == {}



# Generated at 2022-06-13 07:20:36.855024
# Unit test for function from_yaml
def test_from_yaml():
    """This unit test is intended to be run via nose."""
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils.six import string_types

    class TestYAMLObject(AnsibleBaseYAMLObject):
        def __init__(self, backend, data):
            AnsibleBaseYAMLObject.__init__(self, backend, data)
            self.ansible_pos = (u'<unicode>', 1, 0)

    class TestYAMLUnicode(AnsibleUnicode):
        def __init__(self, data):
            AnsibleUnicode.__init__(self, data)
            self.ansible_pos = (u'<unicode>', 1, 0)


# Generated at 2022-06-13 07:20:45.830405
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"foo\": \"bar\"}", json_only=True) == {"foo": "bar"}
    assert from_yaml("foo: bar") == {"foo": "bar"}
    assert from_yaml("foo: bar\n") == {"foo": "bar"}
    assert from_yaml("[\"foo\", \"bar\", \"baz\"]", json_only=True) == ["foo", "bar", "baz"]
    assert from_yaml("[foo, bar, baz]") == ["foo", "bar", "baz"]
    assert from_yaml("[foo, bar, baz]\n") == ["foo", "bar", "baz"]

# Generated at 2022-06-13 07:20:55.219420
# Unit test for function from_yaml

# Generated at 2022-06-13 07:21:07.907298
# Unit test for function from_yaml
def test_from_yaml():
    # First, test parsing a valid JSON string
    test_string1 = '{"a": ["foo", "bar", "baz"], "b": {"c": "d", "e": "f"}}'
    expected_result1 = {u'a': [u'foo', u'bar', u'baz'], u'b': {u'c': u'd', u'e': u'f'}}
    assert from_yaml(test_string1) == expected_result1

    # Test parsing a valid YAML string
    test_string2 = '''
    a:
      - foo
      - bar
      - baz
    b:
      c: d
      e: f
    '''

# Generated at 2022-06-13 07:21:13.819277
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoaderError

    # Test No Error
    yaml_str = 'devices: [a,b,c]'
    assert from_yaml(yaml_str) == {'devices': ['a','b','c']}

    # Test Raise Error
    yaml_str = 'devices: [...'
    try:
        from_yaml(yaml_str)
    except AnsibleLoaderError as e:
        assert e.orig_exc


# Generated at 2022-06-13 07:21:21.733255
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "foo": "bar" }') == {"foo":"bar"}
    assert from_yaml('{ "foo": "bar"', '<string>') == {"foo":"bar"}
    assert from_yaml('"foo"') == "foo"
    assert from_yaml('#foo') == "#foo"
    assert from_yaml('{ foo: "bar" }') == {"foo":"bar"}

    try:
        from_yaml('Test')
        assert False, "from_yaml did not fail when it should have"
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:21:37.371762
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    if sys.version_info[0:2] == (3, 4):
        # we have to skip this test on python 3.4 as it fails due to
        # a bug in the built-in yaml parser
        return

    import tempfile

    from ansible.parsing.yaml.loader import AnsibleUnicode

    # We also want to be able to test the type of object returned by from_yaml
    # with bytes input. So test that when a unicode string is returned, and the
    # input was an encoded to bytes (unicode on py2), the result is of type
    # AnsibleUnicode.
    def get_yaml_obj(data):
        fd, path = tempfile.mkstemp()
        tmpf = os.fdopen(fd, "w")

# Generated at 2022-06-13 07:21:44.244318
# Unit test for function from_yaml
def test_from_yaml():
    ''' Test case for function from_yaml()'''
    new_data = from_yaml("""---
- name: test_from_yaml
  hosts: localhost
  tasks:
  - ping:
      data: flow
    """, file_name="<test>", show_content=True, vault_secrets=None, json_only=False)

    assert new_data[0]['name'] == 'test_from_yaml',\
    'from_yaml() did not return expected value for name'
    assert new_data[0]['hosts'] == 'localhost',\
    'from_yaml() did not return expected value for hosts'


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:53.805221
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3
    data = '{"a": 1, "b": 2}'
    obj = from_yaml(data)
    assert obj.get('a') == 1
    assert obj.get('b') == 2
    if PY3:
        assert isinstance(obj['a'], int)
        assert isinstance(obj['b'], int)
    else:
        assert isinstance(obj['a'], long)
        assert isinstance(obj['b'], long)
    data = '''{
      "a": 1,
      "b": 2
}'''
    obj = from_yaml(data)
    assert obj.get('a') == 1
    assert obj.get('b') == 2

# Generated at 2022-06-13 07:22:04.856372
# Unit test for function from_yaml

# Generated at 2022-06-13 07:22:12.796854
# Unit test for function from_yaml
def test_from_yaml():
    # Test valid json
    json_data = '{"a": "b", "c": "d"}'
    assert from_yaml(json_data) == {"a": "b", "c": "d"}

    # Test valid yaml
    yaml_data = '---\na: b\nc: d\n'
    assert from_yaml(yaml_data) == {"a": "b", "c": "d"}

    # Test valid json with vault

# Generated at 2022-06-13 07:22:25.676251
# Unit test for function from_yaml
def test_from_yaml():

    from datetime import datetime
    from decimal import Decimal
    from ansible.parsing.ajson import AnsibleJSONEncoder

    # create a pretty complex object

# Generated at 2022-06-13 07:22:31.215722
# Unit test for function from_yaml
def test_from_yaml():
    test_data = """
---
hello: world
key:
  - a
  - b
"""
    yaml_data = from_yaml(test_data)
    assert yaml_data == {"hello": "world", "key": ["a", "b"]}

# Generated at 2022-06-13 07:22:44.666787
# Unit test for function from_yaml
def test_from_yaml():

    data = '{"test": "value"}'
    assert from_yaml(data, json_only=True) == {"test": "value"}

    data = '{"test": "value"}'
    assert from_yaml(data) == {"test": "value"}

    data = '{"test": "value"}'
    data = '---\n%s' % data
    assert from_yaml(data) == {"test": "value"}

    data = '{"test": "value"}'
    data = '---\n%s' % data
    assert from_yaml(data) == {"test": "value"}

    data = 'access_token: foo\n'
    data = '---\n%s' % data
    assert from_yaml(data) == {"access_token": "foo"}


# Generated at 2022-06-13 07:22:56.299959
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml
    ansible.parsing.yaml.AnsibleBaseYAMLObject.ansible_pos = 'test'
    assert from_yaml(u'{ "test": "data" }') == { u'test': u'data' }
    assert from_yaml(u'{ "test": "data" }', json_only=True) == { u'test': u'data' }
    try:
        from_yaml(u'{ "test": "data" }', json_only=True)
    except AnsibleParserError:
        assert False, b"json_only=True should raise an error for yaml data"
    assert from_yaml(u'{ "test": "data" }', json_only=True) == { u'test': u'data' }

# Generated at 2022-06-13 07:23:05.963922
# Unit test for function from_yaml
def test_from_yaml():
    json_string1='[{"name": "test", "id": 1}, {"name": "test", "id": 2}]'
    yaml_string1='- {name: test, id: 1}\n- {name: test, id: 2}'
    expected_result1=json.loads(json_string1)
    assert expected_result1==from_yaml(json_string1)
    assert expected_result1==from_yaml(yaml_string1)

    json_string2="{\"a\": 1, \"b\": 2, \"c\": {\"a\": 10, \"b\": 20}, \"d\": [1, 2, 3, 4]}"
    yaml_string2="a: 1\nb: 2\nc:\n  a: 10\n  b: 20\nd: [1, 2, 3, 4]"

# Generated at 2022-06-13 07:23:16.088093
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    def _get_from_yaml(yaml_data):
        return from_yaml(yaml_data)

    # from_yaml should accept a string and return a dictionary.
    assert _get_from_yaml("'foo'") == {'foo': None}
    assert _get_from_yaml("foo") == {'foo': None}
    assert _get_from_yaml("['foo', 'bar']") == {'foo': ['foo', 'bar']}
    assert _get_from_yaml("foo: bar") == {'foo': 'bar'}
    assert _get_from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    # from_yaml should return an empty dictionary

# Generated at 2022-06-13 07:23:26.284353
# Unit test for function from_yaml
def test_from_yaml():
    from datetime import date
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml import objects


# Generated at 2022-06-13 07:23:31.968509
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml({'foo': 'bar'}) == {"foo": "bar"}
    assert from_yaml('[1,2,3]') == [1, 2, 3]
    assert from_yaml([1, 2, 3]) == [1, 2, 3]
    assert from_yaml('yaml: not yaml') == 'yaml: not yaml'
    assert from_yaml('{"foo": "{{ 3 + 3 }}"}') == {"foo": "3 + 3"}
    assert from_yaml('{"foo": "{{ 3 + 3 }}"}', json_only=True) == {"foo": "{{ 3 + 3 }}"}

# Generated at 2022-06-13 07:23:43.628363
# Unit test for function from_yaml
def test_from_yaml():
    import sys, os, json
    try:
        import test.support
        import test.support.script_helper
        import test.support.import_helper
    except ImportError:
        from test import support

# Generated at 2022-06-13 07:23:55.272803
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Run unit test for the function _from_yaml
    '''

    def run_test(data, file_name, expected, show_content, vault_secrets, json_only, exception_expected=False):
        '''
        Run a single unit test
        '''
        test_passed = False
        new_data = None

        try:
            new_data = from_yaml(data, file_name, show_content, vault_secrets, json_only)
            test_passed = (new_data == expected)
        except Exception as e:
            test_passed = exception_expected
            new_data = e


# Generated at 2022-06-13 07:24:05.530536
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import six

    def _get_vault_secret():
        ''' Creates a VaultSecret object with the specified password '''
        from ansible.parsing.vault import VaultSecret
        return VaultSecret('secret')

    def _run_test(value, expected, expected_tb, vault_secrets=None, json_only=False):
        try:
            result = from_yaml(to_text(value), vault_secrets=vault_secrets, json_only=json_only)
        except AnsibleParserError as e:
            assert expected is None
            assert expected_tb == str(e)
        else:
            assert result == expected


# Generated at 2022-06-13 07:24:16.589849
# Unit test for function from_yaml
def test_from_yaml():
    import os

    # Get test directory
    test_dir = os.path.dirname(os.path.abspath(__file__))

    # Get test data
    test_data = os.path.join(test_dir, 'test_data/test_from_yaml.txt')

    # Get shared code directory
    shared_code_dir = os.path.join(test_dir, 'shared_code')

    # Unit test for from_yaml when file_name is specified
    def from_yaml_test_file_name():
        data = '''
        ---
        - foo
        - bar
        '''

        with open(test_data, 'w+') as outfile:
            outfile.write(data)

        # Generate test result

# Generated at 2022-06-13 07:24:23.814934
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

    expected = [1, 2, 3]
    yaml = '---\n- 1\n- 2\n- 3\n'
    assert from_yaml(yaml) == expected
    assert from_yaml(yaml, json_only=True) == expected
    assert from_yaml(yaml, json_only=True) == expected
    assert from_yaml(yaml, json_only=True) == expected

    assert from_yaml(yaml, json_only=True) == expected
    assert from_yaml(yaml, json_only=True, vault_secrets=['test']) == expected


# Generated at 2022-06-13 07:24:33.918042
# Unit test for function from_yaml
def test_from_yaml():

    json_string = '''
    {
        "key1": "value1",
        "key2": "value2",
    }
    '''

    yaml_string = '''
    key1: value1
    key2: value2
    '''

    try:
        assert from_yaml(json_string) == {'key1': 'value1', 'key2': 'value2'}
    except:
        raise AssertionError('from_yaml function failed for valid json string')

    try:
        assert from_yaml(yaml_string) == {'key1': 'value1', 'key2': 'value2'}
    except:
        raise AssertionError('from_yaml function failed for valid yaml string')



# Generated at 2022-06-13 07:24:40.284138
# Unit test for function from_yaml
def test_from_yaml():
    v = {}
    assert False == from_yaml("{", file_name="<string>", show_content=True, vault_secrets=None, json_only=False)
    assert False == from_yaml("", file_name="<string>", show_content=True, vault_secrets=None, json_only=False)
    assert False == from_yaml("{}", file_name="<string>", show_content=True, vault_secrets=None, json_only=False)
    assert False == from_yaml("{", file_name="<string>", show_content=True, vault_secrets=None, json_only=False)
    assert False == from_yaml("/", file_name="<string>", show_content=True, vault_secrets=None, json_only=False)

# Generated at 2022-06-13 07:24:51.617932
# Unit test for function from_yaml
def test_from_yaml():
    # Test for missing vars in vault
    import os
    import sys
    env_bup = os.environ.get('ANSIBLE_VAULT_PASSWORD_FILE')
    os.environ['ANSIBLE_VAULT_PASSWORD_FILE'] = '/tmp/ansible-vault'

# Generated at 2022-06-13 07:25:01.901961
# Unit test for function from_yaml

# Generated at 2022-06-13 07:25:06.799446
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[1,2,3]') == [1, 2, 3]
    assert from_yaml('foo: bar\nbaz:')

    # should error out and return None
    try:
        from_yaml('foo')
    except AnsibleParserError:
        pass
    except:
        raise
    else:
        raise AssertionError('did not detect invalid YAML')

# Generated at 2022-06-13 07:25:15.112415
# Unit test for function from_yaml
def test_from_yaml():

    assert(from_yaml("") == None)

    assert(from_yaml("{}") == {})
    assert(from_yaml("{a: []}") == {"a": []})

    assert(from_yaml("{}", json_only=True) == {})
    assert(from_yaml("{a: []}", json_only=True) == {})

    try:
        from_yaml("[a: []")
        assert False
    except AnsibleParserError as e:
        assert(str(e).startswith("We were unable to read either as JSON nor YAML, these are the errors we got from each:"))
        assert(str(e).find("JSON:") != -1)
        assert(str(e).find("YAML:") != -1)


# Generated at 2022-06-13 07:25:23.213139
# Unit test for function from_yaml
def test_from_yaml():
    # This tests the 'from_yaml' function.
    # Complete
    assert from_yaml("{'data' : 'value'}") == {"data": "value"}
    assert from_yaml("'data'") == "data"
    assert from_yaml("- 'a'\n- 'b'") == ['a', 'b']
    assert from_yaml("a: b") == {'a': 'b'}
    assert from_yaml("- 1\n- 2") == [1, 2]
    assert from_yaml(unicode('- 1\n- 2')) == [1, 2]
    assert from_yaml("a: 1") == {'a': 1}
    assert from_yaml("- 1\n- 2") == [1, 2]

# Generated at 2022-06-13 07:25:31.878257
# Unit test for function from_yaml
def test_from_yaml():
    data1 = "---\n- hosts: all\n  tasks:\n    - name: Test\n      fail: msg='This is a test'"
    data2 = data1.replace("'", '"')
    data3 = data1.replace("fail:", "import_tasks:")
    data4 = "{\"ansible_ssh_user\": \"{{ variable }}, \"ansible_ssh_port\": \"22\"}"
    assert from_yaml(data1) == from_yaml(data2)
    assert from_yaml(data1) != from_yaml(data3)
    assert from_yaml(data1) != from_yaml(data4)

# Generated at 2022-06-13 07:25:41.523684
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    vanilla_yaml_file = C.DEFAULT_DATA_PATH + "/test_parser.yml"
    vanilla_yaml_str = """
    v1: data1
    v2: '{{path1}}'
    v3: '{{path2}}'
    """

    dl = DataLoader()

# Generated at 2022-06-13 07:25:55.539623
# Unit test for function from_yaml
def test_from_yaml():
    # Valid
    test_data = {
        "This is a dictionary": {},
        "This is an integer": 1,
        "This is a float": 2.1,
        "This is a list": [],
        "This is a string": "  "
    }

    for key, value in test_data.items():
        yaml_data = key + ": " + str(value)
        data = from_yaml(yaml_data)
        assert data == {key: value}

    # Invalid
    # All yaml spec invalid strings will fail from from_yaml function
    # See http://www.yaml.org/spec/1.2/spec.html for more info

    # A string that breaks the yaml spec
    data = '"this has\n a break"'

# Generated at 2022-06-13 07:26:07.983809
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "hello": "world" }') == {"hello": "world"}
    assert from_yaml('{"hello": "world"}') == {"hello": "world"}
    assert from_yaml('\n{ "hello": "world" }\n') == {"hello": "world"}

    # test errors
    try:
        from_yaml('{ "hello": "world" }\n{ "bad": "json" }')
        assert False
    except AnsibleParserError:
        assert True

    try:
        from_yaml('{ "hello": "world" \n')
        assert False
    except AnsibleParserError:
        assert True


# Generated at 2022-06-13 07:26:15.338837
# Unit test for function from_yaml
def test_from_yaml():
    content = """
  - name: Task name
    fail: msg="Trying to fail"
    when: ansible_os_family != "RedHat"
  - name: Task name
    shell: echo "success"
    when: ansible_os_family == "RedHat"
    """
    result = from_yaml(content)
    assert result == [{
        'name': 'Task name',
        'fail': {'msg': 'Trying to fail'},
        'when': 'ansible_os_family != "RedHat"'}, {
        'name': 'Task name',
        'shell': 'echo "success"',
        'when': 'ansible_os_family == "RedHat"'}]
    print(result)

# Generated at 2022-06-13 07:26:28.902657
# Unit test for function from_yaml
def test_from_yaml():
    def check_yaml(given, expected):
        actual = from_yaml(given)
        assert actual == expected

    def check_exception(given, expected):
        try:
            from_yaml(given)
            assert False, "expected exception"
        except AnsibleParserError as e:
            assert e.message == expected

    check_yaml("{\"foo\": \"bar\"}", {"foo": "bar"})
    check_yaml("{\"bar\": \"{{baz}}\"}",{"bar": "{{baz}}"})

    # These should fail to parse

# Generated at 2022-06-13 07:26:36.171244
# Unit test for function from_yaml
def test_from_yaml():
    # Check that AnsibleJSONDecoder works.  We'll skip the test failure if the
    # decoder isn't installed.
    try:
        from ansible.parsing.ajson import AnsibleJSONDecoder
    except ImportError:
        pass
    else:
        good_JSON = '{"dict": {"a": "b", "c": "d"}, "list": [1, 2, 3]}'
        bad_JSON = '{"dict": {"a": "b", "c: "d"}, "list": [1, 2, 3]'
        ansible_decoder = AnsibleJSONDecoder()
        assert ansible_decoder.decode(good_JSON) == json.loads(good_JSON)
        try:
            ansible_decoder.decode(bad_JSON)
        except ValueError as e:
            assert e

# Generated at 2022-06-13 07:26:47.820769
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Ensure that AnsisbleParserError is raised when an error occurs
    and also ensure AnsibleParserError is not raised when there are no errors.
    '''
    # Raise AnsibleParserError if 'test' is YAML compatible file
    test = "test"
    try:
        from_yaml(test, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    except AnsibleParserError:
        pass
    # Should not raise AnsibleParserError if 'test' is not YAML compatible file
    test = {"test": "test"}
    try:
        from_yaml(test, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    except AnsibleParserError:
        assert False

# Generated at 2022-06-13 07:26:59.625604
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    # This class uses the unittest.TestCase class for setup, etc.
    class TestFromYAML(unittest.TestCase):

        # Testing from_yaml function

        # Test that from_yaml can read a file
        def test_from_yaml_file(self):
            data = from_yaml("---\n- 'hello world'", show_content=False)
            self.assertEqual(data[0], 'hello world')

        # Test that from_yaml can read JSON
        def test_from_yaml_json(self):
            data = from_yaml("[\"Hello world\"]", show_content=False)
            self.assertEqual(data[0], 'Hello world')

        # Test that YAMLError gets raise on some known wrong formating.

# Generated at 2022-06-13 07:27:10.984906
# Unit test for function from_yaml
def test_from_yaml():
    json_data = '{"a": "b", "c": "d"}'
    assert from_yaml(json_data) == json.loads(json_data)
    json_data = '[{"a": "b", "c": "d"}, {"a": "b", "c": "d"}]'
    assert from_yaml(json_data) == json.loads(json_data)
    json_data = '{"a": "b", "c": "d", "e": {"a": "b", "c": "d"}}'
    assert from_yaml(json_data) == json.loads(json_data)

    yaml_data = """
- a: b
  c: d
- a: b
  c: d
"""

# Generated at 2022-06-13 07:27:17.988006
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    data = dl.load_from_file('tests/yaml_data/from_yaml_test.yaml')
    print(data)
    data = dl.load_from_file('tests/yaml_data/from_yaml_test.json')
    print(data)


# Generated at 2022-06-13 07:27:28.808712
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('123') == 123
    assert from_yaml('[1,2,3]') == [1,2,3]
    assert from_yaml('{"k":"v"}') == {'k':'v'}
    assert from_yaml('{"k":"v"}', json_only=True) == {'k':'v'}
    # YAML file START
    assert from_yaml('''
foo:
  bar: world
  baz: hello
''') == {'foo': {'bar': 'world', 'baz': 'hello'}}
    assert from_yaml('''
foo:
  bar: world
  baz: hello
''') == {'foo': {'bar': 'world', 'baz': 'hello'}}
    # YAML file END