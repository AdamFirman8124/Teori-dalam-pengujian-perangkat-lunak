

# Generated at 2022-06-13 07:17:36.765022
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.ajson import AnsibleJSONEncoder
    import json
    import sys

    def _assert_from_yaml(data, expected, vault_secrets=None):
        file_name = 'test_from_yaml'
        result = from_yaml(data, file_name=file_name, vault_secrets=vault_secrets)
        if result != expected:
            # Note: Single-quoted JSON is printed to make the diff between YAML and JSON more obvious.
            print('\n%-10s: %-30s: %s' % (result, 'expected', json.dumps(expected, cls=AnsibleJSONEncoder, sort_keys=True)))
            sys.exit(1)


# Generated at 2022-06-13 07:17:46.392441
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    from ansible.parsing.ajson import AnsibleJSONDecoder

    assert from_yaml('{}') == {}
    assert from_yaml('true')
    assert from_yaml('false') is False
    assert from_yaml('[{}, {}]') == [{}, {}]
    assert from_yaml('["foo", "bar"]') == ["foo", "bar"]

    assert from_yaml('{"key": "value"}') == {"key": "value"}

# Generated at 2022-06-13 07:17:50.690902
# Unit test for function from_yaml
def test_from_yaml():
    print("Testing from_yaml")
    # Test if yaml is being properly passed as a dict as expected
    from_yaml("num: 1", json_only=True)
    # Test if json is being properly passed as a dict as expected
    from_yaml("{\"num\": 1}", json_only=True)

# Generated at 2022-06-13 07:17:57.396657
# Unit test for function from_yaml
def test_from_yaml():
    # tests that unicode is handled correctly
    data = u'{"a": "\u2654"}'
    assert from_yaml(data, json_only=True) == {u"a": u"\u2654"}

    data = '{"a": "\u2654"}'
    assert from_yaml(data, json_only=True) == {u"a": u"\u2654"}


if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:18:03.584067
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This function tests the from_yaml function from parsing\yaml\__init__.py
    '''
    # Test 1
    # Test with invalid yaml data
    # define some invalid yaml data
    data = [{'name': 'package',
             'state': 'present',
             'package': 'httpd',
             'update_cache': 'yes'
             }]
    try:
        test = from_yaml(data)
    # check if exception is raised
    except Exception as e:
        assert isinstance(e, YAMLError)

    # Test 2
    # Test with valid yaml data
    # define some valid yaml data
    data = [{'name': 'httpd',
            'action': 'asdf'
            }]
    test = from_yaml(data)

# Generated at 2022-06-13 07:18:13.717655
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, dir) # python search directory
    if __name__ == "__main__":
        import test
    else:
        from test import *

    # test case: 1
    # file: yaml_test.yml
    # test case: 1.1 Util test_from_yaml 
    # yaml string:

# Generated at 2022-06-13 07:18:24.038609
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{\"a\": 1, \"b\": 2}") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\nb: 2") == {"a": 1, "b": 2}
    assert from_yaml("a: 1\n") == {"a": 1}
    assert from_yaml("a: 1\n---\nb: 2") == [{"a": 1}, {"b": 2}]
    assert from_yaml("a: 1\n---\n- b: 2") == {"a": 1, "- b": 2}
    assert from_yaml("a: 1\n---\n---\nb: 2") == [{"a": 1}, {"b": 2}]

# Generated at 2022-06-13 07:18:30.597690
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Verify that from_yaml returns the correct data structure for each of
    the provided test vectors.
    '''

# Generated at 2022-06-13 07:18:37.945432
# Unit test for function from_yaml
def test_from_yaml():
    # Test basic load
    assert '"name": "value"' == to_native(json.dumps(from_yaml('name: value')))
    assert '"key": "value"' == to_native(json.dumps(from_yaml('{"key": "value"}')))

    # Test json_only=True
    try:
        from_yaml('name: value', json_only=True)
        raise AssertionError('Should fail')
    except AnsibleParserError:
        pass
    # Test that json_only=True still allows JSON
    assert '"name": "value"' == to_native(json.dumps(from_yaml('{"name": "value"}', json_only=True)))

    # Test per-vault secret

# Generated at 2022-06-13 07:18:45.001290
# Unit test for function from_yaml
def test_from_yaml():
    # 1. test for invalid json syntax
    data = '{"a":1 "b":2}'
    try:
        from_yaml(data)
    except AnsibleParserError as parser_err:
        assert parser_err.message[:10] == 'We were una'
        assert parser_err.message[-15:] == 'from each:\n'

    #  2. test for invalid yaml syntax
    data = "{a:1, b:2}"
    try:
        from_yaml(data)
    except AnsibleParserError as parser_err:
        assert parser_err.message[:10] == 'We were una'
        assert parser_err.message[-15:] == 'from each:\n'

    # 3. test for empty string
    assert from_yaml('') == {}

    #

# Generated at 2022-06-13 07:18:57.162623
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"7": [0, 1, "a"], "6": {"a": "b", "c": "d"}}'
    new_data = from_yaml(data)
    assert new_data == json.loads(data)

    data = '{"7": [0, 1, "a"], "6": {"a": "b", "c": "d"}}'
    new_data = from_yaml(data, show_content=False)
    assert new_data == json.loads(data)

    data = '{"7": [0, 1, "a"], "6": {"a": "b", "c": "d"'

# Generated at 2022-06-13 07:19:06.806059
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('key1: [1,2]\n') == {u'key1': [1, 2]}
    assert from_yaml('key1: {key2: 1}\n') == {u'key1': {u'key2': 1}}
    assert from_yaml('key1: {key2: 1}\n', json_only=True) is None


# Generated at 2022-06-13 07:19:18.815575
# Unit test for function from_yaml
def test_from_yaml():
    # data:
    #   a: 1
    #   b: 2
    #   c: 3
    #   d: 4
    #   e: 5
    #   f: 6
    #   g: 7
    #   h: 8
    #   i: 9
    #   j: 10
    data_yaml_1 = """
        data:
          a: 1
          b: 2
          c: 3
          d: 4
          e: 5
          f: 6
          g: 7
          h: 8
          i: 9
          j: 10
    """

    # {"data": {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}}
   

# Generated at 2022-06-13 07:19:20.373424
# Unit test for function from_yaml
def test_from_yaml():
    # TODO: write unit test for from_yaml
    pass

# Generated at 2022-06-13 07:19:27.569575
# Unit test for function from_yaml
def test_from_yaml():
    d = from_yaml('{ "a": "b" }')
    assert d["a"] == "b"

    d = from_yaml('a: b')
    assert d["a"] == "b"

    d = from_yaml('{ "a": "b", "c": "d"}')
    assert d["a"] == "b"
    assert d["c"] == "d"

    d = from_yaml('a: b\nc: d')
    assert d["a"] == "b"
    assert d["c"] == "d"

# Generated at 2022-06-13 07:19:28.432385
# Unit test for function from_yaml
def test_from_yaml():
    assert None == from_yaml(None)
    assert 1 == from_yaml('1')



# Generated at 2022-06-13 07:19:30.147883
# Unit test for function from_yaml
def test_from_yaml():
    """
    This function is not intended to be run as a unit test. Instead, it is
    a placeholder for unit tests to be added in the future.
    """

# Generated at 2022-06-13 07:19:34.437335
# Unit test for function from_yaml
def test_from_yaml():
    data1 = {"name":"John", "age":3, "class": "kindergarten"}
    data2 = "{\"name\":\"John\", \"age\":3, \"class\": \"kindergarten\"}"
    data3 = '''
    name: John
    age: 3
    class: kindergarten
    '''
    assert from_yaml(data1) == from_yaml(data2)
    assert from_yaml(data1) == from_yaml(data3)

test_from_yaml()

# Generated at 2022-06-13 07:19:46.137011
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import tempfile
    import shutil
    from ansible.modules.extras.test.vmware import VMwareObject


# Generated at 2022-06-13 07:19:55.309473
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    import types
    # ensure safe_load produces an AnsibleSequence
    test_data = AnsibleSequence()
    test_data.append(AnsibleMapping())
    test_data[0]['test0'] = '0'
    test_data[0]['test1'] = '1'

# Generated at 2022-06-13 07:20:10.408886
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test for function from_yaml
    '''
    data_yaml = "---\n- {a: 1, b: 2}\n- {a: 3, b: 4}\n"
    data_json = "[ {\"a\": 1, \"b\": 2}, {\"a\": 3, \"b\": 4} ]"
    data_mixed = "{a: 1, b: 2}\n"
    data_bad = "!@#$%^&"
    assert from_yaml(data_yaml, json_only=False) == [{u'a': 1, u'b': 2}, {u'a': 3, u'b': 4}]

# Generated at 2022-06-13 07:20:21.102978
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""{
        "foo": 1,
        "bar": 2,
        "baz": {
            "spam": 3,
            "eggs": 4
        }
    }""") == dict(foo=1, bar=2, baz=dict(spam=3, eggs=4))

    assert from_yaml(u"""{
        "foo": 1,
        "bar": 2,
        "baz": {
            "spam": 3,
            "eggs": 4
        }
    }""") == dict(foo=1, bar=2, baz=dict(spam=3, eggs=4))


# Generated at 2022-06-13 07:20:31.896905
# Unit test for function from_yaml
def test_from_yaml():

    # Test loading YAML
    data = "foo: bar"
    assert from_yaml(data) == {'foo': 'bar'}

    # Test loading JSON
    data = json.dumps({'json': 'test'})
    assert from_yaml(data) == {'json': 'test'}

    # Test YAML error reporting
    data = "foo"
    from_yaml_error = False
    try:
        from_yaml(data, json_only=True)
    except AnsibleParserError as e:
        from_yaml_error = e
    assert from_yaml_error.__class__.__name__ == 'AnsibleParserError'

    # Test JSON error reporting
    data = "foo"
    from_yaml_error = False

# Generated at 2022-06-13 07:20:37.868858
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"a":  "b"}'
    # Test with vault_secrets
    vault_secrets = 'vault_secrets'
    new_data = from_yaml(data, vault_secrets=vault_secrets)
    assert new_data == {"a":  "b"}
    # Test without vault_secrets
    new_data = from_yaml(data)
    assert new_data == {"a":  "b"}

# Generated at 2022-06-13 07:20:48.399126
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""{
        "foo" : {
            "bar" : {
                "baz" : 1
            }
        }
    }""") == {"foo": {"bar": {"baz": 1}}}
    assert from_yaml("""
        foo :
          bar :
            baz : 1""") == {"foo": {"bar": {"baz": 1}}}
    assert from_yaml("""
        foo:
          bar:
            baz: 1""") == {"foo": {"bar": {"baz": 1}}}
    assert from_yaml("""
        foo: {
          bar: {
            baz: 1
          }
        }""") == {"foo": {"bar": {"baz": 1}}}

# Generated at 2022-06-13 07:20:56.350664
# Unit test for function from_yaml
def test_from_yaml():
    # Test for JSON string
    object_from_yaml = from_yaml('{"test": "json"}')
    assert object_from_yaml["test"] == "json"

    # Test for YAML string
    object_from_yaml = from_yaml('test: yaml')
    assert object_from_yaml["test"] == "yaml"

    # Test for JSON string with a vault
    object_from_yaml = from_yaml('{"test": "json", "test2": "test3: test4"}', vault_secrets='some')
    assert object_from_yaml["test"] == "json"
    assert object_from_yaml["test2"] == {"test3": "test4"}

# Generated at 2022-06-13 07:21:00.920592
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("'foo'") == 'foo'
    assert from_yaml("bar") == 'bar'
    assert from_yaml("[1, 2, 3]") == [1, 2, 3]
    assert from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    assert from_yaml("""
        ---
        - hosts: localhost
          tasks:
          - debug:
              msg: 'Hello World!'
        ...
        """) == [{'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'Hello World!'}}]}]

# Generated at 2022-06-13 07:21:11.602106
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.dataloader import DataLoader
    ansible_loader = DataLoader()
    yaml_loader = AnsibleLoader(None)
    with open("test_data.yml", 'r') as stream:
        data = yaml_loader.get_single_data(stream)
        #print(ansible_loader.load(data))
    assert(ansible_loader.load(data) is not None)


# Generated at 2022-06-13 07:21:14.165901
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('--- foo') == 'foo'
    assert from_yaml('--- 1') == 1
    assert from_yaml('--- true') is True


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:23.174429
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    import unittest
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(FILE_DIR, '../../'))

    from ansible.utils.vars import combine_vars
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedString
    from ansible.parsing.yaml.quoting import unquote


# Generated at 2022-06-13 07:21:32.489612
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '{"foo": "bar"}'
    yaml_str = 'foo: bar\n'
    json_result = from_yaml(json_str)
    assert json_result['foo'] == 'bar'
    yaml_result = from_yaml(yaml_str)
    assert yaml_result['foo'] == 'bar'
    both_result = from_yaml(json_str)
    assert both_result['foo'] == 'bar'
    both_result = from_yaml(yaml_str)
    assert both_result['foo'] == 'bar'

    # unit test for exception handling
    both_str = '["foo":"bar", "baz":"qux"]'
    try:
        both_result = from_yaml(both_str)
    except:
        pass
   

# Generated at 2022-06-13 07:21:37.876385
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from_yaml_data = from_yaml("{'a': 'b'}")
    assert isinstance(from_yaml_data, dict)
    assert isinstance(from_yaml_data['a'], AnsibleUnsafeText)
    assert from_yaml_data == {'a': 'b'}

# Generated at 2022-06-13 07:21:45.145106
# Unit test for function from_yaml
def test_from_yaml():
    test_string = "world"
    ansible_dict = {'hello': 'world'}

    # Test with no vault_secrets
    assert from_yaml(json.dumps(ansible_dict)) == ansible_dict

    vault_secrets = [
        ('default', ['my_secret'])
    ]

    # Test with vault_secrets
    assert from_yaml(json.dumps(ansible_dict), vault_secrets=vault_secrets) == ansible_dict

    # Test with vault_secrets and yaml

# Generated at 2022-06-13 07:21:54.516897
# Unit test for function from_yaml
def test_from_yaml():
    import os

    filename = "test.dict"
    filepath = str(os.path.dirname(os.path.realpath(__file__)) + "/" + filename)
    data = [
        "a: test",
        "b: test",
        "c: test"
    ]
    with open(filepath, "w") as fh:
        fh.write('%s' % "\n".join(data))

# Generated at 2022-06-13 07:21:57.860225
# Unit test for function from_yaml
def test_from_yaml():
    result = from_yaml('{"foo": 42}')
    assert result['foo'] == 42

    result = from_yaml('foo: 42')
    assert result['foo'] == 42

# Generated at 2022-06-13 07:22:03.294244
# Unit test for function from_yaml
def test_from_yaml():
    yaml_string = '''
    - name: inventory-test
      host: "localhost"
      tasks:
        - debug: 
            msg: "Hello"
        - debug: 
            msg: "Test"
    '''    
    data = from_yaml(yaml_string)
    assert data is not None

# Generated at 2022-06-13 07:22:11.921898
# Unit test for function from_yaml
def test_from_yaml():
    # From the AnsiblePlaybookYAML1
    data = "a: 1"
    assert from_yaml(data) == {"a": 1}

    # From the AnsiblePlaybookYAML2
    data = """
    - hosts:
      remote_user: root
      tasks:
        - name: change hostname
          command: hostname {{new_hostname}}
          args:
            creates: /etc/debian_version
        - name: ensure packages are installed
          apt:
            name:
              - apache2
              - memcached
            state: present
    """

# Generated at 2022-06-13 07:22:19.692097
# Unit test for function from_yaml
def test_from_yaml():
    result = from_yaml('{"name": "myvar"}')
    assert result == {"name": "myvar"}

    result = from_yaml('{"name": "myvar"')
    assert result == {"name": "myvar"}

    result = from_yaml('{"name": "myvar", "version": "1.0.0"')
    assert result == {"name": "myvar", "version": "1.0.0"}

# Generated at 2022-06-13 07:22:28.565680
# Unit test for function from_yaml
def test_from_yaml():
    # Test the JSON parsing
    result = from_yaml('{"key1": "value1", "key2": "value2"}')
    assert result == {"key1": "value1", "key2": "value2"}

    # Test basic YAML parsing
    result = from_yaml('key1: value1\nkey2: value2')
    assert result == {"key1": "value1", "key2": "value2"}

    # When both JSON and YAML input are invalid, the parser should prefer to raise JSON exception
    json_exc = json.decoder.JSONDecodeError('Expecting value', ('<unicode string>', 1, 0, '"'))

# Generated at 2022-06-13 07:22:30.252204
# Unit test for function from_yaml
def test_from_yaml():
    pass

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:37.845131
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
- - - first
      second
      third
  - fourth
  - fifth
'''

    assert len(from_yaml(data)) == 3

# Generated at 2022-06-13 07:22:47.207325
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    # Test YAML
    data_yaml = """
    - hosts: all
      tasks:
        - user:
            name: test_user
            state: present
            groups:
              - test_group1
              - test_group2
              - test_group3
    """
    result = from_yaml(data_yaml)
    assert len(result) == 1
    assert result[0]['hosts'] == 'all'
    assert result[0]['tasks'][0]['user']['name'] == 'test_user'
    assert result[0]['tasks'][0]['user']['state'] == 'present'

# Generated at 2022-06-13 07:22:58.828104
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib

    def test_from_yaml_original(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False):
        new_data = None

        try:
            # in case we have to deal with vaults
            AnsibleJSONDecoder.set_secrets(vault_secrets)
            # we first try to load this data as JSON.
            # Fixes issues with extra vars json strings not being parsed correctly by the yaml parser
            new_data = json.loads(data, cls=AnsibleJSONDecoder)
        except Exception as json_exc:

            if json_only:
                raise AnsibleParserError(to_native(json_exc), orig_exc=json_exc)

            # must not be JSON

# Generated at 2022-06-13 07:23:05.769247
# Unit test for function from_yaml
def test_from_yaml():
    d = from_yaml("""
    foo:
      - hosts:
          - localhost
        gather_facts: no
        tasks:
          - name: 1
            debug: msg="1"
          - name: 2
            debug: msg="2"
    """)
    assert d == {'foo': [{'tasks': [{'debug': {'msg': '1'}, 'name': '1'},
                                   {'debug': {'msg': '2'}, 'name': '2'}],
                    'gather_facts': 'no', 'hosts': ['localhost']}]}

# Generated at 2022-06-13 07:23:09.418917
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": ["b", "c"], "d": "e"}') == {"a": ["b", "c"], "d": "e"}
    assert from_yaml("a: [b, c]\nd: e") == {"a": ["b", "c"], "d": "e"}
    assert from_yaml("a: [b, c]\nd: e\n") == {"a": ["b", "c"], "d": "e"}

# Generated at 2022-06-13 07:23:14.240932
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test our from_yaml() function.
    '''
    assert from_yaml('1') == 1
    assert from_yaml('{a: 1}') == {'a': 1}
    assert from_yaml('{a: 1}') == {'a': 1}
    assert from_yaml('a: 1') == {'a': 1}

# Generated at 2022-06-13 07:23:17.492638
# Unit test for function from_yaml
def test_from_yaml():
    ansible_yaml = ''' foo : ok
    bar:
    - 1
    - 2
    - 3
    '''
    decoded = from_yaml(ansible_yaml)
    assert decoded == { 'foo': 'ok', 'bar': [1, 2, 3] }, "from_yaml should return the correct decoded data."

# Generated at 2022-06-13 07:23:26.923398
# Unit test for function from_yaml
def test_from_yaml():
  yaml_text = "---\n- hosts: localhost\n  tasks: []\n"
  data = from_yaml(yaml_text) 
  print(data)
  assert data == [{'tasks': [], 'hosts': 'localhost'}]
  json_text = "{\"---\": [{\"hosts\": \"localhost\", \"tasks\": []}]}"
  data = from_yaml(json_text)
  print(data)
  assert data == [{'tasks': [], 'hosts': 'localhost'}]
  text = "{\"---\": [{\"- hosts\": \"localhost\n  tasks\": []\n\"}]}"
  print(text)
  data = from_yaml(text)
  print(data)

# Generated at 2022-06-13 07:23:37.170266
# Unit test for function from_yaml
def test_from_yaml():
    # Test with empty dict
    assert from_yaml("{}") == {}

    # Test with empty string
    assert from_yaml('""') == ""

    # Test simple string
    assert from_yaml('"test"') == "test"

    # Test with a non ansible enabled yaml
    yaml_string = """
    key: "value"
    """
    assert from_yaml(yaml_string) == {"key" : "value"}

    # Test with an empty list
    assert from_yaml('[]') == []

    # Test with a single item list
    assert from_yaml('[1]') == [1]

    # Test with a list
    assert from_yaml('[1,2,3]') == [1,2,3]

    # Test with a simple dictionary

# Generated at 2022-06-13 07:23:46.595348
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleSequence
    yaml_string = '''
# Example
name: foo
block:
  - hosts: all
    roles:
      - common
'''
    yaml_string_with_vault = '''
# Example
name: foo
vars_files:
  - vault.yml
block:
  - hosts: all
    roles:
      - common
'''
    data = from_yaml(to_bytes(yaml_string))
    assert data['name'] == 'foo'
    assert isinstance(data['block'], AnsibleSequence)
    assert data['block'][0]['hosts'] == 'all'

# Generated at 2022-06-13 07:23:57.271267
# Unit test for function from_yaml

# Generated at 2022-06-13 07:24:04.010787
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six.moves import StringIO

    # This was failing before due to a bug in the YAML parser.
    from_yaml("""
foo:
- hosts: localhost
  tasks:
  - name: test
    assert:
      that:
        - 1 == 1
        - "{{ foo }}" == "bar"
    with_items:
      - one
      - two
      - three
      - four
      - five
      - six
      - seven""")



# Generated at 2022-06-13 07:24:11.395367
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from collections import namedtuple

    MyTest = namedtuple('MyTest', ['name', 'data', 'expected', 'error'])
    tests = []

    # Test a typical YAML file
    name = 'test_from_yaml_0'
    data = """---
- hosts: foo
  gather_facts: true
  tasks:
  - name: test yaml parser
    debug: msg="hello world"
    """

# Generated at 2022-06-13 07:24:21.242933
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function ansible.parsing.yaml.from_yaml
    '''
    import os
    import sys

    TEST_DIR = os.path.join(os.path.dirname(__file__), 'testdata')

    # Test loading good YAML/JSON data
    yaml_data = open(os.path.join(TEST_DIR, 'test1.yaml')).read()
    json_data = open(os.path.join(TEST_DIR, 'test1.json')).read()

    from_yaml_data = from_yaml(yaml_data, 'test1.yaml')
    from_json_data = from_yaml(json_data, 'test1.json')

    assert from_yaml_data == from_json_data

    #

# Generated at 2022-06-13 07:24:27.564291
# Unit test for function from_yaml
def test_from_yaml():
    """
    In Case of YAML Exception, AnsibleParserError handles error message
    """
    try:
        from_yaml('{')
    except AnsibleParserError as e:
        assert "We were unable to read either as JSON nor YAML" in str(e)
        assert isinstance(e.orig_exc, YAMLError)



# Generated at 2022-06-13 07:24:36.461756
# Unit test for function from_yaml
def test_from_yaml():
    # Test scenario - try to load valid json string as json
    json_data = '{"key1":"val1", "key2":"val2"}'
    assert from_yaml(json_data) == {"key1": "val1", "key2": "val2"}
    # Test scenario - try to load valid json string as json and yaml
    assert from_yaml(json_data, json_only=False) == {"key1": "val1", "key2": "val2"}
    # Test scenario - try to load valid yaml string as yaml only
    yaml_data = 'key1: val1\nkey2: val2'
    assert from_yaml(yaml_data) == {"key1": "val1", "key2": "val2"}
    # Test scenario - try to load valid yaml string as json

# Generated at 2022-06-13 07:24:41.862901
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{}") == {}
    assert from_yaml("x: 1") == {"x": 1}
    assert from_yaml("x: \"{{ y }}\"") == {"x": "{{ y }}"}
    assert from_yaml("x: \"{{ foo.bar.baz }}\"") == {"x": "{{ foo.bar.baz }}"}
    assert from_yaml("x: \"{{ foo.bar.baz | d() }}\"") == {"x": "{{ foo.bar.baz | d() }}"}
    assert from_yaml("x: \"{{ foo.bar.baz | d('foo') }}\"") == {"x": "{{ foo.bar.baz | d('foo') }}"}

# Generated at 2022-06-13 07:24:43.272764
# Unit test for function from_yaml
def test_from_yaml():

    # TODO
    pass


# Generated at 2022-06-13 07:24:52.061214
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestFromYaml(unittest.TestCase):
        def test_from_yaml_vault_data(self):

            from ansible.parsing.vault import VaultLib
            from ansible.plugins.vars import BaseVarsPlugin

            vault = VaultLib(password=None)

# Generated at 2022-06-13 07:24:58.110313
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    assert from_yaml('{"test": "string"}') == {'test': 'string'}
    assert isinstance(from_yaml('''{
      "test": {
        "test": "string"
      },
      "test2": "string"
    }'''), AnsibleMapping)

# Generated at 2022-06-13 07:25:05.564538
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
test:
  - 7
  - 8
  - 9
'''

    data_load = from_yaml(data)
    assert isinstance(data_load, dict)
    assert len(data_load) == 1

# Generated at 2022-06-13 07:25:10.250848
# Unit test for function from_yaml
def test_from_yaml():
    fy = from_yaml
    fn = 'testing'

    def test_json():
        assert fy('{"a": "b"}', fn) == {'a': "b"}
        assert fy('{"a": "b"}', fn, json_only=True) == {'a': "b"}

    def test_var():
        assert fy('a: b', fn) == {'a': "b"}

    def test_combined():
        assert fy('a:\n  - b: c', fn) == {'a': [{'b': "c"}]}
        assert fy('{"a": [{"b": "c"}]}', fn) == {'a': [{'b': "c"}]}

# Generated at 2022-06-13 07:25:19.676000
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'key' : 'value'}") == {'key': 'value'}
    assert from_yaml("{'key' : 'value'}", json_only=True) == {'key': 'value'}
    assert from_yaml("{'key' : 'value'}") == from_yaml("{'key' : 'value'}")
    #assert from_yaml("{'key' : 'value'}", show_content=True) == from_yaml("{'key' : 'value'}", show_content=True)
    assert from_yaml("{'key' : 'value'}", show_content=True) == from_yaml("{'key' : 'value'}")
    #assert from_yaml("{'key' : 'value'}",

# Generated at 2022-06-13 07:25:26.470113
# Unit test for function from_yaml
def test_from_yaml():
    test_json_string = '{"foo":"bar"}'
    assert from_yaml(test_json_string) == {'foo': 'bar'}
    assert from_yaml(test_json_string, json_only=True) == {'foo': 'bar'}
    test_yaml_string = 'foo: bar'
    assert from_yaml(test_yaml_string) == {'foo': 'bar'}
    test_yaml_string = "foo: bar\n"
    assert from_yaml(test_yaml_string) == {'foo': 'bar'}
    test_yaml_string = 'foo: null'
    assert from_yaml(test_yaml_string) == {'foo': None}

# Generated at 2022-06-13 07:25:32.789419
# Unit test for function from_yaml
def test_from_yaml():
    d = '{"a": "b"}'
    assert from_yaml(d) == {'a':'b'}
    d = '{"a": "b", "c": "d", "e": "f"}'
    assert from_yaml(d) == {'a':'b', 'c':'d', 'e':'f'}
    d = '{"a": "b", "c": {"d": "e"}, "f": "g"}'
    assert from_yaml(d) == {'a':'b', 'c':{'d':'e'}, 'f':'g'}

# Generated at 2022-06-13 07:25:40.121875
# Unit test for function from_yaml
def test_from_yaml():

    # Test that data can be parsed as json
    print ("testing json")
    data = {
        'a': 1,
        'b': 2
    }
    assert from_yaml(json.dumps(data)) == data

    # Test that data can be parsed as yaml
    print ("testing yaml")
    data = '''
    a: 1
    b: 2
    '''
    assert from_yaml(data) == {'a': 1, 'b': 2}


if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:25:45.663831
# Unit test for function from_yaml
def test_from_yaml():
    # Test yaml
    yaml_data = '''
- hosts: localhost
  tasks:
  - debug: msg="hello world"
'''
    assert from_yaml(yaml_data) == [{'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'hello world'}}]}]
    assert from_yaml(yaml_data, vault_secrets=[{'secret': 's3cr3t', 'key': 's3cr3tkey'}], json_only=False) == [{'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'hello world', 'vault_secret_value': '5f4dcc3b5aa765d61d8327deb882cf99'}}]}]

# Generated at 2022-06-13 07:25:56.636086
# Unit test for function from_yaml
def test_from_yaml():

    # Test JSON parsing
    expected = {'test': 'This is a test', 'is': ['a', 'test']}
    result = from_yaml('{"test": "This is a test", "is": ["a", "test"]}')
    assert expected == result
    assert type(result) is dict
    assert type(result['is']) is list

    # Test YAML parsing
    expected = {'test': 'This is a test', 'is': ['a', 'test']}
    result = from_yaml('test: This is a test\nis:\n  - a\n  - test')
    assert expected == result
    assert type(result) is dict
    assert type(result['is']) is list

    # Test JSON parsing failure

# Generated at 2022-06-13 07:25:57.889305
# Unit test for function from_yaml
def test_from_yaml():
    # Need to add test
    assert True == True

# Generated at 2022-06-13 07:26:05.857392
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("not yaml") == "not yaml"
    assert from_yaml("{\"not yaml\": true}") == {"not yaml": True}
    assert from_yaml("not: yaml") == {"not": "yaml"}
    assert from_yaml("[1, 2, 3]") == [1, 2, 3]
    assert from_yaml("[1, 2, 3]", json_only=True) == "[1, 2, 3]"



# Generated at 2022-06-13 07:26:25.715696
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping

    input_dict = dict(name='Kubernetes Cluster', status='Ready', icon='imgKubernetes.png')
    input_yaml = '''\
    name: Kubernetes Cluster
    status: Ready
    icon: imgKubernetes.png'''

    output_dict = dict(name='Kubernetes Cluster', status='Ready', icon='imgKubernetes.png')
    output_yaml = '''\
    name: Kubernetes Cluster
    status: Ready
    icon: imgKubernetes.png'''


# Generated at 2022-06-13 07:26:30.906533
# Unit test for function from_yaml
def test_from_yaml():
    # valid yaml
    data = from_yaml(u'---\n{"hello": "world"}')

    assert data == {u'hello': u'world'}

    try:
        # invalid yaml
        from_yaml(u'{hello: world}')
        assert False  # should not get here
    except AnsibleParserError as e:
        assert isinstance(e.orig_exc, YAMLError)

# Generated at 2022-06-13 07:26:41.590295
# Unit test for function from_yaml
def test_from_yaml():
    tst_data = '''
    roles:
      - { role: apache, other_variable: blah, some_weird_variable: "some_value" }
      - { role: php, x: { "3": 4 } }
      - role: foo
      - role: bar
    '''

    data = from_yaml(tst_data)
    assert data is not None
    assert list == type(data.get('roles'))
    assert dict == type(data.get('roles')[0])
    assert 'apache' == data.get('roles')[0].get('role')
    assert 'some_value' == data.get('roles')[0].get('some_weird_variable')
    assert 4 == data.get('roles')[1].get('x').get('3')


# Generated at 2022-06-13 07:26:49.180905
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    foo: 1
    bar: 2
    '''

    # Test when data is a string
    data_string = from_yaml(data)
    assert isinstance(data_string, dict)
    assert data_string == {'bar': 2, 'foo': 1}

    # Test when data is not a string
    data_not_string = from_yaml(data, '<string>', False)
    assert isinstance(data_not_string, dict)
    assert data_not_string == {'bar': 2, 'foo': 1}

# Generated at 2022-06-13 07:26:52.603933
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('this is not valid yaml') == 'this is not valid yaml'

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:26:57.811204
# Unit test for function from_yaml
def test_from_yaml():
    data = '{\n  "linux": {\n     "gid": "9"\n   }\n}'
    json_result = {u'linux': {u'gid': u'9'}}
    assert(from_yaml(data) == json_result)

# Generated at 2022-06-13 07:27:09.724507
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'key': 'value'}") == {'key': 'value'}
    success = False
    try:
        from_yaml("key: value")
    except AnsibleParserError:
        success = True
    assert success
    assert from_yaml("{'key': 'value'}", json_only=True) == {'key': 'value'}
    success = False
    try:
        from_yaml("{'key': 'value'}", json_only=True)
    except AnsibleParserError:
        success = True
    assert success

from ansible.module_utils.six import PY3
if PY3:
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-13 07:27:18.000604
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('- foo\n- bar') == ["foo", "bar"]
    assert from_yaml('{a: 1, b: 2, c: 3}') == {'a': 1, 'b': 2, 'c': 3}
    assert from_yaml('foo: bar') == {'foo': 'bar'}
    assert from_yaml('foo: [1, 2, 3]') == {'foo': [1, 2, 3]}

    assert from_yaml('- foo\n- bar', file_name='foo.yml') == ["foo", "bar"]
    assert from_yaml('{a: 1, b: 2, c: 3}', file_name='foo.yml') == {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-13 07:27:19.678713
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{"mon": "sunday"}'))
    print(from_yaml('mon: sunday'))


# Generated at 2022-06-13 07:27:21.202414
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a": "b"}') == {"a": "b"}